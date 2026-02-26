---
title: policy_compliance_for_jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - policy_compliance_for_jobs
  - jobs
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

Creates, updates, deletes, gets or lists a <code>policy_compliance_for_jobs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="policy_compliance_for_jobs" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.jobs.policy_compliance_for_jobs" /></td></tr>
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
    "name": "is_compliant",
    "type": "boolean",
    "description": ""
  },
  {
    "name": "violations",
    "type": "object",
    "description": "An object containing key-value mappings representing the first 200 policy validation errors. The keys indicate the path where the policy validation error is occurring. An identifier for the job cluster is prepended to the path. The values indicate an error message describing the policy validation error."
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "job_id",
    "type": "integer",
    "description": ""
  },
  {
    "name": "is_compliant",
    "type": "boolean",
    "description": "Whether this job is in compliance with the latest version of its policy."
  },
  {
    "name": "violations",
    "type": "object",
    "description": "An object containing key-value mappings representing the first 200 policy validation errors. The keys indicate the path where the policy validation error is occurring. An identifier for the job cluster is prepended to the path. The values indicate an error message describing the policy validation error."
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
    <td><a href="#parameter-job_id"><code>job_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Returns the policy compliance status of a job. Jobs could be out of compliance if a cluster policy</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-policy_id"><code>policy_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>Returns the policy compliance status of all jobs that use a given policy. Jobs could be out of</td>
</tr>
<tr>
    <td><a href="#enforce"><CopyableCode code="enforce" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-job_id"><code>job_id</code></a></td>
    <td></td>
    <td>Updates a job so the job clusters that are created when running the job (specified in `new_cluster`)</td>
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
<tr id="parameter-job_id">
    <td><CopyableCode code="job_id" /></td>
    <td><code>integer</code></td>
    <td>The ID of the job whose compliance status you are requesting.</td>
</tr>
<tr id="parameter-policy_id">
    <td><CopyableCode code="policy_id" /></td>
    <td><code>string</code></td>
    <td>Canonical unique identifier for the cluster policy.</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>integer</code></td>
    <td>Use this field to specify the maximum number of results to be returned by the server. The server may further constrain the maximum number of results returned in a single page.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>A page token that can be used to navigate to the next page or previous page as returned by `next_page_token` or `prev_page_token`.</td>
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

Returns the policy compliance status of a job. Jobs could be out of compliance if a cluster policy

```sql
SELECT
is_compliant,
violations
FROM databricks_workspace.jobs.policy_compliance_for_jobs
WHERE job_id = '{{ job_id }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
;
```
</TabItem>
<TabItem value="list">

Returns the policy compliance status of all jobs that use a given policy. Jobs could be out of

```sql
SELECT
job_id,
is_compliant,
violations
FROM databricks_workspace.jobs.policy_compliance_for_jobs
WHERE policy_id = '{{ policy_id }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND page_size = '{{ page_size }}'
AND page_token = '{{ page_token }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="enforce"
    values={[
        { label: 'enforce', value: 'enforce' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="enforce">

Updates a job so the job clusters that are created when running the job (specified in `new_cluster`)

```sql
INSERT INTO databricks_workspace.jobs.policy_compliance_for_jobs (
job_id,
validate_only,
deployment_name
)
SELECT 
{{ job_id }} /* required */,
{{ validate_only }},
'{{ deployment_name }}'
RETURNING
has_changes,
job_cluster_changes,
settings
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: policy_compliance_for_jobs
  props:
    - name: deployment_name
      value: "{{ deployment_name }}"
      description: Required parameter for the policy_compliance_for_jobs resource.
    - name: job_id
      value: {{ job_id }}
      description: |
        The ID of the job you want to enforce policy compliance on.
    - name: validate_only
      value: {{ validate_only }}
      description: |
        If set, previews changes made to the job to comply with its policy, but does not update the job.
`}</CodeBlock>

</TabItem>
</Tabs>
