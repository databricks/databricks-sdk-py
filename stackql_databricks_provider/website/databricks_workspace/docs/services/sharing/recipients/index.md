---
title: recipients
hide_title: false
hide_table_of_contents: false
keywords:
  - recipients
  - sharing
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

Creates, updates, deletes, gets or lists a <code>recipients</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>recipients</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.sharing.recipients" /></td></tr>
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
    "description": "[Create,Update:IGN] common - id of the recipient"
  },
  {
    "name": "name",
    "type": "string",
    "description": "Name of Recipient."
  },
  {
    "name": "data_recipient_global_metastore_id",
    "type": "string",
    "description": "The global Unity Catalog metastore id provided by the data recipient. This field is only present when the __authentication_type__ is **DATABRICKS**. The identifier is of format __cloud__:__region__:__metastore-uuid__."
  },
  {
    "name": "metastore_id",
    "type": "string",
    "description": "Unique identifier of recipient's Unity Catalog Metastore. This field is only present when the __authentication_type__ is **DATABRICKS**."
  },
  {
    "name": "activated",
    "type": "boolean",
    "description": ""
  },
  {
    "name": "activation_url",
    "type": "string",
    "description": "Full activation url to retrieve the access token. It will be empty if the token is already retrieved."
  },
  {
    "name": "authentication_type",
    "type": "string",
    "description": "The delta sharing authentication type."
  },
  {
    "name": "cloud",
    "type": "string",
    "description": "Cloud vendor of the recipient's Unity Catalog Metastore. This field is only present when the __authentication_type__ is **DATABRICKS**."
  },
  {
    "name": "comment",
    "type": "string",
    "description": "Description about the recipient."
  },
  {
    "name": "created_at",
    "type": "integer",
    "description": "Time at which this recipient was created, in epoch milliseconds."
  },
  {
    "name": "created_by",
    "type": "string",
    "description": "Username of recipient creator."
  },
  {
    "name": "expiration_time",
    "type": "integer",
    "description": "Expiration timestamp of the token, in epoch milliseconds."
  },
  {
    "name": "ip_access_list",
    "type": "object",
    "description": "IP Access List",
    "children": [
      {
        "name": "allowed_ip_addresses",
        "type": "array",
        "description": ""
      }
    ]
  },
  {
    "name": "owner",
    "type": "string",
    "description": "Username of the recipient owner."
  },
  {
    "name": "properties_kvpairs",
    "type": "object",
    "description": "Recipient properties as map of string key-value pairs. When provided in update request, the specified properties will override the existing properties. To add and remove properties, one would need to perform a read-modify-write.",
    "children": [
      {
        "name": "properties",
        "type": "object",
        "description": "A map of key-value properties attached to the securable."
      }
    ]
  },
  {
    "name": "region",
    "type": "string",
    "description": "Cloud region of the recipient's Unity Catalog Metastore. This field is only present when the __authentication_type__ is **DATABRICKS**."
  },
  {
    "name": "sharing_code",
    "type": "string",
    "description": "The one-time sharing code provided by the data recipient. This field is only present when the __authentication_type__ is **DATABRICKS**."
  },
  {
    "name": "tokens",
    "type": "array",
    "description": "This field is only present when the __authentication_type__ is **TOKEN**.",
    "children": [
      {
        "name": "activation_url",
        "type": "string",
        "description": ""
      },
      {
        "name": "created_at",
        "type": "integer",
        "description": "Time at which this recipient token was created, in epoch milliseconds."
      },
      {
        "name": "created_by",
        "type": "string",
        "description": "Username of recipient token creator."
      },
      {
        "name": "expiration_time",
        "type": "integer",
        "description": "Expiration timestamp of the token in epoch milliseconds."
      },
      {
        "name": "id",
        "type": "string",
        "description": "Unique ID of the recipient token."
      },
      {
        "name": "updated_at",
        "type": "integer",
        "description": "Time at which this recipient token was updated, in epoch milliseconds."
      },
      {
        "name": "updated_by",
        "type": "string",
        "description": "Username of recipient token updater."
      }
    ]
  },
  {
    "name": "updated_at",
    "type": "integer",
    "description": "Time at which the recipient was updated, in epoch milliseconds."
  },
  {
    "name": "updated_by",
    "type": "string",
    "description": "Username of recipient updater."
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "id",
    "type": "string",
    "description": "[Create,Update:IGN] common - id of the recipient"
  },
  {
    "name": "name",
    "type": "string",
    "description": "Name of Recipient."
  },
  {
    "name": "data_recipient_global_metastore_id",
    "type": "string",
    "description": "The global Unity Catalog metastore id provided by the data recipient. This field is only present when the __authentication_type__ is **DATABRICKS**. The identifier is of format __cloud__:__region__:__metastore-uuid__."
  },
  {
    "name": "metastore_id",
    "type": "string",
    "description": "Unique identifier of recipient's Unity Catalog Metastore. This field is only present when the __authentication_type__ is **DATABRICKS**."
  },
  {
    "name": "activated",
    "type": "boolean",
    "description": ""
  },
  {
    "name": "activation_url",
    "type": "string",
    "description": "Full activation url to retrieve the access token. It will be empty if the token is already retrieved."
  },
  {
    "name": "authentication_type",
    "type": "string",
    "description": "The delta sharing authentication type."
  },
  {
    "name": "cloud",
    "type": "string",
    "description": "Cloud vendor of the recipient's Unity Catalog Metastore. This field is only present when the __authentication_type__ is **DATABRICKS**."
  },
  {
    "name": "comment",
    "type": "string",
    "description": "Description about the recipient."
  },
  {
    "name": "created_at",
    "type": "integer",
    "description": "Time at which this recipient was created, in epoch milliseconds."
  },
  {
    "name": "created_by",
    "type": "string",
    "description": "Username of recipient creator."
  },
  {
    "name": "expiration_time",
    "type": "integer",
    "description": "Expiration timestamp of the token, in epoch milliseconds."
  },
  {
    "name": "ip_access_list",
    "type": "object",
    "description": "IP Access List",
    "children": [
      {
        "name": "allowed_ip_addresses",
        "type": "array",
        "description": ""
      }
    ]
  },
  {
    "name": "owner",
    "type": "string",
    "description": "Username of the recipient owner."
  },
  {
    "name": "properties_kvpairs",
    "type": "object",
    "description": "Recipient properties as map of string key-value pairs. When provided in update request, the specified properties will override the existing properties. To add and remove properties, one would need to perform a read-modify-write.",
    "children": [
      {
        "name": "properties",
        "type": "object",
        "description": "A map of key-value properties attached to the securable."
      }
    ]
  },
  {
    "name": "region",
    "type": "string",
    "description": "Cloud region of the recipient's Unity Catalog Metastore. This field is only present when the __authentication_type__ is **DATABRICKS**."
  },
  {
    "name": "sharing_code",
    "type": "string",
    "description": "The one-time sharing code provided by the data recipient. This field is only present when the __authentication_type__ is **DATABRICKS**."
  },
  {
    "name": "tokens",
    "type": "array",
    "description": "This field is only present when the __authentication_type__ is **TOKEN**.",
    "children": [
      {
        "name": "activation_url",
        "type": "string",
        "description": ""
      },
      {
        "name": "created_at",
        "type": "integer",
        "description": "Time at which this recipient token was created, in epoch milliseconds."
      },
      {
        "name": "created_by",
        "type": "string",
        "description": "Username of recipient token creator."
      },
      {
        "name": "expiration_time",
        "type": "integer",
        "description": "Expiration timestamp of the token in epoch milliseconds."
      },
      {
        "name": "id",
        "type": "string",
        "description": "Unique ID of the recipient token."
      },
      {
        "name": "updated_at",
        "type": "integer",
        "description": "Time at which this recipient token was updated, in epoch milliseconds."
      },
      {
        "name": "updated_by",
        "type": "string",
        "description": "Username of recipient token updater."
      }
    ]
  },
  {
    "name": "updated_at",
    "type": "integer",
    "description": "Time at which the recipient was updated, in epoch milliseconds."
  },
  {
    "name": "updated_by",
    "type": "string",
    "description": "Username of recipient updater."
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
    <td></td>
    <td>Gets a share recipient from the metastore. The caller must be one of: * A user with **USE_RECIPIENT**<br />privilege on the metastore * The owner of the share recipient * A metastore admin<br /><br />:param name: str<br />  Name of the recipient.<br /><br />:returns: :class:`RecipientInfo`</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-data_recipient_global_metastore_id"><code>data_recipient_global_metastore_id</code></a>, <a href="#parameter-max_results"><code>max_results</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>Gets an array of all share recipients within the current metastore where:<br /><br />* the caller is a metastore admin, or * the caller is the owner. There is no guarantee of a specific<br />ordering of the elements in the array.<br /><br />:param data_recipient_global_metastore_id: str (optional)<br />  If not provided, all recipients will be returned. If no recipients exist with this ID, no results<br />  will be returned.<br />:param max_results: int (optional)<br />  Maximum number of recipients to return. - when set to 0, the page length is set to a server<br />  configured value (recommended); - when set to a value greater than 0, the page length is the minimum<br />  of this value and a server configured value; - when set to a value less than 0, an invalid parameter<br />  error is returned; - If not set, all valid recipients are returned (not recommended). - Note: The<br />  number of returned recipients might be less than the specified max_results size, even zero. The only<br />  definitive indication that no further recipients can be fetched is when the next_page_token is unset<br />  from the response.<br />:param page_token: str (optional)<br />  Opaque pagination token to go to next page based on previous query.<br /><br />:returns: Iterator over :class:`RecipientInfo`</td>
</tr>
<tr>
    <td><a href="#rotate_token"><CopyableCode code="rotate_token" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-data__existing_token_expire_in_seconds"><code>data__existing_token_expire_in_seconds</code></a></td>
    <td></td>
    <td>Refreshes the specified recipient's delta sharing authentication token with the provided token info.<br />The caller must be the owner of the recipient.<br /><br />:param name: str<br />  The name of the Recipient.<br />:param existing_token_expire_in_seconds: int<br />  The expiration time of the bearer token in ISO 8601 format. This will set the expiration_time of<br />  existing token only to a smaller timestamp, it cannot extend the expiration_time. Use 0 to expire<br />  the existing token immediately, negative number will return an error.<br /><br />:returns: :class:`RecipientInfo`</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-data__name"><code>data__name</code></a>, <a href="#parameter-data__authentication_type"><code>data__authentication_type</code></a></td>
    <td></td>
    <td>Creates a new recipient with the delta sharing authentication type in the metastore. The caller must<br />be a metastore admin or have the **CREATE_RECIPIENT** privilege on the metastore.<br /><br />:param name: str<br />  Name of Recipient.<br />:param authentication_type: :class:`AuthenticationType`<br />:param comment: str (optional)<br />  Description about the recipient.<br />:param data_recipient_global_metastore_id: str (optional)<br />  The global Unity Catalog metastore id provided by the data recipient. This field is only present<br />  when the __authentication_type__ is **DATABRICKS**. The identifier is of format<br />  __cloud__:__region__:__metastore-uuid__.<br />:param expiration_time: int (optional)<br />  Expiration timestamp of the token, in epoch milliseconds.<br />:param id: str (optional)<br />  [Create,Update:IGN] common - id of the recipient<br />:param ip_access_list: :class:`IpAccessList` (optional)<br />  IP Access List<br />:param owner: str (optional)<br />  Username of the recipient owner.<br />:param properties_kvpairs: :class:`SecurablePropertiesKvPairs` (optional)<br />  Recipient properties as map of string key-value pairs. When provided in update request, the<br />  specified properties will override the existing properties. To add and remove properties, one would<br />  need to perform a read-modify-write.<br />:param sharing_code: str (optional)<br />  The one-time sharing code provided by the data recipient. This field is only present when the<br />  __authentication_type__ is **DATABRICKS**.<br /><br />:returns: :class:`RecipientInfo`</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Updates an existing recipient in the metastore. The caller must be a metastore admin or the owner of<br />the recipient. If the recipient name will be updated, the user must be both a metastore admin and the<br />owner of the recipient.<br /><br />:param name: str<br />  Name of the recipient.<br />:param comment: str (optional)<br />  Description about the recipient.<br />:param expiration_time: int (optional)<br />  Expiration timestamp of the token, in epoch milliseconds.<br />:param id: str (optional)<br />  [Create,Update:IGN] common - id of the recipient<br />:param ip_access_list: :class:`IpAccessList` (optional)<br />  IP Access List<br />:param new_name: str (optional)<br />  New name for the recipient. .<br />:param owner: str (optional)<br />  Username of the recipient owner.<br />:param properties_kvpairs: :class:`SecurablePropertiesKvPairs` (optional)<br />  Recipient properties as map of string key-value pairs. When provided in update request, the<br />  specified properties will override the existing properties. To add and remove properties, one would<br />  need to perform a read-modify-write.<br /><br />:returns: :class:`RecipientInfo`</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Deletes the specified recipient from the metastore. The caller must be the owner of the recipient.<br /><br />:param name: str<br />  Name of the recipient.</td>
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
    <td>Name of the recipient.</td>
</tr>
<tr id="parameter-data_recipient_global_metastore_id">
    <td><CopyableCode code="data_recipient_global_metastore_id" /></td>
    <td><code>string</code></td>
    <td>If not provided, all recipients will be returned. If no recipients exist with this ID, no results will be returned.</td>
</tr>
<tr id="parameter-max_results">
    <td><CopyableCode code="max_results" /></td>
    <td><code>string</code></td>
    <td>Maximum number of recipients to return. - when set to 0, the page length is set to a server configured value (recommended); - when set to a value greater than 0, the page length is the minimum of this value and a server configured value; - when set to a value less than 0, an invalid parameter error is returned; - If not set, all valid recipients are returned (not recommended). - Note: The number of returned recipients might be less than the specified max_results size, even zero. The only definitive indication that no further recipients can be fetched is when the next_page_token is unset from the response.</td>
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

Gets a share recipient from the metastore. The caller must be one of: * A user with **USE_RECIPIENT**<br />privilege on the metastore * The owner of the share recipient * A metastore admin<br /><br />:param name: str<br />  Name of the recipient.<br /><br />:returns: :class:`RecipientInfo`

```sql
SELECT
id,
name,
data_recipient_global_metastore_id,
metastore_id,
activated,
activation_url,
authentication_type,
cloud,
comment,
created_at,
created_by,
expiration_time,
ip_access_list,
owner,
properties_kvpairs,
region,
sharing_code,
tokens,
updated_at,
updated_by
FROM databricks_workspace.sharing.recipients
WHERE name = '{{ name }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets an array of all share recipients within the current metastore where:<br /><br />* the caller is a metastore admin, or * the caller is the owner. There is no guarantee of a specific<br />ordering of the elements in the array.<br /><br />:param data_recipient_global_metastore_id: str (optional)<br />  If not provided, all recipients will be returned. If no recipients exist with this ID, no results<br />  will be returned.<br />:param max_results: int (optional)<br />  Maximum number of recipients to return. - when set to 0, the page length is set to a server<br />  configured value (recommended); - when set to a value greater than 0, the page length is the minimum<br />  of this value and a server configured value; - when set to a value less than 0, an invalid parameter<br />  error is returned; - If not set, all valid recipients are returned (not recommended). - Note: The<br />  number of returned recipients might be less than the specified max_results size, even zero. The only<br />  definitive indication that no further recipients can be fetched is when the next_page_token is unset<br />  from the response.<br />:param page_token: str (optional)<br />  Opaque pagination token to go to next page based on previous query.<br /><br />:returns: Iterator over :class:`RecipientInfo`

```sql
SELECT
id,
name,
data_recipient_global_metastore_id,
metastore_id,
activated,
activation_url,
authentication_type,
cloud,
comment,
created_at,
created_by,
expiration_time,
ip_access_list,
owner,
properties_kvpairs,
region,
sharing_code,
tokens,
updated_at,
updated_by
FROM databricks_workspace.sharing.recipients
WHERE deployment_name = '{{ deployment_name }}' -- required
AND data_recipient_global_metastore_id = '{{ data_recipient_global_metastore_id }}'
AND max_results = '{{ max_results }}'
AND page_token = '{{ page_token }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="rotate_token"
    values={[
        { label: 'rotate_token', value: 'rotate_token' },
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="rotate_token">

Refreshes the specified recipient's delta sharing authentication token with the provided token info.<br />The caller must be the owner of the recipient.<br /><br />:param name: str<br />  The name of the Recipient.<br />:param existing_token_expire_in_seconds: int<br />  The expiration time of the bearer token in ISO 8601 format. This will set the expiration_time of<br />  existing token only to a smaller timestamp, it cannot extend the expiration_time. Use 0 to expire<br />  the existing token immediately, negative number will return an error.<br /><br />:returns: :class:`RecipientInfo`

```sql
INSERT INTO databricks_workspace.sharing.recipients (
data__existing_token_expire_in_seconds,
name,
deployment_name
)
SELECT 
{{ existing_token_expire_in_seconds }} /* required */,
'{{ name }}',
'{{ deployment_name }}'
RETURNING
id,
name,
data_recipient_global_metastore_id,
metastore_id,
activated,
activation_url,
authentication_type,
cloud,
comment,
created_at,
created_by,
expiration_time,
ip_access_list,
owner,
properties_kvpairs,
region,
sharing_code,
tokens,
updated_at,
updated_by
;
```
</TabItem>
<TabItem value="create">

Creates a new recipient with the delta sharing authentication type in the metastore. The caller must<br />be a metastore admin or have the **CREATE_RECIPIENT** privilege on the metastore.<br /><br />:param name: str<br />  Name of Recipient.<br />:param authentication_type: :class:`AuthenticationType`<br />:param comment: str (optional)<br />  Description about the recipient.<br />:param data_recipient_global_metastore_id: str (optional)<br />  The global Unity Catalog metastore id provided by the data recipient. This field is only present<br />  when the __authentication_type__ is **DATABRICKS**. The identifier is of format<br />  __cloud__:__region__:__metastore-uuid__.<br />:param expiration_time: int (optional)<br />  Expiration timestamp of the token, in epoch milliseconds.<br />:param id: str (optional)<br />  [Create,Update:IGN] common - id of the recipient<br />:param ip_access_list: :class:`IpAccessList` (optional)<br />  IP Access List<br />:param owner: str (optional)<br />  Username of the recipient owner.<br />:param properties_kvpairs: :class:`SecurablePropertiesKvPairs` (optional)<br />  Recipient properties as map of string key-value pairs. When provided in update request, the<br />  specified properties will override the existing properties. To add and remove properties, one would<br />  need to perform a read-modify-write.<br />:param sharing_code: str (optional)<br />  The one-time sharing code provided by the data recipient. This field is only present when the<br />  __authentication_type__ is **DATABRICKS**.<br /><br />:returns: :class:`RecipientInfo`

```sql
INSERT INTO databricks_workspace.sharing.recipients (
data__name,
data__authentication_type,
data__comment,
data__data_recipient_global_metastore_id,
data__expiration_time,
data__id,
data__ip_access_list,
data__owner,
data__properties_kvpairs,
data__sharing_code,
deployment_name
)
SELECT 
'{{ name }}' /* required */,
'{{ authentication_type }}' /* required */,
'{{ comment }}',
'{{ data_recipient_global_metastore_id }}',
'{{ expiration_time }}',
'{{ id }}',
'{{ ip_access_list }}',
'{{ owner }}',
'{{ properties_kvpairs }}',
'{{ sharing_code }}',
'{{ deployment_name }}'
RETURNING
id,
name,
data_recipient_global_metastore_id,
metastore_id,
activated,
activation_url,
authentication_type,
cloud,
comment,
created_at,
created_by,
expiration_time,
ip_access_list,
owner,
properties_kvpairs,
region,
sharing_code,
tokens,
updated_at,
updated_by
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: recipients
  props:
    - name: name
      value: string
      description: Required parameter for the recipients resource.
    - name: deployment_name
      value: string
      description: Required parameter for the recipients resource.
    - name: existing_token_expire_in_seconds
      value: integer
      description: |
        The expiration time of the bearer token in ISO 8601 format. This will set the expiration_time of existing token only to a smaller timestamp, it cannot extend the expiration_time. Use 0 to expire the existing token immediately, negative number will return an error.
    - name: name
      value: string
      description: |
        Name of Recipient.
    - name: authentication_type
      value: string
      description: |
        :param comment: str (optional) Description about the recipient.
    - name: comment
      value: string
    - name: data_recipient_global_metastore_id
      value: string
      description: |
        The global Unity Catalog metastore id provided by the data recipient. This field is only present when the __authentication_type__ is **DATABRICKS**. The identifier is of format __cloud__:__region__:__metastore-uuid__.
    - name: expiration_time
      value: string
      description: |
        Expiration timestamp of the token, in epoch milliseconds.
    - name: id
      value: string
      description: |
        [Create,Update:IGN] common - id of the recipient
    - name: ip_access_list
      value: string
      description: |
        IP Access List
    - name: owner
      value: string
      description: |
        Username of the recipient owner.
    - name: properties_kvpairs
      value: string
      description: |
        Recipient properties as map of string key-value pairs. When provided in update request, the specified properties will override the existing properties. To add and remove properties, one would need to perform a read-modify-write.
    - name: sharing_code
      value: string
      description: |
        The one-time sharing code provided by the data recipient. This field is only present when the __authentication_type__ is **DATABRICKS**.
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

Updates an existing recipient in the metastore. The caller must be a metastore admin or the owner of<br />the recipient. If the recipient name will be updated, the user must be both a metastore admin and the<br />owner of the recipient.<br /><br />:param name: str<br />  Name of the recipient.<br />:param comment: str (optional)<br />  Description about the recipient.<br />:param expiration_time: int (optional)<br />  Expiration timestamp of the token, in epoch milliseconds.<br />:param id: str (optional)<br />  [Create,Update:IGN] common - id of the recipient<br />:param ip_access_list: :class:`IpAccessList` (optional)<br />  IP Access List<br />:param new_name: str (optional)<br />  New name for the recipient. .<br />:param owner: str (optional)<br />  Username of the recipient owner.<br />:param properties_kvpairs: :class:`SecurablePropertiesKvPairs` (optional)<br />  Recipient properties as map of string key-value pairs. When provided in update request, the<br />  specified properties will override the existing properties. To add and remove properties, one would<br />  need to perform a read-modify-write.<br /><br />:returns: :class:`RecipientInfo`

```sql
UPDATE databricks_workspace.sharing.recipients
SET 
data__comment = '{{ comment }}',
data__expiration_time = '{{ expiration_time }}',
data__id = '{{ id }}',
data__ip_access_list = '{{ ip_access_list }}',
data__new_name = '{{ new_name }}',
data__owner = '{{ owner }}',
data__properties_kvpairs = '{{ properties_kvpairs }}'
WHERE 
name = '{{ name }}' --required
AND deployment_name = '{{ deployment_name }}' --required
RETURNING
id,
name,
data_recipient_global_metastore_id,
metastore_id,
activated,
activation_url,
authentication_type,
cloud,
comment,
created_at,
created_by,
expiration_time,
ip_access_list,
owner,
properties_kvpairs,
region,
sharing_code,
tokens,
updated_at,
updated_by;
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

Deletes the specified recipient from the metastore. The caller must be the owner of the recipient.<br /><br />:param name: str<br />  Name of the recipient.

```sql
DELETE FROM databricks_workspace.sharing.recipients
WHERE name = '{{ name }}' --required
AND deployment_name = '{{ deployment_name }}' --required
;
```
</TabItem>
</Tabs>
