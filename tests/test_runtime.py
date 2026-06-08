"""Tests for the import-time behavior of the ``databricks.sdk.runtime`` package."""

import importlib
import sys
import types

import pytest


class _RemoteClientInitializer:
    """Stand-in for ``dbruntime.UserNamespaceInitializer`` on a Spark Connect runtime.

    On a shared-access-mode (Spark Connect) cluster, materializing the legacy user namespace
    builds a ``SparkContext``, which is unavailable in remote clients and raises
    ``CONTEXT_UNAVAILABLE_FOR_REMOTE_CLIENT``.
    """

    @staticmethod
    def getOrCreate():
        class _Namespace:
            def get_namespace_globals(self):
                raise RuntimeError(
                    "[CONTEXT_UNAVAILABLE_FOR_REMOTE_CLIENT] Calls to SparkContext are not "
                    "supported on a Spark Connect cluster. Use spark instead."
                )

        return _Namespace()


@pytest.fixture
def spark_connect_runtime(monkeypatch):
    """Simulate a Spark Connect runtime: ``dbruntime`` is importable, but materializing the
    legacy user namespace raises ``CONTEXT_UNAVAILABLE_FOR_REMOTE_CLIENT``."""
    fake = types.ModuleType("dbruntime")
    fake.UserNamespaceInitializer = _RemoteClientInitializer
    had_dbruntime = "dbruntime" in sys.modules
    saved_dbruntime = sys.modules.get("dbruntime")
    sys.modules["dbruntime"] = fake

    # The remote fallback constructs ``RemoteDbUtils()``, which initializes a default ``Config``;
    # give it hermetic PAT credentials so the fallback itself doesn't fail for unrelated auth
    # reasons (see databricks-sdk-py#986).
    monkeypatch.setenv("DATABRICKS_HOST", "https://test.cloud.databricks.com")
    monkeypatch.setenv("DATABRICKS_TOKEN", "test-token")

    saved_runtime = sys.modules.get("databricks.sdk.runtime")
    try:
        yield
    finally:
        if had_dbruntime:
            sys.modules["dbruntime"] = saved_dbruntime
        else:
            sys.modules.pop("dbruntime", None)
        # Restore ``databricks.sdk.runtime`` to its pre-test state. If it was loaded before this
        # test, reload it cleanly while the PAT env is still set; otherwise drop it so it is
        # re-imported lazily on next use.
        if saved_runtime is None:
            sys.modules.pop("databricks.sdk.runtime", None)
        else:
            importlib.reload(saved_runtime)


def test_runtime_import_survives_spark_connect_remote_client(spark_connect_runtime):
    """Regression for dbt-databricks#1252: importing ``databricks.sdk.runtime`` on a Spark
    Connect runtime must fall back to the remote implementation instead of raising."""
    import databricks.sdk.runtime as runtime

    importlib.reload(runtime)  # re-execute the module body with the faked ``dbruntime`` present

    assert runtime.is_local_implementation is True
    assert runtime.dbutils is not None


def test_workspace_client_constructs_on_spark_connect(spark_connect_runtime, config):
    """End-to-end: constructing a ``WorkspaceClient`` on a Spark Connect runtime must not raise
    ``CONTEXT_UNAVAILABLE_FOR_REMOTE_CLIENT`` (the actual dbt-databricks#1252 failure, since
    ``WorkspaceClient.__init__`` eagerly builds dbutils via ``databricks.sdk.runtime``)."""
    import databricks.sdk.runtime as runtime

    importlib.reload(runtime)

    from databricks.sdk import WorkspaceClient

    ws = WorkspaceClient(config=config)

    assert ws is not None
