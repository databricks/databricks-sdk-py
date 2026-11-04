Lakewatch
=========

These dataclasses are used in the SDK to represent API requests and responses for services in the ``databricks.sdk.service.lakewatch`` module.

.. py:currentmodule:: databricks.sdk.service.lakewatch
.. autoclass:: AlertConfig
   :members:
   :undoc-members:

.. autoclass:: AutoLoader
   :members:
   :undoc-members:

.. py:class:: AutoLoaderFormat

   File format of the source files that Auto Loader reads.

   .. py:attribute:: AUTOLOADER_FORMAT_CSV
      :value: "AUTOLOADER_FORMAT_CSV"

   .. py:attribute:: AUTOLOADER_FORMAT_JSON
      :value: "AUTOLOADER_FORMAT_JSON"

   .. py:attribute:: AUTOLOADER_FORMAT_JSONL
      :value: "AUTOLOADER_FORMAT_JSONL"

   .. py:attribute:: AUTOLOADER_FORMAT_PARQUET
      :value: "AUTOLOADER_FORMAT_PARQUET"

   .. py:attribute:: AUTOLOADER_FORMAT_XML
      :value: "AUTOLOADER_FORMAT_XML"

.. autoclass:: CloudWatchLogsEnvelope
   :members:
   :undoc-members:

.. autoclass:: CommonConfig
   :members:
   :undoc-members:

.. autoclass:: ContentPackReference
   :members:
   :undoc-members:

.. autoclass:: Datasource
   :members:
   :undoc-members:

.. py:class:: DatasourceComputeMode

   Compute mode for the datasource's ingestion job.

   .. py:attribute:: DS_COMPUTE_PERFORMANCE_OPTIMIZED
      :value: "DS_COMPUTE_PERFORMANCE_OPTIMIZED"

   .. py:attribute:: DS_COMPUTE_STANDARD
      :value: "DS_COMPUTE_STANDARD"

.. autoclass:: DatasourceConfig
   :members:
   :undoc-members:

.. autoclass:: DatasourceStatus
   :members:
   :undoc-members:

.. py:class:: DatasourceView

   Which fields list responses return for each datasource.

   .. py:attribute:: DATASOURCE_VIEW_BASIC
      :value: "DATASOURCE_VIEW_BASIC"

   .. py:attribute:: DATASOURCE_VIEW_FULL
      :value: "DATASOURCE_VIEW_FULL"

.. autoclass:: Envelope
   :members:
   :undoc-members:

.. autoclass:: ExistingTable
   :members:
   :undoc-members:

.. autoclass:: ExportConfig
   :members:
   :undoc-members:

.. autoclass:: JiraExportConfig
   :members:
   :undoc-members:

.. autoclass:: JsonArrayEnvelope
   :members:
   :undoc-members:

.. autoclass:: ListDatasourcesResponse
   :members:
   :undoc-members:

.. autoclass:: ListRulesResponse
   :members:
   :undoc-members:

.. autoclass:: ParserRef
   :members:
   :undoc-members:

.. autoclass:: Principal
   :members:
   :undoc-members:

.. py:class:: PrincipalType

   Type of a principal (user / SP / system).

   .. py:attribute:: REGULAR_USER
      :value: "REGULAR_USER"

   .. py:attribute:: SERVICE_PRINCIPAL
      :value: "SERVICE_PRINCIPAL"

   .. py:attribute:: SYSTEM_USER
      :value: "SYSTEM_USER"

.. autoclass:: ResourceStatus
   :members:
   :undoc-members:

.. py:class:: ResourceStatusLifecycle

   Configured scheduling / existence of the job or pipeline.

   .. py:attribute:: DELETED
      :value: "DELETED"

   .. py:attribute:: SCHEDULED
      :value: "SCHEDULED"

   .. py:attribute:: STOPPED
      :value: "STOPPED"

   .. py:attribute:: UNSCHEDULED
      :value: "UNSCHEDULED"

.. py:class:: ResourceStatusRunState

   Outcome / progress of the most recent (or in-flight) run.

   .. py:attribute:: CANCELED
      :value: "CANCELED"

   .. py:attribute:: FAILED
      :value: "FAILED"

   .. py:attribute:: RUNNING
      :value: "RUNNING"

   .. py:attribute:: SUCCEEDED
      :value: "SUCCEEDED"

.. autoclass:: Rule
   :members:
   :undoc-members:

.. autoclass:: RuleConfig
   :members:
   :undoc-members:

.. py:class:: RuleDeduplication

   Signal deduplication mode for a detection rule.

   .. py:attribute:: DEDUPLICATION_DEFAULT
      :value: "DEDUPLICATION_DEFAULT"

   .. py:attribute:: DEDUPLICATION_DISABLED
      :value: "DEDUPLICATION_DISABLED"

   .. py:attribute:: DEDUPLICATION_ENABLED
      :value: "DEDUPLICATION_ENABLED"

.. py:class:: RuleFidelity

   Maturity of a detection rule.

   .. py:attribute:: FIDELITY_DEVELOPMENT
      :value: "FIDELITY_DEVELOPMENT"

   .. py:attribute:: FIDELITY_HIGH
      :value: "FIDELITY_HIGH"

   .. py:attribute:: FIDELITY_INVESTIGATIVE
      :value: "FIDELITY_INVESTIGATIVE"

   .. py:attribute:: FIDELITY_MEDIUM
      :value: "FIDELITY_MEDIUM"

.. autoclass:: RuleInputBatch
   :members:
   :undoc-members:

.. autoclass:: RuleInputBatchSql
   :members:
   :undoc-members:

.. autoclass:: RuleInputCustomNotebook
   :members:
   :undoc-members:

.. autoclass:: RuleMitreMapping
   :members:
   :undoc-members:

.. autoclass:: RuleOutput
   :members:
   :undoc-members:

.. autoclass:: RuleSchedule
   :members:
   :undoc-members:

.. autoclass:: RuleTimeRange
   :members:
   :undoc-members:

.. py:class:: RuleView

   Selects how much of each rule a list response returns.

   .. py:attribute:: RULE_VIEW_BASIC
      :value: "RULE_VIEW_BASIC"

   .. py:attribute:: RULE_VIEW_FULL
      :value: "RULE_VIEW_FULL"

.. autoclass:: Schedule
   :members:
   :undoc-members:

.. autoclass:: ServiceNowExportConfig
   :members:
   :undoc-members:

.. autoclass:: SlackExportConfig
   :members:
   :undoc-members:

.. autoclass:: TableName
   :members:
   :undoc-members:

.. autoclass:: TinesExportConfig
   :members:
   :undoc-members:

.. autoclass:: UnityCatalogConnection
   :members:
   :undoc-members:

.. autoclass:: WebhookExportConfig
   :members:
   :undoc-members:
