"""Sandbox command-execution mixin.

Extends the generated :class:`~databricks.sdk.service.sandbox.SandboxAPI` with
the streaming command RPCs that codegen does not produce a client for:
``execute_command_streaming``, ``attach_command`` (both gRPC server-streaming)
and ``stream_input`` (gRPC client-streaming). They run on the generic gRPC
transport in :mod:`databricks.sdk.mixins._grpc_transport`.

The wire types come from the committed stubs in
:mod:`databricks.sdk._sandbox_grpc` (generated from a slim copy of the sandbox
daemon proto; see that package for provenance). grpcio and those stubs are
imported lazily inside the methods, so this module imports without the optional
``sandbox`` extra installed.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Callable, Dict, Iterable, Iterator, Optional, Tuple

from databricks.sdk.mixins._grpc_transport import (
    _DEFAULT_MAX_ATTEMPTS,
    _DEFAULT_RETRY_INTERVAL_SECONDS,
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
    """Retry predicate for :meth:`SandboxExt.execute_command_streaming`: never
    retry. ExecuteCommand starts a process and is not idempotent (its
    ``command_id`` is a stream-resume token, not a dedup key), so re-issuing a
    failed open could run the command twice."""
    return False


class SandboxExt(SandboxAPI):
    __doc__ = SandboxAPI.__doc__

    def execute_command_streaming(
        self,
        name: str,
        cmd: str,
        *,
        args: Optional[list[str]] = None,
        envs: Optional[Dict[str, str]] = None,
        is_retryable: Optional[Callable[[Exception], bool]] = None,
        max_attempts: int = _DEFAULT_MAX_ATTEMPTS,
        retry_interval_seconds: float = _DEFAULT_RETRY_INTERVAL_SECONDS,
    ) -> Iterator["_pb.ExecuteCommandResponse"]:
        """Run ``cmd`` in sandbox ``name`` and stream its process events.

        Streaming counterpart of :meth:`SandboxAPI.execute_command_sync`: the same
        ``name`` (``sandboxes/{sandbox_id}``), ``cmd``, ``args``, and ``envs``,
        but the process output is streamed instead of returned in one response.
        Yields ``ExecuteCommandResponse`` messages, each carrying one
        ``ProcessEvent`` (a start event, then stdout/stderr data chunks, then an
        end event with the exit code) and a monotonic ``sequence_number``.

        Retries are off by default (``is_retryable`` defaults to
        :func:`_never_retry`) because ExecuteCommand is not idempotent: re-issuing
        a failed open could run the command twice. Pass an ``is_retryable``
        predicate - e.g. one matching ``UNAVAILABLE`` - to retry the stream open
        when the command is safe to run more than once, optionally tuning
        ``max_attempts`` and ``retry_interval_seconds``. Only the stream open is
        retried; a failure once events are flowing is always raised.
        """
        from databricks.sdk._sandbox_grpc import sandbox_service_pb2 as _pb  # noqa: FlagLocalImports - lazy; stubs ship only with the optional "sandbox" extra

        request = _pb.ExecuteCommandRequest(cmd=cmd, args=list(args or []), envs=dict(envs or {}))
        yield from self._server_stream(
            name,
            lambda stub, metadata: stub.ExecuteCommand(request, metadata=metadata),
            is_retryable=_never_retry if is_retryable is None else is_retryable,
            max_attempts=max_attempts,
            retry_interval_seconds=retry_interval_seconds,
        )

    def attach_command(
        self,
        name: str,
        command_id: str,
        *,
        last_sequence_number: Optional[int] = None,
        is_retryable: Optional[Callable[[Exception], bool]] = None,
        max_attempts: int = _DEFAULT_MAX_ATTEMPTS,
        retry_interval_seconds: float = _DEFAULT_RETRY_INTERVAL_SECONDS,
    ) -> Iterator["_pb.AttachCommandResponse"]:
        """Attach to a running command in sandbox ``name`` and stream its output.

        ``command_id`` comes from the ``StartEvent`` of a prior
        :meth:`execute_command_streaming`. The server replays buffered events with
        ``sequence_number`` greater than ``last_sequence_number`` (0 replays from
        the beginning; omitted tails live output only), then streams live events.

        Unlike :meth:`execute_command_streaming`, retries default to the
        transport's ``UNAVAILABLE`` policy: attach is a resumable replay, so
        re-opening from ``last_sequence_number`` is safe. Pass ``is_retryable`` to
        override.
        """
        from databricks.sdk._sandbox_grpc import sandbox_service_pb2 as _pb  # noqa: FlagLocalImports - lazy; stubs ship only with the optional "sandbox" extra

        request = _pb.AttachCommandRequest(command_id=command_id)
        if last_sequence_number is not None:
            request.last_sequence_number = last_sequence_number
        yield from self._server_stream(
            name,
            lambda stub, metadata: stub.AttachCommand(request, metadata=metadata),
            is_retryable=is_retryable,
            max_attempts=max_attempts,
            retry_interval_seconds=retry_interval_seconds,
        )

    def stream_input(
        self,
        name: str,
        command_id: str,
        inputs: Iterable[bytes],
        *,
        close_stdin: bool = True,
    ) -> "_pb.StreamInputResponse":
        """Forward stdin ``inputs`` to a running command in sandbox ``name``.

        ``command_id`` comes from the ``StartEvent`` of a prior
        :meth:`execute_command_streaming`. Sends a start message, one data message
        per chunk of ``inputs``, then (unless ``close_stdin`` is false) a close
        message that sends EOF to the process's stdin. Returns the server's
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

    def _server_stream(
        self,
        name: str,
        make_stream: Callable[["_pb_grpc.SandboxServiceStub", _Metadata], Iterator],
        *,
        is_retryable: Optional[Callable[[Exception], bool]],
        max_attempts: int,
        retry_interval_seconds: float,
    ) -> Iterator:
        """Open a per-call authenticated channel, run ``make_stream`` on the stub
        under :func:`open_stream_with_retry`, and yield its items, closing the
        channel once iteration ends or is abandoned."""
        # Lazy import: grpcio and the generated stubs ship only with the optional
        # "sandbox" extra, so importing this module must not require them.
        from databricks.sdk._sandbox_grpc import sandbox_service_pb2_grpc as _pb_grpc  # noqa: FlagLocalImports - lazy; stubs ship only with the optional "sandbox" extra

        channel = open_channel(self._api._cfg)
        try:
            stub = _pb_grpc.SandboxServiceStub(channel)
            metadata: _Metadata = ((_SANDBOX_NAME_METADATA, name),)
            yield from open_stream_with_retry(
                lambda: make_stream(stub, metadata),
                is_retryable=is_retryable,
                max_attempts=max_attempts,
                retry_interval_seconds=retry_interval_seconds,
            )
        finally:
            channel.close()
