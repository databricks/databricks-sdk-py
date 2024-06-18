import time

from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

cr = w.git_credentials.create(git_provider="gitHub", git_username="test", personal_access_token="test")

w.git_credentials.update(credential_id=cr.credential_id,
                         git_provider="gitHub",
                         git_username=f'sdk-{time.time_ns()}@example.com',
                         personal_access_token=f'sdk-{time.time_ns()}')

# cleanup
w.git_credentials.delete(credential_id=cr.credential_id)
