from __future__ import annotations

import base64
import datetime
import functools
import json
import logging
import math
import os
import pathlib
import platform
import re
import shutil
import xml.etree.ElementTree as ET
from abc import ABC, abstractmethod
from collections import deque
from collections.abc import Iterator
from dataclasses import dataclass
from datetime import timedelta
from enum import Enum
from io import BytesIO
from threading import Lock
from types import TracebackType
from typing import TYPE_CHECKING, AnyStr, BinaryIO, Callable, Generator, Iterable, Optional, Type, Union
from urllib import parse

import requests
import requests.adapters

from .._base_client import _BaseClient, _json_default, _StreamingResponse
from .._property import _cached_property
from ..config import Config
from ..errors import AlreadyExists, NotFound
from ..errors.mapper import _error_mapper
from databricks.sdk.service import files
from databricks.sdk.service._internal import _escape_multi_segment_path_parameter
from databricks.sdk.service.files import DownloadResponse
from .files_utils import (
    CreateDownloadUrlResponse,
    _ByteRange,
    _common_decision,
    _download_ranges_to_file,
    _DownloadDestination,
    _Failure,
    _MultipartUploadSession,
    _plan_upload,
    _PresignedUrlDistributor,
    _RangeResponse,
    _RequestFailed,
    _ResilientDownload,
    _retry,
    _RetryBudget,
    _split_into_ranges,
    _TransferStatus,
    _UploadData,
    _upload_to,
    _UrlExpired,
    _walk_endpoints,
    _WalkingDownloadStream,
)

if TYPE_CHECKING:
    from _typeshed import Self

_LOG = logging.getLogger(__name__)

# The workspace's Files API 2.0 handler rejects a request body over 5 GiB, so it takes no single-shot upload above it.
_WORKSPACE_MAX_SINGLE_SHOT_SIZE = 5 * 1024 * 1024 * 1024
# The workspace, the usual fallback for uploads, takes single-shot uploads only, so a transient failure before commit
# is retried once before the upload moves there.
_UPLOAD_RETRIES_BEFORE_COMMIT = 1


class _DbfsIO(BinaryIO):
    MAX_CHUNK_SIZE = 1024 * 1024

    _status: files.FileInfo = None
    _created: files.CreateResponse = None
    _offset = 0
    _closed = False

    def __init__(
        self,
        api: files.DbfsAPI,
        path: str,
        *,
        read: bool = False,
        write: bool = False,
        overwrite: bool = False,
    ):
        self._api = api
        self._path = path
        if write and read:
            raise IOError("can open either for reading or writing")
        if read:
            self._status = api.get_status(path)
        elif write:
            self._created = api.create(path, overwrite=overwrite)
        else:
            raise IOError("need to open either for reading or writing")

    def __enter__(self) -> Self:
        return self

    @property
    def name(self) -> str:
        return self._path

    def writable(self) -> bool:
        """
        Return whether object was opened for writing.

        If False, write() will raise OSError.
        """
        return self._created is not None

    def write(self, buffer: bytes) -> int:
        """Write bytes to file.

        :return: Return the number of bytes written.
        """
        if not self.writable():
            raise IOError("file not open for writing")
        if type(buffer) is not bytes:
            # Python doesn't strictly enforce types. Even if they're specified.
            raise TypeError(f"a bytes-like object is required, not {type(buffer)}")
        total = 0
        while total < len(buffer):
            chunk = buffer[total:]
            if len(chunk) > self.MAX_CHUNK_SIZE:
                chunk = chunk[: self.MAX_CHUNK_SIZE]
            encoded = base64.b64encode(chunk).decode()
            self._api.add_block(self._created.handle, encoded)
            total += len(chunk)
        return total

    def close(self) -> None:
        """Disable all I/O operations."""
        if self.writable():
            self._api.close(self._created.handle)
        self._closed = True

    @property
    def closed(self) -> bool:
        return self._closed

    def __exit__(
        self,
        __t: Type[BaseException] | None,
        __value: BaseException | None,
        __traceback: TracebackType | None,
    ):
        self.close()

    def readable(self) -> bool:
        return self._status is not None

    def read(self, size: int = ...) -> bytes:
        """Read at most size bytes, returned as a bytes object.

        :param size: If the size argument is negative, read until EOF is reached.
                     Return an empty bytes object at EOF.
        :return: bytes
        """
        if not self.readable():
            raise IOError("file not open for reading")

        # call __iter__() and read until EOF is reached
        if size is ... or size < 0:
            buffer = b""
            for chunk in self:
                buffer += chunk
            return buffer

        response = self._api.read(self._path, length=size, offset=self._offset)
        # The guard against offset >= size happens above, so this can only happen
        # if the file is modified or truncated while reading. If this happens,
        # the read contents will likely be corrupted, so we return an error.
        if response.bytes_read == 0:
            # as per Python interface convention, return an empty bytes object at EOF,
            # and not the EOFError as in other SDKs
            return b""

        raw = base64.b64decode(response.data)
        self._offset += response.bytes_read
        return raw

    def __iter__(self) -> Iterator[bytes]:
        while self._offset < self._status.file_size:
            yield self.__next__()

    def __next__(self) -> bytes:
        # TODO: verify semantics
        return self.read(self.MAX_CHUNK_SIZE)

    def fileno(self) -> int:
        return 0

    def flush(self) -> None:
        pass

    def isatty(self) -> bool:
        return False

    def readline(self, __limit: int = ...) -> AnyStr:
        raise NotImplementedError

    def readlines(self, __hint: int = ...) -> list[AnyStr]:
        raise NotImplementedError

    def seek(self, __offset: int, __whence: int = ...) -> int:
        raise NotImplementedError

    def seekable(self) -> bool:
        return False

    def tell(self) -> int:
        return self._offset

    def truncate(self, __size: int | None = ...) -> int:
        raise NotImplementedError

    def writelines(self, __lines: Iterable[AnyStr]) -> None:
        raise NotImplementedError

    def __repr__(self) -> str:
        return f"<_DbfsIO {self._path} {'read' if self.readable() else 'write'}=True>"


class _VolumesIO(BinaryIO):
    def __init__(
        self,
        api: files.FilesAPI,
        path: str,
        *,
        read: bool,
        write: bool,
        overwrite: bool,
    ):
        self._buffer = []
        self._api = api
        self._path = path
        self._read = read
        self._write = write
        self._overwrite = overwrite
        self._closed = False
        self._read_handle = None
        self._offset = 0

    def __enter__(self):
        if self._read:
            self.__open_read()
        return self

    def close(self):
        if self._closed:
            return
        if self._write:
            to_write = b"".join(self._buffer)
            self._api.upload(
                self._path,
                contents=BytesIO(to_write),
                overwrite=self._overwrite,
            )
        elif self._read:
            self._read_handle.close()
        self._closed = True

    def fileno(self) -> int:
        return 0

    def flush(self):
        raise NotImplementedError()

    def isatty(self) -> bool:
        return False

    def __check_closed(self):
        if self._closed:
            raise ValueError("I/O operation on closed file")

    def __open_read(self):
        if self._read_handle is None:
            self._read_handle = self._api.download(self._path).contents

    def read(self, __n=...):
        self.__check_closed()
        self.__open_read()
        return self._read_handle.read(__n)

    def readable(self):
        return self._read

    def readline(self, __limit=...):
        raise NotImplementedError()

    def readlines(self, __hint=...):
        raise NotImplementedError()

    def seek(self, __offset, __whence=...):
        raise NotImplementedError()

    def seekable(self):
        return False

    def tell(self):
        if self._read_handle is not None:
            return self._read_handle.tell()
        return self._offset

    def truncate(self, __size=...):
        raise NotImplementedError()

    def writable(self):
        return self._write

    def write(self, __s):
        self.__check_closed()
        self._buffer.append(__s)

    def writelines(self, __lines):
        raise NotImplementedError()

    def __next__(self):
        self.__check_closed()
        return self._read_handle.__next__()

    def __iter__(self):
        self.__check_closed()
        return self._read_handle.__iter__()

    def __exit__(self, __t, __value, __traceback):
        self.close()

    def __repr__(self) -> str:
        return f"<_VolumesIO {self._path} {'read' if self.readable() else 'write'}=True>"


class _Path(ABC):
    @abstractmethod
    def __init__(self): ...

    @property
    def is_local(self) -> bool:
        return self._is_local()

    @abstractmethod
    def _is_local(self) -> bool: ...

    @property
    def is_dbfs(self) -> bool:
        return self._is_dbfs()

    @abstractmethod
    def _is_dbfs(self) -> bool: ...

    @abstractmethod
    def child(self, path: str) -> str: ...

    @_cached_property
    def is_dir(self) -> bool:
        return self._is_dir()

    @abstractmethod
    def _is_dir(self) -> bool: ...

    @abstractmethod
    def exists(self) -> bool: ...

    @abstractmethod
    def open(self, *, read=False, write=False, overwrite=False): ...

    def list(self, *, recursive=False) -> Generator[files.FileInfo, None, None]: ...

    @abstractmethod
    def mkdir(self): ...

    @abstractmethod
    def delete(self, *, recursive=False): ...

    @property
    def name(self) -> str:
        return self._path.name

    @property
    def as_string(self) -> str:
        return str(self._path)


class _LocalPath(_Path):
    def __init__(self, path: str):
        if platform.system() == "Windows":
            self._path = pathlib.Path(str(path).replace("file:///", "").replace("file:", ""))
        else:
            self._path = pathlib.Path(str(path).replace("file:", ""))

    def _is_local(self) -> bool:
        return True

    def _is_dbfs(self) -> bool:
        return False

    def child(self, path: str) -> Self:
        return _LocalPath(str(self._path / path))

    def _is_dir(self) -> bool:
        return self._path.is_dir()

    def mkdir(self):
        self._path.mkdir(mode=0o755, parents=True, exist_ok=True)

    def exists(self) -> bool:
        return self._path.exists()

    def open(self, *, read=False, write=False, overwrite=False):
        # make local fs follow the similar semantics as DBFS
        self._path.parent.mkdir(mode=0o755, parents=True, exist_ok=True)
        return self._path.open(mode="wb" if overwrite else "rb" if read else "xb")

    def list(self, recursive=False) -> Generator[files.FileInfo, None, None]:
        if not self.is_dir:
            st = self._path.stat()
            yield files.FileInfo(
                path="file:" + str(self._path.absolute()),
                is_dir=False,
                file_size=st.st_size,
                modification_time=int(st.st_mtime_ns / 1e6),
            )
            return
        queue = deque([self._path])
        while queue:
            path = queue.popleft()
            for leaf in path.iterdir():
                if leaf.is_dir():
                    if recursive:
                        queue.append(leaf)
                    continue
                info = leaf.stat()
                yield files.FileInfo(
                    path="file:" + str(leaf.absolute()),
                    is_dir=False,
                    file_size=info.st_size,
                    modification_time=int(info.st_mtime_ns / 1e6),
                )

    def delete(self, *, recursive=False):
        if self.is_dir:
            if recursive:
                for leaf in self.list(recursive=True):
                    _LocalPath(leaf.path).delete()
            self._path.rmdir()
        else:
            self._path.unlink(missing_ok=True)

    def __repr__(self) -> str:
        return f"<_LocalPath {self._path}>"


class _VolumesPath(_Path):
    def __init__(self, api: files.FilesAPI, src: Union[str, pathlib.Path]):
        self._path = pathlib.PurePosixPath(str(src).replace("dbfs:", "").replace("file:", ""))
        self._api = api

    def _is_local(self) -> bool:
        return False

    def _is_dbfs(self) -> bool:
        return False

    def child(self, path: str) -> Self:
        return _VolumesPath(self._api, str(self._path / path))

    def _is_dir(self) -> bool:
        try:
            self._api.get_directory_metadata(self.as_string)
            return True
        except NotFound:
            return False

    def mkdir(self):
        self._api.create_directory(self.as_string)

    def exists(self) -> bool:
        try:
            self._api.get_metadata(self.as_string)
            return True
        except NotFound:
            return self.is_dir

    def open(self, *, read=False, write=False, overwrite=False) -> BinaryIO:
        return _VolumesIO(
            self._api,
            self.as_string,
            read=read,
            write=write,
            overwrite=overwrite,
        )

    def list(self, *, recursive=False) -> Generator[files.FileInfo, None, None]:
        if not self.is_dir:
            meta = self._api.get_metadata(self.as_string)
            yield files.FileInfo(
                path=self.as_string,
                is_dir=False,
                file_size=meta.content_length,
                modification_time=meta.last_modified,
            )
            return
        queue = deque([self])
        while queue:
            next_path = queue.popleft()
            for file in self._api.list_directory_contents(next_path.as_string):
                if recursive and file.is_directory:
                    queue.append(self.child(file.name))
                if not recursive or not file.is_directory:
                    yield files.FileInfo(
                        path=file.path,
                        is_dir=file.is_directory,
                        file_size=file.file_size,
                        modification_time=file.last_modified,
                    )

    def delete(self, *, recursive=False):
        if self.is_dir:
            for entry in self.list(recursive=False):
                _VolumesPath(self._api, entry.path).delete(recursive=True)
            self._api.delete_directory(self.as_string)
        else:
            self._api.delete(self.as_string)

    def __repr__(self) -> str:
        return f"<_VolumesPath {self._path}>"


class _DbfsPath(_Path):
    def __init__(self, api: files.DbfsAPI, src: str):
        self._path = pathlib.PurePosixPath(str(src).replace("dbfs:", "").replace("file:", ""))
        self._api = api

    def _is_local(self) -> bool:
        return False

    def _is_dbfs(self) -> bool:
        return True

    def child(self, path: str) -> Self:
        child = self._path / path
        return _DbfsPath(self._api, str(child))

    def _is_dir(self) -> bool:
        try:
            remote = self._api.get_status(self.as_string)
            return remote.is_dir
        except NotFound:
            return False

    def mkdir(self):
        self._api.mkdirs(self.as_string)

    def exists(self) -> bool:
        try:
            self._api.get_status(self.as_string)
            return True
        except NotFound:
            return False

    def open(self, *, read=False, write=False, overwrite=False) -> BinaryIO:
        return _DbfsIO(
            self._api,
            self.as_string,
            read=read,
            write=write,
            overwrite=overwrite,
        )

    def list(self, *, recursive=False) -> Generator[files.FileInfo, None, None]:
        if not self.is_dir:
            meta = self._api.get_status(self.as_string)
            yield files.FileInfo(
                path=self.as_string,
                is_dir=False,
                file_size=meta.file_size,
                modification_time=meta.modification_time,
            )
            return
        queue = deque([self])
        while queue:
            next_path = queue.popleft()
            for file in self._api.list(next_path.as_string):
                if recursive and file.is_dir:
                    queue.append(self.child(file.path))
                if not recursive or not file.is_dir:
                    yield file

    def delete(self, *, recursive=False):
        self._api.delete(self.as_string, recursive=recursive)

    def __repr__(self) -> str:
        return f"<_DbfsPath {self._path}>"


class _RetryableException(Exception):
    """Base class for retryable exceptions in DBFS operations."""

    def __init__(self, message: str, http_status_code: int):
        super().__init__()
        self.message = message
        self.http_status_code = http_status_code

    def __str__(self) -> str:
        return f"{self.message} (HTTP Status: {self.http_status_code})"

    @staticmethod
    def make_error(response: requests.Response) -> "_RetryableException":
        """Map the response to a retryable exception."""

        return _RetryableException(
            message=response.text,
            http_status_code=response.status_code,
        )


class DbfsExt(files.DbfsAPI):
    __doc__ = files.DbfsAPI.__doc__

    def __init__(self, api_client):
        super().__init__(api_client)
        self._files_api = files.FilesAPI(api_client)
        self._dbfs_api = files.DbfsAPI(api_client)

    def open(
        self,
        path: str,
        *,
        read: bool = False,
        write: bool = False,
        overwrite: bool = False,
    ) -> BinaryIO:
        return self._path(path).open(read=read, write=write, overwrite=overwrite)

    def upload(self, path: str, src: BinaryIO, *, overwrite: bool = False):
        """Upload file to DBFS"""
        with self.open(path, write=True, overwrite=overwrite) as dst:
            shutil.copyfileobj(src, dst, length=_DbfsIO.MAX_CHUNK_SIZE)

    def download(self, path: str) -> BinaryIO:
        """Download file from DBFS"""
        return self.open(path, read=True)

    def list(self, path: str, *, recursive=False) -> Iterator[files.FileInfo]:
        """List directory contents or file details.

        List the contents of a directory, or details of the file. If the file or directory does not exist,
        this call throws an exception with `RESOURCE_DOES_NOT_EXIST`.

        When calling list on a large directory, the list operation will time out after approximately 60
        seconds.

        :param path: the DBFS or UC Volume path to list
        :param recursive: traverse deep into directory tree
        :returns iterator of metadata for every file
        """
        p = self._path(path)
        yield from p.list(recursive=recursive)

    def mkdirs(self, path: str):
        """Create directory on DBFS"""
        p = self._path(path)
        p.mkdir()

    def exists(self, path: str) -> bool:
        """If file exists on DBFS"""
        p = self._path(path)
        return p.exists()

    __ALLOWED_SCHEMES = [None, "file", "dbfs"]

    def _path(self, src):
        src = parse.urlparse(str(src))
        if src.scheme and src.scheme not in self.__ALLOWED_SCHEMES:
            raise ValueError(
                f'unsupported scheme "{src.scheme}". DBUtils in the SDK only supports local, root DBFS, and '
                "UC Volumes paths, not external locations or DBFS mount points."
            )
        if src.scheme == "file":
            return _LocalPath(src.geturl())
        if src.path.startswith("/Volumes"):
            return _VolumesPath(self._files_api, src.geturl())
        return _DbfsPath(self._dbfs_api, src.geturl())

    def copy(self, src: str, dst: str, *, recursive=False, overwrite=False):
        """Copy files between DBFS and local filesystems"""
        src = self._path(src)
        dst = self._path(dst)
        if src.is_local and dst.is_local:
            raise IOError("both destinations are on local FS")
        if dst.exists() and dst.is_dir:
            # if target is a folder, make file with the same name there
            dst = dst.child(src.name)
        if src.is_dir:
            queue = [self._path(x.path) for x in src.list(recursive=recursive) if not x.is_dir]
        else:
            queue = [src]
        for child in queue:
            child_dst = dst.child(os.path.relpath(child.as_string, src.as_string))
            with child.open(read=True) as reader:
                with child_dst.open(write=True, overwrite=overwrite) as writer:
                    shutil.copyfileobj(reader, writer, length=_DbfsIO.MAX_CHUNK_SIZE)

    def move_(self, src: str, dst: str, *, recursive=False, overwrite=False):
        """Move files between local and DBFS systems"""
        source = self._path(src)
        target = self._path(dst)
        if source.is_dbfs and target.is_dbfs:
            # Moves a file from one location to another location within DBFS.
            # this operation is recursive by default.
            return self.move(source.as_string, target.as_string)
        if source.is_local and target.is_local:
            raise IOError("both destinations are on local FS")
        if source.is_dir and not recursive:
            src_type = "local" if source.is_local else "DBFS" if source.is_dbfs else "UC Volume"
            dst_type = "local" if target.is_local else "DBFS" if target.is_dbfs else "UC Volume"
            raise IOError(f"moving a directory from {src_type} to {dst_type} requires recursive flag")
        # do cross-fs moving
        self.copy(src, dst, recursive=recursive, overwrite=overwrite)
        self.delete(src, recursive=recursive)

    def delete(self, path: str, *, recursive=False):
        """Delete file or directory on DBFS"""
        p = self._path(path)
        if p.is_dir and not recursive:
            raise IOError("deleting directories requires recursive flag")
        p.delete(recursive=recursive)


class FallbackToUploadUsingFilesApi(Exception):
    """Custom exception that signals to fallback to FilesAPI for upload"""

    def __init__(self, buffer, message):
        super().__init__(message)
        self.buffer = buffer


class FallbackToDownloadUsingFilesApi(Exception):
    """Custom exception that signals to fallback to FilesAPI for download"""

    def __init__(self, message):
        super().__init__(message)


@dataclass
class UploadStreamResult:
    """Result of an upload from stream operation. Currently empty, but can be extended in the future."""


@dataclass
class UploadFileResult:
    """Result of an upload from file operation. Currently empty, but can be extended in the future."""


@dataclass
class DownloadFileResult:
    """Result of a download to file operation. Currently empty, but can be extended in the future."""


@dataclass
class _PresignedUrl:
    """Resolved presigned URL with associated headers for cloud storage operations."""

    url: str
    headers: dict[str, str]
    part_number: int | None = None


class _ResolvedEndpoint(Enum):
    """A file transfer protocol this SDK can speak, identified by the (api, api_version) pair the
    endpoints API returns."""

    IO_OFFLOAD = "IO_OFFLOAD"
    FILES_API_V2 = "FILES_API_V2"


# Maps the server's (api, api_version) to a protocol compiled into this SDK. Pairs not listed here are
# skipped, which lets the server advertise newer protocols without breaking older SDKs. IO_OFFLOAD is
# unversioned during the preview, so a versioned IO_OFFLOAD is newer than this SDK.
_RECOGNIZED_ENDPOINTS: dict[tuple[str, Optional[str]], _ResolvedEndpoint] = {
    ("IO_OFFLOAD", None): _ResolvedEndpoint.IO_OFFLOAD,
    ("FILES_API", "2.0"): _ResolvedEndpoint.FILES_API_V2,
}

# The Files API path each protocol initiates, completes, uploads and downloads through. IO_OFFLOAD initiates
# and completes uploads through Files API 2.0 on the workspace host.
_FILES_API_PATHS: dict[_ResolvedEndpoint, str] = {
    _ResolvedEndpoint.IO_OFFLOAD: "/api/2.0/fs/files",
    _ResolvedEndpoint.FILES_API_V2: "/api/2.0/fs/files",
}

_ENDPOINT_SCHEMES = ("http", "https")


@dataclass(frozen=True)
class _Endpoint:
    """One entry of the ordered endpoint list a file transfer walks, best first."""

    kind: _ResolvedEndpoint
    base_url: str
    """Scheme and hostname as returned by the server, e.g. https://example.cloud.databricks.com."""
    multipart_upload_supported: bool


def _files_api_file_path(path: str) -> str:
    """The escaped file path that follows /fs/files in a Files API URL."""
    escaped = _escape_multi_segment_path_parameter(path)
    # Mirrors the API client, which collapses a doubled leading slash in Files API paths.
    return escaped[1:] if escaped.startswith("//") else escaped


class _PresignedUrlRequestBuilder:
    """Builds presigned URL requests for file upload operations.

    Encapsulates the coordination API calls (create-upload-part-urls, create-download-url) and response parsing
    into a single place.
    """

    def __init__(self, api, hostname: str):
        self._api = api
        self._hostname = hostname

    def build_upload_part_urls(
        self, path: str, session_token: str, start_part_number: int, count: int, expire_time: str
    ) -> list[_PresignedUrl]:
        """Fetches a batch of presigned URLs for uploading multiple multipart parts."""
        body = {
            "path": path,
            "session_token": session_token,
            "start_part_number": start_part_number,
            "count": count,
            "expire_time": expire_time,
        }
        response = self._api.do(
            "POST",
            url=f"{self._hostname}/api/2.0/fs/create-upload-part-urls",
            headers={"Content-Type": "application/json"},
            body=body,
        )
        upload_part_urls = response.get("upload_part_urls", [])
        if len(upload_part_urls) == 0:
            raise ValueError(f"Unexpected server response: {response}")
        results = []
        for part_info in upload_part_urls:
            url = part_info["url"]
            part_number = part_info["part_number"]
            headers: dict[str, str] = {"Content-Type": "application/octet-stream"}
            for h in part_info.get("headers", []):
                headers[h["name"]] = h["value"]
            results.append(_PresignedUrl(url=url, headers=headers, part_number=part_number))
        return results

    def build_download_url(self, path: str, expire_time: str) -> CreateDownloadUrlResponse:
        """Fetches a presigned URL for downloading a file."""
        response = self._api.do(
            "POST",
            url=f"{self._hostname}/api/2.0/fs/create-download-url",
            query={
                "path": path,
                "expire_time": expire_time,
            },
        )
        return CreateDownloadUrlResponse.from_dict(response)


class _StorageProxyRequestBuilder:
    """Builds direct upload requests to the storage proxy.

    Skips the presigned URL coordination APIs entirely. Instead, constructs
    URLs that point directly at the proxy endpoint with query parameters for
    session token, upload type, and part number. The proxy handles cloud
    storage interaction internally.
    """

    def __init__(self, hostname: str):
        self._hostname = hostname

    def build_upload_part_urls(
        self, path: str, session_token: str, start_part_number: int, count: int, expire_time: str
    ) -> list[_PresignedUrl]:
        """Builds URLs for uploading multipart parts directly to the storage proxy."""
        base = f"{self._hostname}/api/2.0/fs/files{_files_api_file_path(path)}"
        results = []
        for i in range(count):
            part_number = start_part_number + i
            query = parse.urlencode(
                {
                    "session_token": session_token,
                    "upload_type": "multipart",
                    "part_number": part_number,
                }
            )
            results.append(
                _PresignedUrl(
                    url=f"{base}?{query}",
                    headers={"Content-Type": "application/octet-stream"},
                    part_number=part_number,
                )
            )
        return results

    def build_download_url(self, path: str, expire_time: str) -> CreateDownloadUrlResponse:
        """Builds a URL for downloading a file directly from the storage proxy."""
        return CreateDownloadUrlResponse(
            url=f"{self._hostname}/api/2.0/fs/files{_files_api_file_path(path)}",
            headers={},
        )


