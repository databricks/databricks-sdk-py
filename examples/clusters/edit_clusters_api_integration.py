from databricks.sdk import WorkspaceClient
from databricks.sdk.service import _internal, iam, iam, sql, serving, catalog, billing, billing, catalog, sharing, compute, compute, compute, catalog, provisioning, settings, iam, oauth2, sql, sql, sql, files, sql, provisioning, ml, catalog, files, catalog, workspace, compute, catalog, iam, compute, compute, settings, jobs, compute, billing, catalog, catalog, ml, catalog, settings, settings, provisioning, oauth2, iam, pipelines, compute, provisioning, sharing, oauth2, sql, sql, sql, sharing, sharing, catalog, workspace, catalog, workspace, oauth2, iam, serving, settings, sharing, sql, provisioning, catalog, catalog, catalog, catalog, settings, settings, iam, catalog, provisioning, sql, workspace, iam, catalog, settings, provisioning
import time, base64, os

w = WorkspaceClient()

cluster_name = f'sdk-{time.time_ns()}'

latest = w.clusters.select_spark_version(latest=True)

clstr = w.clusters.create(cluster_name=cluster_name,
                          spark_version=latest,
                          instance_pool_id=os.environ["TEST_INSTANCE_POOL_ID"],
                          autotermination_minutes=15,
                          num_workers=1).result()

_ = w.clusters.edit(cluster_id=clstr.cluster_id,
                    spark_version=latest,
                    cluster_name=cluster_name,
                    instance_pool_id=os.environ["TEST_INSTANCE_POOL_ID"],
                    autotermination_minutes=10,
                    num_workers=2).result()

# cleanup
w.clusters.permanent_delete(cluster_id=clstr.cluster_id)
