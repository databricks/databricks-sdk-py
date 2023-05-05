def _get_global_dbutils():
    try:
        global dbutils
        return dbutils
    except NameError:
        return None

is_oss_implementation = True

try:
    # Internal implementation
    from dbruntime import UserNamespaceInitializer

    # All objects that are injected into the Notebook's user namespace should also be made
    # available to be imported from databricks.sdk.runtime.globals. This import can be used
    # in Python modules so users can access these objects from Files more easily.
    __all__ = ["display", "displayHTML", "dbutils", "table", "sql", "udf", "getArgument", "sc", "sqlContext", "spark"]

    userNamespaceGlobals = UserNamespaceInitializer.getOrCreate().get_namespace_globals()
    _globals = globals()
    for var in __all__:
        _globals[var] = userNamespaceGlobals[var]
    is_oss_implementation = False
except ImportError:
    # OSS implementation
    is_oss_implementation = True
    dbutils = _get_global_dbutils()

    try:
        from .stub import *
    except ImportError:
        from databricks.sdk.dbutils import RemoteDbUtils
        if not dbutils:
            # this assumes that all environment variables are set
            dbutils = RemoteDbUtils()
    except NameError:
        from databricks.sdk.dbutils import RemoteDbUtils
        if not dbutils:
            # this assumes that all environment variables are set
            dbutils = RemoteDbUtils()

__all__ = ['dbutils'] if is_oss_implementation else ["display", "displayHTML", "dbutils", "table", "sql", "udf", "getArgument", "sc", "sqlContext", "spark"]
