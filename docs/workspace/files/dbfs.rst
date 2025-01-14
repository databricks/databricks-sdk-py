``w.dbfs``: DBFS
================
.. currentmodule:: databricks.sdk.service.files

.. py:class:: DbfsExt

    DBFS API makes it simple to interact with various data sources without having to include a users
    credentials every time to read a file.

    .. py:method:: add_block(handle: int, data: str)

        Append data block.
        
        Appends a block of data to the stream specified by the input handle. If the handle does not exist,
        this call will throw an exception with ``RESOURCE_DOES_NOT_EXIST``.
        
        If the block of data exceeds 1 MB, this call will throw an exception with ``MAX_BLOCK_SIZE_EXCEEDED``.
        
        :param handle: int
          The handle on an open stream.
        :param data: str
          The base64-encoded data to append to the stream. This has a limit of 1 MB.
        



    .. py:method:: close(handle: int)

        Close the stream.
        
        Closes the stream specified by the input handle. If the handle does not exist, this call throws an
        exception with ``RESOURCE_DOES_NOT_EXIST``.
        
        :param handle: int
          The handle on an open stream.
        



    .. py:method:: copy(src: str, dst: str [, recursive: bool = False, overwrite: bool = False])

        Copy files between DBFS and local filesystems

    .. py:method:: create(path: str [, overwrite: Optional[bool]]) -> CreateResponse

        Open a stream.
        
        Opens a stream to write to a file and returns a handle to this stream. There is a 10 minute idle
        timeout on this handle. If a file or directory already exists on the given path and __overwrite__ is
        set to false, this call will throw an exception with ``RESOURCE_ALREADY_EXISTS``.
        
        A typical workflow for file upload would be:
        
        1. Issue a ``create`` call and get a handle. 2. Issue one or more ``add-block`` calls with the handle
        you have. 3. Issue a ``close`` call with the handle you have.
        
        :param path: str
          The path of the new file. The path should be the absolute DBFS path.
        :param overwrite: bool (optional)
          The flag that specifies whether to overwrite existing file/files.
        
        :returns: :class:`CreateResponse`


    .. py:method:: delete(path: str [, recursive: bool = False])

        Delete file or directory on DBFS

    .. py:method:: download(path: str) -> BinaryIO


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

    .. py:method:: exists(path: str) -> bool

        If file exists on DBFS

    .. py:method:: get_status(path: str) -> FileInfo

        Get the information of a file or directory.
        
        Gets the file information for a file or directory. If the file or directory does not exist, this call
        throws an exception with `RESOURCE_DOES_NOT_EXIST`.
        
        :param path: str
          The path of the file or directory. The path should be the absolute DBFS path.
        
        :returns: :class:`FileInfo`


    .. py:method:: list(path: str [, recursive: bool = False]) -> Iterator[files.FileInfo]

        List directory contents or file details.
        
        List the contents of a directory, or details of the file. If the file or directory does not exist,
        this call throws an exception with `RESOURCE_DOES_NOT_EXIST`.
        
        When calling list on a large directory, the list operation will time out after approximately 60
        seconds.
        
        :param path: the DBFS or UC Volume path to list
        :param recursive: traverse deep into directory tree
        :returns iterator of metadata for every file


    .. py:method:: mkdirs(path: str)

        Create directory on DBFS

    .. py:method:: move(source_path: str, destination_path: str)

        Move a file.
        
        Moves a file from one location to another location within DBFS. If the source file does not exist,
        this call throws an exception with `RESOURCE_DOES_NOT_EXIST`. If a file already exists in the
        destination path, this call throws an exception with `RESOURCE_ALREADY_EXISTS`. If the given source
        path is a directory, this call always recursively moves all files.
        
        :param source_path: str
          The source path of the file or directory. The path should be the absolute DBFS path.
        :param destination_path: str
          The destination path of the file or directory. The path should be the absolute DBFS path.
        



    .. py:method:: move_(src: str, dst: str [, recursive: bool = False, overwrite: bool = False])

        Move files between local and DBFS systems

    .. py:method:: open(path: str [, read: bool = False, write: bool = False, overwrite: bool = False]) -> BinaryIO


    .. py:method:: put(path: str [, contents: Optional[str], overwrite: Optional[bool]])

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
        



    .. py:method:: read(path: str [, length: Optional[int], offset: Optional[int]]) -> ReadResponse

        Get the contents of a file.
        
        Returns the contents of a file. If the file does not exist, this call throws an exception with
        `RESOURCE_DOES_NOT_EXIST`. If the path is a directory, the read length is negative, or if the offset
        is negative, this call throws an exception with `INVALID_PARAMETER_VALUE`. If the read length exceeds
        1 MB, this call throws an exception with `MAX_READ_SIZE_EXCEEDED`.
        
        If `offset + length` exceeds the number of bytes in a file, it reads the contents until the end of
        file.
        
        :param path: str
          The path of the file to read. The path should be the absolute DBFS path.
        :param length: int (optional)
          The number of bytes to read starting from the offset. This has a limit of 1 MB, and a default value
          of 0.5 MB.
        :param offset: int (optional)
          The offset to read from in bytes.
        
        :returns: :class:`ReadResponse`


    .. py:method:: upload(path: str, src: BinaryIO [, overwrite: bool = False])

        Upload file to DBFS