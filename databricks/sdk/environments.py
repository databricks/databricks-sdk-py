from dataclasses import dataclass
from enum import Enum
from typing import Optional

from .azure import ARM_DATABRICKS_RESOURCE_ID, ENVIRONMENTS, AzureEnvironment


class Cloud(Enum):
    AWS = "AWS"
    AZURE = "AZURE"
    GCP = "GCP"


@dataclass
class DatabricksEnvironment:
    cloud: Cloud
    dns_zone: str
    azure_application_id: Optional[str] = None
    azure_environment: Optional[AzureEnvironment] = None

    def deployment_url(self, name: str) -> str:
        return f"https://{name}{self.dns_zone}"

    @property
    def azure_service_management_endpoint(self) -> Optional[str]:
        if self.azure_environment is None:
            return None
        return self.azure_environment.service_management_endpoint

    @property
    def azure_resource_manager_endpoint(self) -> Optional[str]:
        if self.azure_environment is None:
            return None
        return self.azure_environment.resource_manager_endpoint

    @property
    def azure_active_directory_endpoint(self) -> Optional[str]:
        if self.azure_environment is None:
            return None
        return self.azure_environment.active_directory_endpoint


DEFAULT_ENVIRONMENT = DatabricksEnvironment(Cloud.AWS, ".cloud.databricks.com")

ALL_ENVS = [
    DatabricksEnvironment(Cloud.AWS, ".dev.databricks.com"),
    DatabricksEnvironment(Cloud.AWS, ".staging.cloud.databricks.com"),
    DatabricksEnvironment(Cloud.AWS, ".cloud.databricks.us"), DEFAULT_ENVIRONMENT,
    DatabricksEnvironment(Cloud.AZURE,
                          ".dev.azuredatabricks.net",
                          azure_application_id="62a912ac-b58e-4c1d-89ea-b2dbfc7358fc",
                          azure_environment=ENVIRONMENTS["PUBLIC"]),
    DatabricksEnvironment(Cloud.AZURE,
                          ".staging.azuredatabricks.net",
                          azure_application_id="4a67d088-db5c-48f1-9ff2-0aace800ae68",
                          azure_environment=ENVIRONMENTS["PUBLIC"]),
    DatabricksEnvironment(Cloud.AZURE,
                          ".azuredatabricks.net",
                          azure_application_id=ARM_DATABRICKS_RESOURCE_ID,
                          azure_environment=ENVIRONMENTS["PUBLIC"]),
    DatabricksEnvironment(Cloud.AZURE,
                          ".databricks.azure.us",
                          azure_application_id=ARM_DATABRICKS_RESOURCE_ID,
                          azure_environment=ENVIRONMENTS["USGOVERNMENT"]),
    DatabricksEnvironment(Cloud.AZURE,
                          ".databricks.azure.cn",
                          azure_application_id=ARM_DATABRICKS_RESOURCE_ID,
                          azure_environment=ENVIRONMENTS["CHINA"]),
    DatabricksEnvironment(Cloud.GCP, ".dev.gcp.databricks.com"),
    DatabricksEnvironment(Cloud.GCP, ".staging.gcp.databricks.com"),
    DatabricksEnvironment(Cloud.GCP, ".gcp.databricks.com")
]
