import pytest

from databricks.sdk.mixins._grpc_transport import (
    _ReplayFirstStream,
    _auth_metadata,
    _channel_options,
    _grpc_target,
    _headers_to_metadata,
    _is_unavailable,
    call_with_retry,
    open_channel,
    open_stream_with_retry,
)


class _FakeConfig:
    """Minimal stand-in for databricks.sdk.config.Config: the transport reads
    ``host``, ``user_agent``, ``_custom_headers``, and calls ``authenticate()``."""

    def __init__(
        self,
        *,
        headers=None,
        host="https://foo.cloud.databricks.com",
        error=None,
        custom_headers=None,
        user_agent="databricks-sdk-py/1.0.0 python/3.12 os/linux auth/pat",
    ):
        self._headers = headers or {}
        self._error = error
        self.host = host
        self._custom_headers = custom_headers or {}
        self.user_agent = user_agent

    def authenticate(self):
        if self._error is not None:
            raise self._error
        return self._headers


@pytest.mark.parametrize(
    "host,expected",
    [
        ("https://foo.cloud.databricks.com", "foo.cloud.databricks.com:443"),
        ("http://foo.cloud.databricks.com", "foo.cloud.databricks.com:443"),
        ("foo.cloud.databricks.com", "foo.cloud.databricks.com:443"),
        ("https://foo.cloud.databricks.com/", "foo.cloud.databricks.com:443"),
        ("https://foo.cloud.databricks.com/?x=1", "foo.cloud.databricks.com:443"),
        ("https://foo.cloud.databricks.com/some/path", "foo.cloud.databricks.com:443"),
        ("https://foo.cloud.databricks.com#frag", "foo.cloud.databricks.com:443"),
        # An explicit port is preserved rather than having :443 appended.
        ("https://localhost:8443", "localhost:8443"),
        ("localhost:8443", "localhost:8443"),
    ],
)
def test_grpc_target(host, expected):
    assert _grpc_target(host) == expected


def test_grpc_target_custom_port():
    assert _grpc_target("foo.cloud.databricks.com", port=9090) == "foo.cloud.databricks.com:9090"


def test_headers_to_metadata_lowercases_keys():
    headers = {"Authorization": "Bearer tok", "X-Databricks-Org-Id": "123"}
    assert _headers_to_metadata(headers) == [
        ("authorization", "Bearer tok"),
        ("x-databricks-org-id", "123"),
    ]


def test_headers_to_metadata_empty():
    assert _headers_to_metadata({}) == []


class _Retryable(Exception):
    pass


class _Fatal(Exception):
    pass


def _is_retryable(err: BaseException) -> bool:
    return isinstance(err, _Retryable)


def test_retry_succeeds_after_transient_failures():
    calls = {"n": 0}
    slept: list[float] = []

    def make_call():
        calls["n"] += 1
        if calls["n"] < 3:
            raise _Retryable()
        return "ok"

    result = call_with_retry(
        make_call,
        is_retryable=_is_retryable,
        max_attempts=5,
        retry_interval_seconds=1.5,
        sleep=slept.append,
    )

    assert result == "ok"
    assert calls["n"] == 3
    # Slept once before each of the two retries, never after success.
    assert slept == [1.5, 1.5]


def test_retry_reraises_non_retryable():
    calls = {"n": 0}

    def make_call():
        calls["n"] += 1
        raise _Fatal()

    with pytest.raises(_Fatal):
        call_with_retry(make_call, is_retryable=_is_retryable, max_attempts=5, sleep=lambda _: None)
    # A non-retryable error propagates on the first attempt, no retries.
    assert calls["n"] == 1


def test_retry_exhausts_attempts():
    calls = {"n": 0}

    def make_call():
        calls["n"] += 1
        raise _Retryable()

    with pytest.raises(TimeoutError):
        call_with_retry(
            make_call,
            is_retryable=_is_retryable,
            max_attempts=4,
            retry_interval_seconds=2.0,
            sleep=lambda _: None,
        )
    assert calls["n"] == 4


def test_stream_retry_opens_and_yields_full_stream():
    slept: list[float] = []
    opens = {"n": 0}

    def make_stream():
        opens["n"] += 1
        if opens["n"] < 3:
            # A not-ready backend fails on the first pull, so raise from the
            # iterator rather than from make_stream itself.
            def failing():
                raise _Retryable()
                yield  # pragma: no cover - unreachable, makes this a generator

            return failing()
        return iter(["start", "data", "end"])

    stream = open_stream_with_retry(
        make_stream,
        is_retryable=_is_retryable,
        max_attempts=5,
        retry_interval_seconds=1.0,
        sleep=slept.append,
    )

    assert list(stream) == ["start", "data", "end"]
    assert opens["n"] == 3
    assert slept == [1.0, 1.0]


