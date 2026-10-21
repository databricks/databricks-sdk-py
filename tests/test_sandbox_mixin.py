import threading

import grpc
import pytest

from databricks.sdk._sandbox_grpc import sandbox_service_pb2 as pb
from databricks.sdk._sandbox_grpc import sandbox_service_pb2_grpc as pb_grpc
from databricks.sdk.mixins import sandbox as sandbox_mod
from databricks.sdk.mixins.sandbox import SandboxExt, StreamMode

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
