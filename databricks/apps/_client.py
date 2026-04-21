"""Client helpers for code running inside Databricks Apps.

Two client-construction helpers, each one correct by construction under concurrent requests:

- :func:`get_workspace_client`: returns a SP-authenticated :class:`WorkspaceClient` that acts
  as the app's service principal. Uses OAuth M2M via the ``DATABRICKS_CLIENT_ID`` /
  ``DATABRICKS_CLIENT_SECRET`` env vars injected by the Apps runtime.

- :func:`get_user_workspace_client`: returns an OBO (on-behalf-of) :class:`WorkspaceClient`
  built from the ``X-Forwarded-Access-Token`` header that the Apps proxy adds to every
  request. Uses PAT auth with an explicit token — *does not mutate process env vars*, so it
  is safe to call concurrently from multiple request handlers.

Both helpers explicitly set ``auth_type`` so the SDK's auth validator does not raise
``more than one authorization method configured`` when both SP env vars and user tokens
are available in the same process.

A third helper, :func:`get_mcp_client`, is exposed as a placeholder and currently raises
``NotImplementedError``. It will be wired up when MCP resource provisioning lands
(tracked separately as SDK-02).
"""

from __future__ import annotations

import os
from typing import Any, Mapping, Optional, Protocol

from databricks.sdk import WorkspaceClient

_OBO_HEADER = "X-Forwarded-Access-Token"


class _HasHeaders(Protocol):
    """Minimal structural type for a request object with a ``headers`` mapping.

    This covers Flask, FastAPI/Starlette, Django, and bare ``dict``-like objects without
    requiring an import from any specific web framework.
    """

    headers: Mapping[str, str]


def get_workspace_client(host: Optional[str] = None, **kwargs: Any) -> WorkspaceClient:
    """Return a WorkspaceClient authenticated as the app's service principal.

    Uses OAuth M2M with the SP credentials injected by the Apps container runtime
    (``DATABRICKS_CLIENT_ID`` + ``DATABRICKS_CLIENT_SECRET``). ``auth_type`` is pinned to
    ``"oauth-m2m"`` so the SDK does not also attempt to read ``DATABRICKS_TOKEN`` from
    the environment and raise a dual-auth validation error.

    Args:
        host: Override for ``DATABRICKS_HOST``. Defaults to the env var.
        **kwargs: Forwarded to :class:`WorkspaceClient`.

    Returns:
        A configured :class:`WorkspaceClient`.

    Raises:
        RuntimeError: If the required SP env vars are not set.
    """
    client_id = os.environ.get("DATABRICKS_CLIENT_ID", "")
    client_secret = os.environ.get("DATABRICKS_CLIENT_SECRET", "")
    if not client_id or not client_secret:
        raise RuntimeError(
            "get_workspace_client() requires DATABRICKS_CLIENT_ID and DATABRICKS_CLIENT_SECRET; "
            "are you running inside a Databricks App container?"
        )
    return WorkspaceClient(
        host=host or os.environ.get("DATABRICKS_HOST", ""),
        client_id=client_id,
        client_secret=client_secret,
        auth_type="oauth-m2m",
        **kwargs,
    )


def get_user_workspace_client(
    request: Optional[_HasHeaders] = None,
    *,
    token: Optional[str] = None,
    host: Optional[str] = None,
    **kwargs: Any,
) -> WorkspaceClient:
    """Return a WorkspaceClient authenticated as the end user (OBO).

    Reads the user's access token either from ``X-Forwarded-Access-Token`` on the passed
    request, or from the explicit ``token`` argument. ``auth_type`` is pinned to ``"pat"``
    so the SDK does not fall back to the SP env vars and raise a dual-auth validation
    error when both are present.

    This function is safe to call concurrently from multiple request handlers: it does
    not mutate process environment variables (the historical workaround pattern that is
    *not* thread-safe).

    Args:
        request: Any object with a ``headers`` mapping (Flask, FastAPI, Django, etc.).
            If provided, the access token is read from ``X-Forwarded-Access-Token``.
        token: Explicit user access token. Overrides the header if both are provided.
        host: Override for ``DATABRICKS_HOST``. Defaults to the env var.
        **kwargs: Forwarded to :class:`WorkspaceClient`.

    Returns:
        A configured :class:`WorkspaceClient`.

    Raises:
        ValueError: If no user token can be found from either the request or ``token``.
    """
    if token is None and request is not None:
        token = _extract_obo_token(request)

    if not token:
        raise ValueError(
            "get_user_workspace_client() could not find a user access token. Pass `request` "
            "(with an X-Forwarded-Access-Token header) or an explicit `token` argument."
        )

    return WorkspaceClient(
        host=host or os.environ.get("DATABRICKS_HOST", ""),
        token=token,
        auth_type="pat",
        **kwargs,
    )


def get_mcp_client(*args: Any, **kwargs: Any):  # pragma: no cover - placeholder
    """Placeholder for the Apps MCP client (tracked as SDK-02).

    The MCP client is provisioned from ``mcp_server`` resources declared in ``app.yaml``.
    Until the runtime wires that up, this helper raises ``NotImplementedError`` so callers
    get a clear signal instead of a silent import failure.
    """
    raise NotImplementedError(
        "databricks.apps.get_mcp_client is not yet implemented; tracked as SDK-02. "
        "See the EMEA Apps gaps doc for status."
    )


def _extract_obo_token(request: _HasHeaders) -> Optional[str]:
    headers = getattr(request, "headers", None)
    if headers is None:
        return None
    # Most header mappings are case-insensitive, but fall back to a manual scan for
    # the rare ones (e.g. bare dicts in test code) that are not.
    try:
        value = headers.get(_OBO_HEADER)
        if value:
            return value
    except AttributeError:
        pass
    for key, value in dict(headers).items():
        if key.lower() == _OBO_HEADER.lower():
            return value
    return None
