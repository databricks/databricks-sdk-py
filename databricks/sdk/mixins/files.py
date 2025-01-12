from __future__ import annotations

import base64
import logging
import os
import pathlib
import platform
import shutil
import sys
from abc import ABC, abstractmethod
from collections import deque
from collections.abc import Iterator
from io import BytesIO
from types import TracebackType
from typing import (TYPE_CHECKING, AnyStr, BinaryIO, Generator, Iterable,
                    Optional, Type, Union)
from urllib import parse

from requests import RequestException

from .._base_client import _RawResponse, _StreamingResponse
from .._property import _cached_property
from ..errors import NotFound
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

    def __init__(self,
                 api: files.DbfsAPI,
                 path: str,
                 *,
                 read: bool = False,
                 write: bool = False,
                 overwrite: bool = False):
        self._api = api
        self._path = path
        if write and read: raise IOError(f'can open either for reading or writing')
        if read: self._status = api.get_status(path)
        elif write: self._created = api.create(path, overwrite=overwrite)
        else: raise IOError(f'need to open either for reading or writing')

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
        """ Write bytes to file.

        :return: Return the number of bytes written.
        """
        if not self.writable():
            raise IOError('file not open for writing')
        if type(buffer) is not bytes:
            # Python doesn't strictly enforce types. Even if they're specified.
            raise TypeError(f'a bytes-like object is required, not {type(buffer)}')
        total = 0
        while total < len(buffer):
            chunk = buffer[total:]
            if len(chunk) > self.MAX_CHUNK_SIZE:
                chunk = chunk[:self.MAX_CHUNK_SIZE]
            encoded = base64.b64encode(chunk).decode()
            self._api.add_block(self._created.handle, encoded)
            total += len(chunk)
        return total

    def close(self) -> None:
        """ Disable all I/O operations. """
        if self.writable(): self._api.close(self._created.handle)
        self._closed = True

    @property
    def closed(self) -> bool:
        return self._closed

    def __exit__(self, __t: Type[BaseException] | None, __value: BaseException | None,
                 __traceback: TracebackType | None):
        self.close()

    def readable(self) -> bool:
        return self._status is not None

    def read(self, size: int = ...) -> bytes:
        """ Read at most size bytes, returned as a bytes object.

        :param size: If the size argument is negative, read until EOF is reached.
                     Return an empty bytes object at EOF.
        :return: bytes
        """
        if not self.readable():
            raise IOError('file not open for reading')

        # call __iter__() and read until EOF is reached
        if size is ... or size < 0:
            buffer = b''
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
            return b''

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

    def __init__(self, api: files.FilesAPI, path: str, *, read: bool, write: bool, overwrite: bool):
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
            to_write = b''.join(self._buffer)
            self._api.upload(self._path, contents=BytesIO(to_write), overwrite=self._overwrite)
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
            raise ValueError('I/O operation on closed file')

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
    def __init__(self):
        ...

    @property
    def is_local(self) -> bool:
        return self._is_local()

    @abstractmethod
    def _is_local(self) -> bool:
        ...

    @property
    def is_dbfs(self) -> bool:
        return self._is_dbfs()

    @abstractmethod
    def _is_dbfs(self) -> bool:
        ...

    @abstractmethod
    def child(self, path: str) -> str:
        ...

    @_cached_property
    def is_dir(self) -> bool:
        return self._is_dir()

    @abstractmethod
    def _is_dir(self) -> bool:
        ...

    @abstractmethod
    def exists(self) -> bool:
        ...

    @abstractmethod
    def open(self, *, read=False, write=False, overwrite=False):
        ...

    def list(self, *, recursive=False) -> Generator[files.FileInfo, None, None]:
        ...

    @abstractmethod
    def mkdir(self):
        ...

    @abstractmethod
    def delete(self, *, recursive=False):
        ...

    @property
    def name(self) -> str:
        return self._path.name

    @property
    def as_string(self) -> str:
        return str(self._path)


class _LocalPath(_Path):

    def __init__(self, path: str):
        if platform.system() == "Windows":
            self._path = pathlib.Path(str(path).replace('file:///', '').replace('file:', ''))
        else:
            self._path = pathlib.Path(str(path).replace('file:', ''))

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
        return self._path.open(mode='wb' if overwrite else 'rb' if read else 'xb')

    def list(self, recursive=False) -> Generator[files.FileInfo, None, None]:
        if not self.is_dir:
            st = self._path.stat()
            yield files.FileInfo(path='file:' + str(self._path.absolute()),
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
                yield files.FileInfo(path='file:' + str(leaf.absolute()),
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
                kw['missing_ok'] = True
            self._path.unlink(**kw)

    def __repr__(self) -> str:
        return f'<_LocalPath {self._path}>'


class _VolumesPath(_Path):

    def __init__(self, api: files.FilesAPI, src: Union[str, pathlib.Path]):
        self._path = pathlib.PurePosixPath(str(src).replace('dbfs:', '').replace('file:', ''))
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
        return _VolumesIO(self._api, self.as_string, read=read, write=write, overwrite=overwrite)

    def list(self, *, recursive=False) -> Generator[files.FileInfo, None, None]:
        if not self.is_dir:
            meta = self._api.get_metadata(self.as_string)
            yield files.FileInfo(path=self.as_string,
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
                    yield files.FileInfo(path=file.path,
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
        return f'<_VolumesPath {self._path}>'


class _DbfsPath(_Path):

    def __init__(self, api: files.DbfsAPI, src: str):
        self._path = pathlib.PurePosixPath(str(src).replace('dbfs:', '').replace('file:', ''))
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
        return _DbfsIO(self._api, self.as_string, read=read, write=write, overwrite=overwrite)

    def list(self, *, recursive=False) -> Generator[files.FileInfo, None, None]:
        if not self.is_dir:
            meta = self._api.get_status(self.as_string)
            yield files.FileInfo(path=self.as_string,
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
        return f'<_DbfsPath {self._path}>'


class DbfsExt(files.DbfsAPI):
    __doc__ = files.DbfsAPI.__doc__

    def __init__(self, api_client):
        super().__init__(api_client)
        self._files_api = files.FilesAPI(api_client)
        self._dbfs_api = files.DbfsAPI(api_client)

    def open(self,
             path: str,
             *,
             read: bool = False,
             write: bool = False,
             overwrite: bool = False) -> BinaryIO:
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

    __ALLOWED_SCHEMES = [None, 'file', 'dbfs']

    def _path(self, src):
        src = parse.urlparse(str(src))
        if src.scheme and src.scheme not in self.__ALLOWED_SCHEMES:
            raise ValueError(
                f'unsupported scheme "{src.scheme}". DBUtils in the SDK only supports local, root DBFS, and '
                'UC Volumes paths, not external locations or DBFS mount points.')
        if src.scheme == 'file':
            return _LocalPath(src.geturl())
        if src.path.startswith('/Volumes'):
            return _VolumesPath(self._files_api, src.geturl())
        return _DbfsPath(self._dbfs_api, src.geturl())

    def copy(self, src: str, dst: str, *, recursive=False, overwrite=False):
        """Copy files between DBFS and local filesystems"""
        src = self._path(src)
        dst = self._path(dst)
        if src.is_local and dst.is_local:
            raise IOError('both destinations are on local FS')
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
            raise IOError('both destinations are on local FS')
        if source.is_dir and not recursive:
            src_type = 'local' if source.is_local else 'DBFS' if source.is_dbfs else 'UC Volume'
            dst_type = 'local' if target.is_local else 'DBFS' if target.is_dbfs else 'UC Volume'
            raise IOError(f'moving a directory from {src_type} to {dst_type} requires recursive flag')
        # do cross-fs moving
        self.copy(src, dst, recursive=recursive, overwrite=overwrite)
        self.delete(src, recursive=recursive)

    def delete(self, path: str, *, recursive=False):
        """Delete file or directory on DBFS"""
        p = self._path(path)
        if p.is_dir and not recursive:
            raise IOError('deleting directories requires recursive flag')
        p.delete(recursive=recursive)


class FilesExt(files.FilesAPI):
    __doc__ = files.FilesAPI.__doc__

    def __init__(self, api_client, config: Config):
        super().__init__(api_client)
        self._config = config.copy()

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

        initial_response: DownloadResponse = self._download_raw_stream(file_path=file_path,
                                                                       start_byte_offset=0,
                                                                       if_unmodified_since_timestamp=None)

        wrapped_response = self._wrap_stream(file_path, initial_response)
        initial_response.contents._response = wrapped_response
        return initial_response

    def _download_raw_stream(self,
                             file_path: str,
                             start_byte_offset: int,
                             if_unmodified_since_timestamp: Optional[str] = None) -> DownloadResponse:
        headers = {'Accept': 'application/octet-stream', }

        if start_byte_offset and not if_unmodified_since_timestamp:
            raise Exception("if_unmodified_since_timestamp is required if start_byte_offset is specified")

        if start_byte_offset:
            headers['Range'] = f'bytes={start_byte_offset}-'

        if if_unmodified_since_timestamp:
            headers['If-Unmodified-Since'] = if_unmodified_since_timestamp

        response_headers = ['content-length', 'content-type', 'last-modified', ]
        res = self._api.do('GET',
                           f'/api/2.0/fs/files{_escape_multi_segment_path_parameter(file_path)}',
                           headers=headers,
                           response_headers=response_headers,
                           raw=True)

        result = DownloadResponse.from_dict(res)
        if not isinstance(result.contents, _StreamingResponse):
            raise Exception("Internal error: response contents is of unexpected type: " +
                            type(result.contents).__name__)

        return result

    def _wrap_stream(self, file_path: str, downloadResponse: DownloadResponse):
        underlying_response = _ResilientIterator._extract_raw_response(downloadResponse)
        return _ResilientResponse(self,
                                  file_path,
                                  downloadResponse.last_modified,
                                  offset=0,
                                  underlying_response=underlying_response)


class _ResilientResponse(_RawResponse):

    def __init__(self, api: FilesExt, file_path: str, file_last_modified: str, offset: int,
                 underlying_response: _RawResponse):
        self.api = api
        self.file_path = file_path
        self.underlying_response = underlying_response
        self.offset = offset
        self.file_last_modified = file_last_modified

    def iter_content(self, chunk_size=1, decode_unicode=False):
        if decode_unicode:
            raise ValueError('Decode unicode is not supported')

        iterator = self.underlying_response.iter_content(chunk_size=chunk_size, decode_unicode=False)
        self.iterator = _ResilientIterator(iterator, self.file_path, self.file_last_modified, self.offset,
                                           self.api, chunk_size)
        return self.iterator

    def close(self):
        self.iterator.close()


class _ResilientIterator(Iterator):
    # This class tracks current offset (returned to the client code)
    # and recovers from failures by requesting download from the current offset.

    @staticmethod
    def _extract_raw_response(download_response: DownloadResponse) -> _RawResponse:
        streaming_response: _StreamingResponse = download_response.contents # this is an instance of _StreamingResponse
        return streaming_response._response

    def __init__(self, underlying_iterator, file_path: str, file_last_modified: str, offset: int,
                 api: FilesExt, chunk_size: int):
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
        if self._api._config.files_api_client_download_max_total_recovers_without_progressing is not None and self._recovers_without_progressing_count >= self._api._config.files_api_client_download_max_total_recovers_without_progressing:
            _LOG.debug("No progression recovers limit exceeded")
            return False
        return True

    def _recover(self) -> bool:
        if not self._should_recover():
            return False # recover suppressed, rethrow original exception

        self._total_recovers_count += 1
        self._recovers_without_progressing_count += 1

        try:
            self._underlying_iterator.close()

            _LOG.debug("Trying to recover from offset " + str(self._offset))

            # following call includes all the required network retries
            downloadResponse = self._api._download_raw_stream(self._file_path, self._offset,
                                                              self._file_last_modified)
            underlying_response = _ResilientIterator._extract_raw_response(downloadResponse)
            self._underlying_iterator = underlying_response.iter_content(chunk_size=self._chunk_size,
                                                                         decode_unicode=False)
            _LOG.debug("Recover succeeded")
            return True
        except:
            return False # recover failed, rethrow original exception

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
