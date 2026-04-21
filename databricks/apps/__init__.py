# See: https://packaging.python.org/guides/packaging-namespace-packages/#pkgutil-style-namespace-packages
#
# This file keeps databricks.apps as a pkgutil-style namespace package alongside
# databricks.sdk. The content below is the public re-export surface.
__path__ = __import__("pkgutil").extend_path(__path__, __name__)

from databricks.apps._client import (
    get_mcp_client,
    get_user_workspace_client,
    get_workspace_client,
)

__all__ = [
    "get_mcp_client",
    "get_user_workspace_client",
    "get_workspace_client",
]
