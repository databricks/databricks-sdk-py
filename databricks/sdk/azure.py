import logging
from dataclasses import dataclass
from typing import Dict
from urllib import parse

import requests

from .oauth import TokenSource
from .service.provisioning import Workspace


logger = logging.getLogger(__name__)

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


def _load_azure_tenant_id(cfg: 'Config'):
    if not cfg.is_azure or cfg.azure_tenant_id is not None or cfg.host is None:
        return
    logging.debug(f'Loading tenant ID from {cfg.host}/aad/auth')
    resp = requests.get(f'{cfg.host}/aad/auth', allow_redirects=False)
    entra_id_endpoint = resp.headers.get('Location')
    if entra_id_endpoint is None:
        logging.debug(f'No Location header in response from {cfg.host}/aad/auth')
        return
    url = parse.urlparse(entra_id_endpoint)
    cfg.azure_tenant_id = url.path.split('/')[1]
    logging.debug(f'Loaded tenant ID: {cfg.azure_tenant_id}')
