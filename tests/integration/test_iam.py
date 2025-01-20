import pytest

from databricks.sdk import errors
from databricks.sdk.core import DatabricksError


def test_filtering_groups(w, random):
    all = w.groups.list(filter=f'displayName eq any-{random(12)}')
    found = len(list(all))
    assert found == 0


def test_scim_error_unmarshall(w, random):
    with pytest.raises(DatabricksError) as exc_info:
        groups = w.groups.list(filter=random(12))
        next(groups)
    assert isinstance(exc_info.value, errors.BadRequest)


def test_scim_get_user_as_dict(w):
    first_user = next(w.users.list())
    user = w.users.get(first_user.id)
    # should not throw
    user.as_dict()
