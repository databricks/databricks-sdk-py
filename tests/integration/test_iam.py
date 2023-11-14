import pytest

from databricks.sdk.core import DatabricksError


def test_filtering_groups(w, random):
    all = w.groups.list(filter=f'displayName eq any-{random(12)}')
    found = len(list(all))
    assert found == 0


def test_scim_error_unmarshall(w, random):
    with pytest.raises(DatabricksError) as exc_info:
        w.groups.list(filter=random(12))
    assert 'Given filter operator is not supported' in str(exc_info.value)


@pytest.mark.parametrize("path,call", [
    ("/api/2.0/preview/scim/v2/Users", lambda w: w.users.list(count=1)),
    ("/api/2.0/preview/scim/v2/Groups", lambda w: w.groups.list(count=1)),
    ("/api/2.0/preview/scim/v2/ServicePrincipals", lambda w: w.service_principals.list(count=1)),
])
def test_workspace_users_list_pagination(w, path, call):
    raw = w.api_client.do('GET', path)
    total = raw['totalResults']
    all = call(w)
    found = len(list(all))
    assert found == total


@pytest.mark.parametrize("path,call", [
    # there are ~7k users in our aws prod account
    ("/api/2.0/accounts/%s/scim/v2/Users", lambda a: a.users.list(count=1000)),
    ("/api/2.0/accounts/%s/scim/v2/Groups", lambda a: a.groups.list(count=1)),
    # there are ~3k service principals in our aws prod account
    ("/api/2.0/accounts/%s/scim/v2/ServicePrincipals", lambda a: a.service_principals.list(count=1000)),
])
def test_account_users_list_pagination(a, path, call):
    raw = a.api_client.do('GET', path.replace("%s", a.config.account_id))
    total = raw['totalResults']
    all = call(a)
    found = len(list(all))
    assert found == total
