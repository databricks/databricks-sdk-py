import functools
import logging
import os
import platform
import threading
from abc import ABC, abstractmethod
from datetime import timedelta
from io import BytesIO, RawIOBase, UnsupportedOperation
from typing import BinaryIO, Callable, List, Optional, Tuple

import pytest
import requests

from databricks.sdk.errors import AlreadyExists
from databricks.sdk.mixins.files_utils import (
    _ByteRange,
    _Cancelled,
    _common_decision,
    _ConcatenatedInputStream,
    _download_ranges_to_file,
    _DownloadDestination,
    _Failure,
    _MultipartUploadSession,
    _plan_upload,
    _PresignedUrlDistributor,
    _RangeResponse,
    _RequestFailed,
    _ResilientDownload,
    _retry,
    _RetryBudget,
    _run_in_parallel,
    _split_into_ranges,
    _TransferStatus,
    _UploadData,
    _UploadPlan,
    _upload_to,
    _walk_endpoints,
    _WalkingDownloadStream,
)

logger = logging.getLogger(__name__)


class Utils:
    @staticmethod
    def parse_range_header(range_header: str, content_length: Optional[int] = None) -> Tuple[int, int]:
        """
        Parses a Range header string and returns the start and end byte positions.
        Example input: "bytes=0-499"
        Example output: (0, 499)
        """
        if not range_header.startswith("bytes="):
            raise ValueError("Invalid Range header format")
        byte_range = range_header[len("bytes=") :]
        start_str, end_str = byte_range.split("-")
        start = int(start_str) if start_str else 0
        end = int(end_str) if end_str else None

        if content_length is not None:
            if start >= content_length:
                raise ValueError(f"Start byte {start} exceeds content length {content_length}")
            if end is not None and end >= content_length:
                raise ValueError(f"End byte {end} exceeds content length {content_length}")
            if end is not None and start > end:
                raise ValueError(f"Start byte {start} is greater than end byte {end}")

        return start, end


class NonSeekableBuffer(RawIOBase, BinaryIO):
    """
    A non-seekable buffer that wraps a bytes object. Used for unit tests only.
    This class implements the BinaryIO interface but does not support seeking.
    It is used to simulate a non-seekable stream for testing purposes.
    """

    def __init__(self, data: bytes):
        self._stream = BytesIO(data)

    def read(self, size: int = -1) -> bytes:
        return self._stream.read(size)

    def readline(self, size: int = -1) -> bytes:
        return self._stream.readline(size)

    def readlines(self, size: int = -1) -> List[bytes]:
        return self._stream.readlines(size)

    def readable(self) -> bool:
        return True

    def seekable(self) -> bool:
        return False

    def seek(self, *args, **kwargs) -> int:
        raise UnsupportedOperation("seek not supported")

    def tell(self) -> int:
        raise UnsupportedOperation("tell not supported")


class ConcatenatedInputStreamTestCase(ABC):
    @abstractmethod
    def generate(self) -> Tuple[bytes, BinaryIO]:
        pass


class ConcatenatedInputStreamTestCase(ConcatenatedInputStreamTestCase):
    def __init__(self, head: bytes, tail: bytes, is_seekable: bool = True):
        self._head = head
        self._tail = tail
        self._is_seekable = is_seekable

    def generate(self) -> Tuple[bytes, BinaryIO]:
        """
        Generate a pair of:
        (a) implementation under test
        (b) concatenated byte array (to create reference implementation from)
        """
        full_stream = self._head + self._tail
        if self._is_seekable:
            concatenated_stream = _ConcatenatedInputStream(BytesIO(self._head), BytesIO(self._tail))
        else:
            concatenated_stream = _ConcatenatedInputStream(NonSeekableBuffer(self._head), NonSeekableBuffer(self._tail))
        return full_stream, concatenated_stream

    def test_to_string(self) -> str:
        head = self._head.decode("utf-8")
        tail = self._tail.decode("utf-8")
        seekable = "seekable" if self._is_seekable else "non-seekable"
        return f"{head}-{tail}-{seekable}"

    @staticmethod
    def to_string(test_case) -> str:
        return test_case.test_to_string()


test_cases = [
    ConcatenatedInputStreamTestCase(b"", b"zzzz"),
    ConcatenatedInputStreamTestCase(b"", b""),
    ConcatenatedInputStreamTestCase(b"", b"", is_seekable=False),
    ConcatenatedInputStreamTestCase(b"foo", b"bar"),
    ConcatenatedInputStreamTestCase(b"foo", b"bar", is_seekable=False),
    ConcatenatedInputStreamTestCase(b"", b"zzzz", is_seekable=False),
    ConcatenatedInputStreamTestCase(b"non_empty", b""),
    ConcatenatedInputStreamTestCase(b"non_empty", b"", is_seekable=False),
    ConcatenatedInputStreamTestCase(b"\n\n\n", b"\n\n"),
    ConcatenatedInputStreamTestCase(b"\n\n\n", b"\n\n", is_seekable=False),
    ConcatenatedInputStreamTestCase(b"aa\nbb\nccc\n", b"dd\nee\nff"),
    ConcatenatedInputStreamTestCase(b"aa\nbb\nccc\n", b"dd\nee\nff", is_seekable=False),
    ConcatenatedInputStreamTestCase(b"First line\nsecond line", b"first line with line \nbreak"),
    ConcatenatedInputStreamTestCase(b"First line\nsecond line", b"first line with line \nbreak", is_seekable=False),
    ConcatenatedInputStreamTestCase(b"First line\n", b"\nsecond line"),
    ConcatenatedInputStreamTestCase(b"First line\n", b"\nsecond line", is_seekable=False),
    ConcatenatedInputStreamTestCase(b"First line\n", b"\n"),
    ConcatenatedInputStreamTestCase(b"First line\n", b"\n", is_seekable=False),
    ConcatenatedInputStreamTestCase(b"First line\n", b""),
    ConcatenatedInputStreamTestCase(b"First line\n", b"", is_seekable=False),
    ConcatenatedInputStreamTestCase(b"", b"\nA line"),
    ConcatenatedInputStreamTestCase(b"", b"\nA line", is_seekable=False),
    ConcatenatedInputStreamTestCase(b"\n", b"\nA line"),
    ConcatenatedInputStreamTestCase(b"\n", b"\nA line", is_seekable=False),
]


def verify(test_case: ConcatenatedInputStreamTestCase, apply: Callable[[BinaryIO], Tuple[any, bool]]):
    """
    This method applies given function iteratively to both implementation under test
    and reference implementation of the stream, and verifies the result on each step is identical.
    """
    result_bytes, implementation_under_test = test_case.generate()
    reference_implementation = BytesIO(result_bytes)

    while True:
        expected = apply(reference_implementation)
        actual = apply(implementation_under_test)

        assert actual == expected

        should_stop = actual[1]
        if should_stop:
            break

    if len(result_bytes) == reference_implementation.tell():
        verify_eof(implementation_under_test)
        verify_eof(reference_implementation)


def verify_eof(buffer: BinaryIO):
    assert len(buffer.read()) == 0
    assert len(buffer.read(100)) == 0
    assert len(buffer.readline()) == 0
    assert len(buffer.readline(100)) == 0
    assert len(buffer.readlines()) == 0
    assert len(buffer.readlines(100)) == 0


@pytest.mark.parametrize("test_case", test_cases, ids=ConcatenatedInputStreamTestCase.to_string)
@pytest.mark.parametrize("limit", [-1, 0, 1, 3, 4, 5, 6, 10, 100, 1000])
def test_read(config, test_case: ConcatenatedInputStreamTestCase, limit: int):
    def apply(buffer: BinaryIO):
        value = buffer.read(limit)

        if limit > 0:
            assert len(value) <= limit

        should_stop = (limit > 0 and len(value) < limit) or len(value) == 0
        return value, should_stop

    verify(test_case, apply)


@pytest.mark.parametrize("test_case", test_cases, ids=ConcatenatedInputStreamTestCase.to_string)
@pytest.mark.parametrize("limit", [-1, 0, 1, 2, 3, 4, 5, 6, 9, 10, 11, 12, 100, 1000])
def test_read_line(config, test_case: ConcatenatedInputStreamTestCase, limit: int):
    def apply(buffer: BinaryIO):
        value = buffer.readline(limit)
        should_stop = len(value) == 0
        return value, should_stop

    verify(test_case, apply)


@pytest.mark.parametrize("test_case", test_cases, ids=ConcatenatedInputStreamTestCase.to_string)
@pytest.mark.parametrize("limit", [-1, 0, 1, 2, 3, 4, 5, 6, 9, 10, 11, 12, 100, 1000])
def test_read_lines(config, test_case: ConcatenatedInputStreamTestCase, limit: int):
    def apply(buffer: BinaryIO):
        value = buffer.readlines(limit)
        should_stop = len(value) == 0
        return value, should_stop

    verify(test_case, apply)


@pytest.mark.parametrize("test_case", test_cases, ids=ConcatenatedInputStreamTestCase.to_string)
def test_iterator(config, test_case: ConcatenatedInputStreamTestCase):
    def apply(buffer: BinaryIO):
        try:
            value = buffer.__next__()
            return value, False
        except StopIteration:
            return None, True

    verify(test_case, apply)


def seeks_to_string(seeks: [Tuple[int, int]]):
    ", ".join(list(map(lambda seek: f"Seek: offset={seek[0]}, whence={seek[1]}", seeks)))


@pytest.mark.parametrize("test_case", test_cases, ids=ConcatenatedInputStreamTestCase.to_string)
@pytest.mark.parametrize(
    "seeks",
    [
        [(0, os.SEEK_SET)],
        [(-10, os.SEEK_SET), (1, os.SEEK_SET)],
        [(10000, os.SEEK_SET)],
        [(0, os.SEEK_END)],
        [(10000, os.SEEK_END)],
        [(-10000, os.SEEK_END)],
        [(1, os.SEEK_SET)],
        [(5, os.SEEK_SET)],
        [(-1, os.SEEK_END)],
        [(-1, os.SEEK_CUR)],
        [(-100, os.SEEK_CUR), (105, os.SEEK_CUR), (2, os.SEEK_CUR), (-2, os.SEEK_CUR)],
    ],
    ids=seeks_to_string,
)
def test_seek(config, test_case: ConcatenatedInputStreamTestCase, seeks: List[Tuple[int, int]]):
    def read_and_restore(buf: BinaryIO) -> bytes:
        pos = buf.tell()
        result = buf.read()
        buf.seek(pos)
        return result

    def safe_call(buf: BinaryIO, call: Callable[[BinaryIO], any]) -> (any, bool):
        """
        Calls the provided function on the buffer and returns the result.
        It is a wrapper to handle exceptions gracefully.
        If an exception occurs, it returns None and False.
        :param buf: The buffer to operate on.
        :param call: The function to call with the buffer.
        :return: A tuple of (result, success), where success is True if the call succeeded, False otherwise.
        """
        try:
            result = call(buf)
            return result, True
        except Exception:
            return None, False

    underlying, buffer = test_case.generate()
    native_buffer = BytesIO(underlying)
    if not buffer.seekable():
        return

    assert buffer.tell() == native_buffer.tell()
    for seek in seeks:

        def do_seek(buf):
            return buf.seek(seek[0], seek[1])

        assert safe_call(buffer, do_seek) == safe_call(native_buffer, do_seek)
        assert buffer.tell() == native_buffer.tell()
        assert read_and_restore(buffer) == read_and_restore(native_buffer)


class DummyResponse:
    def __init__(self, value):
        self.value = value


def test_get_url_returns_url_and_version():
    distributor = _PresignedUrlDistributor(lambda: DummyResponse("url1"))
    url, version = distributor.get_url()
    assert isinstance(url, DummyResponse)
    assert url.value == "url1"
    assert version == 0


def test_get_url_caches_url():
    calls = []
    distributor = _PresignedUrlDistributor(lambda: calls.append(1) or DummyResponse("url2"))
    url1, version1 = distributor.get_url()
    url2, version2 = distributor.get_url()
    assert url1 is url2
    assert version1 == version2
    assert calls.count(1) == 1  # Only called once


def test_invalidate_url_changes_url_and_version():
    responses = [DummyResponse("urlA"), DummyResponse("urlB")]
    distributor = _PresignedUrlDistributor(lambda: responses.pop(0))
    url1, version1 = distributor.get_url()
    distributor.invalidate_url(version1)
    url2, version2 = distributor.get_url()
    assert url1.value == "urlA"
    assert url2.value == "urlB"
    assert version2 == version1 + 1


def test_invalidate_url_wrong_version_does_not_invalidate():
    distributor = _PresignedUrlDistributor(lambda: DummyResponse("urlX"))
    url1, version1 = distributor.get_url()
    distributor.invalidate_url(version1 + 1)  # Wrong version
    url2, version2 = distributor.get_url()
    assert url1 is url2
    assert version2 == version1


# ======================== The endpoint walk, retries and the transfer helpers ========================


class _Clock:
    def __init__(self):
        self.now = 0.0
        self.sleeps = []

    def time(self) -> float:
        return self.now

    def sleep(self, seconds: float) -> None:
        self.sleeps.append(seconds)
        self.now += seconds


_FOREVER = timedelta(hours=1)


def _always(decision):
    return lambda failure: decision


_LAST = _TransferStatus(is_last_endpoint=True)
"""No endpoint left to walk to: retries are allowed before commit."""


def _sender(*outcomes):
    """A send() that returns or raises the given outcomes in turn, counting its calls."""
    outcomes = list(outcomes)
    calls = []

    def send():
        calls.append(1)
        outcome = outcomes.pop(0)
        if isinstance(outcome, BaseException):
            raise outcome
        return outcome

    send.calls = calls
    return send


def test_retry_retries_until_it_succeeds():
    send = _sender(ValueError("a"), ValueError("b"), "ok")
    budget = _RetryBudget(None, _FOREVER)

    result = _retry(send, _always("retry"), budget, _LAST, _Clock())

    assert result == "ok"
    assert len(send.calls) == 3


@pytest.mark.parametrize("decision", ["walk", "raise"])
def test_retry_hands_back_walk_and_raise_without_retrying(decision):
    error = ValueError("boom")
    budget = _RetryBudget(None, _FOREVER)

    result = _retry(_sender(error), _always(decision), budget, _LAST, _Clock())

    assert result == _Failure(error, decision)


def test_retry_unwraps_the_error_it_surfaces():
    error = ValueError("boom")
    budget = _RetryBudget(None, _FOREVER)

    result = _retry(_sender(_RequestFailed(error, 500)), _common_decision, budget, _LAST, _Clock())

    assert result == _Failure(error, "walk")


def test_retry_raises_like_the_sdk_retry_helper_when_attempts_run_out():
    last = ConnectionError("down")
    send = _sender(ConnectionError("1"), ConnectionError("2"), last)
    budget = _RetryBudget(3, _FOREVER)

    result = _retry(send, _always("retry"), budget, _LAST, _Clock())

    assert isinstance(result.error, RuntimeError)
    assert result.error.__cause__ is last
    assert result.decision == "walk"
    assert len(send.calls) == 3


def test_retry_raises_timeout_error_when_the_deadline_passes():
    send = _sender(*[ConnectionError(str(n)) for n in range(100)])
    budget = _RetryBudget(None, timedelta(seconds=30))

    result = _retry(send, _always("retry"), budget, _LAST, _Clock())

    assert isinstance(result.error, TimeoutError)
    assert result.decision == "walk"


@pytest.mark.parametrize(
    "status, sends",
    [
        (_TransferStatus(), 1),
        (_TransferStatus(retries_before_commit=1), 2),
        (_TransferStatus(committed=True), 5),
        (_TransferStatus(is_last_endpoint=True), 5),
    ],
    ids=["before commit", "before commit with one retry", "committed", "last endpoint"],
)
def test_retry_sends_once_before_commit_unless_no_endpoint_is_left(status, sends):
    last = ValueError("last")
    send = _sender(*[ValueError(str(n)) for n in range(4)], last)

    result = _retry(send, _always("retry"), _RetryBudget(5, _FOREVER), status, _Clock())

    assert len(send.calls) == sends
    assert result.decision == "walk"
    if sends == 1:
        # Nothing was retried, so the walk gets the error itself.
        assert str(result.error) == "0"


def test_retry_waits_for_retry_after():
    throttled = ValueError("slow down")
    throttled.retry_after_secs = 7
    clock = _Clock()
    budget = _RetryBudget(None, _FOREVER)

    _retry(_sender(throttled, "ok"), _always("retry"), budget, _LAST, clock)

    assert 7 <= sum(clock.sleeps) < 8


@pytest.mark.parametrize("stop", ["cancelled", "cannot send again"])
def test_retry_stops_retrying(stop):
    status = _TransferStatus(cancelled=stop == "cancelled", is_last_endpoint=True)
    error = ValueError("boom")
    send = _sender(error, "ok")
    budget = _RetryBudget(None, _FOREVER)
    can_retry_opt = (lambda: False) if stop == "cannot send again" else None

    result = _retry(send, _always("retry"), budget, status, _Clock(), can_retry_opt=can_retry_opt)

    assert result == _Failure(error, "walk")
    assert len(send.calls) == 1


class _CancellingClock(_Clock):
    """Cancels the transfer during its first sleep."""

    def __init__(self, status: _TransferStatus):
        super().__init__()
        self._status = status

    def sleep(self, seconds: float) -> None:
        super().sleep(seconds)
        self._status.cancel()


def test_retry_stops_when_cancelled_during_the_wait():
    status = _TransferStatus(is_last_endpoint=True)
    clock = _CancellingClock(status)
    error = ValueError("boom")
    send = _sender(error, "ok")

    result = _retry(send, _always("retry"), _RetryBudget(None, _FOREVER), status, clock)

    assert result == _Failure(error, "walk")
    assert len(send.calls) == 1
    assert clock.sleeps == [1.0]


def test_retry_calls_before_retry_before_each_retry_but_not_after_the_last_attempt():
    calls = []
    send = _sender(ValueError("1"), ValueError("2"), ValueError("3"))

    result = _retry(
        send,
        _always("retry"),
        _RetryBudget(3, _FOREVER),
        _LAST,
        _Clock(),
        before_retry_opt=lambda: calls.append(1),
    )

    assert isinstance(result.error, RuntimeError)
    assert len(calls) == 2


class _Client:
    def __init__(self, name, outcome=None):
        self.name = name
        self.outcome = outcome


def _transfer_that(outcomes, commit=()):
    """A transfer that answers per client name, committing first for the names in `commit`."""
    calls = []

    def transfer(client, status):
        calls.append(client.name)
        if client.name in commit:
            status.commit()
        return outcomes.get(client.name)

    transfer.calls = calls
    return transfer


def test_walk_moves_on_after_a_walk_failure_before_commit():
    transfer = _transfer_that({"a": _Failure(ValueError("a"), "walk")})
    moves = []

    _walk_endpoints([_Client("a"), _Client("b")], transfer, before_next_endpoint=lambda: moves.append(1))

    assert transfer.calls == ["a", "b"]
    assert moves == [1]


@pytest.mark.parametrize(
    "decision, commit, can_send_again",
    [("raise", (), True), ("walk", ("a",), True), ("walk", (), False)],
    ids=["raise", "committed", "cannot-send-again"],
)
def test_walk_raises_without_moving_on(decision, commit, can_send_again):
    error = ValueError("a")
    transfer = _transfer_that({"a": _Failure(error, decision)}, commit)

    with pytest.raises(ValueError) as raised:
        _walk_endpoints([_Client("a"), _Client("b")], transfer, can_send_again=lambda: can_send_again)

    assert raised.value is error
    assert transfer.calls == ["a"]


def test_walk_marks_only_the_last_endpoint():
    seen = []

    def transfer(client, status):
        seen.append(status.is_last_endpoint)
        return _Failure(ValueError(client.name), "walk")

    with pytest.raises(ValueError):
        _walk_endpoints([_Client("a"), _Client("b"), _Client("c")], transfer)

    assert seen == [False, False, True]


def test_walk_raises_the_last_endpoints_error():
    transfer = _transfer_that({"a": _Failure(ValueError("a"), "walk"), "b": _Failure(KeyError("b"), "walk")})

    with pytest.raises(KeyError):
        _walk_endpoints([_Client("a"), _Client("b")], transfer)


@pytest.mark.parametrize("decision", ["walk", "raise"])
def test_no_walk_once_a_byte_was_transferred(decision):
    # The commit rule holds for every decision a failure can carry.
    error = ValueError("after a byte")
    transfer = _transfer_that({"a": _Failure(error, decision)}, commit=("a",))

    with pytest.raises(ValueError):
        _walk_endpoints([_Client("a"), _Client("b"), _Client("c")], transfer)

    assert transfer.calls == ["a"]


def _range_response(chunks, content_length=None):
    def chunk_iterator():
        for chunk in chunks:
            if isinstance(chunk, BaseException):
                raise chunk
            yield chunk

    return _RangeResponse(200, content_length, "application/octet-stream", "yesterday", chunk_iterator(), lambda: None)


def _scripted_open(*responses):
    """A get_file_range that answers with the given responses in turn and records what it was asked for."""
    responses = list(responses)
    requests_made = []

    def get_file_range(requested, if_unmodified_since_opt, expected_length_opt, status):
        requests_made.append((requested, if_unmodified_since_opt))
        return responses.pop(0)

    get_file_range.requests = requests_made
    return get_file_range


def _read_all(download):
    data = b""
    while True:
        chunk = download.read_chunk()
        if chunk is None:
            return data
        if isinstance(chunk, _Failure):
            return chunk
        data += chunk


def test_resilient_download_resumes_after_a_break_from_the_offset():
    get_file_range = _scripted_open(
        _range_response([b"abc", requests.exceptions.ChunkedEncodingError("cut")], 6),
        _range_response([b"def"], 3),
    )
    download = _ResilientDownload(
        get_file_range, _RetryBudget(None, _FOREVER, 1), _TransferStatus(committed=True), _ByteRange(0, None), None
    )

    assert download.open() is None
    assert _read_all(download) == b"abcdef"
    # The resume asks for the rest, guarded by the first response's Last-Modified.
    assert get_file_range.requests[1] == (_ByteRange(3, None), "yesterday")


def test_resilient_download_stops_resuming_without_progress():
    cut = requests.exceptions.ChunkedEncodingError("cut")
    get_file_range = _scripted_open(_range_response([cut]), _range_response([cut]), _range_response([b"never"]))
    download = _ResilientDownload(
        get_file_range, _RetryBudget(None, _FOREVER, 1), _TransferStatus(committed=True), _ByteRange(0, None), None
    )
    download.open()

    assert _read_all(download) == _Failure(cut, "walk")
    assert len(get_file_range.requests) == 2


def test_resilient_download_surfaces_the_break_when_the_reopen_fails():
    cut = requests.exceptions.ChunkedEncodingError("cut")
    get_file_range = _scripted_open(_range_response([b"a", cut]), _Failure(ValueError("reopen failed"), "raise"))
    download = _ResilientDownload(
        get_file_range, _RetryBudget(None, _FOREVER, 1), _TransferStatus(committed=True), _ByteRange(0, None), None
    )
    download.open()

    assert _read_all(download) == _Failure(cut, "raise")


def test_run_in_parallel_cancels_the_other_threads_on_the_first_failure():
    failure = _Failure(ValueError("first"), "walk")
    status = _TransferStatus()
    lock = threading.Lock()
    started = []
    items = iter(range(100))

    def work(item, status):
        with lock:
            started.append(item)
        if item == 0:
            return failure
        # The other items run until the failure cancels them.
        while not status.cancelled:
            pass
        return _Failure(ValueError(f"cancelled {item}"), "walk")

    assert _run_in_parallel(4, lambda: next(items, None), work, status) is failure
    assert status.cancelled
    assert len(started) <= 4


@pytest.mark.parametrize("raises_in", ["next_item", "work"])
def test_run_in_parallel_turns_an_exception_into_a_walk_failure(raises_in):
    error = RuntimeError("unexpected")

    def next_item():
        if raises_in == "next_item":
            raise error
        return 1

    def work(item, status):
        raise error

    failure = _run_in_parallel(2, next_item, work, _TransferStatus())

    assert failure == _Failure(error, "walk")


@pytest.mark.parametrize("size, part_size", [(0, 2), (1, 2), (5, 2), (6, 2), (7, 7), (1000, 7)])
def test_split_into_ranges_covers_the_file_without_gaps_or_overlaps(size, part_size):
    ranges = _split_into_ranges(size, part_size)

    covered = [offset for r in ranges for offset in range(r.start, r.end_opt + 1)]
    assert covered == list(range(size))
    assert all(r.end_opt - r.start + 1 == part_size for r in ranges[:-1])


def test_resilient_download_stops_when_cancelled():
    status = _TransferStatus(committed=True)
    download = _ResilientDownload(
        _scripted_open(_range_response([b"abc", b"def"])),
        _RetryBudget(None, _FOREVER, 1),
        status,
        _ByteRange(0, None),
        None,
    )
    download.open()
    assert download.read_chunk() == b"abc"

    status.cancel()

    failure = download.read_chunk()
    assert isinstance(failure.error, _Cancelled) and failure.decision == "walk"


def test_resilient_download_does_not_resume_after_an_unexpected_error():
    error = RuntimeError("unexpected")
    get_file_range = _scripted_open(_range_response([b"a", error]), _range_response([b"never"]))
    download = _ResilientDownload(
        get_file_range, _RetryBudget(None, _FOREVER, 1), _TransferStatus(committed=True), _ByteRange(0, None), None
    )
    download.open()

    assert _read_all(download) == _Failure(error, "walk")
    assert len(get_file_range.requests) == 1


def test_resilient_download_skips_empty_chunks():
    download = _ResilientDownload(
        _scripted_open(_range_response([b"ab", b"", b"cd"])),
        _RetryBudget(None, _FOREVER, 1),
        _TransferStatus(),
        _ByteRange(0, None),
        None,
    )
    download.open()

    assert _read_all(download) == b"abcd"


def test_resilient_download_resumes_with_the_callers_if_unmodified_since():
    cut = requests.exceptions.ChunkedEncodingError("cut")
    get_file_range = _scripted_open(_range_response([b"a", cut]), _range_response([b"b"]))
    download = _ResilientDownload(
        get_file_range, _RetryBudget(None, _FOREVER, 1), _TransferStatus(committed=True), _ByteRange(0, None), "caller"
    )
    download.open()

    assert _read_all(download) == b"ab"
    assert [guard for _, guard in get_file_range.requests] == ["caller", "caller"]


