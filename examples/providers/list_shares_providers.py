import time

from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

public_share_recipient = """{
        "shareCredentialsVersion":1,
        "bearerToken":"dapiabcdefghijklmonpqrstuvwxyz",
        "endpoint":"https://sharing.delta.io/delta-sharing/"
    }
"""

created = w.providers.create(name=f'sdk-{time.time_ns()}', recipient_profile_str=public_share_recipient)

shares = w.providers.list_shares(name=created.name)

# cleanup
w.providers.delete(name=created.name)
