# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

from dataclasses import dataclass
from enum import Enum
from typing import Optional, Dict, List, Any


# all definitions in this file are in alphabetical order


@dataclass
class AddBlock:

    # The base64-encoded data to append to the stream. This has a limit of 1 MB.
    data: str
    # The handle on an open stream.
    handle: int

    def as_request(self) -> (dict, dict):
        addBlock_query, addBlock_body = {}, {}
        if self.data:
            addBlock_body["data"] = self.data
        if self.handle:
            addBlock_body["handle"] = self.handle

        return addBlock_query, addBlock_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "AddBlock":
        return cls(
            data=d.get("data", None),
            handle=d.get("handle", None),
        )


@dataclass
class Close:

    # The handle on an open stream.
    handle: int

    def as_request(self) -> (dict, dict):
        close_query, close_body = {}, {}
        if self.handle:
            close_body["handle"] = self.handle

        return close_query, close_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "Close":
        return cls(
            handle=d.get("handle", None),
        )


@dataclass
class Create:

    # The flag that specifies whether to overwrite existing file/files.
    overwrite: bool
    # The path of the new file. The path should be the absolute DBFS path.
    path: str

    def as_request(self) -> (dict, dict):
        create_query, create_body = {}, {}
        if self.overwrite:
            create_body["overwrite"] = self.overwrite
        if self.path:
            create_body["path"] = self.path

        return create_query, create_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "Create":
        return cls(
            overwrite=d.get("overwrite", None),
            path=d.get("path", None),
        )


@dataclass
class CreateResponse:

    # Handle which should subsequently be passed into the AddBlock and Close
    # calls when writing to a file through a stream.
    handle: int

    def as_request(self) -> (dict, dict):
        createResponse_query, createResponse_body = {}, {}
        if self.handle:
            createResponse_body["handle"] = self.handle

        return createResponse_query, createResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "CreateResponse":
        return cls(
            handle=d.get("handle", None),
        )


@dataclass
class Delete:

    # The path of the file or directory to delete. The path should be the
    # absolute DBFS path.
    path: str
    # Whether or not to recursively delete the directory's contents. Deleting
    # empty directories can be done without providing the recursive flag.
    recursive: bool

    def as_request(self) -> (dict, dict):
        delete_query, delete_body = {}, {}
        if self.path:
            delete_body["path"] = self.path
        if self.recursive:
            delete_body["recursive"] = self.recursive

        return delete_query, delete_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "Delete":
        return cls(
            path=d.get("path", None),
            recursive=d.get("recursive", None),
        )


@dataclass
class FileInfo:

    # The length of the file in bytes or zero if the path is a directory.
    file_size: int
    # True if the path is a directory.
    is_dir: bool
    # Last modification time of given file/dir in milliseconds since Epoch.
    modification_time: int
    # The path of the file or directory.
    path: str

    def as_request(self) -> (dict, dict):
        fileInfo_query, fileInfo_body = {}, {}
        if self.file_size:
            fileInfo_body["file_size"] = self.file_size
        if self.is_dir:
            fileInfo_body["is_dir"] = self.is_dir
        if self.modification_time:
            fileInfo_body["modification_time"] = self.modification_time
        if self.path:
            fileInfo_body["path"] = self.path

        return fileInfo_query, fileInfo_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "FileInfo":
        return cls(
            file_size=d.get("file_size", None),
            is_dir=d.get("is_dir", None),
            modification_time=d.get("modification_time", None),
            path=d.get("path", None),
        )


@dataclass
class GetStatus:
    """Get the information of a file or directory"""

    # The path of the file or directory. The path should be the absolute DBFS
    # path.
    path: str  # query

    def as_request(self) -> (dict, dict):
        getStatus_query, getStatus_body = {}, {}
        if self.path:
            getStatus_query["path"] = self.path

        return getStatus_query, getStatus_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "GetStatus":
        return cls(
            path=d.get("path", None),
        )


@dataclass
class List:
    """List directory contents or file details"""

    # The path of the file or directory. The path should be the absolute DBFS
    # path.
    path: str  # query

    def as_request(self) -> (dict, dict):
        list_query, list_body = {}, {}
        if self.path:
            list_query["path"] = self.path

        return list_query, list_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "List":
        return cls(
            path=d.get("path", None),
        )


@dataclass
class ListStatusResponse:

    # A list of FileInfo's that describe contents of directory or file. See
    # example above.
    files: "List[FileInfo]"

    def as_request(self) -> (dict, dict):
        listStatusResponse_query, listStatusResponse_body = {}, {}
        if self.files:
            listStatusResponse_body["files"] = [v.as_request()[1] for v in self.files]

        return listStatusResponse_query, listStatusResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ListStatusResponse":
        return cls(
            files=[FileInfo.from_dict(v) for v in d["files"]] if "files" in d else None,
        )


