import io
import random
from http.server import BaseHTTPRequestHandler
from typing import Callable, Iterator, List, Optional, Tuple, Type
from unittest.mock import Mock

import pytest
from requests import PreparedRequest, Response, Timeout

from databricks.sdk import errors, useragent
from databricks.sdk._base_client import (_BaseClient, _RawResponse,
                                         _StreamingResponse)
from databricks.sdk.core import DatabricksError

from .clock import FakeClock
from .fixture_server import http_fixture_server


class DummyResponse(_RawResponse):
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


@pytest.mark.parametrize(
    'chunk_size,expected_chunks,data_size',
    [
        (5, 20, 100), # 100 / 5 bytes per chunk = 20 chunks
        (10, 10, 100), # 100 / 10 bytes per chunk = 10 chunks
        (200, 1, 100), # 100 / 200 bytes per chunk = 1 chunk
    ])
def test_streaming_response_chunk_size(chunk_size, expected_chunks, data_size):
    rng = random.Random(42)
    test_data = bytes(rng.getrandbits(8) for _ in range(data_size))

    content_chunks = []
    mock_response = Mock(spec=_RawResponse)

    def mock_iter_content(chunk_size: int, decode_unicode: bool):
        # Simulate how requests would chunk the data.
        for i in range(0, len(test_data), chunk_size):
            chunk = test_data[i:i + chunk_size]
            content_chunks.append(chunk) # track chunks for verification
            yield chunk

    mock_response.iter_content = mock_iter_content
    stream = _StreamingResponse(mock_response)
    stream.set_chunk_size(chunk_size)

    # Read all data one byte at a time.
    received_data = b""
    while True:
        chunk = stream.read(1)
        if not chunk:
            break
        received_data += chunk

    assert received_data == test_data # all data was received correctly
    assert len(content_chunks) == expected_chunks # correct number of chunks
    assert all(len(c) <= chunk_size for c in content_chunks) # chunks don't exceed size


def test_is_seekable_stream():
    client = _BaseClient()

    # Test various input types that are not streams.
    assert not client._is_seekable_stream(None) # None
    assert not client._is_seekable_stream("string data") # str
    assert not client._is_seekable_stream(b"binary data") # bytes
    assert not client._is_seekable_stream(["list", "data"]) # list
    assert not client._is_seekable_stream(42) # int

    # Test non-seekable stream.
    non_seekable = io.BytesIO(b"test data")
    non_seekable.seekable = lambda: False
    assert not client._is_seekable_stream(non_seekable)

    # Test seekable streams.
    assert client._is_seekable_stream(io.BytesIO(b"test data")) # BytesIO
    assert client._is_seekable_stream(io.StringIO("test data")) # StringIO

    # Test file objects.
    with open(__file__, 'rb') as f:
        assert client._is_seekable_stream(f) # File object

    # Test custom seekable stream.
    class CustomSeekableStream(io.IOBase):

        def seekable(self):
            return True

        def seek(self, offset, whence=0):
            return 0

        def tell(self):
            return 0

    assert client._is_seekable_stream(CustomSeekableStream())


class RetryTestCase:

    def __init__(self, data_provider: Callable, offset: Optional[int], expected_failure: bool,
                 expected_result: bytes):
        self._data_provider = data_provider
        self._offset = offset
        self._expected_result = expected_result
        self._expected_failure = expected_failure

    def get_data(self):
        data = self._data_provider()
        if self._offset is not None:
            data.seek(self._offset)
        return data

    @classmethod
    def create_non_seekable_stream(cls, data: bytes):
        result = io.BytesIO(data)
        result.seekable = lambda: False # makes the stream appear non-seekable
        return result


class MockSession:

    def __init__(self, failure_count: int, failure_provider: Callable[[], Response]):
        self._failure_count = failure_count
        self._received_requests: List[bytes] = []
        self._failure_provider = failure_provider

    @classmethod
    def raise_timeout_exception(cls):
        raise Timeout("Fake timeout")

    @classmethod
    def return_retryable_response(cls):
        # fill response fields so that logging does not fail
        response = Response()
        response._content = b''
        response.status_code = 429
        response.headers = {'Retry-After': '1'}
        response.url = 'http://test.com/'

        response.request = PreparedRequest()
        response.request.url = response.url
        response.request.method = 'POST'
        response.request.headers = None
        response.request.body = b''
        return response

    # following the signature of Session.request()
    def request(self,
                method,
                url,
                params=None,
                data=None,
                headers=None,
                cookies=None,
                files=None,
                auth=None,
                timeout=None,
                allow_redirects=True,
                proxies=None,
                hooks=None,
                stream=None,
                verify=None,
                cert=None,
                json=None):
        request_body = data.read()

        if isinstance(request_body, str):
            request_body = request_body.encode('utf-8') # to be able to compare with expected bytes

        self._received_requests.append(request_body)
        if self._failure_count > 0:
            self._failure_count -= 1
            return self._failure_provider()
            #
        else:
            # fill response fields so that logging does not fail
            response = Response()
            response._content = b''
            response.status_code = 200
            response.reason = 'OK'
            response.url = url

            response.request = PreparedRequest()
            response.request.url = url
            response.request.method = method
            response.request.headers = headers
            response.request.body = data
            return response


@pytest.mark.parametrize(
    'test_case',
    [
        # bytes -> BytesIO
        RetryTestCase(lambda: b"0123456789", None, False, b"0123456789"),
        # str -> BytesIO
        RetryTestCase(lambda: "0123456789", None, False, b"0123456789"),
        # BytesIO directly
        RetryTestCase(lambda: io.BytesIO(b"0123456789"), None, False, b"0123456789"),
        # BytesIO directly with offset
        RetryTestCase(lambda: io.BytesIO(b"0123456789"), 4, False, b"456789"),
        # StringIO
        RetryTestCase(lambda: io.StringIO("0123456789"), None, False, b"0123456789"),
        # Non-seekable
        RetryTestCase(lambda: RetryTestCase.create_non_seekable_stream(b"0123456789"), None, True,
                      b"0123456789")
    ])
@pytest.mark.parametrize('failure', [[MockSession.raise_timeout_exception, Timeout],
                                     [MockSession.return_retryable_response, errors.TooManyRequests]])
def test_rewind_seekable_stream(test_case: RetryTestCase, failure: Tuple[Callable[[], Response], Type]):
    failure_count = 2

    data = test_case.get_data()

    session = MockSession(failure_count, failure[0])
    client = _BaseClient()
    client._session = session

    def do():
        client.do('POST', f'test.com/foo', data=data)

    if test_case._expected_failure:
        expected_attempts_made = 1
        exception_class = failure[1]
        with pytest.raises(exception_class):
            do()
    else:
        expected_attempts_made = failure_count + 1
        do()

    assert session._received_requests == [test_case._expected_result for _ in range(expected_attempts_made)]
