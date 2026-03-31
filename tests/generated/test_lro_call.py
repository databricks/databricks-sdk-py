# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

from datetime import timedelta
from typing import Any, Dict

import pytest

import databricks.sdk.core as client
from databricks.sdk.common import lro
from tests.databricks.sdk.service.lrotesting import (
    DatabricksServiceExceptionWithDetailsProto, ErrorCode, LroTestingAPI,
    Operation, TestResource, TestResourceOperationMetadata)


@pytest.mark.parametrize(
    "fixtures,want_result,want_err",
    [
        pytest.param(
            [
                {
                    "method": "POST",
                    "url": "http://localhost/api/2.0/lro-testing/resources",
                    "response": Operation(
                        done=False,
                        metadata={"resource_id": "test-resource-123", "progress_percent": 5},
                        name="operations/test-resource-create-12345",
                    ),
                },
                {
                    "method": "GET",
                    "url": "http://localhost/api/2.0/lro-testing/operations/operations/test-resource-create-12345",
                    "response": Operation(
                        done=False,
                        metadata={"resource_id": "test-resource-123", "progress_percent": 75},
                        name="operations/test-resource-create-12345",
                    ),
                },
                {
                    "method": "GET",
                    "url": "http://localhost/api/2.0/lro-testing/operations/operations/test-resource-create-12345",
                    "response": Operation(
                        done=True,
                        metadata={"resource_id": "test-resource-123", "progress_percent": 100},
                        name="operations/test-resource-create-12345",
                        response={"id": "test-resource-123", "name": "test-resource"},
                    ),
                },
            ],
            TestResource(
                id="test-resource-123",
                name="test-resource",
            ),
            False,
            id="Success",
        ),
        pytest.param(
            [
                {
                    "method": "POST",
                    "url": "http://localhost/api/2.0/lro-testing/resources",
                    "response": Operation(
                        done=False,
                        metadata={"resource_id": "test-resource-123", "progress_percent": 5},
                        name="operations/test-resource-create-12345",
                    ),
                },
                {
                    "method": "GET",
                    "url": "http://localhost/api/2.0/lro-testing/operations/operations/test-resource-create-12345",
                    "response": Operation(
                        done=True,
                        error=DatabricksServiceExceptionWithDetailsProto(
                            error_code=ErrorCode.INTERNAL_ERROR,
                            message="Test error message",
                        ),
                        name="operations/test-resource-create-12345",
                    ),
                },
            ],
            None,
            True,
            id="Error",
        ),
    ],
)
def test_lro_create_test_resource_wait(
    config, requests_mock, fixtures: Dict[str, Any], want_result: TestResource, want_err: bool
):
    for fixture in fixtures:
        method = getattr(requests_mock, fixture["method"].lower())
        assert isinstance(fixture["response"], Operation)
        method(fixture["url"], json=fixture["response"].as_dict())

    api_client = client.ApiClient(config)
    service = LroTestingAPI(api_client)
    lro_op = service.create_test_resource(resource=TestResource())

    if want_err:
        with pytest.raises(Exception):
            lro_op.wait(opts=lro.LroOptions(timeout=timedelta(minutes=1)))
    else:
        result = lro_op.wait(opts=lro.LroOptions(timeout=timedelta(minutes=1)))
        assert result == want_result


@pytest.mark.parametrize(
    "fixtures,want_err",
    [
        pytest.param(
            [
                {
                    "method": "POST",
                    "url": "http://localhost/api/2.0/lro-testing/resources",
                    "response": Operation(
                        done=False,
                        metadata={"resource_id": "test-resource-123", "progress_percent": 5},
                        name="operations/test-resource-create-12345",
                    ),
                },
                {
                    "method": "POST",
                    "url": "http://localhost/api/2.0/lro-testing/operations/operations/test-resource-create-12345/cancel",
                    "response": Operation(
                        done=True,
                        name="operations/test-resource-create-12345",
                    ),
                },
            ],
            False,
            id="Success",
        ),
    ],
)
def test_lro_cancel_test_resource_cancel(config, requests_mock, fixtures: Dict[str, Any], want_err: bool):
    for fixture in fixtures:
        method = getattr(requests_mock, fixture["method"].lower())
        method(fixture["url"], json=fixture["response"].as_dict())

    api_client = client.ApiClient(config)
    service = LroTestingAPI(api_client)
    lro_op = service.create_test_resource(resource=TestResource())

    if want_err:
        with pytest.raises(Exception):
            lro_op.cancel()
    else:
        lro_op.cancel()


