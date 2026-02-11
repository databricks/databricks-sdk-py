---
title: tables
hide_title: false
hide_table_of_contents: false
keywords:
  - tables
  - catalog
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

Creates, updates, deletes, gets or lists a <code>tables</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tables</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.catalog.tables" /></td></tr>
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
    "name": "name",
    "type": "string",
    "description": "Name of table, relative to parent schema."
  },
  {
    "name": "data_access_configuration_id",
    "type": "string",
    "description": "Unique ID of the Data Access Configuration to use with the table data."
  },
  {
    "name": "metastore_id",
    "type": "string",
    "description": "Unique identifier of parent metastore."
  },
  {
    "name": "pipeline_id",
    "type": "string",
    "description": "The pipeline ID of the table. Applicable for tables created by pipelines (Materialized View, Streaming Table, etc.)."
  },
  {
    "name": "table_id",
    "type": "string",
    "description": "The unique identifier of the table."
  },
  {
    "name": "catalog_name",
    "type": "string",
    "description": "Name of parent catalog."
  },
  {
    "name": "full_name",
    "type": "string",
    "description": "Full name of table, in form of __catalog_name__.__schema_name__.__table_name__"
  },
  {
    "name": "schema_name",
    "type": "string",
    "description": "Name of parent schema relative to its parent catalog."
  },
  {
    "name": "storage_credential_name",
    "type": "string",
    "description": "Name of the storage credential, when a storage credential is configured for use with this table."
  },
  {
    "name": "access_point",
    "type": "string",
    "description": ""
  },
  {
    "name": "browse_only",
    "type": "boolean",
    "description": "Indicates whether the principal is limited to retrieving metadata for the associated object through the BROWSE privilege when include_browse is enabled in the request."
  },
  {
    "name": "columns",
    "type": "array",
    "description": "The array of __ColumnInfo__ definitions of the table's columns.",
    "children": [
      {
        "name": "comment",
        "type": "string",
        "description": ""
      },
      {
        "name": "mask",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "function_name",
            "type": "string",
            "description": ""
          },
          {
            "name": "using_column_names",
            "type": "array",
            "description": "The list of additional table columns to be passed as input to the column mask function. The first arg of the mask function should be of the type of the column being masked and the types of the rest of the args should match the types of columns in 'using_column_names'."
          }
        ]
      },
      {
        "name": "name",
        "type": "string",
        "description": "Name of Column."
      },
      {
        "name": "nullable",
        "type": "boolean",
        "description": "Whether field may be Null (default: true)."
      },
      {
        "name": "partition_index",
        "type": "integer",
        "description": "Partition index for column."
      },
      {
        "name": "position",
        "type": "integer",
        "description": "Ordinal position of column (starting at position 0)."
      },
      {
        "name": "type_interval_type",
        "type": "string",
        "description": "Format of IntervalType."
      },
      {
        "name": "type_json",
        "type": "string",
        "description": "Full data type specification, JSON-serialized."
      },
      {
        "name": "type_name",
        "type": "string",
        "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details."
      },
      {
        "name": "type_precision",
        "type": "integer",
        "description": "Digits of precision; required for DecimalTypes."
      },
      {
        "name": "type_scale",
        "type": "integer",
        "description": "Digits to right of decimal; Required for DecimalTypes."
      },
      {
        "name": "type_text",
        "type": "string",
        "description": "Full data type specification as SQL/catalogString text."
      }
    ]
  },
  {
    "name": "comment",
    "type": "string",
    "description": "User-provided free-form text description."
  },
  {
    "name": "created_at",
    "type": "integer",
    "description": "Time at which this table was created, in epoch milliseconds."
  },
  {
    "name": "created_by",
    "type": "string",
    "description": "Username of table creator."
  },
  {
    "name": "data_source_format",
    "type": "string",
    "description": "Data source format"
  },
  {
    "name": "deleted_at",
    "type": "integer",
    "description": "Time at which this table was deleted, in epoch milliseconds. Field is omitted if table is not deleted."
  },
  {
    "name": "delta_runtime_properties_kvpairs",
    "type": "object",
    "description": "Information pertaining to current state of the delta table.",
    "children": [
      {
        "name": "delta_runtime_properties",
        "type": "object",
        "description": "A map of key-value properties attached to the securable."
      }
    ]
  },
  {
    "name": "effective_predictive_optimization_flag",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "value",
        "type": "string",
        "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details."
      },
      {
        "name": "inherited_from_name",
        "type": "string",
        "description": "The name of the object from which the flag was inherited. If there was no inheritance, this field is left blank."
      },
      {
        "name": "inherited_from_type",
        "type": "string",
        "description": "The type of the object from which the flag was inherited. If there was no inheritance, this field is left blank."
      }
    ]
  },
  {
    "name": "enable_predictive_optimization",
    "type": "string",
    "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details."
  },
  {
    "name": "encryption_details",
    "type": "object",
    "description": "Encryption options that apply to clients connecting to cloud storage.",
    "children": [
      {
        "name": "sse_encryption_details",
        "type": "object",
        "description": "Server-Side Encryption properties for clients communicating with AWS s3.",
        "children": [
          {
            "name": "algorithm",
            "type": "string",
            "description": "Sets the value of the 'x-amz-server-side-encryption' header in S3 request."
          },
          {
            "name": "aws_kms_key_arn",
            "type": "string",
            "description": "Optional. The ARN of the SSE-KMS key used with the S3 location, when algorithm = \"SSE-KMS\". Sets the value of the 'x-amz-server-side-encryption-aws-kms-key-id' header."
          }
        ]
      }
    ]
  },
  {
    "name": "owner",
    "type": "string",
    "description": "Username of current owner of table."
  },
  {
    "name": "properties",
    "type": "object",
    "description": "A map of key-value properties attached to the securable."
  },
  {
    "name": "row_filter",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "function_name",
        "type": "string",
        "description": ""
      },
      {
        "name": "input_column_names",
        "type": "array",
        "description": "The list of table columns to be passed as input to the row filter function. The column types should match the types of the filter function arguments."
      }
    ]
  },
  {
    "name": "securable_kind_manifest",
    "type": "object",
    "description": "SecurableKindManifest of table, including capabilities the table has.",
    "children": [
      {
        "name": "assignable_privileges",
        "type": "array",
        "description": "Privileges that can be assigned to the securable."
      },
      {
        "name": "capabilities",
        "type": "array",
        "description": "A list of capabilities in the securable kind."
      },
      {
        "name": "options",
        "type": "array",
        "description": "Detailed specs of allowed options.",
        "children": [
          {
            "name": "allowed_values",
            "type": "array",
            "description": "For drop down / radio button selections, UI will want to know the possible input values, it can also be used by other option types to limit input selections."
          },
          {
            "name": "default_value",
            "type": "string",
            "description": "The default value of the option, for example, value '443' for 'port' option."
          },
          {
            "name": "description",
            "type": "string",
            "description": "A concise user facing description of what the input value of this option should look like."
          },
          {
            "name": "hint",
            "type": "string",
            "description": "The hint is used on the UI to suggest what the input value can possibly be like, for example: example.com for 'host' option. Unlike default value, it will not be applied automatically without user input."
          },
          {
            "name": "is_copiable",
            "type": "boolean",
            "description": "Indicates whether an option should be displayed with copy button on the UI."
          },
          {
            "name": "is_creatable",
            "type": "boolean",
            "description": "Indicates whether an option can be provided by users in the create/update path of an entity."
          },
          {
            "name": "is_hidden",
            "type": "boolean",
            "description": "Is the option value not user settable and is thus not shown on the UI."
          },
          {
            "name": "is_loggable",
            "type": "boolean",
            "description": "Specifies whether this option is safe to log, i.e. no sensitive information."
          },
          {
            "name": "is_required",
            "type": "boolean",
            "description": "Is the option required."
          },
          {
            "name": "is_secret",
            "type": "boolean",
            "description": "Is the option value considered secret and thus redacted on the UI."
          },
          {
            "name": "is_updatable",
            "type": "boolean",
            "description": "Is the option updatable by users."
          },
          {
            "name": "name",
            "type": "string",
            "description": "The unique name of the option."
          },
          {
            "name": "oauth_stage",
            "type": "string",
            "description": "Specifies when the option value is displayed on the UI within the OAuth flow."
          },
          {
            "name": "type",
            "type": "string",
            "description": "The type of the option."
          }
        ]
      },
      {
        "name": "securable_kind",
        "type": "string",
        "description": "Securable kind to get manifest of."
      },
      {
        "name": "securable_type",
        "type": "string",
        "description": "The type of Unity Catalog securable."
      }
    ]
  },
  {
    "name": "sql_path",
    "type": "string",
    "description": "List of schemes whose objects can be referenced without qualification."
  },
  {
    "name": "storage_location",
    "type": "string",
    "description": "Storage root URL for table (for **MANAGED**, **EXTERNAL** tables)."
  },
  {
    "name": "table_constraints",
    "type": "array",
    "description": "List of table constraints. Note: this field is not set in the output of the __listTables__ API.",
    "children": [
      {
        "name": "foreign_key_constraint",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "name",
            "type": "string",
            "description": ""
          },
          {
            "name": "child_columns",
            "type": "array",
            "description": "Column names for this constraint."
          },
          {
            "name": "parent_table",
            "type": "string",
            "description": "The full name of the parent constraint."
          },
          {
            "name": "parent_columns",
            "type": "array",
            "description": "Column names for this constraint."
          },
          {
            "name": "rely",
            "type": "boolean",
            "description": "True if the constraint is RELY, false or unset if NORELY."
          }
        ]
      },
      {
        "name": "named_table_constraint",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "name",
            "type": "string",
            "description": ""
          }
        ]
      },
      {
        "name": "primary_key_constraint",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "name",
            "type": "string",
            "description": ""
          },
          {
            "name": "child_columns",
            "type": "array",
            "description": "Column names for this constraint."
          },
          {
            "name": "rely",
            "type": "boolean",
            "description": "True if the constraint is RELY, false or unset if NORELY."
          },
          {
            "name": "timeseries_columns",
            "type": "array",
            "description": "Column names that represent a timeseries."
          }
        ]
      }
    ]
  },
  {
    "name": "table_type",
    "type": "string",
    "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details."
  },
  {
    "name": "updated_at",
    "type": "integer",
    "description": "Time at which this table was last modified, in epoch milliseconds."
  },
  {
    "name": "updated_by",
    "type": "string",
    "description": "Username of user who last modified the table."
  },
  {
    "name": "view_definition",
    "type": "string",
    "description": "View definition SQL (when __table_type__ is **VIEW**, **MATERIALIZED_VIEW**, or **STREAMING_TABLE**)"
  },
  {
    "name": "view_dependencies",
    "type": "object",
    "description": "View dependencies (when table_type == **VIEW** or **MATERIALIZED_VIEW**, **STREAMING_TABLE**) - when DependencyList is None, the dependency is not provided; - when DependencyList is an empty list, the dependency is provided but is empty; - when DependencyList is not an empty list, dependencies are provided and recorded. Note: this field is not set in the output of the __listTables__ API.",
    "children": [
      {
        "name": "dependencies",
        "type": "array",
        "description": "Array of dependencies.",
        "children": [
          {
            "name": "connection",
            "type": "object",
            "description": "A connection that is dependent on a SQL object.",
            "children": [
              {
                "name": "connection_name",
                "type": "string",
                "description": "Full name of the dependent connection, in the form of __connection_name__."
              }
            ]
          },
          {
            "name": "credential",
            "type": "object",
            "description": "A credential that is dependent on a SQL object.",
            "children": [
              {
                "name": "credential_name",
                "type": "string",
                "description": "Full name of the dependent credential, in the form of __credential_name__."
              }
            ]
          },
          {
            "name": "function",
            "type": "object",
            "description": "A function that is dependent on a SQL object.",
            "children": [
              {
                "name": "function_full_name",
                "type": "string",
                "description": "Full name of the dependent function, in the form of __catalog_name__.__schema_name__.__function_name__."
              }
            ]
          },
          {
            "name": "table",
            "type": "object",
            "description": "A table that is dependent on a SQL object.",
            "children": [
              {
                "name": "table_full_name",
                "type": "string",
                "description": "Full name of the dependent table, in the form of __catalog_name__.__schema_name__.__table_name__."
              }
            ]
          }
        ]
      }
    ]
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "name",
    "type": "string",
    "description": "Name of table, relative to parent schema."
  },
  {
    "name": "data_access_configuration_id",
    "type": "string",
    "description": "Unique ID of the Data Access Configuration to use with the table data."
  },
  {
    "name": "metastore_id",
    "type": "string",
    "description": "Unique identifier of parent metastore."
  },
  {
    "name": "pipeline_id",
    "type": "string",
    "description": "The pipeline ID of the table. Applicable for tables created by pipelines (Materialized View, Streaming Table, etc.)."
  },
  {
    "name": "table_id",
    "type": "string",
    "description": "The unique identifier of the table."
  },
  {
    "name": "catalog_name",
    "type": "string",
    "description": "Name of parent catalog."
  },
  {
    "name": "full_name",
    "type": "string",
    "description": "Full name of table, in form of __catalog_name__.__schema_name__.__table_name__"
  },
  {
    "name": "schema_name",
    "type": "string",
    "description": "Name of parent schema relative to its parent catalog."
  },
  {
    "name": "storage_credential_name",
    "type": "string",
    "description": "Name of the storage credential, when a storage credential is configured for use with this table."
  },
  {
    "name": "access_point",
    "type": "string",
    "description": ""
  },
  {
    "name": "browse_only",
    "type": "boolean",
    "description": "Indicates whether the principal is limited to retrieving metadata for the associated object through the BROWSE privilege when include_browse is enabled in the request."
  },
  {
    "name": "columns",
    "type": "array",
    "description": "The array of __ColumnInfo__ definitions of the table's columns.",
    "children": [
      {
        "name": "comment",
        "type": "string",
        "description": ""
      },
      {
        "name": "mask",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "function_name",
            "type": "string",
            "description": ""
          },
          {
            "name": "using_column_names",
            "type": "array",
            "description": "The list of additional table columns to be passed as input to the column mask function. The first arg of the mask function should be of the type of the column being masked and the types of the rest of the args should match the types of columns in 'using_column_names'."
          }
        ]
      },
      {
        "name": "name",
        "type": "string",
        "description": "Name of Column."
      },
      {
        "name": "nullable",
        "type": "boolean",
        "description": "Whether field may be Null (default: true)."
      },
      {
        "name": "partition_index",
        "type": "integer",
        "description": "Partition index for column."
      },
      {
        "name": "position",
        "type": "integer",
        "description": "Ordinal position of column (starting at position 0)."
      },
      {
        "name": "type_interval_type",
        "type": "string",
        "description": "Format of IntervalType."
      },
      {
        "name": "type_json",
        "type": "string",
        "description": "Full data type specification, JSON-serialized."
      },
      {
        "name": "type_name",
        "type": "string",
        "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details."
      },
      {
        "name": "type_precision",
        "type": "integer",
        "description": "Digits of precision; required for DecimalTypes."
      },
      {
        "name": "type_scale",
        "type": "integer",
        "description": "Digits to right of decimal; Required for DecimalTypes."
      },
      {
        "name": "type_text",
        "type": "string",
        "description": "Full data type specification as SQL/catalogString text."
      }
    ]
  },
  {
    "name": "comment",
    "type": "string",
    "description": "User-provided free-form text description."
  },
  {
    "name": "created_at",
    "type": "integer",
    "description": "Time at which this table was created, in epoch milliseconds."
  },
  {
    "name": "created_by",
    "type": "string",
    "description": "Username of table creator."
  },
  {
    "name": "data_source_format",
    "type": "string",
    "description": "Data source format"
  },
  {
    "name": "deleted_at",
    "type": "integer",
    "description": "Time at which this table was deleted, in epoch milliseconds. Field is omitted if table is not deleted."
  },
  {
    "name": "delta_runtime_properties_kvpairs",
    "type": "object",
    "description": "Information pertaining to current state of the delta table.",
    "children": [
      {
        "name": "delta_runtime_properties",
        "type": "object",
        "description": "A map of key-value properties attached to the securable."
      }
    ]
  },
  {
    "name": "effective_predictive_optimization_flag",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "value",
        "type": "string",
        "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details."
      },
      {
        "name": "inherited_from_name",
        "type": "string",
        "description": "The name of the object from which the flag was inherited. If there was no inheritance, this field is left blank."
      },
      {
        "name": "inherited_from_type",
        "type": "string",
        "description": "The type of the object from which the flag was inherited. If there was no inheritance, this field is left blank."
      }
    ]
  },
  {
    "name": "enable_predictive_optimization",
    "type": "string",
    "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details."
  },
  {
    "name": "encryption_details",
    "type": "object",
    "description": "Encryption options that apply to clients connecting to cloud storage.",
    "children": [
      {
        "name": "sse_encryption_details",
        "type": "object",
        "description": "Server-Side Encryption properties for clients communicating with AWS s3.",
        "children": [
          {
            "name": "algorithm",
            "type": "string",
            "description": "Sets the value of the 'x-amz-server-side-encryption' header in S3 request."
          },
          {
            "name": "aws_kms_key_arn",
            "type": "string",
            "description": "Optional. The ARN of the SSE-KMS key used with the S3 location, when algorithm = \"SSE-KMS\". Sets the value of the 'x-amz-server-side-encryption-aws-kms-key-id' header."
          }
        ]
      }
    ]
  },
  {
    "name": "owner",
    "type": "string",
    "description": "Username of current owner of table."
  },
  {
    "name": "properties",
    "type": "object",
    "description": "A map of key-value properties attached to the securable."
  },
  {
    "name": "row_filter",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "function_name",
        "type": "string",
        "description": ""
      },
      {
        "name": "input_column_names",
        "type": "array",
        "description": "The list of table columns to be passed as input to the row filter function. The column types should match the types of the filter function arguments."
      }
    ]
  },
  {
    "name": "securable_kind_manifest",
    "type": "object",
    "description": "SecurableKindManifest of table, including capabilities the table has.",
    "children": [
      {
        "name": "assignable_privileges",
        "type": "array",
        "description": "Privileges that can be assigned to the securable."
      },
      {
        "name": "capabilities",
        "type": "array",
        "description": "A list of capabilities in the securable kind."
      },
      {
        "name": "options",
        "type": "array",
        "description": "Detailed specs of allowed options.",
        "children": [
          {
            "name": "allowed_values",
            "type": "array",
            "description": "For drop down / radio button selections, UI will want to know the possible input values, it can also be used by other option types to limit input selections."
          },
          {
            "name": "default_value",
            "type": "string",
            "description": "The default value of the option, for example, value '443' for 'port' option."
          },
          {
            "name": "description",
            "type": "string",
            "description": "A concise user facing description of what the input value of this option should look like."
          },
          {
            "name": "hint",
            "type": "string",
            "description": "The hint is used on the UI to suggest what the input value can possibly be like, for example: example.com for 'host' option. Unlike default value, it will not be applied automatically without user input."
          },
          {
            "name": "is_copiable",
            "type": "boolean",
            "description": "Indicates whether an option should be displayed with copy button on the UI."
          },
          {
            "name": "is_creatable",
            "type": "boolean",
            "description": "Indicates whether an option can be provided by users in the create/update path of an entity."
          },
          {
            "name": "is_hidden",
            "type": "boolean",
            "description": "Is the option value not user settable and is thus not shown on the UI."
          },
          {
            "name": "is_loggable",
            "type": "boolean",
            "description": "Specifies whether this option is safe to log, i.e. no sensitive information."
          },
          {
            "name": "is_required",
            "type": "boolean",
            "description": "Is the option required."
          },
          {
            "name": "is_secret",
            "type": "boolean",
            "description": "Is the option value considered secret and thus redacted on the UI."
          },
          {
            "name": "is_updatable",
            "type": "boolean",
            "description": "Is the option updatable by users."
          },
          {
            "name": "name",
            "type": "string",
            "description": "The unique name of the option."
          },
          {
            "name": "oauth_stage",
            "type": "string",
            "description": "Specifies when the option value is displayed on the UI within the OAuth flow."
          },
          {
            "name": "type",
            "type": "string",
            "description": "The type of the option."
          }
        ]
      },
      {
        "name": "securable_kind",
        "type": "string",
        "description": "Securable kind to get manifest of."
      },
      {
        "name": "securable_type",
        "type": "string",
        "description": "The type of Unity Catalog securable."
      }
    ]
  },
  {
    "name": "sql_path",
    "type": "string",
    "description": "List of schemes whose objects can be referenced without qualification."
  },
  {
    "name": "storage_location",
    "type": "string",
    "description": "Storage root URL for table (for **MANAGED**, **EXTERNAL** tables)."
  },
  {
    "name": "table_constraints",
    "type": "array",
    "description": "List of table constraints. Note: this field is not set in the output of the __listTables__ API.",
    "children": [
      {
        "name": "foreign_key_constraint",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "name",
            "type": "string",
            "description": ""
          },
          {
            "name": "child_columns",
            "type": "array",
            "description": "Column names for this constraint."
          },
          {
            "name": "parent_table",
            "type": "string",
            "description": "The full name of the parent constraint."
          },
          {
            "name": "parent_columns",
            "type": "array",
            "description": "Column names for this constraint."
          },
          {
            "name": "rely",
            "type": "boolean",
            "description": "True if the constraint is RELY, false or unset if NORELY."
          }
        ]
      },
      {
        "name": "named_table_constraint",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "name",
            "type": "string",
            "description": ""
          }
        ]
      },
      {
        "name": "primary_key_constraint",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "name",
            "type": "string",
            "description": ""
          },
          {
            "name": "child_columns",
            "type": "array",
            "description": "Column names for this constraint."
          },
          {
            "name": "rely",
            "type": "boolean",
            "description": "True if the constraint is RELY, false or unset if NORELY."
          },
          {
            "name": "timeseries_columns",
            "type": "array",
            "description": "Column names that represent a timeseries."
          }
        ]
      }
    ]
  },
  {
    "name": "table_type",
    "type": "string",
    "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details."
  },
  {
    "name": "updated_at",
    "type": "integer",
    "description": "Time at which this table was last modified, in epoch milliseconds."
  },
  {
    "name": "updated_by",
    "type": "string",
    "description": "Username of user who last modified the table."
  },
  {
    "name": "view_definition",
    "type": "string",
    "description": "View definition SQL (when __table_type__ is **VIEW**, **MATERIALIZED_VIEW**, or **STREAMING_TABLE**)"
  },
  {
    "name": "view_dependencies",
    "type": "object",
    "description": "View dependencies (when table_type == **VIEW** or **MATERIALIZED_VIEW**, **STREAMING_TABLE**) - when DependencyList is None, the dependency is not provided; - when DependencyList is an empty list, the dependency is provided but is empty; - when DependencyList is not an empty list, dependencies are provided and recorded. Note: this field is not set in the output of the __listTables__ API.",
    "children": [
      {
        "name": "dependencies",
        "type": "array",
        "description": "Array of dependencies.",
        "children": [
          {
            "name": "connection",
            "type": "object",
            "description": "A connection that is dependent on a SQL object.",
            "children": [
              {
                "name": "connection_name",
                "type": "string",
                "description": "Full name of the dependent connection, in the form of __connection_name__."
              }
            ]
          },
          {
            "name": "credential",
            "type": "object",
            "description": "A credential that is dependent on a SQL object.",
            "children": [
              {
                "name": "credential_name",
                "type": "string",
                "description": "Full name of the dependent credential, in the form of __credential_name__."
              }
            ]
          },
          {
            "name": "function",
            "type": "object",
            "description": "A function that is dependent on a SQL object.",
            "children": [
              {
                "name": "function_full_name",
                "type": "string",
                "description": "Full name of the dependent function, in the form of __catalog_name__.__schema_name__.__function_name__."
              }
            ]
          },
          {
            "name": "table",
            "type": "object",
            "description": "A table that is dependent on a SQL object.",
            "children": [
              {
                "name": "table_full_name",
                "type": "string",
                "description": "Full name of the dependent table, in the form of __catalog_name__.__schema_name__.__table_name__."
              }
            ]
          }
        ]
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
    <td><a href="#parameter-full_name"><code>full_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-include_browse"><code>include_browse</code></a>, <a href="#parameter-include_delta_metadata"><code>include_delta_metadata</code></a>, <a href="#parameter-include_manifest_capabilities"><code>include_manifest_capabilities</code></a></td>
    <td>Gets a table from the metastore for a specific catalog and schema. The caller must satisfy one of the<br />following requirements: * Be a metastore admin * Be the owner of the parent catalog * Be the owner of<br />the parent schema and have the **USE_CATALOG** privilege on the parent catalog * Have the<br />**USE_CATALOG** privilege on the parent catalog and the **USE_SCHEMA** privilege on the parent schema,<br />and either be the table owner or have the **SELECT** privilege on the table.<br /><br />:param full_name: str<br />  Full name of the table.<br />:param include_browse: bool (optional)<br />  Whether to include tables in the response for which the principal can only access selective metadata<br />  for.<br />:param include_delta_metadata: bool (optional)<br />  Whether delta metadata should be included in the response.<br />:param include_manifest_capabilities: bool (optional)<br />  Whether to include a manifest containing table capabilities in the response.<br /><br />:returns: :class:`TableInfo`</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-catalog_name"><code>catalog_name</code></a>, <a href="#parameter-schema_name"><code>schema_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-include_browse"><code>include_browse</code></a>, <a href="#parameter-include_manifest_capabilities"><code>include_manifest_capabilities</code></a>, <a href="#parameter-max_results"><code>max_results</code></a>, <a href="#parameter-omit_columns"><code>omit_columns</code></a>, <a href="#parameter-omit_properties"><code>omit_properties</code></a>, <a href="#parameter-omit_username"><code>omit_username</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>Gets an array of all tables for the current metastore under the parent catalog and schema. The caller<br />must be a metastore admin or an owner of (or have the **SELECT** privilege on) the table. For the<br />latter case, the caller must also be the owner or have the **USE_CATALOG** privilege on the parent<br />catalog and the **USE_SCHEMA** privilege on the parent schema. There is no guarantee of a specific<br />ordering of the elements in the array.<br /><br />NOTE: **view_dependencies** and **table_constraints** are not returned by ListTables queries.<br /><br />NOTE: we recommend using max_results=0 to use the paginated version of this API. Unpaginated calls<br />will be deprecated soon.<br /><br />PAGINATION BEHAVIOR: When using pagination (max_results &gt;= 0), a page may contain zero results while<br />still providing a next_page_token. Clients must continue reading pages until next_page_token is<br />absent, which is the only indication that the end of results has been reached.<br /><br />:param catalog_name: str<br />  Name of parent catalog for tables of interest.<br />:param schema_name: str<br />  Parent schema of tables.<br />:param include_browse: bool (optional)<br />  Whether to include tables in the response for which the principal can only access selective metadata<br />  for.<br />:param include_manifest_capabilities: bool (optional)<br />  Whether to include a manifest containing table capabilities in the response.<br />:param max_results: int (optional)<br />  Maximum number of tables to return. If not set, all the tables are returned (not recommended). -<br />  when set to a value greater than 0, the page length is the minimum of this value and a server<br />  configured value; - when set to 0, the page length is set to a server configured value<br />  (recommended); - when set to a value less than 0, an invalid parameter error is returned;<br />:param omit_columns: bool (optional)<br />  Whether to omit the columns of the table from the response or not.<br />:param omit_properties: bool (optional)<br />  Whether to omit the properties of the table from the response or not.<br />:param omit_username: bool (optional)<br />  Whether to omit the username of the table (e.g. owner, updated_by, created_by) from the response or<br />  not.<br />:param page_token: str (optional)<br />  Opaque token to send for the next page of results (pagination).<br /><br />:returns: Iterator over :class:`TableInfo`</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-data__name"><code>data__name</code></a>, <a href="#parameter-data__catalog_name"><code>data__catalog_name</code></a>, <a href="#parameter-data__schema_name"><code>data__schema_name</code></a>, <a href="#parameter-data__table_type"><code>data__table_type</code></a>, <a href="#parameter-data__data_source_format"><code>data__data_source_format</code></a>, <a href="#parameter-data__storage_location"><code>data__storage_location</code></a></td>
    <td></td>
    <td>Creates a new table in the specified catalog and schema.<br /><br />To create an external delta table, the caller must have the **EXTERNAL_USE_SCHEMA** privilege on the<br />parent schema and the **EXTERNAL_USE_LOCATION** privilege on the external location. These privileges<br />must always be granted explicitly, and cannot be inherited through ownership or **ALL_PRIVILEGES**.<br /><br />Standard UC permissions needed to create tables still apply: **USE_CATALOG** on the parent catalog (or<br />ownership of the parent catalog), **CREATE_TABLE** and **USE_SCHEMA** on the parent schema (or<br />ownership of the parent schema), and **CREATE_EXTERNAL_TABLE** on external location.<br /><br />The **columns** field needs to be in a Spark compatible format, so we recommend you use Spark to<br />create these tables. The API itself does not validate the correctness of the column spec. If the spec<br />is not Spark compatible, the tables may not be readable by Databricks Runtime.<br /><br />NOTE: The Create Table API for external clients only supports creating **external delta tables**. The<br />values shown in the respective enums are all values supported by Databricks, however for this specific<br />Create Table API, only **table_type** **EXTERNAL** and **data_source_format** **DELTA** are supported.<br />Additionally, column masks are not supported when creating tables through this API.<br /><br />:param name: str<br />  Name of table, relative to parent schema.<br />:param catalog_name: str<br />  Name of parent catalog.<br />:param schema_name: str<br />  Name of parent schema relative to its parent catalog.<br />:param table_type: :class:`TableType`<br />:param data_source_format: :class:`DataSourceFormat`<br />:param storage_location: str<br />  Storage root URL for table (for **MANAGED**, **EXTERNAL** tables).<br />:param columns: List[:class:`ColumnInfo`] (optional)<br />  The array of __ColumnInfo__ definitions of the table's columns.<br />:param properties: Dict[str,str] (optional)<br />  A map of key-value properties attached to the securable.<br /><br />:returns: :class:`TableInfo`</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-full_name"><code>full_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Change the owner of the table. The caller must be the owner of the parent catalog, have the<br />**USE_CATALOG** privilege on the parent catalog and be the owner of the parent schema, or be the owner<br />of the table and have the **USE_CATALOG** privilege on the parent catalog and the **USE_SCHEMA**<br />privilege on the parent schema.<br /><br />:param full_name: str<br />  Full name of the table.<br />:param owner: str (optional)<br />  Username of current owner of table.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-full_name"><code>full_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Deletes a table from the specified parent catalog and schema. The caller must be the owner of the<br />parent catalog, have the **USE_CATALOG** privilege on the parent catalog and be the owner of the<br />parent schema, or be the owner of the table and have the **USE_CATALOG** privilege on the parent<br />catalog and the **USE_SCHEMA** privilege on the parent schema.<br /><br />:param full_name: str<br />  Full name of the table.</td>
</tr>
<tr>
    <td><a href="#exists"><CopyableCode code="exists" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-full_name"><code>full_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Gets if a table exists in the metastore for a specific catalog and schema. The caller must satisfy one<br />of the following requirements: * Be a metastore admin * Be the owner of the parent catalog * Be the<br />owner of the parent schema and have the **USE_CATALOG** privilege on the parent catalog * Have the<br />**USE_CATALOG** privilege on the parent catalog and the **USE_SCHEMA** privilege on the parent schema,<br />and either be the table owner or have the **SELECT** privilege on the table. * Have **BROWSE**<br />privilege on the parent catalog * Have **BROWSE** privilege on the parent schema<br /><br />:param full_name: str<br />  Full name of the table.<br /><br />:returns: :class:`TableExistsResponse`</td>
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
<tr id="parameter-catalog_name">
    <td><CopyableCode code="catalog_name" /></td>
    <td><code>string</code></td>
    <td>Name of parent catalog for tables of interest.</td>
</tr>
<tr id="parameter-deployment_name">
    <td><CopyableCode code="deployment_name" /></td>
    <td><code>string</code></td>
    <td>The Databricks Workspace Deployment Name (default: dbc-abcd0123-a1bc)</td>
</tr>
<tr id="parameter-full_name">
    <td><CopyableCode code="full_name" /></td>
    <td><code>string</code></td>
    <td>Full name of the table.</td>
</tr>
<tr id="parameter-schema_name">
    <td><CopyableCode code="schema_name" /></td>
    <td><code>string</code></td>
    <td>Parent schema of tables.</td>
</tr>
<tr id="parameter-include_browse">
    <td><CopyableCode code="include_browse" /></td>
    <td><code>string</code></td>
    <td>Whether to include tables in the response for which the principal can only access selective metadata for.</td>
</tr>
<tr id="parameter-include_delta_metadata">
    <td><CopyableCode code="include_delta_metadata" /></td>
    <td><code>string</code></td>
    <td>Whether delta metadata should be included in the response.</td>
</tr>
<tr id="parameter-include_manifest_capabilities">
    <td><CopyableCode code="include_manifest_capabilities" /></td>
    <td><code>string</code></td>
    <td>Whether to include a manifest containing table capabilities in the response.</td>
</tr>
<tr id="parameter-max_results">
    <td><CopyableCode code="max_results" /></td>
    <td><code>string</code></td>
    <td>Maximum number of tables to return. If not set, all the tables are returned (not recommended). - when set to a value greater than 0, the page length is the minimum of this value and a server configured value; - when set to 0, the page length is set to a server configured value (recommended); - when set to a value less than 0, an invalid parameter error is returned;</td>
</tr>
<tr id="parameter-omit_columns">
    <td><CopyableCode code="omit_columns" /></td>
    <td><code>string</code></td>
    <td>Whether to omit the columns of the table from the response or not.</td>
</tr>
<tr id="parameter-omit_properties">
    <td><CopyableCode code="omit_properties" /></td>
    <td><code>string</code></td>
    <td>Whether to omit the properties of the table from the response or not.</td>
</tr>
<tr id="parameter-omit_username">
    <td><CopyableCode code="omit_username" /></td>
    <td><code>string</code></td>
    <td>Whether to omit the username of the table (e.g. owner, updated_by, created_by) from the response or not.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>Opaque token to send for the next page of results (pagination).</td>
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

Gets a table from the metastore for a specific catalog and schema. The caller must satisfy one of the<br />following requirements: * Be a metastore admin * Be the owner of the parent catalog * Be the owner of<br />the parent schema and have the **USE_CATALOG** privilege on the parent catalog * Have the<br />**USE_CATALOG** privilege on the parent catalog and the **USE_SCHEMA** privilege on the parent schema,<br />and either be the table owner or have the **SELECT** privilege on the table.<br /><br />:param full_name: str<br />  Full name of the table.<br />:param include_browse: bool (optional)<br />  Whether to include tables in the response for which the principal can only access selective metadata<br />  for.<br />:param include_delta_metadata: bool (optional)<br />  Whether delta metadata should be included in the response.<br />:param include_manifest_capabilities: bool (optional)<br />  Whether to include a manifest containing table capabilities in the response.<br /><br />:returns: :class:`TableInfo`

```sql
SELECT
name,
data_access_configuration_id,
metastore_id,
pipeline_id,
table_id,
catalog_name,
full_name,
schema_name,
storage_credential_name,
access_point,
browse_only,
columns,
comment,
created_at,
created_by,
data_source_format,
deleted_at,
delta_runtime_properties_kvpairs,
effective_predictive_optimization_flag,
enable_predictive_optimization,
encryption_details,
owner,
properties,
row_filter,
securable_kind_manifest,
sql_path,
storage_location,
table_constraints,
table_type,
updated_at,
updated_by,
view_definition,
view_dependencies
FROM databricks_workspace.catalog.tables
WHERE full_name = '{{ full_name }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND include_browse = '{{ include_browse }}'
AND include_delta_metadata = '{{ include_delta_metadata }}'
AND include_manifest_capabilities = '{{ include_manifest_capabilities }}'
;
```
</TabItem>
<TabItem value="list">

Gets an array of all tables for the current metastore under the parent catalog and schema. The caller<br />must be a metastore admin or an owner of (or have the **SELECT** privilege on) the table. For the<br />latter case, the caller must also be the owner or have the **USE_CATALOG** privilege on the parent<br />catalog and the **USE_SCHEMA** privilege on the parent schema. There is no guarantee of a specific<br />ordering of the elements in the array.<br /><br />NOTE: **view_dependencies** and **table_constraints** are not returned by ListTables queries.<br /><br />NOTE: we recommend using max_results=0 to use the paginated version of this API. Unpaginated calls<br />will be deprecated soon.<br /><br />PAGINATION BEHAVIOR: When using pagination (max_results &gt;= 0), a page may contain zero results while<br />still providing a next_page_token. Clients must continue reading pages until next_page_token is<br />absent, which is the only indication that the end of results has been reached.<br /><br />:param catalog_name: str<br />  Name of parent catalog for tables of interest.<br />:param schema_name: str<br />  Parent schema of tables.<br />:param include_browse: bool (optional)<br />  Whether to include tables in the response for which the principal can only access selective metadata<br />  for.<br />:param include_manifest_capabilities: bool (optional)<br />  Whether to include a manifest containing table capabilities in the response.<br />:param max_results: int (optional)<br />  Maximum number of tables to return. If not set, all the tables are returned (not recommended). -<br />  when set to a value greater than 0, the page length is the minimum of this value and a server<br />  configured value; - when set to 0, the page length is set to a server configured value<br />  (recommended); - when set to a value less than 0, an invalid parameter error is returned;<br />:param omit_columns: bool (optional)<br />  Whether to omit the columns of the table from the response or not.<br />:param omit_properties: bool (optional)<br />  Whether to omit the properties of the table from the response or not.<br />:param omit_username: bool (optional)<br />  Whether to omit the username of the table (e.g. owner, updated_by, created_by) from the response or<br />  not.<br />:param page_token: str (optional)<br />  Opaque token to send for the next page of results (pagination).<br /><br />:returns: Iterator over :class:`TableInfo`

```sql
SELECT
name,
data_access_configuration_id,
metastore_id,
pipeline_id,
table_id,
catalog_name,
full_name,
schema_name,
storage_credential_name,
access_point,
browse_only,
columns,
comment,
created_at,
created_by,
data_source_format,
deleted_at,
delta_runtime_properties_kvpairs,
effective_predictive_optimization_flag,
enable_predictive_optimization,
encryption_details,
owner,
properties,
row_filter,
securable_kind_manifest,
sql_path,
storage_location,
table_constraints,
table_type,
updated_at,
updated_by,
view_definition,
view_dependencies
FROM databricks_workspace.catalog.tables
WHERE catalog_name = '{{ catalog_name }}' -- required
AND schema_name = '{{ schema_name }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND include_browse = '{{ include_browse }}'
AND include_manifest_capabilities = '{{ include_manifest_capabilities }}'
AND max_results = '{{ max_results }}'
AND omit_columns = '{{ omit_columns }}'
AND omit_properties = '{{ omit_properties }}'
AND omit_username = '{{ omit_username }}'
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

Creates a new table in the specified catalog and schema.<br /><br />To create an external delta table, the caller must have the **EXTERNAL_USE_SCHEMA** privilege on the<br />parent schema and the **EXTERNAL_USE_LOCATION** privilege on the external location. These privileges<br />must always be granted explicitly, and cannot be inherited through ownership or **ALL_PRIVILEGES**.<br /><br />Standard UC permissions needed to create tables still apply: **USE_CATALOG** on the parent catalog (or<br />ownership of the parent catalog), **CREATE_TABLE** and **USE_SCHEMA** on the parent schema (or<br />ownership of the parent schema), and **CREATE_EXTERNAL_TABLE** on external location.<br /><br />The **columns** field needs to be in a Spark compatible format, so we recommend you use Spark to<br />create these tables. The API itself does not validate the correctness of the column spec. If the spec<br />is not Spark compatible, the tables may not be readable by Databricks Runtime.<br /><br />NOTE: The Create Table API for external clients only supports creating **external delta tables**. The<br />values shown in the respective enums are all values supported by Databricks, however for this specific<br />Create Table API, only **table_type** **EXTERNAL** and **data_source_format** **DELTA** are supported.<br />Additionally, column masks are not supported when creating tables through this API.<br /><br />:param name: str<br />  Name of table, relative to parent schema.<br />:param catalog_name: str<br />  Name of parent catalog.<br />:param schema_name: str<br />  Name of parent schema relative to its parent catalog.<br />:param table_type: :class:`TableType`<br />:param data_source_format: :class:`DataSourceFormat`<br />:param storage_location: str<br />  Storage root URL for table (for **MANAGED**, **EXTERNAL** tables).<br />:param columns: List[:class:`ColumnInfo`] (optional)<br />  The array of __ColumnInfo__ definitions of the table's columns.<br />:param properties: Dict[str,str] (optional)<br />  A map of key-value properties attached to the securable.<br /><br />:returns: :class:`TableInfo`

```sql
INSERT INTO databricks_workspace.catalog.tables (
data__name,
data__catalog_name,
data__schema_name,
data__table_type,
data__data_source_format,
data__storage_location,
data__columns,
data__properties,
deployment_name
)
SELECT 
'{{ name }}' /* required */,
'{{ catalog_name }}' /* required */,
'{{ schema_name }}' /* required */,
'{{ table_type }}' /* required */,
'{{ data_source_format }}' /* required */,
'{{ storage_location }}' /* required */,
'{{ columns }}',
'{{ properties }}',
'{{ deployment_name }}'
RETURNING
name,
data_access_configuration_id,
metastore_id,
pipeline_id,
table_id,
catalog_name,
full_name,
schema_name,
storage_credential_name,
access_point,
browse_only,
columns,
comment,
created_at,
created_by,
data_source_format,
deleted_at,
delta_runtime_properties_kvpairs,
effective_predictive_optimization_flag,
enable_predictive_optimization,
encryption_details,
owner,
properties,
row_filter,
securable_kind_manifest,
sql_path,
storage_location,
table_constraints,
table_type,
updated_at,
updated_by,
view_definition,
view_dependencies
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: tables
  props:
    - name: deployment_name
      value: string
      description: Required parameter for the tables resource.
    - name: name
      value: string
      description: |
        Name of table, relative to parent schema.
    - name: catalog_name
      value: string
      description: |
        Name of parent catalog.
    - name: schema_name
      value: string
      description: |
        Name of parent schema relative to its parent catalog.
    - name: table_type
      value: string
      description: |
        :param data_source_format: :class:`DataSourceFormat`
    - name: data_source_format
      value: string
    - name: storage_location
      value: string
      description: |
        Storage root URL for table (for **MANAGED**, **EXTERNAL** tables).
    - name: columns
      value: string
      description: |
        The array of __ColumnInfo__ definitions of the table's columns.
    - name: properties
      value: string
      description: |
        A map of key-value properties attached to the securable.
```
</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' }
    ]}
>
<TabItem value="update">

Change the owner of the table. The caller must be the owner of the parent catalog, have the<br />**USE_CATALOG** privilege on the parent catalog and be the owner of the parent schema, or be the owner<br />of the table and have the **USE_CATALOG** privilege on the parent catalog and the **USE_SCHEMA**<br />privilege on the parent schema.<br /><br />:param full_name: str<br />  Full name of the table.<br />:param owner: str (optional)<br />  Username of current owner of table.

```sql
UPDATE databricks_workspace.catalog.tables
SET 
data__owner = '{{ owner }}'
WHERE 
full_name = '{{ full_name }}' --required
AND deployment_name = '{{ deployment_name }}' --required;
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

Deletes a table from the specified parent catalog and schema. The caller must be the owner of the<br />parent catalog, have the **USE_CATALOG** privilege on the parent catalog and be the owner of the<br />parent schema, or be the owner of the table and have the **USE_CATALOG** privilege on the parent<br />catalog and the **USE_SCHEMA** privilege on the parent schema.<br /><br />:param full_name: str<br />  Full name of the table.

```sql
DELETE FROM databricks_workspace.catalog.tables
WHERE full_name = '{{ full_name }}' --required
AND deployment_name = '{{ deployment_name }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="exists"
    values={[
        { label: 'exists', value: 'exists' }
    ]}
>
<TabItem value="exists">

Gets if a table exists in the metastore for a specific catalog and schema. The caller must satisfy one<br />of the following requirements: * Be a metastore admin * Be the owner of the parent catalog * Be the<br />owner of the parent schema and have the **USE_CATALOG** privilege on the parent catalog * Have the<br />**USE_CATALOG** privilege on the parent catalog and the **USE_SCHEMA** privilege on the parent schema,<br />and either be the table owner or have the **SELECT** privilege on the table. * Have **BROWSE**<br />privilege on the parent catalog * Have **BROWSE** privilege on the parent schema<br /><br />:param full_name: str<br />  Full name of the table.<br /><br />:returns: :class:`TableExistsResponse`

```sql
EXEC databricks_workspace.catalog.tables.exists 
@full_name='{{ full_name }}' --required, 
@deployment_name='{{ deployment_name }}' --required
;
```
</TabItem>
</Tabs>
