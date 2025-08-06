# NEXT CHANGELOG

## Release v0.62.0

### New Features and Improvements

### Bug Fixes

* Fix `Config.oauth_token()` to avoid re-creating a new `CredentialsProvider` at each call. This fix indirectly makes `oauth_token()` benefit from the internal caching mechanism of some providers. 

### Documentation

### Internal Changes

### API Changes
* Added `statement_id_signature` field for `databricks.sdk.service.dashboards.Result`.
* Added `effective_database_instance_name` and `effective_logical_database_name` fields for `databricks.sdk.service.database.SyncedDatabaseTable`.
* Added `table` field for `databricks.sdk.service.jobs.TriggerStateProto`.
* Added `email_notifications` field for `databricks.sdk.service.serving.CreatePtEndpointRequest`.
* Added `email_notifications` field for `databricks.sdk.service.serving.CreateServingEndpoint`.
* Added `email_notifications` field for `databricks.sdk.service.serving.ServingEndpointDetailed`.
* [Breaking] Changed `list()` method for [w.consumer_providers](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/marketplace/consumer_providers.html) workspace-level service . New request type is `databricks.sdk.service.marketplace.ListConsumerProvidersRequest` dataclass.
* [Breaking] Changed `create()` method for [a.private_access](https://databricks-sdk-py.readthedocs.io/en/latest/account/provisioning/private_access.html) account-level service with new required argument order.
* [Breaking] Changed `create()` method for [a.private_access](https://databricks-sdk-py.readthedocs.io/en/latest/account/provisioning/private_access.html) account-level service . New request type is `databricks.sdk.service.provisioning.CreatePrivateAccessSettingsRequest` dataclass.
* [Breaking] Changed `replace()` method for [a.private_access](https://databricks-sdk-py.readthedocs.io/en/latest/account/provisioning/private_access.html) account-level service . New request type is `databricks.sdk.service.provisioning.ReplacePrivateAccessSettingsRequest` dataclass.
* [Breaking] Removed `is_featured` field for `databricks.sdk.service.marketplace.ListProvidersRequest`.