@pytest.mark.parametrize(
    "fixtures,want_name",
    [
        pytest.param(
            [
                {
                    "method": "POST",
                    "url": "http://localhost/api/2.0/lro-testing/resources",
                    "response": Operation(
                        done=False,
                        metadata={"resource_id": "test-resource-123", "progress_percent": 5},
                        name="operations/test-resource-create-12345",
                    ),
                },
            ],
            "operations/test-resource-create-12345",
            id="Success",
        ),
    ],
)
def test_lro_create_test_resource_name(config, requests_mock, fixtures: Dict[str, Any], want_name: str):
    for fixture in fixtures:
        method = getattr(requests_mock, fixture["method"].lower())
        method(fixture["url"], json=fixture["response"].as_dict())

    api_client = client.ApiClient(config)
    service = LroTestingAPI(api_client)
    lro_op = service.create_test_resource(resource=TestResource())

    name = lro_op.name()
    assert name == want_name


@pytest.mark.parametrize(
    "fixtures,want_metadata,want_err",
    [
        pytest.param(
            [
                {
                    "method": "POST",
                    "url": "http://localhost/api/2.0/lro-testing/resources",
                    "response": Operation(
                        done=False,
                        metadata={"resource_id": "test-resource-123", "progress_percent": 5},
                        name="operations/test-resource-create-12345",
                    ),
                },
            ],
            TestResourceOperationMetadata(
                progress_percent=5,
                resource_id="test-resource-123",
            ),
            False,
            id="Success",
        ),
    ],
)
def test_lro_create_test_resource_metadata(
    config, requests_mock, fixtures: Dict[str, Any], want_metadata: TestResourceOperationMetadata, want_err: bool
):
    for fixture in fixtures:
        method = getattr(requests_mock, fixture["method"].lower())
        method(fixture["url"], json=fixture["response"].as_dict())

    api_client = client.ApiClient(config)
    service = LroTestingAPI(api_client)
    lro_op = service.create_test_resource(resource=TestResource())

    if want_err:
        with pytest.raises(Exception):
            lro_op.metadata()
    else:
        metadata = lro_op.metadata()
        assert metadata == want_metadata


@pytest.mark.parametrize(
    "fixtures,want_done,want_err",
    [
        pytest.param(
            [
                {
                    "method": "POST",
                    "url": "http://localhost/api/2.0/lro-testing/resources",
                    "response": Operation(
                        done=False,
                        metadata={"resource_id": "test-resource-123", "progress_percent": 5},
                        name="operations/test-resource-create-12345",
                    ),
                },
                {
                    "method": "GET",
                    "url": "http://localhost/api/2.0/lro-testing/operations/operations/test-resource-create-12345",
                    "response": Operation(
                        done=True,
                        metadata={"resource_id": "test-resource-123", "progress_percent": 100},
                        name="operations/test-resource-create-12345",
                        response={"id": "test-resource-123", "name": "test-resource"},
                    ),
                },
            ],
            True,
            False,
            id="True",
        ),
        pytest.param(
            [
                {
                    "method": "POST",
                    "url": "http://localhost/api/2.0/lro-testing/resources",
                    "response": Operation(
                        done=False,
                        metadata={"resource_id": "test-resource-123", "progress_percent": 5},
                        name="operations/test-resource-create-12345",
                    ),
                },
                {
                    "method": "GET",
                    "url": "http://localhost/api/2.0/lro-testing/operations/operations/test-resource-create-12345",
                    "response": Operation(
                        done=False,
                        metadata={"resource_id": "test-resource-123", "progress_percent": 75},
                        name="operations/test-resource-create-12345",
                    ),
                },
            ],
            False,
            False,
            id="False",
        ),
    ],
)
def test_lro_create_test_resource_done(
    config, requests_mock, fixtures: Dict[str, Any], want_done: bool, want_err: bool
):
    for fixture in fixtures:
        method = getattr(requests_mock, fixture["method"].lower())
        method(fixture["url"], json=fixture["response"].as_dict())

    api_client = client.ApiClient(config)
    service = LroTestingAPI(api_client)
    lro_op = service.create_test_resource(resource=TestResource())

    if want_err:
        with pytest.raises(Exception):
            lro_op.done()
    else:
        done = lro_op.done()
        assert done == want_done
