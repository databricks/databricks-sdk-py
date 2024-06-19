from databricks.sdk import WorkspaceClient
from databricks.sdk.service import catalog

w = WorkspaceClient()

all = w.storage_credentials.list(catalog.ListStorageCredentialsRequest())
