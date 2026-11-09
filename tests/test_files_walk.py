"""Which endpoints FilesExt transfers files through, and what a caller sees when they fail.

With experimental_files_ext_enable_endpoints_api, the endpoint list comes from GET /api/2.0/fs/endpoints. Otherwise,
or when the workspace does not answer with a usable list, it is the built-in order.

FakeFilesServer stands in for the hosts a transfer can reach: the workspace (the Files API and the presigned URL
coordination API), the data-plane storage proxy, a Files API 3.0 host (RIG), and cloud storage behind presigned URLs.
It records every operation per endpoint.

The scenario matrix runs every combination of endpoint configuration, endpoint availability and transfer input,
and checks only what a caller sees: the file stored or downloaded, or the error raised. The outcome each scenario
must have comes from the rules in expected_upload and expected_download.
"""

import collections
import io
import itertools
import json
import os
import platform
from dataclasses import dataclass
from tempfile import TemporaryDirectory
from threading import Lock, Thread
from typing import Callable, Dict, List, Optional, Tuple, Union
from urllib.parse import parse_qs, urlparse

import pytest
import requests
import requests_mock
from urllib3.exceptions import ProtocolError

from databricks.sdk import WorkspaceClient
from databricks.sdk.core import Config
from databricks.sdk.errors.platform import AlreadyExists, InternalError, PermissionDenied
from databricks.sdk.mixins import files as files_mixin

from .test_files_utils import NonSeekableBuffer

WORKSPACE = "localhost"
STORAGE_PROXY = "storage-proxy.databricks.com"
RIG = "rig.example.com"
CLOUD = "cloud.example.com"
FILE_PATH = "/Volumes/catalog/schema/volume/file.bin"
LAST_MODIFIED = "Thu, 28 Nov 2024 16:39:14 GMT"
PART_SIZE = 1024

DP_ENTRY = {
    "api": "FILES_API",
    "api_version": "2.0",
    "scheme": "http",
    "hostname": STORAGE_PROXY,
    "multipart_upload_supported": True,
}
RIG_ENTRY = {
    "api": "FILES_API",
    "api_version": "3.0",
    "scheme": "https",
    "hostname": RIG,
    "multipart_upload_supported": True,
}
OFFLOAD_ENTRY = {"api": "IO_OFFLOAD", "scheme": "http", "hostname": WORKSPACE, "multipart_upload_supported": True}
FLOOR_ENTRY = {
    "api": "FILES_API",
    "api_version": "2.0",
    "scheme": "http",
    "hostname": WORKSPACE,
    "multipart_upload_supported": False,
}
# What a data-plane caller gets: storage proxy, then presigned URLs, then the single-shot floor.
DATA_PLANE = [DP_ENTRY, OFFLOAD_ENTRY, FLOOR_ENTRY]
# What a caller that can reach RIG gets: Files API 3.0 there, then presigned URLs, then the single-shot floor.
RIG_PLAN = [RIG_ENTRY, OFFLOAD_ENTRY, FLOOR_ENTRY]

_ERROR_CODES = {
    400: "INVALID_PARAMETER_VALUE",
    403: "PERMISSION_DENIED",
    404: "NOT_FOUND",
    409: "ALREADY_EXISTS",
    500: "INTERNAL_ERROR",
}

# Operations on presigned cloud URLs. They must never carry workspace credentials.
_PRESIGNED_OPS = {"offload.part", "offload.get"}

# Requests that pick the endpoint list or read file metadata rather than transfer data.
_NOT_ENDPOINTS = {"endpoints", "scim", "probe", "workspace"}


class BreakAfter:
    """A download fault: the connection drops after `n` bytes of the body."""

    def __init__(self, n: int):
        self.n = n


class _BreakingBody(io.BytesIO):
    """Serves the first `break_at` bytes, then fails every further read like a dropped connection.

    Covers every read method, since urllib3 may read through any of them.
    """

    def __init__(self, data: bytes, break_at: int):
        super().__init__(data)
        self._break_at = break_at

    def _limit(self, size: Optional[int]) -> int:
        position = self.tell()
        if position >= self._break_at:
            raise ProtocolError("Connection broken: simulated")
        remaining = self._break_at - position
        return remaining if size is None or size < 0 else min(size, remaining)

    def read(self, size: Optional[int] = -1) -> bytes:
        return super().read(self._limit(size))

    def read1(self, size: Optional[int] = -1) -> bytes:
        return super().read1(self._limit(size))

    def readinto(self, buffer) -> int:
        return super().readinto(memoryview(buffer)[: self._limit(len(buffer))])

    def readinto1(self, buffer) -> int:
        return super().readinto1(memoryview(buffer)[: self._limit(len(buffer))])


Fault = Union[int, type, BreakAfter]


def always(fault: Fault) -> Callable[[int], Optional[Fault]]:
    return lambda call: fault


def on_calls(fault: Fault, *calls: int) -> Callable[[int], Optional[Fault]]:
    return lambda call: fault if call in calls else None


class FakeFilesServer:
    def __init__(
        self, faults: Optional[Dict[str, Callable[[int], Optional[Fault]]]] = None, plan: Optional[List[dict]] = None
    ):
        # The list GET /api/2.0/fs/endpoints answers with; None means the workspace does not serve it.
        self.plan = plan
        self.faults = faults or {}
        self.download_content = b""
        self.calls: List[str] = []
        self.counts = collections.Counter()
        self.parts: Dict[str, Dict[int, bytes]] = collections.defaultdict(dict)
        self.stored: Dict[str, bytes] = {}
        self.aborted = set()
        self.ranges: Dict[str, List[Optional[str]]] = collections.defaultdict(list)
        self.credentials: Dict[str, List[bool]] = collections.defaultdict(list)
        self.request_headers: Dict[str, List[Dict[str, str]]] = collections.defaultdict(list)
        self.urls: Dict[str, List[str]] = collections.defaultdict(list)
        # Protocol checks that failed; a client that catches its request errors would otherwise hide them.
        self.violations: List[str] = []
        self._lock = Lock()

    def ops(self, prefix: str) -> List[str]:
        return [op for op in self.calls if op.startswith(prefix)]

    def endpoints_touched(self) -> List[str]:
        """Endpoints in the order they were first used, ignoring the probe and metadata requests."""
        seen = []
        for op in self.calls:
            endpoint = op.split(".")[0]
            if endpoint not in _NOT_ENDPOINTS and endpoint not in seen:
                seen.append(endpoint)
        return seen

    def stored_file(self) -> Optional[bytes]:
        """The file as a caller would read it back, whichever endpoint stored it."""
        assert len(self.stored) <= 1, f"the file was stored by more than one endpoint: {sorted(self.stored)}"
        return next(iter(self.stored.values()), None)

    def assert_credentials(self) -> None:
        for op, sent in self.credentials.items():
            if op in _PRESIGNED_OPS:
                assert not any(sent), f"workspace credentials were sent to a presigned URL ({op})"
            else:
                assert all(sent), f"workspace credentials were missing on {op}"

    def _operation(self, request: requests.Request) -> str:
        url = urlparse(request.url)
        query = parse_qs(url.query)
        host, method, path = url.hostname, request.method, url.path
        if host == WORKSPACE and path == "/api/2.0/fs/endpoints" and method == "GET":
            return "endpoints"
        if host == WORKSPACE and path == "/api/2.0/preview/scim/v2/Me" and method == "GET":
            return "scim"
        if host == STORAGE_PROXY and path == "/api/2.0/fs/files/DatabricksInternal/Probe/fullstack/wis":
            return "probe"
        if path == f"/api/3.0/fs/files{FILE_PATH}":
            assert host == RIG, f"Files API 3.0 request to {host}"
            assert not {"upload_type", "session_token"} & query.keys(), f"2.0 parameters on {request.url}"
            action = query.get("action", [None])[0]
            if method == "POST" and action in ("initiate-upload", "complete-upload", "abort-upload"):
                return f"rig.{action.split('-')[0]}"
            if method == "PUT" and "part_number" in query:
                return "rig.part"
            if method == "PUT":
                return "rig.single"
            if method == "GET":
                return "rig.get"
        if path == f"/api/2.0/fs/files{FILE_PATH}":
            assert host in (WORKSPACE, STORAGE_PROXY), f"Files API 2.0 request to {host}"
            endpoint = "dp" if host == STORAGE_PROXY else None
            action = query.get("action", [None])[0]
            if method == "POST" and action == "initiate-upload":
                return f"{endpoint or 'offload'}.initiate"
            if method == "POST" and action == "complete-upload":
                return f"{endpoint or 'offload'}.complete"
            if method == "POST" and action == "abort-upload":
                assert query.get("upload_type") == ["multipart"], f"abort-upload without upload_type: {request.url}"
                return f"{endpoint or 'offload'}.abort"
            if method == "PUT" and query.get("upload_type") == ["multipart"]:
                return f"{endpoint}.part"
            if method == "PUT":
                return f"{endpoint or 'floor'}.single"
            if method == "GET":
                return f"{endpoint or 'floor'}.get"
            if method == "HEAD" and host == WORKSPACE:
                return "workspace.head"
        if host == WORKSPACE and path == "/api/2.0/fs/create-upload-part-urls":
            return "offload.part-urls"
        if host == WORKSPACE and path == "/api/2.0/fs/create-download-url":
            return "offload.download-url"
        if host == CLOUD and path.startswith("/part/") and method == "PUT":
            return "offload.part"
        if host == CLOUD and path == "/download" and method == "GET":
            return "offload.get"
        raise AssertionError(f"Unexpected request {method} {request.url}")

    def handle(self, request: requests.Request) -> requests.Response:
        op = self._operation(request)
        with self._lock:
            self.calls.append(op)
            self.counts[op] += 1
            call = self.counts[op]
            self.credentials[op].append(request.headers.get("Authorization") is not None)
            self.request_headers[op].append(dict(request.headers))
            self.urls[op].append(request.url)
        fault = self.faults.get(op, lambda _: None)(call)
        if isinstance(fault, type):
            raise fault("simulated network failure")
        if isinstance(fault, int):
            body = {"error_code": _ERROR_CODES.get(fault, "UNKNOWN"), "message": f"simulated {fault} on {op}"}
            return requests_mock.create_response(request, status_code=fault, json=body)
        return self._respond(op, request, fault)

    def _respond(self, op: str, request: requests.Request, fault: Optional[Fault]) -> requests.Response:
        if op == "endpoints":
            if self.plan is None:
                body = {"error_code": "NOT_FOUND", "message": "no endpoints API"}
                return requests_mock.create_response(request, status_code=404, json=body)
            return requests_mock.create_response(request, json={"endpoints": self.plan})
        if op == "scim":
            return requests_mock.create_response(request, json={}, headers={"X-Databricks-Org-Id": "12345"})
        if op == "probe":
            return requests_mock.create_response(request)
        endpoint, action = op.split(".", 1)
        url = urlparse(request.url)
        query = parse_qs(url.query)
        if endpoint == "rig" and action in ("part", "complete", "abort"):
            assert query.get("upload_id") == ["upload-rig"], f"{op} without the upload_id from initiate-upload"
        if endpoint == "rig" and action in ("part", "single"):
            assert request.headers.get("Content-Length") is not None, f"Files API 3.0 requires a Content-Length on {op}"
        if op == "rig.initiate":
            return requests_mock.create_response(request, json={"upload_id": "upload-rig"})
        if action == "initiate":
            return requests_mock.create_response(
                request, json={"multipart_upload": {"session_token": f"token-{endpoint}"}}
            )
        if op == "offload.part-urls":
            body = json.loads(request.body)
            assert body["session_token"] == "token-offload"
            start, count = body["start_part_number"], body["count"]
            urls = [
                {"part_number": n, "url": f"https://{CLOUD}/part/{n}", "headers": []}
                for n in range(start, start + count)
            ]
            return requests_mock.create_response(request, json={"upload_part_urls": urls})
        if action == "part":
            part_number = int(url.path.split("/")[-1]) if endpoint == "offload" else int(query["part_number"][0])
            with self._lock:
                self.parts[endpoint][part_number] = _read_body(request)
            return requests_mock.create_response(request, headers={"ETag": f"etag-{endpoint}-{part_number}"})
        if action == "complete":
            parts = json.loads(request.body)["parts"]
            for part in parts:
                assert part["etag"] == f"etag-{endpoint}-{part['part_number']}"
            numbers = [part["part_number"] for part in parts]
            assert numbers == sorted(self.parts[endpoint]), "complete-upload must list every uploaded part"
            self.stored[endpoint] = b"".join(self.parts[endpoint][n] for n in numbers)
            return requests_mock.create_response(request, json={})
        if action == "abort":
            if endpoint != "rig":
                assert query.get("session_token") == [f"token-{endpoint}"]
            self.aborted.add(endpoint)
            return requests_mock.create_response(request, json={})
        if action == "single":
            self.stored[endpoint] = _read_body(request)
            return requests_mock.create_response(request, json={})
        if op == "offload.download-url":
            return requests_mock.create_response(request, json={"url": f"https://{CLOUD}/download", "headers": []})
        if op == "workspace.head":
            return requests_mock.create_response(
                request,
                headers={
                    "Content-Length": str(len(self.download_content)),
                    "Content-Type": "application/octet-stream",
                    "Last-Modified": LAST_MODIFIED,
                },
            )
        if action == "get":
            return self._download(endpoint, request, fault)
        raise AssertionError(f"No response for {op}")

    def _download(self, endpoint: str, request: requests.Request, fault: Optional[Fault]) -> requests.Response:
        range_header = request.headers.get("Range")
        self.ranges[endpoint].append(range_header)
        data, status = self.download_content, 200
        if range_header:
            start_s, end_s = range_header[len("bytes=") :].split("-")
            start = int(start_s)
            end = int(end_s) if end_s else len(data) - 1
            data, status = data[start : end + 1], 206
        headers = {
            "Content-Length": str(len(data)),
            "Content-Type": "application/octet-stream",
            "Last-Modified": LAST_MODIFIED,
        }
        body = _BreakingBody(data, fault.n) if isinstance(fault, BreakAfter) else io.BytesIO(data)
        return requests_mock.create_response(request, status_code=status, headers=headers, body=body)


