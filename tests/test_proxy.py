import os
import urllib.parse
import pytest
from databricks.sdk.config import Config
from databricks.sdk._base_client import _BaseClient
from databricks.sdk.core import ApiClient

def test_config_proxy_attributes():
    cfg = Config(
        host="https://test.databricks.com",
        token="test-token",
        proxy_url="http://proxy.example.com:8080",
        proxy_username="user123",
        proxy_password="secretpassword",
        proxy_auth_type="BASIC",
    )
    assert cfg.proxy_url == "http://proxy.example.com:8080"
    assert cfg.proxy_username == "user123"
    assert cfg.proxy_password == "secretpassword"
    assert cfg.proxy_auth_type == "BASIC"
    assert "proxy_password=***" in cfg.debug_string()

def test_config_proxy_from_env(monkeypatch):
    monkeypatch.setenv("DATABRICKS_PROXY_URL", "http://proxy.env.com:8080")
    monkeypatch.setenv("DATABRICKS_PROXY_USERNAME", "envuser")
    monkeypatch.setenv("DATABRICKS_PROXY_PASSWORD", "envpass")
    monkeypatch.setenv("DATABRICKS_PROXY_AUTH_TYPE", "BASIC")

    cfg = Config(host="https://test.databricks.com", token="test-token")
    assert cfg.proxy_url == "http://proxy.env.com:8080"
    assert cfg.proxy_username == "envuser"
    assert cfg.proxy_password == "envpass"
    assert cfg.proxy_auth_type == "BASIC"

def test_base_client_proxy_url_construction():
    # Test proxy with username and password containing special characters that need encoding
    client = _BaseClient(
        proxy_url="http://proxy.example.com:8080",
        proxy_username="user@domain",
        proxy_password="pass:word",
    )
    # The constructed proxy URL should have encoded credentials
    expected_url = "http://user%40domain:pass%3Aword@proxy.example.com:8080"
    assert client._session.proxies == {
        "http": expected_url,
        "https": expected_url,
    }

def test_base_client_proxy_no_credentials():
    client = _BaseClient(proxy_url="proxy.example.com:8080")
    # Scheme should be prepended
    expected_url = "http://proxy.example.com:8080"
    assert client._session.proxies == {
        "http": expected_url,
        "https": expected_url,
    }

def test_base_client_proxy_from_env(monkeypatch):
    monkeypatch.setenv("DATABRICKS_PROXY_URL", "http://envproxy.com:8080")
    monkeypatch.setenv("DATABRICKS_PROXY_USERNAME", "envuser")
    monkeypatch.setenv("DATABRICKS_PROXY_PASSWORD", "envpass")

    client = _BaseClient()
    expected_url = "http://envuser:envpass@envproxy.com:8080"
    assert client._session.proxies == {
        "http": expected_url,
        "https": expected_url,
    }
