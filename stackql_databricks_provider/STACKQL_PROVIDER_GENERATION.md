# StackQL Databricks Provider Generation

This document describes the end-to-end workflow for generating, testing, and publishing the StackQL Databricks provider.

## Prerequisites

- Python 3.9+ with the Databricks SDK installed (`pip install -e ".[dev]"` from repo root)
- Node.js 18+ with npm
- npm dependencies installed (`cd stackql_databricks_provider && npm install`)

## Overview

The Databricks provider is split into two scopes:

| Scope | Provider ID | Base URL |
|-------|-------------|----------|
| **Account** | `databricks_account` | `https://accounts.cloud.databricks.com` |
| **Workspace** | `databricks_workspace` | `https://{deployment_name}.cloud.databricks.com` |

Each scope has its own set of OpenAPI specs, CSV mappings, and generated provider output.

## Workflow

From the repo root:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

### 1. Generate OpenAPI Specs

Extract OpenAPI 3.0 specs from the Databricks Python SDK:

```bash
python3 -m stackql_databricks_provider.generate
```

This produces JSON specs under `stackql_databricks_provider/openapi_generated/{account,workspace}/`.

To regenerate a single service:

```bash
python3 -m stackql_databricks_provider.generate -s compute
```

### 2. Generate CSV Operation Inventories

Generate CSV mapping files from the OpenAPI specs:

```bash
# Sync response_object with specs (run after regenerating specs)
python3 -m stackql_databricks_provider.inventory_gen --refresh-response-objects

# Populate objectKey for Iterator list endpoints  
python3 -m stackql_databricks_provider.inventory_gen --populate-object-keys

# Regenerate CSVs from scratch (preserves manual edits to other columns)
python3 -m stackql_databricks_provider.inventory_gen
```

This produces:
- Per-service CSVs under `stackql_databricks_provider/inventory/{account,workspace}/`
- Consolidated `all_services.csv` per scope

**Important:** The inventory generator preserves existing CSV mappings. Only new operations are appended. Any manual edits to `stackql_resource_name`, `stackql_method_name`, `stackql_verb`, or `stackql_object_key` are retained.

### 3. Review and Edit CSV Mappings

Edit the CSV files to customize resource/method mappings before generating the provider. Key columns:

| Column | Description |
|--------|-------------|
| `stackql_resource_name` | StackQL resource name (defaults to last tag) |
| `stackql_method_name` | StackQL method name (defaults to operationId) |
| `stackql_verb` | SQL verb: `select`, `insert`, `replace`, `update`, `delete`, `exec` |
| `stackql_object_key` | JSON path to response data array (e.g. `$.items`) |

after making any updates to the service scoped csv files (masters), run the following:

```bash
python3 -m stackql_databricks_provider.inventory_gen
```

### 4. Generate Provider

This step transforms the OpenAPI specs into a fully-functional StackQL provider using the CSV mappings. Run this **separately for each scope**:

#### Account scope

```bash
cd stackql_databricks_provider
npm run generate-provider -- \
  --provider-name databricks_account \
  --input-dir openapi_generated/account \
  --output-dir stackql-provider/src/databricks_account \
  --config-path inventory/account/all_services.csv \
  --servers '[{"url": "https://accounts.cloud.databricks.com"}]' \
  --provider-config '{"auth":{"type":"oauth2","client_id_env_var":"DATABRICKS_CLIENT_ID","client_secret_env_var":"DATABRICKS_CLIENT_SECRET","grant_type":"client_credentials","token_url":"https://accounts.cloud.databricks.com/oidc/accounts/{{ .__env__DATABRICKS_ACCOUNT_ID }}/v1/token","scopes":["all-apis"]}}' \
  --service-config '{"pagination":{"requestToken":{"key":"page_token","location":"query"},"responseToken":{"key":"next_page_token","location":"body"}}}' \
  --naive-req-body-translate \
  --overwrite
```

#### Workspace scope

