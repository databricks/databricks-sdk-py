# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

import logging
from dataclasses import dataclass
from typing import Dict, Iterator, List

from ._internal import _repeated

_LOG = logging.getLogger('databricks.sdk')

# all definitions in this file are in alphabetical order


@dataclass
class AddBlock:
    handle: int
    data: str

    def as_dict(self) -> dict:
        body = {}
        if self.data: body['data'] = self.data
        if self.handle: body['handle'] = self.handle
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'AddBlock':
        return cls(data=d.get('data', None), handle=d.get('handle', None))


@dataclass
class Close:
    handle: int

    def as_dict(self) -> dict:
        body = {}
        if self.handle: body['handle'] = self.handle
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Close':
        return cls(handle=d.get('handle', None))


@dataclass
class Create:
    path: str
    overwrite: bool = None

    def as_dict(self) -> dict:
        body = {}
        if self.overwrite: body['overwrite'] = self.overwrite
        if self.path: body['path'] = self.path
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Create':
        return cls(overwrite=d.get('overwrite', None), path=d.get('path', None))


@dataclass
class CreateResponse:
    handle: int = None

    def as_dict(self) -> dict:
        body = {}
        if self.handle: body['handle'] = self.handle
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateResponse':
        return cls(handle=d.get('handle', None))


@dataclass
class Delete:
    path: str
    recursive: bool = None

    def as_dict(self) -> dict:
        body = {}
        if self.path: body['path'] = self.path
        if self.recursive: body['recursive'] = self.recursive
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Delete':
        return cls(path=d.get('path', None), recursive=d.get('recursive', None))


@dataclass
class FileInfo:
    file_size: int = None
    is_dir: bool = None
    modification_time: int = None
    path: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.file_size: body['file_size'] = self.file_size
        if self.is_dir: body['is_dir'] = self.is_dir
        if self.modification_time: body['modification_time'] = self.modification_time
        if self.path: body['path'] = self.path
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'FileInfo':
        return cls(file_size=d.get('file_size', None),
                   is_dir=d.get('is_dir', None),
                   modification_time=d.get('modification_time', None),
                   path=d.get('path', None))


@dataclass
class GetStatus:
    """Get the information of a file or directory"""

    path: str


@dataclass
class ListRequest:
    """List directory contents or file details"""

    path: str


@dataclass
class ListStatusResponse:
    files: 'List[FileInfo]' = None

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
        if self.path: body['path'] = self.path
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
        if self.destination_path: body['destination_path'] = self.destination_path
        if self.source_path: body['source_path'] = self.source_path
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Move':
        return cls(destination_path=d.get('destination_path', None), source_path=d.get('source_path', None))


@dataclass
class Put:
    path: str
    contents: str = None
    overwrite: bool = None

    def as_dict(self) -> dict:
        body = {}
        if self.contents: body['contents'] = self.contents
        if self.overwrite: body['overwrite'] = self.overwrite
        if self.path: body['path'] = self.path
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Put':
        return cls(contents=d.get('contents', None),
                   overwrite=d.get('overwrite', None),
                   path=d.get('path', None))


@dataclass
class Read:
    """Get the contents of a file"""

    path: str
    length: int = None
    offset: int = None


@dataclass
class ReadResponse:
    bytes_read: int = None
    data: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.bytes_read: body['bytes_read'] = self.bytes_read
        if self.data: body['data'] = self.data
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ReadResponse':
        return cls(bytes_read=d.get('bytes_read', None), data=d.get('data', None))


class DbfsAPI:
    """DBFS API makes it simple to interact with various data sources without having to include a users
    credentials every time to read a file."""

    def __init__(self, api_client):
        self._api = api_client

    def add_block(self, handle: int, data: str, **kwargs):
        """Append data block.
        
        Appends a block of data to the stream specified by the input handle. If the handle does not exist,
        this call will throw an exception with `RESOURCE_DOES_NOT_EXIST`.
        
        If the block of data exceeds 1 MB, this call will throw an exception with `MAX_BLOCK_SIZE_EXCEEDED`."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = AddBlock(data=data, handle=handle)
        body = request.as_dict()
        self._api.do('POST', '/api/2.0/dbfs/add-block', body=body)

    def close(self, handle: int, **kwargs):
        """Close the stream.
        
        Closes the stream specified by the input handle. If the handle does not exist, this call throws an
        exception with `RESOURCE_DOES_NOT_EXIST`."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = Close(handle=handle)
        body = request.as_dict()
        self._api.do('POST', '/api/2.0/dbfs/close', body=body)

    def create(self, path: str, *, overwrite: bool = None, **kwargs) -> CreateResponse:
        """Open a stream.
        
        "Opens a stream to write to a file and returns a handle to this stream. There is a 10 minute idle
        timeout on this handle. If a file or directory already exists on the given path and __overwrite__ is
        set to `false`, this call throws an exception with `RESOURCE_ALREADY_EXISTS`.
        
        A typical workflow for file upload would be:
        
        1. Issue a `create` call and get a handle. 2. Issue one or more `add-block` calls with the handle you
        have. 3. Issue a `close` call with the handle you have."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = Create(overwrite=overwrite, path=path)
        body = request.as_dict()

        json = self._api.do('POST', '/api/2.0/dbfs/create', body=body)
        return CreateResponse.from_dict(json)

    def delete(self, path: str, *, recursive: bool = None, **kwargs):
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
        jobs."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = Delete(path=path, recursive=recursive)
        body = request.as_dict()
        self._api.do('POST', '/api/2.0/dbfs/delete', body=body)

    def get_status(self, path: str, **kwargs) -> FileInfo:
        """Get the information of a file or directory.
        
        Gets the file information for a file or directory. If the file or directory does not exist, this call
        throws an exception with `RESOURCE_DOES_NOT_EXIST`."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GetStatus(path=path)

        query = {}
        if path: query['path'] = request.path

        json = self._api.do('GET', '/api/2.0/dbfs/get-status', query=query)
        return FileInfo.from_dict(json)

    def list(self, path: str, **kwargs) -> Iterator[FileInfo]:
        """List directory contents or file details.
        
        List the contents of a directory, or details of the file. If the file or directory does not exist,
        this call throws an exception with `RESOURCE_DOES_NOT_EXIST`.
        
        When calling list on a large directory, the list operation will time out after approximately 60
        seconds. We strongly recommend using list only on directories containing less than 10K files and
        discourage using the DBFS REST API for operations that list more than 10K files. Instead, we recommend
        that you perform such operations in the context of a cluster, using the [File system utility
        (dbutils.fs)](/dev-tools/databricks-utils.html#dbutils-fs), which provides the same functionality
        without timing out."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = ListRequest(path=path)

        query = {}
        if path: query['path'] = request.path

        json = self._api.do('GET', '/api/2.0/dbfs/list', query=query)
        return [FileInfo.from_dict(v) for v in json.get('files', [])]

    def mkdirs(self, path: str, **kwargs):
        """Create a directory.
        
        Creates the given directory and necessary parent directories if they do not exist. If a file (not a
        directory) exists at any prefix of the input path, this call throws an exception with
        `RESOURCE_ALREADY_EXISTS`. **Note**: If this operation fails, it might have succeeded in creating some
        of the necessary parent directories."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = MkDirs(path=path)
        body = request.as_dict()
        self._api.do('POST', '/api/2.0/dbfs/mkdirs', body=body)

    def move(self, source_path: str, destination_path: str, **kwargs):
        """Move a file.
        
        Moves a file from one location to another location within DBFS. If the source file does not exist,
        this call throws an exception with `RESOURCE_DOES_NOT_EXIST`. If a file already exists in the
        destination path, this call throws an exception with `RESOURCE_ALREADY_EXISTS`. If the given source
        path is a directory, this call always recursively moves all files.","""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = Move(destination_path=destination_path, source_path=source_path)
        body = request.as_dict()
        self._api.do('POST', '/api/2.0/dbfs/move', body=body)

    def put(self, path: str, *, contents: str = None, overwrite: bool = None, **kwargs):
        """Upload a file.
        
        Uploads a file through the use of multipart form post. It is mainly used for streaming uploads, but
        can also be used as a convenient single call for data upload.
        
        Alternatively you can pass contents as base64 string.
        
        The amount of data that can be passed (when not streaming) using the __contents__ parameter is limited
        to 1 MB. `MAX_BLOCK_SIZE_EXCEEDED` will be thrown if this limit is exceeded.
        
        If you want to upload large files, use the streaming upload. For details, see :method:dbfs/create,
        :method:dbfs/addBlock, :method:dbfs/close."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = Put(contents=contents, overwrite=overwrite, path=path)
        body = request.as_dict()
        self._api.do('POST', '/api/2.0/dbfs/put', body=body)

    def read(self, path: str, *, length: int = None, offset: int = None, **kwargs) -> ReadResponse:
        """Get the contents of a file.
        
        "Returns the contents of a file. If the file does not exist, this call throws an exception with
        `RESOURCE_DOES_NOT_EXIST`. If the path is a directory, the read length is negative, or if the offset
        is negative, this call throws an exception with `INVALID_PARAMETER_VALUE`. If the read length exceeds
        1 MB, this call throws an exception with `MAX_READ_SIZE_EXCEEDED`.
        
        If `offset + length` exceeds the number of bytes in a file, it reads the contents until the end of
        file.","""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = Read(length=length, offset=offset, path=path)

        query = {}
        if length: query['length'] = request.length
        if offset: query['offset'] = request.offset
        if path: query['path'] = request.path

        json = self._api.do('GET', '/api/2.0/dbfs/read', query=query)
        return ReadResponse.from_dict(json)
