import time

from databricks.sdk import WorkspaceClient
from databricks.sdk.service import iam

w = WorkspaceClient()

created = w.service_principals.create(display_name=f'sdk-{time.time_ns()}')

w.service_principals.update(id=created.id,
                            display_name=f'sdk-{time.time_ns()}',
                            roles=[iam.ComplexValue(value="xyz")])

# cleanup
w.service_principals.delete(id=created.id)