```bash
npm run generate-provider -- \
  --provider-name databricks_workspace \
  --input-dir openapi_generated/workspace \
  --output-dir stackql-provider/src/databricks_workspace \
  --config-path inventory/workspace/all_services.csv \
  --servers '[{"url":"https://{deployment_name}.cloud.databricks.com","variables":{"deployment_name":{"description":"The Databricks Workspace Deployment Name","default":"dbc-abcd0123-a1bc"}}}]' \
  --provider-config '{"auth":{"type":"oauth2","client_id_env_var":"DATABRICKS_CLIENT_ID","client_secret_env_var":"DATABRICKS_CLIENT_SECRET","grant_type":"client_credentials","token_url":"https://accounts.cloud.databricks.com/oidc/accounts/{{ .__env__DATABRICKS_ACCOUNT_ID }}/v1/token","scopes":["all-apis"]}}' \
  --service-config '{"pagination":{"requestToken":{"key":"page_token","location":"query"},"responseToken":{"key":"next_page_token","location":"body"}}}' \
  --naive-req-body-translate \
  --overwrite
```

add any post generation response transforms:

```bash
python -m add_response_transforms
```

merge view definitions into the provider service specs (final post-gen step):

```bash
python -m merge_views
```

View definitions live in ``views/{account,workspace}/{service}/views.yaml`` and are injected into ``components.x-stackQL-resources`` of the matching service YAML.

**Parameters explained:**

- `--provider-name` - The StackQL provider identifier
- `--input-dir` - Directory containing the OpenAPI JSON specs (must be flat, no subdirectories)
- `--output-dir` - Output directory for the generated provider
- `--config-path` - Path to the consolidated CSV mapping file
- `--servers` - JSON array defining the base URL pattern for API requests
- `--provider-config` - Authentication configuration
- `--service-config` - Service level config added to `x-stackQL-config`
- `--naive-req-body-translate` - Adds naive translation to all methods with body params (omits `data__` disambiguation prefixes for top level body fields)
- `--overwrite` - Overwrite existing generated files

### 5. Test Provider

#### Test Meta Routes

Test all metadata routes (services, resources, methods) in the provider:

```bash
# start server
PROVIDER_REGISTRY_ROOT_DIR="$(pwd)/stackql-provider"
npm run start-server -- --registry $PROVIDER_REGISTRY_ROOT_DIR
```

**Account scope:**

```bash
# Test account provider
npm run test-meta-routes -- databricks_account --verbose
```

**Workspace scope:**

```bash
# Test workspace provider
npm run test-meta-routes -- databricks_workspace --verbose
```

Manage server:

```bash
npm run server-status

npm run stop-server
```

#### Run Test Queries

Run interactive queries against the provider using the StackQL shell:

```bash
PROVIDER_REGISTRY_ROOT_DIR="$(pwd)/stackql-provider"
REG_STR='{"url": "file://'${PROVIDER_REGISTRY_ROOT_DIR}'", "localDocRoot": "'${PROVIDER_REGISTRY_ROOT_DIR}'", "verifyConfig": {"nopVerify": true}}'
./stackql shell --registry="${REG_STR}"
```

Example queries:

```sql
-- List workspaces in an account
SELECT
  workspace_id,
  workspace_name,
  workspace_status,
  aws_region,
  compute_mode,
  deployment_name,
  datetime(creation_time/1000, 'unixepoch') as creation_date_time
FROM databricks_account.provisioning.workspaces
WHERE account_id = 'ebfcc5a9-9d49-4c93-b651-b3ee6cf1c9ce';

-- Query account users and roles
SELECT
  id as user_id,
  displayName as display_name,
  userName as user_name,
  active,
  IIF(JSON_EXTRACT(roles,'$[0].value') = 'account_admin', 'true', 'false') as is_account_admin
FROM databricks_account.iam.account_users
WHERE account_id = 'ebfcc5a9-9d49-4c93-b651-b3ee6cf1c9ce';

--List catalogs in a workspace
SELECT
  full_name,
  catalog_type,
  comment,
  datetime(created_at/1000, 'unixepoch') as created_at,
  created_by,
  datetime(updated_at/1000, 'unixepoch') as updated_at,
  updated_by,
  enable_predictive_optimization
FROM databricks_workspace.catalog.catalogs
WHERE deployment_name = 'dbc-36ff48e3-4a69';

SELECT * FROM
databricks_workspace.settings.vw_all_settings
WHERE deployment_name = 'dbc-36ff48e3-4a69';

SELECT *
FROM databricks_account.iam.vw_account_user_roles
WHERE account_id = 'ebfcc5a9-9d49-4c93-b651-b3ee6cf1c9ce';
```

