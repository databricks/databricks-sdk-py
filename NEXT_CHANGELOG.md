# NEXT CHANGELOG

## Release v0.89.0

### New Features and Improvements
* Remove cloud type restrictions from Azure/GCP credential providers. Azure and GCP authentication now works with any Databricks host when credentials are properly configured,enabling authentication against cloud-agnostic endpoints such as aliased hosts.

### Security

### Bug Fixes

* Fix the bug where the SDK would fail to properly recursively traverse directories in the _VolumesPath.list function

### Documentation

### Internal Changes

### API Changes
