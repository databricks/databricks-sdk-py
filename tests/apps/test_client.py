from __future__ import annotations

import pytest

from databricks.apps import (
    get_mcp_client,
    get_user_workspace_client,
    get_workspace_client,
)

# Tests assert on the kwargs passed to WorkspaceClient — not on its constructed Config
# object — to avoid triggering the SDK's eager host-metadata resolution during unit
# tests. Auth-type correctness is about what we pass, not what the SDK resolves.


class _FakeRequest:
    def __init__(self, headers):
        self.headers = headers


def _clear_auth_env(monkeypatch):
    for key in (
        "DATABRICKS_HOST",
        "DATABRICKS_CLIENT_ID",
        "DATABRICKS_CLIENT_SECRET",
        "DATABRICKS_TOKEN",
        "DATABRICKS_CONFIG_FILE",
        "DATABRICKS_CONFIG_PROFILE",
    ):
        monkeypatch.delenv(key, raising=False)


@pytest.fixture
def patch_workspace_client(mocker):
    return mocker.patch("databricks.apps._client.WorkspaceClient")


def test_get_workspace_client_uses_oauth_m2m(monkeypatch, patch_workspace_client):
    _clear_auth_env(monkeypatch)
    monkeypatch.setenv("DATABRICKS_HOST", "https://example.cloud.databricks.com")
    monkeypatch.setenv("DATABRICKS_CLIENT_ID", "client-id")
    monkeypatch.setenv("DATABRICKS_CLIENT_SECRET", "client-secret")

    get_workspace_client()

    patch_workspace_client.assert_called_once_with(
        host="https://example.cloud.databricks.com",
        client_id="client-id",
        client_secret="client-secret",
        auth_type="oauth-m2m",
    )


def test_get_workspace_client_raises_without_sp_env(monkeypatch):
    _clear_auth_env(monkeypatch)
    with pytest.raises(RuntimeError, match="DATABRICKS_CLIENT_ID"):
        get_workspace_client()


def test_get_user_workspace_client_from_request_header(monkeypatch, patch_workspace_client):
    _clear_auth_env(monkeypatch)
    monkeypatch.setenv("DATABRICKS_HOST", "https://example.cloud.databricks.com")

    request = _FakeRequest({"X-Forwarded-Access-Token": "user-token"})
    get_user_workspace_client(request)

    patch_workspace_client.assert_called_once_with(
        host="https://example.cloud.databricks.com",
        token="user-token",
        auth_type="pat",
    )


def test_get_user_workspace_client_with_dual_auth_present(monkeypatch, patch_workspace_client):
    """Regression: the historical bug was that SP env vars + a user token made
    WorkspaceClient raise 'more than one authorization method configured'.
    Pinning auth_type='pat' here is what keeps that from happening."""
    _clear_auth_env(monkeypatch)
    monkeypatch.setenv("DATABRICKS_HOST", "https://example.cloud.databricks.com")
    monkeypatch.setenv("DATABRICKS_CLIENT_ID", "client-id")
    monkeypatch.setenv("DATABRICKS_CLIENT_SECRET", "client-secret")

    get_user_workspace_client(token="user-token")

    _, kwargs = patch_workspace_client.call_args
    assert kwargs["auth_type"] == "pat"
    assert kwargs["token"] == "user-token"


def test_get_user_workspace_client_case_insensitive_header(monkeypatch, patch_workspace_client):
    _clear_auth_env(monkeypatch)
    monkeypatch.setenv("DATABRICKS_HOST", "https://example.cloud.databricks.com")

    request = _FakeRequest({"x-forwarded-access-token": "user-token"})
    get_user_workspace_client(request)

    _, kwargs = patch_workspace_client.call_args
    assert kwargs["token"] == "user-token"


def test_get_user_workspace_client_does_not_mutate_env(monkeypatch, patch_workspace_client):
    """Thread-safety contract: the helper must not pop DATABRICKS_CLIENT_ID / SECRET
    from os.environ. That is the historical workaround that breaks under concurrency."""
    import os

    _clear_auth_env(monkeypatch)
    monkeypatch.setenv("DATABRICKS_HOST", "https://example.cloud.databricks.com")
    monkeypatch.setenv("DATABRICKS_CLIENT_ID", "client-id")
    monkeypatch.setenv("DATABRICKS_CLIENT_SECRET", "client-secret")

    get_user_workspace_client(token="user-token")

    assert os.environ["DATABRICKS_CLIENT_ID"] == "client-id"
    assert os.environ["DATABRICKS_CLIENT_SECRET"] == "client-secret"


def test_get_user_workspace_client_without_token_raises(monkeypatch):
    _clear_auth_env(monkeypatch)
    monkeypatch.setenv("DATABRICKS_HOST", "https://example.cloud.databricks.com")

    request = _FakeRequest({})
    with pytest.raises(ValueError, match="user access token"):
        get_user_workspace_client(request)


def test_get_mcp_client_is_placeholder():
    with pytest.raises(NotImplementedError, match="SDK-02"):
        get_mcp_client()
