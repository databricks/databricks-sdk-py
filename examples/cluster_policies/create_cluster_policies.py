import time

from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

created = w.cluster_policies.create(name=f'sdk-{time.time_ns()}',
                                    definition="""{
            "spark_conf.spark.databricks.delta.preview.enabled": {
                "type": "fixed",
                "value": true
            }
        }
""")

# cleanup
w.cluster_policies.delete(delete=created.policy_id)
