"""Tests for stackql_databricks_provider.generate module."""

import json
import os
import tempfile

import pytest

from stackql_databricks_provider.generate import (
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
