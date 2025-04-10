import pytest

from databricks.sdk.databricks import errors
from databricks.sdk.databricks.core import ApiClient, DatabricksError
from databricks.sdk.iam.v2.client import (AccountGroupsClient,
                                          AccountServicePrincipalsClient,
                                          AccountUsersClient, GroupsClient,
                                          ServicePrincipalsClient, UsersClient)


def test_filtering_groups(w, random):
    gc = GroupsClient(config=w)

    all = gc.list(filter=f"displayName eq any-{random(12)}")
    found = len(list(all))
    assert found == 0


def test_scim_error_unmarshall(w, random):
    gc = GroupsClient(config=w)

    with pytest.raises(DatabricksError) as exc_info:
        groups = gc.list(filter=random(12))
        next(groups)
    assert isinstance(exc_info.value, errors.BadRequest)


def test_scim_get_user_as_dict(w):
    uc = UsersClient(config=w)

    first_user = next(uc.list())
    user = uc.get(first_user.id)
    # should not throw
    user.as_dict()


@pytest.mark.parametrize(
    "client_class,path,count",
    [
        (UsersClient, "/api/2.0/preview/scim/v2/Users", 10),
        (GroupsClient, "/api/2.0/preview/scim/v2/Groups", 40),
        (ServicePrincipalsClient, "/api/2.0/preview/scim/v2/ServicePrincipals", 10),
    ],
)
def test_workspace_users_list_pagination(w, client_class, path, count):
    client = client_class(config=w)
    api_client = ApiClient(cfg=w)
    raw = api_client.do("GET", path)
    total = raw["totalResults"]
    all = client.list(count=count)
    found = len(list(all))
    assert found == total


@pytest.mark.parametrize(
    "client_class,path,count",
    [
        (AccountUsersClient, "/api/2.0/accounts/%s/scim/v2/Users", 3000),
        (AccountGroupsClient, "/api/2.0/accounts/%s/scim/v2/Groups", 50),
        (AccountServicePrincipalsClient, "/api/2.0/accounts/%s/scim/v2/ServicePrincipals", 1000),
    ],
)
def test_account_users_list_pagination(a, client_class, path, count):
    client = client_class(config=a)
    api_client = ApiClient(cfg=a)
    raw = api_client.do("GET", path.replace("%s", a.account_id))
    total = raw["totalResults"]
    all = client.list(count=count)
    found = len(list(all))
    assert found == total
