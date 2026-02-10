import base64
import io
import json
import re
import shutil
import subprocess
import sys
import typing
import urllib.parse
from functools import partial
from pathlib import Path

import pytest

from databricks.sdk import AccountClient, WorkspaceClient
from databricks.sdk.service import iam, oauth2
from databricks.sdk.service.compute import (ClusterSpec, DataSecurityMode,
                                            Library, ResultType, SparkVersion)
from databricks.sdk.service.jobs import NotebookTask, Task, ViewType
from databricks.sdk.service.workspace import ImportFormat


@pytest.fixture
def fresh_wheel_file(tmp_path) -> Path:
    this_file = Path(__file__)
    project_root = this_file.parent.parent.parent.absolute()
    build_root = tmp_path / "databricks-sdk-py"
    shutil.copytree(project_root, build_root)
    try:
        completed_process = subprocess.run(
            [sys.executable, "-m", "build"],
            capture_output=True,
            cwd=build_root,
        )
        if completed_process.returncode != 0:
            raise RuntimeError(completed_process.stderr)

        from databricks.sdk.version import __version__

        filename = f"databricks_sdk-{__version__}-py3-none-any.whl"
        wheel_file = build_root / "dist" / filename

        return wheel_file
    except subprocess.CalledProcessError as e:
        raise RuntimeError(e.stderr)


@pytest.mark.parametrize("mode", [DataSecurityMode.SINGLE_USER, DataSecurityMode.USER_ISOLATION])
def test_runtime_auth_from_interactive_on_uc(ucws, fresh_wheel_file, env_or_skip, random, mode):
    instance_pool_id = env_or_skip("TEST_INSTANCE_POOL_ID")
    latest = ucws.clusters.select_spark_version(latest=True)

    my_user = ucws.current_user.me().user_name

    workspace_location = f"/Users/{my_user}/wheels/{random(10)}"
    ucws.workspace.mkdirs(workspace_location)

    wsfs_wheel = f"{workspace_location}/{fresh_wheel_file.name}"
    with fresh_wheel_file.open("rb") as f:
        ucws.workspace.upload(wsfs_wheel, f, format=ImportFormat.AUTO)

    from databricks.sdk.service.compute import Language

    interactive_cluster = ucws.clusters.create(
        cluster_name=f"native-auth-on-{mode.name}",
        spark_version=latest,
        instance_pool_id=instance_pool_id,
        autotermination_minutes=10,
        num_workers=1,
        data_security_mode=mode,
    ).result()
    ctx = ucws.command_execution.create(cluster_id=interactive_cluster.cluster_id, language=Language.PYTHON).result()
    run = partial(
        ucws.command_execution.execute,
        cluster_id=interactive_cluster.cluster_id,
        context_id=ctx.id,
        language=Language.PYTHON,
    )
    try:
        res = run(command=f"%pip install /Workspace{wsfs_wheel}\ndbutils.library.restartPython()").result()
        results = res.results
        if results.result_type != ResultType.TEXT:
            msg = f"({mode}) unexpected result type: {results.result_type}: {results.summary}\n{results.cause}"
            raise RuntimeError(msg)

        res = run(
            command="\n".join(
                [
                    "from databricks.sdk import WorkspaceClient",
                    "w = WorkspaceClient()",
                    "me = w.current_user.me()",
                    "print(me.user_name)",
                ]
            )
        ).result()
        assert res.results.result_type == ResultType.TEXT, f"unexpected result type: {res.results.result_type}"

        assert my_user == res.results.data, f"unexpected user: {res.results.data}"
    finally:
        ucws.clusters.permanent_delete(interactive_cluster.cluster_id)


def _get_lts_versions(w) -> typing.List[SparkVersion]:
    v = w.clusters.spark_versions()
    lts_runtimes = [
        x
        for x in v.versions
        if "LTS" in x.name and "-ml" not in x.key and "-photon" not in x.key and "-aarch64" not in x.key
    ]
    return lts_runtimes


def test_runtime_auth_from_jobs_volumes(ucws, files_api, fresh_wheel_file, env_or_skip, random, volume):
    dbr_versions = [v for v in _get_lts_versions(ucws) if int(v.key.split(".")[0]) >= 15]

    volume_wheel = f"{volume}/tmp/wheels/{random(10)}/{fresh_wheel_file.name}"
    with fresh_wheel_file.open("rb") as f:
        files_api.upload(volume_wheel, f)

    lib = Library(whl=volume_wheel)
    return _test_runtime_auth_from_jobs_inner(ucws, env_or_skip, random, dbr_versions, lib)