class FilesExt(files.FilesAPI):
    __doc__ = files.FilesAPI.__doc__

    # Storage-proxy hostname for data plane file operations.
    _STORAGE_PROXY_HOSTNAME: str = "http://storage-proxy.databricks.com"

    # Timeout in seconds for the storage-proxy health check probe.
    _STORAGE_PROXY_PROBE_TIMEOUT: float = 3.0

    _ENDPOINTS_API_PATH: str = "/api/2.0/fs/endpoints"

    # Endpoint discovery is a single attempt bounded by this timeout: it precedes a transfer, so it
    # must fail fast to the default order rather than retry and stall the upload or download.
    _ENDPOINTS_RESOLVE_TIMEOUT_SECONDS: float = 10.0

    def __init__(self, api_client, config: Config):
        super().__init__(api_client)
        self._config = config.copy()
        self._multipart_upload_read_ahead_bytes = 1
        self._cached_cloud_provider_session: Optional[requests.Session] = None
        self._cloud_provider_session_lock = Lock()
        self._dp_hostname_available: Optional[bool] = None
        self._storage_proxy_probe_lock = Lock()
        self._cached_authenticated_session: Optional[requests.Session] = None
        self._authenticated_session_lock = Lock()
        self._cached_endpoints: Optional[list[_Endpoint]] = None
        self._endpoints_lock = Lock()

    def _resolve_endpoints(self) -> list[_Endpoint]:
        """Returns the ordered endpoints to try for a file transfer, best first.

        The server is asked once per client and its answer, including a failure, is cached. Anything
        short of a usable list falls back to the built-in order, so endpoint discovery never fails a
        transfer.
        """
        if not self._config.experimental_files_ext_enable_endpoints_api:
            return self._default_endpoints()
        with self._endpoints_lock:
            if self._cached_endpoints is None:
                self._cached_endpoints = self._fetch_endpoints() or self._default_endpoints()
            return list(self._cached_endpoints)

    def _default_endpoints(self) -> list[_Endpoint]:
        """The built-in order: presigned URLs, or the storage proxy when experimental_files_ext_enable_storage_proxy
        is set and the probe finds it can serve this workspace; then the Files API on the workspace host, which takes
        uploads only in a single shot.
        """
        host = self._config.host
        if self._storage_proxy_available():
            first = _Endpoint(
                _ResolvedEndpoint.FILES_API_V2, self._STORAGE_PROXY_HOSTNAME, multipart_upload_supported=True
            )
        else:
            first = _Endpoint(_ResolvedEndpoint.IO_OFFLOAD, host, multipart_upload_supported=True)
        return [first, _Endpoint(_ResolvedEndpoint.FILES_API_V2, host, multipart_upload_supported=False)]

    def _transfer_endpoints(self) -> list[_Endpoint]:
        """The endpoints a transfer walks, best first."""
        return self._default_endpoints()

    def _storage_proxy_available(self) -> bool:
        """Whether the storage-proxy flag is set and the proxy can serve this workspace.

        The probe runs once per client and its result, including a failure, is cached.
        """
        if not self._config.experimental_files_ext_enable_storage_proxy:
            return False
        available = self._dp_hostname_available
        if available is not None:
            return available
        with self._storage_proxy_probe_lock:
            if self._dp_hostname_available is None:
                self._dp_hostname_available = self._probe_storage_proxy()
                if self._dp_hostname_available:
                    _LOG.info("Storage proxy is available, will use it for file operations.")
                else:
                    _LOG.info("Storage proxy is not available, will use presigned URLs.")
            return self._dp_hostname_available

    def _fetch_endpoints(self) -> list[_Endpoint]:
        """Fetches the endpoint list from the server, keeping only entries this SDK can speak.

        Discovery runs before a transfer, so it is a single short-timeout attempt with no retries: a
        slow or failing endpoint must fall back to the default order quickly rather than hold up the
        upload or download.
        """
        url = f"{self._config.host}{self._ENDPOINTS_API_PATH}"
        try:
            response = self._cloud_provider_session().request(
                "GET",
                url,
                headers={**self._config.authenticate(), "Accept": "application/json"},
                timeout=self._ENDPOINTS_RESOLVE_TIMEOUT_SECONDS,
            )
        except Exception as e:
            # Broad on purpose: network and auth failures must all fail safe to the default order.
            _LOG.warning(f"Failed to resolve file endpoints, using the default endpoints: {e}")
            return []

        # Lets a failure below be traced to the server's request log.
        request_id = response.headers.get("x-request-id")
        if response.status_code == 404:
            # Not a warning: until the server-side rollout completes, some workspaces do not serve the API.
            _LOG.info(
                f"Endpoints API is not served for this workspace (request ID {request_id}), using the default endpoints."
            )
            return []
        if response.status_code != 200:
            _LOG.warning(
                f"Unexpected status resolving file endpoints ({response.status_code}, request ID {request_id}), "
                "using the default endpoints."
            )
            return []
        try:
            body = response.json()
        except Exception as e:
            _LOG.warning(
                f"Failed to parse endpoints response (request ID {request_id}), using the default endpoints: {e}"
            )
            return []

        # Proto3 JSON leaves out an empty repeated field.
        entries = body.get("endpoints", []) if isinstance(body, dict) else None
        if not isinstance(entries, list):
            _LOG.warning(
                f"Unexpected endpoints response (request ID {request_id}), using the default endpoints: {body}"
            )
            return []
        endpoints = []
        for entry in entries:
            kind = self._endpoint_kind(entry)
            if kind is None:
                # Not a warning: an older SDK is expected to skip entries for APIs added after it shipped.
                _LOG.info(f"Skipping endpoint this SDK cannot use (request ID {request_id}): {entry}")
                continue
            endpoint = self._parse_endpoint(entry, kind)
            if endpoint is None:
                _LOG.warning(
                    f"Skipping {kind.value} endpoint with an unusable address (request ID {request_id}): {entry}"
                )
                continue
            endpoints.append(endpoint)
        if not endpoints:
            _LOG.warning(f"No usable endpoints in the response (request ID {request_id}), using the default endpoints.")
        return endpoints

    @staticmethod
    def _endpoint_kind(entry) -> Optional[_ResolvedEndpoint]:
        """Returns the protocol of a listed endpoint, or None if this SDK does not speak it."""
        if not isinstance(entry, dict):
            return None
        api = entry.get("api")
        api_version = entry.get("api_version")
        # The entry is unvalidated JSON: an unhashable value such as a list would make the lookup below raise
        # instead of skipping the entry. IO_OFFLOAD entries have no api_version, so None is allowed.
        if not isinstance(api, str) or not (api_version is None or isinstance(api_version, str)):
            return None
        return _RECOGNIZED_ENDPOINTS.get((api, api_version))

    @staticmethod
    def _parse_endpoint(entry: dict, kind: _ResolvedEndpoint) -> Optional[_Endpoint]:
        scheme = entry.get("scheme")
        hostname = entry.get("hostname")
        if scheme not in _ENDPOINT_SCHEMES or not isinstance(hostname, str) or not hostname:
            return None
        # Mirrors the proto getter: an unset optional bool reads as false.
        multipart_upload_supported = entry.get("multipart_upload_supported") is True
        return _Endpoint(kind, f"{scheme}://{hostname}", multipart_upload_supported)

    def _uses_api_client(self, endpoint: _Endpoint) -> bool:
        """Whether transfers to the endpoint go through the workspace API client.

        The workspace host keeps the API client's retries, as its Files API always has. Other hosts get the
        bounded transfer retries, so that a failing endpoint gives way to the next one quickly.
        """
        return endpoint.kind != _ResolvedEndpoint.IO_OFFLOAD and _origin(endpoint.base_url) == _origin(
            self._config.host
        )

    @staticmethod
    def _files_api_url(endpoint: _Endpoint, path: str) -> str:
        """The URL of a file in the endpoint's Files API."""
        return f"{endpoint.base_url}{_FILES_API_PATHS[endpoint.kind]}{_files_api_file_path(path)}"

    def _request_builder_for(self, endpoint: _Endpoint):
        """Maps an endpoint to the builder that speaks its protocol.

        The offload path coordinates presigned URLs through the workspace API; the direct Files API path
        builds URLs straight at the endpoint host.
        """
        if endpoint.kind == _ResolvedEndpoint.IO_OFFLOAD:
            return _PresignedUrlRequestBuilder(self._api, endpoint.base_url)
        return _StorageProxyRequestBuilder(endpoint.base_url)

    def _resolve_workspace_id(self) -> Optional[str]:
        """Resolves the workspace ID by querying the SCIM Me endpoint."""
        try:
            response = self._api.do("GET", "/api/2.0/preview/scim/v2/Me", response_headers=["X-Databricks-Org-Id"])
            workspace_id = response.get("X-Databricks-Org-Id")
            if workspace_id:
                return str(workspace_id)
        except Exception:
            _LOG.debug("Failed to resolve workspace ID for storage proxy probe.")
        return None

    def _probe_storage_proxy(self) -> bool:
        """Probes the storage proxy to check if it can serve this workspace.

        Uses a HEAD request to the probe endpoint with the workspace ID as a
        query parameter. The proxy returns 200 if it can serve this workspace,
        403 for a wrong workspace, and connection errors if unreachable.
        Returns False if the workspace ID cannot be resolved.
        """
        workspace_id = self._resolve_workspace_id()
        if not workspace_id:
            _LOG.debug("Workspace ID not available, skipping storage proxy probe.")
            return False
        proxy_host = self._STORAGE_PROXY_HOSTNAME
        probe_url = f"{proxy_host}/api/2.0/fs/files/DatabricksInternal/Probe/fullstack/wis?ew={workspace_id}"
        try:
            headers = self._config.authenticate()
            session = self._cloud_provider_session()
            response = session.request(
                "HEAD",
                probe_url,
                headers=headers,
                timeout=self._STORAGE_PROXY_PROBE_TIMEOUT,
            )
            return response.status_code == 200
        except Exception:
            return False

    def _authenticated_session(self) -> requests.Session:
        """Returns an HTTP session with SDK auth for direct Files API data requests.

        Unlike _cloud_provider_session (which has no auth), this session includes the SDK authentication
        callback so that every request carries valid credentials. The session is created on first call and
        cached for reuse.
        """
        with self._authenticated_session_lock:
            if self._cached_authenticated_session is not None:
                return self._cached_authenticated_session
            session = requests.Session()
            config = self._config

            def authenticate(r: requests.PreparedRequest) -> requests.PreparedRequest:
                auth_headers = config.authenticate()
                r.headers.update(auth_headers)
                return r

            session.auth = authenticate
            http_adapter = requests.adapters.HTTPAdapter(
                config.max_connection_pools or 20,
                config.max_connections_per_pool or 20,
                pool_block=True,
            )
            session.mount("https://", http_adapter)
            session.mount("http://", http_adapter)
            self._cached_authenticated_session = session
            return session

    def _upload_endpoints(self) -> list[_Endpoint]:
        """The endpoints an upload walks, in order.

        A list with only IO_OFFLOAD gets the Files API on the workspace host, which every workspace serves: small and
        empty files need a single-shot upload, which presigned URLs can't take.
        """
        endpoints = self._transfer_endpoints()
        if all(e.kind == _ResolvedEndpoint.IO_OFFLOAD for e in endpoints):
            endpoints.append(
                _Endpoint(_ResolvedEndpoint.FILES_API_V2, self._config.host, multipart_upload_supported=False)
            )
        return endpoints

    def download(
        self,
        file_path: str,
    ) -> DownloadResponse:
        """Download a file.

        Downloads a file as a stream into memory.

        Use this when you want to process the downloaded file in memory or pipe it into another system. Supports files of any size in SDK v0.72.0+. Earlier versions have a 5 GB file size limit.

        If the download is successful, the function returns the downloaded file result. If the download is unsuccessful, the function raises an exception.

        :param file_path: str
          The remote path of the file, e.g. /Volumes/path/to/your/file

        :returns: :class:`DownloadResponse`
        """
        if self._config.disable_experimental_files_api_client:
            _LOG.info("Disable experimental files API client, will use the original download method.")
            return super().download(file_path)

        stream = _WalkingDownloadStream(self._clients_for(self._transfer_endpoints()), file_path)
        return DownloadResponse(
            content_length=stream.content_length_opt,
            content_type=stream.content_type_opt,
            last_modified=stream.last_modified_opt,
            contents=_StreamingResponse(stream),
        )

    def download_to(
        self,
        file_path: str,
        destination: str,
        *,
        overwrite: bool = True,
        use_parallel: bool = False,
        parallelism: Optional[int] = None,
    ) -> DownloadFileResult:
        """Downloads a file directly to a local file path.

        Use this when you want to write the file straight to disk instead of holding it in memory. Supports files of any size in SDK v0.72.0+. Earlier versions have a 5 GB file size limit.

        Supports parallel download (use_parallel=True), which may improve performance for large files. This is available on all operating systems except Windows.

        :param file_path: str
          The remote path of the file, e.g. /Volumes/path/to/your/file
        :param destination: str
          The local path where the file will be saved. A new file is written next to it and moved into place when the
          download completes; an existing destination is written in place.
        :param overwrite: bool
          If true, an existing file will be overwritten. When not specified, defaults to True.
        :param use_parallel: bool
          If true, the download will be performed using multiple threads.
        :param parallelism: int
          The number of parallel threads to use for downloading. If not specified, defaults to the number of CPU cores.

        :returns: :class:`DownloadFileResult`
        """
        if self._config.disable_experimental_files_api_client:
            raise NotImplementedError(
                "Experimental files API features are disabled, download_to is not supported. Please use download instead."
            )

        # The existence of the target file is checked before starting the download. This is a best-effort check
        # to avoid overwriting an existing file. However, there is nothing preventing a file from being created
        # at the destination path after this check and before the file is written, and no way to prevent other
        # actor from writing to the destination path concurrently.
        if not overwrite and os.path.exists(destination):
            raise FileExistsError(destination)
        if os.path.isdir(destination):
            raise IsADirectoryError(destination)
        if use_parallel and not _DownloadDestination.takes_ranges(destination):
            _LOG.debug(f"{destination} is not a regular file, so it is downloaded sequentially")
            use_parallel = False
        ranges = [_ByteRange(0, None)]
        size_opt = None
        last_modified = None
        if use_parallel:
            # Parallel download is not supported for Windows due to the limit of only one open file handle
            # for writing. If parallel download is requested on Windows, fall back to sequential download with
            # a warning.
            if platform.system() == "Windows":
                _LOG.warning("Parallel download is not supported on Windows. Falling back to sequential download.")
                use_parallel = False
            else:
                if parallelism is None:
                    parallelism = self._config.files_ext_parallel_download_default_parallelism
                if parallelism < 1 or parallelism > 64:
                    raise ValueError("parallelism must be between 1 and 64")
                file_info = self.get_metadata(file_path)
                last_modified = file_info.last_modified
                part_size = self._config.files_ext_parallel_download_default_part_size
                # A file under the threshold, or that fits one range, is downloaded whole: a range covering the
                # whole file may be answered with 200 instead of 206.
                if file_info.content_length > max(self._config.files_ext_parallel_download_min_file_size, part_size):
                    size_opt = file_info.content_length
                    ranges = _split_into_ranges(file_info.content_length, part_size)
        target = _DownloadDestination.create(destination, size_opt)
        try:
            _walk_endpoints(
                self._clients_for(self._transfer_endpoints()),
                functools.partial(
                    _download_ranges_to_file,
                    path=file_path,
                    ranges=ranges,
                    last_modified=last_modified,
                    destination=target,
                    parallelism=parallelism if size_opt is not None else 1,
                ),
            )
            target.finish()
        except BaseException:
            target.discard()
            raise
        return DownloadFileResult()

    def _get_optimized_performance_parameters_for_upload(
        self, content_length: Optional[int], part_size_overwrite: Optional[int]
    ) -> (int, int):
        """Get optimized part size and batch size for upload based on content length and provided part size.

        Returns tuple of (part_size, batch_size).
        """
        chosen_part_size = None

        # 1. decide on the part size
        if part_size_overwrite is not None:  # If a part size is provided, we use it directly after validation.
            if part_size_overwrite > self._config.files_ext_multipart_upload_max_part_size:
                raise ValueError(
                    f"Part size {part_size_overwrite} exceeds maximum allowed size {self._config.files_ext_multipart_upload_max_part_size} bytes."
                )
            chosen_part_size = part_size_overwrite
            _LOG.debug(f"Using provided part size: {chosen_part_size} bytes")
        else:  # If no part size is provided, we will optimize based on the content length.
            if content_length is not None:
                # Choosing the smallest part size that allows for a maximum of 100 parts.
                for part_size in self._config.files_ext_multipart_upload_part_size_options:
                    part_num = (content_length + part_size - 1) // part_size
                    if part_num <= 100:
                        chosen_part_size = part_size
                        _LOG.debug(
                            f"Optimized part size for upload: {chosen_part_size} bytes for content length {content_length} bytes"
                        )
                        break
                if chosen_part_size is None:  # If no part size was chosen, we default to the maximum allowed part size.
                    chosen_part_size = self._config.files_ext_multipart_upload_max_part_size

        # Use defaults if not determined yet
        if chosen_part_size is None:
            chosen_part_size = self._config.files_ext_multipart_upload_default_part_size

        # 2. decide on the batch size
        if content_length is not None and chosen_part_size is not None:
            part_num = (content_length + chosen_part_size - 1) // chosen_part_size
            chosen_batch_size = int(
                math.ceil(math.sqrt(part_num))
            )  # Using the square root of the number of parts as a heuristic for batch size.
        else:
            chosen_batch_size = self._config.files_ext_multipart_upload_batch_url_count

        return chosen_part_size, chosen_batch_size

    def upload(
        self,
        file_path: str,
        contents: BinaryIO,
        *,
        overwrite: Optional[bool] = None,
        part_size: Optional[int] = None,
        use_parallel: bool = True,
        parallelism: Optional[int] = None,
    ) -> UploadStreamResult:
        """
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
        """
        if self._config.disable_experimental_files_api_client:
            _LOG.info("Disable experimental files API client, will use the original upload method.")
            super().upload(file_path=file_path, contents=contents, overwrite=overwrite)
            return UploadStreamResult()

        _LOG.debug("Uploading file from BinaryIO stream")
        if parallelism is not None and not use_parallel:
            raise ValueError("parallelism can only be set if use_parallel is True")
        if parallelism is None and use_parallel:
            parallelism = self._config.files_ext_multipart_upload_default_parallelism

        data = _UploadData.from_stream(contents)
        part_size, batch_size = self._get_optimized_performance_parameters_for_upload(data.size_opt, part_size)
        if data.size_opt is None:
            # A one-pass stream's size is only known once read: a short one is sent in a single shot.
            data.read_ahead(self._config.files_ext_multipart_upload_min_stream_size)
        self._upload(file_path, data, overwrite, part_size, batch_size, use_parallel, parallelism)
        return UploadStreamResult()

    def upload_from(
        self,
        file_path: str,
        source_path: str,
        *,
        overwrite: Optional[bool] = None,
        part_size: Optional[int] = None,
        use_parallel: bool = True,
        parallelism: Optional[int] = None,
    ) -> UploadFileResult:
        """
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
        """
        if self._config.disable_experimental_files_api_client:
            raise NotImplementedError(
                "Experimental files API features are disabled, upload_from is not supported. Please use upload instead."
            )

        _LOG.debug(f"Uploading file from local path: {source_path}")

        if parallelism is not None and not use_parallel:
            raise ValueError("parallelism can only be set if use_parallel is True")
        if parallelism is None and use_parallel:
            parallelism = self._config.files_ext_multipart_upload_default_parallelism
        data = _UploadData.from_file(source_path)
        part_size, batch_size = self._get_optimized_performance_parameters_for_upload(data.size_opt, part_size)
        self._upload(file_path, data, overwrite, part_size, batch_size, use_parallel, parallelism)
        return UploadFileResult()

    def _upload(
        self,
        file_path: str,
        data: _UploadData,
        overwrite: Optional[bool],
        part_size: int,
        batch_size: int,
        use_parallel: bool,
        parallelism: Optional[int],
    ) -> None:
        clients = self._clients_for(self._upload_endpoints())
        plans = {}
        too_large = []
        for client in clients:
            plan_opt = _plan_upload(
                data,
                client,
                use_parallel,
                parallelism,
                part_size,
                batch_size,
                self._config.files_ext_multipart_upload_min_stream_size,
            )
            if plan_opt is not None:
                plans[client] = plan_opt
            elif client.max_single_shot_size_opt is not None:
                too_large.append(client.name)
        if not plans and too_large:
            data.close()
            raise ValueError(
                f"No endpoint can take this upload of {data.size_opt} bytes: {', '.join(too_large)} takes a single "
                "request of at most 5 GiB, and no endpoint for multipart uploads is available"
            )
        try:
            _walk_endpoints(
                list(plans),
                functools.partial(_upload_to, plans=plans, path=file_path, overwrite_opt=overwrite, data=data),
                can_send_again=data.can_send_again,
                before_next_endpoint=data.restart,
                retries_before_commit=_UPLOAD_RETRIES_BEFORE_COMMIT,
            )
        finally:
            data.close()

    def _clients_for(self, endpoints: list[_Endpoint]) -> list:
        """One client per endpoint, built per transfer. The only place transfers branch on the endpoint kind."""
        clients = []
        for endpoint in endpoints:
            if endpoint.kind == _ResolvedEndpoint.IO_OFFLOAD:
                clients.append(_PresignedEndpointClient(self, endpoint))
            else:
                clients.append(_FilesApiV2EndpointClient(self, endpoint))
        return clients

    def _api_client_budget(self) -> _RetryBudget:
        """The API client's budget: no attempt cap, retry_timeout_seconds in all."""
        return _RetryBudget(None, timedelta(seconds=self._config.retry_timeout_seconds or 300))

    def _cloud_budget(self) -> _RetryBudget:
        """The bounded budget for hosts other than the workspace, so a failing host gives way to the next quickly."""
        return _RetryBudget(
            self._config.experimental_files_ext_cloud_api_max_retries,
            timedelta(seconds=self._config.retry_timeout_seconds or 300),
        )

    def _resume_budget(self) -> _RetryBudget:
        """How often a download may resume after a break: in all, and in a row without progress."""
        return _RetryBudget(
            self._config.files_ext_client_download_max_total_recovers,
            timedelta(seconds=self._config.retry_timeout_seconds or 300),
            self._config.files_ext_client_download_max_total_recovers_without_progressing,
        )

    @staticmethod
    def _upload_response_error(response: requests.Response) -> Exception:
        """Maps an unsuccessful part upload response to the error to raise."""
        message = f"Unsuccessful chunk upload. Response status: {response.status_code}, body: {response.content}"
        return FilesExt._response_error(response, message)

    @staticmethod
    def _response_error(response: requests.Response, message: str) -> Exception:
        """Maps an unsuccessful data-plane response to an SDK error, keeping a Databricks JSON error if it has one."""
        try:
            body = response.json()
        except ValueError:
            body = None
        if isinstance(body, dict) and ("error_code" in body or "message" in body):
            return _error_mapper(response, body)
        return _error_mapper(response, {"message": message})

    @staticmethod
    def _is_url_expired_response(response: requests.Response) -> bool:
        """
        Checks if response matches one of the known "URL expired" responses from the cloud storage providers.
        """
        if response.status_code not in (400, 403):
            return False

        try:
            xml_root = ET.fromstring(response.content)
            if xml_root.tag != "Error":
                return False

            code = xml_root.find("Code")
            if code is None:
                return False

            if code.text == "ExpiredToken":
                # GCP, and AWS when the URL was signed with temporary credentials that have since expired.
                return True

            if code.text == "AuthenticationFailed":
                # Azure
                details = xml_root.find("AuthenticationErrorDetail")
                if details is not None and "Signature not valid in the specified time frame" in details.text:
                    return True

            if code.text == "AccessDenied":
                # AWS
                message = xml_root.find("Message")
                if message is not None and message.text == "Request has expired":
                    return True

        except ET.ParseError:
            pass

        return False

    def _get_rfc339_timestamp_with_future_offset(self, base_time: datetime.datetime, offset: timedelta) -> str:
        """Generates an offset timestamp in an RFC3339 format suitable for URL generation"""
        offset_timestamp = base_time + offset
        # From Google Protobuf doc:
        # In JSON format, the Timestamp type is encoded as a string in the
        #   * [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) format. That is, the
        #   * format is "{year}-{month}-{day}T{hour}:{min}:{sec}[.{frac_sec}]Z"
        return offset_timestamp.strftime("%Y-%m-%dT%H:%M:%SZ")

    def _get_upload_url_expire_time(self) -> str:
        """Generates expiration time in the required format."""
        current_time = datetime.datetime.now(datetime.timezone.utc)
        return self._get_rfc339_timestamp_with_future_offset(
            current_time, self._config.files_ext_multipart_upload_url_expiration_duration
        )

    def _get_download_url_expire_time(self) -> str:
        """Generates expiration time in the required format."""
        current_time = datetime.datetime.now(datetime.timezone.utc)
        return self._get_rfc339_timestamp_with_future_offset(
            current_time, self._config.files_ext_presigned_download_url_expiration_duration
        )

    def _cloud_provider_session(self) -> requests.Session:
        """Returns an unauthenticated session for presigned URL operations.

        Presigned URLs already carry their authorization. The session is created on first call and cached for
        reuse.
        """
        with self._cloud_provider_session_lock:
            if self._cached_cloud_provider_session is None:
                session = requests.Session()
                # Following session config in _BaseClient.
                http_adapter = requests.adapters.HTTPAdapter(
                    self._config.max_connection_pools or 20,
                    self._config.max_connections_per_pool or 20,
                    pool_block=True,
                )
                session.mount("https://", http_adapter)
                session.mount("http://", http_adapter)
                self._cached_cloud_provider_session = session
        return self._cached_cloud_provider_session


def _origin(url: str) -> tuple[str, str, Optional[int]]:
    """The scheme, host and port of a URL, normalized so that two spellings of one origin compare equal."""
    parsed = parse.urlsplit(url)
    scheme = parsed.scheme.lower()
    return scheme, (parsed.hostname or "").lower(), parsed.port or {"http": 80, "https": 443}.get(scheme)


def _optional_int(value: Optional[str]) -> Optional[int]:
    return int(value) if value is not None else None


# ======================== Endpoint clients ========================
#
# One client per endpoint, built per transfer by FilesExt._clients_for. A client talks to one endpoint: it decides what
# each failure means, retries locally, and hands back only walk or raise (see _retry in files_utils).


class _SingleAttemptApi:
    """Sends one request through the workspace API client's session and error parsing, without its retries: the
    endpoint client retries."""

    def __init__(self, api):
        self._api = api

    def _request(
        self, method: str, url: str, query=None, headers=None, body=None, raw: bool = False, data=None
    ) -> requests.Response:
        api_client = self._api._api_client
        headers = {**self._api._cfg._custom_headers, **(headers or {})}
        headers["User-Agent"] = api_client._user_agent_base
        # An empty body stays as is, as requests would send an empty stream chunked.
        if isinstance(data, (str, bytes)) and data:
            data = BytesIO(data.encode("utf-8") if isinstance(data, str) else data)
        json_data = None
        if body is not None and data is None:
            json_data = json.dumps(body, allow_nan=False, default=_json_default)
            headers = {"Content-Type": "application/json", **headers}
        # ApiClient._perform without raising, so that deciding can use the status code.
        response = api_client._session.request(
            method,
            url,
            params=api_client._fix_query_string(query),
            headers=headers,
            data=json_data if json_data is not None else data,
            stream=raw,
            timeout=api_client._http_timeout_seconds,
        )
        api_client._record_request_log(response, raw=raw or data is not None)
        error = api_client._error_parser.get_api_error(response)
        if error is not None:
            raise _RequestFailed(error, response.status_code)
        return response

    def do(
        self,
        method: str,
        path: Optional[str] = None,
        url: Optional[str] = None,
        query=None,
        headers=None,
        body=None,
        data=None,
    ) -> dict:
        """Like ApiClient.do, for JSON responses."""
        if url is None:
            path = re.sub("^/api/2.0/fs/files//", "/api/2.0/fs/files/", path)
            url = f"{self._api._cfg.host}{path}"
        response = self._request(method, url, query=query, headers=headers, body=body, data=data)
        if not len(response.content):
            return {}
        json_response = response.json()
        if json_response is None:
            return {}
        if isinstance(json_response, list):
            return json_response
        return json_response

    def get_stream(self, url: str, headers: dict) -> requests.Response:
        return self._request("GET", url, headers=headers, raw=True)


