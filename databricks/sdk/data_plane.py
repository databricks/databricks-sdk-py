from dataclasses import dataclass
from typing import Callable

from databricks.sdk.oauth import Token
from databricks.sdk.service.oauth2 import DataPlaneInfo


@dataclass
class DataPlaneDetails:
    endpointUrl: str
    token: Token


class DataPlaneDetailsFetcher:

    def __init__(self):
        self._data_plane_info = {}
        self._tokens = {}

    def get_data_plane_details(self, method: str, params: list[str], refresh: Callable[[DataPlaneInfo], Token], info_getter: Callable[[], DataPlaneInfo]):
        all_elements = params.copy()
        all_elements.insert(0, method)
        map_key = "/".join(all_elements)
        info = self._data_plane_info.get(map_key)
        if not info:
            info = info_getter()
            self._data_plane_info[map_key] = info

        token = self._tokens.get(map_key)
        if not token or not token.valid():
            token = refresh(info)
            self._tokens[map_key] = token

        return DataPlaneDetails(endpointUrl=info.endpoint_url, token=token)
