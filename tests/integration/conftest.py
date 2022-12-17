import json
import os
import pathlib
import sys

import pytest
from databricks.sdk import AccountClient, WorkspaceClient


@pytest.fixture()
def account_client() -> AccountClient:
    load_debug_env_if_runs_from_ide('account')
    account_client = AccountClient()
    if not account_client.api_client.is_account_client:
        pytest.skip("not Databricks Account client")
    return account_client


@pytest.fixture
def workspace_client() -> WorkspaceClient:
    load_debug_env_if_runs_from_ide('workspace')
    if 'DATABRICKS_ACCOUNT_ID' in os.environ:
        pytest.skip("Skipping workspace test on account level")
    return WorkspaceClient()


@pytest.fixture
def env_or_skip():
    def inner(var) -> str:
        if var not in os.environ:
            pytest.skip(f'Environment variable {var} is missing')
        return os.environ[var]
    return inner


def load_debug_env_if_runs_from_ide(key):
    if not is_in_debug():
        return
    conf_file = pathlib.Path.home() / '.databricks/debug-env.json'
    with conf_file.open('r') as f:
        conf = json.load(f)
        if key not in conf:
            raise KeyError(f'{key} not found in ~/.databricks/debug-env.json')
        for k,v in conf[key].items():
            os.environ[k] = v


def is_in_debug() -> bool:
    return os.path.basename(sys.argv[0]) == '_jb_pytest_runner.py'
