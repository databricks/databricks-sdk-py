import pytest  # type: ignore[import-not-found]

from databricks.sdk import WorkspaceClient

from .conftest import _load_debug_env_if_runs_from_ide


@pytest.fixture(scope="session")
def env(env_or_skip):  # type: ignore[no-untyped-def]
    if not _load_debug_env_if_runs_from_ide("workspace"):
        pytest.skip("runnable only on dev machines")
    return env_or_skip


def test_pkce_app(env):  # type: ignore[no-untyped-def]
    w = WorkspaceClient(
        host=env("DATABRICKS_HOST"),
        client_id=env("TEST_PKCE_APP_CLIENT_ID"),
        auth_type="external-browser",
    )
    clusters = w.clusters.list()
    for cl in clusters:
        print(f" - {cl.cluster_name} is {cl.state}")


def test_public_app(env):  # type: ignore[no-untyped-def]
    w = WorkspaceClient(
        host=env("DATABRICKS_HOST"),
        client_id=env("TEST_PUBLIC_APP_CLIENT_ID"),
        auth_type="external-browser",
    )
    clusters = w.clusters.list()
    for cl in clusters:
        print(f" - {cl.cluster_name} is {cl.state}")


def test_private_app(env):  # type: ignore[no-untyped-def]
    w = WorkspaceClient(
        host=env("DATABRICKS_HOST"),
        client_id=env("TEST_PRIVATE_APP_CLIENT_ID"),
        client_secret=env("TEST_PRIVATE_APP_CLIENT_SECRET"),
        auth_type="external-browser",
    )
    clusters = w.clusters.list()
    for cl in clusters:
        print(f" - {cl.cluster_name} is {cl.state}")