def test_runtime_auth_from_jobs_dbfs(w, fresh_wheel_file, env_or_skip, random):
    # Library installation from DBFS is not supported past DBR 14.3
    dbr_versions = [v for v in _get_lts_versions(w) if int(v.key.split(".")[0]) < 15]

    dbfs_wheel = f"/tmp/wheels/{random(10)}/{fresh_wheel_file.name}"
    with fresh_wheel_file.open("rb") as f:
        w.dbfs.upload(dbfs_wheel, f)

    lib = Library(whl=f"dbfs:{dbfs_wheel}")
    return _test_runtime_auth_from_jobs_inner(w, env_or_skip, random, dbr_versions, lib)


def _test_runtime_auth_from_jobs_inner(w, env_or_skip, random, dbr_versions, library):
    instance_pool_id = env_or_skip("TEST_INSTANCE_POOL_ID")

    my_name = w.current_user.me().user_name
    notebook_path = f"/Users/{my_name}/notebook-native-auth"
    notebook_content = io.BytesIO(
        b"""
from databricks.sdk import WorkspaceClient
w = WorkspaceClient()
me = w.current_user.me()
print(me.user_name)"""
    )

    from databricks.sdk.service.workspace import Language

    w.workspace.upload(
        notebook_path,
        notebook_content,
        language=Language.PYTHON,
        overwrite=True,
    )

    tasks = []
    for v in dbr_versions:
        t = Task(
            task_key=f'test_{v.key.replace(".", "_")}',
            notebook_task=NotebookTask(notebook_path=notebook_path),
            new_cluster=ClusterSpec(
                spark_version=v.key,
                num_workers=1,
                instance_pool_id=instance_pool_id,
                # GCP uses "custom" data security mode by default, which does not support UC.
                data_security_mode=DataSecurityMode.SINGLE_USER,
            ),
            libraries=[library],
        )
        tasks.append(t)

    waiter = w.jobs.submit(run_name=f"Runtime Native Auth {random(10)}", tasks=tasks)
    run = waiter.result()
    for task_key, output in _task_outputs(w, run).items():
        assert my_name in output, f"{task_key} does not work with notebook native auth"


def _task_outputs(w, run):
    notebook_model_re = re.compile(r"var __DATABRICKS_NOTEBOOK_MODEL = '(.*)';", re.MULTILINE)

    task_outputs = {}
    for task_run in run.tasks:
        output = ""
        run_output = w.jobs.export_run(task_run.run_id)
        for view in run_output.views:
            if view.type != ViewType.NOTEBOOK:
                continue
            for b64 in notebook_model_re.findall(view.content):
                url_encoded: bytes = base64.b64decode(b64)
                json_encoded = urllib.parse.unquote(url_encoded.decode("utf-8"))
                notebook_model = json.loads(json_encoded)
                for command in notebook_model["commands"]:
                    results_data = command["results"]["data"]
                    if isinstance(results_data, str):
                        output += results_data
                    else:
                        for data in results_data:
                            output += data["data"]
        task_outputs[task_run.task_key] = output
    return task_outputs


def test_wif_account(ucacct, env_or_skip, random):

    sp = ucacct.service_principals.create(
        active=True,
        display_name="py-sdk-test-" + random(),
        roles=[iam.ComplexValue(value="account_admin")],
    )

    ucacct.service_principal_federation_policy.create(
        policy=oauth2.FederationPolicy(
            oidc_policy=oauth2.OidcFederationPolicy(
                issuer="https://token.actions.githubusercontent.com",
                audiences=["https://github.com/databricks-eng"],
                subject="repo:databricks-eng/eng-dev-ecosystem:environment:integration-tests",
            )
        ),
        service_principal_id=sp.id,
    )

    ac = AccountClient(
        host=ucacct.config.host,
        account_id=ucacct.config.account_id,
        client_id=sp.application_id,
        auth_type="github-oidc",
        token_audience="https://github.com/databricks-eng",
    )

    groups = ac.groups.list()

    next(groups)


def test_wif_workspace(ucacct, env_or_skip, random):

    workspace_id = env_or_skip("TEST_WORKSPACE_ID")
    workspace_url = env_or_skip("TEST_WORKSPACE_URL")

    sp = ucacct.service_principals.create(
        active=True,
        display_name="py-sdk-test-" + random(),
    )

    ucacct.service_principal_federation_policy.create(
        policy=oauth2.FederationPolicy(
            oidc_policy=oauth2.OidcFederationPolicy(
                issuer="https://token.actions.githubusercontent.com",
                audiences=["https://github.com/databricks-eng"],
                subject="repo:databricks-eng/eng-dev-ecosystem:environment:integration-tests",
            )
        ),
        service_principal_id=sp.id,
    )

    ucacct.workspace_assignment.update(
        workspace_id=workspace_id,
        principal_id=sp.id,
        permissions=[iam.WorkspacePermission.ADMIN],
    )

    ws = WorkspaceClient(
        host=workspace_url,
        client_id=sp.application_id,
        auth_type="github-oidc",
        token_audience="https://github.com/databricks-eng",
    )

    ws.current_user.me()


def test_workspace_oauth_m2m_auth(w,env_or_skip):
    env_or_skip("CLOUD_ENV")

    # Get environment variables
    host = env_or_skip("DATABRICKS_HOST")
    client_id = env_or_skip("TEST_DATABRICKS_CLIENT_ID")
    client_secret = env_or_skip("TEST_DATABRICKS_CLIENT_SECRET")

    # Create workspace client with OAuth M2M authentication
    ws = WorkspaceClient(
        host=host,
        client_id=client_id,
        client_secret=client_secret,
        auth_type="oauth-m2m",
    )

    # Call the "me" API
    me = ws.current_user.me()

    # Verify we got a valid response
    assert me.user_name, "expected non-empty user_name"


def test_workspace_azure_client_secret_auth(w, env_or_skip):
    env_or_skip("CLOUD_ENV")

    host = env_or_skip("DATABRICKS_HOST")
    azure_client_id = env_or_skip("ARM_CLIENT_ID")
    azure_client_secret = env_or_skip("ARM_CLIENT_SECRET")
    azure_tenant_id = env_or_skip("ARM_TENANT_ID")

    # Create workspace client with Azure client secret authentication
    ws = WorkspaceClient(
        host=host,
        azure_client_id=azure_client_id,
        azure_client_secret=azure_client_secret,
        azure_tenant_id=azure_tenant_id,
        auth_type="azure-client-secret",
    )

    # Call the "me" API
    me = ws.current_user.me()

    # Verify we got a valid response
    assert me.user_name, "expected non-empty user_name"


def test_account_oauth_m2m_auth(a, env_or_skip):
    env_or_skip("CLOUD_ENV")

    # Get environment variables
    host = env_or_skip("DATABRICKS_HOST")
    account_id = env_or_skip("DATABRICKS_ACCOUNT_ID")
    client_id = env_or_skip("TEST_DATABRICKS_CLIENT_ID")
    client_secret = env_or_skip("TEST_DATABRICKS_CLIENT_SECRET")

    # Create account client with OAuth M2M authentication
    ac = AccountClient(
        host=host,
        account_id=account_id,
        client_id=client_id,
        client_secret=client_secret,
        auth_type="oauth-m2m",
    )

    # List service principals to verify authentication works
    sps = ac.service_principals.list()
    next(sps)


def test_account_azure_client_secret_auth(a, env_or_skip):
    env_or_skip("CLOUD_ENV")

    # Get environment variables
    host = env_or_skip("DATABRICKS_HOST")
    account_id = env_or_skip("DATABRICKS_ACCOUNT_ID")
    azure_client_id = env_or_skip("ARM_CLIENT_ID")
    azure_client_secret = env_or_skip("ARM_CLIENT_SECRET")
    azure_tenant_id = env_or_skip("ARM_TENANT_ID")

    # Create account client with Azure client secret authentication
    ac = AccountClient(
        host=host,
        account_id=account_id,
        azure_client_id=azure_client_id,
        azure_client_secret=azure_client_secret,
        azure_tenant_id=azure_tenant_id,
        auth_type="azure-client-secret",
    )

    # List service principals to verify authentication works
    sps = ac.service_principals.list()
    next(sps)
