#!env python3
"""Detailed demonstration of long-running operations

This example goes over the advanced usage of long-running operations like:

    - w.clusters.create
    - w.clusters.delete
    - w.clusters.edit
    - w.clusters.resize
    - w.clusters.restart
    - w.clusters.start
    - w.command_execution.cancel
    - w.command_execution.create
    - w.command_execution.execute
    - a.workspaces.create
    - a.workspaces.update
    - w.serving_endpoints.create
    - w.serving_endpoints.update_config
    - w.jobs.cancel_run
    - w.jobs.repair_run
    - w.jobs.run_now
    - w.jobs.submit
    - w.pipelines.reset
    - w.pipelines.stop
    - w.warehouses.create
    - w.warehouses.delete
    - w.warehouses.edit
    - w.warehouses.start
    - w.warehouses.stop

In this example, you'll learn how block main thread until operation reaches a terminal state or times out.
You'll also learn how to add a custom callback for intermediate state updates.

You can change `logging.INFO` to `logging.DEBUG` to see HTTP traffic performed by SDK under the hood.
"""

import datetime
import logging
import sys
import time

from databricks.sdk import WorkspaceClient
from databricks.sdk.service import compute, jobs

if __name__ == "__main__":
    logging.basicConfig(
        stream=sys.stdout,
        level=logging.INFO,
        format="%(asctime)s [%(name)s][%(levelname)s] %(message)s",
    )

    w = WorkspaceClient()

    # create a dummy file on DBFS that just sleeps for 10 seconds
    py_on_dbfs = f"/home/{w.current_user.me().user_name}/sample.py"
    with w.dbfs.open(py_on_dbfs, write=True, overwrite=True) as f:
        f.write(b'import time; time.sleep(10); print("Hello, World!")')

    # trigger one-time-run job and get waiter object
    waiter = w.jobs.submit(
        run_name=f"py-sdk-run-{time.time()}",
        tasks=[
            jobs.SubmitTask(
                task_key="hello_world",
                new_cluster=compute.ClusterSpec(
                    spark_version=w.clusters.select_spark_version(long_term_support=True),
                    node_type_id=w.clusters.select_node_type(local_disk=True),
                    num_workers=1,
                ),
                spark_python_task=jobs.SparkPythonTask(python_file=f"dbfs:{py_on_dbfs}"),
            )
        ],
    )

    logging.info(f"starting to poll: {waiter.run_id}")

    # callback, that receives a polled entity between state updates
    def print_status(run: jobs.Run):
        statuses = [f"{t.task_key}: {t.state.life_cycle_state}" for t in run.tasks]
        logging.info(f'workflow intermediate status: {", ".join(statuses)}')

    # If you want to perform polling in a separate thread, process, or service,
    # you can use w.jobs.wait_get_run_job_terminated_or_skipped(
    #   run_id=waiter.run_id,
    #   timeout=datetime.timedelta(minutes=15),
    #   callback=print_status) to achieve the same results.
    #
    # Waiter interface allows for `w.jobs.submit(..).result()` simplicity in
    # the scenarios, where you need to block the calling thread for the job to finish.
    run = waiter.result(timeout=datetime.timedelta(minutes=15), callback=print_status)

    logging.info(f"job finished: {run.run_page_url}")
