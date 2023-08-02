import base64
import json
import logging
import threading
import typing
from collections import namedtuple

from .core import ApiClient, Config, DatabricksError
from .mixins import compute as compute_ext
from .mixins import files as dbfs_ext
from .service import compute, workspace

_LOG = logging.getLogger('databricks.sdk')


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
              mount_point: str,
              encryption_type: str = None,
              owner: str = None,
              extra_configs: 'typing.Dict[str, str]' = None) -> bool:
        """Mounts the given source directory into DBFS at the given mount point"""
        fs = self._proxy_factory('fs')
        kwargs = {}
        if encryption_type:
            kwargs['encryption_type'] = encryption_type
        if owner:
            kwargs['owner'] = owner
        if extra_configs:
            kwargs['extra_configs'] = extra_configs
        return fs.mount(source, mount_point, **kwargs)

    def unmount(self, mount_point: str) -> bool:
        """Deletes a DBFS mount point"""
        fs = self._proxy_factory('fs')
        return fs.unmount(mount_point)

    def updateMount(self,
                    source: str,
                    mount_point: str,
                    encryption_type: str = None,
                    owner: str = None,
                    extra_configs: 'typing.Dict[str, str]' = None) -> bool:
        """ Similar to mount(), but updates an existing mount point (if present) instead of creating a new one """
        fs = self._proxy_factory('fs')
        kwargs = {}
        if encryption_type:
            kwargs['encryption_type'] = encryption_type
        if owner:
            kwargs['owner'] = owner
        if extra_configs:
            kwargs['extra_configs'] = extra_configs
        return fs.updateMount(source, mount_point, **kwargs)

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
        self._widgets = None

    # When we import widget_impl, the init file checks whether user has the
    # correct dependencies required for running on notebook or not (ipywidgets etc).
    # We only want these checks (and the subsequent errors and warnings), to
    # happen when the user actually uses widgets.
    @property
    def widgets(self):
        if self._widgets is None:
            from ._widgets import widget_impl
            self._widgets = widget_impl()

        return self._widgets

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
                                              language=compute.Language.PYTHON).result()
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


import html
import re


class _ProxyCall:

    def __init__(self, *, command_execution: compute.CommandExecutionAPI,
                 context_factory: typing.Callable[[], compute.ContextStatusResponse], cluster_id: str,
                 util: str, method: str):
        self._commands = command_execution
        self._cluster_id = cluster_id
        self._context_factory = context_factory
        self._util = util
        self._method = method

    _out_re = re.compile(r'Out\[[\d\s]+]:\s')
    _tag_re = re.compile(r'<[^>]*>')
    _exception_re = re.compile(r'.*Exception:\s+(.*)')
    _execution_error_re = re.compile(
        r'ExecutionError: ([\s\S]*)\n(StatusCode=[0-9]*)\n(StatusDescription=.*)\n')
    _error_message_re = re.compile(r'ErrorMessage=(.+)\n')
    _ascii_escape_re = re.compile(r'(\x9B|\x1B\[)[0-?]*[ -/]*[@-~]')

    def _is_failed(self, results: compute.Results) -> bool:
        return results.result_type == compute.ResultType.ERROR

    def _text(self, results: compute.Results) -> str:
        if results.result_type != compute.ResultType.TEXT:
            return ''
        return self._out_re.sub("", str(results.data))

    def _raise_if_failed(self, results: compute.Results):
        if not self._is_failed(results):
            return
        raise DatabricksError(self._error_from_results(results))

    def _error_from_results(self, results: compute.Results):
        if not self._is_failed(results):
            return
        if results.cause:
            _LOG.debug(f'{self._ascii_escape_re.sub("", results.cause)}')

        summary = self._tag_re.sub("", results.summary)
        summary = html.unescape(summary)

        exception_matches = self._exception_re.findall(summary)
        if len(exception_matches) == 1:
            summary = exception_matches[0].replace("; nested exception is:", "")
            summary = summary.rstrip(" ")
            return summary

        execution_error_matches = self._execution_error_re.findall(results.cause)
        if len(execution_error_matches) == 1:
            return "\n".join(execution_error_matches[0])

        error_message_matches = self._error_message_re.findall(results.cause)
        if len(error_message_matches) == 1:
            return error_message_matches[0]

        return summary

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
                                        language=compute.Language.PYTHON,
                                        context_id=ctx.id,
                                        command=code).result()
        if result.status == compute.CommandStatus.FINISHED:
            self._raise_if_failed(result.results)
            raw = result.results.data
            return json.loads(raw)
        else:
            raise Exception(result.results.summary)
