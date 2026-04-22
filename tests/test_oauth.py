from unittest.mock import MagicMock, patch

import pytest

from databricks.sdk import oauth as oauth_module
from databricks.sdk._base_client import _BaseClient
from databricks.sdk.oauth import (HostMetadata, OidcEndpoints,
                                  PATOAuthTokenExchange, TokenCache,
                                  get_account_endpoints,
                                  get_azure_entra_id_workspace_endpoints,
                                  get_endpoints_from_url, get_host_metadata,
                                  get_workspace_endpoints, retrieve_token)

from .clock import FakeClock


def test_token_cache_unique_filename_by_host():
    common_args = dict(
        client_id="abc",
        redirect_url="http://localhost:8020",
        oidc_endpoints=OidcEndpoints("http://localhost:1234", "http://localhost:1234"),
    )
    assert (
        TokenCache(host="http://localhost:", **common_args).filename
        != TokenCache("https://bar.cloud.databricks.com", **common_args).filename
    )


def test_token_cache_unique_filename_by_client_id():
    common_args = dict(
        host="http://localhost:",
        redirect_url="http://localhost:8020",
        oidc_endpoints=OidcEndpoints("http://localhost:1234", "http://localhost:1234"),
    )
    assert TokenCache(client_id="abc", **common_args).filename != TokenCache(client_id="def", **common_args).filename


def test_token_cache_unique_filename_by_scopes():
    common_args = dict(
        host="http://localhost:",
        client_id="abc",
        redirect_url="http://localhost:8020",
        oidc_endpoints=OidcEndpoints("http://localhost:1234", "http://localhost:1234"),
    )
    assert TokenCache(scopes=["foo"], **common_args).filename != TokenCache(scopes=["bar"], **common_args).filename


def test_token_cache_unique_filename_by_profile():
    common_args = dict(
        host="http://localhost:",
        client_id="abc",
        redirect_url="http://localhost:8020",
        oidc_endpoints=OidcEndpoints("http://localhost:1234", "http://localhost:1234"),
    )
    assert TokenCache(profile="dev", **common_args).filename != TokenCache(profile="prod", **common_args).filename


def test_token_cache_filename_no_profile_matches_empty_profile():
    common_args = dict(
        host="http://localhost:",
        client_id="abc",
        redirect_url="http://localhost:8020",
        oidc_endpoints=OidcEndpoints("http://localhost:1234", "http://localhost:1234"),
    )
    assert TokenCache(**common_args).filename == TokenCache(profile=None, **common_args).filename


def test_token_cache_filename_no_delimiter_collision():
    """Scopes and profile with shared comma content must not collide."""
    common_args = dict(
        host="http://localhost:",
        client_id="abc",
        redirect_url="http://localhost:8020",
        oidc_endpoints=OidcEndpoints("http://localhost:1234", "http://localhost:1234"),
    )
    assert (
        TokenCache(scopes=["a,b"], profile="c", **common_args).filename
        != TokenCache(scopes=["a"], profile=",bc", **common_args).filename
    )


def test_account_oidc_endpoints(requests_mock):
    requests_mock.get(
        "https://accounts.cloud.databricks.com/oidc/accounts/abc-123/.well-known/oauth-authorization-server",
        json={
            "authorization_endpoint": "https://accounts.cloud.databricks.com/oidc/accounts/abc-123/oauth/authorize",
            "token_endpoint": "https://accounts.cloud.databricks.com/oidc/accounts/abc-123/oauth/token",
        },
    )
    client = _BaseClient(clock=FakeClock())
    endpoints = get_account_endpoints("accounts.cloud.databricks.com", "abc-123", client=client)
    assert endpoints == OidcEndpoints(
        "https://accounts.cloud.databricks.com/oidc/accounts/abc-123/oauth/authorize",
        "https://accounts.cloud.databricks.com/oidc/accounts/abc-123/oauth/token",
    )


