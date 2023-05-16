from databricks.sdk import WorkspaceClient
from databricks.sdk.service import ml

w = WorkspaceClient()

all = w.model_registry.list_webhooks(ml.ListWebhooksRequest())
