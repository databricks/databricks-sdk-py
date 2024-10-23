# Data Plane APIs

Some APIs such as Model Serving support direct Data Plane access for higher throughput and lower latency requests. 
To access Data Plane access, a dedicated short-lived OAuth token must be used. The SDK is able to generate and refresh 
such tokens transparently for the user.

## Prerequisites
Databricks SDK must be configured using a supported OAuth token. For more information, see
[Supported Databricks authentication types](https://docs.databricks.com/en/dev-tools/auth/index.html)

The desired service or endpoint must have direct Data Plane access enabled.

## Usage
Databricks SDK provides a separate service to be used for Data Plane access, which includes a `_data_plane` suffix.
This service contains the subset of the methods for the original service which are supported in the Data Plane.

Example:

```python
from databricks.sdk import WorkspaceClient
# Control Plane
w = WorkspaceClient()
w.serving_endpoints.query(...)
# Data Plane
w.serving_endpoints_data_plane.query(...)
```

