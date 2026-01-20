from datetime import timedelta
from typing import Any, Literal, Optional, Tuple, Type

import pytest

from databricks.sdk.errors import NotFound, ResourceDoesNotExist
from databricks.sdk.retries import RetryError, poll, retried
from tests.clock import FakeClock


def test_match_retry_condition_on_no_qualifier():
    with pytest.raises(SyntaxError):

        @retried()
        def foo():
            return 1


def test_match_retry_condition_on_conflict():
    with pytest.raises(SyntaxError):

        @retried(on=[IOError], is_retryable=lambda _: "always", clock=FakeClock())
        def foo():
            return 1


def test_match_retry_always():
    with pytest.raises(TimeoutError):

        @retried(
            is_retryable=lambda _: "always",
            timeout=timedelta(seconds=1),
            clock=FakeClock(),
        )
        def foo():
            raise StopIteration()

        foo()


def test_match_on_errors():
    with pytest.raises(TimeoutError):

        @retried(
            on=[KeyError, AttributeError],
            timeout=timedelta(seconds=0.5),
            clock=FakeClock(),
        )
        def foo():
            raise KeyError(1)

        foo()


def test_match_on_subclass():
    with pytest.raises(TimeoutError):

        @retried(on=[NotFound], timeout=timedelta(seconds=0.5), clock=FakeClock())
        def foo():
            raise ResourceDoesNotExist(...)

        foo()


def test_propagates_outside_exception():
    with pytest.raises(KeyError):

        @retried(
            on=[AttributeError],
            timeout=timedelta(seconds=0.5),
            clock=FakeClock(),
        )
        def foo():
            raise KeyError(1)

        foo()


@pytest.mark.parametrize(
    "scenario,attempts,result_value,exception_type,exception_msg,timeout,min_time,max_time",
    [
        pytest.param(
            "success",
            1,
            "immediate",
            None,
            None,
            60,
            0.0,
            0.0,
            id="returns string immediately on first attempt with no sleep",
        ),
        pytest.param("success", 2, 42, None, None, 60, 1.05, 1.75, id="returns integer after 1 retry with ~1s backoff"),
        pytest.param(
            "success",
            3,
            {"key": "val"},
            None,
            None,
            60,
            3.10,
            4.50,
            id="returns dict after 2 retries with linear backoff (1s+2s)",
        ),
        pytest.param(
            "success",
            5,
            [1, 2],
            None,
            None,
            60,
            10.2,
            13.0,
            id="returns list after 4 retries with linear backoff (1s+2s+3s+4s)",
        ),
        pytest.param(
            "success",
            1,
            None,
            None,
            None,
            60,
            0.0,
            0.0,
            id="returns None as valid result immediately (None is acceptable)",
        ),
        pytest.param(
            "success", 5, "ok", None, None, 200, 10.2, 13.0, id="verifies linear backoff increase over 4 retries"
        ),
        pytest.param(
            "success",
            11,
            "ok",
            None,
            None,
            200,
            55.5,
            62.5,
            id="verifies linear backoff approaching 10s cap over 10 retries",
        ),
        pytest.param(
            "success", 15, "ok", None, None, 200, 95.7, 105.5, id="verifies backoff is capped at 10s after 10th retry"
        ),
        pytest.param(
            "timeout",
            None,
            None,
            TimeoutError,
            "Timed out after",
            1,
            1,
            None,
            id="raises TimeoutError after 1 second of continuous retries",
        ),
        pytest.param(
            "timeout",
            None,
            None,
            TimeoutError,
            "Timed out after",
            5,
            5,
            None,
            id="raises TimeoutError after 5 seconds of continuous retries",
        ),
        pytest.param(
            "timeout",
            None,
            None,
            TimeoutError,
            "Timed out after",
            15,
            15,
            None,
            id="raises TimeoutError after 15 seconds of continuous retries",
        ),
        pytest.param(
            "halt",
            1,
            None,
            ValueError,
            "halt error",
            60,
            None,
            None,
            id="raises ValueError immediately when halt error on first attempt",
        ),
        pytest.param(
            "halt",
            2,
            None,
            ValueError,
            "halt error",
            60,
            None,
            None,
            id="raises ValueError after 1 retry when halt error on second attempt",
        ),
        pytest.param(
            "halt",
            3,
            None,
            ValueError,
            "halt error",
            60,
            None,
            None,
            id="raises ValueError after 2 retries when halt error on third attempt",
        ),
        pytest.param(
            "unexpected",
            1,
            None,
            RuntimeError,
            "unexpected",
            60,
            None,
            None,
            id="raises RuntimeError immediately on unexpected exception",
        ),
        pytest.param(
            "unexpected",
            3,
            None,
            RuntimeError,
            "unexpected",
            60,
            None,
            None,
            id="raises RuntimeError after 2 retries on unexpected exception",
        ),
    ],
)
def test_poll_behavior(
    scenario: Literal["success", "timeout", "halt", "unexpected"],
    attempts: Optional[int],
    result_value: Any,
    exception_type: Optional[Type[Exception]],
    exception_msg: Optional[str],
    timeout: int,
    min_time: Optional[float],
    max_time: Optional[float],
) -> None:
    """
    Comprehensive test for poll function covering all scenarios:
    - Success cases with various return types and retry counts
    - Backoff timing behavior (linear increase, 10s cap)
    - Timeout behavior
    - Halting errors
    - Unexpected exceptions
    """
    clock: FakeClock = FakeClock()
    call_count: int = 0

    def fn() -> Tuple[Any, Optional[RetryError]]:
        nonlocal call_count
        call_count += 1

        if scenario == "success":
            if call_count < attempts:
                return None, RetryError.continues(f"attempt {call_count}")
            return result_value, None

        elif scenario == "timeout":
            return None, RetryError.continues("retrying")

        elif scenario == "halt":
            if call_count < attempts:
                return None, RetryError.continues("retrying")
            return None, RetryError.halt(ValueError(exception_msg))

        elif scenario == "unexpected":
            if call_count < attempts:
                return None, RetryError.continues("retrying")
            raise RuntimeError(exception_msg)

    if scenario == "success":
        result: Any = poll(fn, timeout=timedelta(seconds=timeout), clock=clock)
        assert result == result_value
        assert call_count == attempts
        if min_time is not None:
            assert clock.time() >= min_time
        if max_time is not None:
            assert clock.time() <= max_time
    else:
        with pytest.raises(exception_type) as exc_info:
            poll(fn, timeout=timedelta(seconds=timeout), clock=clock)

        assert exception_msg in str(exc_info.value)
        assert call_count >= 1

        if scenario == "timeout":
            assert clock.time() >= min_time
        elif scenario in ("halt", "unexpected"):
            assert call_count == attempts


def test_max_attempts_respected():
    """Test that max_attempts parameter is respected and stops retrying after the limit."""
    clock = FakeClock()
    call_count = 0

    @retried(
        is_retryable=lambda _: "always retry",
        timeout=timedelta(seconds=60),  # High timeout, should hit max_attempts first
        max_attempts=3,
        clock=clock,
    )
    def failing_function():
        nonlocal call_count
        call_count += 1
        raise ValueError("test error")

    with pytest.raises(TimeoutError) as exc_info:
        failing_function()

    # Should have attempted 3 times (initial + 2 retries)
    assert call_count == 3
    # Error message should indicate max attempts exceeded
    assert "Exceeded max retry attempts (3)" in str(exc_info.value)


def test_timeout_exceeded_before_max_attempts():
    """Test that timeout is respected even when max_attempts is not reached."""
    clock = FakeClock()
    call_count = 0

    @retried(
        is_retryable=lambda _: "always retry",
        timeout=timedelta(seconds=2),  # Short timeout
        max_attempts=100,  # High max attempts
        clock=clock,
    )
    def failing_function():
        nonlocal call_count
        call_count += 1
        raise ValueError("test error")

    with pytest.raises(TimeoutError) as exc_info:
        failing_function()

    # Should timeout before reaching 100 attempts
    assert call_count < 100
    # Error message should indicate timeout (not max attempts)
    assert "Timed out after" in str(exc_info.value)
    assert "Exceeded max retry attempts" not in str(exc_info.value)


def test_successful_retry_within_max_attempts():
    """Test that function succeeds when it recovers before max_attempts is hit."""
    clock = FakeClock()
    call_count = 0

    @retried(
        is_retryable=lambda _: "always retry",
        timeout=timedelta(seconds=60),
        max_attempts=5,
        clock=clock,
    )
    def eventually_succeeds():
        nonlocal call_count
        call_count += 1
        if call_count < 3:
            raise ValueError("not yet")
        return "success"

    result = eventually_succeeds()
    assert result == "success"
    assert call_count == 3


def test_max_attempts_none_preserves_backward_compatibility():
    """Test that max_attempts=None only uses timeout (backward compatibility)."""
    clock = FakeClock()
    call_count = 0

    @retried(
        is_retryable=lambda _: "always retry",
        timeout=timedelta(seconds=3),
        max_attempts=None,  # No attempt limit
        clock=clock,
    )
    def failing_function():
        nonlocal call_count
        call_count += 1
        raise ValueError("test error")

    with pytest.raises(TimeoutError) as exc_info:
        failing_function()

    # Should have made multiple attempts based on timeout
    assert call_count > 1
    # Error message should indicate timeout
    assert "Timed out after" in str(exc_info.value)


def test_max_attempts_with_non_retryable_error():
    """Test that non-retryable errors are raised immediately regardless of max_attempts."""
    clock = FakeClock()
    call_count = 0

    @retried(
        on=[ValueError],
        timeout=timedelta(seconds=60),
        max_attempts=5,
        clock=clock,
    )
    def raises_non_retryable():
        nonlocal call_count
        call_count += 1
        raise KeyError("not retryable")

    with pytest.raises(KeyError):
        raises_non_retryable()

    # Should only attempt once since error is not retryable
    assert call_count == 1
