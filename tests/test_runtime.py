"""Tests for the import-time behavior of ``databricks.sdk.runtime``."""

import importlib
import sys
import types

import pytest

from databricks.sdk.dbutils import RemoteDbUtils


@pytest.fixture
def spark_connect_runtime(monkeypatch):
    """``dbruntime`` is importable, but materializing the legacy user namespace raises
    ``CONTEXT_UNAVAILABLE_FOR_REMOTE_CLIENT`` — the Spark Connect failure mode."""

    class _Initializer:
        @staticmethod
        def getOrCreate():
            class _Namespace:
                def get_namespace_globals(self):
                    raise RuntimeError(
                        "[CONTEXT_UNAVAILABLE_FOR_REMOTE_CLIENT] Calls to SparkContext are "
                        "not supported on a Spark Connect cluster. Use spark instead."
                    )

            return _Namespace()

    fake = types.ModuleType("dbruntime")
    fake.UserNamespaceInitializer = _Initializer
    monkeypatch.setitem(sys.modules, "dbruntime", fake)

    # The remote fallback constructs ``RemoteDbUtils()``, which initializes a default
    # ``Config``; hermetic PAT credentials keep the fallback from failing for unrelated
    # auth reasons (see databricks-sdk-py#986).
    monkeypatch.setenv("DATABRICKS_HOST", "https://test.cloud.databricks.com")
    monkeypatch.setenv("DATABRICKS_TOKEN", "test-token")

    # Re-execute ``databricks.sdk.runtime``'s module body with the fake ``dbruntime`` in
    # place, then restore on teardown by reloading once more without it.
    import databricks.sdk.runtime

    importlib.reload(databricks.sdk.runtime)
    yield
    importlib.reload(databricks.sdk.runtime)


def test_runtime_import_falls_back_on_spark_connect(spark_connect_runtime):
    """Regression for dbt-databricks#1252: import survives the namespace failure."""
    import databricks.sdk.runtime as runtime

    assert runtime.is_local_implementation is True
    assert isinstance(runtime.dbutils, RemoteDbUtils)


def test_workspace_client_constructs_on_spark_connect(spark_connect_runtime, config):
    """Regression for dbt-databricks#1252: ``WorkspaceClient.__init__`` eagerly builds
    dbutils via ``databricks.sdk.runtime`` and must not raise on Spark Connect."""
    from databricks.sdk import WorkspaceClient

    ws = WorkspaceClient(config=config)

    assert ws is not None
