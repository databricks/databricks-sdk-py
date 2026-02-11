---
title: external_locations
hide_title: false
hide_table_of_contents: false
keywords:
  - external_locations
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

Creates, updates, deletes, gets or lists an <code>external_locations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>external_locations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.catalog.external_locations" /></td></tr>
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
    "description": "Name of the external location."
  },
  {
    "name": "credential_id",
    "type": "string",
    "description": "Unique ID of the location's storage credential."
  },
  {
    "name": "metastore_id",
    "type": "string",
    "description": "Unique identifier of metastore hosting the external location."
  },
  {
    "name": "credential_name",
    "type": "string",
    "description": "Name of the storage credential used with this location."
  },
  {
    "name": "browse_only",
    "type": "boolean",
    "description": ""
  },
  {
    "name": "comment",
    "type": "string",
    "description": "User-provided free-form text description."
  },
  {
    "name": "created_at",
    "type": "integer",
    "description": "Time at which this external location was created, in epoch milliseconds."
  },
  {
    "name": "created_by",
    "type": "string",
    "description": "Username of external location creator."
  },
  {
    "name": "enable_file_events",
    "type": "boolean",
    "description": "Whether to enable file events on this external location. Default to `true`. Set to `false` to disable file events."
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
    "name": "fallback",
    "type": "boolean",
    "description": "Indicates whether fallback mode is enabled for this external location. When fallback mode is enabled, the access to the location falls back to cluster credentials if UC credentials are not sufficient."
  },
  {
    "name": "file_event_queue",
    "type": "object",
    "description": "File event queue settings. If `enable_file_events` is not `false`, must be defined and have exactly one of the documented properties.",
    "children": [
      {
        "name": "managed_aqs",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "managed_resource_id",
            "type": "string",
            "description": ""
          },
          {
            "name": "queue_url",
            "type": "string",
            "description": "The AQS queue url in the format https://&#123;storage account&#125;.queue.core.windows.net/&#123;queue name&#125; Only required for provided_aqs."
          },
          {
            "name": "resource_group",
            "type": "string",
            "description": "Optional resource group for the queue, event grid subscription, and external location storage account. Only required for locations with a service principal storage credential"
          },
          {
            "name": "subscription_id",
            "type": "string",
            "description": "Optional subscription id for the queue, event grid subscription, and external location storage account. Required for locations with a service principal storage credential"
          }
        ]
      },
      {
        "name": "managed_pubsub",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "managed_resource_id",
            "type": "string",
            "description": ""
          },
          {
            "name": "subscription_name",
            "type": "string",
            "description": "The Pub/Sub subscription name in the format projects/&#123;project&#125;/subscriptions/&#123;subscription name&#125;. Only required for provided_pubsub."
          }
        ]
      },
      {
        "name": "managed_sqs",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "managed_resource_id",
            "type": "string",
            "description": ""
          },
          {
            "name": "queue_url",
            "type": "string",
            "description": "The AQS queue url in the format https://sqs.&#123;region&#125;.amazonaws.com/&#123;account id&#125;/&#123;queue name&#125;. Only required for provided_sqs."
          }
        ]
      },
      {
        "name": "provided_aqs",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "managed_resource_id",
            "type": "string",
            "description": ""
          },
          {
            "name": "queue_url",
            "type": "string",
            "description": "The AQS queue url in the format https://&#123;storage account&#125;.queue.core.windows.net/&#123;queue name&#125; Only required for provided_aqs."
          },
          {
            "name": "resource_group",
            "type": "string",
            "description": "Optional resource group for the queue, event grid subscription, and external location storage account. Only required for locations with a service principal storage credential"
          },
          {
            "name": "subscription_id",
            "type": "string",
            "description": "Optional subscription id for the queue, event grid subscription, and external location storage account. Required for locations with a service principal storage credential"
          }
        ]
      },
      {
        "name": "provided_pubsub",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "managed_resource_id",
            "type": "string",
            "description": ""
          },
          {
            "name": "subscription_name",
            "type": "string",
            "description": "The Pub/Sub subscription name in the format projects/&#123;project&#125;/subscriptions/&#123;subscription name&#125;. Only required for provided_pubsub."
          }
        ]
      },
      {
        "name": "provided_sqs",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "managed_resource_id",
            "type": "string",
            "description": ""
          },
          {
            "name": "queue_url",
            "type": "string",
            "description": "The AQS queue url in the format https://sqs.&#123;region&#125;.amazonaws.com/&#123;account id&#125;/&#123;queue name&#125;. Only required for provided_sqs."
          }
        ]
      }
    ]
  },
  {
    "name": "isolation_mode",
    "type": "string",
    "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details."
  },
  {
    "name": "owner",
    "type": "string",
    "description": "The owner of the external location."
  },
  {
    "name": "read_only",
    "type": "boolean",
    "description": "Indicates whether the external location is read-only."
  },
  {
    "name": "updated_at",
    "type": "integer",
    "description": "Time at which external location this was last modified, in epoch milliseconds."
  },
  {
    "name": "updated_by",
    "type": "string",
    "description": "Username of user who last modified the external location."
  },
  {
    "name": "url",
    "type": "string",
    "description": "Path URL of the external location."
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "name",
    "type": "string",
    "description": "Name of the external location."
  },
  {
    "name": "credential_id",
    "type": "string",
    "description": "Unique ID of the location's storage credential."
  },
  {
    "name": "metastore_id",
    "type": "string",
    "description": "Unique identifier of metastore hosting the external location."
  },
  {
    "name": "credential_name",
    "type": "string",
    "description": "Name of the storage credential used with this location."
  },
  {
    "name": "browse_only",
    "type": "boolean",
    "description": ""
  },
  {
    "name": "comment",
    "type": "string",
    "description": "User-provided free-form text description."
  },
  {
    "name": "created_at",
    "type": "integer",
    "description": "Time at which this external location was created, in epoch milliseconds."
  },
  {
    "name": "created_by",
    "type": "string",
    "description": "Username of external location creator."
  },
  {
    "name": "enable_file_events",
    "type": "boolean",
    "description": "Whether to enable file events on this external location. Default to `true`. Set to `false` to disable file events."
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
    "name": "fallback",
    "type": "boolean",
    "description": "Indicates whether fallback mode is enabled for this external location. When fallback mode is enabled, the access to the location falls back to cluster credentials if UC credentials are not sufficient."
  },
  {
    "name": "file_event_queue",
    "type": "object",
    "description": "File event queue settings. If `enable_file_events` is not `false`, must be defined and have exactly one of the documented properties.",
    "children": [
      {
        "name": "managed_aqs",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "managed_resource_id",
            "type": "string",
            "description": ""
          },
          {
            "name": "queue_url",
            "type": "string",
            "description": "The AQS queue url in the format https://&#123;storage account&#125;.queue.core.windows.net/&#123;queue name&#125; Only required for provided_aqs."
          },
          {
            "name": "resource_group",
            "type": "string",
            "description": "Optional resource group for the queue, event grid subscription, and external location storage account. Only required for locations with a service principal storage credential"
          },
          {
            "name": "subscription_id",
            "type": "string",
            "description": "Optional subscription id for the queue, event grid subscription, and external location storage account. Required for locations with a service principal storage credential"
          }
        ]
      },
      {
        "name": "managed_pubsub",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "managed_resource_id",
            "type": "string",
            "description": ""
          },
          {
            "name": "subscription_name",
            "type": "string",
            "description": "The Pub/Sub subscription name in the format projects/&#123;project&#125;/subscriptions/&#123;subscription name&#125;. Only required for provided_pubsub."
          }
        ]
      },
      {
        "name": "managed_sqs",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "managed_resource_id",
            "type": "string",
            "description": ""
          },
          {
            "name": "queue_url",
            "type": "string",
            "description": "The AQS queue url in the format https://sqs.&#123;region&#125;.amazonaws.com/&#123;account id&#125;/&#123;queue name&#125;. Only required for provided_sqs."
          }
        ]
      },
      {
        "name": "provided_aqs",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "managed_resource_id",
            "type": "string",
            "description": ""
          },
          {
            "name": "queue_url",
            "type": "string",
            "description": "The AQS queue url in the format https://&#123;storage account&#125;.queue.core.windows.net/&#123;queue name&#125; Only required for provided_aqs."
          },
          {
            "name": "resource_group",
            "type": "string",
            "description": "Optional resource group for the queue, event grid subscription, and external location storage account. Only required for locations with a service principal storage credential"
          },
          {
            "name": "subscription_id",
            "type": "string",
            "description": "Optional subscription id for the queue, event grid subscription, and external location storage account. Required for locations with a service principal storage credential"
          }
        ]
      },
      {
        "name": "provided_pubsub",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "managed_resource_id",
            "type": "string",
            "description": ""
          },
          {
            "name": "subscription_name",
            "type": "string",
            "description": "The Pub/Sub subscription name in the format projects/&#123;project&#125;/subscriptions/&#123;subscription name&#125;. Only required for provided_pubsub."
          }
        ]
      },
      {
        "name": "provided_sqs",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "managed_resource_id",
            "type": "string",
            "description": ""
          },
          {
            "name": "queue_url",
            "type": "string",
            "description": "The AQS queue url in the format https://sqs.&#123;region&#125;.amazonaws.com/&#123;account id&#125;/&#123;queue name&#125;. Only required for provided_sqs."
          }
        ]
      }
    ]
  },
  {
    "name": "isolation_mode",
    "type": "string",
    "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details."
  },
  {
    "name": "owner",
    "type": "string",
    "description": "The owner of the external location."
  },
  {
    "name": "read_only",
    "type": "boolean",
    "description": "Indicates whether the external location is read-only."
  },
  {
    "name": "updated_at",
    "type": "integer",
    "description": "Time at which external location this was last modified, in epoch milliseconds."
  },
  {
    "name": "updated_by",
    "type": "string",
    "description": "Username of user who last modified the external location."
  },
  {
    "name": "url",
    "type": "string",
    "description": "Path URL of the external location."
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
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-include_browse"><code>include_browse</code></a></td>
    <td>Gets an external location from the metastore. The caller must be either a metastore admin, the owner<br />of the external location, or a user that has some privilege on the external location.<br /><br />:param name: str<br />  Name of the external location.<br />:param include_browse: bool (optional)<br />  Whether to include external locations in the response for which the principal can only access<br />  selective metadata for<br /><br />:returns: :class:`ExternalLocationInfo`</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-include_browse"><code>include_browse</code></a>, <a href="#parameter-include_unbound"><code>include_unbound</code></a>, <a href="#parameter-max_results"><code>max_results</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>Gets an array of external locations (__ExternalLocationInfo__ objects) from the metastore. The caller<br />must be a metastore admin, the owner of the external location, or a user that has some privilege on<br />the external location. There is no guarantee of a specific ordering of the elements in the array.<br /><br />NOTE: we recommend using max_results=0 to use the paginated version of this API. Unpaginated calls<br />will be deprecated soon.<br /><br />PAGINATION BEHAVIOR: When using pagination (max_results &gt;= 0), a page may contain zero results while<br />still providing a next_page_token. Clients must continue reading pages until next_page_token is<br />absent, which is the only indication that the end of results has been reached.<br /><br />:param include_browse: bool (optional)<br />  Whether to include external locations in the response for which the principal can only access<br />  selective metadata for<br />:param include_unbound: bool (optional)<br />  Whether to include external locations not bound to the workspace. Effective only if the user has<br />  permission to update the location–workspace binding.<br />:param max_results: int (optional)<br />  Maximum number of external locations to return. If not set, all the external locations are returned<br />  (not recommended). - when set to a value greater than 0, the page length is the minimum of this<br />  value and a server configured value; - when set to 0, the page length is set to a server configured<br />  value (recommended); - when set to a value less than 0, an invalid parameter error is returned;<br />:param page_token: str (optional)<br />  Opaque pagination token to go to next page based on previous query.<br /><br />:returns: Iterator over :class:`ExternalLocationInfo`</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-data__name"><code>data__name</code></a>, <a href="#parameter-data__url"><code>data__url</code></a>, <a href="#parameter-data__credential_name"><code>data__credential_name</code></a></td>
    <td></td>
    <td>Creates a new external location entry in the metastore. The caller must be a metastore admin or have<br />the **CREATE_EXTERNAL_LOCATION** privilege on both the metastore and the associated storage<br />credential.<br /><br />:param name: str<br />  Name of the external location.<br />:param url: str<br />  Path URL of the external location.<br />:param credential_name: str<br />  Name of the storage credential used with this location.<br />:param comment: str (optional)<br />  User-provided free-form text description.<br />:param enable_file_events: bool (optional)<br />  Whether to enable file events on this external location. Default to `true`. Set to `false` to<br />  disable file events.<br />:param encryption_details: :class:`EncryptionDetails` (optional)<br />:param fallback: bool (optional)<br />  Indicates whether fallback mode is enabled for this external location. When fallback mode is<br />  enabled, the access to the location falls back to cluster credentials if UC credentials are not<br />  sufficient.<br />:param file_event_queue: :class:`FileEventQueue` (optional)<br />  File event queue settings. If `enable_file_events` is not `false`, must be defined and have exactly<br />  one of the documented properties.<br />:param read_only: bool (optional)<br />  Indicates whether the external location is read-only.<br />:param skip_validation: bool (optional)<br />  Skips validation of the storage credential associated with the external location.<br /><br />:returns: :class:`ExternalLocationInfo`</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Updates an external location in the metastore. The caller must be the owner of the external location,<br />or be a metastore admin. In the second case, the admin can only update the name of the external<br />location.<br /><br />:param name: str<br />  Name of the external location.<br />:param comment: str (optional)<br />  User-provided free-form text description.<br />:param credential_name: str (optional)<br />  Name of the storage credential used with this location.<br />:param enable_file_events: bool (optional)<br />  Whether to enable file events on this external location. Default to `true`. Set to `false` to<br />  disable file events.<br />:param encryption_details: :class:`EncryptionDetails` (optional)<br />:param fallback: bool (optional)<br />  Indicates whether fallback mode is enabled for this external location. When fallback mode is<br />  enabled, the access to the location falls back to cluster credentials if UC credentials are not<br />  sufficient.<br />:param file_event_queue: :class:`FileEventQueue` (optional)<br />  File event queue settings. If `enable_file_events` is not `false`, must be defined and have exactly<br />  one of the documented properties.<br />:param force: bool (optional)<br />  Force update even if changing url invalidates dependent external tables or mounts.<br />:param isolation_mode: :class:`IsolationMode` (optional)<br />:param new_name: str (optional)<br />  New name for the external location.<br />:param owner: str (optional)<br />  The owner of the external location.<br />:param read_only: bool (optional)<br />  Indicates whether the external location is read-only.<br />:param skip_validation: bool (optional)<br />  Skips validation of the storage credential associated with the external location.<br />:param url: str (optional)<br />  Path URL of the external location.<br /><br />:returns: :class:`ExternalLocationInfo`</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-force"><code>force</code></a></td>
    <td>Deletes the specified external location from the metastore. The caller must be the owner of the<br />external location.<br /><br />:param name: str<br />  Name of the external location.<br />:param force: bool (optional)<br />  Force deletion even if there are dependent external tables or mounts.</td>
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
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the external location.</td>
</tr>
<tr id="parameter-force">
    <td><CopyableCode code="force" /></td>
    <td><code>string</code></td>
    <td>Force deletion even if there are dependent external tables or mounts.</td>
</tr>
<tr id="parameter-include_browse">
    <td><CopyableCode code="include_browse" /></td>
    <td><code>string</code></td>
    <td>Whether to include external locations in the response for which the principal can only access selective metadata for</td>
</tr>
<tr id="parameter-include_unbound">
    <td><CopyableCode code="include_unbound" /></td>
    <td><code>string</code></td>
    <td>Whether to include external locations not bound to the workspace. Effective only if the user has permission to update the location–workspace binding.</td>
</tr>
<tr id="parameter-max_results">
    <td><CopyableCode code="max_results" /></td>
    <td><code>string</code></td>
    <td>Maximum number of external locations to return. If not set, all the external locations are returned (not recommended). - when set to a value greater than 0, the page length is the minimum of this value and a server configured value; - when set to 0, the page length is set to a server configured value (recommended); - when set to a value less than 0, an invalid parameter error is returned;</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>Opaque pagination token to go to next page based on previous query.</td>
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

Gets an external location from the metastore. The caller must be either a metastore admin, the owner<br />of the external location, or a user that has some privilege on the external location.<br /><br />:param name: str<br />  Name of the external location.<br />:param include_browse: bool (optional)<br />  Whether to include external locations in the response for which the principal can only access<br />  selective metadata for<br /><br />:returns: :class:`ExternalLocationInfo`

```sql
SELECT
name,
credential_id,
metastore_id,
credential_name,
browse_only,
comment,
created_at,
created_by,
enable_file_events,
encryption_details,
fallback,
file_event_queue,
isolation_mode,
owner,
read_only,
updated_at,
updated_by,
url
FROM databricks_workspace.catalog.external_locations
WHERE name = '{{ name }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND include_browse = '{{ include_browse }}'
;
```
</TabItem>
<TabItem value="list">

Gets an array of external locations (__ExternalLocationInfo__ objects) from the metastore. The caller<br />must be a metastore admin, the owner of the external location, or a user that has some privilege on<br />the external location. There is no guarantee of a specific ordering of the elements in the array.<br /><br />NOTE: we recommend using max_results=0 to use the paginated version of this API. Unpaginated calls<br />will be deprecated soon.<br /><br />PAGINATION BEHAVIOR: When using pagination (max_results &gt;= 0), a page may contain zero results while<br />still providing a next_page_token. Clients must continue reading pages until next_page_token is<br />absent, which is the only indication that the end of results has been reached.<br /><br />:param include_browse: bool (optional)<br />  Whether to include external locations in the response for which the principal can only access<br />  selective metadata for<br />:param include_unbound: bool (optional)<br />  Whether to include external locations not bound to the workspace. Effective only if the user has<br />  permission to update the location–workspace binding.<br />:param max_results: int (optional)<br />  Maximum number of external locations to return. If not set, all the external locations are returned<br />  (not recommended). - when set to a value greater than 0, the page length is the minimum of this<br />  value and a server configured value; - when set to 0, the page length is set to a server configured<br />  value (recommended); - when set to a value less than 0, an invalid parameter error is returned;<br />:param page_token: str (optional)<br />  Opaque pagination token to go to next page based on previous query.<br /><br />:returns: Iterator over :class:`ExternalLocationInfo`

```sql
SELECT
name,
credential_id,
metastore_id,
credential_name,
browse_only,
comment,
created_at,
created_by,
enable_file_events,
encryption_details,
fallback,
file_event_queue,
isolation_mode,
owner,
read_only,
updated_at,
updated_by,
url
FROM databricks_workspace.catalog.external_locations
WHERE deployment_name = '{{ deployment_name }}' -- required
AND include_browse = '{{ include_browse }}'
AND include_unbound = '{{ include_unbound }}'
AND max_results = '{{ max_results }}'
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

Creates a new external location entry in the metastore. The caller must be a metastore admin or have<br />the **CREATE_EXTERNAL_LOCATION** privilege on both the metastore and the associated storage<br />credential.<br /><br />:param name: str<br />  Name of the external location.<br />:param url: str<br />  Path URL of the external location.<br />:param credential_name: str<br />  Name of the storage credential used with this location.<br />:param comment: str (optional)<br />  User-provided free-form text description.<br />:param enable_file_events: bool (optional)<br />  Whether to enable file events on this external location. Default to `true`. Set to `false` to<br />  disable file events.<br />:param encryption_details: :class:`EncryptionDetails` (optional)<br />:param fallback: bool (optional)<br />  Indicates whether fallback mode is enabled for this external location. When fallback mode is<br />  enabled, the access to the location falls back to cluster credentials if UC credentials are not<br />  sufficient.<br />:param file_event_queue: :class:`FileEventQueue` (optional)<br />  File event queue settings. If `enable_file_events` is not `false`, must be defined and have exactly<br />  one of the documented properties.<br />:param read_only: bool (optional)<br />  Indicates whether the external location is read-only.<br />:param skip_validation: bool (optional)<br />  Skips validation of the storage credential associated with the external location.<br /><br />:returns: :class:`ExternalLocationInfo`

```sql
INSERT INTO databricks_workspace.catalog.external_locations (
data__name,
data__url,
data__credential_name,
data__comment,
data__enable_file_events,
data__encryption_details,
data__fallback,
data__file_event_queue,
data__read_only,
data__skip_validation,
deployment_name
)
SELECT 
'{{ name }}' /* required */,
'{{ url }}' /* required */,
'{{ credential_name }}' /* required */,
'{{ comment }}',
'{{ enable_file_events }}',
'{{ encryption_details }}',
'{{ fallback }}',
'{{ file_event_queue }}',
'{{ read_only }}',
'{{ skip_validation }}',
'{{ deployment_name }}'
RETURNING
name,
credential_id,
metastore_id,
credential_name,
browse_only,
comment,
created_at,
created_by,
enable_file_events,
encryption_details,
fallback,
file_event_queue,
isolation_mode,
owner,
read_only,
updated_at,
updated_by,
url
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: external_locations
  props:
    - name: deployment_name
      value: string
      description: Required parameter for the external_locations resource.
    - name: name
      value: string
      description: |
        Name of the external location.
    - name: url
      value: string
      description: |
        Path URL of the external location.
    - name: credential_name
      value: string
      description: |
        Name of the storage credential used with this location.
    - name: comment
      value: string
      description: |
        User-provided free-form text description.
    - name: enable_file_events
      value: string
      description: |
        Whether to enable file events on this external location. Default to `true`. Set to `false` to disable file events.
    - name: encryption_details
      value: string
      description: |
        :param fallback: bool (optional) Indicates whether fallback mode is enabled for this external location. When fallback mode is enabled, the access to the location falls back to cluster credentials if UC credentials are not sufficient.
    - name: fallback
      value: string
    - name: file_event_queue
      value: string
      description: |
        File event queue settings. If `enable_file_events` is not `false`, must be defined and have exactly one of the documented properties.
    - name: read_only
      value: string
      description: |
        Indicates whether the external location is read-only.
    - name: skip_validation
      value: string
      description: |
        Skips validation of the storage credential associated with the external location.
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

Updates an external location in the metastore. The caller must be the owner of the external location,<br />or be a metastore admin. In the second case, the admin can only update the name of the external<br />location.<br /><br />:param name: str<br />  Name of the external location.<br />:param comment: str (optional)<br />  User-provided free-form text description.<br />:param credential_name: str (optional)<br />  Name of the storage credential used with this location.<br />:param enable_file_events: bool (optional)<br />  Whether to enable file events on this external location. Default to `true`. Set to `false` to<br />  disable file events.<br />:param encryption_details: :class:`EncryptionDetails` (optional)<br />:param fallback: bool (optional)<br />  Indicates whether fallback mode is enabled for this external location. When fallback mode is<br />  enabled, the access to the location falls back to cluster credentials if UC credentials are not<br />  sufficient.<br />:param file_event_queue: :class:`FileEventQueue` (optional)<br />  File event queue settings. If `enable_file_events` is not `false`, must be defined and have exactly<br />  one of the documented properties.<br />:param force: bool (optional)<br />  Force update even if changing url invalidates dependent external tables or mounts.<br />:param isolation_mode: :class:`IsolationMode` (optional)<br />:param new_name: str (optional)<br />  New name for the external location.<br />:param owner: str (optional)<br />  The owner of the external location.<br />:param read_only: bool (optional)<br />  Indicates whether the external location is read-only.<br />:param skip_validation: bool (optional)<br />  Skips validation of the storage credential associated with the external location.<br />:param url: str (optional)<br />  Path URL of the external location.<br /><br />:returns: :class:`ExternalLocationInfo`

```sql
UPDATE databricks_workspace.catalog.external_locations
SET 
data__comment = '{{ comment }}',
data__credential_name = '{{ credential_name }}',
data__enable_file_events = '{{ enable_file_events }}',
data__encryption_details = '{{ encryption_details }}',
data__fallback = '{{ fallback }}',
data__file_event_queue = '{{ file_event_queue }}',
data__force = '{{ force }}',
data__isolation_mode = '{{ isolation_mode }}',
data__new_name = '{{ new_name }}',
data__owner = '{{ owner }}',
data__read_only = '{{ read_only }}',
data__skip_validation = '{{ skip_validation }}',
data__url = '{{ url }}'
WHERE 
name = '{{ name }}' --required
AND deployment_name = '{{ deployment_name }}' --required
RETURNING
name,
credential_id,
metastore_id,
credential_name,
browse_only,
comment,
created_at,
created_by,
enable_file_events,
encryption_details,
fallback,
file_event_queue,
isolation_mode,
owner,
read_only,
updated_at,
updated_by,
url;
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

Deletes the specified external location from the metastore. The caller must be the owner of the<br />external location.<br /><br />:param name: str<br />  Name of the external location.<br />:param force: bool (optional)<br />  Force deletion even if there are dependent external tables or mounts.

```sql
DELETE FROM databricks_workspace.catalog.external_locations
WHERE name = '{{ name }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND force = '{{ force }}'
;
```
</TabItem>
</Tabs>
