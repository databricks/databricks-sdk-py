"""Sandbox mixin.

Extends the generated :class:`~databricks.sdk.service.sandbox.SandboxAPI` with
``execute_command`` and ``connect_command``, which return a
:class:`CommandProcess` handle exposing a command's stdout, stderr, stdin, and
exit code as an ergonomic, file-like interface - without the caller handling the
raw gRPC process-event stream.

``forward`` returns a :class:`Forward` that relays a local TCP listener
to an app in the sandbox through the workspace's sandbox proxy. It uses only
the standard library, so it works without the optional ``sandbox`` extra.

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
import socket
import socketserver
import ssl
import sys
import threading
import time
from enum import Enum
from typing import (
    TYPE_CHECKING,
    Callable,
    Dict,
    FrozenSet,
    Iterable,
    Iterator,
    List,
    NamedTuple,
    Optional,
    Set,
    Tuple,
    Union,
)
from urllib.parse import quote, unquote_to_bytes, urlsplit

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


# Bounds a malformed or hostile request head; real heads are a few KiB.
_MAX_HEAD_BYTES = 64 * 1024
_CHUNK_BYTES = 64 * 1024
# A client that never finishes its request head would otherwise hold a relay thread forever.
_HEAD_TIMEOUT_SECONDS = 60.0
# close() cannot interrupt a connect or TLS handshake, because the socket is tracked only once it is connected.
_CONNECT_TIMEOUT_SECONDS = 30.0
# Body length marker for a request sent with Transfer-Encoding: chunked.
_CHUNKED = -1
_HOP_BY_HOP_HEADERS = frozenset(
    {
        "connection",
        "keep-alive",
        "proxy-authenticate",
        "proxy-connection",
        "te",
        "trailer",
        "upgrade",
    }
)
# RFC 9110 token characters. Methods and header names must consist of them, so whitespace or a
# line break cannot hide a header from the relay's checks.
_TOKEN_CHARS = frozenset("!#$%&'*+-.^_`|~0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
# Naming these in Connection would drop them from the forwarded head while the relay still frames the body by them.
_FRAMING_HEADERS = frozenset({"content-length", "transfer-encoding"})
# Workspace gateways read identity and routing from these, so only the SDK's credentials may set them.
_GATEWAY_HEADER_PREFIXES = ("x-databricks-", "s2s-")


class Forward:
    """An active forward from ``127.0.0.1`` to an app in a sandbox, returned
    by :meth:`SandboxExt.forward`.

    Forwarding runs on background threads until :meth:`close`, which also closes
    connections still open. Usable as a context manager.
    """

    def __init__(
        self,
        *,
        host: str,
        authenticate: Callable[[], Dict[str, str]],
        name: str,
        remote_port: int,
        local_port: int = 0,
    ) -> None:
        # The name becomes a path segment of every request, so it must not be able to add segments.
        sandbox_id = name.removeprefix("sandboxes/")
        if sandbox_id in ("", ".", "..") or quote(sandbox_id, safe="") != sandbox_id:
            raise ValueError(f"not a sandbox name: {name!r}; expected sandboxes/{{sandbox_id}}")
        workspace = urlsplit(host if "://" in host else f"https://{host}")
        self._server = _RelayServer(
            ("127.0.0.1", local_port),
            _Target(
                scheme=workspace.scheme,
                netloc=workspace.netloc,
                hostname=workspace.hostname or "",
                port=workspace.port or (443 if workspace.scheme == "https" else 80),
                path_prefix=f"{workspace.path.rstrip('/')}/sandbox-proxy/sandboxes/{sandbox_id}/ports/{remote_port}",
                authenticate=authenticate,
            ),
        )
        self._thread = threading.Thread(
            target=self._server.serve_forever,
            name=f"forward-{remote_port}",
            daemon=True,
        )
        self._thread.start()

    @property
    def local_port(self) -> int:
        """The port bound on ``127.0.0.1``."""
        return self._server.server_address[1]

    @property
    def url(self) -> str:
        """The local URL of the forwarded app, ``http://127.0.0.1:<local_port>``."""
        return f"http://127.0.0.1:{self.local_port}"

    def close(self) -> None:
        """Stop forwarding and close open connections."""
        self._server.shutdown()
        self._server.server_close()
        self._server.close_connections()
        self._thread.join()

    def __enter__(self) -> "Forward":
        return self

    def __exit__(self, *args: object) -> None:
        self.close()