def test_resilient_download_stops_at_the_total_resume_budget():
    cut = requests.exceptions.ChunkedEncodingError("cut")
    get_file_range = _scripted_open(
        _range_response([b"a", cut]), _range_response([b"b", cut]), _range_response([b"never"])
    )
    download = _ResilientDownload(
        get_file_range, _RetryBudget(1, _FOREVER, None), _TransferStatus(committed=True), _ByteRange(0, None), None
    )
    download.open()

    # The second break made progress, but the one resume allowed is spent.
    assert _read_all(download) == _Failure(cut, "walk")
    assert len(get_file_range.requests) == 2


@pytest.mark.parametrize(
    "byte_range, content_length",
    [(_ByteRange(0, 5), None), (_ByteRange(0, None), 6)],
    ids=["range", "whole-file-with-content-length"],
)
def test_resilient_download_resumes_a_body_that_ends_short(byte_range, content_length):
    get_file_range = _scripted_open(_range_response([b"abc"], content_length), _range_response([b"def"]))
    download = _ResilientDownload(
        get_file_range, _RetryBudget(None, _FOREVER, 1), _TransferStatus(committed=True), byte_range, None
    )
    download.open()

    assert _read_all(download) == b"abcdef"
    assert get_file_range.requests[1][0] == _ByteRange(3, byte_range.end_opt)


@pytest.mark.parametrize(
    "byte_range, content_length",
    [(_ByteRange(0, 2), None), (_ByteRange(0, None), 3)],
    ids=["range", "whole-file-with-content-length"],
)
def test_resilient_download_fails_a_body_longer_than_expected(byte_range, content_length):
    get_file_range = _scripted_open(_range_response([b"ab", b"cd"], content_length))
    download = _ResilientDownload(get_file_range, _RetryBudget(None, _FOREVER, 1), _TransferStatus(), byte_range, None)
    download.open()

    assert download.read_chunk() == b"ab"
    failure = download.read_chunk()
    assert isinstance(failure.error, IOError) and failure.decision == "walk"


def test_resilient_download_fails_a_body_that_ends_short_without_a_resume():
    get_file_range = _scripted_open(_range_response([b"abc"]))
    download = _ResilientDownload(
        get_file_range, _RetryBudget(0, _FOREVER, 0), _TransferStatus(), _ByteRange(0, 5), None
    )
    download.open()

    failure = _read_all(download)
    assert isinstance(failure.error, IOError) and failure.decision == "walk"


def test_resilient_download_does_not_resume_before_commit_unless_no_endpoint_is_left():
    cut = requests.exceptions.ChunkedEncodingError("cut")
    get_file_range = _scripted_open(_range_response([cut]), _range_response([b"abc"], 3))
    download = _ResilientDownload(
        get_file_range, _RetryBudget(None, _FOREVER), _TransferStatus(), _ByteRange(0, None), None
    )
    download.open()

    assert _read_all(download) == _Failure(cut, "walk")
    assert len(get_file_range.requests) == 1


class _DownloadClient:
    """A client whose get_file_range opens a scripted download, or fails."""

    def __init__(self, name, *outcomes):
        self.name = name
        self._outcomes = list(outcomes)
        self.if_unmodified_since_asked = []

    def get_file_range(self, path, byte_range, if_unmodified_since_opt, status):
        self.if_unmodified_since_asked.append(if_unmodified_since_opt)
        outcome = self._outcomes.pop(0)
        if isinstance(outcome, _Failure):
            return outcome
        download = _ResilientDownload(
            _scripted_open(outcome), _RetryBudget(0, _FOREVER, 0), status, byte_range, if_unmodified_since_opt
        )
        return download.open() or download


def test_walking_stream_walks_at_open_and_before_the_first_byte():
    cut = requests.exceptions.ChunkedEncodingError("cut")
    clients = [
        _DownloadClient("a", _Failure(ValueError("a"), "walk")),
        _DownloadClient("b", _range_response([cut])),
        _DownloadClient("c", _range_response([b"data"])),
    ]

    assert b"".join(_WalkingDownloadStream(clients, "/f")) == b"data"


def test_walking_stream_asks_later_endpoints_for_the_file_it_described():
    cut = requests.exceptions.ChunkedEncodingError("cut")
    # The file changed after the first endpoint described it, so the next endpoint fails the precondition.
    changed = _Failure(ValueError("412"), _common_decision(_RequestFailed(ValueError("412"), 412)))
    a = _DownloadClient("a", _range_response([cut]))
    b = _DownloadClient("b", changed)
    c = _DownloadClient("c", _range_response([b"new"]))
    stream = _WalkingDownloadStream([a, b, c], "/f")

    with pytest.raises(ValueError, match="412"):
        next(stream)
    assert a.if_unmodified_since_asked == [None]
    assert b.if_unmodified_since_asked == [stream.last_modified_opt] == ["yesterday"]
    assert c.if_unmodified_since_asked == []


def test_walking_stream_raises_after_the_first_byte():
    cut = requests.exceptions.ChunkedEncodingError("cut")
    clients = [_DownloadClient("a", _range_response([b"x", cut])), _DownloadClient("b", _range_response([b"data"]))]
    stream = _WalkingDownloadStream(clients, "/f")

    assert next(stream) == b"x"
    with pytest.raises(requests.exceptions.ChunkedEncodingError):
        next(stream)


def test_run_in_parallel_stops_at_the_first_failure():
    failure = _Failure(ValueError("third"), "walk")
    status = _TransferStatus()
    done = []
    items = iter(range(100))

    def work(item, status):
        if item == 3:
            return failure
        done.append(item)
        return None

    assert _run_in_parallel(1, lambda: next(items, None), work, status) is failure
    assert status.cancelled
    assert done == [0, 1, 2]


def test_run_in_parallel_runs_every_item():
    lock = threading.Lock()
    done = []
    items = iter(range(50))

    def work(item, status):
        with lock:
            done.append(item)

    assert _run_in_parallel(4, lambda: next(items, None), work, _TransferStatus()) is None
    assert sorted(done) == list(range(50))


def test_download_ranges_into_the_temp_file(tmp_path):
    destination = str(tmp_path / "out.bin")
    temp_file = _DownloadDestination.create(destination, 6)

    class Client:
        name = "a"

        def get_file_range(self, path, byte_range, if_unmodified_since_opt, status):
            data = b"abcdef"[byte_range.start : byte_range.end_opt + 1]
            download = _ResilientDownload(
                _scripted_open(_range_response([data])), _RetryBudget(0, _FOREVER, 0), status, byte_range, None
            )
            return download.open() or download

    status = _TransferStatus()
    ranges = [_ByteRange(0, 1), _ByteRange(2, 3), _ByteRange(4, 5)]
    failure_opt = _download_ranges_to_file(
        Client(), status, path="/f", ranges=ranges, last_modified=None, destination=temp_file, parallelism=2
    )
    temp_file.finish()

    assert failure_opt is None and status.committed
    assert open(destination, "rb").read() == b"abcdef"


