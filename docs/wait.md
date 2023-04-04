# Long-running operations

When you invoke a long-running operation, the SDK provides a high-level API to _trigger_ these operations and _wait_ for the related entities
to reach the correct state or return the error message in case of failure. All long-running operations return generic `Wait` instance with `result()`
method to get a result of long-running operation, once it's finished. Databricks SDK for Python picks the most reasonable default timeouts for
every method, but sometimes you may find yourself in a situation, where you'd want to provide `datatime.timedelta()` as the value of `timeout`
argument to `result()` method.

There are a number of long-runng opereations in Databricks APIs such as managing:
* Clusters,
* Command execution
* Jobs
* Libraries
* Delta Live Tables pipelines
* Databricks SQL warehouses.

For example, in the Clusters API, once you create a cluster, you receive a cluster ID, and the cluster is in the `PENDING` state Meanwhile
Databricks takes care of provisioning virtual machines from the cloud provider in the background. The cluster is
only usable in the `RUNNING` state and so you have to wait for that state to be reached.

Another example is the API for running a job or repairing the run: right after
the run starts, the run is in the `PENDING` state. The job is only considered to be finished when it is in either
the `TERMINATED` or `SKIPPED` state. Also you would likely need the error message if the long-running
operation times out failed with an error code. Other times you may want to configure a custom timeout other than
the default of 20 minutes.

In the following example, `w.clusters.create` returns `ClusterInfo` only once the cluster is in the `RUNNING` state,
otherwise it will timeout in 10 minutes:

```python
import datetime
import logging
from databricks.sdk import WorkspaceClient

w = WorkspaceClient()
info = w.clusters.create_and_wait(cluster_name='Created cluster',
                                  spark_version='12.0.x-scala2.12',
                                  node_type_id='m5d.large',
                                  autotermination_minutes=10,
                                  num_workers=1,
                                  timeout=datetime.timedelta(minutes=10))
logging.info(f'Created: {info}')
```

Please look at the `examples/starting_job_and_waiting.py` for a more advanced usage:

```python
import datetime
import logging
import time

from databricks.sdk import WorkspaceClient
import databricks.sdk.service.jobs as j

w = WorkspaceClient()

# create a dummy file on DBFS that just sleeps for 10 seconds
py_on_dbfs = f'/home/{w.current_user.me().user_name}/sample.py'
with w.dbfs.open(py_on_dbfs, write=True, overwrite=True) as f:
    f.write(b'import time; time.sleep(10); print("Hello, World!")')

# trigger one-time-run job and get waiter object
waiter = w.jobs.submit(run_name=f'py-sdk-run-{time.time()}', tasks=[
    j.RunSubmitTaskSettings(
        task_key='hello_world',
        new_cluster=j.BaseClusterInfo(
            spark_version=w.clusters.select_spark_version(long_term_support=True),
            node_type_id=w.clusters.select_node_type(local_disk=True),
            num_workers=1
        ),
        spark_python_task=j.SparkPythonTask(
            python_file=f'dbfs:{py_on_dbfs}'
        ),
    )
])

logging.info(f'starting to poll: {waiter.run_id}')

# callback, that receives a polled entity between state updates
def print_status(run: j.Run):
    statuses = [f'{t.task_key}: {t.state.life_cycle_state}' for t in run.tasks]
    logging.info(f'workflow intermediate status: {", ".join(statuses)}')

# If you want to perform polling in a separate thread, process, or service,
# you can use w.jobs.wait_get_run_job_terminated_or_skipped(
#   run_id=waiter.run_id,
#   timeout=datetime.timedelta(minutes=15),
#   callback=print_status) to achieve the same results.
#
# Waiter interface allows for `w.jobs.submit(..).result()` simplicity in
# the scenarios, where you need to block the calling thread for the job to finish.
run = waiter.result(timeout=datetime.timedelta(minutes=15),
                    callback=print_status)

logging.info(f'job finished: {run.run_page_url}')
```
