import os
import pathlib
import platform
import random
import string
from datetime import datetime
from typing import Optional
from urllib.parse import parse_qs

import pytest

from databricks.sdk import AccountClient, WorkspaceClient, oauth, useragent
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


def test_client_type_unified_without_account_id(requests_mock):
    """Test that client type is workspace when unified host fetches workspace_id."""
    # Mock the SCIM endpoint to return workspace ID
    requests_mock.get(
        "https://unified.databricks.com/api/2.0/preview/scim/v2/Me",
        headers={"x-databricks-org-id": "123456"},
    )

    config = Config(
        host="https://unified.databricks.com",
        experimental_is_unified_host=True,
        token="test-token",
    )

    # Should return WORKSPACE since workspace_id is fetched from API
    assert config.client_type == ClientType.WORKSPACE
    assert config.workspace_id == "123456"


def test_is_account_client_backward_compatibility():
    """Test that is_account_client property still works for backward compatibility."""
    config_workspace = Config(host="https://test.databricks.com", token="test-token")
    assert not config_workspace.is_account_client

    config_account = Config(host="https://accounts.cloud.databricks.com", account_id="test-account", token="test-token")
    assert config_account.is_account_client


def test_is_account_client_on_unified_host():
    """Test that is_account_client returns truthiness of account_id for unified hosts."""
    config = Config(
        host="https://unified.databricks.com",
        experimental_is_unified_host=True,
        workspace_id="test-workspace",
        token="test-token",
    )
    # Should be falsy since account_id is not set
    assert not config.is_account_client

    # With account_id set, should be truthy
    config_with_account = Config(
        host="https://unified.databricks.com",
        experimental_is_unified_host=True,
        workspace_id="test-workspace",
        account_id="test-account",
        token="test-token",
    )
    assert config_with_account.is_account_client


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


def test_oidc_endpoints_unified_missing_ids(requests_mock):
    """Test that unified host without account_id falls back to workspace endpoints."""
    # Mock the SCIM endpoint for workspace ID fetch
    requests_mock.get(
        "https://unified.databricks.com/api/2.0/preview/scim/v2/Me",
        headers={"x-databricks-org-id": "123456"},
    )
    # Mock the workspace OIDC endpoint
    requests_mock.get(
        "https://unified.databricks.com/oidc/.well-known/oauth-authorization-server",
        json={
            "authorization_endpoint": "https://unified.databricks.com/oidc/v1/authorize",
            "token_endpoint": "https://unified.databricks.com/oidc/v1/token",
        },
    )

    config = Config(host="https://unified.databricks.com", experimental_is_unified_host=True, token="test-token")

    # Should fall back to workspace endpoints when account_id is missing
    endpoints = config.oidc_endpoints
    assert endpoints is not None
    assert "oidc/v1/authorize" in endpoints.authorization_endpoint


def test_workspace_org_id_header_on_unified_host(requests_mock):
    """Test that X-Databricks-Org-Id header is added for workspace clients on unified hosts."""

    requests_mock.get("https://unified.databricks.com/api/2.0/preview/scim/v2/Me", json={"result": "success"})

    config = Config(
        host="https://unified.databricks.com",
        account_id="test-account",
        workspace_id="test-workspace-123",
        experimental_is_unified_host=True,
        token="test-token",
    )

    workspace_client = WorkspaceClient(config=config)
    workspace_client.current_user.me()

    # Verify the request was made with the X-Databricks-Org-Id header
    assert requests_mock.last_request.headers.get("X-Databricks-Org-Id") == "test-workspace-123"


def test_not_workspace_org_id_header_on_unified_host_on_account_endpoint(requests_mock):
    """Test that X-Databricks-Org-Id header is added for workspace clients on unified hosts."""

    requests_mock.get(
        "https://unified.databricks.com/api/2.0/accounts/test-account/scim/v2/Groups/test-group-123",
        json={"result": "success"},
    )

    config = Config(
        host="https://unified.databricks.com",
        account_id="test-account",
        workspace_id="test-workspace-123",
        experimental_is_unified_host=True,
        token="test-token",
    )

    account_client = AccountClient(config=config)
    account_client.groups.get("test-group-123")

    # Verify the request was made without the X-Databricks-Org-Id header
    assert "X-Databricks-Org-Id" not in requests_mock.last_request.headers


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
    assert not config.disable_oauth_refresh_token


@pytest.mark.parametrize(
    "profile,expected_scopes",
    [
        ("scope-empty", ["all-apis"]),
        ("scope-single", ["clusters"]),
        ("scope-multiple", ["clusters", "files:read", "iam:read", "jobs", "mlflow", "model-serving:read", "pipelines"]),
    ],
    ids=["empty_defaults_to_all_apis", "single_scope", "multiple_sorted"],
)
def test_config_file_scopes(monkeypatch, mocker, profile, expected_scopes):
    """Test scopes from config file profiles."""
    mocker.patch("databricks.sdk.config.Config.init_auth")
    set_home(monkeypatch, "/testdata")
    config = Config(profile=profile)
    assert config.get_scopes() == expected_scopes


