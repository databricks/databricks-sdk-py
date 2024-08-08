import json
import logging
import os
import pathlib
import string
import sys

import pytest

from databricks.sdk import AccountClient, WorkspaceClient
from databricks.sdk.service.catalog import VolumeType


def pytest_addoption(parser):
    # make logging sensible and readable.
    parser.addini('log_format', '...', 'string', '%(asctime)s [%(name)s][%(levelname)s] %(message)s')
    parser.addini('log_date_format', '...', 'string', '%H:%M')


def pytest_configure(config):
    # disable urllib3, as it adds more noise
    logger = logging.getLogger('urllib3.connectionpool')
    logger.propagate = False

    config.addinivalue_line('markers',
                            'integration: marks tests as those requiring a real Databricks backend')
    config.addinivalue_line('markers',
                            'benchmark: marks tests as benchmarks which should not be run by default')


def pytest_collection_modifyitems(items):
    # safer to refer to fixture fns instead of strings
    client_fixtures = [x.__name__ for x in [a, w, ucws]]
    for item in items:
        current_fixtures = getattr(item, 'fixturenames', ())
        for requires_client in client_fixtures:
            if requires_client in current_fixtures:
                item.add_marker('integration')


@pytest.fixture(scope='session')
def random():
    import random

    def inner(k=16) -> str:
        charset = string.ascii_uppercase + string.ascii_lowercase + string.digits
        return ''.join(random.choices(charset, k=int(k)))

    return inner


@pytest.fixture(scope='session')
def a(env_or_skip) -> AccountClient:
    _load_debug_env_if_runs_from_ide('account')
    env_or_skip("CLOUD_ENV")
    account_client = AccountClient()
    if not account_client.config.is_account_client:
        pytest.skip("not Databricks Account client")
    return account_client


@pytest.fixture(scope='session')
def ucacct(env_or_skip) -> AccountClient:
    _load_debug_env_if_runs_from_ide('ucacct')
    env_or_skip("CLOUD_ENV")
    account_client = AccountClient()
    if not account_client.config.is_account_client:
        pytest.skip("not Databricks Account client")
    if 'TEST_METASTORE_ID' not in os.environ:
        pytest.skip("not in Unity Catalog Workspace test env")
    return account_client


@pytest.fixture(scope='session')
def w(env_or_skip) -> WorkspaceClient:
    _load_debug_env_if_runs_from_ide('workspace')
    env_or_skip("CLOUD_ENV")
    if 'DATABRICKS_ACCOUNT_ID' in os.environ:
        pytest.skip("Skipping workspace test on account level")
    return WorkspaceClient()


@pytest.fixture(scope='session')
def ucws(env_or_skip) -> WorkspaceClient:
    _load_debug_env_if_runs_from_ide('ucws')
    env_or_skip("CLOUD_ENV")
    if 'DATABRICKS_ACCOUNT_ID' in os.environ:
        pytest.skip("Skipping workspace test on account level")
    if 'TEST_METASTORE_ID' not in os.environ:
        pytest.skip("not in Unity Catalog Workspace test env")
    return WorkspaceClient()


@pytest.fixture(scope='session')
def env_or_skip():

    def inner(var: str) -> str:
        if var not in os.environ:
            pytest.skip(f'Environment variable {var} is missing')
        return os.environ[var]

    return inner


@pytest.fixture(scope='session')
def schema(ucws, random):
    schema = ucws.schemas.create('dbfs-' + random(), 'main')
    yield schema
    ucws.schemas.delete(schema.full_name)


@pytest.fixture(scope='session')
def volume(ucws, schema):
    volume = ucws.volumes.create('main', schema.name, 'dbfs-test', VolumeType.MANAGED)
    yield '/Volumes/' + volume.full_name.replace(".", "/")
    ucws.volumes.delete(volume.full_name)


@pytest.fixture()
def workspace_dir(w, random):
    directory = f'/Users/{w.current_user.me().user_name}/dir-{random(12)}'
    w.workspace.mkdirs(directory)
    yield directory
    w.workspace.delete(directory, recursive=True)


def _load_debug_env_if_runs_from_ide(key) -> bool:
    if not _is_in_debug():
        return False
    conf_file = pathlib.Path.home() / '.databricks/debug-env.json'
    with conf_file.open('r') as f:
        conf = json.load(f)
        if key not in conf:
            raise KeyError(f'{key} not found in ~/.databricks/debug-env.json')
        for k, v in conf[key].items():
            os.environ[k] = v
    return True


def _is_in_debug() -> bool:
    return os.path.basename(sys.argv[0]) in ['_jb_pytest_runner.py', 'testlauncher.py', ]


@pytest.fixture(scope="function")
def restorable_env():
    import os
    current_env = os.environ.copy()
    yield
    for k, v in os.environ.items():
        if k not in current_env:
            del os.environ[k]
        elif v != current_env[k]:
            os.environ[k] = current_env[k]
