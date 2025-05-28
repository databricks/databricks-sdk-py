import time

import httpx
import pytest


@pytest.mark.asyncio
async def test_mcp_oauth_provider(monkeypatch):
    monkeypatch.setattr(time, "time", lambda: 100)
    from databricks.sdk import WorkspaceClient

    monkeypatch.setenv("DATABRICKS_HOST", "test_host")
    monkeypatch.setenv("DATABRICKS_TOKEN", "test_token")

    w = WorkspaceClient()
    mcp_oauth_provider = w.mcp.get_oauth_provider()

    request = httpx.Request("GET", "https://example.com")
    response = await anext(mcp_oauth_provider.async_auth_flow(request))
    assert response.headers["Authorization"] == "Bearer test_token"
