# NEXT CHANGELOG

## Release v0.104.0

### New Features and Improvements

### Security

### Bug Fixes

### Documentation

### Breaking Changes

### Internal Changes

* Expanded AI agent detection: added Goose, Amp, Augment, Copilot (VS Code), Kiro, Windsurf. Honors the `AGENT=<name>` standard (resolves to a known product if the value matches one, otherwise `unknown`). Presence-only env var matchers now treat an empty string as "set" for parity with the Go and Java SDKs.

### API Changes
