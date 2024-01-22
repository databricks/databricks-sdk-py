import json
from datetime import datetime, timedelta

import requests

from databricks.sdk.core import Config
from databricks.sdk.credentials_provider import MetadataServiceTokenSource


def get_test_server(host: str, token: str, expires_after: int):
    counter = 0

    def inner(*args, **kwargs):
        nonlocal counter
        headers = kwargs['headers']
        if headers.get(MetadataServiceTokenSource.METADATA_SERVICE_VERSION_HEADER
                       ) != MetadataServiceTokenSource.METADATA_SERVICE_VERSION:
            resp = requests.Response()
            resp.status_code = 400
            return resp
        if headers.get(MetadataServiceTokenSource.METADATA_SERVICE_HOST_HEADER) != host:
            resp = requests.Response()
            resp.status_code = 404
            return resp

        json_data = {
            "access_token": f"{token}-{counter}",
            "expires_on": int((datetime.now() + timedelta(seconds=expires_after)).timestamp()),
            "token_type": "Bearer"
        }
        resp = requests.Response()
        resp.status_code = 200
        resp._content = json.dumps(json_data).encode('utf-8')
        counter += 1
        return resp

    return inner


def test_config_metadata_service(monkeypatch):
    monkeypatch.setattr(requests, 'get', get_test_server('https://x', 'token', 100))
    monkeypatch.setenv('DATABRICKS_HOST', 'x')
    monkeypatch.setenv('DATABRICKS_METADATA_SERVICE_URL', 'http://y')
    cfg = Config()

    assert cfg.auth_type == 'metadata-service'
    assert cfg.host == 'https://x'
    assert cfg.metadata_service_url == 'http://y'


def test_config_metadata_service_athenticate(monkeypatch):
    monkeypatch.setattr(requests, 'get', get_test_server('https://x', 'token', 1000))
    monkeypatch.setenv('DATABRICKS_HOST', 'x')
    monkeypatch.setenv('DATABRICKS_METADATA_SERVICE_URL', 'http://y')
    cfg = Config()

    assert cfg.auth_type == 'metadata-service'
    assert cfg.host == 'https://x'
    assert cfg.metadata_service_url == 'http://y'

    headers = cfg.authenticate()
    assert headers.get("Authorization") == "Bearer token-0"


def test_config_metadata_service_refresh(monkeypatch):
    monkeypatch.setattr(requests, 'get', get_test_server('https://x', 'token', 10))
    monkeypatch.setenv('DATABRICKS_HOST', 'x')
    monkeypatch.setenv('DATABRICKS_METADATA_SERVICE_URL', 'http://y')
    cfg = Config()

    assert cfg.auth_type == 'metadata-service'
    assert cfg.host == 'https://x'
    assert cfg.metadata_service_url == 'http://y'

    headers = cfg.authenticate()
    # the first refresh happens when initialising config. So this is the second refresh
    assert headers.get("Authorization") == "Bearer token-1"

    headers = cfg.authenticate()
    assert headers.get("Authorization") == "Bearer token-2"
