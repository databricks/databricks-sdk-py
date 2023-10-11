# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

import logging
from dataclasses import dataclass
from typing import BinaryIO, Dict, Iterator, List, Optional

from ._internal import _repeated

_LOG = logging.getLogger('databricks.sdk')

# all definitions in this file are in alphabetical order


@dataclass
class AddBlock:
    handle: int
    data: str

    def as_dict(self) -> dict:
        body = {}
        if self.data is not None: body['data'] = self.data
        if self.handle is not None: body['handle'] = self.handle
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'AddBlock':
        return cls(data=d.get('data', None), handle=d.get('handle', None))


@dataclass
class Close:
    handle: int

    def as_dict(self) -> dict:
        body = {}
        if self.handle is not None: body['handle'] = self.handle
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Close':
        return cls(handle=d.get('handle', None))


@dataclass
class Create:
    path: str
    overwrite: Optional[bool] = None

    def as_dict(self) -> dict:
        body = {}
        if self.overwrite is not None: body['overwrite'] = self.overwrite
        if self.path is not None: body['path'] = self.path
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Create':
        return cls(overwrite=d.get('overwrite', None), path=d.get('path', None))


@dataclass
class CreateResponse:
    handle: Optional[int] = None

    def as_dict(self) -> dict:
        body = {}
        if self.handle is not None: body['handle'] = self.handle
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateResponse':
        return cls(handle=d.get('handle', None))


@dataclass
class Delete:
    path: str
    recursive: Optional[bool] = None

    def as_dict(self) -> dict:
        body = {}
        if self.path is not None: body['path'] = self.path
        if self.recursive is not None: body['recursive'] = self.recursive
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Delete':
        return cls(path=d.get('path', None), recursive=d.get('recursive', None))


@dataclass
class DownloadResponse:
    contents: Optional[BinaryIO] = None


@dataclass
class FileInfo:
    file_size: Optional[int] = None
    is_dir: Optional[bool] = None
    modification_time: Optional[int] = None
    path: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.file_size is not None: body['file_size'] = self.file_size
        if self.is_dir is not None: body['is_dir'] = self.is_dir
        if self.modification_time is not None: body['modification_time'] = self.modification_time
        if self.path is not None: body['path'] = self.path
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'FileInfo':
        return cls(file_size=d.get('file_size', None),
                   is_dir=d.get('is_dir', None),
                   modification_time=d.get('modification_time', None),
                   path=d.get('path', None))


