import time

from databricks.sdk import WorkspaceClient
from databricks.sdk.service import settings

w = WorkspaceClient()

created = w.ip_access_lists.create(label=f'sdk-{time.time_ns()}',
                                   ip_addresses=["1.0.0.0/16"],
                                   list_type=settings.ListType.BLOCK)

by_id = w.ip_access_lists.get(ip_access_list_id=created.ip_access_list.list_id)

# cleanup
w.ip_access_lists.delete(ip_access_list_id=created.ip_access_list.list_id)
