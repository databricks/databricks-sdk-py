#!env python3
import logging
import sys

from databricks.sdk import WorkspaceClient
from databricks.sdk.service import jobs

if __name__ == "__main__":
    logging.basicConfig(stream=sys.stdout,
                        level=logging.INFO,
                        format="%(asctime)s [%(name)s][%(levelname)s] %(message)s",
                        )

    w = WorkspaceClient()

    # we set expand_tasks to true because the cluster information will exist in the tasks
    job_runs = w.jobs.list_runs(expand_tasks=True)

    for run in job_runs:
        # filter to SubmitRun jobs
        if run.run_type == jobs.RunType.SUBMIT_RUN:
            tasks = run.tasks

            compute_used = []
            # Iterate over tasks in the run
            for task in run.tasks:
                '''
                - Tasks with All Purpose clusters will have an existing_cluster_id
                - Tasks with a Jobs cluster will have the new_cluster represented as ClusterSpec
                - SQL tasks will have a sql_warehouse_id
                '''
                task_compute = (
                    {"existing_cluster_id": task.existing_cluster_id} if task.existing_cluster_id else
                    {"new_cluster": task.new_cluster} if task.new_cluster else
                    {"sql_warehouse_id": task.sql_task.warehouse_id} if task.sql_task else
                    {}
                )

                # Append the task compute info to a list for the job
                compute_used.append(task_compute)
            
            logging.info(f"run_id: {run.run_id}, compute_used: {compute_used}")