def _send_multipart_abort(session: requests.Session, url: str, params: dict, timeout: float) -> None:
    """Aborts a multipart upload session. Best-effort, so sent once."""
    abort_response = session.request("POST", url, params=params, timeout=timeout)
    if not abort_response.ok:
        raise ValueError(abort_response)


def _header(response, name: str) -> Optional[str]:
    """A response header, from a requests response or a test double with a plain dict of headers."""
    value = response.headers.get(name)
    if value is None:
        value = response.headers.get(name.lower())
    return None if value is None else str(value)


def _range_headers(byte_range: _ByteRange, if_unmodified_since_opt: Optional[str]) -> dict[str, str]:
    headers = {"Accept": "application/octet-stream"}
    if not byte_range.is_whole_file():
        headers["Range"] = byte_range.header()
    if if_unmodified_since_opt:
        headers["If-Unmodified-Since"] = if_unmodified_since_opt
    return headers


def _range_response(response, chunk_size: Optional[int]) -> _RangeResponse:
    chunks = response.iter_content(chunk_size=chunk_size, decode_unicode=False)

    def close() -> None:
        for closable in (chunks, response):
            close_it = getattr(closable, "close", None)
            if close_it is not None:
                close_it()

    return _RangeResponse(
        status_code=response.status_code,
        content_length_opt=_optional_int(_header(response, "Content-Length")),
        content_type_opt=_header(response, "Content-Type"),
        last_modified_opt=_header(response, "Last-Modified"),
        chunks=chunks,
        close=close,
    )


