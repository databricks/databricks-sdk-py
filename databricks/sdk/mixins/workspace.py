import logging
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from queue import Queue
from threading import Condition
from typing import BinaryIO, Iterable, Iterator, Optional

from ..core import DatabricksError
from ..service.workspace import (ExportFormat, ImportFormat, Language,
                                 ObjectInfo, ObjectType, WorkspaceAPI)

_PARALLEL_RECURSIVE_LISTING_HINT_THRESHOLD = 100


def _fqcn(x: any) -> str:
    return f'{x.__module__}.{x.__name__}'


_LOG = logging.getLogger(__name__)


class _ParallelRecursiveListing(Iterable[ObjectInfo]):

    def __init__(self, path, listing, threads, yield_folders, notebooks_modified_after, max_depth):
        self._path = path
        self._listing = listing
        self._threads = threads
        self._max_depth = max_depth
        self._yield_folders = yield_folders
        self._notebooks_modified_after = notebooks_modified_after
        self._scans = 0
        self._in_progress = 0
        self._work = Queue()
        self._results = Queue()
        self._cond = Condition()
        self._reporter_interval = 5
        self._reporter_cond = Condition()

    def _enter_folder(self, path: str):
        with self._cond:
            _LOG.debug(f"Entering folder: {path}")
            self._in_progress += 1
        self._work.put_nowait(path)

    def _leave_folder(self, path: str):
        with self._cond:
            self._in_progress -= 1
            self._scans += 1
            _LOG.debug(f"Leaving folder: {path}")
            if self._in_progress != 0:
                return
            self._cond.notify_all()
            _LOG.debug("Sending poison pills to other workers")
            for _ in range(0, self._threads - 1):
                self._work.put(None)

    def _is_running(self):
        with self._cond:
            return self._in_progress > 0

    def _reporter(self):
        _LOG.debug("Starting workspace listing reporter")
        while self._is_running():
            with self._reporter_cond:
                self._reporter_cond.wait(self._reporter_interval)
            scans = self._scans
            took = datetime.now() - self._started
            rps = int(scans / took.total_seconds())
            _LOG.info(f"Scanned {scans} workspace folders at {rps}rps")
        _LOG.debug("Finished workspace listing reporter")

    def _worker(self, num):
        _LOG.debug(f"Starting workspace listing worker {num}")
        while self._is_running():
            path = self._work.get()
            if path is None:
                self._work.task_done()
                break # poison pill
            try:
                listing = self._listing(path, notebooks_modified_after=self._notebooks_modified_after)
                for object_info in sorted(listing, key=lambda _: _.path):
                    if object_info.object_type == ObjectType.DIRECTORY:
                        if self._yield_folders:
                            self._results.put_nowait(object_info)
                        if self._max_depth is not None and len(object_info.path.split('/')) > self._max_depth:
                            msg = f"Folder is too deep (max depth {self._max_depth}): {object_info.path}. Skipping"
                            _LOG.warning(msg)
                            continue
                        self._enter_folder(object_info.path)
                        continue
                    self._results.put_nowait(object_info)
            except DatabricksError as err:
                # See https://github.com/databrickslabs/ucx/issues/230
                if err.error_code != "RESOURCE_DOES_NOT_EXIST":
                    raise err
                _LOG.warning(f"{path} is not listable. Ignoring")
            finally:
                self._work.task_done()
                self._leave_folder(path)
        _LOG.debug(f"Finished workspace listing worker {num}")

    def __iter__(self):
        self._started = datetime.now()
        with ThreadPoolExecutor(max_workers=self._threads) as pool:
            self._enter_folder(self._path)
            pool.submit(self._reporter)
            for num in range(self._threads):
                pool.submit(self._worker, num)
            while self._is_running():
                get = self._results.get()
                yield get
        took = datetime.now() - self._started
        _LOG.debug(f"Finished iterating over {self._path}. Took {took}")


class WorkspaceExt(WorkspaceAPI):
    __doc__ = WorkspaceAPI.__doc__

    def list(self,
             path: str,
             *,
             notebooks_modified_after: Optional[int] = None,
             recursive: Optional[bool] = False,
             yield_folders: Optional[bool] = False,
             threads: Optional[int] = None,
             max_depth: Optional[int] = None,
             **kwargs) -> Iterator[ObjectInfo]:
        """List workspace objects

        :param path: str
            The absolute path of the workspace directory.
        :param notebooks_modified_after: int (optional)
            UTC timestamp in milliseconds
        :param recursive: bool (optional)
            Optionally invoke recursive traversal. Increase performance by adding `threads` argument.
        :param yield_folders: bool (optional)
            Also get the names of folders within a path in addition to non-folder objects,
            like notebooks or files.
        :param threads: int (optional)
            Opt-in for the  high-performance parallel listing implementation, where Databricks SDK
            for Python makes workspace listing calls in parallel, yet still preserving the Iterator
            interface of this method.
        :param max_depth: int (optional)
            If threads and max_depth are specified, stop iterating after reaching the specified folder depth,
            so that this method finishes execution earlier on large workspaces with more than 10K notebooks.

        :returns: Iterator of ObjectInfo
        """
        parent_list = super().list
        if recursive and threads is not None:
            return _ParallelRecursiveListing(path, parent_list, threads, yield_folders,
                                             notebooks_modified_after, max_depth)
        queue = [path]
        folders_listed = 0
        while queue:
            path, queue = queue[0], queue[1:]
            for object_info in parent_list(path, notebooks_modified_after=notebooks_modified_after):
                if recursive and object_info.object_type == ObjectType.DIRECTORY:
                    queue.append(object_info.path)
                    if yield_folders:
                        yield object_info
                    if folders_listed == _PARALLEL_RECURSIVE_LISTING_HINT_THRESHOLD:
                        _LOG.warning(f'Scanned more than {_PARALLEL_RECURSIVE_LISTING_HINT_THRESHOLD} with '
                                     f'`recursive=True`. Consider adding `threads=10` for some parallelism')
                    continue
                yield object_info

    def upload(self,
               path: str,
               content: BinaryIO,
               *,
               format: Optional[ImportFormat] = None,
               language: Optional[Language] = None,
               overwrite: Optional[bool] = False) -> None:
        """
        Uploads a workspace object (for example, a notebook or file) or the contents of an entire
        directory (`DBC` format).

        Errors:
         * `RESOURCE_ALREADY_EXISTS`: if `path` already exists no `overwrite=True`.
         * `INVALID_PARAMETER_VALUE`: if `format` and `content` values are not compatible.

        :param path:     target location of the file on workspace.
        :param content:  file-like `io.BinaryIO` of the `path` contents.
        :param format:   By default, `ImportFormat.SOURCE`. If using `ImportFormat.AUTO` the `path`
                         is imported or exported as either a workspace file or a notebook, depending
                         on an analysis of the `item`’s extension and the header content provided in
                         the request. In addition, if the `path` is imported as a notebook, then
                         the `item`’s extension is automatically removed.
        :param language: Only required if using `ExportFormat.SOURCE`.
        """
        if format is not None and not isinstance(format, ImportFormat):
            raise ValueError(
                f'format is expected to be {_fqcn(ImportFormat)}, but got {_fqcn(format.__class__)}')
        if (not format or format == ImportFormat.SOURCE) and not language:
            suffixes = {
                '.py': Language.PYTHON,
                '.sql': Language.SQL,
                '.scala': Language.SCALA,
                '.R': Language.R
            }
            for sfx, lang in suffixes.items():
                if path.endswith(sfx):
                    language = lang
                    break
        if language is not None and not isinstance(language, Language):
            raise ValueError(
                f'language is expected to be {_fqcn(Language)}, but got {_fqcn(language.__class__)}')
        data = {'path': path}
        if format: data['format'] = format.value
        if language: data['language'] = language.value
        if overwrite: data['overwrite'] = 'true'
        try:
            return self._api.do('POST', '/api/2.0/workspace/import', files={'content': content}, data=data)
        except DatabricksError as e:
            if e.error_code == 'INVALID_PARAMETER_VALUE':
                msg = f'Perhaps you forgot to specify the `format=ImportFormat.AUTO`. {e}'
                raise DatabricksError(message=msg, error_code=e.error_code)
            else:
                raise e

    def download(self, path: str, *, format: Optional[ExportFormat] = None) -> BinaryIO:
        """
        Downloads notebook or file from the workspace

        :param path:     location of the file or notebook on workspace.
        :param format:   By default, `ExportFormat.SOURCE`. If using `ExportFormat.AUTO` the `path`
                         is imported or exported as either a workspace file or a notebook, depending
                         on an analysis of the `item`’s extension and the header content provided in
                         the request.
        :return:         file-like `io.BinaryIO` of the `path` contents.
        """
        query = {'path': path, 'direct_download': 'true'}
        if format: query['format'] = format.value
        return self._api.do('GET', '/api/2.0/workspace/export', query=query, raw=True)
