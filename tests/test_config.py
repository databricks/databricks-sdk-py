import os
import pathlib
import platform
import random
import string
from datetime import datetime

import pytest

from databricks.sdk import AccountClient, WorkspaceClient, oauth, useragent
from databricks.sdk.config import Config, ConfigType, HostType, with_product, with_user_agent_extra
from databricks.sdk.version import __version__

from .conftest import noop_credentials, set_az_path

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


def test_host_type_aws_account():
    """Test that host_type returns ACCOUNT_HOST for AWS accounts host."""
    config = Config(
        host="https://accounts.cloud.databricks.com",
        account_id="123e4567-e89b-12d3-a456-426614174000",
        credentials_strategy=noop_credentials,
    )
    assert config.host_type() == HostType.ACCOUNT_HOST


def test_host_type_aws_dod_account():
    """Test that host_type returns ACCOUNT_HOST for AWS DoD accounts host."""
    config = Config(
        host="https://accounts-dod.cloud.databricks.us",
        account_id="123e4567-e89b-12d3-a456-426614174000",
        credentials_strategy=noop_credentials,
    )
    assert config.host_type() == HostType.ACCOUNT_HOST


def test_host_type_aws_workspace():
    """Test that host_type returns WORKSPACE_HOST for AWS workspace host."""
    config = Config(
        host="https://my-workspace.cloud.databricks.us",
        account_id="123e4567-e89b-12d3-a456-426614174000",
        credentials_strategy=noop_credentials,
    )
    assert config.host_type() == HostType.WORKSPACE_HOST


def test_host_type_unified():
    """Test that host_type returns UNIFIED_HOST for unified host."""
    config = Config(
        host="https://unified.cloud.databricks.com",
        account_id="123e4567-e89b-12d3-a456-426614174000",
        experimental_is_unified_host=True,
        credentials_strategy=noop_credentials,
    )
    assert config.host_type() == HostType.UNIFIED_HOST


def test_is_account_client_raises_on_unified_host():
    """Test that is_account_client raises RuntimeError on unified host."""
    config = Config(
        host="https://unified.cloud.databricks.com",
        account_id="test-account",
        experimental_is_unified_host=True,
        credentials_strategy=noop_credentials,
    )
    with pytest.raises(RuntimeError) as exc_info:
        _ = config.is_account_client
    assert "is_account_client cannot be used with unified hosts" in str(exc_info.value)


def test_config_type_account():
    """Test that config_type returns ACCOUNT_CONFIG for account host."""
    config = Config(
        host="https://accounts.cloud.databricks.com",
        account_id="123e4567-e89b-12d3-a456-426614174000",
        credentials_strategy=noop_credentials,
    )
    assert config.config_type() == ConfigType.ACCOUNT_CONFIG


def test_config_type_workspace():
    """Test that config_type returns WORKSPACE_CONFIG for workspace host."""
    config = Config(
        host="https://my-workspace.cloud.databricks.us",
        credentials_strategy=noop_credentials,
    )
    assert config.config_type() == ConfigType.WORKSPACE_CONFIG


def test_config_type_unified_with_workspace_id():
    """Test that config_type returns WORKSPACE_CONFIG for unified host with workspace_id."""
    config = Config(
        host="https://unified.cloud.databricks.com",
        account_id="123e4567-e89b-12d3-a456-426614174000",
        workspace_id="12345",
        experimental_is_unified_host=True,
        credentials_strategy=noop_credentials,
    )
    assert config.config_type() == ConfigType.WORKSPACE_CONFIG


def test_config_type_unified_without_workspace_id():
    """Test that config_type returns ACCOUNT_CONFIG for unified host without workspace_id."""
    config = Config(
        host="https://unified.cloud.databricks.com",
        account_id="123e4567-e89b-12d3-a456-426614174000",
        experimental_is_unified_host=True,
        credentials_strategy=noop_credentials,
    )
    assert config.config_type() == ConfigType.ACCOUNT_CONFIG


def test_config_type_unified_invalid_without_account_id():
    """Test that config_type returns INVALID_CONFIG for unified host without account_id."""
    config = Config(
        host="https://unified.cloud.databricks.com",
        experimental_is_unified_host=True,
        credentials_strategy=noop_credentials,
    )
    assert config.config_type() == ConfigType.INVALID_CONFIG


def test_oidc_endpoints_unified(requests_mock):
    """Test OIDC endpoints for unified host."""
    mock = requests_mock.get(
        "https://unified.cloud.databricks.com/oidc/accounts/abc/.well-known/oauth-authorization-server",
        json={
            "authorization_endpoint": "https://unified.cloud.databricks.com/oidc/accounts/abc/v1/authorize",
            "token_endpoint": "https://unified.cloud.databricks.com/oidc/accounts/abc/v1/token",
        },
    )
    config = Config(
        host="https://unified.cloud.databricks.com",
        account_id="abc",
        experimental_is_unified_host=True,
        credentials_strategy=noop_credentials,
    )
    endpoints = config.oidc_endpoints
    assert endpoints is not None
    assert endpoints.authorization_endpoint == "https://unified.cloud.databricks.com/oidc/accounts/abc/v1/authorize"
    assert endpoints.token_endpoint == "https://unified.cloud.databricks.com/oidc/accounts/abc/v1/token"
    assert mock.called_once