def _check_range(requested: _ByteRange, response, expected_length_opt: Optional[int], source: str) -> None:
    """A requested range must come back as a 206, or as a 200 of exactly the requested length.

    A 200 with the whole file must not be written at the range's offset.
    """
    if requested.is_whole_file() or response.status_code == 206:
        return
    if response.status_code == 200 and expected_length_opt is not None:
        if _optional_int(_header(response, "Content-Length")) == expected_length_opt:
            return
    close = getattr(response, "close", None)
    if close is not None:
        close()
    raise ValueError(f"Received {response.status_code} from {source} for {requested.header()}")


class _PresignedDownloadUrls:
    """The presigned URL every range of one download shares: created on first use, replaced once it expires.

    A failure to create it is kept, so that every range sees the same failure and none can commit an endpoint that is
    failing.
    """

    def __init__(self, mint: Callable[[], Union[CreateDownloadUrlResponse, _Failure]]):
        def get_new_url() -> CreateDownloadUrlResponse:
            result = mint()
            if isinstance(result, _Failure):
                raise _RequestFailed(result.error, decision_opt=result.decision)
            return result

        self._distributor = _PresignedUrlDistributor(get_new_url)
        self._failure_opt: Optional[_RequestFailed] = None
        self._lock = Lock()

    def url_for(self) -> tuple[CreateDownloadUrlResponse, int]:
        with self._lock:
            if self._failure_opt is not None:
                raise self._failure_opt
        try:
            return self._distributor.get_url()
        except _RequestFailed as e:
            with self._lock:
                self._failure_opt = e
            raise

    def invalidate(self, version: int) -> None:
        self._distributor.invalidate_url(version)


class _PresignedEndpointClient:
    """IO_OFFLOAD: data goes to presigned URLs on cloud storage, without credentials; sessions and URLs come from Files
    API 2.0 on the workspace host. No single-shot upload."""

    supports_single_shot = False
    max_single_shot_size_opt: Optional[int] = None
    max_part_size_opt: Optional[int] = None

    def __init__(self, ext: "FilesExt", endpoint: _Endpoint):
        self._ext = ext
        self._endpoint = endpoint
        self._config = ext._config
        self.name = f"{endpoint.kind.value} at {endpoint.base_url}"
        self.supports_multipart = endpoint.multipart_upload_supported
        self._api = _SingleAttemptApi(ext._api)
        self._builder = _PresignedUrlRequestBuilder(self._api, endpoint.base_url)
        self._download_urls: dict[str, _PresignedDownloadUrls] = {}
        self._lock = Lock()

    def _control(self, send: Callable, status: _TransferStatus):
        """A call to the host that coordinates the presigned URLs: the API client's budget on the workspace host and
        the bounded one elsewhere."""
        on_workspace = _origin(self._endpoint.base_url) == _origin(self._config.host)
        budget = self._ext._api_client_budget() if on_workspace else self._ext._cloud_budget()
        return _retry(send, _common_decision, budget, status, self._config.clock)

    @staticmethod
    def _decide(failure: BaseException) -> str:
        if isinstance(failure, _UrlExpired):
            # Not retried here: the caller replaces the URL, up to its own limit.
            return "walk"
        return _common_decision(failure)

    def _download_url_provider(self, path: str, status: _TransferStatus) -> _PresignedDownloadUrls:
        with self._lock:
            if path not in self._download_urls:
                self._download_urls[path] = _PresignedDownloadUrls(
                    lambda: self._control(
                        lambda: self._builder.build_download_url(path, self._ext._get_download_url_expire_time()),
                        status,
                    )
                )
            return self._download_urls[path]

    def _get_once(
        self,
        urls: _PresignedDownloadUrls,
        requested: _ByteRange,
        if_unmodified_since_opt: Optional[str],
        expected_length_opt: Optional[int],
    ) -> _RangeResponse:
        url, version = urls.url_for()
        added_headers = _range_headers(requested, if_unmodified_since_opt)
        header_overlap = added_headers.keys() & url.headers.keys()
        if header_overlap:
            raise ValueError(
                f"Provided headers overlap with required headers from the CSP API bundle: {header_overlap}"
            )
        response = self._ext._cloud_provider_session().request(
            "GET",
            url.url,
            headers={**added_headers, **url.headers},
            timeout=self._config.files_ext_network_transfer_inactivity_timeout_seconds,
            stream=True,
        )
        if response.status_code in (200, 201, 206):
            _check_range(requested, response, expected_length_opt, "presigned URL")
            return _range_response(response, self._config.files_ext_client_download_streaming_chunk_size)
        if FilesExt._is_url_expired_response(response):
            _LOG.info("Presigned URL expired, fetching a new one.")
            urls.invalidate(version)
            raise _UrlExpired("The presigned download URL expired")
        message = f"Unsuccessful download. Response status: {response.status_code}, body: {response.content}"
        raise _RequestFailed(_error_mapper(response, {"message": message}), response.status_code)

    # Download: opens one byte range. Used by download() and download_to().
    def get_file_range(
        self, path: str, byte_range: _ByteRange, if_unmodified_since_opt: Optional[str], status: _TransferStatus
    ) -> Union[_ResilientDownload, _Failure]:
        urls = self._download_url_provider(path, status)
        budget = self._ext._cloud_budget()

        def get_file_range(requested, if_unmodified_since_opt, expected_length_opt, status):
            refreshes = 0
            while True:
                result = _retry(
                    lambda: self._get_once(urls, requested, if_unmodified_since_opt, expected_length_opt),
                    self._decide,
                    budget,
                    status,
                    self._config.clock,
                )
                if not (isinstance(result, _Failure) and isinstance(result.error, _UrlExpired)):
                    return result
                if refreshes >= self._config.files_ext_parallel_download_max_retries:
                    return _Failure(
                        ValueError(
                            "Exceeded maximum retries for downloading with presigned URL: URL expired too many times"
                        ),
                        "walk",
                    )
                refreshes += 1

        download = _ResilientDownload(
            get_file_range, self._ext._resume_budget(), status, byte_range, if_unmodified_since_opt
        )
        return download.open() or download

    # Single-shot upload: presigned URLs have none.
    def put_file(self, path, overwrite_opt, data, status) -> Optional[_Failure]:
        raise NotImplementedError("The offload path has no single-shot upload")

    # Multipart upload: opens an upload session.
    def initiate_upload(
        self, path: str, overwrite_opt: Optional[bool], status: _TransferStatus, part_url_batch_size: int = 1
    ) -> Union[_MultipartUploadSession, _Failure]:
        query: dict = {"action": "initiate-upload"}
        if overwrite_opt is not None:
            query["overwrite"] = overwrite_opt
        response = self._control(
            lambda: self._api.do("POST", url=FilesExt._files_api_url(self._endpoint, path), query=query), status
        )
        if isinstance(response, _Failure):
            return response
        try:
            if response.get("multipart_upload"):
                session_token = response["multipart_upload"].get("session_token")
                if not session_token:
                    raise ValueError(f"Unexpected server response: {response}")
                return _PresignedMultipartSession(self, path, session_token, part_url_batch_size)
            raise ValueError(f"Unexpected server response: {response}")
        except (ValueError, KeyError, TypeError, AttributeError) as e:
            return _Failure(e, "walk")


class _PresignedMultipartSession(_MultipartUploadSession):
    """A multipart upload whose parts go to presigned URLs, requested from the workspace a batch at a time."""

    def __init__(self, client: _PresignedEndpointClient, path: str, session_token: str, batch_size: int):
        self._client = client
        self._ext = client._ext
        self._path = path
        self._session_token = session_token
        self._batch_size = batch_size
        self._urls: dict[int, _PresignedUrl] = {}
        self._failure_opt: Optional[_Failure] = None
        self._lock = Lock()

    def _part_url(self, number: int, status: _TransferStatus) -> Union[_PresignedUrl, _Failure]:
        with self._lock:
            if self._failure_opt is not None:
                return self._failure_opt
            url = self._urls.get(number)
        if url is not None:
            return url
        result = self._client._control(
            lambda: self._client._builder.build_upload_part_urls(
                self._path, self._session_token, number, self._batch_size, self._ext._get_upload_url_expire_time()
            ),
            status,
        )
        with self._lock:
            if isinstance(result, _Failure):
                self._failure_opt = result
                return result
            for part_url in result:
                self._urls[part_url.part_number] = part_url
            url = self._urls.get(number)
            if url is None:
                self._failure_opt = _Failure(
                    ValueError(f"Unexpected server response: no URL for part {number}"), "walk"
                )
                return self._failure_opt
            return url

    def _put_once(self, number: int, data: bytes, status: _TransferStatus) -> str:
        url = self._part_url(number, status)
        if isinstance(url, _Failure):
            raise _RequestFailed(url.error, decision_opt=url.decision)
        _LOG.debug(f"Uploading part {number}")
        response = self._ext._cloud_provider_session().request(
            "PUT",
            url.url,
            headers=url.headers,
            data=BytesIO(data),
            timeout=self._ext._config.files_ext_network_transfer_inactivity_timeout_seconds,
        )
        if response.status_code in (200, 201):
            return response.headers.get("ETag", "")
        if FilesExt._is_url_expired_response(response):
            _LOG.debug("Upload URL expired, retrying...")
            with self._lock:
                self._urls.pop(number, None)
            raise _UrlExpired("The presigned upload URL expired")
        raise _RequestFailed(FilesExt._upload_response_error(response), response.status_code)

    def put_part(self, number: int, data: bytes, status: _TransferStatus) -> Union[str, _Failure]:
        refreshes = 0
        while True:
            result = _retry(
                lambda: self._put_once(number, data, status),
                self._client._decide,
                self._ext._cloud_budget(),
                status,
                self._ext._config.clock,
            )
            if not (isinstance(result, _Failure) and isinstance(result.error, _UrlExpired)):
                return result
            if refreshes >= self._ext._config.files_ext_multipart_upload_max_retries:
                # Don't confuse user with unrelated "Permission denied" error.
                return _Failure(
                    ValueError(f"Unsuccessful chunk upload: upload URL expired after {refreshes} retries"), "walk"
                )
            refreshes += 1

    def complete(self, etags: dict, status: _TransferStatus) -> Optional[_Failure]:
        query = {"action": "complete-upload", "upload_type": "multipart", "session_token": self._session_token}
        body = {"parts": [{"part_number": n, "etag": etag} for n, etag in sorted(etags.items())]}
        result = self._client._control(
            lambda: self._client._api.do(
                "POST",
                url=FilesExt._files_api_url(self._client._endpoint, self._path),
                query=query,
                headers={"Content-Type": "application/json"},
                body=body,
            ),
            status,
        )
        return result if isinstance(result, _Failure) else None

    def abort(self) -> None:
        try:
            _send_multipart_abort(
                self._ext._authenticated_session(),
                FilesExt._files_api_url(self._client._endpoint, self._path),
                {"action": "abort-upload", "upload_type": "multipart", "session_token": self._session_token},
                self._ext._config.files_ext_network_transfer_inactivity_timeout_seconds,
            )
        except Exception as ex:
            _LOG.warning(f"Failed to abort upload: {ex}")


