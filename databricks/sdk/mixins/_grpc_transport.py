"""Generic gRPC streaming transport for hand-written SDK mixins.

The databricks-sdk client is HTTP-only; its generated service clients speak
JSON over the shared ``ApiClient``. Some APIs are gRPC-streaming RPCs that the
SDK's codegen does not produce a client for, so a mixin for such an API needs a
gRPC channel instead of the HTTP transport.

This module provides that channel, built from the SDK ``Config`` so it carries
the same credentials as the rest of the SDK: auth headers come from
``Config.authenticate()`` on every RPC, like the HTTP client's ``session.auth``
hook, so whatever credential strategy the caller configured authenticates the
gRPC calls too. Any ``Config`` custom headers ride along as well, as they do on
the HTTP client's requests, and the channel advertises the SDK's User-Agent (the
same string the HTTP client sends) so gRPC traffic is attributable to the SDK.

It is deliberately generic: it knows nothing about any particular service's
protos, headers, or responses. Those live in the mixin that uses the channel.

``grpcio`` is imported lazily inside the functions that need it, so importing
this module never requires grpcio to be installed; grpcio ships only with the
optional ``sandbox`` extra.
"""

from __future__ import annotations

import logging
import time
import urllib.parse
from typing import TYPE_CHECKING, Callable, Dict, Iterator, List, Optional, Tuple, TypeVar

if TYPE_CHECKING:
    import grpc

    from databricks.sdk.config import Config

_LOG = logging.getLogger("databricks.sdk")

# 443 is the default HTTPS port, reused here as the default gRPC port (overridable via `port`).
_DEFAULT_GRPC_PORT = 443

# Retry defaults for transient gRPC failures - e.g. a backend still starting up
# refuses connections (UNAVAILABLE). 30 attempts x 3s bounds the wait at ~90s.
_DEFAULT_MAX_ATTEMPTS = 30
_DEFAULT_RETRY_INTERVAL_SECONDS = 3.0

_T = TypeVar("_T")

# Distinguishes "stream opened but yielded nothing" from a real first message.
_UNSET = object()


def _grpc_target(host: str, port: int = _DEFAULT_GRPC_PORT) -> str:
    """Turn an SDK host (e.g. ``https://foo.databricks.com``) into a
    ``host:port`` gRPC dial target. Keeps only host and port, dropping any path,
    query, or fragment; appends ``port`` when the host has none."""
    if "://" not in host:
        host = f"https://{host}"
    netloc = urllib.parse.urlparse(host).netloc
    if ":" not in netloc:
        netloc = f"{netloc}:{port}"
    return netloc


def _headers_to_metadata(headers: Dict[str, str]) -> List[Tuple[str, str]]:
    """Convert HTTP-style auth headers into gRPC metadata. gRPC requires
    lowercase metadata keys; values pass through unchanged."""
    return [(key.lower(), value) for key, value in headers.items()]


def _auth_metadata(cfg: "Config", callback: Callable[..., None]) -> None:
    """Resolve the SDK's auth headers plus any configured custom headers and pass
    them to gRPC's metadata ``callback``.

    Mirrors the HTTP client, which sends ``Config`` custom headers on every
    request and layers auth on top; the two are merged here with auth winning on
    a name collision. The merge is case-insensitive - gRPC metadata keys are
    lowercase, so each source is lowercased before merging and every name ends up
    at most once, with auth overriding a custom header of the same name whatever
    its original casing. gRPC expects failures reported through ``callback``, not
    raised, so a credential error is passed to the callback rather than raised.
    Module-level (not a closure) so it stays testable without grpcio.
    """
    try:
        auth_headers = cfg.authenticate()
    except Exception as e:  # noqa: BLE001 - report the failure via callback, not by raising
        callback((), e)
        return
    metadata: Dict[str, str] = {}
    metadata.update(_headers_to_metadata(cfg._custom_headers))
    metadata.update(_headers_to_metadata(auth_headers))
    callback(tuple(metadata.items()), None)


def _channel_options(cfg: "Config") -> List[Tuple[str, str]]:
    """gRPC channel options that carry the SDK's identity. Sets the channel
    User-Agent to ``Config.user_agent`` - the same string the HTTP client sends
    (``ApiClient`` is built with ``user_agent_base=cfg.user_agent``) - so gRPC
    traffic is attributable to databricks-sdk exactly like the REST calls. gRPC
    prepends it to its own agent token. Module-level so it stays testable
    without grpcio."""
    return [("grpc.primary_user_agent", cfg.user_agent)]


def open_channel(cfg: "Config", *, port: int = _DEFAULT_GRPC_PORT) -> "grpc.Channel":
    """Open a TLS gRPC channel to the workspace host, authenticated with the
    SDK's configured credentials.

    Experimental: an internal helper for hand-written mixins, not public SDK
    API. It may change or be removed without warning; do not call it directly.

    Auth headers are resolved from ``cfg.authenticate()`` on every RPC via a
    gRPC call-credentials plugin (:func:`_auth_metadata`), so the channel
    inherits whatever the SDK's credential strategy produces, refreshed per
    call. The channel also advertises the SDK's User-Agent, the same string the
    HTTP client sends (see :func:`_channel_options`). The caller owns the
    returned channel and must ``close()`` it.
    """
    import grpc  # noqa: FlagLocalImports - lazy; grpcio ships only with the optional "sandbox" extra

    # Config.skip_verify is intentionally not honored: the SDK's HTTP client does not act
    # on it either (it always verifies), so the gRPC transport keeps the same TLS behavior.
    channel_credentials = grpc.composite_channel_credentials(
        grpc.ssl_channel_credentials(),
        grpc.metadata_call_credentials(lambda context, callback: _auth_metadata(cfg, callback)),
    )
    return grpc.secure_channel(_grpc_target(cfg.host, port), channel_credentials, options=_channel_options(cfg))


def _is_unavailable(error: Exception) -> bool:
    """Default retry predicate: true only for gRPC ``UNAVAILABLE``, the code that
    usually means the request never reached the server. Retrying re-issues the
    call (at-least-once), so a caller needing other codes - or none - passes its
    own ``is_retryable``."""
    import grpc  # noqa: FlagLocalImports - lazy; grpcio ships only with the optional "sandbox" extra

    return isinstance(error, grpc.RpcError) and error.code() == grpc.StatusCode.UNAVAILABLE


def call_with_retry(
    make_call: Callable[[], _T],
    *,
    is_retryable: Optional[Callable[[Exception], bool]] = None,
    max_attempts: int = _DEFAULT_MAX_ATTEMPTS,
    retry_interval_seconds: float = _DEFAULT_RETRY_INTERVAL_SECONDS,
    sleep: Callable[[float], None] = time.sleep,
) -> _T:
    """Invoke a gRPC call, retrying it on transient failures.

    Experimental: an internal helper for hand-written mixins, not public SDK
    API. It may change or be removed without warning; do not call it directly.

    ``make_call`` performs the RPC and is re-invoked on each attempt.
    ``is_retryable`` decides which errors retry (default: :func:`_is_unavailable`);
    a non-retryable error propagates immediately, and once the attempt budget is
    exhausted a ``TimeoutError`` is raised. For a server-streaming RPC use
    :func:`open_stream_with_retry`.
    """
    if is_retryable is None:
        is_retryable = _is_unavailable

    last_error: Optional[Exception] = None
    for attempt in range(max_attempts):
        try:
            return make_call()
        except Exception as e:  # noqa: BLE001 - broad exception catch by design. Retry on retryable errors and raise non-retryable ones.
            if is_retryable(e):
                last_error = e
                _LOG.debug(
                    "gRPC call failed with a retryable error (attempt %d/%d); retrying in %ss",
                    attempt + 1,
                    max_attempts,
                    retry_interval_seconds,
                )
                sleep(retry_interval_seconds)
                continue
            raise
    waited = max_attempts * retry_interval_seconds
    raise TimeoutError(f"gRPC call still failing after {waited:.0f}s ({max_attempts} attempts)") from last_error


class _ReplayFirstStream:
    """Yields an already-read first item, then the rest of a server-streaming
    gRPC call. The first item was read early to check the stream opened (see
    :func:`open_stream_with_retry`); this hands it back before continuing.

    Attribute access delegates to the underlying stream, so a caller that
    abandons iteration can still call ``cancel()`` (or any other stream method)
    on the live RPC - which a plain chained iterator would hide.
    """

    def __init__(self, first: _T, stream: Iterator[_T]):
        self._first = first
        self._first_pending = True
        self._stream = stream

    def __iter__(self) -> "Iterator[_T]":
        return self

    def __next__(self) -> _T:
        if self._first_pending:
            self._first_pending = False
            return self._first
        return next(self._stream)

    def __getattr__(self, name: str):
        # Reached only for attributes this proxy does not define (e.g. cancel);
        # forward them to the underlying gRPC stream.
        return getattr(self._stream, name)


