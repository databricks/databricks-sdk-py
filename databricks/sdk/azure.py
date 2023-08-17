from dataclasses import dataclass
from typing import Dict

from .oauth import TokenSource


@dataclass
class AzureEnvironment:
    name: str
    service_management_endpoint: str
    resource_manager_endpoint: str
    active_directory_endpoint: str


ARM_DATABRICKS_RESOURCE_ID = "2ff814a6-3304-4ab8-85cb-cd0e6f879c1d"

ENVIRONMENTS = dict(
    PUBLIC=AzureEnvironment(name="AzurePublicCloud",
                            service_management_endpoint="https://management.core.windows.net/",
                            resource_manager_endpoint="https://management.azure.com/",
                            active_directory_endpoint="https://login.microsoftonline.com/"),
    GERMAN=AzureEnvironment(name="AzureGermanCloud",
                            service_management_endpoint="https://management.core.cloudapi.de/",
                            resource_manager_endpoint="https://management.microsoftazure.de/",
                            active_directory_endpoint="https://login.microsoftonline.de/"),
    USGOVERNMENT=AzureEnvironment(name="AzureUSGovernmentCloud",
                                  service_management_endpoint="https://management.core.usgovcloudapi.net/",
                                  resource_manager_endpoint="https://management.usgovcloudapi.net/",
                                  active_directory_endpoint="https://login.microsoftonline.us/"),
    CHINA=AzureEnvironment(name="AzureChinaCloud",
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
