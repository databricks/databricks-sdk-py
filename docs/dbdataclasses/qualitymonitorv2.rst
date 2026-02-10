Quality Monitor
===============

These dataclasses are used in the SDK to represent API requests and responses for services in the ``databricks.sdk.service.qualitymonitorv2`` module.

.. py:currentmodule:: databricks.sdk.service.qualitymonitorv2
.. autoclass:: AnomalyDetectionConfig
   :members:
   :undoc-members:

.. py:class:: AnomalyDetectionRunStatus

   Status of Anomaly Detection Job Run

   .. py:attribute:: ANOMALY_DETECTION_RUN_STATUS_CANCELED
      :value: "ANOMALY_DETECTION_RUN_STATUS_CANCELED"

   .. py:attribute:: ANOMALY_DETECTION_RUN_STATUS_FAILED
      :value: "ANOMALY_DETECTION_RUN_STATUS_FAILED"

   .. py:attribute:: ANOMALY_DETECTION_RUN_STATUS_JOB_DELETED
      :value: "ANOMALY_DETECTION_RUN_STATUS_JOB_DELETED"

   .. py:attribute:: ANOMALY_DETECTION_RUN_STATUS_PENDING
      :value: "ANOMALY_DETECTION_RUN_STATUS_PENDING"

   .. py:attribute:: ANOMALY_DETECTION_RUN_STATUS_RUNNING
      :value: "ANOMALY_DETECTION_RUN_STATUS_RUNNING"

   .. py:attribute:: ANOMALY_DETECTION_RUN_STATUS_SUCCESS
      :value: "ANOMALY_DETECTION_RUN_STATUS_SUCCESS"

   .. py:attribute:: ANOMALY_DETECTION_RUN_STATUS_UNKNOWN
      :value: "ANOMALY_DETECTION_RUN_STATUS_UNKNOWN"

   .. py:attribute:: ANOMALY_DETECTION_RUN_STATUS_WORKSPACE_MISMATCH_ERROR
      :value: "ANOMALY_DETECTION_RUN_STATUS_WORKSPACE_MISMATCH_ERROR"

.. py:class:: HostType

   Enum representing the type of Databricks host.

   .. py:attribute:: ACCOUNTS
      :value: "ACCOUNTS"

   .. py:attribute:: WORKSPACE
      :value: "WORKSPACE"

   .. py:attribute:: UNIFIED
      :value: "UNIFIED"

.. autoclass:: ListQualityMonitorResponse
   :members:
   :undoc-members:

.. autoclass:: PercentNullValidityCheck
   :members:
   :undoc-members:

.. autoclass:: QualityMonitor
   :members:
   :undoc-members:

.. autoclass:: RangeValidityCheck
   :members:
   :undoc-members:

.. autoclass:: UniquenessValidityCheck
   :members:
   :undoc-members:

.. autoclass:: ValidityCheckConfiguration
   :members:
   :undoc-members:
