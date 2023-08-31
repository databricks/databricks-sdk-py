import ast
import datetime
import html
import json
import logging
import platform
import re
import sys
import threading
import time
from dataclasses import dataclass
from typing import Any, Callable, Optional

from databricks.sdk.core import DatabricksError
from databricks.sdk.errors import OperationFailed
from databricks.sdk.service import compute

_LOG = logging.getLogger('databricks.sdk')
_out_re = re.compile(r"Out\[[\d\s]+]:\s")
_tag_re = re.compile(r"<[^>]*>")
_exception_re = re.compile(r".*Exception:\s+(.*)")
_execution_error_re = re.compile(r"ExecutionError: ([\s\S]*)\n(StatusCode=[0-9]*)\n(StatusDescription=.*)\n")
_error_message_re = re.compile(r"ErrorMessage=(.+)\n")
_ascii_escape_re = re.compile(r"(\x9B|\x1B\[)[0-?]*[ -/]*[@-~]")


@dataclass
class SemVer:
    major: int
    minor: int
    patch: int
    pre_release: Optional[str] = None
    build: Optional[str] = None

    # official https://semver.org/ recommendation: https://regex101.com/r/Ly7O1x/
    # with addition of "x" wildcards for minor/patch versions
    _pattern = re.compile(r"^"
                          r"(?P<major>0|[1-9]\d*)\.(?P<minor>x|0|[1-9]\d*)\.(?P<patch>x|0|[1-9x]\d*)"
                          r"(?:-(?P<pre_release>(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)"
                          r"(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?"
                          r"(?:\+(?P<build>[0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$")

    @classmethod
    def parse(cls, v: str) -> 'SemVer':
        if not v:
            raise ValueError(f'Not a valid SemVer: {v}')
        if v[0] != 'v':
            v = f'v{v}'
        m = cls._pattern.match(v[1:])
        if not m:
            raise ValueError(f'Not a valid SemVer: {v}')
        # patch and/or minor versions may be wildcards.
        # for now, we're converting wildcards to zeroes.
        minor = m.group('minor')
        patch = m.group('patch')
        return SemVer(major=int(m.group('major')),
                      minor=0 if minor == 'x' else int(minor),
                      patch=0 if patch == 'x' else int(patch),
                      pre_release=m.group('pre_release'),
                      build=m.group('build'))

    def __lt__(self, other: 'SemVer'):
        if not other:
            return False
        if self.major != other.major:
            return self.major < other.major
        if self.minor != other.minor:
            return self.minor < other.minor
        if self.patch != other.patch:
            return self.patch < other.patch
        if self.pre_release != other.pre_release:
            return self.pre_release < other.pre_release
        return self.build < other.build


class ClustersExt(compute.ClustersAPI):
    __doc__ = compute.ClustersAPI.__doc__

    def select_spark_version(self,
                             long_term_support: bool = False,
                             beta: bool = False,
                             latest: bool = True,
                             ml: bool = False,
                             genomics: bool = False,
                             gpu: bool = False,
                             scala: str = "2.12",
                             spark_version: str = None,
                             photon: bool = False,
                             graviton: bool = False) -> str:
        """Selects the latest Databricks Runtime Version.

        :param long_term_support: bool
        :param beta: bool
        :param latest: bool
        :param ml: bool
        :param gpu: bool
        :param scala: bool
        :param spark_version: bool
        :param photon: bool
        :param graviton: bool

        :returns: `spark_version` compatible string
        """
        # Logic ported from https://github.com/databricks/databricks-sdk-go/blob/main/service/compute/spark_version.go
        versions = []
        sv = self.spark_versions()
        for version in sv.versions:
            if "-scala" + scala not in version.key:
                continue
            matches = ((not "apache-spark-" in version.key) and (("-ml-" in version.key) == ml)
                       and (("-hls-" in version.key) == genomics) and (("-gpu-" in version.key) == gpu)
                       and (("-photon-" in version.key) == photon)
                       and (("-aarch64-" in version.key) == graviton) and (("Beta" in version.name) == beta))
            if matches and long_term_support:
                matches = matches and (("LTS" in version.name) or ("-esr-" in version.key))
            if matches and spark_version:
                matches = matches and ("Apache Spark " + spark_version in version.name)
            if matches:
                versions.append(version.key)
        if len(versions) < 1:
            raise ValueError("spark versions query returned no results")
        if len(versions) > 1:
            if not latest:
                raise ValueError("spark versions query returned multiple results")
            versions = sorted(versions, key=SemVer.parse, reverse=True)
        return versions[0]

    @staticmethod
    def _node_sorting_tuple(item: compute.NodeType) -> tuple:
        local_disks = local_disk_size_gb = local_nvme_disk = local_nvme_disk_size_gb = 0
        if item.node_instance_type is not None:
            local_disks = item.node_instance_type.local_disks
            local_nvme_disk = item.node_instance_type.local_nvme_disks
            local_disk_size_gb = item.node_instance_type.local_disk_size_gb
            local_nvme_disk_size_gb = item.node_instance_type.local_nvme_disk_size_gb
        return (item.is_deprecated, item.num_cores, item.memory_mb, local_disks, local_disk_size_gb,
                local_nvme_disk, local_nvme_disk_size_gb, item.num_gpus, item.instance_type_id)

    @staticmethod
    def _should_node_be_skipped(nt: compute.NodeType) -> bool:
        if not nt.node_info:
            return False
        if not nt.node_info.status:
            return False
        val = compute.CloudProviderNodeStatus
        for st in nt.node_info.status:
            if st in (val.NOT_AVAILABLE_IN_REGION, val.NOT_ENABLED_ON_SUBSCRIPTION):
                return True
        return False

    def select_node_type(self,
                         min_memory_gb: int = None,
                         gb_per_core: int = None,
                         min_cores: int = None,
                         min_gpus: int = None,
                         local_disk: bool = None,
                         local_disk_min_size: int = None,
                         category: str = None,
                         photon_worker_capable: bool = None,
                         photon_driver_capable: bool = None,
                         graviton: bool = None,
                         is_io_cache_enabled: bool = None,
                         support_port_forwarding: bool = None,
                         fleet: str = None) -> str:
        """Selects smallest available node type given the conditions.

        :param min_memory_gb: int
        :param gb_per_core: int
        :param min_cores: int
        :param min_gpus: int
        :param local_disk: bool
        :param local_disk_min_size: bool
        :param category: bool
        :param photon_worker_capable: bool
        :param photon_driver_capable: bool
        :param graviton: bool
        :param is_io_cache_enabled: bool

        :returns: `node_type` compatible string
        """
        # Logic ported from https://github.com/databricks/databricks-sdk-go/blob/main/service/clusters/node_type.go
        res = self.list_node_types()
        types = sorted(res.node_types, key=self._node_sorting_tuple)
        for nt in types:
            if self._should_node_be_skipped(nt):
                continue
            gbs = nt.memory_mb // 1024
            if fleet is not None and fleet not in nt.node_type_id:
                continue
            if min_memory_gb is not None and gbs < min_memory_gb:
                continue
            if gb_per_core is not None and gbs // nt.num_cores < gb_per_core:
                continue
            if min_cores is not None and nt.num_cores < min_cores:
                continue
            if (min_gpus is not None and nt.num_gpus < min_gpus) or (min_gpus == 0 and nt.num_gpus > 0):
                continue
            if local_disk or local_disk_min_size is not None:
                instance_type = nt.node_instance_type
                local_disks = int(instance_type.local_disks) if instance_type.local_disks else 0
                local_nvme_disks = int(
                    instance_type.local_nvme_disks) if instance_type.local_nvme_disks else 0
                if instance_type is None or (local_disks < 1 and local_nvme_disks < 1):
                    continue
                local_disk_size_gb = instance_type.local_disk_size_gb if instance_type.local_disk_size_gb else 0
                local_nvme_disk_size_gb = instance_type.local_nvme_disk_size_gb if instance_type.local_nvme_disk_size_gb else 0
                all_disks_size = local_disk_size_gb + local_nvme_disk_size_gb
                if local_disk_min_size is not None and all_disks_size < local_disk_min_size:
                    continue
            if category is not None and not nt.category.lower() == category.lower():
                continue
            if is_io_cache_enabled and not nt.is_io_cache_enabled:
                continue
            if support_port_forwarding and not nt.support_port_forwarding:
                continue
            if photon_driver_capable and not nt.photon_driver_capable:
                continue
            if photon_worker_capable and not nt.photon_worker_capable:
                continue
            if graviton and nt.is_graviton != graviton:
                continue
            return nt.node_type_id
        raise ValueError("cannot determine smallest node type")

    def ensure_cluster_is_running(self, cluster_id: str) -> None:
        """Ensures that given cluster is running, regardless of the current state"""
        timeout = datetime.timedelta(minutes=20)
        deadline = time.time() + timeout.total_seconds()
        while time.time() < deadline:
            try:
                state = compute.State
                info = self.get(cluster_id)
                if info.state == state.RUNNING:
                    return
                elif info.state == state.TERMINATED:
                    self.start(cluster_id).result()
                    return
                elif info.state == state.TERMINATING:
                    self.wait_get_cluster_terminated(cluster_id)
                    self.start(cluster_id).result()
                    return
                elif info.state in (state.PENDING, state.RESIZING, state.RESTARTING):
                    self.wait_get_cluster_running(cluster_id)
                    return
                elif info.state in (state.ERROR, state.UNKNOWN):
                    raise RuntimeError(f'Cluster {info.cluster_name} is {info.state}: {info.state_message}')
            except DatabricksError as e:
                if e.error_code == 'INVALID_STATE':
                    _LOG.debug(f'Cluster was started by other process: {e} Retrying.')
                    continue
                raise e
            except OperationFailed as e:
                _LOG.debug('Operation failed, retrying', exc_info=e)
        raise TimeoutError(f'timed out after {timeout}')

    def commands(self,
                 *,
                 cluster_id: Optional[str] = None,
                 language: compute.Language = compute.Language.PYTHON) -> 'CommandExecutor':
        """Create command executor for a cluster.

        Use `run` method on the result object to issue commands through a cluster and
        get their results. Upon the first command run the executor would ensure
        the cluster is running.

        :param cluster_id: str (optional)
            Databricks Cluster ID to run execute commands on. If no value is provided,
            `DATABRICKS_CLUSTER_ID` environment variable or `cluster_id` configuration
            attribute is used to find the cluster. In case no cluster is found, raises
            the `ValueError`.

        :param language: :class:`databricks.sdk.service.compute.Language`
            Supported programming language for command execution. Supported values are:
            - Language.PYTHON
            - Language.SCALA
            - Language.SQL

            By default, SDK creates command executors with Language.PYTHON.

        :return: :class:`CommandExecutor`
        """
        if not cluster_id:
            cluster_id = self._api._cfg.cluster_id
        if not cluster_id:
            message = 'cluster_id is required either in configuration or ' \
                      'in DATABRICKS_CLUSTER_ID environment variable'
            raise ValueError(message)
        command_execution_api = compute.CommandExecutionAPI(self._api)
        return CommandExecutor(self, command_execution_api, lambda: cluster_id, language=language)


