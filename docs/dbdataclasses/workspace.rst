Workspace
=========

These dataclasses are used in the SDK to represent API requests and responses for services in the ``databricks.sdk.service.workspace`` module.

.. py:currentmodule:: databricks.sdk.service.workspace
.. autoclass:: AclItem
   :members:
   :undoc-members:

.. py:class:: AclPermission

   The ACL permission levels for Secret ACLs applied to secret scopes.

   .. py:attribute:: MANAGE
      :value: "MANAGE"

   .. py:attribute:: READ
      :value: "READ"

   .. py:attribute:: WRITE
      :value: "WRITE"

.. autoclass:: AzureKeyVaultSecretScopeMetadata
   :members:
   :undoc-members:

.. autoclass:: CreateCredentialsResponse
   :members:
   :undoc-members:

.. autoclass:: CreateRepoResponse
   :members:
   :undoc-members:

.. autoclass:: CreateScopeResponse
   :members:
   :undoc-members:

.. autoclass:: CredentialInfo
   :members:
   :undoc-members:

.. autoclass:: DeleteAclResponse
   :members:
   :undoc-members:

.. autoclass:: DeleteCredentialsResponse
   :members:
   :undoc-members:

.. autoclass:: DeleteRepoResponse
   :members:
   :undoc-members:

.. autoclass:: DeleteResponse
   :members:
   :undoc-members:

.. autoclass:: DeleteScopeResponse
   :members:
   :undoc-members:

.. autoclass:: DeleteSecretResponse
   :members:
   :undoc-members:

.. py:class:: ExportFormat

   The format for workspace import and export.

   .. py:attribute:: AUTO
      :value: "AUTO"

   .. py:attribute:: DBC
      :value: "DBC"

   .. py:attribute:: HTML
      :value: "HTML"

   .. py:attribute:: JUPYTER
      :value: "JUPYTER"

   .. py:attribute:: RAW
      :value: "RAW"

   .. py:attribute:: R_MARKDOWN
      :value: "R_MARKDOWN"

   .. py:attribute:: SOURCE
      :value: "SOURCE"

.. autoclass:: ExportResponse
   :members:
   :undoc-members:

.. autoclass:: GetCredentialsResponse
   :members:
   :undoc-members:

.. autoclass:: GetRepoPermissionLevelsResponse
   :members:
   :undoc-members:

.. autoclass:: GetRepoResponse
   :members:
   :undoc-members:

.. autoclass:: GetSecretResponse
   :members:
   :undoc-members:

.. autoclass:: GetWorkspaceObjectPermissionLevelsResponse
   :members:
   :undoc-members:

.. py:class:: ImportFormat

   The format for workspace import and export.

   .. py:attribute:: AUTO
      :value: "AUTO"

   .. py:attribute:: DBC
      :value: "DBC"

   .. py:attribute:: HTML
      :value: "HTML"

   .. py:attribute:: JUPYTER
      :value: "JUPYTER"

   .. py:attribute:: RAW
      :value: "RAW"

   .. py:attribute:: R_MARKDOWN
      :value: "R_MARKDOWN"

   .. py:attribute:: SOURCE
      :value: "SOURCE"

.. autoclass:: ImportResponse
   :members:
   :undoc-members:

.. py:class:: Language

   The language of notebook.

   .. py:attribute:: PYTHON
      :value: "PYTHON"

   .. py:attribute:: R
      :value: "R"

   .. py:attribute:: SCALA
      :value: "SCALA"

   .. py:attribute:: SQL
      :value: "SQL"

.. autoclass:: ListAclsResponse
   :members:
   :undoc-members:

.. autoclass:: ListCredentialsResponse
   :members:
   :undoc-members:

.. autoclass:: ListReposResponse
   :members:
   :undoc-members:

.. autoclass:: ListResponse
   :members:
   :undoc-members:

.. autoclass:: ListScopesResponse
   :members:
   :undoc-members:

.. autoclass:: ListSecretsResponse
   :members:
   :undoc-members:

.. autoclass:: MkdirsResponse
   :members:
   :undoc-members:

.. autoclass:: ObjectInfo
   :members:
   :undoc-members:

.. py:class:: ObjectType

   The type of the object in workspace.

   .. py:attribute:: DASHBOARD
      :value: "DASHBOARD"

   .. py:attribute:: DIRECTORY
      :value: "DIRECTORY"

   .. py:attribute:: FILE
      :value: "FILE"

   .. py:attribute:: LIBRARY
      :value: "LIBRARY"

   .. py:attribute:: NOTEBOOK
      :value: "NOTEBOOK"

   .. py:attribute:: REPO
      :value: "REPO"

.. autoclass:: PutAclResponse
   :members:
   :undoc-members:

.. autoclass:: PutSecretResponse
   :members:
   :undoc-members:

.. autoclass:: RepoAccessControlRequest
   :members:
   :undoc-members:

.. autoclass:: RepoAccessControlResponse
   :members:
   :undoc-members:

.. autoclass:: RepoInfo
   :members:
   :undoc-members:

.. autoclass:: RepoPermission
   :members:
   :undoc-members:

.. py:class:: RepoPermissionLevel

   Permission level

   .. py:attribute:: CAN_EDIT
      :value: "CAN_EDIT"

   .. py:attribute:: CAN_MANAGE
      :value: "CAN_MANAGE"

   .. py:attribute:: CAN_READ
      :value: "CAN_READ"

   .. py:attribute:: CAN_RUN
      :value: "CAN_RUN"

.. autoclass:: RepoPermissions
   :members:
   :undoc-members:

.. autoclass:: RepoPermissionsDescription
   :members:
   :undoc-members:

.. py:class:: ScopeBackendType

   The types of secret scope backends in the Secret Manager. Azure KeyVault backed secret scopes will be supported in a later release.

   .. py:attribute:: AZURE_KEYVAULT
      :value: "AZURE_KEYVAULT"

   .. py:attribute:: DATABRICKS
      :value: "DATABRICKS"

.. autoclass:: SecretMetadata
   :members:
   :undoc-members:

.. autoclass:: SecretScope
   :members:
   :undoc-members:

.. autoclass:: SparseCheckout
   :members:
   :undoc-members:

.. autoclass:: SparseCheckoutUpdate
   :members:
   :undoc-members:

.. autoclass:: Token
   :members:
   :undoc-members:

.. autoclass:: UpdateCredentialsResponse
   :members:
   :undoc-members:

.. autoclass:: UpdateRepoResponse
   :members:
   :undoc-members:

.. autoclass:: WorkspaceObjectAccessControlRequest
   :members:
   :undoc-members:

.. autoclass:: WorkspaceObjectAccessControlResponse
   :members:
   :undoc-members:

.. autoclass:: WorkspaceObjectPermission
   :members:
   :undoc-members:

.. py:class:: WorkspaceObjectPermissionLevel

   Permission level

   .. py:attribute:: CAN_EDIT
      :value: "CAN_EDIT"

   .. py:attribute:: CAN_MANAGE
      :value: "CAN_MANAGE"

   .. py:attribute:: CAN_READ
      :value: "CAN_READ"

   .. py:attribute:: CAN_RUN
      :value: "CAN_RUN"

.. autoclass:: WorkspaceObjectPermissions
   :members:
   :undoc-members:

.. autoclass:: WorkspaceObjectPermissionsDescription
   :members:
   :undoc-members:
