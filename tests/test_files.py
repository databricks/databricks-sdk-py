import copy
import hashlib
import io
import json
import logging
import os
import random
import re
import time
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from tempfile import mkstemp
from typing import Callable, List, Optional, Type, Union
from urllib.parse import parse_qs, urlparse

import pytest
import requests
import requests_mock
from requests import RequestException

from databricks.sdk import WorkspaceClient
from databricks.sdk.databricks.core import Config
from databricks.sdk.databricks.errors.platform import (AlreadyExists, BadRequest,
                                            InternalError, PermissionDenied,
                                            TooManyRequests)

logger = logging.getLogger(__name__)


@dataclass
class RequestData:

    def __init__(self, offset: int):
        self._offset: int = offset


class DownloadTestCase:

    def __init__(
        self,
        name: str,
        enable_new_client: bool,
        file_size: int,
        failure_at_absolute_offset: List[int],
        max_recovers_total: Union[int, None],
        max_recovers_without_progressing: Union[int, None],
        expected_success: bool,
        expected_requested_offsets: List[int],
    ):
        self.name = name
        self.enable_new_client = enable_new_client
        self.file_size = file_size
        self.failure_at_absolute_offset = failure_at_absolute_offset
        self.max_recovers_total = max_recovers_total
        self.max_recovers_without_progressing = max_recovers_without_progressing
        self.expected_success = expected_success
        self.expected_requested_offsets = expected_requested_offsets

    @staticmethod
    def to_string(test_case):
        return test_case.name

    def run(self, config: Config):
        config = config.copy()
        config.enable_experimental_files_api_client = self.enable_new_client
        config.files_api_client_download_max_total_recovers = self.max_recovers_total
        config.files_api_client_download_max_total_recovers_without_progressing = self.max_recovers_without_progressing

        w = WorkspaceClient(config=config)

        session = MockSession(self)
        w.files._api._api_client._session = session

        response = w.files.download("/test").contents
        if self.expected_success:
            actual_content = response.read()
            assert len(actual_content) == len(session.content)
            assert actual_content == session.content
        else:
            with pytest.raises(RequestException):
                response.read()

        received_requests = session.received_requests

        assert len(self.expected_requested_offsets) == len(received_requests)
        for idx, requested_offset in enumerate(self.expected_requested_offsets):
            assert requested_offset == received_requests[idx]._offset


class MockSession:

    def __init__(self, test_case: DownloadTestCase):
        self.test_case: DownloadTestCase = test_case
        self.received_requests: List[RequestData] = []
        self.content: bytes = os.urandom(self.test_case.file_size)
        self.failure_pointer = 0
        self.last_modified = "Thu, 28 Nov 2024 16:39:14 GMT"

    # following the signature of Session.request()
    def request(
        self,
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
        json=None,
    ):
        assert method == "GET"
        assert stream == True

        offset = 0
        if "Range" in headers:
            range = headers["Range"]
            match = re.search("^bytes=(\\d+)-$", range)
            if match:
                offset = int(match.group(1))
            else:
                raise Exception("Unexpected range header: " + range)

            if "If-Unmodified-Since" in headers:
                assert headers["If-Unmodified-Since"] == self.last_modified
            else:
                raise Exception("If-Unmodified-Since header should be passed along with Range")

        logger.info("Client requested offset: %s", offset)

        if offset > len(self.content):
            raise Exception("Offset %s exceeds file length %s", offset, len(self.content))

        self.received_requests.append(RequestData(offset))
        return MockResponse(self, offset, MockRequest(url))


# required only for correct logging
class MockRequest:

    def __init__(self, url: str):
        self.url = url
        self.method = "GET"
        self.headers = dict()
        self.body = None


class MockResponse:

    def __init__(self, session: MockSession, offset: int, request: MockRequest):
        self.session = session
        self.offset = offset
        self.request = request
        self.status_code = 200
        self.reason = "OK"
        self.headers = dict()
        self.headers["Content-Length"] = len(session.content) - offset
        self.headers["Content-Type"] = "application/octet-stream"
        self.headers["Last-Modified"] = session.last_modified
        self.ok = True
        self.url = request.url

    def iter_content(self, chunk_size: int, decode_unicode: bool):
        assert decode_unicode == False
        return MockIterator(self, chunk_size)


class MockIterator:

    def __init__(self, response: MockResponse, chunk_size: int):
        self.response = response
        self.chunk_size = chunk_size
        self.offset = 0

    def __next__(self):
        start_offset = self.response.offset + self.offset
        if start_offset == len(self.response.session.content):
            raise StopIteration

        end_offset = start_offset + self.chunk_size  # exclusive, might be out of range

        if self.response.session.failure_pointer < len(self.response.session.test_case.failure_at_absolute_offset):
            failure_after_byte = self.response.session.test_case.failure_at_absolute_offset[
                self.response.session.failure_pointer
            ]
            if failure_after_byte < end_offset:
                self.response.session.failure_pointer += 1
                raise RequestException("Fake error")

        result = self.response.session.content[start_offset:end_offset]
        self.offset += len(result)
        return result

    def close(self):
        pass


class _Constants:
    underlying_chunk_size = 1024 * 1024  # see ticket #832


@pytest.mark.parametrize(
    "test_case",
    [
        DownloadTestCase(
            name="Old client: no failures, file of 5 bytes",
            enable_new_client=False,
            file_size=5,
            failure_at_absolute_offset=[],
            max_recovers_total=0,
            max_recovers_without_progressing=0,
            expected_success=True,
            expected_requested_offsets=[0],
        ),
        DownloadTestCase(
            name="Old client: no failures, file of 1.5 chunks",
            enable_new_client=False,
            file_size=int(1.5 * _Constants.underlying_chunk_size),
            failure_at_absolute_offset=[],
            max_recovers_total=0,
            max_recovers_without_progressing=0,
            expected_success=True,
            expected_requested_offsets=[0],
        ),
        DownloadTestCase(
            name="Old client: failure",
            enable_new_client=False,
            file_size=1024,
            failure_at_absolute_offset=[100],
            max_recovers_total=None,  # unlimited but ignored
            max_recovers_without_progressing=None,  # unlimited but ignored
            expected_success=False,
            expected_requested_offsets=[0],
        ),
        DownloadTestCase(
            name="New client: no failures, file of 5 bytes",
            enable_new_client=True,
            file_size=5,
            failure_at_absolute_offset=[],
            max_recovers_total=0,
            max_recovers_without_progressing=0,
            expected_success=True,
            expected_requested_offsets=[0],
        ),
        DownloadTestCase(
            name="New client: no failures, file of 1 Kb",
            enable_new_client=True,
            file_size=1024,
            max_recovers_total=None,
            max_recovers_without_progressing=None,
            failure_at_absolute_offset=[],
            expected_success=True,
            expected_requested_offsets=[0],
        ),
        DownloadTestCase(
            name="New client: no failures, file of 1.5 chunks",
            enable_new_client=True,
            file_size=int(1.5 * _Constants.underlying_chunk_size),
            failure_at_absolute_offset=[],
            max_recovers_total=0,
            max_recovers_without_progressing=0,
            expected_success=True,
            expected_requested_offsets=[0],
        ),
        DownloadTestCase(
            name="New client: no failures, file of 10 chunks",
            enable_new_client=True,
            file_size=10 * _Constants.underlying_chunk_size,
            failure_at_absolute_offset=[],
            max_recovers_total=0,
            max_recovers_without_progressing=0,
            expected_success=True,
            expected_requested_offsets=[0],
        ),
        DownloadTestCase(
            name="New client: recovers are disabled, first failure leads to download abort",
            enable_new_client=True,
            file_size=10000,
            failure_at_absolute_offset=[5],
            max_recovers_total=0,
            max_recovers_without_progressing=0,
            expected_success=False,
            expected_requested_offsets=[0],
        ),
        DownloadTestCase(
            name="New client: unlimited recovers allowed",
            enable_new_client=True,
            file_size=_Constants.underlying_chunk_size * 5,
            # causes errors on requesting the third chunk
            failure_at_absolute_offset=[
                _Constants.underlying_chunk_size - 1,
                _Constants.underlying_chunk_size - 1,
                _Constants.underlying_chunk_size - 1,
                _Constants.underlying_chunk_size + 1,
                _Constants.underlying_chunk_size * 3,
            ],
            max_recovers_total=None,
            max_recovers_without_progressing=None,
            expected_success=True,
            expected_requested_offsets=[
                0,
                0,
                0,
                0,
                _Constants.underlying_chunk_size,
                _Constants.underlying_chunk_size * 3,
            ],
        ),
        DownloadTestCase(
            name="New client: we respect limit on total recovers when progressing",
            enable_new_client=True,
            file_size=_Constants.underlying_chunk_size * 10,
            failure_at_absolute_offset=[
                1,
                _Constants.underlying_chunk_size + 1,  # progressing
                _Constants.underlying_chunk_size * 2 + 1,  # progressing
                _Constants.underlying_chunk_size * 3 + 1,  # progressing
            ],
            max_recovers_total=3,
            max_recovers_without_progressing=None,
            expected_success=False,
            expected_requested_offsets=[
                0,
                0,
                _Constants.underlying_chunk_size * 1,
                _Constants.underlying_chunk_size * 2,
            ],
        ),
        DownloadTestCase(
            name="New client: we respect limit on total recovers when not progressing",
            enable_new_client=True,
            file_size=_Constants.underlying_chunk_size * 10,
            failure_at_absolute_offset=[1, 1, 1, 1],
            max_recovers_total=3,
            max_recovers_without_progressing=None,
            expected_success=False,
            expected_requested_offsets=[0, 0, 0, 0],
        ),
        DownloadTestCase(
            name="New client: we respect limit on non-progressing recovers",
            enable_new_client=True,
            file_size=_Constants.underlying_chunk_size * 2,
            failure_at_absolute_offset=[
                _Constants.underlying_chunk_size - 1,
                _Constants.underlying_chunk_size - 1,
                _Constants.underlying_chunk_size - 1,
                _Constants.underlying_chunk_size - 1,
            ],
            max_recovers_total=None,
            max_recovers_without_progressing=3,
            expected_success=False,
            expected_requested_offsets=[0, 0, 0, 0],
        ),
        DownloadTestCase(
            name="New client: non-progressing recovers count is reset when progressing",
            enable_new_client=True,
            file_size=_Constants.underlying_chunk_size * 10,
            failure_at_absolute_offset=[
                _Constants.underlying_chunk_size + 1,  # this recover is after progressing
                _Constants.underlying_chunk_size + 1,  # this is not
                _Constants.underlying_chunk_size * 2 + 1,  # this recover is after progressing
                _Constants.underlying_chunk_size * 2 + 1,  # this is not
                _Constants.underlying_chunk_size * 2 + 1,  # this is not, we abort here
            ],
            max_recovers_total=None,
            max_recovers_without_progressing=2,
            expected_success=False,
            expected_requested_offsets=[
                0,
                _Constants.underlying_chunk_size,
                _Constants.underlying_chunk_size,
                _Constants.underlying_chunk_size * 2,
                _Constants.underlying_chunk_size * 2,
            ],
        ),
        DownloadTestCase(
            name="New client: non-progressing recovers count is reset when progressing - 2",
            enable_new_client=True,
            file_size=_Constants.underlying_chunk_size * 10,
            failure_at_absolute_offset=[
                1,
                _Constants.underlying_chunk_size + 1,
                _Constants.underlying_chunk_size * 2 + 1,
                _Constants.underlying_chunk_size * 3 + 1,
            ],
            max_recovers_total=None,
            max_recovers_without_progressing=1,
            expected_success=True,
            expected_requested_offsets=[
                0,
                0,
                _Constants.underlying_chunk_size,
                _Constants.underlying_chunk_size * 2,
                _Constants.underlying_chunk_size * 3,
            ],
        ),
    ],
    ids=DownloadTestCase.to_string,
)
def test_download_recover(config: Config, test_case: DownloadTestCase):
    test_case.run(config)


class FileContent:

    def __init__(self, length: int, checksum: str):
        self._length = length
        self.checksum = checksum

    @classmethod
    def from_bytes(cls, data: bytes):
        sha256 = hashlib.sha256()
        sha256.update(data)
        return FileContent(len(data), sha256.hexdigest())

    def __repr__(self):
        return f"Length: {self._length}, checksum: {self.checksum}"

    def __eq__(self, other):
        if not isinstance(other, FileContent):
            return NotImplemented
        return self._length == other._length and self.checksum == other.checksum


class MultipartUploadServerState:
    upload_chunk_url_prefix = "https://cloud_provider.com/upload-chunk/"
    abort_upload_url_prefix = "https://cloud_provider.com/abort-upload/"

    def __init__(self):
        self.issued_multipart_urls = {}  # part_number -> expiration_time
        self.uploaded_chunks = {}  # part_number -> [chunk file path, etag]
        self.session_token = "token-" + MultipartUploadServerState.randomstr()
        self.file_content = None
        self.issued_abort_url_expire_time = None
        self.aborted = False

    def create_upload_chunk_url(self, path: str, part_number: int, expire_time: datetime) -> str:
        assert not self.aborted
        # client may have requested a URL for the same part if retrying on network error
        self.issued_multipart_urls[part_number] = expire_time
        return f"{self.upload_chunk_url_prefix}{path}/{part_number}"

    def create_abort_url(self, path: str, expire_time: datetime) -> str:
        assert not self.aborted
        self.issued_abort_url_expire_time = expire_time
        return f"{self.abort_upload_url_prefix}{path}"

    def save_part(self, part_number: int, part_content: bytes, etag: str):
        assert not self.aborted
        assert len(part_content) > 0

        logger.info(f"Saving part {part_number} of size {len(part_content)}")

        # chunk might already have been uploaded
        existing_chunk = self.uploaded_chunks.get(part_number)
        if existing_chunk:
            chunk_file = existing_chunk[0]
            with open(chunk_file, "wb") as f:
                f.write(part_content)
        else:
            fd, chunk_file = mkstemp()
            with open(fd, "wb") as f:
                f.write(part_content)

        self.uploaded_chunks[part_number] = [chunk_file, etag]

    def cleanup(self):
        for [file, _] in self.uploaded_chunks.values():
            os.remove(file)

    def get_file_content(self) -> FileContent:
        assert not self.aborted
        return self.file_content

    def upload_complete(self, etags: dict):
        assert not self.aborted
        # validate etags
        expected_etags = {}
        for part_number in self.uploaded_chunks.keys():
            expected_etags[part_number] = self.uploaded_chunks[part_number][1]
        assert etags == expected_etags

        size = 0
        sha256 = hashlib.sha256()

        sorted_chunks = sorted(self.uploaded_chunks.keys())
        for part_number in sorted_chunks:
            [chunk_path, _] = self.uploaded_chunks[part_number]
            size += os.path.getsize(chunk_path)
            with open(chunk_path, "rb") as f:
                chunk_content = f.read()
                sha256.update(chunk_content)

        self.file_content = FileContent(size, sha256.hexdigest())

    def abort_upload(self):
        self.aborted = True

    @staticmethod
    def randomstr():
        return f"{random.randrange(10000)}-{int(time.time())}"


class CustomResponse:
    """Custom response allows to override the "default" response generated by the server
    with the "custom" response to simulate failure error code, unexpected response body or
    network error.

    The server is represented by the `processor` parameter in `generate_response()` call.
    """

    def __init__(
        self,
        # If False, default response is always returned.
        # If True, response is defined by the current invocation count
        # with respect to first_invocation / last_invocation / only_invocation
        enabled=True,
        # Custom code to return
        code: Optional[int] = 200,
        # Custom body to return
        body: Optional[str] = None,
        # Custom exception to raise
        exception: Optional[Type[BaseException]] = None,
        # Whether exception should be raised before calling processor()
        # (so changing server state)
        exception_happened_before_processing: bool = False,
        # First invocation (1-based) at which return custom response
        first_invocation: Optional[int] = None,
        # Last invocation (1-based) at which return custom response
        last_invocation: Optional[int] = None,
        # Only invocation (1-based) at which return custom response
        only_invocation: Optional[int] = None,
    ):
        self.enabled = enabled
        self.code = code
        self.body = body
        self.exception = exception
        self.exception_happened_before_processing = exception_happened_before_processing
        self.first_invocation = first_invocation
        self.last_invocation = last_invocation
        self.only_invocation = only_invocation

        if self.only_invocation and (self.first_invocation or self.last_invocation):
            raise ValueError("Cannot set both only invocation and first/last invocation")

        if self.exception_happened_before_processing and not self.exception:
            raise ValueError("Exception is not defined")

        self.invocation_count = 0

    def invocation_matches(self):
        if not self.enabled:
            return False

        self.invocation_count += 1

        if self.only_invocation:
            return self.invocation_count == self.only_invocation

        if self.first_invocation and self.invocation_count < self.first_invocation:
            return False
        if self.last_invocation and self.invocation_count > self.last_invocation:
            return False
        return True

    def generate_response(self, request: requests.Request, processor: Callable[[], list]):
        activate_for_current_invocation = self.invocation_matches()

        if activate_for_current_invocation and self.exception and self.exception_happened_before_processing:
            # if network exception is thrown while processing a request, it's not defined
            # if server actually processed the request (and so changed its state)
            raise self.exception

        custom_response = [self.code, self.body or "", {}]

        if activate_for_current_invocation:
            if self.code and 400 <= self.code < 500:
                # if server returns client error, it's not supposed to change its state,
                # so we're not calling processor()
                [code, body, headers] = custom_response
            else:
                # we're calling processor() but override its response with the custom one
                processor()
                [code, body, headers] = custom_response
        else:
            [code, body, headers] = processor()

        if activate_for_current_invocation and self.exception:
            # self.exception_happened_before_processing is False
            raise self.exception

        resp = requests.Response()

        resp.request = request
        resp.status_code = code
        resp._content = body.encode()

        for key in headers:
            resp.headers[key] = headers[key]

        return resp


class MultipartUploadTestCase:
    """Test case for multipart upload of a file. Multipart uploads are used on AWS and Azure.

    Multipart upload via presigned URLs involves multiple HTTP requests:
    - initiating upload (call to Databricks Files API)
    - requesting upload part URLs (calls to Databricks Files API)
    - uploading data in chunks (calls to cloud storage provider or Databricks storage proxy)
    - completing the upload (call to Databricks Files API)
    - requesting abort upload URL (call to Databricks Files API)
    - aborting the upload (call to cloud storage provider or Databricks storage proxy)

    Test case uses requests-mock library to mock all these requests. Within a test, mocks use
    shared server state that tracks the upload. Mocks generate the "default" (successful) response.

    Response of each call can be modified by parameterising a respective `CustomResponse` object.
    """

    path = "/test.txt"

    expired_url_aws_response = (
        '<?xml version="1.0" encoding="utf-8"?><Error><Code>'
        "AuthenticationFailed</Code><Message>Server failed to authenticate "
        "the request. Make sure the value of Authorization header is formed "
        "correctly including the signature.\nRequestId:1abde581-601e-0028-"
        "4a6d-5c3952000000\nTime:2025-01-01T16:54:20.5343181Z</Message"
        "><AuthenticationErrorDetail>Signature not valid in the specified "
        "time frame: Start [Wed, 01 Jan 2025 16:38:41 GMT] - Expiry [Wed, "
        "01 Jan 2025 16:53:45 GMT] - Current [Wed, 01 Jan 2025 16:54:20 "
        "GMT]</AuthenticationErrorDetail></Error>"
    )

    expired_url_azure_response = (
        '<?xml version="1.0" encoding="UTF-8"?>\n<Error><Code>AccessDenied'
        "</Code><Message>Request has expired</Message><X-Amz-Expires>"
        "14</X-Amz-Expires><Expires>2025-01-01T17:47:13Z</Expires>"
        "<ServerTime>2025-01-01T17:48:01Z</ServerTime><RequestId>"
        "JY66KDXM4CXBZ7X2</RequestId><HostId>n8Qayqg60rbvut9P7pk0</HostId>"
        "</Error>"
    )

    # TODO test for overwrite = false

    def __init__(
        self,
        name: str,
        stream_size: int,  # size of uploaded file or, technically, stream
        multipart_upload_chunk_size: Optional[int] = None,
        sdk_retry_timeout_seconds: Optional[int] = None,
        multipart_upload_max_retries: Optional[int] = None,
        multipart_upload_batch_url_count: Optional[int] = None,
        custom_response_on_initiate=CustomResponse(enabled=False),
        custom_response_on_create_multipart_url=CustomResponse(enabled=False),
        custom_response_on_upload=CustomResponse(enabled=False),
        custom_response_on_complete=CustomResponse(enabled=False),
        custom_response_on_create_abort_url=CustomResponse(enabled=False),
        custom_response_on_abort=CustomResponse(enabled=False),
        # exception which is expected to be thrown (so upload is expected to have failed)
        expected_exception_type: Optional[Type[BaseException]] = None,
        # if abort is expected to be called
        expected_aborted: bool = False,
    ):
        self.name = name
        self.stream_size = stream_size
        self.multipart_upload_chunk_size = multipart_upload_chunk_size
        self.sdk_retry_timeout_seconds = sdk_retry_timeout_seconds
        self.multipart_upload_max_retries = multipart_upload_max_retries
        self.multipart_upload_batch_url_count = multipart_upload_batch_url_count
        self.custom_response_on_initiate = copy.deepcopy(custom_response_on_initiate)
        self.custom_response_on_create_multipart_url = copy.deepcopy(custom_response_on_create_multipart_url)
        self.custom_response_on_upload = copy.deepcopy(custom_response_on_upload)
        self.custom_response_on_complete = copy.deepcopy(custom_response_on_complete)
        self.custom_response_on_create_abort_url = copy.deepcopy(custom_response_on_create_abort_url)
        self.custom_response_on_abort = copy.deepcopy(custom_response_on_abort)
        self.expected_exception_type = expected_exception_type
        self.expected_aborted: bool = expected_aborted

    def setup_session_mock(self, session_mock: requests_mock.Mocker, server_state: MultipartUploadServerState):

        def custom_matcher(request):
            request_url = urlparse(request.url)
            request_query = parse_qs(request_url.query)

            # initial request
            if (
                request_url.hostname == "localhost"
                and request_url.path == f"/api/2.0/fs/files{MultipartUploadTestCase.path}"
                and request_query.get("action") == ["initiate-upload"]
                and request.method == "POST"
            ):

                assert MultipartUploadTestCase.is_auth_header_present(request)
                assert request.text is None

                def processor():
                    response_json = {"multipart_upload": {"session_token": server_state.session_token}}
                    return [200, json.dumps(response_json), {}]

                return self.custom_response_on_initiate.generate_response(request, processor)

            # multipart upload, create upload part URLs
            elif (
                request_url.hostname == "localhost"
                and request_url.path == "/api/2.0/fs/create-upload-part-urls"
                and request.method == "POST"
            ):

                assert MultipartUploadTestCase.is_auth_header_present(request)

                request_json = request.json()
                assert request_json.keys() == {"count", "expire_time", "path", "session_token", "start_part_number"}
                assert request_json["path"] == self.path
                assert request_json["session_token"] == server_state.session_token

                start_part_number = int(request_json["start_part_number"])
                count = int(request_json["count"])
                assert count >= 1

                expire_time = MultipartUploadTestCase.parse_and_validate_expire_time(request_json["expire_time"])

                def processor():
                    response_nodes = []
                    for part_number in range(start_part_number, start_part_number + count):
                        upload_part_url = server_state.create_upload_chunk_url(self.path, part_number, expire_time)
                        response_nodes.append(
                            {
                                "part_number": part_number,
                                "url": upload_part_url,
                                "headers": [{"name": "name1", "value": "value1"}],
                            }
                        )

                    response_json = {"upload_part_urls": response_nodes}
                    return [200, json.dumps(response_json), {}]

                return self.custom_response_on_create_multipart_url.generate_response(request, processor)

            # multipart upload, uploading part
            elif request.url.startswith(MultipartUploadServerState.upload_chunk_url_prefix) and request.method == "PUT":

                assert not MultipartUploadTestCase.is_auth_header_present(request)

                url_path = request.url[len(MultipartUploadServerState.abort_upload_url_prefix) :]
                part_num = url_path.split("/")[-1]
                assert url_path[: -len(part_num) - 1] == self.path

                def processor():
                    body = request.body.read()
                    etag = "etag-" + MultipartUploadServerState.randomstr()
                    server_state.save_part(int(part_num), body, etag)
                    return [200, "", {"ETag": etag}]

                return self.custom_response_on_upload.generate_response(request, processor)

            # multipart upload, completion
            elif (
                request_url.hostname == "localhost"
                and request_url.path == f"/api/2.0/fs/files{MultipartUploadTestCase.path}"
                and request_query.get("action") == ["complete-upload"]
                and request_query.get("upload_type") == ["multipart"]
                and request.method == "POST"
            ):

                assert MultipartUploadTestCase.is_auth_header_present(request)
                assert [server_state.session_token] == request_query.get("session_token")

                def processor():
                    request_json = request.json()
                    etags = {}

                    for part in request_json["parts"]:
                        etags[part["part_number"]] = part["etag"]

                    server_state.upload_complete(etags)
                    return [200, "", {}]

                return self.custom_response_on_complete.generate_response(request, processor)

            # create abort URL
            elif request.url == "http://localhost/api/2.0/fs/create-abort-upload-url" and request.method == "POST":
                assert MultipartUploadTestCase.is_auth_header_present(request)
                request_json = request.json()
                assert request_json["path"] == self.path
                expire_time = MultipartUploadTestCase.parse_and_validate_expire_time(request_json["expire_time"])

                def processor():
                    response_json = {
                        "abort_upload_url": {
                            "url": server_state.create_abort_url(self.path, expire_time),
                            "headers": [{"name": "header1", "value": "headervalue1"}],
                        }
                    }
                    return [200, json.dumps(response_json), {}]

                return self.custom_response_on_create_abort_url.generate_response(request, processor)

            # abort upload
            elif (
                request.url.startswith(MultipartUploadServerState.abort_upload_url_prefix)
                and request.method == "DELETE"
            ):
                assert not MultipartUploadTestCase.is_auth_header_present(request)
                assert request.url[len(MultipartUploadServerState.abort_upload_url_prefix) :] == self.path

                def processor():
                    server_state.abort_upload()
                    return [200, "", {}]

                return self.custom_response_on_abort.generate_response(request, processor)

            return None

        session_mock.add_matcher(matcher=custom_matcher)

    @staticmethod
    def setup_token_auth(config: Config):
        pat_token = "some_pat_token"
        config._header_factory = lambda: {"Authorization": f"Bearer {pat_token}"}

    @staticmethod
    def is_auth_header_present(r: requests.Request):
        return r.headers.get("Authorization") is not None

    @staticmethod
    def parse_and_validate_expire_time(s: str) -> datetime:
        expire_time = datetime.strptime(s, "%Y-%m-%dT%H:%M:%SZ")
        expire_time = expire_time.replace(tzinfo=timezone.utc)  # Explicitly add timezone
        now = datetime.now(timezone.utc)
        max_expiration = now + timedelta(hours=2)
        assert now < expire_time < max_expiration
        return expire_time

    def run(self, config: Config):
        config = config.copy()

        MultipartUploadTestCase.setup_token_auth(config)

        if self.sdk_retry_timeout_seconds:
            config.retry_timeout_seconds = self.sdk_retry_timeout_seconds
        if self.multipart_upload_chunk_size:
            config.multipart_upload_chunk_size = self.multipart_upload_chunk_size
        if self.multipart_upload_max_retries:
            config.multipart_upload_max_retries = self.multipart_upload_max_retries
        if self.multipart_upload_batch_url_count:
            config.multipart_upload_batch_url_count = self.multipart_upload_batch_url_count
        config.enable_experimental_files_api_client = True
        config.multipart_upload_min_stream_size = 0  # disable single-shot uploads

        file_content = os.urandom(self.stream_size)

        upload_state = MultipartUploadServerState()

        try:
            w = WorkspaceClient(config=config)
            with requests_mock.Mocker() as session_mock:
                self.setup_session_mock(session_mock, upload_state)

                def upload():
                    w.files.upload("/test.txt", io.BytesIO(file_content), overwrite=True)

                if self.expected_exception_type is not None:
                    with pytest.raises(self.expected_exception_type):
                        upload()
                else:
                    upload()
                    actual_content = upload_state.get_file_content()
                    assert actual_content == FileContent.from_bytes(file_content)

            assert upload_state.aborted == self.expected_aborted

        finally:
            upload_state.cleanup()

    def __str__(self):
        return self.name

    @staticmethod
    def to_string(test_case):
        return str(test_case)


@pytest.mark.parametrize(
    "test_case",
    [
        # -------------------------- failures on "initiate upload" --------------------------
        MultipartUploadTestCase(
            "Initiate: 400 response is not retried",
            stream_size=1024 * 1024,
            custom_response_on_initiate=CustomResponse(code=400, only_invocation=1),
            expected_exception_type=BadRequest,
            expected_aborted=False,  # upload didn't start
        ),
        MultipartUploadTestCase(
            "Initiate: 403 response is not retried",
            stream_size=1024 * 1024,
            custom_response_on_initiate=CustomResponse(code=403, only_invocation=1),
            expected_exception_type=PermissionDenied,
            expected_aborted=False,  # upload didn't start
        ),
        MultipartUploadTestCase(
            "Initiate: 500 response is not retried",
            stream_size=1024 * 1024,
            custom_response_on_initiate=CustomResponse(code=500, only_invocation=1),
            expected_exception_type=InternalError,
            expected_aborted=False,  # upload didn't start
        ),
        MultipartUploadTestCase(
            "Initiate: non-JSON response is not retried",
            stream_size=1024 * 1024,
            custom_response_on_initiate=CustomResponse(body="this is not a JSON", only_invocation=1),
            expected_exception_type=requests.exceptions.JSONDecodeError,
            expected_aborted=False,  # upload didn't start
        ),
        MultipartUploadTestCase(
            "Initiate: meaningless JSON response is not retried",
            stream_size=1024 * 1024,
            custom_response_on_initiate=CustomResponse(body='{"foo": 123}', only_invocation=1),
            expected_exception_type=ValueError,
            expected_aborted=False,  # upload didn't start
        ),
        MultipartUploadTestCase(
            "Initiate: no session token in response is not retried",
            stream_size=1024 * 1024,
            custom_response_on_initiate=CustomResponse(
                body='{"multipart_upload":{"session_token1": "token123"}}', only_invocation=1
            ),
            expected_exception_type=ValueError,
            expected_aborted=False,  # upload didn't start
        ),
        MultipartUploadTestCase(
            "Initiate: permanent retryable exception",
            stream_size=1024 * 1024,
            custom_response_on_initiate=CustomResponse(exception=requests.ConnectionError),
            sdk_retry_timeout_seconds=30,  # let's not wait 5 min (SDK default timeout)
            expected_exception_type=TimeoutError,  # SDK throws this if retries are taking too long
            expected_aborted=False,  # upload didn't start
        ),
        MultipartUploadTestCase(
            "Initiate: intermittent retryable exception",
            stream_size=1024 * 1024,
            custom_response_on_initiate=CustomResponse(
                exception=requests.ConnectionError,
                # 3 calls fail, but request is successfully retried
                first_invocation=1,
                last_invocation=3,
            ),
            expected_aborted=False,
        ),
        MultipartUploadTestCase(
            "Initiate: intermittent retryable status code",
            stream_size=1024 * 1024,
            custom_response_on_initiate=CustomResponse(
                code=429,
                # 3 calls fail, then retry succeeds
                first_invocation=1,
                last_invocation=3,
            ),
            expected_aborted=False,
        ),
        # -------------------------- failures on "create upload URL" --------------------------
        MultipartUploadTestCase(
            "Create upload URL: 400 response is not retied",
            stream_size=1024 * 1024,
            custom_response_on_create_multipart_url=CustomResponse(
                code=400,
                # 1 failure is enough
                only_invocation=1,
            ),
            expected_exception_type=BadRequest,
            expected_aborted=True,
        ),
        MultipartUploadTestCase(
            "Create upload URL: 500 error is not retied",
            stream_size=1024 * 1024,
            custom_response_on_create_multipart_url=CustomResponse(code=500, only_invocation=1),
            expected_exception_type=InternalError,
            expected_aborted=True,
        ),
        MultipartUploadTestCase(
            "Create upload URL: non-JSON response is not retried",
            stream_size=1024 * 1024,
            custom_response_on_create_multipart_url=CustomResponse(body="this is not a JSON", only_invocation=1),
            expected_exception_type=requests.exceptions.JSONDecodeError,
            expected_aborted=True,
        ),
        MultipartUploadTestCase(
            "Create upload URL: meaningless JSON response is not retried",
            stream_size=1024 * 1024,
            custom_response_on_create_multipart_url=CustomResponse(body='{"foo":123}', only_invocation=1),
            expected_exception_type=ValueError,
            expected_aborted=True,
        ),
        MultipartUploadTestCase(
            "Create upload URL: meaningless JSON response is not retried 2",
            stream_size=1024 * 1024,
            custom_response_on_create_multipart_url=CustomResponse(body='{"upload_part_urls":[]}', only_invocation=1),
            expected_exception_type=ValueError,
            expected_aborted=True,
        ),
        MultipartUploadTestCase(
            "Create upload URL: meaningless JSON response is not retried 3",
            stream_size=1024 * 1024,
            custom_response_on_create_multipart_url=CustomResponse(
                body='{"upload_part_urls":[{"url":""}]}', only_invocation=1
            ),
            expected_exception_type=KeyError,  # TODO we might want to make JSON parsing more reliable
            expected_aborted=True,
        ),
        MultipartUploadTestCase(
            "Create upload URL: permanent retryable exception",
            stream_size=1024 * 1024,
            custom_response_on_create_multipart_url=CustomResponse(exception=requests.ConnectionError),
            sdk_retry_timeout_seconds=30,  # don't wait for 5 min (SDK default timeout)
            expected_exception_type=TimeoutError,
            expected_aborted=True,
        ),
        MultipartUploadTestCase(
            "Create upload URL: intermittent retryable exception",
            stream_size=1024 * 1024,
            custom_response_on_create_multipart_url=CustomResponse(
                exception=requests.Timeout,
                # happens only once, retry succeeds
                only_invocation=1,
            ),
            expected_aborted=False,
        ),
        MultipartUploadTestCase(
            "Create upload URL: intermittent retryable exception 2",
            stream_size=100 * 1024 * 1024,  # 10 chunks
            multipart_upload_chunk_size=10 * 1024 * 1024,
            custom_response_on_create_multipart_url=CustomResponse(
                exception=requests.Timeout,
                # 4th request for multipart URLs fails 3 times, then retry succeeds
                first_invocation=4,
                last_invocation=6,
            ),
            expected_aborted=False,
        ),
        # -------------------------- failures on chunk upload --------------------------
        MultipartUploadTestCase(
            "Upload chunk: 403 response is not retried",
            stream_size=100 * 1024 * 1024,  # 10 chunks
            multipart_upload_chunk_size=10 * 1024 * 1024,
            custom_response_on_upload=CustomResponse(
                code=403,
                # fail only once
                only_invocation=1,
            ),
            expected_exception_type=PermissionDenied,
            expected_aborted=True,
        ),
        MultipartUploadTestCase(
            "Upload chunk: 400 response is not retried",
            stream_size=100 * 1024 * 1024,  # 10 chunks
            multipart_upload_chunk_size=10 * 1024 * 1024,
            custom_response_on_upload=CustomResponse(
                code=400,
                # fail once, but not on the first chunk
                only_invocation=3,
            ),
            expected_exception_type=BadRequest,
            expected_aborted=True,
        ),
        MultipartUploadTestCase(
            "Upload chunk: 500 response is not retried",
            stream_size=100 * 1024 * 1024,  # 10 chunks
            multipart_upload_chunk_size=10 * 1024 * 1024,
            custom_response_on_upload=CustomResponse(code=500, only_invocation=5),
            expected_exception_type=InternalError,
            expected_aborted=True,
        ),
        MultipartUploadTestCase(
            "Upload chunk: expired URL is retried on AWS",
            stream_size=100 * 1024 * 1024,  # 10 chunks
            multipart_upload_chunk_size=10 * 1024 * 1024,
            custom_response_on_upload=CustomResponse(
                code=403, body=MultipartUploadTestCase.expired_url_aws_response, only_invocation=2
            ),
            expected_aborted=False,
        ),
        MultipartUploadTestCase(
            "Upload chunk: expired URL is retried on Azure",
            multipart_upload_max_retries=3,
            stream_size=100 * 1024 * 1024,  # 10 chunks
            multipart_upload_chunk_size=10 * 1024 * 1024,
            custom_response_on_upload=CustomResponse(
                code=403,
                body=MultipartUploadTestCase.expired_url_azure_response,
                # 3 failures don't exceed multipart_upload_max_retries
                first_invocation=2,
                last_invocation=4,
            ),
            expected_aborted=False,
        ),
        MultipartUploadTestCase(
            "Upload chunk: expired URL is retried on Azure, requesting urls by 6",
            multipart_upload_max_retries=3,
            multipart_upload_batch_url_count=6,
            stream_size=100 * 1024 * 1024,  # 100 chunks
            multipart_upload_chunk_size=1 * 1024 * 1024,
            custom_response_on_upload=CustomResponse(
                code=403,
                body=MultipartUploadTestCase.expired_url_azure_response,
                # 3 failures don't exceed multipart_upload_max_retries
                first_invocation=2,
                last_invocation=4,
            ),
            expected_aborted=False,
        ),
        MultipartUploadTestCase(
            "Upload chunk: expired URL retry is exhausted",
            multipart_upload_max_retries=3,
            stream_size=100 * 1024 * 1024,  # 10 chunks
            multipart_upload_chunk_size=10 * 1024 * 1024,
            custom_response_on_upload=CustomResponse(
                code=403,
                body=MultipartUploadTestCase.expired_url_azure_response,
                # 4 failures exceed multipart_upload_max_retries
                first_invocation=2,
                last_invocation=5,
            ),
            expected_exception_type=ValueError,
            expected_aborted=True,
        ),
        MultipartUploadTestCase(
            "Upload chunk: permanent retryable error",
            stream_size=100 * 1024 * 1024,  # 10 chunks
            multipart_upload_chunk_size=10 * 1024 * 1024,
            sdk_retry_timeout_seconds=30,  # don't wait for 5 min (SDK default timeout)
            custom_response_on_upload=CustomResponse(exception=requests.ConnectionError, first_invocation=8),
            expected_exception_type=TimeoutError,
            expected_aborted=True,
        ),
        MultipartUploadTestCase(
            "Upload chunk: permanent retryable status code",
            stream_size=100 * 1024 * 1024,  # 10 chunks
            multipart_upload_chunk_size=10 * 1024 * 1024,
            sdk_retry_timeout_seconds=30,  # don't wait for 5 min (SDK default timeout)
            custom_response_on_upload=CustomResponse(code=429, first_invocation=8),
            expected_exception_type=TimeoutError,
            expected_aborted=True,
        ),
        MultipartUploadTestCase(
            "Upload chunk: intermittent retryable error",
            stream_size=100 * 1024 * 1024,  # 10 chunks
            multipart_upload_chunk_size=10 * 1024 * 1024,
            custom_response_on_upload=CustomResponse(
                exception=requests.ConnectionError, first_invocation=2, last_invocation=5
            ),
            expected_aborted=False,
        ),
        MultipartUploadTestCase(
            "Upload chunk: intermittent retryable status code",
            stream_size=100 * 1024 * 1024,  # 10 chunks
            multipart_upload_chunk_size=10 * 1024 * 1024,
            custom_response_on_upload=CustomResponse(code=429, first_invocation=2, last_invocation=4),
            expected_aborted=False,
        ),
        # -------------------------- failures on abort --------------------------
        MultipartUploadTestCase(
            "Abort URL: 500 response",
            stream_size=1024 * 1024,
            custom_response_on_create_multipart_url=CustomResponse(code=500, only_invocation=1),
            custom_response_on_create_abort_url=CustomResponse(code=400),
            expected_exception_type=InternalError,  # original error
            expected_aborted=False,  # server state didn't change to record abort
        ),
        MultipartUploadTestCase(
            "Abort URL: 403 response",
            stream_size=1024 * 1024,
            custom_response_on_upload=CustomResponse(code=500, only_invocation=1),
            custom_response_on_create_abort_url=CustomResponse(code=403),
            expected_exception_type=InternalError,  # original error
            expected_aborted=False,  # server state didn't change to record abort
        ),
        MultipartUploadTestCase(
            "Abort URL: intermittent retryable error",
            stream_size=1024 * 1024,
            custom_response_on_create_multipart_url=CustomResponse(code=500, only_invocation=1),
            custom_response_on_create_abort_url=CustomResponse(code=429, first_invocation=1, last_invocation=3),
            expected_exception_type=InternalError,  # original error
            expected_aborted=True,  # abort successfully called after abort URL creation is retried
        ),
        MultipartUploadTestCase(
            "Abort URL: intermittent retryable error 2",
            stream_size=1024 * 1024,
            custom_response_on_create_multipart_url=CustomResponse(code=500, only_invocation=1),
            custom_response_on_create_abort_url=CustomResponse(
                exception=requests.Timeout, first_invocation=1, last_invocation=3
            ),
            expected_exception_type=InternalError,  # original error
            expected_aborted=True,  # abort successfully called after abort URL creation is retried
        ),
        MultipartUploadTestCase(
            "Abort: exception",
            stream_size=1024 * 1024,
            # don't wait for 5 min (SDK default timeout)
            sdk_retry_timeout_seconds=30,
            custom_response_on_create_multipart_url=CustomResponse(code=403, only_invocation=1),
            custom_response_on_abort=CustomResponse(
                exception=requests.Timeout,
                # this allows to change the server state to "aborted"
                exception_happened_before_processing=False,
            ),
            expected_exception_type=PermissionDenied,  # original error is reported
            expected_aborted=True,
        ),
        # -------------------------- happy cases --------------------------
        MultipartUploadTestCase(
            "Multipart upload successful: single chunk",
            stream_size=1024 * 1024,  # less than chunk size
            multipart_upload_chunk_size=10 * 1024 * 1024,
        ),
        MultipartUploadTestCase(
            "Multipart upload successful: multiple chunks (aligned)",
            stream_size=100 * 1024 * 1024,  # 10 chunks
            multipart_upload_chunk_size=10 * 1024 * 1024,
        ),
        MultipartUploadTestCase(
            "Multipart upload successful: multiple chunks (aligned), upload urls by 3",
            multipart_upload_batch_url_count=3,
            stream_size=100 * 1024 * 1024,  # 10 chunks
            multipart_upload_chunk_size=10 * 1024 * 1024,
        ),
        MultipartUploadTestCase(
            "Multipart upload successful: multiple chunks (not aligned), upload urls by 1",
            stream_size=100 * 1024 * 1024 + 1566,  # 14 full chunks + remainder
            multipart_upload_chunk_size=7 * 1024 * 1024 - 17,
        ),
        MultipartUploadTestCase(
            "Multipart upload successful: multiple chunks (not aligned), upload urls by 5",
            multipart_upload_batch_url_count=5,
            stream_size=100 * 1024 * 1024 + 1566,  # 14 full chunks + remainder
            multipart_upload_chunk_size=7 * 1024 * 1024 - 17,
        ),
    ],
    ids=MultipartUploadTestCase.to_string,
)
def test_multipart_upload(config: Config, test_case: MultipartUploadTestCase):
    test_case.run(config)


class SingleShotUploadState:

    def __init__(self):
        self.single_shot_file_content = None


class SingleShotUploadTestCase:

    def __init__(self, name: str, stream_size: int, multipart_upload_min_stream_size: int, expected_single_shot: bool):
        self.name = name
        self.stream_size = stream_size
        self.multipart_upload_min_stream_size = multipart_upload_min_stream_size
        self.expected_single_shot = expected_single_shot

    def __str__(self):
        return self.name

    @staticmethod
    def to_string(test_case):
        return str(test_case)

    def run(self, config: Config):
        config = config.copy()
        config.enable_experimental_files_api_client = True
        config.multipart_upload_min_stream_size = self.multipart_upload_min_stream_size

        file_content = os.urandom(self.stream_size)

        session = requests.Session()
        with requests_mock.Mocker(session=session) as session_mock:
            session_mock.get(f"http://localhost/api/2.0/fs/files{MultipartUploadTestCase.path}", status_code=200)

            upload_state = SingleShotUploadState()

            def custom_matcher(request):
                request_url = urlparse(request.url)
                request_query = parse_qs(request_url.query)

                if self.expected_single_shot:
                    if (
                        request_url.hostname == "localhost"
                        and request_url.path == f"/api/2.0/fs/files{MultipartUploadTestCase.path}"
                        and request.method == "PUT"
                    ):
                        body = request.body.read()
                        upload_state.single_shot_file_content = FileContent.from_bytes(body)

                        resp = requests.Response()
                        resp.status_code = 204
                        resp.request = request
                        resp._content = b""
                        return resp
                else:
                    if (
                        request_url.hostname == "localhost"
                        and request_url.path == f"/api/2.0/fs/files{MultipartUploadTestCase.path}"
                        and request_query.get("action") == ["initiate-upload"]
                        and request.method == "POST"
                    ):

                        resp = requests.Response()
                        resp.status_code = 403  # this will throw, that's fine
                        resp.request = request
                        resp._content = b""
                        return resp

                return None

            session_mock.add_matcher(matcher=custom_matcher)

            w = WorkspaceClient(config=config)
            w.files._api._api_client._session = session

            def upload():
                w.files.upload("/test.txt", io.BytesIO(file_content), overwrite=True)

            if self.expected_single_shot:
                upload()
                actual_content = upload_state.single_shot_file_content
                assert actual_content == FileContent.from_bytes(file_content)
            else:
                with pytest.raises(PermissionDenied):
                    upload()


@pytest.mark.parametrize(
    "test_case",
    [
        SingleShotUploadTestCase(
            "Single-shot upload",
            stream_size=1024 * 1024,
            multipart_upload_min_stream_size=1024 * 1024 + 1,
            expected_single_shot=True,
        ),
        SingleShotUploadTestCase(
            "Multipart upload 1",
            stream_size=1024 * 1024,
            multipart_upload_min_stream_size=1024 * 1024,
            expected_single_shot=False,
        ),
        SingleShotUploadTestCase(
            "Multipart upload 2",
            stream_size=1024 * 1024,
            multipart_upload_min_stream_size=0,
            expected_single_shot=False,
        ),
    ],
    ids=SingleShotUploadTestCase.to_string,
)
def test_single_shot_upload(config: Config, test_case: SingleShotUploadTestCase):
    test_case.run(config)


class ResumableUploadServerState:
    resumable_upload_url_prefix = "https://cloud_provider.com/resumable-upload/"
    abort_upload_url_prefix = "https://cloud_provider.com/abort-upload/"

    def __init__(self, unconfirmed_delta: Union[int, list]):
        self.unconfirmed_delta = unconfirmed_delta
        self.confirmed_last_byte: Optional[int] = None  # inclusive
        self.uploaded_parts = []
        self.session_token = "token-" + MultipartUploadServerState.randomstr()
        self.file_content = None
        self.aborted = False

    def save_part(self, start_offset: int, end_offset_incl: int, part_content: bytes, file_size_s: str):
        assert not self.aborted

        assert len(part_content) > 0
        if self.confirmed_last_byte:
            assert start_offset == self.confirmed_last_byte + 1
        else:
            assert start_offset == 0

        assert end_offset_incl == start_offset + len(part_content) - 1

        is_last_part = file_size_s != "*"
        if is_last_part:
            assert int(file_size_s) == end_offset_incl + 1
        else:
            assert not self.file_content  # last chunk should not have been uploaded yet

        if isinstance(self.unconfirmed_delta, int):
            unconfirmed_delta = self.unconfirmed_delta
        elif len(self.uploaded_parts) < len(self.unconfirmed_delta):
            unconfirmed_delta = self.unconfirmed_delta[len(self.uploaded_parts)]
        else:
            unconfirmed_delta = self.unconfirmed_delta[-1]  # take the last delta

        if unconfirmed_delta >= len(part_content):
            unconfirmed_delta = 0  # otherwise we never finish

        logger.info(
            f"Saving part {len(self.uploaded_parts) + 1} of original size {len(part_content)} with unconfirmed delta {unconfirmed_delta}. is_last_part = {is_last_part}"
        )

        if unconfirmed_delta > 0:
            part_content = part_content[:-unconfirmed_delta]

        fd, chunk_file = mkstemp()
        with open(fd, "wb") as f:
            f.write(part_content)

        self.uploaded_parts.append(chunk_file)

        if is_last_part and unconfirmed_delta == 0:
            size = 0
            sha256 = hashlib.sha256()
            for chunk_path in self.uploaded_parts:
                size += os.path.getsize(chunk_path)
                with open(chunk_path, "rb") as f:
                    chunk_content = f.read()
                    sha256.update(chunk_content)

            assert size == end_offset_incl + 1
            self.file_content = FileContent(size, sha256.hexdigest())

        self.confirmed_last_byte = end_offset_incl - unconfirmed_delta

    def create_abort_url(self, path: str, expire_time: datetime) -> str:
        assert not self.aborted
        self.issued_abort_url_expire_time = expire_time
        return f"{self.abort_upload_url_prefix}{path}"

    def cleanup(self):
        for file in self.uploaded_parts:
            os.remove(file)

    def get_file_content(self) -> FileContent:
        assert not self.aborted
        return self.file_content

    def abort_upload(self):
        self.aborted = True


class ResumableUploadTestCase:
    """Test case for resumable upload of a file. Resumable uploads are used on GCP.

    Resumable upload involves multiple HTTP requests:
    - initiating upload (call to Databricks Files API)
    - requesting resumable upload URL (call to Databricks Files API)
    - uploading chunks of data (calls to cloud storage provider or Databricks storage proxy)
    - aborting the upload (call to cloud storage provider or Databricks storage proxy)

    Test case uses requests-mock library to mock all these requests. Within a test, mocks use
    shared server state that tracks the upload. Mocks generate the "default" (successful) response.

    Response of each call can be modified by parameterising a respective `CustomResponse` object.
    """

    path = "/test.txt"

    def __init__(
        self,
        name: str,
        stream_size: int,
        overwrite: bool = True,
        multipart_upload_chunk_size: Optional[int] = None,
        sdk_retry_timeout_seconds: Optional[int] = None,
        multipart_upload_max_retries: Optional[int] = None,
        # In resumable upload, when replying to chunk upload request, server returns
        # (confirms) last accepted byte offset for the client to resume upload after.
        #
        # `unconfirmed_delta` defines offset from the end of the chunk that remains
        # "unconfirmed", i.e. the last accepted offset would be (range_end - unconfirmed_delta).
        # Can be int (same for all chunks) or list (individual for each chunk).
        unconfirmed_delta: Union[int, list] = 0,
        custom_response_on_create_resumable_url=CustomResponse(enabled=False),
        custom_response_on_upload=CustomResponse(enabled=False),
        custom_response_on_status_check=CustomResponse(enabled=False),
        custom_response_on_abort=CustomResponse(enabled=False),
        # exception which is expected to be thrown (so upload is expected to have failed)
        expected_exception_type: Optional[Type[BaseException]] = None,
        # if abort is expected to be called
        expected_aborted: bool = False,
    ):
        self.name = name
        self.stream_size = stream_size
        self.overwrite = overwrite
        self.multipart_upload_chunk_size = multipart_upload_chunk_size
        self.sdk_retry_timeout_seconds = sdk_retry_timeout_seconds
        self.multipart_upload_max_retries = multipart_upload_max_retries
        self.unconfirmed_delta = unconfirmed_delta
        self.custom_response_on_create_resumable_url = copy.deepcopy(custom_response_on_create_resumable_url)
        self.custom_response_on_upload = copy.deepcopy(custom_response_on_upload)
        self.custom_response_on_status_check = copy.deepcopy(custom_response_on_status_check)
        self.custom_response_on_abort = copy.deepcopy(custom_response_on_abort)
        self.expected_exception_type = expected_exception_type
        self.expected_aborted: bool = expected_aborted

    def setup_session_mock(self, session_mock: requests_mock.Mocker, server_state: ResumableUploadServerState):

        def custom_matcher(request):
            request_url = urlparse(request.url)
            request_query = parse_qs(request_url.query)

            # initial request
            if (
                request_url.hostname == "localhost"
                and request_url.path == f"/api/2.0/fs/files{MultipartUploadTestCase.path}"
                and request_query.get("action") == ["initiate-upload"]
                and request.method == "POST"
            ):

                assert MultipartUploadTestCase.is_auth_header_present(request)
                assert request.text is None

                def processor():
                    response_json = {"resumable_upload": {"session_token": server_state.session_token}}
                    return [200, json.dumps(response_json), {}]

                # Different initiate error responses have been verified by test_multipart_upload(),
                # so we're always generating a "success" response.
                return CustomResponse(enabled=False).generate_response(request, processor)

            elif (
                request_url.hostname == "localhost"
                and request_url.path == "/api/2.0/fs/create-resumable-upload-url"
                and request.method == "POST"
            ):

                assert MultipartUploadTestCase.is_auth_header_present(request)

                request_json = request.json()
                assert request_json.keys() == {"path", "session_token"}
                assert request_json["path"] == self.path
                assert request_json["session_token"] == server_state.session_token

                def processor():
                    resumable_upload_url = f"{ResumableUploadServerState.resumable_upload_url_prefix}{self.path}"

                    response_json = {
                        "resumable_upload_url": {
                            "url": resumable_upload_url,
                            "headers": [{"name": "name1", "value": "value1"}],
                        }
                    }
                    return [200, json.dumps(response_json), {}]

                return self.custom_response_on_create_resumable_url.generate_response(request, processor)

            # resumable upload, uploading part
            elif (
                request.url.startswith(ResumableUploadServerState.resumable_upload_url_prefix)
                and request.method == "PUT"
            ):

                assert not MultipartUploadTestCase.is_auth_header_present(request)
                url_path = request.url[len(ResumableUploadServerState.resumable_upload_url_prefix) :]
                assert url_path == self.path

                content_range_header = request.headers["Content-range"]
                is_status_check_request = re.match("bytes \\*/\\*", content_range_header)
                if is_status_check_request:
                    assert not request.body
                    response_customizer = self.custom_response_on_status_check
                else:
                    response_customizer = self.custom_response_on_upload

                def processor():
                    if not is_status_check_request:
                        body = request.body.read()

                        match = re.match("bytes (\\d+)-(\\d+)/(.+)", content_range_header)
                        [range_start_s, range_end_s, file_size_s] = match.groups()

                        server_state.save_part(int(range_start_s), int(range_end_s), body, file_size_s)

                    if server_state.file_content:
                        # upload complete
                        return [200, "", {}]
                    else:
                        # more data expected
                        if server_state.confirmed_last_byte:
                            headers = {"Range": f"bytes=0-{server_state.confirmed_last_byte}"}
                        else:
                            headers = {}
                        return [308, "", headers]

                return response_customizer.generate_response(request, processor)

            # abort upload
            elif (
                request.url.startswith(ResumableUploadServerState.resumable_upload_url_prefix)
                and request.method == "DELETE"
            ):

                assert not MultipartUploadTestCase.is_auth_header_present(request)
                url_path = request.url[len(ResumableUploadServerState.resumable_upload_url_prefix) :]
                assert url_path == self.path

                def processor():
                    server_state.abort_upload()
                    return [200, "", {}]

                return self.custom_response_on_abort.generate_response(request, processor)

            return None

        session_mock.add_matcher(matcher=custom_matcher)

    def run(self, config: Config):
        config = config.copy()
        if self.sdk_retry_timeout_seconds:
            config.retry_timeout_seconds = self.sdk_retry_timeout_seconds
        if self.multipart_upload_chunk_size:
            config.multipart_upload_chunk_size = self.multipart_upload_chunk_size
        if self.multipart_upload_max_retries:
            config.multipart_upload_max_retries = self.multipart_upload_max_retries
        config.enable_experimental_files_api_client = True
        config.multipart_upload_min_stream_size = 0  # disable single-shot uploads

        MultipartUploadTestCase.setup_token_auth(config)

        file_content = os.urandom(self.stream_size)

        upload_state = ResumableUploadServerState(self.unconfirmed_delta)

        try:
            with requests_mock.Mocker() as session_mock:
                self.setup_session_mock(session_mock, upload_state)
                w = WorkspaceClient(config=config)

                def upload():
                    w.files.upload("/test.txt", io.BytesIO(file_content), overwrite=self.overwrite)

                if self.expected_exception_type is not None:
                    with pytest.raises(self.expected_exception_type):
                        upload()
                else:
                    upload()
                    actual_content = upload_state.get_file_content()
                    assert actual_content == FileContent.from_bytes(file_content)

            assert upload_state.aborted == self.expected_aborted

        finally:
            upload_state.cleanup()

    def __str__(self):
        return self.name

    @staticmethod
    def to_string(test_case):
        return str(test_case)


