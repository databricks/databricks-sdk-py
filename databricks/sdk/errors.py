from typing import Dict, List


class OperationFailed(RuntimeError):
    pass


class OperationTimeout(RuntimeError):
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


class DeadlineExceeded(DatabricksError):
    """The deadline expired before the operation could complete. For operations that change the state
    of the system, this error may be returned even if the operation has completed successfully.

    For example, a successful response from a server could have been delayed long enough for
    the deadline to expire. When possible - implementations should make sure further processing of
    the request is aborted, e.g. by throwing an exception instead of making the RPC request,
    making the database query, etc."""


class NotFound(DatabricksError):
    """Operation was performed on a resource that does not exist, e.g. file or directory was not found."""


class AlreadyExists(DatabricksError):
    """Operation was rejected due a conflict with an existing resource, e.g. attempted to create
    file or directory that already exists."""


class Unauthenticated(DatabricksError):
    """The request does not have valid authentication (AuthN) credentials for the operation."""


class InvalidParameterValue(DatabricksError):
    """Supplied value for a parameter was invalid (e.g., giving a number for a string parameter)."""


class PermissionDenied(DatabricksError):
    """The caller does not have permission to execute the specified operation.
    This error code does not imply the request is valid or the requested entity exists or
    satisfies other pre-conditions."""


class ResourceLimitExceeded(DatabricksError):
    """Cluster request was rejected because it would exceed a resource limit."""


_ERROR_CODE_MAPPING = {
    'INTERNAL_ERROR': InternalError,
    'TEMPORARILY_UNAVAILABLE': TemporarilyUnavailable,
    'PARTIAL_DELETE': TemporarilyUnavailable,
    'MAX_LIST_SIZE_EXCEEDED': TemporarilyUnavailable,

    # TBD - could be the same - An external service is unavailable temporarily as it is being updated/re-deployed.
    'SERVICE_UNDER_MAINTENANCE': TemporarilyUnavailable,
    'BAD_REQUEST': BadRequest,

    # TBD - As long as we prefer BAD_REQUEST over MALFORMED_REQUEST, INVALID_STATE,
    # UNPARSEABLE_HTTP_ERROR, we could do this semantic mapping here.
    'MALFORMED_REQUEST': BadRequest,
    'INVALID_STATE': BadRequest,
    'UNPARSEABLE_HTTP_ERROR': BadRequest,
    'NOT_FOUND': NotFound,
    # TBD - RESOURCE_DOES_NOT_EXIST deprecated in favor of NOT_FOUND
    'RESOURCE_DOES_NOT_EXIST': NotFound,
    'FEATURE_DISABLED': NotFound,
    'DEADLINE_EXCEEDED': DeadlineExceeded,
    'ALREADY_EXISTS': AlreadyExists,

    # TBD - RESOURCE_ALREADY_EXISTS is deprecated, and we prefer ALREADY_EXISTS
    'RESOURCE_ALREADY_EXISTS': AlreadyExists,

    # TBD - we prefer AlreadyExists over RESOURCE_CONFLICT.
    'RESOURCE_CONFLICT': AlreadyExists,
    'UNAUTHENTICATED': Unauthenticated,
    'INVALID_PARAMETER_VALUE': InvalidParameterValue,

    # ENDPOINT_NOT_FOUND could be mapped to NOT_IMPLEMENTED, but it conflicts with
    # builtin exception
    'PERMISSION_DENIED': PermissionDenied,

    # TBD - introduce new abstract class LimitExceeded?..
    'RESOURCE_LIMIT_EXCEEDED': ResourceLimitExceeded,

    # TBD - these can be made into more specific exceptions later,
    # where they'll extend NotFound.
    'METASTORE_DOES_NOT_EXIST': NotFound,
    'DAC_DOES_NOT_EXIST': NotFound,
    'CATALOG_DOES_NOT_EXIST': NotFound,
    'SCHEMA_DOES_NOT_EXIST': NotFound,
    'TABLE_DOES_NOT_EXIST': NotFound,
    'SHARE_DOES_NOT_EXIST': NotFound,
    'RECIPIENT_DOES_NOT_EXIST': NotFound,
    'STORAGE_CREDENTIAL_DOES_NOT_EXIST': NotFound,
    'EXTERNAL_LOCATION_DOES_NOT_EXIST': NotFound,
    'PRINCIPAL_DOES_NOT_EXIST': NotFound,
    'PROVIDER_DOES_NOT_EXIST': NotFound,
    'METASTORE_ALREADY_EXISTS': AlreadyExists,
    'DAC_ALREADY_EXISTS': AlreadyExists,
    'CATALOG_ALREADY_EXISTS': AlreadyExists,
    'SCHEMA_ALREADY_EXISTS': AlreadyExists,
    'TABLE_ALREADY_EXISTS': AlreadyExists,
    'SHARE_ALREADY_EXISTS': AlreadyExists,
    'RECIPIENT_ALREADY_EXISTS': AlreadyExists,
    'STORAGE_CREDENTIAL_ALREADY_EXISTS': AlreadyExists,
    'EXTERNAL_LOCATION_ALREADY_EXISTS': AlreadyExists,
    'PROVIDER_ALREADY_EXISTS': AlreadyExists,
}


def _error_mapper(raw: dict) -> DatabricksError:
    if 'error_code' not in raw:
        return DatabricksError(**raw)
    error_code = raw['error_code']
    if error_code in _ERROR_CODE_MAPPING:
        # create specific exception instance if we can
        return _ERROR_CODE_MAPPING[error_code](**raw)
    # catch all others otherwise
    return DatabricksError(**raw)
