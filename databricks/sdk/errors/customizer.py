import abc
import logging
from typing import Optional

import requests


class _ErrorCustomizer(abc.ABC):
    """A customizer for errors from the Databricks REST API."""

    @abc.abstractmethod
    def customize_error(self, response: requests.Response, kwargs: dict):
        """Customize the error constructor parameters."""


class _RetryAfterCustomizer(_ErrorCustomizer):
    _RETRY_AFTER_DEFAULT = 1

    @classmethod
    def _parse_retry_after(cls, response: requests.Response) -> Optional[int]:
        retry_after = response.headers.get("Retry-After")
        if retry_after is None:
            logging.debug(
                f'No Retry-After header received in response with status code 429 or 503. Defaulting to {cls._RETRY_AFTER_DEFAULT}'
            )
            # 429 requests should include a `Retry-After` header, but if it's missing,
            # we default to 1 second.
            return cls._RETRY_AFTER_DEFAULT
        # If the request is throttled, try parse the `Retry-After` header and sleep
        # for the specified number of seconds. Note that this header can contain either
        # an integer or a RFC1123 datetime string.
        # See https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Retry-After
        #
        # For simplicity, we only try to parse it as an integer, as this is what Databricks
        # platform returns. Otherwise, we fall back and don't sleep.
        try:
            return int(retry_after)
        except ValueError:
            logging.debug(
                f'Invalid Retry-After header received: {retry_after}. Defaulting to {cls._RETRY_AFTER_DEFAULT}'
            )
            # defaulting to 1 sleep second to make self._is_retryable() simpler
            return cls._RETRY_AFTER_DEFAULT

    def customize_error(self, response: requests.Response, kwargs: dict):
        status_code = response.status_code
        is_too_many_requests_or_unavailable = status_code in (429, 503)
        if is_too_many_requests_or_unavailable:
            kwargs['retry_after_secs'] = self._parse_retry_after(response)