def test_account_oidc_endpoints_retry_on_429(requests_mock):
    # It doesn't seem possible to use requests_mock to return different responses for the same request, e.g. when
    # simulating a transient failure. Instead, the nth_request matcher increments a test-wide counter and only matches
    # the nth request.
    request_count = 0

    def nth_request(n):

        def observe_request(_request):
            nonlocal request_count
            is_match = request_count == n
            if is_match:
                request_count += 1
            return is_match

        return observe_request

    requests_mock.get(
        "https://accounts.cloud.databricks.com/oidc/accounts/abc-123/.well-known/oauth-authorization-server",
        additional_matcher=nth_request(0),
        status_code=429,
    )
    requests_mock.get(
        "https://accounts.cloud.databricks.com/oidc/accounts/abc-123/.well-known/oauth-authorization-server",
        additional_matcher=nth_request(1),
        json={
            "authorization_endpoint": "https://accounts.cloud.databricks.com/oidc/accounts/abc-123/oauth/authorize",
            "token_endpoint": "https://accounts.cloud.databricks.com/oidc/accounts/abc-123/oauth/token",
        },
    )
    client = _BaseClient(clock=FakeClock())
    endpoints = get_account_endpoints("accounts.cloud.databricks.com", "abc-123", client=client)
    assert endpoints == OidcEndpoints(
        "https://accounts.cloud.databricks.com/oidc/accounts/abc-123/oauth/authorize",
        "https://accounts.cloud.databricks.com/oidc/accounts/abc-123/oauth/token",
    )


def test_workspace_oidc_endpoints(requests_mock):
    requests_mock.get(
        "https://my-workspace.cloud.databricks.com/oidc/.well-known/oauth-authorization-server",
        json={
            "authorization_endpoint": "https://my-workspace.cloud.databricks.com/oidc/oauth/authorize",
            "token_endpoint": "https://my-workspace.cloud.databricks.com/oidc/oauth/token",
        },
    )
    client = _BaseClient(clock=FakeClock())
    endpoints = get_workspace_endpoints("my-workspace.cloud.databricks.com", client=client)
    assert endpoints == OidcEndpoints(
        "https://my-workspace.cloud.databricks.com/oidc/oauth/authorize",
        "https://my-workspace.cloud.databricks.com/oidc/oauth/token",
    )


def test_workspace_oidc_endpoints_retry_on_429(requests_mock):
    request_count = 0

    def nth_request(n):

        def observe_request(_request):
            nonlocal request_count
            is_match = request_count == n
            if is_match:
                request_count += 1
            return is_match

        return observe_request

    requests_mock.get(
        "https://my-workspace.cloud.databricks.com/oidc/.well-known/oauth-authorization-server",
        additional_matcher=nth_request(0),
        status_code=429,
    )
    requests_mock.get(
        "https://my-workspace.cloud.databricks.com/oidc/.well-known/oauth-authorization-server",
        additional_matcher=nth_request(1),
        json={
            "authorization_endpoint": "https://my-workspace.cloud.databricks.com/oidc/oauth/authorize",
            "token_endpoint": "https://my-workspace.cloud.databricks.com/oidc/oauth/token",
        },
    )
    client = _BaseClient(clock=FakeClock())
    endpoints = get_workspace_endpoints("my-workspace.cloud.databricks.com", client=client)
    assert endpoints == OidcEndpoints(
        "https://my-workspace.cloud.databricks.com/oidc/oauth/authorize",
        "https://my-workspace.cloud.databricks.com/oidc/oauth/token",
    )


_DUMMY_HOST = "https://dummy-workspace.databricks.com"
_DUMMY_ACCOUNT_HOST = "https://dummy-accounts.databricks.com"
_DUMMY_ACCOUNT_ID = "00000000-0000-0000-0000-000000000001"
_DUMMY_WORKSPACE_ID = "111111111111111"


