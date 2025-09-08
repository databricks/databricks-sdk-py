``w.workspace_conf``: Workspace Conf
====================================
.. currentmodule:: databricks.sdk.service.settings

.. py:class:: WorkspaceConfAPI

    This API allows updating known workspace settings for advanced users.

    .. py:method:: get_status(keys: str) -> WorkspaceConf


        Usage:

        .. code-block::

            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            conf = w.workspace_conf.get_status(keys="enableWorkspaceFilesystem")

        Gets the configuration status for a workspace.
        
        :param keys: str
        
        :returns: Dict[str,str]
        

    .. py:method:: set_status(contents: Dict[str, str])

        Sets the configuration status for a workspace, including enabling or disabling it.
        
        
        
        