class _ReturnToPrintJson(ast.NodeTransformer):

    def __init__(self) -> None:
        self._has_json_import = False
        self._has_print = False
        self.has_return = False

    @staticmethod
    def transform(code: str) -> (str, bool):
        unsupported_version = platform.python_version_tuple() < ('3', '9', '0')
        has_return_in_last_line = code.splitlines()[-1].startswith('return ')

        if unsupported_version and not has_return_in_last_line:
            return code, False

        if unsupported_version and has_return_in_last_line:
            raise ValueError(f'dynamic conversion of return .. to print(json.dumps(..)) '
                             f'is only possible starting from Python 3.8')

        # perform AST transformations for very repetitive tasks, like JSON serialization
        code_tree = ast.parse(code)
        transform = _ReturnToPrintJson()
        new_tree = transform.apply(code_tree)
        code = ast.unparse(new_tree)
        return code, transform.has_return

    def apply(self, node: ast.AST) -> ast.AST:
        node = self.visit(node)
        if self.has_return and self._has_print:
            msg = 'cannot have print() call, return .. is converted to print(json.dumps(..))'
            raise ValueError(msg)
        if self.has_return and not self._has_json_import:
            new_import = ast.parse("import json").body[0]
            node.body.insert(0, new_import)
        return node

    def visit_Import(self, node: ast.Import) -> ast.Import: # noqa: N802
        for name in node.names:
            if "json" != ast.unparse(name):
                continue
            self._has_json_import = True
            break
        return node

    def visit_Call(self, node: ast.Call): # noqa: N802
        if ast.unparse(node.func) == 'print':
            self._has_print = True
        return node

    def visit_Return(self, node): # noqa: N802
        value = node.value
        if not value:
            # Remove the original return statement
            return None
        return_expr = ast.unparse(value)
        replaced_code = f"print(json.dumps({return_expr}))"
        print_call = ast.parse(replaced_code).body[0]
        self.has_return = True
        return print_call