class _Target:
    def __init__(
        self,
        *,
        scheme: str,
        netloc: str,
        hostname: str,
        port: int,
        path_prefix: str,
        authenticate: Callable[[], Dict[str, str]],
    ) -> None:
        self.scheme = scheme
        self.netloc = netloc
        self.hostname = hostname
        self.port = port
        self.path_prefix = path_prefix
        # Resolved per connection so OAuth tokens refresh over a long-lived forward.
        self.authenticate = authenticate
        self.tls = ssl.create_default_context() if scheme == "https" else None

    def connect(self) -> socket.socket:
        connection = socket.create_connection((self.hostname, self.port), timeout=_CONNECT_TIMEOUT_SECONDS)
        try:
            if self.tls is not None:
                connection = self.tls.wrap_socket(connection, server_hostname=self.hostname)
        except BaseException:
            connection.close()
            raise
        # Responses and WebSocket sessions can stay quiet for long stretches.
        connection.settimeout(None)
        return connection


class _RelayServer(socketserver.ThreadingTCPServer):
    daemon_threads = True
    block_on_close = False
    # Lets a new forward bind the same local port while the last one's connections are in TIME_WAIT.
    # On Windows, SO_REUSEADDR would also let another socket take a port that is in use.
    allow_reuse_address = sys.platform != "win32"

    def __init__(self, address: Tuple[str, int], target: _Target) -> None:
        self.target = target
        self._connections: Set[socket.socket] = set()
        self._connections_lock = threading.Lock()
        self._closed = False
        super().__init__(address, _RelayHandler)

    def track(self, connection: socket.socket) -> None:
        with self._connections_lock:
            if not self._closed:
                self._connections.add(connection)
                return
        # Registered after close: a handler that was already running when the forward closed.
        _shutdown(connection)

    def untrack(self, connection: socket.socket) -> None:
        with self._connections_lock:
            self._connections.discard(connection)

    def close_connections(self) -> None:
        with self._connections_lock:
            self._closed = True
            connections = list(self._connections)
        for connection in connections:
            _shutdown(connection)


class _RelayHandler(socketserver.BaseRequestHandler):
    server: _RelayServer

    def handle(self) -> None:
        client: socket.socket = self.request
        self.server.track(client)
        try:
            self._relay(client)
        finally:
            self.server.untrack(client)

    def _relay(self, client: socket.socket) -> None:
        head, rest = _read_head(client)
        if head is None:
            return
        # Validated before authenticating, so a request the relay refuses never refreshes a token.
        request = _parse_request(head)
        if request is None:
            client.sendall(_error_response(400, "Bad Request", "malformed request, or an unsupported path"))
            return
        target = self.server.target
        try:
            auth_headers = target.authenticate()
        except Exception:  # noqa: BLE001 - reported to the client; raising here would only drop the connection
            client.sendall(_error_response(502, "Bad Gateway", "could not authenticate with the workspace"))
            return
        try:
            sandbox = target.connect()
        except OSError as error:
            client.sendall(_error_response(502, "Bad Gateway", str(error)))
            return
        self.server.track(sandbox)
        try:
            rewritten = _rewrite_head(request, target, auth_headers)
            if request.upgrade:
                sandbox.sendall(rewritten + rest)
                upstream = threading.Thread(target=_copy, args=(client, sandbox), daemon=True)
            else:
                sandbox.sendall(rewritten)
                upstream = threading.Thread(
                    target=_copy_request_body,
                    args=(client, sandbox, rest, _RequestBody(request.body_length)),
                    daemon=True,
                )
            upstream.start()
            _copy(sandbox, client)
            upstream.join()
        except OSError:
            # The peer went away; closing both sides below is all that is left to do.
            pass
        finally:
            self.server.untrack(sandbox)
            sandbox.close()


