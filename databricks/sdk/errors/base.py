import re
from dataclasses import dataclass
from typing import Dict, List, Optional

import requests


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
        if error:
            # API 1.2 has different response format, let's adapt
            message = error
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
