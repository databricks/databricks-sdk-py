# NEXT CHANGELOG

## Release v0.115.0

### New Features and Improvements

* Honor the Vercel `AI_AGENT=<name>` env var as a secondary fallback for AI agent detection in the User-Agent header (after the agents.md `AGENT=<name>` standard). Unrecognized fallback values now pass through the User-Agent sanitized and length-capped at 64 chars instead of being coerced to `agent/unknown`, so versioned variants such as `claude-code_2-1-141_agent` surface as-is.

### Security

### Bug Fixes

* Fall back to the remote runtime implementation when the legacy user namespace cannot be materialized. On Spark Connect runtimes (e.g. shared-access-mode clusters), importing `databricks.sdk.runtime` — which happens when constructing a `WorkspaceClient` on such a cluster — tried to build a legacy `SparkContext` and raised `CONTEXT_UNAVAILABLE_FOR_REMOTE_CLIENT` at import time. It now logs a warning and falls back to the Spark Connect-compatible remote implementation instead of crashing.

### Documentation

### Breaking Changes

### Internal Changes

### API Changes
