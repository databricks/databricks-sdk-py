CurrentUser
===========
.. py:class:: CurrentUserAPI

    This API allows retrieving information about currently authenticated user or service principal.

    .. py:method:: me()

        Usage:

        .. code-block::

            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            me2 = w.current_user.me()

        Get current user info.
        
        Get details about the current method caller's identity.
        
        :returns: :class:`User`
        