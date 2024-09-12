import abc
import functools
import json
import logging
import re
from typing import Optional, List

import requests

from ..logger import RoundTrip
from .base import DatabricksError
from .mapper import _error_mapper
from .private_link import (_get_private_link_validation_error,
                           _is_private_link_redirect)


class _ErrorParser(abc.ABC):
    """A parser for errors from the Databricks REST API."""

    @abc.abstractmethod
    def parse_error(self, response: requests.Response, response_body: bytes) -> Optional[dict]:
        """Parses an error from the Databricks REST API. If the error cannot be parsed, returns None."""


class _ErrorCustomizer(abc.ABC):
    """A customizer for errors from the Databricks REST API."""

    @abc.abstractmethod
    def customize_error(self, response: requests.Response, kwargs: dict):
        """Customize the error constructor parameters."""

class _EmptyParser(_ErrorParser):
    """A parser that handles empty responses."""

    def parse_error(self, response: requests.Response, response_body: bytes) -> Optional[dict]:
        if len(response_body) == 0:
            return {'message': response.reason}
        return None


class _StandardErrorParser(_ErrorParser):
    """
    Parses errors from the Databricks REST API using the standard error format.
    """

    def parse_error(self, response: requests.Response, response_body: bytes) -> Optional[dict]:
        try:
            payload_str = response_body.decode('utf-8')
            resp: dict = json.loads(payload_str)
        except json.JSONDecodeError as e:
            logging.debug('_StandardErrorParser: unable to deserialize response as json', exc_info=e)
            return None

        error_args = {
            'message': resp.get('message', 'request failed'),
            'error_code': resp.get('error_code'),
            'details': resp.get('details'),
        }

        # Handle API 1.2-style errors
        if 'error' in resp:
            error_args['message'] = resp['error']

        # Handle SCIM Errors
        detail = resp.get('detail')
        status = resp.get('status')
        scim_type = resp.get('scimType')
        if detail:
            # Handle SCIM error message details
            # @see https://tools.ietf.org/html/rfc7644#section-3.7.3
            if detail == "null":
                detail = "SCIM API Internal Error"
            error_args['message'] = f"{scim_type} {detail}".strip(" ")
            error_args['error_code'] = f"SCIM_{status}"
        return error_args


class _StringErrorParser(_ErrorParser):
    """
    Parses errors from the Databricks REST API in the format "ERROR_CODE: MESSAGE".
    """

    __STRING_ERROR_REGEX = re.compile(r'([A-Z_]+): (.*)')

    def parse_error(self, response: requests.Response, response_body: bytes) -> Optional[dict]:
        payload_str = response_body.decode('utf-8')
        match = self.__STRING_ERROR_REGEX.match(payload_str)
        if not match:
            logging.debug('_StringErrorParser: unable to parse response as string')
            return None
        error_code, message = match.groups()
        return {'error_code': error_code, 'message': message, 'status': response.status_code, }


class _HtmlErrorParser(_ErrorParser):
    """
    Parses errors from the Databricks REST API in HTML format.
    """

    __HTML_ERROR_REGEXES = [re.compile(r'<pre>(.*)</pre>'), re.compile(r'<title>(.*)</title>'), ]

    def parse_error(self, response: requests.Response, response_body: bytes) -> Optional[dict]:
        payload_str = response_body.decode('utf-8')
        for regex in self.__HTML_ERROR_REGEXES:
            match = regex.search(payload_str)
            if match:
                message = match.group(1) if match.group(1) else response.reason
                return {
                    'status': response.status_code,
                    'message': message,
                    'error_code': response.reason.upper().replace(' ', '_')
                }
        logging.debug('_HtmlErrorParser: no <pre> tag found in error response')
        return None


class _RetryAfterCustomizer(_ErrorCustomizer):
    _RETRY_AFTER_DEFAULT = 1

    @classmethod
    def _parse_retry_after(cls, response: requests.Response) -> Optional[int]:
        retry_after = response.headers.get("Retry-After")
        if retry_after is None:
            logging.debug(f'No Retry-After header received in response with status code 429 or 503. Defaulting to {cls._RETRY_AFTER_DEFAULT}')
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
            logging.debug(f'Invalid Retry-After header received: {retry_after}. Defaulting to {cls._RETRY_AFTER_DEFAULT}')
            # defaulting to 1 sleep second to make self._is_retryable() simpler
            return cls._RETRY_AFTER_DEFAULT

    def customize_error(self, response: requests.Response, kwargs: dict):
        status_code = response.status_code
        is_too_many_requests_or_unavailable = status_code in (429, 503)
        if is_too_many_requests_or_unavailable:
            kwargs['retry_after_secs'] = self._parse_retry_after(response)


# A list of ErrorParsers that are tried in order to parse an API error from a response body. Most errors should be
# parsable by the _StandardErrorParser, but additional parsers can be added here for specific error formats. The order
# of the parsers is not important, as the set of errors that can be parsed by each parser should be disjoint.
_error_parsers = [_EmptyParser(), _StandardErrorParser(), _StringErrorParser(), _HtmlErrorParser(), ]
_error_customizers = [_RetryAfterCustomizer(), ]


def _unknown_error(response: requests.Response) -> str:
    """A standard error message that can be shown when an API response cannot be parsed.

    This error message includes a link to the issue tracker for the SDK for users to report the issue to us.
    """
    request_log = RoundTrip(response, debug_headers=True, debug_truncate_bytes=10 * 1024).generate()
    return (
        'This is likely a bug in the Databricks SDK for Python or the underlying '
        'API. Please report this issue with the following debugging information to the SDK issue tracker at '
        f'https://github.com/databricks/databricks-sdk-go/issues. Request log:```{request_log}```')


class _Parser:
    def __init__(self,
                 extra_error_parsers: Optional[List[_ErrorParser]] = None,
                 extra_error_customizers: Optional[List[_ErrorCustomizer]] = None):
        self._error_parsers = _error_parsers + extra_error_parsers
        self._error_customizers = _error_customizers + extra_error_customizers

    def get_api_error(self, response: requests.Response) -> Optional[DatabricksError]:
        """
        Handles responses from the REST API and returns a DatabricksError if the response indicates an error.
        :param response: The response from the REST API.
        :return: A DatabricksError if the response indicates an error, otherwise None.
        """
        if not response.ok:
            content = response.content
            for parser in self._error_parsers:
                try:
                    error_args = parser.parse_error(response, content)
                    if error_args:
                        for customizer in self._error_customizers:
                            customizer.customize_error(response, error_args)
                        return _error_mapper(response, error_args)
                except Exception as e:
                    logging.debug(f'Error parsing response with {parser}, continuing', exc_info=e)
            return _error_mapper(response, {'message': 'unable to parse response. ' + _unknown_error(response)})

        # Private link failures happen via a redirect to the login page. From a requests-perspective, the request
        # is successful, but the response is not what we expect. We need to handle this case separately.
        if _is_private_link_redirect(response):
            return _get_private_link_validation_error(response.url)
