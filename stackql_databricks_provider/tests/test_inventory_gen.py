"""Tests for stackql_databricks_provider.inventory_gen module."""

import csv
import json
import os
import tempfile

import pytest

from stackql_databricks_provider.inventory_gen import (
    CSV_COLUMNS,
    extract_operations_from_spec,
    generate_all_inventories,
    generate_inventory_for_spec,
    load_existing_csv,
)


SAMPLE_SPEC = {
    "openapi": "3.0.0",
    "info": {"title": "Test", "version": "0.1.0"},
    "paths": {
        "/api/2.0/widgets": {
            "get": {
                "operationId": "widgets_list",
                "summary": "List all widgets.",
                "tags": ["test_service", "widgets"],
                "description": "List all widgets.",
                "parameters": [
                    {"name": "page_size", "in": "query", "schema": {"type": "integer"}},
                ],
                "responses": {
                    "200": {
                        "description": "Success",
                        "content": {
                            "application/json": {
                                "schema": {"$ref": "#/components/schemas/WidgetList"},
                            }
                        },
                    }
                },
            },
            "post": {
                "operationId": "widgets_create",
                "summary": "Create a widget.",
                "tags": ["test_service", "widgets"],
                "description": "Create a widget.",
                "requestBody": {
                    "content": {
                        "application/json": {
                            "schema": {
                                "type": "object",
                                "properties": {
                                    "name": {"type": "string"},
                                    "color": {"type": "string"},
                                },
                            }
                        }
                    }
                },
                "responses": {
                    "200": {
                        "description": "Success",
                        "content": {
                            "application/json": {
                                "schema": {"$ref": "#/components/schemas/Widget"},
                            }
                        },
                    }
                },
            },
        },
        "/api/2.0/widgets/{id}": {
            "get": {
                "operationId": "widgets_get",
                "summary": "Get a widget.",
                "tags": ["test_service", "widgets"],
                "description": "Get a widget.",
                "parameters": [
                    {"name": "id", "in": "path", "schema": {"type": "string"}},
                ],
                "responses": {
                    "200": {
                        "description": "Success",
                        "content": {
                            "application/json": {
                                "schema": {"$ref": "#/components/schemas/Widget"},
                            }
                        },
                    }
                },
            },
            "delete": {
                "operationId": "widgets_delete",
                "summary": "Delete a widget.",
                "tags": ["test_service", "widgets"],
                "description": "Delete a widget.",
                "parameters": [
                    {"name": "id", "in": "path", "schema": {"type": "string"}},
                ],
                "responses": {"200": {"description": "Success"}},
            },
            "patch": {
                "operationId": "widgets_update",
                "summary": "Update a widget.",
                "tags": ["test_service", "widgets"],
                "description": "Update a widget.",
                "parameters": [
                    {"name": "id", "in": "path", "schema": {"type": "string"}},
                ],
                "requestBody": {
                    "content": {
                        "application/json": {
                            "schema": {
                                "type": "object",
                                "properties": {"name": {"type": "string"}},
                            }
                        }
                    }
                },
                "responses": {
                    "200": {
                        "description": "Success",
                        "content": {
                            "application/json": {
                                "schema": {"$ref": "#/components/schemas/Widget"},
                            }
                        },
                    }
                },
            },
            "put": {
                "operationId": "widgets_replace",
                "summary": "Replace a widget.",
                "tags": ["test_service", "widgets"],
                "description": "Replace a widget.",
                "parameters": [
                    {"name": "id", "in": "path", "schema": {"type": "string"}},
                ],
                "responses": {
                    "200": {
                        "description": "Success",
                        "content": {
                            "application/json": {
                                "schema": {"$ref": "#/components/schemas/Widget"},
                            }
                        },
                    }
                },
            },
        },
    },
    "components": {"schemas": {}},
}


class TestExtractOperationsFromSpec:
    def test_extracts_all_operations(self):
        rows = extract_operations_from_spec(SAMPLE_SPEC, "test_service")
        assert len(rows) == 6

    def test_row_columns(self):
        rows = extract_operations_from_spec(SAMPLE_SPEC, "test_service")
        for row in rows:
            for col in CSV_COLUMNS:
                assert col in row, f"Missing column: {col}"

    def test_service_name(self):
        rows = extract_operations_from_spec(SAMPLE_SPEC, "test_service")
        for row in rows:
            assert row["service"] == "test_service"

    def test_operation_ids(self):
        rows = extract_operations_from_spec(SAMPLE_SPEC, "test_service")
        op_ids = {r["operation_id"] for r in rows}
        assert "widgets_list" in op_ids
        assert "widgets_create" in op_ids
        assert "widgets_get" in op_ids
        assert "widgets_delete" in op_ids
        assert "widgets_update" in op_ids
        assert "widgets_replace" in op_ids

    def test_http_verbs(self):
        rows = extract_operations_from_spec(SAMPLE_SPEC, "test_service")
        verbs = {r["operation_id"]: r["http_verb"] for r in rows}
        assert verbs["widgets_list"] == "get"
        assert verbs["widgets_create"] == "post"
        assert verbs["widgets_delete"] == "delete"
        assert verbs["widgets_update"] == "patch"
        assert verbs["widgets_replace"] == "put"

    def test_stackql_verbs(self):
        rows = extract_operations_from_spec(SAMPLE_SPEC, "test_service")
        sq_verbs = {r["operation_id"]: r["stackql_verb"] for r in rows}
        assert sq_verbs["widgets_list"] == "SELECT"
        assert sq_verbs["widgets_create"] == "INSERT"
        assert sq_verbs["widgets_delete"] == "DELETE"
        assert sq_verbs["widgets_update"] == "UPDATE"
        assert sq_verbs["widgets_replace"] == "REPLACE"

    def test_success_response_object(self):
        rows = extract_operations_from_spec(SAMPLE_SPEC, "test_service")
        resp = {r["operation_id"]: r["success_response_object"] for r in rows}
        assert resp["widgets_list"] == "WidgetList"
        assert resp["widgets_get"] == "Widget"
        assert resp["widgets_delete"] == ""

    def test_params(self):
        rows = extract_operations_from_spec(SAMPLE_SPEC, "test_service")
        params = {r["operation_id"]: r["params"] for r in rows}
        assert "page_size" in params["widgets_list"]
        assert "name" in params["widgets_create"]
        assert "color" in params["widgets_create"]

    def test_tags(self):
        rows = extract_operations_from_spec(SAMPLE_SPEC, "test_service")
        for row in rows:
            assert "test_service" in row["tags"]
            assert "widgets" in row["tags"]

    def test_stackql_resource_name_defaults_to_last_tag(self):
        rows = extract_operations_from_spec(SAMPLE_SPEC, "test_service")
        for row in rows:
            assert row["stackql_resource_name"] == "widgets"

    def test_stackql_method_name_defaults_to_operation_id(self):
        rows = extract_operations_from_spec(SAMPLE_SPEC, "test_service")
        for row in rows:
            assert row["stackql_method_name"] == row["operation_id"]

    def test_skips_unmapped_http_verbs(self):
        spec = {
            "paths": {
                "/test": {
                    "head": {
                        "operationId": "test_head",
                        "tags": [],
                        "responses": {},
                    }
                }
            }
        }
        rows = extract_operations_from_spec(spec, "test")
        assert len(rows) == 0