@dataclass
class MkDirs:

    # The path of the new directory. The path should be the absolute DBFS path.
    path: str

    def as_request(self) -> (dict, dict):
        mkDirs_query, mkDirs_body = {}, {}
        if self.path:
            mkDirs_body["path"] = self.path

        return mkDirs_query, mkDirs_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "MkDirs":
        return cls(
            path=d.get("path", None),
        )


@dataclass
class Move:

    # The destination path of the file or directory. The path should be the
    # absolute DBFS path.
    destination_path: str
    # The source path of the file or directory. The path should be the absolute
    # DBFS path.
    source_path: str

    def as_request(self) -> (dict, dict):
        move_query, move_body = {}, {}
        if self.destination_path:
            move_body["destination_path"] = self.destination_path
        if self.source_path:
            move_body["source_path"] = self.source_path

        return move_query, move_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "Move":
        return cls(
            destination_path=d.get("destination_path", None),
            source_path=d.get("source_path", None),
        )


@dataclass
class Put:

    # This parameter might be absent, and instead a posted file will be used.
    contents: str
    # The flag that specifies whether to overwrite existing file/files.
    overwrite: bool
    # The path of the new file. The path should be the absolute DBFS path.
    path: str

    def as_request(self) -> (dict, dict):
        put_query, put_body = {}, {}
        if self.contents:
            put_body["contents"] = self.contents
        if self.overwrite:
            put_body["overwrite"] = self.overwrite
        if self.path:
            put_body["path"] = self.path

        return put_query, put_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "Put":
        return cls(
            contents=d.get("contents", None),
            overwrite=d.get("overwrite", None),
            path=d.get("path", None),
        )


@dataclass
class Read:
    """Get the contents of a file"""

    # The number of bytes to read starting from the offset. This has a limit of
    # 1 MB, and a default value of 0.5 MB.
    length: int  # query
    # The offset to read from in bytes.
    offset: int  # query
    # The path of the file to read. The path should be the absolute DBFS path.
    path: str  # query

    def as_request(self) -> (dict, dict):
        read_query, read_body = {}, {}
        if self.length:
            read_query["length"] = self.length
        if self.offset:
            read_query["offset"] = self.offset
        if self.path:
            read_query["path"] = self.path

        return read_query, read_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "Read":
        return cls(
            length=d.get("length", None),
            offset=d.get("offset", None),
            path=d.get("path", None),
        )


@dataclass
class ReadResponse:

    # The number of bytes read (could be less than `length` if we hit end of
    # file). This refers to number of bytes read in unencoded version (response
    # data is base64-encoded).
    bytes_read: int
    # The base64-encoded contents of the file read.
    data: str

    def as_request(self) -> (dict, dict):
        readResponse_query, readResponse_body = {}, {}
        if self.bytes_read:
            readResponse_body["bytes_read"] = self.bytes_read
        if self.data:
            readResponse_body["data"] = self.data

        return readResponse_query, readResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ReadResponse":
        return cls(
            bytes_read=d.get("bytes_read", None),
            data=d.get("data", None),
        )


