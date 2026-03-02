from databricks.sdk.service import catalog


# https://github.com/databricks/databricks-sdk-py/issues/135
def test_issue_135():
    from databricks.sdk.service.compute import Library, PythonPyPiLibrary
    from databricks.sdk.service.jobs import Task

    jts = Task(
        libraries=[Library(pypi=PythonPyPiLibrary(package="databricks-sdk"))],
        task_key="abc",
    )

    assert jts.as_dict() == {
        "task_key": "abc",
        "libraries": [{"pypi": {"package": "databricks-sdk"}}],
    }


# https://github.com/databricks/databricks-sdk-py/issues/103
def test_issue_103():
    from databricks.sdk.service.compute import ClusterSpec
    from databricks.sdk.service.jobs import JobCluster

    jc = JobCluster(
        job_cluster_key="no_worker",
        new_cluster=ClusterSpec(
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


def test_foundation_model_serde():
    from databricks.sdk.service.serving import FoundationModel

    model = FoundationModel(
        name="system.ai.databricks-claude-sonnet-4-5",
        display_name="Claude Sonnet 4.5",
        docs="https://docs.databricks.com/machine-learning/foundation-models/supported-models.html#claude-sonnet-4-5",
        description="Claude Sonnet 4.5 is Anthropic's most advanced hybrid reasoning model. It offers two modes: near-instant responses and extended thinking for deeper reasoning based on the complexity of the task. Claude Sonnet 4.5 specializes in application that require a balance of practical throughput and advanced thinking such as customer-facing agents, production coding workflows, and content generation at scale. This endpoint is hosted by Databricks",
        price="214.286",
        input_price="85.714",
        price_unit="DBUs per 1M tokens",
        pricing_model="Pay-per-token",
        model_class="claude",
    )

    expected = {
        "name": "system.ai.databricks-claude-sonnet-4-5",
        "display_name": "Claude Sonnet 4.5",
        "docs": "https://docs.databricks.com/machine-learning/foundation-models/supported-models.html#claude-sonnet-4-5",
        "description": "Claude Sonnet 4.5 is Anthropic's most advanced hybrid reasoning model. It offers two modes: near-instant responses and extended thinking for deeper reasoning based on the complexity of the task. Claude Sonnet 4.5 specializes in application that require a balance of practical throughput and advanced thinking such as customer-facing agents, production coding workflows, and content generation at scale. This endpoint is hosted by Databricks",
        "price": "214.286",
        "input_price": "85.714",
        "price_unit": "DBUs per 1M tokens",
        "pricing_model": "Pay-per-token",
        "model_class": "claude",
    }

    assert model.as_dict() == expected
    assert model.as_shallow_dict() == expected
    assert model == FoundationModel.from_dict(model.as_dict())


def test_foundation_model_serde_partial():
    from databricks.sdk.service.serving import FoundationModel

    model = FoundationModel(
        name="system.ai.databricks-claude-sonnet-4-5",
        price="214.286",
        model_class="claude",
    )

    expected = {
        "name": "system.ai.databricks-claude-sonnet-4-5",
        "price": "214.286",
        "model_class": "claude",
    }

    assert model.as_dict() == expected
    assert model.as_shallow_dict() == expected
    assert model == FoundationModel.from_dict(model.as_dict())
