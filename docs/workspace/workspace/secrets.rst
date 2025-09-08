``w.secrets``: Secret
=====================
.. currentmodule:: databricks.sdk.service.workspace

.. py:class:: SecretsAPI

    The Secrets API allows you to manage secrets, secret scopes, and access permissions.
    
    Sometimes accessing data requires that you authenticate to external data sources through JDBC. Instead of
    directly entering your credentials into a notebook, use Databricks secrets to store your credentials and
    reference them in notebooks and jobs.
    
    Administrators, secret creators, and users granted permission can read Databricks secrets. While
    Databricks makes an effort to redact secret values that might be displayed in notebooks, it is not
    possible to prevent such users from reading secrets.

    .. py:method:: create_scope(scope: str [, backend_azure_keyvault: Optional[AzureKeyVaultSecretScopeMetadata], initial_manage_principal: Optional[str], scope_backend_type: Optional[ScopeBackendType]])


        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            key_name = f"sdk-{time.time_ns()}"
            
            scope_name = f"sdk-{time.time_ns()}"
            
            w.secrets.create_scope(scope=scope_name)
            
            # cleanup
            w.secrets.delete_secret(scope=scope_name, key=key_name)
            w.secrets.delete_scope(scope=scope_name)

        Creates a new secret scope.
        
        The scope name must consist of alphanumeric characters, dashes, underscores, and periods, and may not
        exceed 128 characters.
        
        Example request:
        
        .. code::
        
        { "scope": "my-simple-databricks-scope", "initial_manage_principal": "users" "scope_backend_type":
        "databricks|azure_keyvault", # below is only required if scope type is azure_keyvault
        "backend_azure_keyvault": { "resource_id":
        "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/xxxx/providers/Microsoft.KeyVault/vaults/xxxx",
        "tenant_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx", "dns_name": "https://xxxx.vault.azure.net/", } }
        
        If ``initial_manage_principal`` is specified, the initial ACL applied to the scope is applied to the
        supplied principal (user or group) with ``MANAGE`` permissions. The only supported principal for this
        option is the group ``users``, which contains all users in the workspace. If
        ``initial_manage_principal`` is not specified, the initial ACL with ``MANAGE`` permission applied to
        the scope is assigned to the API request issuer's user identity.
        
        If ``scope_backend_type`` is ``azure_keyvault``, a secret scope is created with secrets from a given
        Azure KeyVault. The caller must provide the keyvault_resource_id and the tenant_id for the key vault.
        If ``scope_backend_type`` is ``databricks`` or is unspecified, an empty secret scope is created and
        stored in Databricks's own storage.
        
        Throws ``RESOURCE_ALREADY_EXISTS`` if a scope with the given name already exists. Throws
        ``RESOURCE_LIMIT_EXCEEDED`` if maximum number of scopes in the workspace is exceeded. Throws
        ``INVALID_PARAMETER_VALUE`` if the scope name is invalid. Throws ``BAD_REQUEST`` if request violated
        constraints. Throws ``CUSTOMER_UNAUTHORIZED`` if normal user attempts to create a scope with name
        reserved for databricks internal usage. Throws ``UNAUTHENTICATED`` if unable to verify user access
        permission on Azure KeyVault
        
        :param scope: str
          Scope name requested by the user. Scope names are unique.
        :param backend_azure_keyvault: :class:`AzureKeyVaultSecretScopeMetadata` (optional)
          The metadata for the secret scope if the type is ``AZURE_KEYVAULT``
        :param initial_manage_principal: str (optional)
          The principal that is initially granted ``MANAGE`` permission to the created scope.
        :param scope_backend_type: :class:`ScopeBackendType` (optional)
          The backend type the scope will be created with. If not specified, will default to ``DATABRICKS``
        
        
        

    .. py:method:: delete_acl(scope: str, principal: str)

        Deletes the given ACL on the given scope.
        
        Users must have the ``MANAGE`` permission to invoke this API.
        
        Example request:
        
        .. code::
        
        { "scope": "my-secret-scope", "principal": "data-scientists" }
        
        Throws ``RESOURCE_DOES_NOT_EXIST`` if no such secret scope, principal, or ACL exists. Throws
        ``PERMISSION_DENIED`` if the user does not have permission to make this API call. Throws
        ``INVALID_PARAMETER_VALUE`` if the permission or principal is invalid.
        
        :param scope: str
          The name of the scope to remove permissions from.
        :param principal: str
          The principal to remove an existing ACL from.
        
        
        

    .. py:method:: delete_scope(scope: str)

        Deletes a secret scope.
        
        Example request:
        
        .. code::
        
        { "scope": "my-secret-scope" }
        
        Throws ``RESOURCE_DOES_NOT_EXIST`` if the scope does not exist. Throws ``PERMISSION_DENIED`` if the
        user does not have permission to make this API call. Throws ``BAD_REQUEST`` if system user attempts to
        delete internal secret scope.
        
        :param scope: str
          Name of the scope to delete.
        
        
        

    .. py:method:: delete_secret(scope: str, key: str)

        Deletes the secret stored in this secret scope. You must have ``WRITE`` or ``MANAGE`` permission on
        the Secret Scope.
        
        Example request:
        
        .. code::
        
        { "scope": "my-secret-scope", "key": "my-secret-key" }
        
        Throws ``RESOURCE_DOES_NOT_EXIST`` if no such secret scope or secret exists. Throws
        ``PERMISSION_DENIED`` if the user does not have permission to make this API call. Throws
        ``BAD_REQUEST`` if system user attempts to delete an internal secret, or request is made against Azure
        KeyVault backed scope.
        
        :param scope: str
          The name of the scope that contains the secret to delete.
        :param key: str
          Name of the secret to delete.
        
        
        

    .. py:method:: get_acl(scope: str, principal: str) -> AclItem

        Describes the details about the given ACL, such as the group and permission.
        
        Users must have the ``MANAGE`` permission to invoke this API.
        
        Example response:
        
        .. code::
        
        { "principal": "data-scientists", "permission": "READ" }
        
        Throws ``RESOURCE_DOES_NOT_EXIST`` if no such secret scope exists. Throws ``PERMISSION_DENIED`` if the
        user does not have permission to make this API call. Throws ``INVALID_PARAMETER_VALUE`` if the
        permission or principal is invalid.
        
        :param scope: str
          The name of the scope to fetch ACL information from.
        :param principal: str
          The principal to fetch ACL information for.
        
        :returns: :class:`AclItem`
        

    .. py:method:: get_secret(scope: str, key: str) -> GetSecretResponse

        Gets a secret for a given key and scope. This API can only be called from the DBUtils interface. Users
        need the READ permission to make this call.
        
        Example response:
        
        .. code::
        
        { "key": "my-string-key", "value": <bytes of the secret value> }
        
        Note that the secret value returned is in bytes. The interpretation of the bytes is determined by the
        caller in DBUtils and the type the data is decoded into.
        
        Throws ``RESOURCE_DOES_NOT_EXIST`` if no such secret or secret scope exists. Throws
        ``PERMISSION_DENIED`` if the user does not have permission to make this API call.
        
        Note: This is explicitly an undocumented API. It also doesn't need to be supported for the /preview
        prefix, because it's not a customer-facing API (i.e. only used for DBUtils SecretUtils to fetch
        secrets).
        
        Throws ``RESOURCE_DOES_NOT_EXIST`` if no such secret scope or secret exists. Throws ``BAD_REQUEST`` if
        normal user calls get secret outside of a notebook. AKV specific errors: Throws
        ``INVALID_PARAMETER_VALUE`` if secret name is not alphanumeric or too long. Throws
        ``PERMISSION_DENIED`` if secret manager cannot access AKV with 403 error Throws ``MALFORMED_REQUEST``
        if secret manager cannot access AKV with any other 4xx error
        
        :param scope: str
          The name of the scope that contains the secret.
        :param key: str
          Name of the secret to fetch value information.
        
        :returns: :class:`GetSecretResponse`
        

    .. py:method:: list_acls(scope: str) -> Iterator[AclItem]


        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            key_name = f"sdk-{time.time_ns()}"
            
            scope_name = f"sdk-{time.time_ns()}"
            
            w.secrets.create_scope(scope=scope_name)
            
            acls = w.secrets.list_acls(scope=scope_name)
            
            # cleanup
            w.secrets.delete_secret(scope=scope_name, key=key_name)
            w.secrets.delete_scope(scope=scope_name)

        Lists the ACLs set on the given scope.
        
        Users must have the ``MANAGE`` permission to invoke this API.
        
        Example response:
        
        .. code::
        
        { "acls": [{ "principal": "admins", "permission": "MANAGE" },{ "principal": "data-scientists",
        "permission": "READ" }] }
        
        Throws ``RESOURCE_DOES_NOT_EXIST`` if no such secret scope exists. Throws ``PERMISSION_DENIED`` if the
        user does not have permission to make this API call.
        
        :param scope: str
          The name of the scope to fetch ACL information from.
        
        :returns: Iterator over :class:`AclItem`
        

    .. py:method:: list_scopes() -> Iterator[SecretScope]


        Usage:

        .. code-block::

            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            scopes = w.secrets.list_scopes()

        Lists all secret scopes available in the workspace.
        
        Example response:
        
        .. code::
        
        { "scopes": [{ "name": "my-databricks-scope", "backend_type": "DATABRICKS" },{ "name": "mount-points",
        "backend_type": "DATABRICKS" }] }
        
        Throws ``PERMISSION_DENIED`` if the user does not have permission to make this API call.
        
        
        :returns: Iterator over :class:`SecretScope`
        

    .. py:method:: list_secrets(scope: str) -> Iterator[SecretMetadata]


        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            key_name = f"sdk-{time.time_ns()}"
            
            scope_name = f"sdk-{time.time_ns()}"
            
            w.secrets.create_scope(scope=scope_name)
            
            scrts = w.secrets.list_secrets(scope=scope_name)
            
            # cleanup
            w.secrets.delete_secret(scope=scope_name, key=key_name)
            w.secrets.delete_scope(scope=scope_name)

        Lists the secret keys that are stored at this scope. This is a metadata-only operation; secret data
        cannot be retrieved using this API. Users need the READ permission to make this call.
        
        Example response:
        
        .. code::
        
        { "secrets": [ { "key": "my-string-key"", "last_updated_timestamp": "1520467595000" }, { "key":
        "my-byte-key", "last_updated_timestamp": "1520467595000" }, ] }
        
        The lastUpdatedTimestamp returned is in milliseconds since epoch.
        
        Throws ``RESOURCE_DOES_NOT_EXIST`` if no such secret scope exists. Throws ``PERMISSION_DENIED`` if the
        user does not have permission to make this API call.
        
        :param scope: str
          The name of the scope to list secrets within.
        
        :returns: Iterator over :class:`SecretMetadata`
        

    .. py:method:: put_acl(scope: str, principal: str, permission: AclPermission)


        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import workspace
            
            w = WorkspaceClient()
            
            key_name = f"sdk-{time.time_ns()}"
            
            group = w.groups.create(display_name=f"sdk-{time.time_ns()}")
            
            scope_name = f"sdk-{time.time_ns()}"
            
            w.secrets.create_scope(scope=scope_name)
            
            w.secrets.put_acl(
                scope=scope_name,
                permission=workspace.AclPermission.MANAGE,
                principal=group.display_name,
            )
            
            # cleanup
            w.groups.delete(id=group.id)
            w.secrets.delete_secret(scope=scope_name, key=key_name)
            w.secrets.delete_scope(scope=scope_name)

        Creates or overwrites the ACL associated with the given principal (user or group) on the specified
        scope point. In general, a user or group will use the most powerful permission available to them, and
        permissions are ordered as follows:
        
        * ``MANAGE`` - Allowed to change ACLs, and read and write to this secret scope. * ``WRITE`` - Allowed
        to read and write to this secret scope. * ``READ`` - Allowed to read this secret scope and list what
        secrets are available.
        
        Note that in general, secret values can only be read from within a command on a cluster (for example,
        through a notebook). There is no API to read the actual secret value material outside of a cluster.
        However, the user's permission will be applied based on who is executing the command, and they must
        have at least READ permission.
        
        Users must have the ``MANAGE`` permission to invoke this API.
        
        Example request:
        
        .. code::
        
        { "scope": "my-secret-scope", "principal": "data-scientists", "permission": "READ" }
        
        The principal is a user or group name corresponding to an existing Databricks principal to be granted
        or revoked access.
        
        Throws ``RESOURCE_DOES_NOT_EXIST`` if no such secret scope exists. Throws ``RESOURCE_ALREADY_EXISTS``
        if a permission for the principal already exists. Throws ``INVALID_PARAMETER_VALUE`` if the permission
        or principal is invalid. Throws ``PERMISSION_DENIED`` if the user does not have permission to make
        this API call.
        
        :param scope: str
          The name of the scope to apply permissions to.
        :param principal: str
          The principal in which the permission is applied.
        :param permission: :class:`AclPermission`
          The permission level applied to the principal.
        
        
        

    .. py:method:: put_secret(scope: str, key: str [, bytes_value: Optional[str], string_value: Optional[str]])


        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            key_name = f"sdk-{time.time_ns()}"
            
            scope_name = f"sdk-{time.time_ns()}"
            
            w.secrets.create_scope(scope=scope_name)
            
            w.secrets.put_secret(scope=scope_name, key=key_name, string_value=f"sdk-{time.time_ns()}")
            
            # cleanup
            w.secrets.delete_secret(scope=scope_name, key=key_name)
            w.secrets.delete_scope(scope=scope_name)

        Inserts a secret under the provided scope with the given name. If a secret already exists with the
        same name, this command overwrites the existing secret's value. The server encrypts the secret using
        the secret scope's encryption settings before storing it. You must have ``WRITE`` or ``MANAGE``
        permission on the secret scope.
        
        The secret key must consist of alphanumeric characters, dashes, underscores, and periods, and cannot
        exceed 128 characters. The maximum allowed secret value size is 128 KB. The maximum number of secrets
        in a given scope is 1000.
        
        Example request:
        
        .. code::
        
        { "scope": "my-databricks-scope", "key": "my-string-key", "string_value": "foobar" }
        
        The input fields "string_value" or "bytes_value" specify the type of the secret, which will determine
        the value returned when the secret value is requested. Exactly one must be specified.
        
        Throws ``RESOURCE_DOES_NOT_EXIST`` if no such secret scope exists. Throws ``RESOURCE_LIMIT_EXCEEDED``
        if maximum number of secrets in scope is exceeded. Throws ``INVALID_PARAMETER_VALUE`` if the request
        parameters are invalid. Throws ``PERMISSION_DENIED`` if the user does not have permission to make this
        API call. Throws ``MALFORMED_REQUEST`` if request is incorrectly formatted or conflicting. Throws
        ``BAD_REQUEST`` if request is made against Azure KeyVault backed scope.
        
        :param scope: str
          The name of the scope to which the secret will be associated with.
        :param key: str
          A unique name to identify the secret.
        :param bytes_value: str (optional)
          If specified, value will be stored as bytes.
        :param string_value: str (optional)
          If specified, note that the value will be stored in UTF-8 (MB4) form.
        
        
        