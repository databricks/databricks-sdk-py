from databricks.sdk import AccountClient, WorkspaceClient


def test_workspace_operations(unified_config):
    client = WorkspaceClient(config=unified_config)
    user = client.current_user.me()
    assert user is not None


def test_account_operations(unified_config):
    client = AccountClient(config=unified_config)
    groups = client.groups.list()
    assert groups is not None


# SPOG/W — Workspace operations on unified host with explicit auth


# Environment: azure-prod-ucws
def test_spog_workspace_oauth_m2m(isolated_env):
    host = isolated_env("UNIFIED_HOST")
    client_id = isolated_env("TEST_DATABRICKS_CLIENT_ID")
    client_secret = isolated_env("TEST_DATABRICKS_CLIENT_SECRET")
    workspace_id = isolated_env("THIS_WORKSPACE_ID")
    account_id = isolated_env("TEST_ACCOUNT_ID")
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


# Environment: azure-prod, azure-prod-ucws
def test_spog_workspace_azure_client_secret(isolated_env):
    host = isolated_env("UNIFIED_HOST")
    workspace_id = isolated_env("THIS_WORKSPACE_ID")
    account_id = isolated_env("TEST_ACCOUNT_ID")
    azure_client_id = isolated_env("ARM_CLIENT_ID")
    azure_client_secret = isolated_env("ARM_CLIENT_SECRET")
    azure_tenant_id = isolated_env("ARM_TENANT_ID")
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


# Environment: gcp-prod, gcp-prod-ucws
def test_spog_workspace_google_credentials(isolated_env):
    host = isolated_env("UNIFIED_HOST")
    workspace_id = isolated_env("THIS_WORKSPACE_ID")
    account_id = isolated_env("TEST_ACCOUNT_ID")
    google_credentials = isolated_env("GOOGLE_CREDENTIALS")
    google_service_account = isolated_env("DATABRICKS_GOOGLE_SERVICE_ACCOUNT")
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


# Environment: aws-prod, gcp-prod, gcp-prod-ucws
def test_spog_workspace_pat(isolated_env):
    host = isolated_env("UNIFIED_HOST")
    workspace_id = isolated_env("THIS_WORKSPACE_ID")
    account_id = isolated_env("TEST_ACCOUNT_ID")
    token = isolated_env("TEST_SP_TOKEN")
    ws = WorkspaceClient(
        host=host,
        workspace_id=workspace_id,
        account_id=account_id,
        token=token,
    )
    me = ws.current_user.me()
    assert me.user_name


# SPOG/A — Account operations on unified host with explicit auth


# Environment: azure-prod-acct
def test_spog_account_oauth_m2m(isolated_env):
    host = isolated_env("UNIFIED_HOST")
    account_id = isolated_env("DATABRICKS_ACCOUNT_ID")
    client_id = isolated_env("TEST_DATABRICKS_CLIENT_ID")
    client_secret = isolated_env("TEST_DATABRICKS_CLIENT_SECRET")
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
    host = isolated_env("UNIFIED_HOST")
    account_id = isolated_env("DATABRICKS_ACCOUNT_ID")
    azure_client_id = isolated_env("ARM_CLIENT_ID")
    azure_client_secret = isolated_env("ARM_CLIENT_SECRET")
    azure_tenant_id = isolated_env("ARM_TENANT_ID")
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


# Environment: gcp-acct-prod, gcp-prod-ucacct
def test_spog_account_google_credentials(isolated_env):
    host = isolated_env("UNIFIED_HOST")
    account_id = isolated_env("DATABRICKS_ACCOUNT_ID")
    google_credentials = isolated_env("GOOGLE_CREDENTIALS")
    google_service_account = isolated_env("DATABRICKS_GOOGLE_SERVICE_ACCOUNT")
    ac = AccountClient(
        host=host,
        account_id=account_id,
        google_credentials=google_credentials,
        google_service_account=google_service_account,
        auth_type="google-credentials",
    )
    sps = ac.service_principals.list()
    next(sps)
