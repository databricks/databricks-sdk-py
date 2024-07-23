from databricks.sdk import WorkspaceClient


# Test cases below are checking that we pinned API 2.1 for certain endpoints, DO NOT REMOVE OR CHANGE THEM. https://databricks.atlassian.net/browse/JOBS-19298
def test_jobs_create(config, requests_mock):
    requests_mock.post("http://localhost/api/2.1/jobs/create",
                       request_headers={
                           'Accept': 'application/json',
                           'Content-Type': 'application/json',
                       },
                       text="null",
                       )

    w = WorkspaceClient(config=config)
    w.jobs.create()

    assert requests_mock.call_count == 1
    assert requests_mock.called


def test_jobs_update(config, requests_mock):
    requests_mock.post("http://localhost/api/2.1/jobs/update",
                       request_headers={
                           'Accept': 'application/json',
                           'Content-Type': 'application/json',
                       },
                       text="null",
                       )

    w = WorkspaceClient(config=config)
    w.jobs.update(job_id="job_id")

    assert requests_mock.call_count == 1
    assert requests_mock.called


def test_jobs_list(config, requests_mock):
    requests_mock.get("http://localhost/api/2.1/jobs/list",
                      request_headers={
                          'Accept': 'application/json',
                      },
                      text="null",
                      )

    w = WorkspaceClient(config=config)
    for _ in w.jobs.list():
        pass

    assert requests_mock.call_count == 1
    assert requests_mock.called


def test_jobs_get(config, requests_mock):
    requests_mock.get("http://localhost/api/2.1/jobs/get",
                      request_headers={
                          'Accept': 'application/json',
                      },
                      text="null",
                      )

    w = WorkspaceClient(config=config)
    w.jobs.get(job_id="job_id")

    assert requests_mock.call_count == 1
    assert requests_mock.called


def test_jobs_reset(config, requests_mock):
    requests_mock.post("http://localhost/api/2.1/jobs/reset",
                       request_headers={
                           'Accept': 'application/json',
                           'Content-Type': 'application/json',
                       },
                       text="null",
                       )

    w = WorkspaceClient(config=config)
    w.jobs.reset(job_id="job_id", new_settings=None)

    assert requests_mock.call_count == 1
    assert requests_mock.called


def test_jobs_runs_list(config, requests_mock):
    requests_mock.get("http://localhost/api/2.1/jobs/runs/list",
                      request_headers={
                          'Accept': 'application/json',
                      },
                      text="null",
                      )

    w = WorkspaceClient(config=config)
    for _ in w.jobs.list_runs(job_id="job_id"):
        pass

    assert requests_mock.call_count == 1
    assert requests_mock.called


# End of test cases for API 2.1 pinning
