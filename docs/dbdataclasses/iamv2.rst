Identity and Access Management
==============================

These dataclasses are used in the SDK to represent API requests and responses for services in the ``databricks.sdk.service.iamv2`` module.

.. py:currentmodule:: databricks.sdk.service.iamv2
.. autoclass:: Group
   :members:
   :undoc-members:

.. py:class:: PrincipalType

   The type of the principal (user/sp/group).

   .. py:attribute:: GROUP
      :value: "GROUP"

   .. py:attribute:: SERVICE_PRINCIPAL
      :value: "SERVICE_PRINCIPAL"

   .. py:attribute:: USER
      :value: "USER"

.. autoclass:: ResolveGroupResponse
   :members:
   :undoc-members:

.. autoclass:: ResolveServicePrincipalResponse
   :members:
   :undoc-members:

.. autoclass:: ResolveUserResponse
   :members:
   :undoc-members:

.. autoclass:: ServicePrincipal
   :members:
   :undoc-members:

.. py:class:: State

   The activity status of a user or service principal in a Databricks account or workspace.

   .. py:attribute:: ACTIVE
      :value: "ACTIVE"

   .. py:attribute:: INACTIVE
      :value: "INACTIVE"

.. autoclass:: User
   :members:
   :undoc-members:

.. autoclass:: UserName
   :members:
   :undoc-members:

.. autoclass:: WorkspaceAccessDetail
   :members:
   :undoc-members:

.. py:class:: WorkspaceAccessDetailAccessType

   The type of access the principal has to the workspace.

   .. py:attribute:: DIRECT
      :value: "DIRECT"

   .. py:attribute:: INDIRECT
      :value: "INDIRECT"

.. py:class:: WorkspaceAccessDetailView

   Controls what fields are returned in the GetWorkspaceAccessDetail response.

   .. py:attribute:: BASIC
      :value: "BASIC"

   .. py:attribute:: FULL
      :value: "FULL"

.. py:class:: WorkspacePermission

   The type of permission a principal has to a workspace (admin/user).

   .. py:attribute:: ADMIN_PERMISSION
      :value: "ADMIN_PERMISSION"

   .. py:attribute:: USER_PERMISSION
      :value: "USER_PERMISSION"
