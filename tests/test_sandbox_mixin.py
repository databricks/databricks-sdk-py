import http.client
import itertools
import queue
import socket
import socketserver
import sys
import threading

import grpc
import pytest

from databricks.sdk import WorkspaceClient
from databricks.sdk._sandbox_grpc import sandbox_service_pb2 as pb
from databricks.sdk._sandbox_grpc import sandbox_service_pb2_grpc as pb_grpc
from databricks.sdk.credentials_provider import credentials_strategy
from databricks.sdk.mixins import sandbox as sandbox_mod
from databricks.sdk.mixins.sandbox import (
    _CHUNKED,
    PortForward,
    SandboxExt,
    StreamMode,
    _RequestBody,
    _rewrite_head,
    _Target,
)

# The fakes below stand in for the authenticated gRPC channel and stub so these
# unit tests exercise execute_command's routing, streaming, retry, and channel
# lifecycle without opening a real network connection.


class _FakeApiClient:
    def __init__(self):
        self._cfg = object()


class _FakeChannel:
    def __init__(self, on_close=None):
        self.closed = 0
        self._on_close = on_close

    def close(self):
        self.closed += 1
        if self._on_close is not None:
            self._on_close()


def _response(seq, **event):
    return pb.ExecuteCommandResponse(process_event=pb.ProcessEvent(**event), sequence_number=seq)


def test_stream_input_sends_start_data_close_and_closes_channel(monkeypatch):
    channel = _FakeChannel()
    captured = {}

    class _FakeStub:
        def __init__(self, ch):
            pass

        def StreamInput(self, request_iterator, metadata=None):
            captured["requests"] = list(request_iterator)
            captured["metadata"] = metadata
            return pb.StreamInputResponse()

    monkeypatch.setattr(sandbox_mod, "open_channel", lambda cfg: channel)
    monkeypatch.setattr(pb_grpc, "SandboxServiceStub", _FakeStub)

    resp = SandboxExt(_FakeApiClient())._stream_input("sandboxes/s1", "cmd-1", [b"a", b"bc"])

    assert isinstance(resp, pb.StreamInputResponse)
    reqs = captured["requests"]
    assert [r.WhichOneof("event") for r in reqs] == ["start", "data", "data", "close"]
    assert reqs[0].start.command_id == "cmd-1"
    assert [reqs[1].data.data, reqs[2].data.data] == [b"a", b"bc"]
    assert captured["metadata"] == (("x-databricks-sandbox-name", "sandboxes/s1"),)
    assert channel.closed == 1


def test_stream_input_omits_close_when_disabled(monkeypatch):
    channel = _FakeChannel()
    captured = {}

    class _FakeStub:
        def __init__(self, ch):
            pass

        def StreamInput(self, request_iterator, metadata=None):
            captured["requests"] = list(request_iterator)
            return pb.StreamInputResponse()

    monkeypatch.setattr(sandbox_mod, "open_channel", lambda cfg: channel)
    monkeypatch.setattr(pb_grpc, "SandboxServiceStub", _FakeStub)

    SandboxExt(_FakeApiClient())._stream_input("sandboxes/s1", "cmd-1", [b"x"], close_stdin=False)

    assert [r.WhichOneof("event") for r in captured["requests"]] == ["start", "data"]
    assert channel.closed == 1


class _RpcError(grpc.RpcError):
    def __init__(self, code):
        self._code = code

    def code(self):
        return self._code


def _stream(items):
    """Yield ``items`` in order, raising any exception and running any callable
    (used to block the stream until the test releases it)."""
    for item in items:
        if isinstance(item, Exception):
            raise item
        if callable(item):
            item()
            continue
        yield item


def _attach_response(seq, **event):
    return pb.AttachCommandResponse(process_event=pb.ProcessEvent(**event), sequence_number=seq)


def _install_stub(
    monkeypatch,
    *,
    execute=(),
    attach=(),
    input_error=None,
    input_gate=None,
    input_fails_fast=False,
    on_channel_close=None,
):
    """Fake the channel and stub; return a dict capturing the requests sent.

    ``input_error``, if set, is raised by StreamInput: after it reads the input,
    or before reading anything when ``input_fails_fast``. ``input_gate``, if set,
    makes StreamInput wait on it before reading. ``on_channel_close``, if set, is
    called when any channel is closed - used to model a gRPC read that unblocks
    when the channel is torn down."""
    captured = {"channels": [], "attach_requests": [], "input_calls": 0}

    def new_channel(cfg):
        channel = _FakeChannel(on_channel_close)
        captured["channels"].append(channel)
        return channel

    class _FakeStub:
        def __init__(self, ch):
            pass

        def ExecuteCommand(self, request, metadata=None):
            captured["execute_request"] = request
            return _stream(execute)

        def AttachCommand(self, request, metadata=None):
            captured["attach_requests"].append(request)
            return _stream(attach)

        def StreamInput(self, request_iterator, metadata=None):
            captured["input_calls"] += 1
            if input_fails_fast:
                raise input_error
            if input_gate is not None:
                input_gate.wait()
            captured["input_requests"] = list(request_iterator)
            if input_error is not None:
                raise input_error
            return pb.StreamInputResponse()

    monkeypatch.setattr(sandbox_mod, "open_channel", new_channel)
    monkeypatch.setattr(pb_grpc, "SandboxServiceStub", _FakeStub)
    return captured


