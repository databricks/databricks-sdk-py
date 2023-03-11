import base64
import configparser
import dataclasses
import functools
import logging
import os
import pathlib
import platform
import subprocess
import threading
import urllib.parse
from abc import ABC, abstractmethod
from os import getenv
import subprocess
import json
from datetime import datetime
from typing import Type, Dict, List, Iterator, Optional, Callable

import requests
import requests.auth
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from .azure import ARM_DATABRICKS_RESOURCE_ID, ENVIRONMENTS, AzureEnvironment
from .oauth import ClientCredentials, Refreshable, Token, TokenSource

logger = logging.getLogger(__name__)


class DatabricksError(Exception):

    def __init__(self, message: str = None, *,
                 error_code: str = None,
                 detail: str = None,
                 status: str = None,
                 scimType: str = None,
                 error: str = None,
                 cfg: 'Config' = None,
                 **kwargs):
        if not message and error:
            # API 1.2 has different response format, let's adapt
            message = error
        if not message and detail:
            # Handle SCIM error message details
            # @see https://tools.ietf.org/html/rfc7644#section-3.7.3
            if detail == "null":
                message = "SCIM API Internal Error"
            else:
                message = detail
            # add more context from SCIM responses
            message = f"{scimType} {message}".strip(" ")
            error_code = f"SCIM_{status}"
        if cfg:
            debug_string = cfg.debug_string()
            if debug_string:
                message = f'{message}. {debug_string}'
        super().__init__(message if message else error)
        self.error_code = error_code
        self.kwargs = kwargs


from collections.abc import Callable

RequestVisitor = Callable[[], dict[str,str]]
CredentialsProvider = Callable[['Config'], Optional[RequestVisitor]]


def auth(name: str, require: list[str]):
    def inner(func: CredentialsProvider):
        @functools.wraps(func)
        def wrapper(cfg: 'Config') -> Optional[RequestVisitor]:
            for attr in require:
                if not getattr(cfg, attr):
                    return None
            return func(cfg)
        # TODO: make a proper Abstract Base Class, so that custom auth can be supplied here
        wrapper.auth_type = name
        return wrapper
    return inner


@auth('basic', ['username', 'password'])
def basic_auth(cfg: 'Config') -> Optional[RequestVisitor]:
    encoded = base64.b64encode(f'{cfg.username}:{cfg.password}'.encode())
    static_credentials = {'Authorization': f'Basic {encoded}'}

    def inner() -> dict[str,str]:
        return static_credentials
    return inner


@auth('pat', ['token'])
def pat_auth(cfg: 'Config') -> Optional[RequestVisitor]:
    static_credentials = {'Authorization': f'Bearer {cfg.token}'}

    def inner() -> dict[str,str]:
        return static_credentials
    return inner


@auth('oauth-m2m', ['is_aws', 'host', 'client_id', 'client_secret'])
def oauth_service_principal(cfg: 'Config') -> Optional[RequestVisitor]:
    resp = requests.get(f"{cfg.host}/oidc/.well-known/oauth-authorization-server")
    if not resp.ok:
        return None
    token_source = ClientCredentials(client_id=cfg.client_id,
                                      client_secret=cfg.client_secret,
                                      token_url=resp.json()["token_endpoint"],
                                      scopes=["all-apis"],
                                      use_header=True)

    def inner() -> dict[str,str]:
        token = token_source.token()
        return {'Authorization': f'{token.token_type} {token.access_token}'}
    return inner


def _ensure_host_present(cfg: 'Config', token_source_for: Callable[[str],TokenSource]):
    if cfg.host:
        return
    arm = cfg.arm_environment.resource_manager_endpoint
    token = token_source_for(arm).token()
    resp = requests.get(f"{arm}{cfg.azure_workspace_resource_id}?api-version=2018-04-01",
                        headers={"Authorization": f"Bearer {token.access_token}"})
    if not resp.ok:
        raise DatabricksError(f"Cannot resolve Azure Databricks workspace: {resp.content}")
    cfg.host = f"https://{resp.json()['properties']['workspaceUrl']}"


