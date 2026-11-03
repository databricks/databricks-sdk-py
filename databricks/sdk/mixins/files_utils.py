from __future__ import annotations

import logging
import os
import random
import secrets
import stat
import threading
from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import timedelta
from io import BytesIO
from typing import Any, BinaryIO, Callable, Iterable, Iterator, NamedTuple, Optional, TypeVar, Union

import requests

from .._base_client import _BaseClient
from ..errors import AlreadyExists, DatabricksError

_LOG = logging.getLogger(__name__)

T = TypeVar("T")


@dataclass
class CreateDownloadUrlResponse:
    """Response from the download URL API call."""

    url: str
    """The presigned URL to download the file."""
    headers: dict[str, str]
    """Headers to use when making the download request."""

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> CreateDownloadUrlResponse:
        """Create an instance from a dictionary."""
        if "url" not in data:
            raise ValueError("Missing 'url' in response data")
        headers = data["headers"] if "headers" in data else {}
        parsed_headers = {x["name"]: x["value"] for x in headers}
        return cls(url=data["url"], headers=parsed_headers)


class _ConcatenatedInputStream(BinaryIO):
    """This class joins two input streams into one."""

    def __init__(self, head_stream: BinaryIO, tail_stream: BinaryIO):
        if not head_stream.readable():
            raise ValueError("head_stream is not readable")
        if not tail_stream.readable():
            raise ValueError("tail_stream is not readable")

        self._head_stream = head_stream
        self._tail_stream = tail_stream
        self._head_size = None
        self._tail_size = None

    def close(self) -> None:
        try:
            self._head_stream.close()
        finally:
            self._tail_stream.close()

    def fileno(self) -> int:
        raise AttributeError()

    def flush(self) -> None:
        raise NotImplementedError("Stream is not writable")

    def isatty(self) -> bool:
        raise NotImplementedError()

    def read(self, __n: int = -1) -> bytes:
        head = self._head_stream.read(__n)
        remaining_bytes = __n - len(head) if __n >= 0 else __n
        tail = self._tail_stream.read(remaining_bytes)
        return head + tail

    def readable(self) -> bool:
        return True

    def readline(self, __limit: int = -1) -> bytes:
        # Read and return one line from the stream.
        # If __limit is specified, at most __limit bytes will be read.
        # The line terminator is always b'\n' for binary files.
        head = self._head_stream.readline(__limit)
        if len(head) > 0 and head[-1:] == b"\n":
            # end of line happened before (or at) the limit
            return head

        # if __limit >= 0, len(head) can't exceed limit
        remaining_bytes = __limit - len(head) if __limit >= 0 else __limit
        tail = self._tail_stream.readline(remaining_bytes)
        return head + tail

    def readlines(self, __hint: int = -1) -> list[bytes]:
        # Read and return a list of lines from the stream.
        # Hint can be specified to control the number of lines read: no more lines will be read
        # If the total size (in bytes/characters) of all lines so far exceeds hint.

        # In fact, BytesIO(bytes) will not read next line if total size of all lines
        # *equals or* exceeds hint.

        head_result = self._head_stream.readlines(__hint)
        head_total_bytes = sum(len(line) for line in head_result)

        if 0 < __hint <= head_total_bytes and head_total_bytes > 0:
            # We reached (or passed) the hint by reading from head_stream, or exhausted head_stream.

            if head_result[-1][-1:] == b"\n":
                # If we reached/passed the hint and also stopped at the line break, return.
                return head_result

            # Reading from head_stream could have stopped only because the stream was exhausted
            if len(self._head_stream.read(1)) > 0:
                raise ValueError(
                    f"Stream reading finished prematurely after reading {head_total_bytes} bytes, reaching or exceeding hint {__hint}"
                )

            # We need to finish reading the current line, now from tail_stream.

            tail_result = self._tail_stream.readlines(1)  # We will only read the first line from tail_stream.
            assert len(tail_result) <= 1
            if len(tail_result) > 0:
                # We will then append the tail as the last line of the result.
                return head_result[:-1] + [head_result[-1] + tail_result[0]]
            else:
                return head_result

        # We did not reach the hint by reading head_stream but exhausted it, continue reading from tail_stream
        # with an adjusted hint
        if __hint >= 0:
            remaining_bytes = __hint - head_total_bytes
        else:
            remaining_bytes = __hint

        tail_result = self._tail_stream.readlines(remaining_bytes)

        if head_total_bytes > 0 and head_result[-1][-1:] != b"\n" and len(tail_result) > 0:
            # If head stream does not end with the line break, we need to concatenate
            # the last line of the head result and the first line of tail result
            return head_result[:-1] + [head_result[-1] + tail_result[0]] + tail_result[1:]
        else:
            # Otherwise, just append two lists of lines.
            return head_result + tail_result

    def _get_stream_size(self, stream: BinaryIO) -> int:
        prev_offset = stream.tell()
        try:
            stream.seek(0, os.SEEK_END)
            return stream.tell()
        finally:
            stream.seek(prev_offset, os.SEEK_SET)

    def _get_head_size(self) -> int:
        if self._head_size is None:
            self._head_size = self._get_stream_size(self._head_stream)
        return self._head_size

    def _get_tail_size(self) -> int:
        if self._tail_size is None:
            self._tail_size = self._get_stream_size(self._tail_stream)
        return self._tail_size

    def seek(self, __offset: int, __whence: int = os.SEEK_SET) -> int:
        if not self.seekable():
            raise NotImplementedError("Stream is not seekable")

        if __whence == os.SEEK_SET:
            if __offset < 0:
                # Follow native buffer behavior
                raise ValueError(f"Negative seek value: {__offset}")

            head_size = self._get_head_size()

            if __offset <= head_size:
                self._head_stream.seek(__offset, os.SEEK_SET)
                self._tail_stream.seek(0, os.SEEK_SET)
            else:
                self._head_stream.seek(0, os.SEEK_END)  # move head stream to the end
                self._tail_stream.seek(__offset - head_size, os.SEEK_SET)

        elif __whence == os.SEEK_CUR:
            current_offset = self.tell()
            new_offset = current_offset + __offset
            if new_offset < 0:
                # gracefully don't seek before start
                new_offset = 0
            self.seek(new_offset, os.SEEK_SET)

        elif __whence == os.SEEK_END:
            if __offset > 0:
                # Python allows to seek beyond the end of stream.

                # Move head to EOF and tail to (EOF + offset), so subsequent tell()
                # returns len(head) + len(tail) + offset, same as for native buffer
                self._head_stream.seek(0, os.SEEK_END)
                self._tail_stream.seek(__offset, os.SEEK_END)
            else:
                self._tail_stream.seek(__offset, os.SEEK_END)
                tail_pos = self._tail_stream.tell()
                if tail_pos > 0:
                    # target position lies within the tail, move head to EOF
                    self._head_stream.seek(0, os.SEEK_END)
                else:
                    tail_size = self._get_tail_size()
                    self._head_stream.seek(__offset + tail_size, os.SEEK_END)
        else:
            raise ValueError(__whence)
        return self.tell()

    def seekable(self) -> bool:
        return self._head_stream.seekable() and self._tail_stream.seekable()

    def __getattribute__(self, name: str) -> Any:
        if name == "fileno":
            raise AttributeError()
        elif name in ["tell", "seek"] and not self.seekable():
            raise AttributeError()

        return super().__getattribute__(name)

    def tell(self) -> int:
        if not self.seekable():
            raise NotImplementedError()

        # Assuming that tail stream stays at 0 until head stream is exhausted
        return self._head_stream.tell() + self._tail_stream.tell()

    def truncate(self, __size: Optional[int] = None) -> int:
        raise NotImplementedError("Stream is not writable")

    def writable(self) -> bool:
        return False

    def write(self, __s: bytes) -> int:
        raise NotImplementedError("Stream is not writable")

    def writelines(self, __lines: Iterable[bytes]) -> None:
        raise NotImplementedError("Stream is not writable")

    def __next__(self) -> bytes:
        # IOBase [...] supports the iterator protocol, meaning that an IOBase object can be
        # iterated over yielding the lines in a stream. [...] See readline().
        result = self.readline()
        if len(result) == 0:
            raise StopIteration
        return result

    def __iter__(self) -> "BinaryIO":
        return self

    def __enter__(self) -> "BinaryIO":
        self._head_stream.__enter__()
        self._tail_stream.__enter__()
        return self

    def __exit__(self, __type, __value, __traceback) -> None:
        self._head_stream.__exit__(__type, __value, __traceback)
        self._tail_stream.__exit__(__type, __value, __traceback)

    def __str__(self) -> str:
        return f"Concat: {self._head_stream}, {self._tail_stream}]"


class _PresignedUrlDistributor:
    """
    Distributes and manages presigned URLs for downloading files.

    This class ensures thread-safe access to a presigned URL, allowing retrieval and invalidation.
    When the URL is invalidated, a new one will be fetched using the provided function.
    """

    def __init__(self, get_new_url_func: Callable[[], CreateDownloadUrlResponse]):
        """
        Initialize the distributor.

        Args:
            get_new_url_func: A callable that returns a new presigned URL response.
        """
        self._get_new_url_func = get_new_url_func
        self._current_url = None
        self.current_version = 0
        self.lock = threading.RLock()

    def get_url(self) -> tuple[CreateDownloadUrlResponse, int]:
        """
        Get the current presigned URL and its version.

        Returns:
            A tuple containing the current presigned URL response and its version.
        """
        with self.lock:
            if self._current_url is None:
                self._current_url = self._get_new_url_func()
            return self._current_url, self.current_version

    def invalidate_url(self, version: int) -> None:
        """
        Invalidate the current presigned URL if the version matches. If the version does not match,
        the URL remains unchanged. This ensures that only the most recent version can invalidate the URL.

        Args:
            version: The version to check before invalidating the URL.
        """
        with self.lock:
            if version == self.current_version:
                self._current_url = None
                self.current_version += 1


# ======================== Failures, retries and the endpoint walk ========================


@dataclass(frozen=True)
class _Failure:
    """A failure handed back by an endpoint client: what the walk should do with it."""

    error: BaseException
    """Raised as is at the public API."""
    decision: str
    """"walk" or "raise". Retries already happened inside the client."""


@dataclass(frozen=True)
class _RetryBudget:
    max_attempts_opt: Optional[int]
    timeout: timedelta
    max_retries_without_progress_opt: Optional[int] = None


class _TransferStatus:
    """One transfer on one endpoint. Shared by every thread of that transfer.

    Set only by the walk side: the walking stream, the range helper and _upload_to. Clients only read it. Both
    flags are only ever set, never cleared, so a thread reads them without a lock.
    """

    def __init__(
        self,
        committed: bool = False,
        cancelled: bool = False,
        is_last_endpoint: bool = False,
        retries_before_commit: int = 0,
    ):
        # Set on the first acknowledged byte.
        self.committed = committed
        # Set on the first failure when running in parallel.
        self.cancelled = cancelled
        # No endpoint is left to walk to, so a failure before commit is retried instead of walked.
        self.is_last_endpoint = is_last_endpoint
        # How often a request is retried before commit when another endpoint is left.
        self.retries_before_commit = retries_before_commit

    def commit(self) -> None:
        self.committed = True

    def cancel(self) -> None:
        self.cancelled = True


class _RequestFailed(Exception):
    """A failed request inside an endpoint client: the error to surface, and what deciding needs to know."""

    def __init__(
        self,
        error: BaseException,
        status_code_opt: Optional[int] = None,
        decision_opt: Optional[str] = None,
    ):
        super().__init__(str(error))
        self.error = error
        self.status_code_opt = status_code_opt
        self.decision_opt = decision_opt


class _UrlExpired(Exception):
    """A presigned URL was answered with the cloud's "URL expired" error."""


_RETRYABLE_STATUS_CODES = (408, 429, 502, 503, 504)


def _unwrap(failure: BaseException) -> BaseException:
    return failure.error if isinstance(failure, _RequestFailed) else failure


def _api_client_decision(failure: BaseException) -> str:
    """The API client's rules: a throttled response, a dropped connection or a timeout is retried.

    Anything else walks, as no rule says it is certain to fail everywhere.
    """
    if isinstance(failure, _RequestFailed) and failure.decision_opt is not None:
        return failure.decision_opt
    error = _unwrap(failure)
    if isinstance(error, AlreadyExists):
        return "raise"
    if getattr(error, "retry_after_secs", None) is not None or _BaseClient._is_retryable(error) is not None:
        return "retry"
    if not isinstance(error, (requests.RequestException, DatabricksError, ValueError, OSError, _UrlExpired)):
        _LOG.warning(f"Unexpected error, trying the next endpoint: {error!r}", exc_info=error)
    return "walk"


def _common_decision(failure: BaseException) -> str:
    """The rows every endpoint shares: 408, 429, 502, 503 and 504 responses are retried, a 412 raises, then the API
    client's rules."""
    if isinstance(failure, _RequestFailed) and failure.decision_opt is None:
        if failure.status_code_opt in _RETRYABLE_STATUS_CODES:
            return "retry"
        if failure.status_code_opt == 412:
            # The file no longer matches the request's precondition, on every endpoint.
            return "raise"
    return _api_client_decision(failure)


def _exhausted_error(budget: _RetryBudget, attempts: int, last: Optional[BaseException]) -> BaseException:
    """The error the SDK's retry helper raises once its budget is spent, so callers see the same types."""
    if budget.max_attempts_opt is not None and attempts > budget.max_attempts_opt:
        error: BaseException = RuntimeError(f"Exceeded max retry attempts ({budget.max_attempts_opt})")
    else:
        error = TimeoutError(f"Timed out after {budget.timeout}")
    error.__cause__ = last
    return error


def _sleep(clock, seconds: float, status: _TransferStatus) -> None:
    """Waits, waking early once the transfer is cancelled."""
    remaining = seconds
    while remaining > 0 and not status.cancelled:
        step = min(remaining, 1.0)
        clock.sleep(step)
        remaining -= step


