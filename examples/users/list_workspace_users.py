from databricks.sdk import WorkspaceClient
from databricks.sdk.service import _internal
import time, base64, os

w = WorkspaceClient()

all_users = w.users.list(attributes="id,userName",
                         sort_by="userName",
                         sort_order=iam.ListSortOrder.DESCENDING)
