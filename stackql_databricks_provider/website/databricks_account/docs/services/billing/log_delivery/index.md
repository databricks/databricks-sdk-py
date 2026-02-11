---
title: log_delivery
hide_title: false
hide_table_of_contents: false
keywords:
  - log_delivery
  - billing
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

Creates, updates, deletes, gets or lists a <code>log_delivery</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>log_delivery</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.billing.log_delivery" /></td></tr>
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
    "name": "account_id",
    "type": "string",
    "description": "Databricks account ID."
  },
  {
    "name": "config_id",
    "type": "string",
    "description": "The unique UUID of log delivery configuration"
  },
  {
    "name": "credentials_id",
    "type": "string",
    "description": "The ID for a method:credentials/create that represents the AWS IAM role with policy and trust relationship as described in the main billable usage documentation page. See [Configure billable usage delivery]. [Configure billable usage delivery]: https://docs.databricks.com/administration-guide/account-settings/billable-usage-delivery.html"
  },
  {
    "name": "storage_configuration_id",
    "type": "string",
    "description": "The ID for a method:storage/create that represents the S3 bucket with bucket policy as described in the main billable usage documentation page. See [Configure billable usage delivery]. [Configure billable usage delivery]: https://docs.databricks.com/administration-guide/account-settings/billable-usage-delivery.html"
  },
  {
    "name": "config_name",
    "type": "string",
    "description": "The optional human-readable name of the log delivery configuration. Defaults to empty."
  },
  {
    "name": "creation_time",
    "type": "integer",
    "description": "Time in epoch milliseconds when the log delivery configuration was created."
  },
  {
    "name": "delivery_path_prefix",
    "type": "string",
    "description": "The optional delivery path prefix within Amazon S3 storage. Defaults to empty, which means that logs are delivered to the root of the bucket. This must be a valid S3 object key. This must not start or end with a slash character."
  },
  {
    "name": "delivery_start_time",
    "type": "string",
    "description": "This field applies only if log_type is BILLABLE_USAGE. This is the optional start month and year for delivery, specified in YYYY-MM format. Defaults to current year and month. BILLABLE_USAGE logs are not available for usage before March 2019 (2019-03)."
  },
  {
    "name": "log_delivery_status",
    "type": "object",
    "description": "The LogDeliveryStatus of this log delivery configuration",
    "children": [
      {
        "name": "status",
        "type": "string",
        "description": "* The status string for log delivery. Possible values are: `CREATED`: There were no log delivery<br />attempts since the config was created. `SUCCEEDED`: The latest attempt of log delivery has<br />succeeded completely. `USER_FAILURE`: The latest attempt of log delivery failed because of<br />misconfiguration of customer provided permissions on role or storage. `SYSTEM_FAILURE`: The<br />latest attempt of log delivery failed because of an Databricks internal error. Contact support<br />if it doesn't go away soon. `NOT_FOUND`: The log delivery status as the configuration has been<br />disabled since the release of this feature or there are no workspaces in the account."
      },
      {
        "name": "message",
        "type": "string",
        "description": "Informative message about the latest log delivery attempt. If the log delivery fails with USER_FAILURE, error details will be provided for fixing misconfigurations in cloud permissions."
      },
      {
        "name": "last_attempt_time",
        "type": "string",
        "description": "The UTC time for the latest log delivery attempt."
      },
      {
        "name": "last_successful_attempt_time",
        "type": "string",
        "description": "The UTC time for the latest successful log delivery."
      }
    ]
  },
  {
    "name": "log_type",
    "type": "string",
    "description": "Log delivery type. Supported values are: * `BILLABLE_USAGE` — Configure [billable usage log delivery]. For the CSV schema, see the [View billable usage]. * `AUDIT_LOGS` — Configure [audit log delivery]. For the JSON schema, see [Configure audit logging] [Configure audit logging]: https://docs.databricks.com/administration-guide/account-settings/audit-logs.html [View billable usage]: https://docs.databricks.com/administration-guide/account-settings/usage.html [audit log delivery]: https://docs.databricks.com/administration-guide/account-settings/audit-logs.html [billable usage log delivery]: https://docs.databricks.com/administration-guide/account-settings/billable-usage-delivery.html"
  },
  {
    "name": "output_format",
    "type": "string",
    "description": "The file type of log delivery. * If `log_type` is `BILLABLE_USAGE`, this value must be `CSV`. Only the CSV (comma-separated values) format is supported. For the schema, see the [View billable usage] * If `log_type` is `AUDIT_LOGS`, this value must be `JSON`. Only the JSON (JavaScript Object Notation) format is supported. For the schema, see the [Configuring audit logs]. [Configuring audit logs]: https://docs.databricks.com/administration-guide/account-settings/audit-logs.html [View billable usage]: https://docs.databricks.com/administration-guide/account-settings/usage.html"
  },
  {
    "name": "status",
    "type": "string",
    "description": "Status of log delivery configuration. Set to `ENABLED` (enabled) or `DISABLED` (disabled). Defaults to `ENABLED`. You can [enable or disable the configuration](#operation/patch-log-delivery-config-status) later. Deletion of a configuration is not supported, so disable a log delivery configuration that is no longer needed."
  },
  {
    "name": "update_time",
    "type": "integer",
    "description": "Time in epoch milliseconds when the log delivery configuration was updated."
  },
  {
    "name": "workspace_ids_filter",
    "type": "array",
    "description": "Optional filter that specifies workspace IDs to deliver logs for. By default the workspace filter is empty and log delivery applies at the account level, delivering workspace-level logs for all workspaces in your account, plus account level logs. You can optionally set this field to an array of workspace IDs (each one is an `int64`) to which log delivery should apply, in which case only workspace-level logs relating to the specified workspaces are delivered. If you plan to use different log delivery configurations for different workspaces, set this field explicitly. Be aware that delivery configurations mentioning specific workspaces won't apply to new workspaces created in the future, and delivery won't include account level logs. For some types of Databricks deployments there is only one workspace per account ID, so this field is unnecessary."
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "account_id",
    "type": "string",
    "description": "Databricks account ID."
  },
  {
    "name": "config_id",
    "type": "string",
    "description": "The unique UUID of log delivery configuration"
  },
  {
    "name": "credentials_id",
    "type": "string",
    "description": "The ID for a method:credentials/create that represents the AWS IAM role with policy and trust relationship as described in the main billable usage documentation page. See [Configure billable usage delivery]. [Configure billable usage delivery]: https://docs.databricks.com/administration-guide/account-settings/billable-usage-delivery.html"
  },
  {
    "name": "storage_configuration_id",
    "type": "string",
    "description": "The ID for a method:storage/create that represents the S3 bucket with bucket policy as described in the main billable usage documentation page. See [Configure billable usage delivery]. [Configure billable usage delivery]: https://docs.databricks.com/administration-guide/account-settings/billable-usage-delivery.html"
  },
  {
    "name": "config_name",
    "type": "string",
    "description": "The optional human-readable name of the log delivery configuration. Defaults to empty."
  },
  {
    "name": "creation_time",
    "type": "integer",
    "description": "Time in epoch milliseconds when the log delivery configuration was created."
  },
  {
    "name": "delivery_path_prefix",
    "type": "string",
    "description": "The optional delivery path prefix within Amazon S3 storage. Defaults to empty, which means that logs are delivered to the root of the bucket. This must be a valid S3 object key. This must not start or end with a slash character."
  },
  {
    "name": "delivery_start_time",
    "type": "string",
    "description": "This field applies only if log_type is BILLABLE_USAGE. This is the optional start month and year for delivery, specified in YYYY-MM format. Defaults to current year and month. BILLABLE_USAGE logs are not available for usage before March 2019 (2019-03)."
  },
  {
    "name": "log_delivery_status",
    "type": "object",
    "description": "The LogDeliveryStatus of this log delivery configuration",
    "children": [
      {
        "name": "status",
        "type": "string",
        "description": "* The status string for log delivery. Possible values are: `CREATED`: There were no log delivery<br />attempts since the config was created. `SUCCEEDED`: The latest attempt of log delivery has<br />succeeded completely. `USER_FAILURE`: The latest attempt of log delivery failed because of<br />misconfiguration of customer provided permissions on role or storage. `SYSTEM_FAILURE`: The<br />latest attempt of log delivery failed because of an Databricks internal error. Contact support<br />if it doesn't go away soon. `NOT_FOUND`: The log delivery status as the configuration has been<br />disabled since the release of this feature or there are no workspaces in the account."
      },
      {
        "name": "message",
        "type": "string",
        "description": "Informative message about the latest log delivery attempt. If the log delivery fails with USER_FAILURE, error details will be provided for fixing misconfigurations in cloud permissions."
      },
      {
        "name": "last_attempt_time",
        "type": "string",
        "description": "The UTC time for the latest log delivery attempt."
      },
      {
        "name": "last_successful_attempt_time",
        "type": "string",
        "description": "The UTC time for the latest successful log delivery."
      }
    ]
  },
  {
    "name": "log_type",
    "type": "string",
    "description": "Log delivery type. Supported values are: * `BILLABLE_USAGE` — Configure [billable usage log delivery]. For the CSV schema, see the [View billable usage]. * `AUDIT_LOGS` — Configure [audit log delivery]. For the JSON schema, see [Configure audit logging] [Configure audit logging]: https://docs.databricks.com/administration-guide/account-settings/audit-logs.html [View billable usage]: https://docs.databricks.com/administration-guide/account-settings/usage.html [audit log delivery]: https://docs.databricks.com/administration-guide/account-settings/audit-logs.html [billable usage log delivery]: https://docs.databricks.com/administration-guide/account-settings/billable-usage-delivery.html"
  },
  {
    "name": "output_format",
    "type": "string",
    "description": "The file type of log delivery. * If `log_type` is `BILLABLE_USAGE`, this value must be `CSV`. Only the CSV (comma-separated values) format is supported. For the schema, see the [View billable usage] * If `log_type` is `AUDIT_LOGS`, this value must be `JSON`. Only the JSON (JavaScript Object Notation) format is supported. For the schema, see the [Configuring audit logs]. [Configuring audit logs]: https://docs.databricks.com/administration-guide/account-settings/audit-logs.html [View billable usage]: https://docs.databricks.com/administration-guide/account-settings/usage.html"
  },
  {
    "name": "status",
    "type": "string",
    "description": "Status of log delivery configuration. Set to `ENABLED` (enabled) or `DISABLED` (disabled). Defaults to `ENABLED`. You can [enable or disable the configuration](#operation/patch-log-delivery-config-status) later. Deletion of a configuration is not supported, so disable a log delivery configuration that is no longer needed."
  },
  {
    "name": "update_time",
    "type": "integer",
    "description": "Time in epoch milliseconds when the log delivery configuration was updated."
  },
  {
    "name": "workspace_ids_filter",
    "type": "array",
    "description": "Optional filter that specifies workspace IDs to deliver logs for. By default the workspace filter is empty and log delivery applies at the account level, delivering workspace-level logs for all workspaces in your account, plus account level logs. You can optionally set this field to an array of workspace IDs (each one is an `int64`) to which log delivery should apply, in which case only workspace-level logs relating to the specified workspaces are delivered. If you plan to use different log delivery configurations for different workspaces, set this field explicitly. Be aware that delivery configurations mentioning specific workspaces won't apply to new workspaces created in the future, and delivery won't include account level logs. For some types of Databricks deployments there is only one workspace per account ID, so this field is unnecessary."
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-log_delivery_configuration_id"><code>log_delivery_configuration_id</code></a></td>
    <td></td>
    <td>Gets a Databricks log delivery configuration object for an account, both specified by ID.<br /><br />:param log_delivery_configuration_id: str<br />  The log delivery configuration id of customer<br /><br />:returns: :class:`GetLogDeliveryConfigurationResponse`</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-credentials_id"><code>credentials_id</code></a>, <a href="#parameter-page_token"><code>page_token</code></a>, <a href="#parameter-status"><code>status</code></a>, <a href="#parameter-storage_configuration_id"><code>storage_configuration_id</code></a></td>
    <td>Gets all Databricks log delivery configurations associated with an account specified by ID.<br /><br />:param credentials_id: str (optional)<br />  The Credentials id to filter the search results with<br />:param page_token: str (optional)<br />  A page token received from a previous get all budget configurations call. This token can be used to<br />  retrieve the subsequent page. Requests first page if absent.<br />:param status: :class:`LogDeliveryConfigStatus` (optional)<br />  The log delivery status to filter the search results with<br />:param storage_configuration_id: str (optional)<br />  The Storage Configuration id to filter the search results with<br /><br />:returns: Iterator over :class:`LogDeliveryConfiguration`</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-data__log_delivery_configuration"><code>data__log_delivery_configuration</code></a></td>
    <td></td>
    <td>Creates a new Databricks log delivery configuration to enable delivery of the specified type of logs<br />to your storage location. This requires that you already created a [credential<br />object](:method:Credentials/Create) (which encapsulates a cross-account service IAM role) and a<br />[storage configuration object](:method:Storage/Create) (which encapsulates an S3 bucket).<br /><br />For full details, including the required IAM role policies and bucket policies, see [Deliver and<br />access billable usage logs] or [Configure audit logging].<br /><br />**Note**: There is a limit on the number of log delivery configurations available per account (each<br />limit applies separately to each log type including billable usage and audit logs). You can create a<br />maximum of two enabled account-level delivery configurations (configurations without a workspace<br />filter) per type. Additionally, you can create two enabled workspace-level delivery configurations per<br />workspace for each log type, which means that the same workspace ID can occur in the workspace filter<br />for no more than two delivery configurations per log type.<br /><br />You cannot delete a log delivery configuration, but you can disable it (see [Enable or disable log<br />delivery configuration](:method:LogDelivery/PatchStatus)).<br /><br />[Configure audit logging]: https://docs.databricks.com/administration-guide/account-settings/audit-logs.html<br />[Deliver and access billable usage logs]: https://docs.databricks.com/administration-guide/account-settings/billable-usage-delivery.html<br /><br />:param log_delivery_configuration: :class:`CreateLogDeliveryConfigurationParams`<br /><br />:returns: :class:`WrappedLogDeliveryConfiguration`</td>
</tr>
<tr>
    <td><a href="#patch_status"><CopyableCode code="patch_status" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-log_delivery_configuration_id"><code>log_delivery_configuration_id</code></a>, <a href="#parameter-status"><code>status</code></a></td>
    <td></td>
    <td>Enables or disables a log delivery configuration. Deletion of delivery configurations is not<br />supported, so disable log delivery configurations that are no longer needed. Note that you can't<br />re-enable a delivery configuration if this would violate the delivery configuration limits described<br />under [Create log delivery](:method:LogDelivery/Create).<br /><br />:param log_delivery_configuration_id: str<br />  The log delivery configuration id of customer<br />:param status: :class:`LogDeliveryConfigStatus`<br />  Status of log delivery configuration. Set to `ENABLED` (enabled) or `DISABLED` (disabled). Defaults<br />  to `ENABLED`. You can [enable or disable the<br />  configuration](#operation/patch-log-delivery-config-status) later. Deletion of a configuration is<br />  not supported, so disable a log delivery configuration that is no longer needed.</td>
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
<tr id="parameter-log_delivery_configuration_id">
    <td><CopyableCode code="log_delivery_configuration_id" /></td>
    <td><code>string</code></td>
    <td>The log delivery configuration id of customer</td>
</tr>
<tr id="parameter-credentials_id">
    <td><CopyableCode code="credentials_id" /></td>
    <td><code>string</code></td>
    <td>The Credentials id to filter the search results with</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>A page token received from a previous get all budget configurations call. This token can be used to retrieve the subsequent page. Requests first page if absent.</td>
</tr>
<tr id="parameter-status">
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The log delivery status to filter the search results with</td>
</tr>
<tr id="parameter-storage_configuration_id">
    <td><CopyableCode code="storage_configuration_id" /></td>
    <td><code>string</code></td>
    <td>The Storage Configuration id to filter the search results with</td>
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

Gets a Databricks log delivery configuration object for an account, both specified by ID.<br /><br />:param log_delivery_configuration_id: str<br />  The log delivery configuration id of customer<br /><br />:returns: :class:`GetLogDeliveryConfigurationResponse`

```sql
SELECT
account_id,
config_id,
credentials_id,
storage_configuration_id,
config_name,
creation_time,
delivery_path_prefix,
delivery_start_time,
log_delivery_status,
log_type,
output_format,
status,
update_time,
workspace_ids_filter
FROM databricks_account.billing.log_delivery
WHERE account_id = '{{ account_id }}' -- required
AND log_delivery_configuration_id = '{{ log_delivery_configuration_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets all Databricks log delivery configurations associated with an account specified by ID.<br /><br />:param credentials_id: str (optional)<br />  The Credentials id to filter the search results with<br />:param page_token: str (optional)<br />  A page token received from a previous get all budget configurations call. This token can be used to<br />  retrieve the subsequent page. Requests first page if absent.<br />:param status: :class:`LogDeliveryConfigStatus` (optional)<br />  The log delivery status to filter the search results with<br />:param storage_configuration_id: str (optional)<br />  The Storage Configuration id to filter the search results with<br /><br />:returns: Iterator over :class:`LogDeliveryConfiguration`

```sql
SELECT
account_id,
config_id,
credentials_id,
storage_configuration_id,
config_name,
creation_time,
delivery_path_prefix,
delivery_start_time,
log_delivery_status,
log_type,
output_format,
status,
update_time,
workspace_ids_filter
FROM databricks_account.billing.log_delivery
WHERE account_id = '{{ account_id }}' -- required
AND credentials_id = '{{ credentials_id }}'
AND page_token = '{{ page_token }}'
AND status = '{{ status }}'
AND storage_configuration_id = '{{ storage_configuration_id }}'
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

Creates a new Databricks log delivery configuration to enable delivery of the specified type of logs<br />to your storage location. This requires that you already created a [credential<br />object](:method:Credentials/Create) (which encapsulates a cross-account service IAM role) and a<br />[storage configuration object](:method:Storage/Create) (which encapsulates an S3 bucket).<br /><br />For full details, including the required IAM role policies and bucket policies, see [Deliver and<br />access billable usage logs] or [Configure audit logging].<br /><br />**Note**: There is a limit on the number of log delivery configurations available per account (each<br />limit applies separately to each log type including billable usage and audit logs). You can create a<br />maximum of two enabled account-level delivery configurations (configurations without a workspace<br />filter) per type. Additionally, you can create two enabled workspace-level delivery configurations per<br />workspace for each log type, which means that the same workspace ID can occur in the workspace filter<br />for no more than two delivery configurations per log type.<br /><br />You cannot delete a log delivery configuration, but you can disable it (see [Enable or disable log<br />delivery configuration](:method:LogDelivery/PatchStatus)).<br /><br />[Configure audit logging]: https://docs.databricks.com/administration-guide/account-settings/audit-logs.html<br />[Deliver and access billable usage logs]: https://docs.databricks.com/administration-guide/account-settings/billable-usage-delivery.html<br /><br />:param log_delivery_configuration: :class:`CreateLogDeliveryConfigurationParams`<br /><br />:returns: :class:`WrappedLogDeliveryConfiguration`

```sql
INSERT INTO databricks_account.billing.log_delivery (
data__log_delivery_configuration,
account_id
)
SELECT 
'{{ log_delivery_configuration }}' /* required */,
'{{ account_id }}'
RETURNING
log_delivery_configuration
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: log_delivery
  props:
    - name: account_id
      value: string
      description: Required parameter for the log_delivery resource.
    - name: log_delivery_configuration
      value: string
      description: |
        :returns: :class:`WrappedLogDeliveryConfiguration`
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="patch_status"
    values={[
        { label: 'patch_status', value: 'patch_status' }
    ]}
>
<TabItem value="patch_status">

Enables or disables a log delivery configuration. Deletion of delivery configurations is not<br />supported, so disable log delivery configurations that are no longer needed. Note that you can't<br />re-enable a delivery configuration if this would violate the delivery configuration limits described<br />under [Create log delivery](:method:LogDelivery/Create).<br /><br />:param log_delivery_configuration_id: str<br />  The log delivery configuration id of customer<br />:param status: :class:`LogDeliveryConfigStatus`<br />  Status of log delivery configuration. Set to `ENABLED` (enabled) or `DISABLED` (disabled). Defaults<br />  to `ENABLED`. You can [enable or disable the<br />  configuration](#operation/patch-log-delivery-config-status) later. Deletion of a configuration is<br />  not supported, so disable a log delivery configuration that is no longer needed.

```sql
EXEC databricks_account.billing.log_delivery.patch_status 
@account_id='{{ account_id }}' --required, 
@log_delivery_configuration_id='{{ log_delivery_configuration_id }}' --required 
@@json=
'{
"status": "{{ status }}"
}'
;
```
</TabItem>
</Tabs>
