import json
import re
from typing import Optional, Pattern

from databricks.sdk import WorkspaceClient


def make_getrun_path_pattern(run_id: int, page_token: Optional[str] = None) -> Pattern[str]:
    if page_token:
        return re.compile(
            rf'{re.escape("http://localhost/api/")}2.\d{re.escape(f"/jobs/runs/get?page_token={page_token}&run_id={run_id}")}'
        )
    else:
        return re.compile(
            rf'{re.escape("http://localhost/api/")}2.\d{re.escape(f"/jobs/runs/get?run_id={run_id}")}')


def make_getjob_path_pattern(job_id: int, page_token: str) -> Pattern[str]:
    return re.compile(
        rf'{re.escape("http://localhost/api/")}2.\d{re.escape(f"/jobs/get?job_id={job_id}&page_token={page_token}")}'
    )


def make_listruns_path_pattern(page_token: str) -> Pattern[str]:
    return re.compile(
        rf'{re.escape("http://localhost/api/")}2.\d{re.escape(f"/jobs/runs/list")}\?(?:expand_tasks=(?:true|false)&)?page_token={re.escape(page_token)}'
    )


def test_get_run_with_no_pagination(config, requests_mock):
    run1 = {"tasks": [{"run_id": 0}, {"run_id": 1}], }
    requests_mock.get(make_getrun_path_pattern(1337, "initialToken"), text=json.dumps(run1))
    w = WorkspaceClient(config=config)

    run = w.jobs.get_run(1337, page_token="initialToken")

    assert run.as_dict() == {"tasks": [{'run_id': 0}, {'run_id': 1}], }


def test_get_run_pagination_with_tasks(config, requests_mock):
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
    run1 = {
        "tasks": [{
            "run_id": 0
        }, {
            "run_id": 1
        }],
        "job_clusters": [cluster1.as_dict(), cluster2.as_dict(), ],
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
        "job_clusters": [cluster3.as_dict(), cluster4.as_dict(), ],
        "job_parameters": [{
            "name": "param2",
            "value": "value2"
        }],
        "next_page_token": "tokenToThirdPage",
    }
    run3 = {"tasks": [{"run_id": 4}]}
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
        "job_clusters": [cluster1.as_dict(),
                         cluster2.as_dict(),
                         cluster3.as_dict(),
                         cluster4.as_dict()],
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
    run3 = {"tasks": [{"run_id": 1337}], "iterations": [{"run_id": 4}], }
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


def test_list_runs_without_task_expansion(config, requests_mock):
    listruns_page1 = {
        "runs": [{
            "run_id": 100,
            "run_name": "run100",
        }, {
            "run_id":
            200,
            "run_name":
            "run200",
            "job_parameters": [{
                "name": "param1",
                "default": "default1"
            }, {
                "name": "param2",
                "default": "default2"
            }]
        }, {
            "run_id": 300,
            "run_name": "run300",
        }],
        "next_page_token":
        "tokenToSecondPage"
    }
    listruns_page2 = {
        "runs": [{
            "run_id": 400,
            "run_name": "run400",
            "repair_history": [{
                "id": "repair400_1",
            }, {
                "id": "repair400_2",
            }]
        }]
    }

    requests_mock.get(make_listruns_path_pattern("initialToken"), text=json.dumps(listruns_page1))
    requests_mock.get(make_listruns_path_pattern("tokenToSecondPage"), text=json.dumps(listruns_page2))
    w = WorkspaceClient(config=config)

    runs_list = list(w.jobs.list_runs(expand_tasks=False, page_token="initialToken"))
    runs_dict = [run.as_dict() for run in runs_list]

    assert runs_dict == [{
        "run_id": 100,
        "run_name": "run100",
    }, {
        "run_id":
        200,
        "run_name":
        "run200",
        "job_parameters": [{
            "name": "param1",
            "default": "default1"
        }, {
            "name": "param2",
            "default": "default2"
        }]
    }, {
        "run_id": 300,
        "run_name": "run300",
    }, {
        "run_id": 400,
        "run_name": "run400",
        "repair_history": [{
            "id": "repair400_1",
        }, {
            "id": "repair400_2",
        }]
    }]

    # only two requests should be made which are jobs/list requests
    assert requests_mock.call_count == 2


def test_list_runs(config, requests_mock):
    listruns_page1 = {
        "runs": [{
            "run_id": 100,
            "tasks": [{
                "task_key": "taskkey101"
            }, {
                "task_key": "taskkey102"
            }],
            "has_more": True
        }, {
            "run_id": 200,
            "tasks": [{
                "task_key": "taskkey201"
            }]
        }, {
            "run_id": 300,
            "tasks": [{
                "task_key": "taskkey301"
            }]
        }],
        "next_page_token":
        "tokenToSecondPage"
    }
    listruns_page2 = {
        "runs": [{
            "run_id": 400,
            "tasks": [{
                "task_key": "taskkey401"
            }, {
                "task_key": "taskkey402"
            }],
            "has_more": True
        }]
    }

    getrun_100_page1 = {
        "run_id": 100,
        "tasks": [{
            "task_key": "taskkey101"
        }, {
            "task_key": "taskkey102"
        }],
        "next_page_token": "tokenToSecondPage_100"
    }
    getrun_100_page2 = {"run_id": 100, "tasks": [{"task_key": "taskkey103"}]}
    getrun_400_page1 = {
        "run_id": 400,
        "tasks": [{
            "task_key": "taskkey401"
        }, {
            "task_key": "taskkey403"
        }],
        "next_page_token": "tokenToSecondPage_400"
    }
    getrun_400_page2 = {"run_id": 400, "tasks": [{"task_key": "taskkey402"}, {"task_key": "taskkey404"}]}

    requests_mock.get(make_listruns_path_pattern("initialToken"), text=json.dumps(listruns_page1))
    requests_mock.get(make_listruns_path_pattern("tokenToSecondPage"), text=json.dumps(listruns_page2))

    requests_mock.get(make_getrun_path_pattern(100), text=json.dumps(getrun_100_page1))
    requests_mock.get(make_getrun_path_pattern(100, "tokenToSecondPage_100"),
                      text=json.dumps(getrun_100_page2))

    requests_mock.get(make_getrun_path_pattern(400), text=json.dumps(getrun_400_page1))
    requests_mock.get(make_getrun_path_pattern(400, "tokenToSecondPage_400"),
                      text=json.dumps(getrun_400_page2))
    w = WorkspaceClient(config=config)

    runs_list = list(w.jobs.list_runs(expand_tasks=True, page_token="initialToken"))
    runs_dict = [run.as_dict() for run in runs_list]

    assert runs_dict == [{
        "run_id":
        100,
        "tasks": [{
            "task_key": "taskkey101",
        }, {
            "task_key": "taskkey102",
        }, {
            "task_key": "taskkey103",
        }],
    }, {
        "run_id": 200,
        "tasks": [{
            "task_key": "taskkey201",
        }],
    }, {
        "run_id": 300,
        "tasks": [{
            "task_key": "taskkey301",
        }],
    }, {
        "run_id":
        400,
        "tasks": [{
            "task_key": "taskkey401",
        }, {
            "task_key": "taskkey403",
        }, {
            "task_key": "taskkey402",
        }, {
            "task_key": "taskkey404",
        }],
    }]

    # check that job_id 200 and 300 was never used in runs/get call
    history = requests_mock.request_history
    assert all('300' not in request.qs.get("run_id", ['']) for request in history)
    assert all('200' not in request.qs.get("run_id", ['']) for request in history)