def _retry(
    send: Callable[[], T],
    decide: Callable[[BaseException], str],
    budget: _RetryBudget,
    status: _TransferStatus,
    clock,
    before_retry_opt: Optional[Callable[[], None]] = None,
    can_retry_opt: Optional[Callable[[], bool]] = None,
) -> Union[T, _Failure]:
    """The one retry loop, called by every client.

    Sends until it succeeds, until decide() says walk or raise, until the budget is used up (then walk), or until
    the status is cancelled. Before commit it retries only status.retries_before_commit times unless this is the last
    endpoint: walking is cheaper than waiting. Waits min(10, attempt) seconds plus jitter, or Retry-After. The wait wakes early if the status is
    cancelled.
    """
    deadline = clock.time() + budget.timeout.total_seconds()
    attempt = 1
    last: Optional[BaseException] = None
    while clock.time() < deadline and (budget.max_attempts_opt is None or attempt <= budget.max_attempts_opt):
        try:
            return send()
        except Exception as e:
            last = e
        decision = decide(last)
        if decision != "retry":
            return _Failure(_unwrap(last), decision)
        if (
            status.cancelled
            or (not (status.committed or status.is_last_endpoint) and attempt > status.retries_before_commit)
            or (can_retry_opt is not None and not can_retry_opt())
        ):
            return _Failure(_unwrap(last), "walk")
        if budget.max_attempts_opt is not None and attempt >= budget.max_attempts_opt:
            attempt += 1
            break
        retry_after = getattr(_unwrap(last), "retry_after_secs", None)
        wait = retry_after if retry_after is not None else min(10, attempt)
        _LOG.debug(f"Retrying after {_unwrap(last)} (sleeping ~{wait}s)")
        if before_retry_opt is not None:
            before_retry_opt()
        _sleep(clock, wait + random.random(), status)
        if status.cancelled:
            return _Failure(_unwrap(last), "walk")
        attempt += 1
    return _Failure(_exhausted_error(budget, attempt, _unwrap(last) if last else None), "walk")


def _may_walk(
    failure: _Failure, status: _TransferStatus, has_next_endpoint: bool, can_send_again: Callable[[], bool]
) -> bool:
    """The one walk rule, shared by _walk_endpoints and _WalkingDownloadStream."""
    return failure.decision == "walk" and not status.committed and has_next_endpoint and can_send_again()


_AttemptOnEndpoint = Callable[[Any, _TransferStatus], Optional[_Failure]]
"""One attempt of a transfer on one endpoint client, with that attempt's status."""


def _walk_endpoints(
    clients: list,
    attempt: _AttemptOnEndpoint,
    can_send_again: Callable[[], bool] = lambda: True,
    before_next_endpoint: Callable[[], None] = lambda: None,
    retries_before_commit: int = 0,
) -> None:
    """Runs the transfer on each client in order with a new _TransferStatus.

    Returns once one succeeds. Moves on only if the failure is walk, the transfer is not committed, and the data can
    be sent again. Otherwise raises the failure's error.
    """
    for index, client in enumerate(clients):
        status = _TransferStatus(
            is_last_endpoint=index + 1 == len(clients), retries_before_commit=retries_before_commit
        )
        failure_opt = attempt(client, status)
        if failure_opt is None:
            return
        if not _may_walk(failure_opt, status, index + 1 < len(clients), can_send_again):
            raise failure_opt.error
        _LOG.info(f"{client.name} failed before commit, trying the next endpoint: {failure_opt.error}")
        before_next_endpoint()
    raise ValueError("No endpoint can take this transfer")


def _run_in_parallel(
    parallelism: int,
    next_item: Callable[[], Optional[T]],
    work: Callable[[T, _TransferStatus], Optional[_Failure]],
    status: _TransferStatus,
) -> Optional[_Failure]:
    """Runs work(item) on up to `parallelism` threads until next_item() returns None.

    Creates and shuts down its own threads on each call; it holds no state between calls. next_item is called under
    a lock. The first failure sets status.cancelled, so no new item starts, and is returned once every running item
    has finished.
    """
    lock = threading.Lock()
    failures: list = []

    def fail(failure: _Failure) -> None:
        with lock:
            if not failures:
                failures.append(failure)
            elif not isinstance(failure.error, _Cancelled):
                # The first failure decides; the others are only logged.
                _LOG.info(f"Another part of the transfer failed too: {failure.error!r}")
            status.cancel()

    def worker() -> None:
        while True:
            try:
                with lock:
                    if status.cancelled:
                        return
                    item = next_item()
            except Exception as e:
                fail(_Failure(e, "walk"))
                return
            if item is None:
                return
            try:
                failure_opt = work(item, status)
            except Exception as e:
                _LOG.warning(f"Unexpected error in a parallel transfer: {e!r}", exc_info=e)
                failure_opt = _Failure(e, "walk")
            if failure_opt is not None:
                fail(failure_opt)
                return

    if parallelism <= 1:
        worker()
    else:
        threads = [threading.Thread(target=worker) for _ in range(parallelism)]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
    return failures[0] if failures else None


# ======================== Downloads ========================


class _ByteRange(NamedTuple):
    """A byte range of a file: plain numbers, no sessions."""

    start: int
    end_opt: Optional[int]
    """Inclusive; None means to the end of the file."""

    def is_whole_file(self) -> bool:
        return self.start == 0 and self.end_opt is None

    def header(self) -> str:
        return f"bytes={self.start}-{'' if self.end_opt is None else self.end_opt}"


@dataclass
class _RangeResponse:
    """One open response to a GET of a byte range."""

    status_code: int
    content_length_opt: Optional[int]
    content_type_opt: Optional[str]
    last_modified_opt: Optional[str]
    chunks: Iterator[bytes]
    close: Callable[[], None]


class _Cancelled(Exception):
    """A parallel transfer was cancelled after another part of it failed."""