@pytest.mark.parametrize(
    "scopes_input,expected_scopes",
    [
        # List input
        (["jobs", "clusters", "mlflow"], ["clusters", "jobs", "mlflow"]),
        # Deduplication (list)
        (["clusters", "jobs", "clusters", "jobs", "mlflow"], ["clusters", "jobs", "mlflow"]),
        # Deduplication (string)
        ("clusters,jobs,clusters,jobs,mlflow", ["clusters", "jobs", "mlflow"]),
        # Space-separated (backwards compatibility)
        ("clusters jobs mlflow", ["clusters", "jobs", "mlflow"]),
        # Mixed separators
        ("clusters, jobs  mlflow,pipelines", ["clusters", "jobs", "mlflow", "pipelines"]),
        # Empty string defaults to all-apis
        ("", ["all-apis"]),
        # Whitespace-only defaults to all-apis
        ("   ", ["all-apis"]),
        # None defaults to all-apis
        (None, ["all-apis"]),
        # Empty list defaults to all-apis
        ([], ["all-apis"]),
        # Empty strings in list are filtered
        (["clusters", "", "jobs", ""], ["clusters", "jobs"]),
        # List with only empty strings defaults to all-apis
        (["", "", ""], ["all-apis"]),
    ],
    ids=[
        "list_input",
        "deduplication_list",
        "deduplication_string",
        "space_separated",
        "mixed_separators",
        "empty_string",
        "whitespace_only",
        "none",
        "empty_list",
        "list_with_empty_strings",
        "list_only_empty_strings",
    ],
)
def test_scopes_parsing(mocker, scopes_input, expected_scopes):
    """Test scopes parsing with various input formats."""
    mocker.patch("databricks.sdk.config.Config.init_auth")
    config = Config(host="https://test.databricks.com", scopes=scopes_input)
    assert config.get_scopes() == expected_scopes


def test_config_file_scopes_multiple_sorted(monkeypatch, mocker):
    """Test multiple scopes from config file are sorted."""
    mocker.patch("databricks.sdk.config.Config.init_auth")
    set_home(monkeypatch, "/testdata")
    config = Config(profile="scope-multiple")
    # Should be sorted alphabetically
    expected = ["clusters", "files:read", "iam:read", "jobs", "mlflow", "model-serving:read", "pipelines"]
    assert config.get_scopes() == expected


def _get_scope_from_request(request_text: str) -> Optional[str]:
    """Extract the scope value from a URL-encoded request body."""
    params = parse_qs(request_text)
    scope_list = params.get("scope")
    return scope_list[0] if scope_list else None


@pytest.mark.parametrize(
    "scopes_input,expected_scope",
    [
        (None, "all-apis"),
        (["unity-catalog:read"], "unity-catalog:read"),
        (["jobs:read", "clusters", "mlflow:read"], "clusters jobs:read mlflow:read"),
    ],
    ids=["default_scope", "single_custom_scope", "multiple_scopes_sorted"],
)
def test_m2m_scopes_sent_to_token_endpoint(requests_mock, scopes_input, expected_scope):
    """Test M2M authentication sends correct scopes to token endpoint."""
    requests_mock.get(
        "https://test.databricks.com/oidc/.well-known/oauth-authorization-server",
        json={
            "authorization_endpoint": "https://test.databricks.com/oidc/v1/authorize",
            "token_endpoint": "https://test.databricks.com/oidc/v1/token",
        },
    )
    token_mock = requests_mock.post(
        "https://test.databricks.com/oidc/v1/token",
        json={"access_token": "test-token", "token_type": "Bearer", "expires_in": 3600},
    )

    config = Config(
        host="https://test.databricks.com",
        client_id="test-client-id",
        client_secret="test-client-secret",
        auth_type="oauth-m2m",
        scopes=scopes_input,
    )
    config.authenticate()

    assert _get_scope_from_request(token_mock.last_request.text) == expected_scope


@pytest.mark.parametrize(
    "scopes_input,expected_scope",
    [
        (None, "all-apis"),
        (["unity-catalog:read", "clusters"], "clusters unity-catalog:read"),
        (["jobs:read"], "jobs:read"),
    ],
    ids=["default_scope", "multiple_scopes", "single_scope"],
)
def test_oidc_scopes_sent_to_token_endpoint(requests_mock, tmp_path, scopes_input, expected_scope):
    """Test OIDC token exchange sends correct scopes to token endpoint."""
    oidc_token_file = tmp_path / "oidc_token"
    oidc_token_file.write_text("mock-id-token")

    requests_mock.get(
        "https://test.databricks.com/oidc/.well-known/oauth-authorization-server",
        json={
            "authorization_endpoint": "https://test.databricks.com/oidc/v1/authorize",
            "token_endpoint": "https://test.databricks.com/oidc/v1/token",
        },
    )
    token_mock = requests_mock.post(
        "https://test.databricks.com/oidc/v1/token",
        json={"access_token": "test-token", "token_type": "Bearer", "expires_in": 3600},
    )

    config = Config(
        host="https://test.databricks.com",
        oidc_token_filepath=str(oidc_token_file),
        auth_type="file-oidc",
        scopes=scopes_input,
    )
    config.authenticate()

    assert _get_scope_from_request(token_mock.last_request.text) == expected_scope


