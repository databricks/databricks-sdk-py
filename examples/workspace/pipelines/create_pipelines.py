import os
import time

from databricks.sdk import WorkspaceClient
from databricks.sdk.service import pipelines

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

# cleanup
w.pipelines.delete(pipeline_id=created.pipeline_id)