def _start(seq=1, command_id="cmd-1", pid=7):
    return _response(seq, start=pb.StartEvent(pid=pid, command_id=command_id))


def test_execute_command_splits_output_and_returns_exit_code(monkeypatch):
    captured = _install_stub(
        monkeypatch,
        execute=[
            _start(),
            _response(2, data=pb.DataEvent(stdout=b"hello\n")),
            _response(3, data=pb.DataEvent(stderr=b"oops\n")),
            _response(4, data=pb.DataEvent(stdout=b"bye\n")),
            _response(5, end=pb.EndEvent(exit_code=3)),
        ],
    )

    process = SandboxExt(_FakeApiClient()).execute_command(
        "sandboxes/s1", "/bin/bash", args=["-c", "x"], envs={"K": "v"}
    )

    assert process.command_id == "cmd-1"
    assert process.wait() == 3
    assert process.exit_code == 3
    assert process.pid == 7
    assert list(process.stdout) == ["hello\n", "bye\n"]
    assert process.stderr.read() == "oops\n"
    assert captured["execute_request"].cmd == "/bin/bash"
    assert list(captured["execute_request"].args) == ["-c", "x"]
    assert dict(captured["execute_request"].envs) == {"K": "v"}
    assert all(channel.closed == 1 for channel in captured["channels"])


def test_execute_command_decodes_characters_split_across_chunks(monkeypatch):
    snowman = "☃".encode("utf-8")
    _install_stub(
        monkeypatch,
        execute=[
            _start(),
            _response(2, data=pb.DataEvent(stdout=snowman[:1])),
            _response(3, data=pb.DataEvent(stdout=snowman[1:])),
            _response(4, end=pb.EndEvent(exit_code=0)),
        ],
    )

    process = SandboxExt(_FakeApiClient()).execute_command("s", "cmd")

    assert process.stdout.read() == "☃"


def test_execute_command_returns_bytes_when_text_is_false(monkeypatch):
    _install_stub(
        monkeypatch,
        execute=[_start(), _response(2, data=pb.DataEvent(stdout=b"\xff")), _response(3, end=pb.EndEvent(exit_code=0))],
    )

    process = SandboxExt(_FakeApiClient()).execute_command("s", "cmd", text=False)

    assert process.stdout.read() == b"\xff"


def test_execute_command_stream_modes(monkeypatch):
    events = [
        _start(),
        _response(2, data=pb.DataEvent(stdout=b"out ")),
        _response(3, data=pb.DataEvent(stderr=b"err")),
        _response(4, end=pb.EndEvent(exit_code=0)),
    ]
    _install_stub(monkeypatch, execute=events)
    api = SandboxExt(_FakeApiClient())

    merged = api.execute_command("s", "cmd", stderr=StreamMode.STDOUT)
    assert merged.stdout.read() == "out err"
    assert merged.stderr.read() == ""

    discarded = api.execute_command("s", "cmd", stdout=StreamMode.DEVNULL, stderr=StreamMode.DEVNULL)
    assert discarded.wait() == 0
    assert discarded.stdout.read() == ""
    assert discarded.stderr.read() == ""


def test_execute_command_rejects_stdout_redirected_to_stdout(monkeypatch):
    _install_stub(monkeypatch, execute=[_start(), _response(2, end=pb.EndEvent(exit_code=0))])

    with pytest.raises(ValueError, match="only valid for stderr"):
        SandboxExt(_FakeApiClient()).execute_command("s", "cmd", stdout=StreamMode.STDOUT)


def test_execute_command_requires_a_start_event(monkeypatch):
    _install_stub(monkeypatch, execute=[_response(1, end=pb.EndEvent(exit_code=0))])

    with pytest.raises(RuntimeError, match="expected a start event"):
        SandboxExt(_FakeApiClient()).execute_command("s", "cmd")


def test_stdin_sends_writes_then_end_of_file(monkeypatch):
    input_sent = threading.Event()
    captured = _install_stub(
        monkeypatch,
        execute=[
            _start(),
            input_sent.wait,
            _response(2, data=pb.DataEvent(stdout=b"ab")),
            _response(3, end=pb.EndEvent(exit_code=0)),
        ],
    )

    process = SandboxExt(_FakeApiClient()).execute_command("sandboxes/s1", "/bin/cat")
    process.stdin.write("a")
    process.stdin.write(b"b")
    process.stdin.close()
    input_sent.set()

    assert process.stdout.read() == "ab"
    requests = captured["input_requests"]
    assert [r.WhichOneof("event") for r in requests] == ["start", "data", "data", "close"]
    assert requests[0].start.command_id == "cmd-1"
    assert [requests[1].data.data, requests[2].data.data] == [b"a", b"b"]
    with pytest.raises(ValueError, match="stdin is closed"):
        process.stdin.write("c")


def test_stdin_left_open_is_closed_when_the_command_exits(monkeypatch):
    input_written = threading.Event()
    captured = _install_stub(
        monkeypatch,
        execute=[_start(), input_written.wait, _response(2, end=pb.EndEvent(exit_code=0))],
    )

    process = SandboxExt(_FakeApiClient()).execute_command("s", "cmd")
    process.stdin.write("partial")
    input_written.set()

    assert process.wait() == 0
    process.stdin._sender.join(timeout=5)
    assert [r.WhichOneof("event") for r in captured["input_requests"]] == ["start", "data", "close"]
    with pytest.raises(ValueError, match="stdin is closed"):
        process.stdin.write("more")
    process.stdin.close()


