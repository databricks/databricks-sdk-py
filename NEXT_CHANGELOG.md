# NEXT CHANGELOG

## Release v0.72.0

### New Features and Improvements

### Bug Fixes
- Fix `FilesExt` can fail to upload and download data when Presigned URLs are not available in certain environments (e.g. Serverless GPU clusters).

- Fix `FilesExt.upload` and `FilesExt.upload_from` would fail when the source content is empty and `use_parallel=True`.

### Documentation

### Internal Changes

### API Changes
