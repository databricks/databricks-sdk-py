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
from databricks.sdk.environments import Cloud
from databricks.sdk.oauth import HostMetadata
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


def test_oidc_token_filepath_env_alias(monkeypatch, mocker):
    monkeypatch.setenv("DATABRICKS_HOST", "https://abc.def.ghi")
    monkeypatch.setenv("DATABRICKS_OIDC_TOKEN_FILE", "/tmp/token")
    monkeypatch.delenv("DATABRICKS_OIDC_TOKEN_FILEPATH", raising=False)
    mocker.patch("databricks.sdk.config.Config.init_auth")
    assert Config().oidc_token_filepath == "/tmp/token"


def test_oidc_token_filepath_env_primary_precedence(monkeypatch, mocker):
    monkeypatch.setenv("DATABRICKS_HOST", "https://abc.def.ghi")
    monkeypatch.setenv("DATABRICKS_OIDC_TOKEN_FILEPATH", "/tmp/primary")
    monkeypatch.setenv("DATABRICKS_OIDC_TOKEN_FILE", "/tmp/alias")
    mocker.patch("databricks.sdk.config.Config.init_auth")
    assert Config().oidc_token_filepath == "/tmp/primary"


def test_oidc_token_filepath_env_constructor_precedence(monkeypatch, mocker):
    monkeypatch.setenv("DATABRICKS_HOST", "https://abc.def.ghi")
    monkeypatch.setenv("DATABRICKS_OIDC_TOKEN_FILEPATH", "/tmp/env")
    monkeypatch.setenv("DATABRICKS_OIDC_TOKEN_FILE", "/tmp/alias")
    mocker.patch("databricks.sdk.config.Config.init_auth")
    assert Config(oidc_token_filepath="/tmp/constructor").oidc_token_filepath == "/tmp/constructor"


def test_extra_and_upstream_user_agent(monkeypatch):

    class MockUname:

        @property
        def system(self):
            return "TestOS"

    # Clear all environment variables and cached providers.
    for k in os.environ:
        monkeypatch.delenv(k, raising=False)
    monkeypatch.setattr(useragent, "_extra", [])
    monkeypatch.setattr(useragent, "_cicd_provider", None)
    monkeypatch.setattr(useragent, "_agent_provider", None)

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


def test_client_type_workspace():
    """Test that client type is workspace when workspace_id is set on unified host."""
    config = Config(
        host="https://unified.databricks.com",
        workspace_id="test-workspace",
        account_id="test-account",
        token="test-token",
    )
    assert config.client_type == ClientType.WORKSPACE


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


def test_is_account_client_backward_compatibility():
    """Test that is_account_client property still works for backward compatibility."""
    config_workspace = Config(host="https://test.databricks.com", token="test-token")
    assert not config_workspace.is_account_client

    config_account = Config(host="https://accounts.cloud.databricks.com", account_id="test-account", token="test-token")
    assert config_account.is_account_client


def test_is_account_client_does_not_raise_on_unified_host():
    """Test that is_account_client raises ValueError when used with unified hosts."""
    config = Config(
        host="https://unified.databricks.com",
        workspace_id="test-workspace",
        token="test-token",
    )
    config.is_account_client


def test_oidc_endpoints_unified_missing_ids(mocker):
    """Test that host metadata resolution raises error when oidc_endpoint has {account_id} placeholder but no account_id."""
    mocker.patch(
        "databricks.sdk.config.get_host_metadata",
        return_value=HostMetadata(
            oidc_endpoint="https://unified.databricks.com/oidc/accounts/{account_id}",
        ),
    )

    with pytest.raises(ValueError, match="account_id is required"):
        Config(host="https://unified.databricks.com", token="test-token")


def test_databricks_oidc_endpoints_ignores_azure_client_id(mocker, requests_mock):
    """Test that databricks_oidc_endpoints returns Databricks endpoints even when azure_client_id is set."""
    mocker.patch(
        "databricks.sdk.config.get_host_metadata",
        return_value=HostMetadata(
            oidc_endpoint="https://adb-123.4.azuredatabricks.net/oidc",
        ),
    )
    requests_mock.get(
        "https://adb-123.4.azuredatabricks.net/oidc/.well-known/oauth-authorization-server",
        json={
            "authorization_endpoint": "https://adb-123.4.azuredatabricks.net/oidc/v1/authorize",
            "token_endpoint": "https://adb-123.4.azuredatabricks.net/oidc/v1/token",
        },
    )

    # Disable auth validation since we're only testing oidc_endpoints property
    mocker.patch("databricks.sdk.config.Config.init_auth")
    config = Config(
        host="https://adb-123.4.azuredatabricks.net",
        azure_client_id="test-azure-client-id",  # This should be ignored by databricks_oidc_endpoints
    )

    endpoints = config.databricks_oidc_endpoints
    assert endpoints is not None
    assert "https://adb-123.4.azuredatabricks.net/oidc/v1/authorize" == endpoints.authorization_endpoint
    assert "https://adb-123.4.azuredatabricks.net/oidc/v1/token" == endpoints.token_endpoint


def test_oidc_endpoints_returns_azure_when_azure_client_id_set(mocker):
    """Test that deprecated oidc_endpoints returns Azure endpoints when azure_client_id is set on Azure.

    This tests the deprecated behavior that is maintained for backward compatibility.
    """
    # Mock the Azure endpoint detection
    mocker.patch(
        "databricks.sdk.config.get_azure_entra_id_workspace_endpoints",
        return_value=mocker.Mock(
            authorization_endpoint="https://login.microsoftonline.com/tenant-id/oauth2/v2.0/authorize",
            token_endpoint="https://login.microsoftonline.com/tenant-id/oauth2/v2.0/token",
        ),
    )
    # Disable auth validation since we're only testing oidc_endpoints property
    mocker.patch("databricks.sdk.config.Config.init_auth")

    config = Config(
        host="https://adb-123.4.azuredatabricks.net",
        azure_client_id="test-azure-client-id",
    )

    endpoints = config.oidc_endpoints
    assert endpoints is not None
    assert "login.microsoftonline.com" in endpoints.authorization_endpoint
    assert "login.microsoftonline.com" in endpoints.token_endpoint


def test_oidc_endpoints_falls_back_to_databricks_when_no_azure_client_id(mocker, requests_mock):
    """Test that deprecated oidc_endpoints falls back to Databricks endpoints when azure_client_id is not set."""
    mocker.patch(
        "databricks.sdk.config.get_host_metadata",
        return_value=HostMetadata(
            oidc_endpoint="https://adb-123.4.azuredatabricks.net/oidc",
        ),
    )
    requests_mock.get(
        "https://adb-123.4.azuredatabricks.net/oidc/.well-known/oauth-authorization-server",
        json={
            "authorization_endpoint": "https://adb-123.4.azuredatabricks.net/oidc/v1/authorize",
            "token_endpoint": "https://adb-123.4.azuredatabricks.net/oidc/v1/token",
        },
    )

    config = Config(
        host="https://adb-123.4.azuredatabricks.net",
        token="test-token",
    )

    endpoints = config.oidc_endpoints
    assert endpoints is not None
    assert "https://adb-123.4.azuredatabricks.net/oidc/v1/authorize" == endpoints.authorization_endpoint
    assert "https://adb-123.4.azuredatabricks.net/oidc/v1/token" == endpoints.token_endpoint


