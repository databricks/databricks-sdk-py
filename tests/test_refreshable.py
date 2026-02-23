import time
from datetime import datetime, timedelta
from time import sleep
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
        super().__init__(token, disable_async)
        # Optional override: bypasses the dynamic min(TTL×0.5, max) formula so
        # tests can put a token directly into STALE state at construction time.
        if stale_duration is not None:
            self._stale_duration = stale_duration
        self._refresh_effect = refresh_effect
        self._refresh_count = 0

    def refresh(self) -> Token:
        if self._refresh_effect:
            self._token = self._refresh_effect()
        self._refresh_count += 1
        return self._token


def fail() -> Token:
    raise Exception("Simulated token refresh failure")


def static_token(token: Token, wait: int = 0) -> Callable[[], Token]:

    def f() -> Token:
        time.sleep(wait)
        return token

    return f


def blocking_refresh(
    token: Token,
) -> (Callable[[], Token], Callable[[], None]):
    """
    Create a refresh function that blocks until unblock is called.

    Param:
     token: the token that will be returned

    Returns:
        A tuple containing the refresh function and the unblock function.

    """
    blocking = True

    def refresh():
        while blocking:
            sleep(0.1)
        return token

    def unblock():
        nonlocal blocking
        blocking = False

    return refresh, unblock


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
    token = Token(
        access_token="access_token",
        expiry=datetime.now() + timedelta(seconds=50),
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
    # Create a token that is already stale. If async is disabled, the token should not be refreshed.
    token = Token(
        access_token="access_token",
        expiry=datetime.now() + timedelta(seconds=300),
    )
    r = _MockRefreshable(token=token, disable_async=True, refresh_effect=fail)
    result = r.token()
    assert r._refresh_count == 0
    assert result == token


def test_disable_async_expired_does_refresh():
    expired_token = Token(
        access_token="access_token",
        expiry=datetime.now() - timedelta(seconds=300),
    )
    new_token = Token(
        access_token="access_token",
        expiry=datetime.now() + timedelta(seconds=300),
    )
    # Add one second to the refresh time to ensure that the call is blocking.
    # If the call is not blocking, the wait time will ensure that the
    # old token is returned.
    r = _MockRefreshable(
        token=expired_token,
        disable_async=True,
        refresh_effect=static_token(new_token, wait=1),
    )
    result = r.token()
    assert r._refresh_count == 1
    assert result == new_token


def test_expired_does_refresh():
    expired_token = Token(
        access_token="access_token",
        expiry=datetime.now() - timedelta(seconds=300),
    )
    new_token = Token(
        access_token="access_token",
        expiry=datetime.now() + timedelta(seconds=300),
    )
    # Add one second to the refresh time to ensure that the call is blocking.
    # If the call is not blocking, the wait time will ensure that the
    # old token is returned.
    r = _MockRefreshable(
        token=expired_token,
        disable_async=False,
        refresh_effect=static_token(new_token, wait=1),
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
    # Add one second to the refresh to avoid race conditions.
    # Without it, the new token may be returned in some cases.
    refresh, unblock = blocking_refresh(new_token)
    r = _MockRefreshable(
        token=stale_token, disable_async=False, stale_duration=timedelta(seconds=60), refresh_effect=refresh
    )
    result = r.token()
    # NOTE: Do not check for refresh count here, since the
    assert result == stale_token
    assert r._refresh_count == 0
    # Unblock the refresh and wait
    unblock()
    time.sleep(2)
    # Call again and check that you get the new token
    result = r.token()
    assert result == new_token
    # Ensure that all calls have completed
    time.sleep(0.1)
    assert r._refresh_count == 1


def test_no_token_does_refresh():
    new_token = Token(
        access_token="access_token",
        expiry=datetime.now() + timedelta(seconds=300),
    )
    # Add one second to the refresh time to ensure that the call is blocking.
    # If the call is not blocking, the wait time will ensure that the
    # token is not returned.
    r = _MockRefreshable(
        token=None,
        disable_async=False,
        refresh_effect=static_token(new_token, wait=1),
    )
    result = r.token()
    assert r._refresh_count == 1
    assert result == new_token


def test_fresh_does_not_refresh():
    fresh_token = Token(
        access_token="access_token",
        expiry=datetime.now() + timedelta(seconds=300),
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
    refresh, unblock = blocking_refresh(new_token)
    r = _MockRefreshable(
        token=stale_token, disable_async=False, stale_duration=timedelta(seconds=60), refresh_effect=refresh
    )
    # Call twice. The second call should not start a new thread.
    result = r.token()
    assert result == stale_token
    result = r.token()
    assert result == stale_token
    unblock()
    # Wait for the refresh to complete
    time.sleep(1)
    result = r.token()
    # Check that only one refresh was called
    assert r._refresh_count == 1
    assert result == new_token


def test_async_failure_disables_async():
    stale_token = Token(
        access_token="access_token",
        expiry=datetime.now() + timedelta(seconds=59),
    )
    new_token = Token(
        access_token="new_token",
        expiry=datetime.now() + timedelta(seconds=300),
    )
    r = _MockRefreshable(
        token=stale_token, disable_async=False, stale_duration=timedelta(seconds=60), refresh_effect=fail
    )
    # The call should fail and disable async refresh,
    # but the exception will be catch inside the tread.
    result = r.token()
    assert result == stale_token
    # Give time to the async refresh to fail
    time.sleep(1)
    assert r._refresh_err
    # Now, the refresh should be blocking.
    # Blocking refresh only happens for expired, not stale.
    # Therefore, the next call should return the stale token.
    r._refresh_effect = static_token(new_token, wait=1)
    result = r.token()
    assert result == stale_token
    # Wait to be sure no async thread was started
    time.sleep(1)
    assert r._refresh_count == 0

    # Inject an expired token.
    expired_token = Token(
        access_token="access_token",
        expiry=datetime.now() - timedelta(seconds=300),
    )
    r._token = expired_token

    # This should be blocking and return the new token.
    result = r.token()
    assert r._refresh_count == 1
    assert result == new_token
    # The refresh error should be cleared.
    assert not r._refresh_err


def test_dynamic_stale_period():
    """
    For each token type, verifies:
    - Stale tokens trigger async refresh (returns old token immediately)
    - Expired tokens trigger blocking refresh (blocks and returns new token)
    """
    test_cases = [
        {
            "name": "standard OAuth token with 60-min TTL",
            "token_ttl": timedelta(minutes=60),
            "want_stale_duration": timedelta(minutes=20),  # min(30min, 20min) = 20min (capped)
            "advance_time_for_stale": timedelta(minutes=41),  # 19min remaining < 20min stale period
        },
        {
            "name": "FastPath token with 10-min TTL",
            "token_ttl": timedelta(minutes=10),
            "want_stale_duration": timedelta(minutes=5),  # min(5min, 20min) = 5min (not capped)
            "advance_time_for_stale": timedelta(minutes=6),  # 4min remaining < 5min stale period
        },
        {
            "name": "very short token with 90-seconds TTL",
            "token_ttl": timedelta(seconds=90),
            "want_stale_duration": timedelta(seconds=45),  # min(90s, 20min) = 45s (not capped)
            "advance_time_for_stale": timedelta(seconds=46),  # 44s remaining < 45s stale period
        },
    ]

    for tc in test_cases:
        now = datetime(2024, 1, 1, 12, 0, 0)

        with patch("databricks.sdk.oauth.datetime") as mock_dt:
            mock_dt.now.return_value = now

            initial_token = Token(access_token="initial", expiry=now + tc["token_ttl"])

            stale_refresh_token = Token(
                access_token="after_stale_refresh",
                expiry=now + tc["token_ttl"] + tc["token_ttl"],
            )
            refresh_fn, unblock = blocking_refresh(stale_refresh_token)
            r = _MockRefreshable(token=initial_token, disable_async=False, refresh_effect=refresh_fn)

            assert r._stale_duration == tc["want_stale_duration"]
            assert (
                r._token_state() == _TokenState.FRESH
            ), f'{tc["name"]}: initial state should be FRESH, is {r._token_state()}'

            # --- STALE: async refresh returns old token immediately ---
            mock_dt.now.return_value = now + tc["advance_time_for_stale"]
            assert r._token_state() == _TokenState.STALE, f'{tc["name"]}: state should be STALE, is {r._token_state()}'

            result = r.token()
            assert result.access_token == "initial", f'{tc["name"]}: stale refresh should return old token (async)'

            unblock()
            time.sleep(1)

            result = r.token()
            assert (
                result.access_token == "after_stale_refresh"
            ), f'{tc["name"]}: after async refresh should return new token'
            assert r._refresh_count == 1, f'{tc["name"]}: one refresh after stale, got {r._refresh_count}'

            # --- EXPIRED: blocking refresh returns new token ---
            expired_time = now + tc["token_ttl"] + tc["token_ttl"] + timedelta(seconds=5)
            mock_dt.now.return_value = expired_time
            assert (
                r._token_state() == _TokenState.EXPIRED
            ), f'{tc["name"]}: state should be EXPIRED, is {r._token_state()}'

            fresh_after_expired = Token(
                access_token="after_expired_refresh",
                expiry=expired_time + tc["token_ttl"],
            )
            r._refresh_effect = static_token(fresh_after_expired, wait=1)

            result = r.token()
            assert (
                result.access_token == "after_expired_refresh"
            ), f'{tc["name"]}: expired refresh should return new token (blocking)'
            assert (
                r._refresh_count == 2
            ), f'{tc["name"]}: two refreshes total (one stale + one expired), got {r._refresh_count}'
            assert (
                r._token_state() == _TokenState.FRESH
            ), f'{tc["name"]}: state should be FRESH after expired refresh, is {r._token_state()}'
