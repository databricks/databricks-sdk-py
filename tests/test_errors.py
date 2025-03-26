import http.client
import json
from dataclasses import dataclass, field
from typing import Any, List, Optional

import pytest
import requests

from databricks.sdk.databricks import errors
from databricks.sdk.databricks.errors import details


def fake_response(
    method: str,
    status_code: int,
    response_body: str,
    path: Optional[str] = None,
) -> requests.Response:
    return fake_raw_response(method, status_code, response_body.encode("utf-8"), path)


def fake_raw_response(
    method: str,
    status_code: int,
    response_body: bytes,
    path: Optional[str] = None,
) -> requests.Response:
    resp = requests.Response()
    resp.status_code = status_code
    resp.reason = http.client.responses.get(status_code, "")
    if path is None:
        path = "/api/2.0/service"
    resp.request = requests.Request(method, f"https://databricks.com{path}").prepare()
    resp._content = response_body
    return resp


def fake_valid_response(
    method: str,
    status_code: int,
    error_code: str,
    message: str,
    path: Optional[str] = None,
    details: List[Any] = [],
) -> requests.Response:
    body = {"message": message}
    if error_code:
        body["error_code"] = error_code
    if len(details) > 0:
        body["details"] = details

    return fake_response(method, status_code, json.dumps(body), path)


def make_private_link_response() -> requests.Response:
    resp = requests.Response()
    resp.url = "https://databricks.com/login.html?error=private-link-validation-error"
    resp.request = requests.Request("GET", "https://databricks.com/api/2.0/service").prepare()
    resp._content = b"{}"
    resp.status_code = 200
    return resp


@dataclass
class TestCase:
    name: str
    response: requests.Response
    want_err_type: type
    want_message: str = ""
    want_details: details.ErrorDetails = field(default_factory=details.ErrorDetails)


_basic_test_cases_no_details = [
    TestCase(
        name=f'{x[0]} "{x[1]}" {x[2]}',
        response=fake_valid_response("GET", x[0], x[1], "nope"),
        want_err_type=x[2],
        want_message="nope",
    )
    for x in [
        (400, "", errors.BadRequest),
        (400, "INVALID_PARAMETER_VALUE", errors.BadRequest),
        (400, "INVALID_PARAMETER_VALUE", errors.InvalidParameterValue),
        (400, "REQUEST_LIMIT_EXCEEDED", errors.TooManyRequests),
        (400, "", IOError),
        (401, "", errors.Unauthenticated),
        (401, "", IOError),
        (403, "", errors.PermissionDenied),
        (403, "", IOError),
        (404, "", errors.NotFound),
        (404, "", IOError),
        (409, "", errors.ResourceConflict),
        (409, "ABORTED", errors.Aborted),
        (409, "ABORTED", errors.ResourceConflict),
        (409, "ALREADY_EXISTS", errors.AlreadyExists),
        (409, "ALREADY_EXISTS", errors.ResourceConflict),
        (409, "", IOError),
        (429, "", errors.TooManyRequests),
        (429, "REQUEST_LIMIT_EXCEEDED", errors.TooManyRequests),
        (429, "REQUEST_LIMIT_EXCEEDED", errors.RequestLimitExceeded),
        (429, "RESOURCE_EXHAUSTED", errors.TooManyRequests),
        (429, "RESOURCE_EXHAUSTED", errors.ResourceExhausted),
        (429, "", IOError),
        (499, "", errors.Cancelled),
        (499, "", IOError),
        (500, "", errors.InternalError),
        (500, "UNKNOWN", errors.InternalError),
        (500, "UNKNOWN", errors.Unknown),
        (500, "DATA_LOSS", errors.InternalError),
        (500, "DATA_LOSS", errors.DataLoss),
        (500, "", IOError),
        (501, "", errors.NotImplemented),
        (501, "", IOError),
        (503, "", errors.TemporarilyUnavailable),
        (503, "", IOError),
        (504, "", errors.DeadlineExceeded),
        (504, "", IOError),
        (444, "", errors.DatabricksError),
        (444, "", IOError),
    ]
]


