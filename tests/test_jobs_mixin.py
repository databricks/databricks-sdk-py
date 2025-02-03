import json
import re
from typing import Pattern

from databricks.sdk import WorkspaceClient


def make_getrun_path_pattern(run_id: int, page_token: str) -> Pattern[str]:
    return re.compile(
        rf'{re.escape("http://localhost/api/")}2.\d{re.escape(f"/jobs/runs/get?page_token={page_token}&run_id={run_id}")}'
    )


def make_getjob_path_pattern(job_id: int, page_token: str) -> Pattern[str]:
    return re.compile(
        rf'{re.escape("http://localhost/api/")}2.\d{re.escape(f"/jobs/get?job_id={job_id}&page_token={page_token}")}'
    )


def test_get_run_with_no_pagination(config, requests_mock):
    run1 = {"tasks": [{"run_id": 0}, {"run_id": 1}], }
    requests_mock.get(make_getrun_path_pattern(1337, "initialToken"), text=json.dumps(run1))
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
    requests_mock.get(make_getrun_path_pattern(1337, "initialToken"), text=json.dumps(run1))
    requests_mock.get(make_getrun_path_pattern(1337, "tokenToSecondPage"), text=json.dumps(run2))
    requests_mock.get(make_getrun_path_pattern(1337, "tokenToThirdPage"), text=json.dumps(run3))
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
    requests_mock.get(make_getrun_path_pattern(1337, "initialToken"), text=json.dumps(run1))
    requests_mock.get(make_getrun_path_pattern(1337, "tokenToSecondPage"), text=json.dumps(run2))
    requests_mock.get(make_getrun_path_pattern(1337, "tokenToThirdPage"), text=json.dumps(run3))
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


def test_get_job_with_no_pagination(config, requests_mock):
    job1 = {"settings": {"tasks": [{"task_key": "taskKey1"}, {"task_key": "taskKey2"}], }}
    requests_mock.get(make_getjob_path_pattern(1337, "initialToken"), text=json.dumps(job1))
    w = WorkspaceClient(config=config)

    job = w.jobs.get(1337, page_token="initialToken")

    assert job.as_dict() == {"settings": {"tasks": [{"task_key": "taskKey1"}, {"task_key": "taskKey2"}], }}


def test_get_job_pagination_with_tasks(config, requests_mock):
    from databricks.sdk.service import compute, jobs
    cluster_spec = compute.ClusterSpec(spark_version="11.3.x-scala2.12",
                                       custom_tags={"ResourceClass": "SingleNode"},
                                       num_workers=0,
                                       node_type_id="Standard_DS3_v2",
                                       )
    cluster1 = jobs.JobCluster(job_cluster_key="cluster1", new_cluster=cluster_spec)
    cluster2 = jobs.JobCluster(job_cluster_key="cluster2", new_cluster=cluster_spec)
    cluster3 = jobs.JobCluster(job_cluster_key="cluster3", new_cluster=cluster_spec)
    cluster4 = jobs.JobCluster(job_cluster_key="cluster4", new_cluster=cluster_spec)
    job1 = {
        "settings": {
            "tasks": [{
                "task_key": "taskKey1"
            }, {
                "task_key": "taskKey2"
            }],
            "job_clusters": [cluster1.as_dict(), cluster2.as_dict()],
            "parameters": [{
                "name": "param1",
                "default": "default1"
            }],
            "environments": [{
                "environment_key": "key1"
            }, {
                "environment_key": "key2"
            }]
        },
        "next_page_token": "tokenToSecondPage"
    }
    job2 = {
        "settings": {
            "tasks": [{
                "task_key": "taskKey3"
            }, {
                "task_key": "taskKey4"
            }],
            "job_clusters": [cluster3.as_dict(), cluster4.as_dict()],
            "parameters": [{
                "name": "param2",
                "default": "default2"
            }],
            "environments": [{
                "environment_key": "key3"
            }]
        },
        "next_page_token": "tokenToThirdPage"
    }
    job3 = {
        "settings": {
            "tasks": [{
                "task_key": "taskKey5"
            }],
            "parameters": [{
                "name": "param3",
                "default": "default3"
            }]
        },
    }

    requests_mock.get(make_getjob_path_pattern(1337, "initialToken"), text=json.dumps(job1))
    requests_mock.get(make_getjob_path_pattern(1337, "tokenToSecondPage"), text=json.dumps(job2))
    requests_mock.get(make_getjob_path_pattern(1337, "tokenToThirdPage"), text=json.dumps(job3))
    w = WorkspaceClient(config=config)

    job = w.jobs.get(1337, page_token="initialToken")

    assert job.as_dict() == {
        "settings": {
            "tasks": [{
                "task_key": "taskKey1"
            }, {
                "task_key": "taskKey2"
            }, {
                "task_key": "taskKey3"
            }, {
                "task_key": "taskKey4"
            }, {
                "task_key": "taskKey5"
            }],
            "job_clusters": [cluster1.as_dict(),
                             cluster2.as_dict(),
                             cluster3.as_dict(),
                             cluster4.as_dict()],
            "parameters": [{
                "name": "param1",
                "default": "default1"
            }, {
                "name": "param2",
                "default": "default2"
            }, {
                "name": "param3",
                "default": "default3"
            }],
            "environments": [{
                "environment_key": "key1"
            }, {
                "environment_key": "key2"
            }, {
                "environment_key": "key3"
            }]
        }
    }