class CommandExecutor:

    def __init__(self,
                 clusters: ClustersExt,
                 command_execution: compute.CommandExecutionAPI,
                 cluster_id_provider: Callable[[], str],
                 *,
                 language: compute.Language = compute.Language.PYTHON):
        self._cluster_id_provider = cluster_id_provider
        self._language = language
        self._clusters = clusters
        self._commands = command_execution
        self._lock = threading.Lock()
        self._ctx = None

    def run(self, code: str, *, result_as_json=False, detect_return=True) -> Any:
        code = self._trim_leading_whitespace(code)

        if self._language == compute.Language.PYTHON and detect_return and not result_as_json:
            code, result_as_json = _ReturnToPrintJson.transform(code)

        ctx = self._running_command_context()
        cluster_id = self._cluster_id_provider()
        command_status_response = self._commands.execute(cluster_id=cluster_id,
                                                         language=self._language,
                                                         context_id=ctx.id,
                                                         command=code).result()

        results = command_status_response.results
        if command_status_response.status == compute.CommandStatus.FINISHED:
            self._raise_if_failed(results)
            if results.result_type == compute.ResultType.TEXT and result_as_json:
                try:
                    # parse json from converted return statement
                    return json.loads(results.data)
                except json.JSONDecodeError as e:
                    _LOG.warning('cannot parse converted return statement. Just returning text', exc_info=e)
                    return results.data
            return results.data
        else:
            # there might be an opportunity to convert builtin exceptions
            raise DatabricksError(results.summary)

    def install_notebook_library(self, library: str):
        return self.run(f"""
            get_ipython().run_line_magic('pip', 'install {library}')
            dbutils.library.restartPython()
            """)

    def _running_command_context(self) -> compute.ContextStatusResponse:
        if self._ctx:
            return self._ctx
        with self._lock:
            if self._ctx:
                return self._ctx
            cluster_id = self._cluster_id_provider()
            self._clusters.ensure_cluster_is_running(cluster_id)
            self._ctx = self._commands.create(cluster_id=cluster_id, language=self._language).result()
        return self._ctx

    @staticmethod
    def _is_failed(results: compute.Results) -> bool:
        return results.result_type == compute.ResultType.ERROR

    @staticmethod
    def _text(results: compute.Results) -> str:
        if results.result_type != compute.ResultType.TEXT:
            return ""
        return _out_re.sub("", str(results.data))

    def _raise_if_failed(self, results: compute.Results):
        if not self._is_failed(results):
            return
        raise DatabricksError(self._error_from_results(results))

    def _error_from_results(self, results: compute.Results) -> str:
        if not self._is_failed(results):
            return ''
        if results.cause:
            sys.stderr.write(_ascii_escape_re.sub("", results.cause))

        summary = _tag_re.sub("", results.summary)
        summary = html.unescape(summary)

        exception_matches = _exception_re.findall(summary)
        if len(exception_matches) == 1:
            summary = exception_matches[0].replace("; nested exception is:", "")
            summary = summary.rstrip(" ")
            return summary

        execution_error_matches = _execution_error_re.findall(results.cause)
        if len(execution_error_matches) == 1:
            return "\n".join(execution_error_matches[0])

        error_message_matches = _error_message_re.findall(results.cause)
        if len(error_message_matches) == 1:
            return error_message_matches[0]

        return summary

    @staticmethod
    def _trim_leading_whitespace(command_str: str) -> str:
        """Removes leading whitespace, so that Python code blocks that
        are embedded into Python code still could be interpreted properly."""
        lines = command_str.replace("\t", "    ").split("\n")
        leading_whitespace = float("inf")
        if lines[0] == "":
            lines = lines[1:]
        for line in lines:
            pos = 0
            for char in line:
                if char in (" ", "\t"):
                    pos += 1
                else:
                    break
            if pos < leading_whitespace:
                leading_whitespace = pos
        new_command = ""
        for line in lines:
            if line == "" or line.strip(" \t") == "":
                continue
            if len(line) < leading_whitespace:
                new_command += line + "\n"
            else:
                new_command += line[leading_whitespace:] + "\n"
        return new_command.strip()
