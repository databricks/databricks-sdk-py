import abc
import json
import logging
import re
import requests
import warnings
from dataclasses import dataclass
from typing import Dict, List, Optional

from ..logger import RoundTripLogger

from .mapper import error_mapper
from .private_link import _get_private_link_validation_error, _is_private_link_redirect


class ErrorDetail:

    def __init__(self,
                 type: str = None,
                 reason: str = None,
                 domain: str = None,
                 metadata: dict = None,
                 **kwargs):
        self.type = type
        self.reason = reason
        self.domain = domain
        self.metadata = metadata

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ErrorDetail':
        if '@type' in d:
            d['type'] = d['@type']
        return cls(**d)


class DatabricksError(IOError):
    """ Generic error from Databricks REST API """
    # Known ErrorDetail types
    _error_info_type = "type.googleapis.com/google.rpc.ErrorInfo"

    def __init__(self,
                 message: str = None,
                 *,
                 error_code: str = None,
                 detail: str = None,
                 status: str = None,
                 scimType: str = None,
                 error: str = None,
                 retry_after_secs: int = None,
                 details: List[Dict[str, any]] = None,
                 **kwargs):
        """

        :param message:
        :param error_code:
        :param detail: [Deprecated]
        :param status: [Deprecated]
        :param scimType: [Deprecated]
        :param error: [Deprecated]
        :param retry_after_secs:
        :param details:
        :param kwargs:
        """
        # SCIM-specific parameters are deprecated
        if detail:
            warnings.warn("The 'detail' parameter of DatabricksError is deprecated and will be removed in a future version.")
        if scimType:
            warnings.warn("The 'scimType' parameter of DatabricksError is deprecated and will be removed in a future version.")
        if status:
            warnings.warn("The 'status' parameter of DatabricksError is deprecated and will be removed in a future version.")

        # API 1.2-specific parameters are deprecated
        if error:
            warnings.warn("The 'error' parameter of DatabricksError is deprecated and will be removed in a future version.")

        if detail:
            # Handle SCIM error message details
            # @see https://tools.ietf.org/html/rfc7644#section-3.7.3
            if detail == "null":
                message = "SCIM API Internal Error"
            else:
                message = detail
            # add more context from SCIM responses
            message = f"{scimType} {message}".strip(" ")
            error_code = f"SCIM_{status}"
        super().__init__(message if message else error)
        self.error_code = error_code
        self.retry_after_secs = retry_after_secs
        self.details = [ErrorDetail.from_dict(detail) for detail in details] if details else []
        self.kwargs = kwargs

    def get_error_info(self) -> List[ErrorDetail]:
        return self._get_details_by_type(DatabricksError._error_info_type)

    def _get_details_by_type(self, error_type) -> List[ErrorDetail]:
        if self.details == None:
            return []
        return [detail for detail in self.details if detail.type == error_type]


@dataclass
class _ErrorOverride:
    # The name of the override. Used for logging purposes.
    debug_name: str

    # A regex that must match the path of the request for this override to be applied.
    path_regex: re.Pattern

    # The HTTP method of the request for the override to apply
    verb: str

    # The custom error class to use for this override.
    custom_error: type

    # A regular expression that must match the error code for this override to be applied. If None,
    # this field is ignored.
    status_code_matcher: Optional[re.Pattern] = None

    # A regular expression that must match the error code for this override to be applied. If None,
    # this field is ignored.
    error_code_matcher: Optional[re.Pattern] = None

    # A regular expression that must match the message for this override to be applied. If None,
    # this field is ignored.
    message_matcher: Optional[re.Pattern] = None

    def matches(self, response: requests.Response, raw_error: dict):
        if response.request.method != self.verb:
            return False
        if not self.path_regex.match(response.request.path_url):
            return False
        if self.status_code_matcher and not self.status_code_matcher.match(str(response.status_code)):
            return False
        if self.error_code_matcher and not self.error_code_matcher.match(raw_error.get('error_code', '')):
            return False
        if self.message_matcher and not self.message_matcher.match(raw_error.get('message', '')):
            return False
        return True


class _ErrorParser(abc.ABC):
    """A parser for errors from the Databricks REST API."""
    @abc.abstractmethod
    def parse_error(self, response: requests.Response, response_body: bytes) -> Optional[dict]:
        """Parses an error from the Databricks REST API. If the error cannot be parsed, returns None."""
        pass


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
            error_args['message'] = f"{scim_type} {error_args.get('message', 'SCIM API Internal Error')}".strip(" ")
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
        return {
            'error_code': error_code,
            'message': message,
            'status': response.status_code,
        }


class _HtmlErrorParser(_ErrorParser):
    """
    Parses errors from the Databricks REST API in HTML format.
    """

    __HTML_ERROR_REGEXES = [
        re.compile(r'<pre>(.*)</pre>'),
        re.compile(r'<title>(.*)</title>'),
    ]

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
_error_parsers = [
    _StandardErrorParser(),
    _StringErrorParser(),
    _HtmlErrorParser(),
]


def _unknown_error(response: requests.Response) -> DatabricksError:
    request_log = RoundTripLogger(response, debug_headers=True, debug_truncate_bytes=10*1024).generate()
    return DatabricksError(
        'unable to parse response. This is likely a bug in the Databricks SDK for Python or the underlying '
        'API. Please report this issue with the following debugging information to the SDK issue tracker at '
        f'https://github.com/databricks/databricks-sdk-go/issues. Request log:```{request_log}```''',
    )


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
