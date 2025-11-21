# Authentication Types Reference

This document provides a comprehensive reference for all authentication types (`auth_type`) supported by the Databricks SDK for Python.

## Authentication Types Table

| Auth Type | Description | Required Parameters | Optional Parameters | Environment Variables |
|-----------|-------------|---------------------|---------------------|----------------------|
| `pat` | Personal Access Token authentication - the most common method for programmatic access | `host`, `token` | - | `DATABRICKS_HOST`, `DATABRICKS_TOKEN` |
| `basic` | Basic HTTP authentication using username and password (primarily for AWS) | `host`, `username`, `password` | `account_id` (for account-level operations) | `DATABRICKS_HOST`, `DATABRICKS_USERNAME`, `DATABRICKS_PASSWORD`, `DATABRICKS_ACCOUNT_ID` |
| `oauth-m2m` | OAuth 2.0 Machine-to-Machine (service principal) authentication | `host`, `client_id`, `client_secret` | `scopes`, `authorization_details` | `DATABRICKS_HOST`, `DATABRICKS_CLIENT_ID`, `DATABRICKS_CLIENT_SECRET` |
| `external-browser` | OAuth 2.0 authentication flow using local browser for user login | `host`, `auth_type='external-browser'` | `client_id`, `client_secret` | `DATABRICKS_HOST`, `DATABRICKS_AUTH_TYPE`, `DATABRICKS_CLIENT_ID` |
| `databricks-cli` | Uses tokens from the Databricks CLI (`databricks auth login`) | `host` | `account_id` (for account-level), `databricks_cli_path` | `DATABRICKS_HOST`, `DATABRICKS_ACCOUNT_ID`, `DATABRICKS_CLI_PATH` |
| `azure-client-secret` | Azure Active Directory (AAD) Service Principal authentication | `azure_client_id`, `azure_client_secret`, `azure_tenant_id` | `host`, `azure_workspace_resource_id`, `azure_environment` | `ARM_CLIENT_ID`, `ARM_CLIENT_SECRET`, `ARM_TENANT_ID`, `DATABRICKS_HOST`, `DATABRICKS_AZURE_RESOURCE_ID`, `ARM_ENVIRONMENT` |
| `azure-cli` | Uses credentials from Azure CLI (`az login`) | `host` (or `azure_workspace_resource_id`) | `azure_tenant_id` | `DATABRICKS_HOST`, `DATABRICKS_AZURE_RESOURCE_ID`, `ARM_TENANT_ID` |
| `github-oidc` | GitHub Actions OIDC authentication (workload identity federation) | `host`, `client_id` | `token_audience`, `account_id` | `DATABRICKS_HOST`, `DATABRICKS_CLIENT_ID`, `DATABRICKS_TOKEN_AUDIENCE`, `DATABRICKS_ACCOUNT_ID` |
| `github-oidc-azure` | GitHub Actions OIDC for Azure Databricks workspaces | `host`, `azure_client_id` | `azure_tenant_id` | `DATABRICKS_HOST`, `ARM_CLIENT_ID`, `ARM_TENANT_ID` |
| `azure-devops-oidc` | Azure DevOps Pipelines OIDC authentication | `host`, `client_id` | `token_audience`, `account_id` | `DATABRICKS_HOST`, `DATABRICKS_CLIENT_ID`, `SYSTEM_ACCESSTOKEN` |
| `google-credentials` | Google Cloud service account authentication using credentials JSON | `host`, `google_credentials` | - | `DATABRICKS_HOST`, `GOOGLE_CREDENTIALS` |
| `google-id` | Google Cloud authentication using service account impersonation | `host`, `google_service_account` | - | `DATABRICKS_HOST`, `DATABRICKS_GOOGLE_SERVICE_ACCOUNT` |
| `metadata-service` | Authentication using Databricks-hosted metadata service | `host`, `metadata_service_url` | - | `DATABRICKS_HOST`, `DATABRICKS_METADATA_SERVICE_URL` |
| `runtime` | Auto-detected authentication when running in Databricks Runtime (notebooks, jobs) | _(auto-detected)_ | - | `DATABRICKS_RUNTIME_VERSION` (auto-set) |
| `runtime-oauth` | OAuth authentication for Databricks Runtime with fine-grained permissions | `scopes` | `authorization_details` | `DATABRICKS_RUNTIME_VERSION` (auto-set) |
| `model-serving` | Auto-detected authentication when running in Databricks Model Serving environment | _(auto-detected)_ | - | `IS_IN_DB_MODEL_SERVING_ENV` or `IS_IN_DATABRICKS_MODEL_SERVING_ENV` (auto-set) |
| `env-oidc` | OIDC token from environment variable | `host` | `oidc_token_env`, `client_id` | `DATABRICKS_HOST`, `DATABRICKS_OIDC_TOKEN`, `DATABRICKS_OIDC_TOKEN_ENV`, `DATABRICKS_CLIENT_ID` |
| `file-oidc` | OIDC token from file path | `host`, `oidc_token_filepath` | `client_id` | `DATABRICKS_HOST`, `DATABRICKS_OIDC_TOKEN_FILE`, `DATABRICKS_CLIENT_ID` |

