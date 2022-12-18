import logging


def test_repos_list(w):
    for repo in w.repos.list():
        logging.info(f'Found repo: {repo}')