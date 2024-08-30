import http.client
import json
from typing import List, Optional, Tuple

import pytest
import requests

from databricks.sdk import errors


def fake_response(method: str,
                  status_code: int,
                  response_body: str,
                  path: Optional[str] = None) -> requests.Response:
    resp = requests.Response()
    resp.status_code = status_code
    resp.reason = http.client.responses.get(status_code, '')
    if path is None:
        path = '/api/2.0/service'
    resp.request = requests.Request(method, f"https://databricks.com{path}").prepare()
    resp._content = response_body.encode('utf-8')
    return resp


def fake_valid_response(method: str,
                        status_code: int,
                        error_code: str,
                        message: str,
                        path: Optional[str] = None) -> requests.Response:
    body = {'message': message}
    if error_code:
        body['error_code'] = error_code
    return fake_response(method, status_code, json.dumps(body), path)


def make_private_link_response() -> requests.Response:
    resp = requests.Response()
    resp.url = 'https://databricks.com/login.html?error=private-link-validation-error'
    resp.request = requests.Request('GET', 'https://databricks.com/api/2.0/service').prepare()
    resp._content = b'{}'
    resp.status_code = 200
    return resp


# This should be `(int, str, type)` but doesn't work in Python 3.7-3.8.
base_subclass_test_cases: List[Tuple[int, str,
                                     type]] = [(400, '', errors.BadRequest),
                                               (400, 'INVALID_PARAMETER_VALUE', errors.BadRequest),
                                               (400, 'INVALID_PARAMETER_VALUE', errors.InvalidParameterValue),
                                               (400, 'REQUEST_LIMIT_EXCEEDED', errors.TooManyRequests),
                                               (400, '', IOError), (401, '', errors.Unauthenticated),
                                               (401, '', IOError), (403, '', errors.PermissionDenied),
                                               (403, '', IOError), (404, '', errors.NotFound),
                                               (404, '', IOError), (409, '', errors.ResourceConflict),
                                               (409, 'ABORTED', errors.Aborted),
                                               (409, 'ABORTED', errors.ResourceConflict),
                                               (409, 'ALREADY_EXISTS', errors.AlreadyExists),
                                               (409, 'ALREADY_EXISTS', errors.ResourceConflict),
                                               (409, '', IOError), (429, '', errors.TooManyRequests),
                                               (429, 'REQUEST_LIMIT_EXCEEDED', errors.TooManyRequests),
                                               (429, 'REQUEST_LIMIT_EXCEEDED', errors.RequestLimitExceeded),
                                               (429, 'RESOURCE_EXHAUSTED', errors.TooManyRequests),
                                               (429, 'RESOURCE_EXHAUSTED', errors.ResourceExhausted),
                                               (429, '', IOError), (499, '', errors.Cancelled),
                                               (499, '', IOError), (500, '', errors.InternalError),
                                               (500, 'UNKNOWN', errors.InternalError),
                                               (500, 'UNKNOWN', errors.Unknown),
                                               (500, 'DATA_LOSS', errors.InternalError),
                                               (500, 'DATA_LOSS', errors.DataLoss), (500, '', IOError),
                                               (501, '', errors.NotImplemented), (501, '', IOError),
                                               (503, '', errors.TemporarilyUnavailable), (503, '', IOError),
                                               (504, '', errors.DeadlineExceeded), (504, '', IOError),
                                               (444, '', errors.DatabricksError), (444, '', IOError), ]

subclass_test_cases = [(fake_valid_response('GET', x[0], x[1], 'nope'), x[2], 'nope')
                       for x in base_subclass_test_cases]


@pytest.mark.parametrize(
    'response, expected_error, expected_message', subclass_test_cases +
    [(fake_response('GET', 400, ''), errors.BadRequest, 'Bad Request'),
     (fake_valid_response('GET', 417, 'WHOOPS', 'nope'), errors.DatabricksError, 'nope'),
     (fake_valid_response('GET', 522, '', 'nope'), errors.DatabricksError, 'nope'),
     (make_private_link_response(), errors.PrivateLinkValidationError,
      ('The requested workspace has AWS PrivateLink enabled and is not accessible from the current network. '
       'Ensure that AWS PrivateLink is properly configured and that your device has access to the AWS VPC '
       'endpoint. For more information, see '
       'https://docs.databricks.com/en/security/network/classic/privatelink.html.'),
      ),
     (fake_valid_response(
         'GET', 400, 'INVALID_PARAMETER_VALUE', 'Cluster abcde does not exist',
         '/api/2.0/clusters/get'), errors.ResourceDoesNotExist, 'Cluster abcde does not exist'),
     (fake_valid_response('GET', 400, 'INVALID_PARAMETER_VALUE', 'Job abcde does not exist',
                          '/api/2.0/jobs/get'), errors.ResourceDoesNotExist, 'Job abcde does not exist'),
     (fake_valid_response('GET', 400, 'INVALID_PARAMETER_VALUE', 'Job abcde does not exist',
                          '/api/2.1/jobs/get'), errors.ResourceDoesNotExist, 'Job abcde does not exist'),
     (fake_valid_response('GET', 400, 'INVALID_PARAMETER_VALUE', 'Invalid spark version',
                          '/api/2.1/jobs/get'), errors.InvalidParameterValue, 'Invalid spark version'),
     (fake_response(
         'GET', 400,
         'MALFORMED_REQUEST: vpc_endpoints malformed parameters: VPC Endpoint ... with use_case ... cannot be attached in ... list'
     ), errors.BadRequest,
      'vpc_endpoints malformed parameters: VPC Endpoint ... with use_case ... cannot be attached in ... list'
      ),
     (fake_response('GET', 400, '<pre>Worker environment not ready</pre>'), errors.BadRequest,
      'Worker environment not ready'),
     (fake_response('GET', 400, 'this is not a real response'), errors.BadRequest,
      ('unable to parse response. This is likely a bug in the Databricks SDK for Python or the underlying API. '
       'Please report this issue with the following debugging information to the SDK issue tracker at '
       'https://github.com/databricks/databricks-sdk-go/issues. Request log:```GET /api/2.0/service\n'
       '< 400 Bad Request\n'
       '< this is not a real response```')), ])
def test_get_api_error(response, expected_error, expected_message):
    with pytest.raises(errors.DatabricksError) as e:
        raise errors.get_api_error(response)
    assert isinstance(e.value, expected_error)
    assert str(e.value) == expected_message
