from databricks.sdk import WorkspaceClient
from databricks.sdk.service import _internal, iam, iam, sql, serving, catalog, billing, billing, catalog, sharing, compute, compute, compute, catalog, provisioning, settings, iam, oauth2, sql, sql, sql, files, sql, provisioning, ml, catalog, files, catalog, workspace, compute, catalog, iam, compute, compute, settings, jobs, compute, billing, catalog, catalog, ml, catalog, settings, settings, provisioning, oauth2, iam, pipelines, compute, provisioning, sharing, oauth2, sql, sql, sql, sharing, sharing, catalog, workspace, catalog, workspace, oauth2, iam, serving, settings, sharing, sql, provisioning, catalog, catalog, catalog, catalog, settings, settings, iam, catalog, provisioning, sql, workspace, iam, catalog, settings, provisioning
import time, base64, os

w = WorkspaceClient()

notebook_path = f'/Users/{w.current_user.me().user_name}/sdk-{time.time_ns()}'

created = w.pipelines.create(
    continuous=False,
    name=f'sdk-{time.time_ns()}',
    libraries=[pipelines.PipelineLibrary(notebook=pipelines.NotebookLibrary(path=notebook_path))],
    clusters=[
        pipelines.PipelineCluster(instance_pool_id=os.environ["TEST_INSTANCE_POOL_ID"],
                                  label="default",
                                  num_workers=1,
                                  custom_tags={
                                      "cluster_type": "default",
                                  })
    ])

w.pipelines.update(
    pipeline_id=created.pipeline_id,
    name=f'sdk-{time.time_ns()}',
    libraries=[pipelines.PipelineLibrary(notebook=pipelines.NotebookLibrary(path=notebook_path))],
    clusters=[
        pipelines.PipelineCluster(instance_pool_id=os.environ["TEST_INSTANCE_POOL_ID"],
                                  label="default",
                                  num_workers=1,
                                  custom_tags={
                                      "cluster_type": "default",
                                  })
    ])

# cleanup
w.pipelines.delete(pipeline_id=created.pipeline_id)
