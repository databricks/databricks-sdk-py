from databricks.sdk import WorkspaceClient
from databricks.sdk.service import ml

w = WorkspaceClient()

all = w.experiments.list_experiments(ml.ListExperimentsRequest())
