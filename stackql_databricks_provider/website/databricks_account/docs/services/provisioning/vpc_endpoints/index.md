---
title: vpc_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - vpc_endpoints
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import SchemaTable from '@site/src/components/SchemaTable/SchemaTable';

Creates, updates, deletes, gets or lists a <code>vpc_endpoints</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpc_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.provisioning.vpc_endpoints" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="vpc_endpoints_get"
    values={[
        { label: 'vpc_endpoints_get', value: 'vpc_endpoints_get' },
        { label: 'vpc_endpoints_list', value: 'vpc_endpoints_list' }
    ]}
>
<TabItem value="vpc_endpoints_get">

<SchemaTable fields={[
  {
    "name": "account_id",
    "type": "string",
    "description": "The Databricks account ID that hosts the VPC endpoint configuration. TODO - This may signal an OpenAPI diff; it does not show up in the generated spec"
  },
  {
    "name": "aws_account_id",
    "type": "string",
    "description": "The AWS Account in which the VPC endpoint object exists."
  },
  {
    "name": "aws_endpoint_service_id",
    "type": "string",
    "description": "The ID of the Databricks [endpoint service] that this VPC endpoint is connected to. For a list of endpoint service IDs for each supported AWS region, see the [Databricks PrivateLink documentation]. [Databricks PrivateLink documentation]: https://docs.databricks.com/administration-guide/cloud-configurations/aws/privatelink.html [endpoint service]: https://docs.aws.amazon.com/vpc/latest/privatelink/endpoint-service.html"
  },
  {
    "name": "aws_vpc_endpoint_id",
    "type": "string",
    "description": "The ID of the VPC endpoint object in AWS."
  },
  {
    "name": "vpc_endpoint_id",
    "type": "string",
    "description": "Databricks VPC endpoint ID. This is the Databricks-specific name of the VPC endpoint. Do not confuse this with the `aws_vpc_endpoint_id`, which is the ID within AWS of the VPC endpoint."
  },
  {
    "name": "vpc_endpoint_name",
    "type": "string",
    "description": "The human-readable name of the storage configuration."
  },
  {
    "name": "gcp_vpc_endpoint_info",
    "type": "object",
    "description": "The cloud info of this vpc endpoint. Info for a GCP vpc endpoint.",
    "children": [
      {
        "name": "project_id",
        "type": "string",
        "description": ""
      },
      {
        "name": "psc_endpoint_name",
        "type": "string",
        "description": ""
      },
      {
        "name": "endpoint_region",
        "type": "string",
        "description": ""
      },
      {
        "name": "psc_connection_id",
        "type": "string",
        "description": ""
      },
      {
        "name": "service_attachment_id",
        "type": "string",
        "description": ""
      }
    ]
  },
  {
    "name": "region",
    "type": "string",
    "description": "The AWS region in which this VPC endpoint object exists."
  },
  {
    "name": "state",
    "type": "string",
    "description": "The current state (such as `available` or `rejected`) of the VPC endpoint. Derived from AWS. For the full set of values, see [AWS DescribeVpcEndpoint documentation]. [AWS DescribeVpcEndpoint documentation]: https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-vpc-endpoints.html"
  },
  {
    "name": "use_case",
    "type": "string",
    "description": "This enumeration represents the type of Databricks VPC endpoint service that was used when creating this VPC endpoint. If the VPC endpoint connects to the Databricks control plane for either the front-end connection or the back-end REST API connection, the value is WORKSPACE_ACCESS. If the VPC endpoint connects to the Databricks workspace for the back-end secure cluster connectivity relay, the value is DATAPLANE_RELAY_ACCESS."
  }
]} />
</TabItem>
<TabItem value="vpc_endpoints_list">

<SchemaTable fields={[
  {
    "name": "account_id",
    "type": "string",
    "description": "The Databricks account ID that hosts the VPC endpoint configuration. TODO - This may signal an OpenAPI diff; it does not show up in the generated spec"
  },
  {
    "name": "aws_account_id",
    "type": "string",
    "description": "The AWS Account in which the VPC endpoint object exists."
  },
  {
    "name": "aws_endpoint_service_id",
    "type": "string",
    "description": "The ID of the Databricks [endpoint service] that this VPC endpoint is connected to. For a list of endpoint service IDs for each supported AWS region, see the [Databricks PrivateLink documentation]. [Databricks PrivateLink documentation]: https://docs.databricks.com/administration-guide/cloud-configurations/aws/privatelink.html [endpoint service]: https://docs.aws.amazon.com/vpc/latest/privatelink/endpoint-service.html"
  },
  {
    "name": "aws_vpc_endpoint_id",
    "type": "string",
    "description": "The ID of the VPC endpoint object in AWS."
  },
  {
    "name": "vpc_endpoint_id",
    "type": "string",
    "description": "Databricks VPC endpoint ID. This is the Databricks-specific name of the VPC endpoint. Do not confuse this with the `aws_vpc_endpoint_id`, which is the ID within AWS of the VPC endpoint."
  },
  {
    "name": "vpc_endpoint_name",
    "type": "string",
    "description": "The human-readable name of the storage configuration."
  },
  {
    "name": "gcp_vpc_endpoint_info",
    "type": "object",
    "description": "The cloud info of this vpc endpoint. Info for a GCP vpc endpoint.",
    "children": [
      {
        "name": "project_id",
        "type": "string",
        "description": ""
      },
      {
        "name": "psc_endpoint_name",
        "type": "string",
        "description": ""
      },
      {
        "name": "endpoint_region",
        "type": "string",
        "description": ""
      },
      {
        "name": "psc_connection_id",
        "type": "string",
        "description": ""
      },
      {
        "name": "service_attachment_id",
        "type": "string",
        "description": ""
      }
    ]
  },
  {
    "name": "region",
    "type": "string",
    "description": "The AWS region in which this VPC endpoint object exists."
  },
  {
    "name": "state",
    "type": "string",
    "description": "The current state (such as `available` or `rejected`) of the VPC endpoint. Derived from AWS. For the full set of values, see [AWS DescribeVpcEndpoint documentation]. [AWS DescribeVpcEndpoint documentation]: https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-vpc-endpoints.html"
  },
  {
    "name": "use_case",
    "type": "string",
    "description": "This enumeration represents the type of Databricks VPC endpoint service that was used when creating this VPC endpoint. If the VPC endpoint connects to the Databricks control plane for either the front-end connection or the back-end REST API connection, the value is WORKSPACE_ACCESS. If the VPC endpoint connects to the Databricks workspace for the back-end secure cluster connectivity relay, the value is DATAPLANE_RELAY_ACCESS."
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
    <td><a href="#vpc_endpoints_get"><CopyableCode code="vpc_endpoints_get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-vpc_endpoint_id"><code>vpc_endpoint_id</code></a></td>
    <td></td>
    <td>Gets a VPC endpoint configuration, which represents a [VPC endpoint] object in AWS used to communicate<br />privately with Databricks over [AWS PrivateLink].<br /><br />[AWS PrivateLink]: https://aws.amazon.com/privatelink<br />[VPC endpoint]: https://docs.aws.amazon.com/vpc/latest/privatelink/concepts.html<br /><br />:param vpc_endpoint_id: str<br />  Databricks VPC endpoint ID.<br /><br />:returns: :class:`VpcEndpoint`</td>
</tr>
<tr>
    <td><a href="#vpc_endpoints_list"><CopyableCode code="vpc_endpoints_list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Lists Databricks VPC endpoint configurations for an account.<br /><br /><br />:returns: Iterator over :class:`VpcEndpoint`</td>
</tr>
<tr>
    <td><a href="#vpc_endpoints_create"><CopyableCode code="vpc_endpoints_create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Creates a VPC endpoint configuration, which represents a [VPC endpoint] object in AWS used to<br />communicate privately with Databricks over [AWS PrivateLink].<br /><br />After you create the VPC endpoint configuration, the Databricks [endpoint service] automatically<br />accepts the VPC endpoint.<br /><br />Before configuring PrivateLink, read the [Databricks article about PrivateLink].<br /><br />[AWS PrivateLink]: https://aws.amazon.com/privatelink<br />[Databricks article about PrivateLink]: https://docs.databricks.com/administration-guide/cloud-configurations/aws/privatelink.html<br />[VPC endpoint]: https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints.html<br />[endpoint service]: https://docs.aws.amazon.com/vpc/latest/privatelink/privatelink-share-your-services.html<br /><br />:param aws_vpc_endpoint_id: str (optional)<br />  The ID of the VPC endpoint object in AWS.<br />:param gcp_vpc_endpoint_info: :class:`GcpVpcEndpointInfo` (optional)<br />  The cloud info of this vpc endpoint.<br />:param region: str (optional)<br />  The region in which this VPC endpoint object exists.<br />:param vpc_endpoint_name: str (optional)<br />  The human-readable name of the storage configuration.<br /><br />:returns: :class:`VpcEndpoint`</td>
</tr>
<tr>
    <td><a href="#vpc_endpoints_delete"><CopyableCode code="vpc_endpoints_delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-vpc_endpoint_id"><code>vpc_endpoint_id</code></a></td>
    <td></td>
    <td>Deletes a Databricks VPC endpoint configuration. You cannot delete a VPC endpoint configuration that<br />is associated with any workspace.<br /><br />:param vpc_endpoint_id: str<br /><br />:returns: :class:`VpcEndpoint`</td>
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
<tr id="parameter-vpc_endpoint_id">
    <td><CopyableCode code="vpc_endpoint_id" /></td>
    <td><code>string</code></td>
    <td>:returns: :class:`VpcEndpoint`</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="vpc_endpoints_get"
    values={[
        { label: 'vpc_endpoints_get', value: 'vpc_endpoints_get' },
        { label: 'vpc_endpoints_list', value: 'vpc_endpoints_list' }
    ]}
>
<TabItem value="vpc_endpoints_get">

Gets a VPC endpoint configuration, which represents a [VPC endpoint] object in AWS used to communicate<br />privately with Databricks over [AWS PrivateLink].<br /><br />[AWS PrivateLink]: https://aws.amazon.com/privatelink<br />[VPC endpoint]: https://docs.aws.amazon.com/vpc/latest/privatelink/concepts.html<br /><br />:param vpc_endpoint_id: str<br />  Databricks VPC endpoint ID.<br /><br />:returns: :class:`VpcEndpoint`

```sql
SELECT
account_id,
aws_account_id,
aws_endpoint_service_id,
aws_vpc_endpoint_id,
vpc_endpoint_id,
vpc_endpoint_name,
gcp_vpc_endpoint_info,
region,
state,
use_case
FROM databricks_account.provisioning.vpc_endpoints
WHERE account_id = '{{ account_id }}' -- required
AND vpc_endpoint_id = '{{ vpc_endpoint_id }}' -- required
;
```
</TabItem>
<TabItem value="vpc_endpoints_list">

Lists Databricks VPC endpoint configurations for an account.<br /><br /><br />:returns: Iterator over :class:`VpcEndpoint`

```sql
SELECT
account_id,
aws_account_id,
aws_endpoint_service_id,
aws_vpc_endpoint_id,
vpc_endpoint_id,
vpc_endpoint_name,
gcp_vpc_endpoint_info,
region,
state,
use_case
FROM databricks_account.provisioning.vpc_endpoints
WHERE account_id = '{{ account_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="vpc_endpoints_create"
    values={[
        { label: 'vpc_endpoints_create', value: 'vpc_endpoints_create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="vpc_endpoints_create">

Creates a VPC endpoint configuration, which represents a [VPC endpoint] object in AWS used to<br />communicate privately with Databricks over [AWS PrivateLink].<br /><br />After you create the VPC endpoint configuration, the Databricks [endpoint service] automatically<br />accepts the VPC endpoint.<br /><br />Before configuring PrivateLink, read the [Databricks article about PrivateLink].<br /><br />[AWS PrivateLink]: https://aws.amazon.com/privatelink<br />[Databricks article about PrivateLink]: https://docs.databricks.com/administration-guide/cloud-configurations/aws/privatelink.html<br />[VPC endpoint]: https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints.html<br />[endpoint service]: https://docs.aws.amazon.com/vpc/latest/privatelink/privatelink-share-your-services.html<br /><br />:param aws_vpc_endpoint_id: str (optional)<br />  The ID of the VPC endpoint object in AWS.<br />:param gcp_vpc_endpoint_info: :class:`GcpVpcEndpointInfo` (optional)<br />  The cloud info of this vpc endpoint.<br />:param region: str (optional)<br />  The region in which this VPC endpoint object exists.<br />:param vpc_endpoint_name: str (optional)<br />  The human-readable name of the storage configuration.<br /><br />:returns: :class:`VpcEndpoint`

```sql
INSERT INTO databricks_account.provisioning.vpc_endpoints (
data__aws_vpc_endpoint_id,
data__gcp_vpc_endpoint_info,
data__region,
data__vpc_endpoint_name,
account_id
)
SELECT 
'{{ aws_vpc_endpoint_id }}',
'{{ gcp_vpc_endpoint_info }}',
'{{ region }}',
'{{ vpc_endpoint_name }}',
'{{ account_id }}'
RETURNING
account_id,
aws_account_id,
aws_endpoint_service_id,
aws_vpc_endpoint_id,
vpc_endpoint_id,
vpc_endpoint_name,
gcp_vpc_endpoint_info,
region,
state,
use_case
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: vpc_endpoints
  props:
    - name: account_id
      value: string
      description: Required parameter for the vpc_endpoints resource.
    - name: aws_vpc_endpoint_id
      value: string
      description: |
        The ID of the VPC endpoint object in AWS.
    - name: gcp_vpc_endpoint_info
      value: string
      description: |
        The cloud info of this vpc endpoint.
    - name: region
      value: string
      description: |
        The region in which this VPC endpoint object exists.
    - name: vpc_endpoint_name
      value: string
      description: |
        The human-readable name of the storage configuration.
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="vpc_endpoints_delete"
    values={[
        { label: 'vpc_endpoints_delete', value: 'vpc_endpoints_delete' }
    ]}
>
<TabItem value="vpc_endpoints_delete">

Deletes a Databricks VPC endpoint configuration. You cannot delete a VPC endpoint configuration that<br />is associated with any workspace.<br /><br />:param vpc_endpoint_id: str<br /><br />:returns: :class:`VpcEndpoint`

```sql
DELETE FROM databricks_account.provisioning.vpc_endpoints
WHERE account_id = '{{ account_id }}' --required
AND vpc_endpoint_id = '{{ vpc_endpoint_id }}' --required
;
```
</TabItem>
</Tabs>
