``w.current_user``: Current User
================================
.. currentmodule:: databricks.sdk.service.iam

.. py:class:: CurrentUserAPI

    This API allows retrieving information about currently authenticated user or service principal.

    .. py:method:: me( [, attributes: Optional[str], excluded_attributes: Optional[str]]) -> User


        Usage:

        .. code-block::

            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            me2 = w.current_user.me()

        Get details about the current method caller's identity.

        :param attributes: str (optional)
          Comma-separated list of attributes to return in response.
        :param excluded_attributes: str (optional)
          Comma-separated list of attributes to exclude in response.

        :returns: :class:`User`
        