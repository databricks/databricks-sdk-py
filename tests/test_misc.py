from databricks.sdk.catalog.v2 import catalog
from databricks.sdk.jobs.v2 import jobs


# https://github.com/databricks/databricks-sdk-py/issues/135
def test_issue_135():

    jts = jobs.Task(
        libraries=[jobs.Library(pypi=jobs.PythonPyPiLibrary(package="databricks-sdk"))],
        task_key="abc",
    )

    assert jts.as_dict() == {
        "task_key": "abc",
        "libraries": [{"pypi": {"package": "databricks-sdk"}}],
    }


# https://github.com/databricks/databricks-sdk-py/issues/103
def test_issue_103():
    jc = jobs.JobCluster(
        job_cluster_key="no_worker",
        new_cluster=jobs.JobsClusterSpec(
            spark_version="11.3.x-scala2.12",
            custom_tags={"ResourceClass": "SingleNode"},
            num_workers=0,
            node_type_id="Standard_DS3_v2",
        ),
    )

    assert jc.as_dict() == {
        "job_cluster_key": "no_worker",
        "new_cluster": {
            "custom_tags": {"ResourceClass": "SingleNode"},
            "num_workers": 0,
            "node_type_id": "Standard_DS3_v2",
            "spark_version": "11.3.x-scala2.12",
        },
    }


def test_serde_with_empty_dataclass():
    inst = catalog.OnlineTableSpec(
        pipeline_id="123",
        run_continuously=catalog.OnlineTableSpecContinuousSchedulingPolicy(),
    )
    assert inst.as_dict() == {"pipeline_id": "123", "run_continuously": {}}
    assert inst == catalog.OnlineTableSpec.from_dict(inst.as_dict())
