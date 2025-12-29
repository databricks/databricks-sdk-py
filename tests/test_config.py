import os
import pathlib
import platform
import random
import string
from datetime import datetime

import pytest

from databricks.sdk import oauth, useragent
from databricks.sdk.config import (ClientType, Config, HostType, with_product,
                                   with_user_agent_extra)
from databricks.sdk.version import __version__

from .conftest import noop_credentials, set_az_path, set_home

__tests__ = os.path.dirname(__file__)


def test_config_supports_legacy_credentials_provider():
    c = Config(
        credentials_provider=noop_credentials,
        product="foo",
        product_version="1.2.3",
    )
    c2 = c.copy()
    assert c2._product_info == ("foo", "1.2.3")


@pytest.mark.parametrize(
    "host,expected",
    [
        ("https://abc.def.ghi", "https://abc.def.ghi"),
        ("https://abc.def.ghi/", "https://abc.def.ghi"),
        ("abc.def.ghi", "https://abc.def.ghi"),
        ("abc.def.ghi/", "https://abc.def.ghi"),
        ("https://abc.def.ghi:443", "https://abc.def.ghi"),
        ("abc.def.ghi:443", "https://abc.def.ghi"),
    ],
)
def test_config_host_url_format_check(mocker, host, expected):
    mocker.patch("databricks.sdk.config.Config.init_auth")
    assert Config(host=host).host == expected


def test_extra_and_upstream_user_agent(monkeypatch):

    class MockUname:

        @property
        def system(self):
            return "TestOS"

    # Clear all environment variables and cached CICD provider.
    for k in os.environ:
        monkeypatch.delenv(k, raising=False)
    useragent._cicd_provider = None

    monkeypatch.setattr(platform, "python_version", lambda: "3.0.0")
    monkeypatch.setattr(platform, "uname", MockUname)
    monkeypatch.setenv("DATABRICKS_SDK_UPSTREAM", "upstream-product")
    monkeypatch.setenv("DATABRICKS_SDK_UPSTREAM_VERSION", "0.0.1")
    monkeypatch.setenv("DATABRICKS_RUNTIME_VERSION", "13.1 anything/else")

    config = (
        Config(
            host="http://localhost",
            username="something",
            password="something",
            product="test",
            product_version="0.0.0",
        )
        .with_user_agent_extra("test-extra-1", "1")
        .with_user_agent_extra("test-extra-2", "2")
    )

    assert config.user_agent == (
        f"test/0.0.0 databricks-sdk-py/{__version__} python/3.0.0 os/testos auth/basic"
        " test-extra-1/1 test-extra-2/2 upstream/upstream-product upstream-version/0.0.1"
        " runtime/13.1-anything-else"
    )

    with_product("some-product", "0.32.1")
    config2 = Config(host="http://localhost", token="...")
    assert config2.user_agent.startswith("some-product/0.32.1")

    config3 = Config(
        host="http://localhost",
        token="...",
        product="abc",
        product_version="1.2.3",
    )
    assert not config3.user_agent.startswith("some-product/0.32.1")


def test_config_copy_deep_copies_user_agent_other_info(config):
    config_copy = config.copy()

    config.with_user_agent_extra("test", "test1")
    assert "test/test1" not in config_copy.user_agent
    assert "test/test1" in config.user_agent

    config_copy.with_user_agent_extra("test", "test2")
    assert "test/test2" in config_copy.user_agent
    assert "test/test2" not in config.user_agent

    original_extra = useragent.extra()
    with_user_agent_extra("blueprint", "0.4.6")
    assert "blueprint/0.4.6" in config.user_agent
    assert "blueprint/0.4.6" in config_copy.user_agent
    useragent._reset_extra(original_extra)


def test_config_deep_copy(monkeypatch, mocker, tmp_path):
    mocker.patch(
        "databricks.sdk.credentials_provider.CliTokenSource.refresh",
        return_value=oauth.Token(
            access_token="token",
            token_type="Bearer",
            expiry=datetime(2023, 5, 22, 0, 0, 0),
        ),
    )

    write_large_dummy_executable(tmp_path)
    monkeypatch.setenv("PATH", tmp_path.as_posix())

    config = Config(host="https://abc123.azuredatabricks.net", auth_type="databricks-cli")
    config_copy = config.deep_copy()
    assert config_copy.host == config.host


