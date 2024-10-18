from databricks.sdk._base_client import _BaseClient
from databricks.sdk.oauth import (OidcEndpoints, TokenCache,
                                  get_account_endpoints,
                                  get_workspace_endpoints)

from .clock import FakeClock


def test_token_cache_unique_filename_by_host():
    common_args = dict(client_id="abc",
                       redirect_url="http://localhost:8020",
                       oidc_endpoints=OidcEndpoints("http://localhost:1234", "http://localhost:1234"))
    assert TokenCache(host="http://localhost:",
                      **common_args).filename != TokenCache("https://bar.cloud.databricks.com",
                                                            **common_args).filename


def test_token_cache_unique_filename_by_client_id():
    common_args = dict(host="http://localhost:",
                       redirect_url="http://localhost:8020",
                       oidc_endpoints=OidcEndpoints("http://localhost:1234", "http://localhost:1234"))
    assert TokenCache(client_id="abc", **common_args).filename != TokenCache(client_id="def",
                                                                             **common_args).filename


def test_token_cache_unique_filename_by_scopes():
    common_args = dict(host="http://localhost:",
                       client_id="abc",
                       redirect_url="http://localhost:8020",
                       oidc_endpoints=OidcEndpoints("http://localhost:1234", "http://localhost:1234"))
    assert TokenCache(scopes=["foo"], **common_args).filename != TokenCache(scopes=["bar"],
                                                                            **common_args).filename


def test_account_oidc_endpoints(requests_mock):
    requests_mock.get(
        "https://accounts.cloud.databricks.com/oidc/accounts/abc-123/.well-known/oauth-authorization-server",
        json={
            "authorization_endpoint":
            "https://accounts.cloud.databricks.com/oidc/accounts/abc-123/oauth/authorize",
            "token_endpoint": "https://accounts.cloud.databricks.com/oidc/accounts/abc-123/oauth/token"
        })
    client = _BaseClient(clock=FakeClock())
    endpoints = get_account_endpoints("accounts.cloud.databricks.com", "abc-123", client=client)
    assert endpoints == OidcEndpoints(
        "https://accounts.cloud.databricks.com/oidc/accounts/abc-123/oauth/authorize",
        "https://accounts.cloud.databricks.com/oidc/accounts/abc-123/oauth/token")


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
        status_code=429)
    requests_mock.get(
        "https://accounts.cloud.databricks.com/oidc/accounts/abc-123/.well-known/oauth-authorization-server",
        additional_matcher=nth_request(1),
        json={
            "authorization_endpoint":
            "https://accounts.cloud.databricks.com/oidc/accounts/abc-123/oauth/authorize",
            "token_endpoint": "https://accounts.cloud.databricks.com/oidc/accounts/abc-123/oauth/token"
        })
    client = _BaseClient(clock=FakeClock())
    endpoints = get_account_endpoints("accounts.cloud.databricks.com", "abc-123", client=client)
    assert endpoints == OidcEndpoints(
        "https://accounts.cloud.databricks.com/oidc/accounts/abc-123/oauth/authorize",
        "https://accounts.cloud.databricks.com/oidc/accounts/abc-123/oauth/token")


def test_workspace_oidc_endpoints(requests_mock):
    requests_mock.get("https://my-workspace.cloud.databricks.com/oidc/.well-known/oauth-authorization-server",
                      json={
                          "authorization_endpoint":
                          "https://my-workspace.cloud.databricks.com/oidc/oauth/authorize",
                          "token_endpoint": "https://my-workspace.cloud.databricks.com/oidc/oauth/token"
                      })
    client = _BaseClient(clock=FakeClock())
    endpoints = get_workspace_endpoints("my-workspace.cloud.databricks.com", client=client)
    assert endpoints == OidcEndpoints("https://my-workspace.cloud.databricks.com/oidc/oauth/authorize",
                                      "https://my-workspace.cloud.databricks.com/oidc/oauth/token")


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

    requests_mock.get("https://my-workspace.cloud.databricks.com/oidc/.well-known/oauth-authorization-server",
                      additional_matcher=nth_request(0),
                      status_code=429)
    requests_mock.get("https://my-workspace.cloud.databricks.com/oidc/.well-known/oauth-authorization-server",
                      additional_matcher=nth_request(1),
                      json={
                          "authorization_endpoint":
                          "https://my-workspace.cloud.databricks.com/oidc/oauth/authorize",
                          "token_endpoint": "https://my-workspace.cloud.databricks.com/oidc/oauth/token"
                      })
    client = _BaseClient(clock=FakeClock())
    endpoints = get_workspace_endpoints("my-workspace.cloud.databricks.com", client=client)
    assert endpoints == OidcEndpoints("https://my-workspace.cloud.databricks.com/oidc/oauth/authorize",
                                      "https://my-workspace.cloud.databricks.com/oidc/oauth/token")
