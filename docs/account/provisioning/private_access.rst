``a.private_access``: Private Access Settings
=============================================
.. currentmodule:: databricks.sdk.service.provisioning

.. py:class:: PrivateAccessAPI

    These APIs manage private access settings for this account.

    .. py:method:: create( [, allowed_vpc_endpoint_ids: Optional[List[str]], private_access_level: Optional[PrivateAccessLevel], private_access_settings_name: Optional[str], public_access_enabled: Optional[bool], region: Optional[str]]) -> PrivateAccessSettings


        Usage:

        .. code-block::

            import os
            import time
            
            from databricks.sdk import AccountClient
            
            a = AccountClient()
            
            created = a.private_access.create(
                private_access_settings_name=f"sdk-{time.time_ns()}",
                region=os.environ["AWS_REGION"],
            )
            
            # cleanup
            a.private_access.delete(private_access_settings_id=created.private_access_settings_id)

        Creates a private access settings configuration, which represents network access restrictions for
        workspace resources. Private access settings configure whether workspaces can be accessed from the
        public internet or only from private endpoints.

        :param allowed_vpc_endpoint_ids: List[str] (optional)
          An array of Databricks VPC endpoint IDs. This is the Databricks ID returned when registering the VPC
          endpoint configuration in your Databricks account. This is not the ID of the VPC endpoint in AWS.
          Only used when private_access_level is set to ENDPOINT. This is an allow list of VPC endpoints
          registered in your Databricks account that can connect to your workspace over AWS PrivateLink. Note:
          If hybrid access to your workspace is enabled by setting public_access_enabled to true, this control
          only works for PrivateLink connections. To control how your workspace is accessed via public
          internet, see IP access lists.
        :param private_access_level: :class:`PrivateAccessLevel` (optional)
          The private access level controls which VPC endpoints can connect to the UI or API of any workspace
          that attaches this private access settings object. `ACCOUNT` level access (the default) allows only
          VPC endpoints that are registered in your Databricks account connect to your workspace. `ENDPOINT`
          level access allows only specified VPC endpoints connect to your workspace. For details, see
          allowed_vpc_endpoint_ids.
        :param private_access_settings_name: str (optional)
          The human-readable name of the private access settings object.
        :param public_access_enabled: bool (optional)
          Determines if the workspace can be accessed over public internet. For fully private workspaces, you
          can optionally specify false, but only if you implement both the front-end and the back-end
          PrivateLink connections. Otherwise, specify true, which means that public access is enabled.
        :param region: str (optional)
          The AWS region for workspaces attached to this private access settings object.

        :returns: :class:`PrivateAccessSettings`
        

    .. py:method:: delete(private_access_settings_id: str) -> PrivateAccessSettings

        Deletes a Databricks private access settings configuration, both specified by ID.

        :param private_access_settings_id: str

        :returns: :class:`PrivateAccessSettings`
        

    .. py:method:: get(private_access_settings_id: str) -> PrivateAccessSettings


        Usage:

        .. code-block::

            import os
            import time
            
            from databricks.sdk import AccountClient
            
            a = AccountClient()
            
            created = a.private_access.create(
                private_access_settings_name=f"sdk-{time.time_ns()}",
                region=os.environ["AWS_REGION"],
            )
            
            by_id = a.private_access.get(private_access_settings_id=created.private_access_settings_id)
            
            # cleanup
            a.private_access.delete(private_access_settings_id=created.private_access_settings_id)

        Gets a Databricks private access settings configuration, both specified by ID.

        :param private_access_settings_id: str

        :returns: :class:`PrivateAccessSettings`
        

    .. py:method:: list() -> Iterator[PrivateAccessSettings]


        Usage:

        .. code-block::

            from databricks.sdk import AccountClient
            
            a = AccountClient()
            
            all = a.private_access.list()

        Lists Databricks private access settings for an account.


        :returns: Iterator over :class:`PrivateAccessSettings`
        

    .. py:method:: replace(private_access_settings_id: str, customer_facing_private_access_settings: PrivateAccessSettings) -> PrivateAccessSettings


        Usage:

        .. code-block::

            import os
            import time
            
            from databricks.sdk import AccountClient
            
            a = AccountClient()
            
            created = a.private_access.create(
                private_access_settings_name=f"sdk-{time.time_ns()}",
                region=os.environ["AWS_REGION"],
            )
            
            a.private_access.replace(
                private_access_settings_id=created.private_access_settings_id,
                private_access_settings_name=f"sdk-{time.time_ns()}",
                region=os.environ["AWS_REGION"],
            )
            
            # cleanup
            a.private_access.delete(private_access_settings_id=created.private_access_settings_id)

        Updates an existing private access settings object, which specifies how your workspace is accessed
        over AWS PrivateLink. To use AWS PrivateLink, a workspace must have a private access settings object
        referenced by ID in the workspace's private_access_settings_id property. This operation completely
        overwrites your existing private access settings object attached to your workspaces. All workspaces
        attached to the private access settings are affected by any change. If public_access_enabled,
        private_access_level, or allowed_vpc_endpoint_ids are updated, effects of these changes might take
        several minutes to propagate to the workspace API. You can share one private access settings object
        with multiple workspaces in a single account. However, private access settings are specific to AWS
        regions, so only workspaces in the same AWS region can use a given private access settings object.
        Before configuring PrivateLink, read the Databricks article about PrivateLink.

        :param private_access_settings_id: str
          Databricks private access settings ID.
        :param customer_facing_private_access_settings: :class:`PrivateAccessSettings`
          Properties of the new private access settings object.

        :returns: :class:`PrivateAccessSettings`
        