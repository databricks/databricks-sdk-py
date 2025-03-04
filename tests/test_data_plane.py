from datetime import datetime, timedelta
from unittest.mock import patch
from urllib import parse

from databricks.sdk import data_plane, oauth
from databricks.sdk.data_plane import DataPlaneService
from databricks.sdk.oauth import Token
from databricks.sdk.service.serving import DataPlaneInfo

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
    token_source = data_plane.DataPlaneTokenSource(config.host, success_callable(token), disable_async=True)
    token_source._token_sources["endpoint:authDetails"] = MockEndpointTokenSource(another_token)

    with patch("databricks.sdk.oauth.retrieve_token", return_value=dp_token) as retrieve_token:
        result_token = token_source.token(endpoint="endpoint", auth_details="authDetails")

    retrieve_token.assert_not_called()
    assert result_token.access_token == another_token.access_token


## These tests are for the old implementation. #TODO: Remove after the new implementation is used

info = DataPlaneInfo(authorization_details="authDetails", endpoint_url="url")

token = Token(
    access_token="token",
    token_type="type",
    expiry=datetime.now() + timedelta(hours=1),
)


class MockRefresher:

    def __init__(self, expected: str):
        self._expected = expected

    def __call__(self, auth_details: str) -> Token:
        assert self._expected == auth_details
        return token


def throw_exception():
    raise Exception("Expected value to be cached")


def test_not_cached():
    data_plane = DataPlaneService()
    res = data_plane.get_data_plane_details(
        "method",
        ["params"],
        lambda: info,
        lambda a: MockRefresher(info.authorization_details).__call__(a),
    )
    assert res.endpoint_url == info.endpoint_url
    assert res.token == token


def test_token_expired():
    expired = Token(
        access_token="expired",
        token_type="type",
        expiry=datetime.now() + timedelta(hours=-1),
    )
    data_plane = DataPlaneService()
    data_plane._tokens["method/params"] = expired
    res = data_plane.get_data_plane_details(
        "method",
        ["params"],
        lambda: info,
        lambda a: MockRefresher(info.authorization_details).__call__(a),
    )
    assert res.endpoint_url == info.endpoint_url
    assert res.token == token


def test_info_cached():
    data_plane = DataPlaneService()
    data_plane._data_plane_info["method/params"] = info
    res = data_plane.get_data_plane_details(
        "method",
        ["params"],
        throw_exception,
        lambda a: MockRefresher(info.authorization_details).__call__(a),
    )
    assert res.endpoint_url == info.endpoint_url
    assert res.token == token


def test_token_cached():
    data_plane = DataPlaneService()
    data_plane._data_plane_info["method/params"] = info
    data_plane._tokens["method/params"] = token
    res = data_plane.get_data_plane_details("method", ["params"], throw_exception, throw_exception)
    assert res.endpoint_url == info.endpoint_url
    assert res.token == token
