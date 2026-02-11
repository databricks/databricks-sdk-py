"""Tests for stackql_databricks_provider.generate module."""

import json
import os
import tempfile

import pytest

from stackql_databricks_provider.generate import (
    _apply_overrides,
    _parse_json_path,
    _resolve_json_path,
    generate_all,
    generate_spec_for_service,
)


class TestGenerateSpecForService:
    def test_generates_valid_openapi_structure(self):
        spec = generate_spec_for_service("agentbricks", "workspace")
        assert spec["openapi"] == "3.0.0"
        assert "info" in spec
        assert "paths" in spec
        assert "components" in spec
        assert "schemas" in spec["components"]

    def test_has_paths(self):
        spec = generate_spec_for_service("agentbricks", "workspace")
        assert len(spec["paths"]) > 0

    def test_has_schemas(self):
        spec = generate_spec_for_service("agentbricks", "workspace")
        schemas = spec["components"]["schemas"]
        assert "CustomLlm" in schemas

    def test_account_server_url(self):
        spec = generate_spec_for_service("billing", "account")
        assert "accounts" in spec["servers"][0]["url"]

    def test_workspace_server_url(self):
        spec = generate_spec_for_service("agentbricks", "workspace")
        assert "{workspace}" in spec["servers"][0]["url"]

    def test_filter_by_api_class(self):
        # Only generate for AgentBricksAPI (the only one in this module)
        spec = generate_spec_for_service(
            "agentbricks", "workspace", api_class_names=["AgentBricksAPI"]
        )
        assert len(spec["paths"]) > 0

    def test_spec_is_json_serializable(self):
        spec = generate_spec_for_service("agentbricks", "workspace")
        json_str = json.dumps(spec)
        assert len(json_str) > 0