@auth('azure-client-secret', ['is_azure', 'azure_client_id', 'azure_client_secret', 'azure_tenant_id'])
def azure_service_principal(cfg: 'Config') -> Optional[RequestVisitor]:
    def token_source_for(resource: str) -> TokenSource:
        aad_endpoint = cfg.arm_environment.active_directory_endpoint
        return ClientCredentials(client_id=cfg.azure_client_id,
                                 client_secret=cfg.azure_client_secret,
                                 token_url=f"{aad_endpoint}{cfg.azure_tenant_id}/oauth2/token",
                                 endpoint_params={"resource": resource},
                                 use_params=True)

    _ensure_host_present(cfg, token_source_for)
    logger.info("Configured AAD token for Service Principal (%s)", cfg.azure_client_id)
    inner = token_source_for(cfg.effective_azure_login_app_id)
    cloud = token_source_for(cfg.arm_environment.service_management_endpoint)

    def refreshed_headers() -> dict[str,str]:
        headers = {
            'Authorization': f"Bearer {inner.token().access_token}",
            'X-Databricks-Azure-SP-Management-Token': cloud.token().access_token,
        }
        if cfg.azure_workspace_resource_id:
            headers["X-Databricks-Azure-Workspace-Resource-Id"] = cfg.azure_workspace_resource_id
        return headers
    return refreshed_headers


class AzureCliTokenSource(Refreshable):
    def __init__(self, resource: str):
        super().__init__()
        self.resource = resource

    def refresh(self) -> Token:
        cmd = ["az", "account", "get-access-token", "--resource", self.resource, "--output", "json"]
        out = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
        try:
            it = json.loads(out.decode())
        except ValueError as e:
            raise ValueError("Cannot unmarshal CLI result: {}".format(e))
        expires_on = datetime.strptime(it["expiresOn"], "%Y-%m-%d %H:%M:%S.%f")

        return Token(
            access_token=it["accessToken"],
            refresh_token=it.get('refreshToken', None),
            token_type=it["tokenType"],
            expiry=expires_on)


@auth('azure-cli', ['is_azure'])
def azure_cli(cfg: 'Config') -> Optional[RequestVisitor]:
    token_source = AzureCliTokenSource(cfg.effective_azure_login_app_id)
    try:
        token_source.token()
    except Exception as e:
        '''if err != nil {
            if strings.Contains(err.Error(), "No subscription found") {
                // auth is not configured
                return nil, nil
            }
            if strings.Contains(err.Error(), "executable file not found") {
                logger.Debugf(ctx, "Most likely Azure CLI is not installed. "+
                    "See https://docs.microsoft.com/en-us/cli/azure/?view=azure-cli-latest for details")
                return nil, nil
            }
            return nil, err
        }'''
        return None

    _ensure_host_present(cfg, lambda resource: AzureCliTokenSource(resource))
    logger.info("Using Azure CLI authentication with AAD tokens")

    def inner() -> dict[str,str]:
        token = token_source.token()
        return {'Authorization': f'{token.token_type} {token.access_token}'}
    return inner


def default_auth(cfg: 'Config') -> RequestVisitor:
    auth_providers = [pat_auth, basic_auth, oauth_service_principal, azure_service_principal, azure_cli]
    for provider in auth_providers:
        if cfg.auth_type and provider.auth_type != cfg.auth_type:
            # ignore other auth types if one is explicitly enforced
            logger.debug(f"Ignoring {provider.auth_type} auth, because {cfg.auth_type} is preferred")
            continue
        logger.debug(f'Attempting to configure auth: {provider.auth_type}')
        visitor = provider(cfg)
        if not visitor:
            continue
        cfg.auth_type = provider.auth_type
        return provider
    raise DatabricksError("default auth: cannot configure default credentials", cfg=cfg)


default_auth.auth_type = 'default'


class ConfigAttribute:
    # name and transform are discovered from Config.__new__
    name: str = None
    transform: type = str

    def __init__(self, env: str = None, auth: str = None, sensitive: bool = False):
        self.env = env
        self.auth = auth
        self.sensitive = sensitive

    def __get__(self, cfg: 'Config', owner):
        if not cfg:
            return None
        return cfg._inner.get(self.name, None)

    def __set__(self, cfg: 'Config', value: any):
        cfg._inner[self.name] = self.transform(value)

    def __repr__(self) -> str:
        return f"<ConfigAttribute '{self.name}' {self.transform.__name__}>"


