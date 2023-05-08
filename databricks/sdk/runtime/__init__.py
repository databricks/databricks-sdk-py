is_local_implementation = True

try:
    # Internal implementation
    from dbruntime import UserNamespaceInitializer

    # All objects that are injected into the Notebook's user namespace should also be made
    # available to be imported from databricks.sdk.runtime.globals. This import can be used
    # in Python modules so users can access these objects from Files more easily.
    __all__ = [
        "display", "displayHTML", "dbutils", "table", "sql", "udf", "getArgument", "sc", "sqlContext", "spark"
    ]

    userNamespaceGlobals = UserNamespaceInitializer.getOrCreate().get_namespace_globals()
    _globals = globals()
    for var in __all__:
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

__all__ = ['dbutils'] if is_local_implementation else [
    "display", "displayHTML", "dbutils", "table", "sql", "udf", "getArgument", "sc", "sqlContext", "spark"
]
