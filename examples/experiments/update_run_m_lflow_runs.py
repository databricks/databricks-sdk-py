from databricks.sdk import WorkspaceClient
from databricks.sdk.service import _internal, iam, iam, sql, serving, catalog, billing, billing, catalog, sharing, compute, compute, compute, catalog, provisioning, settings, iam, oauth2, sql, sql, sql, files, sql, provisioning, ml, catalog, files, catalog, workspace, compute, catalog, iam, compute, compute, settings, jobs, compute, billing, catalog, catalog, ml, catalog, settings, settings, provisioning, oauth2, iam, pipelines, compute, provisioning, sharing, oauth2, sql, sql, sql, sharing, sharing, catalog, workspace, catalog, workspace, oauth2, iam, serving, settings, sharing, sql, provisioning, catalog, catalog, catalog, catalog, settings, settings, iam, catalog, provisioning, sql, workspace, iam, catalog, settings, provisioning
import time, base64, os

w = WorkspaceClient()

experiment = w.experiments.create_experiment(name=f'sdk-{time.time_ns()}')

created = w.experiments.create_run(experiment_id=experiment.experiment_id,
                                   tags=[ml.RunTag(key="foo", value="bar")])

_ = w.experiments.update_run(run_id=created.run.info.run_id, status=ml.UpdateRunStatus.KILLED)

# cleanup
w.experiments.delete_experiment(experiment_id=experiment.experiment_id)
w.experiments.delete_run(run_id=created.run.info.run_id)
