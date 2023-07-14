import datetime
import logging


def test_jobs(w):
    found = 0
    for job in w.jobs.list():
        logging.info(f'Looking at {job.settings.name}')
        found += 1
    assert found > 0


def test_submitting_jobs(w, random, env_or_skip):
    from databricks.sdk.service import compute, jobs

    py_on_dbfs = f'/home/{w.current_user.me().user_name}/sample.py'
    with w.dbfs.open(py_on_dbfs, write=True, overwrite=True) as f:
        f.write(b'import time; time.sleep(10); print("Hello, World!")')

    waiter = w.jobs.submit(run_name=f'py-sdk-{random(8)}',
                           tasks=[
                               jobs.SubmitTask(
                                   task_key='pi',
                                   new_cluster=compute.ClusterSpec(
                                       spark_version=w.clusters.select_spark_version(long_term_support=True),
                                       # node_type_id=w.clusters.select_node_type(local_disk=True),
                                       instance_pool_id=env_or_skip('TEST_INSTANCE_POOL_ID'),
                                       num_workers=1),
                                   spark_python_task=jobs.SparkPythonTask(python_file=f'dbfs:{py_on_dbfs}'),
                               )
                           ])

    logging.info(f'starting to poll: {waiter.run_id}')

    def print_status(run: jobs.Run):
        statuses = [f'{t.task_key}: {t.state.life_cycle_state}' for t in run.tasks]
        logging.info(f'workflow intermediate status: {", ".join(statuses)}')

    run = waiter.result(timeout=datetime.timedelta(minutes=15), callback=print_status)

    logging.info(f'job finished: {run.run_page_url}')


def test_last_job_runs(w):
    from collections import defaultdict
    from datetime import datetime, timezone

    latest_state = {}
    all_jobs = {}
    durations = defaultdict(list)

    for job in w.jobs.list():
        all_jobs[job.job_id] = job
        for run in w.jobs.list_runs(job_id=job.job_id, expand_tasks=False):
            durations[job.job_id].append(run.run_duration)
            if job.job_id not in latest_state:
                latest_state[job.job_id] = run
                continue
            if run.end_time < latest_state[job.job_id].end_time:
                continue
            latest_state[job.job_id] = run

    summary = []
    for job_id, run in latest_state.items():
        summary.append({
            'job_name': all_jobs[job_id].settings.name,
            'last_status': run.state.result_state,
            'last_finished': datetime.fromtimestamp(run.end_time / 1000, timezone.utc),
            'average_duration': sum(durations[job_id]) / len(durations[job_id])
        })

    for line in sorted(summary, key=lambda s: s['last_finished'], reverse=True):
        logging.info(f'Latest: {line}')


def test_create_job(w):
    from databricks.sdk.service import compute, jobs

    cluster = jobs.JobCluster(job_cluster_key="cluster1",
                              new_cluster=compute.ClusterSpec(
                                  num_workers=2,
                                  spark_version=w.clusters.select_spark_version(),
                                  node_type_id=w.clusters.select_node_type(local_disk=True)))

    task1 = jobs.Task(task_key="task1",
                      job_cluster_key="cluster1",
                      python_wheel_task=jobs.PythonWheelTask(entry_point="test", package_name="deepspeed"))

    w.jobs.create(job_clusters=[cluster], tasks=[task1])

def test_permission_level_job(w):
    from databricks.sdk.service import jobs, iam, compute
    
    task1 = jobs.Task(task_key="task1",
                      job_cluster_key="cluster1",
                      python_wheel_task=jobs.PythonWheelTask(entry_point="test", package_name="deepspeed"))
    
    cluster = jobs.JobCluster(job_cluster_key="cluster1",
                              new_cluster=compute.ClusterSpec(
                                  num_workers=2,
                                  spark_version=w.clusters.select_spark_version(),
                                  node_type_id=w.clusters.select_node_type(local_disk=True)))
    
    access_control_list = [
        iam.AccessControlRequest(
            group_name = 'gp_manage',
            permission_level = iam.PermissionLevel('CAN_MANAGE')
        ),
        iam.AccessControlRequest(
            group_name = 'gp_read',
            permission_level = iam.PermissionLevel('CAN_READ')
        )
    ]

    w.jobs.create(job_clusters=[cluster], tasks=[task1], access_control_list = [access_control_list])