_test_case_with_details = [
    TestCase(
        name="all_error_details",
        response=fake_valid_response(
            method="GET",
            status_code=404,
            error_code="NOT_FOUND",
            message="test message",
            details=[
                {
                    "@type": "type.googleapis.com/google.rpc.ErrorInfo",
                    "reason": "reason",
                    "domain": "domain",
                    "metadata": {"k1": "v1", "k2": "v2"},
                },
                {
                    "@type": "type.googleapis.com/google.rpc.RequestInfo",
                    "request_id": "req42",
                    "serving_data": "data",
                },
                {
                    "@type": "type.googleapis.com/google.rpc.RetryInfo",
                    "retry_delay": "42.000000001s",
                },
                {
                    "@type": "type.googleapis.com/google.rpc.DebugInfo",
                    "stack_entries": ["entry1", "entry2"],
                    "detail": "detail",
                },
                {
                    "@type": "type.googleapis.com/google.rpc.QuotaFailure",
                    "violations": [{"subject": "subject", "description": "description"}],
                },
                {
                    "@type": "type.googleapis.com/google.rpc.PreconditionFailure",
                    "violations": [{"type": "type", "subject": "subject", "description": "description"}],
                },
                {
                    "@type": "type.googleapis.com/google.rpc.BadRequest",
                    "field_violations": [{"field": "field", "description": "description"}],
                },
                {
                    "@type": "type.googleapis.com/google.rpc.ResourceInfo",
                    "resource_type": "resource_type",
                    "resource_name": "resource_name",
                    "owner": "owner",
                    "description": "description",
                },
                {
                    "@type": "type.googleapis.com/google.rpc.Help",
                    "links": [{"description": "description", "url": "url"}],
                },
            ],
        ),
        want_err_type=errors.NotFound,
        want_message="test message",
        want_details=details.ErrorDetails(
            error_info=details.ErrorInfo(
                reason="reason",
                domain="domain",
                metadata={"k1": "v1", "k2": "v2"},
            ),
            request_info=details.RequestInfo(
                request_id="req42",
                serving_data="data",
            ),
            retry_info=details.RetryInfo(
                retry_delay_seconds=42.000000001,
            ),
            debug_info=details.DebugInfo(
                stack_entries=["entry1", "entry2"],
                detail="detail",
            ),
            quota_failure=details.QuotaFailure(
                violations=[
                    details.QuotaFailureViolation(
                        subject="subject",
                        description="description",
                    )
                ],
            ),
            precondition_failure=details.PreconditionFailure(
                violations=[
                    details.PreconditionFailureViolation(
                        type="type",
                        subject="subject",
                        description="description",
                    )
                ],
            ),
            bad_request=details.BadRequest(
                field_violations=[
                    details.BadRequestFieldViolation(
                        field="field",
                        description="description",
                    )
                ],
            ),
            resource_info=details.ResourceInfo(
                resource_type="resource_type",
                resource_name="resource_name",
                owner="owner",
                description="description",
            ),
            help=details.Help(
                links=[
                    details.HelpLink(
                        description="description",
                        url="url",
                    )
                ],
            ),
            unknown_details=[],
        ),
    ),
    TestCase(
        name="unknown_error_details",
        response=fake_valid_response(
            method="GET",
            status_code=404,
            error_code="NOT_FOUND",
            message="test message",
            details=[
                1,
                "foo",
                ["foo", "bar"],
                {
                    "@type": "type.googleapis.com/google.rpc.FooBar",
                    "reason": "reason",
                    "domain": "domain",
                },
            ],
        ),
        want_err_type=errors.NotFound,
        want_message="test message",
        want_details=details.ErrorDetails(
            unknown_details=[
                1,
                "foo",
                ["foo", "bar"],
                {
                    "@type": "type.googleapis.com/google.rpc.FooBar",
                    "reason": "reason",
                    "domain": "domain",
                },
            ],
        ),
    ),
]

