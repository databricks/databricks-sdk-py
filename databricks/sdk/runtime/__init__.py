from typing import Callable, Dict, Tuple

is_local_implementation = True

# All objects that are injected into the Notebook's user namespace should also be made
# available to be imported from databricks.sdk.runtime.globals. This import can be used
# in Python modules so users can access these objects from Files more easily.
dbruntime_objects = [
    "display", "displayHTML", "dbutils", "table", "sql", "udf", "getArgument", "sc", "sqlContext", "spark"
]

RuntimeAuth = Tuple[str, Callable[[], Dict[str, str]]]


def init_runtime_native_auth() -> RuntimeAuth:
    raise NotImplementedError


try:
    # Internal implementation
    from dbruntime import UserNamespaceInitializer

    userNamespaceGlobals = UserNamespaceInitializer.getOrCreate().get_namespace_globals()
    _globals = globals()
    for var in dbruntime_objects:
        _globals[var] = userNamespaceGlobals[var]
    is_local_implementation = False
except ImportError:
    # OSS implementation
    is_local_implementation = True

    try:
        from .stub import *
    except (ImportError, NameError):
        from databricks.sdk.dbutils import RemoteDbUtils

        # this assumes that all environment variables are set
        dbutils = RemoteDbUtils()

__all__ = ['dbutils'] if is_local_implementation else dbruntime_objects