def test_stdin_write_after_the_command_exits_raises(monkeypatch):
    captured = _install_stub(monkeypatch, execute=[_start(), _response(2, end=pb.EndEvent(exit_code=0))])

    process = SandboxExt(_FakeApiClient()).execute_command("s", "cmd")
    process.wait()

    with pytest.raises(ValueError, match="stdin is closed"):
        process.stdin.write("too late")
    assert "input_requests" not in captured


def test_stdin_failure_surfaces_from_close(monkeypatch):
    release = threading.Event()
    _install_stub(
        monkeypatch,
        execute=[_start(), release.wait, _response(2, end=pb.EndEvent(exit_code=0))],
        input_error=_RpcError(grpc.StatusCode.PERMISSION_DENIED),
    )

    process = SandboxExt(_FakeApiClient()).execute_command("s", "/bin/cat")
    process.stdin.write("data")

    with pytest.raises(grpc.RpcError):
        process.stdin.close()
    release.set()
    assert process.wait() == 0


def test_concurrent_stdin_writes_share_one_input_stream(monkeypatch):
    release = threading.Event()
    captured = _install_stub(monkeypatch, execute=[_start(), release.wait, _response(2, end=pb.EndEvent(exit_code=0))])
    process = SandboxExt(_FakeApiClient()).execute_command("s", "/bin/cat")

    writers = [threading.Thread(target=process.stdin.write, args=(f"{i}\n",)) for i in range(20)]
    for writer in writers:
        writer.start()
    for writer in writers:
        writer.join(timeout=5)
    process.stdin.close()
    release.set()

    assert captured["input_calls"] == 1
    sent = sorted(r.data.data for r in captured["input_requests"] if r.WhichOneof("event") == "data")
    assert sent == sorted(f"{i}\n".encode() for i in range(20))
    assert process.wait() == 0


def test_stdin_write_blocks_while_input_is_backed_up(monkeypatch):
    input_gate = threading.Event()
    release = threading.Event()
    captured = _install_stub(
        monkeypatch,
        execute=[_start(), release.wait, _response(2, end=pb.EndEvent(exit_code=0))],
        input_gate=input_gate,
    )
    process = SandboxExt(_FakeApiClient()).execute_command("s", "/bin/cat")

    def write_past_the_buffer():
        for i in range(sandbox_mod._STDIN_BUFFERED_CHUNKS + 1):
            process.stdin.write(f"{i}")

    writer = threading.Thread(target=write_past_the_buffer)
    writer.start()
    writer.join(timeout=0.5)
    assert writer.is_alive()

    input_gate.set()
    writer.join(timeout=5)
    assert not writer.is_alive()
    process.stdin.close()
    release.set()
    sent = [r for r in captured["input_requests"] if r.WhichOneof("event") == "data"]
    assert len(sent) == sandbox_mod._STDIN_BUFFERED_CHUNKS + 1


def test_stdin_send_failure_unblocks_a_waiting_write(monkeypatch):
    release = threading.Event()
    _install_stub(
        monkeypatch,
        execute=[_start(), release.wait, _response(2, end=pb.EndEvent(exit_code=0))],
        input_error=_RpcError(grpc.StatusCode.PERMISSION_DENIED),
        input_fails_fast=True,
    )
    process = SandboxExt(_FakeApiClient()).execute_command("s", "/bin/cat")
    errors = []

    def write_until_it_fails():
        try:
            for i in range(sandbox_mod._STDIN_BUFFERED_CHUNKS * 4):
                process.stdin.write(f"{i}")
        except grpc.RpcError as e:
            errors.append(e)

    writer = threading.Thread(target=write_until_it_fails)
    writer.start()
    writer.join(timeout=5)
    release.set()

    assert not writer.is_alive()
    assert [e.code() for e in errors] == [grpc.StatusCode.PERMISSION_DENIED]


def test_execute_command_raises_when_the_command_cannot_start(monkeypatch):
    captured = _install_stub(monkeypatch, execute=[_RpcError(grpc.StatusCode.NOT_FOUND)])

    with pytest.raises(grpc.RpcError) as error:
        SandboxExt(_FakeApiClient()).execute_command("sandboxes/missing", "cmd")

    assert error.value.code() == grpc.StatusCode.NOT_FOUND
    assert len(captured["channels"]) == 1
    assert captured["channels"][0].closed == 1


def test_execute_command_resumes_after_a_dropped_connection(monkeypatch):
    captured = _install_stub(
        monkeypatch,
        execute=[
            _start(),
            _response(2, data=pb.DataEvent(stdout=b"one ")),
            _RpcError(grpc.StatusCode.UNAVAILABLE),
        ],
        attach=[
            _attach_response(3, data=pb.DataEvent(stdout=b"two")),
            _attach_response(4, end=pb.EndEvent(exit_code=0)),
        ],
    )

    process = SandboxExt(_FakeApiClient()).execute_command("sandboxes/s1", "cmd")

    assert process.stdout.read() == "one two"
    assert process.wait() == 0
    [attach_request] = captured["attach_requests"]
    assert attach_request.command_id == "cmd-1"
    assert attach_request.last_sequence_number == 2


