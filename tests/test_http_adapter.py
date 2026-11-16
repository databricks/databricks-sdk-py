import pytest
import requests_mock

from databricks.sdk import AccountClient, WorkspaceClient
from databricks.sdk.core import ApiClient, Config, DatabricksError
from databricks.sdk.oauth import get_host_metadata

from .clock import FakeClock


@pytest.fixture
def adapter():
    return requests_mock.Adapter()


@pytest.mark.parametrize("scheme", ["http", "https"])
@pytest.mark.parametrize("client_type", [WorkspaceClient, AccountClient])
def test_adapter_handles_discovery_and_authenticated_api_calls(mocker, scheme, client_type, adapter):
    # The suite normally stubs discovery; exercise it over the same transport as the API.
    mocker.patch("databricks.sdk.config.get_host_metadata", get_host_metadata)
    host = f"{scheme}://sdk.example"
    discovery = adapter.register_uri("GET", f"{host}/.well-known/databricks-config", json={"workspace_id": 42})
    api = adapter.register_uri("GET", f"{host}/api/example", json={"value": "ok"})
    client = client_type(
        host=host,
        token="test-token",
        http_adapter=adapter,
        custom_headers={"X-Request-ID": "test-request"},
    )

    assert client.config.workspace_id == "42"
    assert client.api_client.do("GET", "/api/example") == {"value": "ok"}
    assert discovery.call_count == 1
    assert api.last_request.headers["Authorization"] == "Bearer test-token"
    assert api.last_request.headers["X-Request-ID"] == "test-request"


def test_adapter_preserves_sdk_retries_and_error_decoding(adapter):
    api = adapter.register_uri(
        "GET",
        "https://sdk.example/api/example",
        [
            {"status_code": 429, "headers": {"Retry-After": "1"}},
            {"status_code": 400, "json": {"error_code": "INVALID_PARAMETER_VALUE", "message": "bad input"}},
        ],
    )
    config = Config(host="https://sdk.example", token="test-token", http_adapter=adapter, clock=FakeClock())

    with pytest.raises(DatabricksError, match="bad input") as error:
        ApiClient(config).do("GET", "/api/example")

    assert error.value.error_code == "INVALID_PARAMETER_VALUE"
    assert api.call_count == 2
    assert all(r.headers["Authorization"] == "Bearer test-token" for r in api.request_history)


def test_failed_discovery_falls_back_to_explicit_config(mocker, adapter):
    mocker.patch("databricks.sdk.config.get_host_metadata", get_host_metadata)
    adapter.register_uri("GET", "https://sdk.example/.well-known/databricks-config", status_code=404)
    adapter.register_uri("GET", "https://sdk.example/api/example", json={"value": "ok"})
    config = Config(host="https://sdk.example", token="test-token", http_adapter=adapter, workspace_id=123)

    assert config.workspace_id == "123"
    assert ApiClient(config.copy()).do("GET", "/api/example") == {"value": "ok"}
