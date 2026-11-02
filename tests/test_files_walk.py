"""Which endpoints FilesExt transfers files through, and what a caller sees when they fail.

FakeFilesServer stands in for the hosts a transfer can reach: the workspace (the Files API and the presigned URL
coordination API), the data-plane storage proxy, and cloud storage behind presigned URLs. It records every
operation per endpoint.

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
from tempfile import NamedTemporaryFile
from threading import Lock
from typing import Callable, Dict, List, Optional, Tuple, Union
from urllib.parse import parse_qs, urlparse

import pytest
import requests
import requests_mock
from urllib3.exceptions import ProtocolError

from databricks.sdk import WorkspaceClient
from databricks.sdk.core import Config

from .test_files_utils import NonSeekableBuffer

WORKSPACE = "localhost"
STORAGE_PROXY = "storage-proxy.databricks.com"
CLOUD = "cloud.example.com"
FILE_PATH = "/Volumes/catalog/schema/volume/file.bin"
LAST_MODIFIED = "Thu, 28 Nov 2024 16:39:14 GMT"
PART_SIZE = 1024

_ERROR_CODES = {
    400: "INVALID_PARAMETER_VALUE",
    403: "PERMISSION_DENIED",
    404: "NOT_FOUND",
    409: "ALREADY_EXISTS",
    500: "INTERNAL_ERROR",
}

# Operations on presigned cloud URLs. They must never carry workspace credentials.
_PRESIGNED_OPS = {"offload.part", "offload.get"}


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


class FakeFilesServer:
    def __init__(self, faults: Optional[Dict[str, Callable[[int], Optional[Fault]]]] = None):
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
        if host == WORKSPACE and path == "/api/2.0/preview/scim/v2/Me" and method == "GET":
            return "scim"
        if host == STORAGE_PROXY and path == "/api/2.0/fs/files/DatabricksInternal/Probe/fullstack/wis":
            return "probe"
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
        if op == "scim":
            return requests_mock.create_response(request, json={}, headers={"X-Databricks-Org-Id": "12345"})
        if op == "probe":
            return requests_mock.create_response(request)
        endpoint, action = op.split(".", 1)
        url = urlparse(request.url)
        query = parse_qs(url.query)
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


def _client(config: Config, storage_proxy: bool = True) -> WorkspaceClient:
    config = config.copy()
    config.experimental_files_ext_enable_storage_proxy = storage_proxy
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


ENDPOINT_LISTS = [
    EndpointList("built-in", ("presigned", "workspace")),
    EndpointList("built-in with the storage proxy", ("proxy", "presigned", "workspace"), storage_proxy=True),
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
}
# The fake's name for each endpoint that can come first in a list.
_FAKE_NAMES = {"proxy": "dp", "presigned": "offload"}

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


def _first_endpoint(scenario: Scenario) -> str:
    """The endpoint a multipart upload or a download starts on: the storage proxy when it is enabled and its
    probe reaches it, otherwise presigned URLs."""
    if scenario.endpoint_list.storage_proxy and dict(scenario.availability)["proxy"] != DOWN:
        return "proxy"
    return "presigned"


# Retries that run out raise TimeoutError from the API client's retry budget, which covers the workspace, and
# RuntimeError from the bounded retries of transfers to presigned URLs and the storage proxy.
def expected_upload(scenario: Scenario):
    """The outcome an upload has.

    - A file under one part is sent in a single shot to the workspace.
    - A non-seekable stream's size is known only once it is read. Read sequentially, a short one is sent in a
      single shot as above. Read in parallel, an upload session is opened first; an empty stream is then sent in a
      single shot to the workspace, and a short one as one part.
    - Anything else is a multipart upload on the first endpoint. A failure there raises, except a rejected
      transfer (403), which falls back to a single shot on the workspace.
    - A single shot that follows a rejected part replays the part read plus the unread rest, which can't be
      rewound, so the API client sends it once. An upload from a file in parallel reopens the file instead.
    """
    states = dict(scenario.availability)
    size = SIZES[scenario.size]
    session_first = scenario.source == "non-seekable" and scenario.mode == "parallel"
    workspace_up = states["workspace"] == UP
    if size < PART_SIZE and not session_first:
        return SUCCEEDS if workspace_up else TimeoutError
    if session_first and size == 0:
        return SUCCEEDS if workspace_up else requests.ConnectionError
    state = states[_first_endpoint(scenario)]
    if state == UP:
        return SUCCEEDS
    if state != REJECTS:
        return RuntimeError
    if workspace_up:
        return SUCCEEDS
    return TimeoutError if scenario.source == "file" and scenario.mode == "parallel" else requests.ConnectionError


def expected_download(scenario: Scenario):
    """The outcome a download has.

    - It starts on the first endpoint. A failure there raises, except a rejected transfer (403), which falls back
      to the Files API on the workspace.
    - After bytes arrived, a stream resumes on that endpoint and, if that fails too, raises its broken connection;
      a parallel download raises the failure of a later range.
    """
    states = dict(scenario.availability)
    state = states[_first_endpoint(scenario)]
    if state == UP:
        return SUCCEEDS
    if state == BREAKS:
        return RuntimeError if scenario.mode == "parallel" else requests.exceptions.ChunkedEncodingError
    if state == REJECTS:
        return SUCCEEDS if states["workspace"] == UP else TimeoutError
    return RuntimeError


def _scenario_client(config: Config, scenario: Scenario) -> WorkspaceClient:
    return _client(config, storage_proxy=scenario.endpoint_list.storage_proxy)


@pytest.mark.parametrize("scenario", UPLOAD_SCENARIOS, ids=str)
def test_upload_scenario(config, tmp_path, scenario):
    server = FakeFilesServer(scenario.faults())
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


def _download(w: WorkspaceClient) -> bytes:
    return w.files.download(FILE_PATH).contents.read()


def _download_to(w: WorkspaceClient, use_parallel: bool, parallelism: Optional[int] = None) -> bytes:
    if use_parallel and platform.system() == "Windows":
        # FilesExt downloads sequentially on Windows, so the parallel rules don't apply there.
        pytest.skip("Skipping parallel download tests on Windows")
    with NamedTemporaryFile(delete=False) as f:
        destination = f.name
    try:
        w.files.download_to(FILE_PATH, destination, use_parallel=use_parallel, parallelism=parallelism)
        with open(destination, "rb") as f:
            return f.read()
    finally:
        os.remove(destination)


@pytest.mark.parametrize("scenario", DOWNLOAD_SCENARIOS, ids=str)
def test_download_scenario(config, scenario):
    server = FakeFilesServer(scenario.faults())
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
