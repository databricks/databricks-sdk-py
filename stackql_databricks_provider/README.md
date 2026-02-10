# StackQL Databricks Provider - OpenAPI Schema Generator

A library of modular, testable functions to parse the Databricks Python SDK and extract components for generating OpenAPI specifications.

## Features

- **Small, modular functions** - Each function has a single, well-defined responsibility
- **Comprehensive logging** - Detailed logging at INFO and DEBUG levels to track anomalies
- **Type-safe** - Full type hints throughout
- **Well-tested** - Unit tests for all core functionality
- **Incremental design** - Built to be extended without creating a monolith
- **Account/Workspace separation** - Specs are organized by scope based on the SDK's `AccountClient` and `WorkspaceClient` definitions

## Project Structure

```
stackql_databricks_provider/
├── __init__.py              # Public API (get_resources, get_operations, etc.)
├── extract.py               # Core extraction functions (routes, schemas, params)
├── registry.py              # Service registry (account vs workspace classification)
├── generate.py              # OpenAPI spec generation and CLI entry point
├── README.md                # This file
├── tests/
│   ├── __init__.py
│   ├── test_extract.py      # Tests for extraction functions
│   ├── test_registry.py     # Tests for service registry
│   └── test_generate.py     # Tests for spec generation
└── openapi_generated/       # Generated output (after running the generator)
    ├── account/             # Account-level service specs
    │   ├── billing.json
    │   ├── catalog.json
    │   ├── iam.json
    │   ├── iamv2.json
    │   ├── oauth2.json
    │   ├── provisioning.json
    │   ├── settings.json
    │   └── settingsv2.json
    └── workspace/           # Workspace-level service specs
        ├── agentbricks.json
        ├── apps.json
        ├── catalog.json
        ├── cleanrooms.json
        ├── compute.json
        ├── dashboards.json
        ├── database.json
        ├── dataquality.json
        ├── files.json
        ├── iam.json
        ├── iamv2.json
        ├── jobs.json
        ├── marketplace.json
        ├── ml.json
        ├── oauth2.json
        ├── pipelines.json
        ├── postgres.json
        ├── qualitymonitorv2.json
        ├── serving.json
        ├── settings.json
        ├── settingsv2.json
        ├── sharing.json
        ├── sql.json
        ├── tags.json
        ├── vectorsearch.json
        └── workspace.json
```

## Setup

Install the project and its dependencies from the repository root:

```bash
pip install -e ".[dev]"
```

## How to Run

### Generate all specs

```bash
python -m stackql_databricks_provider.generate
```

This produces OpenAPI 3.0 JSON files under `stackql_databricks_provider/openapi_generated/`, organized into `account/` and `workspace/` subdirectories.

### Generate a single service

```bash
python -m stackql_databricks_provider.generate -s compute
```

### Custom output directory

```bash
python -m stackql_databricks_provider.generate -o /path/to/output
```

### Verbose/debug logging

```bash
python -m stackql_databricks_provider.generate -v
```

## How to Test

Run the full test suite:

```bash
python -m pytest stackql_databricks_provider/tests/ -v
```

Run a specific test file:

```bash
python -m pytest stackql_databricks_provider/tests/test_extract.py -v
```

Run a specific test class or method:

```bash
python -m pytest stackql_databricks_provider/tests/test_extract.py::TestGetResources -v
python -m pytest stackql_databricks_provider/tests/test_extract.py::TestGetOperationDetails::test_get_operation_structure -v
```

## How to Update

When the upstream Databricks Python SDK is updated with new services or API changes:

1. **Pull the latest SDK changes** into this repository (update the `databricks/` directory).

2. **Check for new service modules** - If new files appear under `databricks/sdk/service/`, add the module name to `SERVICE_MODULES` in `registry.py`.

3. **Check for new Account-level APIs** - If new API classes are added to `AccountClient.__init__()` in `databricks/sdk/__init__.py`, add the class name to `ACCOUNT_API_CLASSES` in `registry.py`.

4. **Regenerate specs**:
   ```bash
   python -m stackql_databricks_provider.generate
   ```

5. **Run tests** to verify nothing broke:
   ```bash
   python -m pytest stackql_databricks_provider/tests/ -v
   ```

6. **Review the diff** in the generated files to understand what changed.

## Public API

The package exports these functions via `stackql_databricks_provider`:

### `get_resources(service_module) -> List[Tuple[str, str]]`

Extract API resource classes from a service module. Returns `(class_name, snake_case_name)` tuples.

```python
from databricks.sdk.service import compute
from stackql_databricks_provider import get_resources

resources = get_resources(compute)
# [('ClusterPoliciesAPI', 'cluster_policies'), ('ClustersAPI', 'clusters'), ...]
```

### `get_operations(service_module, class_name) -> List[str]`

Extract public method names from an API class.

```python
from stackql_databricks_provider import get_operations

ops = get_operations(compute, "ClustersAPI")
# ['create', 'delete', 'edit', 'get', 'list', ...]
```

### `get_operation_details(service_module, class_name, method_name, ...) -> Dict`

Extract a complete OpenAPI path object for a single API method, including HTTP method, path, parameters, request body, and responses.

```python
from stackql_databricks_provider import get_operation_details

details = get_operation_details(
    compute, "ClustersAPI", "get",
    service_name="compute", resource_snake_name="clusters"
)
# {"/api/2.0/clusters/get": {"get": {"operationId": "get", ...}}}
```

### `get_data_classes(service_module) -> List[Type]`

Extract all dataclass types from a service module.

### `get_schema_from_data_class(service_module, dc) -> Dict`

Generate an OpenAPI component schema from a dataclass, resolving string type annotations, nested dataclass references, enum references, and `List[...]` types.

## Architecture Notes

- **Extraction is done via source introspection** - The generator parses the Python source of each SDK method to find `self._api.do("METHOD", "/path", ...)` calls. This avoids needing to instantiate any API clients or make HTTP calls.

- **Account vs Workspace classification** - Uses a static mapping of API class names based on which classes are instantiated in `AccountClient.__init__()` vs `WorkspaceClient.__init__()`. Some service modules (e.g., `iam`, `catalog`, `settings`) contain both account and workspace APIs - these get split into separate spec files.

- **String annotation resolution** - The SDK uses `from __future__ import annotations`, which makes all type annotations strings at runtime. The generator resolves these back to actual types against the service module namespace for proper schema generation.

- **Skipped operations** - Methods that don't contain a `self._api.do()` call (e.g., `wait_*` polling helpers, `*_and_wait` convenience wrappers) are automatically skipped since they don't represent direct REST API endpoints.
