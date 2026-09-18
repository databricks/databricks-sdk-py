from datetime import datetime, timedelta
from unittest.mock import patch
from urllib import parse

from databricks.sdk import WorkspaceClient, data_plane, oauth
from databricks.sdk.config import Config
from databricks.sdk.credentials_provider import OAuthCredentialsProvider, OauthCredentialsStrategy
from databricks.sdk.oauth import Token

cp_token = Token(access_token="control plane token", token_type="type", expiry=datetime.now() + timedelta(hours=1))
dp_token = Token(access_token="data plane token", token_type="type", expiry=datetime.now() + timedelta(hours=1))


def success_callable(token: oauth.Token):
    def success() -> oauth.Token:
        return token

    return success


def test_endpoint_token_source_get_token(config):
    token_source = data_plane.DataPlaneEndpointTokenSource(
        config.host, success_callable(cp_token), "authDetails", disable_async=True
    )

    with patch("databricks.sdk.oauth.retrieve_token", return_value=dp_token) as retrieve_token:
        token_source.token()

    retrieve_token.assert_called_once()
    args, kwargs = retrieve_token.call_args

    assert kwargs["token_url"] == config.host + "/oidc/v1/token"
    assert kwargs["params"] == parse.urlencode(
        {
            "grant_type": "urn:ietf:params:oauth:grant-type:jwt-bearer",
            "authorization_details": "authDetails",
            "assertion": cp_token.access_token,
        }
    )
    assert kwargs["headers"] == {"Content-Type": "application/x-www-form-urlencoded"}


def test_token_source_get_token_not_existing(config):
    token_source = data_plane.DataPlaneTokenSource(config.host, success_callable(cp_token), disable_async=True)

    with patch("databricks.sdk.oauth.retrieve_token", return_value=dp_token) as retrieve_token:
        result_token = token_source.token(endpoint="endpoint", auth_details="authDetails")

    retrieve_token.assert_called_once()
    assert result_token.access_token == dp_token.access_token
    assert "endpoint:authDetails" in token_source._token_sources


class MockEndpointTokenSource:
    def __init__(self, token: oauth.Token):
        self._token = token

    def token(self):
        return self._token


def test_token_source_get_token_existing(config):
    another_token = Token(access_token="another token", token_type="type", expiry=datetime.now() + timedelta(hours=1))
    token_source = data_plane.DataPlaneTokenSource(config.host, success_callable(cp_token), disable_async=True)
    token_source._token_sources["endpoint:authDetails"] = MockEndpointTokenSource(another_token)

    with patch("databricks.sdk.oauth.retrieve_token", return_value=dp_token) as retrieve_token:
        result_token = token_source.token(endpoint="endpoint", auth_details="authDetails")

    retrieve_token.assert_not_called()
    assert result_token.access_token == another_token.access_token


def test_serving_endpoint_data_plane_discovers_exchanges_and_queries_over_http(requests_mock):
    control_plane_token = Token(access_token="control-plane-token", token_type="Bearer")
    credentials_strategy = OauthCredentialsStrategy(
        "fixture-oauth",
        lambda _: OAuthCredentialsProvider(
            lambda: {"Authorization": "Bearer control-plane-token"},
            lambda: control_plane_token,
        ),
    )
    config = Config(
        host="http://localhost",
        workspace_id="12345",
        credentials_strategy=credentials_strategy,
        disable_async_token_refresh=True,
    )
    endpoint_name = "route-optimized"
    data_plane_url = "https://data-plane.example/invocations"
    authorization_details = '{"type":"query","resource":"route-optimized"}'
    requests_mock.get(
        f"http://localhost/api/2.0/serving-endpoints/{endpoint_name}",
        json={
            "name": endpoint_name,
            "data_plane_info": {
                "query_info": {
                    "endpoint_url": data_plane_url,
                    "authorization_details": authorization_details,
                }
            },
        },
    )
    requests_mock.post(
        "http://localhost/oidc/v1/token",
        json={"access_token": "data-plane-token", "token_type": "Bearer", "expires_in": 3600},
    )
    requests_mock.post(
        data_plane_url,
        json={"predictions": [0.75]},
        headers={"served-model-name": "model-v1"},
    )

    response = WorkspaceClient(config=config).serving_endpoints_data_plane.query(
        name=endpoint_name,
        dataframe_records=[{"col": 1.0}],
    )

    discovery_request, exchange_request, query_request = requests_mock.request_history
    assert response.predictions == [0.75]
    assert response.served_model_name == "model-v1"
    assert discovery_request.method == "GET"
    assert discovery_request.headers["Authorization"] == "Bearer control-plane-token"
    assert parse.parse_qs(exchange_request.text) == {
        "assertion": ["control-plane-token"],
        "authorization_details": [authorization_details],
        "grant_type": ["urn:ietf:params:oauth:grant-type:jwt-bearer"],
    }
    assert exchange_request.headers["Content-Type"] == "application/x-www-form-urlencoded"
    assert query_request.url == data_plane_url
    assert query_request.headers["Authorization"] == "Bearer data-plane-token"
    assert query_request.headers["X-Databricks-Workspace-Id"] == "12345"
    assert query_request.json() == {"dataframe_records": [{"col": 1.0}]}
