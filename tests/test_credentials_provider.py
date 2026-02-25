from datetime import datetime, timedelta
from unittest.mock import Mock

import pytest

from databricks.sdk import credentials_provider, oauth, oidc
from databricks.sdk.client_types import ClientType
from databricks.sdk.config import Config


# Tests for external_browser function
def test_external_browser_refresh_success(mocker):
    """Tests successful refresh of existing credentials."""

    # Mock Config.
    mock_cfg = Mock()
    mock_cfg.auth_type = "external-browser"
    mock_cfg.host = "test-host"
    mock_cfg.databricks_oidc_endpoints = {"token_endpoint": "test-token-endpoint"}
    mock_cfg.client_id = "test-client-id"  # Or use azure_client_id
    mock_cfg.client_secret = "test-client-secret"  # Or use azure_client_secret

    # Mock TokenCache.
    mock_token_cache = Mock()
    mock_session_credentials = Mock()
    mock_session_credentials.token.return_value = "valid_token"  # Simulate successful refresh
    mock_token_cache.load.return_value = mock_session_credentials

    # Mock SessionCredentials.
    def want_credentials_provider(_):
        return "new_credentials"

    mock_session_credentials.return_value = want_credentials_provider

    # Inject the mock implementations.
    mocker.patch(
        "databricks.sdk.oauth.TokenCache",
        return_value=mock_token_cache,
    )

    got_credentials_provider = credentials_provider.external_browser(mock_cfg)

    mock_token_cache.load.assert_called_once()
    mock_session_credentials.token.assert_called_once()  # Verify token refresh was attempted
    assert got_credentials_provider == want_credentials_provider


def test_external_browser_refresh_failure_new_oauth_flow(mocker):
    """Tests failed refresh, triggering a new OAuth flow."""

    # Mock Config.
    mock_cfg = Mock()
    mock_cfg.auth_type = "external-browser"
    mock_cfg.host = "test-host"
    mock_cfg.databricks_oidc_endpoints = {"token_endpoint": "test-token-endpoint"}
    mock_cfg.client_id = "test-client-id"
    mock_cfg.client_secret = "test-client-secret"

    # Mock TokenCache.
    mock_token_cache = Mock()
    mock_session_credentials = Mock()
    mock_session_credentials.token.side_effect = Exception("Simulated refresh error")  # Simulate a failed refresh
    mock_token_cache.load.return_value = mock_session_credentials

    # Mock SessionCredentials.
    def want_credentials_provider(_):
        return "new_credentials"

    mock_session_credentials.return_value = want_credentials_provider

    # Mock OAuthClient.
    mock_oauth_client = Mock()
    mock_consent = Mock()
    mock_consent.launch_external_browser.return_value = mock_session_credentials
    mock_oauth_client.initiate_consent.return_value = mock_consent

    # Inject the mock implementations.
    mocker.patch(
        "databricks.sdk.oauth.TokenCache",
        return_value=mock_token_cache,
    )
    mocker.patch(
        "databricks.sdk.oauth.OAuthClient",
        return_value=mock_oauth_client,
    )

    got_credentials_provider = credentials_provider.external_browser(mock_cfg)

    mock_token_cache.load.assert_called_once()
    mock_session_credentials.token.assert_called_once()  # Refresh attempt
    mock_oauth_client.initiate_consent.assert_called_once()
    mock_consent.launch_external_browser.assert_called_once()
    mock_token_cache.save.assert_called_once_with(mock_session_credentials)
    assert got_credentials_provider == want_credentials_provider


