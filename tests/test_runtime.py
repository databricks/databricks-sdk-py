"""Tests for the import-time behavior of ``databricks.sdk.runtime``."""

import subprocess
import sys
import textwrap
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

    # Force ``databricks.sdk.runtime`` to re-execute its module body on next import so it
    # picks up the fake ``dbruntime``. Earlier tests (e.g. test_notebook_oauth.py) cache a
    # fake module here directly via ``sys.modules`` without going through the import
    # machinery, which leaves the ``runtime`` attribute on ``databricks.sdk`` unset —
    # dropping the cached entry repairs that on the next real import. ``monkeypatch``
    # restores the prior value on teardown.
    monkeypatch.delitem(sys.modules, "databricks.sdk.runtime", raising=False)


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


def test_import_does_not_configure_root_logger():
    """Importing the module must not install a handler on the root logger.

    The module logs from its import-time global-init blocks. Routing those through the
    root ``logging.<level>()`` functions calls ``logging.basicConfig()`` while the root
    logger has no handler, which installs one -- so a downstream ``logging.basicConfig()``
    silently becomes a no-op and the importer's logs vanish. Run in a subprocess with a
    clean root logger, since this process has already imported the module (and configured
    logging), and the module is import-cached.
    """
    check = textwrap.dedent(
        """
        import logging
        import sys

        # databricks-connect is installed here; force its import in the OSS fallback to fail
        # fast so the block logs via the ImportError path instead of trying to open a session.
        sys.modules["databricks.connect"] = None

        assert not logging.getLogger().handlers, "precondition: root logger starts clean"
        try:
            import databricks.sdk.runtime  # noqa: F401
        except Exception:
            # The fallback ends by building RemoteDbUtils()/Config, which can fail or block on
            # host resolution without credentials. That runs *after* the import-time global-init
            # logging this test guards, so tolerate it -- we only assert the root logger was
            # left untouched by that earlier logging.
            pass
        handlers = logging.getLogger().handlers
        assert not handlers, f"import configured the root logger: {handlers!r}"
        """
    )
    result = subprocess.run([sys.executable, "-c", check], capture_output=True, text=True)
    assert result.returncode == 0, f"stdout:\n{result.stdout}\nstderr:\n{result.stderr}"
