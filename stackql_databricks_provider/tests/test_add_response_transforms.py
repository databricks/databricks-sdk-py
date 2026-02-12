"""Tests for stackql_databricks_provider.add_response_transforms module."""

import json
import os
import tempfile

import pytest
import yaml

from stackql_databricks_provider.add_response_transforms import (
    _find_method_in_resources,
    _find_service_yaml,
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


class TestFindServiceYaml:
    def test_finds_yaml_in_versioned_dir(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            svc_dir = os.path.join(tmpdir, "databricks_account", "v00.00.00000", "services")
            os.makedirs(svc_dir)
            yaml_path = os.path.join(svc_dir, "billing.yaml")
            with open(yaml_path, "w") as f:
                f.write("openapi: '3.0.0'\n")

            result = _find_service_yaml(tmpdir, "databricks_account", "billing")
            assert result == yaml_path

    def test_returns_none_for_missing_service(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            result = _find_service_yaml(tmpdir, "databricks_account", "billing")
            assert result is None


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
    def _make_provider_tree(self, tmpdir, scope, service, operation_id):
        """Create a minimal provider YAML spec tree."""
        provider = "databricks_account" if scope == "account" else "databricks_workspace"
        svc_dir = os.path.join(tmpdir, provider, "v00.00.00000", "services")
        os.makedirs(svc_dir)

        spec = {
            "openapi": "3.0.0",
            "components": {
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
                }
            },
        }

        spec_path = os.path.join(svc_dir, f"{service}.yaml")
        with open(spec_path, "w") as f:
            yaml.dump(spec, f, default_flow_style=False, sort_keys=False)
        return spec_path

    def test_applies_transform_to_yaml_spec(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            spec_path = self._make_provider_tree(
                tmpdir, "account", "billing", "billable_usage_download"
            )

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

            # Verify the YAML was updated
            with open(spec_path) as f:
                updated = yaml.safe_load(f)
            resources = updated["components"]["x-stackQL-resources"]
            method = resources["test_resource"]["methods"]["billable_usage_download"]
            assert method["response"]["overrideMediaType"] == "application/json"
            assert "transform" in method["response"]
            assert method["response"]["transform"]["type"] == "golang_template_text_v0.3.0"
            # Original fields preserved
            assert method["response"]["openAPIDocKey"] == "200"
            assert method["response"]["mediaType"] == "text/plain"

    def test_skips_when_no_x_stackql_resources(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            provider = "databricks_account"
            svc_dir = os.path.join(tmpdir, provider, "v00.00.00000", "services")
            os.makedirs(svc_dir)
            spec_path = os.path.join(svc_dir, "billing.yaml")
            with open(spec_path, "w") as f:
                yaml.dump({"openapi": "3.0.0", "components": {}}, f)

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

    def test_applies_to_real_billing_yaml(self):
        """Test against the actual generated billing.yaml if it exists."""
        real_spec_dir = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            "stackql-provider", "src",
        )
        billing_yaml = os.path.join(
            real_spec_dir, "databricks_account", "v00.00.00000",
            "services", "billing.yaml",
        )
        if not os.path.exists(billing_yaml):
            pytest.skip("billing.yaml not present (run npm run generate-provider first)")

        with open(billing_yaml) as f:
            spec = yaml.safe_load(f)

        resources = spec.get("components", {}).get("x-stackQL-resources", {})
        assert resources, "No x-stackQL-resources in billing.yaml"

        method = _find_method_in_resources(resources, "billable_usage_download")
        assert method is not None, "billable_usage_download not found in resources"
