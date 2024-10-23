Identity and Access Management
==============================

These dataclasses are used in the SDK to represent API requests and responses for services in the ``databricks.sdk.service.iam`` module.

.. py:currentmodule:: databricks.sdk.service.iam
.. autoclass:: AccessControlRequest
   :members:
   :undoc-members:

.. autoclass:: AccessControlResponse
   :members:
   :undoc-members:

.. autoclass:: ComplexValue
   :members:
   :undoc-members:

.. autoclass:: DeleteResponse
   :members:
   :undoc-members:

.. autoclass:: DeleteWorkspacePermissionAssignmentResponse
   :members:
   :undoc-members:

.. autoclass:: GetAssignableRolesForResourceResponse
   :members:
   :undoc-members:

.. autoclass:: GetPasswordPermissionLevelsResponse
   :members:
   :undoc-members:

.. autoclass:: GetPermissionLevelsResponse
   :members:
   :undoc-members:

.. py:class:: GetSortOrder

   .. py:attribute:: ASCENDING
      :value: "ASCENDING"

   .. py:attribute:: DESCENDING
      :value: "DESCENDING"

.. autoclass:: GrantRule
   :members:
   :undoc-members:

.. autoclass:: Group
   :members:
   :undoc-members:

.. py:class:: GroupSchema

   .. py:attribute:: URN_IETF_PARAMS_SCIM_SCHEMAS_CORE_2_0_GROUP
      :value: "URN_IETF_PARAMS_SCIM_SCHEMAS_CORE_2_0_GROUP"

.. autoclass:: ListGroupsResponse
   :members:
   :undoc-members:

.. py:class:: ListResponseSchema

   .. py:attribute:: URN_IETF_PARAMS_SCIM_API_MESSAGES_2_0_LIST_RESPONSE
      :value: "URN_IETF_PARAMS_SCIM_API_MESSAGES_2_0_LIST_RESPONSE"

.. autoclass:: ListServicePrincipalResponse
   :members:
   :undoc-members:

.. py:class:: ListSortOrder

   .. py:attribute:: ASCENDING
      :value: "ASCENDING"

   .. py:attribute:: DESCENDING
      :value: "DESCENDING"

.. autoclass:: ListUsersResponse
   :members:
   :undoc-members:

.. autoclass:: MigratePermissionsRequest
   :members:
   :undoc-members:

.. autoclass:: MigratePermissionsResponse
   :members:
   :undoc-members:

.. autoclass:: Name
   :members:
   :undoc-members:

.. autoclass:: ObjectPermissions
   :members:
   :undoc-members:

.. autoclass:: PartialUpdate
   :members:
   :undoc-members:

.. autoclass:: PasswordAccessControlRequest
   :members:
   :undoc-members:

.. autoclass:: PasswordAccessControlResponse
   :members:
   :undoc-members:

.. autoclass:: PasswordPermission
   :members:
   :undoc-members:

.. py:class:: PasswordPermissionLevel

   Permission level

   .. py:attribute:: CAN_USE
      :value: "CAN_USE"

.. autoclass:: PasswordPermissions
   :members:
   :undoc-members:

.. autoclass:: PasswordPermissionsDescription
   :members:
   :undoc-members:

.. autoclass:: PasswordPermissionsRequest
   :members:
   :undoc-members:

.. autoclass:: Patch
   :members:
   :undoc-members:

.. py:class:: PatchOp

   Type of patch operation.

   .. py:attribute:: ADD
      :value: "ADD"

   .. py:attribute:: REMOVE
      :value: "REMOVE"

   .. py:attribute:: REPLACE
      :value: "REPLACE"

.. autoclass:: PatchResponse
   :members:
   :undoc-members:

.. py:class:: PatchSchema

   .. py:attribute:: URN_IETF_PARAMS_SCIM_API_MESSAGES_2_0_PATCH_OP
      :value: "URN_IETF_PARAMS_SCIM_API_MESSAGES_2_0_PATCH_OP"

.. autoclass:: Permission
   :members:
   :undoc-members:

.. autoclass:: PermissionAssignment
   :members:
   :undoc-members:

.. autoclass:: PermissionAssignments
   :members:
   :undoc-members:

.. py:class:: PermissionLevel

   Permission level

   .. py:attribute:: CAN_ATTACH_TO
      :value: "CAN_ATTACH_TO"

   .. py:attribute:: CAN_BIND
      :value: "CAN_BIND"

   .. py:attribute:: CAN_EDIT
      :value: "CAN_EDIT"

   .. py:attribute:: CAN_EDIT_METADATA
      :value: "CAN_EDIT_METADATA"

   .. py:attribute:: CAN_MANAGE
      :value: "CAN_MANAGE"

   .. py:attribute:: CAN_MANAGE_PRODUCTION_VERSIONS
      :value: "CAN_MANAGE_PRODUCTION_VERSIONS"

   .. py:attribute:: CAN_MANAGE_RUN
      :value: "CAN_MANAGE_RUN"

   .. py:attribute:: CAN_MANAGE_STAGING_VERSIONS
      :value: "CAN_MANAGE_STAGING_VERSIONS"

   .. py:attribute:: CAN_MONITOR
      :value: "CAN_MONITOR"

   .. py:attribute:: CAN_QUERY
      :value: "CAN_QUERY"

   .. py:attribute:: CAN_READ
      :value: "CAN_READ"

   .. py:attribute:: CAN_RESTART
      :value: "CAN_RESTART"

   .. py:attribute:: CAN_RUN
      :value: "CAN_RUN"

   .. py:attribute:: CAN_USE
      :value: "CAN_USE"

   .. py:attribute:: CAN_VIEW
      :value: "CAN_VIEW"

   .. py:attribute:: CAN_VIEW_METADATA
      :value: "CAN_VIEW_METADATA"

   .. py:attribute:: IS_OWNER
      :value: "IS_OWNER"

.. autoclass:: PermissionOutput
   :members:
   :undoc-members:

.. autoclass:: PermissionsDescription
   :members:
   :undoc-members:

.. autoclass:: PermissionsRequest
   :members:
   :undoc-members:

.. autoclass:: PrincipalOutput
   :members:
   :undoc-members:

.. autoclass:: ResourceMeta
   :members:
   :undoc-members:

.. autoclass:: Role
   :members:
   :undoc-members:

.. autoclass:: RuleSetResponse
   :members:
   :undoc-members:

.. autoclass:: RuleSetUpdateRequest
   :members:
   :undoc-members:

.. autoclass:: ServicePrincipal
   :members:
   :undoc-members:

.. py:class:: ServicePrincipalSchema

   .. py:attribute:: URN_IETF_PARAMS_SCIM_SCHEMAS_CORE_2_0_SERVICE_PRINCIPAL
      :value: "URN_IETF_PARAMS_SCIM_SCHEMAS_CORE_2_0_SERVICE_PRINCIPAL"

.. autoclass:: UpdateResponse
   :members:
   :undoc-members:

.. autoclass:: UpdateRuleSetRequest
   :members:
   :undoc-members:

.. autoclass:: UpdateWorkspaceAssignments
   :members:
   :undoc-members:

.. autoclass:: User
   :members:
   :undoc-members:

.. py:class:: UserSchema

   .. py:attribute:: URN_IETF_PARAMS_SCIM_SCHEMAS_CORE_2_0_USER
      :value: "URN_IETF_PARAMS_SCIM_SCHEMAS_CORE_2_0_USER"

   .. py:attribute:: URN_IETF_PARAMS_SCIM_SCHEMAS_EXTENSION_WORKSPACE_2_0_USER
      :value: "URN_IETF_PARAMS_SCIM_SCHEMAS_EXTENSION_WORKSPACE_2_0_USER"

.. py:class:: WorkspacePermission

   .. py:attribute:: ADMIN
      :value: "ADMIN"

   .. py:attribute:: UNKNOWN
      :value: "UNKNOWN"

   .. py:attribute:: USER
      :value: "USER"

.. autoclass:: WorkspacePermissions
   :members:
   :undoc-members:
