import threading
from dataclasses import dataclass
from typing import Callable, List

from databricks.sdk.oauth import Token
from databricks.sdk.service.oauth2 import DataPlaneInfo


@dataclass
class DataPlaneDetails:
    """
    Contains details required to query a DataPlane endpoint.
    """
    endpoint_url: str
    """URL used to query the endpoint through the DataPlane."""
    token: Token
    """Token to query the DataPlane endpoint."""


class DataPlaneService:
    """Helper class to fetch and manage DataPlane details."""

    def __init__(self):
        self._data_plane_info = {}
        self._tokens = {}
        self._lock = threading.Lock()

    def get_data_plane_details(self, method: str, params: List[str], info_getter: Callable[[], DataPlaneInfo],
                               refresh: Callable[[str], Token]):
        """Get and cache information required to query a Data Plane endpoint using the provided methods.

        Returns a cached DataPlaneDetails if the details have already been fetched previously and are still valid.
        If not, it uses the provided functions to fetch the details.

        :param method: method name. Used to construct a unique key for the cache.
        :param params: path params used in the "get" operation which uniquely determine the object. Used to construct a unique key for the cache.
        :param info_getter: function which returns the DataPlaneInfo. It will only be called if the information is not already present in the cache.
        :param refresh: function to refresh the token. It will only be called if the token is missing or expired.
        """
        all_elements = params.copy()
        all_elements.insert(0, method)
        map_key = "/".join(all_elements)
        info = self._data_plane_info.get(map_key)
        if not info:
            self._lock.acquire()
            try:
                info = self._data_plane_info.get(map_key)
                if not info:
                    info = info_getter()
                    self._data_plane_info[map_key] = info
            finally:
                self._lock.release()

        token = self._tokens.get(map_key)
        if not token or not token.valid:
            self._lock.acquire()
            token = self._tokens.get(map_key)
            try:
                if not token or not token.valid:
                    token = refresh(info.authorization_details)
                    self._tokens[map_key] = token
            finally:
                self._lock.release()

        return DataPlaneDetails(endpoint_url=info.endpoint_url, token=token)
