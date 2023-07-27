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

policy = w.cluster_policies.get(policy_id=created.policy_id)

# cleanup
w.cluster_policies.delete(policy_id=created.policy_id)
