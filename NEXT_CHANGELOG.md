# NEXT CHANGELOG

## Release v0.89.0

### New Features and Improvements
* Remove cloud type restrictions from Azure/GCP credential providers. Azure and GCP authentication now works with any Databricks host when credentials are properly configured,enabling authentication against cloud-agnostic endpoints such as aliased hosts.

### Security

### Bug Fixes

* Fixed recursive file lising in `WorkspaceClient.dbfs.list` on volumes. ([#1260](https://github.com/databricks/databricks-sdk-py/pull/1260))

### Documentation

### Internal Changes

### API Changes