def _read_body(request: requests.Request) -> bytes:
    body = request.body
    if body is None:
        return b""
    if hasattr(body, "read"):
        return body.read()
    return body.encode() if isinstance(body, str) else bytes(body)


def _client(config: Config, storage_proxy: bool = False, endpoints_api: Optional[bool] = False) -> WorkspaceClient:
    """endpoints_api=None keeps the flag's default."""
    config = config.copy()
    config.experimental_files_ext_enable_storage_proxy = storage_proxy
    if endpoints_api is not None:
        config.experimental_files_ext_enable_endpoints_api = endpoints_api
    config._header_factory = lambda: {"Authorization": "Bearer workspace-token"}
    config.files_ext_multipart_upload_min_stream_size = PART_SIZE
    config.files_ext_parallel_download_min_file_size = PART_SIZE
    config.files_ext_parallel_download_default_part_size = PART_SIZE
    config.files_ext_client_download_streaming_chunk_size = 512
    return WorkspaceClient(config=config)


SOURCES = ["file", "seekable", "non-seekable"]


def _upload(
    w: WorkspaceClient, source: str, data: bytes, use_parallel: bool, tmp_path, overwrite: Optional[bool] = None
) -> None:
    if source == "file":
        local = tmp_path / "source.bin"
        local.write_bytes(data)
        w.files.upload_from(FILE_PATH, str(local), overwrite=overwrite, part_size=PART_SIZE, use_parallel=use_parallel)
        return
    stream = io.BytesIO(data) if source == "seekable" else NonSeekableBuffer(data)
    w.files.upload(FILE_PATH, stream, overwrite=overwrite, part_size=PART_SIZE, use_parallel=use_parallel)


def _run(server: FakeFilesServer, fn: Callable[[], object]) -> object:
    def handle(request: requests.Request) -> requests.Response:
        try:
            return server.handle(request)
        except AssertionError as e:
            server.violations.append(str(e))
            return requests_mock.create_response(request, status_code=400, json={"message": str(e)})

    try:
        with requests_mock.Mocker() as mock:
            mock.add_matcher(handle)
            return fn()
    finally:
        assert not server.violations, server.violations


LARGE = os.urandom(4 * PART_SIZE + 100)
SMALL = os.urandom(100)


# ======================== Scenario matrix (black box) ========================
#
# Every combination of the endpoint configuration, which of its endpoints are up, and the transfer input, checked
# only on what the caller sees: the file stored or downloaded, or the error raised. The outcome a scenario must have
# comes from the rules in expected_upload and expected_download, not from the client.


@dataclass(frozen=True)
class EndpointList:
    name: str
    # The endpoints a transfer can use, best first.
    endpoints: Tuple[str, ...]
    storage_proxy: bool = False
    # Served by GET /api/2.0/fs/endpoints; None leaves the client on its built-in order.
    plan: Optional[List[dict]] = None


ENDPOINT_LISTS = [
    EndpointList("built-in", ("presigned", "workspace")),
    # The storage-proxy flag is deprecated and has no effect.
    EndpointList("built-in with the storage-proxy flag", ("presigned", "workspace"), storage_proxy=True),
    EndpointList("server: proxy, presigned, workspace", ("proxy", "presigned", "workspace"), plan=DATA_PLANE),
    EndpointList("server: rig, presigned, workspace", ("rig", "presigned", "workspace"), plan=RIG_PLAN),
    EndpointList("server: presigned only", ("presigned",), plan=[OFFLOAD_ENTRY]),
]

