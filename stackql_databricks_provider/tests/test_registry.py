"""Tests for stackql_databricks_provider.registry module."""

from stackql_databricks_provider.registry import (
    ACCOUNT_API_CLASSES,
    SERVICE_MODULES,
    classify_api_class,
    get_all_services_by_scope,
    get_service_api_classes,
    load_service_module,
)


class TestLoadServiceModule:
    def test_loads_agentbricks(self):
        module = load_service_module("agentbricks")
        assert hasattr(module, "AgentBricksAPI")

    def test_loads_compute(self):
        module = load_service_module("compute")
        assert hasattr(module, "ClustersAPI")

    def test_loads_all_modules(self):
        for svc in SERVICE_MODULES:
            module = load_service_module(svc)
            assert module is not None


class TestClassifyApiClass:
    def test_account_classes(self):
        assert classify_api_class("AccountAccessControlAPI") == "account"
        assert classify_api_class("BillableUsageAPI") == "account"
        assert classify_api_class("WorkspacesAPI") == "account"
        assert classify_api_class("EncryptionKeysAPI") == "account"

    def test_workspace_classes(self):
        assert classify_api_class("ClustersAPI") == "workspace"
        assert classify_api_class("JobsAPI") == "workspace"
        assert classify_api_class("AgentBricksAPI") == "workspace"

    def test_unknown_defaults_to_workspace(self):
        assert classify_api_class("SomeFutureAPI") == "workspace"


class TestGetServiceApiClasses:
    def test_billing_all_account(self):
        groups = get_service_api_classes("billing")
        assert len(groups["account"]) > 0

    def test_compute_all_workspace(self):
        groups = get_service_api_classes("compute")
        assert len(groups["workspace"]) > 0
        assert len(groups["account"]) == 0

    def test_iam_has_both(self):
        groups = get_service_api_classes("iam")
        assert len(groups["account"]) > 0
        assert len(groups["workspace"]) > 0


class TestGetAllServicesByScope:
    def test_returns_both_scopes(self):
        result = get_all_services_by_scope()
        assert "account" in result
        assert "workspace" in result

    def test_has_entries(self):
        result = get_all_services_by_scope()
        assert len(result["account"]) > 0
        assert len(result["workspace"]) > 0

    def test_entries_are_tuples(self):
        result = get_all_services_by_scope()
        for svc, cls in result["account"]:
            assert isinstance(svc, str)
            assert isinstance(cls, str)
