import logging
import os
from abc import ABC, abstractmethod
from io import BytesIO, RawIOBase, UnsupportedOperation
from typing import BinaryIO, Callable, List, Optional, Tuple

import pytest  # type: ignore[import-not-found]

from databricks.sdk.mixins.files_utils import (_ConcatenatedInputStream,
                                               _PresignedUrlDistributor)

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

        return start, end  # type: ignore[return-value]


class NonSeekableBuffer(RawIOBase, BinaryIO):  # type: ignore[misc]
    """
    A non-seekable buffer that wraps a bytes object. Used for unit tests only.
    This class implements the BinaryIO interface but does not support seeking.
    It is used to simulate a non-seekable stream for testing purposes.
    """

    def __init__(self, data: bytes):
        self._stream = BytesIO(data)

    def read(self, size: int = -1) -> bytes:
        return self._stream.read(size)

    def readline(self, size: int = -1) -> bytes:  # type: ignore[override]
        return self._stream.readline(size)

    def readlines(self, size: int = -1) -> List[bytes]:
        return self._stream.readlines(size)

    def readable(self) -> bool:
        return True

    def seekable(self) -> bool:
        return False

    def seek(self, *args, **kwargs) -> int:  # type: ignore[no-untyped-def]
        raise UnsupportedOperation("seek not supported")

    def tell(self) -> int:
        raise UnsupportedOperation("tell not supported")


class ConcatenatedInputStreamTestCase(ABC):

    @abstractmethod
    def generate(self) -> Tuple[bytes, BinaryIO]:
        pass


class ConcatenatedInputStreamTestCase(ConcatenatedInputStreamTestCase):  # type: ignore[no-redef]
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
    def to_string(test_case) -> str:  # type: ignore[no-untyped-def]
        return test_case.test_to_string()  # type: ignore[no-any-return]


test_cases = [
    ConcatenatedInputStreamTestCase(b"", b"zzzz"),  # type: ignore[abstract, call-arg]
    ConcatenatedInputStreamTestCase(b"", b""),  # type: ignore[abstract, call-arg]
    ConcatenatedInputStreamTestCase(b"", b"", is_seekable=False),  # type: ignore[abstract, call-arg]
    ConcatenatedInputStreamTestCase(b"foo", b"bar"),  # type: ignore[abstract, call-arg]
    ConcatenatedInputStreamTestCase(b"foo", b"bar", is_seekable=False),  # type: ignore[abstract, call-arg]
    ConcatenatedInputStreamTestCase(b"", b"zzzz", is_seekable=False),  # type: ignore[abstract, call-arg]
    ConcatenatedInputStreamTestCase(b"non_empty", b""),  # type: ignore[abstract, call-arg]
    ConcatenatedInputStreamTestCase(b"non_empty", b"", is_seekable=False),  # type: ignore[abstract, call-arg]
    ConcatenatedInputStreamTestCase(b"\n\n\n", b"\n\n"),  # type: ignore[abstract, call-arg]
    ConcatenatedInputStreamTestCase(b"\n\n\n", b"\n\n", is_seekable=False),  # type: ignore[abstract, call-arg]
    ConcatenatedInputStreamTestCase(b"aa\nbb\nccc\n", b"dd\nee\nff"),  # type: ignore[abstract, call-arg]
    ConcatenatedInputStreamTestCase(b"aa\nbb\nccc\n", b"dd\nee\nff", is_seekable=False),  # type: ignore[abstract, call-arg]
    ConcatenatedInputStreamTestCase(b"First line\nsecond line", b"first line with line \nbreak"),  # type: ignore[abstract, call-arg]
    ConcatenatedInputStreamTestCase(b"First line\nsecond line", b"first line with line \nbreak", is_seekable=False),  # type: ignore[abstract, call-arg]
    ConcatenatedInputStreamTestCase(b"First line\n", b"\nsecond line"),  # type: ignore[abstract, call-arg]
    ConcatenatedInputStreamTestCase(b"First line\n", b"\nsecond line", is_seekable=False),  # type: ignore[abstract, call-arg]
    ConcatenatedInputStreamTestCase(b"First line\n", b"\n"),  # type: ignore[abstract, call-arg]
    ConcatenatedInputStreamTestCase(b"First line\n", b"\n", is_seekable=False),  # type: ignore[abstract, call-arg]
    ConcatenatedInputStreamTestCase(b"First line\n", b""),  # type: ignore[abstract, call-arg]
    ConcatenatedInputStreamTestCase(b"First line\n", b"", is_seekable=False),  # type: ignore[abstract, call-arg]
    ConcatenatedInputStreamTestCase(b"", b"\nA line"),  # type: ignore[abstract, call-arg]
    ConcatenatedInputStreamTestCase(b"", b"\nA line", is_seekable=False),  # type: ignore[abstract, call-arg]
    ConcatenatedInputStreamTestCase(b"\n", b"\nA line"),  # type: ignore[abstract, call-arg]
    ConcatenatedInputStreamTestCase(b"\n", b"\nA line", is_seekable=False),  # type: ignore[abstract, call-arg]
]


def verify(test_case: ConcatenatedInputStreamTestCase, apply: Callable[[BinaryIO], Tuple[any, bool]]):  # type: ignore[no-untyped-def, valid-type]
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


def verify_eof(buffer: BinaryIO):  # type: ignore[no-untyped-def]
    assert len(buffer.read()) == 0
    assert len(buffer.read(100)) == 0
    assert len(buffer.readline()) == 0
    assert len(buffer.readline(100)) == 0
    assert len(buffer.readlines()) == 0
    assert len(buffer.readlines(100)) == 0


