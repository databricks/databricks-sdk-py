# NEXT CHANGELOG

## Release v0.89.0

### New Features and Improvements
* Remove cloud type restrictions from Azure/GCP credential providers. Azure and GCP authentication now works with any Databricks host when credentials are properly configured,enabling authentication against cloud-agnostic endpoints such as aliased hosts.

### Security

### Bug Fixes
* Fixes TypeError in _unknown_error() when API returns unparseable error on streaming request (#1264) 

### Documentation

### Internal Changes

### API Changes
