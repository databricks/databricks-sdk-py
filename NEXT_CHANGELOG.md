# NEXT CHANGELOG

## Release v0.69.0

### New Features and Improvements

* Add a new interface `upload_from` to `databricks.sdk.mixins.FilesExt` to support upload from a file in local filesystem.
* Improve `databricks.sdk.mixins.FilesExt` upload throughput by uploading data in parallel by default.
* Add a new interface `download_to` to `databricks.sdk.mixins.FilesExt` to support download to a file in local filesystem. This interface will also download the file in parallel by default. Parallel downloading is currently unavailable on Windows.
* Improve `databricks.sdk.mixins.FilesExt.upload` to support uploading when Presigned URL is not enabled for the Workspace by introducing a fallback to Single Part Upload.

### Bug Fixes

### Documentation

### Internal Changes

### API Changes

* Add `upload_from()`, `download_to()` method for `databricks.sdk.mixins.FilesExt`.
* Add `use_parallel`, `parallelism`, `part_size` field for `databricks.sdk.mixins.FilesExt.upload`.
* [Breaking] Change `files_api_client_download_max_total_recovers` to `files_ext_client_download_max_total_recovers` for `databricks.sdk.Config`
* [Breaking] Change `files_api_client_download_max_total_recovers_without_progressing` to `files_ext_client_download_max_total_recovers_without_progressing` for `databricks.sdk.Config`
* [Breaking] Change `multipart_upload_min_stream_size` to `files_ext_multipart_upload_min_stream_size` for `databricks.sdk.Config`
* [Breaking] Change `multipart_upload_batch_url_count` to `files_ext_multipart_upload_batch_url_count` for `databricks.sdk.Config`
* [Breaking] Change `multipart_upload_chunk_size` to `files_ext_multipart_upload_default_part_size` for `databricks.sdk.Config`
* [Breaking] Change `multipart_upload_url_expiration_duration` to `files_ext_multipart_upload_url_expiration_duration` for `databricks.sdk.Config`
* [Breaking] Change `multipart_upload_max_retries` to `files_ext_multipart_upload_max_retries` for `databricks.sdk.Config`
* Add `files_ext_client_download_streaming_chunk_size`, `files_ext_multipart_upload_part_size_options`, `files_ext_multipart_upload_max_part_size`, `files_ext_multipart_upload_default_parallelism`, `files_ext_presigned_download_url_expiration_duration`, `files_ext_parallel_download_default_parallelism`, `files_ext_parallel_download_min_file_size`, `files_ext_parallel_download_default_part_size`, `files_ext_parallel_download_max_retries` for `databricks.sdk.Config`
