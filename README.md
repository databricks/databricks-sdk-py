# Databricks SDK for Python

**Stability**: [Experimental](https://docs.databricks.com/release-notes/release-types.html)

The Databricks SDK for Python includes functionality to accelerate development with [Python](https://www.python.org/) for the Databricks Lakehouse. 
It covers all public [Databricks REST API](https://docs.databricks.com/dev-tools/api/index.html) operations. 
The SDK's internal HTTP client is robust and handles failures on different levels by performing intelligent retries.

## Contents

- [Getting started](#getting-started)
- [Authentication](#authentication)
- [Code examples](#code-examples)
- [Long running operations](#long-running-operations)
- [Paginated responses](#paginated-responses)
- [Logging](#logging)
- [Interface stability](#interface-stability)

## Getting started

1. Please install Databricks SDK for Python and instantiate `WorkspaceClient`:

```python
from databricks.sdk import WorkspaceClient
w = WorkspaceClient()
for c in w.clusters.list():
    print(c.cluster_name)
```

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

1. Credentials that hard-coded into configuration arguments.

   **Caution**: Databricks does not recommend hard-coding credentials into arguments, as they can be exposed in plain text in version control systems. Use environment variables or configuration profiles instead.

2. Credentials in Databricks-specific [environment variables](https://docs.databricks.com/dev-tools/auth.html#environment-variables).
3. For Databricks native authentication, credentials in the `.databrickscfg` file's `DEFAULT` [configuration profile](https://docs.databricks.com/dev-tools/auth.html#configuration-profiles) from its default file location (`~` for Linux or macOS, and `%USERPROFILE%` for Windows).
4. For Azure native authentication, the SDK searches for credentials through the Azure CLI as needed.

Depending on the Databricks authentication method, the SDK uses the following information. Presented are the `WorkspaceClient` and `AccountClient` arguments (which have corresponding `.databrickscfg` file fields), their descriptions, and any corresponding environment variables.

### Databricks native authentication

By default, the Databricks SDK for Python initially tries Databricks token authentication (`auth_type='pat'` argument). If the SDK is unsuccessful, it then tries Databricks basic (username/password) authentication (`auth_type="basic"` argument).

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

More than 20 methods across different Databricks APIs are long-running operations for managing things like clusters, 
command execution, jobs, libraries, Delta Live Tables pipelines, and Databricks SQL warehouses. For example, in 
the Clusters API, once you create a cluster, you receive a cluster ID, and the cluster is in the `PENDING` state while 
Databricks takes care of provisioning virtual machines from the cloud provider in the background. But the cluster is 
only usable in the `RUNNING` state. Another example is the API for running a job or repairing the run: right after 
the run starts, the run is in the `PENDING` state, though the job is considered to be finished only when it is in 
the `TERMINATED` or `SKIPPED` states. And of course you. would want to know the error message when the long-running 
operation times out or why things fail. And sometimes you want to configure a custom timeout other than 
the default of 20 minutes.

To hide all of the integration-specific complexity from the end user, Databricks SDK for Python provides 
a high-level API for _triggering_ the long-running operations and _waiting_ for the releated entities to reach the right 
state or return back the error message about the problem in case of failure. All long-running operations have 
the `wait: bool` optional keyword argument, which is enabled by default. These methods return information about 
the relevant entity once the operation is finished. It is possible to configure a custom timeout by optionally providing 
a number of minutes in `timeout` keyword argument.

In the following example, `CreateAndWait` returns `ClusterInfo` only once the cluster is in the `RUNNING` state, 
otherwise it will timeout in 10 minutes:

```python
import logging
from databricks.sdk import WorkspaceClient
w = WorkspaceClient()
info = w.clusters.create(cluster_name='Created cluster',
                         spark_version='12.0.x-scala2.12',
                         node_type_id='m5d.large',
                         autotermination_minutes=10,
                         num_workers=1,
                         timeout=10)
logging.info(f'Created: {info}')
```

## Paginated responses

On the platform side, some Databricks APIs have result pagination, and some of them do not. Some APIs follow 
the offset-plus-limit pagination, some start their offsets from 0 and some from 1, some use the cursor-based iteration, 
and others just return all results in a single response. The Databricks SDK for Python hides this intricate complexity 
under `Iterator[T]` abstraction, where multi-page results `yield` items. Python typing helps to auto-complete 
the individual item fields.

```python
import logging
from databricks.sdk import WorkspaceClient
w = WorkspaceClient()
for repo in w.repos.list():
   logging.info(f'Found repo: {repo.path}')
```

## Logging

Databricks SDK for Python integrates with the standard [Logging facility for Python](https://docs.python.org/3/library/logging.html). 
Integration will evolve in the future versions of Databricks SDK for Python.

## Interface stability

During the [Experimental](https://docs.databricks.com/release-notes/release-types.html) period, Databricks is actively working on stabilizing the Databricks SDK for Python's interfaces. API clients for all services are generated from specification files that are synchronized from the main platform. You are highly encouraged to pin the exact dependency version and read the [changelog](https://github.com/databricks/databricks-sdk-py/blob/main/CHANGELOG.md) where Databricks documents the changes. Databricks may have minor [documented](https://github.com/databricks/databricks-sdk-py/blob/main/CHANGELOG.md) backward-incompatible changes, such as renaming the methods or some type names to bring more consistency. 
