import base64
import json
import os
import random
import threading
import time
import typing
from collections import namedtuple

from databricks.sdk import errors
from databricks.sdk.service import clusters, commands


class FileInfo(namedtuple('FileInfo', ['path', 'name', 'size', "modificationTime"])):
    pass


class MountInfo(namedtuple('MountInfo', ['mountPoint', 'source', 'encryptionType'])):
    pass


class _FsUtil:
    """ Manipulates the Databricks filesystem (DBFS) """

    def __init__(self, utils: '_RemoteDbUtils'):
        self._api = utils._api.dbfs # nolint
        self._utils = utils

    def cp(self, from_: str, to: str, recurse: bool = False) -> bool:
        """ Copies a file or directory, possibly across FileSystems """
        self._api.copy(from_, to, recursive=recurse)
        return True

    def head(self, file: str, maxBytes: int = 65536) -> str:
        """ Returns up to the first 'maxBytes' bytes of the given file as a String encoded in UTF-8 """
        res = self._api.read(file, length=maxBytes, offset=0)
        raw = base64.b64decode(res.data)
        return raw.decode('utf8')

    def ls(self, dir: str) -> typing.List[FileInfo]:
        """ Lists the contents of a directory """
        result = []
        for f in self._api.list(dir):
            name = f.path.split('/')[-1]
            result.append(FileInfo(f'dbfs:{f.path}', name, f.file_size, f.modification_time))
        return result

    def mkdirs(self, dir: str) -> bool:
        """ Creates the given directory if it does not exist, also creating any necessary parent directories """
        self._api.mkdirs(dir)
        return True

    def mv(self, from_: str, to: str, recurse: bool = False) -> bool:
        """ Moves a file or directory, possibly across FileSystems """
        self._api.move_(from_, to, recursive=recurse, overwrite=True)
        return True

    def put(self, file: str, contents: str, overwrite: bool = False) -> bool:
        """ Writes the given String out to a file, encoded in UTF-8 """
        self._api.put(file, contents=contents, overwrite=overwrite)
        return True

    def rm(self, dir: str, recurse: bool = False) -> bool:
        """ Removes a file or directory """
        self._api.delete(dir, recursive=recurse)
        return True

    def mount(self,
              source: str,
              mountPoint: str,
              encryptionType: str = "",
              owner: str = "",
              extraConfigs: 'typing.Dict[str, str]' = None,
              ) -> bool:
        """ Mounts the given source directory into DBFS at the given mount point """
        return self._utils._proxy('fs', 'mount')(source=source,
                                                 mountPoint=mountPoint,
                                                 encryptionType=encryptionType,
                                                 owner=owner,
                                                 extraConfigs=extraConfigs)

    def unmount(self, mountPoint: str) -> bool:
        """ Deletes a DBFS mount point """
        return self._utils._proxy('fs', 'unmount')(mountPoint)

    def updateMount(self,
                    source: str,
                    mountPoint: str,
                    encryptionType: str = "",
                    owner: str = "",
                    extraConfigs: 'typing.Dict[str, str]' = None,
                    ) -> bool:
        """ Similar to mount(), but updates an existing mount point (if present) instead of creating a new one """
        return self._utils._proxy('fs', 'updateMount')(source=source,
                                                       mountPoint=mountPoint,
                                                       encryptionType=encryptionType,
                                                       owner=owner,
                                                       extraConfigs=extraConfigs)

    def mounts(self) -> typing.List[MountInfo]:
        """ Displays information about what is mounted within DBFS """
        result = []
        for info in self._utils._proxy('fs', 'mounts')():
            result.append(MountInfo(info[0], info[1], info[2]))
        return result

    def refreshMounts(self) -> bool:
        """ Forces all machines in this cluster to refresh their mount cache,
        ensuring they receive the most recent information """
        return self._utils._proxy('fs', 'refreshMounts')()


class _RemoteDbUtils:

    def __init__(self, *, cluster_id=None):
        from databricks.sdk import WorkspaceClient
        if not cluster_id:
            cluster_id = os.getenv('DATABRICKS_CLUSTER_ID')
        self._cluster_id = cluster_id
        self._api = WorkspaceClient()
        self._lock = threading.Lock()
        self._ctx = None

        self.fs = _FsUtil(self)

    def _running_command_context(self) -> commands.ContextStatusResponse:
        if self._ctx:
            return self._ctx
        with self._lock:
            if self._ctx:
                return self._ctx
            self._api.clusters.ensure_cluster_is_running(self._cluster_id)
            self._ctx = self._api.command_execution.create(
                cluster_id=self._cluster_id,
                language=commands.Language.python,
                wait=True)
        return self._ctx

    def _proxy(self, util: str, method: str) -> '_ProxyCall':
        return _ProxyCall(self, util, method)

    def __getattr__(self, util) -> '_ProxyUtil':
        return _ProxyUtil(self, util)


class _ProxyUtil:

    def __init__(self, remote_utils: _RemoteDbUtils, name: str):
        self._remote_utils = remote_utils
        self._name = name

    def __getattr__(self, method: str) -> '_ProxyCall':
        return _ProxyCall(self._remote_utils, self._name, method)


class _ProxyCall:

    def __init__(self, utils: _RemoteDbUtils, util: str, method: str):
        self._api = utils._api.command_execution # nolint
        self._cluster_id = utils._cluster_id # nolint
        self._remote_utils = utils
        self._util = util
        self._method = method

    @property
    def _context_id(self) -> str:
        ctx = self._remote_utils._running_command_context()
        return ctx.id

    def __call__(self, *args, **kwargs):
        raw = json.dumps((args, kwargs))
        code = f'''
        import json
        (args, kwargs) = json.loads('{raw}')
        result = dbutils.{self._util}.{self._method}(*args, **kwargs)
        dbutils.notebook.exit(json.dumps(result))
        '''
        result = self._api.execute(cluster_id=self._cluster_id,
                                   language=commands.Language.python,
                                   context_id=self._context_id,
                                   command=code,
                                   wait=True)
        if result.status == commands.CommandStatus.Finished:
            raw = result.results.data
            return json.loads(raw)
        else:
            raise Exception(result.results.summary)