## Common Parameters Across All Auth Types

These parameters can be used with any authentication type:

| Parameter | Description | Environment Variable |
|-----------|-------------|---------------------|
| `http_timeout_seconds` | HTTP request timeout (default: 60 seconds) | - |
| `retry_timeout_seconds` | Total retry timeout (default: 300 seconds / 5 minutes) | - |
| `debug_truncate_bytes` | Truncate debug logs above this size (default: 96 bytes) | `DATABRICKS_DEBUG_TRUNCATE_BYTES` |
| `debug_headers` | Enable debug logging of HTTP headers (default: false) | `DATABRICKS_DEBUG_HEADERS` |
| `rate_limit` | Maximum requests per second to Databricks API | `DATABRICKS_RATE_LIMIT` |
| `skip_verify` | Skip SSL certificate verification (not recommended) | - |

## Usage Examples

### Personal Access Token (PAT)
```python
from databricks.sdk import WorkspaceClient

w = WorkspaceClient(
    host="https://your-workspace.cloud.databricks.com",
    token="dapi1234567890abcdef"
)
```

### OAuth Machine-to-Machine (Service Principal)
```python
from databricks.sdk import WorkspaceClient

w = WorkspaceClient(
    host="https://your-workspace.cloud.databricks.com",
    client_id="your-client-id",
    client_secret="your-client-secret"
)
```

### External Browser (OAuth for Users)
```python
from databricks.sdk import WorkspaceClient

w = WorkspaceClient(
    host="https://your-workspace.cloud.databricks.com",
    auth_type="external-browser"
)
```

### Azure Service Principal
```python
from databricks.sdk import WorkspaceClient

w = WorkspaceClient(
    host="https://adb-1234567890.azuredatabricks.net",
    azure_client_id="your-azure-client-id",
    azure_client_secret="your-azure-client-secret",
    azure_tenant_id="your-azure-tenant-id"
)
```

### Databricks CLI
```python
from databricks.sdk import WorkspaceClient

# Assumes you've run: databricks auth login --host https://your-workspace.cloud.databricks.com
w = WorkspaceClient(
    host="https://your-workspace.cloud.databricks.com"
)
```

### GitHub Actions OIDC
```python
from databricks.sdk import WorkspaceClient

# In GitHub Actions with OIDC configured
w = WorkspaceClient(
    host="https://your-workspace.cloud.databricks.com",
    client_id="your-databricks-oauth-client-id"
)
```

### Google Cloud Credentials
```python
from databricks.sdk import WorkspaceClient

w = WorkspaceClient(
    host="https://your-workspace.gcp.databricks.com",
    google_credentials="/path/to/service-account-key.json"
)
```

### Runtime (in Databricks Notebooks)
```python
from databricks.sdk import WorkspaceClient

# No credentials needed when running in Databricks Runtime
w = WorkspaceClient()
```

## Authentication Priority Order

When no `auth_type` is explicitly specified, the SDK attempts authentication methods in this order:

1. `pat` - Personal Access Token
2. `basic` - Username/Password
3. `metadata-service` - Metadata Service (if URL provided)
4. `oauth-m2m` - OAuth Service Principal
5. `env-oidc` - Environment OIDC token
6. `file-oidc` - File-based OIDC token
7. `github-oidc` - GitHub OIDC
8. `azure-client-secret` - Azure Service Principal
9. `github-oidc-azure` - GitHub OIDC for Azure
10. `azure-cli` - Azure CLI
11. `azure-devops-oidc` - Azure DevOps OIDC
12. `external-browser` - Browser-based OAuth
13. `databricks-cli` - Databricks CLI
14. `runtime-oauth` - Databricks Runtime OAuth
15. `runtime` - Databricks Runtime native
16. `google-credentials` - Google Cloud credentials
17. `google-id` - Google Cloud ID
18. `model-serving` - Model Serving environment

You can override this order by explicitly setting the `auth_type` parameter.

## Notes

- **Auto-detected auth types** (`runtime`, `runtime-oauth`, `model-serving`): These are automatically detected based on environment variables and don't require explicit configuration.
- **Azure authentication**: When using Azure-specific auth types, if `host` is not provided but `azure_workspace_resource_id` is, the SDK will automatically resolve the workspace URL.
- **OIDC authentication**: OIDC-based methods (`github-oidc`, `azure-devops-oidc`, `env-oidc`, `file-oidc`) use token exchange to obtain Databricks tokens from external identity providers.
- **Scopes**: OAuth-based methods support the `scopes` parameter for fine-grained access control (e.g., `scopes="clusters sql"`).

## See Also

- [Main README Authentication Section](../README.md#authentication)
- [OAuth Documentation](./oauth.md)
- [Azure AD Authentication](./azure-ad.md)
- [Databricks Authentication Documentation](https://docs.databricks.com/dev-tools/auth.html)