@pytest.mark.skipif(platform.system() == "Windows", reason="Windows has no POSIX permission bits")
def test_download_temp_file_gets_the_permissions_of_a_new_file(tmp_path):
    destination = tmp_path / "out.bin"
    old_umask = os.umask(0o027)
    try:
        temp_file = _DownloadDestination.create(str(destination), 3)
    finally:
        os.umask(old_umask)
    temp_file.finish()

    assert os.stat(destination).st_mode & 0o777 == 0o640
    assert os.path.getsize(destination) == 3


def test_download_destination_fails_for_a_directory(tmp_path):
    destination = tmp_path / "downloads"
    destination.mkdir()
    temp_file = _DownloadDestination.create(str(destination), 3)

    with pytest.raises(OSError):
        temp_file.finish()
    temp_file.discard()

    assert list(destination.iterdir()) == []
    assert sorted(p.name for p in tmp_path.iterdir()) == ["downloads"]


def test_download_destination_discards_its_temp_file(tmp_path):
    destination = tmp_path / "out.bin"
    target = _DownloadDestination.create(str(destination), None)
    target.write_at(0, b"ab")

    target.discard()

    assert list(tmp_path.iterdir()) == []


def test_download_destination_writes_an_existing_file_in_place(tmp_path):
    destination = tmp_path / "out.bin"
    destination.write_bytes(b"old content")
    target = _DownloadDestination.create(str(destination), None)

    target.write_at(0, b"ab")
    target.write_at(2, b"cd")
    target.finish()

    assert destination.read_bytes() == b"abcd"
    assert list(tmp_path.iterdir()) == [destination]


def test_download_destination_leaves_an_existing_file_as_it_was_without_any_data(tmp_path):
    destination = tmp_path / "out.bin"
    destination.write_bytes(b"old content")
    target = _DownloadDestination.create(str(destination), None)

    target.discard()

    assert destination.read_bytes() == b"old content"


def test_download_destination_empties_an_existing_file_for_an_empty_download(tmp_path):
    destination = tmp_path / "out.bin"
    destination.write_bytes(b"old content")
    target = _DownloadDestination.create(str(destination), None)

    target.finish()

    assert destination.read_bytes() == b""


def test_download_destination_takes_ranges_for_a_new_or_regular_file(tmp_path):
    existing = tmp_path / "existing.bin"
    existing.write_bytes(b"x")

    assert _DownloadDestination.takes_ranges(str(tmp_path / "new.bin"))
    assert _DownloadDestination.takes_ranges(str(existing))


@pytest.mark.skipif(not hasattr(os, "mkfifo"), reason="needs named pipes")
def test_download_destination_takes_no_ranges_for_a_pipe(tmp_path):
    pipe = tmp_path / "pipe"
    os.mkfifo(pipe)

    assert not _DownloadDestination.takes_ranges(str(pipe))


def test_parallel_download_raises_when_another_range_committed_before_it_stopped(tmp_path):
    # Range A fails without seeing that range B already wrote a byte. The decision is made once both stopped, and
    # the download is committed, so it raises A's error instead of walking.
    b_committed = threading.Event()
    failure = _Failure(ValueError("502 on range A"), "walk")

    class Client:
        name = "first"

        def get_file_range(self, path, byte_range, if_unmodified_since_opt, status):
            if byte_range.start == 0:
                assert b_committed.wait(5)
                return failure

            def chunks():
                yield b"c"
                # download_range committed the first chunk before asking for the next one.
                b_committed.set()
                yield b"d"

            response = _RangeResponse(206, 2, "application/octet-stream", "yesterday", chunks(), lambda: None)
            download = _ResilientDownload(
                _scripted_open(response), _RetryBudget(0, _FOREVER, 0), status, byte_range, None
            )
            return download.open() or download

    class NeverUsed:
        name = "second"

        def get_file_range(self, *args):
            raise AssertionError("the download walked after commit")

    temp_file = _DownloadDestination.create(str(tmp_path / "out.bin"), 4)
    attempt = functools.partial(
        _download_ranges_to_file,
        path="/f",
        ranges=[_ByteRange(0, 1), _ByteRange(2, 3)],
        last_modified=None,
        destination=temp_file,
        parallelism=2,
    )

    with pytest.raises(ValueError, match="502 on range A"):
        _walk_endpoints([Client(), NeverUsed()], attempt)
    temp_file.discard()


def test_download_ranges_returns_the_first_failure_and_closes_every_response(tmp_path):
    temp_file = _DownloadDestination.create(str(tmp_path / "out.bin"), 6)
    failure = _Failure(ValueError("range 2"), "walk")
    closed = []

    class Client:
        name = "a"

        def get_file_range(self, path, byte_range, if_unmodified_since_opt, status):
            if byte_range.start == 2:
                return failure
            response = _range_response([b"ab"])
            response.close = lambda: closed.append(byte_range.start)
            download = _ResilientDownload(
                _scripted_open(response), _RetryBudget(0, _FOREVER, 0), status, byte_range, None
            )
            return download.open() or download

    status = _TransferStatus()
    ranges = [_ByteRange(0, 1), _ByteRange(2, 3), _ByteRange(4, 5)]

    result = _download_ranges_to_file(
        Client(), status, path="/f", ranges=ranges, last_modified=None, destination=temp_file, parallelism=1
    )
    temp_file.discard()

    assert result is failure
    assert status.cancelled
    # The first range was written, so the transfer is committed and won't walk.
    assert status.committed
    assert closed == [0]


def _upload_data(source: str, content: bytes, tmp_path) -> _UploadData:
    if source == "file":
        path = tmp_path / "source"
        path.write_bytes(content)
        return _UploadData.from_file(str(path))
    if source == "seekable":
        return _UploadData.from_stream(BytesIO(content))
    if source == "one-pass":
        return _UploadData.from_stream(NonSeekableBuffer(content))
    # A pipe-like stream that returns fewer bytes than asked for before it ends.
    return _UploadData.from_stream(_ShortReads(content, 3))


_SOURCES = ["file", "seekable", "one-pass", "short-reads"]
_REWINDABLE = {"file", "seekable"}
_CONTENT = bytes(range(10))


def _read_to_end(stream: BinaryIO) -> bytes:
    # As requests sends a body: read until an empty read, since a pipe returns fewer bytes than asked for.
    out = b""
    while chunk := stream.read(4):
        out += chunk
    return out


def _all_parts(data: _UploadData, size: int) -> list:
    parts = []
    while (part := data.next_part(size)) is not None:
        parts.append(part)
    return parts


