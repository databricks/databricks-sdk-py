# Getting Started

## Installation

To install the Databricks SDK for Python, simply run:

```bash
pip install databricks-sdk
```

Databricks Runtime starting from version 13.1 includes a bundled version of the Python SDK. It is highly recommended to upgrade to the latest version which you can do by running the following in a notebook cell:

```
%pip install --upgrade databricks-sdk
```

followed by

```python
dbutils.library.restartPython()
```

## Authentication

There are two primary entry points to the Databricks SDK:
* `databricks.sdk.WorkspaceClient` for working with workspace-level APIs, and
* `databricks.sdk.AccountClient` for working with account-level APIs.

To work with APIs, client instances need to authenticate that could be done different ways (according to the [Unified Authentication](https://docs.databricks.com/en/dev-tools/auth/index.html#unified-auth) approach that is used by all Databricks SDKs and related tools):
* When `WorkspaceClient` is created in the notebook, and no authentication parameters provided, then it will automatically pull authentication information from the execution context. This implicit authentication doesn't work for AccountClient. Simply use the following code fragment:
```python
from databricks.sdk import WorkspaceClient
w = WorkspaceClient()
```
* When `WorkspaceClient` or `AccountClient` are created outside of the notebook, then they will read authentication information from environment variables and your `.databrickscfg` file. This method is recommended when writing command-line tools as it allows more flexible configuration of authentication.
* Authentication parameters may also be explicitly passed when creating `WorkspaceClient` or `AccountClient`. For example:
```python
from databricks.sdk import WorkspaceClient
w = WorkspaceClient(
    host='http://my-databricks-instance.com',
    username='my-user',
    password='my-password')
```

It's also possible to provide a custom authentication implementation if necessary. For more details, see [Authentication](authentication.md).

## Listing resources

One of the key advantages of the Databricks SDK is that it provides a consistent interface for working with APIs returning paginated responses. The pagination details are hidden from the caller. Instead, the SDK returns a generator that yields each item in the list. For example, to list all clusters in the workspace, you can use the following code:

```python
for cluster in w.clusters.list():
    print(f'cluster {cluster.cluster_name} has {cluster.num_workers} workers')
```

See [Pagination](pagination.md) for more details.

## Using Data Classes & Enums

The Databricks SDK for Python makes use of Python's data classes and enums to represent data for APIs - this makes code more readable and type-safe, and it allows easier work with code compared with untyped dicts.

Specific data classes are organized into separate packages under `databricks.sdk.service`. For example, `databricks.sdk.service.jobs` has defintions for data classes & enums related to the Jobs API.

For more information, consult the [Dataclasses API Reference](dbdataclasses/index.rst).

## Examples

The Databricks SDK for Python comes with a number of examples demonstrating how to use the library for various common use-cases, including

* [Using the SDK with OAuth from a webserver](https://github.com/databricks/databricks-sdk-py/blob/main/examples/flask_app_with_oauth.py)
* [Using long-running operations](https://github.com/databricks/databricks-sdk-py/blob/main/examples/starting_job_and_waiting.py)
* [Authenticating a client app using OAuth](https://github.com/databricks/databricks-sdk-py/blob/main/examples/local_browser_oauth.py)

These examples and more are located in the [`examples/` directory of the Github repository](https://github.com/databricks/databricks-sdk-py/tree/main/examples).

Some other examples of using the SDK include:
* [Unity Catalog Automated Migration](https://github.com/databricks/ucx) heavily relies on Python SDK for working with Databricks APIs.
* [ip-access-list-analyzer](https://github.com/alexott/databricks-playground/tree/main/ip-access-list-analyzer) checks & prunes invalid entries from IP Access Lists.