# up: the endpoint works. down: every request to it fails, as when it can't be reached. rejects data: its probe and
# sessions answer, but every transfer fails. breaks mid-transfer: it takes the first part or sends the first bytes,
# then fails.
UP, DOWN, REJECTS, BREAKS = "up", "down", "rejects data", "breaks mid-transfer"

_DATA = {"empty": b"", "small": SMALL, "one part": os.urandom(PART_SIZE), "several parts": LARGE}
SIZES = {size: len(data) for size, data in _DATA.items()}
UPLOAD_MODES = ["sequential", "parallel"]
DOWNLOAD_MODES = ["stream", "to-file", "parallel"]

# What fails while an endpoint is down. For the workspace that is its Files API transfers: it still serves file
# metadata, opens presigned URL sessions and issues their URLs.
_DOWN_OPS = {
    "proxy": ["probe", "dp.initiate", "dp.part", "dp.complete", "dp.abort", "dp.single", "dp.get"],
    "presigned": ["offload.part", "offload.get"],
    "workspace": ["floor.single", "floor.get"],
    "rig": ["rig.initiate", "rig.part", "rig.complete", "rig.abort", "rig.single", "rig.get"],
}
# The fake's name for each endpoint that can come first in a list.
_FAKE_NAMES = {"proxy": "dp", "presigned": "offload", "rig": "rig"}

SUCCEEDS = "succeeds"


@dataclass(frozen=True)
class Scenario:
    transfer: str
    endpoint_list: EndpointList
    availability: Tuple[Tuple[str, str], ...]
    size: str
    mode: str
    source: Optional[str] = None

    def __str__(self) -> str:
        transfer_input = ", ".join(x for x in (self.size, self.source, self.mode) if x)
        states = ", ".join(f"{endpoint} {state}" for endpoint, state in self.availability)
        return f"{transfer_input} | {self.endpoint_list.name} | {states}"

    def faults(self) -> Dict[str, Callable[[int], Optional[Fault]]]:
        faults = {}
        for endpoint, state in self.availability:
            if state == DOWN:
                faults.update({op: always(requests.ConnectionError) for op in _DOWN_OPS[endpoint]})
            elif state == REJECTS:
                faults.update({f"{_FAKE_NAMES[endpoint]}.{op}": always(403) for op in ("part", "single", "get")})
            elif state == BREAKS and self.transfer == "upload":
                # The first part lands, every later one fails.
                faults[f"{_FAKE_NAMES[endpoint]}.part"] = lambda call: requests.ConnectionError if call > 1 else None
            elif state == BREAKS and self.mode == "parallel":
                # The first range lands, every later one fails.
                faults[f"{_FAKE_NAMES[endpoint]}.get"] = lambda call: requests.ConnectionError if call > 1 else None
            elif state == BREAKS:
                # The response is cut off after some bytes reached the caller, and the endpoint is down after that.
                faults[f"{_FAKE_NAMES[endpoint]}.get"] = lambda call: (
                    BreakAfter(3 * 512) if call == 1 else requests.ConnectionError
                )
        return faults


def _availabilities(endpoint_list: EndpointList) -> List[Tuple[Tuple[str, str], ...]]:
    # An upload falls back to the workspace when the list has nothing else and a download doesn't, so the workspace is
    # always on the axis.
    axis = endpoint_list.endpoints
    if "workspace" not in axis:
        axis += ("workspace",)
    combinations = [tuple(zip(axis, states)) for states in itertools.product([UP, DOWN], repeat=len(axis))]
    first, rest = axis[0], axis[1:]
    combinations.append(((first, BREAKS),) + tuple((endpoint, UP) for endpoint in rest))
    combinations += [
        ((first, REJECTS),) + tuple(zip(rest, states)) for states in itertools.product([UP, DOWN], repeat=len(rest))
    ]
    return combinations


def _scenarios(transfer: str, modes: List[str], sources: List[Optional[str]]) -> List[Scenario]:
    return [
        Scenario(transfer, endpoint_list, availability, size, mode, source)
        for endpoint_list in ENDPOINT_LISTS
        for availability in _availabilities(endpoint_list)
        for size in SIZES
        for source in sources
        for mode in modes
        # Only a transfer of several parts or chunks has data committed before a later failure.
        if size == "several parts" or BREAKS not in dict(availability).values()
    ]


UPLOAD_SCENARIOS = _scenarios("upload", UPLOAD_MODES, SOURCES)
DOWNLOAD_SCENARIOS = _scenarios("download", DOWNLOAD_MODES, [None])


def _walk_order(scenario: Scenario) -> List[str]:
    """The endpoints a transfer tries, in order. The built-in order is presigned URLs, then the workspace. A list from
    the server is used as it is."""
    endpoints = scenario.endpoint_list.endpoints
    if scenario.endpoint_list.plan is not None:
        # An upload with only presigned URLs listed gets the workspace after them, for small files.
        if "workspace" not in endpoints and scenario.transfer == "upload":
            return list(endpoints) + ["workspace"]
        return list(endpoints)
    return ["presigned", "workspace"]


# Retries that run out raise TimeoutError from the API client's retry budget, which covers the workspace, and
# RuntimeError from the bounded retries of transfers to other hosts.
def expected_upload(scenario: Scenario):
    """The outcome an upload has.

    - Endpoints are tried in order, ending with the workspace, which takes single-shot uploads only.
    - A file under one part is sent in a single shot, which presigned URLs can't take, so they are skipped.
    - A non-seekable stream's size is known only once it is read, so it is read up to one part first: a short one
      is sent in a single shot as above.
    - A failure before any data was committed moves the upload to the next endpoint; after a part has landed, a
      failure raises.
    - A stream of a part or more is replayed as the part read plus the unread rest, which can't be rewound, so the
      API client sends it once.
    """
    states = dict(scenario.availability)
    size = SIZES[scenario.size]
    non_seekable = scenario.source == "non-seekable"
    for endpoint in _walk_order(scenario):
        state = states[endpoint]
        if endpoint == "workspace":
            if state == UP:
                return SUCCEEDS
            return requests.ConnectionError if non_seekable and size >= PART_SIZE else TimeoutError
        if size < PART_SIZE and endpoint == "presigned":
            continue
        if state == UP:
            return SUCCEEDS
        if state == BREAKS:
            return RuntimeError
    raise AssertionError("every walk ends with the workspace")


