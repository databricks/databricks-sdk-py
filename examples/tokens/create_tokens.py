import time

from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

token = w.tokens.create(comment=f'sdk-{time.time_ns()}', lifetime_seconds=300)

# cleanup
w.tokens.delete(delete=token.token_info.token_id)
