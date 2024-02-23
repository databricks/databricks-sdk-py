# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

from __future__ import annotations

import logging
from dataclasses import dataclass
from enum import Enum
from typing import BinaryIO, Dict, Iterator, List, Optional

from ._internal import _enum, _from_dict, _repeated_dict

_LOG = logging.getLogger('databricks.sdk')

# all definitions in this file are in alphabetical order


@dataclass
class Budget:
    """Budget configuration to be created."""

    name: str
    """Human-readable name of the budget."""

    period: str
    """Period length in years, months, weeks and/or days. Examples: `1 month`, `30 days`, `1 year, 2
    months, 1 week, 2 days`"""

    start_date: str
    """Start date of the budget period calculation."""

    target_amount: str
    """Target amount of the budget per period in USD."""

    filter: str
    """SQL-like filter expression with workspaceId, SKU and tag. Usage in your account that matches
    this expression will be counted in this budget.
    
    Supported properties on left-hand side of comparison: * `workspaceId` - the ID of the workspace
    * `sku` - SKU of the cluster, e.g. `STANDARD_ALL_PURPOSE_COMPUTE` * `tag.tagName`, `tag.'tag
    name'` - tag of the cluster
    
    Supported comparison operators: * `=` - equal * `!=` - not equal
    
    Supported logical operators: `AND`, `OR`.
    
    Examples: * `workspaceId=123 OR (sku='STANDARD_ALL_PURPOSE_COMPUTE' AND tag.'my tag'='my
    value')` * `workspaceId!=456` * `sku='STANDARD_ALL_PURPOSE_COMPUTE' OR
    sku='PREMIUM_ALL_PURPOSE_COMPUTE'` * `tag.name1='value1' AND tag.name2='value2'`"""

    alerts: Optional[List[BudgetAlert]] = None

    end_date: Optional[str] = None
    """Optional end date of the budget."""

    def as_dict(self) -> dict:
        """Serializes the Budget into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.alerts: body['alerts'] = [v.as_dict() for v in self.alerts]
        if self.end_date is not None: body['end_date'] = self.end_date
        if self.filter is not None: body['filter'] = self.filter
        if self.name is not None: body['name'] = self.name
        if self.period is not None: body['period'] = self.period
        if self.start_date is not None: body['start_date'] = self.start_date
        if self.target_amount is not None: body['target_amount'] = self.target_amount
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> Budget:
        """Deserializes the Budget from a dictionary."""
        return cls(alerts=_repeated_dict(d, 'alerts', BudgetAlert),
                   end_date=d.get('end_date', None),
                   filter=d.get('filter', None),
                   name=d.get('name', None),
                   period=d.get('period', None),
                   start_date=d.get('start_date', None),
                   target_amount=d.get('target_amount', None))


@dataclass
class BudgetAlert:
    email_notifications: Optional[List[str]] = None
    """List of email addresses to be notified when budget percentage is exceeded in the given period."""

    min_percentage: Optional[int] = None
    """Percentage of the target amount used in the currect period that will trigger a notification."""

    def as_dict(self) -> dict:
        """Serializes the BudgetAlert into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.email_notifications: body['email_notifications'] = [v for v in self.email_notifications]
        if self.min_percentage is not None: body['min_percentage'] = self.min_percentage
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> BudgetAlert:
        """Deserializes the BudgetAlert from a dictionary."""
        return cls(email_notifications=d.get('email_notifications', None),
                   min_percentage=d.get('min_percentage', None))


@dataclass
class BudgetList:
    """List of budgets."""

    budgets: Optional[List[BudgetWithStatus]] = None

    def as_dict(self) -> dict:
        """Serializes the BudgetList into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.budgets: body['budgets'] = [v.as_dict() for v in self.budgets]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> BudgetList:
        """Deserializes the BudgetList from a dictionary."""
        return cls(budgets=_repeated_dict(d, 'budgets', BudgetWithStatus))


@dataclass
class BudgetWithStatus:
    """Budget configuration with daily status."""

    alerts: Optional[List[BudgetAlert]] = None

    budget_id: Optional[str] = None

    creation_time: Optional[str] = None

    end_date: Optional[str] = None
    """Optional end date of the budget."""

    filter: Optional[str] = None
    """SQL-like filter expression with workspaceId, SKU and tag. Usage in your account that matches
    this expression will be counted in this budget.
    
    Supported properties on left-hand side of comparison: * `workspaceId` - the ID of the workspace
    * `sku` - SKU of the cluster, e.g. `STANDARD_ALL_PURPOSE_COMPUTE` * `tag.tagName`, `tag.'tag
    name'` - tag of the cluster
    
    Supported comparison operators: * `=` - equal * `!=` - not equal
    
    Supported logical operators: `AND`, `OR`.
    
    Examples: * `workspaceId=123 OR (sku='STANDARD_ALL_PURPOSE_COMPUTE' AND tag.'my tag'='my
    value')` * `workspaceId!=456` * `sku='STANDARD_ALL_PURPOSE_COMPUTE' OR
    sku='PREMIUM_ALL_PURPOSE_COMPUTE'` * `tag.name1='value1' AND tag.name2='value2'`"""

    name: Optional[str] = None
    """Human-readable name of the budget."""

    period: Optional[str] = None
    """Period length in years, months, weeks and/or days. Examples: `1 month`, `30 days`, `1 year, 2
    months, 1 week, 2 days`"""

    start_date: Optional[str] = None
    """Start date of the budget period calculation."""

    status_daily: Optional[List[BudgetWithStatusStatusDailyItem]] = None
    """Amount used in the budget for each day (noncumulative)."""

    target_amount: Optional[str] = None
    """Target amount of the budget per period in USD."""

    update_time: Optional[str] = None

    def as_dict(self) -> dict:
        """Serializes the BudgetWithStatus into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.alerts: body['alerts'] = [v.as_dict() for v in self.alerts]
        if self.budget_id is not None: body['budget_id'] = self.budget_id
        if self.creation_time is not None: body['creation_time'] = self.creation_time
        if self.end_date is not None: body['end_date'] = self.end_date
        if self.filter is not None: body['filter'] = self.filter
        if self.name is not None: body['name'] = self.name
        if self.period is not None: body['period'] = self.period
        if self.start_date is not None: body['start_date'] = self.start_date
        if self.status_daily: body['status_daily'] = [v.as_dict() for v in self.status_daily]
        if self.target_amount is not None: body['target_amount'] = self.target_amount
        if self.update_time is not None: body['update_time'] = self.update_time
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> BudgetWithStatus:
        """Deserializes the BudgetWithStatus from a dictionary."""
        return cls(alerts=_repeated_dict(d, 'alerts', BudgetAlert),
                   budget_id=d.get('budget_id', None),
                   creation_time=d.get('creation_time', None),
                   end_date=d.get('end_date', None),
                   filter=d.get('filter', None),
                   name=d.get('name', None),
                   period=d.get('period', None),
                   start_date=d.get('start_date', None),
                   status_daily=_repeated_dict(d, 'status_daily', BudgetWithStatusStatusDailyItem),
                   target_amount=d.get('target_amount', None),
                   update_time=d.get('update_time', None))


@dataclass
class BudgetWithStatusStatusDailyItem:
    amount: Optional[str] = None
    """Amount used in this day in USD."""

    date: Optional[str] = None

    def as_dict(self) -> dict:
        """Serializes the BudgetWithStatusStatusDailyItem into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.amount is not None: body['amount'] = self.amount
        if self.date is not None: body['date'] = self.date
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> BudgetWithStatusStatusDailyItem:
        """Deserializes the BudgetWithStatusStatusDailyItem from a dictionary."""
        return cls(amount=d.get('amount', None), date=d.get('date', None))


@dataclass
class CreateLogDeliveryConfigurationParams:
    log_type: LogType
    """Log delivery type. Supported values are:
    
    * `BILLABLE_USAGE` — Configure [billable usage log delivery]. For the CSV schema, see the
    [View billable usage].
    
    * `AUDIT_LOGS` — Configure [audit log delivery]. For the JSON schema, see [Configure audit
    logging]
    
    [Configure audit logging]: https://docs.databricks.com/administration-guide/account-settings/audit-logs.html
    [View billable usage]: https://docs.databricks.com/administration-guide/account-settings/usage.html
    [audit log delivery]: https://docs.databricks.com/administration-guide/account-settings/audit-logs.html
    [billable usage log delivery]: https://docs.databricks.com/administration-guide/account-settings/billable-usage-delivery.html"""

    output_format: OutputFormat
    """The file type of log delivery.
    
    * If `log_type` is `BILLABLE_USAGE`, this value must be `CSV`. Only the CSV (comma-separated
    values) format is supported. For the schema, see the [View billable usage] * If `log_type` is
    `AUDIT_LOGS`, this value must be `JSON`. Only the JSON (JavaScript Object Notation) format is
    supported. For the schema, see the [Configuring audit logs].
    
    [Configuring audit logs]: https://docs.databricks.com/administration-guide/account-settings/audit-logs.html
    [View billable usage]: https://docs.databricks.com/administration-guide/account-settings/usage.html"""

    credentials_id: str
    """The ID for a method:credentials/create that represents the AWS IAM role with policy and trust
    relationship as described in the main billable usage documentation page. See [Configure billable
    usage delivery].
    
    [Configure billable usage delivery]: https://docs.databricks.com/administration-guide/account-settings/billable-usage-delivery.html"""

    storage_configuration_id: str
    """The ID for a method:storage/create that represents the S3 bucket with bucket policy as described
    in the main billable usage documentation page. See [Configure billable usage delivery].
    
    [Configure billable usage delivery]: https://docs.databricks.com/administration-guide/account-settings/billable-usage-delivery.html"""

    config_name: Optional[str] = None
    """The optional human-readable name of the log delivery configuration. Defaults to empty."""

    delivery_path_prefix: Optional[str] = None
    """The optional delivery path prefix within Amazon S3 storage. Defaults to empty, which means that
    logs are delivered to the root of the bucket. This must be a valid S3 object key. This must not
    start or end with a slash character."""

    delivery_start_time: Optional[str] = None
    """This field applies only if `log_type` is `BILLABLE_USAGE`. This is the optional start month and
    year for delivery, specified in `YYYY-MM` format. Defaults to current year and month.
    `BILLABLE_USAGE` logs are not available for usage before March 2019 (`2019-03`)."""

    status: Optional[LogDeliveryConfigStatus] = None
    """Status of log delivery configuration. Set to `ENABLED` (enabled) or `DISABLED` (disabled).
    Defaults to `ENABLED`. You can [enable or disable the
    configuration](#operation/patch-log-delivery-config-status) later. Deletion of a configuration
    is not supported, so disable a log delivery configuration that is no longer needed."""

    workspace_ids_filter: Optional[List[int]] = None
    """Optional filter that specifies workspace IDs to deliver logs for. By default the workspace
    filter is empty and log delivery applies at the account level, delivering workspace-level logs
    for all workspaces in your account, plus account level logs. You can optionally set this field
    to an array of workspace IDs (each one is an `int64`) to which log delivery should apply, in
    which case only workspace-level logs relating to the specified workspaces are delivered. If you
    plan to use different log delivery configurations for different workspaces, set this field
    explicitly. Be aware that delivery configurations mentioning specific workspaces won't apply to
    new workspaces created in the future, and delivery won't include account level logs. For some
    types of Databricks deployments there is only one workspace per account ID, so this field is
    unnecessary."""

    def as_dict(self) -> dict:
        """Serializes the CreateLogDeliveryConfigurationParams into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.config_name is not None: body['config_name'] = self.config_name
        if self.credentials_id is not None: body['credentials_id'] = self.credentials_id
        if self.delivery_path_prefix is not None: body['delivery_path_prefix'] = self.delivery_path_prefix
        if self.delivery_start_time is not None: body['delivery_start_time'] = self.delivery_start_time
        if self.log_type is not None: body['log_type'] = self.log_type.value
        if self.output_format is not None: body['output_format'] = self.output_format.value
        if self.status is not None: body['status'] = self.status.value
        if self.storage_configuration_id is not None:
            body['storage_configuration_id'] = self.storage_configuration_id
        if self.workspace_ids_filter: body['workspace_ids_filter'] = [v for v in self.workspace_ids_filter]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> CreateLogDeliveryConfigurationParams:
        """Deserializes the CreateLogDeliveryConfigurationParams from a dictionary."""
        return cls(config_name=d.get('config_name', None),
                   credentials_id=d.get('credentials_id', None),
                   delivery_path_prefix=d.get('delivery_path_prefix', None),
                   delivery_start_time=d.get('delivery_start_time', None),
                   log_type=_enum(d, 'log_type', LogType),
                   output_format=_enum(d, 'output_format', OutputFormat),
                   status=_enum(d, 'status', LogDeliveryConfigStatus),
                   storage_configuration_id=d.get('storage_configuration_id', None),
                   workspace_ids_filter=d.get('workspace_ids_filter', None))


@dataclass
class DeleteResponse:

    def as_dict(self) -> dict:
        """Serializes the DeleteResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> DeleteResponse:
        """Deserializes the DeleteResponse from a dictionary."""
        return cls()


class DeliveryStatus(Enum):
    """The status string for log delivery. Possible values are: * `CREATED`: There were no log delivery
    attempts since the config was created. * `SUCCEEDED`: The latest attempt of log delivery has
    succeeded completely. * `USER_FAILURE`: The latest attempt of log delivery failed because of
    misconfiguration of customer provided permissions on role or storage. * `SYSTEM_FAILURE`: The
    latest attempt of log delivery failed because of an Databricks internal error. Contact support
    if it doesn't go away soon. * `NOT_FOUND`: The log delivery status as the configuration has been
    disabled since the release of this feature or there are no workspaces in the account."""

    CREATED = 'CREATED'
    NOT_FOUND = 'NOT_FOUND'
    SUCCEEDED = 'SUCCEEDED'
    SYSTEM_FAILURE = 'SYSTEM_FAILURE'
    USER_FAILURE = 'USER_FAILURE'


@dataclass
class DownloadResponse:
    contents: Optional[BinaryIO] = None

    def as_dict(self) -> dict:
        """Serializes the DownloadResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.contents: body['contents'] = self.contents
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> DownloadResponse:
        """Deserializes the DownloadResponse from a dictionary."""
        return cls(contents=d.get('contents', None))


class LogDeliveryConfigStatus(Enum):
    """Status of log delivery configuration. Set to `ENABLED` (enabled) or `DISABLED` (disabled).
    Defaults to `ENABLED`. You can [enable or disable the
    configuration](#operation/patch-log-delivery-config-status) later. Deletion of a configuration
    is not supported, so disable a log delivery configuration that is no longer needed."""

    DISABLED = 'DISABLED'
    ENABLED = 'ENABLED'


@dataclass
class LogDeliveryConfiguration:
    account_id: Optional[str] = None
    """The Databricks account ID that hosts the log delivery configuration."""

    config_id: Optional[str] = None
    """Databricks log delivery configuration ID."""

    config_name: Optional[str] = None
    """The optional human-readable name of the log delivery configuration. Defaults to empty."""

    creation_time: Optional[int] = None
    """Time in epoch milliseconds when the log delivery configuration was created."""

    credentials_id: Optional[str] = None
    """The ID for a method:credentials/create that represents the AWS IAM role with policy and trust
    relationship as described in the main billable usage documentation page. See [Configure billable
    usage delivery].
    
    [Configure billable usage delivery]: https://docs.databricks.com/administration-guide/account-settings/billable-usage-delivery.html"""

    delivery_path_prefix: Optional[str] = None
    """The optional delivery path prefix within Amazon S3 storage. Defaults to empty, which means that
    logs are delivered to the root of the bucket. This must be a valid S3 object key. This must not
    start or end with a slash character."""

    delivery_start_time: Optional[str] = None
    """This field applies only if `log_type` is `BILLABLE_USAGE`. This is the optional start month and
    year for delivery, specified in `YYYY-MM` format. Defaults to current year and month.
    `BILLABLE_USAGE` logs are not available for usage before March 2019 (`2019-03`)."""

    log_delivery_status: Optional[LogDeliveryStatus] = None
    """Databricks log delivery status."""

    log_type: Optional[LogType] = None
    """Log delivery type. Supported values are:
    
    * `BILLABLE_USAGE` — Configure [billable usage log delivery]. For the CSV schema, see the
    [View billable usage].
    
    * `AUDIT_LOGS` — Configure [audit log delivery]. For the JSON schema, see [Configure audit
    logging]
    
    [Configure audit logging]: https://docs.databricks.com/administration-guide/account-settings/audit-logs.html
    [View billable usage]: https://docs.databricks.com/administration-guide/account-settings/usage.html
    [audit log delivery]: https://docs.databricks.com/administration-guide/account-settings/audit-logs.html
    [billable usage log delivery]: https://docs.databricks.com/administration-guide/account-settings/billable-usage-delivery.html"""

    output_format: Optional[OutputFormat] = None
    """The file type of log delivery.
    
    * If `log_type` is `BILLABLE_USAGE`, this value must be `CSV`. Only the CSV (comma-separated
    values) format is supported. For the schema, see the [View billable usage] * If `log_type` is
    `AUDIT_LOGS`, this value must be `JSON`. Only the JSON (JavaScript Object Notation) format is
    supported. For the schema, see the [Configuring audit logs].
    
    [Configuring audit logs]: https://docs.databricks.com/administration-guide/account-settings/audit-logs.html
    [View billable usage]: https://docs.databricks.com/administration-guide/account-settings/usage.html"""

    status: Optional[LogDeliveryConfigStatus] = None
    """Status of log delivery configuration. Set to `ENABLED` (enabled) or `DISABLED` (disabled).
    Defaults to `ENABLED`. You can [enable or disable the
    configuration](#operation/patch-log-delivery-config-status) later. Deletion of a configuration
    is not supported, so disable a log delivery configuration that is no longer needed."""

    storage_configuration_id: Optional[str] = None
    """The ID for a method:storage/create that represents the S3 bucket with bucket policy as described
    in the main billable usage documentation page. See [Configure billable usage delivery].
    
    [Configure billable usage delivery]: https://docs.databricks.com/administration-guide/account-settings/billable-usage-delivery.html"""

    update_time: Optional[int] = None
    """Time in epoch milliseconds when the log delivery configuration was updated."""

    workspace_ids_filter: Optional[List[int]] = None
    """Optional filter that specifies workspace IDs to deliver logs for. By default the workspace
    filter is empty and log delivery applies at the account level, delivering workspace-level logs
    for all workspaces in your account, plus account level logs. You can optionally set this field
    to an array of workspace IDs (each one is an `int64`) to which log delivery should apply, in
    which case only workspace-level logs relating to the specified workspaces are delivered. If you
    plan to use different log delivery configurations for different workspaces, set this field
    explicitly. Be aware that delivery configurations mentioning specific workspaces won't apply to
    new workspaces created in the future, and delivery won't include account level logs. For some
    types of Databricks deployments there is only one workspace per account ID, so this field is
    unnecessary."""

    def as_dict(self) -> dict:
        """Serializes the LogDeliveryConfiguration into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.account_id is not None: body['account_id'] = self.account_id
        if self.config_id is not None: body['config_id'] = self.config_id
        if self.config_name is not None: body['config_name'] = self.config_name
        if self.creation_time is not None: body['creation_time'] = self.creation_time
        if self.credentials_id is not None: body['credentials_id'] = self.credentials_id
        if self.delivery_path_prefix is not None: body['delivery_path_prefix'] = self.delivery_path_prefix
        if self.delivery_start_time is not None: body['delivery_start_time'] = self.delivery_start_time
        if self.log_delivery_status: body['log_delivery_status'] = self.log_delivery_status.as_dict()
        if self.log_type is not None: body['log_type'] = self.log_type.value
        if self.output_format is not None: body['output_format'] = self.output_format.value
        if self.status is not None: body['status'] = self.status.value
        if self.storage_configuration_id is not None:
            body['storage_configuration_id'] = self.storage_configuration_id
        if self.update_time is not None: body['update_time'] = self.update_time
        if self.workspace_ids_filter: body['workspace_ids_filter'] = [v for v in self.workspace_ids_filter]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> LogDeliveryConfiguration:
        """Deserializes the LogDeliveryConfiguration from a dictionary."""
        return cls(account_id=d.get('account_id', None),
                   config_id=d.get('config_id', None),
                   config_name=d.get('config_name', None),
                   creation_time=d.get('creation_time', None),
                   credentials_id=d.get('credentials_id', None),
                   delivery_path_prefix=d.get('delivery_path_prefix', None),
                   delivery_start_time=d.get('delivery_start_time', None),
                   log_delivery_status=_from_dict(d, 'log_delivery_status', LogDeliveryStatus),
                   log_type=_enum(d, 'log_type', LogType),
                   output_format=_enum(d, 'output_format', OutputFormat),
                   status=_enum(d, 'status', LogDeliveryConfigStatus),
                   storage_configuration_id=d.get('storage_configuration_id', None),
                   update_time=d.get('update_time', None),
                   workspace_ids_filter=d.get('workspace_ids_filter', None))


@dataclass
class LogDeliveryStatus:
    """Databricks log delivery status."""

    last_attempt_time: Optional[str] = None
    """The UTC time for the latest log delivery attempt."""

    last_successful_attempt_time: Optional[str] = None
    """The UTC time for the latest successful log delivery."""

    message: Optional[str] = None
    """Informative message about the latest log delivery attempt. If the log delivery fails with
    USER_FAILURE, error details will be provided for fixing misconfigurations in cloud permissions."""

    status: Optional[DeliveryStatus] = None
    """The status string for log delivery. Possible values are: * `CREATED`: There were no log delivery
    attempts since the config was created. * `SUCCEEDED`: The latest attempt of log delivery has
    succeeded completely. * `USER_FAILURE`: The latest attempt of log delivery failed because of
    misconfiguration of customer provided permissions on role or storage. * `SYSTEM_FAILURE`: The
    latest attempt of log delivery failed because of an Databricks internal error. Contact support
    if it doesn't go away soon. * `NOT_FOUND`: The log delivery status as the configuration has been
    disabled since the release of this feature or there are no workspaces in the account."""

    def as_dict(self) -> dict:
        """Serializes the LogDeliveryStatus into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.last_attempt_time is not None: body['last_attempt_time'] = self.last_attempt_time
        if self.last_successful_attempt_time is not None:
            body['last_successful_attempt_time'] = self.last_successful_attempt_time
        if self.message is not None: body['message'] = self.message
        if self.status is not None: body['status'] = self.status.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> LogDeliveryStatus:
        """Deserializes the LogDeliveryStatus from a dictionary."""
        return cls(last_attempt_time=d.get('last_attempt_time', None),
                   last_successful_attempt_time=d.get('last_successful_attempt_time', None),
                   message=d.get('message', None),
                   status=_enum(d, 'status', DeliveryStatus))


class LogType(Enum):
    """Log delivery type. Supported values are:
    
    * `BILLABLE_USAGE` — Configure [billable usage log delivery]. For the CSV schema, see the
    [View billable usage].
    
    * `AUDIT_LOGS` — Configure [audit log delivery]. For the JSON schema, see [Configure audit
    logging]
    
    [Configure audit logging]: https://docs.databricks.com/administration-guide/account-settings/audit-logs.html
    [View billable usage]: https://docs.databricks.com/administration-guide/account-settings/usage.html
    [audit log delivery]: https://docs.databricks.com/administration-guide/account-settings/audit-logs.html
    [billable usage log delivery]: https://docs.databricks.com/administration-guide/account-settings/billable-usage-delivery.html"""

    AUDIT_LOGS = 'AUDIT_LOGS'
    BILLABLE_USAGE = 'BILLABLE_USAGE'


class OutputFormat(Enum):
    """The file type of log delivery.
    
    * If `log_type` is `BILLABLE_USAGE`, this value must be `CSV`. Only the CSV (comma-separated
    values) format is supported. For the schema, see the [View billable usage] * If `log_type` is
    `AUDIT_LOGS`, this value must be `JSON`. Only the JSON (JavaScript Object Notation) format is
    supported. For the schema, see the [Configuring audit logs].
    
    [Configuring audit logs]: https://docs.databricks.com/administration-guide/account-settings/audit-logs.html
    [View billable usage]: https://docs.databricks.com/administration-guide/account-settings/usage.html"""

    CSV = 'CSV'
    JSON = 'JSON'


@dataclass
class PatchStatusResponse:

    def as_dict(self) -> dict:
        """Serializes the PatchStatusResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> PatchStatusResponse:
        """Deserializes the PatchStatusResponse from a dictionary."""
        return cls()


@dataclass
class UpdateLogDeliveryConfigurationStatusRequest:
    status: LogDeliveryConfigStatus
    """Status of log delivery configuration. Set to `ENABLED` (enabled) or `DISABLED` (disabled).
    Defaults to `ENABLED`. You can [enable or disable the
    configuration](#operation/patch-log-delivery-config-status) later. Deletion of a configuration
    is not supported, so disable a log delivery configuration that is no longer needed."""

    log_delivery_configuration_id: Optional[str] = None
    """Databricks log delivery configuration ID"""

    def as_dict(self) -> dict:
        """Serializes the UpdateLogDeliveryConfigurationStatusRequest into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.log_delivery_configuration_id is not None:
            body['log_delivery_configuration_id'] = self.log_delivery_configuration_id
        if self.status is not None: body['status'] = self.status.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> UpdateLogDeliveryConfigurationStatusRequest:
        """Deserializes the UpdateLogDeliveryConfigurationStatusRequest from a dictionary."""
        return cls(log_delivery_configuration_id=d.get('log_delivery_configuration_id', None),
                   status=_enum(d, 'status', LogDeliveryConfigStatus))


@dataclass
class UpdateResponse:

    def as_dict(self) -> dict:
        """Serializes the UpdateResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> UpdateResponse:
        """Deserializes the UpdateResponse from a dictionary."""
        return cls()


@dataclass
class WrappedBudget:
    budget: Budget
    """Budget configuration to be created."""

    budget_id: Optional[str] = None
    """Budget ID"""

    def as_dict(self) -> dict:
        """Serializes the WrappedBudget into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.budget: body['budget'] = self.budget.as_dict()
        if self.budget_id is not None: body['budget_id'] = self.budget_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> WrappedBudget:
        """Deserializes the WrappedBudget from a dictionary."""
        return cls(budget=_from_dict(d, 'budget', Budget), budget_id=d.get('budget_id', None))


@dataclass
class WrappedBudgetWithStatus:
    budget: BudgetWithStatus
    """Budget configuration with daily status."""

    def as_dict(self) -> dict:
        """Serializes the WrappedBudgetWithStatus into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.budget: body['budget'] = self.budget.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> WrappedBudgetWithStatus:
        """Deserializes the WrappedBudgetWithStatus from a dictionary."""
        return cls(budget=_from_dict(d, 'budget', BudgetWithStatus))


@dataclass
class WrappedCreateLogDeliveryConfiguration:
    log_delivery_configuration: Optional[CreateLogDeliveryConfigurationParams] = None

    def as_dict(self) -> dict:
        """Serializes the WrappedCreateLogDeliveryConfiguration into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.log_delivery_configuration:
            body['log_delivery_configuration'] = self.log_delivery_configuration.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> WrappedCreateLogDeliveryConfiguration:
        """Deserializes the WrappedCreateLogDeliveryConfiguration from a dictionary."""
        return cls(log_delivery_configuration=_from_dict(d, 'log_delivery_configuration',
                                                         CreateLogDeliveryConfigurationParams))


@dataclass
class WrappedLogDeliveryConfiguration:
    log_delivery_configuration: Optional[LogDeliveryConfiguration] = None

    def as_dict(self) -> dict:
        """Serializes the WrappedLogDeliveryConfiguration into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.log_delivery_configuration:
            body['log_delivery_configuration'] = self.log_delivery_configuration.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> WrappedLogDeliveryConfiguration:
        """Deserializes the WrappedLogDeliveryConfiguration from a dictionary."""
        return cls(
            log_delivery_configuration=_from_dict(d, 'log_delivery_configuration', LogDeliveryConfiguration))


@dataclass
class WrappedLogDeliveryConfigurations:
    log_delivery_configurations: Optional[List[LogDeliveryConfiguration]] = None

    def as_dict(self) -> dict:
        """Serializes the WrappedLogDeliveryConfigurations into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.log_delivery_configurations:
            body['log_delivery_configurations'] = [v.as_dict() for v in self.log_delivery_configurations]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> WrappedLogDeliveryConfigurations:
        """Deserializes the WrappedLogDeliveryConfigurations from a dictionary."""
        return cls(log_delivery_configurations=_repeated_dict(d, 'log_delivery_configurations',
                                                              LogDeliveryConfiguration))


class BillableUsageAPI:
    """This API allows you to download billable usage logs for the specified account and date range. This feature
    works with all account types."""

    def __init__(self, api_client):
        self._api = api_client

    def download(self,
                 start_month: str,
                 end_month: str,
                 *,
                 personal_data: Optional[bool] = None) -> DownloadResponse:
        """Return billable usage logs.
        
        Returns billable usage logs in CSV format for the specified account and date range. For the data
        schema, see [CSV file schema]. Note that this method might take multiple minutes to complete.
        
        **Warning**: Depending on the queried date range, the number of workspaces in the account, the size of
        the response and the internet speed of the caller, this API may hit a timeout after a few minutes. If
        you experience this, try to mitigate by calling the API with narrower date ranges.
        
        [CSV file schema]: https://docs.databricks.com/administration-guide/account-settings/usage-analysis.html#schema
        
        :param start_month: str
          Format: `YYYY-MM`. First month to return billable usage logs for. This field is required.
        :param end_month: str
          Format: `YYYY-MM`. Last month to return billable usage logs for. This field is required.
        :param personal_data: bool (optional)
          Specify whether to include personally identifiable information in the billable usage logs, for
          example the email addresses of cluster creators. Handle this information with care. Defaults to
          false.
        
        :returns: :class:`DownloadResponse`
        """

        query = {}
        if end_month is not None: query['end_month'] = end_month
        if personal_data is not None: query['personal_data'] = personal_data
        if start_month is not None: query['start_month'] = start_month
        headers = {'Accept': 'text/plain', }

        res = self._api.do('GET',
                           f'/api/2.0/accounts/{self._api.account_id}/usage/download',
                           query=query,
                           headers=headers,
                           raw=True)
        return DownloadResponse.from_dict(res)


class BudgetsAPI:
    """These APIs manage budget configuration including notifications for exceeding a budget for a period. They
    can also retrieve the status of each budget."""

    def __init__(self, api_client):
        self._api = api_client

    def create(self, budget: Budget) -> WrappedBudgetWithStatus:
        """Create a new budget.
        
        Creates a new budget in the specified account.
        
        :param budget: :class:`Budget`
          Budget configuration to be created.
        
        :returns: :class:`WrappedBudgetWithStatus`
        """
        body = {}
        if budget is not None: body['budget'] = budget.as_dict()
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        res = self._api.do('POST',
                           f'/api/2.0/accounts/{self._api.account_id}/budget',
                           body=body,
                           headers=headers)
        return WrappedBudgetWithStatus.from_dict(res)

    def delete(self, budget_id: str):
        """Delete budget.
        
        Deletes the budget specified by its UUID.
        
        :param budget_id: str
          Budget ID
        
        
        """

        headers = {'Accept': 'application/json', }

        self._api.do('DELETE',
                     f'/api/2.0/accounts/{self._api.account_id}/budget/{budget_id}',
                     headers=headers)

    def get(self, budget_id: str) -> WrappedBudgetWithStatus:
        """Get budget and its status.
        
        Gets the budget specified by its UUID, including noncumulative status for each day that the budget is
        configured to include.
        
        :param budget_id: str
          Budget ID
        
        :returns: :class:`WrappedBudgetWithStatus`
        """

        headers = {'Accept': 'application/json', }

        res = self._api.do('GET',
                           f'/api/2.0/accounts/{self._api.account_id}/budget/{budget_id}',
                           headers=headers)
        return WrappedBudgetWithStatus.from_dict(res)

    def list(self) -> Iterator[BudgetWithStatus]:
        """Get all budgets.
        
        Gets all budgets associated with this account, including noncumulative status for each day that the
        budget is configured to include.
        
        :returns: Iterator over :class:`BudgetWithStatus`
        """

        headers = {'Accept': 'application/json', }

        json = self._api.do('GET', f'/api/2.0/accounts/{self._api.account_id}/budget', headers=headers)
        parsed = BudgetList.from_dict(json).budgets
        return parsed if parsed is not None else []

    def update(self, budget_id: str, budget: Budget):
        """Modify budget.
        
        Modifies a budget in this account. Budget properties are completely overwritten.
        
        :param budget_id: str
          Budget ID
        :param budget: :class:`Budget`
          Budget configuration to be created.
        
        
        """
        body = {}
        if budget is not None: body['budget'] = budget.as_dict()
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        self._api.do('PATCH',
                     f'/api/2.0/accounts/{self._api.account_id}/budget/{budget_id}',
                     body=body,
                     headers=headers)


class LogDeliveryAPI:
    """These APIs manage log delivery configurations for this account. The two supported log types for this API
    are _billable usage logs_ and _audit logs_. This feature is in Public Preview. This feature works with all
    account ID types.
    
    Log delivery works with all account types. However, if your account is on the E2 version of the platform
    or on a select custom plan that allows multiple workspaces per account, you can optionally configure
    different storage destinations for each workspace. Log delivery status is also provided to know the latest
    status of log delivery attempts. The high-level flow of billable usage delivery:
    
    1. **Create storage**: In AWS, [create a new AWS S3 bucket] with a specific bucket policy. Using
    Databricks APIs, call the Account API to create a [storage configuration object](:method:Storage/Create)
    that uses the bucket name. 2. **Create credentials**: In AWS, create the appropriate AWS IAM role. For
    full details, including the required IAM role policies and trust relationship, see [Billable usage log
    delivery]. Using Databricks APIs, call the Account API to create a [credential configuration
    object](:method:Credentials/Create) that uses the IAM role"s ARN. 3. **Create log delivery
    configuration**: Using Databricks APIs, call the Account API to [create a log delivery
    configuration](:method:LogDelivery/Create) that uses the credential and storage configuration objects from
    previous steps. You can specify if the logs should include all events of that log type in your account
    (_Account level_ delivery) or only events for a specific set of workspaces (_workspace level_ delivery).
    Account level log delivery applies to all current and future workspaces plus account level logs, while
    workspace level log delivery solely delivers logs related to the specified workspaces. You can create
    multiple types of delivery configurations per account.
    
    For billable usage delivery: * For more information about billable usage logs, see [Billable usage log
    delivery]. For the CSV schema, see the [Usage page]. * The delivery location is
    `<bucket-name>/<prefix>/billable-usage/csv/`, where `<prefix>` is the name of the optional delivery path
    prefix you set up during log delivery configuration. Files are named
    `workspaceId=<workspace-id>-usageMonth=<month>.csv`. * All billable usage logs apply to specific
    workspaces (_workspace level_ logs). You can aggregate usage for your entire account by creating an
    _account level_ delivery configuration that delivers logs for all current and future workspaces in your
    account. * The files are delivered daily by overwriting the month's CSV file for each workspace.
    
    For audit log delivery: * For more information about about audit log delivery, see [Audit log delivery],
    which includes information about the used JSON schema. * The delivery location is
    `<bucket-name>/<delivery-path-prefix>/workspaceId=<workspaceId>/date=<yyyy-mm-dd>/auditlogs_<internal-id>.json`.
    Files may get overwritten with the same content multiple times to achieve exactly-once delivery. * If the
    audit log delivery configuration included specific workspace IDs, only _workspace-level_ audit logs for
    those workspaces are delivered. If the log delivery configuration applies to the entire account (_account
    level_ delivery configuration), the audit log delivery includes workspace-level audit logs for all
    workspaces in the account as well as account-level audit logs. See [Audit log delivery] for details. *
    Auditable events are typically available in logs within 15 minutes.
    
    [Audit log delivery]: https://docs.databricks.com/administration-guide/account-settings/audit-logs.html
    [Billable usage log delivery]: https://docs.databricks.com/administration-guide/account-settings/billable-usage-delivery.html
    [Usage page]: https://docs.databricks.com/administration-guide/account-settings/usage.html
    [create a new AWS S3 bucket]: https://docs.databricks.com/administration-guide/account-api/aws-storage.html"""

    def __init__(self, api_client):
        self._api = api_client

    def create(
        self,
        *,
        log_delivery_configuration: Optional[CreateLogDeliveryConfigurationParams] = None
    ) -> WrappedLogDeliveryConfiguration:
        """Create a new log delivery configuration.
        
        Creates a new Databricks log delivery configuration to enable delivery of the specified type of logs
        to your storage location. This requires that you already created a [credential
        object](:method:Credentials/Create) (which encapsulates a cross-account service IAM role) and a
        [storage configuration object](:method:Storage/Create) (which encapsulates an S3 bucket).
        
        For full details, including the required IAM role policies and bucket policies, see [Deliver and
        access billable usage logs] or [Configure audit logging].
        
        **Note**: There is a limit on the number of log delivery configurations available per account (each
        limit applies separately to each log type including billable usage and audit logs). You can create a
        maximum of two enabled account-level delivery configurations (configurations without a workspace
        filter) per type. Additionally, you can create two enabled workspace-level delivery configurations per
        workspace for each log type, which means that the same workspace ID can occur in the workspace filter
        for no more than two delivery configurations per log type.
        
        You cannot delete a log delivery configuration, but you can disable it (see [Enable or disable log
        delivery configuration](:method:LogDelivery/PatchStatus)).
        
        [Configure audit logging]: https://docs.databricks.com/administration-guide/account-settings/audit-logs.html
        [Deliver and access billable usage logs]: https://docs.databricks.com/administration-guide/account-settings/billable-usage-delivery.html
        
        :param log_delivery_configuration: :class:`CreateLogDeliveryConfigurationParams` (optional)
        
        :returns: :class:`WrappedLogDeliveryConfiguration`
        """
        body = {}
        if log_delivery_configuration is not None:
            body['log_delivery_configuration'] = log_delivery_configuration.as_dict()
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        res = self._api.do('POST',
                           f'/api/2.0/accounts/{self._api.account_id}/log-delivery',
                           body=body,
                           headers=headers)
        return WrappedLogDeliveryConfiguration.from_dict(res)

    def get(self, log_delivery_configuration_id: str) -> WrappedLogDeliveryConfiguration:
        """Get log delivery configuration.
        
        Gets a Databricks log delivery configuration object for an account, both specified by ID.
        
        :param log_delivery_configuration_id: str
          Databricks log delivery configuration ID
        
        :returns: :class:`WrappedLogDeliveryConfiguration`
        """

        headers = {'Accept': 'application/json', }

        res = self._api.do(
            'GET',
            f'/api/2.0/accounts/{self._api.account_id}/log-delivery/{log_delivery_configuration_id}',
            headers=headers)
        return WrappedLogDeliveryConfiguration.from_dict(res)

    def list(self,
             *,
             credentials_id: Optional[str] = None,
             status: Optional[LogDeliveryConfigStatus] = None,
             storage_configuration_id: Optional[str] = None) -> Iterator[LogDeliveryConfiguration]:
        """Get all log delivery configurations.
        
        Gets all Databricks log delivery configurations associated with an account specified by ID.
        
        :param credentials_id: str (optional)
          Filter by credential configuration ID.
        :param status: :class:`LogDeliveryConfigStatus` (optional)
          Filter by status `ENABLED` or `DISABLED`.
        :param storage_configuration_id: str (optional)
          Filter by storage configuration ID.
        
        :returns: Iterator over :class:`LogDeliveryConfiguration`
        """

        query = {}
        if credentials_id is not None: query['credentials_id'] = credentials_id
        if status is not None: query['status'] = status.value
        if storage_configuration_id is not None: query['storage_configuration_id'] = storage_configuration_id
        headers = {'Accept': 'application/json', }

        json = self._api.do('GET',
                            f'/api/2.0/accounts/{self._api.account_id}/log-delivery',
                            query=query,
                            headers=headers)
        parsed = WrappedLogDeliveryConfigurations.from_dict(json).log_delivery_configurations
        return parsed if parsed is not None else []

    def patch_status(self, log_delivery_configuration_id: str, status: LogDeliveryConfigStatus):
        """Enable or disable log delivery configuration.
        
        Enables or disables a log delivery configuration. Deletion of delivery configurations is not
        supported, so disable log delivery configurations that are no longer needed. Note that you can't
        re-enable a delivery configuration if this would violate the delivery configuration limits described
        under [Create log delivery](:method:LogDelivery/Create).
        
        :param log_delivery_configuration_id: str
          Databricks log delivery configuration ID
        :param status: :class:`LogDeliveryConfigStatus`
          Status of log delivery configuration. Set to `ENABLED` (enabled) or `DISABLED` (disabled). Defaults
          to `ENABLED`. You can [enable or disable the
          configuration](#operation/patch-log-delivery-config-status) later. Deletion of a configuration is
          not supported, so disable a log delivery configuration that is no longer needed.
        
        
        """
        body = {}
        if status is not None: body['status'] = status.value
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        self._api.do('PATCH',
                     f'/api/2.0/accounts/{self._api.account_id}/log-delivery/{log_delivery_configuration_id}',
                     body=body,
                     headers=headers)
