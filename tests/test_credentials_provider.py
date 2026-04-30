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


def test_external_browser_passes_profile_to_token_cache(mocker):
    """Tests that external_browser passes cfg.profile to TokenCache."""
    mock_cfg = Mock()
    mock_cfg.auth_type = "external-browser"
    mock_cfg.host = "https://test.databricks.com"
    mock_cfg.profile = "myprofile"
    mock_cfg.client_id = "test-client-id"
    mock_cfg.client_secret = None
    mock_cfg.azure_client_id = None
    mock_cfg.get_scopes.return_value = ["all-apis"]
    mock_cfg.disable_oauth_refresh_token = False

    mock_token_cache_class = mocker.patch("databricks.sdk.credentials_provider.oauth.TokenCache")
    mock_token_cache = Mock()
    mock_token_cache.load.return_value = None
    mock_token_cache_class.return_value = mock_token_cache

    mock_oauth_client = Mock()
    mock_consent = Mock()
    mock_consent.launch_external_browser.return_value = Mock()
    mock_oauth_client.initiate_consent.return_value = mock_consent
    mocker.patch("databricks.sdk.credentials_provider.oauth.OAuthClient", return_value=mock_oauth_client)

    credentials_provider.external_browser(mock_cfg)

    assert mock_token_cache_class.call_args.kwargs["profile"] == "myprofile"


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


_CV = credentials_provider.CliVersion


@pytest.fixture(autouse=True)
def _clear_cli_version_cache():
    # `_probe_cli_version` is `@lru_cache`-decorated, so a value cached by one
    # test would leak into the next. Clear before every test.
    credentials_provider.DatabricksCliTokenSource._probe_cli_version.cache_clear()


@pytest.mark.parametrize(
    "output,expected",
    [
        # Stable releases.
        ('{"Major": 0, "Minor": 207, "Patch": 1}', _CV(0, 207, 1)),
        ('{"Major": 0, "Minor": 296, "Patch": 0}', _CV(0, 296, 0)),
        ('{"Major": 1, "Minor": 2, "Patch": 3}', _CV(1, 2, 3)),
        # RC release — we intentionally ignore the prerelease tag;
        # the base triple alone is what we gate features on.
        ('{"Major": 0, "Minor": 296, "Patch": 0, "Prerelease": "rc.1"}', _CV(0, 296, 0)),
        # Nightly snapshot.
        ('{"Major": 0, "Minor": 295, "Patch": 1, "Prerelease": "dev"}', _CV(0, 295, 1)),
        # Default dev build: numeric fields stay at their "0" defaults when
        # the CLI is built without version metadata. (0, 0, 0) is the sentinel.
        ('{"Major": 0, "Minor": 0, "Patch": 0}', _CV(0, 0, 0)),
        # User-chosen dev version (intentional — treated as v1.0.0).
        ('{"Major": 1, "Minor": 0, "Patch": 0, "Prerelease": "dev"}', _CV(1, 0, 0)),
        # Full real-world payload with the additional fields the CLI emits.
        (
            '{"ProjectName":"cli","Version":"0.295.0","Branch":"HEAD","Tag":"v0.295.0",'
            '"Major":0,"Minor":295,"Patch":0,"Prerelease":"","IsSnapshot":false}',
            _CV(0, 295, 0),
        ),
        # Failure cases — all fall back to the unknown CliVersion() (-1,-1,-1).
        ("not json", _CV()),
        ("", _CV()),
        # Old CLIs that don't support --output json emit text — parse fails.
        ("Databricks CLI v0.207.1", _CV()),
        # Missing a numeric field.
        ('{"Minor": 207, "Patch": 1}', _CV()),
        # Wrong type on a numeric field.
        ('{"Major": "oops", "Minor": 207, "Patch": 1}', _CV()),
    ],
)
def test_parse_cli_version(output, expected):
    assert credentials_provider.DatabricksCliTokenSource._parse_cli_version(output) == expected