def test_execute_command_resumes_after_a_drop_right_after_start(monkeypatch):
    captured = _install_stub(
        monkeypatch,
        execute=[_start(), _RpcError(grpc.StatusCode.UNAVAILABLE)],
        attach=[
            _attach_response(2, data=pb.DataEvent(stdout=b"late")),
            _attach_response(3, end=pb.EndEvent(exit_code=0)),
        ],
    )

    process = SandboxExt(_FakeApiClient()).execute_command("s", "cmd")

    assert process.stdout.read() == "late"
    assert process.wait() == 0
    [attach_request] = captured["attach_requests"]
    assert attach_request.last_sequence_number == 1


def test_execute_command_stops_reconnecting_after_the_retry_budget(monkeypatch):
    monkeypatch.setattr(sandbox_mod, "_DEFAULT_MAX_ATTEMPTS", 2)
    captured = _install_stub(
        monkeypatch,
        execute=[_start(), _RpcError(grpc.StatusCode.UNAVAILABLE)],
        attach=[_attach_response(2, data=pb.DataEvent(stdout=b"x")), _RpcError(grpc.StatusCode.UNAVAILABLE)],
    )

    process = SandboxExt(_FakeApiClient()).execute_command("s", "cmd")

    with pytest.raises(grpc.RpcError) as error:
        process.wait(timeout=5)
    assert error.value.code() == grpc.StatusCode.UNAVAILABLE
    assert len(captured["attach_requests"]) == 2


def test_execute_command_fails_when_the_stream_ends_without_an_end_event(monkeypatch):
    _install_stub(monkeypatch, execute=[_start(), _response(2, data=pb.DataEvent(stdout=b"x"))])

    process = SandboxExt(_FakeApiClient()).execute_command("s", "cmd")

    with pytest.raises(RuntimeError, match="ended before the command exited"):
        process.wait(timeout=5)
    assert process.exit_code is None


def test_execute_command_surfaces_a_non_retryable_stream_failure(monkeypatch):
    _install_stub(
        monkeypatch,
        execute=[
            _start(),
            _response(2, data=pb.DataEvent(stdout=b"partial")),
            _RpcError(grpc.StatusCode.PERMISSION_DENIED),
        ],
    )

    process = SandboxExt(_FakeApiClient()).execute_command("s", "cmd")

    with pytest.raises(grpc.RpcError):
        process.wait()
    with pytest.raises(grpc.RpcError):
        list(process.stdout)
    assert process.exit_code is None


def test_wait_raises_timeout_while_the_command_runs(monkeypatch):
    release = threading.Event()
    _install_stub(monkeypatch, execute=[_start(), release.wait, _response(2, end=pb.EndEvent(exit_code=0))])

    process = SandboxExt(_FakeApiClient()).execute_command("s", "cmd")

    with pytest.raises(TimeoutError):
        process.wait(timeout=0.05)
    release.set()
    assert process.wait() == 0


def test_connect_command_replays_output_from_the_beginning(monkeypatch):
    captured = _install_stub(
        monkeypatch,
        attach=[
            _attach_response(1, start=pb.StartEvent(pid=9, command_id="cmd-1")),
            _attach_response(2, data=pb.DataEvent(stdout=b"replayed")),
            _attach_response(3, end=pb.EndEvent(exit_code=4)),
        ],
    )

    process = SandboxExt(_FakeApiClient()).connect_command("sandboxes/s1", "cmd-1")

    assert process.stdout.read() == "replayed"
    assert process.wait() == 4
    assert process.pid == 9
    [attach_request] = captured["attach_requests"]
    assert attach_request.command_id == "cmd-1"
    assert attach_request.last_sequence_number == 0


def test_close_tears_down_a_blocked_command(monkeypatch):
    cancelled = threading.Event()
    captured = _install_stub(
        monkeypatch,
        execute=[_start(), cancelled.wait, _RpcError(grpc.StatusCode.CANCELLED)],
        on_channel_close=cancelled.set,
    )
    process = SandboxExt(_FakeApiClient()).execute_command("s", "cmd")

    reader_done = threading.Event()
    output = []

    def read():
        output.append(process.stdout.read())
        reader_done.set()

    threading.Thread(target=read, daemon=True).start()
    assert not reader_done.wait(0.3)  # hung: no output and the stream is blocked

    process.close()

    assert reader_done.wait(5)
    assert output == [""]
    assert process._closed
    assert captured["channels"][0].closed >= 1
    with pytest.raises(RuntimeError, match="handle was closed"):
        process.wait(timeout=5)


def test_close_is_idempotent_after_completion(monkeypatch):
    _install_stub(monkeypatch, execute=[_start(), _response(2, end=pb.EndEvent(exit_code=0))])
    process = SandboxExt(_FakeApiClient()).execute_command("s", "cmd")

    assert process.wait(timeout=5) == 0
    process.close()
    process.close()
    assert process._closed


def test_context_manager_closes_the_handle(monkeypatch):
    cancelled = threading.Event()
    _install_stub(
        monkeypatch,
        execute=[_start(), cancelled.wait, _RpcError(grpc.StatusCode.CANCELLED)],
        on_channel_close=cancelled.set,
    )

    with SandboxExt(_FakeApiClient()).execute_command("s", "cmd") as process:
        assert process.command_id == "cmd-1"

    assert process._closed
    assert process._done.is_set()