@pytest.mark.parametrize("source", _SOURCES)
@pytest.mark.parametrize("length", [0, 3, 4, 10])
def test_upload_data_parts_cover_the_data_in_order(source, length, tmp_path):
    content = _CONTENT[:length]
    data = _upload_data(source, content, tmp_path)

    parts = _all_parts(data, 4)

    assert [number for number, _ in parts] == list(range(1, len(parts) + 1))
    assert all(len(part) == 4 for _, part in parts[:-1])
    assert b"".join(part for _, part in parts) == content
    assert data.size_opt == length


@pytest.mark.parametrize("source", _SOURCES)
def test_upload_data_size_is_known_up_front_only_when_rewindable(source, tmp_path):
    data = _upload_data(source, _CONTENT, tmp_path)

    assert data.size_opt == (len(_CONTENT) if source in _REWINDABLE else None)


@pytest.mark.parametrize("source", _SOURCES)
@pytest.mark.parametrize("ahead, size_opt", [(5, None), (10, None), (11, 10)], ids=["shorter", "exact", "longer"])
def test_upload_data_read_ahead_learns_the_size_of_a_short_stream_without_consuming(source, ahead, size_opt, tmp_path):
    data = _upload_data(source, _CONTENT, tmp_path)

    data.read_ahead(ahead)

    if source in _REWINDABLE:
        size_opt = len(_CONTENT)
    assert data.size_opt == size_opt
    assert _all_parts(data, 4) == [(1, _CONTENT[:4]), (2, _CONTENT[4:8]), (3, _CONTENT[8:])]


@pytest.mark.parametrize("source", ["one-pass", "short-reads"])
def test_upload_data_read_ahead_of_an_empty_stream_learns_size_zero(source, tmp_path):
    data = _upload_data(source, b"", tmp_path)

    data.read_ahead(4)

    assert data.size_opt == 0
    assert data.next_part(4) is None


@pytest.mark.parametrize("source", _SOURCES)
def test_upload_data_restarts_from_the_start_before_commit(source, tmp_path):
    data = _upload_data(source, _CONTENT, tmp_path)
    assert data.next_part(4) == (1, _CONTENT[:4])

    assert data.can_send_again()
    data.restart()

    assert _all_parts(data, 4) == [(1, _CONTENT[:4]), (2, _CONTENT[4:8]), (3, _CONTENT[8:])]


@pytest.mark.parametrize("source", _SOURCES)
def test_upload_data_after_commit_continues_and_only_rewindable_data_can_be_sent_again(source, tmp_path):
    data = _upload_data(source, _CONTENT, tmp_path)
    assert data.next_part(4) == (1, _CONTENT[:4])

    data.drop_replay_buffer()

    assert _all_parts(data, 4) == [(2, _CONTENT[4:8]), (3, _CONTENT[8:])]
    assert data.can_send_again() == (source in _REWINDABLE)


@pytest.mark.parametrize("source", ["one-pass", "short-reads"])
def test_one_pass_upload_data_keeps_no_bytes_after_commit(source, tmp_path):
    data = _upload_data(source, bytes(1000), tmp_path)
    data.next_part(100)

    data.drop_replay_buffer()
    _all_parts(data, 100)

    assert len(data._replay) == 0


@pytest.mark.parametrize("source", _SOURCES)
@pytest.mark.parametrize("ahead", [0, 4, 11], ids=["not-read-ahead", "read-ahead-in-part", "read-ahead-whole"])
def test_upload_data_whole_is_the_data_from_the_start(source, ahead, tmp_path):
    data = _upload_data(source, _CONTENT, tmp_path)
    data.read_ahead(ahead)

    assert _read_to_end(data.whole()) == _CONTENT
    # A one-pass stream read whole ahead is sent from memory; otherwise its rest is streamed once.
    assert data.can_send_again() == (source in _REWINDABLE or ahead > len(_CONTENT))


@pytest.mark.parametrize("source", _SOURCES)
def test_upload_data_whole_after_a_part_is_the_data_from_the_start(source, tmp_path):
    data = _upload_data(source, _CONTENT, tmp_path)
    data.next_part(4)
    data.restart()

    assert _read_to_end(data.whole()) == _CONTENT


