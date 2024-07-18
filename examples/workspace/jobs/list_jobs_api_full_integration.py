from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

job_list = w.jobs.list(expand_tasks=False)