def test_read_times_out_when_output_stalls(monkeypatch):
    stall = threading.Event()
    _install_stub(monkeypatch, execute=[_start(), stall.wait, _response(2, end=pb.EndEvent(exit_code=0))])
    process = SandboxExt(_FakeApiClient()).execute_command("s", "cmd")

    with pytest.raises(TimeoutError):
        process.stdout.read(timeout=0.3)

    stall.set()
    assert process.wait(timeout=5) == 0


def test_output_iterates_lines_across_chunk_boundaries(monkeypatch):
    _install_stub(
        monkeypatch,
        execute=[
            _start(),
            _response(2, data=pb.DataEvent(stdout=b"foo")),
            _response(3, data=pb.DataEvent(stdout=b"bar\nbaz\n")),
            _response(4, data=pb.DataEvent(stdout=b"qux")),
            _response(5, end=pb.EndEvent(exit_code=0)),
        ],
    )
    process = SandboxExt(_FakeApiClient()).execute_command("s", "cmd")

    assert list(process.stdout) == ["foobar\n", "baz\n", "qux"]
    assert process.wait() == 0


def test_readline_returns_one_line_at_a_time(monkeypatch):
    _install_stub(
        monkeypatch,
        execute=[
            _start(),
            _response(2, data=pb.DataEvent(stdout=b"one\ntwo\n")),
            _response(3, end=pb.EndEvent(exit_code=0)),
        ],
    )
    process = SandboxExt(_FakeApiClient()).execute_command("s", "cmd")

    assert process.stdout.readline() == "one\n"
    assert process.stdout.readline() == "two\n"
    assert process.stdout.readline() == ""  # EOF
    assert process.wait() == 0


def test_read1_returns_output_as_it_arrives(monkeypatch):
    _install_stub(
        monkeypatch,
        execute=[
            _start(),
            _response(2, data=pb.DataEvent(stdout=b"ab")),
            _response(3, data=pb.DataEvent(stdout=b"cd")),
            _response(4, end=pb.EndEvent(exit_code=0)),
        ],
    )
    process = SandboxExt(_FakeApiClient()).execute_command("s", "cmd")

    out = process.stdout
    chunks = []
    while chunk := out.read1():
        chunks.append(chunk)
    assert chunks == ["ab", "cd"]
    assert out.read1() == ""  # EOF
    assert process.wait() == 0


def test_read_with_size_returns_bounded_output(monkeypatch):
    _install_stub(
        monkeypatch,
        execute=[
            _start(),
            _response(2, data=pb.DataEvent(stdout=b"ab")),
            _response(3, data=pb.DataEvent(stdout=b"cd")),
            _response(4, data=pb.DataEvent(stdout=b"ef")),
            _response(5, end=pb.EndEvent(exit_code=0)),
        ],
    )
    process = SandboxExt(_FakeApiClient()).execute_command("s", "cmd")

    out = process.stdout
    assert out.read(3) == "abc"  # exactly size units; remainder stays buffered
    assert out.read(10) == "def"  # size larger than what is left returns the rest
    assert out.read() == ""  # drained
    assert process.wait() == 0


def test_read1_with_size_returns_at_most_size(monkeypatch):
    _install_stub(
        monkeypatch,
        execute=[
            _start(),
            _response(2, data=pb.DataEvent(stdout=b"abcd")),
            _response(3, end=pb.EndEvent(exit_code=0)),
        ],
    )
    process = SandboxExt(_FakeApiClient()).execute_command("s", "cmd")

    out = process.stdout
    assert out.read1(2) == "ab"  # at most size from what is available now
    assert out.read1(2) == "cd"  # remainder stayed buffered
    assert out.read1() == ""  # EOF
    assert process.wait() == 0


def test_pid_is_available_synchronously(monkeypatch):
    release = threading.Event()
    _install_stub(monkeypatch, execute=[_start(pid=4321), release.wait, _response(2, end=pb.EndEvent(exit_code=0))])

    process = SandboxExt(_FakeApiClient()).execute_command("s", "cmd")

    # Set from the start event before execute_command returns - the command is
    # still running (reader blocked) and no output has been read.
    assert process.pid == 4321
    release.set()
    assert process.wait() == 0


# The fake workspace stands in for the sandbox proxy: it records each request head
# that the relay sends, so these tests check exactly what leaves the SDK.

_WAIT_SECONDS = 5
_SANDBOX_ID = "happy-panda-4821"
_PROXY_PREFIX = f"/sandbox-proxy/sandboxes/{_SANDBOX_ID}/ports/10080"


@credentials_strategy("sandbox-port-forward-test-bearer", [])
def _bearer_credentials(_cfg):
    return lambda: {"Authorization": "Bearer dapi-token"}


class _FakeWorkspace(socketserver.ThreadingTCPServer):
    """Records each request head and either echoes an upgraded stream or answers with a fixed response."""

    daemon_threads = True
    allow_reuse_address = True

    def __init__(self):
        self.received = queue.Queue()
        super().__init__(("127.0.0.1", 0), _FakeWorkspaceHandler)

    @property
    def url(self) -> str:
        return f"http://127.0.0.1:{self.server_address[1]}"


