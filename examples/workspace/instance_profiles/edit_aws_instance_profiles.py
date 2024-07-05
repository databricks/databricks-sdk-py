from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

arn = "arn:aws:iam::000000000000:instance-profile/abc"

w.instance_profiles.edit(instance_profile_arn=arn, iam_role_arn="arn:aws:iam::000000000000:role/bcdf")
