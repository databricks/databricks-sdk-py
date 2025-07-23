# NEXT CHANGELOG

## Release v0.60.0

### New Features and Improvements

* Added headers to HttpRequestResponse in OpenAI client.

### Bug Fixes

- Correctly issue in OIDC implementation that prevented the use of the feature (see #994).
- Fix a reported issue where `FilesExt` fails to retry if it receives certain status code from server.

### Documentation

### Internal Changes

- Refactor unit tests for `FilesExt` to improve its readability.

### API Changes
* Added `databricks.sdk.service.agentbricks` package.
* Added `provisioning_phase` field for `databricks.sdk.service.database.SyncedTablePipelineProgress`.
* Added `redshift` and `sqldw` enum values for `databricks.sdk.service.pipelines.IngestionSourceType`.
* Added `germany_c5` enum value for `databricks.sdk.service.settings.ComplianceStandard`.
* Changed `asset_type` and `name` fields for `databricks.sdk.service.cleanrooms.CleanRoomAsset` to be required.
* [Breaking] Changed `asset_type` and `name` fields for `databricks.sdk.service.cleanrooms.CleanRoomAsset` to be required.
* [Breaking] Changed `local_name` field for `databricks.sdk.service.cleanrooms.CleanRoomAssetForeignTableLocalDetails` to be required.
* Changed `local_name` field for `databricks.sdk.service.cleanrooms.CleanRoomAssetForeignTableLocalDetails` to be required.
* Changed `notebook_content` field for `databricks.sdk.service.cleanrooms.CleanRoomAssetNotebook` to be required.
* [Breaking] Changed `notebook_content` field for `databricks.sdk.service.cleanrooms.CleanRoomAssetNotebook` to be required.
* Changed `local_name` field for `databricks.sdk.service.cleanrooms.CleanRoomAssetTableLocalDetails` to be required.
* [Breaking] Changed `local_name` field for `databricks.sdk.service.cleanrooms.CleanRoomAssetTableLocalDetails` to be required.
* [Breaking] Changed `local_name` field for `databricks.sdk.service.cleanrooms.CleanRoomAssetViewLocalDetails` to be required.
* Changed `local_name` field for `databricks.sdk.service.cleanrooms.CleanRoomAssetViewLocalDetails` to be required.
* [Breaking] Changed `local_name` field for `databricks.sdk.service.cleanrooms.CleanRoomAssetVolumeLocalDetails` to be required.
* Changed `local_name` field for `databricks.sdk.service.cleanrooms.CleanRoomAssetVolumeLocalDetails` to be required.
* [Breaking] Removed `databricks.sdk.service.aibuilder` package.