class _ResilientDownload:
    """One byte range from one endpoint. Created by the client's get_file_range, already open.

    Resumes after a break with Range from the current offset and If-Unmodified-Since (the caller's value, or else the
    first response's Last-Modified). Returns bytes, None at the end, or a _Failure that is walk or raise.
    """

    def __init__(
        self,
        get_file_range: Callable[
            [_ByteRange, Optional[str], Optional[int], _TransferStatus], Union[_RangeResponse, _Failure]
        ],
        resume_budget: _RetryBudget,
        status: _TransferStatus,
        byte_range: _ByteRange,
        if_unmodified_since_opt: Optional[str],
    ):
        self._get_file_range = get_file_range
        self._resume_budget = resume_budget
        self._status = status
        self._range = byte_range
        self._if_unmodified_since_opt = if_unmodified_since_opt
        self._offset = byte_range.start
        self._total_opt: Optional[int] = None
        self._response_opt: Optional[_RangeResponse] = None
        self._recovers = 0
        self._recovers_without_progress = 0
        self.content_length_opt: Optional[int] = None
        self.content_type_opt: Optional[str] = None
        self.last_modified_opt: Optional[str] = None

    def open(self) -> Optional[_Failure]:
        result = self._open_at(self._offset)
        if isinstance(result, _Failure):
            return result
        self.content_length_opt = result.content_length_opt
        self.content_type_opt = result.content_type_opt
        self.last_modified_opt = result.last_modified_opt
        if self._if_unmodified_since_opt is None:
            self._if_unmodified_since_opt = result.last_modified_opt
        if self._range.end_opt is None and result.content_length_opt is not None:
            self._total_opt = self._range.start + result.content_length_opt
        return None

    def _expected_length(self, requested: _ByteRange) -> Optional[int]:
        if requested.end_opt is not None:
            return requested.end_opt - requested.start + 1
        if self._total_opt is not None:
            return self._total_opt - requested.start
        return None

    def _open_at(self, offset: int) -> Union[_RangeResponse, _Failure]:
        requested = _ByteRange(offset, self._range.end_opt)
        result = self._get_file_range(
            requested, self._if_unmodified_since_opt, self._expected_length(requested), self._status
        )
        if not isinstance(result, _Failure):
            self._response_opt = result
        return result

    def _may_resume(self) -> bool:
        if not (self._status.committed or self._status.is_last_endpoint):
            return False
        max_total = self._resume_budget.max_attempts_opt
        max_without_progress = self._resume_budget.max_retries_without_progress_opt
        if max_total is not None and self._recovers >= max_total:
            return False
        if max_without_progress is not None and self._recovers_without_progress >= max_without_progress:
            return False
        return True

    def read_chunk(self) -> Union[bytes, None, _Failure]:
        while True:
            if self._status.cancelled:
                return _Failure(_Cancelled(), "walk")
            try:
                chunk = next(self._response_opt.chunks)
            except StopIteration:
                end_opt = self._end_opt()
                if end_opt is None or self._offset >= end_opt:
                    return None
                # A body cut short without an error (urllib3 1.x does not enforce Content-Length) is a break too.
                failure_opt = self._resume_after(IOError(f"The download ended at byte {self._offset} of {end_opt}"))
                if failure_opt is not None:
                    return failure_opt
                continue
            except requests.RequestException as e:
                failure_opt = self._resume_after(e)
                if failure_opt is not None:
                    return failure_opt
                continue
            except Exception as e:
                _LOG.warning(f"Unexpected error while reading a download: {e!r}", exc_info=e)
                return _Failure(e, "walk")
            if not chunk:
                continue
            end_opt = self._end_opt()
            if end_opt is not None and self._offset + len(chunk) > end_opt:
                # Bytes past the end would overwrite the next range of a parallel download.
                return _Failure(IOError(f"The download went past byte {end_opt}"), "walk")
            self._offset += len(chunk)
            self._recovers_without_progress = 0
            return chunk

    def _end_opt(self) -> Optional[int]:
        """The offset just past the last byte this download expects, if known."""
        return self._range.end_opt + 1 if self._range.end_opt is not None else self._total_opt

    def _resume_after(self, error: BaseException) -> Optional[_Failure]:
        """Reopens at the current offset after a break. A failed reopen surfaces the break, as the caller saw it."""
        if not self._may_resume():
            _LOG.debug("Download resume budget exceeded")
            return _Failure(error, "walk")
        if self._if_unmodified_since_opt is None:
            # Without it, a file changed in between would be spliced from two versions.
            _LOG.debug("Not resuming the download: no Last-Modified to guard it with")
            return _Failure(error, "walk")
        self._recovers += 1
        self._recovers_without_progress += 1
        self.close()
        _LOG.debug(f"Resuming the download from offset {self._offset}")
        result = self._open_at(self._offset)
        if isinstance(result, _Failure):
            return _Failure(error, result.decision)
        return None

    def close(self) -> None:
        if self._response_opt is not None:
            self._response_opt.close()