def test_authenticate_adds_org_id_header_for_unified_workspace():
    """Test that authenticate() adds X-Databricks-Org-Id header for unified workspace config."""
    config = Config(
        host="https://unified.cloud.databricks.com",
        account_id="123e4567-e89b-12d3-a456-426614174000",
        workspace_id="12345",
        experimental_is_unified_host=True,
        credentials_strategy=noop_credentials,
    )
    headers = config.authenticate()
    assert "X-Databricks-Org-Id" in headers
    assert headers["X-Databricks-Org-Id"] == "12345"


def test_authenticate_no_org_id_header_for_unified_account():
    """Test that authenticate() does not add X-Databricks-Org-Id header for unified account config."""
    config = Config(
        host="https://unified.cloud.databricks.com",
        account_id="123e4567-e89b-12d3-a456-426614174000",
        experimental_is_unified_host=True,
        credentials_strategy=noop_credentials,
    )
    headers = config.authenticate()
    assert "X-Databricks-Org-Id" not in headers


def test_authenticate_no_org_id_header_for_workspace_host():
    """Test that authenticate() does not add X-Databricks-Org-Id header for non-unified workspace host."""
    config = Config(
        host="https://my-workspace.cloud.databricks.us",
        credentials_strategy=noop_credentials,
    )
    headers = config.authenticate()
    assert "X-Databricks-Org-Id" not in headers


def test_workspace_client_rejects_account_host():
    """Test that WorkspaceClient raises ValueError for account host."""
    with pytest.raises(ValueError) as exc_info:
        WorkspaceClient(
            host="https://accounts.cloud.databricks.com",
            account_id="123e4567-e89b-12d3-a456-426614174000",
            credentials_strategy=noop_credentials,
        )
    assert "invalid Databricks Workspace configuration - host is not a workspace host" in str(exc_info.value)


def test_workspace_client_rejects_unified_host_without_workspace_id():
    """Test that WorkspaceClient raises ValueError for unified host without workspace_id."""
    with pytest.raises(ValueError) as exc_info:
        WorkspaceClient(
            host="https://unified.cloud.databricks.com",
            account_id="123e4567-e89b-12d3-a456-426614174000",
            experimental_is_unified_host=True,
            credentials_strategy=noop_credentials,
        )
    assert "workspace_id must be set when using WorkspaceClient with unified host" in str(exc_info.value)


def test_workspace_client_accepts_unified_host_with_workspace_id():
    """Test that WorkspaceClient accepts unified host with workspace_id."""
    client = WorkspaceClient(
        host="https://unified.cloud.databricks.com",
        account_id="123e4567-e89b-12d3-a456-426614174000",
        workspace_id="12345",
        experimental_is_unified_host=True,
        credentials_strategy=noop_credentials,
    )
    assert client is not None
    assert client.config.workspace_id == "12345"


def test_workspace_client_accepts_workspace_host():
    """Test that WorkspaceClient accepts workspace host."""
    client = WorkspaceClient(
        host="https://my-workspace.cloud.databricks.us",
        credentials_strategy=noop_credentials,
    )
    assert client is not None


def test_account_client_rejects_workspace_host():
    """Test that AccountClient raises ValueError for workspace host."""
    with pytest.raises(ValueError) as exc_info:
        AccountClient(
            host="https://my-workspace.cloud.databricks.us",
            account_id="123e4567-e89b-12d3-a456-426614174000",
            credentials_strategy=noop_credentials,
        )
    assert "invalid Databricks Account configuration - host incorrect or account_id missing" in str(exc_info.value)


def test_account_client_rejects_missing_account_id():
    """Test that AccountClient raises ValueError when account_id is missing."""
    with pytest.raises(ValueError) as exc_info:
        AccountClient(
            host="https://accounts.cloud.databricks.com",
            credentials_strategy=noop_credentials,
        )
    assert "invalid Databricks Account configuration - host incorrect or account_id missing" in str(exc_info.value)


def test_account_client_rejects_workspace_id():
    """Test that AccountClient raises ValueError when workspace_id is set."""
    with pytest.raises(ValueError) as exc_info:
        AccountClient(
            host="https://accounts.cloud.databricks.com",
            account_id="123e4567-e89b-12d3-a456-426614174000",
            workspace_id="12345",
            credentials_strategy=noop_credentials,
        )
    assert "workspace_id must not be set when using AccountClient" in str(exc_info.value)


def test_account_client_accepts_account_host():
    """Test that AccountClient accepts account host."""
    client = AccountClient(
        host="https://accounts.cloud.databricks.com",
        account_id="123e4567-e89b-12d3-a456-426614174000",
        credentials_strategy=noop_credentials,
    )
    assert client is not None
    assert client.config.account_id == "123e4567-e89b-12d3-a456-426614174000"


def test_account_client_accepts_unified_host():
    """Test that AccountClient accepts unified host without workspace_id."""
    client = AccountClient(
        host="https://unified.cloud.databricks.com",
        account_id="123e4567-e89b-12d3-a456-426614174000",
        experimental_is_unified_host=True,
        credentials_strategy=noop_credentials,
    )
    assert client is not None
    assert client.config.account_id == "123e4567-e89b-12d3-a456-426614174000"
