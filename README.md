# Databricks SDK for Python (Beta)

[![PyPI - Downloads](https://img.shields.io/pypi/dw/databricks-sdk)](https://pypistats.org/packages/databricks-sdk)
[![PyPI - License](https://img.shields.io/pypi/l/databricks-sdk)](https://github.com/databricks/databricks-sdk-py/blob/main/LICENSE)
[![databricks-sdk](https://snyk.io/advisor/python/databricks-sdk/badge.svg)](https://snyk.io/advisor/python/databricks-sdk)
![PyPI](https://img.shields.io/pypi/v/databricks-sdk)
[![codecov](https://codecov.io/gh/databricks/databricks-sdk-py/branch/main/graph/badge.svg?token=GU63K7WDBE)](https://codecov.io/gh/databricks/databricks-sdk-py)

[Beta](https://docs.databricks.com/release-notes/release-types.html): This SDK is supported for production use cases, 
but we do expect future releases to have some interface changes; see [Interface stability](#interface-stability). 
We are keen to hear feedback from you on these SDKs. Please [file issues](https://github.com/databricks/databricks-sdk-py/issues), and we will address them. 
| See also the [SDK for Java](https://github.com/databricks/databricks-sdk-java) 
| See also the [SDK for Go](https://github.com/databricks/databricks-sdk-go) 
| See also the [Terraform Provider](https://github.com/databricks/terraform-provider-databricks)
| See also cloud-specific docs ([AWS](https://docs.databricks.com/dev-tools/sdk-python.html), 
   [Azure](https://learn.microsoft.com/en-us/azure/databricks/dev-tools/sdk-python), 
   [GCP](https://docs.gcp.databricks.com/dev-tools/sdk-python.html)) 
| See also the [API reference on readthedocs](https://databricks-sdk-py.readthedocs.io/en/latest/)

The Databricks SDK for Python includes functionality to accelerate development with [Python](https://www.python.org/) for the Databricks Lakehouse.
It covers all public [Databricks REST API](https://docs.databricks.com/dev-tools/api/index.html) operations.
The SDK's internal HTTP client is robust and handles failures on different levels by performing intelligent retries.

## Contents

- [Getting started](#getting-started)
- [Code examples](#code-examples)
- [Authentication](#authentication)
- [Code examples](#code-examples)
- [Long-running operations](#long-running-operations)
- [Paginated responses](#paginated-responses)
- [Single-sign-on with OAuth](#single-sign-on-sso-with-oauth)
- [Logging](#logging)
- [Integration with `dbutils`](#interaction-with-dbutils)
- [Interface stability](#interface-stability)

## Getting started

1. Please install Databricks SDK for Python via `pip install databricks-sdk` and instantiate `WorkspaceClient`:

```python
from databricks.sdk import WorkspaceClient
w = WorkspaceClient()
for c in w.clusters.list():
    print(c.cluster_name)
```

Databricks SDK for Python is compatible with Python 3.7 _(until [June 2023](https://devguide.python.org/versions/))_, 3.8, 3.9, 3.10, and 3.11.

## Code examples

Please checkout [custom credentials provider](https://github.com/databricks/databricks-sdk-py/tree/main/examples/custom_auth.py), 
[OAuth with Flask](https://github.com/databricks/databricks-sdk-py/tree/main/examples/flask_app_with_oauth.py), 
[Last job runs](https://github.com/databricks/databricks-sdk-py/tree/main/examples/last_job_runs.py), 
[Starting job and waiting](https://github.com/databricks/databricks-sdk-py/tree/main/examples/starting_job_and_waiting.py) examples. You can also dig deeper into different services, like
[alerts](https://github.com/databricks/databricks-sdk-py/tree/main/examples/alerts), 
[billable_usage](https://github.com/databricks/databricks-sdk-py/tree/main/examples/billable_usage), 
[catalogs](https://github.com/databricks/databricks-sdk-py/tree/main/examples/catalogs), 
[cluster_policies](https://github.com/databricks/databricks-sdk-py/tree/main/examples/cluster_policies), 
[clusters](https://github.com/databricks/databricks-sdk-py/tree/main/examples/clusters), 
[credentials](https://github.com/databricks/databricks-sdk-py/tree/main/examples/credentials), 
[current_user](https://github.com/databricks/databricks-sdk-py/tree/main/examples/current_user), 
[dashboards](https://github.com/databricks/databricks-sdk-py/tree/main/examples/dashboards), 
[data_sources](https://github.com/databricks/databricks-sdk-py/tree/main/examples/data_sources), 
[databricks](https://github.com/databricks/databricks-sdk-py/tree/main/examples/databricks), 
[encryption_keys](https://github.com/databricks/databricks-sdk-py/tree/main/examples/encryption_keys), 
[experiments](https://github.com/databricks/databricks-sdk-py/tree/main/examples/experiments), 
[external_locations](https://github.com/databricks/databricks-sdk-py/tree/main/examples/external_locations), 
[git_credentials](https://github.com/databricks/databricks-sdk-py/tree/main/examples/git_credentials), 
[global_init_scripts](https://github.com/databricks/databricks-sdk-py/tree/main/examples/global_init_scripts), 
[groups](https://github.com/databricks/databricks-sdk-py/tree/main/examples/groups), 
[instance_pools](https://github.com/databricks/databricks-sdk-py/tree/main/examples/instance_pools), 
[instance_profiles](https://github.com/databricks/databricks-sdk-py/tree/main/examples/instance_profiles), 
[ip_access_lists](https://github.com/databricks/databricks-sdk-py/tree/main/examples/ip_access_lists), 
[jobs](https://github.com/databricks/databricks-sdk-py/tree/main/examples/jobs), 
[libraries](https://github.com/databricks/databricks-sdk-py/tree/main/examples/libraries), 
[local_browser_oauth.py](https://github.com/databricks/databricks-sdk-py/tree/main/examples/local_browser_oauth.py), 
[log_delivery](https://github.com/databricks/databricks-sdk-py/tree/main/examples/log_delivery), 
[metastores](https://github.com/databricks/databricks-sdk-py/tree/main/examples/metastores), 
[model_registry](https://github.com/databricks/databricks-sdk-py/tree/main/examples/model_registry), 
[networks](https://github.com/databricks/databricks-sdk-py/tree/main/examples/networks), 
[permissions](https://github.com/databricks/databricks-sdk-py/tree/main/examples/permissions), 
[pipelines](https://github.com/databricks/databricks-sdk-py/tree/main/examples/pipelines), 
[private_access](https://github.com/databricks/databricks-sdk-py/tree/main/examples/private_access), 
[queries](https://github.com/databricks/databricks-sdk-py/tree/main/examples/queries), 
[recipients](https://github.com/databricks/databricks-sdk-py/tree/main/examples/recipients), 
[repos](https://github.com/databricks/databricks-sdk-py/tree/main/examples/repos), 
[schemas](https://github.com/databricks/databricks-sdk-py/tree/main/examples/schemas), 
[secrets](https://github.com/databricks/databricks-sdk-py/tree/main/examples/secrets), 
[service_principals](https://github.com/databricks/databricks-sdk-py/tree/main/examples/service_principals), 
[storage](https://github.com/databricks/databricks-sdk-py/tree/main/examples/storage), 
[storage_credentials](https://github.com/databricks/databricks-sdk-py/tree/main/examples/storage_credentials), 
[tokens](https://github.com/databricks/databricks-sdk-py/tree/main/examples/tokens), 
[users](https://github.com/databricks/databricks-sdk-py/tree/main/examples/users), 
[vpc_endpoints](https://github.com/databricks/databricks-sdk-py/tree/main/examples/vpc_endpoints), 
[warehouses](https://github.com/databricks/databricks-sdk-py/tree/main/examples/warehouses), 
[workspace](https://github.com/databricks/databricks-sdk-py/tree/main/examples/workspace), 
[workspace_assignment](https://github.com/databricks/databricks-sdk-py/tree/main/examples/workspace_assignment), 
[workspace_conf](https://github.com/databricks/databricks-sdk-py/tree/main/examples/workspace_conf), 
and [workspaces](https://github.com/databricks/databricks-sdk-py/tree/main/examples/workspaces).

## Authentication

If you use Databricks [configuration profiles](https://docs.databricks.com/dev-tools/auth.html#configuration-profiles)
or Databricks-specific [environment variables](https://docs.databricks.com/dev-tools/auth.html#environment-variables)
for [Databricks authentication](https://docs.databricks.com/dev-tools/auth.html), the only code required to start
working with a Databricks workspace is the following code snippet, which instructs the Databricks SDK for Python to use
its [default authentication flow](#default-authentication-flow):

```python
from databricks.sdk import WorkspaceClient
w = WorkspaceClient()
w. # press <TAB> for autocompletion
```

The conventional name for the variable that holds the workspace-level client of the Databricks SDK for Python is `w`, which is shorthand for `workspace`.

### In this section

- [Default authentication flow](#default-authentication-flow)
- [Databricks native authentication](#databricks-native-authentication)
- [Azure native authentication](#azure-native-authentication)
- [Overriding .databrickscfg](#overriding-databrickscfg)
- [Additional authentication configuration options](#additional-authentication-configuration-options)

### Default authentication flow

If you run the [Databricks Terraform Provider](https://registry.terraform.io/providers/databrickslabs/databricks/latest),
the [Databricks SDK for Go](https://github.com/databricks/databricks-sdk-go), the [Databricks CLI](https://docs.databricks.com/dev-tools/cli/index.html),
or applications that target the Databricks SDKs for other languages, most likely they will all interoperate nicely together.
By default, the Databricks SDK for Python tries the following [authentication](https://docs.databricks.com/dev-tools/auth.html) methods,
in the following order, until it succeeds:

1. [Databricks native authentication](#databricks-native-authentication)
2. [Azure native authentication](#azure-native-authentication)
4. If the SDK is unsuccessful at this point, it returns an authentication error and stops running.

You can instruct the Databricks SDK for Python to use a specific authentication method by setting the `auth_type` argument
as described in the following sections.

For each authentication method, the SDK searches for compatible authentication credentials in the following locations,
in the following order. Once the SDK finds a compatible set of credentials that it can use, it stops searching:

1. Credentials that are hard-coded into configuration arguments.

   :warning: **Caution**: Databricks does not recommend hard-coding credentials into arguments, as they can be exposed in plain text in version control systems. Use environment variables or configuration profiles instead.

2. Credentials in Databricks-specific [environment variables](https://docs.databricks.com/dev-tools/auth.html#environment-variables).
3. For Databricks native authentication, credentials in the `.databrickscfg` file's `DEFAULT` [configuration profile](https://docs.databricks.com/dev-tools/auth.html#configuration-profiles) from its default file location (`~` for Linux or macOS, and `%USERPROFILE%` for Windows).
4. For Azure native authentication, the SDK searches for credentials through the Azure CLI as needed.

Depending on the Databricks authentication method, the SDK uses the following information. Presented are the `WorkspaceClient` and `AccountClient` arguments (which have corresponding `.databrickscfg` file fields), their descriptions, and any corresponding environment variables.

### Databricks native authentication

By default, the Databricks SDK for Python initially tries [Databricks token authentication](https://docs.databricks.com/dev-tools/api/latest/authentication.html) (`auth_type='pat'` argument). If the SDK is unsuccessful, it then tries Databricks basic (username/password) authentication (`auth_type="basic"` argument).

- For Databricks token authentication, you must provide `host` and `token`; or their environment variable or `.databrickscfg` file field equivalents.
- For Databricks basic authentication, you must provide `host`, `username`, and `password` _(for AWS workspace-level operations)_; or `host`, `account_id`, `username`, and `password` _(for AWS, Azure, or GCP account-level operations)_; or their environment variable or `.databrickscfg` file field equivalents.

| Argument     | Description | Environment variable |
|--------------|-------------|-------------------|
| `host`       | _(String)_ The Databricks host URL for either the Databricks workspace endpoint or the Databricks accounts endpoint. | `DATABRICKS_HOST` |     
| `account_id` | _(String)_ The Databricks account ID for the Databricks accounts endpoint. Only has effect when `Host` is either `https://accounts.cloud.databricks.com/` _(AWS)_, `https://accounts.azuredatabricks.net/` _(Azure)_, or `https://accounts.gcp.databricks.com/` _(GCP)_. | `DATABRICKS_ACCOUNT_ID` |
| `token`      | _(String)_ The Databricks personal access token (PAT) _(AWS, Azure, and GCP)_ or Azure Active Directory (Azure AD) token _(Azure)_. | `DATABRICKS_TOKEN` |
| `username`   | _(String)_ The Databricks username part of basic authentication. Only possible when `Host` is `*.cloud.databricks.com` _(AWS)_. | `DATABRICKS_USERNAME` |
| `password`   | _(String)_ The Databricks password part of basic authentication. Only possible when `Host` is `*.cloud.databricks.com` _(AWS)_. | `DATABRICKS_PASSWORD` |

For example, to use Databricks token authentication:

```python
from databricks.sdk import WorkspaceClient
w = WorkspaceClient(host=input('Databricks Workspace URL: '), token=input('Token: '))
```

### Azure native authentication

By default, the Databricks SDK for Python first tries Azure client secret authentication (`auth_type='azure-client-secret'` argument). If the SDK is unsuccessful, it then tries Azure CLI authentication (`auth_type='azure-cli'` argument). See [Manage service principals](https://learn.microsoft.com/azure/databricks/administration-guide/users-groups/service-principals).

The Databricks SDK for Python picks up an Azure CLI token, if you've previously authenticated as an Azure user by running `az login` on your machine. See [Get Azure AD tokens for users by using the Azure CLI](https://learn.microsoft.com/azure/databricks/dev-tools/api/latest/aad/user-aad-token).

To authenticate as an Azure Active Directory (Azure AD) service principal, you must provide one of the following. See also [Add a service principal to your Azure Databricks account](https://learn.microsoft.com/azure/databricks/administration-guide/users-groups/service-principals#add-sp-account):

- `azure_resource_id`, `azure_client_secret`, `azure_client_id`, and `azure_tenant_id`; or their environment variable or `.databrickscfg` file field equivalents.
- `azure_resource_id` and `azure_use_msi`; or their environment variable or `.databrickscfg` file field equivalents.

| Argument              | Description | Environment variable |
|-----------------------|-------------|----------------------|
| `azure_resource_id`   | _(String)_ The Azure Resource Manager ID for the Azure Databricks workspace, which is exchanged for a Databricks host URL. | `DATABRICKS_AZURE_RESOURCE_ID` |
| `azure_use_msi`       | _(Boolean)_ `true` to use Azure Managed Service Identity passwordless authentication flow for service principals. _This feature is not yet implemented in the Databricks SDK for Python._ | `ARM_USE_MSI` |
| `azure_client_secret` | _(String)_ The Azure AD service principal's client secret. | `ARM_CLIENT_SECRET` |
| `azure_client_id`     | _(String)_ The Azure AD service principal's application ID. | `ARM_CLIENT_ID` |
| `azure_tenant_id`     | _(String)_ The Azure AD service principal's tenant ID. | `ARM_TENANT_ID` |
| `azure_environment`   | _(String)_ The Azure environment type (such as Public, UsGov, China, and Germany) for a specific set of API endpoints. Defaults to `PUBLIC`. | `ARM_ENVIRONMENT` |

For example, to use Azure client secret authentication:

```python
from databricks.sdk import WorkspaceClient
w = WorkspaceClient(host=input('Databricks Workspace URL: '),
                    azure_workspace_resource_id=input('Azure Resource ID: '),
                    azure_tenant_id=input('AAD Tenant ID: '),
                    azure_client_id=input('AAD Client ID: '),
                    azure_client_secret=input('AAD Client Secret: '))
```

Please see more examples in [this document](./docs/azure-ad.md).

### Overriding `.databrickscfg`

For [Databricks native authentication](#databricks-native-authentication), you can override the default behavior for using `.databrickscfg` as follows:

| Argument      | Description | Environment variable |
|---------------|-------------|----------------------|
| `profile`     | _(String)_ A connection profile specified within `.databrickscfg` to use instead of `DEFAULT`. | `DATABRICKS_CONFIG_PROFILE` |
| `config_file` | _(String)_ A non-default location of the Databricks CLI credentials file. | `DATABRICKS_CONFIG_FILE` |

For example, to use a profile named `MYPROFILE` instead of `DEFAULT`:

```python
from databricks.sdk import WorkspaceClient
w = WorkspaceClient(profile='MYPROFILE')
# Now call the Databricks workspace APIs as desired...
```

### Additional authentication configuration options

For all authentication methods, you can override the default behavior in client arguments as follows:

| Argument                | Description | Environment variable   |
|-------------------------|-------------|------------------------|
| `auth_type`             | _(String)_ When multiple auth attributes are available in the environment, use the auth type specified by this argument. This argument also holds the currently selected auth. | `DATABRICKS_AUTH_TYPE` |
| `http_timeout_seconds`  | _(Integer)_ Number of seconds for HTTP timeout. Default is _60_. | _(None)_               |
| `retry_timeout_seconds` | _(Integer)_ Number of seconds to keep retrying HTTP requests. Default is _300 (5 minutes)_. | _(None)_               |
| `debug_truncate_bytes`  | _(Integer)_ Truncate JSON fields in debug logs above this limit. Default is 96. | `DATABRICKS_DEBUG_TRUNCATE_BYTES` |
| `debug_headers`         | _(Boolean)_ `true` to debug HTTP headers of requests made by the application. Default is `false`, as headers contain sensitive data, such as access tokens. | `DATABRICKS_DEBUG_HEADERS` |
| `rate_limit`            | _(Integer)_ Maximum number of requests per second made to Databricks REST API. | `DATABRICKS_RATE_LIMIT` |

For example, to turn on debug HTTP headers:

```python
from databricks.sdk import WorkspaceClient
w = WorkspaceClient(debug_headers=True)
# Now call the Databricks workspace APIs as desired...
```

## Code examples

To find code examples that demonstrate how to call the Databricks SDK for Python, see the top-level [examples](/examples) folder within this repository

## Long-running operations

When you invoke a long-running operation, the SDK provides a high-level API to _trigger_ these operations and _wait_ for the related entities
to reach the correct state or return the error message in case of failure. All long-running operations return generic `Wait` instance with `result()`
method to get a result of long-running operation, once it's finished. Databricks SDK for Python picks the most reasonable default timeouts for
every method, but sometimes you may find yourself in a situation, where you'd want to provide `datetime.timedelta()` as the value of `timeout`
argument to `result()` method.

There are a number of long-running operations in Databricks APIs such as managing:
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
operation times out and fails with an error code. Other times you may want to configure a custom timeout other than
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

## Paginated responses

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

## Single-Sign-On (SSO) with OAuth

### Authorization Code flow with PKCE

For a regular web app running on a server, it's recommended to use the Authorization Code Flow to obtain an Access Token
and a Refresh Token. This method is considered safe because the Access Token is transmitted directly to the server
hosting the app, without passing through the user's web browser and risking exposure.

To enhance the security of the Authorization Code Flow, the PKCE (Proof Key for Code Exchange) mechanism can be
employed. With PKCE, the calling application generates a secret called the Code Verifier, which is verified by
the authorization server. The app also creates a transform value of the Code Verifier, called the Code Challenge,
and sends it over HTTPS to obtain an Authorization Code. By intercepting the Authorization Code, a malicious attacker
cannot exchange it for a token without possessing the Code Verifier.

The [presented sample](https://github.com/databricks/databricks-sdk-py/blob/main/examples/flask_app_with_oauth.py)
is a Python3 script that uses the Flask web framework along with Databricks SDK for Python to demonstrate how to
implement the OAuth Authorization Code flow with PKCE security. It can be used to build an app where each user uses
their identity to access Databricks resources. The script can be executed with or without client and secret credentials
for a custom OAuth app.

Databricks SDK for Python exposes the `oauth_client.initiate_consent()` helper to acquire user redirect URL and initiate
PKCE state verification. Application developers are expected to persist `RefreshableCredentials` in the webapp session
and restore it via `RefreshableCredentials.from_dict(oauth_client, session['creds'])` helpers.

Works for both AWS and Azure. Not supported for GCP at the moment.

```python
from databricks.sdk.oauth import OAuthClient

oauth_client = OAuthClient(host='<workspace-url>',
                           client_id='<oauth client ID>',
                           redirect_url=f'http://host.domain/callback',
                           scopes=['clusters'])

import secrets
from flask import Flask, render_template_string, request, redirect, url_for, session

APP_NAME = 'flask-demo'
app = Flask(APP_NAME)
app.secret_key = secrets.token_urlsafe(32)


@app.route('/callback')
def callback():
   from databricks.sdk.oauth import Consent
   consent = Consent.from_dict(oauth_client, session['consent'])
   session['creds'] = consent.exchange_callback_parameters(request.args).as_dict()
   return redirect(url_for('index'))


@app.route('/')
def index():
   if 'creds' not in session:
      consent = oauth_client.initiate_consent()
      session['consent'] = consent.as_dict()
      return redirect(consent.auth_url)

   from databricks.sdk import WorkspaceClient
   from databricks.sdk.oauth import SessionCredentials

   credentials_provider = SessionCredentials.from_dict(oauth_client, session['creds'])
   workspace_client = WorkspaceClient(host=oauth_client.host,
                                      product=APP_NAME,
                                      credentials_provider=credentials_provider)

   return render_template_string('...', w=workspace_client)
```

### SSO for local scripts on development machines

For applications, that do run on developer workstations, Databricks SDK for Python provides `auth_type='external-browser'`
utility, that opens up a browser for a user to go through SSO flow. Azure support is still in the early experimental
stage.

```python
from databricks.sdk import WorkspaceClient

host = input('Enter Databricks host: ')

w = WorkspaceClient(host=host, auth_type='external-browser')
clusters = w.clusters.list()

for cl in clusters:
    print(f' - {cl.cluster_name} is {cl.state}')
```

### Creating custom OAuth applications

In order to use OAuth with Databricks SDK for Python, you should use `account_client.custom_app_integration.create` API.

```python
import logging, getpass
from databricks.sdk import AccountClient
account_client = AccountClient(host='https://accounts.cloud.databricks.com',
                               account_id=input('Databricks Account ID: '),
                               username=input('Username: '),
                               password=getpass.getpass('Password: '))

logging.info('Enrolling all published apps...')
account_client.o_auth_enrollment.create(enable_all_published_apps=True)

status = account_client.o_auth_enrollment.get()
logging.info(f'Enrolled all published apps: {status}')

custom_app = account_client.custom_app_integration.create(
    name='awesome-app',
    redirect_urls=[f'https://host.domain/path/to/callback'],
    confidential=True)
logging.info(f'Created new custom app: '
             f'--client_id {custom_app.client_id} '
             f'--client_secret {custom_app.client_secret}')
```

## Logging

The Databricks SDK for Python seamlessly integrates with the standard [Logging facility for Python](https://docs.python.org/3/library/logging.html).
This allows developers to easily enable and customize logging for their Databricks Python projects.
To enable debug logging in your Databricks Python project, you can follow the example below:

```python
import logging, sys
logging.basicConfig(stream=sys.stderr,
                    level=logging.INFO,
                    format='%(asctime)s [%(name)s][%(levelname)s] %(message)s')
logging.getLogger('databricks.sdk').setLevel(logging.DEBUG)

from databricks.sdk import WorkspaceClient
w = WorkspaceClient(debug_truncate_bytes=1024, debug_headers=False)
for cluster in w.clusters.list():
    logging.info(f'Found cluster: {cluster.cluster_name}')
```

In the above code snippet, the logging module is imported and the `basicConfig()` method is used to set the logging level to `DEBUG`.
This will enable logging at the debug level and above. Developers can adjust the logging level as needed to control the verbosity of the logging output.
The SDK will log all requests and responses to standard error output, using the format `> ` for requests and `< ` for responses.
In some cases, requests or responses may be truncated due to size considerations. If this occurs, the log message will include
the text `... (XXX additional elements)` to indicate that the request or response has been truncated. To increase the truncation limits,
developers can set the `debug_truncate_bytes` configuration property or the `DATABRICKS_DEBUG_TRUNCATE_BYTES` environment variable.
To protect sensitive data, such as authentication tokens, passwords, or any HTTP headers, the SDK will automatically replace these
values with `**REDACTED**` in the log output. Developers can disable this redaction by setting the `debug_headers` configuration property to `True`.

```text
2023-03-22 21:19:21,702 [databricks.sdk][DEBUG] GET /api/2.0/clusters/list
< 200 OK
< {
<   "clusters": [
<     {
<       "autotermination_minutes": 60,
<       "cluster_id": "1109-115255-s1w13zjj",
<       "cluster_name": "DEFAULT Test Cluster",
<       ... truncated for brevity
<     },
<     "... (47 additional elements)"
<   ]
< }
```

Overall, the logging capabilities provided by the Databricks SDK for Python can be a powerful tool for monitoring and troubleshooting your
Databricks Python projects. Developers can use the various logging methods and configuration options provided by the SDK to customize
the logging output to their specific needs.

## Interaction with `dbutils`

You can use the client-side implementation of [`dbutils`](https://docs.databricks.com/dev-tools/databricks-utils.html) by accessing `dbutils` property on the `WorkspaceClient`.
Most of the `dbutils.fs` operations and `dbutils.secrets` are implemented natively in Python within Databricks SDK. Non-SDK implementations still require a Databricks cluster,
that you have to specify through the `cluster_id` configuration attribute or `DATABRICKS_CLUSTER_ID` environment variable. Don't worry if cluster is not running: internally,
Databricks SDK for Python calls `w.clusters.ensure_cluster_is_running()`.

```python
from databricks.sdk import WorkspaceClient

w = WorkspaceClient()
dbutils = w.dbutils

files_in_root = dbutils.fs.ls('/')
print(f'number of files in root: {len(files_in_root)}')
```

Alternatively, you can import `dbutils` from `databricks.sdk.runtime` module, but you have to make sure that all configuration is already [present in the environment variables](#default-authentication-flow):

```python
from databricks.sdk.runtime import dbutils

for secret_scope in dbutils.secrets.listScopes():
    for secret_metadata in dbutils.secrets.list(secret_scope.name):
        print(f'found {secret_metadata.key} secret in {secret_scope.name} scope')
```

## Interface stability

Databricks is actively working on stabilizing the Databricks SDK for Python's interfaces. 
API clients for all services are generated from specification files that are synchronized from the main platform. 
You are highly encouraged to pin the exact dependency version and read the [changelog](https://github.com/databricks/databricks-sdk-py/blob/main/CHANGELOG.md) 
where Databricks documents the changes. Databricks may have minor [documented](https://github.com/databricks/databricks-sdk-py/blob/main/CHANGELOG.md) 
backward-incompatible changes, such as renaming some type names to bring more consistency.
