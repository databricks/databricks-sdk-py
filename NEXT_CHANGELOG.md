# NEXT CHANGELOG

## Release v0.83.0

### New Features and Improvements

### Security

### Bug Fixes

### Documentation

### Internal Changes
* add capability to read the `product` field from the env variable.

### API Changes
* Add `generate_download_full_query_result()` and `get_download_full_query_result()` methods for [w.genie](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/dashboards/genie.html) workspace-level service.
* Add `active_instances` field for `databricks.sdk.service.apps.ComputeStatus`.
* [Breaking] Change `create_role()` method for [w.postgres](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/postgres/postgres.html) workspace-level service. HTTP method/verb has changed.