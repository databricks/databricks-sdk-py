# Paginated responses

On the platform side the Databricks APIs have different wait to deal with pagination:
* Some APIs follow the offset-plus-limit pagination
* Some start their offsets from 0 and some from 1
* Some use the cursor-based iteration
* Others just return all results in a single response

The Databricks SDK for Python hides this  complexity
under `Iterator[T]` abstraction, where multi-page results `yield` items. Python typing helps to auto-complete
the individual item fields.

```python
import logging
from databricks.sdk import WorkspaceClient
w = WorkspaceClient()
for repo in w.repos.list():
    logging.info(f'Found repo: {repo.path}')
```

Please look at the `examples/last_job_runs.py` for a more advanced usage:

```python
import logging
from collections import defaultdict
from datetime import datetime, timezone
from databricks.sdk import WorkspaceClient

latest_state = {}
all_jobs = {}
durations = defaultdict(list)

w = WorkspaceClient()
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
        'last_finished': datetime.fromtimestamp(run.end_time/1000, timezone.utc),
        'average_duration': sum(durations[job_id]) / len(durations[job_id])
    })

for line in sorted(summary, key=lambda s: s['last_finished'], reverse=True):
    logging.info(f'Latest: {line}')
```