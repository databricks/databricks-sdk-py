from databricks.sdk.core import Config
from databricks.sdk.oauth import OAuthClient, OidcEndpoints, TokenCache


def test_token_cache_unique_filename_by_host(mocker):
    mocker.patch.object(Config, "oidc_endpoints",
                        OidcEndpoints("http://localhost:1234", "http://localhost:1234"))
    common_args = dict(client_id="abc", redirect_url="http://localhost:8020")
    c1 = OAuthClient(host="http://localhost:", **common_args)
    c2 = OAuthClient(host="https://bar.cloud.databricks.com", **common_args)
    assert TokenCache(c1).filename != TokenCache(c2).filename


def test_token_cache_unique_filename_by_client_id(mocker):
    mocker.patch.object(Config, "oidc_endpoints",
                        OidcEndpoints("http://localhost:1234", "http://localhost:1234"))
    common_args = dict(host="http://localhost:", redirect_url="http://localhost:8020")
    c1 = OAuthClient(client_id="abc", **common_args)
    c2 = OAuthClient(client_id="def", **common_args)
    assert TokenCache(c1).filename != TokenCache(c2).filename


def test_token_cache_unique_filename_by_scopes(mocker):
    mocker.patch.object(Config, "oidc_endpoints",
                        OidcEndpoints("http://localhost:1234", "http://localhost:1234"))
    common_args = dict(host="http://localhost:", client_id="abc", redirect_url="http://localhost:8020")
    c1 = OAuthClient(scopes=["foo"], **common_args)
    c2 = OAuthClient(scopes=["bar"], **common_args)
    assert TokenCache(c1).filename != TokenCache(c2).filename