@pytest.mark.parametrize(
    "test_case",
    [
        # ------------------ failures on creating resumable upload URL ------------------
        ResumableUploadTestCase(
            "Create resumable URL: 400 response is not retried",
            stream_size=1024 * 1024,
            custom_response_on_create_resumable_url=CustomResponse(
                code=400,
                # 1 failure is enough
                only_invocation=1,
            ),
            expected_exception_type=BadRequest,
            expected_aborted=False,  # upload didn't start
        ),
        ResumableUploadTestCase(
            "Create resumable URL: 403 response is not retried",
            stream_size=1024 * 1024,
            custom_response_on_create_resumable_url=CustomResponse(code=403, only_invocation=1),
            expected_exception_type=PermissionDenied,
            expected_aborted=False,  # upload didn't start
        ),
        ResumableUploadTestCase(
            "Create resumable URL: 500 response is not retried",
            stream_size=1024 * 1024,
            custom_response_on_create_resumable_url=CustomResponse(code=500, only_invocation=1),
            expected_exception_type=InternalError,
            expected_aborted=False,  # upload didn't start
        ),
        ResumableUploadTestCase(
            "Create resumable URL: non-JSON response is not retried",
            stream_size=1024 * 1024,
            custom_response_on_create_resumable_url=CustomResponse(body="Foo bar", only_invocation=1),
            expected_exception_type=requests.exceptions.JSONDecodeError,
            expected_aborted=False,  # upload didn't start
        ),
        ResumableUploadTestCase(
            "Create resumable URL: meaningless JSON response is not retried",
            stream_size=1024 * 1024,
            custom_response_on_create_resumable_url=CustomResponse(
                body='{"upload_part_urls":[{"url":""}]}', only_invocation=1
            ),
            expected_exception_type=ValueError,
            expected_aborted=False,  # upload didn't start
        ),
        ResumableUploadTestCase(
            "Create resumable URL: permanent retryable status code",
            stream_size=1024 * 1024,
            custom_response_on_create_resumable_url=CustomResponse(code=429),
            sdk_retry_timeout_seconds=30,  # don't wait for 5 min (SDK default timeout)
            expected_exception_type=TimeoutError,
            expected_aborted=False,  # upload didn't start
        ),
        ResumableUploadTestCase(
            "Create resumable URL: intermittent retryable exception is retried",
            stream_size=1024 * 1024,
            custom_response_on_create_resumable_url=CustomResponse(
                exception=requests.Timeout,
                # 3 failures total
                first_invocation=1,
                last_invocation=3,
            ),
            expected_aborted=False,  # upload succeeds
        ),
        # ------------------ failures during upload ------------------
        ResumableUploadTestCase(
            "Upload: retryable exception after file is uploaded",
            stream_size=1024 * 1024,
            custom_response_on_upload=CustomResponse(
                exception=requests.ConnectionError,
                # this makes server state change before exception is thrown
                exception_happened_before_processing=False,
            ),
            # Despite the returned error, file has been uploaded. We'll discover that
            # on the next status check and consider upload completed.
            expected_aborted=False,
        ),
        ResumableUploadTestCase(
            "Upload: retryable exception before file is uploaded, not enough retries",
            stream_size=1024 * 1024,
            multipart_upload_max_retries=3,
            custom_response_on_upload=CustomResponse(
                exception=requests.ConnectionError,
                # prevent server from saving this chunk
                exception_happened_before_processing=True,
                # fail 4 times, exceeding max_retries
                first_invocation=1,
                last_invocation=4,
            ),
            # File was never uploaded and we gave up retrying
            expected_exception_type=requests.ConnectionError,
            expected_aborted=True,
        ),
        ResumableUploadTestCase(
            "Upload: retryable exception before file is uploaded, enough retries",
            stream_size=1024 * 1024,
            multipart_upload_max_retries=4,
            custom_response_on_upload=CustomResponse(
                exception=requests.ConnectionError,
                # prevent server from saving this chunk
                exception_happened_before_processing=True,
                # fail 4 times, not exceeding max_retries
                first_invocation=1,
                last_invocation=4,
            ),
            # File was uploaded after retries
            expected_aborted=False,
        ),
        ResumableUploadTestCase(
            "Upload: intermittent 429 response: retried",
            stream_size=100 * 1024 * 1024,
            multipart_upload_chunk_size=7 * 1024 * 1024,
            multipart_upload_max_retries=3,
            custom_response_on_upload=CustomResponse(
                code=429,
                # 3 failures not exceeding max_retries
                first_invocation=2,
                last_invocation=4,
            ),
            expected_aborted=False,  # upload succeeded
        ),
        ResumableUploadTestCase(
            "Upload: intermittent 429 response: retry exhausted",
            stream_size=100 * 1024 * 1024,
            multipart_upload_chunk_size=1 * 1024 * 1024,
            multipart_upload_max_retries=3,
            custom_response_on_upload=CustomResponse(
                code=429,
                # 4 failures exceeding max_retries
                first_invocation=2,
                last_invocation=5,
            ),
            expected_exception_type=TooManyRequests,
            expected_aborted=True,
        ),
        # -------------- abort failures --------------
        ResumableUploadTestCase(
            "Abort: client error",
            stream_size=1024 * 1024,
            # prevent chunk from being uploaded
            custom_response_on_upload=CustomResponse(code=403),
            # internal server error does not prevent server state change
            custom_response_on_abort=CustomResponse(code=500),
            expected_exception_type=PermissionDenied,
            # abort returned error but was actually processed
            expected_aborted=True,
        ),
        # -------------- file already exists --------------
        ResumableUploadTestCase(
            "File already exists",
            stream_size=1024 * 1024,
            overwrite=False,
            custom_response_on_upload=CustomResponse(code=412, only_invocation=1),
            expected_exception_type=AlreadyExists,
            expected_aborted=True,
        ),
        # -------------- success cases --------------
        ResumableUploadTestCase(
            "Multiple chunks, zero unconfirmed delta",
            stream_size=100 * 1024 * 1024,
            multipart_upload_chunk_size=7 * 1024 * 1024 + 566,
            # server accepts all the chunks in full
            unconfirmed_delta=0,
            expected_aborted=False,
        ),
        ResumableUploadTestCase(
            "Multiple small chunks, zero unconfirmed delta",
            stream_size=100 * 1024 * 1024,
            multipart_upload_chunk_size=100 * 1024,
            # server accepts all the chunks in full
            unconfirmed_delta=0,
            expected_aborted=False,
        ),
        ResumableUploadTestCase(
            "Multiple chunks, non-zero unconfirmed delta",
            stream_size=100 * 1024 * 1024,
            multipart_upload_chunk_size=7 * 1024 * 1024 + 566,
            # for every chunk, server accepts all except last 239 bytes
            unconfirmed_delta=239,
            expected_aborted=False,
        ),
        ResumableUploadTestCase(
            "Multiple chunks, variable unconfirmed delta",
            stream_size=100 * 1024 * 1024,
            multipart_upload_chunk_size=7 * 1024 * 1024 + 566,
            # for the first chunk, server accepts all except last 15Kib
            # for the second chunk, server accepts it all
            # for the 3rd chunk, server accepts all except last 25000 bytes
            # for the 4th chunk, server accepts all except last 7 Mb
            # for the 5th chunk onwards server accepts all except last 5 bytes
            unconfirmed_delta=[15 * 1024, 0, 25000, 7 * 1024 * 1024, 5],
            expected_aborted=False,
        ),
    ],
    ids=ResumableUploadTestCase.to_string,
)
def test_resumable_upload(config: Config, test_case: ResumableUploadTestCase):
    test_case.run(config)
