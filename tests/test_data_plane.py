from datetime import datetime, timedelta
from unittest.mock import patch
from urllib import parse

from databricks.sdk import data_plane, oauth
from databricks.sdk.oauth import Token

cp_token = Token(access_token="control plane token", token_type="type", expiry=datetime.now() + timedelta(hours=1))
dp_token = Token(access_token="data plane token", token_type="type", expiry=datetime.now() + timedelta(hours=1))


def success_callable(token: oauth.Token):  # type: ignore[no-untyped-def]

    def success() -> oauth.Token:
        return token

    return success


def test_endpoint_token_source_get_token(config):  # type: ignore[no-untyped-def]
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


def test_token_source_get_token_not_existing(config):  # type: ignore[no-untyped-def]
    token_source = data_plane.DataPlaneTokenSource(config.host, success_callable(cp_token), disable_async=True)

    with patch("databricks.sdk.oauth.retrieve_token", return_value=dp_token) as retrieve_token:
        result_token = token_source.token(endpoint="endpoint", auth_details="authDetails")  # type: ignore[no-untyped-call]

    retrieve_token.assert_called_once()
    assert result_token.access_token == dp_token.access_token
    assert "endpoint:authDetails" in token_source._token_sources


class MockEndpointTokenSource:

    def __init__(self, token: oauth.Token):
        self._token = token

    def token(self):  # type: ignore[no-untyped-def]
        return self._token


def test_token_source_get_token_existing(config):  # type: ignore[no-untyped-def]
    another_token = Token(access_token="another token", token_type="type", expiry=datetime.now() + timedelta(hours=1))
    token_source = data_plane.DataPlaneTokenSource(config.host, success_callable(cp_token), disable_async=True)
    token_source._token_sources["endpoint:authDetails"] = MockEndpointTokenSource(another_token)

    with patch("databricks.sdk.oauth.retrieve_token", return_value=dp_token) as retrieve_token:
        result_token = token_source.token(endpoint="endpoint", auth_details="authDetails")  # type: ignore[no-untyped-call]

    retrieve_token.assert_not_called()
    assert result_token.access_token == another_token.access_token
