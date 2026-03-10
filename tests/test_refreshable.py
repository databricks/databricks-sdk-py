from contextlib import contextmanager
from datetime import datetime, timedelta
from typing import Callable
from unittest.mock import patch

from databricks.sdk.oauth import Refreshable, Token, _TokenState


class _MockRefreshable(Refreshable):

    def __init__(
        self,
        disable_async,
        token=None,
        stale_duration=None,
        refresh_effect: Callable[[], Token] = None,
    ):
        super().__init__(token=token, disable_async=disable_async, stale_duration=stale_duration)
        self._refresh_effect = refresh_effect
        self._refresh_count = 0

    def refresh(self) -> Token:
        if self._refresh_effect:
            self._token = self._refresh_effect()
        self._refresh_count += 1
        return self._token


class _ManualExecutor:
    """Fake executor that queues callables for explicit, deterministic execution.

    Replaces the real thread pool so async-refresh tests need no threads,
    events, or sleeps: call .token() to queue the refresh, then run_all()
    to execute it on the test thread.
    """

    def __init__(self):
        self._pending: list = []
        self.submission_count: int = 0

    def submit(self, fn, *args, **kwargs):
        self.submission_count += 1
        self._pending.append((fn, args, kwargs))

    def run_all(self):
        while self._pending:
            fn, args, kwargs = self._pending.pop(0)
            fn(*args, **kwargs)


@contextmanager
def _manual_executor():
    executor = _ManualExecutor()
    with patch.object(Refreshable, '_get_executor', return_value=executor):
        yield executor


def fail() -> Token:
    raise Exception("Simulated token refresh failure")


def static_token(token: Token) -> Callable[[], Token]:
    def f() -> Token:
        return token

    return f


# --- disable_async tests (synchronous path, no executor involvement) ---


def test_disable_async_stale_does_not_refresh():
    stale_token = Token(
        access_token="access_token",
        expiry=datetime.now() + timedelta(seconds=50),
    )
    r = _MockRefreshable(token=stale_token, disable_async=True, refresh_effect=fail)
    result = r.token()
    assert r._refresh_count == 0
    assert result == stale_token


def test_disable_async_no_token_does_refresh():
    now = datetime.now()
    token = Token(
        access_token="access_token",
        expiry=now + timedelta(hours=1),
    )
    r = _MockRefreshable(token=None, disable_async=True, refresh_effect=static_token(token))
    result = r.token()
    assert r._refresh_count == 1
    assert result == token


def test_disable_async_no_expiration_does_not_refresh():
    non_expiring_token = Token(
        access_token="access_token",
    )
    r = _MockRefreshable(token=non_expiring_token, disable_async=True, refresh_effect=fail)
    result = r.token()
    assert r._refresh_count == 0
    assert result == non_expiring_token


def test_disable_async_fresh_does_not_refresh():
    now = datetime.now()
    token = Token(
        access_token="access_token",
        expiry=now + timedelta(hours=1),
    )
    r = _MockRefreshable(token=token, disable_async=True, refresh_effect=fail)
    result = r.token()
    assert r._refresh_count == 0
    assert result == token


def test_disable_async_expired_does_refresh():
    now = datetime.now()
    expired_token = Token(
        access_token="access_token",
        expiry=now - timedelta(minutes=5),
    )
    new_token = Token(
        access_token="access_token",
        expiry=now + timedelta(hours=1),
    )
    r = _MockRefreshable(
        token=expired_token,
        disable_async=True,
        refresh_effect=static_token(new_token),
    )
    result = r.token()
    assert r._refresh_count == 1
    assert result == new_token


# --- async-enabled tests ---


def test_expired_does_refresh():
    now = datetime.now()
    expired_token = Token(
        access_token="access_token",
        expiry=now - timedelta(minutes=5),
    )
    new_token = Token(
        access_token="access_token",
        expiry=now + timedelta(hours=1),
    )
    r = _MockRefreshable(
        token=expired_token,
        disable_async=False,
        refresh_effect=static_token(new_token),
    )
    result = r.token()
    assert r._refresh_count == 1
    assert result == new_token


def test_stale_does_refresh_async():
    stale_token = Token(
        access_token="access_token",
        expiry=datetime.now() + timedelta(seconds=50),
    )
    new_token = Token(
        access_token="access_token",
        expiry=datetime.now() + timedelta(seconds=300),
    )
    with _manual_executor() as executor:
        r = _MockRefreshable(
            token=stale_token,
            disable_async=False,
            stale_duration=timedelta(seconds=60),
            refresh_effect=static_token(new_token),
        )
        result = r.token()
        assert result == stale_token
        assert r._refresh_count == 0
        assert executor.submission_count == 1

        executor.run_all()

        result = r.token()
        assert result == new_token
        assert r._refresh_count == 1


def test_no_token_does_refresh():
    now = datetime.now()
    new_token = Token(
        access_token="access_token",
        expiry=now + timedelta(hours=1),
    )
    r = _MockRefreshable(
        token=None,
        disable_async=False,
        refresh_effect=static_token(new_token),
    )
    result = r.token()
    assert r._refresh_count == 1
    assert result == new_token


def test_fresh_does_not_refresh():
    now = datetime.now()
    fresh_token = Token(
        access_token="access_token",
        expiry=now + timedelta(hours=1),
    )
    r = _MockRefreshable(token=fresh_token, disable_async=False, refresh_effect=fail)
    result = r.token()
    assert r._refresh_count == 0
    assert result == fresh_token


def test_multiple_calls_dont_start_many_threads():
    stale_token = Token(
        access_token="access_token",
        expiry=datetime.now() + timedelta(seconds=59),
    )
    new_token = Token(
        access_token="access_token",
        expiry=datetime.now() + timedelta(seconds=300),
    )
    with _manual_executor() as executor:
        r = _MockRefreshable(
            token=stale_token,
            disable_async=False,
            stale_duration=timedelta(seconds=60),
            refresh_effect=static_token(new_token),
        )
        result = r.token()
        assert result == stale_token
        result = r.token()
        assert result == stale_token
        assert executor.submission_count == 1

        executor.run_all()

        result = r.token()
        assert r._refresh_count == 1
        assert result == new_token


def test_repeated_calls_during_async_failure_cooldown_do_not_refresh():
    now = datetime(2024, 1, 1, 12, 0, 0)
    stale_time = now + timedelta(minutes=41)

    stale_token = Token(
        access_token="access_token",
        expiry=now + timedelta(minutes=60),
    )
    new_token = Token(
        access_token="new_token",
        expiry=now + timedelta(minutes=120),
    )

    with _manual_executor() as executor, patch("databricks.sdk.oauth.datetime") as mock_dt:
        mock_dt.now.return_value = now
        r = _MockRefreshable(token=stale_token, disable_async=False, refresh_effect=fail)

        mock_dt.now.return_value = stale_time
        result = r.token()
        assert result == stale_token
        assert executor.submission_count == 1

        executor.run_all()
        assert r._stale_after is not None

        r._refresh_effect = static_token(new_token)
        mock_dt.now.return_value = r._stale_after - timedelta(seconds=1)

        assert r.token() == stale_token
        assert r.token() == stale_token
        assert r.token() == stale_token

        assert executor.submission_count == 1
        assert r._refresh_count == 0


def test_call_after_async_failure_cooldown_refreshes_token_async():
    now = datetime(2024, 1, 1, 12, 0, 0)
    stale_time = now + timedelta(minutes=41)

    stale_token = Token(
        access_token="access_token",
        expiry=now + timedelta(minutes=60),
    )
    new_token = Token(
        access_token="new_token",
        expiry=now + timedelta(minutes=120),
    )

    with _manual_executor() as executor, patch("databricks.sdk.oauth.datetime") as mock_dt:
        mock_dt.now.return_value = now
        r = _MockRefreshable(token=stale_token, disable_async=False, refresh_effect=fail)

        mock_dt.now.return_value = stale_time
        result = r.token()
        assert result == stale_token

        executor.run_all()
        assert r._stale_after is not None

        r._refresh_effect = static_token(new_token)
        mock_dt.now.return_value = r._stale_after + timedelta(seconds=1)

        result = r.token()
        assert result == stale_token
        assert executor.submission_count == 2
        assert r._refresh_count == 0

        executor.run_all()

        result = r.token()
        assert result == new_token
        assert r._refresh_count == 1


# --- Stale threshold computation tests ---


