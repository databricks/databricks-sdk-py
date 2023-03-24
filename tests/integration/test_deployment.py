import logging

import pytest


def test_workspaces(a):
    if a.config.is_azure:
        pytest.skip('not available on Azure')
    for w in a.workspaces.list():
        logging.info(f'Found workspace: {w.workspace_name}')