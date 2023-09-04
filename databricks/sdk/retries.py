import functools
import logging
import time
from datetime import timedelta
from random import random
from typing import Callable, List, Optional, Type

logger = logging.getLogger('databricks.sdk')


def retried(*,
            on: List[Type[BaseException]] = None,
            is_retryable: Callable[[BaseException], Optional[str]] = None,
            timeout=timedelta(minutes=20)):
    has_allowlist = on is not None
    has_callback = is_retryable is not None
    if not (has_allowlist or has_callback) or (has_allowlist and has_callback):
        raise SyntaxError('either on=[Exception] or callback=lambda x: .. is required')

    def decorator(func):

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            deadline = time.time() + timeout.total_seconds()
            attempt = 1
            last_err = None
            while time.time() < deadline:
                try:
                    return func(*args, **kwargs)
                except Exception as err:
                    last_err = err
                    retry_reason = None
                    if is_retryable is not None:
                        retry_reason = is_retryable(err)
                    elif type(err) in on:
                        retry_reason = f'{type(err).__name__} is allowed to retry'

                    if retry_reason is None:
                        # raise if exception is not retryable
                        raise err

                    # sleep 10s max per attempt
                    sleep = min(10, attempt)
                    logger.debug(f'Retrying: {retry_reason} (sleeping ~{sleep}s)')
                    time.sleep(sleep + random())
                    attempt += 1
            raise TimeoutError(f'Timed out after {timeout}') from last_err

        return wrapper

    return decorator
