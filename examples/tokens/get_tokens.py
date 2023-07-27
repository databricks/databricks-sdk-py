import time

from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

token = w.tokens.create(comment=f'sdk-{time.time_ns()}', lifetime_seconds=300)

by_name = w.tokens.get(comment=token.token_info.comment)

# cleanup
w.tokens.delete(token_id=token.token_info.token_id)
