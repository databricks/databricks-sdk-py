from databricks.sdk import WorkspaceClient
from databricks.sdk.service import _internal
import time, base64, os

w = WorkspaceClient()

model = w.model_registry.create_model(name=f'sdk-{time.time_ns()}')

created = w.model_registry.create_model_version(name=model.registered_model.name, source="dbfs:/tmp")
