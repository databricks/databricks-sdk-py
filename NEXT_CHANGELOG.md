# NEXT CHANGELOG

## Release v0.87.0

### New Features and Improvements

### Security

### Bug Fixes

* Fixed Databricks M2M OAuth to correctly use Databricks OIDC endpoints instead of incorrectly using Azure endpoints when `ARM_CLIENT_ID` is set. Added new `databricks_oidc_endpoints` property that returns only Databricks OIDC endpoints, and updated all Databricks OAuth flows to use it. The old `oidc_endpoints` property is deprecated but maintained for backward compatibility. ([#TBD](https://github.com/databricks/databricks-sdk-py/pull/TBD)).

### Documentation

### Internal Changes

### API Changes
