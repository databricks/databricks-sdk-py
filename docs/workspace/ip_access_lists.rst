IP Access Lists
===============
.. currentmodule:: databricks.sdk.service.settings

.. py:class:: IpAccessListsAPI

    IP Access List enables admins to configure IP access lists.
    
    IP access lists affect web application access and REST API access to this workspace only. If the feature
    is disabled for a workspace, all access is allowed for this workspace. There is support for allow lists
    (inclusion) and block lists (exclusion).
    
    When a connection is attempted: 1. **First, all block lists are checked.** If the connection IP address
    matches any block list, the connection is rejected. 2. **If the connection was not rejected by block
    lists**, the IP address is compared with the allow lists.
    
    If there is at least one allow list for the workspace, the connection is allowed only if the IP address
    matches an allow list. If there are no allow lists for the workspace, all IP addresses are allowed.
    
    For all allow lists and block lists combined, the workspace supports a maximum of 1000 IP/CIDR values,
    where one CIDR counts as a single value.
    
    After changes to the IP access list feature, it can take a few minutes for changes to take effect.

    .. py:method:: create(label: str, list_type: ListType [, ip_addresses: Optional[List[str]]]) -> CreateIpAccessListResponse


        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import settings
            
            w = WorkspaceClient()
            
            created = w.ip_access_lists.create(label=f'sdk-{time.time_ns()}',
                                               ip_addresses=["1.0.0.0/16"],
                                               list_type=settings.ListType.BLOCK)
            
            # cleanup
            w.ip_access_lists.delete(ip_access_list_id=created.ip_access_list.list_id)

        Create access list.
        
        Creates an IP access list for this workspace.
        
        A list can be an allow list or a block list. See the top of this file for a description of how the
        server treats allow lists and block lists at runtime.
        
        When creating or updating an IP access list:
        
        * For all allow lists and block lists combined, the API supports a maximum of 1000 IP/CIDR values,
        where one CIDR counts as a single value. Attempts to exceed that number return error 400 with
        `error_code` value `QUOTA_EXCEEDED`. * If the new list would block the calling user's current IP,
        error 400 is returned with `error_code` value `INVALID_STATE`.
        
        It can take a few minutes for the changes to take effect. **Note**: Your new IP access list has no
        effect until you enable the feature. See :method:workspaceconf/setStatus
        
        :param label: str
          Label for the IP access list. This **cannot** be empty.
        :param list_type: :class:`ListType`
          Type of IP access list. Valid values are as follows and are case-sensitive:
          
          * `ALLOW`: An allow list. Include this IP or range. * `BLOCK`: A block list. Exclude this IP or
          range. IP addresses in the block list are excluded even if they are included in an allow list.
        :param ip_addresses: List[str] (optional)
        
        :returns: :class:`CreateIpAccessListResponse`
        

    .. py:method:: delete(ip_access_list_id: str)

        Delete access list.
        
        Deletes an IP access list, specified by its list ID.
        
        :param ip_access_list_id: str
          The ID for the corresponding IP access list
        
        
        

    .. py:method:: get(ip_access_list_id: str) -> FetchIpAccessListResponse


        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import settings
            
            w = WorkspaceClient()
            
            created = w.ip_access_lists.create(label=f'sdk-{time.time_ns()}',
                                               ip_addresses=["1.0.0.0/16"],
                                               list_type=settings.ListType.BLOCK)
            
            by_id = w.ip_access_lists.get(ip_access_list_id=created.ip_access_list.list_id)
            
            # cleanup
            w.ip_access_lists.delete(ip_access_list_id=created.ip_access_list.list_id)

        Get access list.
        
        Gets an IP access list, specified by its list ID.
        
        :param ip_access_list_id: str
          The ID for the corresponding IP access list
        
        :returns: :class:`FetchIpAccessListResponse`
        

    .. py:method:: list() -> Iterator[IpAccessListInfo]


        Usage:

        .. code-block::

            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            all = w.ip_access_lists.list()

        Get access lists.
        
        Gets all IP access lists for the specified workspace.
        
        :returns: Iterator over :class:`IpAccessListInfo`
        

    .. py:method:: replace(ip_access_list_id: str, label: str, list_type: ListType, enabled: bool [, ip_addresses: Optional[List[str]]])


        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import settings
            
            w = WorkspaceClient()
            
            created = w.ip_access_lists.create(label=f'sdk-{time.time_ns()}',
                                               ip_addresses=["1.0.0.0/16"],
                                               list_type=settings.ListType.BLOCK)
            
            w.ip_access_lists.replace(ip_access_list_id=created.ip_access_list.list_id,
                                      label=f'sdk-{time.time_ns()}',
                                      ip_addresses=["1.0.0.0/24"],
                                      list_type=settings.ListType.BLOCK,
                                      enabled=False)
            
            # cleanup
            w.ip_access_lists.delete(ip_access_list_id=created.ip_access_list.list_id)

        Replace access list.
        
        Replaces an IP access list, specified by its ID.
        
        A list can include allow lists and block lists. See the top of this file for a description of how the
        server treats allow lists and block lists at run time. When replacing an IP access list: * For all
        allow lists and block lists combined, the API supports a maximum of 1000 IP/CIDR values, where one
        CIDR counts as a single value. Attempts to exceed that number return error 400 with `error_code` value
        `QUOTA_EXCEEDED`. * If the resulting list would block the calling user's current IP, error 400 is
        returned with `error_code` value `INVALID_STATE`. It can take a few minutes for the changes to take
        effect. Note that your resulting IP access list has no effect until you enable the feature. See
        :method:workspaceconf/setStatus.
        
        :param ip_access_list_id: str
          The ID for the corresponding IP access list
        :param label: str
          Label for the IP access list. This **cannot** be empty.
        :param list_type: :class:`ListType`
          Type of IP access list. Valid values are as follows and are case-sensitive:
          
          * `ALLOW`: An allow list. Include this IP or range. * `BLOCK`: A block list. Exclude this IP or
          range. IP addresses in the block list are excluded even if they are included in an allow list.
        :param enabled: bool
          Specifies whether this IP access list is enabled.
        :param ip_addresses: List[str] (optional)
        
        
        

    .. py:method:: update(ip_access_list_id: str [, enabled: Optional[bool], ip_addresses: Optional[List[str]], label: Optional[str], list_type: Optional[ListType]])

        Update access list.
        
        Updates an existing IP access list, specified by its ID.
        
        A list can include allow lists and block lists. See the top of this file for a description of how the
        server treats allow lists and block lists at run time.
        
        When updating an IP access list:
        
        * For all allow lists and block lists combined, the API supports a maximum of 1000 IP/CIDR values,
        where one CIDR counts as a single value. Attempts to exceed that number return error 400 with
        `error_code` value `QUOTA_EXCEEDED`. * If the updated list would block the calling user's current IP,
        error 400 is returned with `error_code` value `INVALID_STATE`.
        
        It can take a few minutes for the changes to take effect. Note that your resulting IP access list has
        no effect until you enable the feature. See :method:workspaceconf/setStatus.
        
        :param ip_access_list_id: str
          The ID for the corresponding IP access list
        :param enabled: bool (optional)
          Specifies whether this IP access list is enabled.
        :param ip_addresses: List[str] (optional)
        :param label: str (optional)
          Label for the IP access list. This **cannot** be empty.
        :param list_type: :class:`ListType` (optional)
          Type of IP access list. Valid values are as follows and are case-sensitive:
          
          * `ALLOW`: An allow list. Include this IP or range. * `BLOCK`: A block list. Exclude this IP or
          range. IP addresses in the block list are excluded even if they are included in an allow list.
        
        
        