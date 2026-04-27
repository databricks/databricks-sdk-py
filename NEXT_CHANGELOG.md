# NEXT CHANGELOG

## Release v0.110.0

### New Features and Improvements

### Security

### Bug Fixes
* Fix incorrect use of Python's `any` builtin as a type annotation; replace with `typing.Any` in `_internal.py`, `config.py`, `dbutils.py`, `oauth.py`, and `runtime/dbutils_stub.py` to resolve spurious mypy `[attr-defined]` errors.

### Documentation

### Breaking Changes

### Internal Changes

### API Changes
