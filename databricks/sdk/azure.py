from dataclasses import dataclass
from typing import Dict

from .oauth import TokenSource
from .service.provisioning import Workspace


@dataclass
class AzureEnvironment:
    name: str
    service_management_endpoint: str
    resource_manager_endpoint: str
    active_directory_endpoint: str


ARM_DATABRICKS_RESOURCE_ID = "2ff814a6-3304-4ab8-85cb-cd0e6f879c1d"

ENVIRONMENTS = dict(
    PUBLIC=AzureEnvironment(name="PUBLIC",
                            service_management_endpoint="https://management.core.windows.net/",
                            resource_manager_endpoint="https://management.azure.com/",
                            active_directory_endpoint="https://login.microsoftonline.com/"),
    USGOVERNMENT=AzureEnvironment(name="USGOVERNMENT",
                                  service_management_endpoint="https://management.core.usgovcloudapi.net/",
                                  resource_manager_endpoint="https://management.usgovcloudapi.net/",
                                  active_directory_endpoint="https://login.microsoftonline.us/"),
    CHINA=AzureEnvironment(name="CHINA",
                           service_management_endpoint="https://management.core.chinacloudapi.cn/",
                           resource_manager_endpoint="https://management.chinacloudapi.cn/",
                           active_directory_endpoint="https://login.chinacloudapi.cn/"),
)


def add_workspace_id_header(cfg: 'Config', headers: Dict[str, str]):
    if cfg.azure_workspace_resource_id:
        headers["X-Databricks-Azure-Workspace-Resource-Id"] = cfg.azure_workspace_resource_id


def add_sp_management_token(token_source: 'TokenSource', headers: Dict[str, str]):
    mgmt_token = token_source.token()
    headers['X-Databricks-Azure-SP-Management-Token'] = mgmt_token.access_token


def get_azure_resource_id(workspace: Workspace):
    """
    Returns the Azure Resource ID for the given workspace, if it is an Azure workspace.
    :param workspace:
    :return:
    """
    if workspace.azure_workspace_info is None:
        return None
    return (f'/subscriptions/{workspace.azure_workspace_info.subscription_id}'
            f'/resourceGroups/{workspace.azure_workspace_info.resource_group}'
            f'/providers/Microsoft.Databricks/workspaces/{workspace.workspace_name}')
