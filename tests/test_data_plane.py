from datetime import datetime, timedelta

from databricks.sdk.data_plane import DataPlaneService
from databricks.sdk.oauth import Token
from databricks.sdk.service.oauth2 import DataPlaneInfo

info = DataPlaneInfo(authorization_details="authDetails", endpoint_url="url")

token = Token(access_token="token", token_type="type", expiry=datetime.now() + timedelta(hours=1))


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
    res = data_plane.get_data_plane_details("method", ["params"], lambda: info,
                                            lambda a: MockRefresher(info.authorization_details).__call__(a))
    assert res.endpoint_url == info.endpoint_url
    assert res.token == token


def test_token_expired():
    expired = Token(access_token="expired", token_type="type", expiry=datetime.now() + timedelta(hours=-1))
    data_plane = DataPlaneService()
    data_plane._tokens["method/params"] = expired
    res = data_plane.get_data_plane_details("method", ["params"], lambda: info,
                                            lambda a: MockRefresher(info.authorization_details).__call__(a))
    assert res.endpoint_url == info.endpoint_url
    assert res.token == token


def test_info_cached():
    data_plane = DataPlaneService()
    data_plane._data_plane_info["method/params"] = info
    res = data_plane.get_data_plane_details("method", ["params"], throw_exception,
                                            lambda a: MockRefresher(info.authorization_details).__call__(a))
    assert res.endpoint_url == info.endpoint_url
    assert res.token == token


def test_token_cached():
    data_plane = DataPlaneService()
    data_plane._data_plane_info["method/params"] = info
    data_plane._tokens["method/params"] = token
    res = data_plane.get_data_plane_details("method", ["params"], throw_exception, throw_exception)
    assert res.endpoint_url == info.endpoint_url
    assert res.token == token
