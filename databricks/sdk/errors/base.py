from typing import Dict, List


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