@pytest.mark.parametrize(
    "a,b,ordering",
    [
        (_CV(0, 207, 1), _CV(0, 207, 1), "=="),
        (_CV(0, 207, 2), _CV(0, 207, 1), ">"),
        (_CV(0, 207, 0), _CV(0, 207, 1), "<"),
        (_CV(0, 208, 0), _CV(0, 207, 1), ">"),
        (_CV(0, 206, 9), _CV(0, 207, 1), "<"),
        (_CV(1, 0, 0), _CV(0, 207, 1), ">"),
        (_CV(0, 999, 0), _CV(1, 0, 0), "<"),
        (_CV(0, 0, 0), _CV(0, 0, 0), "=="),
        (_CV(0, 0, 0), _CV(0, 207, 1), "<"),
        # Unknown (-1, -1, -1) compares less than every real version so all
        # feature gates fail for it.
        (_CV(), _CV(0, 207, 1), "<"),
        (_CV(), _CV(0, 0, 0), "<"),
        (_CV(), _CV(), "=="),
    ],
)
def test_cli_version_total_order(a, b, ordering):
    # Lock in all six operators so a future refactor that replaces
    # @dataclass(order=True) with a custom __lt__ can't introduce
    # asymmetries (e.g. `a > b` True while `b < a` False).
    lt, eq, gt = ordering == "<", ordering == "==", ordering == ">"
    assert (a < b) is lt
    assert (a == b) is eq
    assert (a > b) is gt
    assert (a <= b) is (lt or eq)
    assert (a >= b) is (gt or eq)
    assert (a != b) is not eq


@pytest.mark.parametrize(
    "version,expected",
    [
        # Default dev build: the CLI's "no version injected" sentinel.
        (_CV(0, 0, 0), True),
        # Regular releases.
        (_CV(0, 207, 1), False),
        (_CV(0, 296, 0), False),
        (_CV(1, 0, 0), False),
        # Unknown (detection failure) is distinct from the dev-build sentinel.
        (_CV(), False),
    ],
)
def test_cli_version_is_default_dev_build(version, expected):
    assert version.is_default_dev_build is expected


_CLI = "/path/to/databricks"
_HOST = "https://workspace.databricks.com"
_ACCT_HOST = "https://accounts.cloud.databricks.com"


def _make_cfg(*, profile=None, host=None, account_id=None):
    cfg = Mock()
    cfg.profile = profile
    cfg.host = host
    cfg.account_id = account_id
    cfg.client_type = ClientType.ACCOUNT if (host and "accounts" in host) else ClientType.WORKSPACE
    return cfg


@pytest.mark.parametrize(
    "name,cfg,version,expected",
    [
        ("host only", _make_cfg(host=_HOST), _CV(0, 200, 0), [_CLI, "auth", "token", "--host", _HOST]),
        (
            "account host",
            _make_cfg(host=_ACCT_HOST, account_id="acct-123"),
            _CV(0, 200, 0),
            [_CLI, "auth", "token", "--host", _ACCT_HOST, "--account-id", "acct-123"],
        ),
        (
            "profile with new CLI",
            _make_cfg(profile="my-profile", host=_HOST),
            _CV(0, 207, 1),
            [_CLI, "auth", "token", "--profile", "my-profile"],
        ),
        (
            "profile with old CLI falls back to host",
            _make_cfg(profile="my-profile", host=_HOST),
            _CV(0, 200, 0),
            [_CLI, "auth", "token", "--host", _HOST],
        ),
        (
            "unknown version falls back to host",
            _make_cfg(profile="my-profile", host=_HOST),
            _CV(),
            [_CLI, "auth", "token", "--host", _HOST],
        ),
        (
            "dev-build version falls back to host",
            _make_cfg(profile="my-profile", host=_HOST),
            _CV(0, 0, 0),
            [_CLI, "auth", "token", "--host", _HOST],
        ),
    ],
)
def test_build_cli_command(name, cfg, version, expected):
    assert credentials_provider.DatabricksCliTokenSource._build_cli_command(_CLI, cfg, version) == expected


@pytest.mark.parametrize(
    "name,cfg,version,match",
    [
        (
            "neither profile nor host",
            _make_cfg(),
            _CV(0, 207, 1),
            r"neither profile nor host is configured",
        ),
        (
            "profile only with old CLI has no host fallback",
            _make_cfg(profile="my-profile"),
            _CV(0, 200, 0),
            r"does not support --profile .* and no host fallback is configured",
        ),
    ],
)
def test_build_cli_command_errors(name, cfg, version, match):
    with pytest.raises(IOError, match=match):
        credentials_provider.DatabricksCliTokenSource._build_cli_command(_CLI, cfg, version)


def test_build_cli_command_old_cli_logs_warning(caplog):
    import logging

    cfg = _make_cfg(profile="my-profile", host=_HOST)
    with caplog.at_level(logging.WARNING, logger="databricks.sdk"):
        credentials_provider.DatabricksCliTokenSource._build_cli_command(_CLI, cfg, _CV(0, 200, 0))
    assert any("does not support --profile" in rec.message and rec.levelname == "WARNING" for rec in caplog.records)


@pytest.mark.parametrize(
    "version",
    [
        # Detection failed: we don't actually know the CLI lacks --profile.
        _CV(),
        # Default dev build: no version metadata injected, same story.
        _CV(0, 0, 0),
    ],
)
def test_build_cli_command_unconfirmed_profile_softens_warning(caplog, version):
    import logging

    cfg = _make_cfg(profile="my-profile", host=_HOST)
    with caplog.at_level(logging.WARNING, logger="databricks.sdk"):
        credentials_provider.DatabricksCliTokenSource._build_cli_command(_CLI, cfg, version)
    # Softer phrasing for states where --profile support wasn't proven absent.
    assert any(
        "Could not confirm --profile support" in rec.message and rec.levelname == "WARNING" for rec in caplog.records
    )
    assert not any("does not support --profile" in rec.message for rec in caplog.records)


def _stub_version_output(mocker, output: str):
    """Mock `_run_subprocess` so `_get_cli_version` returns a controlled version."""
    return mocker.patch(
        "databricks.sdk.credentials_provider._run_subprocess",
        return_value=Mock(stdout=output.encode()),
    )


def test_resolve_cli_command_dev_build_logs_info_and_falls_back(mocker, caplog):
    import logging

    _stub_version_output(
        mocker,
        '{"Version": "0.0.0-dev+abcdef123456", "Major": 0, "Minor": 0, "Patch": 0}',
    )
    cfg = _make_cfg(profile="my-profile", host=_HOST)
    with caplog.at_level(logging.INFO, logger="databricks.sdk.credentials_provider"):
        cmd = credentials_provider.DatabricksCliTokenSource._resolve_cli_command(_CLI, cfg)
    # Dev build reports as zero version, so --profile is disabled and we fall
    # back to --host.
    assert cmd == [_CLI, "auth", "token", "--host", _HOST]
    assert any("development build" in rec.message and rec.levelname == "INFO" for rec in caplog.records)


def test_resolve_cli_command_version_detection_failure_logs_warning(mocker, caplog):
    import logging

    mocker.patch(
        "databricks.sdk.credentials_provider._run_subprocess",
        side_effect=OSError("boom"),
    )
    cfg = _make_cfg(host=_HOST)
    with caplog.at_level(logging.WARNING, logger="databricks.sdk.credentials_provider"):
        cmd = credentials_provider.DatabricksCliTokenSource._resolve_cli_command(_CLI, cfg)
    assert cmd == [_CLI, "auth", "token", "--host", _HOST]
    assert any(
        "Failed to detect Databricks CLI version" in rec.message and rec.levelname == "WARNING"
        for rec in caplog.records
    )


def test_get_cli_version_does_not_cache_subprocess_failures(mocker):
    # Regression: a transient subprocess failure (timeout, OSError) must not
    # be cached. Otherwise a one-off blip pins every later DatabricksCliTokenSource
    # to the conservative fallback for the rest of the process lifetime.
    mock_run = mocker.patch(
        "databricks.sdk.credentials_provider._run_subprocess",
        side_effect=[
            OSError("transient"),
            Mock(stdout=b'{"Major": 0, "Minor": 207, "Patch": 1}'),
        ],
    )
    assert credentials_provider.DatabricksCliTokenSource._get_cli_version(_CLI) == _CV()
    assert credentials_provider.DatabricksCliTokenSource._get_cli_version(_CLI) == _CV(0, 207, 1)
    assert mock_run.call_count == 2


def test_resolve_cli_command_wraps_missing_config_error(mocker):
    _stub_version_output(
        mocker,
        '{"Version": "0.207.1", "Major": 0, "Minor": 207, "Patch": 1}',
    )
    cfg = _make_cfg()
    with pytest.raises(
        IOError,
        match=r"cannot configure CLI token source: neither profile nor host is configured",
    ):
        credentials_provider.DatabricksCliTokenSource._resolve_cli_command(_CLI, cfg)


