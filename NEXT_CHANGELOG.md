# NEXT CHANGELOG

## Release v0.115.0

### New Features and Improvements

* Honor the Vercel `AI_AGENT=<name>` env var as a secondary fallback for AI agent detection in the User-Agent header (after the agents.md `AGENT=<name>` standard). Unrecognized fallback values now pass through the User-Agent sanitized and length-capped at 64 chars instead of being coerced to `agent/unknown`, so versioned variants such as `claude-code_2-1-141_agent` surface as-is.

### Security

### Bug Fixes

### Documentation

### Breaking Changes

### Internal Changes

### API Changes
