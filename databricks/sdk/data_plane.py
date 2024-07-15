import threading
from dataclasses import dataclass
from typing import Callable, List

from databricks.sdk.oauth import Token
from databricks.sdk.service.oauth2 import DataPlaneInfo


@dataclass
class DataPlaneDetails:
    endpoint_url: str
    token: Token


class DataPlaneService:

    def __init__(self):
        self._data_plane_info = {}
        self._tokens = {}
        self._lock = threading.Lock()

    def get_data_plane_details(self, method: str, params: List[str], info_getter: Callable[[], DataPlaneInfo],
                               refresh: Callable[[str], Token]):
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
