import logging


def test_workspaces(a):
    for w in a.workspaces.list():
        logging.info(f'Found workspace: {w.workspace_name}')