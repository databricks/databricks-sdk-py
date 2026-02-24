---
title: dashboards
hide_title: false
hide_table_of_contents: false
keywords:
  - dashboards
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

Creates, updates, deletes, gets or lists a <code>dashboards</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="dashboards" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.sql.dashboards" /></td></tr>
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
    "name": "id",
    "type": "string",
    "description": "The ID for this dashboard."
  },
  {
    "name": "name",
    "type": "string",
    "description": "The title of the dashboard that appears in list views and at the top of the dashboard page."
  },
  {
    "name": "user_id",
    "type": "integer",
    "description": "The ID of the user who owns the dashboard."
  },
  {
    "name": "can_edit",
    "type": "boolean",
    "description": "Whether the authenticated user can edit the query definition."
  },
  {
    "name": "created_at",
    "type": "string",
    "description": "Timestamp when this dashboard was created."
  },
  {
    "name": "dashboard_filters_enabled",
    "type": "boolean",
    "description": "In the web application, query filters that share a name are coupled to a single selection box if this value is `true`."
  },
  {
    "name": "is_archived",
    "type": "boolean",
    "description": "Indicates whether a dashboard is trashed. Trashed dashboards won't appear in list views. If this boolean is `true`, the `options` property for this dashboard includes a `moved_to_trash_at` timestamp. Items in trash are permanently deleted after 30 days."
  },
  {
    "name": "is_draft",
    "type": "boolean",
    "description": "Whether a dashboard is a draft. Draft dashboards only appear in list views for their owners."
  },
  {
    "name": "is_favorite",
    "type": "boolean",
    "description": "Indicates whether this query object appears in the current user's favorites list. This flag determines whether the star icon for favorites is selected."
  },
  {
    "name": "options",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "moved_to_trash_at",
        "type": "string",
        "description": ""
      }
    ]
  },
  {
    "name": "parent",
    "type": "string",
    "description": "The identifier of the workspace folder containing the object."
  },
  {
    "name": "permission_tier",
    "type": "string",
    "description": "* `CAN_VIEW`: Can view the query * `CAN_RUN`: Can run the query * `CAN_EDIT`: Can edit the query * `CAN_MANAGE`: Can manage the query (CAN_EDIT, CAN_MANAGE, CAN_RUN, CAN_VIEW)"
  },
  {
    "name": "slug",
    "type": "string",
    "description": "URL slug. Usually mirrors the query name with dashes (`-`) instead of spaces. Appears in the URL for this query."
  },
  {
    "name": "tags",
    "type": "array",
    "description": ""
  },
  {
    "name": "updated_at",
    "type": "string",
    "description": "Timestamp when this dashboard was last updated."
  },
  {
    "name": "user",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "email",
        "type": "string",
        "description": ""
      },
      {
        "name": "id",
        "type": "integer",
        "description": ""
      },
      {
        "name": "name",
        "type": "string",
        "description": ""
      }
    ]
  },
  {
    "name": "widgets",
    "type": "array",
    "description": "",
    "children": [
      {
        "name": "id",
        "type": "string",
        "description": ""
      },
      {
        "name": "options",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "created_at",
            "type": "string",
            "description": ""
          },
          {
            "name": "description",
            "type": "string",
            "description": "Custom description of the widget"
          },
          {
            "name": "isHidden",
            "type": "boolean",
            "description": "Whether this widget is hidden on the dashboard."
          },
          {
            "name": "parameterMappings",
            "type": "object",
            "description": "How parameters used by the visualization in this widget relate to other widgets on the dashboard. Databricks does not recommend modifying this definition in JSON."
          },
          {
            "name": "position",
            "type": "object",
            "description": "Coordinates of this widget on a dashboard. This portion of the API changes frequently and is unsupported.",
            "children": [
              {
                "name": "autoHeight",
                "type": "boolean",
                "description": "reserved for internal use"
              },
              {
                "name": "col",
                "type": "integer",
                "description": "column in the dashboard grid. Values start with 0"
              },
              {
                "name": "row",
                "type": "integer",
                "description": "row in the dashboard grid. Values start with 0"
              },
              {
                "name": "sizeX",
                "type": "integer",
                "description": "width of the widget measured in dashboard grid cells"
              },
              {
                "name": "sizeY",
                "type": "integer",
                "description": "height of the widget measured in dashboard grid cells"
              }
            ]
          },
          {
            "name": "title",
            "type": "string",
            "description": "Custom title of the widget"
          },
          {
            "name": "updated_at",
            "type": "string",
            "description": "Timestamp of the last time this object was updated."
          }
        ]
      },
      {
        "name": "visualization",
        "type": "object",
        "description": "The visualization description API changes frequently and is unsupported. You can duplicate a visualization by copying description objects received _from the API_ and then using them to create a new one with a POST request to the same endpoint. Databricks does not recommend constructing ad-hoc visualizations entirely in JSON.",
        "children": [
          {
            "name": "created_at",
            "type": "string",
            "description": ""
          },
          {
            "name": "description",
            "type": "string",
            "description": "A short description of this visualization. This is not displayed in the UI."
          },
          {
            "name": "id",
            "type": "string",
            "description": "The UUID for this visualization."
          },
          {
            "name": "name",
            "type": "string",
            "description": "The name of the visualization that appears on dashboards and the query screen."
          },
          {
            "name": "options",
            "type": "object",
            "description": "The options object varies widely from one visualization type to the next and is unsupported. Databricks does not recommend modifying visualization settings in JSON."
          },
          {
            "name": "query",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "can_edit",
                "type": "boolean",
                "description": ""
              },
              {
                "name": "created_at",
                "type": "string",
                "description": "The timestamp when this query was created."
              },
              {
                "name": "data_source_id",
                "type": "string",
                "description": "Data source ID maps to the ID of the data source used by the resource and is distinct from the warehouse ID. [Learn more] [Learn more]: https://docs.databricks.com/api/workspace/datasources/list"
              },
              {
                "name": "description",
                "type": "string",
                "description": "General description that conveys additional information about this query such as usage notes."
              },
              {
                "name": "id",
                "type": "string",
                "description": "Query ID."
              },
              {
                "name": "is_archived",
                "type": "boolean",
                "description": "Indicates whether the query is trashed. Trashed queries can't be used in dashboards, or appear in search results. If this boolean is `true`, the `options` property for this query includes a `moved_to_trash_at` timestamp. Trashed queries are permanently deleted after 30 days."
              },
              {
                "name": "is_draft",
                "type": "boolean",
                "description": "Whether the query is a draft. Draft queries only appear in list views for their owners. Visualizations from draft queries cannot appear on dashboards."
              },
              {
                "name": "is_favorite",
                "type": "boolean",
                "description": "Whether this query object appears in the current user's favorites list. This flag determines whether the star icon for favorites is selected."
              },
              {
                "name": "is_safe",
                "type": "boolean",
                "description": "Text parameter types are not safe from SQL injection for all types of data source. Set this Boolean parameter to `true` if a query either does not use any text type parameters or uses a data source type where text type parameters are handled safely."
              },
              {
                "name": "last_modified_by",
                "type": "object",
                "description": ""
              },
              {
                "name": "last_modified_by_id",
                "type": "integer",
                "description": "The ID of the user who last saved changes to this query."
              },
              {
                "name": "latest_query_data_id",
                "type": "string",
                "description": "If there is a cached result for this query and user, this field includes the query result ID. If this query uses parameters, this field is always null."
              },
              {
                "name": "name",
                "type": "string",
                "description": "The title of this query that appears in list views, widget headings, and on the query page."
              },
              {
                "name": "options",
                "type": "object",
                "description": ""
              },
              {
                "name": "parent",
                "type": "string",
                "description": "The identifier of the workspace folder containing the object."
              },
              {
                "name": "permission_tier",
                "type": "string",
                "description": "* `CAN_VIEW`: Can view the query * `CAN_RUN`: Can run the query * `CAN_EDIT`: Can edit the query * `CAN_MANAGE`: Can manage the query (CAN_EDIT, CAN_MANAGE, CAN_RUN, CAN_VIEW)"
              },
              {
                "name": "query",
                "type": "string",
                "description": "The text of the query to be run."
              },
              {
                "name": "query_hash",
                "type": "string",
                "description": "A SHA-256 hash of the query text along with the authenticated user ID."
              },
              {
                "name": "run_as_role",
                "type": "string",
                "description": "Sets the **Run as** role for the object. Must be set to one of `\"viewer\"` (signifying \"run as viewer\" behavior) or `\"owner\"` (signifying \"run as owner\" behavior) (owner, viewer)"
              },
              {
                "name": "tags",
                "type": "array",
                "description": ""
              },
              {
                "name": "updated_at",
                "type": "string",
                "description": "The timestamp at which this query was last updated."
              },
              {
                "name": "user",
                "type": "object",
                "description": ""
              },
              {
                "name": "user_id",
                "type": "integer",
                "description": "The ID of the user who owns the query."
              },
              {
                "name": "visualizations",
                "type": "array",
                "description": ""
              }
            ]
          },
          {
            "name": "type",
            "type": "string",
            "description": "The type of visualization: chart, table, pivot table, and so on."
          },
          {
            "name": "updated_at",
            "type": "string",
            "description": ""
          }
        ]
      },
      {
        "name": "width",
        "type": "integer",
        "description": "Unused field."
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
    "description": "The ID for this dashboard."
  },
  {
    "name": "name",
    "type": "string",
    "description": "The title of the dashboard that appears in list views and at the top of the dashboard page."
  },
  {
    "name": "user_id",
    "type": "integer",
    "description": "The ID of the user who owns the dashboard."
  },
  {
    "name": "can_edit",
    "type": "boolean",
    "description": "Whether the authenticated user can edit the query definition."
  },
  {
    "name": "created_at",
    "type": "string",
    "description": "Timestamp when this dashboard was created."
  },
  {
    "name": "dashboard_filters_enabled",
    "type": "boolean",
    "description": "In the web application, query filters that share a name are coupled to a single selection box if this value is `true`."
  },
  {
    "name": "is_archived",
    "type": "boolean",
    "description": "Indicates whether a dashboard is trashed. Trashed dashboards won't appear in list views. If this boolean is `true`, the `options` property for this dashboard includes a `moved_to_trash_at` timestamp. Items in trash are permanently deleted after 30 days."
  },
  {
    "name": "is_draft",
    "type": "boolean",
    "description": "Whether a dashboard is a draft. Draft dashboards only appear in list views for their owners."
  },
  {
    "name": "is_favorite",
    "type": "boolean",
    "description": "Indicates whether this query object appears in the current user's favorites list. This flag determines whether the star icon for favorites is selected."
  },
  {
    "name": "options",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "moved_to_trash_at",
        "type": "string",
        "description": ""
      }
    ]
  },
  {
    "name": "parent",
    "type": "string",
    "description": "The identifier of the workspace folder containing the object."
  },
  {
    "name": "permission_tier",
    "type": "string",
    "description": "* `CAN_VIEW`: Can view the query * `CAN_RUN`: Can run the query * `CAN_EDIT`: Can edit the query * `CAN_MANAGE`: Can manage the query (CAN_EDIT, CAN_MANAGE, CAN_RUN, CAN_VIEW)"
  },
  {
    "name": "slug",
    "type": "string",
    "description": "URL slug. Usually mirrors the query name with dashes (`-`) instead of spaces. Appears in the URL for this query."
  },
  {
    "name": "tags",
    "type": "array",
    "description": ""
  },
  {
    "name": "updated_at",
    "type": "string",
    "description": "Timestamp when this dashboard was last updated."
  },
  {
    "name": "user",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "email",
        "type": "string",
        "description": ""
      },
      {
        "name": "id",
        "type": "integer",
        "description": ""
      },
      {
        "name": "name",
        "type": "string",
        "description": ""
      }
    ]
  },
  {
    "name": "widgets",
    "type": "array",
    "description": "",
    "children": [
      {
        "name": "id",
        "type": "string",
        "description": ""
      },
      {
        "name": "options",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "created_at",
            "type": "string",
            "description": ""
          },
          {
            "name": "description",
            "type": "string",
            "description": "Custom description of the widget"
          },
          {
            "name": "isHidden",
            "type": "boolean",
            "description": "Whether this widget is hidden on the dashboard."
          },
          {
            "name": "parameterMappings",
            "type": "object",
            "description": "How parameters used by the visualization in this widget relate to other widgets on the dashboard. Databricks does not recommend modifying this definition in JSON."
          },
          {
            "name": "position",
            "type": "object",
            "description": "Coordinates of this widget on a dashboard. This portion of the API changes frequently and is unsupported.",
            "children": [
              {
                "name": "autoHeight",
                "type": "boolean",
                "description": "reserved for internal use"
              },
              {
                "name": "col",
                "type": "integer",
                "description": "column in the dashboard grid. Values start with 0"
              },
              {
                "name": "row",
                "type": "integer",
                "description": "row in the dashboard grid. Values start with 0"
              },
              {
                "name": "sizeX",
                "type": "integer",
                "description": "width of the widget measured in dashboard grid cells"
              },
              {
                "name": "sizeY",
                "type": "integer",
                "description": "height of the widget measured in dashboard grid cells"
              }
            ]
          },
          {
            "name": "title",
            "type": "string",
            "description": "Custom title of the widget"
          },
          {
            "name": "updated_at",
            "type": "string",
            "description": "Timestamp of the last time this object was updated."
          }
        ]
      },
      {
        "name": "visualization",
        "type": "object",
        "description": "The visualization description API changes frequently and is unsupported. You can duplicate a visualization by copying description objects received _from the API_ and then using them to create a new one with a POST request to the same endpoint. Databricks does not recommend constructing ad-hoc visualizations entirely in JSON.",
        "children": [
          {
            "name": "created_at",
            "type": "string",
            "description": ""
          },
          {
            "name": "description",
            "type": "string",
            "description": "A short description of this visualization. This is not displayed in the UI."
          },
          {
            "name": "id",
            "type": "string",
            "description": "The UUID for this visualization."
          },
          {
            "name": "name",
            "type": "string",
            "description": "The name of the visualization that appears on dashboards and the query screen."
          },
          {
            "name": "options",
            "type": "object",
            "description": "The options object varies widely from one visualization type to the next and is unsupported. Databricks does not recommend modifying visualization settings in JSON."
          },
          {
            "name": "query",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "can_edit",
                "type": "boolean",
                "description": ""
              },
              {
                "name": "created_at",
                "type": "string",
                "description": "The timestamp when this query was created."
              },
              {
                "name": "data_source_id",
                "type": "string",
                "description": "Data source ID maps to the ID of the data source used by the resource and is distinct from the warehouse ID. [Learn more] [Learn more]: https://docs.databricks.com/api/workspace/datasources/list"
              },
              {
                "name": "description",
                "type": "string",
                "description": "General description that conveys additional information about this query such as usage notes."
              },
              {
                "name": "id",
                "type": "string",
                "description": "Query ID."
              },
              {
                "name": "is_archived",
                "type": "boolean",
                "description": "Indicates whether the query is trashed. Trashed queries can't be used in dashboards, or appear in search results. If this boolean is `true`, the `options` property for this query includes a `moved_to_trash_at` timestamp. Trashed queries are permanently deleted after 30 days."
              },
              {
                "name": "is_draft",
                "type": "boolean",
                "description": "Whether the query is a draft. Draft queries only appear in list views for their owners. Visualizations from draft queries cannot appear on dashboards."
              },
              {
                "name": "is_favorite",
                "type": "boolean",
                "description": "Whether this query object appears in the current user's favorites list. This flag determines whether the star icon for favorites is selected."
              },
              {
                "name": "is_safe",
                "type": "boolean",
                "description": "Text parameter types are not safe from SQL injection for all types of data source. Set this Boolean parameter to `true` if a query either does not use any text type parameters or uses a data source type where text type parameters are handled safely."
              },
              {
                "name": "last_modified_by",
                "type": "object",
                "description": ""
              },
              {
                "name": "last_modified_by_id",
                "type": "integer",
                "description": "The ID of the user who last saved changes to this query."
              },
              {
                "name": "latest_query_data_id",
                "type": "string",
                "description": "If there is a cached result for this query and user, this field includes the query result ID. If this query uses parameters, this field is always null."
              },
              {
                "name": "name",
                "type": "string",
                "description": "The title of this query that appears in list views, widget headings, and on the query page."
              },
              {
                "name": "options",
                "type": "object",
                "description": ""
              },
              {
                "name": "parent",
                "type": "string",
                "description": "The identifier of the workspace folder containing the object."
              },
              {
                "name": "permission_tier",
                "type": "string",
                "description": "* `CAN_VIEW`: Can view the query * `CAN_RUN`: Can run the query * `CAN_EDIT`: Can edit the query * `CAN_MANAGE`: Can manage the query (CAN_EDIT, CAN_MANAGE, CAN_RUN, CAN_VIEW)"
              },
              {
                "name": "query",
                "type": "string",
                "description": "The text of the query to be run."
              },
              {
                "name": "query_hash",
                "type": "string",
                "description": "A SHA-256 hash of the query text along with the authenticated user ID."
              },
              {
                "name": "run_as_role",
                "type": "string",
                "description": "Sets the **Run as** role for the object. Must be set to one of `\"viewer\"` (signifying \"run as viewer\" behavior) or `\"owner\"` (signifying \"run as owner\" behavior) (owner, viewer)"
              },
              {
                "name": "tags",
                "type": "array",
                "description": ""
              },
              {
                "name": "updated_at",
                "type": "string",
                "description": "The timestamp at which this query was last updated."
              },
              {
                "name": "user",
                "type": "object",
                "description": ""
              },
              {
                "name": "user_id",
                "type": "integer",
                "description": "The ID of the user who owns the query."
              },
              {
                "name": "visualizations",
                "type": "array",
                "description": ""
              }
            ]
          },
          {
            "name": "type",
            "type": "string",
            "description": "The type of visualization: chart, table, pivot table, and so on."
          },
          {
            "name": "updated_at",
            "type": "string",
            "description": ""
          }
        ]
      },
      {
        "name": "width",
        "type": "integer",
        "description": "Unused field."
      }
    ]
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
    <td><a href="#parameter-dashboard_id"><code>dashboard_id</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Returns a JSON representation of a dashboard object, including its visualization and query objects.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-workspace"><code>workspace</code></a></td>
    <td><a href="#parameter-order"><code>order</code></a>, <a href="#parameter-page"><code>page</code></a>, <a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-q"><code>q</code></a></td>
    <td>Fetch a paginated list of dashboard objects.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-dashboard_id"><code>dashboard_id</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Modify this dashboard definition. This operation only affects attributes of the dashboard object. It</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-dashboard_id"><code>dashboard_id</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Moves a dashboard to the trash. Trashed dashboards do not appear in list views or searches, and cannot</td>
</tr>
<tr>
    <td><a href="#restore"><CopyableCode code="restore" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-dashboard_id"><code>dashboard_id</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>A restored dashboard appears in list views and searches and can be shared.</td>
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
<tr id="parameter-dashboard_id">
    <td><CopyableCode code="dashboard_id" /></td>
    <td><code>string</code></td>
    <td>str</td>
</tr>
<tr id="parameter-workspace">
    <td><CopyableCode code="workspace" /></td>
    <td><code>string</code></td>
    <td>Your Databricks workspace name (default: your-workspace)</td>
</tr>
<tr id="parameter-order">
    <td><CopyableCode code="order" /></td>
    <td><code>string</code></td>
    <td>Name of dashboard attribute to order by.</td>
</tr>
<tr id="parameter-page">
    <td><CopyableCode code="page" /></td>
    <td><code>integer</code></td>
    <td>Page number to retrieve.</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>integer</code></td>
    <td>Number of dashboards to return per page.</td>
</tr>
<tr id="parameter-q">
    <td><CopyableCode code="q" /></td>
    <td><code>string</code></td>
    <td>Full text search term.</td>
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

Returns a JSON representation of a dashboard object, including its visualization and query objects.

```sql
SELECT
id,
name,
user_id,
can_edit,
created_at,
dashboard_filters_enabled,
is_archived,
is_draft,
is_favorite,
options,
parent,
permission_tier,
slug,
tags,
updated_at,
user,
widgets
FROM databricks_workspace.sql.dashboards
WHERE dashboard_id = '{{ dashboard_id }}' -- required
AND workspace = '{{ workspace }}' -- required
;
```
</TabItem>
<TabItem value="list">

Fetch a paginated list of dashboard objects.

```sql
SELECT
id,
name,
user_id,
can_edit,
created_at,
dashboard_filters_enabled,
is_archived,
is_draft,
is_favorite,
options,
parent,
permission_tier,
slug,
tags,
updated_at,
user,
widgets
FROM databricks_workspace.sql.dashboards
WHERE workspace = '{{ workspace }}' -- required
AND order = '{{ order }}'
AND page = '{{ page }}'
AND page_size = '{{ page_size }}'
AND q = '{{ q }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="update">

Modify this dashboard definition. This operation only affects attributes of the dashboard object. It

```sql
INSERT INTO databricks_workspace.sql.dashboards (
name,
run_as_role,
tags,
dashboard_id,
workspace
)
SELECT 
'{{ name }}',
'{{ run_as_role }}',
'{{ tags }}',
'{{ dashboard_id }}',
'{{ workspace }}'
RETURNING
id,
name,
user_id,
can_edit,
created_at,
dashboard_filters_enabled,
is_archived,
is_draft,
is_favorite,
options,
parent,
permission_tier,
slug,
tags,
updated_at,
user,
widgets
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: dashboards
  props:
    - name: dashboard_id
      value: string
      description: Required parameter for the dashboards resource.
    - name: workspace
      value: string
      description: Required parameter for the dashboards resource.
    - name: name
      value: string
    - name: run_as_role
      value: string
      description: |
        Sets the **Run as** role for the object. Must be set to one of `"viewer"` (signifying "run as viewer" behavior) or `"owner"` (signifying "run as owner" behavior)
    - name: tags
      value: array
      description: |
        :returns: :class:`Dashboard`
      items:
        type: string
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

Moves a dashboard to the trash. Trashed dashboards do not appear in list views or searches, and cannot

```sql
DELETE FROM databricks_workspace.sql.dashboards
WHERE dashboard_id = '{{ dashboard_id }}' --required
AND workspace = '{{ workspace }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="restore"
    values={[
        { label: 'restore', value: 'restore' }
    ]}
>
<TabItem value="restore">

A restored dashboard appears in list views and searches and can be shared.

```sql
EXEC databricks_workspace.sql.dashboards.restore 
@dashboard_id='{{ dashboard_id }}' --required, 
@workspace='{{ workspace }}' --required
;
```
</TabItem>
</Tabs>
