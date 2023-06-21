Workspace
=========
.. py:class:: WorkspaceAPI

    

    .. py:method:: delete(path [, recursive])

        Delete a workspace object.
        
        Deletes an object or a directory (and optionally recursively deletes all objects in the directory). *
        If `path` does not exist, this call returns an error `RESOURCE_DOES_NOT_EXIST`. * If `path` is a
        non-empty directory and `recursive` is set to `false`, this call returns an error
        `DIRECTORY_NOT_EMPTY`.
        
        Object deletion cannot be undone and deleting a directory recursively is not atomic.
        
        :param path: str
          The absolute path of the notebook or directory.
        :param recursive: bool (optional)
          The flag that specifies whether to delete the object recursively. It is `false` by default. Please
          note this deleting directory is not atomic. If it fails in the middle, some of objects under this
          directory may be deleted and cannot be undone.
        
        
        

    .. py:method:: download(path [, format])

        
        Downloads notebook or file from the workspace

        :param path:     location of the file or notebook on workspace.
        :param format:   By default, `ExportFormat.SOURCE`. If using `ExportFormat.AUTO` the `path`
                         is imported or exported as either a workspace file or a notebook, depending
                         on an analysis of the `item`’s extension and the header content provided in
                         the request.
        :return:         file-like `io.BinaryIO` of the `path` contents.
        

    .. py:method:: export(path [, format])

        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import workspace
            
            w = WorkspaceClient()
            
            notebook = f'/Users/{w.current_user.me().user_name}/sdk-{time.time_ns()}'
            
            export_response = w.workspace.export(format=workspace.ExportFormat.SOURCE, path=notebook)

        Export a workspace object.
        
        Exports an object or the contents of an entire directory.
        
        If `path` does not exist, this call returns an error `RESOURCE_DOES_NOT_EXIST`.
        
        If the exported data would exceed size limit, this call returns `MAX_NOTEBOOK_SIZE_EXCEEDED`.
        Currently, this API does not support exporting a library.
        
        :param path: str
          The absolute path of the object or directory. Exporting a directory is only supported for the `DBC`
          and `SOURCE` format.
        :param format: :class:`ExportFormat` (optional)
          This specifies the format of the exported file. By default, this is `SOURCE`.
          
          The value is case sensitive.
          
          - `SOURCE`: The notebook is exported as source code. - `HTML`: The notebook is exported as an HTML
          file. - `JUPYTER`: The notebook is exported as a Jupyter/IPython Notebook file. - `DBC`: The
          notebook is exported in Databricks archive format. - `R_MARKDOWN`: The notebook is exported to R
          Markdown format.
        
        :returns: :class:`ExportResponse`
        

    .. py:method:: get_status(path)

        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            notebook_path = f'/Users/{w.current_user.me().user_name}/sdk-{time.time_ns()}'
            
            obj = w.workspace.get_status(get_status=notebook_path)

        Get status.
        
        Gets the status of an object or a directory. If `path` does not exist, this call returns an error
        `RESOURCE_DOES_NOT_EXIST`.
        
        :param path: str
          The absolute path of the notebook or directory.
        
        :returns: :class:`ObjectInfo`
        

    .. py:method:: import_(path [, content, format, language, overwrite])

        Usage:

        .. code-block::

            import base64
            import time
            
            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import workspace
            
            w = WorkspaceClient()
            
            notebook_path = f'/Users/{w.current_user.me().user_name}/sdk-{time.time_ns()}'
            
            w.workspace.import_(content=base64.b64encode(("CREATE LIVE TABLE dlt_sample AS SELECT 1").encode()).decode(),
                                format=workspace.ImportFormat.SOURCE,
                                language=workspace.Language.SQL,
                                overwrite=True,
                                path=notebook_path)

        Import a workspace object.
        
        Imports a workspace object (for example, a notebook or file) or the contents of an entire directory.
        If `path` already exists and `overwrite` is set to `false`, this call returns an error
        `RESOURCE_ALREADY_EXISTS`. One can only use `DBC` format to import a directory.
        
        :param path: str
          The absolute path of the object or directory. Importing a directory is only supported for the `DBC`
          format.
        :param content: str (optional)
          The base64-encoded content. This has a limit of 10 MB.
          
          If the limit (10MB) is exceeded, exception with error code **MAX_NOTEBOOK_SIZE_EXCEEDED** is thrown.
          This parameter might be absent, and instead a posted file is used.
        :param format: :class:`ImportFormat` (optional)
          This specifies the format of the file to be imported.
          
          The value is case sensitive.
          
          - `AUTO`: The item is imported depending on an analysis of the item's extension and the header
          content provided in the request. If the item is imported as a notebook, then the item's extension is
          automatically removed. - `SOURCE`: The notebook is imported as source code. - `HTML`: The notebook
          is imported as an HTML file. - `JUPYTER`: The notebook is imported as a Jupyter/IPython Notebook
          file. - `DBC`: The notebook is imported in Databricks archive format. Required for directories. -
          `R_MARKDOWN`: The notebook is imported from R Markdown format.
        :param language: :class:`Language` (optional)
          The language of the object. This value is set only if the object type is `NOTEBOOK`.
        :param overwrite: bool (optional)
          The flag that specifies whether to overwrite existing object. It is `false` by default. For `DBC`
          format, `overwrite` is not supported since it may contain a directory.
        
        
        

    .. py:method:: list(path [, notebooks_modified_after, recursive])

        Usage:

        .. code-block::

            import os
            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            notebook = f'/Users/{w.current_user.me().user_name}/sdk-{time.time_ns()}'
            
            objects = w.workspace.list(path=os.path.dirname(notebook))

        List workspace objects

        :param recursive: bool
            Optionally invoke recursive traversal

        :returns: Iterator of workspaceObjectInfo
        

    .. py:method:: mkdirs(path)

        Create a directory.
        
        Creates the specified directory (and necessary parent directories if they do not exist). If there is
        an object (not a directory) at any prefix of the input path, this call returns an error
        `RESOURCE_ALREADY_EXISTS`.
        
        Note that if this operation fails it may have succeeded in creating some of the necessary parent
        directories.
        
        :param path: str
          The absolute path of the directory. If the parent directories do not exist, it will also create
          them. If the directory already exists, this command will do nothing and succeed.
        
        
        

    .. py:method:: upload(path, content [, format, language, overwrite])

        
        Uploads a workspace object (for example, a notebook or file) or the contents of an entire
        directory (`DBC` format).

        Errors:
         * `RESOURCE_ALREADY_EXISTS`: if `path` already exists no `overwrite=True`.
         * `INVALID_PARAMETER_VALUE`: if `format` and `content` values are not compatible.

        :param path:     target location of the file on workspace.
        :param content:  file-like `io.BinaryIO` of the `path` contents.
        :param format:   By default, `ImportFormat.SOURCE`. If using `ImportFormat.AUTO` the `path`
                         is imported or exported as either a workspace file or a notebook, depending
                         on an analysis of the `item`’s extension and the header content provided in
                         the request. In addition, if the `path` is imported as a notebook, then
                         the `item`’s extension is automatically removed.
        :param language: Only required if using `ExportFormat.SOURCE`.
        