# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

from dataclasses import dataclass
from enum import Enum
from typing import Optional, Dict, List, Any


# all definitions in this file are in alphabetical order


@dataclass
class Budget:
    """Budget configuration to be created."""

    alerts: "List[BudgetAlert]"
    # Optional end date of the budget.
    end_date: str
    # SQL-like filter expression with workspaceId, SKU and tag. Usage in your
    # account that matches this expression will be counted in this budget.
    #
    # Supported properties on left-hand side of comparison: * `workspaceId` -
    # the ID of the workspace * `sku` - SKU of the cluster, e.g.
    # `STANDARD_ALL_PURPOSE_COMPUTE` * `tag.tagName`, `tag.'tag name'` - tag of
    # the cluster
    #
    # Supported comparison operators: * `=` - equal * `!=` - not equal
    #
    # Supported logical operators: `AND`, `OR`.
    #
    # Examples: * `workspaceId=123 OR (sku='STANDARD_ALL_PURPOSE_COMPUTE' AND
    # tag.'my tag'='my value')` * `workspaceId!=456` *
    # `sku='STANDARD_ALL_PURPOSE_COMPUTE' OR sku='PREMIUM_ALL_PURPOSE_COMPUTE'`
    # * `tag.name1='value1' AND tag.name2='value2'`
    filter: str
    # Human-readable name of the budget.
    name: str
    # Period length in years, months, weeks and/or days. Examples: `1 month`,
    # `30 days`, `1 year, 2 months, 1 week, 2 days`
    period: str
    # Start date of the budget period calculation.
    start_date: str
    # Target amount of the budget per period in USD.
    target_amount: str

    def as_dict(self) -> dict:
        body = {}
        if self.alerts:
            body["alerts"] = [v.as_dict() for v in self.alerts]
        if self.end_date:
            body["end_date"] = self.end_date
        if self.filter:
            body["filter"] = self.filter
        if self.name:
            body["name"] = self.name
        if self.period:
            body["period"] = self.period
        if self.start_date:
            body["start_date"] = self.start_date
        if self.target_amount:
            body["target_amount"] = self.target_amount

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "Budget":
        return cls(
            alerts=[BudgetAlert.from_dict(v) for v in d["alerts"]]
            if "alerts" in d
            else None,
            end_date=d.get("end_date", None),
            filter=d.get("filter", None),
            name=d.get("name", None),
            period=d.get("period", None),
            start_date=d.get("start_date", None),
            target_amount=d.get("target_amount", None),
        )


@dataclass
class BudgetAlert:

    # List of email addresses to be notified when budget percentage is exceeded
    # in the given period.
    email_notifications: "List[str]"
    # Percentage of the target amount used in the currect period that will
    # trigger a notification.
    min_percentage: int

    def as_dict(self) -> dict:
        body = {}
        if self.email_notifications:
            body["email_notifications"] = [v for v in self.email_notifications]
        if self.min_percentage:
            body["min_percentage"] = self.min_percentage

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "BudgetAlert":
        return cls(
            email_notifications=d.get("email_notifications", None),
            min_percentage=d.get("min_percentage", None),
        )


@dataclass
class BudgetList:
    """List of budgets."""

    budgets: "List[BudgetWithStatus]"

    def as_dict(self) -> dict:
        body = {}
        if self.budgets:
            body["budgets"] = [v.as_dict() for v in self.budgets]

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "BudgetList":
        return cls(
            budgets=[BudgetWithStatus.from_dict(v) for v in d["budgets"]]
            if "budgets" in d
            else None,
        )


@dataclass
class BudgetWithStatus:
    """Budget configuration with daily status."""

    alerts: "List[BudgetAlert]"

    budget_id: str

    creation_time: str
    # Optional end date of the budget.
    end_date: str
    # SQL-like filter expression with workspaceId, SKU and tag. Usage in your
    # account that matches this expression will be counted in this budget.
    #
    # Supported properties on left-hand side of comparison: * `workspaceId` -
    # the ID of the workspace * `sku` - SKU of the cluster, e.g.
    # `STANDARD_ALL_PURPOSE_COMPUTE` * `tag.tagName`, `tag.'tag name'` - tag of
    # the cluster
    #
    # Supported comparison operators: * `=` - equal * `!=` - not equal
    #
    # Supported logical operators: `AND`, `OR`.
    #
    # Examples: * `workspaceId=123 OR (sku='STANDARD_ALL_PURPOSE_COMPUTE' AND
    # tag.'my tag'='my value')` * `workspaceId!=456` *
    # `sku='STANDARD_ALL_PURPOSE_COMPUTE' OR sku='PREMIUM_ALL_PURPOSE_COMPUTE'`
    # * `tag.name1='value1' AND tag.name2='value2'`
    filter: str
    # Human-readable name of the budget.
    name: str
    # Period length in years, months, weeks and/or days. Examples: `1 month`,
    # `30 days`, `1 year, 2 months, 1 week, 2 days`
    period: str
    # Start date of the budget period calculation.
    start_date: str
    # Amount used in the budget for each day (noncumulative).
    status_daily: "List[BudgetWithStatusStatusDailyItem]"
    # Target amount of the budget per period in USD.
    target_amount: str

    update_time: str

    def as_dict(self) -> dict:
        body = {}
        if self.alerts:
            body["alerts"] = [v.as_dict() for v in self.alerts]
        if self.budget_id:
            body["budget_id"] = self.budget_id
        if self.creation_time:
            body["creation_time"] = self.creation_time
        if self.end_date:
            body["end_date"] = self.end_date
        if self.filter:
            body["filter"] = self.filter
        if self.name:
            body["name"] = self.name
        if self.period:
            body["period"] = self.period
        if self.start_date:
            body["start_date"] = self.start_date
        if self.status_daily:
            body["status_daily"] = [v.as_dict() for v in self.status_daily]
        if self.target_amount:
            body["target_amount"] = self.target_amount
        if self.update_time:
            body["update_time"] = self.update_time

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "BudgetWithStatus":
        return cls(
            alerts=[BudgetAlert.from_dict(v) for v in d["alerts"]]
            if "alerts" in d
            else None,
            budget_id=d.get("budget_id", None),
            creation_time=d.get("creation_time", None),
            end_date=d.get("end_date", None),
            filter=d.get("filter", None),
            name=d.get("name", None),
            period=d.get("period", None),
            start_date=d.get("start_date", None),
            status_daily=[
                BudgetWithStatusStatusDailyItem.from_dict(v) for v in d["status_daily"]
            ]
            if "status_daily" in d
            else None,
            target_amount=d.get("target_amount", None),
            update_time=d.get("update_time", None),
        )


@dataclass
class BudgetWithStatusStatusDailyItem:

    # Amount used in this day in USD.
    amount: str

    date: str

    def as_dict(self) -> dict:
        body = {}
        if self.amount:
            body["amount"] = self.amount
        if self.date:
            body["date"] = self.date

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "BudgetWithStatusStatusDailyItem":
        return cls(
            amount=d.get("amount", None),
            date=d.get("date", None),
        )


@dataclass
class CreateLogDeliveryConfigurationParams:

    # The optional human-readable name of the log delivery configuration.
    # Defaults to empty.
    config_name: str
    # The ID for a method:CredetialConfigurations/createCredentialConfig that
    # represents the AWS IAM role with policy and trust relationship as
    # described in the main billable usage documentation page. See [Configure
    # billable usage delivery].
    #
    # [Configure billable usage delivery]: https://docs.databricks.com/administration-guide/account-settings/billable-usage-delivery.html
    credentials_id: str
    # The optional delivery path prefix within Amazon S3 storage. Defaults to
    # empty, which means that logs are delivered to the root of the bucket. This
    # must be a valid S3 object key. This must not start or end with a slash
    # character.
    delivery_path_prefix: str
    # This field applies only if `log_type` is `BILLABLE_USAGE`. This is the
    # optional start month and year for delivery, specified in `YYYY-MM` format.
    # Defaults to current year and month. `BILLABLE_USAGE` logs are not
    # available for usage before March 2019 (`2019-03`).
    delivery_start_time: str
    # Log delivery type. Supported values are:
    #
    # * `BILLABLE_USAGE` — Configure [billable usage log delivery]. For the
    # CSV schema, see the [View billable usage].
    #
    # * `AUDIT_LOGS` — Configure [audit log delivery]. For the JSON schema,
    # see [Configure audit logging]
    #
    # [Configure audit logging]: https://docs.databricks.com/administration-guide/account-settings/audit-logs.html
    # [View billable usage]: https://docs.databricks.com/administration-guide/account-settings/usage.html
    # [audit log delivery]: https://docs.databricks.com/administration-guide/account-settings/audit-logs.html
    # [billable usage log delivery]: https://docs.databricks.com/administration-guide/account-settings/billable-usage-delivery.html
    log_type: "LogType"
    # The file type of log delivery.
    #
    # * If `log_type` is `BILLABLE_USAGE`, this value must be `CSV`. Only the
    # CSV (comma-separated values) format is supported. For the schema, see the
    # [View billable usage] * If `log_type` is `AUDIT_LOGS`, this value must be
    # `JSON`. Only the JSON (JavaScript Object Notation) format is supported.
    # For the schema, see the [Configuring audit logs].
    #
    # [Configuring audit logs]: https://docs.databricks.com/administration-guide/account-settings/audit-logs.html
    # [View billable usage]: https://docs.databricks.com/administration-guide/account-settings/usage.html
    output_format: "OutputFormat"
    # Status of log delivery configuration. Set to `ENABLED` (enabled) or
    # `DISABLED` (disabled). Defaults to `ENABLED`. You can [enable or disable
    # the configuration](#operation/patch-log-delivery-config-status) later.
    # Deletion of a configuration is not supported, so disable a log delivery
    # configuration that is no longer needed.
    status: "LogDeliveryConfigStatus"
    # "The ID for a method:StorageConfiguration/createCredentialConfig that
    # represents the S3 bucket with bucket policy as described in the main
    # billable usage documentation page. See [Configure billable usage
    # delivery]."
    #
    # [Configure billable usage delivery]: https://docs.databricks.com/administration-guide/account-settings/billable-usage-delivery.html
    storage_configuration_id: str
    # Optional filter that specifies workspace IDs to deliver logs for. By
    # default the workspace filter is empty and log delivery applies at the
    # account level, delivering workspace-level logs for all workspaces in your
    # account, plus account level logs. You can optionally set this field to an
    # array of workspace IDs (each one is an `int64`) to which log delivery
    # should apply, in which case only workspace-level logs relating to the
    # specified workspaces are delivered. If you plan to use different log
    # delivery configurations for different workspaces, set this field
    # explicitly. Be aware that delivery configurations mentioning specific
    # workspaces won't apply to new workspaces created in the future, and
    # delivery won't include account level logs. For some types of Databricks
    # deployments there is only one workspace per account ID, so this field is
    # unnecessary.
    workspace_ids_filter: "List[int]"

    def as_dict(self) -> dict:
        body = {}
        if self.config_name:
            body["config_name"] = self.config_name
        if self.credentials_id:
            body["credentials_id"] = self.credentials_id
        if self.delivery_path_prefix:
            body["delivery_path_prefix"] = self.delivery_path_prefix
        if self.delivery_start_time:
            body["delivery_start_time"] = self.delivery_start_time
        if self.log_type:
            body["log_type"] = self.log_type.value
        if self.output_format:
            body["output_format"] = self.output_format.value
        if self.status:
            body["status"] = self.status.value
        if self.storage_configuration_id:
            body["storage_configuration_id"] = self.storage_configuration_id
        if self.workspace_ids_filter:
            body["workspace_ids_filter"] = [v for v in self.workspace_ids_filter]

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "CreateLogDeliveryConfigurationParams":
        return cls(
            config_name=d.get("config_name", None),
            credentials_id=d.get("credentials_id", None),
            delivery_path_prefix=d.get("delivery_path_prefix", None),
            delivery_start_time=d.get("delivery_start_time", None),
            log_type=LogType(d["log_type"]) if "log_type" in d else None,
            output_format=OutputFormat(d["output_format"])
            if "output_format" in d
            else None,
            status=LogDeliveryConfigStatus(d["status"]) if "status" in d else None,
            storage_configuration_id=d.get("storage_configuration_id", None),
            workspace_ids_filter=d.get("workspace_ids_filter", None),
        )


@dataclass
class DeleteBudgetRequest:
    """Delete budget"""

    # Budget ID
    budget_id: str  # path

    def as_dict(self) -> dict:
        body = {}
        if self.budget_id:
            body["budget_id"] = self.budget_id

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "DeleteBudgetRequest":
        return cls(
            budget_id=d.get("budget_id", None),
        )


class DeliveryStatus(Enum):
    """This describes an enum"""

    CREATED = "CREATED"
    NOT_FOUND = "NOT_FOUND"
    SUCCEEDED = "SUCCEEDED"
    SYSTEM_FAILURE = "SYSTEM_FAILURE"
    USER_FAILURE = "USER_FAILURE"


@dataclass
class DownloadRequest:
    """Return billable usage logs"""

    # Format: `YYYY-MM`. Last month to return billable usage logs for. This
    # field is required.
    end_month: str  # query
    # Specify whether to include personally identifiable information in the
    # billable usage logs, for example the email addresses of cluster creators.
    # Handle this information with care. Defaults to false.
    personal_data: bool  # query
    # Format: `YYYY-MM`. First month to return billable usage logs for. This
    # field is required.
    start_month: str  # query

    def as_dict(self) -> dict:
        body = {}
        if self.end_month:
            body["end_month"] = self.end_month
        if self.personal_data:
            body["personal_data"] = self.personal_data
        if self.start_month:
            body["start_month"] = self.start_month

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "DownloadRequest":
        return cls(
            end_month=d.get("end_month", None),
            personal_data=d.get("personal_data", None),
            start_month=d.get("start_month", None),
        )


@dataclass
class GetBudgetRequest:
    """Get budget and its status"""

    # Budget ID
    budget_id: str  # path

    def as_dict(self) -> dict:
        body = {}
        if self.budget_id:
            body["budget_id"] = self.budget_id

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "GetBudgetRequest":
        return cls(
            budget_id=d.get("budget_id", None),
        )


@dataclass
class GetLogDeliveryRequest:
    """Get log delivery configuration"""

    # Databricks log delivery configuration ID
    log_delivery_configuration_id: str  # path

    def as_dict(self) -> dict:
        body = {}
        if self.log_delivery_configuration_id:
            body["log_delivery_configuration_id"] = self.log_delivery_configuration_id

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "GetLogDeliveryRequest":
        return cls(
            log_delivery_configuration_id=d.get("log_delivery_configuration_id", None),
        )


@dataclass
class ListLogDeliveryRequest:
    """Get all log delivery configurations"""

    # Filter by credential configuration ID.
    credentials_id: str  # query
    # Filter by status `ENABLED` or `DISABLED`.
    status: "LogDeliveryConfigStatus"  # query
    # Filter by storage configuration ID.
    storage_configuration_id: str  # query

    def as_dict(self) -> dict:
        body = {}
        if self.credentials_id:
            body["credentials_id"] = self.credentials_id
        if self.status:
            body["status"] = self.status.value
        if self.storage_configuration_id:
            body["storage_configuration_id"] = self.storage_configuration_id

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ListLogDeliveryRequest":
        return cls(
            credentials_id=d.get("credentials_id", None),
            status=LogDeliveryConfigStatus(d["status"]) if "status" in d else None,
            storage_configuration_id=d.get("storage_configuration_id", None),
        )


class LogDeliveryConfigStatus(Enum):
    """Status of log delivery configuration. Set to `ENABLED` (enabled) or
    `DISABLED` (disabled). Defaults to `ENABLED`. You can [enable or disable the
    configuration](#operation/patch-log-delivery-config-status) later. Deletion
    of a configuration is not supported, so disable a log delivery configuration
    that is no longer needed."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


@dataclass
class LogDeliveryConfiguration:

    # The Databricks account ID that hosts the log delivery configuration.
    account_id: str
    # Databricks log delivery configuration ID.
    config_id: str
    # The optional human-readable name of the log delivery configuration.
    # Defaults to empty.
    config_name: str
    # Time in epoch milliseconds when the log delivery configuration was
    # created.
    creation_time: int
    # The ID for a method:CredetialConfigurations/createCredentialConfig that
    # represents the AWS IAM role with policy and trust relationship as
    # described in the main billable usage documentation page. See [Configure
    # billable usage delivery].
    #
    # [Configure billable usage delivery]: https://docs.databricks.com/administration-guide/account-settings/billable-usage-delivery.html
    credentials_id: str
    # The optional delivery path prefix within Amazon S3 storage. Defaults to
    # empty, which means that logs are delivered to the root of the bucket. This
    # must be a valid S3 object key. This must not start or end with a slash
    # character.
    delivery_path_prefix: str
    # This field applies only if `log_type` is `BILLABLE_USAGE`. This is the
    # optional start month and year for delivery, specified in `YYYY-MM` format.
    # Defaults to current year and month. `BILLABLE_USAGE` logs are not
    # available for usage before March 2019 (`2019-03`).
    delivery_start_time: str
    # Databricks log delivery status.
    log_delivery_status: "LogDeliveryStatus"
    # Log delivery type. Supported values are:
    #
    # * `BILLABLE_USAGE` — Configure [billable usage log delivery]. For the
    # CSV schema, see the [View billable usage].
    #
    # * `AUDIT_LOGS` — Configure [audit log delivery]. For the JSON schema,
    # see [Configure audit logging]
    #
    # [Configure audit logging]: https://docs.databricks.com/administration-guide/account-settings/audit-logs.html
    # [View billable usage]: https://docs.databricks.com/administration-guide/account-settings/usage.html
    # [audit log delivery]: https://docs.databricks.com/administration-guide/account-settings/audit-logs.html
    # [billable usage log delivery]: https://docs.databricks.com/administration-guide/account-settings/billable-usage-delivery.html
    log_type: "LogType"
    # The file type of log delivery.
    #
    # * If `log_type` is `BILLABLE_USAGE`, this value must be `CSV`. Only the
    # CSV (comma-separated values) format is supported. For the schema, see the
    # [View billable usage] * If `log_type` is `AUDIT_LOGS`, this value must be
    # `JSON`. Only the JSON (JavaScript Object Notation) format is supported.
    # For the schema, see the [Configuring audit logs].
    #
    # [Configuring audit logs]: https://docs.databricks.com/administration-guide/account-settings/audit-logs.html
    # [View billable usage]: https://docs.databricks.com/administration-guide/account-settings/usage.html
    output_format: "OutputFormat"
    # Status of log delivery configuration. Set to `ENABLED` (enabled) or
    # `DISABLED` (disabled). Defaults to `ENABLED`. You can [enable or disable
    # the configuration](#operation/patch-log-delivery-config-status) later.
    # Deletion of a configuration is not supported, so disable a log delivery
    # configuration that is no longer needed.
    status: "LogDeliveryConfigStatus"
    # "The ID for a method:StorageConfiguration/createCredentialConfig that
    # represents the S3 bucket with bucket policy as described in the main
    # billable usage documentation page. See [Configure billable usage
    # delivery]."
    #
    # [Configure billable usage delivery]: https://docs.databricks.com/administration-guide/account-settings/billable-usage-delivery.html
    storage_configuration_id: str
    # Time in epoch milliseconds when the log delivery configuration was
    # updated.
    update_time: int
    # Optional filter that specifies workspace IDs to deliver logs for. By
    # default the workspace filter is empty and log delivery applies at the
    # account level, delivering workspace-level logs for all workspaces in your
    # account, plus account level logs. You can optionally set this field to an
    # array of workspace IDs (each one is an `int64`) to which log delivery
    # should apply, in which case only workspace-level logs relating to the
    # specified workspaces are delivered. If you plan to use different log
    # delivery configurations for different workspaces, set this field
    # explicitly. Be aware that delivery configurations mentioning specific
    # workspaces won't apply to new workspaces created in the future, and
    # delivery won't include account level logs. For some types of Databricks
    # deployments there is only one workspace per account ID, so this field is
    # unnecessary.
    workspace_ids_filter: "List[int]"

    def as_dict(self) -> dict:
        body = {}
        if self.account_id:
            body["account_id"] = self.account_id
        if self.config_id:
            body["config_id"] = self.config_id
        if self.config_name:
            body["config_name"] = self.config_name
        if self.creation_time:
            body["creation_time"] = self.creation_time
        if self.credentials_id:
            body["credentials_id"] = self.credentials_id
        if self.delivery_path_prefix:
            body["delivery_path_prefix"] = self.delivery_path_prefix
        if self.delivery_start_time:
            body["delivery_start_time"] = self.delivery_start_time
        if self.log_delivery_status:
            body["log_delivery_status"] = self.log_delivery_status.as_dict()
        if self.log_type:
            body["log_type"] = self.log_type.value
        if self.output_format:
            body["output_format"] = self.output_format.value
        if self.status:
            body["status"] = self.status.value
        if self.storage_configuration_id:
            body["storage_configuration_id"] = self.storage_configuration_id
        if self.update_time:
            body["update_time"] = self.update_time
        if self.workspace_ids_filter:
            body["workspace_ids_filter"] = [v for v in self.workspace_ids_filter]

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "LogDeliveryConfiguration":
        return cls(
            account_id=d.get("account_id", None),
            config_id=d.get("config_id", None),
            config_name=d.get("config_name", None),
            creation_time=d.get("creation_time", None),
            credentials_id=d.get("credentials_id", None),
            delivery_path_prefix=d.get("delivery_path_prefix", None),
            delivery_start_time=d.get("delivery_start_time", None),
            log_delivery_status=LogDeliveryStatus.from_dict(d["log_delivery_status"])
            if "log_delivery_status" in d
            else None,
            log_type=LogType(d["log_type"]) if "log_type" in d else None,
            output_format=OutputFormat(d["output_format"])
            if "output_format" in d
            else None,
            status=LogDeliveryConfigStatus(d["status"]) if "status" in d else None,
            storage_configuration_id=d.get("storage_configuration_id", None),
            update_time=d.get("update_time", None),
            workspace_ids_filter=d.get("workspace_ids_filter", None),
        )


@dataclass
class LogDeliveryStatus:
    """Databricks log delivery status."""

    # The UTC time for the latest log delivery attempt.
    last_attempt_time: str
    # The UTC time for the latest successful log delivery.
    last_successful_attempt_time: str
    # Informative message about the latest log delivery attempt. If the log
    # delivery fails with USER_FAILURE, error details will be provided for
    # fixing misconfigurations in cloud permissions.
    message: str
    # This describes an enum
    status: "DeliveryStatus"

    def as_dict(self) -> dict:
        body = {}
        if self.last_attempt_time:
            body["last_attempt_time"] = self.last_attempt_time
        if self.last_successful_attempt_time:
            body["last_successful_attempt_time"] = self.last_successful_attempt_time
        if self.message:
            body["message"] = self.message
        if self.status:
            body["status"] = self.status.value

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "LogDeliveryStatus":
        return cls(
            last_attempt_time=d.get("last_attempt_time", None),
            last_successful_attempt_time=d.get("last_successful_attempt_time", None),
            message=d.get("message", None),
            status=DeliveryStatus(d["status"]) if "status" in d else None,
        )


class LogType(Enum):
    """Log delivery type. Supported values are:

    * `BILLABLE_USAGE` — Configure [billable usage log delivery]. For the CSV
    schema, see the [View billable usage].

    * `AUDIT_LOGS` — Configure [audit log delivery]. For the JSON schema, see
    [Configure audit logging]

    [Configure audit logging]: https://docs.databricks.com/administration-guide/account-settings/audit-logs.html
    [View billable usage]: https://docs.databricks.com/administration-guide/account-settings/usage.html
    [audit log delivery]: https://docs.databricks.com/administration-guide/account-settings/audit-logs.html
    [billable usage log delivery]: https://docs.databricks.com/administration-guide/account-settings/billable-usage-delivery.html"""

    AUDIT_LOGS = "AUDIT_LOGS"
    BILLABLE_USAGE = "BILLABLE_USAGE"


class OutputFormat(Enum):
    """The file type of log delivery.

    * If `log_type` is `BILLABLE_USAGE`, this value must be `CSV`. Only the CSV
    (comma-separated values) format is supported. For the schema, see the [View
    billable usage] * If `log_type` is `AUDIT_LOGS`, this value must be `JSON`.
    Only the JSON (JavaScript Object Notation) format is supported. For the
    schema, see the [Configuring audit logs].

    [Configuring audit logs]: https://docs.databricks.com/administration-guide/account-settings/audit-logs.html
    [View billable usage]: https://docs.databricks.com/administration-guide/account-settings/usage.html"""

    CSV = "CSV"
    JSON = "JSON"


@dataclass
class UpdateLogDeliveryConfigurationStatusRequest:

    # Databricks log delivery configuration ID
    log_delivery_configuration_id: str  # path
    # Status of log delivery configuration. Set to `ENABLED` (enabled) or
    # `DISABLED` (disabled). Defaults to `ENABLED`. You can [enable or disable
    # the configuration](#operation/patch-log-delivery-config-status) later.
    # Deletion of a configuration is not supported, so disable a log delivery
    # configuration that is no longer needed.
    status: "LogDeliveryConfigStatus"

    def as_dict(self) -> dict:
        body = {}
        if self.log_delivery_configuration_id:
            body["log_delivery_configuration_id"] = self.log_delivery_configuration_id
        if self.status:
            body["status"] = self.status.value

        return body

    @classmethod
    def from_dict(
        cls, d: Dict[str, any]
    ) -> "UpdateLogDeliveryConfigurationStatusRequest":
        return cls(
            log_delivery_configuration_id=d.get("log_delivery_configuration_id", None),
            status=LogDeliveryConfigStatus(d["status"]) if "status" in d else None,
        )


@dataclass
class WrappedBudget:

    # Budget configuration to be created.
    budget: "Budget"
    # Budget ID
    budget_id: str  # path

    def as_dict(self) -> dict:
        body = {}
        if self.budget:
            body["budget"] = self.budget.as_dict()
        if self.budget_id:
            body["budget_id"] = self.budget_id

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "WrappedBudget":
        return cls(
            budget=Budget.from_dict(d["budget"]) if "budget" in d else None,
            budget_id=d.get("budget_id", None),
        )


@dataclass
class WrappedBudgetWithStatus:

    # Budget configuration with daily status.
    budget: "BudgetWithStatus"

    def as_dict(self) -> dict:
        body = {}
        if self.budget:
            body["budget"] = self.budget.as_dict()

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "WrappedBudgetWithStatus":
        return cls(
            budget=BudgetWithStatus.from_dict(d["budget"]) if "budget" in d else None,
        )


@dataclass
class WrappedCreateLogDeliveryConfiguration:

    log_delivery_configuration: "CreateLogDeliveryConfigurationParams"

    def as_dict(self) -> dict:
        body = {}
        if self.log_delivery_configuration:
            body[
                "log_delivery_configuration"
            ] = self.log_delivery_configuration.as_dict()

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "WrappedCreateLogDeliveryConfiguration":
        return cls(
            log_delivery_configuration=CreateLogDeliveryConfigurationParams.from_dict(
                d["log_delivery_configuration"]
            )
            if "log_delivery_configuration" in d
            else None,
        )


@dataclass
class WrappedLogDeliveryConfiguration:

    log_delivery_configuration: "LogDeliveryConfiguration"

    def as_dict(self) -> dict:
        body = {}
        if self.log_delivery_configuration:
            body[
                "log_delivery_configuration"
            ] = self.log_delivery_configuration.as_dict()

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "WrappedLogDeliveryConfiguration":
        return cls(
            log_delivery_configuration=LogDeliveryConfiguration.from_dict(
                d["log_delivery_configuration"]
            )
            if "log_delivery_configuration" in d
            else None,
        )


@dataclass
class WrappedLogDeliveryConfigurations:

    log_delivery_configurations: "List[LogDeliveryConfiguration]"

    def as_dict(self) -> dict:
        body = {}
        if self.log_delivery_configurations:
            body["log_delivery_configurations"] = [
                v.as_dict() for v in self.log_delivery_configurations
            ]

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "WrappedLogDeliveryConfigurations":
        return cls(
            log_delivery_configurations=[
                LogDeliveryConfiguration.from_dict(v)
                for v in d["log_delivery_configurations"]
            ]
            if "log_delivery_configurations" in d
            else None,
        )


class BillableUsageAPI:
    def __init__(self, api_client):
        self._api = api_client

    def download(
        self, start_month: str, end_month: str, *, personal_data: bool = None, **kwargs
    ):
        """Return billable usage logs.

        Returns billable usage logs in CSV format for the specified account and
        date range. For the data schema, see [CSV file schema]. Note that this
        method might take multiple seconds to complete.

        [CSV file schema]: https://docs.databricks.com/administration-guide/account-settings/usage-analysis.html#schema"""

        request = kwargs.get("request", None)
        if not request:
            request = DownloadRequest(
                end_month=end_month,
                personal_data=personal_data,
                start_month=start_month,
            )
        body = request.as_dict()
        query = {}
        if end_month:
            query["end_month"] = end_month
        if personal_data:
            query["personal_data"] = personal_data
        if start_month:
            query["start_month"] = start_month

        self._api.do(
            "GET", f"/api/2.0/accounts//usage/download", query=query, body=body
        )


class BudgetsAPI:
    def __init__(self, api_client):
        self._api = api_client

    def create(
        self, budget: Budget, budget_id: str, **kwargs
    ) -> WrappedBudgetWithStatus:
        """Create a new budget.

        Creates a new budget in the specified account."""

        request = kwargs.get("request", None)
        if not request:
            request = WrappedBudget(budget=budget, budget_id=budget_id)
        body = request.as_dict()
        query = {}

        json = self._api.do(
            "POST", f"/api/2.0/accounts//budget", query=query, body=body
        )
        return WrappedBudgetWithStatus.from_dict(json)

    def delete(self, budget_id: str, **kwargs):
        """Delete budget.

        Deletes the budget specified by its UUID."""

        request = kwargs.get("request", None)
        if not request:
            request = DeleteBudgetRequest(budget_id=budget_id)
        body = request.as_dict()
        query = {}

        self._api.do(
            "DELETE", f"/api/2.0/accounts//budget/{budget_id}", query=query, body=body
        )

    def get(self, budget_id: str, **kwargs) -> WrappedBudgetWithStatus:
        """Get budget and its status.

        Gets the budget specified by its UUID, including noncumulative status
        for each day that the budget is configured to include."""

        request = kwargs.get("request", None)
        if not request:
            request = GetBudgetRequest(budget_id=budget_id)
        body = request.as_dict()
        query = {}

        json = self._api.do(
            "GET", f"/api/2.0/accounts//budget/{budget_id}", query=query, body=body
        )
        return WrappedBudgetWithStatus.from_dict(json)

    def list(self) -> BudgetList:
        """Get all budgets.

        Gets all budgets associated with this account, including noncumulative
        status for each day that the budget is configured to include."""

        json = self._api.do("GET", f"/api/2.0/accounts//budget")
        return BudgetList.from_dict(json)

    def update(self, budget: Budget, budget_id: str, **kwargs):
        """Modify budget.

        Modifies a budget in this account. Budget properties are completely
        overwritten."""

        request = kwargs.get("request", None)
        if not request:
            request = WrappedBudget(budget=budget, budget_id=budget_id)
        body = request.as_dict()
        query = {}

        self._api.do(
            "PATCH", f"/api/2.0/accounts//budget/{budget_id}", query=query, body=body
        )


