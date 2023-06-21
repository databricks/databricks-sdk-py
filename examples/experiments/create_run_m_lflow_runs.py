import time

from databricks.sdk import WorkspaceClient
from databricks.sdk.service import ml

w = WorkspaceClient()

experiment = w.experiments.create_experiment(name=f'sdk-{time.time_ns()}')

created = w.experiments.create_run(experiment_id=experiment.experiment_id,
                                   tags=[ml.RunTag(key="foo", value="bar")])

# cleanup
w.experiments.delete_experiment(experiment_id=experiment.experiment_id)
w.experiments.delete_run(run_id=created.run.info.run_id)