@dataclass
class ListStatusResponse:
    files: Optional['List[FileInfo]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.files: body['files'] = [v.as_dict() for v in self.files]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListStatusResponse':
        return cls(files=_repeated(d, 'files', FileInfo))


@dataclass
class MkDirs:
    path: str

    def as_dict(self) -> dict:
        body = {}
        if self.path is not None: body['path'] = self.path
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'MkDirs':
        return cls(path=d.get('path', None))


@dataclass
class Move:
    source_path: str
    destination_path: str

    def as_dict(self) -> dict:
        body = {}
        if self.destination_path is not None: body['destination_path'] = self.destination_path
        if self.source_path is not None: body['source_path'] = self.source_path
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Move':
        return cls(destination_path=d.get('destination_path', None), source_path=d.get('source_path', None))


@dataclass
class Put:
    path: str
    contents: Optional[str] = None
    overwrite: Optional[bool] = None

    def as_dict(self) -> dict:
        body = {}
        if self.contents is not None: body['contents'] = self.contents
        if self.overwrite is not None: body['overwrite'] = self.overwrite
        if self.path is not None: body['path'] = self.path
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Put':
        return cls(contents=d.get('contents', None),
                   overwrite=d.get('overwrite', None),
                   path=d.get('path', None))


@dataclass
class ReadResponse:
    bytes_read: Optional[int] = None
    data: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.bytes_read is not None: body['bytes_read'] = self.bytes_read
        if self.data is not None: body['data'] = self.data
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ReadResponse':
        return cls(bytes_read=d.get('bytes_read', None), data=d.get('data', None))


class DbfsAPI:
    """DBFS API makes it simple to interact with various data sources without having to include a users
    credentials every time to read a file."""

    def __init__(self, api_client):
        self._api = api_client

    def add_block(self, handle: int, data: str):
        """Append data block.
        
        Appends a block of data to the stream specified by the input handle. If the handle does not exist,
        this call will throw an exception with `RESOURCE_DOES_NOT_EXIST`.
        
        If the block of data exceeds 1 MB, this call will throw an exception with `MAX_BLOCK_SIZE_EXCEEDED`.
        
        :param handle: int
          The handle on an open stream.
        :param data: str
          The base64-encoded data to append to the stream. This has a limit of 1 MB.
        
        
        """
        body = {}
        if data is not None: body['data'] = data
        if handle is not None: body['handle'] = handle
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        self._api.do('POST', '/api/2.0/dbfs/add-block', body=body, headers=headers)

    def close(self, handle: int):
        """Close the stream.
        
        Closes the stream specified by the input handle. If the handle does not exist, this call throws an
        exception with `RESOURCE_DOES_NOT_EXIST`.
        
        :param handle: int
          The handle on an open stream.
        
        
        """
        body = {}
        if handle is not None: body['handle'] = handle
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        self._api.do('POST', '/api/2.0/dbfs/close', body=body, headers=headers)

    def create(self, path: str, *, overwrite: Optional[bool] = None) -> CreateResponse:
        """Open a stream.
        
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
        """
        body = {}
        if overwrite is not None: body['overwrite'] = overwrite
        if path is not None: body['path'] = path
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        res = self._api.do('POST', '/api/2.0/dbfs/create', body=body, headers=headers)
        return CreateResponse.from_dict(res)

    def delete(self, path: str, *, recursive: Optional[bool] = None):
        """Delete a file/directory.
        
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
        
        
        """
        body = {}
        if path is not None: body['path'] = path
        if recursive is not None: body['recursive'] = recursive
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        self._api.do('POST', '/api/2.0/dbfs/delete', body=body, headers=headers)

    def get_status(self, path: str) -> FileInfo:
        """Get the information of a file or directory.
        
        Gets the file information for a file or directory. If the file or directory does not exist, this call
        throws an exception with `RESOURCE_DOES_NOT_EXIST`.
        
        :param path: str
          The path of the file or directory. The path should be the absolute DBFS path.
        
        :returns: :class:`FileInfo`
        """

        query = {}
        if path is not None: query['path'] = path
        headers = {'Accept': 'application/json', }
        res = self._api.do('GET', '/api/2.0/dbfs/get-status', query=query, headers=headers)
        return FileInfo.from_dict(res)

    def list(self, path: str) -> Iterator['FileInfo']:
        """List directory contents or file details.
        
        List the contents of a directory, or details of the file. If the file or directory does not exist,
        this call throws an exception with `RESOURCE_DOES_NOT_EXIST`.
        
        When calling list on a large directory, the list operation will time out after approximately 60
        seconds. We strongly recommend using list only on directories containing less than 10K files and
        discourage using the DBFS REST API for operations that list more than 10K files. Instead, we recommend
        that you perform such operations in the context of a cluster, using the [File system utility
        (dbutils.fs)](/dev-tools/databricks-utils.html#dbutils-fs), which provides the same functionality
        without timing out.
        
        :param path: str
          The path of the file or directory. The path should be the absolute DBFS path.
        
        :returns: Iterator over :class:`FileInfo`
        """

        query = {}
        if path is not None: query['path'] = path
        headers = {'Accept': 'application/json', }
        json = self._api.do('GET', '/api/2.0/dbfs/list', query=query, headers=headers)
        parsed = ListStatusResponse.from_dict(json).files
        return parsed if parsed is not None else []

    def mkdirs(self, path: str):
        """Create a directory.
        
        Creates the given directory and necessary parent directories if they do not exist. If a file (not a
        directory) exists at any prefix of the input path, this call throws an exception with
        `RESOURCE_ALREADY_EXISTS`. **Note**: If this operation fails, it might have succeeded in creating some
        of the necessary parent directories.
        
        :param path: str
          The path of the new directory. The path should be the absolute DBFS path.
        
        
        """
        body = {}
        if path is not None: body['path'] = path
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        self._api.do('POST', '/api/2.0/dbfs/mkdirs', body=body, headers=headers)

    def move(self, source_path: str, destination_path: str):
        """Move a file.
        
        Moves a file from one location to another location within DBFS. If the source file does not exist,
        this call throws an exception with `RESOURCE_DOES_NOT_EXIST`. If a file already exists in the
        destination path, this call throws an exception with `RESOURCE_ALREADY_EXISTS`. If the given source
        path is a directory, this call always recursively moves all files.",
        
        :param source_path: str
          The source path of the file or directory. The path should be the absolute DBFS path.
        :param destination_path: str
          The destination path of the file or directory. The path should be the absolute DBFS path.
        
        
        """
        body = {}
        if destination_path is not None: body['destination_path'] = destination_path
        if source_path is not None: body['source_path'] = source_path
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        self._api.do('POST', '/api/2.0/dbfs/move', body=body, headers=headers)

    def put(self, path: str, *, contents: Optional[str] = None, overwrite: Optional[bool] = None):
        """Upload a file.
        
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
        
        
        """
        body = {}
        if contents is not None: body['contents'] = contents
        if overwrite is not None: body['overwrite'] = overwrite
        if path is not None: body['path'] = path
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        self._api.do('POST', '/api/2.0/dbfs/put', body=body, headers=headers)

    def read(self, path: str, *, length: Optional[int] = None, offset: Optional[int] = None) -> ReadResponse:
        """Get the contents of a file.
        
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
        """

        query = {}
        if length is not None: query['length'] = length
        if offset is not None: query['offset'] = offset
        if path is not None: query['path'] = path
        headers = {'Accept': 'application/json', }
        res = self._api.do('GET', '/api/2.0/dbfs/read', query=query, headers=headers)
        return ReadResponse.from_dict(res)


class FilesAPI:
    """The Files API allows you to read, write, and delete files and directories in Unity Catalog volumes."""

    def __init__(self, api_client):
        self._api = api_client

    def delete(self, file_path: str):
        """Delete a file or directory.
        
        Deletes a file or directory.
        
        :param file_path: str
          The absolute path of the file or directory in DBFS.
        
        
        """

        headers = {}
        self._api.do('DELETE', f'/api/2.0/fs/files/{file_path}', headers=headers)

    def download(self, file_path: str) -> DownloadResponse:
        """Download a file.
        
        Downloads a file of up to 2 GiB.
        
        :param file_path: str
          The absolute path of the file or directory in DBFS.
        
        :returns: :class:`DownloadResponse`
        """

        headers = {'Accept': 'application/octet-stream', }
        res = self._api.do('GET', f'/api/2.0/fs/files/{file_path}', headers=headers, raw=True)
        return DownloadResponse(contents=res)

    def get_status(self, path: str) -> FileInfo:
        """Get file or directory status.
        
        Returns the status of a file or directory.
        
        :param path: str
          The absolute path of the file or directory in the Files API, omitting the initial slash.
        
        :returns: :class:`FileInfo`
        """

        query = {}
        if path is not None: query['path'] = path
        headers = {'Accept': 'application/json', }
        res = self._api.do('GET', '/api/2.0/fs/get-status', query=query, headers=headers)
        return FileInfo.from_dict(res)

    def upload(self, file_path: str, contents: BinaryIO, *, overwrite: Optional[bool] = None):
        """Upload a file.
        
        Uploads a file of up to 2 GiB.
        
        :param file_path: str
          The absolute path of the file or directory in DBFS.
        :param contents: BinaryIO
        :param overwrite: bool (optional)
          If true, an existing file will be overwritten.
        
        
        """

        query = {}
        if overwrite is not None: query['overwrite'] = overwrite
        headers = {'Content-Type': 'application/octet-stream', }
        self._api.do('PUT', f'/api/2.0/fs/files/{file_path}', query=query, headers=headers, data=contents)