def test_workspace_org_id_header_on_unified_host(requests_mock):
    """Test that X-Databricks-Org-Id header is added for workspace clients on unified hosts."""

    requests_mock.get("https://unified.databricks.com/api/2.0/preview/scim/v2/Me", json={"result": "success"})

    config = Config(
        host="https://unified.databricks.com",
        account_id="test-account",
        workspace_id="test-workspace-123",
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
def test_m2m_scopes_sent_to_token_endpoint(mocker, requests_mock, scopes_input, expected_scope):
    """Test M2M authentication sends correct scopes to token endpoint."""
    mocker.patch(
        "databricks.sdk.config.get_host_metadata",
        return_value=HostMetadata(
            oidc_endpoint="https://test.databricks.com/oidc",
        ),
    )
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
def test_oidc_scopes_sent_to_token_endpoint(mocker, requests_mock, tmp_path, scopes_input, expected_scope):
    """Test OIDC token exchange sends correct scopes to token endpoint."""
    mocker.patch(
        "databricks.sdk.config.get_host_metadata",
        return_value=HostMetadata(
            oidc_endpoint="https://test.databricks.com/oidc",
        ),
    )
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


_DUMMY_WS_HOST = "https://dummy-workspace.databricks.com"
_DUMMY_ACC_HOST = "https://dummy-accounts.databricks.com"
_DUMMY_ACCOUNT_ID = "00000000-0000-0000-0000-000000000001"
_DUMMY_WORKSPACE_ID = "111111111111111"
_DUMMY_AUTH_ENDPOINT = f"{_DUMMY_WS_HOST}/oidc/v1/authorize"
_DUMMY_TOKEN_ENDPOINT = f"{_DUMMY_WS_HOST}/oidc/v1/token"


def test_discovery_url_from_env(monkeypatch):
    monkeypatch.setenv("DATABRICKS_DISCOVERY_URL", "https://custom.idp.example.com/oidc")
    config = Config(host=_DUMMY_WS_HOST, token="t")
    assert config.discovery_url == "https://custom.idp.example.com/oidc"


def test_databricks_oidc_endpoints_uses_discovery_url(requests_mock):
    discovery_url = f"{_DUMMY_WS_HOST}/oidc"
    requests_mock.get(
        discovery_url,
        json={"authorization_endpoint": _DUMMY_AUTH_ENDPOINT, "token_endpoint": _DUMMY_TOKEN_ENDPOINT},
    )
    config = Config(host=_DUMMY_WS_HOST, token="t", discovery_url=discovery_url)
    endpoints = config.databricks_oidc_endpoints
    assert endpoints.authorization_endpoint == _DUMMY_AUTH_ENDPOINT
    assert endpoints.token_endpoint == _DUMMY_TOKEN_ENDPOINT


@pytest.mark.parametrize(
    "host,response_json,config_kwargs,expected_fields",
    [
        pytest.param(
            _DUMMY_WS_HOST,
            {
                "oidc_endpoint": f"{_DUMMY_WS_HOST}/oidc",
                "account_id": _DUMMY_ACCOUNT_ID,
                "workspace_id": _DUMMY_WORKSPACE_ID,
            },
            {},
            {
                "account_id": _DUMMY_ACCOUNT_ID,
                "workspace_id": _DUMMY_WORKSPACE_ID,
                "discovery_url": f"{_DUMMY_WS_HOST}/oidc/.well-known/oauth-authorization-server",
            },
            id="unified-populates-all-fields",
        ),
        pytest.param(
            _DUMMY_ACC_HOST,
            {"oidc_endpoint": f"{_DUMMY_ACC_HOST}/oidc/accounts/{{account_id}}"},
            {"account_id": _DUMMY_ACCOUNT_ID},
            {
                "discovery_url": f"{_DUMMY_ACC_HOST}/oidc/accounts/{_DUMMY_ACCOUNT_ID}/.well-known/oauth-authorization-server"
            },
            id="unified-substitutes-account-id",
        ),
        pytest.param(
            _DUMMY_WS_HOST,
            {"oidc_endpoint": f"{_DUMMY_WS_HOST}/oidc", "account_id": "other-account", "workspace_id": "other-ws"},
            {
                "account_id": _DUMMY_ACCOUNT_ID,
                "workspace_id": _DUMMY_WORKSPACE_ID,
            },
            {"account_id": _DUMMY_ACCOUNT_ID, "workspace_id": _DUMMY_WORKSPACE_ID},
            id="unified-does-not-overwrite-existing-fields",
        ),
    ],
)
def test_resolve_host_metadata(mocker, host, response_json, config_kwargs, expected_fields):
    mocker.patch("databricks.sdk.config.get_host_metadata", return_value=oauth.HostMetadata.from_dict(response_json))
    config = Config(host=host, token="t", **config_kwargs)
    for field, expected in expected_fields.items():
        assert getattr(config, field) == expected


def test_resolve_host_metadata_missing_account_id(mocker):
    """Raises when the oidc_endpoint template requires account_id but none is configured."""
    mocker.patch(
        "databricks.sdk.config.get_host_metadata",
        return_value=oauth.HostMetadata.from_dict({"oidc_endpoint": f"{_DUMMY_ACC_HOST}/oidc/accounts/{{account_id}}"}),
    )
    with pytest.raises(ValueError, match="account_id is required to resolve discovery_url"):
        Config(host=_DUMMY_ACC_HOST, token="t")


def test_resolve_host_metadata_no_oidc_endpoint(mocker):
    """No raise when metadata has no oidc_endpoint; discovery_url stays unset."""
    mocker.patch(
        "databricks.sdk.config.get_host_metadata",
        return_value=oauth.HostMetadata.from_dict({"account_id": _DUMMY_ACCOUNT_ID}),
    )
    config = Config(host=_DUMMY_WS_HOST, token="t")
    assert config.account_id == _DUMMY_ACCOUNT_ID
    assert config.discovery_url is None


def test_resolve_host_metadata_http_error(mocker):
    """HTTP failure is swallowed with a warning; fields remain unset."""
    mocker.patch(
        "databricks.sdk.config.get_host_metadata",
        side_effect=ValueError(f"Failed to fetch host metadata from {_DUMMY_WS_HOST}/.well-known/databricks-config"),
    )
    config = Config(host=_DUMMY_WS_HOST, token="t")
    assert config.account_id is None
    assert config.discovery_url is None


def test_resolve_host_metadata_called_for_non_unified(mocker):
    """Metadata resolution is skipped entirely for non-unified (workspace/account) hosts."""
    mock_get = mocker.patch("databricks.sdk.config.get_host_metadata")
    Config(host=_DUMMY_WS_HOST, token="t")
    mock_get.assert_called_once()


# ---------------------------------------------------------------------------
# Cloud field tests
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "cloud_str,expected_cloud",
    [
        ("AWS", Cloud.AWS),
        ("aws", Cloud.AWS),
        ("Azure", Cloud.AZURE),
        ("AZURE", Cloud.AZURE),
        ("GCP", Cloud.GCP),
        ("gcp", Cloud.GCP),
    ],
)
def test_cloud_parse_case_insensitive(cloud_str, expected_cloud):
    """Cloud.parse handles any casing."""
    assert Cloud.parse(cloud_str) == expected_cloud


def test_cloud_parse_unknown_returns_none():
    """Cloud.parse returns None for unrecognized values (forward compatibility)."""
    assert Cloud.parse("UNKNOWN_FUTURE_CLOUD") is None


def test_cloud_parse_empty_returns_none():
    assert Cloud.parse("") is None
    assert Cloud.parse(None) is None


def test_cloud_field_overrides_dns_detection_aws():
    """Explicit cloud=AWS wins over hostname-based detection."""
    config = Config(host="https://myworkspace.azuredatabricks.net", token="t", cloud="AWS")
    assert config.is_aws
    assert not config.is_azure
    assert not config.is_gcp


def test_cloud_field_overrides_dns_detection_azure():
    """Explicit cloud=AZURE wins over hostname-based detection."""
    config = Config(host="https://myworkspace.cloud.databricks.com", token="t", cloud="AZURE")
    assert config.is_azure
    assert not config.is_aws
    assert not config.is_gcp


def test_cloud_field_overrides_dns_detection_gcp():
    """Explicit cloud=GCP wins over hostname-based detection."""
    config = Config(host="https://myworkspace.cloud.databricks.com", token="t", cloud="GCP")
    assert config.is_gcp
    assert not config.is_aws
    assert not config.is_azure


def test_cloud_field_falls_back_to_dns_when_unset():
    """When cloud is not set, falls back to DNS-based detection."""
    config = Config(host="https://myworkspace.azuredatabricks.net", token="t")
    assert config.is_azure
    assert not config.is_aws


