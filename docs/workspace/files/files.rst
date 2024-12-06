``w.files``: Files
==================
.. currentmodule:: databricks.sdk.service.files

.. py:class:: FilesAPI

    The Files API is a standard HTTP API that allows you to read, write, list, and delete files and
    directories by referring to their URI. The API makes working with file content as raw bytes easier and
    more efficient.
    
    The API supports [Unity Catalog volumes], where files and directories to operate on are specified using
    their volume URI path, which follows the format
    /Volumes/&lt;catalog_name&gt;/&lt;schema_name&gt;/&lt;volume_name&gt;/&lt;path_to_file&gt;.
    
    The Files API has two distinct endpoints, one for working with files (`/fs/files`) and another one for
    working with directories (`/fs/directories`). Both endpoints, use the standard HTTP methods GET, HEAD,
    PUT, and DELETE to manage files and directories specified using their URI path. The path is always
    absolute.
    
    [Unity Catalog volumes]: https://docs.databricks.com/en/connect/unity-catalog/volumes.html

    .. py:method:: create_directory(directory_path: str)

        Create a directory.
        
        Creates an empty directory. If necessary, also creates any parent directories of the new, empty
        directory (like the shell command `mkdir -p`). If called on an existing directory, returns a success
        response; this method is idempotent (it will succeed if the directory already exists).
        
        :param directory_path: str
          The absolute path of a directory.
        
        
        

    .. py:method:: delete(file_path: str)

        Delete a file.
        
        Deletes a file. If the request is successful, there is no response body.
        
        :param file_path: str
          The absolute path of the file.
        
        
        

    .. py:method:: delete_directory(directory_path: str)

        Delete a directory.
        
        Deletes an empty directory.
        
        To delete a non-empty directory, first delete all of its contents. This can be done by listing the
        directory contents and deleting each file and subdirectory recursively.
        
        :param directory_path: str
          The absolute path of a directory.
        
        
        

    .. py:method:: download(file_path: str) -> DownloadResponse

        Download a file.
        
        Downloads a file. The file contents are the response body. This is a standard HTTP file download, not
        a JSON RPC. It supports the Range and If-Unmodified-Since HTTP headers.
        
        :param file_path: str
          The absolute path of the file.
        
        :returns: :class:`DownloadResponse`
        

    .. py:method:: get_directory_metadata(directory_path: str)

        Get directory metadata.
        
        Get the metadata of a directory. The response HTTP headers contain the metadata. There is no response
        body.
        
        This method is useful to check if a directory exists and the caller has access to it.
        
        If you wish to ensure the directory exists, you can instead use `PUT`, which will create the directory
        if it does not exist, and is idempotent (it will succeed if the directory already exists).
        
        :param directory_path: str
          The absolute path of a directory.
        
        
        

    .. py:method:: get_metadata(file_path: str) -> GetMetadataResponse

        Get file metadata.
        
        Get the metadata of a file. The response HTTP headers contain the metadata. There is no response body.
        
        :param file_path: str
          The absolute path of the file.
        
        :returns: :class:`GetMetadataResponse`
        

    .. py:method:: list_directory_contents(directory_path: str [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[DirectoryEntry]

        List directory contents.
        
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
        

    .. py:method:: upload(file_path: str, contents: BinaryIO [, overwrite: Optional[bool]])

        Upload a file.
        
        Uploads a file of up to 5 GiB. The file contents should be sent as the request body as raw bytes (an
        octet stream); do not encode or otherwise modify the bytes before sending. The contents of the
        resulting file will be exactly the bytes sent in the request body. If the request is successful, there
        is no response body.
        
        :param file_path: str
          The absolute path of the file.
        :param contents: BinaryIO
        :param overwrite: bool (optional)
          If true, an existing file will be overwritten.
        
        
        