def test_external_browser_no_cached_credentials(mocker):
    """Tests the case where there are no cached credentials, initiating a new OAuth flow."""

    # Mock Config.
    mock_cfg = Mock()
    mock_cfg.auth_type = "external-browser"
    mock_cfg.host = "test-host"
    mock_cfg.databricks_oidc_endpoints = {"token_endpoint": "test-token-endpoint"}
    mock_cfg.client_id = "test-client-id"
    mock_cfg.client_secret = "test-client-secret"

    # Mock TokenCache.
    mock_token_cache = Mock()
    mock_token_cache.load.return_value = None  # No cached credentials

    # Mock SessionCredentials.
    mock_session_credentials = Mock()

    def want_credentials_provider(_):
        return "new_credentials"

    mock_session_credentials.return_value = want_credentials_provider

    # Mock OAuthClient.
    mock_consent = Mock()
    mock_consent.launch_external_browser.return_value = mock_session_credentials
    mock_oauth_client = Mock()
    mock_oauth_client.initiate_consent.return_value = mock_consent

    # Inject the mock implementations.
    mocker.patch(
        "databricks.sdk.oauth.TokenCache",
        return_value=mock_token_cache,
    )
    mocker.patch(
        "databricks.sdk.oauth.OAuthClient",
        return_value=mock_oauth_client,
    )

    got_credentials_provider = credentials_provider.external_browser(mock_cfg)

    mock_token_cache.load.assert_called_once()
    mock_oauth_client.initiate_consent.assert_called_once()
    mock_consent.launch_external_browser.assert_called_once()
    mock_token_cache.save.assert_called_once_with(mock_session_credentials)
    assert got_credentials_provider == want_credentials_provider


def test_external_browser_consent_fails(mocker):
    """Tests the case where OAuth consent initiation fails."""

    # Mock Config.
    mock_cfg = Mock()
    mock_cfg.auth_type = "external-browser"
    mock_cfg.host = "test-host"
    mock_cfg.databricks_oidc_endpoints = {"token_endpoint": "test-token-endpoint"}
    mock_cfg.client_id = "test-client-id"
    mock_cfg.client_secret = "test-client-secret"

    # Mock TokenCache.
    mock_token_cache = Mock()
    mock_token_cache.load.return_value = None  # No cached credentials

    # Mock OAuthClient.
    mock_oauth_client = Mock()
    mock_oauth_client.initiate_consent.return_value = None  # Simulate consent failure

    # Inject the mock implementations.
    mocker.patch(
        "databricks.sdk.oauth.TokenCache",
        return_value=mock_token_cache,
    )
    mocker.patch(
        "databricks.sdk.oauth.OAuthClient",
        return_value=mock_oauth_client,
    )

    got_credentials_provider = credentials_provider.external_browser(mock_cfg)

    mock_token_cache.load.assert_called_once()
    mock_oauth_client.initiate_consent.assert_called_once()
    assert got_credentials_provider is None


def _setup_external_browser_mocks(mocker, cfg):
    """Set up mocks for external_browser scope tests. Returns (TokenCache mock, OAuthClient mock)."""
    mock_oidc_endpoints = Mock()
    mock_oidc_endpoints.token_endpoint = "https://test.databricks.com/oidc/v1/token"
    mocker.patch.object(
        type(cfg), "databricks_oidc_endpoints", new_callable=lambda: property(lambda self: mock_oidc_endpoints)
    )

    mock_token_cache_class = mocker.patch("databricks.sdk.credentials_provider.oauth.TokenCache")
    mock_token_cache = Mock()
    mock_token_cache.load.return_value = None
    mock_token_cache_class.return_value = mock_token_cache

    mock_oauth_client_class = mocker.patch("databricks.sdk.credentials_provider.oauth.OAuthClient")
    mock_oauth_client = Mock()
    mock_consent = Mock()
    mock_consent.launch_external_browser.return_value = Mock()
    mock_oauth_client.initiate_consent.return_value = mock_consent
    mock_oauth_client_class.return_value = mock_oauth_client

    return mock_token_cache_class, mock_oauth_client_class


@pytest.mark.parametrize(
    "scopes,disable_refresh,expected_scopes",
    [
        (None, False, ["all-apis", "offline_access"]),
        ("sql, clusters, jobs", False, ["clusters", "jobs", "sql", "offline_access"]),
        (None, True, ["all-apis"]),
        ("sql, clusters, jobs, offline_access", False, ["clusters", "jobs", "offline_access", "sql"]),
    ],
    ids=["default_scopes", "multiple_scopes_sorted", "disable_offline_access", "offline_access_not_duplicated"],
)
def test_external_browser_scopes(mocker, scopes, disable_refresh, expected_scopes):
    """Tests that external_browser passes correct scopes to TokenCache and OAuthClient."""
    mocker.patch("databricks.sdk.config.Config.init_auth")
    cfg = Config(
        host="https://test.databricks.com",
        auth_type="external-browser",
        scopes=scopes,
        disable_oauth_refresh_token=disable_refresh if disable_refresh else None,
    )
    mock_token_cache_class, mock_oauth_client_class = _setup_external_browser_mocks(mocker, cfg)

    credentials_provider.external_browser(cfg)

    assert mock_token_cache_class.call_args.kwargs["scopes"] == expected_scopes
    assert mock_oauth_client_class.call_args.kwargs["scopes"] == expected_scopes


