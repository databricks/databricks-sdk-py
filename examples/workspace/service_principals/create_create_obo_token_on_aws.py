import time

from databricks.sdk import WorkspaceClient
from databricks.sdk.service import iam

w = WorkspaceClient()

groups = w.groups.group_display_name_to_id_map(iam.ListGroupsRequest())

spn = w.service_principals.create(
    display_name=f"sdk-{time.time_ns()}",
    groups=[iam.ComplexValue(value=groups["admins"])],
)

# cleanup
w.service_principals.delete(id=spn.id)
