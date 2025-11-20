Billing
=======

These dataclasses are used in the SDK to represent API requests and responses for services in the ``databricks.sdk.service.billing`` module.

.. py:currentmodule:: databricks.sdk.service.billing
.. autoclass:: ActionConfiguration
   :members:
   :undoc-members:

.. py:class:: ActionConfigurationType

   .. py:attribute:: EMAIL_NOTIFICATION
      :value: "EMAIL_NOTIFICATION"

.. autoclass:: AlertConfiguration
   :members:
   :undoc-members:

.. py:class:: AlertConfigurationQuantityType

   .. py:attribute:: LIST_PRICE_DOLLARS_USD
      :value: "LIST_PRICE_DOLLARS_USD"

.. py:class:: AlertConfigurationTimePeriod

   .. py:attribute:: MONTH
      :value: "MONTH"

.. py:class:: AlertConfigurationTriggerType

   .. py:attribute:: CUMULATIVE_SPENDING_EXCEEDED
      :value: "CUMULATIVE_SPENDING_EXCEEDED"

.. autoclass:: BudgetConfiguration
   :members:
   :undoc-members:

.. autoclass:: BudgetConfigurationFilter
   :members:
   :undoc-members:

.. autoclass:: BudgetConfigurationFilterClause
   :members:
   :undoc-members:

.. py:class:: BudgetConfigurationFilterOperator

   .. py:attribute:: IN
      :value: "IN"

.. autoclass:: BudgetConfigurationFilterTagClause
   :members:
   :undoc-members:

.. autoclass:: BudgetConfigurationFilterWorkspaceIdClause
   :members:
   :undoc-members:

.. autoclass:: BudgetPolicy
   :members:
   :undoc-members:

.. autoclass:: CreateBillingUsageDashboardResponse
   :members:
   :undoc-members:

.. autoclass:: CreateBudgetConfigurationBudget
   :members:
   :undoc-members:

.. autoclass:: CreateBudgetConfigurationBudgetActionConfigurations
   :members:
   :undoc-members:

.. autoclass:: CreateBudgetConfigurationBudgetAlertConfigurations
   :members:
   :undoc-members:

.. autoclass:: CreateBudgetConfigurationResponse
   :members:
   :undoc-members:

.. autoclass:: CreateLogDeliveryConfigurationParams
   :members:
   :undoc-members:

.. autoclass:: DeleteBudgetConfigurationResponse
   :members:
   :undoc-members:

.. py:class:: DeliveryStatus

   * The status string for log delivery. Possible values are: `CREATED`: There were no log delivery attempts since the config was created. `SUCCEEDED`: The latest attempt of log delivery has succeeded completely. `USER_FAILURE`: The latest attempt of log delivery failed because of misconfiguration of customer provided permissions on role or storage. `SYSTEM_FAILURE`: The latest attempt of log delivery failed because of an Databricks internal error. Contact support if it doesn't go away soon. `NOT_FOUND`: The log delivery status as the configuration has been disabled since the release of this feature or there are no workspaces in the account.

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

.. autoclass:: Filter
   :members:
   :undoc-members:

.. autoclass:: GetBillingUsageDashboardResponse
   :members:
   :undoc-members:

.. autoclass:: GetBudgetConfigurationResponse
   :members:
   :undoc-members:

.. autoclass:: GetLogDeliveryConfigurationResponse
   :members:
   :undoc-members:

.. autoclass:: LimitConfig
   :members:
   :undoc-members:

.. autoclass:: ListBudgetConfigurationsResponse
   :members:
   :undoc-members:

.. autoclass:: ListBudgetPoliciesResponse
   :members:
   :undoc-members:

.. autoclass:: ListUsagePoliciesResponse
   :members:
   :undoc-members:

.. py:class:: LogDeliveryConfigStatus

   * Log Delivery Status
   `ENABLED`: All dependencies have executed and succeeded `DISABLED`: At least one dependency has succeeded

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

   * Log Delivery Type

   .. py:attribute:: AUDIT_LOGS
      :value: "AUDIT_LOGS"

   .. py:attribute:: BILLABLE_USAGE
      :value: "BILLABLE_USAGE"

.. py:class:: OutputFormat

   * Log Delivery Output Format

   .. py:attribute:: CSV
      :value: "CSV"

   .. py:attribute:: JSON
      :value: "JSON"

.. autoclass:: PatchStatusResponse
   :members:
   :undoc-members:

.. autoclass:: SortSpec
   :members:
   :undoc-members:

.. py:class:: SortSpecField

   .. py:attribute:: POLICY_NAME
      :value: "POLICY_NAME"

.. autoclass:: UpdateBudgetConfigurationBudget
   :members:
   :undoc-members:

.. autoclass:: UpdateBudgetConfigurationResponse
   :members:
   :undoc-members:

.. py:class:: UsageDashboardMajorVersion

   .. py:attribute:: USAGE_DASHBOARD_MAJOR_VERSION_1
      :value: "USAGE_DASHBOARD_MAJOR_VERSION_1"

   .. py:attribute:: USAGE_DASHBOARD_MAJOR_VERSION_2
      :value: "USAGE_DASHBOARD_MAJOR_VERSION_2"

.. py:class:: UsageDashboardType

   .. py:attribute:: USAGE_DASHBOARD_TYPE_GLOBAL
      :value: "USAGE_DASHBOARD_TYPE_GLOBAL"

   .. py:attribute:: USAGE_DASHBOARD_TYPE_WORKSPACE
      :value: "USAGE_DASHBOARD_TYPE_WORKSPACE"

.. autoclass:: UsagePolicy
   :members:
   :undoc-members:

.. autoclass:: WrappedLogDeliveryConfiguration
   :members:
   :undoc-members:

.. autoclass:: WrappedLogDeliveryConfigurations
   :members:
   :undoc-members:
