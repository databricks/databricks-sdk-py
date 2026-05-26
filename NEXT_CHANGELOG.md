# NEXT CHANGELOG

## Release v0.112.0

### New Features and Improvements

### Security

### Bug Fixes

### Documentation

### Breaking Changes

### Internal Changes

* Switch workspace addressing header on workspace-scoped API calls from `X-Databricks-Org-Id` to `X-Databricks-Workspace-Id`. The value continues to come from `Config.workspace_id` (`DATABRICKS_WORKSPACE_ID`), and now accepts either a classic numeric workspace ID or another workspace identifier format (server disambiguates).
* Switch the formatter and linter from black/isort/autoflake to ruff (format + lint), aligning the SDK formatter with Databricks' internal Python formatting guidelines in preparation for moving the source of truth to a separate internal repository. `make fmt` now runs `ruff format` + `ruff check --fix-only`; `make lint` runs `ruff check` and `ruff format --check` across `databricks` and `tests`. No behavioral changes to the published SDK.

### API Changes
