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


def test_spog_workspace_oauth_m2m(env_or_skip):
    ws = WorkspaceClient(
        host=env_or_skip("UNIFIED_HOST"),
        client_id=env_or_skip("TEST_DATABRICKS_CLIENT_ID"),
        client_secret=env_or_skip("TEST_DATABRICKS_CLIENT_SECRET"),
        workspace_id=env_or_skip("THIS_WORKSPACE_ID"),
        auth_type="oauth-m2m",
    )
    me = ws.current_user.me()
    assert me.user_name


def test_spog_workspace_azure_client_secret(env_or_skip):
    ws = WorkspaceClient(
        host=env_or_skip("UNIFIED_HOST"),
        workspace_id=env_or_skip("THIS_WORKSPACE_ID"),
        azure_client_id=env_or_skip("ARM_CLIENT_ID"),
        azure_client_secret=env_or_skip("ARM_CLIENT_SECRET"),
        azure_tenant_id=env_or_skip("ARM_TENANT_ID"),
        auth_type="azure-client-secret",
    )
    me = ws.current_user.me()
    assert me.user_name


def test_spog_workspace_google_credentials(env_or_skip):
    ws = WorkspaceClient(
        host=env_or_skip("UNIFIED_HOST"),
        workspace_id=env_or_skip("THIS_WORKSPACE_ID"),
        google_credentials=env_or_skip("GOOGLE_CREDENTIALS"),
        google_service_account=env_or_skip("DATABRICKS_GOOGLE_SERVICE_ACCOUNT"),
        auth_type="google-credentials",
    )
    me = ws.current_user.me()
    assert me.user_name


def test_spog_workspace_pat(env_or_skip):
    ws = WorkspaceClient(
        host=env_or_skip("UNIFIED_HOST"),
        workspace_id=env_or_skip("THIS_WORKSPACE_ID"),
        token=env_or_skip("TEST_SP_TOKEN"),
    )
    me = ws.current_user.me()
    assert me.user_name


# SPOG/A — Account operations on unified host with explicit auth


def test_spog_account_oauth_m2m(env_or_skip):
    ac = AccountClient(
        host=env_or_skip("UNIFIED_HOST"),
        account_id=env_or_skip("DATABRICKS_ACCOUNT_ID"),
        client_id=env_or_skip("TEST_DATABRICKS_CLIENT_ID"),
        client_secret=env_or_skip("TEST_DATABRICKS_CLIENT_SECRET"),
        auth_type="oauth-m2m",
    )
    sps = ac.service_principals.list()
    next(sps)


def test_spog_account_azure_client_secret(env_or_skip):
    ac = AccountClient(
        host=env_or_skip("UNIFIED_HOST"),
        account_id=env_or_skip("DATABRICKS_ACCOUNT_ID"),
        azure_client_id=env_or_skip("ARM_CLIENT_ID"),
        azure_client_secret=env_or_skip("ARM_CLIENT_SECRET"),
        azure_tenant_id=env_or_skip("ARM_TENANT_ID"),
        auth_type="azure-client-secret",
    )
    sps = ac.service_principals.list()
    next(sps)


def test_spog_account_google_credentials(env_or_skip):
    ac = AccountClient(
        host=env_or_skip("UNIFIED_HOST"),
        account_id=env_or_skip("DATABRICKS_ACCOUNT_ID"),
        google_credentials=env_or_skip("GOOGLE_CREDENTIALS"),
        google_service_account=env_or_skip("DATABRICKS_GOOGLE_SERVICE_ACCOUNT"),
        auth_type="google-credentials",
    )
    sps = ac.service_principals.list()
    next(sps)
