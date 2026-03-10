# NEXT CHANGELOG

## Release v0.98.0

### New Features and Improvements

### Security

### Bug Fixes

### Documentation

### Internal Changes
* Replace the async-disabling mechanism on token refresh failure with a 1-minute retry backoff. Previously, a single failed async refresh would disable proactive token renewal until the token expired. Now, the SDK waits a short cooldown period and retries, improving resilience to transient errors.

### API Changes
