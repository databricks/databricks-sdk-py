# NEXT CHANGELOG

## Release v0.96.0

### New Features and Improvements

### Security

### Bug Fixes

### Documentation

### Internal Changes
* Move cloud-based credential filtering from individual strategies into `DefaultCredentials`. Azure strategies are skipped on GCP/AWS hosts in auto-detect mode; GCP strategies are skipped on Azure/AWS hosts. When `auth_type` is explicitly set (e.g. `azure-cli`), cloud filtering is bypassed so the named strategy is always attempted regardless of host cloud.

### API Changes
