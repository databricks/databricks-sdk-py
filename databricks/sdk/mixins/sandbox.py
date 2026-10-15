"""Sandbox command-execution mixin.

Extends the generated :class:`~databricks.sdk.service.sandbox.SandboxAPI` with
``execute_command`` and ``connect_command``, which return a
:class:`CommandProcess` handle exposing a command's stdout, stderr, stdin, and
exit code as an ergonomic, file-like interface - without the caller handling the
raw gRPC process-event stream.

The handle is implemented over the sandbox daemon's streaming RPCs
(ExecuteCommand / AttachCommand / StreamInput), which codegen does not produce a
client for; those run internally on the generic gRPC transport in
:mod:`databricks.sdk.mixins._grpc_transport` and are not part of the public API.

The wire types come from the committed stubs in
:mod:`databricks.sdk._sandbox_grpc` (generated from a slim copy of the sandbox
daemon proto; see that package for provenance). grpcio and those stubs are
imported lazily inside the methods, so this module imports without the optional
``sandbox`` extra installed.
"""

from __future__ import annotations

import codecs
import itertools
import queue
import threading
import time
from enum import Enum
from typing import TYPE_CHECKING, Callable, Dict, Iterable, Iterator, Optional, Tuple, Union

from databricks.sdk.mixins._grpc_transport import (
    _DEFAULT_MAX_ATTEMPTS,
    _DEFAULT_RETRY_INTERVAL_SECONDS,
    _is_unavailable,
    open_channel,
    open_stream_with_retry,
)
from databricks.sdk.service.sandbox import SandboxAPI

if TYPE_CHECKING:
    from databricks.sdk._sandbox_grpc import sandbox_service_pb2 as _pb
    from databricks.sdk._sandbox_grpc import sandbox_service_pb2_grpc as _pb_grpc

# gRPC metadata key that routes a command RPC to a specific sandbox.
_SANDBOX_NAME_METADATA = "x-databricks-sandbox-name"

_Metadata = Tuple[Tuple[str, str], ...]


def _never_retry(_error: Exception) -> bool:
    """Retry predicate for the ExecuteCommand stream open: never retry.
    ExecuteCommand starts a process and is not idempotent (its ``command_id`` is
    a stream-resume token, not a dedup key), so re-issuing a failed open could
    run the command twice."""
    return False


_EOF = object()

# Input chunks a CommandStdin holds before write() blocks.
_STDIN_BUFFERED_CHUNKS = 16

# How long close() waits for the reader thread to tear down before returning.
_CLOSE_TEARDOWN_TIMEOUT = 10.0


class StreamMode(Enum):
    """Where :meth:`SandboxExt.execute_command` sends a command's stdout or stderr."""

    PIPE = "PIPE"
    """Buffer the output in memory for reading from the :class:`CommandProcess`."""

    DEVNULL = "DEVNULL"
    """Discard the output."""

    STDOUT = "STDOUT"
    """Only settable for stderr; sends both stderr and stdout to stdout."""


class CommandOutput:
    """Read-only, file-like view of a command's stdout or stderr.

    Iterate it for lines as the command writes them, call :meth:`readline` for a
    single line, or :meth:`read` for up to ``size`` units (all remaining by
    default). :meth:`read1` returns output the instant it arrives, which may not
    end on a line boundary. Values are ``str`` when the command was started with
    ``text=True`` and ``bytes`` otherwise. Output is buffered in memory until
    read, so read every stream left as :attr:`StreamMode.PIPE`. Reads unblock
    when the command exits, its stream fails, or the :class:`CommandProcess` is
    closed.
    """

    def __init__(self, process: "CommandProcess", text: bool):
        self._process = process
        self._chunks: "queue.Queue[object]" = queue.Queue()
        # Incremental, so a multi-byte character split across chunks decodes intact.
        self._decoder = codecs.getincrementaldecoder("utf-8")(errors="replace") if text else None
        self._empty: Union[str, bytes] = "" if text else b""
        self._newline: Union[str, bytes] = "\n" if text else b"\n"
        self._buffer: Union[str, bytes] = self._empty  # pulled from the queue, not yet returned
        self._eof = False

    def read(self, size: int = -1, *, timeout: Optional[float] = None) -> Union[str, bytes]:
        """Read up to ``size`` units (characters when ``text=True``, else bytes).

        ``size < 0`` (default) returns all remaining output, blocking until the
        command exits. Raises ``TimeoutError`` if ``timeout`` seconds pass first;
        output read so far stays buffered for the next call.
        """
        deadline = None if timeout is None else time.monotonic() + timeout
        if size < 0:
            while not self._eof:
                self._fill(deadline)
            data, self._buffer = self._buffer, self._empty
            return data
        while len(self._buffer) < size and not self._eof:
            self._fill(deadline)
        data, self._buffer = self._buffer[:size], self._buffer[size:]
        return data

    def readline(self, *, timeout: Optional[float] = None) -> Union[str, bytes]:
        """Return the next line including its trailing newline; ``''``/``b''`` at EOF.

        Raises ``TimeoutError`` if ``timeout`` seconds pass before a line or EOF.
        """
        deadline = None if timeout is None else time.monotonic() + timeout
        while self._newline not in self._buffer and not self._eof:
            self._fill(deadline)
        split = self._buffer.find(self._newline)
        if split == -1:
            line, self._buffer = self._buffer, self._empty
        else:
            end = split + len(self._newline)
            line, self._buffer = self._buffer[:end], self._buffer[end:]
        return line

    def __iter__(self) -> Iterator[Union[str, bytes]]:
        """Iterate output line by line, like a file."""
        while True:
            line = self.readline()
            if line == self._empty:
                return
            yield line

    def read1(self, size: int = -1, *, timeout: Optional[float] = None) -> Union[str, bytes]:
        """Return output as soon as any is available, without waiting for a full
        line or for ``size`` units; ``''``/``b''`` at EOF.

        At most ``size`` units are returned when ``size >= 0``. For incremental
        output with no trailing newline, such as a prompt. Raises ``TimeoutError``
        if ``timeout`` seconds pass before output or EOF.
        """
        deadline = None if timeout is None else time.monotonic() + timeout
        while not self._buffer and not self._eof:
            self._fill(deadline)
        if size < 0:
            data, self._buffer = self._buffer, self._empty
        else:
            data, self._buffer = self._buffer[:size], self._buffer[size:]
        return data

    def _fill(self, deadline: Optional[float]) -> None:
        chunk = self._next_chunk(deadline)
        if chunk is not None:
            self._buffer += chunk

    def _next_chunk(self, deadline: Optional[float]) -> Optional[Union[str, bytes]]:
        remaining = None if deadline is None else max(0.0, deadline - time.monotonic())
        try:
            item = self._chunks.get(timeout=remaining)
        except queue.Empty:
            raise TimeoutError(f"command {self._process._command_id} produced no further output within the timeout")
        if item is _EOF:
            self._chunks.put(_EOF)
            self._eof = True
            self._process._raise_if_failed()
            return None
        return item

    def _append(self, data: bytes) -> None:
        self._put(self._decoder.decode(data) if self._decoder else data)

    def _finish(self) -> None:
        if self._decoder:
            self._put(self._decoder.decode(b"", final=True))
        self._chunks.put(_EOF)

    def _put(self, chunk: Union[str, bytes]) -> None:
        if chunk:
            self._chunks.put(chunk)


class _DiscardedOutput:
    """Sink for a stream set to :attr:`StreamMode.DEVNULL`."""

    def _append(self, data: bytes) -> None:
        pass


