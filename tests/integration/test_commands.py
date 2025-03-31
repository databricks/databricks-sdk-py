import pytest

from databricks.sdk.databricks.core import DatabricksError


def test_error_unmarshall(w, random):
    from databricks.sdk.compute.v2.client import CommandExecutionClient

    cec = CommandExecutionClient(config=w)
    with pytest.raises(DatabricksError) as exc_info:
        cec.execute(cluster_id="__non_existing__")
    err = exc_info.value
    assert "requirement failed: missing contextId" in str(err)
    assert err.error_code is None
