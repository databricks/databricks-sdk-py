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
    _skip_if_not_environment_type("ACCOUNT", "UC_ACCOUNT")
    return AccountClient()


@pytest.fixture(scope="session")
def ucacct(env_or_skip) -> AccountClient:
    _load_debug_env_if_runs_from_ide("ucacct")
    env_or_skip("CLOUD_ENV")
    _skip_if_not_environment_type("UC_ACCOUNT")
    return AccountClient()


@pytest.fixture(scope="session")
def unified_config(env_or_skip) -> Config:
    _load_debug_env_if_runs_from_ide("account")
    env_or_skip("CLOUD_ENV")
    config = Config()
    config.host = env_or_skip("UNIFIED_HOST")
    config.workspace_id = env_or_skip("TEST_WORKSPACE_ID")
    config.experimental_is_unified_host = True
    config._fix_host_if_needed()
    return config


@pytest.fixture(scope="session")
def w(env_or_skip) -> WorkspaceClient:
    _load_debug_env_if_runs_from_ide("workspace")
    env_or_skip("CLOUD_ENV")
    _skip_if_not_environment_type("WORKSPACE", "UC_WORKSPACE")
    return WorkspaceClient()


@pytest.fixture(scope="session")
def ucws(env_or_skip) -> WorkspaceClient:
    _load_debug_env_if_runs_from_ide("ucws")
    env_or_skip("CLOUD_ENV")
    _skip_if_not_environment_type("UC_WORKSPACE")
    return WorkspaceClient()


@pytest.fixture
def isolated_env(monkeypatch):
    """Fixture for tests that need to construct a client with explicit parameters
    only, without Config picking up env vars automatically.

    Usage:
        def test_something(isolated_env):
            env = isolated_env("workspace")  # loads debug-env key when running from IDE
            host = env("UNIFIED_HOST")

    The first call takes a debug-env key (used only when running from an IDE).
    Returns a callable that looks up vars from the original environment snapshot
    (skipping the test if missing). All Config-related env vars are removed so
    the client only sees explicitly passed parameters."""

    def init(debug_env_key: str):
        _load_debug_env_if_runs_from_ide(debug_env_key)
        original_env = os.environ.copy()

        for attr in vars(Config).values():
            if isinstance(attr, ConfigAttribute) and attr.env:
                monkeypatch.delenv(attr.env, raising=False)

        def get(var: str) -> str:
            if var not in original_env:
                pytest.skip(f"Environment variable {var} is missing")
            return original_env[var]

        return get

    return init


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


def _skip_if_not_environment_type(*expected_types: str):
    """Skip the test if TEST_ENVIRONMENT_TYPE doesn't match any of the expected types.

    TEST_ENVIRONMENT_TYPE values: "ACCOUNT", "WORKSPACE", "UC_ACCOUNT", "UC_WORKSPACE".
    """
    env_type = os.getenv("TEST_ENVIRONMENT_TYPE", "")
    if not env_type:
        pytest.skip("Skipping test because TEST_ENVIRONMENT_TYPE is not set")
    if env_type not in expected_types:
        pytest.skip(f"Skipping {'/'.join(expected_types)} test in {env_type} environment")


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
