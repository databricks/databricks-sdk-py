import time

from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

model = w.model_registry.create_model(name=f'sdk-{time.time_ns()}')

mv = w.model_registry.create_model_version(name=model.registered_model.name, source="dbfs:/tmp")

created = w.model_registry.create_comment(comment=f'sdk-{time.time_ns()}',
                                          name=mv.model_version.name,
                                          version=mv.model_version.version)

_ = w.model_registry.update_comment(comment=f'sdk-{time.time_ns()}', id=created.comment.id)

# cleanup
w.model_registry.delete_comment(id=created.comment.id)
