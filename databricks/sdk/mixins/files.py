from __future__ import annotations

import base64
import datetime
import logging
import os
import pathlib
import platform
import re
import shutil
import sys
import xml.etree.ElementTree as ET
from abc import ABC, abstractmethod
from collections import deque
from collections.abc import Iterator
from datetime import timedelta
from io import BytesIO
from types import TracebackType
from typing import (TYPE_CHECKING, AnyStr, BinaryIO, Callable, Generator,
                    Iterable, Optional, Type, Union)
from urllib import parse

import requests
import requests.adapters
from requests import RequestException

from .._base_client import _BaseClient, _RawResponse, _StreamingResponse
from .._property import _cached_property
from ..config import Config
from ..errors import AlreadyExists, NotFound
from ..errors.customizer import _RetryAfterCustomizer
from ..errors.mapper import _error_mapper
from ..retries import retried
from ..service import files
from ..service._internal import _escape_multi_segment_path_parameter
from ..service.files import DownloadResponse

if TYPE_CHECKING:
    from _typeshed import Self

_LOG = logging.getLogger(__name__)


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
            raise IOError(f"can open either for reading or writing")
        if read:
            self._status = api.get_status(path)
        elif write:
            self._created = api.create(path, overwrite=overwrite)
        else:
            raise IOError(f"need to open either for reading or writing")

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
            kw = {}
            if sys.version_info[:2] > (3, 7):
                kw["missing_ok"] = True
            self._path.unlink(**kw)

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


class FilesExt(files.FilesAPI):
    __doc__ = files.FilesAPI.__doc__

    # note that these error codes are retryable only for idempotent operations
    _RETRYABLE_STATUS_CODES = [408, 429, 500, 502, 503, 504]

    def __init__(self, api_client, config: Config):
        super().__init__(api_client)
        self._config = config.copy()
        self._multipart_upload_read_ahead_bytes = 1

    def download(self, file_path: str) -> DownloadResponse:
        """Download a file.

        Downloads a file of any size. The file contents are the response body.
        This is a standard HTTP file download, not a JSON RPC.

        It is strongly recommended, for fault tolerance reasons,
        to iteratively consume from the stream with a maximum read(size)
        defined instead of using indefinite-size reads.

        :param file_path: str
          The remote path of the file, e.g. /Volumes/path/to/your/file

        :returns: :class:`DownloadResponse`
        """

        initial_response: DownloadResponse = self._open_download_stream(
            file_path=file_path,
            start_byte_offset=0,
            if_unmodified_since_timestamp=None,
        )

        wrapped_response = self._wrap_stream(file_path, initial_response)
        initial_response.contents._response = wrapped_response
        return initial_response

    def upload(self, file_path: str, contents: BinaryIO, *, overwrite: Optional[bool] = None):
        """Upload a file.

        Uploads a file. The file contents should be sent as the request body as raw bytes (an
        octet stream); do not encode or otherwise modify the bytes before sending. The contents of the
        resulting file will be exactly the bytes sent in the request body. If the request is successful, there
        is no response body.

        :param file_path: str
          The absolute remote path of the target file.
        :param contents: BinaryIO
        :param overwrite: bool (optional)
          If true, an existing file will be overwritten. When not specified, assumed True.
        """

        # Upload empty and small files with one-shot upload.
        pre_read_buffer = contents.read(self._config.multipart_upload_min_stream_size)
        if len(pre_read_buffer) < self._config.multipart_upload_min_stream_size:
            _LOG.debug(
                f"Using one-shot upload for input stream of size {len(pre_read_buffer)} below {self._config.multipart_upload_min_stream_size} bytes"
            )
            return super().upload(file_path=file_path, contents=BytesIO(pre_read_buffer), overwrite=overwrite)

        query = {"action": "initiate-upload"}
        if overwrite is not None:
            query["overwrite"] = overwrite

        # Method _api.do() takes care of retrying and will raise an exception in case of failure.
        initiate_upload_response = self._api.do(
            "POST", f"/api/2.0/fs/files{_escape_multi_segment_path_parameter(file_path)}", query=query
        )

        if initiate_upload_response.get("multipart_upload"):
            cloud_provider_session = self._create_cloud_provider_session()
            session_token = initiate_upload_response["multipart_upload"].get("session_token")
            if not session_token:
                raise ValueError(f"Unexpected server response: {initiate_upload_response}")

            try:
                self._perform_multipart_upload(
                    file_path, contents, session_token, pre_read_buffer, cloud_provider_session
                )
            except Exception as e:
                _LOG.info(f"Aborting multipart upload on error: {e}")
                try:
                    self._abort_multipart_upload(file_path, session_token, cloud_provider_session)
                except BaseException as ex:
                    _LOG.warning(f"Failed to abort upload: {ex}")
                    # ignore, abort is a best-effort
                finally:
                    # rethrow original exception
                    raise e from None

        elif initiate_upload_response.get("resumable_upload"):
            cloud_provider_session = self._create_cloud_provider_session()
            session_token = initiate_upload_response["resumable_upload"]["session_token"]
            self._perform_resumable_upload(
                file_path, contents, session_token, overwrite, pre_read_buffer, cloud_provider_session
            )
        else:
            raise ValueError(f"Unexpected server response: {initiate_upload_response}")

    def _perform_multipart_upload(
        self,
        target_path: str,
        input_stream: BinaryIO,
        session_token: str,
        pre_read_buffer: bytes,
        cloud_provider_session: requests.Session,
    ):
        """
        Performs multipart upload using presigned URLs on AWS and Azure:
        https://docs.aws.amazon.com/AmazonS3/latest/userguide/mpuoverview.html
        """
        current_part_number = 1
        etags: dict = {}

        # Why are we buffering the current chunk?
        # AWS and Azure don't support traditional "Transfer-encoding: chunked", so we must
        # provide each chunk size up front. In case of a non-seekable input stream we need
        # to buffer a chunk before uploading to know its size. This also allows us to rewind
        # the stream before retrying on request failure.
        # AWS signed chunked upload: https://docs.aws.amazon.com/AmazonS3/latest/API/sigv4-streaming.html
        # https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blobs-tune-upload-download-python#buffering-during-uploads

        chunk_offset = 0  # used only for logging

        # This buffer is expected to contain at least multipart_upload_chunk_size bytes.
        # Note that initially buffer can be bigger (from pre_read_buffer).
        buffer = pre_read_buffer

        retry_count = 0
        eof = False
        while not eof:
            # If needed, buffer the next chunk.
            buffer = FilesExt._fill_buffer(buffer, self._config.multipart_upload_chunk_size, input_stream)
            if len(buffer) == 0:
                # End of stream, no need to request the next block of upload URLs.
                break

            _LOG.debug(
                f"Multipart upload: requesting next {self._config.multipart_upload_batch_url_count} upload URLs starting from part {current_part_number}"
            )

            body: dict = {
                "path": target_path,
                "session_token": session_token,
                "start_part_number": current_part_number,
                "count": self._config.multipart_upload_batch_url_count,
                "expire_time": self._get_url_expire_time(),
            }

            headers = {"Content-Type": "application/json"}

            # Requesting URLs for the same set of parts is an idempotent operation, safe to retry.
            # Method _api.do() takes care of retrying and will raise an exception in case of failure.
            upload_part_urls_response = self._api.do(
                "POST", "/api/2.0/fs/create-upload-part-urls", headers=headers, body=body
            )

            upload_part_urls = upload_part_urls_response.get("upload_part_urls", [])
            if len(upload_part_urls) == 0:
                raise ValueError(f"Unexpected server response: {upload_part_urls_response}")

            for upload_part_url in upload_part_urls:
                buffer = FilesExt._fill_buffer(buffer, self._config.multipart_upload_chunk_size, input_stream)
                actual_buffer_length = len(buffer)
                if actual_buffer_length == 0:
                    eof = True
                    break

                url = upload_part_url["url"]
                required_headers = upload_part_url.get("headers", [])
                assert current_part_number == upload_part_url["part_number"]

                headers: dict = {"Content-Type": "application/octet-stream"}
                for h in required_headers:
                    headers[h["name"]] = h["value"]

                actual_chunk_length = min(actual_buffer_length, self._config.multipart_upload_chunk_size)
                _LOG.debug(
                    f"Uploading part {current_part_number}: [{chunk_offset}, {chunk_offset + actual_chunk_length - 1}]"
                )

                chunk = BytesIO(buffer[:actual_chunk_length])

                def rewind():
                    chunk.seek(0, os.SEEK_SET)

                def perform():
                    return cloud_provider_session.request(
                        "PUT",
                        url,
                        headers=headers,
                        data=chunk,
                        timeout=self._config.multipart_upload_single_chunk_upload_timeout_seconds,
                    )

                upload_response = self._retry_idempotent_operation(perform, rewind)

                if upload_response.status_code in (200, 201):
                    # Chunk upload successful

                    chunk_offset += actual_chunk_length

                    etag = upload_response.headers.get("ETag", "")
                    etags[current_part_number] = etag

                    # Discard uploaded bytes
                    buffer = buffer[actual_chunk_length:]

                    # Reset retry count when progressing along the stream
                    retry_count = 0

                elif FilesExt._is_url_expired_response(upload_response):
                    if retry_count < self._config.multipart_upload_max_retries:
                        retry_count += 1
                        _LOG.debug("Upload URL expired")
                        # Preserve the buffer so we'll upload the current part again using next upload URL
                    else:
                        # don't confuse user with unrelated "Permission denied" error.
                        raise ValueError(f"Unsuccessful chunk upload: upload URL expired")

                else:
                    message = f"Unsuccessful chunk upload. Response status: {upload_response.status_code}, body: {upload_response.content}"
                    _LOG.warning(message)
                    mapped_error = _error_mapper(upload_response, {})
                    raise mapped_error or ValueError(message)

                current_part_number += 1

        _LOG.debug(
            f"Completing multipart upload after uploading {len(etags)} parts of up to {self._config.multipart_upload_chunk_size} bytes"
        )

        query = {"action": "complete-upload", "upload_type": "multipart", "session_token": session_token}
        headers = {"Content-Type": "application/json"}
        body: dict = {}

        parts = []
        for etag in sorted(etags.items()):
            part = {"part_number": etag[0], "etag": etag[1]}
            parts.append(part)

        body["parts"] = parts

        # Completing upload is an idempotent operation, safe to retry.
        # Method _api.do() takes care of retrying and will raise an exception in case of failure.
        self._api.do(
            "POST",
            f"/api/2.0/fs/files{_escape_multi_segment_path_parameter(target_path)}",
            query=query,
            headers=headers,
            body=body,
        )

    @staticmethod
    def _fill_buffer(buffer: bytes, desired_min_size: int, input_stream: BinaryIO):
        """
        Tries to fill given buffer to contain at least `desired_min_size` bytes by reading from input stream.
        """
        bytes_to_read = max(0, desired_min_size - len(buffer))
        if bytes_to_read > 0:
            next_buf = input_stream.read(bytes_to_read)
            new_buffer = buffer + next_buf
            return new_buffer
        else:
            # we have already buffered enough data
            return buffer

    @staticmethod
    def _is_url_expired_response(response: requests.Response):
        """
        Checks if response matches one of the known "URL expired" responses from the cloud storage providers.
        """
        if response.status_code != 403:
            return False

        try:
            xml_root = ET.fromstring(response.content)
            if xml_root.tag != "Error":
                return False

            code = xml_root.find("Code")
            if code is None:
                return False

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

    def _perform_resumable_upload(
        self,
        target_path: str,
        input_stream: BinaryIO,
        session_token: str,
        overwrite: bool,
        pre_read_buffer: bytes,
        cloud_provider_session: requests.Session,
    ):
        """
        Performs resumable upload on GCP: https://cloud.google.com/storage/docs/performing-resumable-uploads
        """

        # Session URI we're using expires after a week

        # Why are we buffering the current chunk?
        # When using resumable upload API we're uploading data in chunks. During chunk upload
        # server responds with the "received offset" confirming how much data it stored so far,
        # so we should continue uploading from that offset. (Note this is not a failure but an
        # expected behaviour as per the docs.) But, input stream might be consumed beyond that
        # offset, since server might have read more data than it confirmed received, or some data
        # might have been pre-cached by e.g. OS or a proxy. So, to continue upload, we must rewind
        # the input stream back to the byte next to "received offset". This is not possible
        # for non-seekable input stream, so we must buffer the whole last chunk and seek inside
        # the buffer. By always uploading from the buffer we fully support non-seekable streams.

        # Why are we doing read-ahead?
        # It's not possible to upload an empty chunk as "Content-Range" header format does not
        # support this. So if current chunk happens to finish exactly at the end of the stream,
        # we need to know that and mark the chunk as last (by passing real file size in the
        # "Content-Range" header) when uploading it. To detect if we're at the end of the stream
        # we're reading "ahead" an extra bytes but not uploading them immediately. If
        # nothing has been read ahead, it means we're at the end of the stream.
        # On the contrary, in multipart upload we can decide to complete upload *after*
        # last chunk has been sent.

        body: dict = {"path": target_path, "session_token": session_token}

        headers = {"Content-Type": "application/json"}

        # Method _api.do() takes care of retrying and will raise an exception in case of failure.
        resumable_upload_url_response = self._api.do(
            "POST", "/api/2.0/fs/create-resumable-upload-url", headers=headers, body=body
        )

        resumable_upload_url_node = resumable_upload_url_response.get("resumable_upload_url")
        if not resumable_upload_url_node:
            raise ValueError(f"Unexpected server response: {resumable_upload_url_response}")

        resumable_upload_url = resumable_upload_url_node.get("url")
        if not resumable_upload_url:
            raise ValueError(f"Unexpected server response: {resumable_upload_url_response}")

        required_headers = resumable_upload_url_node.get("headers", [])

        try:
            # We will buffer this many bytes: one chunk + read-ahead block.
            # Note buffer may contain more data initially (from pre_read_buffer).
            min_buffer_size = self._config.multipart_upload_chunk_size + self._multipart_upload_read_ahead_bytes

            buffer = pre_read_buffer

            # How many bytes in the buffer were confirmed to be received by the server.
            # All the remaining bytes in the buffer must be uploaded.
            uploaded_bytes_count = 0

            chunk_offset = 0

            retry_count = 0
            while True:
                # If needed, fill the buffer to contain at least min_buffer_size bytes
                # (unless end of stream), discarding already uploaded bytes.
                bytes_to_read = max(0, min_buffer_size - (len(buffer) - uploaded_bytes_count))
                next_buf = input_stream.read(bytes_to_read)
                buffer = buffer[uploaded_bytes_count:] + next_buf

                if len(next_buf) < bytes_to_read:
                    # This is the last chunk in the stream.
                    # Let's upload all the remaining bytes in one go.
                    actual_chunk_length = len(buffer)
                    file_size = chunk_offset + actual_chunk_length
                else:
                    # More chunks expected, let's upload current chunk (excluding read-ahead block).
                    actual_chunk_length = self._config.multipart_upload_chunk_size
                    file_size = "*"

                headers: dict = {"Content-Type": "application/octet-stream"}
                for h in required_headers:
                    headers[h["name"]] = h["value"]

                chunk_last_byte_offset = chunk_offset + actual_chunk_length - 1
                content_range_header = f"bytes {chunk_offset}-{chunk_last_byte_offset}/{file_size}"
                _LOG.debug(f"Uploading chunk: {content_range_header}")
                headers["Content-Range"] = content_range_header

                def retrieve_upload_status() -> Optional[requests.Response]:
                    def perform():
                        return cloud_provider_session.request(
                            "PUT",
                            resumable_upload_url,
                            headers={"Content-Range": "bytes */*"},
                            data=b"",
                            timeout=self._config.multipart_upload_single_chunk_upload_timeout_seconds,
                        )

                    try:
                        return self._retry_idempotent_operation(perform)
                    except RequestException:
                        _LOG.warning("Failed to retrieve upload status")
                        return None

                try:
                    upload_response = cloud_provider_session.request(
                        "PUT",
                        resumable_upload_url,
                        headers=headers,
                        data=BytesIO(buffer[:actual_chunk_length]),
                        timeout=self._config.multipart_upload_single_chunk_upload_timeout_seconds,
                    )

                    # https://cloud.google.com/storage/docs/performing-resumable-uploads#resume-upload
                    # If an upload request is terminated before receiving a response, or if you receive
                    # a 503 or 500 response, then you need to resume the interrupted upload from where it left off.

                    # Let's follow that for all potentially retryable status codes.
                    # Together with the catch block below we replicate the logic in _retry_idempotent_operation().
                    if upload_response.status_code in self._RETRYABLE_STATUS_CODES:
                        if retry_count < self._config.multipart_upload_max_retries:
                            retry_count += 1
                            # let original upload_response be handled as an error
                            upload_response = retrieve_upload_status() or upload_response
                    else:
                        # we received non-retryable response, reset retry count
                        retry_count = 0

                except RequestException as e:
                    # Let's do the same for retryable network errors.
                    if _BaseClient._is_retryable(e) and retry_count < self._config.multipart_upload_max_retries:
                        retry_count += 1
                        upload_response = retrieve_upload_status()
                        if not upload_response:
                            # rethrow original exception
                            raise e from None
                    else:
                        # rethrow original exception
                        raise e from None

                if upload_response.status_code in (200, 201):
                    if file_size == "*":
                        raise ValueError(
                            f"Received unexpected status {upload_response.status_code} before reaching end of stream"
                        )

                    # upload complete
                    break

                elif upload_response.status_code == 308:
                    # chunk accepted (or check-status succeeded), let's determine received offset to resume from there
                    range_string = upload_response.headers.get("Range")
                    confirmed_offset = self._extract_range_offset(range_string)
                    _LOG.debug(f"Received confirmed offset: {confirmed_offset}")

                    if confirmed_offset:
                        if confirmed_offset < chunk_offset - 1 or confirmed_offset > chunk_last_byte_offset:
                            raise ValueError(
                                f"Unexpected received offset: {confirmed_offset} is outside of expected range, chunk offset: {chunk_offset}, chunk last byte offset: {chunk_last_byte_offset}"
                            )
                    else:
                        if chunk_offset > 0:
                            raise ValueError(
                                f"Unexpected received offset: {confirmed_offset} is outside of expected range, chunk offset: {chunk_offset}, chunk last byte offset: {chunk_last_byte_offset}"
                            )

                    # We have just uploaded a part of chunk starting from offset "chunk_offset" and ending
                    # at offset "confirmed_offset" (inclusive), so the next chunk will start at
                    # offset "confirmed_offset + 1"
                    if confirmed_offset:
                        next_chunk_offset = confirmed_offset + 1
                    else:
                        next_chunk_offset = chunk_offset
                    uploaded_bytes_count = next_chunk_offset - chunk_offset
                    chunk_offset = next_chunk_offset

                elif upload_response.status_code == 412 and not overwrite:
                    # Assuming this is only possible reason
                    # Full message in this case: "At least one of the pre-conditions you specified did not hold."
                    raise AlreadyExists("The file being created already exists.")

                else:
                    message = f"Unsuccessful chunk upload. Response status: {upload_response.status_code}, body: {upload_response.content}"
                    _LOG.warning(message)
                    mapped_error = _error_mapper(upload_response, {})
                    raise mapped_error or ValueError(message)

        except Exception as e:
            _LOG.info(f"Aborting resumable upload on error: {e}")
            try:
                self._abort_resumable_upload(resumable_upload_url, required_headers, cloud_provider_session)
            except BaseException as ex:
                _LOG.warning(f"Failed to abort upload: {ex}")
                # ignore, abort is a best-effort
            finally:
                # rethrow original exception
                raise e from None

    @staticmethod
    def _extract_range_offset(range_string: Optional[str]) -> Optional[int]:
        """Parses the response range header to extract the last byte."""
        if not range_string:
            return None  # server did not yet confirm any bytes

        if match := re.match("bytes=0-(\\d+)", range_string):
            return int(match.group(1))
        else:
            raise ValueError(f"Cannot parse response header: Range: {range_string}")

    def _get_url_expire_time(self):
        """Generates expiration time and save it in the required format."""
        current_time = datetime.datetime.now(datetime.timezone.utc)
        expire_time = current_time + self._config.multipart_upload_url_expiration_duration
        # From Google Protobuf doc:
        # In JSON format, the Timestamp type is encoded as a string in the
        #   * [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) format. That is, the
        #   * format is "{year}-{month}-{day}T{hour}:{min}:{sec}[.{frac_sec}]Z"
        return expire_time.strftime("%Y-%m-%dT%H:%M:%SZ")

    def _abort_multipart_upload(self, target_path: str, session_token: str, cloud_provider_session: requests.Session):
        """Aborts ongoing multipart upload session to clean up incomplete file."""
        body: dict = {"path": target_path, "session_token": session_token, "expire_time": self._get_url_expire_time()}

        headers = {"Content-Type": "application/json"}

        # Method _api.do() takes care of retrying and will raise an exception in case of failure.
        abort_url_response = self._api.do("POST", "/api/2.0/fs/create-abort-upload-url", headers=headers, body=body)

        abort_upload_url_node = abort_url_response["abort_upload_url"]
        abort_url = abort_upload_url_node["url"]
        required_headers = abort_upload_url_node.get("headers", [])

        headers: dict = {"Content-Type": "application/octet-stream"}
        for h in required_headers:
            headers[h["name"]] = h["value"]

        def perform():
            return cloud_provider_session.request(
                "DELETE",
                abort_url,
                headers=headers,
                data=b"",
                timeout=self._config.multipart_upload_single_chunk_upload_timeout_seconds,
            )

        abort_response = self._retry_idempotent_operation(perform)

        if abort_response.status_code not in (200, 201):
            raise ValueError(abort_response)

    def _abort_resumable_upload(
        self, resumable_upload_url: str, required_headers: list, cloud_provider_session: requests.Session
    ):
        """Aborts ongoing resumable upload session to clean up incomplete file."""
        headers: dict = {}
        for h in required_headers:
            headers[h["name"]] = h["value"]

        def perform():
            return cloud_provider_session.request(
                "DELETE",
                resumable_upload_url,
                headers=headers,
                data=b"",
                timeout=self._config.multipart_upload_single_chunk_upload_timeout_seconds,
            )

        abort_response = self._retry_idempotent_operation(perform)

        if abort_response.status_code not in (200, 201):
            raise ValueError(abort_response)

    def _create_cloud_provider_session(self):
        """Creates a separate session which does not inherit auth headers from BaseClient session."""
        session = requests.Session()

        # following session config in _BaseClient
        http_adapter = requests.adapters.HTTPAdapter(
            self._config.max_connection_pools or 20, self._config.max_connections_per_pool or 20, pool_block=True
        )
        session.mount("https://", http_adapter)
        # presigned URL for storage proxy can use plain HTTP
        session.mount("http://", http_adapter)
        return session

    def _retry_idempotent_operation(
        self, operation: Callable[[], requests.Response], before_retry: Callable = None
    ) -> requests.Response:
        """Perform given idempotent operation with necessary retries. Since operation is idempotent it's
        safe to retry it for response codes where server state might have changed.
        """

        def delegate():
            response = operation()
            if response.status_code in self._RETRYABLE_STATUS_CODES:
                attrs = {}
                # this will assign "retry_after_secs" to the attrs, essentially making exception look retryable
                _RetryAfterCustomizer().customize_error(response, attrs)
                raise _error_mapper(response, attrs)
            else:
                return response

        # following _BaseClient timeout
        retry_timeout_seconds = self._config.retry_timeout_seconds or 300

        return retried(
            timeout=timedelta(seconds=retry_timeout_seconds),
            # also retry on network errors (connection error, connection timeout)
            # where we believe request didn't reach the server
            is_retryable=_BaseClient._is_retryable,
            before_retry=before_retry,
        )(delegate)()

    def _open_download_stream(
        self, file_path: str, start_byte_offset: int, if_unmodified_since_timestamp: Optional[str] = None
    ) -> DownloadResponse:
        """Opens a download stream from given offset, performing necessary retries."""
        headers = {
            "Accept": "application/octet-stream",
        }

        if start_byte_offset and not if_unmodified_since_timestamp:
            raise Exception("if_unmodified_since_timestamp is required if start_byte_offset is specified")

        if start_byte_offset:
            headers["Range"] = f"bytes={start_byte_offset}-"

        if if_unmodified_since_timestamp:
            headers["If-Unmodified-Since"] = if_unmodified_since_timestamp

        response_headers = [
            "content-length",
            "content-type",
            "last-modified",
        ]
        # Method _api.do() takes care of retrying and will raise an exception in case of failure.
        res = self._api.do(
            "GET",
            f"/api/2.0/fs/files{_escape_multi_segment_path_parameter(file_path)}",
            headers=headers,
            response_headers=response_headers,
            raw=True,
        )

        result = DownloadResponse.from_dict(res)
        if not isinstance(result.contents, _StreamingResponse):
            raise Exception(
                "Internal error: response contents is of unexpected type: " + type(result.contents).__name__
            )

        return result

    def _wrap_stream(self, file_path: str, download_response: DownloadResponse):
        underlying_response = _ResilientIterator._extract_raw_response(download_response)
        return _ResilientResponse(
            self,
            file_path,
            download_response.last_modified,
            offset=0,
            underlying_response=underlying_response,
        )


