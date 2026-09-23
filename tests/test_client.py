import functools
import sys
import types
from unittest.mock import create_autospec
from urllib.parse import parse_qs, urlsplit

import pytest

from databricks.sdk import AccountClient, WorkspaceClient

from .conftest import noop_credentials


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


@pytest.mark.parametrize("client_type", [WorkspaceClient, AccountClient])
def test_client_forwards_group_id_to_config(client_type):
    """Verifies public clients preserve group_id in their underlying configuration."""
    client = client_type(
        host="https://example.cloud.databricks.com",
        group_id="test-group",
        credentials_strategy=noop_credentials,
    )

    assert client.config.group_id == "test-group"


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


def test_account_client_derives_isolated_workspace_client_through_http(requests_mock):
    account_host = "https://accounts.cloud.databricks.com"
    workspace_host = "https://fixture-workspace.cloud.databricks.com"
    account_id = "00000000-0000-0000-0000-000000000000"
    workspace_id = 123456789
    requests_mock.get(
        f"{account_host}/api/2.0/accounts/{account_id}/workspaces/{workspace_id}",
        json={
            "account_id": account_id,
            "aws_region": "us-west-2",
            "deployment_name": "fixture-workspace",
            "workspace_id": workspace_id,
            "workspace_name": "fixture",
            "workspace_status": "RUNNING",
        },
    )
    requests_mock.get(
        f"{workspace_host}/api/2.0/preview/scim/v2/Me",
        json={"active": True, "id": "user-1", "userName": "fixture@databricks.com"},
    )
    account = AccountClient(host=account_host, account_id=account_id, token="test-token")

    workspace = account.workspaces.get(workspace_id)
    derived = account.get_workspace_client(workspace)
    current_user = derived.current_user.me()

    assert current_user.user_name == "fixture@databricks.com"
    assert derived.config.host == workspace_host
    assert derived.config.workspace_id == str(workspace_id)
    assert account.config.host == account_host
    assert account.config.account_id == account_id
    assert requests_mock.request_history[1].headers["X-Databricks-Workspace-Id"] == str(workspace_id)


def test_workspace_scim_pagination_advances_start_index_at_http_boundary(requests_mock):
    host = "https://fixture-workspace.cloud.databricks.com"
    endpoint = f"{host}/api/2.0/preview/scim/v2/Users"
    requests_mock.register_uri(
        "GET",
        endpoint,
        [
            {
                "json": {
                    "Resources": [
                        {"active": True, "id": "user-1", "userName": "one@databricks.com"},
                        {"active": True, "id": "user-2", "userName": "two@databricks.com"},
                    ],
                    "itemsPerPage": 2,
                    "startIndex": 1,
                    "totalResults": 3,
                }
            },
            {
                "json": {
                    "Resources": [{"active": True, "id": "user-3", "userName": "three@databricks.com"}],
                    "itemsPerPage": 1,
                    "startIndex": 3,
                    "totalResults": 3,
                }
            },
            {"json": {"Resources": [], "itemsPerPage": 0, "startIndex": 4, "totalResults": 3}},
        ],
    )
    workspace = WorkspaceClient(host=host, token="test-token")

    users = list(workspace.users.list(count=2))

    assert [user.user_name for user in users] == [
        "one@databricks.com",
        "two@databricks.com",
        "three@databricks.com",
    ]
    assert [parse_qs(urlsplit(request.url).query) for request in requests_mock.request_history] == [
        {"count": ["2"], "startIndex": ["1"]},
        {"count": ["2"], "startIndex": ["3"]},
        {"count": ["2"], "startIndex": ["4"]},
    ]


def test_account_scim_pagination_advances_start_index_at_http_boundary(requests_mock):
    host = "https://accounts.cloud.databricks.com"
    account_id = "00000000-0000-0000-0000-000000000000"
    endpoint = f"{host}/api/2.0/accounts/{account_id}/scim/v2/Users"
    requests_mock.register_uri(
        "GET",
        endpoint,
        [
            {
                "json": {
                    "Resources": [
                        {"active": True, "id": "user-1", "userName": "one@databricks.com"},
                        {"active": True, "id": "user-2", "userName": "two@databricks.com"},
                    ],
                    "itemsPerPage": 2,
                    "startIndex": 1,
                    "totalResults": 3,
                }
            },
            {
                "json": {
                    "Resources": [{"active": True, "id": "user-3", "userName": "three@databricks.com"}],
                    "itemsPerPage": 1,
                    "startIndex": 3,
                    "totalResults": 3,
                }
            },
            {"json": {"Resources": [], "itemsPerPage": 0, "startIndex": 4, "totalResults": 3}},
        ],
    )
    account = AccountClient(host=host, account_id=account_id, token="test-token")

    users = list(account.users.list(count=2))

    assert [user.user_name for user in users] == [
        "one@databricks.com",
        "two@databricks.com",
        "three@databricks.com",
    ]
    assert [parse_qs(urlsplit(request.url).query) for request in requests_mock.request_history] == [
        {"count": ["2"], "startIndex": ["1"]},
        {"count": ["2"], "startIndex": ["3"]},
        {"count": ["2"], "startIndex": ["4"]},
    ]
