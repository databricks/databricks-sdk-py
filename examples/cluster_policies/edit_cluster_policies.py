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

policy = w.cluster_policies.get(get=created.policy_id)

w.cluster_policies.edit(policy_id=policy.policy_id,
                        name=policy.name,
                        definition="""{
            "spark_conf.spark.databricks.delta.preview.enabled": {
                "type": "fixed",
                "value": false
            }
        }
""")

# cleanup
w.cluster_policies.delete(delete=created.policy_id)
