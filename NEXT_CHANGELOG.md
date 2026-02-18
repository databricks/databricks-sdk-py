# NEXT CHANGELOG

## Release v0.91.0

### New Features and Improvements

### Security

### Bug Fixes
* Make `useragent.with_extra()` idempotent to prevent User-Agent header growth in long-lived processes.

### Documentation

### Internal Changes

### API Changes
* Add `attributes` and `membership_roles` fields for `databricks.sdk.service.postgres.RoleRoleSpec`.
* Add `membership_roles` field for `databricks.sdk.service.postgres.RoleRoleStatus`.
* Add `general_access` enum value for `databricks.sdk.service.provisioning.EndpointUseCase`.
