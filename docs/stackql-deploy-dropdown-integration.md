# Integrating the `StackqlDeployDropdown` Component

The `StackqlDeployDropdown` component adds a "stackql-deploy Template" button to resource pages in Docusaurus provider microsites. It parses SQL examples from the rendered page and generates IQL templates with `exists`, `createorupdate`, `statecheck`, `exports`, and `delete` anchors.

This guide covers how to add the component to a new provider microsite.

## Prerequisites

- Docusaurus `>= 3.8.x` with `@docusaurus/preset-classic`
- React `>= 19.0.0`
- Resource pages must follow the URL pattern `/services/{service}/{resource}`
- SQL example sections must use standard heading IDs: `#select-examples`, `#insert-examples`, `#update-examples`, `#replace-examples`, `#delete-examples`, `#lifecycle-methods`

## Step 1 - Install dependencies

Add Material UI packages to the microsite `package.json`:

```bash
npm install @mui/material @mui/icons-material @emotion/react @emotion/styled
```

The full dependency set for reference:

```json
{
  "@docusaurus/core": "3.8.1",
  "@docusaurus/preset-classic": "3.8.1",
  "@emotion/react": "^11.14.0",
  "@emotion/styled": "^11.14.1",
  "@mui/icons-material": "^7.3.1",
  "@mui/material": "^7.3.1",
  "react": "^19.0.0",
  "react-dom": "^19.0.0"
}
```

## Step 2 - Copy component files

Create the component directory and copy both files from an existing microsite (e.g. `databricks_workspace`):

```
src/
  components/
    StackqlDeployDropdown/
      StackqlDeployDropdown.js
      StackqlDeployDropdown.module.css
```

The component is provider-agnostic -- it reads SQL examples from the rendered DOM at runtime, so no provider-specific configuration is needed.

## Step 3 - Swizzle `DocBreadcrumbs`

Create `src/theme/DocBreadcrumbs/index.js`:

```jsx
import React from 'react';
import DocBreadcrumbs from '@theme-original/DocBreadcrumbs';
import StackqlDeployDropdown from '@site/src/components/StackqlDeployDropdown/StackqlDeployDropdown';

export default function DocBreadcrumbsWrapper(props) {
  return (
    <div className="breadcrumbs-with-actions">
      <DocBreadcrumbs {...props} />
      <StackqlDeployDropdown />
    </div>
  );
}
```

This is a [Docusaurus theme wrapper](https://docusaurus.io/docs/swizzling#wrapping) -- it injects the dropdown next to the breadcrumb navigation without modifying Docusaurus internals.

## Step 4 - Add layout CSS

Append the following to `src/css/custom.css`:

```css
/*
* breadcrumbs with actions (stackql-deploy dropdown)
*/
.breadcrumbs-with-actions {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: nowrap;
}

.breadcrumbs-with-actions nav {
  flex: 1;
  min-width: 0;
}
```

No changes to `docusaurus.config.js` are required (the custom CSS file is already loaded by the preset).

## File summary

| File | Purpose |
|---|---|
| `src/components/StackqlDeployDropdown/StackqlDeployDropdown.js` | Component logic: DOM parsing, SQL extraction, IQL template generation |
| `src/components/StackqlDeployDropdown/StackqlDeployDropdown.module.css` | Responsive visibility (hidden on mobile) |
| `src/theme/DocBreadcrumbs/index.js` | Theme swizzle wrapper that renders the dropdown alongside breadcrumbs |
| `src/css/custom.css` | Flex layout for the breadcrumbs + dropdown row |

## How the template generation works

The component scans the page for SQL example headings and extracts code blocks:

1. **SELECT** (prefers "get" tab) -- parsed into fields, table, and WHERE clause
2. **INSERT** (prefers "create" tab) -- used as the `createorupdate` anchor body
3. **UPDATE / REPLACE** -- fallback for `createorupdate` if no INSERT exists
4. **DELETE** -- used as the `delete` anchor body (also checks Lifecycle Methods section)

From the parsed SELECT, the component generates:

- `/*+ exists */` -- a `COUNT(*)` query using only the original WHERE params
- `/*+ statecheck */` -- a `COUNT(*)` query where mutable fields become equality checks
- `/*+ exports */` -- a SELECT query returning only mutable fields

When an INSERT section is present, the statecheck and exports queries are filtered to only include fields that appear in the INSERT column list (after stripping the `data__` prefix). This avoids checking immutable properties like `created_at`, `created_by`, `updated_at`, etc.
