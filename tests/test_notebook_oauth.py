"""Tests for runtime OAuth authentication in notebook environments."""

import os
import sys
import types
from datetime import datetime, timedelta
from typing import Dict

import pytest

from databricks.sdk import oauth
from databricks.sdk.config import Config
from databricks.sdk.credentials_provider import (CredentialsProvider,
                                                 CredentialsStrategy,
                                                 DefaultCredentials,
                                                 runtime_oauth)


@pytest.fixture
def mock_runtime_env(monkeypatch):
    """Set up mock Databricks runtime environment."""
    monkeypatch.setenv("DATABRICKS_RUNTIME_VERSION", "14.3")
    yield
    if "DATABRICKS_RUNTIME_VERSION" in os.environ:
        monkeypatch.delenv("DATABRICKS_RUNTIME_VERSION")


@pytest.fixture
def mock_runtime_native_auth():
    """Mock the runtime_native_auth to return a valid credentials provider."""
    fake_runtime = types.ModuleType("databricks.sdk.runtime")

    def fake_init_runtime_native_auth():
        def inner():
            return {"Authorization": "Bearer test-notebook-pat-token"}

        return "https://test.cloud.databricks.com", inner

    def fake_init_runtime_legacy_auth():
        pass

    def fake_init_runtime_repl_auth():
        pass

    fake_runtime.init_runtime_native_auth = fake_init_runtime_native_auth
    fake_runtime.init_runtime_legacy_auth = fake_init_runtime_legacy_auth
    fake_runtime.init_runtime_repl_auth = fake_init_runtime_repl_auth

    sys.modules["databricks.sdk.runtime"] = fake_runtime
    yield


@pytest.fixture
def mock_pat_exchange(mocker):
    """Mock the PATOAuthTokenExchange to avoid actual HTTP calls."""
    mock_token = oauth.Token(
        access_token="exchanged-oauth-token", token_type="Bearer", expiry=datetime.now() + timedelta(hours=1)
    )

    mock_exchange = mocker.Mock(spec=oauth.PATOAuthTokenExchange)
    mock_exchange.token.return_value = mock_token

    mocker.patch("databricks.sdk.oauth.PATOAuthTokenExchange", return_value=mock_exchange)
    return mock_exchange


class MockCredentialsStrategy(CredentialsStrategy):
    def auth_type(self) -> str:
        return "mock_credentials_strategy"

    def __call__(self, cfg) -> CredentialsProvider:
        def credentials_provider() -> Dict[str, str]:
            return {"Authorization": "Bearer: no_token"}

        return credentials_provider


@pytest.mark.parametrize(
    "scopes,auth_details",
    [
        ("sql offline_access", None),
        ("sql offline_access", '{"type": "databricks_resource"}'),
        ("sql", None),
        ("sql offline_access all-apis", None),
    ],
)
def test_runtime_oauth_success_scenarios(
    mock_runtime_env, mock_runtime_native_auth, mock_pat_exchange, scopes, auth_details
):
    """Test runtime-oauth works correctly in various valid configurations."""
    cfg = Config(
        host="https://test.cloud.databricks.com",
        scopes=scopes,
        authorization_details=auth_details,
        credentials_strategy=MockCredentialsStrategy(),
    )
    creds_provider = runtime_oauth(cfg)

    assert creds_provider is not None
    headers = creds_provider()
    assert headers["Authorization"] == "Bearer exchanged-oauth-token"


@pytest.mark.parametrize(
    "scopes",
    [
        (None),
        (""),
    ],
)
def test_runtime_oauth_missing_scopes(mock_runtime_env, mock_runtime_native_auth, scopes):
    """Test that runtime-oauth returns None when scopes are not provided."""
    cfg = Config(host="https://test.cloud.databricks.com", scopes=scopes)
    creds_provider = runtime_oauth(cfg)
    assert creds_provider is None


def test_runtime_oauth_priority_over_native_auth(mock_runtime_env, mock_runtime_native_auth, mock_pat_exchange):
    """Test that runtime-oauth is prioritized over runtime-native-auth."""
    cfg = Config(host="https://test.cloud.databricks.com", scopes="sql offline_access")

    default_creds = DefaultCredentials()
    creds_provider = default_creds(cfg)

    headers = creds_provider()
    assert headers["Authorization"] == "Bearer exchanged-oauth-token"
    assert default_creds.auth_type() == "runtime-oauth"


def test_fallback_to_native_auth_without_scopes(mock_runtime_env, mock_runtime_native_auth):
    """Test that runtime-native-auth is used when scopes are not provided."""
    cfg = Config(host="https://test.cloud.databricks.com")

    default_creds = DefaultCredentials()
    creds_provider = default_creds(cfg)

    headers = creds_provider()
    assert headers["Authorization"] == "Bearer test-notebook-pat-token"
    assert default_creds.auth_type() == "runtime"


def test_explicit_runtime_oauth_auth_type(mock_runtime_env, mock_runtime_native_auth, mock_pat_exchange):
    """Test that runtime-oauth is used when explicitly specified as auth_type."""
    cfg = Config(host="https://test.cloud.databricks.com", scopes="sql offline_access", auth_type="runtime-oauth")

    default_creds = DefaultCredentials()
    creds_provider = default_creds(cfg)

    headers = creds_provider()
    assert headers["Authorization"] == "Bearer exchanged-oauth-token"
    assert default_creds.auth_type() == "runtime-oauth"


@pytest.mark.parametrize(
    "has_scopes,expected_token",
    [
        (True, "exchanged-oauth-token"),
        (False, "test-notebook-pat-token"),
    ],
)
def test_config_authenticate_integration(
    mock_runtime_env, mock_runtime_native_auth, mock_pat_exchange, has_scopes, expected_token
):
    """Test Config.authenticate() integration with runtime-oauth and fallback."""
    cfg_kwargs = {"host": "https://test.cloud.databricks.com"}
    if has_scopes:
        cfg_kwargs["scopes"] = "sql offline_access"

    cfg = Config(**cfg_kwargs)
    headers = cfg.authenticate()

    assert headers["Authorization"] == f"Bearer {expected_token}"


@pytest.mark.parametrize(
    "scopes_input,expected_scopes",
    [(["sql", "offline_access"], "sql offline_access")],
)
def test_workspace_client_integration(
    mock_runtime_env, mock_runtime_native_auth, mock_pat_exchange, scopes_input, expected_scopes
):
    """Test that WorkspaceClient correctly uses runtime-oauth with different scope inputs."""
    from databricks.sdk import WorkspaceClient

    w = WorkspaceClient(host="https://test.cloud.databricks.com", scopes=scopes_input)

    assert w.config.scopes == expected_scopes
    headers = w.config.authenticate()
    assert headers["Authorization"] == "Bearer exchanged-oauth-token"
