# NEXT CHANGELOG

## Release v0.112.0

### New Features and Improvements

* Detect VS Code agent-initiated terminal commands via the `VSCODE_AGENT` environment variable (VS Code 1.121+). The User-Agent header now reports `agent/vscode-agent` when set. The previous `COPILOT_MODEL` heuristic (which reported `agent/copilot-vscode`) has been removed; it produced false positives for Copilot CLI BYOK users and never reliably identified VS Code.

### Security

### Bug Fixes

### Documentation

### Breaking Changes

### Internal Changes

### API Changes
