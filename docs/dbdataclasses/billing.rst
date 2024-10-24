Billing
=======

These dataclasses are used in the SDK to represent API requests and responses for services in the ``databricks.sdk.service.billing`` module.

.. py:currentmodule:: databricks.sdk.service.billing
.. autoclass:: Budget
   :members:
   :undoc-members:

.. autoclass:: BudgetAlert
   :members:
   :undoc-members:

.. autoclass:: BudgetList
   :members:
   :undoc-members:

.. autoclass:: BudgetWithStatus
   :members:
   :undoc-members:

.. autoclass:: BudgetWithStatusStatusDailyItem
   :members:
   :undoc-members:

.. autoclass:: CreateLogDeliveryConfigurationParams
   :members:
   :undoc-members:

.. autoclass:: DeleteResponse
   :members:
   :undoc-members:

.. py:class:: DeliveryStatus

   The status string for log delivery. Possible values are: * `CREATED`: There were no log delivery attempts since the config was created. * `SUCCEEDED`: The latest attempt of log delivery has succeeded completely. * `USER_FAILURE`: The latest attempt of log delivery failed because of misconfiguration of customer provided permissions on role or storage. * `SYSTEM_FAILURE`: The latest attempt of log delivery failed because of an Databricks internal error. Contact support if it doesn't go away soon. * `NOT_FOUND`: The log delivery status as the configuration has been disabled since the release of this feature or there are no workspaces in the account.

   .. py:attribute:: CREATED
      :value: "CREATED"

   .. py:attribute:: NOT_FOUND
      :value: "NOT_FOUND"

   .. py:attribute:: SUCCEEDED
      :value: "SUCCEEDED"

   .. py:attribute:: SYSTEM_FAILURE
      :value: "SYSTEM_FAILURE"

   .. py:attribute:: USER_FAILURE
      :value: "USER_FAILURE"

.. autoclass:: DownloadResponse
   :members:
   :undoc-members:

.. py:class:: LogDeliveryConfigStatus

   Status of log delivery configuration. Set to `ENABLED` (enabled) or `DISABLED` (disabled). Defaults to `ENABLED`. You can [enable or disable the configuration](#operation/patch-log-delivery-config-status) later. Deletion of a configuration is not supported, so disable a log delivery configuration that is no longer needed.

   .. py:attribute:: DISABLED
      :value: "DISABLED"

   .. py:attribute:: ENABLED
      :value: "ENABLED"

.. autoclass:: LogDeliveryConfiguration
   :members:
   :undoc-members:

.. autoclass:: LogDeliveryStatus
   :members:
   :undoc-members:

.. py:class:: LogType

   Log delivery type. Supported values are:
   * `BILLABLE_USAGE` — Configure [billable usage log delivery]. For the CSV schema, see the [View billable usage].
   * `AUDIT_LOGS` — Configure [audit log delivery]. For the JSON schema, see [Configure audit logging]
   [Configure audit logging]: https://docs.databricks.com/administration-guide/account-settings/audit-logs.html [View billable usage]: https://docs.databricks.com/administration-guide/account-settings/usage.html [audit log delivery]: https://docs.databricks.com/administration-guide/account-settings/audit-logs.html [billable usage log delivery]: https://docs.databricks.com/administration-guide/account-settings/billable-usage-delivery.html

   .. py:attribute:: AUDIT_LOGS
      :value: "AUDIT_LOGS"

   .. py:attribute:: BILLABLE_USAGE
      :value: "BILLABLE_USAGE"

.. py:class:: OutputFormat

   The file type of log delivery.
   * If `log_type` is `BILLABLE_USAGE`, this value must be `CSV`. Only the CSV (comma-separated values) format is supported. For the schema, see the [View billable usage] * If `log_type` is `AUDIT_LOGS`, this value must be `JSON`. Only the JSON (JavaScript Object Notation) format is supported. For the schema, see the [Configuring audit logs].
   [Configuring audit logs]: https://docs.databricks.com/administration-guide/account-settings/audit-logs.html [View billable usage]: https://docs.databricks.com/administration-guide/account-settings/usage.html

   .. py:attribute:: CSV
      :value: "CSV"

   .. py:attribute:: JSON
      :value: "JSON"

.. autoclass:: PatchStatusResponse
   :members:
   :undoc-members:

.. autoclass:: UpdateLogDeliveryConfigurationStatusRequest
   :members:
   :undoc-members:

.. autoclass:: UpdateResponse
   :members:
   :undoc-members:

.. autoclass:: WrappedBudget
   :members:
   :undoc-members:

.. autoclass:: WrappedBudgetWithStatus
   :members:
   :undoc-members:

.. autoclass:: WrappedCreateLogDeliveryConfiguration
   :members:
   :undoc-members:

.. autoclass:: WrappedLogDeliveryConfiguration
   :members:
   :undoc-members:

.. autoclass:: WrappedLogDeliveryConfigurations
   :members:
   :undoc-members:
