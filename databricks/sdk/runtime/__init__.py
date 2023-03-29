def _get_global_dbutils():
    try:
        global dbutils
        return dbutils
    except NameError:
        return None


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

__all__ = ['dbutils']
