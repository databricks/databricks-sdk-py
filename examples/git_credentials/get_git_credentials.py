from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

cr = w.git_credentials.create(git_provider="gitHub", git_username="test", personal_access_token="test")

by_id = w.git_credentials.get(get=cr.credential_id)

# cleanup
w.git_credentials.delete(delete=cr.credential_id)
