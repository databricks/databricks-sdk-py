Data Quality
============

These dataclasses are used in the SDK to represent API requests and responses for services in the ``databricks.sdk.service.dataquality`` module.

.. py:currentmodule:: databricks.sdk.service.dataquality
.. py:class:: AggregationGranularity

   The granularity for aggregating data into time windows based on their timestamp.

   .. py:attribute:: AGGREGATION_GRANULARITY_1_DAY
      :value: "AGGREGATION_GRANULARITY_1_DAY"

   .. py:attribute:: AGGREGATION_GRANULARITY_1_HOUR
      :value: "AGGREGATION_GRANULARITY_1_HOUR"

   .. py:attribute:: AGGREGATION_GRANULARITY_1_MONTH
      :value: "AGGREGATION_GRANULARITY_1_MONTH"

   .. py:attribute:: AGGREGATION_GRANULARITY_1_WEEK
      :value: "AGGREGATION_GRANULARITY_1_WEEK"

   .. py:attribute:: AGGREGATION_GRANULARITY_1_YEAR
      :value: "AGGREGATION_GRANULARITY_1_YEAR"

   .. py:attribute:: AGGREGATION_GRANULARITY_2_WEEKS
      :value: "AGGREGATION_GRANULARITY_2_WEEKS"

   .. py:attribute:: AGGREGATION_GRANULARITY_30_MINUTES
      :value: "AGGREGATION_GRANULARITY_30_MINUTES"

   .. py:attribute:: AGGREGATION_GRANULARITY_3_WEEKS
      :value: "AGGREGATION_GRANULARITY_3_WEEKS"

   .. py:attribute:: AGGREGATION_GRANULARITY_4_WEEKS
      :value: "AGGREGATION_GRANULARITY_4_WEEKS"

   .. py:attribute:: AGGREGATION_GRANULARITY_5_MINUTES
      :value: "AGGREGATION_GRANULARITY_5_MINUTES"

.. autoclass:: AnomalyDetectionConfig
   :members:
   :undoc-members:

.. autoclass:: CancelRefreshResponse
   :members:
   :undoc-members:

.. autoclass:: CronSchedule
   :members:
   :undoc-members:

.. py:class:: CronSchedulePauseStatus

   The data quality monitoring workflow cron schedule pause status.

   .. py:attribute:: CRON_SCHEDULE_PAUSE_STATUS_PAUSED
      :value: "CRON_SCHEDULE_PAUSE_STATUS_PAUSED"

   .. py:attribute:: CRON_SCHEDULE_PAUSE_STATUS_UNPAUSED
      :value: "CRON_SCHEDULE_PAUSE_STATUS_UNPAUSED"

.. autoclass:: DataProfilingConfig
   :members:
   :undoc-members:

.. autoclass:: DataProfilingCustomMetric
   :members:
   :undoc-members:

.. py:class:: DataProfilingCustomMetricType

   The custom metric type.

   .. py:attribute:: DATA_PROFILING_CUSTOM_METRIC_TYPE_AGGREGATE
      :value: "DATA_PROFILING_CUSTOM_METRIC_TYPE_AGGREGATE"

   .. py:attribute:: DATA_PROFILING_CUSTOM_METRIC_TYPE_DERIVED
      :value: "DATA_PROFILING_CUSTOM_METRIC_TYPE_DERIVED"

   .. py:attribute:: DATA_PROFILING_CUSTOM_METRIC_TYPE_DRIFT
      :value: "DATA_PROFILING_CUSTOM_METRIC_TYPE_DRIFT"

.. py:class:: DataProfilingStatus

   The status of the data profiling monitor.

   .. py:attribute:: DATA_PROFILING_STATUS_ACTIVE
      :value: "DATA_PROFILING_STATUS_ACTIVE"

   .. py:attribute:: DATA_PROFILING_STATUS_DELETE_PENDING
      :value: "DATA_PROFILING_STATUS_DELETE_PENDING"

   .. py:attribute:: DATA_PROFILING_STATUS_ERROR
      :value: "DATA_PROFILING_STATUS_ERROR"

   .. py:attribute:: DATA_PROFILING_STATUS_FAILED
      :value: "DATA_PROFILING_STATUS_FAILED"

   .. py:attribute:: DATA_PROFILING_STATUS_PENDING
      :value: "DATA_PROFILING_STATUS_PENDING"

.. py:class:: HostType

   Enum representing the type of Databricks host.

   .. py:attribute:: ACCOUNTS
      :value: "ACCOUNTS"

   .. py:attribute:: WORKSPACE
      :value: "WORKSPACE"

   .. py:attribute:: UNIFIED
      :value: "UNIFIED"

.. autoclass:: InferenceLogConfig
   :members:
   :undoc-members:

.. py:class:: InferenceProblemType

   Inference problem type the model aims to solve.

   .. py:attribute:: INFERENCE_PROBLEM_TYPE_CLASSIFICATION
      :value: "INFERENCE_PROBLEM_TYPE_CLASSIFICATION"

   .. py:attribute:: INFERENCE_PROBLEM_TYPE_REGRESSION
      :value: "INFERENCE_PROBLEM_TYPE_REGRESSION"

.. autoclass:: ListMonitorResponse
   :members:
   :undoc-members:

.. autoclass:: ListRefreshResponse
   :members:
   :undoc-members:

.. autoclass:: Monitor
   :members:
   :undoc-members:

.. autoclass:: NotificationDestination
   :members:
   :undoc-members:

.. autoclass:: NotificationSettings
   :members:
   :undoc-members:

.. autoclass:: Refresh
   :members:
   :undoc-members:

.. py:class:: RefreshState

   The state of the refresh.

   .. py:attribute:: MONITOR_REFRESH_STATE_CANCELED
      :value: "MONITOR_REFRESH_STATE_CANCELED"

   .. py:attribute:: MONITOR_REFRESH_STATE_FAILED
      :value: "MONITOR_REFRESH_STATE_FAILED"

   .. py:attribute:: MONITOR_REFRESH_STATE_PENDING
      :value: "MONITOR_REFRESH_STATE_PENDING"

   .. py:attribute:: MONITOR_REFRESH_STATE_RUNNING
      :value: "MONITOR_REFRESH_STATE_RUNNING"

   .. py:attribute:: MONITOR_REFRESH_STATE_SUCCESS
      :value: "MONITOR_REFRESH_STATE_SUCCESS"

   .. py:attribute:: MONITOR_REFRESH_STATE_UNKNOWN
      :value: "MONITOR_REFRESH_STATE_UNKNOWN"

.. py:class:: RefreshTrigger

   The trigger of the refresh.

   .. py:attribute:: MONITOR_REFRESH_TRIGGER_DATA_CHANGE
      :value: "MONITOR_REFRESH_TRIGGER_DATA_CHANGE"

   .. py:attribute:: MONITOR_REFRESH_TRIGGER_MANUAL
      :value: "MONITOR_REFRESH_TRIGGER_MANUAL"

   .. py:attribute:: MONITOR_REFRESH_TRIGGER_SCHEDULE
      :value: "MONITOR_REFRESH_TRIGGER_SCHEDULE"

   .. py:attribute:: MONITOR_REFRESH_TRIGGER_UNKNOWN
      :value: "MONITOR_REFRESH_TRIGGER_UNKNOWN"

.. autoclass:: SnapshotConfig
   :members:
   :undoc-members:

.. autoclass:: TimeSeriesConfig
   :members:
   :undoc-members:
