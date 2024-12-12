import pytest

from databricks.sdk import WorkspaceClient, AccountClient

@pytest.mark.parametrize(
    "path,call",
    [
        ("/api/2.0/preview/scim/v2/Users", lambda w: w.users.list()),
        ("/api/2.0/preview/scim/v2/Groups", lambda w: w.groups.list()),
        ("/api/2.0/preview/scim/v2/ServicePrincipals", lambda w: w.service_principals.list()),
    ],
)
def test_workspace_iam_list(config, requests_mock, path, call):
    requests_mock.get(
        f"http://localhost{path}",
        request_headers={
            "Accept": "application/json",
        },
        text="null", 
    )
    w = WorkspaceClient(config=config)
    for _ in call(w):
        pass
    assert requests_mock.call_count == 1
    assert requests_mock.called


@pytest.mark.parametrize(
    "path,call",
    [
        ("/api/2.0/accounts/%s/scim/v2/Users", lambda a: a.users.list()),
        ("/api/2.0/accounts/%s/scim/v2/Groups", lambda a: a.groups.list()),
        ("/api/2.0/accounts/%s/scim/v2/ServicePrincipals", lambda a: a.service_principals.list()),
    ],
)
def test_account_iam_list(config, requests_mock, path, call):
    config.account_id = "test_account_id"
    requests_mock.get(
        path.replace("%s", config.account_id),
        request_headers={
            "Accept": "application/json",
        },
        text="null", 
    )
    a = AccountClient(config=config)
    for _ in call(a):
        pass
    assert requests_mock.call_count == 1
    assert requests_mock.called