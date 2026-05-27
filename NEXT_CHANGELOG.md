# NEXT CHANGELOG

## Release v0.112.0

### New Features and Improvements

### Security

### Bug Fixes

### Documentation

### Breaking Changes

### Internal Changes

* Switch the formatter and linter from black/isort/autoflake to ruff (format + lint), aligning the SDK formatter with Databricks' internal Python formatting guidelines in preparation for moving the source of truth to a separate internal repository. `make fmt` now runs `ruff format` + `ruff check --fix-only`; `make lint` runs `ruff check` and `ruff format --check` across `databricks` and `tests`. No behavioral changes to the published SDK.

### API Changes
* Add `pipeline_task_parameters` field for `databricks.sdk.service.jobs.PipelineTask`.
* Add `pipeline_task` field for `databricks.sdk.service.jobs.ResolvedValues`.
* Add `parameters` field for `databricks.sdk.service.pipelines.CreatePipeline`.
* Add `parameters` field for `databricks.sdk.service.pipelines.EditPipeline`.
* Add `parameters` field for `databricks.sdk.service.pipelines.GetPipelineResponse`.