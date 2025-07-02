# NEXT CHANGELOG

## Release v0.58.0

### New Features and Improvements

### Bug Fixes

* Always create a new logger instance, rather than using Python's default global logger instance ([#988](https://github.com/databricks/databricks-sdk-py/pull/988)).

### Documentation

### Internal Changes

### API Changes
* Added `remote_disk_throughput` and `total_initial_remote_disk_size` fields for `databricks.sdk.service.compute.ClusterAttributes`.
* Added `remote_disk_throughput` and `total_initial_remote_disk_size` fields for `databricks.sdk.service.compute.ClusterDetails`.
* Added `remote_disk_throughput` and `total_initial_remote_disk_size` fields for `databricks.sdk.service.compute.ClusterSpec`.
* Added `remote_disk_throughput` and `total_initial_remote_disk_size` fields for `databricks.sdk.service.compute.CreateCluster`.
* Added `remote_disk_throughput` and `total_initial_remote_disk_size` fields for `databricks.sdk.service.compute.CreateInstancePool`.
* Added `remote_disk_throughput` and `total_initial_remote_disk_size` fields for `databricks.sdk.service.compute.EditCluster`.
* Added `remote_disk_throughput` and `total_initial_remote_disk_size` fields for `databricks.sdk.service.compute.EditInstancePool`.
* Added `remote_disk_throughput` and `total_initial_remote_disk_size` fields for `databricks.sdk.service.compute.GetInstancePool`.
* Added `remote_disk_throughput` and `total_initial_remote_disk_size` fields for `databricks.sdk.service.compute.InstancePoolAndStats`.
* Added `remote_disk_throughput` and `total_initial_remote_disk_size` fields for `databricks.sdk.service.compute.UpdateClusterResource`.
* Added `r` enum value for `databricks.sdk.service.compute.Language`.
* Added `continuous` and `continuous_restart` enum values for `databricks.sdk.service.jobs.TriggerType`.