@pytest.mark.parametrize("test_case", test_cases, ids=ConcatenatedInputStreamTestCase.to_string)  # type: ignore[attr-defined, misc]
@pytest.mark.parametrize("limit", [-1, 0, 1, 3, 4, 5, 6, 10, 100, 1000])  # type: ignore[misc]
def test_read(config, test_case: ConcatenatedInputStreamTestCase, limit: int):  # type: ignore[no-untyped-def]
    def apply(buffer: BinaryIO):  # type: ignore[no-untyped-def]
        value = buffer.read(limit)

        if limit > 0:
            assert len(value) <= limit

        should_stop = (limit > 0 and len(value) < limit) or len(value) == 0
        return value, should_stop

    verify(test_case, apply)


@pytest.mark.parametrize("test_case", test_cases, ids=ConcatenatedInputStreamTestCase.to_string)  # type: ignore[attr-defined, misc]
@pytest.mark.parametrize("limit", [-1, 0, 1, 2, 3, 4, 5, 6, 9, 10, 11, 12, 100, 1000])  # type: ignore[misc]
def test_read_line(config, test_case: ConcatenatedInputStreamTestCase, limit: int):  # type: ignore[no-untyped-def]
    def apply(buffer: BinaryIO):  # type: ignore[no-untyped-def]
        value = buffer.readline(limit)
        should_stop = len(value) == 0
        return value, should_stop

    verify(test_case, apply)


@pytest.mark.parametrize("test_case", test_cases, ids=ConcatenatedInputStreamTestCase.to_string)  # type: ignore[attr-defined, misc]
@pytest.mark.parametrize("limit", [-1, 0, 1, 2, 3, 4, 5, 6, 9, 10, 11, 12, 100, 1000])  # type: ignore[misc]
def test_read_lines(config, test_case: ConcatenatedInputStreamTestCase, limit: int):  # type: ignore[no-untyped-def]
    def apply(buffer: BinaryIO):  # type: ignore[no-untyped-def]
        value = buffer.readlines(limit)
        should_stop = len(value) == 0
        return value, should_stop

    verify(test_case, apply)


@pytest.mark.parametrize("test_case", test_cases, ids=ConcatenatedInputStreamTestCase.to_string)  # type: ignore[attr-defined, misc]
def test_iterator(config, test_case: ConcatenatedInputStreamTestCase):  # type: ignore[no-untyped-def]
    def apply(buffer: BinaryIO):  # type: ignore[no-untyped-def]
        try:
            value = buffer.__next__()
            return value, False
        except StopIteration:
            return None, True

    verify(test_case, apply)


def seeks_to_string(seeks: [Tuple[int, int]]):  # type: ignore[misc, no-untyped-def, valid-type]
    ", ".join(list(map(lambda seek: f"Seek: offset={seek[0]}, whence={seek[1]}", seeks)))


@pytest.mark.parametrize("test_case", test_cases, ids=ConcatenatedInputStreamTestCase.to_string)  # type: ignore[attr-defined, misc]
@pytest.mark.parametrize(  # type: ignore[misc]
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
def test_seek(config, test_case: ConcatenatedInputStreamTestCase, seeks: List[Tuple[int, int]]):  # type: ignore[no-untyped-def]
    def read_and_restore(buf: BinaryIO) -> bytes:
        pos = buf.tell()
        result = buf.read()
        buf.seek(pos)
        return result

    def safe_call(buf: BinaryIO, call: Callable[[BinaryIO], any]) -> (any, bool):  # type: ignore[syntax, valid-type]
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
        do_seek = lambda buf: buf.seek(seek[0], seek[1])
        assert safe_call(buffer, do_seek) == safe_call(native_buffer, do_seek)
        assert buffer.tell() == native_buffer.tell()
        assert read_and_restore(buffer) == read_and_restore(native_buffer)


class DummyResponse:
    def __init__(self, value):  # type: ignore[no-untyped-def]
        self.value = value


def test_get_url_returns_url_and_version():  # type: ignore[no-untyped-def]
    distributor = _PresignedUrlDistributor(lambda: DummyResponse("url1"))  # type: ignore[arg-type, no-untyped-call, return-value]
    url, version = distributor.get_url()
    assert isinstance(url, DummyResponse)
    assert url.value == "url1"
    assert version == 0


def test_get_url_caches_url():  # type: ignore[no-untyped-def]
    calls = []
    distributor = _PresignedUrlDistributor(lambda: calls.append(1) or DummyResponse("url2"))  # type: ignore[arg-type, func-returns-value, no-untyped-call, return-value]
    url1, version1 = distributor.get_url()
    url2, version2 = distributor.get_url()
    assert url1 is url2
    assert version1 == version2
    assert calls.count(1) == 1  # Only called once


def test_invalidate_url_changes_url_and_version():  # type: ignore[no-untyped-def]
    responses = [DummyResponse("urlA"), DummyResponse("urlB")]  # type: ignore[no-untyped-call]
    distributor = _PresignedUrlDistributor(lambda: responses.pop(0))  # type: ignore[arg-type, return-value]
    url1, version1 = distributor.get_url()
    distributor.invalidate_url(version1)
    url2, version2 = distributor.get_url()
    assert url1.value == "urlA"  # type: ignore[attr-defined]
    assert url2.value == "urlB"  # type: ignore[attr-defined]
    assert version2 == version1 + 1


def test_invalidate_url_wrong_version_does_not_invalidate():  # type: ignore[no-untyped-def]
    distributor = _PresignedUrlDistributor(lambda: DummyResponse("urlX"))  # type: ignore[arg-type, no-untyped-call, return-value]
    url1, version1 = distributor.get_url()
    distributor.invalidate_url(version1 + 1)  # Wrong version
    url2, version2 = distributor.get_url()
    assert url1 is url2
    assert version2 == version1