class _FilesApiV2EndpointClient:
    """FILES_API 2.0, on the workspace host or the storage proxy. Requests go to the host with workspace credentials:
    on the workspace with the API client's budget, elsewhere with the bounded budget."""

    supports_single_shot = True

    def __init__(self, ext: "FilesExt", endpoint: _Endpoint):
        self._ext = ext
        self._endpoint = endpoint
        self._config = ext._config
        self.name = f"{endpoint.kind.value} at {endpoint.base_url}"
        self.supports_multipart = endpoint.multipart_upload_supported
        self._on_workspace = ext._uses_api_client(endpoint)
        self._api = _SingleAttemptApi(ext._api)
        self._builder = ext._request_builder_for(endpoint)

    @property
    def max_single_shot_size_opt(self) -> Optional[int]:
        # The storage proxy forwards the body to the cloud, whose own single-request limit applies.
        return _WORKSPACE_MAX_SINGLE_SHOT_SIZE if self._on_workspace else None

    @property
    def max_part_size_opt(self) -> Optional[int]:
        return None

    def _budget(self) -> _RetryBudget:
        return self._ext._api_client_budget() if self._on_workspace else self._ext._cloud_budget()

    def _control(self, send: Callable, status: _TransferStatus):
        return _retry(send, _common_decision, self._budget(), status, self._config.clock)

    def _get_once(
        self,
        url: str,
        requested: _ByteRange,
        if_unmodified_since_opt: Optional[str],
        expected_length_opt: Optional[int],
    ) -> _RangeResponse:
        headers = _range_headers(requested, if_unmodified_since_opt)
        if self._on_workspace:
            response = self._api.get_stream(url, headers)
            chunk_size = self._ext._api._api_client._streaming_buffer_size
        else:
            response = self._ext._authenticated_session().request(
                "GET",
                url,
                headers=headers,
                timeout=self._config.files_ext_network_transfer_inactivity_timeout_seconds,
                stream=True,
            )
            chunk_size = self._config.files_ext_client_download_streaming_chunk_size
            if response.status_code not in (200, 201, 206):
                message = f"Unsuccessful download. Response status: {response.status_code}, body: {response.content}"
                raise _RequestFailed(_error_mapper(response, {"message": message}), response.status_code)
        _check_range(requested, response, expected_length_opt, "the Files API")
        return _range_response(response, chunk_size)

    # Download: opens one byte range. Used by download() and download_to().
    def get_file_range(
        self, path: str, byte_range: _ByteRange, if_unmodified_since_opt: Optional[str], status: _TransferStatus
    ) -> Union[_ResilientDownload, _Failure]:
        url = FilesExt._files_api_url(self._endpoint, path)

        def get_file_range(requested, if_unmodified_since_opt, expected_length_opt, status):
            return self._control(
                lambda: self._get_once(url, requested, if_unmodified_since_opt, expected_length_opt), status
            )

        download = _ResilientDownload(
            get_file_range, self._ext._resume_budget(), status, byte_range, if_unmodified_since_opt
        )
        return download.open() or download

    # Single-shot upload: one PUT of the whole file. Used for small files and endpoints without multipart.
    def put_file(
        self, path: str, overwrite_opt: Optional[bool], data: _UploadData, status: _TransferStatus
    ) -> Optional[_Failure]:
        query = {}
        if overwrite_opt is not None:
            query["overwrite"] = overwrite_opt
        headers = {"Content-Type": "application/octet-stream"}
        if self._config.workspace_id:
            headers["X-Databricks-Workspace-Id"] = self._config.workspace_id
        url = FilesExt._files_api_url(self._endpoint, path)

        def send() -> None:
            # requests sends an empty stream chunked, without the Content-Length these hosts require.
            body = b"" if data.size_opt == 0 else data.whole()
            if self._on_workspace:
                self._api.do("PUT", url=url, query=query, headers=headers, data=body)
                return
            response = self._ext._authenticated_session().request(
                "PUT",
                url,
                params=_BaseClient._fix_query_string(query),
                headers=headers,
                data=body,
                timeout=self._config.files_ext_network_transfer_inactivity_timeout_seconds,
            )
            if response.status_code == 412 and overwrite_opt is False:
                raise AlreadyExists("The file being created already exists.")
            if not response.ok:
                message = f"Unsuccessful single-shot upload. Response status: {response.status_code}"
                raise _RequestFailed(FilesExt._response_error(response, message), response.status_code)

        _LOG.debug("Using single-shot upload for input stream")
        budget = self._budget()
        result = _retry(send, _common_decision, budget, status, self._config.clock, can_retry_opt=data.can_send_again)
        return result if isinstance(result, _Failure) else None

    # Multipart upload: opens an upload session.
    def initiate_upload(
        self, path: str, overwrite_opt: Optional[bool], status: _TransferStatus, part_url_batch_size: int = 1
    ) -> Union[_MultipartUploadSession, _Failure]:
        query: dict = {"action": "initiate-upload"}
        if overwrite_opt is not None:
            query["overwrite"] = overwrite_opt
        response = self._control(
            lambda: self._api.do("POST", url=FilesExt._files_api_url(self._endpoint, path), query=query), status
        )
        if isinstance(response, _Failure):
            return response
        try:
            return self._session_from(response, path, overwrite_opt)
        except (ValueError, KeyError, TypeError, AttributeError) as e:
            return _Failure(e, "walk")

    def _session_from(self, response: dict, path: str, overwrite_opt: Optional[bool]):
        if response.get("multipart_upload"):
            session_token = response["multipart_upload"].get("session_token")
            if not session_token:
                raise ValueError(f"Unexpected server response: {response}")
            return _FilesApiMultipartSession(self, path, session_token)
        raise ValueError(f"Unexpected server response: {response}")

    def _complete_query(self, session_token: str) -> dict:
        return {"action": "complete-upload", "upload_type": "multipart", "session_token": session_token}

    def _abort_query(self, session_token: str) -> dict:
        return {"action": "abort-upload", "upload_type": "multipart", "session_token": session_token}


class _FilesApiMultipartSession(_MultipartUploadSession):
    """A multipart upload whose parts go straight to the Files API host, so there is no URL to presign or expire."""

    def __init__(self, client: _FilesApiV2EndpointClient, path: str, session_token: str):
        self._client = client
        self._ext = client._ext
        self._path = path
        self._session_token = session_token

    def _put_once(self, number: int, data: bytes) -> str:
        url = self._client._builder.build_upload_part_urls(
            self._path, self._session_token, number, 1, self._ext._get_upload_url_expire_time()
        )[0]
        response = self._ext._authenticated_session().request(
            "PUT",
            url.url,
            headers=url.headers,
            data=BytesIO(data),
            timeout=self._ext._config.files_ext_network_transfer_inactivity_timeout_seconds,
        )
        if response.status_code in (200, 201):
            return response.headers.get("ETag", "")
        raise _RequestFailed(FilesExt._upload_response_error(response), response.status_code)

    def put_part(self, number: int, data: bytes, status: _TransferStatus) -> Union[str, _Failure]:
        _LOG.debug(f"Uploading part {number}")
        budget = self._ext._cloud_budget()
        return _retry(lambda: self._put_once(number, data), _common_decision, budget, status, self._ext._config.clock)

    def complete(self, etags: dict, status: _TransferStatus) -> Optional[_Failure]:
        body = {"parts": [{"part_number": n, "etag": etag} for n, etag in sorted(etags.items())]}
        result = self._client._control(
            lambda: self._client._api.do(
                "POST",
                url=FilesExt._files_api_url(self._client._endpoint, self._path),
                query=self._client._complete_query(self._session_token),
                headers={"Content-Type": "application/json"},
                body=body,
            ),
            status,
        )
        return result if isinstance(result, _Failure) else None

    def abort(self) -> None:
        try:
            _send_multipart_abort(
                self._ext._authenticated_session(),
                FilesExt._files_api_url(self._client._endpoint, self._path),
                self._client._abort_query(self._session_token),
                self._ext._config.files_ext_network_transfer_inactivity_timeout_seconds,
            )
        except Exception as ex:
            _LOG.warning(f"Failed to abort upload: {ex}")
