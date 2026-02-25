---
title: provider_providers
hide_title: false
hide_table_of_contents: false
keywords:
  - provider_providers
  - marketplace
  - databricks_workspace
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage databricks_workspace resources using SQL
custom_edit_url: null
image: /img/stackql-databricks_workspace-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import SchemaTable from '@site/src/components/SchemaTable/SchemaTable';

Creates, updates, deletes, gets or lists a <code>provider_providers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="provider_providers" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.marketplace.provider_providers" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

<SchemaTable fields={[
  {
    "name": "provider",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "name",
        "type": "string",
        "description": ""
      },
      {
        "name": "business_contact_email",
        "type": "string",
        "description": ""
      },
      {
        "name": "term_of_service_link",
        "type": "string",
        "description": ""
      },
      {
        "name": "privacy_policy_link",
        "type": "string",
        "description": ""
      },
      {
        "name": "company_website_link",
        "type": "string",
        "description": ""
      },
      {
        "name": "dark_mode_icon_file_id",
        "type": "string",
        "description": ""
      },
      {
        "name": "dark_mode_icon_file_path",
        "type": "string",
        "description": ""
      },
      {
        "name": "description",
        "type": "string",
        "description": ""
      },
      {
        "name": "icon_file_id",
        "type": "string",
        "description": ""
      },
      {
        "name": "icon_file_path",
        "type": "string",
        "description": ""
      },
      {
        "name": "id",
        "type": "string",
        "description": ""
      },
      {
        "name": "is_featured",
        "type": "boolean",
        "description": "is_featured is accessible by consumers only"
      },
      {
        "name": "published_by",
        "type": "string",
        "description": "published_by is only applicable to data aggregators (e.g. Crux)"
      },
      {
        "name": "support_contact_email",
        "type": "string",
        "description": ""
      }
    ]
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "id",
    "type": "string",
    "description": ""
  },
  {
    "name": "name",
    "type": "string",
    "description": ""
  },
  {
    "name": "dark_mode_icon_file_id",
    "type": "string",
    "description": ""
  },
  {
    "name": "icon_file_id",
    "type": "string",
    "description": ""
  },
  {
    "name": "business_contact_email",
    "type": "string",
    "description": ""
  },
  {
    "name": "company_website_link",
    "type": "string",
    "description": ""
  },
  {
    "name": "dark_mode_icon_file_path",
    "type": "string",
    "description": ""
  },
  {
    "name": "description",
    "type": "string",
    "description": ""
  },
  {
    "name": "icon_file_path",
    "type": "string",
    "description": ""
  },
  {
    "name": "is_featured",
    "type": "boolean",
    "description": "is_featured is accessible by consumers only"
  },
  {
    "name": "privacy_policy_link",
    "type": "string",
    "description": ""
  },
  {
    "name": "published_by",
    "type": "string",
    "description": "published_by is only applicable to data aggregators (e.g. Crux)"
  },
  {
    "name": "support_contact_email",
    "type": "string",
    "description": ""
  },
  {
    "name": "term_of_service_link",
    "type": "string",
    "description": ""
  }
]} />
</TabItem>
</Tabs>

## Methods

The following methods are available for this resource:

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
    <th>Optional Params</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Get provider profile</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-workspace"><code>workspace</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>List provider profiles for account.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-workspace"><code>workspace</code></a>, <a href="#parameter-provider"><code>provider</code></a></td>
    <td></td>
    <td>Create a provider</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-workspace"><code>workspace</code></a>, <a href="#parameter-provider"><code>provider</code></a></td>
    <td></td>
    <td>Update provider profile</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Delete provider</td>
</tr>
</tbody>
</table>

## Parameters

Parameters can be passed in the `WHERE` clause of a query. Check the [Methods](#methods) section to see which parameters are required or optional for each operation.

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Datatype</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr id="parameter-id">
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td>str</td>
</tr>
<tr id="parameter-workspace">
    <td><CopyableCode code="workspace" /></td>
    <td><code>string</code></td>
    <td>Your Databricks workspace name (default: your-workspace)</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>integer</code></td>
    <td>:param page_token: str (optional)</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Get provider profile

```sql
SELECT
provider
FROM databricks_workspace.marketplace.provider_providers
WHERE id = '{{ id }}' -- required
AND workspace = '{{ workspace }}' -- required
;
```
</TabItem>
<TabItem value="list">

List provider profiles for account.

```sql
SELECT
id,
name,
dark_mode_icon_file_id,
icon_file_id,
business_contact_email,
company_website_link,
dark_mode_icon_file_path,
description,
icon_file_path,
is_featured,
privacy_policy_link,
published_by,
support_contact_email,
term_of_service_link
FROM databricks_workspace.marketplace.provider_providers
WHERE workspace = '{{ workspace }}' -- required
AND page_size = '{{ page_size }}'
AND page_token = '{{ page_token }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create"
    values={[
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create">

Create a provider

```sql
INSERT INTO databricks_workspace.marketplace.provider_providers (
provider,
workspace
)
SELECT 
'{{ provider }}' /* required */,
'{{ workspace }}'
RETURNING
id
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: provider_providers
  props:
    - name: workspace
      value: "{{ workspace }}"
      description: Required parameter for the provider_providers resource.
    - name: provider
      description: |
        :returns: :class:\`CreateProviderResponse\`
      value:
        name: "{{ name }}"
        business_contact_email: "{{ business_contact_email }}"
        term_of_service_link: "{{ term_of_service_link }}"
        privacy_policy_link: "{{ privacy_policy_link }}"
        company_website_link: "{{ company_website_link }}"
        dark_mode_icon_file_id: "{{ dark_mode_icon_file_id }}"
        dark_mode_icon_file_path: "{{ dark_mode_icon_file_path }}"
        description: "{{ description }}"
        icon_file_id: "{{ icon_file_id }}"
        icon_file_path: "{{ icon_file_path }}"
        id: "{{ id }}"
        is_featured: {{ is_featured }}
        published_by: "{{ published_by }}"
        support_contact_email: "{{ support_contact_email }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' }
    ]}
>
<TabItem value="update">

Update provider profile

```sql
REPLACE databricks_workspace.marketplace.provider_providers
SET 
provider = '{{ provider }}'
WHERE 
id = '{{ id }}' --required
AND workspace = '{{ workspace }}' --required
AND provider = '{{ provider }}' --required
RETURNING
provider;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete">

Delete provider

```sql
DELETE FROM databricks_workspace.marketplace.provider_providers
WHERE id = '{{ id }}' --required
AND workspace = '{{ workspace }}' --required
;
```
</TabItem>
</Tabs>