class _ResilientResponse(_RawResponse):

    def __init__(
        self,
        api: FilesExt,
        file_path: str,
        file_last_modified: str,
        offset: int,
        underlying_response: _RawResponse,
    ):
        self.api = api
        self.file_path = file_path
        self.underlying_response = underlying_response
        self.offset = offset
        self.file_last_modified = file_last_modified

    def iter_content(self, chunk_size=1, decode_unicode=False):
        if decode_unicode:
            raise ValueError("Decode unicode is not supported")

        iterator = self.underlying_response.iter_content(chunk_size=chunk_size, decode_unicode=False)
        self.iterator = _ResilientIterator(
            iterator,
            self.file_path,
            self.file_last_modified,
            self.offset,
            self.api,
            chunk_size,
        )
        return self.iterator

    def close(self):
        self.iterator.close()


class _ResilientIterator(Iterator):
    # This class tracks current offset (returned to the client code)
    # and recovers from failures by requesting download from the current offset.

    @staticmethod
    def _extract_raw_response(
        download_response: DownloadResponse,
    ) -> _RawResponse:
        streaming_response: _StreamingResponse = download_response.contents  # this is an instance of _StreamingResponse
        return streaming_response._response

    def __init__(
        self,
        underlying_iterator,
        file_path: str,
        file_last_modified: str,
        offset: int,
        api: FilesExt,
        chunk_size: int,
    ):
        self._underlying_iterator = underlying_iterator
        self._api = api
        self._file_path = file_path

        # Absolute current offset (0-based), i.e. number of bytes from the beginning of the file
        # that were so far returned to the caller code.
        self._offset = offset
        self._file_last_modified = file_last_modified
        self._chunk_size = chunk_size

        self._total_recovers_count: int = 0
        self._recovers_without_progressing_count: int = 0
        self._closed: bool = False

    def _should_recover(self) -> bool:
        if self._total_recovers_count == self._api._config.files_api_client_download_max_total_recovers:
            _LOG.debug("Total recovers limit exceeded")
            return False
        if (
            self._api._config.files_api_client_download_max_total_recovers_without_progressing is not None
            and self._recovers_without_progressing_count
            >= self._api._config.files_api_client_download_max_total_recovers_without_progressing
        ):
            _LOG.debug("No progression recovers limit exceeded")
            return False
        return True

    def _recover(self) -> bool:
        if not self._should_recover():
            return False  # recover suppressed, rethrow original exception

        self._total_recovers_count += 1
        self._recovers_without_progressing_count += 1

        try:
            self._underlying_iterator.close()

            _LOG.debug("Trying to recover from offset " + str(self._offset))

            # following call includes all the required network retries
            downloadResponse = self._api._open_download_stream(self._file_path, self._offset, self._file_last_modified)
            underlying_response = _ResilientIterator._extract_raw_response(downloadResponse)
            self._underlying_iterator = underlying_response.iter_content(
                chunk_size=self._chunk_size, decode_unicode=False
            )
            _LOG.debug("Recover succeeded")
            return True
        except:
            return False  # recover failed, rethrow original exception

    def __next__(self):
        if self._closed:
            # following _BaseClient
            raise ValueError("I/O operation on closed file")

        while True:
            try:
                returned_bytes = next(self._underlying_iterator)
                self._offset += len(returned_bytes)
                self._recovers_without_progressing_count = 0
                return returned_bytes

            except StopIteration:
                raise

            # https://requests.readthedocs.io/en/latest/user/quickstart/#errors-and-exceptions
            except RequestException:
                if not self._recover():
                    raise

    def close(self):
        self._underlying_iterator.close()
        self._closed = True
