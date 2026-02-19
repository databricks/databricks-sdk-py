---
title: vw_ncc_aws_private_endpoint_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - vw_ncc_aws_private_endpoint_rules
  - settings
  - databricks_account
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage databricks_account resources using SQL
custom_edit_url: null
image: /img/stackql-databricks_account-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import SchemaTable from '@site/src/components/SchemaTable/SchemaTable';

Creates, updates, deletes, gets or lists a <code>vw_ncc_aws_private_endpoint_rules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="vw_ncc_aws_private_endpoint_rules" /></td></tr>
<tr><td><b>Type</b></td><td>View</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.settings.vw_ncc_aws_private_endpoint_rules" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by this view:

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Datatype</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr>
    <td><CopyableCode code="account_id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Databricks account ID used to scope the query.</td>
</tr>
<tr>
    <td><CopyableCode code="network_connectivity_config_id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Unique identifier for the parent network connectivity configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="ncc_name" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Human-readable name of the parent network connectivity configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="region" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Cloud region of the parent network connectivity configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="rule_id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Unique identifier for this AWS private endpoint rule (one row per rule).</td>
</tr>
<tr>
    <td><CopyableCode code="rule_ncc_id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Network connectivity config ID stored within the rule object.</td>
</tr>
<tr>
    <td><CopyableCode code="connection_state" /></td>
    <td><CopyableCode code="string" /></td>
    <td>State of the AWS VPC endpoint connection (e.g. pending, available, rejected).</td>
</tr>
<tr>
    <td><CopyableCode code="endpoint_service" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Name of the AWS endpoint service this rule connects to.</td>
</tr>
<tr>
    <td><CopyableCode code="vpc_endpoint_id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>AWS VPC endpoint ID for this private endpoint rule.</td>
</tr>
<tr>
    <td><CopyableCode code="enabled" /></td>
    <td><CopyableCode code="boolean" /></td>
    <td>Whether this private endpoint rule is currently active.</td>
</tr>
<tr>
    <td><CopyableCode code="deactivated" /></td>
    <td><CopyableCode code="boolean" /></td>
    <td>Whether this private endpoint rule has been deactivated.</td>
</tr>
<tr>
    <td><CopyableCode code="resource_names" /></td>
    <td><CopyableCode code="array" /></td>
    <td>List of resource names associated with this private endpoint rule.</td>
</tr>
<tr>
    <td><CopyableCode code="domain_names" /></td>
    <td><CopyableCode code="array" /></td>
    <td>List of domain names routed through this private endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="error_message" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Error message if the private endpoint rule is in a failed state.</td>
</tr>
<tr>
    <td><CopyableCode code="creation_time" /></td>
    <td><CopyableCode code="integer" /></td>
    <td>Unix timestamp (ms) when the rule was created.</td>
</tr>
<tr>
    <td><CopyableCode code="updated_time" /></td>
    <td><CopyableCode code="integer" /></td>
    <td>Unix timestamp (ms) when the rule was last updated.</td>
</tr>
</tbody>
</table>

## SQL Definition

<Tabs
defaultValue="Sqlite3"
values={[
{ label: 'Sqlite3', value: 'Sqlite3' },
{ label: 'Postgres', value: 'Postgres' }
]}
>
<TabItem value="Sqlite3">

```sql
SELECT
  ncc.account_id,
  ncc.network_connectivity_config_id,
  ncc.name AS ncc_name,
  ncc.region,
  JSON_EXTRACT(r.value, '$.rule_id') AS rule_id,
  JSON_EXTRACT(r.value, '$.network_connectivity_config_id') AS rule_ncc_id,
  JSON_EXTRACT(r.value, '$.connection_state') AS connection_state,
  JSON_EXTRACT(r.value, '$.endpoint_service') AS endpoint_service,
  JSON_EXTRACT(r.value, '$.vpc_endpoint_id') AS vpc_endpoint_id,
  JSON_EXTRACT(r.value, '$.enabled') AS enabled,
  JSON_EXTRACT(r.value, '$.deactivated') AS deactivated,
  JSON_EXTRACT(r.value, '$.resource_names') AS resource_names,
  JSON_EXTRACT(r.value, '$.domain_names') AS domain_names,
  JSON_EXTRACT(r.value, '$.error_message') AS error_message,
  JSON_EXTRACT(r.value, '$.creation_time') AS creation_time,
  JSON_EXTRACT(r.value, '$.updated_time') AS updated_time
FROM databricks_account.settings.network_connectivity ncc,
     JSON_EACH(JSON_EXTRACT(ncc.egress_config, '$.target_rules.aws_private_endpoint_rules')) r
WHERE account_id = '{{ account_id }}'
```

</TabItem>
<TabItem value="Postgres">

```sql
SELECT
  ncc.account_id,
  ncc.network_connectivity_config_id,
  ncc.name AS ncc_name,
  ncc.region,
  r.value->>'rule_id' AS rule_id,
  r.value->>'network_connectivity_config_id' AS rule_ncc_id,
  r.value->>'connection_state' AS connection_state,
  r.value->>'endpoint_service' AS endpoint_service,
  r.value->>'vpc_endpoint_id' AS vpc_endpoint_id,
  (r.value->>'enabled')::boolean AS enabled,
  (r.value->>'deactivated')::boolean AS deactivated,
  r.value->'resource_names' AS resource_names,
  r.value->'domain_names' AS domain_names,
  r.value->>'error_message' AS error_message,
  (r.value->>'creation_time')::bigint AS creation_time,
  (r.value->>'updated_time')::bigint AS updated_time
FROM databricks_account.settings.network_connectivity ncc,
     jsonb_array_elements((ncc.egress_config->'target_rules'->'aws_private_endpoint_rules')::jsonb) AS r
WHERE account_id = '{{ account_id }}'
```

</TabItem>
</Tabs>
