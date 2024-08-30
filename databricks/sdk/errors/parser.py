import abc
import json
import logging
import re
from typing import Optional

import requests

from ..logger import RoundTripLogger
from .base import DatabricksError
from .mapper import error_mapper
from .private_link import (_get_private_link_validation_error,
                           _is_private_link_redirect)


class _ErrorParser(abc.ABC):
    """A parser for errors from the Databricks REST API."""

    @abc.abstractmethod
    def parse_error(self, response: requests.Response, response_body: bytes) -> Optional[dict]:
        """Parses an error from the Databricks REST API. If the error cannot be parsed, returns None."""


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
            error_args[
                'message'] = f"{scim_type} {error_args.get('message', 'SCIM API Internal Error')}".strip(" ")
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


# A list of ErrorParsers that are tried in order to parse an API error from a response body. Most errors should be
# parsable by the _StandardErrorParser, but additional parsers can be added here for specific error formats. The order
# of the parsers is not important, as the set of errors that can be parsed by each parser should be disjoint.
_error_parsers = [_StandardErrorParser(), _StringErrorParser(), _HtmlErrorParser(), ]


def _unknown_error(response: requests.Response) -> DatabricksError:
    request_log = RoundTripLogger(response, debug_headers=True, debug_truncate_bytes=10 * 1024).generate()
    return DatabricksError(
        'unable to parse response. This is likely a bug in the Databricks SDK for Python or the underlying '
        'API. Please report this issue with the following debugging information to the SDK issue tracker at '
        f'https://github.com/databricks/databricks-sdk-go/issues. Request log:```{request_log}```'
        '', )


def _get_api_error(response: requests.Response) -> Optional[DatabricksError]:
    """
    Handles responses from the REST API and returns a DatabricksError if the response indicates an error.
    :param response: The response from the REST API.
    :return: A DatabricksError if the response indicates an error, otherwise None.
    """
    if not response.ok:
        content = response.content
        if len(content) == 0:
            return DatabricksError(response.reason, status_code=response.status_code)
        for parser in _error_parsers:
            error_args = parser.parse_error(response, content)
            if error_args:
                return error_mapper(response, error_args)
        return _unknown_error(response)

    # Private link failures happen via a redirect to the login page. From a requests-perspective, the request
    # is successful, but the response is not what we expect. We need to handle this case separately.
    if _is_private_link_redirect(response):
        return _get_private_link_validation_error(response.url)
