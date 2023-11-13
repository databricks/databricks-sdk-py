Account IP Access Lists
=======================
.. py:class:: AccountIpAccessListsAPI

    The Accounts IP Access List API enables account admins to configure IP access lists for access to the
    account console.
    
    Account IP Access Lists affect web application access and REST API access to the account console and
    account APIs. If the feature is disabled for the account, all access is allowed for this account. There is
    support for allow lists (inclusion) and block lists (exclusion).
    
    When a connection is attempted: 1. **First, all block lists are checked.** If the connection IP address
    matches any block list, the connection is rejected. 2. **If the connection was not rejected by block
    lists**, the IP address is compared with the allow lists.
    
    If there is at least one allow list for the account, the connection is allowed only if the IP address
    matches an allow list. If there are no allow lists for the account, all IP addresses are allowed.
    
    For all allow lists and block lists combined, the account supports a maximum of 1000 IP/CIDR values, where
    one CIDR counts as a single value.
    
    After changes to the account-level IP access lists, it can take a few minutes for changes to take effect.

    .. py:method:: create(label, list_type, ip_addresses)

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
        
        Creates an IP access list for the account.
        
        A list can be an allow list or a block list. See the top of this file for a description of how the
        server treats allow lists and block lists at runtime.
        
        When creating or updating an IP access list:
        
        * For all allow lists and block lists combined, the API supports a maximum of 1000 IP/CIDR values,
        where one CIDR counts as a single value. Attempts to exceed that number return error 400 with
        `error_code` value `QUOTA_EXCEEDED`. * If the new list would block the calling user's current IP,
        error 400 is returned with `error_code` value `INVALID_STATE`.
        
        It can take a few minutes for the changes to take effect.
        
        :param label: str
          Label for the IP access list. This **cannot** be empty.
        :param list_type: :class:`ListType`
          Type of IP access list. Valid values are as follows and are case-sensitive:
          
          * `ALLOW`: An allow list. Include this IP or range. * `BLOCK`: A block list. Exclude this IP or
          range. IP addresses in the block list are excluded even if they are included in an allow list.
        :param ip_addresses: List[str]
          Array of IP addresses or CIDR values to be added to the IP access list.
        
        :returns: :class:`CreateIpAccessListResponse`
        

    .. py:method:: delete(ip_access_list_id)

        Delete access list.
        
        Deletes an IP access list, specified by its list ID.
        
        :param ip_access_list_id: str
          The ID for the corresponding IP access list.
        
        
        

    .. py:method:: get(ip_access_list_id)

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

        Get IP access list.
        
        Gets an IP access list, specified by its list ID.
        
        :param ip_access_list_id: str
          The ID for the corresponding IP access list.
        
        :returns: :class:`GetIpAccessListResponse`
        

    .. py:method:: list()

        Usage:

        .. code-block::

            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            all = w.ip_access_lists.list()

        Get access lists.
        
        Gets all IP access lists for the specified account.
        
        :returns: Iterator over :class:`IpAccessListInfo`
        

    .. py:method:: replace(ip_access_list_id, label, list_type, ip_addresses, enabled [, list_id])

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
        effect.
        
        :param ip_access_list_id: str
          The ID for the corresponding IP access list.
        :param label: str
          Label for the IP access list. This **cannot** be empty.
        :param list_type: :class:`ListType`
          Type of IP access list. Valid values are as follows and are case-sensitive:
          
          * `ALLOW`: An allow list. Include this IP or range. * `BLOCK`: A block list. Exclude this IP or
          range. IP addresses in the block list are excluded even if they are included in an allow list.
        :param ip_addresses: List[str]
          Array of IP addresses or CIDR values to be added to the IP access list.
        :param enabled: bool
          Specifies whether this IP access list is enabled.
        :param list_id: str (optional)
          Universally unique identifier (UUID) of the IP access list.
        
        
        

    .. py:method:: update(ip_access_list_id, label, list_type, ip_addresses, enabled [, list_id])

        Update access list.
        
        Updates an existing IP access list, specified by its ID.
        
        A list can include allow lists and block lists. See the top of this file for a description of how the
        server treats allow lists and block lists at run time.
        
        When updating an IP access list:
        
        * For all allow lists and block lists combined, the API supports a maximum of 1000 IP/CIDR values,
        where one CIDR counts as a single value. Attempts to exceed that number return error 400 with
        `error_code` value `QUOTA_EXCEEDED`. * If the updated list would block the calling user's current IP,
        error 400 is returned with `error_code` value `INVALID_STATE`.
        
        It can take a few minutes for the changes to take effect.
        
        :param ip_access_list_id: str
          The ID for the corresponding IP access list.
        :param label: str
          Label for the IP access list. This **cannot** be empty.
        :param list_type: :class:`ListType`
          Type of IP access list. Valid values are as follows and are case-sensitive:
          
          * `ALLOW`: An allow list. Include this IP or range. * `BLOCK`: A block list. Exclude this IP or
          range. IP addresses in the block list are excluded even if they are included in an allow list.
        :param ip_addresses: List[str]
          Array of IP addresses or CIDR values to be added to the IP access list.
        :param enabled: bool
          Specifies whether this IP access list is enabled.
        :param list_id: str (optional)
          Universally unique identifier (UUID) of the IP access list.
        
        
        