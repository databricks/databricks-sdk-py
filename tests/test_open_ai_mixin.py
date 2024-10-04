import sys

import pytest

from databricks.sdk.core import Config


def test_open_ai_client(monkeypatch):
    from databricks.sdk import WorkspaceClient

    monkeypatch.setenv('DATABRICKS_HOST', 'test_host')
    monkeypatch.setenv('DATABRICKS_TOKEN', 'test_token')
    w = WorkspaceClient(config=Config())
    client = w.serving_endpoints.get_open_ai_client()

    assert client.base_url == "https://test_host/serving-endpoints/"
    assert client.api_key == "no-token"


@pytest.mark.skipif(sys.version_info < (3, 8), reason="Requires Python > 3.7")
def test_langchain_open_ai_client(monkeypatch):
    from databricks.sdk import WorkspaceClient

    monkeypatch.setenv('DATABRICKS_HOST', 'test_host')
    monkeypatch.setenv('DATABRICKS_TOKEN', 'test_token')
    w = WorkspaceClient(config=Config())
    client = w.serving_endpoints.get_langchain_chat_open_ai_client("databricks-meta-llama-3-1-70b-instruct")

    assert client.openai_api_base == "https://test_host/serving-endpoints"
    assert client.model_name == "databricks-meta-llama-3-1-70b-instruct"