class _WalkingDownloadStream(Iterator[bytes]):
    """The endpoint walk for download(), done lazily: the caller's reads drive it.

    Opens the first endpoint in __init__, so the headers are known when download() returns.
    """

    def __init__(self, clients: list, path: str):
        self._clients = clients
        self._path = path
        self._index = -1
        self._status = _TransferStatus()
        self._download_opt: Optional[_ResilientDownload] = None
        self._closed = False
        self.last_modified_opt: Optional[str] = None
        self._open_next_endpoint()
        self.content_length_opt = self._download_opt.content_length_opt
        self.content_type_opt = self._download_opt.content_type_opt
        self.last_modified_opt = self._download_opt.last_modified_opt

    def _open_next_endpoint(self) -> None:
        """Opens the next endpoint that answers, from byte 0. Raises if no endpoint is left."""
        while True:
            self._index += 1
            self._status = _TransferStatus(is_last_endpoint=self._index + 1 == len(self._clients))
            client = self._clients[self._index]
            # Once download() returned the first endpoint's metadata, a changed file must fail, not be served under it.
            download = client.get_file_range(self._path, _ByteRange(0, None), self.last_modified_opt, self._status)
            if not isinstance(download, _Failure):
                self._download_opt = download
                return
            if not _may_walk(download, self._status, self._index + 1 < len(self._clients), lambda: True):
                raise download.error
            _LOG.info(f"{client.name} failed before any data was received, trying the next endpoint: {download.error}")

    def __next__(self) -> bytes:
        if self._closed:
            raise ValueError("I/O operation on closed file")
        while True:
            chunk = self._download_opt.read_chunk()
            if isinstance(chunk, bytes):
                self._status.commit()
                return chunk
            if chunk is None:
                raise StopIteration
            if not _may_walk(chunk, self._status, self._index + 1 < len(self._clients), lambda: True):
                raise chunk.error
            _LOG.info(
                f"{self._clients[self._index].name} failed before any data was received, trying the next endpoint: "
                f"{chunk.error}"
            )
            self._download_opt.close()
            self._open_next_endpoint()

    # Follows the _RawResponse interface, so that _StreamingResponse can read from it.
    def iter_content(self, chunk_size: Optional[int] = None, decode_unicode: bool = False) -> Iterator[bytes]:
        if decode_unicode:
            raise ValueError("Decode unicode is not supported")
        return self

    def close(self) -> None:
        if self._download_opt is not None:
            self._download_opt.close()
        self._closed = True


class _DownloadDestination:
    """Where download_to writes.

    A new destination gets a temp file next to it, moved into place once the download finishes, so a failed download
    leaves nothing behind. An existing one is written in place, as open() would: through a symlink, keeping its
    permissions, owner and links, and into a pipe or a device.
    """

    def __init__(self, destination: str, temp_path_opt: Optional[str], size_opt: Optional[int]):
        self._destination = destination
        self._temp_path_opt = temp_path_opt
        self._size_opt = size_opt
        self._lock = threading.Lock()
        self._file_opt: Optional[BinaryIO] = None
        self._position = 0

    @classmethod
    def create(cls, destination: str, size_opt: Optional[int]) -> "_DownloadDestination":
        """For a known size, the file is given that length first, so ranges can be written at any offset."""
        # lexists, so that a broken symlink is written through rather than replaced.
        if os.path.lexists(destination):
            return cls(destination, None, size_opt)
        directory = os.path.dirname(os.path.abspath(destination))
        while True:
            path = os.path.join(directory, f".download-{secrets.token_hex(8)}")
            try:
                # Like mkstemp, but with mode 0o666, so the process umask applies without changing it.
                fd = os.open(path, os.O_RDWR | os.O_CREAT | os.O_EXCL | getattr(os, "O_BINARY", 0), 0o666)
                break
            except FileExistsError:
                continue
        os.close(fd)
        if size_opt is not None:
            os.truncate(path, size_opt)
        return cls(destination, path, None)

    @staticmethod
    def takes_ranges(destination: str) -> bool:
        """Whether ranges can be written at any offset: a new file or a regular one, after following symlinks."""
        try:
            return stat.S_ISREG(os.stat(destination).st_mode)
        except FileNotFoundError:
            return True

    def write_at(self, offset: int, data: bytes) -> None:
        with self._lock:
            if self._file_opt is None:
                self._file_opt = self._open()
            # Only ranges seek, so a pipe is only appended to.
            if offset != self._position:
                self._file_opt.seek(offset)
            self._file_opt.write(data)
            self._position = offset + len(data)

    def _open(self) -> BinaryIO:
        if self._temp_path_opt is not None:
            return open(self._temp_path_opt, "r+b")
        # Opened on the first byte, so a download that fails before any data leaves an existing file as it was.
        f = open(self._destination, "wb")
        if self._size_opt is not None:
            f.truncate(self._size_opt)
        return f

    def _close(self) -> None:
        if self._file_opt is not None:
            self._file_opt.close()
            self._file_opt = None

    def finish(self) -> None:
        with self._lock:
            if self._file_opt is None and self._temp_path_opt is None:
                # An empty download still empties an existing file.
                self._file_opt = self._open()
            self._close()
        if self._temp_path_opt is not None:
            # Unlike shutil.move, raises for a directory, and replaces a file atomically on Windows too.
            os.replace(self._temp_path_opt, self._destination)

    def discard(self) -> None:
        """After a failure: a temp file is removed, and an existing destination keeps what was written."""
        with self._lock:
            self._close()
        if self._temp_path_opt is not None and os.path.exists(self._temp_path_opt):
            os.remove(self._temp_path_opt)


