import pytest
import requests

from databricks.sdk import errors


def fake_response(status_code: int) -> requests.Response:
    resp = requests.Response()
    resp.status_code = status_code
    resp.request = requests.Request('GET', 'https://databricks.com/api/2.0/service').prepare()
    return resp


def test_error_code_has_precedence_over_http_status():
    err = errors.error_mapper(fake_response(400), {
        'error_code': 'INVALID_PARAMETER_VALUE',
        'message': 'nope'
    })
    assert errors.InvalidParameterValue == type(err)


def test_http_status_code_maps_fine():
    err = errors.error_mapper(fake_response(400), {'error_code': 'MALFORMED_REQUEST', 'message': 'nope'})
    assert errors.BadRequest == type(err)


def test_other_errors_also_map_fine():
    err = errors.error_mapper(fake_response(417), {'error_code': 'WHOOPS', 'message': 'nope'})
    assert errors.DatabricksError == type(err)


def test_missing_error_code():
    err = errors.error_mapper(fake_response(522), {'message': 'nope'})
    assert errors.DatabricksError == type(err)


def test_private_link_error():
    resp = requests.Response()
    resp.url = 'https://databricks.com/login.html?error=private-link-validation-error'
    resp.request = requests.Request('GET', 'https://databricks.com/api/2.0/service').prepare()
    err = errors.error_mapper(resp, {})
    assert errors.PrivateLinkValidationError == type(err)


@pytest.mark.parametrize('status_code, error_code, klass',
                         [(400, ..., errors.BadRequest), (400, 'INVALID_PARAMETER_VALUE', errors.BadRequest),
                          (400, 'INVALID_PARAMETER_VALUE', errors.InvalidParameterValue),
                          (400, 'REQUEST_LIMIT_EXCEEDED', errors.TooManyRequests), (400, ..., IOError),
                          (401, ..., errors.Unauthenticated), (401, ..., IOError),
                          (403, ..., errors.PermissionDenied),
                          (403, ..., IOError), (404, ..., errors.NotFound), (404, ..., IOError),
                          (409, ..., errors.ResourceConflict), (409, 'ABORTED', errors.Aborted),
                          (409, 'ABORTED', errors.ResourceConflict),
                          (409, 'ALREADY_EXISTS', errors.AlreadyExists),
                          (409, 'ALREADY_EXISTS', errors.ResourceConflict), (409, ..., IOError),
                          (429, ..., errors.TooManyRequests),
                          (429, 'REQUEST_LIMIT_EXCEEDED', errors.TooManyRequests),
                          (429, 'REQUEST_LIMIT_EXCEEDED', errors.RequestLimitExceeded),
                          (429, 'RESOURCE_EXHAUSTED', errors.TooManyRequests),
                          (429, 'RESOURCE_EXHAUSTED', errors.ResourceExhausted), (429, ..., IOError),
                          (499, ..., errors.Cancelled), (499, ..., IOError), (500, ..., errors.InternalError),
                          (500, 'UNKNOWN', errors.InternalError), (500, 'UNKNOWN', errors.Unknown),
                          (500, 'DATA_LOSS', errors.InternalError), (500, 'DATA_LOSS', errors.DataLoss),
                          (500, ..., IOError), (501, ..., errors.NotImplemented), (501, ..., IOError),
                          (503, ..., errors.TemporarilyUnavailable), (503, ..., IOError),
                          (504, ..., errors.DeadlineExceeded), (504, ..., IOError),
                          (444, ..., errors.DatabricksError), (444, ..., IOError), ])
def test_subclasses(status_code, error_code, klass):
    try:
        raise errors.error_mapper(fake_response(status_code), {'error_code': error_code, 'message': 'nope'})
    except klass:
        return


@pytest.mark.parametrize('verb, path, status_code, error_code, message, expected_error',
                         [[
                             'GET', '/api/2.0/clusters/get', 400, 'INVALID_PARAMETER_VALUE',
                             'Cluster abcde does not exist', errors.ResourceDoesNotExist
                         ],
                          [
                              'GET', '/api/2.0/jobs/get', 400, 'INVALID_PARAMETER_VALUE',
                              'Job abcde does not exist', errors.ResourceDoesNotExist
                          ],
                          [
                              'GET', '/api/2.1/jobs/get', 400, 'INVALID_PARAMETER_VALUE',
                              'Job abcde does not exist', errors.ResourceDoesNotExist
                          ],
                          [
                              'GET', '/api/2.1/jobs/get', 400, 'INVALID_PARAMETER_VALUE',
                              'Invalid spark version', errors.InvalidParameterValue
                          ], ])
def test_error_overrides(verb, path, status_code, error_code, message, expected_error):
    resp = requests.Response()
    resp.status_code = status_code
    resp.request = requests.Request(verb, f'https://databricks.com{path}').prepare()
    with pytest.raises(expected_error):
        raise errors.error_mapper(resp, {'error_code': error_code, 'message': message})
