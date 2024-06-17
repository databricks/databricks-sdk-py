import time

from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

experiment = w.experiments.create_experiment(name=f'sdk-{time.time_ns()}')

_ = w.experiments.get_experiment(experiment_id=experiment.experiment_id)

# cleanup
w.experiments.delete_experiment(experiment_id=experiment.experiment_id)
