---
title: vw_vpc_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - vw_vpc_endpoints
  - provisioning
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

Creates, updates, deletes, gets or lists a <code>vw_vpc_endpoints</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="vw_vpc_endpoints" /></td></tr>
<tr><td><b>Type</b></td><td>View</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.provisioning.vw_vpc_endpoints" /></td></tr>
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
    <td><CopyableCode code="vpc_endpoint_id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Unique Databricks identifier for the VPC endpoint configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="vpc_endpoint_name" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Human-readable name of the VPC endpoint configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="region" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Cloud region where the VPC endpoint is deployed.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Current state of the VPC endpoint (e.g. available, pending, rejected).</td>
</tr>
<tr>
    <td><CopyableCode code="use_case" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Traffic type this endpoint handles (e.g. dataplane-relay, workspace-access).</td>
</tr>
<tr>
    <td><CopyableCode code="aws_account_id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>AWS account ID that owns the VPC endpoint (AWS only).</td>
</tr>
<tr>
    <td><CopyableCode code="aws_endpoint_service_id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>ID of the AWS endpoint service this VPC endpoint connects to (AWS only).</td>
</tr>
<tr>
    <td><CopyableCode code="aws_vpc_endpoint_id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>AWS VPC endpoint ID (AWS only).</td>
</tr>
<tr>
    <td><CopyableCode code="gcp_project_id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>GCP project ID containing the PSC endpoint (GCP only).</td>
</tr>
<tr>
    <td><CopyableCode code="gcp_psc_endpoint_name" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Name of the GCP Private Service Connect endpoint (GCP only).</td>
</tr>
<tr>
    <td><CopyableCode code="gcp_endpoint_region" /></td>
    <td><CopyableCode code="string" /></td>
    <td>GCP region where the PSC endpoint is deployed (GCP only).</td>
</tr>
<tr>
    <td><CopyableCode code="gcp_psc_connection_id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Connection ID of the GCP PSC endpoint (GCP only).</td>
</tr>
<tr>
    <td><CopyableCode code="gcp_service_attachment_id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>ID of the GCP service attachment the PSC endpoint connects to (GCP only).</td>
</tr>
<tr>
    <td><CopyableCode code="cloud_type" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Derived cloud provider for this VPC endpoint - one of AWS, GCP, or UNKNOWN.</td>
</tr>
</tbody>
</table>

## Required Parameters

The following parameters are required by this view:

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
</tbody>
</table>

## `SELECT` Examples

```sql
SELECT
  account_id,
  vpc_endpoint_id,
  vpc_endpoint_name,
  region,
  state,
  use_case,
  aws_account_id,
  aws_endpoint_service_id,
  aws_vpc_endpoint_id,
  gcp_project_id,
  gcp_psc_endpoint_name,
  gcp_endpoint_region,
  gcp_psc_connection_id,
  gcp_service_attachment_id,
  cloud_type
FROM databricks_account.provisioning.vw_vpc_endpoints
WHERE account_id = '{{ account_id }}';
```

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
  v.account_id,
  v.vpc_endpoint_id,
  v.vpc_endpoint_name,
  v.region,
  v.state,
  v.use_case,
  v.aws_account_id,
  v.aws_endpoint_service_id,
  v.aws_vpc_endpoint_id,
  JSON_EXTRACT(v.gcp_vpc_endpoint_info, '$.project_id') AS gcp_project_id,
  JSON_EXTRACT(v.gcp_vpc_endpoint_info, '$.psc_endpoint_name') AS gcp_psc_endpoint_name,
  JSON_EXTRACT(v.gcp_vpc_endpoint_info, '$.endpoint_region') AS gcp_endpoint_region,
  JSON_EXTRACT(v.gcp_vpc_endpoint_info, '$.psc_connection_id') AS gcp_psc_connection_id,
  JSON_EXTRACT(v.gcp_vpc_endpoint_info, '$.service_attachment_id') AS gcp_service_attachment_id,
  CASE
    WHEN v.aws_vpc_endpoint_id IS NOT NULL THEN 'AWS'
    WHEN v.gcp_vpc_endpoint_info IS NOT NULL THEN 'GCP'
    ELSE 'UNKNOWN'
  END AS cloud_type
FROM databricks_account.provisioning.vpc_endpoints v
WHERE account_id = '{{ account_id }}'
```

</TabItem>
<TabItem value="Postgres">

```sql
SELECT
  v.account_id,
  v.vpc_endpoint_id,
  v.vpc_endpoint_name,
  v.region,
  v.state,
  v.use_case,
  v.aws_account_id,
  v.aws_endpoint_service_id,
  v.aws_vpc_endpoint_id,
  v.gcp_vpc_endpoint_info->>'project_id' AS gcp_project_id,
  v.gcp_vpc_endpoint_info->>'psc_endpoint_name' AS gcp_psc_endpoint_name,
  v.gcp_vpc_endpoint_info->>'endpoint_region' AS gcp_endpoint_region,
  v.gcp_vpc_endpoint_info->>'psc_connection_id' AS gcp_psc_connection_id,
  v.gcp_vpc_endpoint_info->>'service_attachment_id' AS gcp_service_attachment_id,
  CASE
    WHEN v.aws_vpc_endpoint_id IS NOT NULL THEN 'AWS'
    WHEN v.gcp_vpc_endpoint_info IS NOT NULL THEN 'GCP'
    ELSE 'UNKNOWN'
  END AS cloud_type
FROM databricks_account.provisioning.vpc_endpoints v
WHERE account_id = '{{ account_id }}'
```

</TabItem>
</Tabs>
