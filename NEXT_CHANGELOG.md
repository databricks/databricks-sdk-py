# NEXT CHANGELOG

## Release v0.81.0

### New Features and Improvements

### Security

### Bug Fixes

### Documentation

### Internal Changes

### API Changes
* Add `postgres_role` field for `databricks.sdk.service.postgres.RoleRoleSpec`.
* Add `postgres_role` field for `databricks.sdk.service.postgres.RoleRoleStatus`.
* Add `purge` field for `databricks.sdk.service.sql.TrashAlertV2Request`.
* [Breaking] Change `create_role()` method for [w.postgres](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/postgres/postgres.html) workspace-level service with new required argument order.
* Change `role_id` field for `databricks.sdk.service.postgres.CreateRoleRequest` to no longer be required.