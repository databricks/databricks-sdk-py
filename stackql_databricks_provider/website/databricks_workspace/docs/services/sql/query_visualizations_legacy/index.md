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
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Updates visualization in the query.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-workspace"><code>workspace</code></a>, <a href="#parameter-options"><code>options</code></a>, <a href="#parameter-query_id"><code>query_id</code></a>, <a href="#parameter-type"><code>type</code></a></td>
    <td></td>
    <td>Creates visualization in the query.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
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
<tr id="parameter-id">
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td>Widget ID returned by :method:queryvisualizations/create</td>
</tr>
<tr id="parameter-workspace">
    <td><CopyableCode code="workspace" /></td>
    <td><code>string</code></td>
    <td>Your Databricks workspace name (default: your-workspace)</td>
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
workspace
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
'{{ workspace }}'
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
workspace
)
SELECT 
'{{ options }}' /* required */,
'{{ query_id }}' /* required */,
'{{ type }}' /* required */,
'{{ description }}',
'{{ name }}',
'{{ workspace }}'
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

```yaml
# Description fields are for documentation purposes
- name: query_visualizations_legacy
  props:
    - name: id
      value: string
      description: Required parameter for the query_visualizations_legacy resource.
    - name: workspace
      value: string
      description: Required parameter for the query_visualizations_legacy resource.
    - name: created_at
      value: string
      description: |
        :param description: str (optional) A short description of this visualization. This is not displayed in the UI.
    - name: description
      value: string
      description: |
        A short description of this visualization. This is not displayed in the UI.
    - name: name
      value: string
      description: |
        The name of the visualization that appears on dashboards and the query screen.
    - name: options
      value: object
      description: |
        The options object varies widely from one visualization type to the next and is unsupported. Databricks does not recommend modifying visualization settings in JSON.
    - name: query
      value: object
      description: |
        :param type: str (optional) The type of visualization: chart, table, pivot table, and so on.
      props:
      - name: can_edit
        value: boolean
      - name: created_at
        value: string
        description: |
          The timestamp when this query was created.
      - name: data_source_id
        value: string
        description: |
          Data source ID maps to the ID of the data source used by the resource and is distinct from the warehouse ID. [Learn more] [Learn more]: https://docs.databricks.com/api/workspace/datasources/list
      - name: description
        value: string
        description: |
          General description that conveys additional information about this query such as usage notes.
      - name: id
        value: string
        description: |
          Query ID.
      - name: is_archived
        value: boolean
        description: |
          Indicates whether the query is trashed. Trashed queries can't be used in dashboards, or appear in search results. If this boolean is `true`, the `options` property for this query includes a `moved_to_trash_at` timestamp. Trashed queries are permanently deleted after 30 days.
      - name: is_draft
        value: boolean
        description: |
          Whether the query is a draft. Draft queries only appear in list views for their owners. Visualizations from draft queries cannot appear on dashboards.
      - name: is_favorite
        value: boolean
        description: |
          Whether this query object appears in the current user's favorites list. This flag determines whether the star icon for favorites is selected.
      - name: is_safe
        value: boolean
        description: |
          Text parameter types are not safe from SQL injection for all types of data source. Set this Boolean parameter to `true` if a query either does not use any text type parameters or uses a data source type where text type parameters are handled safely.
      - name: last_modified_by
        value: object
        props:
        - name: email
          value: string
        - name: id
          value: integer
        - name: name
          value: string
      - name: last_modified_by_id
        value: integer
        description: |
          The ID of the user who last saved changes to this query.
      - name: latest_query_data_id
        value: string
        description: |
          If there is a cached result for this query and user, this field includes the query result ID. If this query uses parameters, this field is always null.
      - name: name
        value: string
        description: |
          The title of this query that appears in list views, widget headings, and on the query page.
      - name: options
        value: object
        props:
        - name: catalog
          value: string
        - name: moved_to_trash_at
          value: string
          description: |
            The timestamp when this query was moved to trash. Only present when the `is_archived` property is `true`. Trashed items are deleted after thirty days.
        - name: parameters
          value: array
          props:
          - name: enumOptions
            value: string
          - name: multiValuesOptions
            value: object
            description: |
              If specified, allows multiple values to be selected for this parameter. Only applies to dropdown list and query-based dropdown list parameters.
            props:
            - name: prefix
              value: string
            - name: separator
              value: string
              description: |
                Character that separates each selected parameter value. Defaults to a comma.
            - name: suffix
              value: string
              description: |
                Character that suffixes each selected parameter value.
          - name: name
            value: string
            description: |
              The literal parameter marker that appears between double curly braces in the query text.
          - name: queryId
            value: string
            description: |
              The UUID of the query that provides the parameter values. Only applies for query-based dropdown list parameters.
          - name: title
            value: string
            description: |
              The text displayed in a parameter picking widget.
          - name: type
            value: string
            description: |
              Parameters can have several different types.
          - name: value
            value: object
            description: |
              The default value for this parameter.
        - name: schema
          value: string
          description: |
            The name of the schema to execute this query in.
      - name: parent
        value: string
        description: |
          The identifier of the workspace folder containing the object.
      - name: permission_tier
        value: string
        description: |
          * `CAN_VIEW`: Can view the query * `CAN_RUN`: Can run the query * `CAN_EDIT`: Can edit the query * `CAN_MANAGE`: Can manage the query
      - name: query
        value: string
        description: |
          The text of the query to be run.
      - name: query_hash
        value: string
        description: |
          A SHA-256 hash of the query text along with the authenticated user ID.
      - name: run_as_role
        value: string
        description: |
          Sets the **Run as** role for the object. Must be set to one of `"viewer"` (signifying "run as viewer" behavior) or `"owner"` (signifying "run as owner" behavior)
      - name: tags
        value: array
        items:
          type: string
      - name: updated_at
        value: string
        description: |
          The timestamp at which this query was last updated.
      - name: user
        value: object
        props:
        - name: email
          value: string
        - name: id
          value: integer
        - name: name
          value: string
      - name: user_id
        value: integer
        description: |
          The ID of the user who owns the query.
      - name: visualizations
        value: array
        props:
        - name: created_at
          value: string
        - name: description
          value: string
          description: |
            A short description of this visualization. This is not displayed in the UI.
        - name: id
          value: string
          description: |
            The UUID for this visualization.
        - name: name
          value: string
          description: |
            The name of the visualization that appears on dashboards and the query screen.
        - name: options
          value: object
          description: |
            The options object varies widely from one visualization type to the next and is unsupported. Databricks does not recommend modifying visualization settings in JSON.
        - name: query
          value: object
          props:
          - name: can_edit
            value: boolean
          - name: created_at
            value: string
            description: |
              The timestamp when this query was created.
          - name: data_source_id
            value: string
            description: |
              Data source ID maps to the ID of the data source used by the resource and is distinct from the warehouse ID. [Learn more] [Learn more]: https://docs.databricks.com/api/workspace/datasources/list
          - name: description
            value: string
            description: |
              General description that conveys additional information about this query such as usage notes.
          - name: id
            value: string
            description: |
              Query ID.
          - name: is_archived
            value: boolean
            description: |
              Indicates whether the query is trashed. Trashed queries can't be used in dashboards, or appear in search results. If this boolean is `true`, the `options` property for this query includes a `moved_to_trash_at` timestamp. Trashed queries are permanently deleted after 30 days.
          - name: is_draft
            value: boolean
            description: |
              Whether the query is a draft. Draft queries only appear in list views for their owners. Visualizations from draft queries cannot appear on dashboards.
          - name: is_favorite
            value: boolean
            description: |
              Whether this query object appears in the current user's favorites list. This flag determines whether the star icon for favorites is selected.
          - name: is_safe
            value: boolean
            description: |
              Text parameter types are not safe from SQL injection for all types of data source. Set this Boolean parameter to `true` if a query either does not use any text type parameters or uses a data source type where text type parameters are handled safely.
          - name: last_modified_by
            value: object
            props:
            - name: email
              value: string
            - name: id
              value: integer
            - name: name
              value: string
          - name: last_modified_by_id
            value: integer
            description: |
              The ID of the user who last saved changes to this query.
          - name: latest_query_data_id
            value: string
            description: |
              If there is a cached result for this query and user, this field includes the query result ID. If this query uses parameters, this field is always null.
          - name: name
            value: string
            description: |
              The title of this query that appears in list views, widget headings, and on the query page.
          - name: options
            value: object
            props:
            - name: catalog
              value: string
            - name: moved_to_trash_at
              value: string
              description: |
                The timestamp when this query was moved to trash. Only present when the `is_archived` property is `true`. Trashed items are deleted after thirty days.
            - name: parameters
              value: array
            - name: schema
              value: string
              description: |
                The name of the schema to execute this query in.
          - name: parent
            value: string
            description: |
              The identifier of the workspace folder containing the object.
          - name: permission_tier
            value: string
            description: |
              * `CAN_VIEW`: Can view the query * `CAN_RUN`: Can run the query * `CAN_EDIT`: Can edit the query * `CAN_MANAGE`: Can manage the query
          - name: query
            value: string
            description: |
              The text of the query to be run.
          - name: query_hash
            value: string
            description: |
              A SHA-256 hash of the query text along with the authenticated user ID.
          - name: run_as_role
            value: string
            description: |
              Sets the **Run as** role for the object. Must be set to one of `"viewer"` (signifying "run as viewer" behavior) or `"owner"` (signifying "run as owner" behavior)
          - name: tags
            value: array
            items:
              type: string
          - name: updated_at
            value: string
            description: |
              The timestamp at which this query was last updated.
          - name: user
            value: object
            props:
            - name: email
              value: string
            - name: id
              value: integer
            - name: name
              value: string
          - name: user_id
            value: integer
            description: |
              The ID of the user who owns the query.
          - name: visualizations
            value: array
            props:
            - name: created_at
              value: string
            - name: description
              value: string
              description: |
                A short description of this visualization. This is not displayed in the UI.
            - name: id
              value: string
              description: |
                The UUID for this visualization.
            - name: name
              value: string
              description: |
                The name of the visualization that appears on dashboards and the query screen.
            - name: options
              value: object
              description: |
                The options object varies widely from one visualization type to the next and is unsupported. Databricks does not recommend modifying visualization settings in JSON.
            - name: query
              value: object
            - name: type
              value: string
              description: |
                The type of visualization: chart, table, pivot table, and so on.
            - name: updated_at
              value: string
        - name: type
          value: string
          description: |
            The type of visualization: chart, table, pivot table, and so on.
        - name: updated_at
          value: string
    - name: type
      value: string
      description: |
        The type of visualization: chart, table, pivot table, and so on.
    - name: updated_at
      value: string
      description: |
        :returns: :class:`LegacyVisualization`
    - name: query_id
      value: string
      description: |
        The identifier returned by :method:queries/create
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

Removes a visualization from the query.

```sql
DELETE FROM databricks_workspace.sql.query_visualizations_legacy
WHERE id = '{{ id }}' --required
AND workspace = '{{ workspace }}' --required
;
```
</TabItem>
</Tabs>
