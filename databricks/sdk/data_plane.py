from __future__ import annotations

import threading
from dataclasses import dataclass
from typing import Callable, List, Optional
from urllib import parse

from databricks.sdk import oauth
from databricks.sdk.oauth import Token

URL_ENCODED_CONTENT_TYPE = "application/x-www-form-urlencoded"
JWT_BEARER_GRANT_TYPE = "urn:ietf:params:oauth:grant-type:jwt-bearer"
OIDC_TOKEN_PATH = "/oidc/v1/token"


class DataPlaneTokenSource:
    """
    EXPERIMENTAL Manages token sources for multiple DataPlane endpoints.
    """

    # TODO: Enable async once its stable. @oauth_credentials_provider must also have async enabled.
    def __init__(self, token_exchange_host: str, cpts: Callable[[], Token], disable_async: Optional[bool] = True):
        self._cpts = cpts
        self._token_exchange_host = token_exchange_host
        self._token_sources = {}
        self._disable_async = disable_async
        self._lock = threading.Lock()

    def token(self, endpoint, auth_details):
        key = f"{endpoint}:{auth_details}"

        # First, try to read without acquiring the lock to avoid contention.
        # Reads are atomic, so this is safe.
        token_source = self._token_sources.get(key)
        if token_source:
            return token_source.token()

        # If token_source is not found, acquire the lock and check again.
        with self._lock:
            # Another thread might have created it while we were waiting for the lock.
            token_source = self._token_sources.get(key)
            if not token_source:
                token_source = DataPlaneEndpointTokenSource(
                    self._token_exchange_host, self._cpts, auth_details, self._disable_async
                )
                self._token_sources[key] = token_source

        return token_source.token()


class DataPlaneEndpointTokenSource(oauth.Refreshable):
    """
    EXPERIMENTAL A token source for a specific DataPlane endpoint.
    """

    def __init__(self, token_exchange_host: str, cpts: Callable[[], Token], auth_details: str, disable_async: bool):
        super().__init__(disable_async=disable_async)
        self._auth_details = auth_details
        self._cpts = cpts
        self._token_exchange_host = token_exchange_host

    def refresh(self) -> Token:
        control_plane_token = self._cpts()
        headers = {"Content-Type": URL_ENCODED_CONTENT_TYPE}
        params = parse.urlencode(
            {
                "grant_type": JWT_BEARER_GRANT_TYPE,
                "authorization_details": self._auth_details,
                "assertion": control_plane_token.access_token,
            }
        )
        return oauth.retrieve_token(
            client_id="",
            client_secret="",
            token_url=self._token_exchange_host + OIDC_TOKEN_PATH,
            params=params,
            headers=headers,
        )


@dataclass
class DataPlaneDetails:
    """
    Contains details required to query a DataPlane endpoint.
    """

    endpoint_url: str
    """URL used to query the endpoint through the DataPlane."""
    token: Token
    """Token to query the DataPlane endpoint."""


## Old implementation. #TODO: Remove after the new implementation is used


class DataPlaneService:
    """Helper class to fetch and manage DataPlane details."""

    from .service.serving import DataPlaneInfo

    def __init__(self):
        self._data_plane_info = {}
        self._tokens = {}
        self._lock = threading.Lock()

    def get_data_plane_details(
        self,
        method: str,
        params: List[str],
        info_getter: Callable[[], DataPlaneInfo],
        refresh: Callable[[str], Token],
    ):
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
