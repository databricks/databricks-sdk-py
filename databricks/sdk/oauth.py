import base64
import datetime
import functools
import hashlib
import logging
import secrets
import threading
import urllib.parse
import webbrowser
from abc import abstractmethod
from dataclasses import dataclass
from http.server import BaseHTTPRequestHandler, HTTPServer
from typing import List

import requests
import requests.auth

logger = logging.getLogger(__name__)


@dataclass
class OidcEndpoints:
    authorization_endpoint: str # ../v1/authorize
    token_endpoint: str # ../v1/token


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
        now = datetime.datetime.now(tz=potentially_expired.tzinfo)
        is_expired = potentially_expired < now
        return is_expired

    @property
    def valid(self):
        return self.access_token and not self.expired

    def as_dict(self) -> dict:
        raw = {'access_token': self.access_token, 'token_type': self.token_type, 'expiry': self.expiry}
        if self.refresh_token:
            raw['refresh_token'] = self.refresh_token
        return raw

    @staticmethod
    def from_dict(raw: dict) -> 'Token':
        return Token(access_token=raw['access_token'],
                     token_type=raw['token_type'],
                     expiry=raw['expiry'],
                     refresh_token=raw.get('refresh_token'))


class TokenSource:

    @abstractmethod
    def token(self) -> Token:
        pass


def retrieve_token(client_id,
                   client_secret,
                   token_url,
                   params,
                   use_params=False,
                   use_header=False,
                   headers=None) -> Token:
    logger.debug(f'Retrieving token for {client_id}')
    if use_params:
        if client_id: params["client_id"] = client_id
        if client_secret: params["client_secret"] = client_secret
    auth = None
    if use_header:
        auth = requests.auth.HTTPBasicAuth(client_id, client_secret)
    resp = requests.post(token_url, params, auth=auth, headers=headers)
    if not resp.ok:
        if resp.headers['Content-Type'].startswith('application/json'):
            err = resp.json()
            code = err.get('errorCode', err.get('error', 'unknown'))
            summary = err.get('errorSummary', err.get('error_description', 'unknown'))
            raise ValueError(f'{code}: {summary}')
        raise ValueError(resp.content)
    try:
        j = resp.json()
        expires_in = int(j["expires_in"])
        expiry = datetime.datetime.now() + datetime.timedelta(seconds=expires_in)
        return Token(access_token=j["access_token"],
                     refresh_token=j.get('refresh_token'),
                     token_type=j["token_type"],
                     expiry=expiry)
    except Exception as e:
        raise NotImplementedError(f"Not supported yet: {e}")


class Refreshable(TokenSource):

    def __init__(self, token=None):
        self._lock = threading.Lock() # to guard _token
        self._token = token

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


class _OAuthCallback(BaseHTTPRequestHandler):

    def __init__(self, feedback: list, *args):
        self._feedback = feedback
        super().__init__(*args)

    def do_GET(self):
        from urllib.parse import parse_qsl
        parts = self.path.split('?')
        if len(parts) != 2:
            self.send_error(400, 'Missing Query')
            return

        query = dict(parse_qsl(parts[1]))
        self._feedback.append(query)

        if 'error' in query:
            self.send_error(400, query['error'], query.get('error_description'))
            return

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        # TODO: show better message
        self.wfile.write(b'You can close this tab.')


class RefreshableCredentials(Refreshable):

    def __init__(self, flow: 'InteractiveFlow', token: Token):
        self._flow = flow
        super().__init__(token)

    def as_dict(self) -> dict:
        return {'flow': self._flow.as_dict(), 'token': self._token.as_dict()}

    @staticmethod
    def from_dict(raw: dict) -> 'RefreshableCredentials':
        return RefreshableCredentials(flow=InteractiveFlow.from_dict(raw['flow']),
                                      token=Token.from_dict(raw['token']))

    def auth_type(self):
        """Implementing CredentialsProvider protocol"""
        # TODO: distinguish between Databricks IDP and Azure AD
        return 'oauth'

    def __call__(self, *args, **kwargs):
        """Implementing CredentialsProvider protocol"""

        def inner() -> dict[str, str]:
            return {'Authorization': f"Bearer {self.token().access_token}"}

        return inner

    def refresh(self) -> Token:
        refresh_token = self._token.refresh_token
        if not refresh_token:
            raise ValueError('oauth2: token expired and refresh token is not set')
        params = {'grant_type': 'refresh_token', 'refresh_token': refresh_token}
        headers = {}
        if 'microsoft' in self._flow.token_url:
            # Tokens issued for the 'Single-Page Application' client-type may
            # only be redeemed via cross-origin requests
            headers = {'Origin': self._flow.redirect_url}
        return retrieve_token(client_id=self._flow.client_id,
                              client_secret=self._flow.client_secret,
                              token_url=self._flow.token_url,
                              params=params,
                              use_params=True,
                              headers=headers)


@dataclass
class Consent:
    flow: 'InteractiveFlow'
    auth_url: str
    state: str
    verifier: str

    def as_dict(self) -> dict:
        return {
            'flow': self.flow.as_dict(),
            'auth_url': self.auth_url,
            'state': self.state,
            'verifier': self.verifier
        }

    @staticmethod
    def from_dict(raw: dict) -> 'Consent':
        return Consent(flow=InteractiveFlow.from_dict(raw['flow']),
                       auth_url=raw['auth_url'],
                       state=raw['state'],
                       verifier=raw['verifier'])

    def launch_external_browser(self) -> RefreshableCredentials:
        redirect_url = urllib.parse.urlparse(self.flow.redirect_url)
        if redirect_url.hostname not in ('localhost', '127.0.0.1'):
            raise ValueError(f'cannot listen on {redirect_url.hostname}')
        feedback = []
        logger.info(f'Opening {self.auth_url} in a browser')
        webbrowser.open_new(self.auth_url)
        port = redirect_url.port
        handler_factory = functools.partial(_OAuthCallback, feedback)
        with HTTPServer(("localhost", port), handler_factory) as httpd:
            logger.info(f'Waiting for redirect to http://localhost:{port}')
            httpd.handle_request()
        if not feedback:
            raise ValueError('No data received in callback')
        query = feedback.pop()
        return self.exchange_query(query)

    def exchange_query(self, query: dict[str, str]) -> RefreshableCredentials:
        if 'error' in query:
            raise ValueError('{error}: {error_description}'.format(**query))
        if 'code' not in query or 'state' not in query:
            raise ValueError('No code returned in callback')
        return self.exchange(query['code'], query['state'])

    def exchange(self, code: str, state: str) -> RefreshableCredentials:
        if self.state != state:
            raise ValueError('state mismatch')
        params = {
            'grant_type': 'authorization_code',
            'code': code,
            'code_verifier': self.verifier,
            'redirect_uri': self.flow.redirect_url
        }
        headers = {}
        if 'microsoft' in self.flow.token_url:
            # Tokens issued for the 'Single-Page Application' client-type may
            # only be redeemed via cross-origin requests
            headers = {'Origin': self.flow.redirect_url}
        token = retrieve_token(client_id=self.flow.client_id,
                               client_secret=self.flow.client_secret,
                               token_url=self.flow.token_url,
                               params=params,
                               headers=headers,
                               use_params=True)
        return RefreshableCredentials(self.flow, token)


@dataclass
class InteractiveFlow:
    """Enables 3-legged OAuth2 flow with PKCE

    For a regular web app running on a server, it's recommended to use
    the Authorization Code Flow to obtain an Access Token and a Refresh
    Token. This method is considered safe because the Access Token is
    transmitted directly to the server hosting the app, without passing
    through the user's web browser and risking exposure.

    To enhance the security of the Authorization Code Flow, the PKCE
    (Proof Key for Code Exchange) mechanism can be employed. With PKCE,
    the calling application generates a secret called the Code Verifier,
    which is verified by the authorization server. The app also creates
    a transform value of the Code Verifier, called the Code Challenge,
    and sends it over HTTPS to obtain an Authorization Code.
    By intercepting the Authorization Code, a malicious attacker cannot
    exchange it for a token without possessing the Code Verifier."""

    client_id: str
    auth_url: str
    token_url: str
    redirect_url: str
    scopes: list[str]
    client_secret: str = None
    use_params: bool = False
    use_header: bool = False

    def as_dict(self) -> dict:
        raw = {
            'client_id': self.client_id,
            'auth_url': self.auth_url,
            'token_url': self.token_url,
            'redirect_url': self.redirect_url,
            'scopes': self.scopes,
            'use_params': self.use_params,
            'use_header': self.use_header
        }
        if self.client_secret:
            raw['client_secret'] = self.client_secret
        return raw

    @staticmethod
    def from_dict(raw: dict) -> 'InteractiveFlow':
        return InteractiveFlow(client_id=raw['client_id'],
                               client_secret=raw.get('client_secret'),
                               redirect_url=raw['redirect_url'],
                               auth_url=raw['auth_url'],
                               token_url=raw['token_url'],
                               scopes=raw['scopes'],
                               use_params=raw.get('use_params', False),
                               use_header=raw.get('use_header', False))

    def auth_code_url(self) -> Consent:
        state = secrets.token_urlsafe(16)

        # token_urlsafe() already returns base64-encoded string

        verifier = secrets.token_urlsafe(32)
        digest = hashlib.sha256(verifier.encode("UTF-8")).digest()
        challenge = (base64.urlsafe_b64encode(digest).decode("UTF-8").replace("=", ""))

        # verifier = secrets.token_bytes(32)
        # sha256 = hashlib.sha256(verifier)
        # challenge = base64.b64encode(sha256.digest()).decode('utf8')

        params = {
            'response_type': 'code',
            'client_id': self.client_id,
            'redirect_uri': self.redirect_url,
            'scope': ' '.join(self.scopes),
            'state': state,
            'code_challenge': challenge,
            'code_challenge_method': 'S256'
        }
        url = f'{self.auth_url}?{urllib.parse.urlencode(params)}'
        return Consent(flow=self, auth_url=url, state=state, verifier=verifier)


@dataclass
class ClientCredentials(Refreshable):
    """Enables client credentials 2-legged OAuth2 flow

    When it comes to authorizing machine-to-machine interactions,
    the need for end-user authorization is eliminated because the SDK
    functions as both the Resource Owner and Client. Typical example is
    the CI/CD process or any other automated job. In this scenario,
    the background job uses the Client ID and Client Secret to obtain
    an Access Token from the Authorization Server.
    """
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