def test_resolve_cli_command_new_cli_uses_profile(mocker):
    # Happy path: post-v0.207.1 CLI + profile+host cfg produces a --profile
    # command. Exercises the primary code path this PR enables end-to-end.
    _stub_version_output(
        mocker,
        '{"Version": "0.207.1", "Major": 0, "Minor": 207, "Patch": 1}',
    )
    cfg = _make_cfg(profile="my-profile", host=_HOST)
    cmd = credentials_provider.DatabricksCliTokenSource._resolve_cli_command(_CLI, cfg)
    assert cmd == [_CLI, "auth", "token", "--profile", "my-profile"]


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

    def test_google_credentials_includes_sa_token_on_success(self, mocker):
        """Test that google_credentials includes GCP SA access token when refresh succeeds."""
        mock_cfg = Mock()
        mock_cfg.host = "https://api.databricks.com"
        mock_cfg.google_credentials = '{"type": "service_account", "project_id": "test"}'
        mock_cfg.disable_async_token_refresh = True

        mock_id_credentials = Mock()
        mock_id_credentials.token = "test-id-token"

        mock_sa_credentials = Mock()
        mock_sa_credentials.token = "test-sa-token"

        mocker.patch(
            "databricks.sdk.credentials_provider.service_account.IDTokenCredentials.from_service_account_info",
            return_value=mock_id_credentials,
        )
        mocker.patch(
            "databricks.sdk.credentials_provider.service_account.Credentials.from_service_account_info",
            return_value=mock_sa_credentials,
        )

        provider = credentials_provider.google_credentials(mock_cfg)
        headers = provider()
        assert headers["Authorization"] == "Bearer test-id-token"
        assert headers["X-Databricks-GCP-SA-Access-Token"] == "test-sa-token"

    def test_google_credentials_warns_on_sa_token_failure(self, mocker):
        """Test that google_credentials logs warning and omits SA token when refresh fails."""
        mock_cfg = Mock()
        mock_cfg.host = "https://api.databricks.com"
        mock_cfg.google_credentials = '{"type": "service_account", "project_id": "test"}'
        mock_cfg.disable_async_token_refresh = True

        mock_id_credentials = Mock()
        mock_id_credentials.token = "test-id-token"

        mock_sa_credentials = Mock()
        mock_sa_credentials.refresh.side_effect = Exception("permission denied")

        mocker.patch(
            "databricks.sdk.credentials_provider.service_account.IDTokenCredentials.from_service_account_info",
            return_value=mock_id_credentials,
        )
        mocker.patch(
            "databricks.sdk.credentials_provider.service_account.Credentials.from_service_account_info",
            return_value=mock_sa_credentials,
        )

        provider = credentials_provider.google_credentials(mock_cfg)
        mock_logger = mocker.patch("databricks.sdk.credentials_provider.logger")
        headers = provider()

        assert headers["Authorization"] == "Bearer test-id-token"
        assert "X-Databricks-GCP-SA-Access-Token" not in headers
        mock_logger.warning.assert_called_once()

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

    def test_google_id_includes_sa_token_on_success(self, mocker):
        """Test that google_id includes GCP SA access token when refresh succeeds."""
        mock_cfg = Mock()
        mock_cfg.host = "https://api.databricks.com"
        mock_cfg.google_service_account = "test-sa@project.iam.gserviceaccount.com"

        mock_source_credentials = Mock()
        mocker.patch(
            "databricks.sdk.credentials_provider.google.auth.default",
            return_value=(mock_source_credentials, "test-project"),
        )

        mock_id_creds = Mock()
        mock_id_creds.token = "test-google-id-token"

        mock_gcp_creds = Mock()
        mock_gcp_creds.token = "test-gcp-sa-token"

        mocker.patch(
            "databricks.sdk.credentials_provider.impersonated_credentials.Credentials",
            return_value=mock_gcp_creds,
        )
        mocker.patch(
            "databricks.sdk.credentials_provider.impersonated_credentials.IDTokenCredentials",
            return_value=mock_id_creds,
        )

        provider = credentials_provider.google_id(mock_cfg)
        headers = provider()
        assert headers["Authorization"] == "Bearer test-google-id-token"
        assert headers["X-Databricks-GCP-SA-Access-Token"] == "test-gcp-sa-token"

    def test_google_id_warns_on_sa_token_failure(self, mocker):
        """Test that google_id logs warning and omits SA token when refresh fails."""
        mock_cfg = Mock()
        mock_cfg.host = "https://api.databricks.com"
        mock_cfg.google_service_account = "test-sa@project.iam.gserviceaccount.com"

        mock_source_credentials = Mock()
        mocker.patch(
            "databricks.sdk.credentials_provider.google.auth.default",
            return_value=(mock_source_credentials, "test-project"),
        )

        mock_id_creds = Mock()
        mock_id_creds.token = "test-google-id-token"

        mock_gcp_creds = Mock()
        mock_gcp_creds.refresh.side_effect = Exception("permission denied")

        mocker.patch(
            "databricks.sdk.credentials_provider.impersonated_credentials.Credentials",
            return_value=mock_gcp_creds,
        )
        mocker.patch(
            "databricks.sdk.credentials_provider.impersonated_credentials.IDTokenCredentials",
            return_value=mock_id_creds,
        )

        provider = credentials_provider.google_id(mock_cfg)
        mock_logger = mocker.patch("databricks.sdk.credentials_provider.logger")
        headers = provider()

        assert headers["Authorization"] == "Bearer test-google-id-token"
        assert "X-Databricks-GCP-SA-Access-Token" not in headers
        mock_logger.warning.assert_called_once()

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
