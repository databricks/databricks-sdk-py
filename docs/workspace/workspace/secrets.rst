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
            
            key_name = f'sdk-{time.time_ns()}'
            
            scope_name = f'sdk-{time.time_ns()}'
            
            w.secrets.create_scope(scope=scope_name)
            
            # cleanup
            w.secrets.delete_secret(scope=scope_name, key=key_name)
            w.secrets.delete_scope(scope=scope_name)

        Create a new secret scope.
        
        The scope name must consist of alphanumeric characters, dashes, underscores, and periods, and may not
        exceed 128 characters.
        
        :param scope: str
          Scope name requested by the user. Scope names are unique.
        :param backend_azure_keyvault: :class:`AzureKeyVaultSecretScopeMetadata` (optional)
          The metadata for the secret scope if the type is `AZURE_KEYVAULT`
        :param initial_manage_principal: str (optional)
          The principal that is initially granted `MANAGE` permission to the created scope.
        :param scope_backend_type: :class:`ScopeBackendType` (optional)
          The backend type the scope will be created with. If not specified, will default to `DATABRICKS`
        



    .. py:method:: delete_acl(scope: str, principal: str)

        Delete an ACL.
        
        Deletes the given ACL on the given scope.
        
        Users must have the `MANAGE` permission to invoke this API. Throws `RESOURCE_DOES_NOT_EXIST` if no
        such secret scope, principal, or ACL exists. Throws `PERMISSION_DENIED` if the user does not have
        permission to make this API call.
        
        :param scope: str
          The name of the scope to remove permissions from.
        :param principal: str
          The principal to remove an existing ACL from.
        



    .. py:method:: delete_scope(scope: str)

        Delete a secret scope.
        
        Deletes a secret scope.
        
        Throws `RESOURCE_DOES_NOT_EXIST` if the scope does not exist. Throws `PERMISSION_DENIED` if the user
        does not have permission to make this API call.
        
        :param scope: str
          Name of the scope to delete.
        



    .. py:method:: delete_secret(scope: str, key: str)

        Delete a secret.
        
        Deletes the secret stored in this secret scope. You must have `WRITE` or `MANAGE` permission on the
        secret scope.
        
        Throws `RESOURCE_DOES_NOT_EXIST` if no such secret scope or secret exists. Throws `PERMISSION_DENIED`
        if the user does not have permission to make this API call.
        
        :param scope: str
          The name of the scope that contains the secret to delete.
        :param key: str
          Name of the secret to delete.
        



    .. py:method:: get_acl(scope: str, principal: str) -> AclItem

        Get secret ACL details.
        
        Gets the details about the given ACL, such as the group and permission. Users must have the `MANAGE`
        permission to invoke this API.
        
        Throws `RESOURCE_DOES_NOT_EXIST` if no such secret scope exists. Throws `PERMISSION_DENIED` if the
        user does not have permission to make this API call.
        
        :param scope: str
          The name of the scope to fetch ACL information from.
        :param principal: str
          The principal to fetch ACL information for.
        
        :returns: :class:`AclItem`


    .. py:method:: get_secret(scope: str, key: str) -> GetSecretResponse

        Get a secret.
        
        Gets the bytes representation of a secret value for the specified scope and key.
        
        Users need the READ permission to make this call.
        
        Note that the secret value returned is in bytes. The interpretation of the bytes is determined by the
        caller in DBUtils and the type the data is decoded into.
        
        Throws ``PERMISSION_DENIED`` if the user does not have permission to make this API call. Throws
        ``RESOURCE_DOES_NOT_EXIST`` if no such secret or secret scope exists.
        
        :param scope: str
          The name of the scope to fetch secret information from.
        :param key: str
          The key to fetch secret for.
        
        :returns: :class:`GetSecretResponse`


    .. py:method:: list_acls(scope: str) -> Iterator[AclItem]


        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            key_name = f'sdk-{time.time_ns()}'
            
            scope_name = f'sdk-{time.time_ns()}'
            
            w.secrets.create_scope(scope=scope_name)
            
            acls = w.secrets.list_acls(scope=scope_name)
            
            # cleanup
            w.secrets.delete_secret(scope=scope_name, key=key_name)
            w.secrets.delete_scope(scope=scope_name)

        Lists ACLs.
        
        List the ACLs for a given secret scope. Users must have the `MANAGE` permission to invoke this API.
        
        Throws `RESOURCE_DOES_NOT_EXIST` if no such secret scope exists. Throws `PERMISSION_DENIED` if the
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

        List all scopes.
        
        Lists all secret scopes available in the workspace.
        
        Throws `PERMISSION_DENIED` if the user does not have permission to make this API call.
        
        :returns: Iterator over :class:`SecretScope`


    .. py:method:: list_secrets(scope: str) -> Iterator[SecretMetadata]


        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            key_name = f'sdk-{time.time_ns()}'
            
            scope_name = f'sdk-{time.time_ns()}'
            
            w.secrets.create_scope(scope=scope_name)
            
            scrts = w.secrets.list_secrets(scope=scope_name)
            
            # cleanup
            w.secrets.delete_secret(scope=scope_name, key=key_name)
            w.secrets.delete_scope(scope=scope_name)

        List secret keys.
        
        Lists the secret keys that are stored at this scope. This is a metadata-only operation; secret data
        cannot be retrieved using this API. Users need the READ permission to make this call.
        
        The lastUpdatedTimestamp returned is in milliseconds since epoch. Throws `RESOURCE_DOES_NOT_EXIST` if
        no such secret scope exists. Throws `PERMISSION_DENIED` if the user does not have permission to make
        this API call.
        
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
            
            key_name = f'sdk-{time.time_ns()}'
            
            group = w.groups.create(display_name=f'sdk-{time.time_ns()}')
            
            scope_name = f'sdk-{time.time_ns()}'
            
            w.secrets.create_scope(scope=scope_name)
            
            w.secrets.put_acl(scope=scope_name, permission=workspace.AclPermission.MANAGE, principal=group.display_name)
            
            # cleanup
            w.groups.delete(id=group.id)
            w.secrets.delete_secret(scope=scope_name, key=key_name)
            w.secrets.delete_scope(scope=scope_name)

        Create/update an ACL.
        
        Creates or overwrites the Access Control List (ACL) associated with the given principal (user or
        group) on the specified scope point.
        
        In general, a user or group will use the most powerful permission available to them, and permissions
        are ordered as follows:
        
        * `MANAGE` - Allowed to change ACLs, and read and write to this secret scope. * `WRITE` - Allowed to
        read and write to this secret scope. * `READ` - Allowed to read this secret scope and list what
        secrets are available.
        
        Note that in general, secret values can only be read from within a command on a cluster (for example,
        through a notebook). There is no API to read the actual secret value material outside of a cluster.
        However, the user's permission will be applied based on who is executing the command, and they must
        have at least READ permission.
        
        Users must have the `MANAGE` permission to invoke this API.
        
        The principal is a user or group name corresponding to an existing Databricks principal to be granted
        or revoked access.
        
        Throws `RESOURCE_DOES_NOT_EXIST` if no such secret scope exists. Throws `RESOURCE_ALREADY_EXISTS` if a
        permission for the principal already exists. Throws `INVALID_PARAMETER_VALUE` if the permission or
        principal is invalid. Throws `PERMISSION_DENIED` if the user does not have permission to make this API
        call.
        
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
            
            key_name = f'sdk-{time.time_ns()}'
            
            scope_name = f'sdk-{time.time_ns()}'
            
            w.secrets.create_scope(scope=scope_name)
            
            w.secrets.put_secret(scope=scope_name, key=key_name, string_value=f'sdk-{time.time_ns()}')
            
            # cleanup
            w.secrets.delete_secret(scope=scope_name, key=key_name)
            w.secrets.delete_scope(scope=scope_name)

        Add a secret.
        
        Inserts a secret under the provided scope with the given name. If a secret already exists with the
        same name, this command overwrites the existing secret's value. The server encrypts the secret using
        the secret scope's encryption settings before storing it.
        
        You must have `WRITE` or `MANAGE` permission on the secret scope. The secret key must consist of
        alphanumeric characters, dashes, underscores, and periods, and cannot exceed 128 characters. The
        maximum allowed secret value size is 128 KB. The maximum number of secrets in a given scope is 1000.
        
        The input fields "string_value" or "bytes_value" specify the type of the secret, which will determine
        the value returned when the secret value is requested. Exactly one must be specified.
        
        Throws `RESOURCE_DOES_NOT_EXIST` if no such secret scope exists. Throws `RESOURCE_LIMIT_EXCEEDED` if
        maximum number of secrets in scope is exceeded. Throws `INVALID_PARAMETER_VALUE` if the key name or
        value length is invalid. Throws `PERMISSION_DENIED` if the user does not have permission to make this
        API call.
        
        :param scope: str
          The name of the scope to which the secret will be associated with.
        :param key: str
          A unique name to identify the secret.
        :param bytes_value: str (optional)
          If specified, value will be stored as bytes.
        :param string_value: str (optional)
          If specified, note that the value will be stored in UTF-8 (MB4) form.
        

