from databricks.sdk import WorkspaceClient
from databricks.sdk.service import iam

w = WorkspaceClient()

all_users = w.users.list(attributes="id,userName",
                         sort_by="userName",
                         sort_order=iam.ListSortOrder.DESCENDING)
