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
    from databricks.sdk.service import compute, jobs
    cluster_spec = compute.ClusterSpec(spark_version="11.3.x-scala2.12", custom_tags={"ResourceClass": "SingleNode"},
                               num_workers=0, node_type_id="Standard_DS3_v2", )
    cluster1 = jobs.JobCluster(job_cluster_key="cluster1",
                               new_cluster=cluster_spec)
    cluster2 = jobs.JobCluster(job_cluster_key="cluster2",
                               new_cluster=cluster_spec)
    cluster3 = jobs.JobCluster(job_cluster_key="cluster3",
                               new_cluster=cluster_spec)
    cluster4 = jobs.JobCluster(job_cluster_key="cluster4",
                               new_cluster=cluster_spec)
    run1 = {
        "tasks": [{
            "run_id": 0
        }, {
            "run_id": 1
        }],
        "job_clusters": [
            cluster1.as_dict(),
            cluster2.as_dict(),
        ],
        "job_parameters": [{
            "name": "param1",
            "value": "value1"
        }],
        "next_page_token": "tokenToSecondPage",
    }
    run2 = {
        "tasks": [{
            "run_id": 2
        }, {
            "run_id": 3
        }],
        "job_clusters": [
            cluster3.as_dict(),
            cluster4.as_dict(),
        ],
        "job_parameters": [{
            "name": "param2",
            "value": "value2"
        }],
        "next_page_token": "tokenToThirdPage",
    }
    run3 = {
        "tasks": [{
            "run_id": 4
        }]
    }
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
        "job_clusters": [
            cluster1.as_dict(),
            cluster2.as_dict(),
            cluster3.as_dict(),
            cluster4.as_dict()
        ],
        "job_parameters": [{
            "name": "param1",
            "value": "value1"
        }, {
            "name": "param2",
            "value": "value2"
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
    }
    run3 = {
        "tasks": [{
            "run_id": 1337
        }],
        "iterations": [{
            "run_id": 4
        }],
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
