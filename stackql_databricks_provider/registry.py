"""
Service registry that maps SDK service modules and API classes
to account or workspace scope.

Uses the WorkspaceClient and AccountClient definitions to determine
which API classes belong to each scope.
"""

import importlib
import logging
from typing import Dict, List, Set, Tuple

logger = logging.getLogger(__name__)

# All service module names under databricks.sdk.service
SERVICE_MODULES = [
    "agentbricks",
    "apps",
    "billing",
    "catalog",
    "cleanrooms",
    "compute",
    "dashboards",
    "database",
    "dataquality",
    "files",
    "iam",
    "iamv2",
    "jobs",
    "marketplace",
    "ml",
    "oauth2",
    "pipelines",
    "postgres",
    "provisioning",
    "qualitymonitorv2",
    "serving",
    "settings",
    "settingsv2",
    "sharing",
    "sql",
    "tags",
    "vectorsearch",
    "workspace",
]

# API classes instantiated in AccountClient.__init__
# (extracted from databricks/sdk/__init__.py AccountClient class)
ACCOUNT_API_CLASSES: Set[str] = {
    "AccountAccessControlAPI",
    "BillableUsageAPI",
    "BudgetPolicyAPI",
    "BudgetsAPI",
    "CredentialsAPI",  # provisioning.CredentialsAPI
    "CustomAppIntegrationAPI",
    "EncryptionKeysAPI",
    "AccountFederationPolicyAPI",
    "AccountGroupsV2API",
    "AccountIamV2API",
    "AccountIpAccessListsAPI",
    "LogDeliveryAPI",
    "AccountMetastoreAssignmentsAPI",
    "AccountMetastoresAPI",
    "NetworkConnectivityAPI",
    "NetworkPoliciesAPI",
    "NetworksAPI",
    "OAuthPublishedAppsAPI",
    "PrivateAccessAPI",
    "PublishedAppIntegrationAPI",
    "ServicePrincipalFederationPolicyAPI",
    "ServicePrincipalSecretsAPI",
    "AccountServicePrincipalsV2API",
    "AccountSettingsAPI",
    "AccountSettingsV2API",
    "StorageAPI",
    "AccountStorageCredentialsAPI",
    "UsageDashboardsAPI",
    "AccountUsersV2API",
    "VpcEndpointsAPI",
    "WorkspaceAssignmentAPI",
    "WorkspaceNetworkConfigurationAPI",
    "WorkspacesAPI",
    "AccountGroupsAPI",
    "AccountServicePrincipalsAPI",
    "AccountUsersAPI",
}


def load_service_module(service_name: str):
    """Import and return a service module by name.

    Args:
        service_name: Short name like ``"compute"`` or ``"catalog"``.

    Returns:
        The imported module.
    """
    module_path = f"databricks.sdk.service.{service_name}"
    return importlib.import_module(module_path)


def classify_api_class(class_name: str) -> str:
    """Determine whether an API class belongs to account or workspace scope.

    Args:
        class_name: The API class name (e.g. ``"ClustersAPI"``).

    Returns:
        ``"account"`` or ``"workspace"``.
    """
    if class_name in ACCOUNT_API_CLASSES:
        return "account"
    return "workspace"


def get_service_api_classes(service_name: str) -> Dict[str, List[str]]:
    """Get API classes for a service, grouped by scope.

    Args:
        service_name: Short name like ``"compute"``.

    Returns:
        Dict with keys ``"account"`` and ``"workspace"``, each
        containing a list of API class names.
    """
    module = load_service_module(service_name)
    from stackql_databricks_provider.extract import get_resources

    resources = get_resources(module)
    result: Dict[str, List[str]] = {"account": [], "workspace": []}
    for class_name, _ in resources:
        scope = classify_api_class(class_name)
        result[scope].append(class_name)
    return result


def get_all_services_by_scope() -> Dict[str, List[Tuple[str, str]]]:
    """Return all (service_module_name, api_class_name) pairs grouped by scope.

    Returns:
        Dict with ``"account"`` and ``"workspace"`` keys, each
        containing a list of ``(service_name, class_name)`` tuples.
    """
    result: Dict[str, List[Tuple[str, str]]] = {"account": [], "workspace": []}
    for svc in SERVICE_MODULES:
        try:
            groups = get_service_api_classes(svc)
            for cls_name in groups["account"]:
                result["account"].append((svc, cls_name))
            for cls_name in groups["workspace"]:
                result["workspace"].append((svc, cls_name))
        except Exception as e:
            logger.error("Failed to process service %s: %s", svc, e)
    logger.info(
        "Registry: %d account APIs, %d workspace APIs",
        len(result["account"]),
        len(result["workspace"]),
    )
    return result