def _open_stream(
    make_stream: Callable[[], Iterator[_T]],
    *,
    is_retryable: Callable[[Exception], bool],
    max_attempts: int,
    retry_interval_seconds: float,
    sleep: Callable[[float], None],
) -> Iterator[_T]:
    """Open the stream and read its first item under :func:`call_with_retry`,
    returning a stream that replays that item at the front (or the raw stream
    when it is empty, so ``cancel()`` still works)."""

    def open_stream_and_read_first_item() -> Tuple[object, Iterator[_T]]:
        stream = make_stream()
        return next(stream, _UNSET), stream

    first, stream = call_with_retry(
        open_stream_and_read_first_item,
        is_retryable=is_retryable,
        max_attempts=max_attempts,
        retry_interval_seconds=retry_interval_seconds,
        sleep=sleep,
    )
    if first is _UNSET:
        return stream
    return _ReplayFirstStream(first, stream)


def _stream_reopening_on_failure(
    first_stream: Iterator[_T],
    make_stream: Callable[[], Iterator[_T]],
    *,
    is_retryable: Callable[[Exception], bool],
    max_attempts: int,
    retry_interval_seconds: float,
    sleep: Callable[[float], None],
) -> Iterator[_T]:
    """Yield from ``first_stream``, re-opening the whole call on a retryable
    mid-stream failure (up to ``max_attempts`` re-opens). Each re-open restarts
    from the first item, so the caller re-receives what it already got."""
    stream = first_stream
    reopens = 0
    while True:
        try:
            item = next(stream)
        except StopIteration:
            return
        except Exception as e:  # noqa: BLE001 - re-open on retryable errors, raise otherwise
            if not is_retryable(e) or reopens >= max_attempts:
                raise
            reopens += 1
            sleep(retry_interval_seconds)
            stream = _open_stream(
                make_stream,
                is_retryable=is_retryable,
                max_attempts=max_attempts,
                retry_interval_seconds=retry_interval_seconds,
                sleep=sleep,
            )
            continue
        yield item


def open_stream_with_retry(
    make_stream: Callable[[], Iterator[_T]],
    *,
    is_retryable: Optional[Callable[[Exception], bool]] = None,
    retry_mid_stream_failures: bool = False,
    max_attempts: int = _DEFAULT_MAX_ATTEMPTS,
    retry_interval_seconds: float = _DEFAULT_RETRY_INTERVAL_SECONDS,
    sleep: Callable[[float], None] = time.sleep,
) -> Iterator[_T]:
    """Open a server-streaming call and read its first item.

    Experimental: an internal helper for hand-written mixins, not public SDK
    API. It may change or be removed without warning; do not call it directly.

    A gRPC stub sends the request only when the first item is read, so a
    not-ready backend fails on that first read. This reads it inside
    :func:`call_with_retry` (default predicate :func:`_is_unavailable`) and
    replays it at the front, so the caller still receives the whole stream; the
    returned object delegates attribute access to the live stream, so
    ``cancel()`` still reaches the RPC.

    By default a failure once items are flowing is raised to the caller, since
    gRPC cannot resume a broken stream. With ``retry_mid_stream_failures``, a
    retryable mid-stream failure instead re-issues the whole call (up to
    ``max_attempts`` re-opens); the new call restarts from the first item, so the
    caller re-receives what it already got and the RPC runs again - use it only
    for an idempotent, replay-tolerant consumer, and note the returned iterator
    then does not expose ``cancel()``. ``is_retryable`` and ``sleep`` are
    forwarded to :func:`call_with_retry`.
    """
    if is_retryable is None:
        is_retryable = _is_unavailable

    stream = _open_stream(
        make_stream,
        is_retryable=is_retryable,
        max_attempts=max_attempts,
        retry_interval_seconds=retry_interval_seconds,
        sleep=sleep,
    )
    if not retry_mid_stream_failures:
        return stream
    return _stream_reopening_on_failure(
        stream,
        make_stream,
        is_retryable=is_retryable,
        max_attempts=max_attempts,
        retry_interval_seconds=retry_interval_seconds,
        sleep=sleep,
    )
