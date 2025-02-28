import json
from dataclasses import dataclass
from datetime import timedelta
from typing import Any, Dict, List, Optional


@dataclass
class ErrorInfo:
    """Describes the cause of the error with structured details."""

    reason: str
    domain: str
    metadata: Dict[str, str]


@dataclass
class RequestInfo:
    """
    Contains metadata about the request that clients can attach when
    filing a bug or providing other forms of feedback.
    """

    request_id: str
    serving_data: str


@dataclass
class RetryInfo:
    """
    Describes when the clients can retry a failed request. Clients could
    ignore the recommendation here or retry when this information is missing
    from error responses.

    It's always recommended that clients should use exponential backoff
    when retrying.

    Clients should wait until `retry_delay` amount of time has passed since
    receiving the error response before retrying.  If retrying requests also
    fail, clients should use an exponential backoff scheme to gradually
    increase the delay between retries based on `retry_delay`, until either
    a maximum number of retries have been reached or a maximum retry delay
    cap has been reached.
    """

    retry_delay: timedelta


@dataclass
class DebugInfo:
    """Describes additional debugging info."""

    stack_entries: List[str]
    detail: str


@dataclass
class QuotaFailureViolation:
    """Describes a single quota violation."""

    subject: str
    description: str


@dataclass
class QuotaFailure:
    """
    Describes how a quota check failed.

    For example if a daily limit was exceeded for the calling project, a
    service could respond with a QuotaFailure detail containing the project
    id and the description of the quota limit that was exceeded.  If the
    calling project hasn't enabled the service in the developer console,
    then a service could respond with the project id and set
    `service_disabled` to true.

    Also see RetryInfo and Help types for other details about handling a
    quota failure.
    """

    violations: List[QuotaFailureViolation]


@dataclass
class PreconditionFailureViolation:
    """Describes a single precondition violation."""

    type: str
    subject: str
    description: str


@dataclass
class PreconditionFailure:
    """Describes what preconditions have failed."""

    violations: List[PreconditionFailureViolation]


@dataclass
class BadRequestFieldViolation:
    """Describes a single field violation in a bad request."""

    field: str
    description: str


@dataclass
class BadRequest:
    """
    Describes violations in a client request. This error type
    focuses on the syntactic aspects of the request.
    """

    field_violations: List[BadRequestFieldViolation]


@dataclass
class ResourceInfo:
    """Describes the resource that is being accessed."""

    resource_type: str
    resource_name: str
    owner: Optional[str] = None
    description: Optional[str] = None


@dataclass
class HelpLink:
    """Describes a single help link."""

    description: str
    url: str


@dataclass
class Help:
    """
    Provides links to documentation or for performing an out of
    band action.

    For example, if a quota check failed with an error indicating
    the calling project hasn't enabled the accessed service, this
    can contain a URL pointing directly to the right place in the
    developer console to flip the bit.
    """

    links: List[HelpLink]


@dataclass
class ErrorDetails:
    """
    ErrorDetails contains the error details of an API error. It
    is the union of known error details types and unknown details.
    """

    error_info: Optional[ErrorInfo] = None
    request_info: Optional[RequestInfo] = None
    retry_info: Optional[RetryInfo] = None
    debug_info: Optional[DebugInfo] = None
    quota_failure: Optional[QuotaFailure] = None
    precondition_failure: Optional[PreconditionFailure] = None
    bad_request: Optional[BadRequest] = None
    resource_info: Optional[ResourceInfo] = None
    help: Optional[Help] = None
    unknown_details: List[Any] = []


@dataclass
class _ErrorInfoPb:
    reason: str
    domain: str
    metadata: Dict[str, str]


@dataclass
class _RequestInfoPb:
    request_id: str
    serving_data: str


@dataclass
class _DurationPb:
    seconds: int
    nanos: int


@dataclass
class _RetryInfoPb:
    retry_delay: _DurationPb


@dataclass
class _DebugInfoPb:
    stack_entries: List[str]
    detail: str


@dataclass
class _QuotaFailureViolationPb:
    subject: str
    description: str


@dataclass
class _QuotaFailurePb:
    violations: List[_QuotaFailureViolationPb]


@dataclass
class _PreconditionFailureViolationPb:
    type: str
    subject: str
    description: str


@dataclass
class _PreconditionFailurePb:
    violations: List[_PreconditionFailureViolationPb]


@dataclass
class _BadRequestFieldViolationPb:
    field: str
    description: str


@dataclass
class _BadRequestPb:
    field_violations: List[_BadRequestFieldViolationPb]


