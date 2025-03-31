import logging

import pytest


def test_workspaces(a):
    from databricks.sdk.provisioning.v2.client import WorkspacesClient

    wc = WorkspacesClient(config=a)
    if a.is_azure:
        pytest.skip("not available on Azure")
    for w in wc.list():
        logging.info(f"Found workspace: {w.workspace_name}")
