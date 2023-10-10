from typing import Dict, List


class OperationFailed(RuntimeError):
    pass


class OperationTimeout(RuntimeError, TimeoutError):
    pass


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


class InternalError(DatabricksError):
    """Some invariants expected by the underlying system have been broken.
    This error generally cannot be resolved by the user."""


class TemporarilyUnavailable(DatabricksError):
    """The service is currently unavailable. This is most likely a transient condition, which can be
    corrected by retrying with a backoff. Note that it is not always safe to retry-on-idempotent
    operations."""


class BadRequest(DatabricksError):
    """The request is invalid."""


class InvalidParameterValue(BadRequest):
    """Supplied value for a parameter was invalid (e.g., giving a number for a string parameter)."""


class DeadlineExceeded(DatabricksError, TimeoutError):
    """The deadline expired before the operation could complete. For operations that change the state
    of the system, this error may be returned even if the operation has completed successfully.

    For example, a successful response from a server could have been delayed long enough for
    the deadline to expire. When possible - implementations should make sure further processing of
    the request is aborted, e.g. by throwing an exception instead of making the RPC request,
    making the database query, etc."""


class Cancelled(DatabricksError):
    """The operation was explicitly canceled by the caller."""


class NotFound(DatabricksError, LookupError):
    """Operation was performed on a resource that does not exist, e.g. file or directory was not found."""


class Unauthenticated(DatabricksError, PermissionError):
    """The request does not have valid authentication (AuthN) credentials for the operation."""


class PermissionDenied(DatabricksError, PermissionError):
    """The caller does not have permission to execute the specified operation.
    This error code does not imply the request is valid or the requested entity exists or
    satisfies other pre-conditions."""


class TooManyRequests(DatabricksError, ResourceWarning):
    """Maps to HTTP code: 429 Too Many Requests"""


class ResourceExhausted(TooManyRequests):
    """Operation is rejected due to per-user rate limiting, e.g. some resource has been exhausted,
    per-user quota triggered, or the entire file system is out of space."""


class RequestLimitExceeded(TooManyRequests):
    """Cluster request was rejected because it would exceed a resource limit."""


class ResourceConflict(DatabricksError):
    """Maps to all HTTP 409 (Conflict) responses."""


class AlreadyExists(ResourceConflict):
    """Operation was rejected due a conflict with an existing resource, e.g. attempted to create
    file or directory that already exists."""


# TODO: or should it be class Aborted(AlreadyExists): ?...
class Aborted(ResourceConflict):
    """The operation was aborted, typically due to a concurrency issue such as a sequencer check failure,
    transaction abort, or transaction conflict."""


class OperationNotImplemented(DatabricksError, NotImplementedError):
    """The operation is not implemented or is not supported/enabled in this service.
    This exception extends `NotImplementedError` from Python Standard Library."""


_STATUS_CODE_MAPPING = {
    400: BadRequest, # also InvalidParameterValue
    401: Unauthenticated,
    403: PermissionDenied,
    404: NotFound,
    409: ResourceConflict, # also Aborted, AlreadyExists
    429: TooManyRequests, # also RequestLimitExceeded, ResourceExhausted
    499: Cancelled,
    500: InternalError,
    501: OperationNotImplemented,
    503: TemporarilyUnavailable,
    504: DeadlineExceeded,
}

_ERROR_CODE_MAPPING = {
    # HTTP 400 variants
    'INVALID_PARAMETER_VALUE': InvalidParameterValue,

    # HTTP 409 variants
    'ABORTED': Aborted,
    'ALREADY_EXISTS': AlreadyExists,
    'RESOURCE_ALREADY_EXISTS': AlreadyExists,

    # HTTP 429 variants
    'RESOURCE_EXHAUSTED': ResourceExhausted,
    'REQUEST_LIMIT_EXCEEDED': RequestLimitExceeded,
}


def _error_mapper(status_code: int, raw: dict) -> DatabricksError:
    if 'error_code' not in raw and status_code not in _STATUS_CODE_MAPPING:
        # strange errors, like from API v1.2 or SCIM
        return DatabricksError(**raw)

    error_code = raw['error_code']
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
