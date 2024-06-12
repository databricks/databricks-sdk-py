from databricks.sdk import WorkspaceClient
from databricks.sdk.service import iam

w = WorkspaceClient()

all = w.service_principals.list(iam.ListServicePrincipalsRequest())
