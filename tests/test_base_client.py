from http.server import BaseHTTPRequestHandler
from typing import Iterator, List

import pytest
import requests

from databricks.sdk import errors, useragent
from databricks.sdk._base_client import _BaseClient, _StreamingResponse
from databricks.sdk.core import DatabricksError

from .clock import FakeClock
from .fixture_server import http_fixture_server


class DummyResponse(requests.Response):
    _content: Iterator[bytes]
    _closed: bool = False

    def __init__(self, content: List[bytes]) -> None:
        super().__init__()
        self._content = iter(content)

    def iter_content(self, chunk_size: int = 1, decode_unicode=False) -> Iterator[bytes]:
        return self._content

    def close(self):
        self._closed = True

    def isClosed(self):
        return self._closed


def test_streaming_response_read(config):
    content = b"some initial binary data: \x00\x01"
    response = _StreamingResponse(DummyResponse([content]))
    assert response.read() == content


def test_streaming_response_read_partial(config):
    content = b"some initial binary data: \x00\x01"
    response = _StreamingResponse(DummyResponse([content]))
    assert response.read(8) == b"some ini"


def test_streaming_response_read_full(config):
    content = b"some initial binary data: \x00\x01"
    response = _StreamingResponse(DummyResponse([content, content]))
    assert response.read() == content + content


def test_streaming_response_read_closes(config):
    content = b"some initial binary data: \x00\x01"
    dummy_response = DummyResponse([content])
    with _StreamingResponse(dummy_response) as response:
        assert response.read() == content
    assert dummy_response.isClosed()


@pytest.mark.parametrize('status_code,headers,body,expected_error', [
    (400, {}, {
        "message":
        "errorMessage",
        "details": [{
            "type": DatabricksError._error_info_type,
            "reason": "error reason",
            "domain": "error domain",
            "metadata": {
                "etag": "error etag"
            },
        }, {
            "type": "wrong type",
            "reason": "wrong reason",
            "domain": "wrong domain",
            "metadata": {
                "etag": "wrong etag"
            }
        }],
    },
     errors.BadRequest('errorMessage',
                       details=[{
                           'type': DatabricksError._error_info_type,
                           'reason': 'error reason',
                           'domain': 'error domain',
                           'metadata': {
                               'etag': 'error etag'
                           },
                       }])),
    (401, {}, {
        'error_code': 'UNAUTHORIZED',
        'message': 'errorMessage',
    }, errors.Unauthenticated('errorMessage', error_code='UNAUTHORIZED')),
    (403, {}, {
        'error_code': 'FORBIDDEN',
        'message': 'errorMessage',
    }, errors.PermissionDenied('errorMessage', error_code='FORBIDDEN')),
    (429, {}, {
        'error_code': 'TOO_MANY_REQUESTS',
        'message': 'errorMessage',
    }, errors.TooManyRequests('errorMessage', error_code='TOO_MANY_REQUESTS', retry_after_secs=1)),
    (429, {
        'Retry-After': '100'
    }, {
        'error_code': 'TOO_MANY_REQUESTS',
        'message': 'errorMessage',
    }, errors.TooManyRequests('errorMessage', error_code='TOO_MANY_REQUESTS', retry_after_secs=100)),
    (503, {}, {
        'error_code': 'TEMPORARILY_UNAVAILABLE',
        'message': 'errorMessage',
    }, errors.TemporarilyUnavailable('errorMessage', error_code='TEMPORARILY_UNAVAILABLE',
                                     retry_after_secs=1)),
    (503, {
        'Retry-After': '100'
    }, {
        'error_code': 'TEMPORARILY_UNAVAILABLE',
        'message': 'errorMessage',
    },
     errors.TemporarilyUnavailable('errorMessage', error_code='TEMPORARILY_UNAVAILABLE',
                                   retry_after_secs=100)),
    (404, {}, {
        'scimType': 'scim type',
        'detail': 'detail',
        'status': 'status',
    }, errors.NotFound('scim type detail', error_code='SCIM_status')),
])
def test_error(requests_mock, status_code, headers, body, expected_error):
    client = _BaseClient(clock=FakeClock())
    requests_mock.get("/test", json=body, status_code=status_code, headers=headers)
    with pytest.raises(DatabricksError) as raised:
        client._perform("GET", "https://localhost/test", headers={"test": "test"})
    actual = raised.value
    assert isinstance(actual, type(expected_error))
    assert str(actual) == str(expected_error)
    assert actual.error_code == expected_error.error_code
    assert actual.retry_after_secs == expected_error.retry_after_secs
    expected_error_infos, actual_error_infos = expected_error.get_error_info(), actual.get_error_info()
    assert len(expected_error_infos) == len(actual_error_infos)
    for expected, actual in zip(expected_error_infos, actual_error_infos):
        assert expected.type == actual.type
        assert expected.reason == actual.reason
        assert expected.domain == actual.domain
        assert expected.metadata == actual.metadata


def test_api_client_do_custom_headers(requests_mock):
    client = _BaseClient()
    requests_mock.get("/test",
                      json={"well": "done"},
                      request_headers={
                          "test": "test",
                          "User-Agent": useragent.to_string()
                      })
    res = client.do("GET", "https://localhost/test", headers={"test": "test"})
    assert res == {"well": "done"}


@pytest.mark.parametrize('status_code,include_retry_after',
                         ((429, False), (429, True), (503, False), (503, True)))
def test_http_retry_after(status_code, include_retry_after):
    requests = []

    def inner(h: BaseHTTPRequestHandler):
        if len(requests) == 0:
            h.send_response(status_code)
            if include_retry_after:
                h.send_header('Retry-After', '1')
            h.send_header('Content-Type', 'application/json')
            h.end_headers()
        else:
            h.send_response(200)
            h.send_header('Content-Type', 'application/json')
            h.end_headers()
            h.wfile.write(b'{"foo": 1}')
        requests.append(h.requestline)

    with http_fixture_server(inner) as host:
        api_client = _BaseClient(clock=FakeClock())
        res = api_client.do('GET', f'{host}/foo')
        assert 'foo' in res

    assert len(requests) == 2


def test_http_retry_after_wrong_format():
    requests = []

    def inner(h: BaseHTTPRequestHandler):
        if len(requests) == 0:
            h.send_response(429)
            h.send_header('Retry-After', '1.58')
            h.end_headers()
        else:
            h.send_response(200)
            h.send_header('Content-Type', 'application/json')
            h.end_headers()
            h.wfile.write(b'{"foo": 1}')
        requests.append(h.requestline)

    with http_fixture_server(inner) as host:
        api_client = _BaseClient(clock=FakeClock())
        res = api_client.do('GET', f'{host}/foo')
        assert 'foo' in res

    assert len(requests) == 2


def test_http_retried_exceed_limit():
    requests = []

    def inner(h: BaseHTTPRequestHandler):
        h.send_response(429)
        h.send_header('Retry-After', '1')
        h.end_headers()
        requests.append(h.requestline)

    with http_fixture_server(inner) as host:
        api_client = _BaseClient(retry_timeout_seconds=1, clock=FakeClock())
        with pytest.raises(TimeoutError):
            api_client.do('GET', f'{host}/foo')

    assert len(requests) == 1


def test_http_retried_on_match():
    requests = []

    def inner(h: BaseHTTPRequestHandler):
        if len(requests) == 0:
            h.send_response(400)
            h.end_headers()
            h.wfile.write(b'{"error_code": "abc", "message": "... ClusterNotReadyException ..."}')
        else:
            h.send_response(200)
            h.end_headers()
            h.wfile.write(b'{"foo": 1}')
        requests.append(h.requestline)

    with http_fixture_server(inner) as host:
        api_client = _BaseClient(clock=FakeClock())
        res = api_client.do('GET', f'{host}/foo')
        assert 'foo' in res

    assert len(requests) == 2


def test_http_not_retried_on_normal_errors():
    requests = []

    def inner(h: BaseHTTPRequestHandler):
        if len(requests) == 0:
            h.send_response(400)
            h.end_headers()
            h.wfile.write(b'{"error_code": "abc", "message": "something not found"}')
        requests.append(h.requestline)

    with http_fixture_server(inner) as host:
        api_client = _BaseClient(clock=FakeClock())
        with pytest.raises(DatabricksError):
            api_client.do('GET', f'{host}/foo')

    assert len(requests) == 1


def test_http_retried_on_connection_error():
    requests = []

    def inner(h: BaseHTTPRequestHandler):
        if len(requests) > 0:
            h.send_response(200)
            h.end_headers()
            h.wfile.write(b'{"foo": 1}')
        requests.append(h.requestline)

    with http_fixture_server(inner) as host:
        api_client = _BaseClient(clock=FakeClock())
        res = api_client.do('GET', f'{host}/foo')
        assert 'foo' in res

    assert len(requests) == 2
