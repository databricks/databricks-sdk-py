import base64
import functools
import hashlib
import json
import logging
import os
import secrets
import threading
import urllib.parse
import webbrowser
from abc import abstractmethod
from dataclasses import dataclass
from datetime import datetime, timedelta
from http.server import BaseHTTPRequestHandler, HTTPServer
from typing import Any, Dict, List, Optional

import requests
import requests.auth

# Error code for PKCE flow in Azure Active Directory, that gets additional retry.
# See https://stackoverflow.com/a/75466778/277035 for more info
NO_ORIGIN_FOR_SPA_CLIENT_ERROR = 'AADSTS9002327'

URL_ENCODED_CONTENT_TYPE = "application/x-www-form-urlencoded"
JWT_BEARER_GRANT_TYPE = "urn:ietf:params:oauth:grant-type:jwt-bearer"
OIDC_TOKEN_PATH = "/oidc/v1/token"

logger = logging.getLogger(__name__)


class IgnoreNetrcAuth(requests.auth.AuthBase):
    """This auth method is a no-op.

    We use it to force requestslib to not use .netrc to write auth headers
    when making .post() requests to the oauth token endpoints, since these
    don't require authentication.

    In cases where .netrc is outdated or corrupt, these requests will fail.

    See issue #121
    """

    def __call__(self, r):
        return r


@dataclass
class OidcEndpoints:
    authorization_endpoint: str # ../v1/authorize
    token_endpoint: str # ../v1/token


@dataclass
class Token:
    access_token: str
    token_type: str = None
    refresh_token: str = None
    expiry: datetime = None

    @property
    def expired(self):
        if not self.expiry:
            return False
        # Azure Databricks rejects tokens that expire in 30 seconds or less,
        # so we refresh the token 40 seconds before it expires.
        potentially_expired = self.expiry - timedelta(seconds=40)
        now = datetime.now(tz=potentially_expired.tzinfo)
        is_expired = potentially_expired < now
        return is_expired

    @property
    def valid(self):
        return self.access_token and not self.expired

    def as_dict(self) -> dict:
        raw = {'access_token': self.access_token, 'token_type': self.token_type}
        if self.expiry:
            raw['expiry'] = self.expiry.isoformat()
        if self.refresh_token:
            raw['refresh_token'] = self.refresh_token
        return raw

    @staticmethod
    def from_dict(raw: dict) -> 'Token':
        return Token(access_token=raw['access_token'],
                     token_type=raw['token_type'],
                     expiry=datetime.fromisoformat(raw['expiry']),
                     refresh_token=raw.get('refresh_token'))

    def jwt_claims(self) -> Dict[str, str]:
        """Get claims from the access token or return an empty dictionary if it is not a JWT token.

        All refreshable tokens we're dealing with are JSON Web Tokens (JWT).

        The common claims are:
        - 'aud' represents the intended recipient of the token. In case of Azure, this is an app's Application ID
                assigned within the Azure portal.
        - 'iss' serves to identify the security token service (STS) responsible for creating and delivering the token.
                In case of Azure, it includes the Azure AD tenant where user authentication occurred.
        - 'appid' stands for the application ID of the client utilizing this token. This application can operate either
                autonomously or on behalf of a user. The application ID commonly represents an application object but
                may also denote a service principal object in case of Azure.
        - 'idp' is used to document the identity provider that authenticated the subject of the token.
        - 'oid' is the unchanging identifier for an entity within the identity system.
        - 'sub' identifies the primary entity for the token, such as the user of an app. This value is specific to
                a particular application ID. If a single user logs into two different apps using distinct client IDs,
                these apps will receive different values for the subject claim.
        - 'tid' In case of Azure, this value represents Azure Tenant ID.

        See https://datatracker.ietf.org/doc/html/rfc7519 for specification.
        See https://jwt.ms for debugger.
        """
        try:
            jwt_split = self.access_token.split(".")
            if len(jwt_split) != 3:
                logger.debug(f'Tried to decode access token as JWT, but failed: {len(jwt_split)} components')
                return {}
            payload_with_padding = jwt_split[1] + "=="
            payload_bytes = base64.standard_b64decode(payload_with_padding)
            payload_json = payload_bytes.decode("utf8")
            claims = json.loads(payload_json)
            return claims
        except ValueError as err:
            logger.debug(f'Tried to decode access token as JWT, but failed: {err}')
            return {}


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
    else:
        auth = IgnoreNetrcAuth()
    resp = requests.post(token_url, params, auth=auth, headers=headers)
    if not resp.ok:
        if resp.headers['Content-Type'].startswith('application/json'):
            err = resp.json()
            code = err.get('errorCode', err.get('error', 'unknown'))
            summary = err.get('errorSummary', err.get('error_description', 'unknown'))
            summary = summary.replace("\r\n", ' ')
            raise ValueError(f'{code}: {summary}')
        raise ValueError(resp.content)
    try:
        j = resp.json()
        expires_in = int(j["expires_in"])
        expiry = datetime.now() + timedelta(seconds=expires_in)
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

    def log_message(self, fmt: str, *args: Any) -> None:
        logger.debug(fmt, *args)

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


class SessionCredentials(Refreshable):

    def __init__(self, client: 'OAuthClient', token: Token):
        self._client = client
        super().__init__(token)

    def as_dict(self) -> dict:
        return {'token': self._token.as_dict()}

    @staticmethod
    def from_dict(client: 'OAuthClient', raw: dict) -> 'SessionCredentials':
        return SessionCredentials(client=client, token=Token.from_dict(raw['token']))

    def auth_type(self):
        """Implementing CredentialsProvider protocol"""
        # TODO: distinguish between Databricks IDP and Azure AD
        return 'oauth'

    def __call__(self, *args, **kwargs):
        """Implementing CredentialsProvider protocol"""

        def inner() -> Dict[str, str]:
            return {'Authorization': f"Bearer {self.token().access_token}"}

        return inner

    def refresh(self) -> Token:
        refresh_token = self._token.refresh_token
        if not refresh_token:
            raise ValueError('oauth2: token expired and refresh token is not set')
        params = {'grant_type': 'refresh_token', 'refresh_token': refresh_token}
        headers = {}
        if 'microsoft' in self._client.token_url:
            # Tokens issued for the 'Single-Page Application' client-type may
            # only be redeemed via cross-origin requests
            headers = {'Origin': self._client.redirect_url}
        return retrieve_token(client_id=self._client.client_id,
                              client_secret=self._client.client_secret,
                              token_url=self._client.token_url,
                              params=params,
                              use_params=True,
                              headers=headers)


class Consent:

    def __init__(self, client: 'OAuthClient', state: str, verifier: str, auth_url: str = None) -> None:
        self.auth_url = auth_url

        self._verifier = verifier
        self._state = state
        self._client = client

    def as_dict(self) -> dict:
        return {'state': self._state, 'verifier': self._verifier}

    @staticmethod
    def from_dict(client: 'OAuthClient', raw: dict) -> 'Consent':
        return Consent(client, raw['state'], raw['verifier'])

    def launch_external_browser(self) -> SessionCredentials:
        redirect_url = urllib.parse.urlparse(self._client.redirect_url)
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
        return self.exchange_callback_parameters(query)

    def exchange_callback_parameters(self, query: Dict[str, str]) -> SessionCredentials:
        if 'error' in query:
            raise ValueError('{error}: {error_description}'.format(**query))
        if 'code' not in query or 'state' not in query:
            raise ValueError('No code returned in callback')
        return self.exchange(query['code'], query['state'])

    def exchange(self, code: str, state: str) -> SessionCredentials:
        if self._state != state:
            raise ValueError('state mismatch')
        params = {
            'redirect_uri': self._client.redirect_url,
            'grant_type': 'authorization_code',
            'code_verifier': self._verifier,
            'code': code
        }
        headers = {}
        while True:
            try:
                token = retrieve_token(client_id=self._client.client_id,
                                       client_secret=self._client.client_secret,
                                       token_url=self._client.token_url,
                                       params=params,
                                       headers=headers,
                                       use_params=True)
                return SessionCredentials(self._client, token)
            except ValueError as e:
                if NO_ORIGIN_FOR_SPA_CLIENT_ERROR in str(e):
                    # Retry in cases of 'Single-Page Application' client-type with
                    # 'Origin' header equal to client's redirect URL.
                    headers['Origin'] = self._client.redirect_url
                    msg = f'Retrying OAuth token exchange with {self._client.redirect_url} origin'
                    logger.debug(msg)
                    continue
                raise e


class OAuthClient:
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
    exchange it for a token without possessing the Code Verifier.
    """

    def __init__(self,
                 host: str,
                 client_id: str,
                 redirect_url: str,
                 *,
                 scopes: List[str] = None,
                 client_secret: str = None):
        # TODO: is it a circular dependency?..
        from .core import Config
        from .credentials_provider import credentials_strategy

        @credentials_strategy('noop', [])
        def noop_credentials(_: any):
            return lambda: {}

        config = Config(host=host, credentials_strategy=noop_credentials)
        if not scopes:
            scopes = ['all-apis']
        oidc = config.oidc_endpoints
        if not oidc:
            raise ValueError(f'{host} does not support OAuth')

        self.host = host
        self.redirect_url = redirect_url
        self.client_id = client_id
        self.client_secret = client_secret
        self.token_url = oidc.token_endpoint
        self.is_aws = config.is_aws
        self.is_azure = config.is_azure
        self.is_gcp = config.is_gcp

        self._auth_url = oidc.authorization_endpoint
        self._scopes = scopes

    def initiate_consent(self) -> Consent:
        state = secrets.token_urlsafe(16)

        # token_urlsafe() already returns base64-encoded string
        verifier = secrets.token_urlsafe(32)
        digest = hashlib.sha256(verifier.encode("UTF-8")).digest()
        challenge = (base64.urlsafe_b64encode(digest).decode("UTF-8").replace("=", ""))

        params = {
            'response_type': 'code',
            'client_id': self.client_id,
            'redirect_uri': self.redirect_url,
            'scope': ' '.join(self._scopes),
            'state': state,
            'code_challenge': challenge,
            'code_challenge_method': 'S256'
        }
        url = f'{self._auth_url}?{urllib.parse.urlencode(params)}'
        return Consent(self, state, verifier, auth_url=url)

    def __repr__(self) -> str:
        return f'<OAuthClient {self.host} client_id={self.client_id}>'


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


class TokenCache():
    BASE_PATH = "~/.config/databricks-sdk-py/oauth"

    def __init__(self, client: OAuthClient) -> None:
        self.client = client

    @property
    def filename(self) -> str:
        # Include host, client_id, and scopes in the cache filename to make it unique.
        hash = hashlib.sha256()
        for chunk in [self.client.host, self.client.client_id, ",".join(self.client._scopes), ]:
            hash.update(chunk.encode('utf-8'))
        return os.path.expanduser(os.path.join(self.__class__.BASE_PATH, hash.hexdigest() + ".json"))

    def load(self) -> Optional[SessionCredentials]:
        """
        Load credentials from cache file. Return None if the cache file does not exist or is invalid.
        """
        if not os.path.exists(self.filename):
            return None

        try:
            with open(self.filename, 'r') as f:
                raw = json.load(f)
                return SessionCredentials.from_dict(self.client, raw)
        except Exception:
            return None

    def save(self, credentials: SessionCredentials) -> None:
        """
        Save credentials to cache file.
        """
        os.makedirs(os.path.dirname(self.filename), exist_ok=True)
        with open(self.filename, 'w') as f:
            json.dump(credentials.as_dict(), f)
        os.chmod(self.filename, 0o600)
