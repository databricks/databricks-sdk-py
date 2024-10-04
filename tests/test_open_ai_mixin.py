from databricks.sdk.core import Config


def test_open_ai_client(monkeypatch):
    from databricks.sdk import WorkspaceClient

    monkeypatch.setenv('DATABRICKS_HOST', 'test_host')
    monkeypatch.setenv('DATABRICKS_TOKEN', 'test_token')
    w = WorkspaceClient(config=Config())
    client = w.serving_endpoints.get_open_api_client()

    assert client.base_url == "https://test_host/serving-endpoints/"
    assert client.api_key == "test_token"
