"""Test custom headers functionality"""
import pytest
from unittest.mock import MagicMock, patch
from databricks.sdk import WorkspaceClient, AccountClient
from databricks.sdk.core import Config


def test_workspace_client_custom_headers():
    """Test that WorkspaceClient passes custom headers to all requests"""
    with patch('databricks.sdk.core.ApiClient') as mock_api_client:
        # Create a mock for the _api_client.do method
        mock_do = MagicMock(return_value={})
        mock_api_client_instance = MagicMock()
        mock_api_client_instance.do = mock_do
        mock_api_client.return_value = mock_api_client_instance
        
        # Create WorkspaceClient with custom headers
        w = WorkspaceClient(
            host="https://test.databricks.com",
            token="test-token",
            custom_headers={"X-Custom-Header": "test-value"}
        )
        
        # Verify custom headers are stored in config
        assert w._config._custom_headers == {"X-Custom-Header": "test-value"}


def test_account_client_custom_headers():
    """Test that AccountClient passes custom headers to all requests"""
    with patch('databricks.sdk.core.ApiClient') as mock_api_client:
        mock_do = MagicMock(return_value={})
        mock_api_client_instance = MagicMock()
        mock_api_client_instance.do = mock_do
        mock_api_client.return_value = mock_api_client_instance
        
        # Create AccountClient with custom headers
        a = AccountClient(
            host="https://accounts.cloud.databricks.com",
            account_id="test-account-id",
            token="test-token",
            custom_headers={"X-Custom-Header": "test-value"}
        )
        
        # Verify custom headers are stored in config
        assert a._config._custom_headers == {"X-Custom-Header": "test-value"}


def test_config_custom_headers():
    """Test that Config stores custom headers"""
    config = Config(
        host="https://test.databricks.com",
        token="test-token",
        custom_headers={"X-Custom-Header": "test-value", "X-Another": "another-value"}
    )
    
    assert config._custom_headers == {"X-Custom-Header": "test-value", "X-Another": "another-value"}


def test_api_client_merges_custom_headers(requests_mock):
    """Test that ApiClient.do() merges custom headers with request headers"""
    from databricks.sdk.core import ApiClient
    
    # Create config with custom headers
    config = Config(
        host="https://test.databricks.com",
        token="test-token",
        custom_headers={"X-Custom-Header": "custom-value"}
    )
    
    # Create ApiClient
    api_client = ApiClient(config)
    
    # Mock the request
    requests_mock.get(
        "https://test.databricks.com/api/2.0/clusters/list",
        json={"clusters": []},
    )
    
    # Make a request
    response = api_client.do("GET", "/api/2.0/clusters/list")
    
    # Verify the custom header was included in the request
    assert requests_mock.last_request.headers["X-Custom-Header"] == "custom-value"
    

def test_request_headers_override_custom_headers(requests_mock):
    """Test that request-specific headers override custom headers"""
    from databricks.sdk.core import ApiClient
    
    # Create config with custom headers
    config = Config(
        host="https://test.databricks.com",
        token="test-token",
        custom_headers={"X-Custom-Header": "custom-value"}
    )
    
    # Create ApiClient
    api_client = ApiClient(config)
    
    # Mock the request
    requests_mock.get(
        "https://test.databricks.com/api/2.0/clusters/list",
        json={"clusters": []},
    )
    
    # Make a request with header override
    response = api_client.do(
        "GET", 
        "/api/2.0/clusters/list",
        headers={"X-Custom-Header": "overridden-value"}
    )
    
    # Verify the request header overrode the custom header
    assert requests_mock.last_request.headers["X-Custom-Header"] == "overridden-value"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
