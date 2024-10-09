Workspace
=========

These dataclasses are used in the SDK to represent API requests and responses for services in the ``databricks.sdk.service.workspace`` module.

.. py:currentmodule:: databricks.sdk.service.workspace
.. autoclass:: AclItem
   :members:
   :undoc-members:

.. py:class:: AclPermission

   .. py:attribute:: MANAGE
      :value: "MANAGE"

   .. py:attribute:: READ
      :value: "READ"

   .. py:attribute:: WRITE
      :value: "WRITE"

.. autoclass:: AzureKeyVaultSecretScopeMetadata
   :members:
   :undoc-members:

.. autoclass:: CreateCredentialsRequest
   :members:
   :undoc-members:

.. autoclass:: CreateCredentialsResponse
   :members:
   :undoc-members:

.. autoclass:: CreateRepoRequest
   :members:
   :undoc-members:

.. autoclass:: CreateRepoResponse
   :members:
   :undoc-members:

.. autoclass:: CreateScope
   :members:
   :undoc-members:

.. autoclass:: CreateScopeResponse
   :members:
   :undoc-members:

.. autoclass:: CredentialInfo
   :members:
   :undoc-members:

.. autoclass:: Delete
   :members:
   :undoc-members:

.. autoclass:: DeleteAcl
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

.. autoclass:: DeleteScope
   :members:
   :undoc-members:

.. autoclass:: DeleteScopeResponse
   :members:
   :undoc-members:

.. autoclass:: DeleteSecret
   :members:
   :undoc-members:

.. autoclass:: DeleteSecretResponse
   :members:
   :undoc-members:

.. py:class:: ExportFormat

   .. py:attribute:: AUTO
      :value: "AUTO"

   .. py:attribute:: DBC
      :value: "DBC"

   .. py:attribute:: HTML
      :value: "HTML"

   .. py:attribute:: JUPYTER
      :value: "JUPYTER"

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

.. autoclass:: Import
   :members:
   :undoc-members:

.. py:class:: ImportFormat

   This specifies the format of the file to be imported.
   The value is case sensitive.
   - `AUTO`: The item is imported depending on an analysis of the item's extension and the header content provided in the request. If the item is imported as a notebook, then the item's extension is automatically removed. - `SOURCE`: The notebook or directory is imported as source code. - `HTML`: The notebook is imported as an HTML file. - `JUPYTER`: The notebook is imported as a Jupyter/IPython Notebook file. - `DBC`: The notebook is imported in Databricks archive format. Required for directories. - `R_MARKDOWN`: The notebook is imported from R Markdown format.

   .. py:attribute:: AUTO
      :value: "AUTO"

   .. py:attribute:: DBC
      :value: "DBC"

   .. py:attribute:: HTML
      :value: "HTML"

   .. py:attribute:: JUPYTER
      :value: "JUPYTER"

   .. py:attribute:: R_MARKDOWN
      :value: "R_MARKDOWN"

   .. py:attribute:: SOURCE
      :value: "SOURCE"

.. autoclass:: ImportResponse
   :members:
   :undoc-members:

.. py:class:: Language

   The language of the object. This value is set only if the object type is `NOTEBOOK`.

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

.. autoclass:: Mkdirs
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
   - `NOTEBOOK`: document that contains runnable code, visualizations, and explanatory text. - `DIRECTORY`: directory - `LIBRARY`: library - `FILE`: file - `REPO`: repository - `DASHBOARD`: Lakeview dashboard

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

.. autoclass:: PutAcl
   :members:
   :undoc-members:

.. autoclass:: PutAclResponse
   :members:
   :undoc-members:

.. autoclass:: PutSecret
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

.. autoclass:: RepoPermissionsRequest
   :members:
   :undoc-members:

.. py:class:: ScopeBackendType

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

.. autoclass:: UpdateCredentialsRequest
   :members:
   :undoc-members:

.. autoclass:: UpdateCredentialsResponse
   :members:
   :undoc-members:

.. autoclass:: UpdateRepoRequest
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

.. autoclass:: WorkspaceObjectPermissionsRequest
   :members:
   :undoc-members:
