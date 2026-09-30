import pytest

from databricks.sdk._sandbox_grpc import sandbox_service_pb2 as pb
from databricks.sdk._sandbox_grpc import sandbox_service_pb2_grpc as pb_grpc
from databricks.sdk.mixins import sandbox as sandbox_mod
from databricks.sdk.mixins.sandbox import SandboxExt

# The fakes below stand in for the authenticated gRPC channel and stub so these
# unit tests exercise execute_command's routing, streaming, retry, and channel
# lifecycle without opening a real network connection.


class _FakeApiClient:
    def __init__(self):
        self._cfg = object()


class _FakeChannel:
    def __init__(self):
        self.closed = 0

    def close(self):
        self.closed += 1


def _response(seq, **event):
    return pb.ExecuteCommandResponse(process_event=pb.ProcessEvent(**event), sequence_number=seq)


def test_execute_command_streams_responses_and_closes_channel(monkeypatch):
    channel = _FakeChannel()
    captured = {}

    class _FakeStub:
        def __init__(self, ch):
            captured["channel"] = ch

        def ExecuteCommand(self, request, metadata=None):
            captured["request"] = request
            captured["metadata"] = metadata
            return iter(
                [
                    _response(1, start=pb.StartEvent(pid=7)),
                    _response(2, data=pb.DataEvent(stdout=b"hi\n")),
                    _response(3, end=pb.EndEvent(exit_code=0)),
                ]
            )

    monkeypatch.setattr(sandbox_mod, "open_channel", lambda cfg: channel)
    monkeypatch.setattr(pb_grpc, "SandboxServiceStub", _FakeStub)

    api = SandboxExt(_FakeApiClient())
    events = list(api.execute_command_streaming("sandboxes/s1", "/bin/echo", args=["hi"], envs={"K": "v"}))

    assert [e.sequence_number for e in events] == [1, 2, 3]
    assert events[0].process_event.start.pid == 7
    assert events[2].process_event.end.exit_code == 0
    assert captured["channel"] is channel
    assert captured["request"].cmd == "/bin/echo"
    assert list(captured["request"].args) == ["hi"]
    assert dict(captured["request"].envs) == {"K": "v"}
    assert captured["metadata"] == (("x-databricks-sandbox-name", "sandboxes/s1"),)
    assert channel.closed == 1


def test_execute_command_closes_channel_when_abandoned(monkeypatch):
    channel = _FakeChannel()

    class _FakeStub:
        def __init__(self, ch):
            pass

        def ExecuteCommand(self, request, metadata=None):
            return iter([_response(1, start=pb.StartEvent(pid=1))])

    monkeypatch.setattr(sandbox_mod, "open_channel", lambda cfg: channel)
    monkeypatch.setattr(pb_grpc, "SandboxServiceStub", _FakeStub)

    stream = SandboxExt(_FakeApiClient()).execute_command_streaming("s", "cmd")
    assert next(stream).sequence_number == 1
    stream.close()
    assert channel.closed == 1


def test_execute_command_does_not_retry_by_default(monkeypatch):
    channel = _FakeChannel()
    calls = {"count": 0}

    class _FailingStub:
        def __init__(self, ch):
            pass

        def ExecuteCommand(self, request, metadata=None):
            calls["count"] += 1
            raise RuntimeError("transport failed")

    monkeypatch.setattr(sandbox_mod, "open_channel", lambda cfg: channel)
    monkeypatch.setattr(pb_grpc, "SandboxServiceStub", _FailingStub)

    stream = SandboxExt(_FakeApiClient()).execute_command_streaming("s", "cmd")
    with pytest.raises(RuntimeError, match="transport failed"):
        next(stream)

    assert calls["count"] == 1
    assert channel.closed == 1


def test_execute_command_retries_stream_open_when_opted_in(monkeypatch):
    channel = _FakeChannel()
    calls = {"count": 0}

    class _FlakyStub:
        def __init__(self, ch):
            pass

        def ExecuteCommand(self, request, metadata=None):
            calls["count"] += 1
            if calls["count"] == 1:
                raise RuntimeError("transient")
            return iter([_response(1, end=pb.EndEvent(exit_code=0))])

    monkeypatch.setattr(sandbox_mod, "open_channel", lambda cfg: channel)
    monkeypatch.setattr(pb_grpc, "SandboxServiceStub", _FlakyStub)

    events = list(
        SandboxExt(_FakeApiClient()).execute_command_streaming(
            "s",
            "cmd",
            is_retryable=lambda _exc: True,
            max_attempts=2,
            retry_interval_seconds=0.0,
        )
    )

    assert calls["count"] == 2
    assert events[0].process_event.end.exit_code == 0
    assert channel.closed == 1


def test_attach_command_streams_and_closes_channel(monkeypatch):
    channel = _FakeChannel()
    captured = {}

    class _FakeStub:
        def __init__(self, ch):
            pass

        def AttachCommand(self, request, metadata=None):
            captured["request"] = request
            captured["metadata"] = metadata
            return iter(
                [
                    pb.AttachCommandResponse(
                        process_event=pb.ProcessEvent(end=pb.EndEvent(exit_code=0)), sequence_number=5
                    )
                ]
            )

    monkeypatch.setattr(sandbox_mod, "open_channel", lambda cfg: channel)
    monkeypatch.setattr(pb_grpc, "SandboxServiceStub", _FakeStub)

    events = list(SandboxExt(_FakeApiClient()).attach_command("sandboxes/s1", "cmd-1", last_sequence_number=4))

    assert [e.sequence_number for e in events] == [5]
    assert captured["request"].command_id == "cmd-1"
    assert captured["request"].last_sequence_number == 4
    assert captured["metadata"] == (("x-databricks-sandbox-name", "sandboxes/s1"),)
    assert channel.closed == 1


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

    resp = SandboxExt(_FakeApiClient()).stream_input("sandboxes/s1", "cmd-1", [b"a", b"bc"])

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

    SandboxExt(_FakeApiClient()).stream_input("sandboxes/s1", "cmd-1", [b"x"], close_stdin=False)

    assert [r.WhichOneof("event") for r in captured["requests"]] == ["start", "data"]
    assert channel.closed == 1
