from datetime import datetime, timedelta
from unittest.mock import Mock
from urllib.parse import parse_qs

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
    mock_cfg.group_id = "group-id"
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
    assert mock_token_cache_class.call_args.kwargs["group_id"] == "group-id"


def test_external_browser_passes_group_to_oauth_client(mocker):
    """Verifies external-browser auth forwards the requested group to its OAuth client."""
    mock_cfg = Mock()
    mock_cfg.auth_type = "external-browser"
    mock_cfg.host = "https://test.databricks.com"
    mock_cfg.group_id = "group-id"
    mock_cfg.profile = None
    mock_cfg.client_id = "client-id"
    mock_cfg.client_secret = None
    mock_cfg.azure_client_id = None
    mock_cfg.get_scopes.return_value = ["all-apis"]
    mock_cfg.disable_oauth_refresh_token = True

    mocker.patch("databricks.sdk.credentials_provider.oauth.TokenCache").return_value.load.return_value = None
    oauth_client_class = mocker.patch("databricks.sdk.credentials_provider.oauth.OAuthClient")
    oauth_client_class.return_value.initiate_consent.return_value = None

    credentials_provider.external_browser(mock_cfg)

    assert oauth_client_class.call_args.kwargs["group_id"] == "group-id"


def test_external_browser_with_azure_entra_rejects_group():
    """Verifies Azure Entra browser auth rejects unsupported group-role requests."""
    cfg = Mock(
        auth_type="external-browser",
        group_id="group-id",
        client_id=None,
        azure_client_id="azure-client-id",
    )

    with pytest.raises(ValueError, match="external-browser with Azure Entra ID"):
        credentials_provider.external_browser(cfg)


def test_external_browser_group_cache_isolation(mocker, monkeypatch, tmp_path):
    """Verifies normal and grouped browser sessions persist in separate cache entries."""
    monkeypatch.setattr(oauth.TokenCache, "BASE_PATH", str(tmp_path))
    oidc_endpoints = oauth.OidcEndpoints(
        "https://test.databricks.com/oidc/v1/authorize",
        "https://test.databricks.com/oidc/v1/token",
    )

    def config(group_id):
        cfg = Mock(
            auth_type="external-browser",
            host="https://test.databricks.com",
            profile=None,
            group_id=group_id,
            client_id="client-id",
            client_secret=None,
            azure_client_id=None,
            disable_oauth_refresh_token=False,
            databricks_oidc_endpoints=oidc_endpoints,
        )
        cfg.get_scopes.return_value = ["all-apis"]
        return cfg

    def oauth_client(**kwargs):
        group_id = kwargs["group_id"] or "normal"
        credentials = oauth.SessionCredentials(
            oauth.Token(
                access_token=f"{group_id}-token",
                token_type="Bearer",
                expiry=datetime.now() + timedelta(hours=1),
            ),
            oidc_endpoints.token_endpoint,
            "client-id",
        )
        consent = Mock()
        consent.launch_external_browser.return_value = credentials
        client = Mock()
        client.initiate_consent.return_value = consent
        return client

    oauth_client_class = mocker.patch(
        "databricks.sdk.credentials_provider.oauth.OAuthClient",
        side_effect=oauth_client,
    )

    for group_id in [None, "group-a", "group-b"]:
        provider = credentials_provider.external_browser(config(group_id))
        assert provider() == {"Authorization": f"Bearer {group_id or 'normal'}-token"}

    assert oauth_client_class.call_count == 3
    assert len(list(tmp_path.iterdir())) == 3

    oauth_client_class.reset_mock()
    for group_id in [None, "group-a", "group-b"]:
        provider = credentials_provider.external_browser(config(group_id))
        assert provider() == {"Authorization": f"Bearer {group_id or 'normal'}-token"}

    oauth_client_class.assert_not_called()


@pytest.mark.parametrize(
    "token_endpoint",
    [
        "https://workspace.cloud.databricks.com/oidc/v1/token",
        "https://accounts.cloud.databricks.com/oidc/accounts/account-id/v1/token",
        "https://db.cloud.databricks.com/oidc/accounts/account-id/v1/token",
    ],
    ids=["workspace", "account", "unified"],
)
def test_oauth_m2m_sends_group(requests_mock, token_endpoint):
    """Verifies M2M sends assume_group to workspace, account, and unified token endpoints."""
    requests_mock.post(
        token_endpoint,
        json={"access_token": "token", "token_type": "Bearer", "expires_in": 3600},
    )
    cfg = Mock(
        group_id="group-id",
        client_id="client-id",
        client_secret="client-secret",
        databricks_oidc_endpoints=oauth.OidcEndpoints("unused", token_endpoint),
        disable_async_token_refresh=True,
        authorization_details=None,
    )
    cfg.get_scopes_as_string.return_value = "all-apis"

    provider = credentials_provider.oauth_service_principal(cfg)
    provider()

    token_form = parse_qs(requests_mock.last_request.text)
    assert token_form["assume_group"] == ["group-id"]


def test_oauth_m2m_without_group_preserves_token_form(requests_mock):
    """Verifies ungrouped M2M requests do not add an assume_group parameter."""
    token_endpoint = "https://workspace.cloud.databricks.com/oidc/v1/token"
    requests_mock.post(
        token_endpoint,
        json={"access_token": "token", "token_type": "Bearer", "expires_in": 3600},
    )
    cfg = Mock(
        group_id=None,
        client_id="client-id",
        client_secret="client-secret",
        databricks_oidc_endpoints=oauth.OidcEndpoints("unused", token_endpoint),
        disable_async_token_refresh=True,
        authorization_details=None,
    )
    cfg.get_scopes_as_string.return_value = "all-apis"

    credentials_provider.oauth_service_principal(cfg)()

    token_form = parse_qs(requests_mock.last_request.text, keep_blank_values=True)
    assert "assume_group" not in token_form


def test_oauth_m2m_group_rejection_does_not_retry_without_group(requests_mock):
    """Verifies a rejected group request is surfaced instead of retried as normal access."""
    token_endpoint = "https://accounts.cloud.databricks.com/oidc/accounts/account-id/v1/token"
    token_request = requests_mock.post(
        token_endpoint,
        status_code=400,
        headers={"Content-Type": "application/json"},
        json={"error": "invalid_request", "error_description": "assume_group is not supported"},
    )
    cfg = Mock(
        group_id="group-id",
        client_id="client-id",
        client_secret="client-secret",
        databricks_oidc_endpoints=oauth.OidcEndpoints("unused", token_endpoint),
        disable_async_token_refresh=True,
        authorization_details=None,
    )
    cfg.get_scopes_as_string.return_value = "all-apis"
    provider = credentials_provider.oauth_service_principal(cfg)

    with pytest.raises(ValueError, match="invalid_request: assume_group is not supported"):
        provider()

    assert token_request.call_count == 1
    assert parse_qs(token_request.last_request.text)["assume_group"] == ["group-id"]


def test_oauth_m2m_reexchange_sends_group(requests_mock):
    """Verifies M2M retains assume_group when an expired token triggers re-exchange."""
    token_endpoint = "https://workspace.cloud.databricks.com/oidc/v1/token"
    token_responses = iter(
        [
            {"access_token": "expired-role-token", "token_type": "Bearer", "expires_in": -1},
            {"access_token": "fresh-role-token", "token_type": "Bearer", "expires_in": 3600},
        ]
    )
    token_request = requests_mock.post(
        token_endpoint,
        json=lambda _request, _context: next(token_responses),
    )
    cfg = Mock(
        group_id="group-id",
        client_id="client-id",
        client_secret="client-secret",
        databricks_oidc_endpoints=oauth.OidcEndpoints("unused", token_endpoint),
        disable_async_token_refresh=True,
        authorization_details=None,
    )
    cfg.get_scopes_as_string.return_value = "all-apis"
    provider = credentials_provider.oauth_service_principal(cfg)

    assert provider() == {"Authorization": "Bearer expired-role-token"}
    assert provider() == {"Authorization": "Bearer fresh-role-token"}

    assert token_request.call_count == 2
    for request in token_request.request_history:
        assert parse_qs(request.text)["assume_group"] == ["group-id"]


def test_oauth_m2m_group_caches_are_isolated_per_provider(requests_mock):
    """Verifies normal and grouped M2M providers cache only their own tokens."""
    token_endpoint = "https://workspace.cloud.databricks.com/oidc/v1/token"

    def issue_token(request, _context):
        group_id = parse_qs(request.text, keep_blank_values=True).get("assume_group", ["normal"])[0]
        return {"access_token": f"{group_id}-token", "token_type": "Bearer", "expires_in": 3600}

    token_request = requests_mock.post(token_endpoint, json=issue_token)
    providers = {}
    for group_id in [None, "group-a", "group-b"]:
        cfg = Mock(
            group_id=group_id,
            client_id="client-id",
            client_secret="client-secret",
            databricks_oidc_endpoints=oauth.OidcEndpoints("unused", token_endpoint),
            disable_async_token_refresh=True,
            authorization_details=None,
        )
        cfg.get_scopes_as_string.return_value = "all-apis"
        providers[group_id] = credentials_provider.oauth_service_principal(cfg)

    for group_id, provider in providers.items():
        expected_headers = {"Authorization": f"Bearer {group_id or 'normal'}-token"}
        assert provider() == expected_headers
        assert provider() == expected_headers

    assert token_request.call_count == 3


def test_oidc_supplier_sends_group(requests_mock):
    """Verifies the shared OIDC credentials provider forwards assume_group."""
    token_endpoint = "https://workspace.cloud.databricks.com/oidc/v1/token"
    requests_mock.post(
        token_endpoint,
        json={"access_token": "token", "token_type": "Bearer", "expires_in": 3600},
    )
    supplier = Mock()
    supplier.get_oidc_token.return_value = "id-token"
    cfg = Mock(
        group_id="group-id",
        token_audience="audience",
        client_id="client-id",
        databricks_oidc_endpoints=oauth.OidcEndpoints("unused", token_endpoint),
        disable_async_token_refresh=True,
        authorization_details=None,
    )
    cfg.get_scopes_as_string.return_value = "all-apis"

    provider = credentials_provider._oidc_credentials_provider(cfg, lambda: supplier, "test OIDC")
    provider()

    token_form = parse_qs(requests_mock.last_request.text)
    assert token_form["assume_group"] == ["group-id"]


@pytest.mark.parametrize(
    "provider",
    [
        credentials_provider.pat_auth,
        credentials_provider.basic_auth,
        credentials_provider.runtime_native_auth,
        credentials_provider.azure_service_principal,
        credentials_provider.github_oidc_azure,
        credentials_provider.google_credentials,
        credentials_provider.google_id,
        credentials_provider.azure_cli,
        credentials_provider.databricks_cli,
        credentials_provider.metadata_service,
        credentials_provider.model_serving_auth,
    ],
    ids=lambda provider: provider.auth_type(),
)
def test_explicit_unsupported_auth_rejects_group(provider):
    """Verifies explicitly selected normal-access strategies reject group-role requests."""
    auth_type = provider.auth_type()
    cfg = Mock(group_id="group-id", auth_type=auth_type)

    with pytest.raises(ValueError, match=f'auth type "{auth_type}" does not support group role assumption'):
        provider(cfg)


def test_default_credentials_skips_unsupported_auth_for_group():
    """Verifies default discovery skips normal-access auth and continues to group-capable auth."""

    @credentials_provider.credentials_strategy("unsupported", [], supports_group=False)
    def unsupported(_):
        return lambda: {"Authorization": "normal"}

    @credentials_provider.credentials_strategy("supported", [], supports_group=True)
    def supported(_):
        return lambda: {"Authorization": "role"}

    strategy = credentials_provider.DefaultCredentials()
    strategy._auth_providers = [unsupported, supported]

    provider = strategy(Mock(group_id="group-id", auth_type=None))

    assert provider() == {"Authorization": "role"}


def test_default_credentials_group_fallback_uses_oauth_m2m_not_pat(requests_mock):
    """Verifies default discovery selects grouped M2M instead of available PAT credentials."""
    token_endpoint = "https://workspace.cloud.databricks.com/oidc/v1/token"
    token_request = requests_mock.post(
        token_endpoint,
        json={"access_token": "role-token", "token_type": "Bearer", "expires_in": 3600},
    )
    cfg = Mock(
        group_id="group-id",
        auth_type=None,
        host="https://workspace.cloud.databricks.com",
        token="normal-pat",
        client_id="client-id",
        client_secret="client-secret",
        databricks_oidc_endpoints=oauth.OidcEndpoints("unused", token_endpoint),
        disable_async_token_refresh=True,
        authorization_details=None,
    )
    cfg.get_scopes_as_string.return_value = "all-apis"
    strategy = credentials_provider.DefaultCredentials()
    strategy._auth_providers = [credentials_provider.pat_auth, credentials_provider.oauth_service_principal]

    provider = strategy(cfg)

    assert provider() == {"Authorization": "Bearer role-token"}
    assert strategy.auth_type() == "oauth-m2m"
    assert parse_qs(token_request.last_request.text)["assume_group"] == ["group-id"]


def test_default_credentials_group_exhaustion_keeps_generic_error():
    """Verifies exhausting default discovery retains its established generic error."""
    cfg = Mock(group_id="group-id", auth_type=None, host=None, scopes=None)

    with pytest.raises(ValueError, match="cannot configure default credentials"):
        credentials_provider.DefaultCredentials()(cfg)


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
        (
            "host with force-refresh",
            _make_cfg(host=_HOST),
            _CV(0, 296, 0),
            [_CLI, "auth", "token", "--host", _HOST, "--force-refresh"],
        ),
        (
            "account host with force-refresh",
            _make_cfg(host=_ACCT_HOST, account_id="acct-123"),
            _CV(0, 296, 0),
            [_CLI, "auth", "token", "--host", _ACCT_HOST, "--account-id", "acct-123", "--force-refresh"],
        ),
        (
            "profile with force-refresh",
            _make_cfg(profile="my-profile", host=_HOST),
            _CV(0, 296, 0),
            [_CLI, "auth", "token", "--profile", "my-profile", "--force-refresh"],
        ),
        (
            "profile supports profile but not force-refresh",
            _make_cfg(profile="my-profile", host=_HOST),
            _CV(0, 207, 1),
            [_CLI, "auth", "token", "--profile", "my-profile"],
        ),
        (
            "profile-only with force-refresh",
            _make_cfg(profile="my-profile"),
            _CV(0, 296, 0),
            [_CLI, "auth", "token", "--profile", "my-profile", "--force-refresh"],
        ),
        (
            "unknown version, host only, no force-refresh",
            _make_cfg(host=_HOST),
            _CV(),
            [_CLI, "auth", "token", "--host", _HOST],
        ),
        (
            "dev-build version, host only, no force-refresh",
            _make_cfg(host=_HOST),
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


def test_build_cli_command_force_refresh_unsupported_logs_warning(caplog):
    import logging

    cfg = _make_cfg(host=_HOST)
    with caplog.at_level(logging.WARNING, logger="databricks.sdk.credentials_provider"):
        credentials_provider.DatabricksCliTokenSource._build_cli_command(_CLI, cfg, _CV(0, 295, 0))
    assert any(
        "does not support --force-refresh" in rec.message and rec.levelname == "WARNING" for rec in caplog.records
    )


@pytest.mark.parametrize(
    "version",
    [
        # Detection failed: we don't actually know the CLI lacks --force-refresh.
        _CV(),
        # Default dev build: no version metadata injected, same story.
        _CV(0, 0, 0),
    ],
)
def test_build_cli_command_unconfirmed_force_refresh_softens_warning(caplog, version):
    import logging

    cfg = _make_cfg(host=_HOST)
    with caplog.at_level(logging.WARNING, logger="databricks.sdk.credentials_provider"):
        credentials_provider.DatabricksCliTokenSource._build_cli_command(_CLI, cfg, version)
    # Softer phrasing for states where --force-refresh support wasn't proven absent.
    assert any(
        "Could not confirm --force-refresh support" in rec.message and rec.levelname == "WARNING"
        for rec in caplog.records
    )
    assert not any("does not support --force-refresh" in rec.message for rec in caplog.records)


def test_build_cli_command_force_refresh_supported_no_warning(caplog):
    import logging

    cfg = _make_cfg(host=_HOST)
    with caplog.at_level(logging.WARNING, logger="databricks.sdk.credentials_provider"):
        credentials_provider.DatabricksCliTokenSource._build_cli_command(_CLI, cfg, _CV(0, 296, 0))
    # No --force-refresh-related warning when the flag is supported.
    assert not any("--force-refresh" in rec.message for rec in caplog.records)


def test_resolve_cli_command_malformed_version_json_falls_back(mocker, caplog):
    # Pin the integrated path: `databricks version --output json` succeeds but
    # emits unparseable JSON. _parse_cli_version returns CliVersion() with only
    # DEBUG logging, _resolve_cli_command falls back to --host, and no WARNING
    # about --profile fires because the unknown sentinel takes the softened branch.
    import logging

    _stub_version_output(mocker, "{not valid json")
    cfg = _make_cfg(profile="my-profile", host=_HOST)
    with caplog.at_level(logging.DEBUG, logger="databricks.sdk.credentials_provider"):
        cmd = credentials_provider.DatabricksCliTokenSource._resolve_cli_command(_CLI, cfg)
    assert cmd == [_CLI, "auth", "token", "--host", _HOST]
    assert any(
        "Failed to parse Databricks CLI version" in rec.message and rec.levelname == "DEBUG" for rec in caplog.records
    )
    assert not any("does not support --profile" in rec.message for rec in caplog.records)


# Tests for cloud-agnostic hosts and removed cloud checks
class TestCloudAgnosticHosts:
    """Tests that credential providers work with cloud-agnostic hosts after removing is_azure/is_gcp checks."""

    def test_azure_service_principal_with_cloud_agnostic_host(self, mocker):
        """Test that azure_service_principal works with cloud-agnostic hosts after removing is_azure requirement."""
        # Mock Config with cloud-agnostic host
        mock_cfg = Mock(group_id=None)
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
        mock_cfg = Mock(group_id=None)
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
        mock_cfg = Mock(group_id=None)
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
        mock_cfg = Mock(group_id=None)
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
        mock_cfg = Mock(group_id=None)
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
        mock_cfg = Mock(group_id=None)
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
        mock_cfg = Mock(group_id=None)
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
        mock_cfg = Mock(group_id=None)
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
        mock_cfg = Mock(group_id=None)
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
        mock_cfg = Mock(group_id=None)
        mock_cfg.host = "https://api.databricks.com"
        mock_cfg.effective_azure_login_app_id = None  # Not set

        # Should return None due to missing requirement
        provider = credentials_provider.azure_cli(mock_cfg)
        assert provider is None