def _split_into_ranges(size: int, part_size: int) -> list:
    return [_ByteRange(start, min(start + part_size, size) - 1) for start in range(0, size, part_size)]


def _download_ranges_to_file(
    client,
    status: _TransferStatus,
    *,
    path: str,
    ranges: list,
    last_modified: Optional[str],
    destination: _DownloadDestination,
    parallelism: int,
) -> Optional[_Failure]:
    """Downloads every range from one endpoint into the destination, on up to `parallelism` threads.

    Marks the status committed on the first chunk of any range.
    """

    def download_range(byte_range: _ByteRange, status: _TransferStatus) -> Optional[_Failure]:
        download = client.get_file_range(path, byte_range, last_modified, status)
        if isinstance(download, _Failure):
            return download
        try:
            offset = byte_range.start
            while True:
                chunk = download.read_chunk()
                if not isinstance(chunk, bytes):
                    return chunk
                status.commit()
                destination.write_at(offset, chunk)
                offset += len(chunk)
        finally:
            download.close()

    return _run_in_parallel(parallelism, _next_or_none(ranges), download_range, status)


def _next_or_none(items: list) -> Callable[[], Optional[Any]]:
    iterator = iter(items)
    return lambda: next(iterator, None)


# ======================== Uploads ========================


class _UploadData:
    """The bytes being uploaded (a file, a seekable stream or a one-pass stream), and whether they can be sent again
    from the start.

    A one-pass stream keeps every byte read until the upload is committed, which a multipart upload limits to the
    first part, so that the next endpoint can be sent the same bytes.
    """

    def __init__(self, path_opt: Optional[str], stream_opt: Optional[BinaryIO], size_opt: Optional[int]):
        self._path_opt = path_opt
        self._stream_opt = stream_opt
        self.size_opt = size_opt
        self._lock = threading.RLock()
        self._rewindable = path_opt is not None or (stream_opt is not None and stream_opt.seekable())
        self._part_number = 0
        # One-pass streams only: the bytes kept for a replay, the offset of their first byte, the offset of the next
        # byte to hand out, whether bytes read from now on are kept, whether the stream ended, and whether bytes were
        # handed out without being kept.
        self._replay = bytearray()
        self._replay_start = 0
        self._position = 0
        self._retaining = True
        self._eof = False
        self._lost = False
        self._stream_bytes_read = 0

    @classmethod
    def from_file(cls, path: str) -> "_UploadData":
        return cls(path, None, os.path.getsize(path))

    @classmethod
    def from_stream(cls, stream: BinaryIO) -> "_UploadData":
        size_opt = None
        if stream.seekable():
            stream.seek(0, os.SEEK_END)
            size_opt = stream.tell()
            stream.seek(0)
        return cls(None, stream, size_opt)

    def _source(self) -> BinaryIO:
        if self._stream_opt is None:
            self._stream_opt = open(self._path_opt, "rb")
        return self._stream_opt

    def _read_stream(self, n: int) -> bytes:
        """Reads n bytes, or fewer only at the end: a raw stream may return less than asked before it ends."""
        # A bytearray, as appending to bytes copies what was read so far, for every short read.
        data = bytearray()
        while len(data) < n:
            more = self._source().read(n - len(data))
            if not more:
                self._eof = True
                break
            data += more
        self._stream_bytes_read += len(data)
        if self._eof:
            self.size_opt = self._stream_bytes_read
        return bytes(data)

    def read_ahead(self, n: int) -> None:
        """Reads up to n bytes of a one-pass stream ahead and keeps them for read, so a shorter stream learns its size.

        A file or a seekable stream knows its size already.
        """
        with self._lock:
            if self._rewindable:
                return
            available = self._replay_start + len(self._replay) - self._position
            if available < n and not self._eof:
                self._replay += self._read_stream(n - available)

    def read(self, n: int) -> bytes:
        with self._lock:
            if self._rewindable:
                return self._source().read(n)
            start = self._position - self._replay_start
            out = bytes(self._replay[start : start + n])
            if len(out) < n and not self._eof:
                more = self._read_stream(n - len(out))
                if self._retaining:
                    self._replay += more
                elif more:
                    self._lost = True
                out += more
            self._position += len(out)
            return out

    def next_part(self, size: int) -> Optional[tuple]:
        """The next part and its number, from 1, or None at the end."""
        with self._lock:
            data = self.read(size)
            if not data:
                return None
            self._part_number += 1
            return self._part_number, data

    def whole(self) -> BinaryIO:
        """The data for a single-shot PUT, from the start."""
        with self._lock:
            if self._rewindable:
                source = self._source()
                source.seek(0)
                return source
            if self._eof and self._replay_start == 0 and not self._lost:
                return BytesIO(bytes(self._replay))
            # The rest is streamed and can't be read again.
            self._lost = True
            start = self._position - self._replay_start
            return _ConcatenatedInputStream(BytesIO(bytes(self._replay[start:])), self._source())

    def can_send_again(self) -> bool:
        with self._lock:
            return self._rewindable or (self._replay_start == 0 and not self._lost)

    def restart(self) -> None:
        with self._lock:
            self._part_number = 0
            if self._rewindable:
                self._source().seek(0)
            elif self.can_send_again():
                self._position = 0

    def drop_replay_buffer(self) -> None:
        """Called at commit: nothing will be sent again from the start."""
        with self._lock:
            if self._rewindable:
                return
            start = self._position - self._replay_start
            del self._replay[:start]
            self._replay_start = self._position
            self._retaining = False

    def close(self) -> None:
        if self._path_opt is not None and self._stream_opt is not None:
            self._stream_opt.close()
            self._stream_opt = None


