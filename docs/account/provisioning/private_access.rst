``a.private_access``: Private Access Settings
=============================================
.. currentmodule:: databricks.sdk.service.provisioning

.. py:class:: PrivateAccessAPI

    These APIs manage private access settings for this account.

    .. py:method:: create(private_access_settings_name: str, region: str [, allowed_vpc_endpoint_ids: Optional[List[str]], private_access_level: Optional[PrivateAccessLevel], public_access_enabled: Optional[bool]]) -> PrivateAccessSettings


        Usage:

        .. code-block::

            import os
            import time
            
            from databricks.sdk import AccountClient
            
            a = AccountClient()
            
            created = a.private_access.create(private_access_settings_name=f'sdk-{time.time_ns()}',
                                              region=os.environ["AWS_REGION"])
            
            # cleanup
            a.private_access.delete(private_access_settings_id=created.private_access_settings_id)

        Create private access settings.

Creates a private access settings object, which specifies how your workspace is accessed over [AWS
PrivateLink]. To use AWS PrivateLink, a workspace must have a private access settings object
referenced by ID in the workspace's `private_access_settings_id` property.

You can share one private access settings with multiple workspaces in a single account. However,
private access settings are specific to AWS regions, so only workspaces in the same AWS region can use
a given private access settings object.

Before configuring PrivateLink, read the [Databricks article about PrivateLink].

[AWS PrivateLink]: https://aws.amazon.com/privatelink
[Databricks article about PrivateLink]: https://docs.databricks.com/administration-guide/cloud-configurations/aws/privatelink.html

:param private_access_settings_name: str
  The human-readable name of the private access settings object.
:param region: str
  The cloud region for workspaces associated with this private access settings object.
:param allowed_vpc_endpoint_ids: List[str] (optional)
  An array of Databricks VPC endpoint IDs. This is the Databricks ID that is returned when registering
  the VPC endpoint configuration in your Databricks account. This is not the ID of the VPC endpoint in
  AWS.
  
  Only used when `private_access_level` is set to `ENDPOINT`. This is an allow list of VPC endpoints
  that in your account that can connect to your workspace over AWS PrivateLink.
  
  If hybrid access to your workspace is enabled by setting `public_access_enabled` to `true`, this
  control only works for PrivateLink connections. To control how your workspace is accessed via public
  internet, see [IP access lists].
  
  [IP access lists]: https://docs.databricks.com/security/network/ip-access-list.html
:param private_access_level: :class:`PrivateAccessLevel` (optional)
  The private access level controls which VPC endpoints can connect to the UI or API of any workspace
  that attaches this private access settings object. * `ACCOUNT` level access (the default) allows
  only VPC endpoints that are registered in your Databricks account connect to your workspace. *
  `ENDPOINT` level access allows only specified VPC endpoints connect to your workspace. For details,
  see `allowed_vpc_endpoint_ids`.
:param public_access_enabled: bool (optional)
  Determines if the workspace can be accessed over public internet. For fully private workspaces, you
  can optionally specify `false`, but only if you implement both the front-end and the back-end
  PrivateLink connections. Otherwise, specify `true`, which means that public access is enabled.

:returns: :class:`PrivateAccessSettings`


    .. py:method:: delete(private_access_settings_id: str)

        Delete a private access settings object.

Deletes a private access settings object, which determines how your workspace is accessed over [AWS
PrivateLink].

Before configuring PrivateLink, read the [Databricks article about PrivateLink].",

[AWS PrivateLink]: https://aws.amazon.com/privatelink
[Databricks article about PrivateLink]: https://docs.databricks.com/administration-guide/cloud-configurations/aws/privatelink.html

:param private_access_settings_id: str
  Databricks Account API private access settings ID.




    .. py:method:: get(private_access_settings_id: str) -> PrivateAccessSettings


        Usage:

        .. code-block::

            import os
            import time
            
            from databricks.sdk import AccountClient
            
            a = AccountClient()
            
            created = a.private_access.create(private_access_settings_name=f'sdk-{time.time_ns()}',
                                              region=os.environ["AWS_REGION"])
            
            by_id = a.private_access.get(private_access_settings_id=created.private_access_settings_id)
            
            # cleanup
            a.private_access.delete(private_access_settings_id=created.private_access_settings_id)

        Get a private access settings object.

