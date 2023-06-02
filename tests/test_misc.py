# https://github.com/databricks/databricks-sdk-py/issues/135
def test_issue_135():
    from databricks.sdk.service.compute import Library, PythonPyPiLibrary
    from databricks.sdk.service.jobs import JobTaskSettings

    jts = JobTaskSettings(libraries=[Library(pypi=PythonPyPiLibrary(package='databricks-sdk'))],
                          task_key='abc')

    assert jts.as_dict() == {'task_key': 'abc', 'libraries': [{'pypi': {'package': 'databricks-sdk'}}]}
