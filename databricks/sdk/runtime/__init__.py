from __future__ import annotations

import logging
from typing import Dict, Union

logger = logging.getLogger('databricks.sdk')
is_local_implementation = True

# All objects that are injected into the Notebook's user namespace should also be made
# available to be imported from databricks.sdk.runtime.globals. This import can be used
# in Python modules so users can access these objects from Files more easily.
dbruntime_objects = [
    "display", "displayHTML", "dbutils", "table", "sql", "udf", "getArgument", "sc", "sqlContext", "spark"
]

# DO NOT MOVE THE TRY-CATCH BLOCK BELOW AND DO NOT ADD THINGS BEFORE IT! WILL MAKE TEST FAIL.
try:
    # We don't want to expose additional entity to user namespace, so
    # a workaround here for exposing required information in notebook environment
    from dbruntime.sdk_credential_provider import init_runtime_native_auth
    logger.debug('runtime SDK credential provider available')
    dbruntime_objects.append("init_runtime_native_auth")
except ImportError:
    init_runtime_native_auth = None

globals()["init_runtime_native_auth"] = init_runtime_native_auth


def init_runtime_repl_auth():
    try:
        from dbruntime.databricks_repl_context import get_context
        ctx = get_context()
        if ctx is None:
            logger.debug('Empty REPL context returned, skipping runtime auth')
            return None, None
        if ctx.workspaceUrl is None:
            logger.debug('Workspace URL is not available, skipping runtime auth')
            return None, None
        host = f'https://{ctx.workspaceUrl}'

        def inner() -> Dict[str, str]:
            ctx = get_context()
            return {'Authorization': f'Bearer {ctx.apiToken}'}

        return host, inner
    except ImportError:
        return None, None


def init_runtime_legacy_auth():
    try:
        import IPython
        ip_shell = IPython.get_ipython()
        if ip_shell is None:
            return None, None
        global_ns = ip_shell.ns_table["user_global"]
        if 'dbutils' not in global_ns:
            return None, None
        dbutils = global_ns["dbutils"].notebook.entry_point.getDbutils()
        if dbutils is None:
            return None, None
        ctx = dbutils.notebook().getContext()
        if ctx is None:
            return None, None
        host = getattr(ctx, 'apiUrl')().get()

        def inner() -> Dict[str, str]:
            ctx = dbutils.notebook().getContext()
            return {'Authorization': f'Bearer {getattr(ctx, "apiToken")().get()}'}

        return host, inner
    except ImportError:
        return None, None


try:
    # Internal implementation
    # Separated from above for backward compatibility
    from dbruntime import UserNamespaceInitializer

    userNamespaceGlobals = UserNamespaceInitializer.getOrCreate().get_namespace_globals()
    _globals = globals()
    for var in dbruntime_objects:
        if var not in userNamespaceGlobals:
            continue
        _globals[var] = userNamespaceGlobals[var]
    is_local_implementation = False
except ImportError:
    from typing import cast

    # OSS implementation
    is_local_implementation = True

    from databricks.sdk.dbutils import RemoteDbUtils

    from . import dbutils_stub

    dbutils_type = Union[dbutils_stub.dbutils, RemoteDbUtils]

    try:
        from .stub import *
    except (ImportError, NameError):
        # this assumes that all environment variables are set
        dbutils = RemoteDbUtils()

    dbutils = cast(dbutils_type, dbutils)

__all__ = ['dbutils'] if is_local_implementation else dbruntime_objects