@dataclass(frozen=True)
class _UploadPlan:
    """How the data is sent to one endpoint.

    multipart: a multipart upload session (initiate_upload) with parts of part_size bytes on up to parallelism
    threads, their presigned URLs requested batch_size at a time. Otherwise one PUT of the whole file (put_file).
    """

    multipart: bool
    part_size: int
    parallelism: int
    batch_size: int = 1


def _plan_upload(
    data: _UploadData,
    client,
    use_parallel: bool,
    parallelism: Optional[int],
    part_size: int,
    batch_size: int,
    min_stream_size: int,
) -> Optional[_UploadPlan]:
    """The plan for this data on this client, or None if the client can't take it: single-shot on IO_OFFLOAD, or data
    of known size over the client's single-request limit (max_single_shot_size_opt).

    Single-shot below the multipart threshold, for empty data (a multipart upload needs a part), or when the client
    has no multipart; part size capped at client.max_part_size_opt. Data of unknown size goes multipart, so a one-pass
    stream is read ahead first: a short one then knows its size.
    """
    small = data.size_opt is not None and data.size_opt < max(min_stream_size, 1)
    if small or not client.supports_multipart:
        limit_opt = client.max_single_shot_size_opt
        if not client.supports_single_shot or (
            limit_opt is not None and data.size_opt is not None and data.size_opt > limit_opt
        ):
            return None
        return _UploadPlan(False, part_size, 1)
    if client.max_part_size_opt is not None:
        part_size = min(part_size, client.max_part_size_opt)
    if use_parallel:
        return _UploadPlan(True, part_size, parallelism or 1, 1)
    return _UploadPlan(True, part_size, 1, batch_size)


class _MultipartUploadSession(ABC):
    @abstractmethod
    def put_part(self, number: int, data: bytes, status: _TransferStatus) -> Union[str, _Failure]:
        """Uploads one part and returns its ETag."""

    @abstractmethod
    def complete(self, etags: dict, status: _TransferStatus) -> Optional[_Failure]:
        """Completes the upload."""

    @abstractmethod
    def abort(self) -> None:
        """Sent once, never retried; a failure is only logged."""


def _upload_to(
    client,
    status: _TransferStatus,
    *,
    plans: dict,
    path: str,
    overwrite_opt: Optional[bool],
    data: _UploadData,
) -> Optional[_Failure]:
    """Uploads the data to one endpoint with its plan. Aborts the upload session once on any failure.

    Marks the status committed on the first acknowledgment. Never retries: the client does.
    """
    plan = plans[client]
    if not plan.multipart:
        failure_opt = client.put_file(path, overwrite_opt, data, status)
        if failure_opt is None:
            status.commit()
        return failure_opt
    session = client.initiate_upload(path, overwrite_opt, status, part_url_batch_size=plan.batch_size)
    if isinstance(session, _Failure):
        return session
    try:
        failure_opt = _multipart_upload(session, data, plan, status)
    except BaseException:
        session.abort()
        raise
    if failure_opt is not None:
        session.abort()
    return failure_opt


def _multipart_upload(
    session: _MultipartUploadSession, data: _UploadData, plan: _UploadPlan, status: _TransferStatus
) -> Optional[_Failure]:
    first = data.next_part(plan.part_size)
    if first is None:
        # _plan_upload sends empty data in a single shot.
        raise ValueError("A multipart upload was planned for empty data")
    # The first part goes alone: its ETag is the commit point.
    number, content = first
    etag = session.put_part(number, content, status)
    if isinstance(etag, _Failure):
        return etag
    status.commit()
    data.drop_replay_buffer()
    etags = {number: etag}
    lock = threading.Lock()

    def upload_part(part: tuple, status: _TransferStatus) -> Optional[_Failure]:
        number, content = part
        etag = session.put_part(number, content, status)
        if isinstance(etag, _Failure):
            return etag
        with lock:
            etags[number] = etag
        return None

    failure_opt = _run_in_parallel(plan.parallelism, lambda: data.next_part(plan.part_size), upload_part, status)
    if failure_opt is not None:
        return failure_opt
    return session.complete(etags, status)