def expected_download(scenario: Scenario):
    """The outcome a download has.

    - Endpoints are tried in order.
    - A failure before any bytes arrived moves the download to the next endpoint. When no endpoint could serve it,
      the last failure is raised.
    - After bytes arrived, the download stays on that endpoint. A stream resumes there and, if that fails too,
      raises its broken connection; a parallel download raises the failure of a later range.
    """
    states = dict(scenario.availability)
    for endpoint in _walk_order(scenario):
        state = states[endpoint]
        if state == UP:
            return SUCCEEDS
        if state == BREAKS:
            return RuntimeError if scenario.mode == "parallel" else requests.exceptions.ChunkedEncodingError
    if endpoint == "workspace":
        return TimeoutError
    # The last endpoint retries a dropped connection until its budget runs out, but not a rejected transfer.
    return PermissionDenied if state == REJECTS else RuntimeError


def _scenario_client(config: Config, scenario: Scenario) -> WorkspaceClient:
    endpoint_list = scenario.endpoint_list
    return _client(config, storage_proxy=endpoint_list.storage_proxy, endpoints_api=endpoint_list.plan is not None)


@pytest.mark.parametrize("scenario", UPLOAD_SCENARIOS, ids=str)
def test_upload_scenario(config, tmp_path, scenario):
    server = FakeFilesServer(scenario.faults(), scenario.endpoint_list.plan)
    w = _scenario_client(config, scenario)
    data = _DATA[scenario.size]
    expected = expected_upload(scenario)

    def upload():
        _upload(w, scenario.source, data, scenario.mode == "parallel", tmp_path)

    if expected == SUCCEEDS:
        _run(server, upload)
        assert server.stored_file() == data
    else:
        with pytest.raises(expected):
            _run(server, upload)
        assert server.stored_file() is None
    server.assert_credentials()
    assert "probe" not in server.calls and "scim" not in server.calls


def _download(w: WorkspaceClient) -> bytes:
    return w.files.download(FILE_PATH).contents.read()


def _skip_parallel_on_windows(use_parallel: bool) -> None:
    if use_parallel and platform.system() == "Windows":
        # FilesExt downloads sequentially on Windows, so the parallel rules don't apply there.
        pytest.skip("Skipping parallel download tests on Windows")


def _download_to(w: WorkspaceClient, use_parallel: bool, parallelism: Optional[int] = None) -> bytes:
    _skip_parallel_on_windows(use_parallel)
    # A new file, the usual destination.
    with TemporaryDirectory() as directory:
        destination = os.path.join(directory, "downloaded.bin")
        w.files.download_to(FILE_PATH, destination, use_parallel=use_parallel, parallelism=parallelism)
        with open(destination, "rb") as f:
            return f.read()


@pytest.mark.parametrize("scenario", DOWNLOAD_SCENARIOS, ids=str)
def test_download_scenario(config, scenario):
    server = FakeFilesServer(scenario.faults(), scenario.endpoint_list.plan)
    server.download_content = _DATA[scenario.size]
    w = _scenario_client(config, scenario)
    download = {
        "stream": lambda: _download(w),
        "to-file": lambda: _download_to(w, use_parallel=False),
        "parallel": lambda: _download_to(w, use_parallel=True),
    }[scenario.mode]
    expected = expected_download(scenario)

    if expected == SUCCEEDS:
        assert _run(server, download) == server.download_content
    else:
        with pytest.raises(expected):
            _run(server, download)
    server.assert_credentials()
    assert "probe" not in server.calls and "scim" not in server.calls


# ======================== Uploads before commit ========================


def test_upload_retries_a_transient_failure_once_before_moving_to_the_workspace(config, tmp_path):
    # The workspace takes single-shot uploads only, so one dropped connection must not send a large file there.
    server = FakeFilesServer({"offload.initiate": lambda call: requests.ConnectionError if call == 1 else None})
    w = _client(config, storage_proxy=False)

    _run(server, lambda: _upload(w, "file", LARGE, False, tmp_path))

    assert server.stored_file() == LARGE
    assert server.counts["offload.initiate"] == 2
    assert "floor.single" not in server.calls


def test_upload_over_the_workspace_limit_stays_on_presigned_urls(config, tmp_path, monkeypatch):
    monkeypatch.setattr(files_mixin, "_WORKSPACE_MAX_SINGLE_SHOT_SIZE", len(LARGE) - 1)
    server = FakeFilesServer({"offload.initiate": always(503)})
    w = _client(config, storage_proxy=False)

    # Presigned URLs are the only endpoint left, so their own failure is raised, not a too-large single shot.
    with pytest.raises(TimeoutError):
        _run(server, lambda: _upload(w, "file", LARGE, False, tmp_path))
    assert "floor.single" not in server.calls


def test_upload_over_the_workspace_limit_without_multipart_endpoints_fails_before_sending(
    config, tmp_path, monkeypatch
):
    monkeypatch.setattr(files_mixin, "_WORKSPACE_MAX_SINGLE_SHOT_SIZE", len(LARGE) - 1)
    server = FakeFilesServer()
    w = _client(config, storage_proxy=False)
    workspace_only = [e for e in w.files._default_endpoints() if not e.multipart_upload_supported]
    monkeypatch.setattr(w.files, "_upload_endpoints", lambda: workspace_only)

    with pytest.raises(ValueError, match="at most 5 GiB"):
        _run(server, lambda: _upload(w, "file", LARGE, False, tmp_path))
    assert server.calls == []


# ======================== download_to onto an existing destination ========================


def _symlink_or_skip(target, link) -> None:
    try:
        os.symlink(target, link)
    except (OSError, NotImplementedError) as e:
        # Windows needs Developer Mode or admin rights to create symlinks.
        pytest.skip(f"Cannot create symlinks here: {e}")


