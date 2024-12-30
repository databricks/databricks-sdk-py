import logging
import os
import re
from dataclasses import dataclass
from typing import List, Union

import pytest
from requests import RequestException

from databricks.sdk import WorkspaceClient
from databricks.sdk.core import Config

logger = logging.getLogger(__name__)


@dataclass
class RequestData:

    def __init__(self, offset: int):
        self._offset: int = offset


class DownloadTestCase:

    def __init__(self, name: str, enable_new_client: bool, file_size: int,
                 failure_at_absolute_offset: List[int], max_recovers_total: Union[int, None],
                 max_recovers_without_progressing: Union[int, None], expected_success: bool,
                 expected_requested_offsets: List[int]):
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
            assert (len(actual_content) == len(session.content))
            assert (actual_content == session.content)
        else:
            with pytest.raises(RequestException):
                response.read()

        received_requests = session.received_requests

        assert (len(self.expected_requested_offsets) == len(received_requests))
        for idx, requested_offset in enumerate(self.expected_requested_offsets):
            assert (requested_offset == received_requests[idx]._offset)


class MockSession:

    def __init__(self, test_case: DownloadTestCase):
        self.test_case: DownloadTestCase = test_case
        self.received_requests: List[RequestData] = []
        self.content: bytes = os.urandom(self.test_case.file_size)
        self.failure_pointer = 0
        self.last_modified = 'Thu, 28 Nov 2024 16:39:14 GMT'

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
        assert method == 'GET'
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
                assert (headers["If-Unmodified-Since"] == self.last_modified)
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
        self.method = 'GET'
        self.headers = dict()
        self.body = None


class MockResponse:

    def __init__(self, session: MockSession, offset: int, request: MockRequest):
        self.session = session
        self.offset = offset
        self.request = request
        self.status_code = 200
        self.reason = 'OK'
        self.headers = dict()
        self.headers['Content-Length'] = len(session.content) - offset
        self.headers['Content-Type'] = 'application/octet-stream'
        self.headers['Last-Modified'] = session.last_modified
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

        end_offset = start_offset + self.chunk_size # exclusive, might be out of range

        if self.response.session.failure_pointer < len(
                self.response.session.test_case.failure_at_absolute_offset):
            failure_after_byte = self.response.session.test_case.failure_at_absolute_offset[
                self.response.session.failure_pointer]
            if failure_after_byte < end_offset:
                self.response.session.failure_pointer += 1
                raise RequestException("Fake error")

        result = self.response.session.content[start_offset:end_offset]
        self.offset += len(result)
        return result

    def close(self):
        pass


class _Constants:
    underlying_chunk_size = 1024 * 1024 # see ticket #832


