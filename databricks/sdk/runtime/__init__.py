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
    from ._impl import _RemoteDbUtils
    if not dbutils:
        dbutils = _RemoteDbUtils()
except NameError:
    from ._impl import _RemoteDbUtils
    if not dbutils:
        dbutils = _RemoteDbUtils()

__all__ = ['dbutils']