class Config:
    credentials: CredentialsProvider = None

    host = ConfigAttribute(env='DATABRICKS_HOST')
    account_id = ConfigAttribute(env='DATABRICKS_ACCOUNT_ID')
    token = ConfigAttribute(env='DATABRICKS_TOKEN', auth='pat', sensitive=True)
    username = ConfigAttribute(env='DATABRICKS_USERNAME', auth='basic')
    password = ConfigAttribute(env='DATABRICKS_PASSWORD', auth='basic', sensitive=True)
    client_id = ConfigAttribute(env='DATABRICKS_CLIENT_ID', auth='oauth')
    client_secret = ConfigAttribute(env='DATABRICKS_CLIENT_SECRET', auth='oauth', sensitive=True)
    profile = ConfigAttribute(env='DATABRICKS_CONFIG_PROFILE')
    config_file = ConfigAttribute(env='DATABRICKS_CONFIG_FILE')
    google_service_account = ConfigAttribute(env='DATABRICKS_GOOGLE_SERVICE_ACCOUNT', auth='google')
    google_credentials = ConfigAttribute(env='GOOGLE_CREDENTIALS', auth='google', sensitive=True)
    azure_workspace_resource_id = ConfigAttribute(env='DATABRICKS_AZURE_RESOURCE_ID', auth='azure')
    azure_use_msi: bool = ConfigAttribute(env='ARM_USE_MSI', auth='azure')
    azure_client_secret = ConfigAttribute(env='ARM_CLIENT_SECRET', auth='azure', sensitive=True)
    azure_client_id = ConfigAttribute(env='ARM_CLIENT_ID', auth='azure')
    azure_tenant_id = ConfigAttribute(env='ARM_TENANT_ID', auth='azure')
    azure_environment = ConfigAttribute(env='ARM_ENVIRONMENT')
    azure_login_app_id = ConfigAttribute(env='DATABRICKS_AZURE_LOGIN_APP_ID', auth='azure')
    bricks_cli_path = ConfigAttribute(env='BRICKS_CLI_PATH')
    auth_type = ConfigAttribute(env='DATABRICKS_AUTH_TYPE')
    skip_verify: bool = ConfigAttribute()
    http_timeout_seconds: int = ConfigAttribute()
    debug_truncate_bytes: int = ConfigAttribute(env='DATABRICKS_DEBUG_TRUNCATE_BYTES')
    debug_headers: bool = ConfigAttribute(env='DATABRICKS_DEBUG_HEADERS')
    rate_limit: int = ConfigAttribute(env='DATABRICKS_RATE_LIMIT')
    retry_timeout_seconds: int = ConfigAttribute()

    _inner = {}
    _lock = threading.Lock()
    _resolved = False

    def __new__(cls: Type['Config']) -> 'Config':
        if not hasattr(cls, '_attributes'):
            # Python 3.7 compatibility: getting type hints require extra hop, as described in
            # "Accessing The Annotations Dict Of An Object In Python 3.9 And Older" section of
            # https://docs.python.org/3/howto/annotations.html
            anno = cls.__dict__['__annotations__']
            attrs = []
            for name, v in cls.__dict__.items():
                if type(v) != ConfigAttribute:
                    continue
                v.name = name
                v.transform = anno.get(name, str)
                attrs.append(v)
            cls._attributes = attrs
        return super().__new__(cls)

    def __init__(self, *, credentials: CredentialsProvider = None, loaders = None, **kwargs):
        #self.credentials = credentials if credentials else DefaultAuth(self) TODO: change
        for attr in self._attributes:
            if attr.name not in kwargs:
                continue
            # make sure that args are of correct type
            self._inner[attr.name] = attr.transform(kwargs[attr.name])
        loaders = loaders if loaders else [self._load_from_env, self._known_file_config_loader]
        for loader in loaders:
            loader(self)

    @staticmethod
    def _load_from_env(cfg: 'Config'):
        found = False
        for attr in cfg._attributes:
            if not attr.env:
                continue
            value = os.getenv(attr.env)
            if not value:
                continue
            cfg._inner[attr.name] = value
            found = True
        if found:
            logger.debug('Loaded from environment')

    @staticmethod
    def _known_file_config_loader(cfg: 'Config'):
        if not cfg.profile and (cfg.is_any_auth_configured or cfg.is_azure):
            # skip loading configuration file if there's any auth configured
            # directly as part of the Config() constructor.
            return
        config_file = cfg.config_file
        if not config_file:
            config_file = "~/.databrickscfg"
        config_path = pathlib.Path(config_file).expanduser()
        if not config_path.exists():
            logger.debug("%s does not exist", config_path)
            return
        ini_file = configparser.ConfigParser()
        ini_file.read(config_path)
        profile = cfg.profile
        has_explicit_profile = cfg.profile is not None
        if not has_explicit_profile:
            profile = "DEFAULT"
        if not ini_file.has_section(profile):
            logger.debug("%s has no %s profile configured", config_path, profile)
            return
        logger.info("loading %s profile from %s", profile, config_path)
        for k, v in ini_file.items(profile):
            cfg.__setattr__(k, v)
        cfg.profile = None
        cfg.config_file = None

    @property
    def is_any_auth_configured(self) -> bool:
        for attr in self._attributes:
            if not attr.auth:
                continue
            value = self._inner.get(attr.name, None)
            if value:
                return True
        return False

    def debug_string(self):
        buf = []
        attrs_used = []
        envs_used = []
        for attr in self._attributes:
            value = getattr(self, attr.name)
            if not value:
                continue
            safe = '***' if attr.sensitive else f'{value}'
            attrs_used.append(f'{attr.name}={safe}')
            if attr.env:
                envs_used.append(attr.env)
        if attrs_used:
            buf.append(f'Config: {", ".join(attrs_used)}')
        if envs_used:
            buf.append(f'Env: {", ".join(envs_used)}')
        return '. '.join(buf)

    @property
    def is_azure(self) -> bool:
        return self.azure_workspace_resource_id or (self.host and ".azuredatabricks.net" in self.host)

    @property
    def is_gcp(self) -> bool:
        return self.host and ".gcp.databricks.com" in self.host

    @property
    def is_aws(self) -> bool:
        return not self.is_azure and not self.is_gcp

    @property
    def is_account_client(self) -> bool:
        return "https://accounts." in self.host

    @property
    def arm_environment(self) -> AzureEnvironment:
        env = self.azure_environment if self.azure_environment else "PUBLIC"
        try:
            return ENVIRONMENTS[env]
        except KeyError:
            raise DatabricksError(f"Cannot find Azure {env} Environment")

    @property
    def effective_azure_login_app_id(self):
        app_id = self.azure_login_app_id
        if app_id:
            return app_id
        return ARM_DATABRICKS_RESOURCE_ID

    @property
    def hostname(self) -> str:
        url = urllib.parse.urlparse(self.host)
        return url.hostname

    def auth(self) -> CredentialsProvider:
        self.load()
        if self.credentials:
            return self.credentials
        self._lock.acquire()
        try:
            if self.credentials:
                return self.credentials
            self.credentials = default_auth(self)
            return self.credentials
        finally:
            self._lock.release()

    def load(self):
        self._synchronized(self._resolve)

    def to_dict(self) -> Dict[str, any]:
        return self._inner

    def _resolve(self):
        if self._resolved:
            return
        if self.host:
            # fix url to remove trailing slash
            o = urllib.parse.urlparse(self.host)
            if not o.hostname:
                # only hostname is specified
                self.host = f"https://{self.host}"
            else:
                self.host = f"{o.scheme}://{o.hostname}"
        self._resolved = True

    def _synchronized(self, cb):
        self._lock.acquire()
        try:
            cb()
        finally:
            self._lock.release()


VERSION = "0.0.1"


class ApiClient(requests.Session):
    _cfg: Config

    def __init__(self, cfg: Config = None, product="unknown", product_version="0.0.0"):
        super().__init__()
        self._cfg = Config() if not cfg else cfg
        retry_strategy = Retry(
            total=6,
            backoff_factor=1,
            status_forcelist=[429],
            method_whitelist=set({"POST"}) | set(Retry.DEFAULT_METHOD_WHITELIST),
            respect_retry_after_header=True,
            raise_on_status=False,  # return original response when retries have been exhausted
        )
        self.auth = self._cfg.auth()
        py_version = platform.python_version()
        os_name = platform.uname().system.lower()
        self._user_agent_base = (f"{product}/{product_version} databricks-sdk-py/{VERSION}"
                                 f" python/{py_version} os/{os_name} auth/{self.auth.name}")

        self.mount("https://", HTTPAdapter(max_retries=retry_strategy))
        # https://github.com/tomasbasham/ratelimit/blob/master/ratelimit/decorators.py

    @property
    def account_id(self) -> str:
        return self._cfg.account_id

    @property
    def is_account_client(self) -> bool:
        return self._cfg.is_account_client

    def do(self, method: str, path, query: dict = None, body: dict = None) -> dict:
        response = self.request(method,
                                f"{self._cfg.host}{path}",
                                params=query,
                                json=body,
                                headers={"User-Agent": self._user_agent_base})
        payload = response.json()
        if not response.ok:
            raise DatabricksError(**payload)
        return payload
