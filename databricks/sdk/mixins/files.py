from __future__ import annotations

import base64
import pathlib
import shutil
import sys
from abc import ABC, abstractmethod
from types import TracebackType
from typing import TYPE_CHECKING, AnyStr, BinaryIO, Iterable, Iterator, Type

from databricks.sdk.core import DatabricksError

from ..service import files

if TYPE_CHECKING:
    from _typeshed import Self


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


class _Path(ABC):

    @property
    @abstractmethod
    def is_local(self) -> bool:
        ...

    @abstractmethod
    def child(self, path: str) -> str:
        ...

    @abstractmethod
    def is_dir(self) -> bool:
        ...

    @abstractmethod
    def exists(self) -> bool:
        ...

    @abstractmethod
    def open(self, *, read=False, write=False, overwrite=False):
        ...

    @abstractmethod
    def list_opened_handles(self, *, recursive=False) -> Iterator[(str, BinaryIO)]:
        ...

    @abstractmethod
    def delete(self, *, recursive=False):
        ...

    def _with_path(self, src: str):
        # create sanitized path representation, so that
        # we can have clean child paths in list_opened_handles()
        self._path = pathlib.Path(str(src).replace('dbfs:', '').replace('file:', ''))

    @property
    def name(self) -> str:
        return self._path.name

    @property
    def as_string(self) -> str:
        return str(self._path)


class _LocalPath(_Path):

    def __init__(self, src: str):
        self._with_path(src)

    @property
    def is_local(self) -> bool:
        return True

    def child(self, path: str) -> Self:
        return _LocalPath(str(self._path / path))

    def is_dir(self) -> bool:
        return self._path.is_dir()

    def exists(self) -> bool:
        return self._path.exists()

    def open(self, *, read=False, write=False, overwrite=False):
        # make local fs follow the similar semantics as DBFS
        self._path.parent.mkdir(mode=0o755, parents=True, exist_ok=True)
        return self._path.open(mode='wb' if overwrite else 'rb' if read else 'xb')

    def _list_local(self, recursive=False):
        queue = [self._path]
        while queue:
            path, queue = queue[0], queue[1:]
            for leaf in path.iterdir():
                if leaf.is_dir():
                    if recursive:
                        queue.append(leaf)
                    continue
                yield leaf

    def list_opened_handles(self, *, recursive=False) -> Iterator[(str, BinaryIO)]:
        for leaf in self._list_local(recursive):
            if not recursive and leaf.is_dir:
                continue
            with leaf.open('rb') as handle:
                child = str(leaf).replace(str(self._path) + '/', '')
                yield child, handle

    def delete(self, *, recursive=False):
        if self.is_dir():
            if recursive:
                for leaf in self._list_local(True):
                    kw = {}
                    if sys.version_info[:2] > (3, 7):
                        # Python3.7 does not support `missing_ok` keyword
                        kw['missing_ok'] = True
                    leaf.unlink(**kw)
            self._path.rmdir()
            return
        self._path.unlink()

    def __repr__(self) -> str:
        return f'<_LocalPath {self._path}>'


class _DbfsPath(_Path):

    def __init__(self, api: 'DbfsExt', src: str):
        self._with_path(src)
        self._api = api

    @property
    def is_local(self) -> bool:
        return False

    def child(self, path: str) -> Self:
        child = self._path / path
        return _DbfsPath(self._api, str(child))

    def is_dir(self) -> bool:
        try:
            remote = self._api.get_status(self.as_string)
            return remote.is_dir
        except DatabricksError as e:
            if e.error_code == 'RESOURCE_DOES_NOT_EXIST':
                return False
            raise e

    def exists(self) -> bool:
        return self._api.exists(self.as_string)

    def open(self, *, read=False, write=False, overwrite=False) -> BinaryIO:
        return self._api.open(self.as_string, read=read, write=write, overwrite=overwrite)

    def list_opened_handles(self, *, recursive=False) -> Iterator[(str, BinaryIO)]:
        for file in self._api.list(self.as_string, recursive=recursive):
            if not recursive and file.is_dir:
                continue
            with self._api.open(file.path, read=True) as handle:
                child = file.path.replace(str(self._path) + '/', '').replace('dbfs:', '')
                yield child, handle

    def delete(self, *, recursive=False):
        self._api.delete(self.as_string, recursive=recursive)

    def __repr__(self) -> str:
        return f'<_DbfsPath {self._path}>'


class DbfsExt(files.DbfsAPI):
    __doc__ = files.DbfsAPI.__doc__

    def open(self, path: str, *, read: bool = False, write: bool = False, overwrite: bool = False) -> _DbfsIO:
        return _DbfsIO(self, path, read=read, write=write, overwrite=overwrite)

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

        :param recursive: traverse deep into directory tree
        :returns iterator of metadata for every file
        """
        queue = [path]
        while queue:
            path, queue = queue[0], queue[1:]
            for file_info in super().list(path):
                if recursive and file_info.is_dir:
                    queue.append(file_info.path)
                    continue
                yield file_info

    def exists(self, path: str) -> bool:
        """If file exists on DBFS"""
        # TODO: check if we want to put it to errors module to prevent circular import
        from databricks.sdk.core import DatabricksError
        try:
            self.get_status(path)
            return True
        except DatabricksError as e:
            if e.error_code == 'RESOURCE_DOES_NOT_EXIST':
                return False
            raise e

    def _path(self, src):
        if str(src).startswith('file:'):
            return _LocalPath(src)
        return _DbfsPath(self, src)

    def copy(self, src: str, dst: str, *, recursive=False, overwrite=False):
        """Copy files between DBFS and local filesystems"""
        src = self._path(src)
        dst = self._path(dst)
        if src.is_local and dst.is_local:
            raise IOError('both destinations are on local FS')
        if dst.exists() and dst.is_dir():
            # if target is a folder, make file with the same name there
            dst = dst.child(src.name)
        if not src.is_dir():
            # copy single file
            with src.open(read=True) as reader:
                with dst.open(write=True, overwrite=overwrite) as writer:
                    shutil.copyfileobj(reader, writer, length=_DbfsIO.MAX_CHUNK_SIZE)
            return
        # iterate through files
        for child, reader in src.list_opened_handles(recursive=recursive):
            with dst.child(child).open(write=True, overwrite=overwrite) as writer:
                shutil.copyfileobj(reader, writer, length=_DbfsIO.MAX_CHUNK_SIZE)

    def move_(self, src: str, dst: str, *, recursive=False, overwrite=False):
        """Move files between local and DBFS systems"""
        source = self._path(src)
        target = self._path(dst)
        if not source.is_local and not target.is_local:
            # Moves a file from one location to another location within DBFS.
            # this operation is recursive by default.
            return self.move(source.as_string, target.as_string)
        if source.is_local and target.is_local:
            raise IOError('both destinations are on local FS')
        if source.is_dir() and not recursive:
            raise IOError('moving directories across filesystems requires recursive flag')
        # do cross-fs moving
        self.copy(src, dst, recursive=recursive, overwrite=overwrite)
        source.delete(recursive=recursive)
