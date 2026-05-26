from urllib.parse import urlparse

import pytest
from requests.adapters import HTTPAdapter

from databricks.sdk import AccountClient, WorkspaceClient
from databricks.sdk.environments import Cloud

from .conftest import _is_cloud


class _CaptureHeadersAdapter(HTTPAdapter):
    """Snapshots request and response headers for a single matching URL path.

    Used to verify wire-level header behavior in integration tests; the request
    is otherwise let through to the real transport unchanged.
    """

    def __init__(self, path, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.path = path
        self.req_headers = None
        self.resp_headers = None

    def send(self, request, **kwargs):
        response = super().send(request, **kwargs)
        if urlparse(request.url).path == self.path:
            self.req_headers = dict(request.headers)
            self.resp_headers = dict(response.headers)
        return response


def test_workspace_operations(unified_config):
    # GCP google-credentials auth produces a workspace-local SP that is not
    # federated at the account level. Workspace APIs via the unified host
    # return 401 for this SP. See test_spog_workspace_google_credentials.
    if _is_cloud(Cloud.GCP):
        pytest.skip("google-credentials workspace ops not supported on unified hosts (workspace-local SP)")
    client = WorkspaceClient(config=unified_config)
    user = client.current_user.me()
    assert user is not None


def test_account_operations(unified_config):
    client = AccountClient(config=unified_config)
    groups = client.groups.list()
    assert groups is not None


# SPOG/W — Workspace operations on unified host with explicit auth


# Environment: azure-prod-pat
def test_spog_workspace_pat(isolated_env):
    env = isolated_env("workspace")
    host = env("UNIFIED_HOST")
    workspace_id = env("TEST_WORKSPACE_ID")
    account_id = env("TEST_ACCOUNT_ID")
    token = env("DATABRICKS_TOKEN")
    ws = WorkspaceClient(
        host=host,
        workspace_id=workspace_id,
        account_id=account_id,
        token=token,
    )
    me = ws.current_user.me()
    assert me.user_name


# Environment: azure-prod-ucws
def test_spog_workspace_oauth_m2m(isolated_env):
    env = isolated_env("ucws")
    host = env("UNIFIED_HOST")
    client_id = env("TEST_DATABRICKS_CLIENT_ID")
    client_secret = env("TEST_DATABRICKS_CLIENT_SECRET")
    workspace_id = env("THIS_WORKSPACE_ID")
    account_id = env("TEST_ACCOUNT_ID")
    ws = WorkspaceClient(
        host=host,
        client_id=client_id,
        client_secret=client_secret,
        workspace_id=workspace_id,
        account_id=account_id,
        auth_type="oauth-m2m",
    )
    me = ws.current_user.me()
    assert me.user_name


# Environment: azure-prod-ucws
def test_spog_workspace_azure_client_secret(isolated_env):
    env = isolated_env("ucws")
    host = env("UNIFIED_HOST")
    workspace_id = env("THIS_WORKSPACE_ID")
    account_id = env("TEST_ACCOUNT_ID")
    azure_client_id = env("ARM_CLIENT_ID")
    azure_client_secret = env("ARM_CLIENT_SECRET")
    azure_tenant_id = env("ARM_TENANT_ID")
    ws = WorkspaceClient(
        host=host,
        workspace_id=workspace_id,
        account_id=account_id,
        azure_client_id=azure_client_id,
        azure_client_secret=azure_client_secret,
        azure_tenant_id=azure_tenant_id,
        auth_type="azure-client-secret",
    )
    me = ws.current_user.me()
    assert me.user_name


# Environment: gcp-prod-ucacct
def test_spog_workspace_google_credentials(isolated_env):
    # google-credentials uses a GCP ID token with target_audience=cfg.host.
    # On the unified host this produces the same token for both account and workspace
    # requests (identical OIDC exchange, identical audience). Account-level APIs accept
    # this token, but workspace-level APIs return 401. The X-Databricks-Workspace-Id header
    # is set correctly. This appears to be a server-side limitation on unified hosts.
    pytest.skip("google-credentials ID token is rejected for workspace operations on unified hosts")
    env = isolated_env("ucacct")
    host = env("UNIFIED_HOST")
    account_id = env("DATABRICKS_ACCOUNT_ID")
    google_credentials = env("GOOGLE_CREDENTIALS")
    google_service_account = env("DATABRICKS_GOOGLE_SERVICE_ACCOUNT")
    workspace_id = env("TEST_WORKSPACE_ID")

    ws = WorkspaceClient(
        host=host,
        workspace_id=workspace_id,
        account_id=account_id,
        google_credentials=google_credentials,
        google_service_account=google_service_account,
        auth_type="google-credentials",
    )
    me = ws.current_user.me()
    assert me.user_name


# SPOG/A — Account operations on unified host with explicit auth


# Environment: azure-prod-acct
def test_spog_account_oauth_m2m(isolated_env):
    env = isolated_env("ucacct")
    host = env("UNIFIED_HOST")
    account_id = env("DATABRICKS_ACCOUNT_ID")
    client_id = env("TEST_DATABRICKS_CLIENT_ID")
    client_secret = env("TEST_DATABRICKS_CLIENT_SECRET")
    ac = AccountClient(
        host=host,
        account_id=account_id,
        client_id=client_id,
        client_secret=client_secret,
        auth_type="oauth-m2m",
    )
    sps = ac.service_principals.list()
    next(sps)


# Environment: azure-prod-acct
def test_spog_account_azure_client_secret(isolated_env):
    env = isolated_env("ucacct")
    host = env("UNIFIED_HOST")
    account_id = env("DATABRICKS_ACCOUNT_ID")
    azure_client_id = env("ARM_CLIENT_ID")
    azure_client_secret = env("ARM_CLIENT_SECRET")
    azure_tenant_id = env("ARM_TENANT_ID")
    ac = AccountClient(
        host=host,
        account_id=account_id,
        azure_client_id=azure_client_id,
        azure_client_secret=azure_client_secret,
        azure_tenant_id=azure_tenant_id,
        auth_type="azure-client-secret",
    )
    sps = ac.service_principals.list()
    next(sps)


# Environment: gcp-prod-ucacct
def test_spog_account_google_credentials(isolated_env):
    env = isolated_env("ucacct")
    host = env("UNIFIED_HOST")
    account_id = env("DATABRICKS_ACCOUNT_ID")
    google_credentials = env("GOOGLE_CREDENTIALS")
    google_service_account = env("DATABRICKS_GOOGLE_SERVICE_ACCOUNT")
    ac = AccountClient(
        host=host,
        account_id=account_id,
        google_credentials=google_credentials,
        google_service_account=google_service_account,
        auth_type="google-credentials",
    )
    sps = ac.service_principals.list()
    next(sps)


# Environment: azure-prod-ucws
def test_spog_unified_host_sends_workspace_id_header(isolated_env):
    """Verify wire-level header behavior of the workspace-id migration on a real unified host.

    Mirrors the Go SDK's TestAccUnifiedHostSendsWorkspaceIdHeader in
    internal/unified_host_test.go. Probes the SCIM Me endpoint and inspects the
    actual headers that cross the wire:
      1. SDK sends the new X-Databricks-Workspace-Id routing header on
         workspace-scoped requests
      2. SDK no longer sends the legacy X-Databricks-Org-Id request header
      3. Server still echoes the legacy X-Databricks-Org-Id on the response,
         since the server-side migration has not yet happened (this is why
         WorkspaceClient.get_workspace_id() still reads the legacy name).
    """
    env = isolated_env("ucws")
    host = env("UNIFIED_HOST")
    client_id = env("TEST_DATABRICKS_CLIENT_ID")
    client_secret = env("TEST_DATABRICKS_CLIENT_SECRET")
    workspace_id = env("THIS_WORKSPACE_ID")
    account_id = env("TEST_ACCOUNT_ID")

    me_path = "/api/2.0/preview/scim/v2/Me"

    ws = WorkspaceClient(
        host=host,
        client_id=client_id,
        client_secret=client_secret,
        workspace_id=workspace_id,
        account_id=account_id,
        auth_type="oauth-m2m",
    )

    # Mount a capture adapter on the SDK's session for wire-level header inspection.
    transport = _CaptureHeadersAdapter(me_path)
    ws._api_client._api_client._session.mount("https://", transport)

    # (1) Workspace-scoped probe against the unified host must succeed.
    me = ws.current_user.me()
    assert me.user_name, "Me should return a non-empty user_name"

    assert transport.req_headers is not None, f"transport did not observe a request to {me_path}"

    # (2) Request side: SDK must send the new header and not the legacy one.
    assert (
        transport.req_headers.get("X-Databricks-Workspace-Id") == workspace_id
    ), "SDK must send X-Databricks-Workspace-Id with Config.workspace_id"
    assert (
        "X-Databricks-Org-Id" not in transport.req_headers
    ), "SDK must no longer send the legacy X-Databricks-Org-Id request header"

    # (3) Response side: server still echoes the legacy header name during the migration.
    assert (
        "X-Databricks-Org-Id" in transport.resp_headers
    ), "server is expected to still echo the legacy X-Databricks-Org-Id response header during the migration"
