import time

from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

model = w.model_registry.create_model(name=f'sdk-{time.time_ns()}')

created = w.model_registry.create_model_version(name=model.registered_model.name, source="dbfs:/tmp")

w.model_registry.update_model_version(description=f'sdk-{time.time_ns()}',
                                      name=created.model_version.name,
                                      version=created.model_version.version)