class TestGenerateAll:
    def test_generates_to_output_dir(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            summary = generate_all(tmpdir)
            assert summary["account_services"] > 0
            assert summary["workspace_services"] > 0
            assert os.path.exists(os.path.join(tmpdir, "account"))
            assert os.path.exists(os.path.join(tmpdir, "workspace"))

    def test_creates_json_files(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            generate_all(tmpdir)
            account_files = os.listdir(os.path.join(tmpdir, "account"))
            workspace_files = os.listdir(os.path.join(tmpdir, "workspace"))
            assert len(account_files) > 0
            assert len(workspace_files) > 0
            for f in account_files + workspace_files:
                assert f.endswith(".json")

    def test_generated_files_are_valid_json(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            generate_all(tmpdir)
            for scope in ("account", "workspace"):
                scope_dir = os.path.join(tmpdir, scope)
                for fname in os.listdir(scope_dir):
                    path = os.path.join(scope_dir, fname)
                    with open(path) as f:
                        data = json.load(f)
                    assert data["openapi"] == "3.0.0"
                    assert "paths" in data

    def test_summary_counts(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            summary = generate_all(tmpdir)
            assert summary["total_paths"] > 100
            assert summary["total_schemas"] > 100

    def test_no_orphaned_refs(self):
        """Verify every $ref in the specs points to a defined schema."""

        def collect_refs(obj, refs=None):
            if refs is None:
                refs = set()
            if isinstance(obj, dict):
                if "$ref" in obj:
                    refs.add(obj["$ref"])
                for v in obj.values():
                    collect_refs(v, refs)
            elif isinstance(obj, list):
                for item in obj:
                    collect_refs(item, refs)
            return refs

        with tempfile.TemporaryDirectory() as tmpdir:
            generate_all(tmpdir)
            orphaned = []
            for scope in ("account", "workspace"):
                scope_dir = os.path.join(tmpdir, scope)
                for fname in os.listdir(scope_dir):
                    path = os.path.join(scope_dir, fname)
                    with open(path) as f:
                        data = json.load(f)
                    schemas = set(data.get("components", {}).get("schemas", {}).keys())
                    refs = collect_refs(data.get("paths", {}))
                    prefix = "#/components/schemas/"
                    for ref in refs:
                        if ref.startswith(prefix):
                            name = ref[len(prefix):]
                            if name not in schemas:
                                orphaned.append(f"{scope}/{fname}: {ref}")
            assert orphaned == [], f"Orphaned $refs found:\n" + "\n".join(orphaned[:20])


class TestProvenance:
    def test_info_has_sdk_version(self):
        spec = generate_spec_for_service("agentbricks", "workspace")
        assert "x-stackql-sdk-version" in spec["info"]
        assert spec["info"]["x-stackql-sdk-version"]  # non-empty

    def test_info_has_date_generated(self):
        spec = generate_spec_for_service("agentbricks", "workspace")
        assert "x-stackql-date-generated" in spec["info"]
        # ISO format: YYYY-MM-DD
        assert len(spec["info"]["x-stackql-date-generated"]) == 10

    def test_info_has_sdk_namespace(self):
        spec = generate_spec_for_service("agentbricks", "workspace")
        assert spec["info"]["x-stackql-sdk-namespace"] == "databricks.sdk.service.agentbricks"

    def test_operations_have_sdk_source(self):
        spec = generate_spec_for_service("agentbricks", "workspace")
        for path, methods in spec["paths"].items():
            for verb, operation in methods.items():
                assert "x-stackql-sdk-source" in operation, (
                    f"{verb.upper()} {path} missing x-stackql-sdk-source"
                )
                assert operation["x-stackql-sdk-source"].endswith("API")


class TestSpecOverrides:
    def test_parse_json_path_simple(self):
        segments = _parse_json_path("paths./api/test.get.summary")
        assert segments == ["paths", "/api/test", "get", "summary"]

    def test_parse_json_path_with_predicate(self):
        segments = _parse_json_path(
            "paths./api/2.0/database/instances:findByUid.get.parameters[name=uid].required"
        )
        assert segments == [
            "paths",
            "/api/2.0/database/instances:findByUid",
            "get",
            "parameters[name=uid]",
            "required",
        ]

    def test_resolve_json_path_dict_key(self):
        obj = {"a": {"b": {"c": 42}}}
        parent, key = _resolve_json_path(obj, ["a", "b", "c"])
        assert parent == {"c": 42}
        assert key == "c"
        assert parent[key] == 42

    def test_resolve_json_path_array_predicate(self):
        obj = {
            "params": [
                {"name": "foo", "required": False},
                {"name": "bar", "required": False},
            ]
        }
        parent, key = _resolve_json_path(obj, ["params[name=bar]", "required"])
        assert parent["name"] == "bar"
        assert key == "required"

    def test_apply_overrides_sets_value(self):
        spec = {
            "paths": {
                "/api/test": {
                    "get": {
                        "parameters": [
                            {"name": "uid", "in": "query", "required": False}
                        ]
                    }
                }
            }
        }
        overrides = {
            "workspace/test_svc": [
                {
                    "json_path": "paths./api/test.get.parameters[name=uid].required",
                    "value": True,
                }
            ]
        }
        count = _apply_overrides(spec, "workspace", "test_svc", overrides)
        assert count == 1
        assert spec["paths"]["/api/test"]["get"]["parameters"][0]["required"] is True

    def test_apply_overrides_no_match_returns_zero(self):
        spec = {"paths": {}}
        overrides = {"account/other": [{"json_path": "paths.x", "value": 1}]}
        count = _apply_overrides(spec, "workspace", "test_svc", overrides)
        assert count == 0

    def test_database_uid_override_applied(self):
        """Verify the real database spec gets the uid override."""
        spec = generate_spec_for_service("database", "workspace")
        path_data = spec["paths"].get("/api/2.0/database/instances:findByUid", {})
        params = path_data.get("get", {}).get("parameters", [])
        uid_param = next((p for p in params if p["name"] == "uid"), None)
        assert uid_param is not None
        assert uid_param["required"] is True
