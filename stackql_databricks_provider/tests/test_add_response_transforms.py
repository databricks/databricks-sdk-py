"""Tests for stackql_databricks_provider.add_response_transforms module."""

import json
import os
import tempfile

import pytest

from stackql_databricks_provider.add_response_transforms import (
    _find_method_in_resources,
    apply_transforms,
    load_transforms,
)


class TestLoadTransforms:
    def test_loads_from_default_path(self):
        transforms = load_transforms()
        assert isinstance(transforms, dict)
        assert len(transforms) > 0

    def test_returns_empty_for_missing_file(self):
        transforms = load_transforms("/nonexistent/path.json")
        assert transforms == {}

    def test_has_billable_usage_transform(self):
        transforms = load_transforms()
        assert "account/billing/billable_usage_download" in transforms

    def test_transform_has_response_config(self):
        transforms = load_transforms()
        entry = transforms["account/billing/billable_usage_download"]
        assert "response" in entry
        assert entry["response"]["mediaType"] == "text/plain"
        assert entry["response"]["overrideMediaType"] == "application/json"
        assert "transform" in entry["response"]
        assert entry["response"]["transform"]["type"] == "golang_template_text_v0.3.0"


class TestFindMethodInResources:
    def test_finds_method_by_operation_id(self):
        resources = {
            "billable_usage": {
                "methods": {
                    "billable_usage_download": {
                        "operation": {"$ref": "#/paths/~1usage~1download/get"},
                        "response": {"openAPIDocKey": "200"},
                    }
                }
            }
        }
        method = _find_method_in_resources(resources, "billable_usage_download")
        assert method is not None
        assert method["operation"]["$ref"] == "#/paths/~1usage~1download/get"

    def test_returns_none_for_missing_operation(self):
        resources = {
            "billable_usage": {
                "methods": {
                    "billable_usage_download": {"response": {}}
                }
            }
        }
        method = _find_method_in_resources(resources, "nonexistent_op")
        assert method is None

    def test_searches_across_resources(self):
        resources = {
            "resource_a": {"methods": {"op_a": {"response": {}}}},
            "resource_b": {"methods": {"op_b": {"response": {}}}},
        }
        assert _find_method_in_resources(resources, "op_b") is not None


class TestApplyTransforms:
    def _make_spec_with_resources(self, operation_id):
        """Create a minimal spec with x-stackQL-resources."""
        return {
            "openapi": "3.0.0",
            "paths": {},
            "x-stackQL-resources": {
                "test_resource": {
                    "methods": {
                        operation_id: {
                            "operation": {"$ref": "#/paths/~1test/get"},
                            "response": {
                                "openAPIDocKey": "200",
                                "mediaType": "text/plain",
                            },
                        }
                    }
                }
            },
        }

    def test_applies_transform_to_matching_operation(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create spec file
            scope_dir = os.path.join(tmpdir, "account")
            os.makedirs(scope_dir)
            spec = self._make_spec_with_resources("billable_usage_download")
            spec_path = os.path.join(scope_dir, "billing.json")
            with open(spec_path, "w") as f:
                json.dump(spec, f)

            # Create transforms config
            config = {
                "transforms": {
                    "account/billing/billable_usage_download": {
                        "response": {
                            "overrideMediaType": "application/json",
                            "transform": {
                                "body": "[{\"contents\": {{ toJson . }}}]",
                                "type": "golang_template_text_v0.3.0",
                            },
                        }
                    }
                }
            }
            config_path = os.path.join(tmpdir, "transforms.json")
            with open(config_path, "w") as f:
                json.dump(config, f)

            summary = apply_transforms(tmpdir, config_path)
            assert summary["account"] == 1

            # Verify the spec was updated
            with open(spec_path) as f:
                updated = json.load(f)
            method = updated["x-stackQL-resources"]["test_resource"]["methods"]["billable_usage_download"]
            assert method["response"]["overrideMediaType"] == "application/json"
            assert "transform" in method["response"]
            assert method["response"]["transform"]["type"] == "golang_template_text_v0.3.0"
            # Original fields preserved
            assert method["response"]["openAPIDocKey"] == "200"
            assert method["response"]["mediaType"] == "text/plain"

    def test_skips_when_no_x_stackql_resources(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            scope_dir = os.path.join(tmpdir, "account")
            os.makedirs(scope_dir)
            spec = {"openapi": "3.0.0", "paths": {}}
            with open(os.path.join(scope_dir, "billing.json"), "w") as f:
                json.dump(spec, f)

            config = {
                "transforms": {
                    "account/billing/billable_usage_download": {
                        "response": {"transform": {"body": "test"}}
                    }
                }
            }
            config_path = os.path.join(tmpdir, "transforms.json")
            with open(config_path, "w") as f:
                json.dump(config, f)

            summary = apply_transforms(tmpdir, config_path)
            assert summary["account"] == 0

    def test_returns_zero_for_empty_config(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            summary = apply_transforms(tmpdir, "/nonexistent/transforms.json")
            assert summary == {"account": 0, "workspace": 0}
