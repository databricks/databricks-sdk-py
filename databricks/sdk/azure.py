from dataclasses import dataclass


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
