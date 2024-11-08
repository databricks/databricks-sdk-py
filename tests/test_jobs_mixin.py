import json
import re
from typing import Pattern

from databricks.sdk import WorkspaceClient


def make_path_pattern(run_id: int, page_token: str) -> Pattern[str]:
    return re.compile(
        rf'{re.escape("http://localhost/api/")}2.\d{re.escape(f"/jobs/runs/get?page_token={page_token}&run_id={run_id}")}'
    )


def test_get_run_with_no_pagination(config, requests_mock):
    run1 = {"tasks": [{"run_id": 0}, {"run_id": 1}], }
    requests_mock.get(make_path_pattern(1337, "initialToken"), text=json.dumps(run1))
    w = WorkspaceClient(config=config)

    run = w.jobs.get_run(1337, page_token="initialToken")

    assert run.as_dict() == {"tasks": [{'run_id': 0}, {'run_id': 1}], }


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
    requests_mock.get(make_path_pattern(1337, "initialToken"), text=json.dumps(run1))
    requests_mock.get(make_path_pattern(1337, "tokenToSecondPage"), text=json.dumps(run2))
    requests_mock.get(make_path_pattern(1337, "tokenToThirdPage"), text=json.dumps(run3))
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
    requests_mock.get(make_path_pattern(1337, "initialToken"), text=json.dumps(run1))
    requests_mock.get(make_path_pattern(1337, "tokenToSecondPage"), text=json.dumps(run2))
    requests_mock.get(make_path_pattern(1337, "tokenToThirdPage"), text=json.dumps(run3))
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
    }