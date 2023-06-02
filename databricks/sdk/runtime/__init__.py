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
    dbruntime_objects.append("init_runtime_native_auth")
except ImportError:
    init_runtime_native_auth = None

globals()["init_runtime_native_auth"] = init_runtime_native_auth

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
    # OSS implementation
    is_local_implementation = True

    try:
        from .stub import *
    except (ImportError, NameError):
        from databricks.sdk.dbutils import RemoteDbUtils

        # this assumes that all environment variables are set
        dbutils = RemoteDbUtils()

__all__ = ['dbutils'] if is_local_implementation else dbruntime_objects