class _Request(NamedTuple):
    method: str
    # Origin form: the path and query.
    target: str
    version: str
    headers: List[Tuple[str, str]]
    connection_tokens: FrozenSet[str]
    upgrade: bool
    # A byte count, or _CHUNKED.
    body_length: int


def _read_head(client: socket.socket) -> Tuple[Optional[bytes], bytes]:
    """Reads up to the end of the request head. Returns the head and any bytes after it, or
    ``(None, b"")`` when the client stops, stalls, or sends a head over the limit."""
    buffer = b""
    client.settimeout(_HEAD_TIMEOUT_SECONDS)
    try:
        while (end := buffer.find(b"\r\n\r\n")) == -1:
            if len(buffer) > _MAX_HEAD_BYTES:
                return None, b""
            chunk = client.recv(_CHUNK_BYTES)
            if not chunk:
                return None, b""
            buffer += chunk
    except OSError:
        # Includes the timeout.
        return None, b""
    finally:
        client.settimeout(None)
    if end > _MAX_HEAD_BYTES:
        return None, b""
    return buffer[:end], buffer[end + 4 :]


def _parse_request(head: bytes) -> Optional[_Request]:
    """Parses a request head, or returns ``None`` for one the relay must not forward.

    That is a malformed head, or a path that :func:`_is_ambiguous_path` rejects: the workspace
    could resolve it out of the port prefix, onto another API with the SDK's credentials
    attached. Lines must end in CRLF and hold no other CR, LF, or NUL, so no header reaches
    the workspace unseen by these checks.

    Also returns ``None`` when the body's length is ambiguous, such as both
    ``Content-Length`` and ``Transfer-Encoding``, because the relay forwards
    exactly one request per connection and must agree with the workspace on where
    it ends.
    """
    request_line, *header_lines = lines = head.decode("latin-1").split("\r\n")
    if any(character in line for line in lines for character in "\r\n\x00"):
        return None
    try:
        method, request_target, version = request_line.split(" ")
        if request_target.startswith(("http://", "https://")):
            absolute = urlsplit(request_target)
            request_target = absolute.path + (f"?{absolute.query}" if absolute.query else "")
    except ValueError:
        return None
    if not method or not _TOKEN_CHARS.issuperset(method) or version != "HTTP/1.1":
        return None
    if not request_target.startswith("/") or _is_ambiguous_path(request_target.split("?", 1)[0]):
        return None

    headers: List[Tuple[str, str]] = []
    for line in header_lines:
        name, separator, value = line.partition(":")
        if not separator or not name or not _TOKEN_CHARS.issuperset(name):
            return None
        headers.append((name, value.strip(" \t")))
    connection_tokens = frozenset(
        token.strip().lower() for name, value in headers if name.lower() == "connection" for token in value.split(",")
    )
    if not connection_tokens.isdisjoint(_FRAMING_HEADERS):
        return None
    upgrade = "upgrade" in connection_tokens and any(name.lower() == "upgrade" for name, _ in headers)
    body_length = _body_length(headers)
    if body_length is None:
        return None
    return _Request(method, request_target, version, headers, connection_tokens, upgrade, body_length)


def _rewrite_head(request: _Request, target: _Target, auth_headers: Dict[str, str]) -> bytes:
    """Points the request at the sandbox port and replaces the caller's credentials with ``auth_headers``.

    ``Connection: close`` makes the workspace end the connection after the response.
    """
    # Caller-supplied credentials and gateway headers are dropped, so a local header cannot override or add to the SDK's.
    replaced = {name.lower() for name in auth_headers} | {"authorization", "host", "proxy-authorization"}
    lines = [f"{request.method} {target.path_prefix}{request.target} {request.version}", f"Host: {target.netloc}"]
    lines.extend(f"{name}: {value}" for name, value in auth_headers.items())
    lines.append("Connection: upgrade" if request.upgrade else "Connection: close")
    for name, value in request.headers:
        lowered = name.lower()
        if request.upgrade and lowered == "upgrade":
            lines.append(f"{name}: {value}")
        elif not (
            lowered in _HOP_BY_HOP_HEADERS
            or lowered in request.connection_tokens
            or lowered in replaced
            or lowered.startswith(_GATEWAY_HEADER_PREFIXES)
        ):
            lines.append(f"{name}: {value}")
    return ("\r\n".join(lines) + "\r\n\r\n").encode("latin-1")


def _body_length(headers: List[Tuple[str, str]]) -> Optional[int]:
    """The request body's length, ``_CHUNKED``, or ``None`` for framing the relay and the
    workspace could read differently."""
    lengths = {value for name, value in headers if name.lower() == "content-length"}
    codings = [value for name, value in headers if name.lower() == "transfer-encoding"]
    if codings:
        if lengths or [coding.strip().lower() for coding in ",".join(codings).split(",")] != ["chunked"]:
            return None
        return _CHUNKED
    if not lengths:
        return 0
    if len(lengths) > 1:
        return None
    (length,) = lengths
    return int(length) if length.isascii() and length.isdigit() else None


class _RequestBody:
    """Finds where one request body ends in the bytes a client sends.

    Raises ``ValueError`` for malformed chunked framing.
    """

    def __init__(self, length: int) -> None:
        self._chunked = length == _CHUNKED
        self._remaining = 0 if self._chunked else length
        self._state = "size" if self._chunked else "data"
        self._line = b""
        self.complete = length == 0

    def take(self, data: bytes) -> bytes:
        """Returns the part of ``data`` that belongs to the body, and sets ``complete`` at its end."""
        taken = 0
        while taken < len(data) and not self.complete:
            if self._state == "data":
                step = min(self._remaining, len(data) - taken)
                taken += step
                self._remaining -= step
                if self._remaining == 0:
                    if self._chunked:
                        self._state = "data-end"
                    else:
                        self.complete = True
                continue
            # The other states read one CRLF-terminated line: a chunk size, the CRLF after chunk data, or a trailer.
            newline = data.find(b"\n", taken)
            stop = len(data) if newline == -1 else newline + 1
            self._line += data[taken:stop]
            taken = stop
            if len(self._line) > _MAX_HEAD_BYTES:
                raise ValueError("chunked framing line too long")
            if newline == -1:
                continue
            line, self._line = self._line, b""
            if not line.endswith(b"\r\n"):
                raise ValueError("chunked framing line without CRLF")
            self._read_line(line[:-2])
        return data[:taken]

    def _read_line(self, line: bytes) -> None:
        if self._state == "data-end":
            if line:
                raise ValueError("chunk longer than its size")
            self._state = "size"
        elif self._state == "size":
            size = line.split(b";", 1)[0].strip()
            if not size or len(size) > 16 or size.strip(b"0123456789abcdefABCDEF"):
                raise ValueError("invalid chunk size")
            self._remaining = int(size, 16)
            self._state = "data" if self._remaining else "trailer"
        elif not line:
            # The empty line after the trailers ends the body.
            self.complete = True


# Bytes a path segment must not contain once percent-decoded: path parameters, separators,
# query and fragment delimiters, escapes that survive the decode (double-encoded or
# malformed), and control characters.
_AMBIGUOUS_PATH_BYTES = frozenset(b";/\\%?#" + bytes(range(0x20)) + b"\x7f")