def _download_onto(config: Config, destination, use_parallel: bool, server: Optional[FakeFilesServer] = None):
    _skip_parallel_on_windows(use_parallel)
    server = server or FakeFilesServer()
    server.download_content = LARGE
    w = _client(config, storage_proxy=False)
    _run(server, lambda: w.files.download_to(FILE_PATH, str(destination), use_parallel=use_parallel))
    return server


@pytest.mark.parametrize("use_parallel", [False, True], ids=["sequential", "parallel"])
def test_download_to_an_existing_file_writes_it_in_place(config, tmp_path, use_parallel):
    destination = tmp_path / "out.bin"
    destination.write_bytes(b"old content")
    link = tmp_path / "link.bin"
    os.link(destination, link)
    if platform.system() != "Windows":
        os.chmod(destination, 0o600)

    _download_onto(config, destination, use_parallel)

    assert destination.read_bytes() == LARGE
    # The same file was written: another link to it sees the new content, and nothing else is left behind.
    assert link.read_bytes() == LARGE
    assert sorted(p.name for p in tmp_path.iterdir()) == ["link.bin", "out.bin"]
    if platform.system() != "Windows":
        assert os.stat(destination).st_mode & 0o777 == 0o600


@pytest.mark.parametrize("use_parallel", [False, True], ids=["sequential", "parallel"])
def test_download_to_a_symlink_writes_through_it(config, tmp_path, use_parallel):
    target = tmp_path / "target.bin"
    target.write_bytes(b"old content")
    link = tmp_path / "link.bin"
    _symlink_or_skip(target, link)

    _download_onto(config, link, use_parallel)

    assert link.is_symlink()
    assert target.read_bytes() == LARGE


def test_download_to_a_broken_symlink_creates_its_target(config, tmp_path):
    target = tmp_path / "target.bin"
    link = tmp_path / "link.bin"
    _symlink_or_skip(target, link)

    _download_onto(config, link, use_parallel=False)

    assert link.is_symlink()
    assert target.read_bytes() == LARGE


@pytest.mark.skipif(not hasattr(os, "mkfifo"), reason="needs named pipes")
def test_download_to_a_pipe_is_sequential(config, tmp_path):
    pipe = tmp_path / "pipe"
    os.mkfifo(pipe)
    received = []
    reader = Thread(target=lambda: received.append(open(pipe, "rb").read()), daemon=True)
    reader.start()

    server = _download_onto(config, pipe, use_parallel=True)
    reader.join(10)

    assert received == [LARGE]
    assert all(r is None for ranges in server.ranges.values() for r in ranges), dict(server.ranges)


def test_download_to_an_existing_file_that_fails_before_any_data_leaves_it_as_it_was(config, tmp_path):
    destination = tmp_path / "out.bin"
    destination.write_bytes(b"old content")
    server = FakeFilesServer({"offload.get": always(403), "floor.get": always(403)})

    with pytest.raises(Exception):
        _download_onto(config, destination, use_parallel=False, server=server)

    assert destination.read_bytes() == b"old content"
    assert sorted(p.name for p in tmp_path.iterdir()) == ["out.bin"]


@pytest.mark.parametrize("storage_proxy", [False, True], ids=["workspace", "storage proxy"])
@pytest.mark.parametrize("source", SOURCES)
def test_an_empty_upload_is_sent_with_a_content_length(config, tmp_path, source, storage_proxy):
    server = FakeFilesServer()
    w = _client(config, storage_proxy=storage_proxy)

    _run(server, lambda: _upload(w, source, b"", False, tmp_path))

    singles = [op for op in server.calls if op.endswith(".single")]
    assert singles, server.calls
    for op in singles:
        for headers in server.request_headers[op]:
            assert headers.get("Content-Length") == "0", (op, headers)
            assert "Transfer-Encoding" not in headers, (op, headers)
    assert server.stored_file() == b""


@pytest.mark.parametrize("source", ["file", "seekable"])
def test_storage_proxy_single_shot_onto_an_existing_file_is_already_exists(config, tmp_path, source):
    server = FakeFilesServer({"dp.single": always(412)}, DATA_PLANE)
    config = config.copy()
    config.workspace_id = "1234"
    w = _client(config, endpoints_api=True)

    with pytest.raises(AlreadyExists):
        _run(server, lambda: _upload(w, source, SMALL, False, tmp_path, overwrite=False))

    # The conflict is the caller's, so the upload does not move on to the workspace.
    assert "floor.single" not in server.calls
    assert server.request_headers["dp.single"][0]["X-Databricks-Workspace-Id"] == "1234"


# ======================== Files API 3.0 (white box) ========================


def _download_server(faults=None, plan=None) -> FakeFilesServer:
    server = FakeFilesServer(faults, plan)
    server.download_content = LARGE
    return server


@pytest.mark.parametrize("use_parallel", [False, True], ids=["sequential", "parallel"])
@pytest.mark.parametrize("source", SOURCES)
def test_rig_upload_uses_the_files_api_3_protocol(config, tmp_path, source, use_parallel):
    server = FakeFilesServer(plan=RIG_PLAN)
    w = _client(config, endpoints_api=True)

    _run(server, lambda: _upload(w, source, LARGE, use_parallel, tmp_path))

    assert server.endpoints_touched() == ["rig"]
    assert server.ops("rig") == ["rig.initiate"] + ["rig.part"] * 5 + ["rig.complete"]
    assert server.stored == {"rig": LARGE}
    server.assert_credentials()


@pytest.mark.parametrize("source", ["file", "seekable"])
def test_rig_small_upload_uses_single_shot(config, tmp_path, source):
    server = FakeFilesServer(plan=RIG_PLAN)
    w = _client(config, endpoints_api=True)

    _run(server, lambda: _upload(w, source, SMALL, False, tmp_path))

    assert server.calls == ["endpoints", "rig.single"]
    assert server.stored == {"rig": SMALL}
    server.assert_credentials()


