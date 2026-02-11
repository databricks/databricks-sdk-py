---
title: provider_listings
hide_title: false
hide_table_of_contents: false
keywords:
  - provider_listings
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import SchemaTable from '@site/src/components/SchemaTable/SchemaTable';

Creates, updates, deletes, gets or lists a <code>provider_listings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>provider_listings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.marketplace.provider_listings" /></td></tr>
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
    "name": "listing",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "summary",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "name",
            "type": "string",
            "description": ""
          },
          {
            "name": "listing_type",
            "type": "string",
            "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details."
          },
          {
            "name": "categories",
            "type": "array",
            "description": ""
          },
          {
            "name": "created_at",
            "type": "integer",
            "description": ""
          },
          {
            "name": "created_by",
            "type": "string",
            "description": ""
          },
          {
            "name": "created_by_id",
            "type": "integer",
            "description": ""
          },
          {
            "name": "exchange_ids",
            "type": "array",
            "description": ""
          },
          {
            "name": "git_repo",
            "type": "object",
            "description": "if a git repo is being created, a listing will be initialized with this field as opposed to a share",
            "children": [
              {
                "name": "git_repo_url",
                "type": "string",
                "description": ""
              }
            ]
          },
          {
            "name": "provider_id",
            "type": "string",
            "description": ""
          },
          {
            "name": "provider_region",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "cloud",
                "type": "string",
                "description": ""
              },
              {
                "name": "region",
                "type": "string",
                "description": ""
              }
            ]
          },
          {
            "name": "published_at",
            "type": "integer",
            "description": ""
          },
          {
            "name": "published_by",
            "type": "string",
            "description": ""
          },
          {
            "name": "setting",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "visibility",
                "type": "string",
                "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details."
              }
            ]
          },
          {
            "name": "share",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "name",
                "type": "string",
                "description": ""
              },
              {
                "name": "type",
                "type": "string",
                "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details."
              }
            ]
          },
          {
            "name": "status",
            "type": "string",
            "description": "Enums"
          },
          {
            "name": "subtitle",
            "type": "string",
            "description": ""
          },
          {
            "name": "updated_at",
            "type": "integer",
            "description": ""
          },
          {
            "name": "updated_by",
            "type": "string",
            "description": ""
          },
          {
            "name": "updated_by_id",
            "type": "integer",
            "description": ""
          }
        ]
      },
      {
        "name": "detail",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "assets",
            "type": "array",
            "description": ""
          },
          {
            "name": "collection_date_end",
            "type": "integer",
            "description": "The ending date timestamp for when the data spans"
          },
          {
            "name": "collection_date_start",
            "type": "integer",
            "description": "The starting date timestamp for when the data spans"
          },
          {
            "name": "collection_granularity",
            "type": "object",
            "description": "Smallest unit of time in the dataset",
            "children": [
              {
                "name": "interval",
                "type": "integer",
                "description": ""
              },
              {
                "name": "unit",
                "type": "string",
                "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details."
              }
            ]
          },
          {
            "name": "cost",
            "type": "string",
            "description": "Whether the dataset is free or paid"
          },
          {
            "name": "data_source",
            "type": "string",
            "description": "Where/how the data is sourced"
          },
          {
            "name": "description",
            "type": "string",
            "description": ""
          },
          {
            "name": "documentation_link",
            "type": "string",
            "description": ""
          },
          {
            "name": "embedded_notebook_file_infos",
            "type": "array",
            "description": "",
            "children": [
              {
                "name": "created_at",
                "type": "integer",
                "description": ""
              },
              {
                "name": "display_name",
                "type": "string",
                "description": "Name displayed to users for applicable files, e.g. embedded notebooks"
              },
              {
                "name": "download_link",
                "type": "string",
                "description": ""
              },
              {
                "name": "file_parent",
                "type": "object",
                "description": ""
              },
              {
                "name": "id",
                "type": "string",
                "description": ""
              },
              {
                "name": "marketplace_file_type",
                "type": "string",
                "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details."
              },
              {
                "name": "mime_type",
                "type": "string",
                "description": ""
              },
              {
                "name": "status",
                "type": "string",
                "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details."
              },
              {
                "name": "status_message",
                "type": "string",
                "description": "Populated if status is in a failed state with more information on reason for the failure."
              },
              {
                "name": "updated_at",
                "type": "integer",
                "description": ""
              }
            ]
          },
          {
            "name": "file_ids",
            "type": "array",
            "description": ""
          },
          {
            "name": "geographical_coverage",
            "type": "string",
            "description": "Which geo region the listing data is collected from"
          },
          {
            "name": "license",
            "type": "string",
            "description": "ID 20, 21 removed don't use License of the data asset - Required for listings with model based assets"
          },
          {
            "name": "pricing_model",
            "type": "string",
            "description": "What the pricing model is (e.g. paid, subscription, paid upfront); should only be present if cost is paid TODO: Not used yet, should deprecate if we will never use it"
          },
          {
            "name": "privacy_policy_link",
            "type": "string",
            "description": ""
          },
          {
            "name": "size",
            "type": "number",
            "description": "size of the dataset in GB"
          },
          {
            "name": "support_link",
            "type": "string",
            "description": ""
          },
          {
            "name": "tags",
            "type": "array",
            "description": "Listing tags - Simple key value pair to annotate listings. When should I use tags vs dedicated fields? Using tags avoids the need to add new columns in the database for new annotations. However, this should be used sparingly since tags are stored as key value pair. Use tags only: 1. If the field is optional and won't need to have NOT NULL integrity check 2. The value is fairly fixed, static and low cardinality (eg. enums). 3. The value won't be used in filters or joins with other tables.",
            "children": [
              {
                "name": "tag_name",
                "type": "string",
                "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details."
              },
              {
                "name": "tag_values",
                "type": "array",
                "description": "String representation of the tag value. Values should be string literals (no complex types)"
              }
            ]
          },
          {
            "name": "terms_of_service",
            "type": "string",
            "description": ""
          },
          {
            "name": "update_frequency",
            "type": "object",
            "description": "How often data is updated",
            "children": [
              {
                "name": "interval",
                "type": "integer",
                "description": ""
              },
              {
                "name": "unit",
                "type": "string",
                "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details."
              }
            ]
          }
        ]
      },
      {
        "name": "id",
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
    "name": "detail",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "assets",
        "type": "array",
        "description": ""
      },
      {
        "name": "collection_date_end",
        "type": "integer",
        "description": "The ending date timestamp for when the data spans"
      },
      {
        "name": "collection_date_start",
        "type": "integer",
        "description": "The starting date timestamp for when the data spans"
      },
      {
        "name": "collection_granularity",
        "type": "object",
        "description": "Smallest unit of time in the dataset",
        "children": [
          {
            "name": "interval",
            "type": "integer",
            "description": ""
          },
          {
            "name": "unit",
            "type": "string",
            "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details."
          }
        ]
      },
      {
        "name": "cost",
        "type": "string",
        "description": "Whether the dataset is free or paid"
      },
      {
        "name": "data_source",
        "type": "string",
        "description": "Where/how the data is sourced"
      },
      {
        "name": "description",
        "type": "string",
        "description": ""
      },
      {
        "name": "documentation_link",
        "type": "string",
        "description": ""
      },
      {
        "name": "embedded_notebook_file_infos",
        "type": "array",
        "description": "",
        "children": [
          {
            "name": "created_at",
            "type": "integer",
            "description": ""
          },
          {
            "name": "display_name",
            "type": "string",
            "description": "Name displayed to users for applicable files, e.g. embedded notebooks"
          },
          {
            "name": "download_link",
            "type": "string",
            "description": ""
          },
          {
            "name": "file_parent",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "file_parent_type",
                "type": "string",
                "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details."
              },
              {
                "name": "parent_id",
                "type": "string",
                "description": "TODO make the following fields required"
              }
            ]
          },
          {
            "name": "id",
            "type": "string",
            "description": ""
          },
          {
            "name": "marketplace_file_type",
            "type": "string",
            "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details."
          },
          {
            "name": "mime_type",
            "type": "string",
            "description": ""
          },
          {
            "name": "status",
            "type": "string",
            "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details."
          },
          {
            "name": "status_message",
            "type": "string",
            "description": "Populated if status is in a failed state with more information on reason for the failure."
          },
          {
            "name": "updated_at",
            "type": "integer",
            "description": ""
          }
        ]
      },
      {
        "name": "file_ids",
        "type": "array",
        "description": ""
      },
      {
        "name": "geographical_coverage",
        "type": "string",
        "description": "Which geo region the listing data is collected from"
      },
      {
        "name": "license",
        "type": "string",
        "description": "ID 20, 21 removed don't use License of the data asset - Required for listings with model based assets"
      },
      {
        "name": "pricing_model",
        "type": "string",
        "description": "What the pricing model is (e.g. paid, subscription, paid upfront); should only be present if cost is paid TODO: Not used yet, should deprecate if we will never use it"
      },
      {
        "name": "privacy_policy_link",
        "type": "string",
        "description": ""
      },
      {
        "name": "size",
        "type": "number",
        "description": "size of the dataset in GB"
      },
      {
        "name": "support_link",
        "type": "string",
        "description": ""
      },
      {
        "name": "tags",
        "type": "array",
        "description": "Listing tags - Simple key value pair to annotate listings. When should I use tags vs dedicated fields? Using tags avoids the need to add new columns in the database for new annotations. However, this should be used sparingly since tags are stored as key value pair. Use tags only: 1. If the field is optional and won't need to have NOT NULL integrity check 2. The value is fairly fixed, static and low cardinality (eg. enums). 3. The value won't be used in filters or joins with other tables.",
        "children": [
          {
            "name": "tag_name",
            "type": "string",
            "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details."
          },
          {
            "name": "tag_values",
            "type": "array",
            "description": "String representation of the tag value. Values should be string literals (no complex types)"
          }
        ]
      },
      {
        "name": "terms_of_service",
        "type": "string",
        "description": ""
      },
      {
        "name": "update_frequency",
        "type": "object",
        "description": "How often data is updated",
        "children": [
          {
            "name": "interval",
            "type": "integer",
            "description": ""
          },
          {
            "name": "unit",
            "type": "string",
            "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details."
          }
        ]
      }
    ]
  },
  {
    "name": "summary",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "name",
        "type": "string",
        "description": ""
      },
      {
        "name": "listing_type",
        "type": "string",
        "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details."
      },
      {
        "name": "categories",
        "type": "array",
        "description": ""
      },
      {
        "name": "created_at",
        "type": "integer",
        "description": ""
      },
      {
        "name": "created_by",
        "type": "string",
        "description": ""
      },
      {
        "name": "created_by_id",
        "type": "integer",
        "description": ""
      },
      {
        "name": "exchange_ids",
        "type": "array",
        "description": ""
      },
      {
        "name": "git_repo",
        "type": "object",
        "description": "if a git repo is being created, a listing will be initialized with this field as opposed to a share",
        "children": [
          {
            "name": "git_repo_url",
            "type": "string",
            "description": ""
          }
        ]
      },
      {
        "name": "provider_id",
        "type": "string",
        "description": ""
      },
      {
        "name": "provider_region",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "cloud",
            "type": "string",
            "description": ""
          },
          {
            "name": "region",
            "type": "string",
            "description": ""
          }
        ]
      },
      {
        "name": "published_at",
        "type": "integer",
        "description": ""
      },
      {
        "name": "published_by",
        "type": "string",
        "description": ""
      },
      {
        "name": "setting",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "visibility",
            "type": "string",
            "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details."
          }
        ]
      },
      {
        "name": "share",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "name",
            "type": "string",
            "description": ""
          },
          {
            "name": "type",
            "type": "string",
            "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details."
          }
        ]
      },
      {
        "name": "status",
        "type": "string",
        "description": "Enums"
      },
      {
        "name": "subtitle",
        "type": "string",
        "description": ""
      },
      {
        "name": "updated_at",
        "type": "integer",
        "description": ""
      },
      {
        "name": "updated_by",
        "type": "string",
        "description": ""
      },
      {
        "name": "updated_by_id",
        "type": "integer",
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
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Get a listing<br /><br />:param id: str<br /><br />:returns: :class:`GetListingResponse`</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>List listings owned by this provider<br /><br />:param page_size: int (optional)<br />:param page_token: str (optional)<br /><br />:returns: Iterator over :class:`Listing`</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-data__listing"><code>data__listing</code></a></td>
    <td></td>
    <td>Create a new listing<br /><br />:param listing: :class:`Listing`<br /><br />:returns: :class:`CreateListingResponse`</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-data__listing"><code>data__listing</code></a></td>
    <td></td>
    <td>Update a listing<br /><br />:param id: str<br />:param listing: :class:`Listing`<br /><br />:returns: :class:`UpdateListingResponse`</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Delete a listing<br /><br />:param id: str</td>
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
    <td>str</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>string</code></td>
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

Get a listing<br /><br />:param id: str<br /><br />:returns: :class:`GetListingResponse`

```sql
SELECT
listing
FROM databricks_workspace.marketplace.provider_listings
WHERE id = '{{ id }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
;
```
</TabItem>
<TabItem value="list">

List listings owned by this provider<br /><br />:param page_size: int (optional)<br />:param page_token: str (optional)<br /><br />:returns: Iterator over :class:`Listing`

```sql
SELECT
id,
detail,
summary
FROM databricks_workspace.marketplace.provider_listings
WHERE deployment_name = '{{ deployment_name }}' -- required
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

Create a new listing<br /><br />:param listing: :class:`Listing`<br /><br />:returns: :class:`CreateListingResponse`

```sql
INSERT INTO databricks_workspace.marketplace.provider_listings (
data__listing,
deployment_name
)
SELECT 
'{{ listing }}' /* required */,
'{{ deployment_name }}'
RETURNING
listing_id
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: provider_listings
  props:
    - name: deployment_name
      value: string
      description: Required parameter for the provider_listings resource.
    - name: listing
      value: string
      description: |
        :returns: :class:`CreateListingResponse`
```
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

Update a listing<br /><br />:param id: str<br />:param listing: :class:`Listing`<br /><br />:returns: :class:`UpdateListingResponse`

```sql
REPLACE databricks_workspace.marketplace.provider_listings
SET 
data__listing = '{{ listing }}'
WHERE 
id = '{{ id }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND data__listing = '{{ listing }}' --required
RETURNING
listing;
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

Delete a listing<br /><br />:param id: str

```sql
DELETE FROM databricks_workspace.marketplace.provider_listings
WHERE id = '{{ id }}' --required
AND deployment_name = '{{ deployment_name }}' --required
;
```
</TabItem>
</Tabs>
