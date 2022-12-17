import logging


def test_jobs(workspace_client):
    found = 0
    for job in workspace_client.jobs.list():
        logging.info(f'Looking at {job.settings.name}')
        found += 1
    assert found > 0