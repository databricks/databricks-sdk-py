import json
import logging
import os
import pathlib
import string
import sys

import pytest

from databricks.sdk import FilesExt
from databricks.sdk.catalog.v2.catalog import VolumeType
from databricks.sdk.databricks.config import Config
from databricks.sdk.files.v2.files import FilesAPI


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
    client_fixtures = [x.__name__ for x in [a, w, ucws, ucacct]]
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
def a(env_or_skip) -> Config:
    _load_debug_env_if_runs_from_ide("account")
    env_or_skip("CLOUD_ENV")
    cfg = Config()
    if not cfg.is_account_client:
        pytest.skip("not Databricks Account client")
    return cfg


@pytest.fixture(scope="session")
def ucacct(env_or_skip) -> Config:
    _load_debug_env_if_runs_from_ide("ucacct")
    env_or_skip("CLOUD_ENV")
    cfg = Config()
    if not cfg.is_account_client:
        pytest.skip("not Databricks Account client")
    if "TEST_METASTORE_ID" not in os.environ:
        pytest.skip("not in Unity Catalog Workspace test env")
    return cfg


@pytest.fixture(scope="session")
def w(env_or_skip) -> Config:
    _load_debug_env_if_runs_from_ide("workspace")
    env_or_skip("CLOUD_ENV")
    if "DATABRICKS_ACCOUNT_ID" in os.environ:
        pytest.skip("Skipping workspace test on account level")
    return Config()


@pytest.fixture(scope="session")
def ucws(env_or_skip) -> Config:
    _load_debug_env_if_runs_from_ide("ucws")
    env_or_skip("CLOUD_ENV")
    if "DATABRICKS_ACCOUNT_ID" in os.environ:
        pytest.skip("Skipping workspace test on account level")
    if "TEST_METASTORE_ID" not in os.environ:
        pytest.skip("not in Unity Catalog Workspace test env")
    return Config()


@pytest.fixture(scope="session")
def env_or_skip():

    def inner(var: str) -> str:
        if var not in os.environ:
            pytest.skip(f"Environment variable {var} is missing")
        return os.environ[var]

    return inner


@pytest.fixture(scope="session")
def schema(ucws, random):
    from databricks.sdk.catalog.v2.client import SchemasClient

    sc = SchemasClient(config=ucws)
    schema = sc.create("dbfs-" + random(), "main")
    yield schema
    sc.delete(schema.full_name)


@pytest.fixture(scope="session")
def volume(ucws, schema):
    from databricks.sdk.catalog.v2.client import VolumesClient

    vc = VolumesClient(config=ucws)
    volume = vc.create("main", schema.name, "dbfs-test", VolumeType.MANAGED)
    yield "/Volumes/" + volume.full_name.replace(".", "/")
    vc.delete(volume.full_name)


@pytest.fixture(scope="session", params=[False, True])
def files_api(request, ucws) -> FilesAPI:

    if request.param:
        # ensure new Files API client is used for files of any size
        ucws.multipart_upload_min_stream_size = 0
        # enable new Files API client
        from databricks.sdk.databricks.core import ApiClient

        client = ApiClient(cfg=ucws)

        return FilesExt(client, ucws)
    else:
        # use the default client
        from databricks.sdk.databricks.core import ApiClient
        from databricks.sdk.files.v2.files import FilesAPI

        client = ApiClient(cfg=ucws)

        api = FilesAPI(api_client=client)
        return api


@pytest.fixture()
def workspace_dir(w, random):
    from databricks.sdk.iam.v2.client import CurrentUserClient
    from databricks.sdk.workspace.v2.client import WorkspaceClient

    cuc = CurrentUserClient(config=w)
    wc = WorkspaceClient(config=w)
    directory = f"/Users/{cuc.me().user_name}/dir-{random(12)}"
    wc.mkdirs(directory)
    yield directory
    wc.delete(directory, recursive=True)


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
        "run_pytest_script.py",
    ]


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
