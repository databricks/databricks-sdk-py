Clean Rooms
===========

These dataclasses are used in the SDK to represent API requests and responses for services in the ``databricks.sdk.service.cleanrooms`` module.

.. py:currentmodule:: databricks.sdk.service.cleanrooms
.. autoclass:: CleanRoom
   :members:
   :undoc-members:

.. py:class:: CleanRoomAccessRestricted

   .. py:attribute:: CSP_MISMATCH
      :value: "CSP_MISMATCH"

   .. py:attribute:: NO_RESTRICTION
      :value: "NO_RESTRICTION"

.. autoclass:: CleanRoomAsset
   :members:
   :undoc-members:

.. py:class:: CleanRoomAssetAssetType

   .. py:attribute:: FOREIGN_TABLE
      :value: "FOREIGN_TABLE"

   .. py:attribute:: NOTEBOOK_FILE
      :value: "NOTEBOOK_FILE"

   .. py:attribute:: TABLE
      :value: "TABLE"

   .. py:attribute:: VIEW
      :value: "VIEW"

   .. py:attribute:: VOLUME
      :value: "VOLUME"

.. autoclass:: CleanRoomAssetForeignTable
   :members:
   :undoc-members:

.. autoclass:: CleanRoomAssetForeignTableLocalDetails
   :members:
   :undoc-members:

.. autoclass:: CleanRoomAssetNotebook
   :members:
   :undoc-members:

.. py:class:: CleanRoomAssetStatusEnum

   .. py:attribute:: ACTIVE
      :value: "ACTIVE"

   .. py:attribute:: PENDING
      :value: "PENDING"

   .. py:attribute:: PERMISSION_DENIED
      :value: "PERMISSION_DENIED"

.. autoclass:: CleanRoomAssetTable
   :members:
   :undoc-members:

.. autoclass:: CleanRoomAssetTableLocalDetails
   :members:
   :undoc-members:

.. autoclass:: CleanRoomAssetView
   :members:
   :undoc-members:

.. autoclass:: CleanRoomAssetViewLocalDetails
   :members:
   :undoc-members:

.. autoclass:: CleanRoomAssetVolumeLocalDetails
   :members:
   :undoc-members:

.. autoclass:: CleanRoomCollaborator
   :members:
   :undoc-members:

.. autoclass:: CleanRoomNotebookReview
   :members:
   :undoc-members:

.. py:class:: CleanRoomNotebookReviewNotebookReviewState

   .. py:attribute:: APPROVED
      :value: "APPROVED"

   .. py:attribute:: PENDING
      :value: "PENDING"

   .. py:attribute:: REJECTED
      :value: "REJECTED"

.. py:class:: CleanRoomNotebookReviewNotebookReviewSubReason

   .. py:attribute:: AUTO_APPROVED
      :value: "AUTO_APPROVED"

   .. py:attribute:: BACKFILLED
      :value: "BACKFILLED"

.. autoclass:: CleanRoomNotebookTaskRun
   :members:
   :undoc-members:

.. autoclass:: CleanRoomOutputCatalog
   :members:
   :undoc-members:

.. py:class:: CleanRoomOutputCatalogOutputCatalogStatus

   .. py:attribute:: CREATED
      :value: "CREATED"

   .. py:attribute:: NOT_CREATED
      :value: "NOT_CREATED"

   .. py:attribute:: NOT_ELIGIBLE
      :value: "NOT_ELIGIBLE"

.. autoclass:: CleanRoomRemoteDetail
   :members:
   :undoc-members:

.. py:class:: CleanRoomStatusEnum

   .. py:attribute:: ACTIVE
      :value: "ACTIVE"

   .. py:attribute:: DELETED
      :value: "DELETED"

   .. py:attribute:: FAILED
      :value: "FAILED"

   .. py:attribute:: PROVISIONING
      :value: "PROVISIONING"

.. autoclass:: CollaboratorJobRunInfo
   :members:
   :undoc-members:

.. autoclass:: ComplianceSecurityProfile
   :members:
   :undoc-members:

.. autoclass:: CreateCleanRoomOutputCatalogResponse
   :members:
   :undoc-members:

.. autoclass:: DeleteCleanRoomAssetResponse
   :members:
   :undoc-members:

.. autoclass:: DeleteResponse
   :members:
   :undoc-members:

.. autoclass:: ListCleanRoomAssetsResponse
   :members:
   :undoc-members:

.. autoclass:: ListCleanRoomNotebookTaskRunsResponse
   :members:
   :undoc-members:

.. autoclass:: ListCleanRoomsResponse
   :members:
   :undoc-members:

.. autoclass:: Token
   :members:
   :undoc-members:

.. autoclass:: UpdateCleanRoomRequest
   :members:
   :undoc-members:
