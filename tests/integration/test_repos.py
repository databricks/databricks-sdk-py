import logging


def test_repos_list(w):  # type: ignore[no-untyped-def]
    for repo in w.repos.list():
        logging.info(f"Found repo: {repo}")