class DbfsAPI:
    def __init__(self, api_client):
        self._api = api_client

    def add_block(self, request: AddBlock):
        """Append data block.

        Appends a block of data to the stream specified by the input handle. If
        the handle does not exist, this call will throw an exception with
        `RESOURCE_DOES_NOT_EXIST`.

        If the block of data exceeds 1 MB, this call will throw an exception
        with `MAX_BLOCK_SIZE_EXCEEDED`."""
        query, body = request.as_request()
        self._api.do("POST", "/api/2.0/dbfs/add-block", query=query, body=body)

    def close(self, request: Close):
        """Close the stream.

        Closes the stream specified by the input handle. If the handle does not
        exist, this call throws an exception with `RESOURCE_DOES_NOT_EXIST`."""
        query, body = request.as_request()
        self._api.do("POST", "/api/2.0/dbfs/close", query=query, body=body)

    def create(self, request: Create) -> CreateResponse:
        """Open a stream.

        "Opens a stream to write to a file and returns a handle to this stream.
        There is a 10 minute idle timeout on this handle. If a file or directory
        already exists on the given path and __overwrite__ is set to `false`,
        this call throws an exception with `RESOURCE_ALREADY_EXISTS`.

        A typical workflow for file upload would be:

        1. Issue a `create` call and get a handle. 2. Issue one or more
        `add-block` calls with the handle you have. 3. Issue a `close` call with
        the handle you have."""
        query, body = request.as_request()
        json = self._api.do("POST", "/api/2.0/dbfs/create", query=query, body=body)
        return CreateResponse.from_dict(json)

    def delete(self, request: Delete):
        """Delete a file/directory.

        Delete the file or directory (optionally recursively delete all files in
        the directory). This call throws an exception with `IO_ERROR` if the
        path is a non-empty directory and `recursive` is set to `false` or on
        other similar errors.

        When you delete a large number of files, the delete operation is done in
        increments. The call returns a response after approximately 45 seconds
        with an error message (503 Service Unavailable) asking you to re-invoke
        the delete operation until the directory structure is fully deleted.

        For operations that delete more than 10K files, we discourage using the
        DBFS REST API, but advise you to perform such operations in the context
        of a cluster, using the [File system utility
        (dbutils.fs)](/dev-tools/databricks-utils.html#dbutils-fs). `dbutils.fs`
        covers the functional scope of the DBFS REST API, but from notebooks.
        Running such operations using notebooks provides better control and
        manageability, such as selective deletes, and the possibility to
        automate periodic delete jobs."""
        query, body = request.as_request()
        self._api.do("POST", "/api/2.0/dbfs/delete", query=query, body=body)

    def get_status(self, request: GetStatus) -> FileInfo:
        """Get the information of a file or directory.

        Gets the file information for a file or directory. If the file or
        directory does not exist, this call throws an exception with
        `RESOURCE_DOES_NOT_EXIST`."""
        query, body = request.as_request()
        json = self._api.do("GET", "/api/2.0/dbfs/get-status", query=query, body=body)
        return FileInfo.from_dict(json)

    def list(self, request: List) -> ListStatusResponse:
        """List directory contents or file details.

        List the contents of a directory, or details of the file. If the file or
        directory does not exist, this call throws an exception with
        `RESOURCE_DOES_NOT_EXIST`.

        When calling list on a large directory, the list operation will time out
        after approximately 60 seconds. We strongly recommend using list only on
        directories containing less than 10K files and discourage using the DBFS
        REST API for operations that list more than 10K files. Instead, we
        recommend that you perform such operations in the context of a cluster,
        using the [File system utility
        (dbutils.fs)](/dev-tools/databricks-utils.html#dbutils-fs), which
        provides the same functionality without timing out."""
        query, body = request.as_request()
        json = self._api.do("GET", "/api/2.0/dbfs/list", query=query, body=body)
        return ListStatusResponse.from_dict(json)

    def mkdirs(self, request: MkDirs):
        """Create a directory.

        Creates the given directory and necessary parent directories if they do
        not exist. If a file (not a directory) exists at any prefix of the input
        path, this call throws an exception with `RESOURCE_ALREADY_EXISTS`.
        **Note**: If this operation fails, it might have succeeded in creating
        some of the necessary parent directories."""
        query, body = request.as_request()
        self._api.do("POST", "/api/2.0/dbfs/mkdirs", query=query, body=body)

    def move(self, request: Move):
        """Move a file.

        Moves a file from one location to another location within DBFS. If the
        source file does not exist, this call throws an exception with
        `RESOURCE_DOES_NOT_EXIST`. If a file already exists in the destination
        path, this call throws an exception with `RESOURCE_ALREADY_EXISTS`. If
        the given source path is a directory, this call always recursively moves
        all files.","""
        query, body = request.as_request()
        self._api.do("POST", "/api/2.0/dbfs/move", query=query, body=body)

    def put(self, request: Put):
        """Upload a file.

        Uploads a file through the use of multipart form post. It is mainly used
        for streaming uploads, but can also be used as a convenient single call
        for data upload.

        Alternatively you can pass contents as base64 string.

        The amount of data that can be passed (when not streaming) using the
        __contents__ parameter is limited to 1 MB. `MAX_BLOCK_SIZE_EXCEEDED`
        will be thrown if this limit is exceeded.

        If you want to upload large files, use the streaming upload. For
        details, see :method:create, :method:addBlock, :method:close."""
        query, body = request.as_request()
        self._api.do("POST", "/api/2.0/dbfs/put", query=query, body=body)

    def read(self, request: Read) -> ReadResponse:
        """Get the contents of a file.

        "Returns the contents of a file. If the file does not exist, this call
        throws an exception with `RESOURCE_DOES_NOT_EXIST`. If the path is a
        directory, the read length is negative, or if the offset is negative,
        this call throws an exception with `INVALID_PARAMETER_VALUE`. If the
        read length exceeds 1 MB, this call throws an\nexception with
        `MAX_READ_SIZE_EXCEEDED`.

        If `offset + length` exceeds the number of bytes in a file, it reads the
        contents until the end of file.","""
        query, body = request.as_request()
        json = self._api.do("GET", "/api/2.0/dbfs/read", query=query, body=body)
        return ReadResponse.from_dict(json)