@pytest.mark.parametrize("use_parallel", [False, True], ids=["sequential", "parallel"])
@pytest.mark.parametrize("source", SOURCES)
def test_rig_first_part_failure_aborts_on_rig_and_moves_to_presigned(config, tmp_path, source, use_parallel):
    server = FakeFilesServer({"rig.part": always(403)}, RIG_PLAN)
    w = _client(config, endpoints_api=True)

    _run(server, lambda: _upload(w, source, LARGE, use_parallel, tmp_path))

    assert server.endpoints_touched() == ["rig", "offload"]
    assert server.counts["rig.part"] == 1
    assert server.aborted == {"rig"}
    assert server.stored == {"offload": LARGE}
    server.assert_credentials()


@pytest.mark.parametrize("use_parallel", [False, True], ids=["sequential", "parallel"])
@pytest.mark.parametrize("source", SOURCES)
def test_rig_later_part_failure_raises_without_walking(config, tmp_path, source, use_parallel):
    server = FakeFilesServer({"rig.part": on_calls(500, 2)}, RIG_PLAN)
    w = _client(config, endpoints_api=True)

    with pytest.raises(InternalError):
        _run(server, lambda: _upload(w, source, LARGE, use_parallel, tmp_path))

    assert server.endpoints_touched() == ["rig"]
    assert server.aborted == {"rig"}
    assert server.stored == {}


@pytest.mark.parametrize("source", ["file", "seekable"])
def test_rig_single_shot_onto_an_existing_file_is_already_exists(config, tmp_path, source):
    server = FakeFilesServer({"rig.single": always(409)}, RIG_PLAN)
    w = _client(config, endpoints_api=True)

    with pytest.raises(AlreadyExists):
        _run(server, lambda: _upload(w, source, SMALL, False, tmp_path, overwrite=False))

    assert server.endpoints_touched() == ["rig"]
    assert parse_qs(urlparse(server.urls["rig.single"][0]).query) == {"overwrite": ["false"]}


@pytest.mark.parametrize("use_parallel", [False, True], ids=["sequential", "parallel"])
@pytest.mark.parametrize("source", SOURCES)
def test_rig_complete_onto_an_existing_file_is_already_exists(config, tmp_path, source, use_parallel):
    server = FakeFilesServer({"rig.complete": always(409)}, RIG_PLAN)
    w = _client(config, endpoints_api=True)

    with pytest.raises(AlreadyExists):
        _run(server, lambda: _upload(w, source, LARGE, use_parallel, tmp_path, overwrite=False))

    # The parts landed, so the upload stays on RIG and aborts there.
    assert server.endpoints_touched() == ["rig"]
    assert server.aborted == {"rig"}


def test_rig_initiate_failure_moves_to_presigned(config, tmp_path):
    server = FakeFilesServer({"rig.initiate": always(500)}, RIG_PLAN)
    w = _client(config, endpoints_api=True)

    _run(server, lambda: _upload(w, "file", LARGE, False, tmp_path))

    assert server.endpoints_touched() == ["rig", "offload"]
    assert server.stored == {"offload": LARGE}


def test_rig_parts_are_capped_at_the_files_api_3_part_size_limit(config, tmp_path, monkeypatch):
    monkeypatch.setattr(files_mixin, "_FILES_API_V3_MAX_PART_SIZE", PART_SIZE)
    server = FakeFilesServer(plan=RIG_PLAN)
    w = _client(config, endpoints_api=True)
    local = tmp_path / "source.bin"
    local.write_bytes(LARGE)

    _run(server, lambda: w.files.upload_from(FILE_PATH, str(local), part_size=2 * PART_SIZE, use_parallel=False))

    assert server.stored == {"rig": LARGE}
    assert max(len(part) for part in server.parts["rig"].values()) == PART_SIZE


@pytest.mark.parametrize("download", ["stream", "to-file"])
def test_rig_download(config, download):
    server = _download_server(plan=RIG_PLAN)
    w = _client(config, endpoints_api=True)
    result = {}

    _run(server, lambda: result.update(data=_download(w) if download == "stream" else _download_to(w, False)))

    assert result["data"] == LARGE
    assert server.endpoints_touched() == ["rig"]
    server.assert_credentials()


def test_rig_parallel_download_uses_rig_for_every_range(config):
    server = _download_server(plan=RIG_PLAN)
    w = _client(config, endpoints_api=True)
    result = {}

    _run(server, lambda: result.update(data=_download_to(w, True, parallelism=2)))

    assert result["data"] == LARGE
    assert server.endpoints_touched() == ["rig"]
    assert len(server.ranges["rig"]) == 5
    server.assert_credentials()


@pytest.mark.parametrize("download", ["stream", "to-file", "parallel"])
def test_rig_download_failure_before_any_bytes_moves_to_presigned(config, download):
    server = _download_server({"rig.get": always(500)}, RIG_PLAN)
    w = _client(config, endpoints_api=True)
    result = {}

    def run():
        if download == "stream":
            result.update(data=_download(w))
        else:
            result.update(data=_download_to(w, download == "parallel", parallelism=2))

    _run(server, run)

    assert result["data"] == LARGE
    assert server.endpoints_touched() == ["rig", "offload"]
    server.assert_credentials()


def test_rig_download_reopens_on_rig_after_a_dropped_connection(config):
    server = _download_server({"rig.get": on_calls(BreakAfter(3 * 512), 1)}, RIG_PLAN)
    w = _client(config, endpoints_api=True)
    result = {}

    _run(server, lambda: result.update(data=_download(w)))

    assert result["data"] == LARGE
    assert server.endpoints_touched() == ["rig"]
    assert server.counts["rig.get"] == 2


# ======================== Endpoints API: the workspace's list (white box) ========================