def test_legacy_workspace_profile_resolves_environment_with_unified_flag(requests_mock):
    """Test that legacy workspace profile (no account_id) resolves environment and fetches workspace ID."""
    # Mock the SCIM endpoint to return workspace ID
    requests_mock.get(
        "https://test.cloud.databricks.com/api/2.0/preview/scim/v2/Me",
        headers={"x-databricks-org-id": "123456789"},
    )

    config = Config(
        host="https://test.cloud.databricks.com",
        experimental_is_unified_host=True,
        token="test-token",
    )

    # Environment should be resolved for AWS
    assert config.environment is not None
    assert config.environment.cloud.value == "AWS"
    assert config.environment.dns_zone == ".cloud.databricks.com"

    # Workspace ID should be fetched from API
    assert config.workspace_id == "123456789"


def test_legacy_azure_workspace_profile_resolves_environment_with_unified_flag(requests_mock):
    """Test that legacy Azure workspace profile resolves environment and fetches workspace ID."""
    # Mock the SCIM endpoint to return workspace ID
    requests_mock.get(
        "https://adb-123.4.azuredatabricks.net/api/2.0/preview/scim/v2/Me",
        headers={"x-databricks-org-id": "987654321"},
    )

    config = Config(
        host="https://adb-123.4.azuredatabricks.net",
        experimental_is_unified_host=True,
        token="test-token",
    )

    # Environment should be resolved for Azure
    assert config.environment is not None
    assert config.environment.cloud.value == "AZURE"
    assert config.environment.dns_zone == ".azuredatabricks.net"

    # Workspace ID should be fetched from API
    assert config.workspace_id == "987654321"


def test_legacy_gcp_workspace_profile_resolves_environment_with_unified_flag(requests_mock):
    """Test that legacy GCP workspace profile resolves environment and fetches workspace ID."""
    # Mock the SCIM endpoint to return workspace ID
    requests_mock.get(
        "https://test.gcp.databricks.com/api/2.0/preview/scim/v2/Me",
        headers={"x-databricks-org-id": "555666777"},
    )

    config = Config(
        host="https://test.gcp.databricks.com",
        experimental_is_unified_host=True,
        token="test-token",
    )

    # Environment should be resolved for GCP
    assert config.environment is not None
    assert config.environment.cloud.value == "GCP"
    assert config.environment.dns_zone == ".gcp.databricks.com"

    # Workspace ID should be fetched from API
    assert config.workspace_id == "555666777"


def test_legacy_account_profile_resolves_environment_with_unified_flag(mocker):
    """Test that legacy account profile (accounts host) resolves environment when unified flag is set."""
    mocker.patch("databricks.sdk.config.Config.init_auth")

    config = Config(
        host="https://accounts.cloud.databricks.com",
        account_id="test-account",
        experimental_is_unified_host=True,
        token="test-token",
    )

    # Environment should be resolved for AWS accounts host
    assert config.environment is not None
    assert config.environment.cloud.value == "AWS"


def test_unified_profile_with_account_id_has_none_environment(mocker):
    """Test that new unified profile with account_id has None environment (cloud-agnostic)."""
    mocker.patch("databricks.sdk.config.Config.init_auth")

    config = Config(
        host="https://unified.databricks.com",
        account_id="test-account",
        workspace_id="test-workspace",
        experimental_is_unified_host=True,
        token="test-token",
    )

    # Unified hosts with account_id should NOT have environment resolved (cloud-agnostic)
    assert config.environment is None
    # But the is_cloud properties should still work without crashing
    assert config.is_azure is False
    assert config.is_gcp is False
    assert config.is_aws is False


def test_azure_resource_id_sets_is_azure_even_without_environment(mocker):
    """Test that azure_workspace_resource_id sets is_azure even when environment is None."""
    mocker.patch("databricks.sdk.config.Config.init_auth")

    config = Config(
        host="https://unified.databricks.com",
        azure_workspace_resource_id="/subscriptions/test/resourceGroups/test/providers/Microsoft.Databricks/workspaces/test",
        experimental_is_unified_host=True,
        azure_client_id="test-client-id",
        azure_tenant_id="test-tenant-id",
        azure_client_secret="test-secret",
    )

    # Manually set environment to None to simulate unified without cloud
    config.databricks_environment = None

    # is_azure should still be True due to azure_workspace_resource_id
    assert config.is_azure is True
    assert config.is_gcp is False
    assert config.is_aws is False
