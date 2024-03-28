from databricks.sdk.errors import platform
from databricks.sdk.errors.base import DatabricksError
from dataclasses import dataclass
import re
from typing import Optional
import requests
from .platform import ResourceDoesNotExist


@dataclass
class _ErrorOverride:
    # The name of the override. Used for logging purposes.
    debug_name: str

    # A regex that must match the path of the request for this override to be applied.
    path_regex: re.Pattern

    # The HTTP method of the request for the override to apply
    verb: str

    # The custom error class to use for this override.
    error_class: type

    # A regular expression that must match the error code for this override to be applied. If None,
    # this field is ignored.
    error_code_regex: Optional[re.Pattern] = None

    # A regular expression that must match the message for this override to be applied. If None,
    # this field is ignored.
    message_regex: Optional[re.Pattern] = None

    def matches(self, response: requests.Response, raw_error: dict):
        if response.request.method != self.verb:
            return False
        if not self.path_regex.match(response.request.path_url):
            return False
        if self.error_code_regex and not self.error_code_regex.match(raw_error.get('error_code', '')):
            return False
        if self.message_regex and not self.message_regex.match(raw_error.get('message', '')):
            return False
        return True


_INVALID_PARAMETER_VALUE = 'INVALID_PARAMETER_VALUE'

_all_overrides = [
    _ErrorOverride(
        debug_name='Clusters InvalidParameterValue => ResourceDoesNotExist',
        path_regex=re.compile(r'/api/2\.0/clusters/get'),
        verb='GET',
        error_code_regex=re.compile(_INVALID_PARAMETER_VALUE),
        message_regex=re.compile(r'Cluster .+ does not exist'),
        error_class=ResourceDoesNotExist,
    ),
    _ErrorOverride(
        debug_name='Jobs InvalidParameterValue => ResourceDoesNotExist',
        path_regex=re.compile(r'/api/2\.\d/jobs/get'),
        verb='GET',
        error_code_regex=re.compile(_INVALID_PARAMETER_VALUE),
        message_regex=re.compile(r'Job .+ does not exist'),
        error_class=ResourceDoesNotExist,
    ),
]

def error_mapper(response: requests.Response, raw: dict) -> DatabricksError:
    for override in _all_overrides:
        if override.matches(response, raw):
            return override.error_class(**raw)
    status_code = response.status_code
    error_code = raw.get('error_code', None)
    if error_code in platform.ERROR_CODE_MAPPING:
        # more specific error codes override more generic HTTP status codes
        return platform.ERROR_CODE_MAPPING[error_code](**raw)

    if status_code in platform.STATUS_CODE_MAPPING:
        # more generic HTTP status codes matched after more specific error codes,
        # where there's a default exception class per HTTP status code, and we do
        # rely on Databricks platform exception mapper to do the right thing.
        return platform.STATUS_CODE_MAPPING[status_code](**raw)

    # backwards-compatible error creation for cases like using older versions of
    # the SDK on way never releases of the platform.
    return DatabricksError(**raw)
