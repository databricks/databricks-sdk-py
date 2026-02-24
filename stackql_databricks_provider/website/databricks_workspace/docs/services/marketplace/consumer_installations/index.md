---
title: consumer_installations
hide_title: false
hide_table_of_contents: false
keywords:
  - consumer_installations
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

Creates, updates, deletes, gets or lists a <code>consumer_installations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="consumer_installations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.marketplace.consumer_installations" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_for_listing"
    values={[
        { label: 'list_for_listing', value: 'list_for_listing' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list_for_listing">

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
    "name": "catalog_name",
    "type": "string",
    "description": ""
  },
  {
    "name": "listing_name",
    "type": "string",
    "description": ""
  },
  {
    "name": "repo_name",
    "type": "string",
    "description": ""
  },
  {
    "name": "share_name",
    "type": "string",
    "description": ""
  },
  {
    "name": "error_message",
    "type": "string",
    "description": ""
  },
  {
    "name": "installed_on",
    "type": "integer",
    "description": ""
  },
  {
    "name": "recipient_type",
    "type": "string",
    "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (DELTA_SHARING_RECIPIENT_TYPE_DATABRICKS, DELTA_SHARING_RECIPIENT_TYPE_OPEN)"
  },
  {
    "name": "repo_path",
    "type": "string",
    "description": ""
  },
  {
    "name": "status",
    "type": "string",
    "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (FAILED, INSTALLED)"
  },
  {
    "name": "token_detail",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "bearerToken",
        "type": "string",
        "description": ""
      },
      {
        "name": "endpoint",
        "type": "string",
        "description": ""
      },
      {
        "name": "expirationTime",
        "type": "string",
        "description": ""
      },
      {
        "name": "shareCredentialsVersion",
        "type": "integer",
        "description": "These field names must follow the delta sharing protocol. Original message: RetrieveToken.Response in managed-catalog/api/messages/recipient.proto"
      }
    ]
  },
  {
    "name": "tokens",
    "type": "array",
    "description": "",
    "children": [
      {
        "name": "activation_url",
        "type": "string",
        "description": ""
      },
      {
        "name": "created_at",
        "type": "integer",
        "description": "Time at which this Recipient Token was created, in epoch milliseconds."
      },
      {
        "name": "created_by",
        "type": "string",
        "description": "Username of Recipient Token creator."
      },
      {
        "name": "expiration_time",
        "type": "integer",
        "description": "Expiration timestamp of the token in epoch milliseconds."
      },
      {
        "name": "id",
        "type": "string",
        "description": "Unique id of the Recipient Token."
      },
      {
        "name": "updated_at",
        "type": "integer",
        "description": "Time at which this Recipient Token was updated, in epoch milliseconds."
      },
      {
        "name": "updated_by",
        "type": "string",
        "description": "Username of Recipient Token updater."
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
    "name": "catalog_name",
    "type": "string",
    "description": ""
  },
  {
    "name": "listing_name",
    "type": "string",
    "description": ""
  },
  {
    "name": "repo_name",
    "type": "string",
    "description": ""
  },
  {
    "name": "share_name",
    "type": "string",
    "description": ""
  },
  {
    "name": "error_message",
    "type": "string",
    "description": ""
  },
  {
    "name": "installed_on",
    "type": "integer",
    "description": ""
  },
  {
    "name": "recipient_type",
    "type": "string",
    "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (DELTA_SHARING_RECIPIENT_TYPE_DATABRICKS, DELTA_SHARING_RECIPIENT_TYPE_OPEN)"
  },
  {
    "name": "repo_path",
    "type": "string",
    "description": ""
  },
  {
    "name": "status",
    "type": "string",
    "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (FAILED, INSTALLED)"
  },
  {
    "name": "token_detail",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "bearerToken",
        "type": "string",
        "description": ""
      },
      {
        "name": "endpoint",
        "type": "string",
        "description": ""
      },
      {
        "name": "expirationTime",
        "type": "string",
        "description": ""
      },
      {
        "name": "shareCredentialsVersion",
        "type": "integer",
        "description": "These field names must follow the delta sharing protocol. Original message: RetrieveToken.Response in managed-catalog/api/messages/recipient.proto"
      }
    ]
  },
  {
    "name": "tokens",
    "type": "array",
    "description": "",
    "children": [
      {
        "name": "activation_url",
        "type": "string",
        "description": ""
      },
      {
        "name": "created_at",
        "type": "integer",
        "description": "Time at which this Recipient Token was created, in epoch milliseconds."
      },
      {
        "name": "created_by",
        "type": "string",
        "description": "Username of Recipient Token creator."
      },
      {
        "name": "expiration_time",
        "type": "integer",
        "description": "Expiration timestamp of the token in epoch milliseconds."
      },
      {
        "name": "id",
        "type": "string",
        "description": "Unique id of the Recipient Token."
      },
      {
        "name": "updated_at",
        "type": "integer",
        "description": "Time at which this Recipient Token was updated, in epoch milliseconds."
      },
      {
        "name": "updated_by",
        "type": "string",
        "description": "Username of Recipient Token updater."
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
    <td><a href="#list_for_listing"><CopyableCode code="list_for_listing" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-listing_id"><code>listing_id</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>List all installations for a particular listing.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-workspace"><code>workspace</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>List all installations across all listings.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-listing_id"><code>listing_id</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Install payload associated with a Databricks Marketplace listing.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-listing_id"><code>listing_id</code></a>, <a href="#parameter-installation_id"><code>installation_id</code></a>, <a href="#parameter-workspace"><code>workspace</code></a>, <a href="#parameter-installation"><code>installation</code></a></td>
    <td></td>
    <td>This is a update API that will update the part of the fields defined in the installation table as well</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-listing_id"><code>listing_id</code></a>, <a href="#parameter-installation_id"><code>installation_id</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Uninstall an installation associated with a Databricks Marketplace listing.</td>
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
<tr id="parameter-installation_id">
    <td><CopyableCode code="installation_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-listing_id">
    <td><CopyableCode code="listing_id" /></td>
    <td><code>string</code></td>
    <td>:param installation_id: str</td>
</tr>
<tr id="parameter-workspace">
    <td><CopyableCode code="workspace" /></td>
    <td><code>string</code></td>
    <td>Your Databricks workspace name (default: your-workspace)</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>integer</code></td>
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
    defaultValue="list_for_listing"
    values={[
        { label: 'list_for_listing', value: 'list_for_listing' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list_for_listing">

List all installations for a particular listing.

```sql
SELECT
id,
listing_id,
catalog_name,
listing_name,
repo_name,
share_name,
error_message,
installed_on,
recipient_type,
repo_path,
status,
token_detail,
tokens
FROM databricks_workspace.marketplace.consumer_installations
WHERE listing_id = '{{ listing_id }}' -- required
AND workspace = '{{ workspace }}' -- required
AND page_size = '{{ page_size }}'
AND page_token = '{{ page_token }}'
;
```
</TabItem>
<TabItem value="list">

List all installations across all listings.

```sql
SELECT
id,
listing_id,
catalog_name,
listing_name,
repo_name,
share_name,
error_message,
installed_on,
recipient_type,
repo_path,
status,
token_detail,
tokens
FROM databricks_workspace.marketplace.consumer_installations
WHERE workspace = '{{ workspace }}' -- required
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

Install payload associated with a Databricks Marketplace listing.

```sql
INSERT INTO databricks_workspace.marketplace.consumer_installations (
accepted_consumer_terms,
catalog_name,
recipient_type,
repo_detail,
share_name,
listing_id,
workspace
)
SELECT 
'{{ accepted_consumer_terms }}',
'{{ catalog_name }}',
'{{ recipient_type }}',
'{{ repo_detail }}',
'{{ share_name }}',
'{{ listing_id }}',
'{{ workspace }}'
RETURNING
installation
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: consumer_installations
  props:
    - name: listing_id
      value: string
      description: Required parameter for the consumer_installations resource.
    - name: workspace
      value: string
      description: Required parameter for the consumer_installations resource.
    - name: accepted_consumer_terms
      value: object
      props:
      - name: version
        value: string
    - name: catalog_name
      value: string
      description: |
        :param recipient_type: :class:`DeltaSharingRecipientType` (optional)
    - name: recipient_type
      value: string
      description: |
        Create a collection of name/value pairs.
        Example enumeration:
        >>> class Color(Enum):
        ...     RED = 1
        ...     BLUE = 2
        ...     GREEN = 3
        Access them by:
        - attribute access::
        >>> Color.RED
        <Color.RED: 1>
        - value lookup:
        >>> Color(1)
        <Color.RED: 1>
        - name lookup:
        >>> Color['RED']
        <Color.RED: 1>
        Enumerations can be iterated over, and know how many members they have:
        >>> len(Color)
        3
        >>> list(Color)
        [<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]
        Methods can be added to enumerations, and members can have their own
        attributes -- see the documentation for details.
    - name: repo_detail
      value: object
      description: |
        for git repo installations
      props:
      - name: repo_name
        value: string
      - name: repo_path
        value: string
        description: |
          refers to the full url file path that navigates the user to the repo's entrypoint (e.g. a README.md file, or the repo file view in the unified UI) should just be a relative path
    - name: share_name
      value: string
      description: |
        :returns: :class:`Installation`
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

This is a update API that will update the part of the fields defined in the installation table as well

```sql
REPLACE databricks_workspace.marketplace.consumer_installations
SET 
installation = '{{ installation }}',
rotate_token = {{ rotate_token }}
WHERE 
listing_id = '{{ listing_id }}' --required
AND installation_id = '{{ installation_id }}' --required
AND workspace = '{{ workspace }}' --required
AND installation = '{{ installation }}' --required
RETURNING
installation;
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

Uninstall an installation associated with a Databricks Marketplace listing.

```sql
DELETE FROM databricks_workspace.marketplace.consumer_installations
WHERE listing_id = '{{ listing_id }}' --required
AND installation_id = '{{ installation_id }}' --required
AND workspace = '{{ workspace }}' --required
;
```
</TabItem>
</Tabs>