def test_stream_retry_empty_stream():
    stream = open_stream_with_retry(lambda: iter(()), is_retryable=_is_retryable, sleep=lambda _: None)
    assert list(stream) == []


def test_stream_retry_does_not_retry_mid_stream_failure():
    opens = {"n": 0}

    def make_stream():
        opens["n"] += 1

        def gen():
            yield "start"
            raise _Retryable()

        return gen()

    stream = open_stream_with_retry(make_stream, is_retryable=_is_retryable, sleep=lambda _: None)

    assert next(stream) == "start"
    with pytest.raises(_Retryable):
        next(stream)
    assert opens["n"] == 1


def test_stream_mid_stream_retry_reopens_and_replays_from_start():
    opens = {"n": 0}
    slept: list[float] = []

    def make_stream():
        opens["n"] += 1
        if opens["n"] == 1:

            def failing():
                yield "start"
                raise _Retryable()

            return failing()
        return iter(["start", "data", "end"])

    stream = open_stream_with_retry(
        make_stream,
        is_retryable=_is_retryable,
        retry_mid_stream_failures=True,
        max_attempts=5,
        retry_interval_seconds=1.0,
        sleep=slept.append,
    )

    # The mid-stream failure re-issues the whole call, which restarts from the
    # first item, so "start" is delivered twice.
    assert list(stream) == ["start", "start", "data", "end"]
    assert opens["n"] == 2
    assert slept == [1.0]


def test_stream_mid_stream_retry_raises_non_retryable():
    opens = {"n": 0}

    def make_stream():
        opens["n"] += 1

        def gen():
            yield "start"
            raise _Fatal()

        return gen()

    stream = open_stream_with_retry(
        make_stream,
        is_retryable=_is_retryable,
        retry_mid_stream_failures=True,
        sleep=lambda _: None,
    )

    assert next(stream) == "start"
    with pytest.raises(_Fatal):
        next(stream)
    assert opens["n"] == 1


def test_stream_mid_stream_retry_bounded_by_max_attempts():
    opens = {"n": 0}
    slept: list[float] = []

    def make_stream():
        opens["n"] += 1

        def gen():
            yield "start"
            raise _Retryable()

        return gen()

    stream = open_stream_with_retry(
        make_stream,
        is_retryable=_is_retryable,
        retry_mid_stream_failures=True,
        max_attempts=3,
        retry_interval_seconds=2.0,
        sleep=slept.append,
    )

    collected = []
    with pytest.raises(_Retryable):
        collected.extend(stream)
    # One initial open plus max_attempts re-opens, each yielding "start".
    assert collected == ["start", "start", "start", "start"]
    assert opens["n"] == 4
    assert slept == [2.0, 2.0, 2.0]


def test_auth_metadata_forwards_headers_as_lowercased_metadata():
    captured = {}

    def callback(metadata, error):
        captured["metadata"] = metadata
        captured["error"] = error

    cfg = _FakeConfig(headers={"Authorization": "Bearer tok", "X-Databricks-Org-Id": "42"})
    _auth_metadata(cfg, callback)

    assert captured["error"] is None
    assert captured["metadata"] == (("authorization", "Bearer tok"), ("x-databricks-org-id", "42"))


def test_auth_metadata_forwards_credential_error():
    captured = {}

    def callback(metadata, error):
        captured["metadata"] = metadata
        captured["error"] = error

    boom = RuntimeError("token refresh failed")
    _auth_metadata(_FakeConfig(error=boom), callback)

    # On failure gRPC's contract is empty metadata + the error, not a raise.
    assert captured["metadata"] == ()
    assert captured["error"] is boom


def test_auth_metadata_merges_custom_headers_with_auth_winning():
    captured = {}

    def callback(metadata, error):
        captured["metadata"] = dict(metadata)
        captured["error"] = error

    cfg = _FakeConfig(
        headers={"Authorization": "Bearer tok"},
        custom_headers={"X-Custom": "v", "Authorization": "should-be-overridden"},
    )
    _auth_metadata(cfg, callback)

    assert captured["error"] is None
    # Custom headers ride along; auth headers win on a key collision.
    assert captured["metadata"] == {"x-custom": "v", "authorization": "Bearer tok"}


