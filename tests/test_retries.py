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


@pytest.mark.parametrize(
    "timeout_seconds,max_attempts,fail_count,expected_error,expected_min_calls,expected_max_calls,expected_msg",
    [
        pytest.param(
            60,
            3,
            None,
            RuntimeError,
            3,
            3,
            "Exceeded max retry attempts (3)",
            id="max_attempts_respected",
        ),
        pytest.param(
            5,
            100,
            None,
            TimeoutError,
            1,
            99,
            "Timed out after",
            id="timeout_exceeded_before_max_attempts",
        ),
        pytest.param(
            60,
            5,
            2,
            None,
            3,
            3,
            None,
            id="successful_retry_within_max_attempts",
        ),
        pytest.param(
            3,
            None,
            None,
            TimeoutError,
            2,
            None,
            "Timed out after",
            id="max_attempts_none",
        ),
    ],
)
def test_max_attempts_behavior(
    timeout_seconds, max_attempts, fail_count, expected_error, expected_min_calls, expected_max_calls, expected_msg
):
    """Test max_attempts parameter behavior with various configurations."""
    clock = FakeClock()
    call_count = 0

    @retried(
        is_retryable=lambda _: "always retry",
        timeout=timedelta(seconds=timeout_seconds),
        max_attempts=max_attempts,
        clock=clock,
    )
    def test_function():
        nonlocal call_count
        call_count += 1
        if fail_count is None or call_count <= fail_count:
            raise ValueError("test error")
        return "success"

    if expected_error:
        with pytest.raises(expected_error) as exc_info:
            test_function()
        if expected_msg:
            assert expected_msg in str(exc_info.value)
    else:
        result = test_function()
        assert result == "success"

    assert call_count >= expected_min_calls
    if expected_max_calls:
        assert call_count <= expected_max_calls


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

    # Should only attempt once since error is not retryable.
    assert call_count == 1
