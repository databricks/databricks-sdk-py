import json
import logging
import os
import pathlib
import string
import sys

import pytest

from databricks.sdk import AccountClient, FilesAPI, FilesExt, WorkspaceClient
from databricks.sdk.config import ConfigAttribute
from databricks.sdk.core import Config
from databricks.sdk.environments import Cloud
from databricks.sdk.service.catalog import VolumeType


@pytest.fixture(autouse=True)
def stub_host_metadata():
    """Override root conftest stub — integration tests hit real endpoints."""


def pytest_addoption(parser):
    # make logging sensible and readable.
    parser.addini(
        "log_format",
        "...",
        "string",
        "%(asctime)s [%(name)s][%(levelname)s] %(message)s",
    )
    parser.addini("log_date_format", "...", "string", "%H:%M")


def pytest_configure(config):
    # disable urllib3, as it adds more noise
    logger = logging.getLogger("urllib3.connectionpool")
    logger.propagate = False

    config.addinivalue_line(
        "markers",
        "integration: marks tests as those requiring a real Databricks backend",
    )
    config.addinivalue_line(
        "markers",
        "benchmark: marks tests as benchmarks which should not be run by default",
    )


def pytest_collection_modifyitems(items):
    # safer to refer to fixture fns instead of strings
    client_fixtures = [x.__name__ for x in [a, w, ucws, ucacct, unified_config, isolated_env]]
    for item in items:
        current_fixtures = getattr(item, "fixturenames", ())
        for requires_client in client_fixtures:
            if requires_client in current_fixtures:
                item.add_marker("integration")


@pytest.fixture(scope="session")
def random():
    import random

    def inner(k=16) -> str:
        charset = string.ascii_uppercase + string.ascii_lowercase + string.digits
        return "".join(random.choices(charset, k=int(k)))

    return inner


@pytest.fixture(scope="session")
def a(env_or_skip) -> AccountClient:
    _load_debug_env_if_runs_from_ide("account")
    env_or_skip("CLOUD_ENV")
    account_client = AccountClient()
    if env_or_skip("TEST_ENVIRONMENT_TYPE") not in ["ACCOUNT", "UC_ACCOUNT"]:
        pytest.skip("not Databricks Account environment")
    return account_client


@pytest.fixture(scope="session")
def ucacct(env_or_skip) -> AccountClient:
    _load_debug_env_if_runs_from_ide("ucacct")
    env_or_skip("CLOUD_ENV")
    account_client = AccountClient()
    if env_or_skip("TEST_ENVIRONMENT_TYPE") not in ["UC_ACCOUNT"]:
        pytest.skip("not Databricks UC Account environment")
    if "TEST_METASTORE_ID" not in os.environ:
        pytest.skip("not in Unity Catalog Workspace test env")
    return account_client


@pytest.fixture(scope="session")
def unified_config(env_or_skip) -> Config:
    _load_debug_env_if_runs_from_ide("account")
    env_or_skip("CLOUD_ENV")
    config = Config()
    config.workspace_id = env_or_skip("TEST_WORKSPACE_ID")
    config.experimental_is_unified_host = True
    return config


@pytest.fixture(scope="session")
def w(env_or_skip) -> WorkspaceClient:
    _load_debug_env_if_runs_from_ide("workspace")
    env_or_skip("CLOUD_ENV")
    if env_or_skip("TEST_ENVIRONMENT_TYPE") not in ["WORKSPACE", "UC_WORKSPACE"]:
        pytest.skip("not Databricks Workspace environment")
    return WorkspaceClient()


@pytest.fixture(scope="session")
def ucws(env_or_skip) -> WorkspaceClient:
    _load_debug_env_if_runs_from_ide("ucws")
    env_or_skip("CLOUD_ENV")
    if env_or_skip("TEST_ENVIRONMENT_TYPE") not in ["UC_WORKSPACE"]:
        pytest.skip("not Databricks UC Workspace environment")
    if "TEST_METASTORE_ID" not in os.environ:
        pytest.skip("not Databricks UC Workspace environment")
    return WorkspaceClient()


@pytest.fixture
def isolated_env(monkeypatch):
    """Fixture for tests that need to construct a client with explicit parameters
    only, without Config picking up env vars automatically.

    Snapshots os.environ, then removes every env var that Config could read.
    Returns a callable that looks up vars from the original snapshot
    (skipping the test if missing)."""
    original_env = os.environ.copy()

    for attr in vars(Config).values():
        if isinstance(attr, ConfigAttribute) and attr.env:
            monkeypatch.delenv(attr.env, raising=False)

    def get(var: str) -> str:
        if var not in original_env:
            pytest.skip(f"Environment variable {var} is missing")
        return original_env[var]

    return get


@pytest.fixture(scope="session")
def env_or_skip():

    def inner(var: str) -> str:
        if var not in os.environ:
            pytest.skip(f"Environment variable {var} is missing")
        return os.environ[var]

    return inner


@pytest.fixture(scope="session")
def schema(ucws, random):
    schema = ucws.schemas.create("dbfs-" + random(), "main")
    yield schema
    ucws.schemas.delete(schema.full_name)


@pytest.fixture(scope="session")
def volume(ucws, schema):
    volume = ucws.volumes.create("main", schema.name, "dbfs-test", VolumeType.MANAGED)
    yield "/Volumes/" + volume.full_name.replace(".", "/")
    ucws.volumes.delete(volume.full_name)


@pytest.fixture(scope="session", params=[False, True])
def files_api(request, ucws) -> FilesAPI:
    if request.param:
        # ensure new Files API client is used for files of any size
        ucws.config.multipart_upload_min_stream_size = 0
        # enable new Files API client
        return FilesExt(ucws.api_client, ucws.config)
    else:
        # use the default client
        return ucws.files


@pytest.fixture()
def workspace_dir(w, random):
    directory = f"/Users/{w.current_user.me().user_name}/dir-{random(12)}"
    w.workspace.mkdirs(directory)
    yield directory
    w.workspace.delete(directory, recursive=True)


def _load_debug_env_if_runs_from_ide(key) -> bool:
    if not _is_in_debug():
        return False
    conf_file = pathlib.Path.home() / ".databricks/debug-env.json"
    with conf_file.open("r") as f:
        conf = json.load(f)
        if key not in conf:
            raise KeyError(f"{key} not found in ~/.databricks/debug-env.json")
        for k, v in conf[key].items():
            os.environ[k] = v
    return True


def _is_in_debug() -> bool:
    return os.path.basename(sys.argv[0]) in [
        "_jb_pytest_runner.py",
        "testlauncher.py",
    ]


def _is_cloud(cloud: Cloud) -> bool:
    """Check if the CLOUD_PROVIDER environment variable matches the specified cloud provider."""
    cloud_provider = os.getenv("CLOUD_PROVIDER", "").upper()
    cloud_upper = cloud.value.upper()
    return cloud_provider == cloud_upper


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
