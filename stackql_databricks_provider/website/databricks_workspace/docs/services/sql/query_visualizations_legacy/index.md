---
title: query_visualizations_legacy
hide_title: false
hide_table_of_contents: false
keywords:
  - query_visualizations_legacy
  - sql
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

Creates, updates, deletes, gets or lists a <code>query_visualizations_legacy</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="query_visualizations_legacy" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.sql.query_visualizations_legacy" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


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
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Updates visualization in the query.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-options"><code>options</code></a>, <a href="#parameter-query_id"><code>query_id</code></a>, <a href="#parameter-type"><code>type</code></a></td>
    <td></td>
    <td>Creates visualization in the query.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Removes a visualization from the query.</td>
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
<tr id="parameter-deployment_name">
    <td><CopyableCode code="deployment_name" /></td>
    <td><code>string</code></td>
    <td>The Databricks Workspace Deployment Name (default: dbc-abcd0123-a1bc)</td>
</tr>
<tr id="parameter-id">
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td>Widget ID returned by :method:queryvisualizations/create</td>
</tr>
</tbody>
</table>

## `INSERT` examples

<Tabs
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' },
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="update">

Updates visualization in the query.

```sql
INSERT INTO databricks_workspace.sql.query_visualizations_legacy (
created_at,
description,
name,
options,
query,
type,
updated_at,
id,
deployment_name
)
SELECT 
'{{ created_at }}',
'{{ description }}',
'{{ name }}',
'{{ options }}',
'{{ query }}',
'{{ type }}',
'{{ updated_at }}',
'{{ id }}',
'{{ deployment_name }}'
RETURNING
id,
name,
created_at,
description,
options,
query,
type,
updated_at
;
```
</TabItem>
<TabItem value="create">

Creates visualization in the query.

```sql
INSERT INTO databricks_workspace.sql.query_visualizations_legacy (
options,
query_id,
type,
description,
name,
deployment_name
)
SELECT 
'{{ options }}' /* required */,
'{{ query_id }}' /* required */,
'{{ type }}' /* required */,
'{{ description }}',
'{{ name }}',
'{{ deployment_name }}'
RETURNING
id,
name,
created_at,
description,
options,
query,
type,
updated_at
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: query_visualizations_legacy
  props:
    - name: id
      value: "{{ id }}"
      description: Required parameter for the query_visualizations_legacy resource.
    - name: deployment_name
      value: "{{ deployment_name }}"
      description: Required parameter for the query_visualizations_legacy resource.
    - name: created_at
      value: "{{ created_at }}"
      description: |
        :param description: str (optional) A short description of this visualization. This is not displayed in the UI.
    - name: description
      value: "{{ description }}"
      description: |
        A short description of this visualization. This is not displayed in the UI.
    - name: name
      value: "{{ name }}"
      description: |
        The name of the visualization that appears on dashboards and the query screen.
    - name: options
      value: "{{ options }}"
      description: |
        The options object varies widely from one visualization type to the next and is unsupported. Databricks does not recommend modifying visualization settings in JSON.
    - name: query
      description: |
        :param type: str (optional) The type of visualization: chart, table, pivot table, and so on.
      value:
        can_edit: {{ can_edit }}
        created_at: "{{ created_at }}"
        data_source_id: "{{ data_source_id }}"
        description: "{{ description }}"
        id: "{{ id }}"
        is_archived: {{ is_archived }}
        is_draft: {{ is_draft }}
        is_favorite: {{ is_favorite }}
        is_safe: {{ is_safe }}
        last_modified_by:
          email: "{{ email }}"
          id: {{ id }}
          name: "{{ name }}"
        last_modified_by_id: {{ last_modified_by_id }}
        latest_query_data_id: "{{ latest_query_data_id }}"
        name: "{{ name }}"
        options:
          catalog: "{{ catalog }}"
          moved_to_trash_at: "{{ moved_to_trash_at }}"
          parameters:
            - enumOptions: "{{ enumOptions }}"
              multiValuesOptions:
                prefix: "{{ prefix }}"
                separator: "{{ separator }}"
                suffix: "{{ suffix }}"
              name: "{{ name }}"
              queryId: "{{ queryId }}"
              title: "{{ title }}"
              type: "{{ type }}"
              value: "{{ value }}"
          schema: "{{ schema }}"
        parent: "{{ parent }}"
        permission_tier: "{{ permission_tier }}"
        query: "{{ query }}"
        query_hash: "{{ query_hash }}"
        run_as_role: "{{ run_as_role }}"
        tags:
          - "{{ tags }}"
        updated_at: "{{ updated_at }}"
        user:
          email: "{{ email }}"
          id: {{ id }}
          name: "{{ name }}"
        user_id: {{ user_id }}
        visualizations:
          - created_at: "{{ created_at }}"
            description: "{{ description }}"
            id: "{{ id }}"
            name: "{{ name }}"
            options: "{{ options }}"
            query:
              can_edit: {{ can_edit }}
              created_at: "{{ created_at }}"
              data_source_id: "{{ data_source_id }}"
              description: "{{ description }}"
              id: "{{ id }}"
              is_archived: {{ is_archived }}
              is_draft: {{ is_draft }}
              is_favorite: {{ is_favorite }}
              is_safe: {{ is_safe }}
              last_modified_by:
                email: "{{ email }}"
                id: {{ id }}
                name: "{{ name }}"
              last_modified_by_id: {{ last_modified_by_id }}
              latest_query_data_id: "{{ latest_query_data_id }}"
              name: "{{ name }}"
              options:
                catalog: "{{ catalog }}"
                moved_to_trash_at: "{{ moved_to_trash_at }}"
                parameters:
                  - enumOptions: "{{ enumOptions }}"
                    multiValuesOptions:
                      prefix: "{{ prefix }}"
                      separator: "{{ separator }}"
                      suffix: "{{ suffix }}"
                    name: "{{ name }}"
                    queryId: "{{ queryId }}"
                    title: "{{ title }}"
                    type: "{{ type }}"
                    value: "{{ value }}"
                schema: "{{ schema }}"
              parent: "{{ parent }}"
              permission_tier: "{{ permission_tier }}"
              query: "{{ query }}"
              query_hash: "{{ query_hash }}"
              run_as_role: "{{ run_as_role }}"
              tags:
                - "{{ tags }}"
              updated_at: "{{ updated_at }}"
              user:
                email: "{{ email }}"
                id: {{ id }}
                name: "{{ name }}"
              user_id: {{ user_id }}
              visualizations:
                - created_at: "{{ created_at }}"
                  description: "{{ description }}"
                  id: "{{ id }}"
                  name: "{{ name }}"
                  options: "{{ options }}"
                  query:
                    can_edit: {{ can_edit }}
                    created_at: "{{ created_at }}"
                    data_source_id: "{{ data_source_id }}"
                    description: "{{ description }}"
                    id: "{{ id }}"
                    is_archived: {{ is_archived }}
                    is_draft: {{ is_draft }}
                    is_favorite: {{ is_favorite }}
                    is_safe: {{ is_safe }}
                    last_modified_by: "{{ last_modified_by }}"
                    last_modified_by_id: {{ last_modified_by_id }}
                    latest_query_data_id: "{{ latest_query_data_id }}"
                    name: "{{ name }}"
                    options: "{{ options }}"
                    parent: "{{ parent }}"
                    permission_tier: "{{ permission_tier }}"
                    query: "{{ query }}"
                    query_hash: "{{ query_hash }}"
                    run_as_role: "{{ run_as_role }}"
                    tags: "{{ tags }}"
                    updated_at: "{{ updated_at }}"
                    user: "{{ user }}"
                    user_id: {{ user_id }}
                    visualizations: "{{ visualizations }}"
                  type: "{{ type }}"
                  updated_at: "{{ updated_at }}"
            type: "{{ type }}"
            updated_at: "{{ updated_at }}"
    - name: type
      value: "{{ type }}"
      description: |
        The type of visualization: chart, table, pivot table, and so on.
    - name: updated_at
      value: "{{ updated_at }}"
      description: |
        :returns: :class:\`LegacyVisualization\`
    - name: query_id
      value: "{{ query_id }}"
      description: |
        The identifier returned by :method:queries/create
`}</CodeBlock>

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

Removes a visualization from the query.

```sql
DELETE FROM databricks_workspace.sql.query_visualizations_legacy
WHERE id = '{{ id }}' --required
AND deployment_name = '{{ deployment_name }}' --required
;
```
</TabItem>
</Tabs>
