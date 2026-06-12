import logging

import pytest

from databricks.sdk.environments import Cloud

from .conftest import _is_cloud


def test_workspaces(a):
    if _is_cloud(Cloud.AZURE):
        pytest.skip("not available on Azure")
    for w in a.workspaces.list():
        logging.info(f"Found workspace: {w.workspace_name}")
