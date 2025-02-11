from unittest.mock import Mock

from databricks.sdk.credentials_provider import external_browser


def test_external_browser_refresh_success(mocker):
    """Tests successful refresh of existing credentials."""

    # Mock Config.
    mock_cfg = Mock()
    mock_cfg.auth_type = 'external-browser'
    mock_cfg.host = 'test-host'
    mock_cfg.oidc_endpoints = {'token_endpoint': 'test-token-endpoint'}
    mock_cfg.client_id = 'test-client-id' # Or use azure_client_id
    mock_cfg.client_secret = 'test-client-secret' # Or use azure_client_secret

    # Mock TokenCache.
    mock_token_cache = Mock()
    mock_session_credentials = Mock()
    mock_session_credentials.token.return_value = "valid_token" # Simulate successful refresh
    mock_token_cache.load.return_value = mock_session_credentials

    # Mock SessionCredentials.
    want_credentials_provider = lambda c: "new_credentials"
    mock_session_credentials.return_value = want_credentials_provider

    # Inject the mock implementations.
    mocker.patch('databricks.sdk.credentials_provider.TokenCache', return_value=mock_token_cache)

    got_credentials_provider = external_browser(mock_cfg)

    mock_token_cache.load.assert_called_once()
    mock_session_credentials.token.assert_called_once() # Verify token refresh was attempted
    assert got_credentials_provider == want_credentials_provider


def test_external_browser_refresh_failure_new_oauth_flow(mocker):
    """Tests failed refresh, triggering a new OAuth flow."""

    # Mock Config.
    mock_cfg = Mock()
    mock_cfg.auth_type = 'external-browser'
    mock_cfg.host = 'test-host'
    mock_cfg.oidc_endpoints = {'token_endpoint': 'test-token-endpoint'}
    mock_cfg.client_id = 'test-client-id'
    mock_cfg.client_secret = 'test-client-secret'

    # Mock TokenCache.
    mock_token_cache = Mock()
    mock_session_credentials = Mock()
    mock_session_credentials.token.side_effect = Exception(
        "Simulated refresh error") # Simulate a failed refresh
    mock_token_cache.load.return_value = mock_session_credentials

    # Mock SessionCredentials.
    want_credentials_provider = lambda c: "new_credentials"
    mock_session_credentials.return_value = want_credentials_provider

    # Mock OAuthClient.
    mock_oauth_client = Mock()
    mock_consent = Mock()
    mock_consent.launch_external_browser.return_value = mock_session_credentials
    mock_oauth_client.initiate_consent.return_value = mock_consent

    # Inject the mock implementations.
    mocker.patch('databricks.sdk.credentials_provider.TokenCache', return_value=mock_token_cache)
    mocker.patch('databricks.sdk.credentials_provider.OAuthClient', return_value=mock_oauth_client)

    got_credentials_provider = external_browser(mock_cfg)

    mock_token_cache.load.assert_called_once()
    mock_session_credentials.token.assert_called_once() # Refresh attempt
    mock_oauth_client.initiate_consent.assert_called_once()
    mock_consent.launch_external_browser.assert_called_once()
    mock_token_cache.save.assert_called_once_with(mock_session_credentials)
    assert got_credentials_provider == want_credentials_provider


def test_external_browser_no_cached_credentials(mocker):
    """Tests the case where there are no cached credentials, initiating a new OAuth flow."""

    # Mock Config.
    mock_cfg = Mock()
    mock_cfg.auth_type = 'external-browser'
    mock_cfg.host = 'test-host'
    mock_cfg.oidc_endpoints = {'token_endpoint': 'test-token-endpoint'}
    mock_cfg.client_id = 'test-client-id'
    mock_cfg.client_secret = 'test-client-secret'

    # Mock TokenCache.
    mock_token_cache = Mock()
    mock_token_cache.load.return_value = None # No cached credentials

    # Mock SessionCredentials.
    mock_session_credentials = Mock()
    want_credentials_provider = lambda c: "new_credentials"
    mock_session_credentials.return_value = want_credentials_provider

    # Mock OAuthClient.
    mock_consent = Mock()
    mock_consent.launch_external_browser.return_value = mock_session_credentials
    mock_oauth_client = Mock()
    mock_oauth_client.initiate_consent.return_value = mock_consent

    # Inject the mock implementations.
    mocker.patch('databricks.sdk.credentials_provider.TokenCache', return_value=mock_token_cache)
    mocker.patch('databricks.sdk.credentials_provider.OAuthClient', return_value=mock_oauth_client)

    got_credentials_provider = external_browser(mock_cfg)

    mock_token_cache.load.assert_called_once()
    mock_oauth_client.initiate_consent.assert_called_once()
    mock_consent.launch_external_browser.assert_called_once()
    mock_token_cache.save.assert_called_once_with(mock_session_credentials)
    assert got_credentials_provider == want_credentials_provider


def test_external_browser_consent_fails(mocker):
    """Tests the case where OAuth consent initiation fails."""

    # Mock Config.
    mock_cfg = Mock()
    mock_cfg.auth_type = 'external-browser'
    mock_cfg.host = 'test-host'
    mock_cfg.oidc_endpoints = {'token_endpoint': 'test-token-endpoint'}
    mock_cfg.client_id = 'test-client-id'
    mock_cfg.client_secret = 'test-client-secret'

    # Mock TokenCache.
    mock_token_cache = Mock()
    mock_token_cache.load.return_value = None # No cached credentials

    # Mock OAuthClient.
    mock_oauth_client = Mock()
    mock_oauth_client.initiate_consent.return_value = None # Simulate consent failure

    # Inject the mock implementations.
    mocker.patch('databricks.sdk.credentials_provider.TokenCache', return_value=mock_token_cache)
    mocker.patch('databricks.sdk.credentials_provider.OAuthClient', return_value=mock_oauth_client)

    got_credentials_provider = external_browser(mock_cfg)

    mock_token_cache.load.assert_called_once()
    mock_oauth_client.initiate_consent.assert_called_once()
    assert got_credentials_provider is None