def test_oidc_credentials_provider_invalid_id_token_source():
    # Use a mock config object to avoid initializing the auth initialization.
    mock_cfg = Mock()
    mock_cfg.host = "https://test-workspace.cloud.databricks.com"
    mock_cfg.databricks_oidc_endpoints = Mock()
    mock_cfg.databricks_oidc_endpoints.token_endpoint = "https://test-workspace.cloud.databricks.com/oidc/v1/token"
    mock_cfg.client_id = "test-client-id"
    mock_cfg.account_id = "test-account-id"
    mock_cfg.disable_async_token_refresh = True

    # An IdTokenSource that raises an error when id_token() is called.
    id_token_source = Mock()
    id_token_source.id_token.side_effect = ValueError("Invalid ID token source")

    cp = credentials_provider.oidc_credentials_provider(mock_cfg, id_token_source)
    assert cp is None


def test_oidc_credentials_provider_valid_id_token_source(mocker):
    # Use a mock config object to avoid initializing the auth initialization.
    mock_cfg = Mock()
    mock_cfg.host = "https://test-workspace.cloud.databricks.com"
    mock_cfg.databricks_oidc_endpoints = Mock()
    mock_cfg.databricks_oidc_endpoints.token_endpoint = "https://test-workspace.cloud.databricks.com/oidc/v1/token"
    mock_cfg.client_id = "test-client-id"
    mock_cfg.account_id = "test-account-id"
    mock_cfg.disable_async_token_refresh = True

    # A valid IdTokenSource that never raises an error.
    id_token_source = Mock()
    id_token_source.id_token.return_value = oidc.IdToken(jwt="test-jwt-token")

    # Mock the _exchange_id_token method on DatabricksOidcTokenSource to return
    # a valid oauth.Token based on the IdToken.
    def mock_exchange_id_token(id_token: oidc.IdToken):
        # Create a token based on the input ID token
        return oauth.Token(
            access_token=f"exchanged-{id_token.jwt}", token_type="Bearer", expiry=datetime.now() + timedelta(hours=1)
        )

    mocker.patch.object(oidc.DatabricksOidcTokenSource, "_exchange_id_token", side_effect=mock_exchange_id_token)

    cp = credentials_provider.oidc_credentials_provider(mock_cfg, id_token_source)
    assert cp is not None

    # Test that the credentials provider returns the expected headers
    headers = cp()
    assert headers == {"Authorization": "Bearer exchanged-test-jwt-token"}


