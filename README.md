# Databricks SDK for Python

```python
from databricks.sdk.client import ApiClient, Config
from databricks.sdk.service.clusters import ClustersAPI
client = ApiClient(Config(profile="demo"))
ClustersAPI(client).list()
```