_test_case_other_errors = [
    TestCase(
        name="private_link_validation_error",
        response=make_private_link_response(),
        want_err_type=errors.PrivateLinkValidationError,
        want_message=(
            "The requested workspace has AWS PrivateLink enabled and is not accessible from the current network. "
            "Ensure that AWS PrivateLink is properly configured and that your device has access to the AWS VPC "
            "endpoint. For more information, see "
            "https://docs.databricks.com/en/security/network/classic/privatelink.html."
        ),
    ),
    TestCase(
        name="malformed_request",
        response=fake_response(
            method="GET",
            status_code=400,
            response_body="MALFORMED_REQUEST: vpc_endpoints malformed parameters: VPC Endpoint ... with use_case ... cannot be attached in ... list",
        ),
        want_err_type=errors.BadRequest,
        want_message="vpc_endpoints malformed parameters: VPC Endpoint ... with use_case ... cannot be attached in ... list",
    ),
    TestCase(
        name="worker_environment_not_ready",
        response=fake_response(
            method="GET",
            status_code=400,
            response_body="<pre>Worker environment not ready</pre>",
        ),
        want_err_type=errors.BadRequest,
        want_message="Worker environment not ready",
    ),
    TestCase(
        name="unable_to_parse_response",
        response=fake_response(
            method="GET",
            status_code=400,
            response_body="this is not a real response",
        ),
        want_err_type=errors.BadRequest,
        want_message=(
            "unable to parse response. This is likely a bug in the Databricks SDK for Python or the underlying API. "
            "Please report this issue with the following debugging information to the SDK issue tracker at "
            "https://github.com/databricks/databricks-sdk-go/issues. Request log:```GET /api/2.0/service\n"
            "< 400 Bad Request\n"
            "< this is not a real response```"
        ),
    ),
    TestCase(
        name="group_not_found",
        response=fake_response(
            method="GET",
            status_code=404,
            response_body=json.dumps(
                {
                    "detail": "Group with id 1234 is not found",
                    "status": "404",
                    "schemas": ["urn:ietf:params:scim:api:messages:2.0:Error"],
                }
            ),
        ),
        want_err_type=errors.NotFound,
        want_message="None Group with id 1234 is not found",
    ),
    TestCase(
        name="unable_to_parse_response2",
        response=fake_response(
            method="GET",
            status_code=404,
            response_body=json.dumps("This is JSON but not a dictionary"),
        ),
        want_err_type=errors.NotFound,
        want_message='unable to parse response. This is likely a bug in the Databricks SDK for Python or the underlying API. Please report this issue with the following debugging information to the SDK issue tracker at https://github.com/databricks/databricks-sdk-go/issues. Request log:```GET /api/2.0/service\n< 404 Not Found\n< "This is JSON but not a dictionary"```',
    ),
    TestCase(
        name="unable_to_parse_response3",
        response=fake_raw_response(
            method="GET",
            status_code=404,
            response_body=b"\x80",
        ),
        want_err_type=errors.NotFound,
        want_message="unable to parse response. This is likely a bug in the Databricks SDK for Python or the underlying API. Please report this issue with the following debugging information to the SDK issue tracker at https://github.com/databricks/databricks-sdk-go/issues. Request log:```GET /api/2.0/service\n< 404 Not Found\n< �```",
    ),
]


_all_test_cases = _basic_test_cases_no_details + _test_case_with_details + _test_case_other_errors


@pytest.mark.parametrize("test_case", [pytest.param(x, id=x.name) for x in _all_test_cases])
def test_get_api_error(test_case: TestCase):
    parser = errors._Parser()

    with pytest.raises(errors.DatabricksError) as e:
        raise parser.get_api_error(test_case.response)

    assert isinstance(e.value, test_case.want_err_type)
    assert str(e.value) == test_case.want_message
    assert e.value.get_error_details() == test_case.want_details
