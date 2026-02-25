---
title: account_rule_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - account_rule_sets
  - iam
  - databricks_account
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage databricks_account resources using SQL
custom_edit_url: null
image: /img/stackql-databricks_account-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import SchemaTable from '@site/src/components/SchemaTable/SchemaTable';

Creates, updates, deletes, gets or lists an <code>account_rule_sets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="account_rule_sets" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.iam.account_rule_sets" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_rule_set"
    values={[
        { label: 'get_rule_set', value: 'get_rule_set' }
    ]}
>
<TabItem value="get_rule_set">

<SchemaTable fields={[
  {
    "name": "name",
    "type": "string",
    "description": ""
  },
  {
    "name": "etag",
    "type": "string",
    "description": "Identifies the version of the rule set returned. Etag used for versioning. The response is at least as fresh as the eTag provided. Etag is used for optimistic concurrency control as a way to help prevent simultaneous updates of a rule set from overwriting each other. It is strongly suggested that systems make use of the etag in the read -&gt; modify -&gt; write pattern to perform rule set updates in order to avoid race conditions that is get an etag from a GET rule set request, and pass it with the PUT update request to identify the rule set version you are updating."
  },
  {
    "name": "grant_rules",
    "type": "array",
    "description": "",
    "children": [
      {
        "name": "role",
        "type": "string",
        "description": ""
      },
      {
        "name": "principals",
        "type": "array",
        "description": "Principals this grant rule applies to. A principal can be a user (for end users), a service principal (for applications and compute workloads), or an account group. Each principal has its own identifier format: * users/&lt;USERNAME&gt; * groups/&lt;GROUP_NAME&gt; * servicePrincipals/&lt;SERVICE_PRINCIPAL_APPLICATION_ID&gt;"
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
    <td><a href="#get_rule_set"><CopyableCode code="get_rule_set" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-etag"><code>etag</code></a></td>
    <td></td>
    <td>Get a rule set by its name. A rule set is always attached to a resource and contains a list of access</td>
</tr>
<tr>
    <td><a href="#update_rule_set"><CopyableCode code="update_rule_set" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-rule_set"><code>rule_set</code></a></td>
    <td></td>
    <td>Replace the rules of a rule set. First, use get to read the current version of the rule set before</td>
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
<tr id="parameter-account_id">
    <td><CopyableCode code="account_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-etag">
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Etag used for versioning. The response is at least as fresh as the eTag provided. Etag is used for optimistic concurrency control as a way to help prevent simultaneous updates of a rule set from overwriting each other. It is strongly suggested that systems make use of the etag in the read -&gt; modify -&gt; write pattern to perform rule set updates in order to avoid race conditions that is get an etag from a GET rule set request, and pass it with the PUT update request to identify the rule set version you are updating. Examples | Summary :--- | :--- `etag=` | An empty etag can only be used in GET to indicate no freshness requirements. `etag=RENUAAABhSweA4NvVmmUYdiU717H3Tgy0UJdor3gE4a+mq/oj9NjAf8ZsQ==` | An etag encoded a specific version of the rule set to get or to be updated.</td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The ruleset name associated with the request. Examples | Summary :--- | :--- `name=accounts/<ACCOUNT_ID>/ruleSets/default` | A name for a rule set on the account. `name=accounts/<ACCOUNT_ID>/groups/<GROUP_ID>/ruleSets/default` | A name for a rule set on the group. `name=accounts/<ACCOUNT_ID>/servicePrincipals/<SERVICE_PRINCIPAL_APPLICATION_ID>/ruleSets/default` | A name for a rule set on the service principal. `name=accounts/<ACCOUNT_ID>/tagPolicies/<TAG_POLICY_ID>/ruleSets/default` | A name for a rule set on the tag policy.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_rule_set"
    values={[
        { label: 'get_rule_set', value: 'get_rule_set' }
    ]}
>
<TabItem value="get_rule_set">

Get a rule set by its name. A rule set is always attached to a resource and contains a list of access

```sql
SELECT
name,
etag,
grant_rules
FROM databricks_account.iam.account_rule_sets
WHERE account_id = '{{ account_id }}' -- required
AND name = '{{ name }}' -- required
AND etag = '{{ etag }}' -- required
;
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="update_rule_set"
    values={[
        { label: 'update_rule_set', value: 'update_rule_set' }
    ]}
>
<TabItem value="update_rule_set">

Replace the rules of a rule set. First, use get to read the current version of the rule set before

```sql
REPLACE databricks_account.iam.account_rule_sets
SET 
name = '{{ name }}',
rule_set = '{{ rule_set }}'
WHERE 
account_id = '{{ account_id }}' --required
AND name = '{{ name }}' --required
AND rule_set = '{{ rule_set }}' --required
RETURNING
name,
etag,
grant_rules;
```
</TabItem>
</Tabs>
