import pytest

from databricks.sdk import errors


def test_error_code_has_precedence_over_http_status():
    err = errors._error_mapper(400, {'error_code': 'INVALID_PARAMETER_VALUE', 'message': 'nope'})
    assert errors.InvalidParameterValue == type(err)


def test_http_status_code_maps_fine():
    err = errors._error_mapper(400, {'error_code': 'MALFORMED_REQUEST', 'message': 'nope'})
    assert errors.BadRequest == type(err)


def test_other_errors_also_map_fine():
    err = errors._error_mapper(417, {'error_code': 'WHOOPS', 'message': 'nope'})
    assert errors.DatabricksError == type(err)


@pytest.mark.parametrize('status_code, error_code, klass',
                         [(400, ..., errors.BadRequest), (400, 'INVALID_PARAMETER_VALUE', errors.BadRequest),
                          (400, 'INVALID_PARAMETER_VALUE', errors.InvalidParameterValue),
                          (400, 'REQUEST_LIMIT_EXCEEDED', errors.TooManyRequests), (400, ..., IOError),
                          (401, ..., errors.Unauthenticated), (401, ..., PermissionError),
                          (401, ..., IOError), (403, ..., errors.PermissionDenied),
                          (403, ..., PermissionError), (403, ..., IOError), (404, ..., errors.NotFound),
                          (404, ..., LookupError), (404, ..., IOError), (409, ..., errors.ResourceConflict),
                          (409, 'ABORTED', errors.Aborted), (409, 'ABORTED', errors.ResourceConflict),
                          (409, 'ALREADY_EXISTS', errors.AlreadyExists),
                          (409, 'ALREADY_EXISTS', errors.ResourceConflict), (409, ..., IOError),
                          (429, ..., errors.TooManyRequests),
                          (429, 'REQUEST_LIMIT_EXCEEDED', errors.TooManyRequests),
                          (429, 'REQUEST_LIMIT_EXCEEDED', errors.RequestLimitExceeded),
                          (429, 'RESOURCE_EXHAUSTED', errors.TooManyRequests),
                          (429, 'RESOURCE_EXHAUSTED', errors.ResourceExhausted), (429, ..., ResourceWarning),
                          (417, 'REQUEST_LIMIT_EXCEEDED', ResourceWarning), (429, ..., IOError),
                          (499, ..., errors.Cancelled), (499, ..., IOError), (500, ..., errors.InternalError),
                          (500, ..., IOError), (501, ..., errors.OperationNotImplemented),
                          (501, ..., NotImplementedError), (501, ..., IOError),
                          (503, ..., errors.TemporarilyUnavailable), (503, ..., IOError),
                          (504, ..., errors.DeadlineExceeded), (504, ..., TimeoutError), (504, ..., IOError),
                          (444, ..., errors.DatabricksError), (444, ..., IOError), ])
def test_subclasses(status_code, error_code, klass):
    try:
        raise errors._error_mapper(status_code, {'error_code': error_code, 'message': 'nope'})
    except klass:
        return
