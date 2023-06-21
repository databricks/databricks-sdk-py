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
