from databricks.sdk import WorkspaceClient
from databricks.sdk.service import _internal
import time, base64, os

w = WorkspaceClient()

all = w.experiments.list_experiments(ml.ListExperimentsRequest())