@pytest.mark.parametrize("source", SOURCES)
def test_upload_follows_the_workspace_list(config, tmp_path, source):
    server = FakeFilesServer({"dp.part": always(403)}, DATA_PLANE)
    w = _client(config, storage_proxy=False, endpoints_api=True)

    _run(server, lambda: _upload(w, source, LARGE, False, tmp_path))

    assert server.endpoints_touched() == ["dp", "offload"]
    assert server.stored == {"offload": LARGE}
    server.assert_credentials()


def test_transfers_follow_the_workspace_list_by_default(config, tmp_path):
    server = FakeFilesServer(plan=RIG_PLAN)
    w = _client(config, storage_proxy=False, endpoints_api=None)

    _run(server, lambda: _upload(w, "file", LARGE, False, tmp_path))

    assert server.endpoints_touched() == ["rig"]
    assert server.stored == {"rig": LARGE}


def test_server_list_takes_precedence_over_the_storage_proxy_probe(config, tmp_path):
    server = FakeFilesServer(plan=[OFFLOAD_ENTRY, FLOOR_ENTRY])
    w = _client(config, storage_proxy=True, endpoints_api=True)

    _run(server, lambda: _upload(w, "file", LARGE, False, tmp_path))

    assert "scim" not in server.calls and "probe" not in server.calls
    assert server.endpoints_touched() == ["offload"]


@pytest.mark.parametrize("storage_proxy", [False, True], ids=["default", "storage-proxy-flag"])
def test_unusable_endpoints_api_uses_the_built_in_order(config, tmp_path, storage_proxy):
    server = FakeFilesServer()
    w = _client(config, storage_proxy=storage_proxy, endpoints_api=True)

    _run(server, lambda: _upload(w, "file", LARGE, False, tmp_path))

    assert server.calls[0] == "endpoints"
    assert "probe" not in server.calls
    assert server.endpoints_touched() == ["offload"]


def test_endpoints_are_resolved_once_per_client(config, tmp_path):
    server = _download_server(plan=DATA_PLANE)
    w = _client(config, storage_proxy=False, endpoints_api=True)

    def transfers():
        _upload(w, "file", LARGE, False, tmp_path)
        _upload(w, "seekable", SMALL, False, tmp_path)
        _download(w)

    _run(server, transfers)

    assert server.counts["endpoints"] == 1


@pytest.mark.parametrize(
    "source, data, use_parallel",
    [
        ("file", SMALL, False),
        # Their size is only known once read, so they reach the presigned path before they turn out to need a
        # single-shot upload.
        ("non-seekable", SMALL, False),
        ("non-seekable", b"", False),
        ("non-seekable", b"", True),
    ],
)
def test_small_upload_with_only_presigned_listed_uses_the_workspace(config, tmp_path, source, data, use_parallel):
    server = FakeFilesServer(plan=[OFFLOAD_ENTRY])
    w = _client(config, storage_proxy=False, endpoints_api=True)

    _run(server, lambda: _upload(w, source, data, use_parallel, tmp_path))

    assert server.calls[0] == "endpoints"
    assert server.stored == {"floor": data}


def test_upload_walks_the_non_data_plane_order_from_presigned_to_rig(config, tmp_path):
    server = FakeFilesServer({"offload.part": always(403)}, [OFFLOAD_ENTRY, RIG_ENTRY, FLOOR_ENTRY])
    w = _client(config, storage_proxy=False, endpoints_api=True)

    _run(server, lambda: _upload(w, "file", LARGE, False, tmp_path))

    assert server.endpoints_touched() == ["offload", "rig"]
    assert server.aborted == {"offload"}
    assert server.stored == {"rig": LARGE}
    server.assert_credentials()


@pytest.mark.parametrize("use_parallel", [False, True], ids=["sequential", "parallel"])
@pytest.mark.parametrize("source", SOURCES)
def test_large_upload_on_single_shot_only_endpoint_uses_single_shot(config, tmp_path, source, use_parallel):
    server = FakeFilesServer(plan=[FLOOR_ENTRY])
    w = _client(config, storage_proxy=False, endpoints_api=True)

    _run(server, lambda: _upload(w, source, LARGE, use_parallel, tmp_path))

    assert server.calls == ["endpoints", "floor.single"]
    assert server.stored == {"floor": LARGE}


@pytest.mark.parametrize("source", ["file", "seekable"])
def test_failed_single_shot_is_replayed_from_a_rereadable_source(config, tmp_path, source):
    single_shot_dp = {**DP_ENTRY, "multipart_upload_supported": False}
    server = FakeFilesServer({"dp.single": always(500)}, [single_shot_dp, OFFLOAD_ENTRY])
    w = _client(config, storage_proxy=False, endpoints_api=True)

    _run(server, lambda: _upload(w, source, LARGE, False, tmp_path))

    assert server.endpoints_touched() == ["dp", "offload"]
    assert server.stored == {"offload": LARGE}


def test_failed_single_shot_of_a_non_seekable_stream_cannot_be_replayed(config, tmp_path):
    # The whole stream was handed to the single-shot PUT, so nothing is left to send to the next endpoint.
    single_shot_dp = {**DP_ENTRY, "multipart_upload_supported": False}
    server = FakeFilesServer({"dp.single": always(500)}, [single_shot_dp, OFFLOAD_ENTRY])
    w = _client(config, storage_proxy=False, endpoints_api=True)

    with pytest.raises(InternalError):
        _run(server, lambda: _upload(w, "non-seekable", LARGE, False, tmp_path))

    assert server.endpoints_touched() == ["dp"]


@pytest.mark.parametrize("download", ["stream", "to-file", "parallel"])
def test_download_follows_the_workspace_list(config, download):
    server = _download_server({"offload.get": always(403)}, [OFFLOAD_ENTRY, FLOOR_ENTRY])
    w = _client(config, storage_proxy=True, endpoints_api=True)
    result = {}

    def run():
        if download == "stream":
            result.update(data=_download(w))
        else:
            result.update(data=_download_to(w, download == "parallel", parallelism=2))

    _run(server, run)

    assert result["data"] == LARGE
    assert "probe" not in server.calls
    assert server.endpoints_touched() == ["offload", "floor"]
    server.assert_credentials()
