# NEXT CHANGELOG

## Release v0.50.0

### New Features and Improvements
* Introduce support for Databricks Workload Identity Federation in GitHub workflows ([933](https://github.com/databricks/databricks-sdk-py/pull/933)).
  See README.md for instructions.
* [Breaking] Users running their workflows in GitHub Actions, which use Cloud native authentication and also have a `DATABRICKS_CLIENT_ID` and `DATABRICKS_HOST`
  environment variables set may see their authentication start failing due to the order in which the SDK tries different authentication methods.

### Bug Fixes

### Documentation

### Internal Changes

### API Changes