@pytest.mark.parametrize("source", _SOURCES)
def test_upload_data_hands_each_part_to_one_thread(source, tmp_path):
    content = os.urandom(10_000)
    data = _upload_data(source, content, tmp_path)
    parts = []
    lock = threading.Lock()

    def worker():
        while (part := data.next_part(7)) is not None:
            with lock:
                parts.append(part)

    threads = [threading.Thread(target=worker) for _ in range(8)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    parts.sort()
    assert [number for number, _ in parts] == list(range(1, len(parts) + 1))
    assert b"".join(part for _, part in parts) == content


def test_upload_data_closes_only_the_file_it_opened(tmp_path):
    path = tmp_path / "source"
    path.write_bytes(_CONTENT)
    from_file = _UploadData.from_file(str(path))
    from_file.next_part(4)
    stream = BytesIO(_CONTENT)
    from_stream = _UploadData.from_stream(stream)

    from_file.close()
    from_stream.close()

    assert from_file._stream_opt is None
    assert not stream.closed


class _PlanClient:
    def __init__(self, single_shot=True, multipart=True, max_part_size=None, max_single_shot_size=None):
        self.supports_single_shot = single_shot
        self.supports_multipart = multipart
        self.max_part_size_opt = max_part_size
        self.max_single_shot_size_opt = max_single_shot_size


@pytest.mark.parametrize(
    "size, min_stream_size, client, use_parallel, expected",
    [
        (5, 10, _PlanClient(), False, (False, 4, 1)),
        (5, 10, _PlanClient(single_shot=False), False, None),
        (0, 0, _PlanClient(), True, (False, 4, 1)),
        (100, 10, _PlanClient(multipart=False), True, (False, 4, 1)),
        (100, 10, _PlanClient(), False, (True, 4, 1)),
        (100, 10, _PlanClient(), True, (True, 4, 3)),
        (100, 10, _PlanClient(max_part_size=2), True, (True, 2, 3)),
        (100, 10, _PlanClient(multipart=False, max_single_shot_size=100), False, (False, 4, 1)),
        (100, 10, _PlanClient(multipart=False, max_single_shot_size=99), False, None),
    ],
    ids=[
        "small",
        "small-without-single-shot",
        "empty",
        "no-multipart",
        "sequential",
        "parallel",
        "capped-part-size",
        "single-shot-at-limit",
        "single-shot-over-limit",
    ],
)
def test_plan_upload(size, min_stream_size, client, use_parallel, expected):
    data = _UploadData.from_stream(BytesIO(b"x" * size))
    plan = _plan_upload(data, client, use_parallel, 3, 4, 1, min_stream_size)

    if expected is None:
        assert plan is None
    else:
        assert (plan.multipart, plan.part_size, plan.parallelism) == expected


def test_plan_upload_sends_a_one_pass_stream_of_unknown_size_multipart():
    data = _UploadData.from_stream(NonSeekableBuffer(b"x" * 5))

    assert _plan_upload(data, _PlanClient(), False, 3, 4, 1, 10).multipart
    data.read_ahead(10)
    assert not _plan_upload(data, _PlanClient(), False, 3, 4, 1, 10).multipart


class _Session(_MultipartUploadSession):
    def __init__(self, fail_on=(), complete_failure_opt=None):
        self.parts = {}
        self.aborts = 0
        self.completed = None
        self._fail_on = fail_on
        self._complete_failure_opt = complete_failure_opt

    def put_part(self, number, data, status):
        if number in self._fail_on:
            return _Failure(ValueError(f"part {number}"), "walk")
        self.parts[number] = data
        return f"etag-{number}"

    def complete(self, etags, status):
        self.completed = etags
        return self._complete_failure_opt

    def abort(self):
        self.aborts += 1


class _UploadClient:
    name = "a"

    def __init__(self, session):
        self.session = session
        self.batch_sizes = []

    def initiate_upload(self, path, overwrite_opt, status, part_url_batch_size=1):
        self.batch_sizes.append(part_url_batch_size)
        return self.session


@pytest.mark.parametrize("parallelism", [1, 3])
def test_upload_to_commits_on_the_first_part_and_completes(parallelism):
    session = _Session()
    client = _UploadClient(session)
    status = _TransferStatus()
    data = _UploadData.from_stream(BytesIO(b"0123456789"))
    plans = {client: _plan_upload(data, _PlanClient(), parallelism > 1, parallelism, 4, 1, 0)}

    assert _upload_to(client, status, plans=plans, path="/f", overwrite_opt=None, data=data) is None
    assert status.committed
    assert session.parts == {1: b"0123", 2: b"4567", 3: b"89"}
    assert session.completed == {1: "etag-1", 2: "etag-2", 3: "etag-3"}
    assert session.aborts == 0


@pytest.mark.parametrize("fail_on, committed", [((1,), False), ((2,), True)], ids=["first-part", "later-part"])
def test_upload_to_aborts_once_on_failure(fail_on, committed):
    session = _Session(fail_on)
    client = _UploadClient(session)
    status = _TransferStatus()
    data = _UploadData.from_stream(BytesIO(b"0123456789"))
    plans = {client: _plan_upload(data, _PlanClient(), False, 1, 4, 1, 0)}

    failure = _upload_to(client, status, plans=plans, path="/f", overwrite_opt=None, data=data)

    assert failure.decision == "walk"
    assert status.committed == committed
    assert session.aborts == 1
    assert session.completed is None


@pytest.mark.parametrize("fails", [False, True], ids=["succeeds", "fails"])
def test_upload_to_single_shot_commits_only_on_success(fails):
    failure = _Failure(ValueError("put"), "walk")

    class Client:
        name = "a"
        puts = []

        def put_file(self, path, overwrite_opt, data, status):
            self.puts.append(data.whole().read())
            return failure if fails else None

    client = Client()
    status = _TransferStatus()
    data = _UploadData.from_stream(BytesIO(b"abc"))

    result = _upload_to(
        client, status, plans={client: _UploadPlan(False, 4, 1)}, path="/f", overwrite_opt=None, data=data
    )

    assert result is (failure if fails else None)
    assert status.committed == (not fails)
    assert client.puts == [b"abc"]


def test_upload_to_returns_an_initiate_failure_without_sending_parts():
    failure = _Failure(ValueError("initiate"), "walk")

    class Client:
        name = "a"

        def initiate_upload(self, path, overwrite_opt, status, part_url_batch_size=1):
            return failure

    client = Client()
    status = _TransferStatus()
    data = _UploadData.from_stream(BytesIO(b"abc"))

    result = _upload_to(
        client, status, plans={client: _UploadPlan(True, 4, 1)}, path="/f", overwrite_opt=None, data=data
    )

    assert result is failure
    assert not status.committed
    assert data.can_send_again()


def test_upload_to_aborts_when_complete_fails():
    failure = _Failure(ValueError("complete"), "walk")
    session = _Session(complete_failure_opt=failure)
    client = _UploadClient(session)
    status = _TransferStatus()
    data = _UploadData.from_stream(BytesIO(b"0123456789"))

    result = _upload_to(
        client, status, plans={client: _UploadPlan(True, 4, 1, 7)}, path="/f", overwrite_opt=None, data=data
    )

    assert result is failure
    assert status.committed
    assert session.aborts == 1
    assert client.batch_sizes == [7]


def test_upload_to_raises_for_a_multipart_upload_of_empty_data():
    session = _Session()
    client = _UploadClient(session)
    data = _UploadData.from_stream(NonSeekableBuffer(b""))
    plans = {client: _UploadPlan(True, 4, 1)}

    with pytest.raises(ValueError, match="empty data"):
        _upload_to(client, _TransferStatus(), plans=plans, path="/f", overwrite_opt=None, data=data)
    assert session.aborts == 1


@pytest.mark.parametrize("status_code", [408, 429, 502, 503, 504])
def test_common_decision_retries_the_retryable_status_codes(status_code):
    assert _common_decision(_RequestFailed(ValueError(), status_code)) == "retry"


def test_common_decision():
    assert _common_decision(_RequestFailed(ValueError(), 403)) == "walk"
    assert _common_decision(_RequestFailed(AlreadyExists("exists"), 409)) == "raise"
    assert _common_decision(requests.ConnectionError()) == "retry"
    assert _common_decision(_RequestFailed(ValueError(), 412)) == "raise"
    # A client's own decision overrides the shared rules.
    assert _common_decision(_RequestFailed(ValueError(), 503, "raise")) == "raise"
    assert _common_decision(_RequestFailed(ValueError(), 403, "retry")) == "retry"


class _ShortReads(RawIOBase):
    """A raw stream that returns at most `step` bytes per read before it ends, like a pipe."""

    def __init__(self, data: bytes, step: int):
        self._data = data
        self._step = step

    def readable(self) -> bool:
        return True

    def read(self, n: int = -1) -> bytes:
        size = self._step if n < 0 else min(n, self._step)
        chunk, self._data = self._data[:size], self._data[size:]
        return chunk


def test_resilient_download_does_not_resume_without_last_modified():
    cut = requests.exceptions.ChunkedEncodingError("cut")
    response = _range_response([b"a", cut])
    response.last_modified_opt = None
    get_file_range = _scripted_open(response, _range_response([b"never"]))
    download = _ResilientDownload(
        get_file_range, _RetryBudget(None, _FOREVER, 1), _TransferStatus(), _ByteRange(0, None), None
    )
    download.open()

    assert _read_all(download) == _Failure(cut, "walk")
    assert len(get_file_range.requests) == 1
