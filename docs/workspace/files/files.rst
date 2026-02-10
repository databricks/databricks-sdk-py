``w.files``: Files
==================
.. currentmodule:: databricks.sdk.service.files

.. py:class:: FilesExt

    The Files API is a standard HTTP API that allows you to read, write, list, and delete files and
    directories by referring to their URI. The API makes working with file content as raw bytes easier and
    more efficient.

    The API supports [Unity Catalog volumes], where files and directories to operate on are specified using
    their volume URI path, which follows the format
    /Volumes/&lt;catalog_name&gt;/&lt;schema_name&gt;/&lt;volume_name&gt;/&lt;path_to_file&gt;.

    The Files API has two distinct endpoints, one for working with files (`/fs/files`) and another one for
    working with directories (`/fs/directories`). Both endpoints use the standard HTTP methods GET, HEAD, PUT,
    and DELETE to manage files and directories specified using their URI path. The path is always absolute.

    Some Files API client features are currently experimental. To enable them, set
    `enable_experimental_files_api_client = True` in your configuration profile or use the environment
    variable `DATABRICKS_ENABLE_EXPERIMENTAL_FILES_API_CLIENT=True`.

    Use of Files API may incur Databricks data transfer charges.

    [Unity Catalog volumes]: https://docs.databricks.com/en/connect/unity-catalog/volumes.html

    .. py:method:: create_directory(directory_path: str)

        Creates an empty directory. If necessary, also creates any parent directories of the new, empty
        directory (like the shell command `mkdir -p`). If called on an existing directory, returns a success
        response; this method is idempotent (it will succeed if the directory already exists).

        :param directory_path: str
          The absolute path of a directory.


        

    .. py:method:: delete(file_path: str)

        Deletes a file. If the request is successful, there is no response body.

        :param file_path: str
          The absolute path of the file.


        

    .. py:method:: delete_directory(directory_path: str)

        Deletes an empty directory.

        To delete a non-empty directory, first delete all of its contents. This can be done by listing the
        directory contents and deleting each file and subdirectory recursively.

        :param directory_path: str
          The absolute path of a directory.


        

    .. py:method:: download(file_path: str) -> DownloadResponse

        Download a file.

        Downloads a file as a stream into memory.

        Use this when you want to process the downloaded file in memory or pipe it into another system. Supports files of any size in SDK v0.72.0+. Earlier versions have a 5 GB file size limit.

        If the download is successful, the function returns the downloaded file result. If the download is unsuccessful, the function raises an exception.

        :param file_path: str
          The remote path of the file, e.g. /Volumes/path/to/your/file

        :returns: :class:`DownloadResponse`
        

    .. py:method:: download_to(file_path: str, destination: str [, overwrite: bool = True, use_parallel: bool = False, parallelism: Optional[int]]) -> DownloadFileResult

        Downloads a file directly to a local file path.

        Use this when you want to write the file straight to disk instead of holding it in memory. Supports files of any size in SDK v0.72.0+. Earlier versions have a 5 GB file size limit.

        Supports parallel download (use_parallel=True), which may improve performance for large files. This is available on all operating systems except Windows.

        :param file_path: str
          The remote path of the file, e.g. /Volumes/path/to/your/file
        :param destination: str
          The local path where the file will be saved.
        :param overwrite: bool
          If true, an existing file will be overwritten. When not specified, defaults to True.
        :param use_parallel: bool
          If true, the download will be performed using multiple threads.
        :param parallelism: int
          The number of parallel threads to use for downloading. If not specified, defaults to the number of CPU cores.

        :returns: :class:`DownloadFileResult`
        

    .. py:method:: get_directory_metadata(directory_path: str)

        Get the metadata of a directory. The response HTTP headers contain the metadata. There is no response
        body.

        This method is useful to check if a directory exists and the caller has access to it.

        If you wish to ensure the directory exists, you can instead use `PUT`, which will create the directory
        if it does not exist, and is idempotent (it will succeed if the directory already exists).

        :param directory_path: str
          The absolute path of a directory.


        

    .. py:method:: get_metadata(file_path: str) -> GetMetadataResponse

        Get the metadata of a file. The response HTTP headers contain the metadata. There is no response body.

        :param file_path: str
          The absolute path of the file.

        :returns: :class:`GetMetadataResponse`
        

    .. py:method:: list_directory_contents(directory_path: str [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[DirectoryEntry]

        Returns the contents of a directory. If there is no directory at the specified path, the API returns a
        HTTP 404 error.

        :param directory_path: str
          The absolute path of a directory.
        :param page_size: int (optional)
          The maximum number of directory entries to return. The response may contain fewer entries. If the
          response contains a `next_page_token`, there may be more entries, even if fewer than `page_size`
          entries are in the response.

          We recommend not to set this value unless you are intentionally listing less than the complete
          directory contents.

          If unspecified, at most 1000 directory entries will be returned. The maximum value is 1000. Values
          above 1000 will be coerced to 1000.
        :param page_token: str (optional)
          An opaque page token which was the `next_page_token` in the response of the previous request to list
          the contents of this directory. Provide this token to retrieve the next page of directory entries.
          When providing a `page_token`, all other parameters provided to the request must match the previous
          request. To list all of the entries in a directory, it is necessary to continue requesting pages of
          entries until the response contains no `next_page_token`. Note that the number of entries returned
          must not be used to determine when the listing is complete.

        :returns: Iterator over :class:`DirectoryEntry`
        

    .. py:method:: upload(file_path: str, contents: BinaryIO [, overwrite: Optional[bool], part_size: Optional[int], use_parallel: bool = True, parallelism: Optional[int]]) -> UploadStreamResult

        
        Uploads a file from memory or a stream interface.

        Use this when you want to upload data already in memory or piped from another system. Supports files of any size in SDK v0.72.0+. Earlier versions have a 5 GB file size limit.

        Limitations: If the storage account is on Azure and has firewall enabled, the maximum file size is 5GB.

        :param file_path: str
            The absolute remote path of the target file, e.g. /Volumes/path/to/your/file
        :param contents: BinaryIO
            The contents of the file to upload. This must be a BinaryIO stream.
        :param overwrite: bool (optional)
            If true, an existing file will be overwritten. When not specified, defaults to True.
        :param part_size: int (optional)
            If set, multipart upload will use the value as its size per uploading part. If not set, an appropriate value will be automatically used.
        :param use_parallel: bool (optional)
            If true, the upload will be performed using multiple threads. Note that this will consume more memory
            because multiple parts will be buffered in memory before being uploaded. The amount of memory used is proportional
            to `parallelism * part_size`.
            If false, the upload will be performed in a single thread.
            Default is True.
        :param parallelism: int (optional)
            The number of threads to use for parallel uploads. This is only used if `use_parallel` is True.

        :returns: :class:`UploadStreamResult`
        

    .. py:method:: upload_from(file_path: str, source_path: str [, overwrite: Optional[bool], part_size: Optional[int], use_parallel: bool = True, parallelism: Optional[int]]) -> UploadFileResult

        
        Uploads a file from a local file path.

        Use this when your data already exists on disk and you want to upload it directly without manually opening it yourself. Supports files of any size in SDK v0.72.0+. Earlier versions have a 5 GB file size limit.

        :param file_path: str
          The absolute remote path of the target file.
        :param source_path: str
          The local path of the file to upload. This must be a path to a local file.
        :param part_size: int (optional)
          If set, multipart upload will use the value as its size per uploading part. If not set, an appropriate default  value will be automatically used.
        :param overwrite: bool (optional)
          If true, an existing file will be overwritten. When not specified, defaults True.
        :param use_parallel: bool (optional)
          If true, the upload will be performed using multiple threads. Default is True.
        :param parallelism: int (optional)
          The number of threads to use for parallel uploads. This is only used if `use_parallel` is True.
          If not specified, the default parallelism will be set to config.multipart_upload_default_parallelism

        :returns: :class:`UploadFileResult`
        