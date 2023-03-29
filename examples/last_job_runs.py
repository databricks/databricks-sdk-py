#!env python3
import logging
import sys
from collections import defaultdict
from datetime import datetime, timezone
from databricks.sdk import WorkspaceClient


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout, level=logging.INFO,
                        format='%(asctime)s [%(name)s][%(levelname)s] %(message)s')

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