Gets a private access settings object, which specifies how your workspace is accessed over [AWS
PrivateLink].

Before configuring PrivateLink, read the [Databricks article about PrivateLink].",

[AWS PrivateLink]: https://aws.amazon.com/privatelink
[Databricks article about PrivateLink]: https://docs.databricks.com/administration-guide/cloud-configurations/aws/privatelink.html

:param private_access_settings_id: str
  Databricks Account API private access settings ID.

:returns: :class:`PrivateAccessSettings`


    .. py:method:: list() -> Iterator[PrivateAccessSettings]


        Usage:

        .. code-block::

            from databricks.sdk import AccountClient
            
            a = AccountClient()
            
            all = a.private_access.list()

        Get all private access settings objects.

Gets a list of all private access settings objects for an account, specified by ID.

:returns: Iterator over :class:`PrivateAccessSettings`


    .. py:method:: replace(private_access_settings_id: str, private_access_settings_name: str, region: str [, allowed_vpc_endpoint_ids: Optional[List[str]], private_access_level: Optional[PrivateAccessLevel], public_access_enabled: Optional[bool]])


        Usage:

        .. code-block::

            import os
            import time
            
            from databricks.sdk import AccountClient
            
            a = AccountClient()
            
            created = a.private_access.create(private_access_settings_name=f'sdk-{time.time_ns()}',
                                              region=os.environ["AWS_REGION"])
            
            a.private_access.replace(private_access_settings_id=created.private_access_settings_id,
                                     private_access_settings_name=f'sdk-{time.time_ns()}',
                                     region=os.environ["AWS_REGION"])
            
            # cleanup
            a.private_access.delete(private_access_settings_id=created.private_access_settings_id)

        Replace private access settings.

Updates an existing private access settings object, which specifies how your workspace is accessed
over [AWS PrivateLink]. To use AWS PrivateLink, a workspace must have a private access settings object
referenced by ID in the workspace's `private_access_settings_id` property.

This operation completely overwrites your existing private access settings object attached to your
workspaces. All workspaces attached to the private access settings are affected by any change. If
`public_access_enabled`, `private_access_level`, or `allowed_vpc_endpoint_ids` are updated, effects of
these changes might take several minutes to propagate to the workspace API.

You can share one private access settings object with multiple workspaces in a single account.
However, private access settings are specific to AWS regions, so only workspaces in the same AWS
region can use a given private access settings object.

Before configuring PrivateLink, read the [Databricks article about PrivateLink].

[AWS PrivateLink]: https://aws.amazon.com/privatelink
[Databricks article about PrivateLink]: https://docs.databricks.com/administration-guide/cloud-configurations/aws/privatelink.html

:param private_access_settings_id: str
  Databricks Account API private access settings ID.
:param private_access_settings_name: str
  The human-readable name of the private access settings object.
:param region: str
  The cloud region for workspaces associated with this private access settings object.
:param allowed_vpc_endpoint_ids: List[str] (optional)
  An array of Databricks VPC endpoint IDs. This is the Databricks ID that is returned when registering
  the VPC endpoint configuration in your Databricks account. This is not the ID of the VPC endpoint in
  AWS.
  
  Only used when `private_access_level` is set to `ENDPOINT`. This is an allow list of VPC endpoints
  that in your account that can connect to your workspace over AWS PrivateLink.
  
  If hybrid access to your workspace is enabled by setting `public_access_enabled` to `true`, this
  control only works for PrivateLink connections. To control how your workspace is accessed via public
  internet, see [IP access lists].
  
  [IP access lists]: https://docs.databricks.com/security/network/ip-access-list.html
:param private_access_level: :class:`PrivateAccessLevel` (optional)
  The private access level controls which VPC endpoints can connect to the UI or API of any workspace
  that attaches this private access settings object. * `ACCOUNT` level access (the default) allows
  only VPC endpoints that are registered in your Databricks account connect to your workspace. *
  `ENDPOINT` level access allows only specified VPC endpoints connect to your workspace. For details,
  see `allowed_vpc_endpoint_ids`.
:param public_access_enabled: bool (optional)
  Determines if the workspace can be accessed over public internet. For fully private workspaces, you
  can optionally specify `false`, but only if you implement both the front-end and the back-end
  PrivateLink connections. Otherwise, specify `true`, which means that public access is enabled.


