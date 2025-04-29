from databricks.sdk import WorkspaceClient
from databricks.sdk.errors import NotFound
from databricks.sdk.service.settings import DefaultNamespaceSetting, StringMessage

default_catalog = "hive_metastore"

ws = WorkspaceClient()
default_namespace = ws.settings.default_namespace

# needs to get the etag first, before patching the setting
try:
    etag = default_namespace.get().etag
except NotFound as err:
    # if not found, the etag is returned in the header
    etag = err.details[0].metadata.get("etag")

default_namespace.update(
    allow_missing=True,
    field_mask="namespace.value",
    setting=DefaultNamespaceSetting(etag=etag, namespace=StringMessage(default_catalog)),
)
