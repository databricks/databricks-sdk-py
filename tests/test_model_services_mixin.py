import sys

import pytest

from databricks.sdk.core import Config


def test_open_ai_client(monkeypatch):
    from databricks.sdk import WorkspaceClient

    monkeypatch.setenv("DATABRICKS_HOST", "test_host")
    monkeypatch.setenv("DATABRICKS_TOKEN", "test_token")
    w = WorkspaceClient(config=Config())
    client = w.model_services.get_open_ai_client()

    assert client.base_url == "https://test_host/ai-gateway/mlflow/v1/"
    assert client.api_key == "no-token"


def test_open_ai_client_with_custom_params(monkeypatch):
    from databricks.sdk import WorkspaceClient

    monkeypatch.setenv("DATABRICKS_HOST", "test_host")
    monkeypatch.setenv("DATABRICKS_TOKEN", "test_token")
    w = WorkspaceClient(config=Config())

    client = w.model_services.get_open_ai_client(timeout=30.0, max_retries=3)

    assert client.base_url == "https://test_host/ai-gateway/mlflow/v1/"
    assert client.api_key == "no-token"
    assert client.timeout == 30.0
    assert client.max_retries == 3


def test_open_ai_client_prevents_reserved_param_override(monkeypatch):
    from databricks.sdk import WorkspaceClient

    monkeypatch.setenv("DATABRICKS_HOST", "test_host")
    monkeypatch.setenv("DATABRICKS_TOKEN", "test_token")
    w = WorkspaceClient(config=Config())

    with pytest.raises(ValueError, match="Cannot override reserved Databricks parameters: base_url"):
        w.model_services.get_open_ai_client(base_url="https://custom-host")

    with pytest.raises(ValueError, match="Cannot override reserved Databricks parameters: api_key"):
        w.model_services.get_open_ai_client(api_key="custom-key")

    with pytest.raises(ValueError, match="Cannot override reserved Databricks parameters: http_client"):
        w.model_services.get_open_ai_client(http_client=None)

    with pytest.raises(ValueError, match="Cannot override reserved Databricks parameters: api_key, base_url"):
        w.model_services.get_open_ai_client(base_url="https://custom-host", api_key="custom-key")


def test_open_ai_client_uses_config_authenticate(monkeypatch):
    from databricks.sdk import WorkspaceClient

    monkeypatch.setenv("DATABRICKS_HOST", "test_host")
    monkeypatch.setenv("DATABRICKS_TOKEN", "test_token")
    w = WorkspaceClient(config=Config())
    client = w.model_services.get_open_ai_client()

    auth_headers = client._client._auth.get_headers_func()
    assert auth_headers["Authorization"] == "Bearer test_token"


@pytest.mark.skipif(sys.version_info < (3, 8), reason="Requires Python > 3.7")
def test_langchain_open_ai_client(monkeypatch):
    from databricks.sdk import WorkspaceClient

    monkeypatch.setenv("DATABRICKS_HOST", "test_host")
    monkeypatch.setenv("DATABRICKS_TOKEN", "test_token")
    w = WorkspaceClient(config=Config())
    client = w.model_services.get_langchain_chat_open_ai_client("system.ai.claude-sonnet-4-5")

    assert client.openai_api_base == "https://test_host/ai-gateway/mlflow/v1"
    assert client.model_name == "system.ai.claude-sonnet-4-5"
