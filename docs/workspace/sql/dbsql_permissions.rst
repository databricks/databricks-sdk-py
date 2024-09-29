``w.dbsql_permissions``: ACL / Permissions
==========================================
.. currentmodule:: databricks.sdk.service.sql

.. py:class:: DbsqlPermissionsAPI

    The SQL Permissions API is similar to the endpoints of the :method:permissions/set. However, this exposes
    only one endpoint, which gets the Access Control List for a given object. You cannot modify any
    permissions using this API.
    
    There are three levels of permission:
    
    - `CAN_VIEW`: Allows read-only access
    
    - `CAN_RUN`: Allows read access and run access (superset of `CAN_VIEW`)
    
    - `CAN_MANAGE`: Allows all actions: read, run, edit, delete, modify permissions (superset of `CAN_RUN`)
    
    **Note**: A new version of the Databricks SQL API is now available. [Learn more]
    
    [Learn more]: https://docs.databricks.com/en/sql/dbsql-api-latest.html

    .. py:method:: get(object_type: ObjectTypePlural, object_id: str) -> GetResponse

        Get object ACL.
        
        Gets a JSON representation of the access control list (ACL) for a specified object.
        
        **Note**: A new version of the Databricks SQL API is now available. Please use
        :method:workspace/getpermissions instead. [Learn more]
        
        [Learn more]: https://docs.databricks.com/en/sql/dbsql-api-latest.html
        
        :param object_type: :class:`ObjectTypePlural`
          The type of object permissions to check.
        :param object_id: str
          Object ID. An ACL is returned for the object with this UUID.
        
        :returns: :class:`GetResponse`
        

    .. py:method:: set(object_type: ObjectTypePlural, object_id: str [, access_control_list: Optional[List[AccessControl]]]) -> SetResponse

        Set object ACL.
        
        Sets the access control list (ACL) for a specified object. This operation will complete rewrite the
        ACL.
        
        **Note**: A new version of the Databricks SQL API is now available. Please use
        :method:workspace/setpermissions instead. [Learn more]
        
        [Learn more]: https://docs.databricks.com/en/sql/dbsql-api-latest.html
        
        :param object_type: :class:`ObjectTypePlural`
          The type of object permission to set.
        :param object_id: str
          Object ID. The ACL for the object with this UUID is overwritten by this request's POST content.
        :param access_control_list: List[:class:`AccessControl`] (optional)
        
        :returns: :class:`SetResponse`
        

    .. py:method:: transfer_ownership(object_type: OwnableObjectType, object_id: TransferOwnershipObjectId [, new_owner: Optional[str]]) -> Success

        Transfer object ownership.
        
        Transfers ownership of a dashboard, query, or alert to an active user. Requires an admin API key.
        
        **Note**: A new version of the Databricks SQL API is now available. For queries and alerts, please use
        :method:queries/update and :method:alerts/update respectively instead. [Learn more]
        
        [Learn more]: https://docs.databricks.com/en/sql/dbsql-api-latest.html
        
        :param object_type: :class:`OwnableObjectType`
          The type of object on which to change ownership.
        :param object_id: :class:`TransferOwnershipObjectId`
          The ID of the object on which to change ownership.
        :param new_owner: str (optional)
          Email address for the new owner, who must exist in the workspace.
        
        :returns: :class:`Success`
        