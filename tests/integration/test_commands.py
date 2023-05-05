import pytest

from databricks.sdk.core import DatabricksError


def test_error_unmarshall(w, random):
    with pytest.raises(DatabricksError) as exc_info:
        w.command_execution.execute(cluster_id='__non_existing__')
    err = exc_info.value
    assert 'requirement failed: missing contextId' in str(err)
    assert err.error_code is None
