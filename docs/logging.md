# Logging

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