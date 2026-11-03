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
from databricks.sdk.mixins import files as files_mixin
from databricks.sdk.errors.platform import AlreadyExists

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
    """The endpoint a transfer starts on: the storage proxy when it is enabled and its probe reaches it, otherwise
    presigned URLs."""
    if scenario.endpoint_list.storage_proxy and dict(scenario.availability)["proxy"] != DOWN:
        return "proxy"
    return "presigned"


# Retries that run out raise TimeoutError from the API client's retry budget, which covers the workspace, and
# RuntimeError from the bounded retries of transfers to presigned URLs and the storage proxy.
def expected_upload(scenario: Scenario):
    """The outcome an upload has.

    - Endpoints are tried in order: the first endpoint, then the workspace, which takes single-shot uploads only.
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
    first = _first_endpoint(scenario)
    if size < PART_SIZE:
        if first == "proxy" and states[first] == UP:
            return SUCCEEDS
    else:
        if states[first] == UP:
            return SUCCEEDS
        if states[first] == BREAKS:
            return RuntimeError
    if states["workspace"] == UP:
        return SUCCEEDS
    return requests.ConnectionError if non_seekable and size >= PART_SIZE else TimeoutError


def expected_download(scenario: Scenario):
    """The outcome a download has.

    - Endpoints are tried in order: the first endpoint, then the workspace.
    - A failure before any bytes arrived moves the download to the next endpoint.
    - After bytes arrived, the download stays on that endpoint. A stream resumes there and, if that fails too,
      raises its broken connection; a parallel download raises the failure of a later range.
    """
    states = dict(scenario.availability)
    state = states[_first_endpoint(scenario)]
    if state == UP:
        return SUCCEEDS
    if state == BREAKS:
        return RuntimeError if scenario.mode == "parallel" else requests.exceptions.ChunkedEncodingError
    return SUCCEEDS if states["workspace"] == UP else TimeoutError


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
    server = FakeFilesServer({"dp.single": always(412)})
    config = config.copy()
    config.workspace_id = "1234"
    w = _client(config)

    with pytest.raises(AlreadyExists):
        _run(server, lambda: _upload(w, source, SMALL, False, tmp_path, overwrite=False))

    # The conflict is the caller's, so the upload does not move on to the workspace.
    assert "floor.single" not in server.calls
    assert server.request_headers["dp.single"][0]["X-Databricks-Workspace-Id"] == "1234"
