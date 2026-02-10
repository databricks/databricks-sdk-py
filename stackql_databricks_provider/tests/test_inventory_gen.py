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

    def test_filename_defaults_to_service_json(self):
        rows = extract_operations_from_spec(SAMPLE_SPEC, "test_service")
        for row in rows:
            assert row["filename"] == "test_service.json"

    def test_filename_can_be_overridden(self):
        rows = extract_operations_from_spec(SAMPLE_SPEC, "test_service", filename="custom.json")
        for row in rows:
            assert row["filename"] == "custom.json"

    def test_operation_ids(self):
        rows = extract_operations_from_spec(SAMPLE_SPEC, "test_service")
        op_ids = {r["operationId"] for r in rows}
        assert "widgets_list" in op_ids
        assert "widgets_create" in op_ids
        assert "widgets_get" in op_ids
        assert "widgets_delete" in op_ids
        assert "widgets_update" in op_ids
        assert "widgets_replace" in op_ids

    def test_http_verbs(self):
        rows = extract_operations_from_spec(SAMPLE_SPEC, "test_service")
        verbs = {r["operationId"]: r["verb"] for r in rows}
        assert verbs["widgets_list"] == "get"
        assert verbs["widgets_create"] == "post"
        assert verbs["widgets_delete"] == "delete"
        assert verbs["widgets_update"] == "patch"
        assert verbs["widgets_replace"] == "put"

    def test_stackql_verbs_lowercase(self):
        rows = extract_operations_from_spec(SAMPLE_SPEC, "test_service")
        sq_verbs = {r["operationId"]: r["stackql_verb"] for r in rows}
        assert sq_verbs["widgets_list"] == "select"
        assert sq_verbs["widgets_create"] == "insert"
        assert sq_verbs["widgets_delete"] == "delete"
        assert sq_verbs["widgets_update"] == "update"
        assert sq_verbs["widgets_replace"] == "replace"

    def test_response_object(self):
        rows = extract_operations_from_spec(SAMPLE_SPEC, "test_service")
        resp = {r["operationId"]: r["response_object"] for r in rows}
        assert resp["widgets_list"] == "WidgetList"
        assert resp["widgets_get"] == "Widget"
        assert resp["widgets_delete"] == ""

    def test_params(self):
        rows = extract_operations_from_spec(SAMPLE_SPEC, "test_service")
        params = {r["operationId"]: r["params"] for r in rows}
        assert "page_size" in params["widgets_list"]
        assert "name" in params["widgets_create"]
        assert "color" in params["widgets_create"]

    def test_tags(self):
        rows = extract_operations_from_spec(SAMPLE_SPEC, "test_service")
        for row in rows:
            assert "test_service" in row["tags"]
            assert "widgets" in row["tags"]

    def test_path_column(self):
        rows = extract_operations_from_spec(SAMPLE_SPEC, "test_service")
        paths = {r["operationId"]: r["path"] for r in rows}
        assert paths["widgets_list"] == "/api/2.0/widgets"
        assert paths["widgets_get"] == "/api/2.0/widgets/{id}"

    def test_stackql_resource_name_defaults_to_last_tag(self):
        rows = extract_operations_from_spec(SAMPLE_SPEC, "test_service")
        for row in rows:
            assert row["stackql_resource_name"] == "widgets"

    def test_stackql_method_name_defaults_to_operation_id(self):
        rows = extract_operations_from_spec(SAMPLE_SPEC, "test_service")
        for row in rows:
            assert row["stackql_method_name"] == row["operationId"]

    def test_stackql_object_key_defaults_to_empty(self):
        rows = extract_operations_from_spec(SAMPLE_SPEC, "test_service")
        for row in rows:
            assert row["stackql_object_key"] == ""

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

    def test_loads_rows_keyed_by_filename_path_verb(self):
        with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
            writer = csv.DictWriter(f, fieldnames=CSV_COLUMNS)
            writer.writeheader()
            writer.writerow({
                "filename": "test.json",
                "path": "/test",
                "operationId": "widgets_get",
                "verb": "get",
                "response_object": "Widget",
                "tags": "test",
                "params": "id",
                "summary": "Get",
                "description": "Get a widget",
                "stackql_resource_name": "custom_name",
                "stackql_method_name": "widgets_get",
                "stackql_verb": "exec",
                "stackql_object_key": "",
            })
            tmp_path = f.name

        try:
            result = load_existing_csv(tmp_path)
            key = "test.json::/test::get"
            assert key in result
            assert result[key]["stackql_verb"] == "exec"
            assert result[key]["stackql_resource_name"] == "custom_name"
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

    def test_csv_has_correct_columns(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            spec_path = os.path.join(tmpdir, "test.json")
            with open(spec_path, "w") as f:
                json.dump(SAMPLE_SPEC, f)

            csv_path, _, _ = generate_inventory_for_spec(spec_path, tmpdir, "workspace")
            with open(csv_path) as f:
                reader = csv.DictReader(f)
                assert list(reader.fieldnames) == CSV_COLUMNS

    def test_preserves_existing_rows(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            spec_path = os.path.join(tmpdir, "test.json")
            with open(spec_path, "w") as f:
                json.dump(SAMPLE_SPEC, f)

            # First run
            generate_inventory_for_spec(spec_path, tmpdir, "workspace")

            # Modify a row - change stackql_verb to exec
            csv_path = os.path.join(tmpdir, "workspace", "test.csv")
            rows = []
            with open(csv_path) as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if row["operationId"] == "widgets_get":
                        row["stackql_verb"] = "exec"
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
                    if row["operationId"] == "widgets_get":
                        assert row["stackql_verb"] == "exec"

    def test_adds_only_new_operations(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create a spec with 1 operation
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
            assert rows[0]["filename"] == "agentbricks.json"

    def test_generates_consolidated_csv(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            generate_all_inventories(output_dir=tmpdir)

            # Check consolidated files exist
            for scope in ("account", "workspace"):
                all_csv = os.path.join(tmpdir, scope, "all_services.csv")
                assert os.path.exists(all_csv), f"Missing {scope}/all_services.csv"
                with open(all_csv) as f:
                    reader = csv.DictReader(f)
                    rows = list(reader)
                assert len(rows) > 0

    def test_consolidated_csv_has_all_columns(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            generate_all_inventories(output_dir=tmpdir)
            all_csv = os.path.join(tmpdir, "workspace", "all_services.csv")
            with open(all_csv) as f:
                reader = csv.DictReader(f)
                assert list(reader.fieldnames) == CSV_COLUMNS
