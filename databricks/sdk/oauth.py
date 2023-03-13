import datetime
import logging
import threading
from abc import abstractmethod
from dataclasses import dataclass
from typing import List

import requests
import requests.auth

logger = logging.getLogger(__name__)


@dataclass
class Token:
    access_token: str
    token_type: str = None
    refresh_token: str = None
    expiry: datetime.datetime = None

    @property
    def expired(self):
        if not self.expiry:
            return False
        potentially_expired = self.expiry - datetime.timedelta(seconds=10)
        now = datetime.datetime.now()
        return potentially_expired < now

    @property
    def valid(self):
        return self.access_token and not self.expired


class TokenSource:

    @abstractmethod
    def token(self) -> Token:
        pass


class OAuthException(Exception):

    def __init__(self, *args: object):
        super().__init__(*args)


def retrieve_token(client_id, client_secret, token_url, params, use_params=False, use_header=False) -> Token:
    if use_params:
        if client_id: params["client_id"] = client_id
        if client_secret: params["client_secret"] = client_secret
    auth = None
    if use_header:
        auth = requests.auth.HTTPBasicAuth(client_id, client_secret)
    resp = requests.post(token_url, params, auth=auth)
    if not resp.ok:
        raise OAuthException(resp.content) # TODO: make it better
    try:
        j = resp.json()
        expires_in = int(j["expires_in"])
        expiry = datetime.datetime.now() + datetime.timedelta(seconds=expires_in)
        return Token(access_token=j["access_token"], token_type=j["token_type"], expiry=expiry)
    except Exception as e:
        raise OAuthException(f"Not supported yet: {e}")


class Refreshable(TokenSource):

    def __init__(self):
        self._lock = threading.Lock() # to guard _token
        self._token = None

    def token(self) -> Token:
        self._lock.acquire()
        try:
            if self._token and self._token.valid:
                return self._token
            self._token = self.refresh()
            return self._token
        finally:
            self._lock.release()

    @abstractmethod
    def refresh(self) -> Token:
        pass


@dataclass
class ClientCredentials(Refreshable):
    client_id: str
    client_secret: str
    token_url: str
    endpoint_params: dict = None
    scopes: List[str] = None
    use_params: bool = False
    use_header: bool = False

    def __post_init__(self):
        super().__init__()

    def refresh(self) -> Token:
        params = {"grant_type": "client_credentials"}
        if self.scopes:
            params["scope"] = " ".join(self.scopes)
        if self.endpoint_params:
            for k, v in self.endpoint_params.items():
                params[k] = v
        return retrieve_token(self.client_id,
                              self.client_secret,
                              self.token_url,
                              params,
                              use_params=self.use_params,
                              use_header=self.use_header)
