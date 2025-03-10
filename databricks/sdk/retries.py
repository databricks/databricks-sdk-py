import functools
import logging
from datetime import timedelta
from random import random
from typing import Callable, Optional, Sequence, Type

from .clock import Clock, RealClock

logger = logging.getLogger(__name__)


def retried(
    *,
    on: Optional[Sequence[Type[BaseException]]] = None,
    is_retryable: Optional[Callable[[BaseException], Optional[str]]] = None,
    timeout=timedelta(minutes=20),
    clock: Optional[Clock] = None,
    before_retry: Optional[Callable] = None,
):
    has_allowlist = on is not None
    has_callback = is_retryable is not None
    if not (has_allowlist or has_callback) or (has_allowlist and has_callback):
        raise SyntaxError("either on=[Exception] or callback=lambda x: .. is required")
    if clock is None:
        clock = RealClock()

    def decorator(func):

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            deadline = clock.time() + timeout.total_seconds()
            attempt = 1
            last_err = None
            while clock.time() < deadline:
                try:
                    return func(*args, **kwargs)
                except Exception as err:
                    last_err = err
                    retry_reason = None
                    # sleep 10s max per attempt, unless it's HTTP 429 or 503
                    sleep = min(10, attempt)
                    retry_after_secs = getattr(err, "retry_after_secs", None)
                    if retry_after_secs is not None:
                        # cannot depend on DatabricksError directly because of circular dependency
                        sleep = retry_after_secs
                        retry_reason = "throttled by platform"
                    elif is_retryable is not None:
                        retry_reason = is_retryable(err)
                    elif on is not None:
                        for err_type in on:
                            if not isinstance(err, err_type):
                                continue
                            retry_reason = f"{type(err).__name__} is allowed to retry"

                    if retry_reason is None:
                        # raise if exception is not retryable
                        raise err

                    logger.debug(f"Retrying: {retry_reason} (sleeping ~{sleep}s)")
                    if before_retry:
                        before_retry()

                    clock.sleep(sleep + random())
                    attempt += 1
            raise TimeoutError(f"Timed out after {timeout}") from last_err

        return wrapper

    return decorator