def test_auth_metadata_merge_is_case_insensitive():
    captured = {}

    def callback(metadata, error):
        captured["metadata"] = list(metadata)

    # Custom header and auth header name the same logical header with different
    # casing: the result must carry a single lowercased key, with auth winning.
    cfg = _FakeConfig(
        headers={"Authorization": "Bearer tok"},
        custom_headers={"authorization": "should-be-overridden"},
    )
    _auth_metadata(cfg, callback)

    assert captured["metadata"] == [("authorization", "Bearer tok")]


def test_is_unavailable_matches_only_unavailable():
    grpc = pytest.importorskip("grpc")

    class _RpcError(grpc.RpcError):
        def __init__(self, code):
            self._code = code

        def code(self):
            return self._code

    assert _is_unavailable(_RpcError(grpc.StatusCode.UNAVAILABLE))
    assert not _is_unavailable(_RpcError(grpc.StatusCode.DEADLINE_EXCEEDED))
    assert not _is_unavailable(RuntimeError("boom"))


def test_call_with_retry_default_retries_unavailable_not_deadline():
    grpc = pytest.importorskip("grpc")

    class _RpcError(grpc.RpcError):
        def __init__(self, code):
            self._code = code

        def code(self):
            return self._code

    unavailable_calls = {"n": 0}

    def raise_unavailable():
        unavailable_calls["n"] += 1
        raise _RpcError(grpc.StatusCode.UNAVAILABLE)

    with pytest.raises(TimeoutError):
        call_with_retry(raise_unavailable, max_attempts=3, sleep=lambda _: None)
    assert unavailable_calls["n"] == 3

    deadline_calls = {"n": 0}

    def raise_deadline():
        deadline_calls["n"] += 1
        raise _RpcError(grpc.StatusCode.DEADLINE_EXCEEDED)

    with pytest.raises(grpc.RpcError):
        call_with_retry(raise_deadline, max_attempts=3, sleep=lambda _: None)
    assert deadline_calls["n"] == 1


def test_call_with_retry_caller_can_opt_into_deadline():
    grpc = pytest.importorskip("grpc")

    class _RpcError(grpc.RpcError):
        def __init__(self, code):
            self._code = code

        def code(self):
            return self._code

    calls = {"n": 0}

    def raise_deadline():
        calls["n"] += 1
        raise _RpcError(grpc.StatusCode.DEADLINE_EXCEEDED)

    def retry_deadline(err):
        return isinstance(err, grpc.RpcError) and err.code() == grpc.StatusCode.DEADLINE_EXCEEDED

    with pytest.raises(TimeoutError):
        call_with_retry(raise_deadline, is_retryable=retry_deadline, max_attempts=2, sleep=lambda _: None)
    assert calls["n"] == 2


def test_replay_first_stream_yields_first_item_then_delegates_attributes():
    class _FakeStream:
        def __init__(self):
            self._rest = iter(["data", "end"])
            self.cancelled = False

        def __next__(self):
            return next(self._rest)

        def cancel(self):
            self.cancelled = True

    underlying = _FakeStream()
    wrapped = _ReplayFirstStream("start", underlying)

    assert list(wrapped) == ["start", "data", "end"]
    # cancel() (and any other attribute) reaches the underlying gRPC stream.
    wrapped.cancel()
    assert underlying.cancelled


def test_stream_retry_default_predicate_excludes_deadline_exceeded():
    grpc = pytest.importorskip("grpc")

    class _RpcError(grpc.RpcError):
        def __init__(self, code):
            self._code = code

        def code(self):
            return self._code

    def make_stream_raising(code):
        def failing():
            raise _RpcError(code)
            yield  # pragma: no cover - unreachable, makes this a generator

        return failing()

    with pytest.raises(grpc.RpcError):
        open_stream_with_retry(
            lambda: make_stream_raising(grpc.StatusCode.DEADLINE_EXCEEDED),
            max_attempts=3,
            sleep=lambda _: None,
        )


def test_channel_options_carry_the_sdk_user_agent():
    cfg = _FakeConfig(user_agent="databricks-sdk-py/9.9.9 python/3.12 os/linux auth/pat")
    # The gRPC channel advertises the same User-Agent the HTTP client sends.
    assert _channel_options(cfg) == [("grpc.primary_user_agent", cfg.user_agent)]


def test_open_channel_returns_secure_channel():
    grpc = pytest.importorskip("grpc")

    channel = open_channel(_FakeConfig(headers={"Authorization": "Bearer tok"}))
    try:
        assert isinstance(channel, grpc.Channel)
    finally:
        channel.close()
