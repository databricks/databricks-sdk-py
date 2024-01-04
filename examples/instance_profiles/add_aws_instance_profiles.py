from databricks.sdk import WorkspaceClient
from databricks.sdk.service import _internal
import time, base64, os

w = WorkspaceClient()

arn = "arn:aws:iam::000000000000:instance-profile/abc"

w.instance_profiles.add(instance_profile_arn=arn,
                        skip_validation=True,
                        iam_role_arn="arn:aws:iam::000000000000:role/bcd")
