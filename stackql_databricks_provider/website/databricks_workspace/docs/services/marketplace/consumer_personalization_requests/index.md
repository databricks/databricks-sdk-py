---
title: consumer_personalization_requests
hide_title: false
hide_table_of_contents: false
keywords:
  - consumer_personalization_requests
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

Creates, updates, deletes, gets or lists a <code>consumer_personalization_requests</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>consumer_personalization_requests</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.marketplace.consumer_personalization_requests" /></td></tr>
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
    "name": "personalization_requests",
    "type": "array",
    "description": "",
    "children": [
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
        "name": "comment",
        "type": "string",
        "description": ""
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
        "name": "id",
        "type": "string",
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
        "name": "listing_id",
        "type": "string",
        "description": ""
      },
      {
        "name": "listing_name",
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
        "name": "recipient_type",
        "type": "string",
        "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details."
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
            "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details."
          }
        ]
      },
      {
        "name": "status",
        "type": "string",
        "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details."
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
    "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details."
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
        "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details."
      }
    ]
  },
  {
    "name": "status",
    "type": "string",
    "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details."
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
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-listing_id"><code>listing_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Get the personalization request for a listing. Each consumer can make at *most* one personalization<br />request for a listing.<br /><br />:param listing_id: str<br /><br />:returns: :class:`GetPersonalizationRequestResponse`</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>List personalization requests for a consumer across all listings.<br /><br />:param page_size: int (optional)<br />:param page_token: str (optional)<br /><br />:returns: Iterator over :class:`PersonalizationRequest`</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-listing_id"><code>listing_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-data__intended_use"><code>data__intended_use</code></a>, <a href="#parameter-data__accepted_consumer_terms"><code>data__accepted_consumer_terms</code></a></td>
    <td></td>
    <td>Create a personalization request for a listing.<br /><br />:param listing_id: str<br />:param intended_use: str<br />:param accepted_consumer_terms: :class:`ConsumerTerms`<br />:param comment: str (optional)<br />:param company: str (optional)<br />:param first_name: str (optional)<br />:param is_from_lighthouse: bool (optional)<br />:param last_name: str (optional)<br />:param recipient_type: :class:`DeltaSharingRecipientType` (optional)<br /><br />:returns: :class:`CreatePersonalizationRequestResponse`</td>
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
    <td>:param intended_use: str</td>
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

Get the personalization request for a listing. Each consumer can make at *most* one personalization<br />request for a listing.<br /><br />:param listing_id: str<br /><br />:returns: :class:`GetPersonalizationRequestResponse`

```sql
SELECT
personalization_requests
FROM databricks_workspace.marketplace.consumer_personalization_requests
WHERE listing_id = '{{ listing_id }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
;
```
</TabItem>
<TabItem value="list">

List personalization requests for a consumer across all listings.<br /><br />:param page_size: int (optional)<br />:param page_token: str (optional)<br /><br />:returns: Iterator over :class:`PersonalizationRequest`

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
FROM databricks_workspace.marketplace.consumer_personalization_requests
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

Create a personalization request for a listing.<br /><br />:param listing_id: str<br />:param intended_use: str<br />:param accepted_consumer_terms: :class:`ConsumerTerms`<br />:param comment: str (optional)<br />:param company: str (optional)<br />:param first_name: str (optional)<br />:param is_from_lighthouse: bool (optional)<br />:param last_name: str (optional)<br />:param recipient_type: :class:`DeltaSharingRecipientType` (optional)<br /><br />:returns: :class:`CreatePersonalizationRequestResponse`

```sql
INSERT INTO databricks_workspace.marketplace.consumer_personalization_requests (
data__intended_use,
data__accepted_consumer_terms,
data__comment,
data__company,
data__first_name,
data__is_from_lighthouse,
data__last_name,
data__recipient_type,
listing_id,
deployment_name
)
SELECT 
'{{ intended_use }}' /* required */,
'{{ accepted_consumer_terms }}' /* required */,
'{{ comment }}',
'{{ company }}',
'{{ first_name }}',
'{{ is_from_lighthouse }}',
'{{ last_name }}',
'{{ recipient_type }}',
'{{ listing_id }}',
'{{ deployment_name }}'
RETURNING
id
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: consumer_personalization_requests
  props:
    - name: listing_id
      value: string
      description: Required parameter for the consumer_personalization_requests resource.
    - name: deployment_name
      value: string
      description: Required parameter for the consumer_personalization_requests resource.
    - name: intended_use
      value: string
    - name: accepted_consumer_terms
      value: string
      description: |
        :param comment: str (optional)
    - name: comment
      value: string
    - name: company
      value: string
      description: |
        :param first_name: str (optional)
    - name: first_name
      value: string
    - name: is_from_lighthouse
      value: string
      description: |
        :param last_name: str (optional)
    - name: last_name
      value: string
    - name: recipient_type
      value: string
      description: |
        :returns: :class:`CreatePersonalizationRequestResponse`
```
</TabItem>
</Tabs>
