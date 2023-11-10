# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

from .base import DatabricksError

__all__ = [
    'error_mapper', 'BadRequest', 'Unauthenticated', 'PermissionDenied', 'NotFound', 'ResourceConflict',
    'TooManyRequests', 'Cancelled', 'InternalError', 'NotImplemented', 'TemporarilyUnavailable',
    'DeadlineExceeded', 'InvalidParameterValue', 'Aborted', 'AlreadyExists', 'ResourceAlreadyExists',
    'ResourceExhausted', 'RequestLimitExceeded', 'Unknown', 'DataLoss'
]


class BadRequest(DatabricksError):
    """the request is invalid"""


class Unauthenticated(DatabricksError, PermissionError):
    """the request does not have valid authentication (AuthN) credentials for the operation"""


class PermissionDenied(DatabricksError, PermissionError):
    """the caller does not have permission to execute the specified operation"""


class NotFound(DatabricksError, LookupError):
    """the operation was performed on a resource that does not exist"""


class ResourceConflict(DatabricksError):
    """maps to all HTTP 409 (Conflict) responses"""


class TooManyRequests(DatabricksError, ResourceWarning):
    """maps to HTTP code: 429 Too Many Requests"""


class Cancelled(DatabricksError):
    """the operation was explicitly canceled by the caller"""


class InternalError(DatabricksError):
    """some invariants expected by the underlying system have been broken"""


class NotImplemented(DatabricksError, NotImplementedError):
    """the operation is not implemented or is not supported/enabled in this service"""


class TemporarilyUnavailable(DatabricksError):
    """the service is currently unavailable"""


class DeadlineExceeded(DatabricksError, TimeoutError):
    """the deadline expired before the operation could complete"""


class InvalidParameterValue(BadRequest):
    """supplied value for a parameter was invalid"""


class Aborted(ResourceConflict):
    """the operation was aborted, typically due to a concurrency issue such as a sequencer check
    failure"""


class AlreadyExists(ResourceConflict):
    """operation was rejected due a conflict with an existing resource"""


class ResourceAlreadyExists(ResourceConflict):
    """operation was rejected due a conflict with an existing resource"""


class ResourceExhausted(TooManyRequests):
    """operation is rejected due to per-user rate limiting"""


class RequestLimitExceeded(TooManyRequests):
    """cluster request was rejected because it would exceed a resource limit"""


class Unknown(InternalError):
    """this error is used as a fallback if the platform-side mapping is missing some reason"""


class DataLoss(InternalError):
    """unrecoverable data loss or corruption"""


_STATUS_CODE_MAPPING = {
    400: BadRequest,
    401: Unauthenticated,
    403: PermissionDenied,
    404: NotFound,
    409: ResourceConflict,
    429: TooManyRequests,
    499: Cancelled,
    500: InternalError,
    501: NotImplemented,
    503: TemporarilyUnavailable,
    504: DeadlineExceeded,
}

_ERROR_CODE_MAPPING = {
    'INVALID_PARAMETER_VALUE': InvalidParameterValue,
    'ABORTED': Aborted,
    'ALREADY_EXISTS': AlreadyExists,
    'RESOURCE_ALREADY_EXISTS': ResourceAlreadyExists,
    'RESOURCE_EXHAUSTED': ResourceExhausted,
    'REQUEST_LIMIT_EXCEEDED': RequestLimitExceeded,
    'UNKNOWN': Unknown,
    'DATA_LOSS': DataLoss,
}


def error_mapper(status_code: int, raw: dict) -> DatabricksError:
    error_code = raw.get('error_code', None)
    if error_code in _ERROR_CODE_MAPPING:
        # more specific error codes override more generic HTTP status codes
        return _ERROR_CODE_MAPPING[error_code](**raw)

    if status_code in _STATUS_CODE_MAPPING:
        # more generic HTTP status codes matched after more specific error codes,
        # where there's a default exception class per HTTP status code, and we do
        # rely on Databricks platform exception mapper to do the right thing.
        return _STATUS_CODE_MAPPING[status_code](**raw)

    # backwards-compatible error creation for cases like using older versions of
    # the SDK on way never releases of the platform.
    return DatabricksError(**raw)