class LogDeliveryAPI:
    def __init__(self, api_client):
        self._api = api_client

    def create(
        self,
        *,
        log_delivery_configuration: CreateLogDeliveryConfigurationParams = None,
        **kwargs,
    ) -> WrappedLogDeliveryConfiguration:
        """Create a new log delivery configuration.

        Creates a new Databricks log delivery configuration to enable delivery
        of the specified type of logs to your storage location. This requires
        that you already created a [credential
        object](#operation/create-credential-config) (which encapsulates a
        cross-account service IAM role) and a [storage configuration
        object](#operation/create-storage-config) (which encapsulates an S3
        bucket).

        For full details, including the required IAM role policies and bucket
        policies, see [Deliver and access billable usage logs] or [Configure
        audit logging].

        **Note**: There is a limit on the number of log delivery configurations
        available per account (each limit applies separately to each log type
        including billable usage and audit logs). You can create a maximum of
        two enabled account-level delivery configurations (configurations
        without a workspace filter) per type. Additionally, you can create two
        enabled workspace-level delivery configurations per workspace for each
        log type, which means that the same workspace ID can occur in the
        workspace filter for no more than two delivery configurations per log
        type.

        You cannot delete a log delivery configuration, but you can disable it
        (see [Enable or disable log delivery
        configuration](#operation/patch-log-delivery-config-status)).

        [Configure audit logging]: https://docs.databricks.com/administration-guide/account-settings/audit-logs.html
        [Deliver and access billable usage logs]: https://docs.databricks.com/administration-guide/account-settings/billable-usage-delivery.html"""

        request = kwargs.get("request", None)
        if not request:
            request = WrappedCreateLogDeliveryConfiguration(
                log_delivery_configuration=log_delivery_configuration
            )
        body = request.as_dict()
        query = {}

        json = self._api.do(
            "POST", f"/api/2.0/accounts//log-delivery", query=query, body=body
        )
        return WrappedLogDeliveryConfiguration.from_dict(json)

    def get(
        self, log_delivery_configuration_id: str, **kwargs
    ) -> WrappedLogDeliveryConfiguration:
        """Get log delivery configuration.

        Gets a Databricks log delivery configuration object for an account, both
        specified by ID."""

        request = kwargs.get("request", None)
        if not request:
            request = GetLogDeliveryRequest(
                log_delivery_configuration_id=log_delivery_configuration_id
            )
        body = request.as_dict()
        query = {}

        json = self._api.do(
            "GET",
            f"/api/2.0/accounts//log-delivery/{log_delivery_configuration_id}",
            query=query,
            body=body,
        )
        return WrappedLogDeliveryConfiguration.from_dict(json)

    def list(
        self,
        *,
        credentials_id: str = None,
        status: LogDeliveryConfigStatus = None,
        storage_configuration_id: str = None,
        **kwargs,
    ) -> WrappedLogDeliveryConfigurations:
        """Get all log delivery configurations.

        Gets all Databricks log delivery configurations associated with an
        account specified by ID."""

        request = kwargs.get("request", None)
        if not request:
            request = ListLogDeliveryRequest(
                credentials_id=credentials_id,
                status=status,
                storage_configuration_id=storage_configuration_id,
            )
        body = request.as_dict()
        query = {}
        if credentials_id:
            query["credentials_id"] = credentials_id
        if status:
            query["status"] = status.value
        if storage_configuration_id:
            query["storage_configuration_id"] = storage_configuration_id

        json = self._api.do(
            "GET", f"/api/2.0/accounts//log-delivery", query=query, body=body
        )
        return WrappedLogDeliveryConfigurations.from_dict(json)

    def patch_status(
        self,
        status: LogDeliveryConfigStatus,
        log_delivery_configuration_id: str,
        **kwargs,
    ):
        """Enable or disable log delivery configuration.

        Enables or disables a log delivery configuration. Deletion of delivery
        configurations is not supported, so disable log delivery configurations
        that are no longer needed. Note that you can't re-enable a delivery
        configuration if this would violate the delivery configuration limits
        described under [Create log
        delivery](#operation/create-log-delivery-config)."""

        request = kwargs.get("request", None)
        if not request:
            request = UpdateLogDeliveryConfigurationStatusRequest(
                log_delivery_configuration_id=log_delivery_configuration_id,
                status=status,
            )
        body = request.as_dict()
        query = {}

        self._api.do(
            "PATCH",
            f"/api/2.0/accounts//log-delivery/{log_delivery_configuration_id}",
            query=query,
            body=body,
        )