def _is_ambiguous_path(path: str) -> bool:
    """Whether a server could resolve a segment of ``path`` as ``.`` or ``..``.

    Proxies on the way to the workspace canonicalize paths before routing, and not only by
    RFC 3986: some treat a dot segment followed by path parameters as a dot segment. Rather
    than track those spellings, only segments that decode once to plain text other than
    ``.`` and ``..`` are accepted.
    """
    for segment in path.split("/"):
        decoded = unquote_to_bytes(segment)
        if decoded in (b".", b"..") or not _AMBIGUOUS_PATH_BYTES.isdisjoint(decoded):
            return True
    return False


def _copy(source: socket.socket, destination: socket.socket) -> None:
    """Copies until the source ends, then shuts both sockets down, which also stops the copy in
    the other direction."""
    try:
        while chunk := source.recv(_CHUNK_BYTES):
            destination.sendall(chunk)
    except OSError:
        # A socket error ends the relay like an EOF.
        pass
    _shutdown(source)
    _shutdown(destination)


def _copy_request_body(client: socket.socket, sandbox: socket.socket, rest: bytes, body: _RequestBody) -> None:
    """Forwards the request body and nothing after it: later bytes, such as a pipelined second
    request, would reach the workspace without a rewritten head. Stops reading once the body is
    complete, so a client that half-closes still gets the response. A client that stops sending
    before the body is complete aborts the exchange, so the workspace does not wait for the rest."""
    data = rest
    try:
        while True:
            if data:
                sandbox.sendall(body.take(data))
            if body.complete:
                return
            data = client.recv(_CHUNK_BYTES)
            if not data:
                break
    except (OSError, ValueError):
        # Ends the exchange like an incomplete body.
        pass
    _shutdown(client)
    _shutdown(sandbox)


def _shutdown(connection: socket.socket) -> None:
    try:
        connection.shutdown(socket.SHUT_RDWR)
    except OSError:
        # Already closed or never connected.
        pass


def _error_response(status: int, reason: str, message: str) -> bytes:
    body = f"forward failed: {message}\n".encode()
    return (
        f"HTTP/1.1 {status} {reason}\r\n"
        "Content-Type: text/plain; charset=utf-8\r\n"
        f"Content-Length: {len(body)}\r\n"
        "Connection: close\r\n\r\n"
    ).encode("latin-1") + body


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

    def forward(self, name: str, remote_port: int, *, local_port: int = 0) -> Forward:
        """Forward ``127.0.0.1:<local_port>`` to an app listening on ``remote_port``
        in sandbox ``name``, and return a :class:`Forward` for the forward.

        The local listener is bound before this returns; forwarding runs on
        background threads until :meth:`Forward.close` or the end of a ``with``
        block. ``local_port=0`` picks a free port; read it from
        :attr:`Forward.local_port`.

        ``name`` is the sandbox's resource name, ``sandboxes/{sandbox_id}``; a bare
        ``{sandbox_id}`` is also accepted. :attr:`Forward.url` is the local URL
        to send requests to.

        The app must listen on ``0.0.0.0`` inside the sandbox. Ports 10000-65535
        are forwardable except 10101, 18767, and 19090. Clients speak HTTP/1.1 to
        the local port, including WebSocket upgrades; each local connection carries
        one request. Requests whose path has a ``.`` or ``..`` segment, a ``;``, a
        backslash, a control character, or an encoded ``/``, ``\\``, ``%``, ``?``,
        or ``#`` get a local 400 response and are never sent, as do malformed
        heads. The caller's ``Authorization``, ``X-Databricks-*``, and ``S2S-*``
        headers are not forwarded, and the SDK's credentials are added.
        """
        cfg = self._api._cfg
        if not cfg.host:
            raise ValueError("Cannot forward a port without a workspace host")
        return Forward(
            host=cfg.host,
            authenticate=cfg.authenticate,
            name=name,
            remote_port=remote_port,
            local_port=local_port,
        )

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
