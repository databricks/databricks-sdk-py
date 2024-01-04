from databricks.sdk import WorkspaceClient
from databricks.sdk.service import _internal
import time, base64, os

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
w.cluster_policies.delete(policy_id=created.policy_id)
