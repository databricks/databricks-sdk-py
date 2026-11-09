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

.. autoclass:: AllowedAppsUserApiScopesMessage
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

.. autoclass:: CollaborationPlatformConnectivityMessage
   :members:
   :undoc-members:

.. py:class:: CollaborationPlatformConnectivityMessageConnectivity

   .. py:attribute:: ALLOW_ALL
      :value: "ALLOW_ALL"

   .. py:attribute:: ALLOW_SLACK
      :value: "ALLOW_SLACK"

   .. py:attribute:: ALLOW_TEAMS
      :value: "ALLOW_TEAMS"

   .. py:attribute:: DENY_ALL
      :value: "DENY_ALL"

.. autoclass:: DashboardTheme
   :members:
   :undoc-members:

.. py:class:: DashboardThemeAlignment

   Horizontal alignment options for widget titles and descriptions.

   .. py:attribute:: CENTER
      :value: "CENTER"

   .. py:attribute:: LEFT
      :value: "LEFT"

   .. py:attribute:: RIGHT
      :value: "RIGHT"

.. autoclass:: DashboardThemeContinuousGradient
   :members:
   :undoc-members:

.. autoclass:: DashboardThemeContinuousGradientCustomDivergingRamp
   :members:
   :undoc-members:

.. autoclass:: DashboardThemeContinuousGradientCustomSequentialRamp
   :members:
   :undoc-members:

.. autoclass:: DashboardThemeContinuousGradientGradientValue
   :members:
   :undoc-members:

.. autoclass:: DashboardThemeDashboardThemeColor
   :members:
   :undoc-members:

.. autoclass:: DashboardThemeFontConfig
   :members:
   :undoc-members:

.. autoclass:: DashboardThemeFontSettings
   :members:
   :undoc-members:

.. py:class:: DashboardThemeFontStyle

   Defines the font style (slant) applied to rendered text.

   .. py:attribute:: FONT_STYLE_ITALIC
      :value: "FONT_STYLE_ITALIC"

   .. py:attribute:: FONT_STYLE_NORMAL
      :value: "FONT_STYLE_NORMAL"

.. autoclass:: DashboardThemeSentimentColors
   :members:
   :undoc-members:

.. py:class:: DashboardThemeTextCase

   Defines the text case transformation applied to rendered text.

   .. py:attribute:: TEXT_CASE_CAPITALIZE
      :value: "TEXT_CASE_CAPITALIZE"

   .. py:attribute:: TEXT_CASE_LOWERCASE
      :value: "TEXT_CASE_LOWERCASE"

   .. py:attribute:: TEXT_CASE_UPPERCASE
      :value: "TEXT_CASE_UPPERCASE"

.. py:class:: DashboardThemeTextDecoration

   Defines the decoration line applied to rendered text.

   .. py:attribute:: TEXT_DECORATION_NONE
      :value: "TEXT_DECORATION_NONE"

   .. py:attribute:: TEXT_DECORATION_UNDERLINE
      :value: "TEXT_DECORATION_UNDERLINE"

.. py:class:: DashboardThemeVerticalAlign

   Vertical alignment options for text box content.

   .. py:attribute:: VERTICAL_ALIGN_BOTTOM
      :value: "VERTICAL_ALIGN_BOTTOM"

   .. py:attribute:: VERTICAL_ALIGN_CENTER
      :value: "VERTICAL_ALIGN_CENTER"

   .. py:attribute:: VERTICAL_ALIGN_TOP
      :value: "VERTICAL_ALIGN_TOP"

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

.. autoclass:: OperationalEmailCustomRecipientMessage
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

.. py:class:: PreviewPhase

   Preview phase for settings that are feature previews. For settings that are not feature previews, the preview_phase field is left unset. Mirrors only the customer-facing phases surfaced in the UI; internal-only phases (DISABLED, DEV, UNDER_MIGRATION, LAUNCHED, etc.) are not exposed here.

   .. py:attribute:: BETA
      :value: "BETA"

   .. py:attribute:: GA
      :value: "GA"

   .. py:attribute:: GA_SOON
      :value: "GA_SOON"

   .. py:attribute:: PRIVATE_PREVIEW
      :value: "PRIVATE_PREVIEW"

   .. py:attribute:: PUBLIC_PREVIEW
      :value: "PUBLIC_PREVIEW"

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

.. autoclass:: WorkspaceLabelMessage
   :members:
   :undoc-members:
