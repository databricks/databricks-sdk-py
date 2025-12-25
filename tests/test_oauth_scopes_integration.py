"""Integration tests for OAuth scopes support.

These tests verify that scopes correctly flow through to token endpoints
across all OAuth authentication methods (M2M, U2M, WIF/OIDC).
"""

from typing import Optional
from urllib.parse import parse_qs

import pytest

from databricks.sdk.config import Config

# --- Helper Functions ---


def get_scope_from_request(request_text: str) -> Optional[str]:
    """Extract and return the scope value from a URL-encoded request body."""
    params = parse_qs(request_text)
    scope_list = params.get("scope")
    return scope_list[0] if scope_list else None


def get_grant_type_from_request(request_text: str) -> Optional[str]:
    """Extract and return the grant_type value from a URL-encoded request body."""
    params = parse_qs(request_text)
    grant_type_list = params.get("grant_type")
    return grant_type_list[0] if grant_type_list else None


# --- M2M (Machine-to-Machine) Integration Tests ---


@pytest.mark.parametrize(
    "scopes_input,expected_scope",
    [
        (None, "all-apis"),
        ("unity-catalog:read", "unity-catalog:read"),
        ("jobs:read, clusters, mlflow:read", "clusters jobs:read mlflow:read"),
    ],
    ids=[
        "default_scope",
        "single_custom_scope",
        "multiple_scopes_sorted",
    ],
)
def test_m2m_scopes(requests_mock, scopes_input, expected_scope):
    """Test M2M authentication sends correct scopes to token endpoint."""
    # Mock the well-known endpoint
    requests_mock.get(
        "https://test.databricks.com/oidc/.well-known/oauth-authorization-server",
        json={
            "authorization_endpoint": "https://test.databricks.com/oidc/v1/authorize",
            "token_endpoint": "https://test.databricks.com/oidc/v1/token",
        },
    )

    # Mock the token endpoint
    token_mock = requests_mock.post(
        "https://test.databricks.com/oidc/v1/token",
        json={"access_token": "test-token", "token_type": "Bearer", "expires_in": 3600},
    )

    # Create config with M2M auth
    config = Config(
        host="https://test.databricks.com",
        client_id="test-client-id",
        client_secret="test-client-secret",
        auth_type="oauth-m2m",
        scopes=scopes_input,
    )

    # Authenticate (triggers token request)
    headers = config.authenticate()

    # Verify scope was sent correctly
    assert token_mock.called
    assert get_scope_from_request(token_mock.last_request.text) == expected_scope
    assert headers["Authorization"] == "Bearer test-token"


# --- WIF/OIDC Integration Tests ---


@pytest.mark.parametrize(
    "scopes_input,expected_scope",
    [
        (None, "all-apis"),
        ("unity-catalog:read, clusters", "clusters unity-catalog:read"),
        ("jobs:read", "jobs:read"),
    ],
    ids=[
        "default_scope",
        "multiple_scopes",
        "single_scope",
    ],
)
def test_oidc_scopes(requests_mock, tmp_path, scopes_input, expected_scope):
    """Test OIDC token exchange sends correct scopes to token endpoint."""
    # Create a temporary OIDC token file
    oidc_token_file = tmp_path / "oidc_token"
    oidc_token_file.write_text("mock-id-token")

    # Mock the well-known endpoint
    requests_mock.get(
        "https://test.databricks.com/oidc/.well-known/oauth-authorization-server",
        json={
            "authorization_endpoint": "https://test.databricks.com/oidc/v1/authorize",
            "token_endpoint": "https://test.databricks.com/oidc/v1/token",
        },
    )

    # Mock the token exchange endpoint
    token_mock = requests_mock.post(
        "https://test.databricks.com/oidc/v1/token",
        json={"access_token": "test-token", "token_type": "Bearer", "expires_in": 3600},
    )

    # Create config with OIDC auth
    config = Config(
        host="https://test.databricks.com",
        oidc_token_filepath=str(oidc_token_file),
        auth_type="file-oidc",
        scopes=scopes_input,
    )

    # Authenticate (triggers token exchange)
    headers = config.authenticate()

    # Verify scope and grant_type were sent correctly
    assert token_mock.called
    assert get_scope_from_request(token_mock.last_request.text) == expected_scope
    assert (
        get_grant_type_from_request(token_mock.last_request.text) == "urn:ietf:params:oauth:grant-type:token-exchange"
    )
    assert headers["Authorization"] == "Bearer test-token"
