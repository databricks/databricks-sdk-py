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
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import SchemaTable from '@site/src/components/SchemaTable/SchemaTable';

Creates, updates, deletes, gets or lists a <code>tables</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="tables" /></td></tr>
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
        "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (ARRAY, BINARY, BOOLEAN, BYTE, CHAR, DATE, DECIMAL, DOUBLE, FLOAT, GEOGRAPHY, GEOMETRY, INT, INTERVAL, LONG, MAP, NULL, SHORT, STRING, STRUCT, TABLE_TYPE, TIMESTAMP, TIMESTAMP_NTZ, USER_DEFINED_TYPE, VARIANT)"
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
    "description": "Data source format (AVRO, BIGQUERY_FORMAT, CSV, DATABRICKS_FORMAT, DATABRICKS_ROW_STORE_FORMAT, DELTA, DELTASHARING, DELTA_UNIFORM_HUDI, DELTA_UNIFORM_ICEBERG, HIVE, ICEBERG, JSON, MONGODB_FORMAT, MYSQL_FORMAT, NETSUITE_FORMAT, ORACLE_FORMAT, ORC, PARQUET, POSTGRESQL_FORMAT, REDSHIFT_FORMAT, SALESFORCE_DATA_CLOUD_FORMAT, SALESFORCE_FORMAT, SNOWFLAKE_FORMAT, SQLDW_FORMAT, SQLSERVER_FORMAT, TERADATA_FORMAT, TEXT, UNITY_CATALOG, VECTOR_INDEX_FORMAT, WORKDAY_RAAS_FORMAT)"
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
        "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (DISABLE, ENABLE, INHERIT)"
      },
      {
        "name": "inherited_from_name",
        "type": "string",
        "description": "The name of the object from which the flag was inherited. If there was no inheritance, this field is left blank."
      },
      {
        "name": "inherited_from_type",
        "type": "string",
        "description": "The type of the object from which the flag was inherited. If there was no inheritance, this field is left blank. (CATALOG, SCHEMA)"
      }
    ]
  },
  {
    "name": "enable_predictive_optimization",
    "type": "string",
    "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (DISABLE, ENABLE, INHERIT)"
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
            "description": "Sets the value of the 'x-amz-server-side-encryption' header in S3 request. (AWS_SSE_KMS, AWS_SSE_S3)"
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
            "description": "Specifies when the option value is displayed on the UI within the OAuth flow. (BEFORE_ACCESS_TOKEN, BEFORE_AUTHORIZATION_CODE)"
          },
          {
            "name": "type",
            "type": "string",
            "description": "The type of the option. (OPTION_BIGINT, OPTION_BOOLEAN, OPTION_ENUM, OPTION_MULTILINE_STRING, OPTION_NUMBER, OPTION_SERVICE_CREDENTIAL, OPTION_STRING)"
          }
        ]
      },
      {
        "name": "securable_kind",
        "type": "string",
        "description": "Securable kind to get manifest of. (TABLE_DB_STORAGE, TABLE_DELTA, TABLE_DELTASHARING, TABLE_DELTASHARING_MUTABLE, TABLE_DELTASHARING_OPEN_DIR_BASED, TABLE_DELTA_EXTERNAL, TABLE_DELTA_ICEBERG_DELTASHARING, TABLE_DELTA_ICEBERG_MANAGED, TABLE_DELTA_UNIFORM_HUDI_EXTERNAL, TABLE_DELTA_UNIFORM_ICEBERG_EXTERNAL, TABLE_DELTA_UNIFORM_ICEBERG_FOREIGN_DELTASHARING, TABLE_DELTA_UNIFORM_ICEBERG_FOREIGN_HIVE_METASTORE_EXTERNAL, TABLE_DELTA_UNIFORM_ICEBERG_FOREIGN_HIVE_METASTORE_MANAGED, TABLE_DELTA_UNIFORM_ICEBERG_FOREIGN_SNOWFLAKE, TABLE_EXTERNAL, TABLE_FEATURE_STORE, TABLE_FEATURE_STORE_EXTERNAL, TABLE_FOREIGN_BIGQUERY, TABLE_FOREIGN_DATABRICKS, TABLE_FOREIGN_DELTASHARING, TABLE_FOREIGN_HIVE_METASTORE, TABLE_FOREIGN_HIVE_METASTORE_DBFS_EXTERNAL, TABLE_FOREIGN_HIVE_METASTORE_DBFS_MANAGED, TABLE_FOREIGN_HIVE_METASTORE_DBFS_SHALLOW_CLONE_EXTERNAL, TABLE_FOREIGN_HIVE_METASTORE_DBFS_SHALLOW_CLONE_MANAGED, TABLE_FOREIGN_HIVE_METASTORE_DBFS_VIEW, TABLE_FOREIGN_HIVE_METASTORE_EXTERNAL, TABLE_FOREIGN_HIVE_METASTORE_MANAGED, TABLE_FOREIGN_HIVE_METASTORE_SHALLOW_CLONE_EXTERNAL, TABLE_FOREIGN_HIVE_METASTORE_SHALLOW_CLONE_MANAGED, TABLE_FOREIGN_HIVE_METASTORE_VIEW, TABLE_FOREIGN_MONGODB, TABLE_FOREIGN_MYSQL, TABLE_FOREIGN_NETSUITE, TABLE_FOREIGN_ORACLE, TABLE_FOREIGN_POSTGRESQL, TABLE_FOREIGN_REDSHIFT, TABLE_FOREIGN_SALESFORCE, TABLE_FOREIGN_SALESFORCE_DATA_CLOUD, TABLE_FOREIGN_SALESFORCE_DATA_CLOUD_FILE_SHARING, TABLE_FOREIGN_SALESFORCE_DATA_CLOUD_FILE_SHARING_VIEW, TABLE_FOREIGN_SNOWFLAKE, TABLE_FOREIGN_SQLDW, TABLE_FOREIGN_SQLSERVER, TABLE_FOREIGN_TERADATA, TABLE_FOREIGN_WORKDAY_RAAS, TABLE_ICEBERG_UNIFORM_MANAGED, TABLE_INTERNAL, TABLE_MANAGED_POSTGRESQL, TABLE_MATERIALIZED_VIEW, TABLE_MATERIALIZED_VIEW_DELTASHARING, TABLE_METRIC_VIEW, TABLE_METRIC_VIEW_DELTASHARING, TABLE_ONLINE_VECTOR_INDEX_DIRECT, TABLE_ONLINE_VECTOR_INDEX_REPLICA, TABLE_ONLINE_VIEW, TABLE_STANDARD, TABLE_STREAMING_LIVE_TABLE, TABLE_STREAMING_LIVE_TABLE_DELTASHARING, TABLE_SYSTEM, TABLE_SYSTEM_DELTASHARING, TABLE_VIEW, TABLE_VIEW_DELTASHARING)"
      },
      {
        "name": "securable_type",
        "type": "string",
        "description": "The type of Unity Catalog securable. (CATALOG, CLEAN_ROOM, CONNECTION, CREDENTIAL, EXTERNAL_LOCATION, EXTERNAL_METADATA, FUNCTION, METASTORE, PIPELINE, PROVIDER, RECIPIENT, SCHEMA, SHARE, STAGING_TABLE, STORAGE_CREDENTIAL, TABLE, VOLUME)"
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
    "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (EXTERNAL, EXTERNAL_SHALLOW_CLONE, FOREIGN, MANAGED, MANAGED_SHALLOW_CLONE, MATERIALIZED_VIEW, METRIC_VIEW, STREAMING_TABLE, VIEW)"
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
        "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (ARRAY, BINARY, BOOLEAN, BYTE, CHAR, DATE, DECIMAL, DOUBLE, FLOAT, GEOGRAPHY, GEOMETRY, INT, INTERVAL, LONG, MAP, NULL, SHORT, STRING, STRUCT, TABLE_TYPE, TIMESTAMP, TIMESTAMP_NTZ, USER_DEFINED_TYPE, VARIANT)"
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
    "description": "Data source format (AVRO, BIGQUERY_FORMAT, CSV, DATABRICKS_FORMAT, DATABRICKS_ROW_STORE_FORMAT, DELTA, DELTASHARING, DELTA_UNIFORM_HUDI, DELTA_UNIFORM_ICEBERG, HIVE, ICEBERG, JSON, MONGODB_FORMAT, MYSQL_FORMAT, NETSUITE_FORMAT, ORACLE_FORMAT, ORC, PARQUET, POSTGRESQL_FORMAT, REDSHIFT_FORMAT, SALESFORCE_DATA_CLOUD_FORMAT, SALESFORCE_FORMAT, SNOWFLAKE_FORMAT, SQLDW_FORMAT, SQLSERVER_FORMAT, TERADATA_FORMAT, TEXT, UNITY_CATALOG, VECTOR_INDEX_FORMAT, WORKDAY_RAAS_FORMAT)"
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
        "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (DISABLE, ENABLE, INHERIT)"
      },
      {
        "name": "inherited_from_name",
        "type": "string",
        "description": "The name of the object from which the flag was inherited. If there was no inheritance, this field is left blank."
      },
      {
        "name": "inherited_from_type",
        "type": "string",
        "description": "The type of the object from which the flag was inherited. If there was no inheritance, this field is left blank. (CATALOG, SCHEMA)"
      }
    ]
  },
  {
    "name": "enable_predictive_optimization",
    "type": "string",
    "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (DISABLE, ENABLE, INHERIT)"
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
            "description": "Sets the value of the 'x-amz-server-side-encryption' header in S3 request. (AWS_SSE_KMS, AWS_SSE_S3)"
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
            "description": "Specifies when the option value is displayed on the UI within the OAuth flow. (BEFORE_ACCESS_TOKEN, BEFORE_AUTHORIZATION_CODE)"
          },
          {
            "name": "type",
            "type": "string",
            "description": "The type of the option. (OPTION_BIGINT, OPTION_BOOLEAN, OPTION_ENUM, OPTION_MULTILINE_STRING, OPTION_NUMBER, OPTION_SERVICE_CREDENTIAL, OPTION_STRING)"
          }
        ]
      },
      {
        "name": "securable_kind",
        "type": "string",
        "description": "Securable kind to get manifest of. (TABLE_DB_STORAGE, TABLE_DELTA, TABLE_DELTASHARING, TABLE_DELTASHARING_MUTABLE, TABLE_DELTASHARING_OPEN_DIR_BASED, TABLE_DELTA_EXTERNAL, TABLE_DELTA_ICEBERG_DELTASHARING, TABLE_DELTA_ICEBERG_MANAGED, TABLE_DELTA_UNIFORM_HUDI_EXTERNAL, TABLE_DELTA_UNIFORM_ICEBERG_EXTERNAL, TABLE_DELTA_UNIFORM_ICEBERG_FOREIGN_DELTASHARING, TABLE_DELTA_UNIFORM_ICEBERG_FOREIGN_HIVE_METASTORE_EXTERNAL, TABLE_DELTA_UNIFORM_ICEBERG_FOREIGN_HIVE_METASTORE_MANAGED, TABLE_DELTA_UNIFORM_ICEBERG_FOREIGN_SNOWFLAKE, TABLE_EXTERNAL, TABLE_FEATURE_STORE, TABLE_FEATURE_STORE_EXTERNAL, TABLE_FOREIGN_BIGQUERY, TABLE_FOREIGN_DATABRICKS, TABLE_FOREIGN_DELTASHARING, TABLE_FOREIGN_HIVE_METASTORE, TABLE_FOREIGN_HIVE_METASTORE_DBFS_EXTERNAL, TABLE_FOREIGN_HIVE_METASTORE_DBFS_MANAGED, TABLE_FOREIGN_HIVE_METASTORE_DBFS_SHALLOW_CLONE_EXTERNAL, TABLE_FOREIGN_HIVE_METASTORE_DBFS_SHALLOW_CLONE_MANAGED, TABLE_FOREIGN_HIVE_METASTORE_DBFS_VIEW, TABLE_FOREIGN_HIVE_METASTORE_EXTERNAL, TABLE_FOREIGN_HIVE_METASTORE_MANAGED, TABLE_FOREIGN_HIVE_METASTORE_SHALLOW_CLONE_EXTERNAL, TABLE_FOREIGN_HIVE_METASTORE_SHALLOW_CLONE_MANAGED, TABLE_FOREIGN_HIVE_METASTORE_VIEW, TABLE_FOREIGN_MONGODB, TABLE_FOREIGN_MYSQL, TABLE_FOREIGN_NETSUITE, TABLE_FOREIGN_ORACLE, TABLE_FOREIGN_POSTGRESQL, TABLE_FOREIGN_REDSHIFT, TABLE_FOREIGN_SALESFORCE, TABLE_FOREIGN_SALESFORCE_DATA_CLOUD, TABLE_FOREIGN_SALESFORCE_DATA_CLOUD_FILE_SHARING, TABLE_FOREIGN_SALESFORCE_DATA_CLOUD_FILE_SHARING_VIEW, TABLE_FOREIGN_SNOWFLAKE, TABLE_FOREIGN_SQLDW, TABLE_FOREIGN_SQLSERVER, TABLE_FOREIGN_TERADATA, TABLE_FOREIGN_WORKDAY_RAAS, TABLE_ICEBERG_UNIFORM_MANAGED, TABLE_INTERNAL, TABLE_MANAGED_POSTGRESQL, TABLE_MATERIALIZED_VIEW, TABLE_MATERIALIZED_VIEW_DELTASHARING, TABLE_METRIC_VIEW, TABLE_METRIC_VIEW_DELTASHARING, TABLE_ONLINE_VECTOR_INDEX_DIRECT, TABLE_ONLINE_VECTOR_INDEX_REPLICA, TABLE_ONLINE_VIEW, TABLE_STANDARD, TABLE_STREAMING_LIVE_TABLE, TABLE_STREAMING_LIVE_TABLE_DELTASHARING, TABLE_SYSTEM, TABLE_SYSTEM_DELTASHARING, TABLE_VIEW, TABLE_VIEW_DELTASHARING)"
      },
      {
        "name": "securable_type",
        "type": "string",
        "description": "The type of Unity Catalog securable. (CATALOG, CLEAN_ROOM, CONNECTION, CREDENTIAL, EXTERNAL_LOCATION, EXTERNAL_METADATA, FUNCTION, METASTORE, PIPELINE, PROVIDER, RECIPIENT, SCHEMA, SHARE, STAGING_TABLE, STORAGE_CREDENTIAL, TABLE, VOLUME)"
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
    "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (EXTERNAL, EXTERNAL_SHALLOW_CLONE, FOREIGN, MANAGED, MANAGED_SHALLOW_CLONE, MATERIALIZED_VIEW, METRIC_VIEW, STREAMING_TABLE, VIEW)"
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
    <td><a href="#parameter-full_name"><code>full_name</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td><a href="#parameter-include_browse"><code>include_browse</code></a>, <a href="#parameter-include_delta_metadata"><code>include_delta_metadata</code></a>, <a href="#parameter-include_manifest_capabilities"><code>include_manifest_capabilities</code></a></td>
    <td>Gets a table from the metastore for a specific catalog and schema. The caller must satisfy one of the</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-catalog_name"><code>catalog_name</code></a>, <a href="#parameter-schema_name"><code>schema_name</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td><a href="#parameter-include_browse"><code>include_browse</code></a>, <a href="#parameter-include_manifest_capabilities"><code>include_manifest_capabilities</code></a>, <a href="#parameter-max_results"><code>max_results</code></a>, <a href="#parameter-omit_columns"><code>omit_columns</code></a>, <a href="#parameter-omit_properties"><code>omit_properties</code></a>, <a href="#parameter-omit_username"><code>omit_username</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>Gets an array of all tables for the current metastore under the parent catalog and schema. The caller</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-workspace"><code>workspace</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-catalog_name"><code>catalog_name</code></a>, <a href="#parameter-schema_name"><code>schema_name</code></a>, <a href="#parameter-table_type"><code>table_type</code></a>, <a href="#parameter-data_source_format"><code>data_source_format</code></a>, <a href="#parameter-storage_location"><code>storage_location</code></a></td>
    <td></td>
    <td>Creates a new table in the specified catalog and schema.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-full_name"><code>full_name</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Change the owner of the table. The caller must be the owner of the parent catalog, have the</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-full_name"><code>full_name</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Deletes a table from the specified parent catalog and schema. The caller must be the owner of the</td>
</tr>
<tr>
    <td><a href="#exists"><CopyableCode code="exists" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-full_name"><code>full_name</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Gets if a table exists in the metastore for a specific catalog and schema. The caller must satisfy one</td>
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
<tr id="parameter-workspace">
    <td><CopyableCode code="workspace" /></td>
    <td><code>string</code></td>
    <td>Your Databricks workspace name (default: your-workspace)</td>
</tr>
<tr id="parameter-include_browse">
    <td><CopyableCode code="include_browse" /></td>
    <td><code>boolean</code></td>
    <td>Whether to include tables in the response for which the principal can only access selective metadata for.</td>
</tr>
<tr id="parameter-include_delta_metadata">
    <td><CopyableCode code="include_delta_metadata" /></td>
    <td><code>boolean</code></td>
    <td>Whether delta metadata should be included in the response.</td>
</tr>
<tr id="parameter-include_manifest_capabilities">
    <td><CopyableCode code="include_manifest_capabilities" /></td>
    <td><code>boolean</code></td>
    <td>Whether to include a manifest containing table capabilities in the response.</td>
</tr>
<tr id="parameter-max_results">
    <td><CopyableCode code="max_results" /></td>
    <td><code>integer</code></td>
    <td>Maximum number of tables to return. If not set, all the tables are returned (not recommended). - when set to a value greater than 0, the page length is the minimum of this value and a server configured value; - when set to 0, the page length is set to a server configured value (recommended); - when set to a value less than 0, an invalid parameter error is returned;</td>
</tr>
<tr id="parameter-omit_columns">
    <td><CopyableCode code="omit_columns" /></td>
    <td><code>boolean</code></td>
    <td>Whether to omit the columns of the table from the response or not.</td>
</tr>
<tr id="parameter-omit_properties">
    <td><CopyableCode code="omit_properties" /></td>
    <td><code>boolean</code></td>
    <td>Whether to omit the properties of the table from the response or not.</td>
</tr>
<tr id="parameter-omit_username">
    <td><CopyableCode code="omit_username" /></td>
    <td><code>boolean</code></td>
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

Gets a table from the metastore for a specific catalog and schema. The caller must satisfy one of the

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
AND workspace = '{{ workspace }}' -- required
AND include_browse = '{{ include_browse }}'
AND include_delta_metadata = '{{ include_delta_metadata }}'
AND include_manifest_capabilities = '{{ include_manifest_capabilities }}'
;
```
</TabItem>
<TabItem value="list">

Gets an array of all tables for the current metastore under the parent catalog and schema. The caller

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
AND workspace = '{{ workspace }}' -- required
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

Creates a new table in the specified catalog and schema.

```sql
INSERT INTO databricks_workspace.catalog.tables (
name,
catalog_name,
schema_name,
table_type,
data_source_format,
storage_location,
columns,
properties,
workspace
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
'{{ workspace }}'
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

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: tables
  props:
    - name: workspace
      value: "{{ workspace }}"
      description: Required parameter for the tables resource.
    - name: name
      value: "{{ name }}"
      description: |
        Name of table, relative to parent schema.
    - name: catalog_name
      value: "{{ catalog_name }}"
      description: |
        Name of parent catalog.
    - name: schema_name
      value: "{{ schema_name }}"
      description: |
        Name of parent schema relative to its parent catalog.
    - name: table_type
      value: "{{ table_type }}"
      description: |
        :param data_source_format: :class:\`DataSourceFormat\`
    - name: data_source_format
      value: "{{ data_source_format }}"
      description: |
        Data source format
    - name: storage_location
      value: "{{ storage_location }}"
      description: |
        Storage root URL for table (for **MANAGED**, **EXTERNAL** tables).
    - name: columns
      description: |
        The array of __ColumnInfo__ definitions of the table's columns.
      value:
        - comment: "{{ comment }}"
          mask:
            function_name: "{{ function_name }}"
            using_column_names:
              - "{{ using_column_names }}"
          name: "{{ name }}"
          nullable: {{ nullable }}
          partition_index: {{ partition_index }}
          position: {{ position }}
          type_interval_type: "{{ type_interval_type }}"
          type_json: "{{ type_json }}"
          type_name: "{{ type_name }}"
          type_precision: {{ type_precision }}
          type_scale: {{ type_scale }}
          type_text: "{{ type_text }}"
    - name: properties
      value: "{{ properties }}"
      description: |
        A map of key-value properties attached to the securable.
`}</CodeBlock>

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

Change the owner of the table. The caller must be the owner of the parent catalog, have the

```sql
UPDATE databricks_workspace.catalog.tables
SET 
owner = '{{ owner }}'
WHERE 
full_name = '{{ full_name }}' --required
AND workspace = '{{ workspace }}' --required;
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

Deletes a table from the specified parent catalog and schema. The caller must be the owner of the

```sql
DELETE FROM databricks_workspace.catalog.tables
WHERE full_name = '{{ full_name }}' --required
AND workspace = '{{ workspace }}' --required
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

Gets if a table exists in the metastore for a specific catalog and schema. The caller must satisfy one

```sql
EXEC databricks_workspace.catalog.tables.exists 
@full_name='{{ full_name }}' --required, 
@workspace='{{ workspace }}' --required
;
```
</TabItem>
</Tabs>