class TestLoadExistingCsv:
    def test_returns_empty_for_missing_file(self):
        result = load_existing_csv("/nonexistent/path.csv")
        assert result == {}

    def test_loads_rows_keyed_by_operation_id(self):
        with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
            writer = csv.DictWriter(f, fieldnames=CSV_COLUMNS)
            writer.writeheader()
            writer.writerow({
                "service": "test",
                "operation_id": "widgets_get",
                "http_path": "/test",
                "http_verb": "get",
                "tags": "test",
                "params": "id",
                "success_response_object": "Widget",
                "summary": "Get",
                "description": "Get a widget",
                "stackql_resource_name": "custom_name",
                "stackql_method_name": "widgets_get",
                "stackql_verb": "EXEC",
            })
            tmp_path = f.name

        try:
            result = load_existing_csv(tmp_path)
            assert "widgets_get" in result
            assert result["widgets_get"]["stackql_verb"] == "EXEC"
            assert result["widgets_get"]["stackql_resource_name"] == "custom_name"
        finally:
            os.unlink(tmp_path)


class TestGenerateInventoryForSpec:
    def test_creates_csv(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            spec_path = os.path.join(tmpdir, "test.json")
            with open(spec_path, "w") as f:
                json.dump(SAMPLE_SPEC, f)

            csv_path, new_count, existing_count = generate_inventory_for_spec(
                spec_path, tmpdir, "workspace"
            )
            assert os.path.exists(csv_path)
            assert new_count == 6
            assert existing_count == 0

    def test_preserves_existing_rows(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            spec_path = os.path.join(tmpdir, "test.json")
            with open(spec_path, "w") as f:
                json.dump(SAMPLE_SPEC, f)

            # First run
            generate_inventory_for_spec(spec_path, tmpdir, "workspace")

            # Modify a row
            csv_path = os.path.join(tmpdir, "workspace", "test.csv")
            rows = []
            with open(csv_path) as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if row["operation_id"] == "widgets_get":
                        row["stackql_verb"] = "EXEC"
                    rows.append(row)
            with open(csv_path, "w", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=CSV_COLUMNS)
                writer.writeheader()
                writer.writerows(rows)

            # Second run - should preserve the modification
            csv_path2, new_count, existing_count = generate_inventory_for_spec(
                spec_path, tmpdir, "workspace"
            )
            assert new_count == 0
            assert existing_count == 6

            with open(csv_path2) as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if row["operation_id"] == "widgets_get":
                        assert row["stackql_verb"] == "EXEC"

    def test_adds_only_new_operations(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create a spec with 2 operations
            small_spec = {
                "paths": {
                    "/api/test": {
                        "get": {
                            "operationId": "test_get",
                            "tags": ["svc"],
                            "responses": {},
                        }
                    }
                }
            }
            spec_path = os.path.join(tmpdir, "test.json")
            with open(spec_path, "w") as f:
                json.dump(small_spec, f)

            # First run
            generate_inventory_for_spec(spec_path, tmpdir, "workspace")

            # Now add another operation to the spec
            small_spec["paths"]["/api/test"]["post"] = {
                "operationId": "test_create",
                "tags": ["svc"],
                "responses": {},
            }
            with open(spec_path, "w") as f:
                json.dump(small_spec, f)

            # Second run
            _, new_count, existing_count = generate_inventory_for_spec(
                spec_path, tmpdir, "workspace"
            )
            assert existing_count == 1  # test_get preserved
            assert new_count == 1  # test_create added


class TestGenerateAllInventories:
    def test_generates_from_real_specs(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            summary = generate_all_inventories(output_dir=tmpdir)
            assert summary["files_generated"] == 34
            assert summary["total_new"] > 500

            # Check directory structure
            assert os.path.isdir(os.path.join(tmpdir, "account"))
            assert os.path.isdir(os.path.join(tmpdir, "workspace"))

            # Spot check a file
            csv_path = os.path.join(tmpdir, "workspace", "agentbricks.csv")
            assert os.path.exists(csv_path)
            with open(csv_path) as f:
                reader = csv.DictReader(f)
                rows = list(reader)
            assert len(rows) > 0
            assert rows[0]["service"] == "agentbricks"
