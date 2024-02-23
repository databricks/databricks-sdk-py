from databricks.sdk.service import catalog


# https://github.com/databricks/databricks-sdk-py/issues/135
def test_issue_135():
    from databricks.sdk.service.compute import Library, PythonPyPiLibrary
    from databricks.sdk.service.jobs import Task

    jts = Task(libraries=[Library(pypi=PythonPyPiLibrary(package='databricks-sdk'))], task_key='abc')

    assert jts.as_dict() == {'task_key': 'abc', 'libraries': [{'pypi': {'package': 'databricks-sdk'}}]}


# https://github.com/databricks/databricks-sdk-py/issues/103
def test_issue_103():
    from databricks.sdk.service.compute import ClusterSpec
    from databricks.sdk.service.jobs import JobCluster

    jc = JobCluster(job_cluster_key="no_worker",
                    new_cluster=ClusterSpec(spark_version="11.3.x-scala2.12",
                                            custom_tags={"ResourceClass": "SingleNode"},
                                            num_workers=0,
                                            node_type_id="Standard_DS3_v2",
                                            ),
                    )

    assert jc.as_dict() == {
        'job_cluster_key': 'no_worker',
        'new_cluster': {
            'custom_tags': {
                'ResourceClass': 'SingleNode'
            },
            'num_workers': 0,
            'node_type_id': 'Standard_DS3_v2',
            'spark_version': '11.3.x-scala2.12'
        }
    }


def test_serde_with_empty_dataclass():
    inst = catalog.OnlineTableSpec(pipeline_id="123",
                                   run_continuously=catalog.OnlineTableSpecContinuousSchedulingPolicy(),
                                   )
    assert inst.as_dict() == {'pipeline_id': '123', 'run_continuously': {}}
    assert inst == catalog.OnlineTableSpec.from_dict(inst.as_dict())
