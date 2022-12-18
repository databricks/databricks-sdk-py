import logging


def test_jobs(w):
    found = 0
    for job in w.jobs.list():
        logging.info(f'Looking at {job.settings.name}')
        found += 1
    assert found > 0