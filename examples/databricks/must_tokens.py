from databricks.sdk import WorkspaceClient
from databricks.sdk.service import _internal
import time, base64, os

w = WorkspaceClient()

token = w.tokens.create(comment=f'sdk-{time.time_ns()}', lifetime_seconds=300)

wsc_inner = w.databricks.must(
    new_workspace_client(databricks.Config(host=w.config.host, token=token.token_value, auth_type="pat")))

# cleanup
w.tokens.delete(token_id=token.token_info.token_id)
