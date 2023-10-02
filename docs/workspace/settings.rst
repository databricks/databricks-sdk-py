Default Namespace
=================
.. py:class:: SettingsAPI

    // TODO(yuyuan.tang) to add the description for the setting

    .. py:method:: delete_default_workspace_namespace(etag)

        Delete the default namespace.
        
        Deletes the default namespace.
        
        :param etag: str
          etag used for versioning. The response is at least as fresh as the eTag provided. This is used for
          optimistic concurrency control as a way to help prevent simultaneous writes of a setting overwriting
          each other. It is strongly suggested that systems make use of the etag in the read -> delete pattern
          to perform setting deletions in order to avoid race conditions. That is, get an etag from a GET
          request, and pass it with the DELETE request to identify the rule set version you are deleting.
        
        :returns: :class:`DeleteDefaultWorkspaceNamespaceResponse`
        

    .. py:method:: read_default_workspace_namespace(etag)

        Get the default namespace.
        
        Gets the default namespace.
        
        :param etag: str
          etag used for versioning. The response is at least as fresh as the eTag provided. This is used for
          optimistic concurrency control as a way to help prevent simultaneous writes of a setting overwriting
          each other. It is strongly suggested that systems make use of the etag in the read -> delete pattern
          to perform setting deletions in order to avoid race conditions. That is, get an etag from a GET
          request, and pass it with the DELETE request to identify the rule set version you are deleting.
        
        :returns: :class:`DefaultNamespaceSetting`
        

    .. py:method:: update_default_workspace_namespace( [, allow_missing, field_mask, setting])

        Updates the default namespace setting.
        
        Updates the default namespace setting for the workspace. A fresh etag needs to be provided in PATCH
        requests (as part the setting field). The etag can be retrieved by making a GET request before the
        PATCH request. Note that if the setting does not exist, GET will return a NOT_FOUND error and the etag
        will be present in the error response, which should be set in the PATCH request.
        
        :param allow_missing: bool (optional)
          This should always be set to true for Settings RPCs. Added for AIP compliance.
        :param field_mask: str (optional)
          Field mask required to be passed into the PATCH request. Field mask specifies which fields of the
          setting payload will be updated. For example, for Default Namespace setting, the field mask is
          supposed to contain fields from the DefaultNamespaceSetting.namespace schema.
          
          The field mask needs to supplied as single string. To specify multiple fields in the field mask, use
          comma as the seperator (no space).
        :param setting: :class:`DefaultNamespaceSetting` (optional)
          Default namespace setting.
        
        :returns: :class:`DefaultNamespaceSetting`
        