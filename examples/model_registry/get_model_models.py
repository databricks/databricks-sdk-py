from databricks.sdk import WorkspaceClient
from databricks.sdk.service import _internal
import time, base64, os

w = WorkspaceClient()

created = w.model_registry.create_model(name=f'sdk-{time.time_ns()}')

model = w.model_registry.get_model(name=created.registered_model.name)
