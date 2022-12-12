# Databricks SDK for Python

```python
from databricks.sdk.client import ApiClient, Config
from databricks.sdk.service.clusters import ClustersAPI
client = ApiClient(Config(profile="demo"))
ClustersAPI(client).list()


from databricks.sdk import account_client
a = account_client()
ws = a.workspaces.create_and_wait(name='foo', credentials_id='bar')

```