import time

from databricks.sdk import WorkspaceClient
from databricks.sdk.service import ml

w = WorkspaceClient()

created = w.model_registry.create_webhook(description=f'sdk-{time.time_ns()}',
                                          events=[ml.RegistryWebhookEvent.MODEL_VERSION_CREATED],
                                          http_url_spec=ml.HttpUrlSpec(url=w.config.host))

w.model_registry.update_webhook(id=created.webhook.id, description=f'sdk-{time.time_ns()}')

# cleanup
w.model_registry.delete_webhook(id=created.webhook.id)