class _FakeWorkspaceHandler(socketserver.StreamRequestHandler):
    server: _FakeWorkspace

    def handle(self):
        request_line = self.rfile.readline().decode("latin-1").rstrip("\r\n")
        if request_line.startswith("GET /.well-known/databricks-config "):
            # WorkspaceClient probes host metadata at construction; that is not a relayed request.
            self.wfile.write(b"HTTP/1.1 404 Not Found\r\nContent-Length: 0\r\nConnection: close\r\n\r\n")
            return
        headers = {}
        while line := self.rfile.readline().decode("latin-1").rstrip("\r\n"):
            name, _, value = line.partition(":")
            headers[name.strip().lower()] = value.strip()
        body = self.rfile.read(int(headers.get("content-length", "0")))
        self.server.received.put((request_line, headers, body))
        if headers.get("upgrade") == "websocket":
            self.wfile.write(b"HTTP/1.1 101 Switching Protocols\r\nUpgrade: websocket\r\nConnection: upgrade\r\n\r\n")
            self.wfile.flush()
            self.wfile.write(self.rfile.read(4))
            return
        self.wfile.write(
            b"HTTP/1.1 201 Created\r\nSet-Cookie: app=1\r\nContent-Length: 5\r\nConnection: close\r\n\r\nhello"
        )


@pytest.fixture
def workspace():
    server = _FakeWorkspace()
    threading.Thread(target=server.serve_forever, daemon=True).start()
    yield server
    server.shutdown()
    server.server_close()


@pytest.fixture
def forward(workspace):
    with PortForward(
        host=workspace.url,
        authenticate=lambda: {"Authorization": "Bearer dapi-token"},
        name=_SANDBOX_ID,
        remote_port=10080,
    ) as forward:
        yield forward


def _connect(port: int) -> socket.socket:
    return socket.create_connection(("127.0.0.1", port), timeout=_WAIT_SECONDS)


@pytest.mark.parametrize("name", [f"sandboxes/{_SANDBOX_ID}", _SANDBOX_ID])
def test_sandbox_port_forward_targets_the_sandbox_proxy_with_sdk_credentials(workspace, name):
    client = WorkspaceClient(host=workspace.url, credentials_strategy=_bearer_credentials)

    with client.sandbox.port_forward(name, 10080) as forward:
        connection = http.client.HTTPConnection("127.0.0.1", forward.local_port, timeout=_WAIT_SECONDS)
        connection.request("GET", "/hello", headers={"Authorization": "Basic local-credential"})
        connection.getresponse().read()

    request_line, headers, _ = workspace.received.get(timeout=_WAIT_SECONDS)
    assert request_line == f"GET {_PROXY_PREFIX}/hello HTTP/1.1"
    assert headers["authorization"] == "Bearer dapi-token"


def test_relays_requests_with_the_token_and_the_apps_path(forward, workspace):
    connection = http.client.HTTPConnection("127.0.0.1", forward.local_port, timeout=_WAIT_SECONDS)
    connection.request(
        "POST",
        "/api/items?limit=5",
        body=b"payload",
        headers={"Authorization": "Basic local-credential", "Cookie": "app=1"},
    )
    response = connection.getresponse()

    request_line, headers, body = workspace.received.get(timeout=_WAIT_SECONDS)
    assert request_line == f"POST {_PROXY_PREFIX}/api/items?limit=5 HTTP/1.1"
    assert headers["authorization"] == "Bearer dapi-token"
    assert headers["host"] == f"127.0.0.1:{workspace.server_address[1]}"
    assert headers["cookie"] == "app=1"
    assert body == b"payload"
    assert response.status == 201
    assert response.getheader("Set-Cookie") == "app=1"
    assert response.read() == b"hello"


def test_relays_upgraded_connections_in_both_directions(forward, workspace):
    with _connect(forward.local_port) as client:
        client.sendall(b"GET /ws HTTP/1.1\r\nHost: 127.0.0.1\r\nConnection: Upgrade\r\nUpgrade: websocket\r\n\r\n")
        reader = client.makefile("rb")
        assert reader.readline().startswith(b"HTTP/1.1 101")
        while reader.readline() != b"\r\n":
            pass
        request_line, headers, _ = workspace.received.get(timeout=_WAIT_SECONDS)
        assert request_line == f"GET {_PROXY_PREFIX}/ws HTTP/1.1"
        assert headers["connection"] == "upgrade"

        client.sendall(b"ping")
        assert reader.read(4) == b"ping"


def test_answers_after_the_client_half_closes(forward):
    with _connect(forward.local_port) as client:
        client.sendall(b"GET /half HTTP/1.1\r\nHost: 127.0.0.1\r\n\r\n")
        client.shutdown(socket.SHUT_WR)

        response = client.makefile("rb").read()

    assert response.startswith(b"HTTP/1.1 201 Created"), response
    assert response.endswith(b"hello"), response