def write_large_dummy_executable(path: pathlib.Path):
    cli = path.joinpath("databricks")

    # Generate a long random string to inflate the file size.
    random_string = "".join(random.choice(string.ascii_letters) for i in range(1024 * 1024))
    cli.write_text(
        """#!/bin/sh
cat <<EOF
{
"access_token": "...",
"token_type": "Bearer",
"expiry": "2023-05-22T00:00:00.000000+00:00"
}
EOF
exit 0
"""
        + random_string
    )
    cli.chmod(0o755)
    assert cli.stat().st_size >= (1024 * 1024)
    return cli


def test_load_azure_tenant_id_404(requests_mock, monkeypatch):
    set_az_path(monkeypatch)
    mock = requests_mock.get("https://abc123.azuredatabricks.net/aad/auth", status_code=404)
    cfg = Config(host="https://abc123.azuredatabricks.net")
    assert cfg.azure_tenant_id is None
    assert mock.called_once


def test_load_azure_tenant_id_no_location_header(requests_mock, monkeypatch):
    set_az_path(monkeypatch)
    mock = requests_mock.get("https://abc123.azuredatabricks.net/aad/auth", status_code=302)
    cfg = Config(host="https://abc123.azuredatabricks.net")
    assert cfg.azure_tenant_id is None
    assert mock.called_once


def test_load_azure_tenant_id_unparsable_location_header(requests_mock, monkeypatch):
    set_az_path(monkeypatch)
    mock = requests_mock.get(
        "https://abc123.azuredatabricks.net/aad/auth",
        status_code=302,
        headers={"Location": "https://unexpected-location"},
    )
    cfg = Config(host="https://abc123.azuredatabricks.net")
    assert cfg.azure_tenant_id is None
    assert mock.called_once


def test_load_azure_tenant_id_happy_path(requests_mock, monkeypatch):
    set_az_path(monkeypatch)
    mock = requests_mock.get(
        "https://abc123.azuredatabricks.net/aad/auth",
        status_code=302,
        headers={"Location": "https://login.microsoftonline.com/tenant-id/oauth2/authorize"},
    )
    cfg = Config(host="https://abc123.azuredatabricks.net")
    assert cfg.azure_tenant_id == "tenant-id"
    assert mock.called_once


def test_oauth_token_with_pat_auth():
    """Test that oauth_token() raises an error for PAT authentication."""
    config = Config(host="https://test.databricks.com", token="dapi1234567890abcdef")

    with pytest.raises(ValueError) as exc_info:
        config.oauth_token()

    assert "OAuth tokens are not available for pat authentication" in str(exc_info.value)


def test_oauth_token_with_basic_auth():
    """Test that oauth_token() raises an error for basic authentication."""
    config = Config(host="https://test.databricks.com", username="testuser", password="testpass")

    with pytest.raises(ValueError) as exc_info:
        config.oauth_token()

    assert "OAuth tokens are not available for basic authentication" in str(exc_info.value)


def test_oauth_token_with_oauth_provider(mocker):
    """Test that oauth_token() works correctly for OAuth authentication."""
    from databricks.sdk.credentials_provider import OAuthCredentialsProvider
    from databricks.sdk.oauth import Token

    # Create a mock OAuth token
    mock_token = Token(access_token="mock_access_token", token_type="Bearer", refresh_token="mock_refresh_token")

    # Create a mock OAuth provider
    mock_oauth_provider = mocker.Mock(spec=OAuthCredentialsProvider)
    mock_oauth_provider.oauth_token.return_value = mock_token

    # Create config with noop credentials to avoid network calls
    config = Config(host="https://test.databricks.com", credentials_strategy=noop_credentials)

    # Replace the header factory with our mock
    config._header_factory = mock_oauth_provider

    # Test that oauth_token() works and returns the expected token
    token = config.oauth_token()
    assert token == mock_token
    mock_oauth_provider.oauth_token.assert_called_once()


def test_oauth_token_reuses_existing_provider(mocker):
    """Test that oauth_token() reuses the existing OAuthCredentialsProvider."""
    from databricks.sdk.credentials_provider import OAuthCredentialsProvider
    from databricks.sdk.oauth import Token

    # Create a mock OAuth token
    mock_token = Token(access_token="mock_access_token", token_type="Bearer", refresh_token="mock_refresh_token")

    # Create a mock OAuth provider
    mock_oauth_provider = mocker.Mock(spec=OAuthCredentialsProvider)
    mock_oauth_provider.oauth_token.return_value = mock_token

    # Create config with noop credentials to avoid network calls
    config = Config(host="https://test.databricks.com", credentials_strategy=noop_credentials)

    # Replace the header factory with our mock
    config._header_factory = mock_oauth_provider

    # Call oauth_token() multiple times to verify reuse
    token1 = config.oauth_token()
    token2 = config.oauth_token()

    # Both calls should work and use the same provider instance
    assert token1 == token2 == mock_token
    assert mock_oauth_provider.oauth_token.call_count == 2


