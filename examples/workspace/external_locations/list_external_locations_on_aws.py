from databricks.sdk import WorkspaceClient
from databricks.sdk.service import catalog

w = WorkspaceClient()

all = w.external_locations.list(catalog.ListExternalLocationsRequest())
