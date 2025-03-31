import pytest

from .conftest import _load_debug_env_if_runs_from_ide


@pytest.fixture(scope="session")
def env(env_or_skip):
    if not _load_debug_env_if_runs_from_ide("workspace"):
        pytest.skip("runnable only on dev machines")
    return env_or_skip


def test_pkce_app(env):
    from databricks.sdk.compute.v2.client import ClustersClient
    cc = ClustersClient(
        host=env("DATABRICKS_HOST"),
        client_id=env("TEST_PKCE_APP_CLIENT_ID"),
        auth_type="external-browser",
    )
    clusters = cc.list()
    for cl in clusters:
        print(f" - {cl.cluster_name} is {cl.state}")


def test_public_app(env):
    from databricks.sdk.compute.v2.client import ClustersClient
    cc = ClustersClient(
        host=env("DATABRICKS_HOST"),
        client_id=env("TEST_PUBLIC_APP_CLIENT_ID"),
        auth_type="external-browser",
    )
    clusters = cc.list()
    for cl in clusters:
        print(f" - {cl.cluster_name} is {cl.state}")


def test_private_app(env):
    from databricks.sdk.compute.v2.client import ClustersClient
    cc = ClustersClient(
        host=env("DATABRICKS_HOST"),
        client_id=env("TEST_PRIVATE_APP_CLIENT_ID"),
        client_secret=env("TEST_PRIVATE_APP_CLIENT_SECRET"),
        auth_type="external-browser",
    )
    clusters = cc.list()
    for cl in clusters:
        print(f" - {cl.cluster_name} is {cl.state}")
