# NEXT CHANGELOG

## Release v0.94.0

### New Features and Improvements
* Added `Config.discovery_url` config field (`DATABRICKS_DISCOVERY_URL` env var). When set, OIDC endpoints are fetched directly from this URL instead of the default host-type-based logic. Mirrors `discoveryUrl` in the Java SDK.

### Security

### Bug Fixes

### Documentation

### Internal Changes

### API Changes
* Add `effective_publishing_mode` field for `databricks.sdk.service.pipelines.GetPipelineResponse`.
* Add `dbr_autoscale` enum value for `databricks.sdk.service.compute.EventDetailsCause`.
* Change `output_catalog` field for `databricks.sdk.service.cleanrooms.CreateCleanRoomOutputCatalogResponse` to be required.
* [Breaking] Remove `internal_attributes` field for `databricks.sdk.service.sharing.Table`.
* [Breaking] Remove `internal_attributes` field for `databricks.sdk.service.sharing.Volume`.