def test_stale_after_is_recomputed_after_blocking_refresh():
    """Verifies that `_stale_after` is recomputed from the refreshed token."""
    test_cases = [
        {
            "name": "recompute to a capped 20-minute stale period",
            "initial_token_ttl": timedelta(minutes=10),
            "refreshed_token_ttl": timedelta(minutes=60),
            "want_stale_after_offset": timedelta(minutes=40),  # 60min - min(30min, 20min)
        },
        {
            "name": "recompute to a proportional 5-minute stale period",
            "initial_token_ttl": timedelta(minutes=60),
            "refreshed_token_ttl": timedelta(minutes=10),
            "want_stale_after_offset": timedelta(minutes=5),  # 10min - min(5min, 20min)
        },
        {
            "name": "recompute to a proportional 45-second stale period",
            "initial_token_ttl": timedelta(minutes=60),
            "refreshed_token_ttl": timedelta(seconds=90),
            "want_stale_after_offset": timedelta(seconds=45),  # 90s - min(45s, 20min)
        },
    ]

    for tc in test_cases:
        now = datetime(2024, 1, 1, 12, 0, 0)
        refresh_time = now + tc["initial_token_ttl"] + timedelta(seconds=5)

        with patch("databricks.sdk.oauth.datetime") as mock_dt:
            mock_dt.now.return_value = now

            initial_token = Token(access_token="initial", expiry=now + tc["initial_token_ttl"])
            r = _MockRefreshable(token=initial_token, disable_async=False)

            fresh_after_expired = Token(
                access_token="after_expired_refresh",
                expiry=refresh_time + tc["refreshed_token_ttl"],
            )
            r._refresh_effect = static_token(fresh_after_expired)

            mock_dt.now.return_value = refresh_time
            result = r.token()
            assert (
                result.access_token == "after_expired_refresh"
            ), f'{tc["name"]}: expired refresh should return new token (blocking)'
            assert (
                r._refresh_count == 1
            ), f'{tc["name"]}: one blocking refresh for expired token, got {r._refresh_count}'
            assert (
                r._token_state() == _TokenState.FRESH
            ), f'{tc["name"]}: state should be FRESH after expired refresh, is {r._token_state()}'
            assert (
                r._stale_after == refresh_time + tc["want_stale_after_offset"]
            ), f'{tc["name"]}: _stale_after should be {refresh_time + tc["want_stale_after_offset"]}, is {r._stale_after}'


def test_stale_after_computation():
    """
    Verifies that `_stale_after` is computed correctly for both the dynamic
    and legacy stale-duration paths.
    """
    test_cases = [
        {
            "name": "standard OAuth token with 60-min TTL uses capped dynamic stale period",
            "token_ttl": timedelta(minutes=60),
            "want_stale_after_offset": timedelta(minutes=40),  # 60min - min(30min, 20min)
        },
        {
            "name": "FastPath token with 10-min TTL uses proportional dynamic stale period",
            "token_ttl": timedelta(minutes=10),
            "want_stale_after_offset": timedelta(minutes=5),  # 10min - min(5min, 20min)
        },
        {
            "name": "very short token with 90-seconds TTL uses proportional dynamic stale period",
            "token_ttl": timedelta(seconds=90),
            "want_stale_after_offset": timedelta(seconds=45),  # 90s - min(45s, 20min)
        },
        {
            "name": "legacy path honors a 5-minute stale duration",
            "token_ttl": timedelta(minutes=60),
            "stale_duration": timedelta(minutes=5),
            "want_stale_after_offset": timedelta(minutes=55),
        },
        {
            "name": "legacy path honors zero stale duration",
            "token_ttl": timedelta(minutes=10),
            "stale_duration": timedelta(seconds=0),
            "want_stale_after_offset": timedelta(minutes=10),
        },
    ]

    for tc in test_cases:
        now = datetime(2024, 1, 1, 12, 0, 0)

        with patch("databricks.sdk.oauth.datetime") as mock_dt:
            mock_dt.now.return_value = now

            initial_token = Token(access_token="initial", expiry=now + tc["token_ttl"])
            r = _MockRefreshable(
                token=initial_token,
                disable_async=False,
                stale_duration=tc.get("stale_duration"),
            )

            assert (
                r._stale_after == now + tc["want_stale_after_offset"]
            ), f'{tc["name"]}: _stale_after should be {now + tc["want_stale_after_offset"]}, is {r._stale_after}'