class CommandStdin:
    """The stdin of a :class:`CommandProcess`.

    The first :meth:`write` opens an input stream to the command that stays open
    until :meth:`close`, which sends end-of-file. A command that reads stdin to
    the end (for example ``cat``) keeps running until stdin is closed. Once the
    command exits, stdin is closed and :meth:`write` raises ``ValueError``.
    :meth:`write` blocks while earlier input is still waiting to be sent.
    """

    def __init__(self, sandbox: "SandboxExt", name: str, command_id: str):
        self._sandbox = sandbox
        self._name = name
        self._command_id = command_id
        self._chunks: "queue.Queue[object]" = queue.Queue(maxsize=_STDIN_BUFFERED_CHUNKS)
        # Serializes the closed check, sender start, and enqueue, so one sender
        # runs per stdin and no input is queued behind end-of-file.
        self._lock = threading.Lock()
        self._sender: Optional[threading.Thread] = None
        self._error: Optional[BaseException] = None
        self._closed = False

    def write(self, data: Union[str, bytes]) -> None:
        """Send ``data`` to the command's stdin. ``str`` is encoded as UTF-8."""
        chunk = data.encode("utf-8") if isinstance(data, str) else data
        with self._lock:
            if self._closed:
                raise ValueError("stdin is closed")
            self._raise_if_failed()
            self._start_sender()
            self._chunks.put(chunk)

    def close(self) -> None:
        """Send end-of-file to the command's stdin and wait until all input is sent."""
        with self._lock:
            if self._closed:
                return
            self._closed = True
            self._start_sender()
            self._chunks.put(_EOF)
        self._sender.join()
        self._raise_if_failed()

    def _start_sender(self) -> None:
        if self._sender is not None:
            return
        self._sender = threading.Thread(target=self._send, daemon=True)
        self._sender.start()

    def _send(self) -> None:
        def chunks() -> Iterator[bytes]:
            while True:
                chunk = self._chunks.get()
                if chunk is _EOF:
                    return
                yield chunk

        try:
            self._sandbox._stream_input(self._name, self._command_id, chunks())
        except Exception as e:  # noqa: BLE001 - surfaced to the caller by write() / close()
            self._error = e
            # Unblock a write() waiting on the full queue so it can see the error.
            while not self._chunks.empty():
                self._chunks.get_nowait()

    def _abandon(self) -> None:
        """Close stdin once the command has exited, releasing any open input stream."""
        with self._lock:
            if self._closed:
                return
            self._closed = True
            if self._sender is not None:
                self._chunks.put(_EOF)

    def _raise_if_failed(self) -> None:
        if self._error is not None:
            raise self._error


class _StreamHandle:
    """A server-streaming gRPC call plus the per-call channel it owns.

    Closing the channel from another thread cancels an in-flight read, so a
    :class:`CommandProcess` can wake its reader thread out of a blocked ``next()``
    and release the channel on :meth:`CommandProcess.close`. The caller owns the
    channel and must :meth:`close` it when done iterating.
    """

    def __init__(self, channel: object, stream: Iterator):
        self._channel = channel
        self._stream = stream

    def __iter__(self) -> Iterator:
        return iter(self._stream)

    def close(self) -> None:
        # cancel() (forwarded to the live gRPC call) and the channel close are
        # both idempotent and safe to call while another thread is in next().
        cancel = getattr(self._stream, "cancel", None)
        if cancel is not None:
            try:
                cancel()
            except Exception:  # noqa: BLE001 - best-effort teardown
                pass
        self._channel.close()


class CommandProcess:
    """Handle to a command running in a sandbox, returned by
    :meth:`SandboxExt.execute_command` and :meth:`SandboxExt.connect_command`.

    Read output from :attr:`stdout` and :attr:`stderr`, send input with
    :attr:`stdin`, and call :meth:`wait` for the exit code. A background thread
    receives the command's output; if the connection is interrupted, it
    reconnects and resumes where it left off.

    Call :meth:`close` to stop receiving output and release the stream and
    thread; the handle is also a context manager that closes on exit. ``close``
    tears down the client side only - the command keeps running in the sandbox.
    """

    def __init__(
        self,
        sandbox: "SandboxExt",
        name: str,
        command_id: str,
        *,
        text: bool,
        stdout: StreamMode,
        stderr: StreamMode,
    ):
        if stdout is StreamMode.STDOUT:
            raise ValueError("StreamMode.STDOUT is only valid for stderr")
        self._sandbox = sandbox
        self._name = name
        self._command_id = command_id
        self._pid: Optional[int] = None
        self._exit_code: Optional[int] = None
        self._error: Optional[BaseException] = None
        self._done = threading.Event()
        # Guards _closed and _stream_handle against the reader thread's reconnect.
        self._lock = threading.Lock()
        self._closed = False
        self._stream_handle: Optional["_StreamHandle"] = None
        self.stdout = CommandOutput(self, text)
        self.stderr = CommandOutput(self, text)
        self.stdin = CommandStdin(sandbox, name, command_id)
        self._stdout_sink = self.stdout if stdout is StreamMode.PIPE else _DiscardedOutput()
        self._stderr_sink = {
            StreamMode.PIPE: self.stderr,
            StreamMode.DEVNULL: _DiscardedOutput(),
            StreamMode.STDOUT: self._stdout_sink,
        }[stderr]

    def __enter__(self) -> "CommandProcess":
        return self

    def __exit__(self, *exc_info: object) -> None:
        self.close()

    @property
    def command_id(self) -> str:
        """Identifier of the command; pass it to :meth:`SandboxExt.connect_command`
        to get a new handle to the same command."""
        return self._command_id

    @property
    def pid(self) -> Optional[int]:
        """Process ID of the command in the sandbox, once known."""
        return self._pid

    @property
    def exit_code(self) -> Optional[int]:
        """Exit code of the command, or ``None`` while it is still running."""
        return self._exit_code

    def wait(self, timeout: Optional[float] = None) -> int:
        """Block until the command exits and return its exit code.

        Raises ``TimeoutError`` if ``timeout`` seconds pass first (the command
        keeps running; call :meth:`close` to give up on it), and re-raises the
        error if the command's output stream failed.
        """
        if not self._done.wait(timeout):
            raise TimeoutError(f"command {self._command_id} did not exit within {timeout} seconds")
        self._raise_if_failed()
        if self._exit_code is None:
            raise RuntimeError(f"command {self._command_id} did not report an exit code; the handle was closed")
        return self._exit_code

    def close(self) -> None:
        """Stop receiving the command's output and release the stream and reader
        thread. Unblocks a pending :meth:`wait` or output read. Idempotent.

        This tears down the client side only: the command keeps running in the
        sandbox. Reconnect later with :meth:`SandboxExt.connect_command`, or stop
        the command itself through the sandbox.
        """
        with self._lock:
            if self._closed:
                return
            self._closed = True
            handle = self._stream_handle
        if handle is not None:
            # Closing the channel wakes the reader thread blocked in next().
            handle.close()
        self._done.wait(_CLOSE_TEARDOWN_TIMEOUT)

    def _start(self, handle: "_StreamHandle", first: object, responses: Iterator) -> None:
        self._stream_handle = handle
        thread = threading.Thread(target=self._receive, args=(handle, first, responses), daemon=True)
        thread.start()

    def _receive(self, handle: "_StreamHandle", first: object, responses: Iterator) -> None:
        try:
            self._consume(handle, first, responses)
        except Exception as e:  # noqa: BLE001 - surfaced to the caller by wait() and the output streams
            if not self._closed:
                self._error = e
        finally:
            self.stdout._finish()
            self.stderr._finish()
            self.stdin._abandon()
            self._done.set()

    def _consume(self, handle: "_StreamHandle", first: object, responses: Iterator) -> None:
        """Route events until the end event, re-attaching from the last sequence
        number when the stream drops with ``UNAVAILABLE``. Stops quietly once the
        handle is closed."""
        events: Iterator = itertools.chain([first], responses)
        last_sequence_number = 0
        reconnects = 0
        while True:
            made_progress = False
            try:
                for response in events:
                    made_progress = True
                    last_sequence_number = response.sequence_number
                    if self._handle_event(response.process_event):
                        return
                raise RuntimeError(f"output stream of command {self._command_id} ended before the command exited")
            except Exception as e:  # noqa: BLE001 - resume on a dropped connection, otherwise surface it
                if self._closed:
                    return
                # A reconnect that fails again before any new output is a lasting failure.
                if not _is_unavailable(e) or not made_progress or reconnects >= _DEFAULT_MAX_ATTEMPTS:
                    raise
            finally:
                # Release the channel now; the end event leaves the stream unexhausted.
                handle.close()
            reconnects += 1
            handle = self._sandbox._open_attach_handle(self._name, self._command_id, last_sequence_number)
            with self._lock:
                if self._closed:
                    handle.close()
                    return
                self._stream_handle = handle
            events = iter(handle)

    def _handle_event(self, event: object) -> bool:
        """Route one process event; return whether it was the end event."""
        kind = event.WhichOneof("event")
        if kind == "start":
            self._pid = event.start.pid
        elif kind == "data":
            stream = event.data.WhichOneof("output")
            if stream == "stderr":
                self._stderr_sink._append(event.data.stderr)
            elif stream is not None:
                self._stdout_sink._append(getattr(event.data, stream))
        elif kind == "end":
            self._exit_code = event.end.exit_code
            return True
        return False

    def _raise_if_failed(self) -> None:
        if self._error is not None:
            raise self._error