@pytest.mark.parametrize(
    "host,response_json,expected",
    [
        pytest.param(
            _DUMMY_HOST,
            {
                "oidc_endpoint": f"{_DUMMY_HOST}/oidc",
                "account_id": _DUMMY_ACCOUNT_ID,
                "workspace_id": _DUMMY_WORKSPACE_ID,
            },
            HostMetadata(
                oidc_endpoint=f"{_DUMMY_HOST}/oidc", account_id=_DUMMY_ACCOUNT_ID, workspace_id=_DUMMY_WORKSPACE_ID
            ),
            id="workspace-static-oidc-endpoint",
        ),
        pytest.param(
            _DUMMY_ACCOUNT_HOST,
            {"oidc_endpoint": f"{_DUMMY_ACCOUNT_HOST}/oidc/accounts/{{account_id}}"},
            HostMetadata(
                oidc_endpoint=f"{_DUMMY_ACCOUNT_HOST}/oidc/accounts/{{account_id}}", account_id=None, workspace_id=None
            ),
            id="account-raw-oidc-endpoint-template",
        ),
    ],
)
def test_get_host_metadata(requests_mock, host, response_json, expected):
    requests_mock.get(f"{host}/.well-known/databricks-config", json=response_json)
    client = _BaseClient(clock=FakeClock())
    assert get_host_metadata(host, client=client) == expected


def test_get_host_metadata_raises_on_http_error(requests_mock):
    requests_mock.get(f"{_DUMMY_HOST}/.well-known/databricks-config", status_code=404, json={"error": "not found"})
    client = _BaseClient(clock=FakeClock())
    with pytest.raises(ValueError, match="Failed to fetch host metadata"):
        get_host_metadata(_DUMMY_HOST, client=client)


def test_get_endpoints_from_url(requests_mock):
    requests_mock.get(
        f"{_DUMMY_HOST}/oidc",
        json={
            "authorization_endpoint": f"{_DUMMY_HOST}/oidc/v1/authorize",
            "token_endpoint": f"{_DUMMY_HOST}/oidc/v1/token",
        },
    )
    client = _BaseClient(clock=FakeClock())
    endpoints = get_endpoints_from_url(f"{_DUMMY_HOST}/oidc", client=client)
    assert endpoints == OidcEndpoints(
        authorization_endpoint=f"{_DUMMY_HOST}/oidc/v1/authorize",
        token_endpoint=f"{_DUMMY_HOST}/oidc/v1/token",
    )


# Regression tests for https://github.com/databricks/databricks-sdk-py/issues/1338:
# the `requests.post` and `requests.get` calls in oauth.py must pass a `timeout=`
# value to avoid hanging indefinitely when the OAuth endpoint is unreachable.


def _ok_response(json_payload=None):
    """Build a minimal mock Response for requests.post/get."""
    resp = MagicMock()
    resp.ok = True
    resp.headers = {"Content-Type": "application/json"}
    resp.json.return_value = json_payload or {
        "access_token": "access",
        "token_type": "Bearer",
        "expires_in": 3600,
    }
    return resp


def test_retrieve_token_passes_timeout():
    with patch("databricks.sdk.oauth.requests.post", return_value=_ok_response()) as post:
        retrieve_token(
            client_id="id",
            client_secret="secret",
            token_url="https://example.com/oidc/v1/token",
            params={"grant_type": "client_credentials"},
            use_header=True,
        )
    post.assert_called_once()
    assert post.call_args.kwargs.get("timeout") == oauth_module._OAUTH_DEFAULT_TIMEOUT_SECONDS


def test_get_azure_entra_id_workspace_endpoints_passes_timeout():
    redirect_resp = MagicMock()
    redirect_resp.headers = {"location": "https://login.microsoftonline.com/tenant/oauth2/v2.0/authorize"}
    with patch("databricks.sdk.oauth.requests.get", return_value=redirect_resp) as get:
        endpoints = get_azure_entra_id_workspace_endpoints("https://my-workspace.cloud.databricks.com")
    get.assert_called_once()
    assert get.call_args.kwargs.get("timeout") == oauth_module._OAUTH_DEFAULT_TIMEOUT_SECONDS
    assert endpoints is not None


def test_pat_oauth_token_exchange_refresh_passes_timeout():
    exchange = PATOAuthTokenExchange(
        get_original_token=lambda: "dapi-pat-token",
        host="https://my-workspace.cloud.databricks.com",
        scopes="all-apis",
    )
    with patch("databricks.sdk.oauth.requests.post", return_value=_ok_response()) as post:
        exchange.refresh()
    post.assert_called_once()
    assert post.call_args.kwargs.get("timeout") == oauth_module._OAUTH_DEFAULT_TIMEOUT_SECONDS
