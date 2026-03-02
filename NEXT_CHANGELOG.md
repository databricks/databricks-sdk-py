# NEXT CHANGELOG

## Release v0.96.0

### New Features and Improvements

### Security

### Bug Fixes

### Documentation

### Internal Changes
* Implement dynamic auth token stale period based on initial token lifetime. Increased up to 20 mins for standard OAuth with proportionally shorter periods for short-lived tokens. Providing a stale_duration in the constructor of the Refreshable class will use that fixed value instead. To match the previous default, pass stale_duration=timedelta(minutes=5).

### API Changes
