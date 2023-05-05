import base64
import json
import threading
import typing
from collections import namedtuple

from .core import ApiClient, Config
from .mixins import compute as compute_ext
from .mixins import dbfs as dbfs_ext
from .service import compute, workspace


class FileInfo(namedtuple('FileInfo', ['path', 'name', 'size', "modificationTime"])):
    pass


class MountInfo(namedtuple('MountInfo', ['mountPoint', 'source', 'encryptionType'])):
    pass


class SecretScope(namedtuple('SecretScope', ['name'])):

    def getName(self):
        return self.name


class SecretMetadata(namedtuple('SecretMetadata', ['key'])):
    pass


class _FsUtil:
    """ Manipulates the Databricks filesystem (DBFS) """

    def __init__(self, dbfs_ext: dbfs_ext.DbfsExt, proxy_factory: typing.Callable[[str], '_ProxyUtil']):
        self._dbfs = dbfs_ext
        self._proxy_factory = proxy_factory

    def cp(self, from_: str, to: str, recurse: bool = False) -> bool:
        """Copies a file or directory, possibly across FileSystems """
        self._dbfs.copy(from_, to, recursive=recurse)
        return True

    def head(self, file: str, maxBytes: int = 65536) -> str:
        """Returns up to the first 'maxBytes' bytes of the given file as a String encoded in UTF-8 """
        res = self._dbfs.read(file, length=maxBytes, offset=0)
        raw = base64.b64decode(res.data)
        return raw.decode('utf8')

    def ls(self, dir: str) -> typing.List[FileInfo]:
        """Lists the contents of a directory """
        result = []
        for f in self._dbfs.list(dir):
            name = f.path.split('/')[-1]
            result.append(FileInfo(f'dbfs:{f.path}', name, f.file_size, f.modification_time))
        return result

    def mkdirs(self, dir: str) -> bool:
        """Creates the given directory if it does not exist, also creating any necessary parent directories """
        self._dbfs.mkdirs(dir)
        return True

    def mv(self, from_: str, to: str, recurse: bool = False) -> bool:
        """Moves a file or directory, possibly across FileSystems """
        self._dbfs.move_(from_, to, recursive=recurse, overwrite=True)
        return True

    def put(self, file: str, contents: str, overwrite: bool = False) -> bool:
        """Writes the given String out to a file, encoded in UTF-8 """
        with self._dbfs.open(file, write=True, overwrite=overwrite) as f:
            f.write(contents.encode('utf8'))
        return True

    def rm(self, dir: str, recurse: bool = False) -> bool:
        """Removes a file or directory """
        self._dbfs.delete(dir, recursive=recurse)
        return True

    def mount(self,
              source: str,
              mountPoint: str,
              encryptionType: str = "",
              owner: str = "",
              extraConfigs: 'typing.Dict[str, str]' = None,
              ) -> bool:
        """Mounts the given source directory into DBFS at the given mount point"""
        fs = self._proxy_factory('fs')
        return fs.mount(source=source,
                        mountPoint=mountPoint,
                        encryptionType=encryptionType,
                        owner=owner,
                        extraConfigs=extraConfigs)

    def unmount(self, mountPoint: str) -> bool:
        """Deletes a DBFS mount point"""
        fs = self._proxy_factory('fs')
        return fs.unmount(mountPoint)

    def updateMount(self,
                    source: str,
                    mountPoint: str,
                    encryptionType: str = "",
                    owner: str = "",
                    extraConfigs: 'typing.Dict[str, str]' = None,
                    ) -> bool:
        """ Similar to mount(), but updates an existing mount point (if present) instead of creating a new one """
        fs = self._proxy_factory('fs')
        return fs.updateMount(source=source,
                              mountPoint=mountPoint,
                              encryptionType=encryptionType,
                              owner=owner,
                              extraConfigs=extraConfigs)

    def mounts(self) -> typing.List[MountInfo]:
        """ Displays information about what is mounted within DBFS """
        result = []
        fs = self._proxy_factory('fs')
        for info in fs.mounts():
            result.append(MountInfo(info[0], info[1], info[2]))
        return result

    def refreshMounts(self) -> bool:
        """ Forces all machines in this cluster to refresh their mount cache,
        ensuring they receive the most recent information """
        fs = self._proxy_factory('fs')
        return fs.refreshMounts()


