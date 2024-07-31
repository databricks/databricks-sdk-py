import json

from databricks.sdk import WorkspaceClient


# Update API version after migration to API 2.2
def test_get_run_pagination_with_tasks(config, requests_mock):
    run1 = {
        "tasks": [{
            "run_id": 0
        }, {
            "run_id": 1
        }],
        "next_page_token": "tokenToSecondPage",
        "prev_page_token": "tokenToPreviousPage"
    }
    run2 = {
        "tasks": [{
            "run_id": 2
        }, {
            "run_id": 3
        }],
        "next_page_token": "tokenToThirdPage",
        "prev_page_token": "initialToken"
    }
    run3 = {"tasks": [{"run_id": 4}], "next_page_token": None, "prev_page_token": "tokenToSecondPage"}
    requests_mock.get("http://localhost/api/2.1/jobs/runs/get?run_id=1337&page_token=initialToken",
                      text=json.dumps(run1))
    requests_mock.get("http://localhost/api/2.1/jobs/runs/get?run_id=1337&page_token=tokenToSecondPage",
                      text=json.dumps(run2))
    requests_mock.get("http://localhost/api/2.1/jobs/runs/get?run_id=1337&page_token=tokenToThirdPage",
                      text=json.dumps(run3))
    w = WorkspaceClient(config=config)

    run = w.jobs.get_run(1337, page_token="initialToken")

    assert run.as_dict() == {
        "tasks": [{
            'run_id': 0
        }, {
            'run_id': 1
        }, {
            'run_id': 2
        }, {
            'run_id': 3
        }, {
            'run_id': 4
        }],
        "prev_page_token": "tokenToPreviousPage"
    }


def test_get_run_pagination_with_iterations(config, requests_mock):
    run1 = {
        "tasks": [{
            "run_id": 1337
        }],
        "iterations": [{
            "run_id": 0
        }, {
            "run_id": 1
        }],
        "next_page_token": "tokenToSecondPage",
        "prev_page_token": "tokenToPreviousPage"
    }
    run2 = {
        "tasks": [{
            "run_id": 1337
        }],
        "iterations": [{
            "run_id": 2
        }, {
            "run_id": 3
        }],
        "next_page_token": "tokenToThirdPage",
        "prev_page_token": "initialToken"
    }
    run3 = {
        "tasks": [{
            "run_id": 1337
        }],
        "iterations": [{
            "run_id": 4
        }],
        "next_page_token": None,
        "prev_page_token": "tokenToSecondPage"
    }
    requests_mock.get("http://localhost/api/2.1/jobs/runs/get?run_id=1337&page_token=initialToken",
                      text=json.dumps(run1))
    requests_mock.get("http://localhost/api/2.1/jobs/runs/get?run_id=1337&page_token=tokenToSecondPage",
                      text=json.dumps(run2))
    requests_mock.get("http://localhost/api/2.1/jobs/runs/get?run_id=1337&page_token=tokenToThirdPage",
                      text=json.dumps(run3))
    w = WorkspaceClient(config=config)

    run = w.jobs.get_run(1337, page_token="initialToken")

    assert run.as_dict() == {
        "tasks": [{
            'run_id': 1337
        }],
        "iterations": [{
            'run_id': 0
        }, {
            'run_id': 1
        }, {
            'run_id': 2
        }, {
            'run_id': 3
        }, {
            'run_id': 4
        }],
        "prev_page_token": "tokenToPreviousPage"
    }
