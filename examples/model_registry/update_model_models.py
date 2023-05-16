import time

from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

created = w.model_registry.create_model(name=f'sdk-{time.time_ns()}')

w.model_registry.update_model(name=created.registered_model.name, description=f'sdk-{time.time_ns()}')