def test_cloud_field_azure_resource_id_still_wins():
    """azure_workspace_resource_id takes precedence over cloud field for is_azure."""
    config = Config(
        host="https://myworkspace.cloud.databricks.com",
        credentials_strategy=noop_credentials,
        cloud="AWS",
        azure_workspace_resource_id="/subscriptions/sub/resourceGroups/rg/providers/Microsoft.Databricks/workspaces/ws",
    )
    assert config.is_azure


def test_resolve_host_metadata_populates_cloud(mocker):
    """Cloud is populated from the discovery endpoint."""
    mocker.patch(
        "databricks.sdk.config.get_host_metadata",
        return_value=oauth.HostMetadata.from_dict(
            {
                "oidc_endpoint": f"{_DUMMY_WS_HOST}/oidc",
                "cloud": "AWS",
            }
        ),
    )
    config = Config(host=_DUMMY_WS_HOST, token="t")
    assert config.cloud == Cloud.AWS


def test_resolve_host_metadata_cloud_not_overwritten(mocker):
    """Explicit cloud config is not overwritten by the discovery endpoint."""
    mocker.patch(
        "databricks.sdk.config.get_host_metadata",
        return_value=oauth.HostMetadata.from_dict(
            {
                "oidc_endpoint": f"{_DUMMY_WS_HOST}/oidc",
                "cloud": "AZURE",
            }
        ),
    )
    config = Config(
        host=_DUMMY_WS_HOST,
        token="t",
        cloud="AWS",
    )
    assert config.cloud == Cloud.AWS


def test_resolve_host_metadata_cloud_missing_in_response(mocker):
    """When endpoint omits cloud, the field stays unset (falls back to DNS)."""
    mocker.patch(
        "databricks.sdk.config.get_host_metadata",
        return_value=oauth.HostMetadata.from_dict({"oidc_endpoint": f"{_DUMMY_WS_HOST}/oidc"}),
    )
    config = Config(host=_DUMMY_WS_HOST, token="t")
    assert config.cloud is None


# ---------------------------------------------------------------------------
# token_audience resolution from host metadata
# ---------------------------------------------------------------------------


def test_resolve_host_metadata_sets_token_audience_for_account_host(mocker):
    """When metadata has no workspace_id, token_audience is set to account_id."""
    mocker.patch(
        "databricks.sdk.config.get_host_metadata",
        return_value=oauth.HostMetadata.from_dict(
            {
                "oidc_endpoint": f"{_DUMMY_ACC_HOST}/oidc/accounts/{_DUMMY_ACCOUNT_ID}",
                "account_id": _DUMMY_ACCOUNT_ID,
            }
        ),
    )
    config = Config(
        host=_DUMMY_ACC_HOST,
        token="t",
        account_id=_DUMMY_ACCOUNT_ID,
    )
    assert config.token_audience == _DUMMY_ACCOUNT_ID


def test_resolve_host_metadata_no_token_audience_for_workspace_host(mocker):
    """When metadata contains workspace_id, token_audience is not set from metadata."""
    mocker.patch(
        "databricks.sdk.config.get_host_metadata",
        return_value=oauth.HostMetadata.from_dict(
            {
                "oidc_endpoint": f"{_DUMMY_WS_HOST}/oidc",
                "account_id": _DUMMY_ACCOUNT_ID,
                "workspace_id": _DUMMY_WORKSPACE_ID,
            }
        ),
    )
    config = Config(host=_DUMMY_WS_HOST, token="t")
    assert config.token_audience is None


