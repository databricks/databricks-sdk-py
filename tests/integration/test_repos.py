import logging

from databricks.sdk.workspace.v2.client import ReposClient


def test_repos_list(w):
    rc = ReposClient(config=w)
    for repo in rc.list():
        logging.info(f"Found repo: {repo}")