def test_host_type_workspace():
    """Test that a regular workspace host is identified correctly."""
    config = Config(host="https://test.databricks.com", token="test-token")
    assert config.host_type == HostType.WORKSPACE


def test_host_type_accounts():
    """Test that an accounts host is identified correctly."""
    config = Config(host="https://accounts.cloud.databricks.com", account_id="test-account", token="test-token")
    assert config.host_type == HostType.ACCOUNTS


def test_host_type_accounts_dod():
    """Test that an accounts-dod host is identified correctly."""
    config = Config(host="https://accounts-dod.cloud.databricks.us", account_id="test-account", token="test-token")
    assert config.host_type == HostType.ACCOUNTS


def test_host_type_unified():
    """Test that a unified host is identified when experimental flag is set."""
    config = Config(
        host="https://unified.databricks.com",
        workspace_id="test-workspace",
        experimental_is_unified_host=True,
        token="test-token",
    )
    assert config.host_type == HostType.UNIFIED


def test_client_type_workspace():
    """Test that client type is workspace when workspace_id is set on unified host."""
    config = Config(
        host="https://unified.databricks.com",
        workspace_id="test-workspace",
        account_id="test-account",
        experimental_is_unified_host=True,
        token="test-token",
    )
    assert config.client_type == ClientType.WORKSPACE


def test_client_type_account():
    """Test that client type is account when account_id is set without workspace_id."""
    config = Config(
        host="https://unified.databricks.com",
        account_id="test-account",
        experimental_is_unified_host=True,
        token="test-token",
    )
    assert config.client_type == ClientType.ACCOUNT


def test_client_type_workspace_default():
    """Test that client type defaults to workspace."""
    config = Config(host="https://test.databricks.com", token="test-token")
    assert config.client_type == ClientType.WORKSPACE


def test_client_type_accounts_host():
    """Test that client type is account for accounts host."""
    config = Config(
        host="https://accounts.cloud.databricks.com",
        account_id="test-account",
        token="test-token",
    )
    assert config.client_type == ClientType.ACCOUNT


def test_client_type_unified_without_account_id():
    """Test that client type raises error for unified host without account_id."""
    config = Config(
        host="https://unified.databricks.com",
        experimental_is_unified_host=True,
        token="test-token",
    )
    with pytest.raises(ValueError, match="Unified host requires account_id"):
        _ = config.client_type


def test_is_account_client_backward_compatibility():
    """Test that is_account_client property still works for backward compatibility."""
    config_workspace = Config(host="https://test.databricks.com", token="test-token")
    assert not config_workspace.is_account_client

    config_account = Config(host="https://accounts.cloud.databricks.com", account_id="test-account", token="test-token")
    assert config_account.is_account_client


def test_is_account_client_raises_on_unified_host():
    """Test that is_account_client raises ValueError when used with unified hosts."""
    config = Config(
        host="https://unified.databricks.com",
        experimental_is_unified_host=True,
        workspace_id="test-workspace",
        token="test-token",
    )
    with pytest.raises(ValueError, match="is_account_client cannot be used with unified hosts"):
        _ = config.is_account_client


def test_oidc_endpoints_unified_workspace(mocker, requests_mock):
    """Test that oidc_endpoints returns unified endpoints for workspace on unified host."""
    requests_mock.get(
        "https://unified.databricks.com/oidc/accounts/test-account/.well-known/oauth-authorization-server",
        json={
            "authorization_endpoint": "https://unified.databricks.com/oidc/accounts/test-account/v1/authorize",
            "token_endpoint": "https://unified.databricks.com/oidc/accounts/test-account/v1/token",
        },
    )

    config = Config(
        host="https://unified.databricks.com",
        workspace_id="test-workspace",
        account_id="test-account",
        experimental_is_unified_host=True,
        token="test-token",
    )

    endpoints = config.oidc_endpoints
    assert endpoints is not None
    assert "accounts/test-account" in endpoints.authorization_endpoint
    assert "accounts/test-account" in endpoints.token_endpoint


