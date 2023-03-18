import json
import os
import pathlib
import string
import sys

import pytest

from databricks.sdk import AccountClient, WorkspaceClient


@pytest.fixture
def random():
    import random

    def inner(k=16) -> str:
        charset = string.ascii_uppercase + string.ascii_lowercase + string.digits
        return ''.join(random.choices(charset, k=int(k)))

    return inner


@pytest.fixture
def a() -> AccountClient:
    _load_debug_env_if_runs_from_ide('account')
    account_client = AccountClient()
    if not account_client.config.is_account_client:
        pytest.skip("not Databricks Account client")
    return account_client


@pytest.fixture
def w() -> WorkspaceClient:
    _load_debug_env_if_runs_from_ide('workspace')
    if 'DATABRICKS_ACCOUNT_ID' in os.environ:
        pytest.skip("Skipping workspace test on account level")
    return WorkspaceClient()


@pytest.fixture
def ucws() -> WorkspaceClient:
    _load_debug_env_if_runs_from_ide('ucws')
    if 'TEST_METASTORE_ID' not in os.environ:
        pytest.skip("not in Unity Catalog Workspace test env")
    return WorkspaceClient()


@pytest.fixture
def env_or_skip():

    def inner(var) -> str:
        if var not in os.environ:
            pytest.skip(f'Environment variable {var} is missing')
        return os.environ[var]

    return inner


def _load_debug_env_if_runs_from_ide(key):
    if not _is_in_debug():
        return
    conf_file = pathlib.Path.home() / '.databricks/debug-env.json'
    with conf_file.open('r') as f:
        conf = json.load(f)
        if key not in conf:
            raise KeyError(f'{key} not found in ~/.databricks/debug-env.json')
        for k, v in conf[key].items():
            os.environ[k] = v


def _is_in_debug() -> bool:
    return os.path.basename(sys.argv[0]) == '_jb_pytest_runner.py'
