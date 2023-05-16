from databricks.sdk import WorkspaceClient
from databricks.sdk.service import sharing

w = WorkspaceClient()

all = w.recipients.list(sharing.ListRecipientsRequest())
