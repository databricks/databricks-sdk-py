---
title: temporary_path_credentials
hide_title: false
hide_table_of_contents: false
keywords:
  - temporary_path_credentials
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

Creates, updates, deletes, gets or lists a <code>temporary_path_credentials</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="temporary_path_credentials" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.catalog.temporary_path_credentials" /></td></tr>
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
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-url"><code>url</code></a>, <a href="#parameter-operation"><code>operation</code></a></td>
    <td></td>
    <td>Get a short-lived credential for directly accessing cloud storage locations registered in Databricks.</td>
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

## `INSERT` examples

<Tabs
    defaultValue="generate"
    values={[
        { label: 'generate', value: 'generate' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="generate">

Get a short-lived credential for directly accessing cloud storage locations registered in Databricks.

```sql
INSERT INTO databricks_workspace.catalog.temporary_path_credentials (
url,
operation,
dry_run,
deployment_name
)
SELECT 
'{{ url }}' /* required */,
'{{ operation }}' /* required */,
'{{ dry_run }}',
'{{ deployment_name }}'
RETURNING
aws_temp_credentials,
azure_aad,
azure_user_delegation_sas,
expiration_time,
gcp_oauth_token,
r2_temp_credentials,
url
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: temporary_path_credentials
  props:
    - name: deployment_name
      value: string
      description: Required parameter for the temporary_path_credentials resource.
    - name: url
      value: string
      description: |
        URL for path-based access.
    - name: operation
      value: string
      description: |
        The operation being performed on the path.
    - name: dry_run
      value: string
      description: |
        Optional. When set to true, the service will not validate that the generated credentials can perform write operations, therefore no new paths will be created and the response will not contain valid credentials. Defaults to false.
```
</TabItem>
</Tabs>