```bash
# Download billable usage to CSV
./stackql exec \
  --registry="${REG_STR}" \
  -o text \
  --hideheaders \
  -f billable_usage.csv \
  "SELECT contents
  FROM databricks_account.billing.billable_usage
  WHERE start_month = '2025-12'
  AND end_month = '2026-01'
  AND account_id = 'ebfcc5a9-9d49-4c93-b651-b3ee6cf1c9ce'"
```

### 6. Publish the Provider

To publish the provider, push the generated `databricks_account` and/or `databricks_workspace` directories to `providers/src` in a feature branch of the [`stackql-provider-registry`](https://github.com/stackql/stackql-provider-registry). Follow the [registry release flow](https://github.com/stackql/stackql-provider-registry/blob/dev/docs/build-and-deployment.md).

Test against the dev registry:

```bash
export DEV_REG='{"url": "https://registry-dev.stackql.app/providers", "verifyConfig": {"nopVerify": true}}'
./stackql --registry="${DEV_REG}" shell
```

Pull the latest dev provider:

```sql
REGISTRY PULL databricks_workspace;
REGISTRY PULL databricks_account;
```

### 7. Generate Web Docs

```bash
# Account docs
npm run generate-docs -- \
  --provider-name databricks_account \
  --provider-dir ./stackql-provider/src/databricks_account/v00.00.00000 \
  --output-dir ./website/databricks_account \
  --provider-data-dir ./docgen/provider-data/databricks_account

# Workspace docs
npm run generate-docs -- \
  --provider-name databricks_workspace \
  --provider-dir ./stackql-provider/src/databricks_workspace/v00.00.00000 \
  --output-dir ./website/databricks_workspace \
  --provider-data-dir ./docgen/provider-data/databricks_workspace
```

```bash
python -m add_doc_examples --doc-dir website
```

### 8. Authentication

Both providers authenticate using OAuth2 with a Databricks service principal. Set the following environment variables:

```bash
export DATABRICKS_ACCOUNT_ID="your-account-id"
export DATABRICKS_CLIENT_ID="your-client-id"
export DATABRICKS_CLIENT_SECRET="your-client-secret"
```

These are the same variables used by Terraform, the Databricks SDKs, and the Databricks CLI.

## Quick Reference

```bash
# Full regeneration pipeline
python -m stackql_databricks_provider.generate          # Step 1: OpenAPI specs
python -m stackql_databricks_provider.inventory_gen      # Step 2: CSV inventories
# Step 3: Edit CSVs as needed
npm run generate-provider -- ...                         # Step 4: Generate provider (run for each scope)
python -m stackql_databricks_provider.add_response_transforms  # Step 4a: Response transforms
python -m stackql_databricks_provider.merge_views              # Step 4b: Merge view definitions (final)

# Testing
python -m pytest stackql_databricks_provider/tests/ -v   # Unit tests
npm run start-server -- --provider <name> --registry ...  # Start StackQL server
npm run test-meta-routes -- <provider-name> --verbose     # Meta route tests
npm run stop-server                                       # Stop server
```

## License

MIT

## Contributing

Contributions to the Databricks provider are welcome! Please feel free to submit a Pull Request.