class _SecretsUtil:
    """Remote equivalent of secrets util"""

    def __init__(self, secrets_api: workspace.SecretsAPI):
        self._api = secrets_api # nolint

    def getBytes(self, scope: str, key: str) -> bytes:
        """Gets the bytes representation of a secret value for the specified scope and key."""
        query = {'scope': scope, 'key': key}
        raw = self._api._api.do('GET', '/api/2.0/secrets/get', query=query)
        return base64.b64decode(raw['value'])

    def get(self, scope: str, key: str) -> str:
        """Gets the string representation of a secret value for the specified secrets scope and key."""
        val = self.getBytes(scope, key)
        string_value = val.decode()
        return string_value

    def list(self, scope) -> typing.List[SecretMetadata]:
        """Lists the metadata for secrets within the specified scope."""

        # transform from SDK dataclass to dbutils-compatible namedtuple
        return [SecretMetadata(v.key) for v in self._api.list_secrets(scope)]

    def listScopes(self) -> typing.List[SecretScope]:
        """Lists the available scopes."""

        # transform from SDK dataclass to dbutils-compatible namedtuple
        return [SecretScope(v.name) for v in self._api.list_scopes()]


class RemoteDbUtils:

    def __init__(self, config: 'Config' = None):
        self._config = Config() if not config else config
        self._client = ApiClient(self._config)
        self._clusters = compute_ext.ClustersExt(self._client)
        self._commands = compute.CommandExecutionAPI(self._client)
        self._lock = threading.Lock()
        self._ctx = None

        self.fs = _FsUtil(dbfs_ext.DbfsExt(self._client), self.__getattr__)
        self.secrets = _SecretsUtil(workspace.SecretsAPI(self._client))

    @property
    def _cluster_id(self) -> str:
        cluster_id = self._config.cluster_id
        if not cluster_id:
            message = 'cluster_id is required in the configuration'
            raise ValueError(self._config.wrap_debug_info(message))
        return cluster_id

    def _running_command_context(self) -> compute.ContextStatusResponse:
        if self._ctx:
            return self._ctx
        with self._lock:
            if self._ctx:
                return self._ctx
            self._clusters.ensure_cluster_is_running(self._cluster_id)
            self._ctx = self._commands.create(cluster_id=self._cluster_id,
                                              language=compute.Language.python).result()
        return self._ctx

    def __getattr__(self, util) -> '_ProxyUtil':
        return _ProxyUtil(command_execution=self._commands,
                          context_factory=self._running_command_context,
                          cluster_id=self._cluster_id,
                          name=util)


class _ProxyUtil:
    """Enables temporary workaround to call remote in-REPL dbutils without having to re-implement them"""

    def __init__(self, *, command_execution: compute.CommandExecutionAPI,
                 context_factory: typing.Callable[[],
                                                  compute.ContextStatusResponse], cluster_id: str, name: str):
        self._commands = command_execution
        self._cluster_id = cluster_id
        self._context_factory = context_factory
        self._name = name

    def __getattr__(self, method: str) -> '_ProxyCall':
        return _ProxyCall(command_execution=self._commands,
                          cluster_id=self._cluster_id,
                          context_factory=self._context_factory,
                          util=self._name,
                          method=method)


class _ProxyCall:

    def __init__(self, *, command_execution: compute.CommandExecutionAPI,
                 context_factory: typing.Callable[[], compute.ContextStatusResponse], cluster_id: str,
                 util: str, method: str):
        self._commands = command_execution
        self._cluster_id = cluster_id
        self._context_factory = context_factory
        self._util = util
        self._method = method

    def __call__(self, *args, **kwargs):
        raw = json.dumps((args, kwargs))
        code = f'''
        import json
        (args, kwargs) = json.loads('{raw}')
        result = dbutils.{self._util}.{self._method}(*args, **kwargs)
        dbutils.notebook.exit(json.dumps(result))
        '''
        ctx = self._context_factory()
        result = self._commands.execute(cluster_id=self._cluster_id,
                                        language=compute.Language.python,
                                        context_id=ctx.id,
                                        command=code).result()
        if result.status == compute.CommandStatus.Finished:
            raw = result.results.data
            return json.loads(raw)
        else:
            raise Exception(result.results.summary)
