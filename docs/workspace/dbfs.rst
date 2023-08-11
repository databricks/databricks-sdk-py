DBFS
====
.. py:class:: DbfsExt

    DBFS API makes it simple to interact with various data sources without having to include a users
    credentials every time to read a file.

    .. py:method:: add_block(handle, data)

        Append data block.
        
        Appends a block of data to the stream specified by the input handle. If the handle does not exist,
        this call will throw an exception with `RESOURCE_DOES_NOT_EXIST`.
        
        If the block of data exceeds 1 MB, this call will throw an exception with `MAX_BLOCK_SIZE_EXCEEDED`.
        
        :param handle: int
          The handle on an open stream.
        :param data: str
          The base64-encoded data to append to the stream. This has a limit of 1 MB.
        
        
        

    .. py:method:: close(handle)

        Close the stream.
        
        Closes the stream specified by the input handle. If the handle does not exist, this call throws an
        exception with `RESOURCE_DOES_NOT_EXIST`.
        
        :param handle: int
          The handle on an open stream.
        
        
        

    .. py:method:: copy(src, dst [, recursive, overwrite])

        Copy files between DBFS and local filesystems

    .. py:method:: create(path [, overwrite])

        Open a stream.
        
        Opens a stream to write to a file and returns a handle to this stream. There is a 10 minute idle
        timeout on this handle. If a file or directory already exists on the given path and __overwrite__ is
        set to `false`, this call throws an exception with `RESOURCE_ALREADY_EXISTS`.
        
        A typical workflow for file upload would be:
        
        1. Issue a `create` call and get a handle. 2. Issue one or more `add-block` calls with the handle you
        have. 3. Issue a `close` call with the handle you have.
        
        :param path: str
          The path of the new file. The path should be the absolute DBFS path.
        :param overwrite: bool (optional)
          The flag that specifies whether to overwrite existing file/files.
        
        :returns: :class:`CreateResponse`
        

    .. py:method:: delete(path [, recursive])

        Delete a file/directory.
        
        Delete the file or directory (optionally recursively delete all files in the directory). This call
        throws an exception with `IO_ERROR` if the path is a non-empty directory and `recursive` is set to
        `false` or on other similar errors.
        
        When you delete a large number of files, the delete operation is done in increments. The call returns
        a response after approximately 45 seconds with an error message (503 Service Unavailable) asking you
        to re-invoke the delete operation until the directory structure is fully deleted.
        
        For operations that delete more than 10K files, we discourage using the DBFS REST API, but advise you
        to perform such operations in the context of a cluster, using the [File system utility
        (dbutils.fs)](/dev-tools/databricks-utils.html#dbutils-fs). `dbutils.fs` covers the functional scope
        of the DBFS REST API, but from notebooks. Running such operations using notebooks provides better
        control and manageability, such as selective deletes, and the possibility to automate periodic delete
        jobs.
        
        :param path: str
          The path of the file or directory to delete. The path should be the absolute DBFS path.
        :param recursive: bool (optional)
          Whether or not to recursively delete the directory's contents. Deleting empty directories can be
          done without providing the recursive flag.
        
        
        

    .. py:method:: download(path)

        Usage:

        .. code-block::

            import io
            import pathlib
            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            root = pathlib.Path(f'/tmp/{time.time_ns()}')
            
            f = io.BytesIO(b"some text data")
            w.dbfs.upload(f'{root}/01', f)
            
            with w.dbfs.download(f'{root}/01') as f:
                assert f.read() == b"some text data"

        Download file from DBFS

    .. py:method:: exists(path)

        If file exists on DBFS

    .. py:method:: get_status(path)

        Get the information of a file or directory.
        
        Gets the file information for a file or directory. If the file or directory does not exist, this call
        throws an exception with `RESOURCE_DOES_NOT_EXIST`.
        
        :param path: str
          The path of the file or directory. The path should be the absolute DBFS path.
        
        :returns: :class:`FileInfo`
        

    .. py:method:: list(path [, recursive])

        List directory contents or file details.

        List the contents of a directory, or details of the file. If the file or directory does not exist,
        this call throws an exception with `RESOURCE_DOES_NOT_EXIST`.

        When calling list on a large directory, the list operation will time out after approximately 60
        seconds.

        :param recursive: traverse deep into directory tree
        :returns iterator of metadata for every file
        

    .. py:method:: mkdirs(path)

        Create a directory.
        
        Creates the given directory and necessary parent directories if they do not exist. If a file (not a
        directory) exists at any prefix of the input path, this call throws an exception with
        `RESOURCE_ALREADY_EXISTS`. **Note**: If this operation fails, it might have succeeded in creating some
        of the necessary parent directories.
        
        :param path: str
          The path of the new directory. The path should be the absolute DBFS path.
        
        
        

    .. py:method:: move(source_path, destination_path)

        Move a file.
        
        Moves a file from one location to another location within DBFS. If the source file does not exist,
        this call throws an exception with `RESOURCE_DOES_NOT_EXIST`. If a file already exists in the
        destination path, this call throws an exception with `RESOURCE_ALREADY_EXISTS`. If the given source
        path is a directory, this call always recursively moves all files.",
        
        :param source_path: str
          The source path of the file or directory. The path should be the absolute DBFS path.
        :param destination_path: str
          The destination path of the file or directory. The path should be the absolute DBFS path.
        
        
        

    .. py:method:: move_(src, dst [, recursive, overwrite])

        Move files between local and DBFS systems

    .. py:method:: put(path [, contents, overwrite])

        Upload a file.
        
        Uploads a file through the use of multipart form post. It is mainly used for streaming uploads, but
        can also be used as a convenient single call for data upload.
        
        Alternatively you can pass contents as base64 string.
        
        The amount of data that can be passed (when not streaming) using the __contents__ parameter is limited
        to 1 MB. `MAX_BLOCK_SIZE_EXCEEDED` will be thrown if this limit is exceeded.
        
        If you want to upload large files, use the streaming upload. For details, see :method:dbfs/create,
        :method:dbfs/addBlock, :method:dbfs/close.
        
        :param path: str
          The path of the new file. The path should be the absolute DBFS path.
        :param contents: str (optional)
          This parameter might be absent, and instead a posted file will be used.
        :param overwrite: bool (optional)
          The flag that specifies whether to overwrite existing file/files.
        
        
        

    .. py:method:: read(path [, length, offset])

        Get the contents of a file.
        
        Returns the contents of a file. If the file does not exist, this call throws an exception with
        `RESOURCE_DOES_NOT_EXIST`. If the path is a directory, the read length is negative, or if the offset
        is negative, this call throws an exception with `INVALID_PARAMETER_VALUE`. If the read length exceeds
        1 MB, this call throws an exception with `MAX_READ_SIZE_EXCEEDED`.
        
        If `offset + length` exceeds the number of bytes in a file, it reads the contents until the end of
        file.",
        
        :param path: str
          The path of the file to read. The path should be the absolute DBFS path.
        :param length: int (optional)
          The number of bytes to read starting from the offset. This has a limit of 1 MB, and a default value
          of 0.5 MB.
        :param offset: int (optional)
          The offset to read from in bytes.
        
        :returns: :class:`ReadResponse`
        

    .. py:method:: upload(path, src [, overwrite])

        Upload file to DBFS