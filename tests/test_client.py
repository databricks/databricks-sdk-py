import functools
import sys
import types
from unittest.mock import create_autospec

import pytest

from databricks.sdk import WorkspaceClient


def test_autospec_fails_on_unknown_service():
    w = create_autospec(WorkspaceClient)
    with pytest.raises(AttributeError):
        w.foo.bar()


def test_autospec_fails_on_setting_unknown_property():
    w = create_autospec(WorkspaceClient, spec_set=True)
    with pytest.raises(AttributeError):
        w.bar = 1


def test_dbutils_is_a_cached_property():
    """``dbutils`` is a ``functools.cached_property`` so consumers that never read it
    pay no build cost — and, on Spark Connect runtimes, never touch the legacy
    ``SparkContext`` path that ``databricks.sdk.runtime`` materializes on import."""
    descriptor = WorkspaceClient.__dict__["dbutils"]
    assert isinstance(descriptor, functools.cached_property)


def test_workspace_client_init_does_not_build_dbutils(config, mocker):
    """Constructing a ``WorkspaceClient`` must not invoke ``_make_dbutils``."""
    spy = mocker.patch("databricks.sdk._make_dbutils")

    WorkspaceClient(config=config)

    spy.assert_not_called()


def test_dbutils_first_access_builds_exactly_once(config, mocker):
    """First read of ``.dbutils`` calls ``_make_dbutils`` once; subsequent reads
    return the cached value without re-invoking."""
    sentinel = object()
    spy = mocker.patch("databricks.sdk._make_dbutils", return_value=sentinel)
    ws = WorkspaceClient(config=config)

    first = ws.dbutils
    assert spy.call_count == 1
    assert first is sentinel

    second = ws.dbutils
    assert spy.call_count == 1  # still 1 — cached_property short-circuits via __dict__
    assert second is sentinel


def test_workspace_client_constructs_on_spark_connect_without_touching_runtime(monkeypatch, config):
    """End-to-end Layer 2 win: with the lazy property, ``WorkspaceClient(config=...)``
    on a Spark Connect cluster succeeds without ever importing
    ``databricks.sdk.runtime`` — so the legacy ``SparkContext`` materialization that
    raises ``CONTEXT_UNAVAILABLE_FOR_REMOTE_CLIENT`` is never even attempted.

    Faked ``dbruntime`` raises on any namespace materialization; if anything during
    construction triggered ``databricks.sdk.runtime``'s import, this test would crash.
    """

    class _Initializer:
        @staticmethod
        def getOrCreate():
            raise RuntimeError(
                "[CONTEXT_UNAVAILABLE_FOR_REMOTE_CLIENT] Calls to SparkContext are not "
                "supported on a Spark Connect cluster."
            )

    fake = types.ModuleType("dbruntime")
    fake.UserNamespaceInitializer = _Initializer
    monkeypatch.setitem(sys.modules, "dbruntime", fake)
    monkeypatch.delitem(sys.modules, "databricks.sdk.runtime", raising=False)

    ws = WorkspaceClient(config=config)

    assert ws is not None
    assert "databricks.sdk.runtime" not in sys.modules
