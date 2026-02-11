---
title: postgres_credentials
hide_title: false
hide_table_of_contents: false
keywords:
  - postgres_credentials
  - postgres
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

Creates, updates, deletes, gets or lists a <code>postgres_credentials</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>postgres_credentials</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.postgres.postgres_credentials" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


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
    <td><a href="#generate"><CopyableCode code="generate" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Generate OAuth credentials for a Postgres database.<br /><br />:param endpoint: str<br />  This field is not yet supported. The endpoint for which this credential will be generated. Format:<br />  projects/&#123;project_id&#125;/branches/&#123;branch_id&#125;/endpoints/&#123;endpoint_id&#125;<br />:param claims: List[:class:`RequestedClaims`] (optional)<br />  The returned token will be scoped to UC tables with the specified permissions.<br /><br />:returns: :class:`DatabaseCredential`</td>
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
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="generate"
    values={[
        { label: 'generate', value: 'generate' }
    ]}
>
<TabItem value="generate">

Generate OAuth credentials for a Postgres database.<br /><br />:param endpoint: str<br />  This field is not yet supported. The endpoint for which this credential will be generated. Format:<br />  projects/&#123;project_id&#125;/branches/&#123;branch_id&#125;/endpoints/&#123;endpoint_id&#125;<br />:param claims: List[:class:`RequestedClaims`] (optional)<br />  The returned token will be scoped to UC tables with the specified permissions.<br /><br />:returns: :class:`DatabaseCredential`

```sql
EXEC databricks_workspace.postgres.postgres_credentials.generate 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"endpoint": "{{ endpoint }}", 
"claims": "{{ claims }}"
}'
;
```
</TabItem>
</Tabs>