def test_resolve_host_metadata_does_not_overwrite_token_audience(mocker):
    """An explicitly set token_audience is never overwritten by metadata resolution."""
    mocker.patch(
        "databricks.sdk.config.get_host_metadata",
        return_value=oauth.HostMetadata.from_dict(
            {
                "oidc_endpoint": f"{_DUMMY_ACC_HOST}/oidc/accounts/{_DUMMY_ACCOUNT_ID}",
                "account_id": _DUMMY_ACCOUNT_ID,
            }
        ),
    )
    config = Config(
        host=_DUMMY_ACC_HOST,
        token="t",
        account_id=_DUMMY_ACCOUNT_ID,
        token_audience="custom-audience",
    )
    assert config.token_audience == "custom-audience"


# ---------------------------------------------------------------------------
# token_federation_default_oidc_audiences resolution from host metadata
# ---------------------------------------------------------------------------


def test_resolve_host_metadata_sets_token_audience_from_token_federation_default_oidc_audiences(mocker):
    """token_audience is set from token_federation_default_oidc_audiences in host metadata."""
    mocker.patch(
        "databricks.sdk.config.get_host_metadata",
        return_value=HostMetadata.from_dict(
            {
                "oidc_endpoint": f"{_DUMMY_WS_HOST}/oidc",
                "account_id": _DUMMY_ACCOUNT_ID,
                "workspace_id": _DUMMY_WORKSPACE_ID,
                "token_federation_default_oidc_audiences": [f"{_DUMMY_WS_HOST}/oidc/v1/token"],
            }
        ),
    )
    config = Config(host=_DUMMY_WS_HOST, token="t")
    assert config.token_audience == f"{_DUMMY_WS_HOST}/oidc/v1/token"


def test_resolve_host_metadata_token_federation_default_oidc_audiences_takes_priority_over_account_id_fallback(mocker):
    """token_federation_default_oidc_audiences takes priority over the account_id fallback."""
    mocker.patch(
        "databricks.sdk.config.get_host_metadata",
        return_value=HostMetadata.from_dict(
            {
                "oidc_endpoint": f"{_DUMMY_ACC_HOST}/oidc/accounts/{_DUMMY_ACCOUNT_ID}",
                "account_id": _DUMMY_ACCOUNT_ID,
                "token_federation_default_oidc_audiences": ["custom-audience-from-server"],
            }
        ),
    )
    config = Config(host=_DUMMY_ACC_HOST, token="t", account_id=_DUMMY_ACCOUNT_ID)
    # token_federation_default_oidc_audiences should take priority over the account_id fallback
    assert config.token_audience == "custom-audience-from-server"


def test_resolve_host_metadata_token_federation_default_oidc_audiences_does_not_override_existing_token_audience(
    mocker,
):
    """An explicitly set token_audience is not overwritten by token_federation_default_oidc_audiences."""
    mocker.patch(
        "databricks.sdk.config.get_host_metadata",
        return_value=HostMetadata.from_dict(
            {
                "oidc_endpoint": f"{_DUMMY_WS_HOST}/oidc",
                "account_id": _DUMMY_ACCOUNT_ID,
                "workspace_id": _DUMMY_WORKSPACE_ID,
                "token_federation_default_oidc_audiences": [f"{_DUMMY_WS_HOST}/oidc/v1/token"],
            }
        ),
    )
    config = Config(host=_DUMMY_WS_HOST, token="t", token_audience="my-custom-audience")
    assert config.token_audience == "my-custom-audience"


def test_resolve_host_metadata_falls_back_to_account_id_when_no_token_federation_default_oidc_audiences(mocker):
    """When no token_federation_default_oidc_audiences and no workspace_id, falls back to account_id."""
    mocker.patch(
        "databricks.sdk.config.get_host_metadata",
        return_value=HostMetadata.from_dict(
            {
                "oidc_endpoint": f"{_DUMMY_ACC_HOST}/oidc/accounts/{_DUMMY_ACCOUNT_ID}",
                "account_id": _DUMMY_ACCOUNT_ID,
            }
        ),
    )
    config = Config(host=_DUMMY_ACC_HOST, token="t", account_id=_DUMMY_ACCOUNT_ID)
    # No token_federation_default_oidc_audiences and no workspace_id → falls back to account_id
    assert config.token_audience == _DUMMY_ACCOUNT_ID
