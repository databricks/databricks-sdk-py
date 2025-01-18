import pytest

from unittest.mock import Mock
from databricks.sdk.credentials_provider import external_browser

def test_external_browser_refresh_success(mocker):
    """Tests successful refresh of existing credentials."""

    # 1. Mock Config
    mock_cfg = Mock()
    mock_cfg.auth_type = 'external-browser'
    mock_cfg.host = 'test-host'
    mock_cfg.oidc_endpoints = {'token_endpoint': 'test-token-endpoint'}
    mock_cfg.client_id = 'test-client-id'  # Or use azure_client_id
    mock_cfg.client_secret = 'test-client-secret'  # Or use azure_client_secret

    # 2. Mock TokenCache
    mock_token_cache = Mock()
    mock_session_credentials = Mock()
    mock_session_credentials.token.return_value = "valid_token"  # Simulate successful refresh
    mock_token_cache.load.return_value = mock_session_credentials

    mock_credentials_provider = Mock()
    mock_session_credentials.return_value = mock_credentials_provider

    # 3. Patch TokenCache (no need to mock OAuthClient in this case)
    mocker.patch('databricks.sdk.credentials_provider.TokenCache', return_value=mock_token_cache)

    # 4. Call the function
    result = external_browser(mock_cfg)

    # 5. Assertions
    mock_token_cache.load.assert_called_once()
    mock_session_credentials.token.assert_called_once()  # Verify token refresh was attempted
    assert result == mock_credentials_provider


def test_external_browser_refresh_failure_new_oauth_flow(mocker):
    """Tests failed refresh, triggering a new OAuth flow."""

    # 1. Mock Config
    mock_cfg = Mock()
    mock_cfg.auth_type = 'external-browser'
    mock_cfg.host = 'test-host'
    mock_cfg.oidc_endpoints = {'token_endpoint': 'test-token-endpoint'}
    mock_cfg.client_id = 'test-client-id'
    mock_cfg.client_secret = 'test-client-secret'

    # 2. Mock TokenCache
    mock_token_cache = Mock()
    mock_session_credentials = Mock()
    mock_session_credentials.token.side_effect = Exception("Simulated refresh error")  # Simulate a failed refresh
    mock_token_cache.load.return_value = mock_session_credentials

    mock_credentials_provider = Mock()
    mock_session_credentials.return_value = mock_credentials_provider

    # 3. Mock OAuthClient
    mock_oauth_client = Mock()
    mock_consent = Mock()
    mock_consent.launch_external_browser.return_value = mock_session_credentials  # Simulate successful OAuth flow
    mock_oauth_client.initiate_consent.return_value = mock_consent

    # 4. Patch TokenCache and OAuthClient
    mocker.patch('databricks.sdk.credentials_provider.TokenCache', return_value=mock_token_cache)
    mocker.patch('databricks.sdk.credentials_provider.OAuthClient', return_value=mock_oauth_client)

    # 5. Call the function
    result = external_browser(mock_cfg)

    # 6. Assertions
    mock_token_cache.load.assert_called_once()
    mock_session_credentials.token.assert_called_once()  # Refresh attempt
    mock_oauth_client.initiate_consent.assert_called_once()
    mock_consent.launch_external_browser.assert_called_once()
    mock_token_cache.save.assert_called_once_with(mock_session_credentials)
    assert result == mock_credentials_provider


def test_external_browser_no_cached_credentials(mocker):
    """Tests the case where there are no cached credentials, initiating a new OAuth flow."""

    # 1. Mock Config
    mock_cfg = Mock()
    mock_cfg.auth_type = 'external-browser'
    mock_cfg.host = 'test-host'
    mock_cfg.oidc_endpoints = {'token_endpoint': 'test-token-endpoint'}
    mock_cfg.client_id = 'test-client-id'
    mock_cfg.client_secret = 'test-client-secret'

    # 2. Mock TokenCache
    mock_token_cache = Mock()
    mock_token_cache.load.return_value = None  # No cached credentials

    mock_session_credentials = lambda c: "new_credentials"

    # 3. Mock OAuthClient
    mock_consent = Mock()
    mock_consent.launch_external_browser.return_value = mock_session_credentials
    mock_oauth_client = Mock()
    mock_oauth_client.initiate_consent.return_value = mock_consent

    # 4. Patch TokenCache and OAuthClient
    mocker.patch('databricks.sdk.credentials_provider.TokenCache', return_value=mock_token_cache)
    mocker.patch('databricks.sdk.credentials_provider.OAuthClient', return_value=mock_oauth_client)

    # 5. Call the function
    result = external_browser(mock_cfg)

    # 6. Assertions
    mock_token_cache.load.assert_called_once()
    mock_oauth_client.initiate_consent.assert_called_once()
    mock_consent.launch_external_browser.assert_called_once()
    mock_token_cache.save.assert_called_once_with(mock_session_credentials)
    assert result == "new_credentials"


def test_external_browser_consent_fails(mocker):
    """Tests the case where OAuth consent initiation fails."""

    # 1. Mock Config
    mock_cfg = Mock()
    mock_cfg.auth_type = 'external-browser'
    mock_cfg.host = 'test-host'
    mock_cfg.oidc_endpoints = {'token_endpoint': 'test-token-endpoint'}
    mock_cfg.client_id = 'test-client-id'
    mock_cfg.client_secret = 'test-client-secret'

    # 2. Mock TokenCache
    mock_token_cache = Mock()
    mock_token_cache.load.return_value = None  # No cached credentials

    # 3. Mock OAuthClient
    mock_oauth_client = Mock()
    mock_oauth_client.initiate_consent.return_value = None  # Simulate consent failure

    # 4. Patch TokenCache and OAuthClient
    mocker.patch('databricks.sdk.credentials_provider.TokenCache', return_value=mock_token_cache)
    mocker.patch('databricks.sdk.credentials_provider.OAuthClient', return_value=mock_oauth_client)

    # 5. Call the function
    result = external_browser(mock_cfg)

    # 6. Assertions
    mock_token_cache.load.assert_called_once()
    mock_oauth_client.initiate_consent.assert_called_once()
    assert result is None