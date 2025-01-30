import sys
from io import BytesIO

import pytest

from databricks.sdk.core import Config
from databricks.sdk.service.serving import ExternalFunctionRequestHttpMethod


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


def test_http_request(w, requests_mock):
    headers = {"Accept": "text/plain", "Content-Type": "application/json", }
    mocked_url = "http://localhost/api/2.0/external-function"
    blob_response = BytesIO(b"The request was successful")

    requests_mock.post(mocked_url,
                       request_headers=headers,
                       content=blob_response.getvalue(),
                       status_code=200,
                       )
    response = w.serving_endpoints.http_request(conn="test_conn",
                                                method=ExternalFunctionRequestHttpMethod.GET,
                                                path="test_path")
    assert requests_mock.call_count == 1
    assert requests_mock.called
    assert response.status_code == 200 # Verify the response status
    assert (response.text == "The request was successful") # Ensure the response body matches the mocked data