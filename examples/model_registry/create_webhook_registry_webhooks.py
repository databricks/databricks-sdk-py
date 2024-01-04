from databricks.sdk import WorkspaceClient
from databricks.sdk.service import _internal
import time, base64, os

w = WorkspaceClient()

created = w.model_registry.create_webhook(description=f'sdk-{time.time_ns()}',
                                          events=[ml.RegistryWebhookEvent.MODEL_VERSION_CREATED],
                                          http_url_spec=ml.HttpUrlSpec(url=w.config.host))

# cleanup
w.model_registry.delete_webhook(id=created.webhook.id)
