"""Tests for stackql_databricks_provider.extract module."""

import json

import pytest
from databricks.sdk.service import agentbricks, billing, catalog, compute, iam

from stackql_databricks_provider.extract import (
    get_data_classes,
    get_enums,
    get_operation_details,
    get_operations,
    get_resources,
    get_schema_from_data_class,
    get_schema_from_enum,
)


# ---------------------------------------------------------------------------
# get_resources
# ---------------------------------------------------------------------------

class TestGetResources:
    def test_returns_list_of_tuples(self):
        resources = get_resources(agentbricks)
        assert isinstance(resources, list)
        for item in resources:
            assert isinstance(item, tuple)
            assert len(item) == 2

    def test_finds_agentbricks_api(self):
        resources = get_resources(agentbricks)
        class_names = [c for c, _ in resources]
        assert "AgentBricksAPI" in class_names

    def test_snake_case_conversion(self):
        resources = get_resources(agentbricks)
        result = dict(resources)
        assert result["AgentBricksAPI"] == "agent_bricks"

    def test_multiple_resources(self):
        resources = get_resources(catalog)
        assert len(resources) > 10  # catalog has many API classes

    def test_sorted_by_class_name(self):
        resources = get_resources(catalog)
        class_names = [c for c, _ in resources]
        assert class_names == sorted(class_names)

    def test_excludes_non_api_classes(self):
        resources = get_resources(agentbricks)
        class_names = [c for c, _ in resources]
        # Dataclasses like CustomLlm should not appear
        assert "CustomLlm" not in class_names
        assert "Dataset" not in class_names


# ---------------------------------------------------------------------------
# get_operations
# ---------------------------------------------------------------------------

class TestGetOperations:
    def test_returns_list_of_strings(self):
        ops = get_operations(agentbricks, "AgentBricksAPI")
        assert isinstance(ops, list)
        for op in ops:
            assert isinstance(op, str)

    def test_finds_crud_operations(self):
        ops = get_operations(agentbricks, "AgentBricksAPI")
        assert "create_custom_llm" in ops
        assert "get_custom_llm" in ops
        assert "delete_custom_llm" in ops
        assert "update_custom_llm" in ops

    def test_excludes_private_methods(self):
        ops = get_operations(agentbricks, "AgentBricksAPI")
        for op in ops:
            assert not op.startswith("_")

    def test_sorted(self):
        ops = get_operations(agentbricks, "AgentBricksAPI")
        assert ops == sorted(ops)

    def test_missing_class_returns_empty(self):
        ops = get_operations(agentbricks, "NonExistentAPI")
        assert ops == []


# ---------------------------------------------------------------------------
# get_operation_details
# ---------------------------------------------------------------------------

class TestGetOperationDetails:
    def test_returns_path_dict(self):
        details = get_operation_details(
            agentbricks, "AgentBricksAPI", "get_custom_llm",
            service_name="agentbricks", resource_snake_name="agent_bricks"
        )
        assert isinstance(details, dict)
        assert len(details) == 1

    def test_get_operation_structure(self):
        details = get_operation_details(
            agentbricks, "AgentBricksAPI", "get_custom_llm",
            service_name="agentbricks", resource_snake_name="agent_bricks"
        )
        path = "/api/2.0/custom-llms/{id}"
        assert path in details
        assert "get" in details[path]
        op = details[path]["get"]
        assert op["operationId"] == "agent_bricks_get_custom_llm"
        assert "parameters" in op
        assert op["parameters"][0]["name"] == "id"
        assert op["parameters"][0]["in"] == "path"

    def test_post_has_request_body(self):
        details = get_operation_details(
            agentbricks, "AgentBricksAPI", "create_custom_llm",
            service_name="agentbricks", resource_snake_name="agent_bricks"
        )
        path = "/api/2.0/custom-llms"
        assert path in details
        op = details[path]["post"]
        assert "requestBody" in op
        schema = op["requestBody"]["content"]["application/json"]["schema"]
        assert "name" in schema["properties"]
        assert "instructions" in schema["properties"]

    def test_required_body_params(self):
        details = get_operation_details(
            agentbricks, "AgentBricksAPI", "create_custom_llm",
            service_name="agentbricks", resource_snake_name="agent_bricks"
        )
        path = "/api/2.0/custom-llms"
        schema = details[path]["post"]["requestBody"]["content"]["application/json"]["schema"]
        assert "name" in schema["required"]
        assert "instructions" in schema["required"]

    def test_return_type_ref(self):
        details = get_operation_details(
            agentbricks, "AgentBricksAPI", "get_custom_llm",
            service_name="agentbricks", resource_snake_name="agent_bricks"
        )
        path = "/api/2.0/custom-llms/{id}"
        response = details[path]["get"]["responses"]["200"]
        assert "$ref" in response["content"]["application/json"]["schema"]

    def test_void_return_no_content(self):
        details = get_operation_details(
            agentbricks, "AgentBricksAPI", "delete_custom_llm",
            service_name="agentbricks", resource_snake_name="agent_bricks"
        )
        path = "/api/2.0/custom-llms/{id}"
        response = details[path]["delete"]["responses"]["200"]
        assert "content" not in response

    def test_tags_present(self):
        details = get_operation_details(
            agentbricks, "AgentBricksAPI", "get_custom_llm",
            service_name="agentbricks", resource_snake_name="agent_bricks"
        )
        path = "/api/2.0/custom-llms/{id}"
        tags = details[path]["get"]["tags"]
        assert "agentbricks" in tags

    def test_error_response_present(self):
        details = get_operation_details(
            agentbricks, "AgentBricksAPI", "get_custom_llm",
            service_name="agentbricks", resource_snake_name="agent_bricks"
        )
        path = "/api/2.0/custom-llms/{id}"
        assert "default" in details[path]["get"]["responses"]

    def test_raises_on_missing_class(self):
        with pytest.raises(ValueError, match="not found"):
            get_operation_details(agentbricks, "FakeAPI", "get")

    def test_raises_on_missing_method(self):
        with pytest.raises(ValueError, match="not found"):
            get_operation_details(agentbricks, "AgentBricksAPI", "fake_method")


# ---------------------------------------------------------------------------
# get_data_classes
# ---------------------------------------------------------------------------

class TestGetDataClasses:
    def test_returns_list_of_types(self):
        dcs = get_data_classes(agentbricks)
        assert isinstance(dcs, list)
        for dc in dcs:
            assert isinstance(dc, type)

    def test_finds_expected_classes(self):
        dcs = get_data_classes(agentbricks)
        names = [dc.__name__ for dc in dcs]
        assert "CustomLlm" in names
        assert "Dataset" in names
        assert "Table" in names

    def test_excludes_non_dataclasses(self):
        dcs = get_data_classes(agentbricks)
        names = [dc.__name__ for dc in dcs]
        assert "AgentBricksAPI" not in names  # API class, not dataclass
        assert "State" not in names  # Enum, not dataclass

    def test_sorted_by_name(self):
        dcs = get_data_classes(agentbricks)
        names = [dc.__name__ for dc in dcs]
        assert names == sorted(names)


# ---------------------------------------------------------------------------
# get_enums
# ---------------------------------------------------------------------------

class TestGetEnums:
    def test_returns_list_of_enum_types(self):
        enums = get_enums(agentbricks)
        assert isinstance(enums, list)
        from enum import Enum
        for e in enums:
            assert issubclass(e, Enum)

    def test_finds_state_enum(self):
        enums = get_enums(agentbricks)
        names = [e.__name__ for e in enums]
        assert "State" in names


# ---------------------------------------------------------------------------
# get_schema_from_data_class
# ---------------------------------------------------------------------------

class TestGetSchemaFromDataClass:
    def test_returns_dict_with_class_name_key(self):
        dcs = get_data_classes(agentbricks)
        custom_llm = next(dc for dc in dcs if dc.__name__ == "CustomLlm")
        schema = get_schema_from_data_class(agentbricks, custom_llm)
        assert "CustomLlm" in schema

    def test_schema_has_type_object(self):
        dcs = get_data_classes(agentbricks)
        custom_llm = next(dc for dc in dcs if dc.__name__ == "CustomLlm")
        schema = get_schema_from_data_class(agentbricks, custom_llm)
        assert schema["CustomLlm"]["type"] == "object"

    def test_properties_present(self):
        dcs = get_data_classes(agentbricks)
        custom_llm = next(dc for dc in dcs if dc.__name__ == "CustomLlm")
        schema = get_schema_from_data_class(agentbricks, custom_llm)
        props = schema["CustomLlm"]["properties"]
        assert "name" in props
        assert "instructions" in props
        assert "id" in props

    def test_required_fields(self):
        dcs = get_data_classes(agentbricks)
        custom_llm = next(dc for dc in dcs if dc.__name__ == "CustomLlm")
        schema = get_schema_from_data_class(agentbricks, custom_llm)
        required = schema["CustomLlm"]["required"]
        assert "name" in required
        assert "instructions" in required
        # Optional fields should not be required
        assert "id" not in required
        assert "creation_time" not in required

    def test_resolves_list_type(self):
        dcs = get_data_classes(agentbricks)
        custom_llm = next(dc for dc in dcs if dc.__name__ == "CustomLlm")
        schema = get_schema_from_data_class(agentbricks, custom_llm)
        datasets_prop = schema["CustomLlm"]["properties"]["datasets"]
        assert datasets_prop["type"] == "array"
        assert "$ref" in datasets_prop["items"]

    def test_resolves_enum_type(self):
        dcs = get_data_classes(agentbricks)
        custom_llm = next(dc for dc in dcs if dc.__name__ == "CustomLlm")
        schema = get_schema_from_data_class(agentbricks, custom_llm)
        state_prop = schema["CustomLlm"]["properties"]["optimization_state"]
        assert "$ref" in state_prop

    def test_field_descriptions(self):
        dcs = get_data_classes(agentbricks)
        custom_llm = next(dc for dc in dcs if dc.__name__ == "CustomLlm")
        schema = get_schema_from_data_class(agentbricks, custom_llm)
        props = schema["CustomLlm"]["properties"]
        assert "description" in props["instructions"]

    def test_raises_on_non_dataclass(self):
        from enum import Enum
        class NotADataclass(Enum):
            A = "a"
        with pytest.raises(TypeError):
            get_schema_from_data_class(agentbricks, NotADataclass)


# ---------------------------------------------------------------------------
# get_schema_from_enum
# ---------------------------------------------------------------------------

class TestGetSchemaFromEnum:
    def test_returns_string_enum_schema(self):
        enums = get_enums(agentbricks)
        state = next(e for e in enums if e.__name__ == "State")
        schema = get_schema_from_enum(state)
        assert "State" in schema
        assert schema["State"]["type"] == "string"
        assert "enum" in schema["State"]

    def test_enum_values(self):
        enums = get_enums(agentbricks)
        state = next(e for e in enums if e.__name__ == "State")
        schema = get_schema_from_enum(state)
        values = schema["State"]["enum"]
        assert "CANCELLED" in values
        assert "COMPLETED" in values
        assert "RUNNING" in values


# ---------------------------------------------------------------------------
# Cross-service tests (validate on larger services)
# ---------------------------------------------------------------------------

class TestCrossService:
    def test_compute_has_many_resources(self):
        resources = get_resources(compute)
        assert len(resources) >= 5

    def test_iam_account_api_operations(self):
        ops = get_operations(iam, "AccountGroupsAPI")
        assert len(ops) > 0

    def test_catalog_dataclasses(self):
        dcs = get_data_classes(catalog)
        assert len(dcs) > 50

    def test_billing_operation_details(self):
        ops = get_operations(billing, "BillableUsageAPI")
        assert len(ops) > 0
        details = get_operation_details(
            billing, "BillableUsageAPI", ops[0],
            service_name="billing", resource_snake_name="billable_usage"
        )
        assert len(details) > 0


# ---------------------------------------------------------------------------
# Response media type detection
# ---------------------------------------------------------------------------

class TestResponseMediaType:
    def test_billing_download_is_text_plain(self):
        """BillableUsageAPI.download sets Accept: text/plain."""
        details = get_operation_details(
            billing, "BillableUsageAPI", "download",
            service_name="billing", resource_snake_name="billable_usage",
        )
        for path, methods in details.items():
            for verb, operation in methods.items():
                resp_200 = operation["responses"]["200"]
                assert "text/plain" in resp_200["content"], (
                    "BillableUsageAPI.download should have text/plain response"
                )
                assert "application/json" not in resp_200["content"]

    def test_billing_download_text_plain_schema_has_contents_property(self):
        """text/plain response should use object with contents property."""
        details = get_operation_details(
            billing, "BillableUsageAPI", "download",
            service_name="billing", resource_snake_name="billable_usage",
        )
        for path, methods in details.items():
            for verb, operation in methods.items():
                schema = operation["responses"]["200"]["content"]["text/plain"]["schema"]
                assert schema["type"] == "object"
                assert "contents" in schema["properties"]
                assert schema["properties"]["contents"]["type"] == "string"

    def test_json_endpoint_still_uses_application_json(self):
        """Normal JSON endpoints should still use application/json."""
        details = get_operation_details(
            billing, "BudgetPolicyAPI", "create",
            service_name="billing", resource_snake_name="budget_policy",
        )
        for path, methods in details.items():
            for verb, operation in methods.items():
                resp_200 = operation["responses"]["200"]
                assert "application/json" in resp_200["content"]
