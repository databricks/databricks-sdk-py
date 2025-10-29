# OpenAPI Specification Generation from Databricks SDK

This document describes how to generate OpenAPI specifications from the Databricks Python SDK source code and how to sync changes from the upstream repository.

## Overview

The Databricks Python SDK is generated from internal OpenAPI specifications that are not publicly available. This repository is a fork of the SDK that includes tools to reverse-engineer the SDK source code back into OpenAPI specifications.

Each service module in `databricks/sdk/service/` is converted into a standalone OpenAPI YAML specification that can be used with tools like StackQL, code generators, and API documentation tools.

## Architecture

The generation process consists of three main components:

### 1. SDK Parser (`tools/sdk_parser.py`)
Parses Python SDK service modules to extract:
- **Dataclasses**: Converted to OpenAPI schemas with all fields, types, and documentation
- **Enums**: Converted to OpenAPI string enums with all possible values
- **API Classes**: Methods are parsed to extract HTTP operations (GET, POST, PUT, PATCH, DELETE)
- **Documentation**: Extracted from docstrings and inline comments

### 2. OpenAPI Generator (`tools/openapi_generator.py`)
Generates OpenAPI 3.0 specifications with:
- **Standalone schemas**: Each service has all its schemas embedded (no shared `common.yaml`)
- **Server configurations**:
  - Account-level APIs: `https://accounts.cloud.databricks.com` with `{account_id}` variable
  - Workspace-level APIs: `https://{deployment_name}.cloud.databricks.com` with `{deployment_name}` variable
- **All properties optional**: To avoid polymorphism issues with cloud-specific fields (e.g., `aws_attributes`, `azure_attributes`, `gcp_attributes` are all included as optional properties)
- **Full documentation**: All descriptions from SDK docstrings are preserved
- **Authentication**: Bearer token (Personal Access Token) security scheme

### 3. Main Generator Script (`tools/generate_openapi_specs.py`)
Orchestrates the generation process:
- Discovers all service modules in `databricks/sdk/service/`
- Cleans the output directory (removes old specs)
- Generates OpenAPI YAML for each service
- Outputs specs to `openapi-specs/` directory

## Generating OpenAPI Specifications

### Prerequisites

- Python 3.8 or higher
- All dependencies from `requirements.txt` installed
- This repository cloned and set up

### Step 1: Clean Old Specifications (if any exist)

The generation script automatically cleans the output directory, but you can manually remove old specs:

```bash
rm -rf openapi-specs/*.yaml openapi-specs/*.yml
```

### Step 2: Run the Generator

From the repository root, run:

```bash
python tools/generate_openapi_specs.py
```

Or if you made it executable:

```bash
./tools/generate_openapi_specs.py
```

### Step 3: Review Generated Specifications

The OpenAPI specifications will be created in the `openapi-specs/` directory:

```bash
ls -lh openapi-specs/
```

Each service gets its own YAML file:
- `catalog.yaml` - Unity Catalog APIs
- `compute.yaml` - Cluster and compute APIs
- `jobs.yaml` - Jobs and workflows APIs
- `iam.yaml` - Identity and access management APIs
- `sql.yaml` - SQL warehouse and query APIs
- ... and many more

### Output Example

```
================================================================================
Databricks SDK to OpenAPI Specification Generator
================================================================================

Loading service modules...
✓ Loaded service module: agentbricks
✓ Loaded service module: apps
✓ Loaded service module: billing
✓ Loaded service module: catalog
...

✓ Loaded 30 service modules

================================================================================
Generating OpenAPI specifications...
================================================================================

[agentbricks]
  Parsing agentbricks...
    - Found 15 schemas
    - Found 1 API classes
    - Found 5 operations
  Generating OpenAPI spec...
  ✓ Saved to: /path/to/openapi-specs/agentbricks.yaml

[catalog]
  Parsing catalog...
    - Found 250 schemas
    - Found 20 API classes
    - Found 150 operations
  Generating OpenAPI spec...
  ✓ Saved to: /path/to/openapi-specs/catalog.yaml

...

================================================================================
Summary
================================================================================
✓ Successfully generated: 30 specs
Output directory: /path/to/openapi-specs
================================================================================
```

## Syncing Changes from Upstream

This fork is not intended to contribute back to the original Databricks SDK repository. However, you may want to pull updates from the upstream repository to get the latest API changes.

### Setting Up Upstream Remote

If you haven't already, add the upstream repository as a remote:

```bash
git remote add upstream https://github.com/databricks/databricks-sdk-py.git
```

Verify your remotes:

```bash
git remote -v
```

You should see:
```
origin      <your-fork-url> (fetch)
origin      <your-fork-url> (push)
upstream    https://github.com/databricks/databricks-sdk-py.git (fetch)
upstream    https://github.com/databricks/databricks-sdk-py.git (push)
```

### Fetching Upstream Changes

Fetch the latest changes from upstream:

```bash
git fetch upstream
```

### Merging Upstream Changes

#### Option 1: Merge into your current branch

If you want to merge upstream changes into your current branch:

```bash
# Make sure you're on your working branch
git checkout main  # or your branch name

# Merge upstream changes
git merge upstream/main
```