def test_oidc_endpoints_unified_account(mocker, requests_mock):
    """Test that oidc_endpoints returns account endpoints for account on unified host."""
    requests_mock.get(
        "https://unified.databricks.com/oidc/accounts/test-account/.well-known/oauth-authorization-server",
        json={
            "authorization_endpoint": "https://unified.databricks.com/oidc/accounts/test-account/v1/authorize",
            "token_endpoint": "https://unified.databricks.com/oidc/accounts/test-account/v1/token",
        },
    )

    config = Config(
        host="https://unified.databricks.com",
        account_id="test-account",
        experimental_is_unified_host=True,
        token="test-token",
    )

    endpoints = config.oidc_endpoints
    assert endpoints is not None
    assert "accounts/test-account" in endpoints.authorization_endpoint
    assert "accounts/test-account" in endpoints.token_endpoint


def test_oidc_endpoints_unified_missing_ids():
    """Test that oidc_endpoints raises error when unified host lacks required account_id."""
    config = Config(host="https://unified.databricks.com", experimental_is_unified_host=True, token="test-token")

    with pytest.raises(ValueError) as exc_info:
        _ = config.oidc_endpoints

    assert "Unified host requires account_id" in str(exc_info.value)


def test_workspace_org_id_header_on_unified_host(requests_mock):
    """Test that X-Databricks-Org-Id header is added for workspace clients on unified hosts."""
    from databricks.sdk.core import ApiClient

    requests_mock.get("https://unified.databricks.com/api/2.0/test", json={"result": "success"})

    config = Config(
        host="https://unified.databricks.com",
        workspace_id="test-workspace-123",
        experimental_is_unified_host=True,
        token="test-token",
    )

    api_client = ApiClient(config)
    api_client.do("GET", "/api/2.0/test")

    # Verify the request was made with the X-Databricks-Org-Id header
    assert requests_mock.last_request.headers.get("X-Databricks-Org-Id") == "test-workspace-123"


def test_no_org_id_header_on_regular_workspace(requests_mock):
    """Test that X-Databricks-Org-Id header is NOT added for regular workspace hosts."""
    from databricks.sdk.core import ApiClient

    requests_mock.get("https://test.databricks.com/api/2.0/test", json={"result": "success"})

    config = Config(host="https://test.databricks.com", token="test-token")

    api_client = ApiClient(config)
    api_client.do("GET", "/api/2.0/test")

    # Verify the X-Databricks-Org-Id header was NOT added
    assert "X-Databricks-Org-Id" not in requests_mock.last_request.headers


def test_disable_oauth_refresh_token_from_env(monkeypatch, mocker):
    mocker.patch("databricks.sdk.config.Config.init_auth")
    monkeypatch.setenv("DATABRICKS_DISABLE_OAUTH_REFRESH_TOKEN", "true")
    config = Config(host="https://test.databricks.com")
    assert config.disable_oauth_refresh_token is True


def test_disable_oauth_refresh_token_defaults_to_false(mocker):
    mocker.patch("databricks.sdk.config.Config.init_auth")
    config = Config(host="https://test.databricks.com")
    assert config.disable_oauth_refresh_token is None  # ConfigAttribute returns None when not set


def test_config_file_scopes_empty_defaults_to_all_apis(monkeypatch, mocker):
    """Test that empty scopes in config file defaults to all-apis."""
    mocker.patch("databricks.sdk.config.Config.init_auth")
    set_home(monkeypatch, "/testdata")
    config = Config(profile="scope-empty")
    assert config.get_scopes() == ["all-apis"]


def test_config_file_scopes_single(monkeypatch, mocker):
    """Test single scope from config file."""
    mocker.patch("databricks.sdk.config.Config.init_auth")
    set_home(monkeypatch, "/testdata")
    config = Config(profile="scope-single")
    assert config.get_scopes() == ["clusters"]


def test_config_file_scopes_multiple_sorted(monkeypatch, mocker):
    """Test multiple scopes from config file are sorted."""
    mocker.patch("databricks.sdk.config.Config.init_auth")
    set_home(monkeypatch, "/testdata")
    config = Config(profile="scope-multiple")
    # Should be sorted alphabetically
    expected = ["clusters", "files:read", "iam:read", "jobs", "mlflow", "model-serving:read", "pipelines"]
    assert config.get_scopes() == expected