@dataclass
class _ResourceInfoPb:
    resource_type: str
    resource_name: str
    owner: str
    description: str


@dataclass
class _HelpLinkPb:
    description: str
    url: str


@dataclass
class _HelpPb:
    links: List[_HelpLinkPb]


# Supported error details proto types.
_ERROR_INFO_TYPE = "type.googleapis.com/google.rpc.ErrorInfo"
_REQUEST_INFO_TYPE = "type.googleapis.com/google.rpc.RequestInfo"
_RETRY_INFO_TYPE = "type.googleapis.com/google.rpc.RetryInfo"
_DEBUG_INFO_TYPE = "type.googleapis.com/google.rpc.DebugInfo"
_QUOTA_FAILURE_TYPE = "type.googleapis.com/google.rpc.QuotaFailure"
_PRECONDITION_FAILURE_TYPE = "type.googleapis.com/google.rpc.PreconditionFailure"
_BAD_REQUEST_TYPE = "type.googleapis.com/google.rpc.BadRequest"
_RESOURCE_INFO_TYPE = "type.googleapis.com/google.rpc.ResourceInfo"
_HELP_TYPE = "type.googleapis.com/google.rpc.Help"


def parse_error_details(details: List[Any]) -> ErrorDetails:
    ed = ErrorDetails()
    for d in details:
        if isinstance(d, ErrorInfo):
            ed.error_info = d
        elif isinstance(d, RequestInfo):
            ed.request_info = d
        elif isinstance(d, RetryInfo):
            ed.retry_info = d
        elif isinstance(d, DebugInfo):
            ed.debug_info = d
        elif isinstance(d, QuotaFailure):
            ed.quota_failure = d
        elif isinstance(d, PreconditionFailure):
            ed.precondition_failure = d
        elif isinstance(d, BadRequest):
            ed.bad_request = d
        elif isinstance(d, ResourceInfo):
            ed.resource_info = d
        elif isinstance(d, Help):
            ed.help = d
        else:
            ed.unknown_details.append(d)
    return ed


def unmarshal_details(d: bytes) -> Any:
    """
    Attempts to unmarshal the given bytes into a known error details type.

    It works as follows:

    - If the message is a known type, it unmarshals the message into that type.
    - If the message is not a known type, it returns the results of calling
      json.loads() on the raw message.
    - If json.loads() fails, it returns the input as is.
    """

    try:
        a = json.loads(d)
    except json.JSONDecodeError:
        return d  # not a valid JSON message

    if not isinstance(a, dict):
        return a  # not a JSON object

    t = a.get("@type")
    if not isinstance(t, str):
        return a  # JSON object with no @type field

    try:
        if t == _ERROR_INFO_TYPE:
            pb = _ErrorInfoPb(**a)
            return ErrorInfo(**pb.__dict__)
        elif t == _REQUEST_INFO_TYPE:
            pb = _RequestInfoPb(**a)
            return RequestInfo(**pb.__dict__)
        elif t == _RETRY_INFO_TYPE:
            pb = _RetryInfoPb(**a)
            return RetryInfo(
                retry_delay=timedelta(
                    seconds=pb.retry_delay.seconds,
                    microseconds=pb.retry_delay.nanos / 1000,
                )
            )
        elif t == _DEBUG_INFO_TYPE:
            pb = _DebugInfoPb(**a)
            return DebugInfo(**pb.__dict__)
        elif t == _QUOTA_FAILURE_TYPE:
            pb = _QuotaFailurePb(**a)
            violations = [QuotaFailureViolation(**v.__dict__) for v in pb.violations]
            return QuotaFailure(violations=violations)
        elif t == _PRECONDITION_FAILURE_TYPE:
            pb = _PreconditionFailurePb(**a)
            violations = [PreconditionFailureViolation(**v.__dict__) for v in pb.violations]
            return PreconditionFailure(violations=violations)
        elif t == _BAD_REQUEST_TYPE:
            pb = _BadRequestPb(**a)
            field_violations = [BadRequestFieldViolation(**v.__dict__) for v in pb.field_violations]
            return BadRequest(field_violations=field_violations)
        elif t == _RESOURCE_INFO_TYPE:
            pb = _ResourceInfoPb(**a)
            return ResourceInfo(**pb.__dict__)
        elif t == _HELP_TYPE:
            pb = _HelpPb(**a)
            links = [HelpLink(**l.__dict__) for l in pb.links]
            return Help(links=links)
    except (TypeError, ValueError):
        return a  # not a valid known type

    return a  # unknown type