If there are conflicts, resolve them manually, then:

```bash
git add .
git commit -m "Merge upstream changes from databricks-sdk-py"
```

#### Option 2: Rebase onto upstream

If you prefer to rebase your changes on top of upstream:

```bash
git checkout main
git rebase upstream/main
```

Resolve any conflicts, then:

```bash
git rebase --continue
```

### After Syncing: Regenerate OpenAPI Specs

After pulling upstream changes, regenerate the OpenAPI specifications to capture any API updates:

```bash
python tools/generate_openapi_specs.py
```

Review the changes:

```bash
git status
git diff openapi-specs/
```

Commit the updated specifications:

```bash
git add openapi-specs/
git commit -m "Regenerate OpenAPI specs after syncing with upstream"
git push origin main
```

## Customization

### Modifying the Parser

If you need to extract additional information from the SDK, edit `tools/sdk_parser.py`:

- `_parse_dataclass()`: Customize how dataclasses are parsed
- `_parse_api_method()`: Customize how API methods are extracted
- `_extract_http_info_from_source()`: Improve HTTP method/path extraction

### Modifying the Generator

To change the OpenAPI output format, edit `tools/openapi_generator.py`:

- `_init_spec()`: Customize the base OpenAPI structure
- `_generate_object_schema()`: Change how schemas are generated
- `_generate_operation()`: Customize operation generation
- `_is_account_level_api()`: Adjust account vs workspace detection logic

### Filtering Services

To generate specs for only specific services, modify `generate_openapi_specs.py`:

```python
# Only generate for specific services
INCLUDED_SERVICES = ['catalog', 'compute', 'jobs']

for service_name, module in sorted(modules.items()):
    if service_name not in INCLUDED_SERVICES:
        continue
    # ... rest of generation logic
```

## Design Decisions

### All Properties Are Optional

Following your requirements, all schema properties are marked as optional in the generated specs. This avoids polymorphism issues where different cloud providers have different required fields:

Example:
```yaml
ClusterAttributes:
  type: object
  properties:
    aws_attributes:      # Optional - only for AWS
      $ref: '#/components/schemas/AwsAttributes'
    azure_attributes:    # Optional - only for Azure
      $ref: '#/components/schemas/AzureAttributes'
    gcp_attributes:      # Optional - only for GCP
      $ref: '#/components/schemas/GcpAttributes'
  # No 'required' array - everything is optional
```

### Standalone Specifications

Each service specification is completely standalone with no dependencies on other files. All referenced schemas are included in the same file under `components/schemas`.

This makes each spec independently usable without having to load multiple files.

### Server Variables

Specs include server URL templates with variables:

**Workspace APIs:**
```yaml
servers:
  - url: https://{deployment_name}.cloud.databricks.com
    variables:
      deployment_name:
        default: your-deployment
        description: Databricks workspace deployment name
```

**Account APIs:**
```yaml
servers:
  - url: https://accounts.cloud.databricks.com
    variables:
      account_id:
        default: your-account-id
        description: Databricks account ID
```

### No Polymorphism

Rather than using `oneOf`, `anyOf`, or `allOf` for cloud-specific variations, all possible properties are included in each schema as optional. This simplifies consumption by API clients and query tools.

## Troubleshooting

### Import Errors

If you get import errors when running the generator:

```bash
# Make sure you're in the repository root
cd /path/to/stackql-provider-databricks

# Install dependencies
pip install -r requirements.txt

# Run the generator
python tools/generate_openapi_specs.py
```

### Missing Service Modules

If some services aren't being generated:

1. Check that the service module exists: `ls databricks/sdk/service/`
2. Check the generator output for error messages
3. The service file might be named with an underscore prefix (internal) - these are intentionally skipped

### Invalid OpenAPI Specs

If the generated specs have validation errors:

1. Use an OpenAPI validator: `npx @apidevtools/swagger-cli validate openapi-specs/catalog.yaml`
2. Check for circular references in schemas
3. Review the parser logic for complex nested types
4. Open an issue with the specific validation error

### Upstream Merge Conflicts

If you get conflicts when merging upstream:

1. Most conflicts will be in `databricks/sdk/service/*.py` files
2. Generally, accept the upstream version (theirs) for SDK service files
3. Keep your version (yours) for the `tools/` directory and this README
4. After resolving, regenerate the OpenAPI specs

```bash
# Accept upstream for SDK files
git checkout --theirs databricks/sdk/service/*.py

# Keep your tooling
git checkout --ours tools/
git checkout --ours OPENAPI_GENERATION.md

# Mark as resolved
git add .
git commit
```

## Contributing

Since this is a fork specifically for OpenAPI generation and not intended for upstream contributions, all development should focus on:

1. Improving the SDK parsing logic
2. Enhancing OpenAPI spec generation
3. Adding better documentation extraction
4. Fixing bugs in the generation tools

Do not make changes to the `databricks/sdk/` directory directly - those should come from upstream syncs.

## License

This fork maintains the same license as the original Databricks SDK. See the LICENSE file for details.

The OpenAPI generation tools in `tools/` are additions to the fork and are provided as-is for reverse engineering purposes.
