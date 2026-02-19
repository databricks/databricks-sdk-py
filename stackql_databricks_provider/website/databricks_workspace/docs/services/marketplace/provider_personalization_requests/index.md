---
title: provider_personalization_requests
hide_title: false
hide_table_of_contents: false
keywords:
  - provider_personalization_requests
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

Creates, updates, deletes, gets or lists a <code>provider_personalization_requests</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="provider_personalization_requests" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.marketplace.provider_personalization_requests" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "id",
    "type": "string",
    "description": ""
  },
  {
    "name": "listing_id",
    "type": "string",
    "description": ""
  },
  {
    "name": "metastore_id",
    "type": "string",
    "description": ""
  },
  {
    "name": "provider_id",
    "type": "string",
    "description": ""
  },
  {
    "name": "listing_name",
    "type": "string",
    "description": ""
  },
  {
    "name": "comment",
    "type": "string",
    "description": ""
  },
  {
    "name": "consumer_region",
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
    "name": "contact_info",
    "type": "object",
    "description": "contact info for the consumer requesting data or performing a listing installation",
    "children": [
      {
        "name": "company",
        "type": "string",
        "description": ""
      },
      {
        "name": "email",
        "type": "string",
        "description": ""
      },
      {
        "name": "first_name",
        "type": "string",
        "description": ""
      },
      {
        "name": "last_name",
        "type": "string",
        "description": ""
      }
    ]
  },
  {
    "name": "created_at",
    "type": "integer",
    "description": ""
  },
  {
    "name": "intended_use",
    "type": "string",
    "description": ""
  },
  {
    "name": "is_from_lighthouse",
    "type": "boolean",
    "description": ""
  },
  {
    "name": "recipient_type",
    "type": "string",
    "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (DELTA_SHARING_RECIPIENT_TYPE_DATABRICKS, DELTA_SHARING_RECIPIENT_TYPE_OPEN)"
  },
  {
    "name": "share",
    "type": "object",
    "description": "Share information is required for data listings but should be empty/ignored for non-data listings (MCP and App).",
    "children": [
      {
        "name": "name",
        "type": "string",
        "description": ""
      },
      {
        "name": "type",
        "type": "string",
        "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (FULL, SAMPLE)"
      }
    ]
  },
  {
    "name": "status",
    "type": "string",
    "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (DENIED, FULFILLED, NEW, REQUEST_PENDING)"
  },
  {
    "name": "status_message",
    "type": "string",
    "description": ""
  },
  {
    "name": "updated_at",
    "type": "integer",
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
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>List personalization requests to this provider. This will return all personalization requests,</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-listing_id"><code>listing_id</code></a>, <a href="#parameter-request_id"><code>request_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-status"><code>status</code></a></td>
    <td></td>
    <td>Update personalization request. This method only permits updating the status of the request.</td>
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
<tr id="parameter-listing_id">
    <td><CopyableCode code="listing_id" /></td>
    <td><code>string</code></td>
    <td>:param request_id: str</td>
</tr>
<tr id="parameter-request_id">
    <td><CopyableCode code="request_id" /></td>
    <td><code>string</code></td>
    <td></td>
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
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

List personalization requests to this provider. This will return all personalization requests,

```sql
SELECT
id,
listing_id,
metastore_id,
provider_id,
listing_name,
comment,
consumer_region,
contact_info,
created_at,
intended_use,
is_from_lighthouse,
recipient_type,
share,
status,
status_message,
updated_at
FROM databricks_workspace.marketplace.provider_personalization_requests
WHERE deployment_name = '{{ deployment_name }}' -- required
AND page_size = '{{ page_size }}'
AND page_token = '{{ page_token }}'
;
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

Update personalization request. This method only permits updating the status of the request.

```sql
REPLACE databricks_workspace.marketplace.provider_personalization_requests
SET 
status = '{{ status }}',
reason = '{{ reason }}',
share = '{{ share }}'
WHERE 
listing_id = '{{ listing_id }}' --required
AND request_id = '{{ request_id }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND status = '{{ status }}' --required
RETURNING
request;
```
</TabItem>
</Tabs>