# Tests for DatabricksCliTokenSource CLI argument construction
class TestDatabricksCliTokenSourceArgs:
    """Tests that DatabricksCliTokenSource constructs correct CLI arguments."""

    def test_unified_host_passes_all_flags(self, mocker):
        """Unified host should pass --experimental-is-unified-host, --account-id, and --workspace-id."""
        # Mock the parent class __init__ to capture the command arguments
        mock_init = mocker.patch.object(
            credentials_provider.CliTokenSource,
            "__init__",
            return_value=None,
        )

        mock_cfg = Mock()
        mock_cfg.profile = None
        mock_cfg.host = "https://example.databricks.com"
        mock_cfg.experimental_is_unified_host = True
        mock_cfg.account_id = "test-account-id"
        mock_cfg.workspace_id = 12345
        mock_cfg.databricks_cli_path = "/path/to/databricks"
        mock_cfg.disable_async_token_refresh = False

        credentials_provider.DatabricksCliTokenSource(mock_cfg)

        # Verify the command was constructed correctly
        call_kwargs = mock_init.call_args
        cmd = call_kwargs.kwargs["cmd"]

        assert cmd[0] == "/path/to/databricks"
        assert "auth" in cmd
        assert "token" in cmd
        assert "--host" in cmd
        assert "https://example.databricks.com" in cmd
        assert "--experimental-is-unified-host" in cmd
        assert "--account-id" in cmd
        assert "test-account-id" in cmd
        assert "--workspace-id" in cmd
        assert "12345" in cmd

    def test_unified_host_without_workspace_id(self, mocker):
        """Unified host without workspace_id should only pass --experimental-is-unified-host and --account-id."""
        mock_init = mocker.patch.object(
            credentials_provider.CliTokenSource,
            "__init__",
            return_value=None,
        )

        mock_cfg = Mock()
        mock_cfg.profile = None
        mock_cfg.host = "https://example.databricks.com"
        mock_cfg.experimental_is_unified_host = True
        mock_cfg.account_id = "test-account-id"
        mock_cfg.workspace_id = None
        mock_cfg.databricks_cli_path = "/path/to/databricks"
        mock_cfg.disable_async_token_refresh = False

        credentials_provider.DatabricksCliTokenSource(mock_cfg)

        call_kwargs = mock_init.call_args
        cmd = call_kwargs.kwargs["cmd"]

        assert "--experimental-is-unified-host" in cmd
        assert "--account-id" in cmd
        assert "test-account-id" in cmd
        assert "--workspace-id" not in cmd

    def test_account_client_passes_account_id(self, mocker):
        """Non-unified account client should pass --account-id."""
        mock_init = mocker.patch.object(
            credentials_provider.CliTokenSource,
            "__init__",
            return_value=None,
        )

        mock_cfg = Mock()
        mock_cfg.profile = None
        mock_cfg.host = "https://accounts.cloud.databricks.com"
        mock_cfg.experimental_is_unified_host = False
        mock_cfg.account_id = "test-account-id"
        mock_cfg.client_type = ClientType.ACCOUNT
        mock_cfg.databricks_cli_path = "/path/to/databricks"
        mock_cfg.disable_async_token_refresh = False

        credentials_provider.DatabricksCliTokenSource(mock_cfg)

        call_kwargs = mock_init.call_args
        cmd = call_kwargs.kwargs["cmd"]

        assert "--experimental-is-unified-host" not in cmd
        assert "--account-id" in cmd
        assert "test-account-id" in cmd
        assert "--workspace-id" not in cmd

    def test_profile_uses_profile_flag_with_host_fallback(self, mocker):
        """When profile is set, --profile is used as primary and --host as fallback."""
        mock_init = mocker.patch.object(
            credentials_provider.CliTokenSource,
            "__init__",
            return_value=None,
        )

        mock_cfg = Mock()
        mock_cfg.profile = "my-profile"
        mock_cfg.host = "https://workspace.databricks.com"
        mock_cfg.experimental_is_unified_host = False
        mock_cfg.databricks_cli_path = "/path/to/databricks"
        mock_cfg.disable_async_token_refresh = False

        credentials_provider.DatabricksCliTokenSource(mock_cfg)

        call_kwargs = mock_init.call_args
        cmd = call_kwargs.kwargs["cmd"]
        host_cmd = call_kwargs.kwargs["host_cmd"]

        assert cmd == ["/path/to/databricks", "auth", "token", "--profile", "my-profile"]
        assert host_cmd is not None
        assert "--host" in host_cmd
        assert "https://workspace.databricks.com" in host_cmd
        assert "--profile" not in host_cmd

    def test_profile_without_host_no_fallback(self, mocker):
        """When profile is set but host is absent, no fallback is built."""
        mock_init = mocker.patch.object(
            credentials_provider.CliTokenSource,
            "__init__",
            return_value=None,
        )

        mock_cfg = Mock()
        mock_cfg.profile = "my-profile"
        mock_cfg.host = None
        mock_cfg.databricks_cli_path = "/path/to/databricks"
        mock_cfg.disable_async_token_refresh = False

        credentials_provider.DatabricksCliTokenSource(mock_cfg)

        call_kwargs = mock_init.call_args
        cmd = call_kwargs.kwargs["cmd"]
        host_cmd = call_kwargs.kwargs["host_cmd"]

        assert cmd == ["/path/to/databricks", "auth", "token", "--profile", "my-profile"]
        assert host_cmd is None


# Tests for CliTokenSource fallback on unknown --profile flag
class TestCliTokenSourceFallback:
    """Tests that CliTokenSource falls back to --host when CLI doesn't support --profile."""

    def _make_token_source(self, host_cmd=None):
        ts = credentials_provider.CliTokenSource.__new__(credentials_provider.CliTokenSource)
        ts._cmd = ["databricks", "auth", "token", "--profile", "my-profile"]
        ts._host_cmd = host_cmd
        ts._token_type_field = "token_type"
        ts._access_token_field = "access_token"
        ts._expiry_field = "expiry"
        return ts

    def _make_process_error(self, stderr: str):
        import subprocess

        err = subprocess.CalledProcessError(1, ["databricks"])
        err.stdout = b""
        err.stderr = stderr.encode()
        return err

    def test_fallback_on_unknown_profile_flag(self, mocker):
        """When --profile fails with 'unknown flag: --profile', falls back to --host command."""
        import json

        expiry = (datetime.now() + timedelta(hours=1)).strftime("%Y-%m-%dT%H:%M:%S")
        valid_response = json.dumps({"access_token": "fallback-token", "token_type": "Bearer", "expiry": expiry})

        mock_run = mocker.patch("databricks.sdk.credentials_provider._run_subprocess")
        mock_run.side_effect = [
            self._make_process_error("Error: unknown flag: --profile"),
            Mock(stdout=valid_response.encode()),
        ]

        host_cmd = ["databricks", "auth", "token", "--host", "https://workspace.databricks.com"]
        ts = self._make_token_source(host_cmd=host_cmd)
        token = ts.refresh()
        assert token.access_token == "fallback-token"
        assert mock_run.call_count == 2
        assert mock_run.call_args_list[1][0][0] == host_cmd

    def test_no_fallback_on_real_auth_error(self, mocker):
        """When --profile fails with a real error (not unknown flag), no fallback is attempted."""
        mock_run = mocker.patch("databricks.sdk.credentials_provider._run_subprocess")
        mock_run.side_effect = self._make_process_error("cache: databricks OAuth is not configured for this host")

        host_cmd = ["databricks", "auth", "token", "--host", "https://workspace.databricks.com"]
        ts = self._make_token_source(host_cmd=host_cmd)
        with pytest.raises(IOError) as exc_info:
            ts.refresh()
        assert "databricks OAuth is not configured" in str(exc_info.value)
        assert mock_run.call_count == 1

    def test_no_fallback_when_host_cmd_not_set(self, mocker):
        """When host_cmd is None and --profile fails, the original error is raised."""
        mock_run = mocker.patch("databricks.sdk.credentials_provider._run_subprocess")
        mock_run.side_effect = self._make_process_error("Error: unknown flag: --profile")

        ts = self._make_token_source(host_cmd=None)
        with pytest.raises(IOError) as exc_info:
            ts.refresh()
        assert "unknown flag: --profile" in str(exc_info.value)
        assert mock_run.call_count == 1