@pytest.mark.parametrize(
    "head",
    [
        b"GARBAGE\r\n\r\n",
        b"GET /../../api/2.0/clusters/list HTTP/1.1\r\nHost: x\r\n\r\n",
        b"POST /x HTTP/1.1\r\nHost: x\r\nContent-Length: 3\r\nTransfer-Encoding: chunked\r\n\r\n",
        b"POST /x HTTP/1.1\r\nHost: x\r\nContent-Length: 3\r\nContent-Length: 4\r\n\r\n",
        b"POST /x HTTP/1.1\r\nHost: x\r\nTransfer-Encoding: gzip, chunked\r\n\r\n",
        b"POST /x HTTP/1.1\r\nHost: x\r\nContent-Length: +3\r\n\r\n",
    ],
)
def test_answers_400_without_reaching_the_workspace(forward, workspace, head):
    with _connect(forward.local_port) as client:
        client.sendall(head)
        response = client.makefile("rb").read()

    assert response.startswith(b"HTTP/1.1 400 Bad Request"), response
    assert workspace.received.empty()


def test_answers_502_when_the_workspace_is_unreachable():
    with socket.socket() as unused:
        unused.bind(("127.0.0.1", 0))
        port = unused.getsockname()[1]
    with PortForward(
        host=f"http://127.0.0.1:{port}",
        authenticate=lambda: {"Authorization": "Bearer t"},
        name=_SANDBOX_ID,
        remote_port=10080,
    ) as forward:
        connection = http.client.HTTPConnection("127.0.0.1", forward.local_port, timeout=_WAIT_SECONDS)
        connection.request("GET", "/")
        response = connection.getresponse()

        assert response.status == 502
        assert response.getheader("Content-Type") == "text/plain; charset=utf-8"
        assert response.read().startswith(b"port forward failed:")


def test_answers_502_without_reaching_the_workspace_when_authentication_fails(workspace):
    def fail():
        raise RuntimeError("token endpoint unavailable")

    with PortForward(host=workspace.url, authenticate=fail, name=_SANDBOX_ID, remote_port=10080) as forward:
        connection = http.client.HTTPConnection("127.0.0.1", forward.local_port, timeout=_WAIT_SECONDS)
        connection.request("GET", "/")
        response = connection.getresponse()

        assert response.status == 502
        assert b"could not authenticate" in response.read()
    assert workspace.received.empty()


def test_resolves_credentials_for_each_connection(workspace):
    tokens = (f"token-{index}" for index in itertools.count())

    with PortForward(
        host=workspace.url,
        authenticate=lambda: {"Authorization": f"Bearer {next(tokens)}"},
        name=_SANDBOX_ID,
        remote_port=10080,
    ) as forward:
        for _ in range(2):
            connection = http.client.HTTPConnection("127.0.0.1", forward.local_port, timeout=_WAIT_SECONDS)
            connection.request("GET", "/")
            connection.getresponse().read()

    authorizations = [workspace.received.get(timeout=_WAIT_SECONDS)[1]["authorization"] for _ in range(2)]
    assert authorizations == ["Bearer token-0", "Bearer token-1"]


def test_forwards_one_request_per_connection(forward, workspace):
    with _connect(forward.local_port) as client:
        client.sendall(
            b"POST /first HTTP/1.1\r\nHost: x\r\nContent-Length: 3\r\n\r\nabc"
            b"GET /second HTTP/1.1\r\nHost: x\r\n\r\n"
        )
        response = client.makefile("rb").read()

    request_line, _, body = workspace.received.get(timeout=_WAIT_SECONDS)
    assert request_line == f"POST {_PROXY_PREFIX}/first HTTP/1.1"
    assert body == b"abc"
    assert response.startswith(b"HTTP/1.1 201 Created"), response
    assert workspace.received.empty()


def test_aborts_when_the_client_stops_before_the_body_ends(forward, workspace):
    with _connect(forward.local_port) as client:
        client.sendall(b"POST /upload HTTP/1.1\r\nHost: x\r\nContent-Length: 10\r\n\r\nabc")
        client.shutdown(socket.SHUT_WR)

        # The workspace sees the upload end early instead of waiting for the other 7 bytes.
        _, _, body = workspace.received.get(timeout=_WAIT_SECONDS)
        assert body == b"abc"
        assert client.makefile("rb").read() == b""


def test_drops_a_head_over_the_limit_that_arrives_in_one_read(forward, workspace):
    with _connect(forward.local_port) as client:
        client.sendall(b"GET / HTTP/1.1\r\nX-Big: " + b"a" * (70 * 1024) + b"\r\n\r\n")
        assert client.makefile("rb").read() == b""
    assert workspace.received.empty()


def test_closes_a_connection_that_never_finishes_its_head(monkeypatch, forward, workspace):
    monkeypatch.setattr(sandbox_mod, "_HEAD_TIMEOUT_SECONDS", 0.2)

    with _connect(forward.local_port) as client:
        client.sendall(b"GET / HTTP/1.1\r\nHost: x\r\n")
        assert client.recv(1) == b""
    assert workspace.received.empty()


def test_answers_502_when_the_workspace_never_completes_the_tls_handshake(monkeypatch):
    monkeypatch.setattr(sandbox_mod, "_CONNECT_TIMEOUT_SECONDS", 0.2)
    with socket.socket() as silent:
        silent.bind(("127.0.0.1", 0))
        silent.listen()
        with PortForward(
            host=f"https://127.0.0.1:{silent.getsockname()[1]}",
            authenticate=lambda: {"Authorization": "Bearer t"},
            name=_SANDBOX_ID,
            remote_port=10080,
        ) as forward:
            connection = http.client.HTTPConnection("127.0.0.1", forward.local_port, timeout=_WAIT_SECONDS)
            connection.request("GET", "/")

            assert connection.getresponse().status == 502