class SandboxExt(SandboxAPI):
    __doc__ = SandboxAPI.__doc__

    def _stream_input(
        self,
        name: str,
        command_id: str,
        inputs: Iterable[bytes],
        *,
        close_stdin: bool = True,
    ) -> "_pb.StreamInputResponse":
        """Forward stdin ``inputs`` to a running command in sandbox ``name``.

        Internal: used by :class:`CommandStdin`. Sends a start message, one data
        message per chunk of ``inputs``, then (unless ``close_stdin`` is false) a
        close message that sends EOF to the process's stdin. Returns the server's
        acknowledgement once the input stream is fully sent.

        Not retried: forwarding input is stateful and side-effecting, so a
        transport failure is raised to the caller.
        """
        from databricks.sdk._sandbox_grpc import sandbox_service_pb2 as _pb  # noqa: FlagLocalImports - lazy; stubs ship only with the optional "sandbox" extra
        from databricks.sdk._sandbox_grpc import sandbox_service_pb2_grpc as _pb_grpc  # noqa: FlagLocalImports - lazy; stubs ship only with the optional "sandbox" extra

        def requests() -> Iterator["_pb.StreamInputRequest"]:
            yield _pb.StreamInputRequest(start=_pb.StreamInputStart(command_id=command_id))
            for chunk in inputs:
                yield _pb.StreamInputRequest(data=_pb.StreamInputData(data=chunk))
            if close_stdin:
                yield _pb.StreamInputRequest(close=_pb.StreamInputClose())

        channel = open_channel(self._api._cfg)
        try:
            stub = _pb_grpc.SandboxServiceStub(channel)
            metadata: _Metadata = ((_SANDBOX_NAME_METADATA, name),)
            return stub.StreamInput(requests(), metadata=metadata)
        finally:
            channel.close()

    def execute_command(
        self,
        name: str,
        cmd: str,
        *,
        args: Optional[list[str]] = None,
        envs: Optional[Dict[str, str]] = None,
        text: bool = True,
        stdout: StreamMode = StreamMode.PIPE,
        stderr: StreamMode = StreamMode.PIPE,
    ) -> CommandProcess:
        """Start ``cmd`` in sandbox ``name`` and return a :class:`CommandProcess`
        handle for its output, input, and exit code.

        Returns once the command has started. ``cmd`` runs directly, not in a
        shell. With ``text=True`` (the default) output is decoded as UTF-8 into
        ``str``; pass ``text=False`` for ``bytes``. ``stdout`` and ``stderr``
        choose where each stream goes (see :class:`StreamMode`).

        The start is not retried, so the command never runs twice.
        """
        handle = self._open_execute_handle(name, cmd, args, envs)
        responses = iter(handle)
        first = next(responses, None)
        kind = first.process_event.WhichOneof("event") if first is not None else None
        if kind != "start":
            handle.close()
            raise RuntimeError(f"expected a start event for command {cmd!r}, got {kind!r}")
        start = first.process_event.start
        process = CommandProcess(self, name, start.command_id, text=text, stdout=stdout, stderr=stderr)
        process._pid = start.pid  # synchronous; _consume re-sets the same value from the start event
        process._start(handle, first, responses)
        return process

    def connect_command(
        self,
        name: str,
        command_id: str,
        *,
        text: bool = True,
        stdout: StreamMode = StreamMode.PIPE,
        stderr: StreamMode = StreamMode.PIPE,
    ) -> CommandProcess:
        """Return a :class:`CommandProcess` handle to a command already started in
        sandbox ``name``, such as one started by another client.

        ``command_id`` is :attr:`CommandProcess.command_id` of the original
        handle. The new handle replays the command's output from the beginning,
        then continues with live output. The server keeps a bounded amount of
        output per command, and keeps a finished command's output only briefly
        after it exits. ``text``, ``stdout``, and ``stderr`` work as in
        :meth:`execute_command`.
        """
        handle = self._open_attach_handle(name, command_id, 0)
        responses = iter(handle)
        first = next(responses, None)
        if first is None:
            handle.close()
            raise RuntimeError(f"no output stream for command {command_id!r}")
        process = CommandProcess(self, name, command_id, text=text, stdout=stdout, stderr=stderr)
        if first.process_event.WhichOneof("event") == "start":
            process._pid = first.process_event.start.pid  # synchronous when the replay starts at the start event
        process._start(handle, first, responses)
        return process

    def _open_stream_handle(
        self,
        name: str,
        make_stream: Callable[["_pb_grpc.SandboxServiceStub", _Metadata], Iterator],
        *,
        is_retryable: Optional[Callable[[Exception], bool]],
        max_attempts: int,
        retry_interval_seconds: float,
    ) -> _StreamHandle:
        """Open a per-call authenticated channel, run ``make_stream`` on the stub
        under :func:`open_stream_with_retry`, and return a :class:`_StreamHandle`
        wrapping the channel and response stream. The caller owns the handle and
        must ``close()`` it. Closes the channel if the open fails."""
        # Lazy import: grpcio and the generated stubs ship only with the optional
        # "sandbox" extra, so importing this module must not require them.
        from databricks.sdk._sandbox_grpc import sandbox_service_pb2_grpc as _pb_grpc  # noqa: FlagLocalImports - lazy; stubs ship only with the optional "sandbox" extra

        channel = open_channel(self._api._cfg)
        try:
            stub = _pb_grpc.SandboxServiceStub(channel)
            metadata: _Metadata = ((_SANDBOX_NAME_METADATA, name),)
            stream = open_stream_with_retry(
                lambda: make_stream(stub, metadata),
                is_retryable=is_retryable,
                max_attempts=max_attempts,
                retry_interval_seconds=retry_interval_seconds,
            )
        except BaseException:
            channel.close()
            raise
        return _StreamHandle(channel, stream)

    def _open_execute_handle(
        self,
        name: str,
        cmd: str,
        args: Optional[list[str]],
        envs: Optional[Dict[str, str]],
    ) -> _StreamHandle:
        """Open an ExecuteCommand stream for :meth:`execute_command`. The start is
        not retried, so the command never runs twice."""
        from databricks.sdk._sandbox_grpc import sandbox_service_pb2 as _pb  # noqa: FlagLocalImports - lazy; stubs ship only with the optional "sandbox" extra

        request = _pb.ExecuteCommandRequest(cmd=cmd, args=list(args or []), envs=dict(envs or {}))
        return self._open_stream_handle(
            name,
            lambda stub, metadata: stub.ExecuteCommand(request, metadata=metadata),
            is_retryable=_never_retry,
            max_attempts=_DEFAULT_MAX_ATTEMPTS,
            retry_interval_seconds=_DEFAULT_RETRY_INTERVAL_SECONDS,
        )

    def _open_attach_handle(self, name: str, command_id: str, last_sequence_number: int) -> _StreamHandle:
        """Open an AttachCommand stream for :meth:`connect_command` and for the
        reconnect path in :class:`CommandProcess`. Attach is a resumable replay,
        so the open retries on ``UNAVAILABLE``."""
        from databricks.sdk._sandbox_grpc import sandbox_service_pb2 as _pb  # noqa: FlagLocalImports - lazy; stubs ship only with the optional "sandbox" extra

        request = _pb.AttachCommandRequest(command_id=command_id, last_sequence_number=last_sequence_number)
        return self._open_stream_handle(
            name,
            lambda stub, metadata: stub.AttachCommand(request, metadata=metadata),
            is_retryable=None,
            max_attempts=_DEFAULT_MAX_ATTEMPTS,
            retry_interval_seconds=_DEFAULT_RETRY_INTERVAL_SECONDS,
        )
