import os

import pytest

from databricks.sdk import AccountClient, WorkspaceClient
from databricks.sdk.config import Config, ConfigAttribute


def test_workspace_operations(unified_config):
    client = WorkspaceClient(config=unified_config)
    user = client.current_user.me()
    assert user is not None


def test_account_operations(unified_config):
    client = AccountClient(config=unified_config)
    groups = client.groups.list()
    assert groups is not None


@pytest.fixture
def clean_env(monkeypatch):
    """Remove all Config-related env vars so that the client only sees
    explicitly passed parameters. Returns a callable that reads from the
    original environment (skipping if missing)."""
    # Snapshot the full environment before cleaning
    original_env = os.environ.copy()

    # Remove every env var that Config could read
    for attr in vars(Config).values():
        if isinstance(attr, ConfigAttribute) and attr.env:
            monkeypatch.delenv(attr.env, raising=False)

    def get(var: str) -> str:
        if var not in original_env:
            pytest.skip(f"Environment variable {var} is missing")
        return original_env[var]

    return get


# SPOG/W — Workspace operations on unified host with explicit auth
# Environments: azure-prod-ucws (oauth-m2m), azure-prod/azure-prod-ucws (azure-client-secret),
#               gcp-prod/gcp-prod-ucws (google-credentials), aws-prod/gcp-prod (pat)


def test_spog_workspace_oauth_m2m(clean_env):
    host = clean_env("UNIFIED_HOST")
    client_id = clean_env("TEST_DATABRICKS_CLIENT_ID")
    client_secret = clean_env("TEST_DATABRICKS_CLIENT_SECRET")
    workspace_id = clean_env("THIS_WORKSPACE_ID")
    account_id = clean_env("TEST_ACCOUNT_ID")
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


def test_spog_workspace_azure_client_secret(clean_env):
    host = clean_env("UNIFIED_HOST")
    workspace_id = clean_env("THIS_WORKSPACE_ID")
    account_id = clean_env("TEST_ACCOUNT_ID")
    azure_client_id = clean_env("ARM_CLIENT_ID")
    azure_client_secret = clean_env("ARM_CLIENT_SECRET")
    azure_tenant_id = clean_env("ARM_TENANT_ID")
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


def test_spog_workspace_google_credentials(clean_env):
    host = clean_env("UNIFIED_HOST")
    workspace_id = clean_env("THIS_WORKSPACE_ID")
    account_id = clean_env("TEST_ACCOUNT_ID")
    google_credentials = clean_env("GOOGLE_CREDENTIALS")
    google_service_account = clean_env("DATABRICKS_GOOGLE_SERVICE_ACCOUNT")
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


def test_spog_workspace_pat(clean_env):
    host = clean_env("UNIFIED_HOST")
    workspace_id = clean_env("THIS_WORKSPACE_ID")
    account_id = clean_env("TEST_ACCOUNT_ID")
    token = clean_env("TEST_SP_TOKEN")
    ws = WorkspaceClient(
        host=host,
        workspace_id=workspace_id,
        account_id=account_id,
        token=token,
    )
    me = ws.current_user.me()
    assert me.user_name


# SPOG/A — Account operations on unified host with explicit auth
# Environments: azure-prod-acct (oauth-m2m, azure-client-secret),
#               gcp-acct-prod/gcp-prod-ucacct (google-credentials)


def test_spog_account_oauth_m2m(clean_env):
    host = clean_env("UNIFIED_HOST")
    account_id = clean_env("DATABRICKS_ACCOUNT_ID")
    client_id = clean_env("TEST_DATABRICKS_CLIENT_ID")
    client_secret = clean_env("TEST_DATABRICKS_CLIENT_SECRET")
    ac = AccountClient(
        host=host,
        account_id=account_id,
        client_id=client_id,
        client_secret=client_secret,
        auth_type="oauth-m2m",
    )
    sps = ac.service_principals.list()
    next(sps)


def test_spog_account_azure_client_secret(clean_env):
    host = clean_env("UNIFIED_HOST")
    account_id = clean_env("DATABRICKS_ACCOUNT_ID")
    azure_client_id = clean_env("ARM_CLIENT_ID")
    azure_client_secret = clean_env("ARM_CLIENT_SECRET")
    azure_tenant_id = clean_env("ARM_TENANT_ID")
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


def test_spog_account_google_credentials(clean_env):
    host = clean_env("UNIFIED_HOST")
    account_id = clean_env("DATABRICKS_ACCOUNT_ID")
    google_credentials = clean_env("GOOGLE_CREDENTIALS")
    google_service_account = clean_env("DATABRICKS_GOOGLE_SERVICE_ACCOUNT")
    ac = AccountClient(
        host=host,
        account_id=account_id,
        google_credentials=google_credentials,
        google_service_account=google_service_account,
        auth_type="google-credentials",
    )
    sps = ac.service_principals.list()
    next(sps)
