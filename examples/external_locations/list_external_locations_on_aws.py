from databricks.sdk import WorkspaceClient
from databricks.sdk.service import _internal
import time, base64, os

w = WorkspaceClient()

all = w.external_locations.list(catalog.ListExternalLocationsRequest())
