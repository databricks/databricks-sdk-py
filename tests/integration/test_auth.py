import base64
import json
import shutil
import subprocess
import sys
import urllib.parse
from pathlib import Path

import io
import pytest

from databricks.sdk.service.compute import ClusterSpec, Library
from databricks.sdk.service.workspace import Language
from databricks.sdk.service.jobs import Task, NotebookTask, ViewType


@pytest.fixture
def fresh_wheel_file(tmp_path) -> Path:
    this_file = Path(__file__)
    project_root = this_file.parent.parent.parent.absolute()
    build_root = tmp_path / 'databricks-sdk-py'
    shutil.copytree(project_root, build_root)
    try:
        completed_process = subprocess.run(
            [sys.executable, 'setup.py', 'bdist_wheel'],
            capture_output=True,
            cwd=build_root)
        if completed_process.returncode != 0:
            raise RuntimeError(completed_process.stderr)

        from databricks.sdk.version import __version__
        filename = f'databricks_sdk-{__version__}-py3-none-any.whl'
        wheel_file = build_root / 'dist' / filename

        return wheel_file
    except subprocess.CalledProcessError as e:
        raise RuntimeError(e.stderr)


def test_runtime_auth(w, fresh_wheel_file, env_or_skip, random):
    instance_pool_id = env_or_skip('TEST_INSTANCE_POOL_ID')

    v = w.clusters.spark_versions()
    lts_runtimes = [x for x in v.versions if 'LTS' in x.name
                    and '-ml' not in x.key
                    and '-photon' not in x.key]

    dbfs_wheel = f'/tmp/wheels/{random(10)}/{fresh_wheel_file.name}'
    with fresh_wheel_file.open('rb') as f:
        w.dbfs.upload(dbfs_wheel, f)

    notebook_path = f'/Users/{w.current_user.me().user_name}/notebook-native-auth'
    notebook_content = io.BytesIO(b'''
from databricks.sdk import WorkspaceClient
w = WorkspaceClient()
me = w.current_user.me()
print(me.user_name)''')
    w.workspace.upload(notebook_path, notebook_content,
                       language=Language.PYTHON,
                       overwrite=True)

    tasks = []
    for v in lts_runtimes:
        t = Task(task_key=f'test_{v.key.replace(".", "_")}',
                 notebook_task=NotebookTask(notebook_path=notebook_path),
                 new_cluster=ClusterSpec(spark_version=v.key,
                                         num_workers=1,
                                         instance_pool_id=instance_pool_id),
                 libraries=[Library(whl=f'dbfs:{dbfs_wheel}')])
        tasks.append(t)
    w.jobs.create(tasks=tasks, name=f'Runtime Native Auth {random(10)}')

    print(v)

def test_job_output(w):
    # workflow_runs = w.jobs.list_runs(job_id=133270013770420)
    this_run = w.jobs.get_run(20504473)

    import re
    notebook_model = re.compile(r"var __DATABRICKS_NOTEBOOK_MODEL = '(.*)';", re.MULTILINE)

    for task_run in this_run.tasks:
        print(task_run.task_key)
        run_output = w.jobs.export_run(task_run.run_id)
        for view in run_output.views:
            if view.type != ViewType.NOTEBOOK:
                continue
            for b64 in notebook_model.findall(view.content):
                url_encoded: bytes = base64.b64decode(b64)
                json_encoded = urllib.parse.unquote(str(url_encoded))
                x = json.loads(json_encoded)
                print(x)