@pytest.mark.parametrize(
    "test_case",
    [
        DownloadTestCase(name="Old client: no failures, file of 5 bytes",
                         enable_new_client=False,
                         file_size=5,
                         failure_at_absolute_offset=[],
                         max_recovers_total=0,
                         max_recovers_without_progressing=0,
                         expected_success=True,
                         expected_requested_offsets=[0]),
        DownloadTestCase(name="Old client: no failures, file of 1.5 chunks",
                         enable_new_client=False,
                         file_size=int(1.5 * _Constants.underlying_chunk_size),
                         failure_at_absolute_offset=[],
                         max_recovers_total=0,
                         max_recovers_without_progressing=0,
                         expected_success=True,
                         expected_requested_offsets=[0]),
        DownloadTestCase(
            name="Old client: failure",
            enable_new_client=False,
            file_size=1024,
            failure_at_absolute_offset=[100],
            max_recovers_total=None, # unlimited but ignored
            max_recovers_without_progressing=None, # unlimited but ignored
            expected_success=False,
            expected_requested_offsets=[0]),
        DownloadTestCase(name="New client: no failures, file of 5 bytes",
                         enable_new_client=True,
                         file_size=5,
                         failure_at_absolute_offset=[],
                         max_recovers_total=0,
                         max_recovers_without_progressing=0,
                         expected_success=True,
                         expected_requested_offsets=[0]),
        DownloadTestCase(name="New client: no failures, file of 1 Kb",
                         enable_new_client=True,
                         file_size=1024,
                         max_recovers_total=None,
                         max_recovers_without_progressing=None,
                         failure_at_absolute_offset=[],
                         expected_success=True,
                         expected_requested_offsets=[0]),
        DownloadTestCase(name="New client: no failures, file of 1.5 chunks",
                         enable_new_client=True,
                         file_size=int(1.5 * _Constants.underlying_chunk_size),
                         failure_at_absolute_offset=[],
                         max_recovers_total=0,
                         max_recovers_without_progressing=0,
                         expected_success=True,
                         expected_requested_offsets=[0]),
        DownloadTestCase(name="New client: no failures, file of 10 chunks",
                         enable_new_client=True,
                         file_size=10 * _Constants.underlying_chunk_size,
                         failure_at_absolute_offset=[],
                         max_recovers_total=0,
                         max_recovers_without_progressing=0,
                         expected_success=True,
                         expected_requested_offsets=[0]),
        DownloadTestCase(name="New client: recovers are disabled, first failure leads to download abort",
                         enable_new_client=True,
                         file_size=10000,
                         failure_at_absolute_offset=[5],
                         max_recovers_total=0,
                         max_recovers_without_progressing=0,
                         expected_success=False,
                         expected_requested_offsets=[0]),
        DownloadTestCase(
            name="New client: unlimited recovers allowed",
            enable_new_client=True,
            file_size=_Constants.underlying_chunk_size * 5,
            # causes errors on requesting the third chunk
            failure_at_absolute_offset=[
                _Constants.underlying_chunk_size - 1, _Constants.underlying_chunk_size - 1,
                _Constants.underlying_chunk_size - 1, _Constants.underlying_chunk_size + 1,
                _Constants.underlying_chunk_size * 3,
            ],
            max_recovers_total=None,
            max_recovers_without_progressing=None,
            expected_success=True,
            expected_requested_offsets=[
                0, 0, 0, 0, _Constants.underlying_chunk_size, _Constants.underlying_chunk_size * 3
            ]),
        DownloadTestCase(
            name="New client: we respect limit on total recovers when progressing",
            enable_new_client=True,
            file_size=_Constants.underlying_chunk_size * 10,
            failure_at_absolute_offset=[
                1,
                _Constants.underlying_chunk_size + 1, # progressing
                _Constants.underlying_chunk_size * 2 + 1, # progressing
                _Constants.underlying_chunk_size * 3 + 1 # progressing
            ],
            max_recovers_total=3,
            max_recovers_without_progressing=None,
            expected_success=False,
            expected_requested_offsets=[
                0, 0, _Constants.underlying_chunk_size * 1, _Constants.underlying_chunk_size * 2
            ]),
        DownloadTestCase(name="New client: we respect limit on total recovers when not progressing",
                         enable_new_client=True,
                         file_size=_Constants.underlying_chunk_size * 10,
                         failure_at_absolute_offset=[1, 1, 1, 1],
                         max_recovers_total=3,
                         max_recovers_without_progressing=None,
                         expected_success=False,
                         expected_requested_offsets=[0, 0, 0, 0]),
        DownloadTestCase(name="New client: we respect limit on non-progressing recovers",
                         enable_new_client=True,
                         file_size=_Constants.underlying_chunk_size * 2,
                         failure_at_absolute_offset=[
                             _Constants.underlying_chunk_size - 1, _Constants.underlying_chunk_size - 1,
                             _Constants.underlying_chunk_size - 1, _Constants.underlying_chunk_size - 1
                         ],
                         max_recovers_total=None,
                         max_recovers_without_progressing=3,
                         expected_success=False,
                         expected_requested_offsets=[0, 0, 0, 0]),
        DownloadTestCase(
            name="New client: non-progressing recovers count is reset when progressing",
            enable_new_client=True,
            file_size=_Constants.underlying_chunk_size * 10,
            failure_at_absolute_offset=[
                _Constants.underlying_chunk_size + 1, # this recover is after progressing
                _Constants.underlying_chunk_size + 1, # this is not
                _Constants.underlying_chunk_size * 2 + 1, # this recover is after progressing
                _Constants.underlying_chunk_size * 2 + 1, # this is not
                _Constants.underlying_chunk_size * 2 + 1, # this is not, we abort here
            ],
            max_recovers_total=None,
            max_recovers_without_progressing=2,
            expected_success=False,
            expected_requested_offsets=[
                0, _Constants.underlying_chunk_size, _Constants.underlying_chunk_size,
                _Constants.underlying_chunk_size * 2, _Constants.underlying_chunk_size * 2
            ]),
        DownloadTestCase(name="New client: non-progressing recovers count is reset when progressing - 2",
                         enable_new_client=True,
                         file_size=_Constants.underlying_chunk_size * 10,
                         failure_at_absolute_offset=[
                             1, _Constants.underlying_chunk_size + 1, _Constants.underlying_chunk_size * 2 +
                             1, _Constants.underlying_chunk_size * 3 + 1
                         ],
                         max_recovers_total=None,
                         max_recovers_without_progressing=1,
                         expected_success=True,
                         expected_requested_offsets=[
                             0, 0, _Constants.underlying_chunk_size, _Constants.underlying_chunk_size * 2,
                             _Constants.underlying_chunk_size * 3
                         ]),
    ],
    ids=DownloadTestCase.to_string)
def test_download_recover(config: Config, test_case: DownloadTestCase):
    test_case.run(config)