@pytest.mark.skipif(sys.platform == "win32", reason="Windows does not reuse local addresses")
def test_rebinds_a_fixed_local_port_right_after_close(workspace):
    def forward_once(local_port):
        with PortForward(
            host=workspace.url,
            authenticate=lambda: {"Authorization": "Bearer t"},
            name=_SANDBOX_ID,
            remote_port=10080,
            local_port=local_port,
        ) as forward:
            # The relay closes the local connection after the response, which leaves it in TIME_WAIT.
            connection = http.client.HTTPConnection("127.0.0.1", forward.local_port, timeout=_WAIT_SECONDS)
            connection.request("GET", "/")
            connection.getresponse().read()
            return forward.local_port

    port = forward_once(0)

    assert forward_once(port) == port


def test_url_is_the_local_http_address(forward):
    assert forward.url == f"http://127.0.0.1:{forward.local_port}"


@pytest.mark.parametrize("name", ["", "sandboxes/", "sandboxes/a/ports/9444", "sandboxes/..", "a b"])
def test_rejects_a_name_that_is_not_one_sandbox(name):
    with pytest.raises(ValueError):
        PortForward(host="https://workspace.example.com", authenticate=dict, name=name, remote_port=10080)


def test_request_body_ends_after_a_chunked_body_split_across_reads():
    stream = b"3;ext=1\r\nabc\r\n10\r\n" + b"x" * 16 + b"\r\n0\r\nTrailer: t\r\n\r\n"
    body = _RequestBody(_CHUNKED)

    taken = b"".join(body.take(stream[i : i + 3]) for i in range(0, len(stream), 3))

    assert taken == stream
    assert body.complete


def test_request_body_excludes_bytes_after_the_body():
    chunked = _RequestBody(_CHUNKED)
    fixed = _RequestBody(3)

    assert chunked.take(b"0\r\n\r\nGET /next") == b"0\r\n\r\n"
    assert fixed.take(b"abcGET /next") == b"abc"
    assert chunked.complete and fixed.complete


@pytest.mark.parametrize("stream", [b"zz\r\n", b"3\r\nabcd\r\n", b"3\nabc"])
def test_request_body_rejects_malformed_chunks(stream):
    with pytest.raises(ValueError):
        _RequestBody(_CHUNKED).take(stream)


def test_close_stops_listening(forward):
    port = forward.local_port

    forward.close()

    with pytest.raises(ConnectionRefusedError):
        socket.create_connection(("127.0.0.1", port), timeout=_WAIT_SECONDS)


_TARGET = _Target(
    scheme="https",
    netloc="workspace.example.com",
    hostname="workspace.example.com",
    port=443,
    path_prefix=_PROXY_PREFIX,
    authenticate=lambda: {},
)


def test_rewrite_drops_local_credentials_and_hop_by_hop_headers():
    head = (
        b"GET http://127.0.0.1:8080/index.html?q=1 HTTP/1.1\r\n"
        b"Host: 127.0.0.1:8080\r\n"
        b"Authorization: Basic local\r\n"
        b"Connection: keep-alive, x-nominated\r\n"
        b"Keep-Alive: timeout=5\r\n"
        b"X-Nominated: dropped\r\n"
        b"Cookie: app=1"
    )

    rewritten = _rewrite_head(head, _TARGET, {"Authorization": "Bearer dapi-token"})

    assert not rewritten.upgrade
    assert (
        rewritten.head
        == (
            f"GET {_PROXY_PREFIX}/index.html?q=1 HTTP/1.1\r\n"
            "Host: workspace.example.com\r\n"
            "Authorization: Bearer dapi-token\r\n"
            "Connection: close\r\n"
            "Cookie: app=1\r\n\r\n"
        ).encode()
    )


def test_rewrite_replaces_a_local_header_whose_name_matches_an_sdk_header():
    head = b"GET /x HTTP/1.1\r\nHost: x\r\nX-Api-Key: local\r\nx-api-key: also-local"

    rewritten = _rewrite_head(head, _TARGET, {"X-Api-Key": "sdk"})

    assert b"local" not in rewritten.head
    assert rewritten.head.count(b"X-Api-Key: sdk") == 1


def test_rewrite_rejects_a_malformed_request_line():
    assert _rewrite_head(b"GARBAGE", _TARGET, {}) is None


@pytest.mark.parametrize(
    "path",
    ["/../../api/2.0/clusters/list", "/a/%2E%2e/b", "/a/.%2e\\b", "/./x?q=1"],
)
def test_rewrite_rejects_dot_segments(path):
    assert _rewrite_head(f"GET {path} HTTP/1.1\r\nHost: x".encode(), _TARGET, {}) is None


def test_rewrite_keeps_dots_inside_segments_and_queries():
    rewritten = _rewrite_head(b"GET /v1.2/file..txt?next=../x HTTP/1.1\r\nHost: x", _TARGET, {})

    assert rewritten.head.startswith(f"GET {_PROXY_PREFIX}/v1.2/file..txt?next=../x HTTP/1.1\r\n".encode())
