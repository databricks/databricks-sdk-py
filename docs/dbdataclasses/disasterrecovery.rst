Disaster Recovery
=================

These dataclasses are used in the SDK to represent API requests and responses for services in the ``databricks.sdk.service.disasterrecovery`` module.

.. py:currentmodule:: databricks.sdk.service.disasterrecovery
.. py:class:: FailoverFailoverGroupRequestFailoverType

   The type of failover to perform.

   .. py:attribute:: FORCED
      :value: "FORCED"

.. autoclass:: FailoverGroup
   :members:
   :undoc-members:

.. py:class:: FailoverGroupState

   The aggregate state of a FailoverGroup.

   .. py:attribute:: ACTIVE
      :value: "ACTIVE"

   .. py:attribute:: CREATING
      :value: "CREATING"

   .. py:attribute:: CREATION_FAILED
      :value: "CREATION_FAILED"

   .. py:attribute:: DELETING
      :value: "DELETING"

   .. py:attribute:: DELETION_FAILED
      :value: "DELETION_FAILED"

   .. py:attribute:: FAILING_OVER
      :value: "FAILING_OVER"

   .. py:attribute:: FAILOVER_FAILED
      :value: "FAILOVER_FAILED"

   .. py:attribute:: INITIAL_REPLICATION
      :value: "INITIAL_REPLICATION"

.. autoclass:: ListFailoverGroupsResponse
   :members:
   :undoc-members:

.. autoclass:: ListStableUrlsResponse
   :members:
   :undoc-members:

.. autoclass:: LocationMapping
   :members:
   :undoc-members:

.. autoclass:: LocationMappingEntry
   :members:
   :undoc-members:

.. autoclass:: StableUrl
   :members:
   :undoc-members:

.. autoclass:: UcCatalog
   :members:
   :undoc-members:

.. autoclass:: UcReplicationConfig
   :members:
   :undoc-members:

.. autoclass:: WorkspaceSet
   :members:
   :undoc-members:
