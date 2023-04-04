# Interaction with `dbutils`

You can use the client-side implementation of [`dbutils`](https://docs.databricks.com/dev-tools/databricks-utils.html) by accessing `dbutils` property on the `WorkspaceClient`.
Most of the `dbutils.fs` operations and `dbutils.secrets` are implemented natively in Python within Databricks SDK. Non-SDK implementations still require a Databricks cluster,
that you have to specify through `cluster_id` configuration attribute or `DATABRICKS_CLUSTER_ID` environment variable. Don't worry if cluster is not running: internally,
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