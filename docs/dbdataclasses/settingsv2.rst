SettingsV2
==========

These dataclasses are used in the SDK to represent API requests and responses for services in the ``databricks.sdk.service.settingsv2`` module.

.. py:currentmodule:: databricks.sdk.service.settingsv2
.. autoclass:: AibiDashboardEmbeddingAccessPolicy
   :members:
   :undoc-members:

.. py:class:: AibiDashboardEmbeddingAccessPolicyAccessPolicyType

   .. py:attribute:: ALLOW_ALL_DOMAINS
      :value: "ALLOW_ALL_DOMAINS"

   .. py:attribute:: ALLOW_APPROVED_DOMAINS
      :value: "ALLOW_APPROVED_DOMAINS"

   .. py:attribute:: DENY_ALL_DOMAINS
      :value: "DENY_ALL_DOMAINS"

.. autoclass:: AibiDashboardEmbeddingApprovedDomains
   :members:
   :undoc-members:

.. autoclass:: BooleanMessage
   :members:
   :undoc-members:

.. autoclass:: ClusterAutoRestartMessage
   :members:
   :undoc-members:

.. autoclass:: ClusterAutoRestartMessageEnablementDetails
   :members:
   :undoc-members:

.. autoclass:: ClusterAutoRestartMessageMaintenanceWindow
   :members:
   :undoc-members:

.. py:class:: ClusterAutoRestartMessageMaintenanceWindowDayOfWeek

   .. py:attribute:: FRIDAY
      :value: "FRIDAY"

   .. py:attribute:: MONDAY
      :value: "MONDAY"

   .. py:attribute:: SATURDAY
      :value: "SATURDAY"

   .. py:attribute:: SUNDAY
      :value: "SUNDAY"

   .. py:attribute:: THURSDAY
      :value: "THURSDAY"

   .. py:attribute:: TUESDAY
      :value: "TUESDAY"

   .. py:attribute:: WEDNESDAY
      :value: "WEDNESDAY"

.. autoclass:: ClusterAutoRestartMessageMaintenanceWindowWeekDayBasedSchedule
   :members:
   :undoc-members:

.. py:class:: ClusterAutoRestartMessageMaintenanceWindowWeekDayFrequency

   .. py:attribute:: EVERY_WEEK
      :value: "EVERY_WEEK"

   .. py:attribute:: FIRST_AND_THIRD_OF_MONTH
      :value: "FIRST_AND_THIRD_OF_MONTH"

   .. py:attribute:: FIRST_OF_MONTH
      :value: "FIRST_OF_MONTH"

   .. py:attribute:: FOURTH_OF_MONTH
      :value: "FOURTH_OF_MONTH"

   .. py:attribute:: SECOND_AND_FOURTH_OF_MONTH
      :value: "SECOND_AND_FOURTH_OF_MONTH"

   .. py:attribute:: SECOND_OF_MONTH
      :value: "SECOND_OF_MONTH"

   .. py:attribute:: THIRD_OF_MONTH
      :value: "THIRD_OF_MONTH"

.. autoclass:: ClusterAutoRestartMessageMaintenanceWindowWindowStartTime
   :members:
   :undoc-members:

.. autoclass:: IntegerMessage
   :members:
   :undoc-members:

.. autoclass:: ListAccountSettingsMetadataResponse
   :members:
   :undoc-members:

.. autoclass:: ListAccountUserPreferencesMetadataResponse
   :members:
   :undoc-members:

.. autoclass:: ListWorkspaceSettingsMetadataResponse
   :members:
   :undoc-members:

.. autoclass:: PersonalComputeMessage
   :members:
   :undoc-members:

.. py:class:: PersonalComputeMessagePersonalComputeMessageEnum

   ON: Grants all users in all workspaces access to the Personal Compute default policy, allowing all users to create single-machine compute resources. DELEGATE: Moves access control for the Personal Compute default policy to individual workspaces and requires a workspace’s users or groups to be added to the ACLs of that workspace’s Personal Compute default policy before they will be able to create compute resources through that policy.

   .. py:attribute:: DELEGATE
      :value: "DELEGATE"

   .. py:attribute:: ON
      :value: "ON"

.. autoclass:: RestrictWorkspaceAdminsMessage
   :members:
   :undoc-members:

.. py:class:: RestrictWorkspaceAdminsMessageStatus

   .. py:attribute:: ALLOW_ALL
      :value: "ALLOW_ALL"

   .. py:attribute:: RESTRICT_TOKENS_AND_JOB_RUN_AS
      :value: "RESTRICT_TOKENS_AND_JOB_RUN_AS"

.. autoclass:: Setting
   :members:
   :undoc-members:

.. autoclass:: SettingsMetadata
   :members:
   :undoc-members:

.. autoclass:: StringMessage
   :members:
   :undoc-members:

.. autoclass:: UserPreference
   :members:
   :undoc-members:
