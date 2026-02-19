---
title: queries_legacy
hide_title: false
hide_table_of_contents: false
keywords:
  - queries_legacy
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

Creates, updates, deletes, gets or lists a <code>queries_legacy</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="queries_legacy" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.sql.queries_legacy" /></td></tr>
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
    "description": "Query ID."
  },
  {
    "name": "name",
    "type": "string",
    "description": "The title of this query that appears in list views, widget headings, and on the query page."
  },
  {
    "name": "data_source_id",
    "type": "string",
    "description": "Data source ID maps to the ID of the data source used by the resource and is distinct from the warehouse ID. [Learn more] [Learn more]: https://docs.databricks.com/api/workspace/datasources/list"
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
    "name": "user_id",
    "type": "integer",
    "description": "The ID of the user who owns the query."
  },
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
    "name": "description",
    "type": "string",
    "description": "General description that conveys additional information about this query such as usage notes."
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
    "name": "options",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "catalog",
        "type": "string",
        "description": ""
      },
      {
        "name": "moved_to_trash_at",
        "type": "string",
        "description": "The timestamp when this query was moved to trash. Only present when the `is_archived` property is `true`. Trashed items are deleted after thirty days."
      },
      {
        "name": "parameters",
        "type": "array",
        "description": "",
        "children": [
          {
            "name": "enumOptions",
            "type": "string",
            "description": ""
          },
          {
            "name": "multiValuesOptions",
            "type": "object",
            "description": "If specified, allows multiple values to be selected for this parameter. Only applies to dropdown list and query-based dropdown list parameters.",
            "children": [
              {
                "name": "prefix",
                "type": "string",
                "description": ""
              },
              {
                "name": "separator",
                "type": "string",
                "description": "Character that separates each selected parameter value. Defaults to a comma."
              },
              {
                "name": "suffix",
                "type": "string",
                "description": "Character that suffixes each selected parameter value."
              }
            ]
          },
          {
            "name": "name",
            "type": "string",
            "description": "The literal parameter marker that appears between double curly braces in the query text."
          },
          {
            "name": "queryId",
            "type": "string",
            "description": "The UUID of the query that provides the parameter values. Only applies for query-based dropdown list parameters."
          },
          {
            "name": "title",
            "type": "string",
            "description": "The text displayed in a parameter picking widget."
          },
          {
            "name": "type",
            "type": "string",
            "description": "Parameters can have several different types. (datetime, enum, number, query, text)"
          },
          {
            "name": "value",
            "type": "object",
            "description": "The default value for this parameter."
          }
        ]
      },
      {
        "name": "schema",
        "type": "string",
        "description": "The name of the schema to execute this query in."
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
    "name": "visualizations",
    "type": "array",
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
            "description": "",
            "children": [
              {
                "name": "catalog",
                "type": "string",
                "description": ""
              },
              {
                "name": "moved_to_trash_at",
                "type": "string",
                "description": "The timestamp when this query was moved to trash. Only present when the `is_archived` property is `true`. Trashed items are deleted after thirty days."
              },
              {
                "name": "parameters",
                "type": "array",
                "description": ""
              },
              {
                "name": "schema",
                "type": "string",
                "description": "The name of the schema to execute this query in."
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
            "name": "user_id",
            "type": "integer",
            "description": "The ID of the user who owns the query."
          },
          {
            "name": "visualizations",
            "type": "array",
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
                "description": ""
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
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "id",
    "type": "string",
    "description": "Query ID."
  },
  {
    "name": "name",
    "type": "string",
    "description": "The title of this query that appears in list views, widget headings, and on the query page."
  },
  {
    "name": "data_source_id",
    "type": "string",
    "description": "Data source ID maps to the ID of the data source used by the resource and is distinct from the warehouse ID. [Learn more] [Learn more]: https://docs.databricks.com/api/workspace/datasources/list"
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
    "name": "user_id",
    "type": "integer",
    "description": "The ID of the user who owns the query."
  },
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
    "name": "description",
    "type": "string",
    "description": "General description that conveys additional information about this query such as usage notes."
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
    "name": "options",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "catalog",
        "type": "string",
        "description": ""
      },
      {
        "name": "moved_to_trash_at",
        "type": "string",
        "description": "The timestamp when this query was moved to trash. Only present when the `is_archived` property is `true`. Trashed items are deleted after thirty days."
      },
      {
        "name": "parameters",
        "type": "array",
        "description": "",
        "children": [
          {
            "name": "enumOptions",
            "type": "string",
            "description": ""
          },
          {
            "name": "multiValuesOptions",
            "type": "object",
            "description": "If specified, allows multiple values to be selected for this parameter. Only applies to dropdown list and query-based dropdown list parameters.",
            "children": [
              {
                "name": "prefix",
                "type": "string",
                "description": ""
              },
              {
                "name": "separator",
                "type": "string",
                "description": "Character that separates each selected parameter value. Defaults to a comma."
              },
              {
                "name": "suffix",
                "type": "string",
                "description": "Character that suffixes each selected parameter value."
              }
            ]
          },
          {
            "name": "name",
            "type": "string",
            "description": "The literal parameter marker that appears between double curly braces in the query text."
          },
          {
            "name": "queryId",
            "type": "string",
            "description": "The UUID of the query that provides the parameter values. Only applies for query-based dropdown list parameters."
          },
          {
            "name": "title",
            "type": "string",
            "description": "The text displayed in a parameter picking widget."
          },
          {
            "name": "type",
            "type": "string",
            "description": "Parameters can have several different types. (datetime, enum, number, query, text)"
          },
          {
            "name": "value",
            "type": "object",
            "description": "The default value for this parameter."
          }
        ]
      },
      {
        "name": "schema",
        "type": "string",
        "description": "The name of the schema to execute this query in."
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
    "name": "visualizations",
    "type": "array",
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
            "description": "",
            "children": [
              {
                "name": "catalog",
                "type": "string",
                "description": ""
              },
              {
                "name": "moved_to_trash_at",
                "type": "string",
                "description": "The timestamp when this query was moved to trash. Only present when the `is_archived` property is `true`. Trashed items are deleted after thirty days."
              },
              {
                "name": "parameters",
                "type": "array",
                "description": ""
              },
              {
                "name": "schema",
                "type": "string",
                "description": "The name of the schema to execute this query in."
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
            "name": "user_id",
            "type": "integer",
            "description": "The ID of the user who owns the query."
          },
          {
            "name": "visualizations",
            "type": "array",
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
                "description": ""
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
    <td><a href="#parameter-query_id"><code>query_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Retrieve a query object definition along with contextual permissions information about the currently</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-order"><code>order</code></a>, <a href="#parameter-page"><code>page</code></a>, <a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-q"><code>q</code></a></td>
    <td>Gets a list of queries. Optionally, this list can be filtered by a search term.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Creates a new query definition. Queries created with this endpoint belong to the authenticated user</td>
</tr>
<tr>
    <td><a href="#replace"><CopyableCode code="replace" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-query_id"><code>query_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Modify this query definition.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-query_id"><code>query_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Moves a query to the trash. Trashed queries immediately disappear from searches and list views, and</td>
</tr>
<tr>
    <td><a href="#restore"><CopyableCode code="restore" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-query_id"><code>query_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Restore a query that has been moved to the trash. A restored query appears in list views and searches.</td>
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
<tr id="parameter-query_id">
    <td><CopyableCode code="query_id" /></td>
    <td><code>string</code></td>
    <td>str</td>
</tr>
<tr id="parameter-order">
    <td><CopyableCode code="order" /></td>
    <td><code>string</code></td>
    <td>Name of query attribute to order by. Default sort order is ascending. Append a dash (`-`) to order descending instead. - `name`: The name of the query. - `created_at`: The timestamp the query was created. - `runtime`: The time it took to run this query. This is blank for parameterized queries. A blank value is treated as the highest value for sorting. - `executed_at`: The timestamp when the query was last run. - `created_by`: The user name of the user that created the query.</td>
</tr>
<tr id="parameter-page">
    <td><CopyableCode code="page" /></td>
    <td><code>string</code></td>
    <td>Page number to retrieve.</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>string</code></td>
    <td>Number of queries to return per page.</td>
</tr>
<tr id="parameter-q">
    <td><CopyableCode code="q" /></td>
    <td><code>string</code></td>
    <td>Full text search term</td>
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

Retrieve a query object definition along with contextual permissions information about the currently

```sql
SELECT
id,
name,
data_source_id,
last_modified_by_id,
latest_query_data_id,
user_id,
can_edit,
created_at,
description,
is_archived,
is_draft,
is_favorite,
is_safe,
last_modified_by,
options,
parent,
permission_tier,
query,
query_hash,
run_as_role,
tags,
updated_at,
user,
visualizations
FROM databricks_workspace.sql.queries_legacy
WHERE query_id = '{{ query_id }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets a list of queries. Optionally, this list can be filtered by a search term.

```sql
SELECT
id,
name,
data_source_id,
last_modified_by_id,
latest_query_data_id,
user_id,
can_edit,
created_at,
description,
is_archived,
is_draft,
is_favorite,
is_safe,
last_modified_by,
options,
parent,
permission_tier,
query,
query_hash,
run_as_role,
tags,
updated_at,
user,
visualizations
FROM databricks_workspace.sql.queries_legacy
WHERE deployment_name = '{{ deployment_name }}' -- required
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
    defaultValue="create"
    values={[
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create">

Creates a new query definition. Queries created with this endpoint belong to the authenticated user

```sql
INSERT INTO databricks_workspace.sql.queries_legacy (
data_source_id,
description,
name,
options,
parent,
query,
run_as_role,
tags,
deployment_name
)
SELECT 
'{{ data_source_id }}',
'{{ description }}',
'{{ name }}',
'{{ options }}',
'{{ parent }}',
'{{ query }}',
'{{ run_as_role }}',
'{{ tags }}',
'{{ deployment_name }}'
RETURNING
id,
name,
data_source_id,
last_modified_by_id,
latest_query_data_id,
user_id,
can_edit,
created_at,
description,
is_archived,
is_draft,
is_favorite,
is_safe,
last_modified_by,
options,
parent,
permission_tier,
query,
query_hash,
run_as_role,
tags,
updated_at,
user,
visualizations
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: queries_legacy
  props:
    - name: deployment_name
      value: string
      description: Required parameter for the queries_legacy resource.
    - name: data_source_id
      value: string
      description: |
        Data source ID maps to the ID of the data source used by the resource and is distinct from the warehouse ID. [Learn more] [Learn more]: https://docs.databricks.com/api/workspace/datasources/list
    - name: description
      value: string
      description: |
        General description that conveys additional information about this query such as usage notes.
    - name: name
      value: string
      description: |
        The title of this query that appears in list views, widget headings, and on the query page.
    - name: options
      value: string
      description: |
        Exclusively used for storing a list parameter definitions. A parameter is an object with `title`, `name`, `type`, and `value` properties. The `value` field here is the default value. It can be overridden at runtime.
    - name: parent
      value: string
      description: |
        The identifier of the workspace folder containing the object.
    - name: query
      value: string
      description: |
        The text of the query to be run.
    - name: run_as_role
      value: string
      description: |
        Sets the **Run as** role for the object. Must be set to one of `"viewer"` (signifying "run as viewer" behavior) or `"owner"` (signifying "run as owner" behavior)
    - name: tags
      value: string
      description: |
        :returns: :class:`LegacyQuery`
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="replace"
    values={[
        { label: 'replace', value: 'replace' }
    ]}
>
<TabItem value="replace">

Modify this query definition.

```sql
REPLACE databricks_workspace.sql.queries_legacy
SET 
data_source_id = '{{ data_source_id }}',
description = '{{ description }}',
name = '{{ name }}',
options = '{{ options }}',
query = '{{ query }}',
run_as_role = '{{ run_as_role }}',
tags = '{{ tags }}'
WHERE 
query_id = '{{ query_id }}' --required
AND deployment_name = '{{ deployment_name }}' --required
RETURNING
id,
name,
data_source_id,
last_modified_by_id,
latest_query_data_id,
user_id,
can_edit,
created_at,
description,
is_archived,
is_draft,
is_favorite,
is_safe,
last_modified_by,
options,
parent,
permission_tier,
query,
query_hash,
run_as_role,
tags,
updated_at,
user,
visualizations;
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

Moves a query to the trash. Trashed queries immediately disappear from searches and list views, and

```sql
DELETE FROM databricks_workspace.sql.queries_legacy
WHERE query_id = '{{ query_id }}' --required
AND deployment_name = '{{ deployment_name }}' --required
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

Restore a query that has been moved to the trash. A restored query appears in list views and searches.

```sql
EXEC databricks_workspace.sql.queries_legacy.restore 
@query_id='{{ query_id }}' --required, 
@deployment_name='{{ deployment_name }}' --required
;
```
</TabItem>
</Tabs>
