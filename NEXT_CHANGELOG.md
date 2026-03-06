# NEXT CHANGELOG

## Release v0.97.0

### New Features and Improvements

### Security

### Bug Fixes
* Fixed Databricks CLI authentication to detect when the cached token's scopes don't match the SDK's configured scopes. Previously, a scope mismatch was silently ignored, causing requests to use wrong permissions. The SDK now raises an error with instructions to re-authenticate.


### Documentation

### Internal Changes
* Move cloud-based credential filtering from individual strategies into `DefaultCredentials`. Azure strategies are skipped on GCP/AWS hosts in auto-detect mode; GCP strategies are skipped on Azure/AWS hosts. When `auth_type` is explicitly set (e.g. `azure-cli`), cloud filtering is bypassed so the named strategy is always attempted regardless of host cloud.

### API Changes
* Add `databricks.sdk.service.dataclassification` and `databricks.sdk.service.knowledgeassistants` packages.
* Add [w.data_classification](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/dataclassification/data_classification.html) workspace-level service.
* Add [w.knowledge_assistants](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/knowledgeassistants/knowledge_assistants.html) workspace-level service.