# Tests for cloud-agnostic hosts and removed cloud checks
class TestCloudAgnosticHosts:
    """Tests that credential providers work with cloud-agnostic hosts after removing is_azure/is_gcp checks."""

    def test_azure_service_principal_with_cloud_agnostic_host(self, mocker):
        """Test that azure_service_principal works with cloud-agnostic hosts after removing is_azure requirement."""
        # Mock Config with cloud-agnostic host
        mock_cfg = Mock()
        mock_cfg.host = "https://api.databricks.com"  # Cloud-agnostic host
        mock_cfg.azure_client_id = "test-azure-client-id"
        mock_cfg.azure_client_secret = "test-azure-secret"
        mock_cfg.azure_tenant_id = "test-tenant-id"
        mock_cfg.azure_workspace_resource_id = None
        mock_cfg.arm_environment = Mock()
        mock_cfg.arm_environment.active_directory_endpoint = "https://login.microsoftonline.com/"
        mock_cfg.arm_environment.service_management_endpoint = "https://management.core.windows.net/"
        mock_cfg.effective_azure_login_app_id = "2ff814a6-3304-4ab8-85cb-cd0e6f879c1d"
        mock_cfg.disable_async_token_refresh = True
        mock_cfg.get_scopes_as_string = Mock(return_value="all-apis")
        mock_cfg.authorization_details = None

        # Mock ClientCredentials to avoid actual token requests
        mock_token = oauth.Token(
            access_token="test-access-token", token_type="Bearer", expiry=datetime.now() + timedelta(hours=1)
        )
        mock_token_source = Mock()
        mock_token_source.token.return_value = mock_token

        mocker.patch("databricks.sdk.credentials_provider.oauth.ClientCredentials", return_value=mock_token_source)
        mocker.patch("databricks.sdk.credentials_provider.azure.add_workspace_id_header")
        mocker.patch("databricks.sdk.credentials_provider.azure.add_sp_management_token")

        # Should work now without is_azure check
        provider = credentials_provider.azure_service_principal(mock_cfg)
        assert provider is not None

        headers = provider()
        assert "Authorization" in headers
        assert headers["Authorization"] == "Bearer test-access-token"

    def test_google_credentials_with_cloud_agnostic_host(self, mocker):
        """Test that google_credentials works with cloud-agnostic hosts after removing is_gcp check."""
        # Mock Config with cloud-agnostic host
        mock_cfg = Mock()
        mock_cfg.host = "https://api.databricks.com"  # Cloud-agnostic host
        mock_cfg.google_credentials = '{"type": "service_account", "project_id": "test"}'
        mock_cfg.client_type = ClientType.WORKSPACE
        mock_cfg.disable_async_token_refresh = True

        # Mock service account credentials
        mock_credentials = Mock()
        mock_credentials.token = "test-google-token"
        mock_credentials.refresh = Mock()

        mocker.patch(
            "databricks.sdk.credentials_provider.service_account.IDTokenCredentials.from_service_account_info",
            return_value=mock_credentials,
        )
        mocker.patch(
            "databricks.sdk.credentials_provider.service_account.Credentials.from_service_account_info",
            return_value=mock_credentials,
        )

        # Should work now without is_gcp check
        provider = credentials_provider.google_credentials(mock_cfg)
        assert provider is not None

        headers = provider()
        assert "Authorization" in headers
        assert headers["Authorization"] == "Bearer test-google-token"

    def test_google_id_with_cloud_agnostic_host(self, mocker):
        """Test that google_id works with cloud-agnostic hosts after removing is_gcp check."""
        # Mock Config with cloud-agnostic host
        mock_cfg = Mock()
        mock_cfg.host = "https://api.databricks.com"  # Cloud-agnostic host
        mock_cfg.google_service_account = "test-sa@project.iam.gserviceaccount.com"
        mock_cfg.client_type = ClientType.WORKSPACE

        # Mock google.auth.default
        mock_source_credentials = Mock()
        mocker.patch(
            "databricks.sdk.credentials_provider.google.auth.default",
            return_value=(mock_source_credentials, "test-project"),
        )

        # Mock impersonated credentials
        mock_id_creds = Mock()
        mock_id_creds.token = "test-google-id-token"
        mock_id_creds.refresh = Mock()

        mock_gcp_creds = Mock()
        mock_gcp_creds.token = "test-gcp-token"
        mock_gcp_creds.refresh = Mock()

        mocker.patch("databricks.sdk.credentials_provider.impersonated_credentials.Credentials", return_value=Mock())
        mocker.patch(
            "databricks.sdk.credentials_provider.impersonated_credentials.IDTokenCredentials",
            return_value=mock_id_creds,
        )

        # Should work now without is_gcp check
        provider = credentials_provider.google_id(mock_cfg)
        assert provider is not None

        headers = provider()
        assert "Authorization" in headers
        assert headers["Authorization"] == "Bearer test-google-id-token"

    def test_github_oidc_azure_with_cloud_agnostic_host(self, mocker):
        """Test that github_oidc_azure works with cloud-agnostic hosts after removing is_azure check."""
        # Set up GitHub Actions environment
        mocker.patch.dict("os.environ", {"ACTIONS_ID_TOKEN_REQUEST_TOKEN": "test-token"})

        # Mock Config with cloud-agnostic host
        mock_cfg = Mock()
        mock_cfg.host = "https://api.databricks.com"  # Cloud-agnostic host
        mock_cfg.azure_client_id = "test-azure-client-id"
        mock_cfg.azure_tenant_id = None  # Will be auto-detected
        mock_cfg.arm_environment = Mock()
        mock_cfg.arm_environment.active_directory_endpoint = "https://login.microsoftonline.com/"
        mock_cfg.effective_azure_login_app_id = "2ff814a6-3304-4ab8-85cb-cd0e6f879c1d"
        mock_cfg.disable_async_token_refresh = True
        mock_cfg.get_scopes_as_string = Mock(return_value="all-apis")
        mock_cfg.authorization_details = None

        # Mock GitHub OIDC token supplier
        mock_supplier = Mock()
        mock_supplier.get_oidc_token.return_value = "test-github-oidc-token"
        mocker.patch(
            "databricks.sdk.credentials_provider.oidc_token_supplier.GitHubOIDCTokenSupplier",
            return_value=mock_supplier,
        )

        # Mock Azure Entra ID endpoints
        mock_endpoints = Mock()
        mock_endpoints.token_endpoint = "https://login.microsoftonline.com/test-tenant-id/oauth2/token"
        mocker.patch(
            "databricks.sdk.credentials_provider.get_azure_entra_id_workspace_endpoints", return_value=mock_endpoints
        )

        # Mock ClientCredentials
        mock_token = oauth.Token(
            access_token="test-azure-token", token_type="Bearer", expiry=datetime.now() + timedelta(hours=1)
        )
        mock_token_source = Mock()
        mock_token_source.token.return_value = mock_token
        mocker.patch("databricks.sdk.credentials_provider.oauth.ClientCredentials", return_value=mock_token_source)

        # Should work now without is_azure check
        provider = credentials_provider.github_oidc_azure(mock_cfg)
        assert provider is not None

        headers = provider()
        assert "Authorization" in headers
        assert headers["Authorization"] == "Bearer test-azure-token"
        # Verify tenant ID was auto-detected
        assert mock_cfg.azure_tenant_id == "test-tenant-id"

    def test_azure_cli_requires_effective_azure_login_app_id(self, mocker):
        """Test that azure_cli now requires effective_azure_login_app_id instead of is_azure."""
        # Mock Config with cloud-agnostic host
        mock_cfg = Mock()
        mock_cfg.host = "https://api.databricks.com"  # Cloud-agnostic host
        mock_cfg.azure_tenant_id = "test-tenant-id"
        mock_cfg.azure_workspace_resource_id = None
        mock_cfg.effective_azure_login_app_id = "2ff814a6-3304-4ab8-85cb-cd0e6f879c1d"

        # Mock load_azure_tenant_id
        mock_cfg.load_azure_tenant_id = Mock()

        # Mock AzureCliTokenSource
        mock_token = oauth.Token(
            access_token="test-az-cli-token", token_type="Bearer", expiry=datetime.now() + timedelta(hours=1)
        )
        mock_token.jwt_claims = Mock(return_value={"upn": "user@example.com"})

        mock_token_source = Mock()
        mock_token_source.token.return_value = mock_token
        mock_token_source.is_human_user.return_value = True

        mocker.patch(
            "databricks.sdk.credentials_provider.AzureCliTokenSource.for_resource", return_value=mock_token_source
        )
        mocker.patch("databricks.sdk.credentials_provider.azure.add_workspace_id_header")

        # Should work with effective_azure_login_app_id set
        provider = credentials_provider.azure_cli(mock_cfg)
        assert provider is not None

        headers = provider()
        assert "Authorization" in headers
        assert headers["Authorization"] == "Bearer test-az-cli-token"

    def test_azure_cli_returns_none_without_effective_azure_login_app_id(self):
        """Test that azure_cli returns None when effective_azure_login_app_id is not set."""
        # Mock Config without effective_azure_login_app_id
        mock_cfg = Mock()
        mock_cfg.host = "https://api.databricks.com"
        mock_cfg.effective_azure_login_app_id = None  # Not set

        # Should return None due to missing requirement
        provider = credentials_provider.azure_cli(mock_cfg)
        assert provider is None
