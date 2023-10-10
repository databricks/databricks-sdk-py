import abc
import base64
import configparser
import copy
import functools
import json
import logging
import os
import pathlib
import platform
import re
import subprocess
import sys
import urllib.parse
from datetime import datetime, timedelta
from json import JSONDecodeError
from types import TracebackType
from typing import (Any, BinaryIO, Callable, Dict, Iterable, Iterator, List,
                    Optional, Type, Union)

import requests
import requests.auth
from requests.adapters import HTTPAdapter

from .azure import (ARM_DATABRICKS_RESOURCE_ID, ENVIRONMENTS, AzureEnvironment,
                    add_sp_management_token, add_workspace_id_header)
from .oauth import (ClientCredentials, OAuthClient, OidcEndpoints, Refreshable,
                    Token, TokenCache, TokenSource)
from .retries import retried
from .version import __version__

__all__ = ['Config', 'DatabricksError']

logger = logging.getLogger('databricks.sdk')

HeaderFactory = Callable[[], Dict[str, str]]


class CredentialsProvider(abc.ABC):
    """ CredentialsProvider is the protocol (call-side interface)
     for authenticating requests to Databricks REST APIs"""

    @abc.abstractmethod
    def auth_type(self) -> str:
        ...

    @abc.abstractmethod
    def __call__(self, cfg: 'Config') -> HeaderFactory:
        ...


def credentials_provider(name: str, require: List[str]):
    """ Given the function that receives a Config and returns RequestVisitor,
    create CredentialsProvider with a given name and required configuration
    attribute names to be present for this function to be called. """

    def inner(func: Callable[['Config'], HeaderFactory]) -> CredentialsProvider:

        @functools.wraps(func)
        def wrapper(cfg: 'Config') -> Optional[HeaderFactory]:
            for attr in require:
                if not getattr(cfg, attr):
                    return None
            return func(cfg)

        wrapper.auth_type = lambda: name
        return wrapper

    return inner


@credentials_provider('basic', ['host', 'username', 'password'])
def basic_auth(cfg: 'Config') -> HeaderFactory:
    """ Given username and password, add base64-encoded Basic credentials """
    encoded = base64.b64encode(f'{cfg.username}:{cfg.password}'.encode()).decode()
    static_credentials = {'Authorization': f'Basic {encoded}'}

    def inner() -> Dict[str, str]:
        return static_credentials

    return inner


@credentials_provider('pat', ['host', 'token'])
def pat_auth(cfg: 'Config') -> HeaderFactory:
    """ Adds Databricks Personal Access Token to every request """
    static_credentials = {'Authorization': f'Bearer {cfg.token}'}

    def inner() -> Dict[str, str]:
        return static_credentials

    return inner


@credentials_provider('runtime', [])
def runtime_native_auth(cfg: 'Config') -> Optional[HeaderFactory]:
    if 'DATABRICKS_RUNTIME_VERSION' not in os.environ:
        return None

    # This import MUST be after the "DATABRICKS_RUNTIME_VERSION" check
    # above, so that we are not throwing import errors when not in
    # runtime and no config variables are set.
    from databricks.sdk.runtime import (init_runtime_legacy_auth,
                                        init_runtime_native_auth,
                                        init_runtime_repl_auth)
    for init in [init_runtime_native_auth, init_runtime_repl_auth, init_runtime_legacy_auth]:
        if init is None:
            continue
        host, inner = init()
        if host is None:
            logger.debug(f'[{init.__name__}] no host detected')
            continue
        cfg.host = host
        logger.debug(f'[{init.__name__}] runtime native auth configured')
        return inner
    return None


@credentials_provider('oauth-m2m', ['is_aws', 'host', 'client_id', 'client_secret'])
def oauth_service_principal(cfg: 'Config') -> Optional[HeaderFactory]:
    """ Adds refreshed Databricks machine-to-machine OAuth Bearer token to every request,
    if /oidc/.well-known/oauth-authorization-server is available on the given host. """
    # TODO: Azure returns 404 for UC workspace after redirecting to
    # https://login.microsoftonline.com/{cfg.azure_tenant_id}/.well-known/oauth-authorization-server
    oidc = cfg.oidc_endpoints
    if oidc is None:
        return None
    token_source = ClientCredentials(client_id=cfg.client_id,
                                     client_secret=cfg.client_secret,
                                     token_url=oidc.token_endpoint,
                                     scopes=["all-apis"],
                                     use_header=True)

    def inner() -> Dict[str, str]:
        token = token_source.token()
        return {'Authorization': f'{token.token_type} {token.access_token}'}

    return inner


@credentials_provider('external-browser', ['host', 'auth_type'])
def external_browser(cfg: 'Config') -> Optional[HeaderFactory]:
    if cfg.auth_type != 'external-browser':
        return None
    if cfg.client_id:
        client_id = cfg.client_id
    elif cfg.is_aws:
        client_id = 'databricks-cli'
    elif cfg.is_azure:
        # Use Azure AD app for cases when Azure CLI is not available on the machine.
        # App has to be registered as Single-page multi-tenant to support PKCE
        # TODO: temporary app ID, change it later.
        client_id = '6128a518-99a9-425b-8333-4cc94f04cacd'
    else:
        raise ValueError(f'local browser SSO is not supported')
    oauth_client = OAuthClient(host=cfg.host,
                               client_id=client_id,
                               redirect_url='http://localhost:8020',
                               client_secret=cfg.client_secret)

    # Load cached credentials from disk if they exist.
    # Note that these are local to the Python SDK and not reused by other SDKs.
    token_cache = TokenCache(oauth_client)
    credentials = token_cache.load()
    if credentials:
        # Force a refresh in case the loaded credentials are expired.
        credentials.token()
    else:
        consent = oauth_client.initiate_consent()
        if not consent:
            return None
        credentials = consent.launch_external_browser()
    token_cache.save(credentials)
    return credentials(cfg)


def _ensure_host_present(cfg: 'Config', token_source_for: Callable[[str], TokenSource]):
    """ Resolves Azure Databricks workspace URL from ARM Resource ID """
    if cfg.host:
        return
    if not cfg.azure_workspace_resource_id:
        return
    arm = cfg.arm_environment.resource_manager_endpoint
    token = token_source_for(arm).token()
    resp = requests.get(f"{arm}{cfg.azure_workspace_resource_id}?api-version=2018-04-01",
                        headers={"Authorization": f"Bearer {token.access_token}"})
    if not resp.ok:
        raise ValueError(f"Cannot resolve Azure Databricks workspace: {resp.content}")
    cfg.host = f"https://{resp.json()['properties']['workspaceUrl']}"


@credentials_provider('azure-client-secret',
                      ['is_azure', 'azure_client_id', 'azure_client_secret', 'azure_tenant_id'])
def azure_service_principal(cfg: 'Config') -> HeaderFactory:
    """ Adds refreshed Azure Active Directory (AAD) Service Principal OAuth tokens
    to every request, while automatically resolving different Azure environment endpoints. """

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

    def refreshed_headers() -> Dict[str, str]:
        headers = {'Authorization': f"Bearer {inner.token().access_token}", }
        add_workspace_id_header(cfg, headers)
        add_sp_management_token(cloud, headers)
        return headers

    return refreshed_headers


class CliTokenSource(Refreshable):

    def __init__(self, cmd: List[str], token_type_field: str, access_token_field: str, expiry_field: str):
        super().__init__()
        self._cmd = cmd
        self._token_type_field = token_type_field
        self._access_token_field = access_token_field
        self._expiry_field = expiry_field

    @staticmethod
    def _parse_expiry(expiry: str) -> datetime:
        for fmt in ("%Y-%m-%d %H:%M:%S.%f", "%Y-%m-%d %H:%M:%S", "%Y-%m-%dT%H:%M:%S.%f%z"):
            try:
                return datetime.strptime(expiry, fmt)
            except ValueError as e:
                last_e = e
        if last_e:
            raise last_e

    def refresh(self) -> Token:
        try:
            is_windows = sys.platform.startswith('win')
            # windows requires shell=True to be able to execute 'az login' or other commands
            # cannot use shell=True all the time, as it breaks macOS
            out = subprocess.check_output(self._cmd, stderr=subprocess.STDOUT, shell=is_windows)
            it = json.loads(out.decode())
            expires_on = self._parse_expiry(it[self._expiry_field])
            return Token(access_token=it[self._access_token_field],
                         token_type=it[self._token_type_field],
                         expiry=expires_on)
        except ValueError as e:
            raise ValueError(f"cannot unmarshal CLI result: {e}")
        except subprocess.CalledProcessError as e:
            message = e.output.decode().strip()
            raise IOError(f'cannot get access token: {message}') from e


class AzureCliTokenSource(CliTokenSource):
    """ Obtain the token granted by `az login` CLI command """

    def __init__(self, resource: str, subscription: str = ""):
        cmd = ["az", "account", "get-access-token", "--resource", resource, "--output", "json"]
        if subscription != "":
            cmd.append("--subscription")
            cmd.append(subscription)
        super().__init__(cmd=cmd,
                         token_type_field='tokenType',
                         access_token_field='accessToken',
                         expiry_field='expiresOn')

    @staticmethod
    def for_resource(cfg: 'Config', resource: str) -> 'AzureCliTokenSource':
        subscription = AzureCliTokenSource._get_subscription(cfg)
        if subscription != "":
            token = AzureCliTokenSource(resource, subscription)
            try:
                # This will fail if the user has access to the workspace, but not to the subscription
                # itself.
                # In such case, we fall back to not using the subscription.
                token.token()
                return token
            except OSError:
                logger.warning("Failed to get token for subscription. Using resource only token.")
        else:
            logger.warning(
                "azure_workspace_resource_id field not provided. " +
                "It is recommended to specify this field in the Databricks configuration to avoid authentication errors."
            )
        token = AzureCliTokenSource(resource)
        token.token()
        return token

    @staticmethod
    def _get_subscription(cfg: 'Config') -> str:
        resource = cfg.azure_workspace_resource_id
        if resource == None or resource == "":
            return ""
        components = resource.split('/')
        if len(components) < 3:
            logger.warning("Invalid azure workspace resource ID")
            return ""
        return components[2]


@credentials_provider('azure-cli', ['is_azure'])
def azure_cli(cfg: 'Config') -> Optional[HeaderFactory]:
    """ Adds refreshed OAuth token granted by `az login` command to every request. """
    token_source = None
    mgmt_token_source = None
    try:
        token_source = AzureCliTokenSource.for_resource(cfg, cfg.effective_azure_login_app_id)
    except FileNotFoundError:
        doc = 'https://docs.microsoft.com/en-us/cli/azure/?view=azure-cli-latest'
        logger.debug(f'Most likely Azure CLI is not installed. See {doc} for details')
        return None
    try:
        mgmt_token_source = AzureCliTokenSource.for_resource(cfg,
                                                             cfg.arm_environment.service_management_endpoint)
    except Exception as e:
        logger.debug(f'Not including service management token in headers', exc_info=e)
        mgmt_token_source = None

    _ensure_host_present(cfg, lambda resource: AzureCliTokenSource.for_resource(cfg, resource))
    logger.info("Using Azure CLI authentication with AAD tokens")

    def inner() -> Dict[str, str]:
        token = token_source.token()
        headers = {'Authorization': f'{token.token_type} {token.access_token}'}
        add_workspace_id_header(cfg, headers)
        if mgmt_token_source:
            add_sp_management_token(mgmt_token_source, headers)
        return headers

    return inner


class DatabricksCliTokenSource(CliTokenSource):
    """ Obtain the token granted by `databricks auth login` CLI command """

    def __init__(self, cfg: 'Config'):
        args = ['auth', 'token', '--host', cfg.host]
        if cfg.is_account_client:
            args += ['--account-id', cfg.account_id]

        cli_path = cfg.databricks_cli_path
        if not cli_path:
            cli_path = 'databricks'

        # If the path is unqualified, look it up in PATH.
        if cli_path.count("/") == 0:
            cli_path = self.__class__._find_executable(cli_path)

        super().__init__(cmd=[cli_path, *args],
                         token_type_field='token_type',
                         access_token_field='access_token',
                         expiry_field='expiry')

    @staticmethod
    def _find_executable(name) -> str:
        err = FileNotFoundError("Most likely the Databricks CLI is not installed")
        for dir in os.getenv("PATH", default="").split(os.path.pathsep):
            path = pathlib.Path(dir).joinpath(name).resolve()
            if not path.is_file():
                continue

            # The new Databricks CLI is a single binary with size > 1MB.
            # We use the size as a signal to determine which Databricks CLI is installed.
            stat = path.stat()
            if stat.st_size < (1024 * 1024):
                err = FileNotFoundError("Databricks CLI version <0.100.0 detected")
                continue

            return str(path)

        raise err


@credentials_provider('databricks-cli', ['host', 'is_aws'])
def databricks_cli(cfg: 'Config') -> Optional[HeaderFactory]:
    try:
        token_source = DatabricksCliTokenSource(cfg)
    except FileNotFoundError as e:
        logger.debug(e)
        return None

    try:
        token_source.token()
    except IOError as e:
        if 'databricks OAuth is not' in str(e):
            logger.debug(f'OAuth not configured or not available: {e}')
            return None
        raise e

    logger.info("Using Databricks CLI authentication")

    def inner() -> Dict[str, str]:
        token = token_source.token()
        return {'Authorization': f'{token.token_type} {token.access_token}'}

    return inner


class MetadataServiceTokenSource(Refreshable):
    """ Obtain the token granted by Databricks Metadata Service """
    METADATA_SERVICE_VERSION = "1"
    METADATA_SERVICE_VERSION_HEADER = "X-Databricks-Metadata-Version"
    METADATA_SERVICE_HOST_HEADER = "X-Databricks-Host"
    _metadata_service_timeout = 10 # seconds

    def __init__(self, cfg: 'Config'):
        super().__init__()
        self.url = cfg.metadata_service_url
        self.host = cfg.host

    def refresh(self) -> Token:
        resp = requests.get(self.url,
                            timeout=self._metadata_service_timeout,
                            headers={
                                self.METADATA_SERVICE_VERSION_HEADER: self.METADATA_SERVICE_VERSION,
                                self.METADATA_SERVICE_HOST_HEADER: self.host
                            })
        json_resp: dict[str, Union[str, float]] = resp.json()
        access_token = json_resp.get("access_token", None)
        if access_token is None:
            raise ValueError("Metadata Service returned empty token")
        token_type = json_resp.get("token_type", None)
        if token_type is None:
            raise ValueError("Metadata Service returned empty token type")
        if json_resp["expires_on"] in ["", None]:
            raise ValueError("Metadata Service returned invalid expiry")
        try:
            expiry = datetime.fromtimestamp(json_resp["expires_on"])
        except:
            raise ValueError("Metadata Service returned invalid expiry")

        return Token(access_token=access_token, token_type=token_type, expiry=expiry)


@credentials_provider('metadata-service', ['host', 'metadata_service_url'])
def metadata_service(cfg: 'Config') -> Optional[HeaderFactory]:
    """ Adds refreshed token granted by Databricks Metadata Service to every request. """

    token_source = MetadataServiceTokenSource(cfg)
    token_source.token()
    logger.info("Using Databricks Metadata Service authentication")

    def inner() -> Dict[str, str]:
        token = token_source.token()
        return {'Authorization': f'{token.token_type} {token.access_token}'}

    return inner


class DefaultCredentials:
    """ Select the first applicable credential provider from the chain """

    def __init__(self) -> None:
        self._auth_type = 'default'

    def auth_type(self) -> str:
        return self._auth_type

    def __call__(self, cfg: 'Config') -> HeaderFactory:
        auth_providers = [
            pat_auth, basic_auth, metadata_service, oauth_service_principal, azure_service_principal,
            azure_cli, external_browser, databricks_cli, runtime_native_auth
        ]
        for provider in auth_providers:
            auth_type = provider.auth_type()
            if cfg.auth_type and auth_type != cfg.auth_type:
                # ignore other auth types if one is explicitly enforced
                logger.debug(f"Ignoring {auth_type} auth, because {cfg.auth_type} is preferred")
                continue
            logger.debug(f'Attempting to configure auth: {auth_type}')
            try:
                header_factory = provider(cfg)
                if not header_factory:
                    continue
                self._auth_type = auth_type
                return header_factory
            except Exception as e:
                raise ValueError(f'{auth_type}: {e}') from e
        raise ValueError('cannot configure default credentials')


class ConfigAttribute:
    """ Configuration attribute metadata and descriptor protocols. """

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
    databricks_cli_path = ConfigAttribute(env='DATABRICKS_CLI_PATH')
    auth_type = ConfigAttribute(env='DATABRICKS_AUTH_TYPE')
    cluster_id = ConfigAttribute(env='DATABRICKS_CLUSTER_ID')
    warehouse_id = ConfigAttribute(env='DATABRICKS_WAREHOUSE_ID')
    skip_verify: bool = ConfigAttribute()
    http_timeout_seconds: int = ConfigAttribute()
    debug_truncate_bytes: int = ConfigAttribute(env='DATABRICKS_DEBUG_TRUNCATE_BYTES')
    debug_headers: bool = ConfigAttribute(env='DATABRICKS_DEBUG_HEADERS')
    rate_limit: int = ConfigAttribute(env='DATABRICKS_RATE_LIMIT')
    retry_timeout_seconds: int = ConfigAttribute()
    metadata_service_url = ConfigAttribute(env='DATABRICKS_METADATA_SERVICE_URL',
                                           auth='metadata-service',
                                           sensitive=True)
    max_connection_pools: int = ConfigAttribute()
    max_connections_per_pool: int = ConfigAttribute()

    def __init__(self,
                 *,
                 credentials_provider: CredentialsProvider = None,
                 product="unknown",
                 product_version="0.0.0",
                 **kwargs):
        self._inner = {}
        self._user_agent_other_info = []
        self._credentials_provider = credentials_provider if credentials_provider else DefaultCredentials()
        try:
            self._set_inner_config(kwargs)
            self._load_from_env()
            self._known_file_config_loader()
            self._fix_host_if_needed()
            self._validate()
            self._init_auth()
            self._product = product
            self._product_version = product_version
        except ValueError as e:
            message = self.wrap_debug_info(str(e))
            raise ValueError(message) from e

    def wrap_debug_info(self, message: str) -> str:
        debug_string = self.debug_string()
        if debug_string:
            message = f'{message.rstrip(".")}. {debug_string}'
        return message

    @staticmethod
    def parse_dsn(dsn: str) -> 'Config':
        uri = urllib.parse.urlparse(dsn)
        if uri.scheme != 'databricks':
            raise ValueError(f'Expected databricks:// scheme, got {uri.scheme}://')
        kwargs = {'host': f'https://{uri.hostname}'}
        if uri.username:
            kwargs['username'] = uri.username
        if uri.password:
            kwargs['password'] = uri.password
        query = dict(urllib.parse.parse_qsl(uri.query))
        for attr in Config.attributes():
            if attr.name not in query:
                continue
            kwargs[attr.name] = query[attr.name]
        return Config(**kwargs)

    def authenticate(self) -> Dict[str, str]:
        """ Returns a list of fresh authentication headers """
        return self._header_factory()

    def as_dict(self) -> dict:
        return self._inner

    @property
    def is_azure(self) -> bool:
        has_resource_id = self.azure_workspace_resource_id is not None
        has_host = self.host is not None
        is_public_cloud = has_host and ".azuredatabricks.net" in self.host
        is_china_cloud = has_host and ".databricks.azure.cn" in self.host
        is_gov_cloud = has_host and ".databricks.azure.us" in self.host
        is_valid_cloud = is_public_cloud or is_china_cloud or is_gov_cloud
        return has_resource_id or (has_host and is_valid_cloud)

    @property
    def is_gcp(self) -> bool:
        return self.host and ".gcp.databricks.com" in self.host

    @property
    def is_aws(self) -> bool:
        return not self.is_azure and not self.is_gcp

    @property
    def is_account_client(self) -> bool:
        if not self.host:
            return False
        return self.host.startswith("https://accounts.") or self.host.startswith("https://accounts-dod.")

    @property
    def arm_environment(self) -> AzureEnvironment:
        env = self.azure_environment if self.azure_environment else "PUBLIC"
        try:
            return ENVIRONMENTS[env]
        except KeyError:
            raise ValueError(f"Cannot find Azure {env} Environment")

    @property
    def effective_azure_login_app_id(self):
        app_id = self.azure_login_app_id
        if app_id:
            return app_id
        return ARM_DATABRICKS_RESOURCE_ID

    @property
    def hostname(self) -> str:
        url = urllib.parse.urlparse(self.host)
        return url.netloc

    @property
    def is_any_auth_configured(self) -> bool:
        for attr in Config.attributes():
            if not attr.auth:
                continue
            value = self._inner.get(attr.name, None)
            if value:
                return True
        return False

    @property
    def user_agent(self):
        """ Returns User-Agent header used by this SDK """
        py_version = platform.python_version()
        os_name = platform.uname().system.lower()

        ua = [
            f"{self._product}/{self._product_version}", f"databricks-sdk-py/{__version__}",
            f"python/{py_version}", f"os/{os_name}", f"auth/{self.auth_type}",
        ]
        if len(self._user_agent_other_info) > 0:
            ua.append(' '.join(self._user_agent_other_info))
        if len(self._upstream_user_agent) > 0:
            ua.append(self._upstream_user_agent)
        if 'DATABRICKS_RUNTIME_VERSION' in os.environ:
            runtime_version = os.environ['DATABRICKS_RUNTIME_VERSION']
            if runtime_version != '':
                runtime_version = self._sanitize_header_value(runtime_version)
                ua.append(f'runtime/{runtime_version}')

        return ' '.join(ua)

    @staticmethod
    def _sanitize_header_value(value: str) -> str:
        value = value.replace(' ', '-')
        value = value.replace('/', '-')
        return value

    @property
    def _upstream_user_agent(self) -> str:
        product = os.environ.get('DATABRICKS_SDK_UPSTREAM', None)
        product_version = os.environ.get('DATABRICKS_SDK_UPSTREAM_VERSION', None)
        if product is not None and product_version is not None:
            return f"upstream/{product} upstream-version/{product_version}"
        return ""

    def with_user_agent_extra(self, key: str, value: str) -> 'Config':
        self._user_agent_other_info.append(f"{key}/{value}")
        return self

    @property
    def oidc_endpoints(self) -> Optional[OidcEndpoints]:
        self._fix_host_if_needed()
        if not self.host:
            return None
        if self.is_azure:
            # Retrieve authorize endpoint to retrieve token endpoint after
            res = requests.get(f'{self.host}/oidc/oauth2/v2.0/authorize', allow_redirects=False)
            real_auth_url = res.headers.get('location')
            if not real_auth_url:
                return None
            return OidcEndpoints(authorization_endpoint=real_auth_url,
                                 token_endpoint=real_auth_url.replace('/authorize', '/token'))
        if self.is_account_client and self.account_id:
            prefix = f'{self.host}/oidc/accounts/{self.account_id}'
            return OidcEndpoints(authorization_endpoint=f'{prefix}/v1/authorize',
                                 token_endpoint=f'{prefix}/v1/token')
        oidc = f'{self.host}/oidc/.well-known/oauth-authorization-server'
        res = requests.get(oidc)
        if res.status_code != 200:
            return None
        auth_metadata = res.json()
        return OidcEndpoints(authorization_endpoint=auth_metadata.get('authorization_endpoint'),
                             token_endpoint=auth_metadata.get('token_endpoint'))

    def debug_string(self) -> str:
        """ Returns log-friendly representation of configured attributes """
        buf = []
        attrs_used = []
        envs_used = []
        for attr in Config.attributes():
            if attr.env and os.environ.get(attr.env):
                envs_used.append(attr.env)
            value = getattr(self, attr.name)
            if not value:
                continue
            safe = '***' if attr.sensitive else f'{value}'
            attrs_used.append(f'{attr.name}={safe}')
        if attrs_used:
            buf.append(f'Config: {", ".join(attrs_used)}')
        if envs_used:
            buf.append(f'Env: {", ".join(envs_used)}')
        return '. '.join(buf)

    def to_dict(self) -> Dict[str, any]:
        return self._inner

    @property
    def sql_http_path(self) -> Optional[str]:
        """(Experimental) Return HTTP path for SQL Drivers.

        If `cluster_id` or `warehouse_id` are configured, return a valid HTTP Path argument
        used in construction of JDBC/ODBC DSN string.

        See https://docs.databricks.com/integrations/jdbc-odbc-bi.html
        """
        if (not self.cluster_id) and (not self.warehouse_id):
            return None
        if self.cluster_id and self.warehouse_id:
            raise ValueError('cannot have both cluster_id and warehouse_id')
        headers = self.authenticate()
        headers['User-Agent'] = f'{self.user_agent} sdk-feature/sql-http-path'
        if self.cluster_id:
            response = requests.get(f"{self.host}/api/2.0/preview/scim/v2/Me", headers=headers)
            # get workspace ID from the response header
            workspace_id = response.headers.get('x-databricks-org-id')
            return f'sql/protocolv1/o/{workspace_id}/{self.cluster_id}'
        if self.warehouse_id:
            return f'/sql/1.0/warehouses/{self.warehouse_id}'

    @classmethod
    def attributes(cls) -> Iterable[ConfigAttribute]:
        """ Returns a list of Databricks SDK configuration metadata """
        if hasattr(cls, '_attributes'):
            return cls._attributes
        if sys.version_info[1] >= 10:
            import inspect
            anno = inspect.get_annotations(cls)
        else:
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
        return cls._attributes

    def _fix_host_if_needed(self):
        if not self.host:
            return
        # fix url to remove trailing slash
        o = urllib.parse.urlparse(self.host)
        if not o.hostname:
            # only hostname is specified
            self.host = f"https://{self.host}"
        else:
            self.host = f"{o.scheme}://{o.netloc}"

    def _set_inner_config(self, keyword_args: Dict[str, any]):
        for attr in self.attributes():
            if attr.name not in keyword_args:
                continue
            if keyword_args.get(attr.name, None) is None:
                continue
            self.__setattr__(attr.name, keyword_args[attr.name])

    def _load_from_env(self):
        found = False
        for attr in self.attributes():
            if not attr.env:
                continue
            if attr.name in self._inner:
                continue
            value = os.environ.get(attr.env)
            if not value:
                continue
            self.__setattr__(attr.name, value)
            found = True
        if found:
            logger.debug('Loaded from environment')

    def _known_file_config_loader(self):
        if not self.profile and (self.is_any_auth_configured or self.host
                                 or self.azure_workspace_resource_id):
            # skip loading configuration file if there's any auth configured
            # directly as part of the Config() constructor.
            return
        config_file = self.config_file
        if not config_file:
            config_file = "~/.databrickscfg"
        config_path = pathlib.Path(config_file).expanduser()
        if not config_path.exists():
            logger.debug("%s does not exist", config_path)
            return
        ini_file = configparser.ConfigParser()
        ini_file.read(config_path)
        profile = self.profile
        has_explicit_profile = self.profile is not None
        # In Go SDK, we skip merging the profile with DEFAULT section, though Python's ConfigParser.items()
        # is returning profile key-value pairs _including those from DEFAULT_. This is not what we expect
        # from Unified Auth test suite at the moment. Hence, the private variable access.
        # See: https://docs.python.org/3/library/configparser.html#mapping-protocol-access
        if not has_explicit_profile and not ini_file.defaults():
            logger.debug(f'{config_path} has no DEFAULT profile configured')
            return
        if not has_explicit_profile:
            profile = "DEFAULT"
        profiles = ini_file._sections
        if ini_file.defaults():
            profiles['DEFAULT'] = ini_file.defaults()
        if profile not in profiles:
            raise ValueError(f'resolve: {config_path} has no {profile} profile configured')
        raw_config = profiles[profile]
        logger.info(f'loading {profile} profile from {config_file}: {", ".join(raw_config.keys())}')
        for k, v in raw_config.items():
            if k in self._inner:
                # don't overwrite a value previously set
                continue
            self.__setattr__(k, v)

    def _validate(self):
        auths_used = set()
        for attr in Config.attributes():
            if attr.name not in self._inner:
                continue
            if not attr.auth:
                continue
            auths_used.add(attr.auth)
        if len(auths_used) <= 1:
            return
        if self.auth_type:
            # client has auth preference set
            return
        names = " and ".join(sorted(auths_used))
        raise ValueError(f'validate: more than one authorization method configured: {names}')

    def _init_auth(self):
        try:
            self._header_factory = self._credentials_provider(self)
            self.auth_type = self._credentials_provider.auth_type()
            if not self._header_factory:
                raise ValueError('not configured')
        except ValueError as e:
            raise ValueError(f'{self._credentials_provider.auth_type()} auth: {e}') from e

    def __repr__(self):
        return f'<{self.debug_string()}>'

    def copy(self):
        """Creates a copy of the config object.
        All the copies share most of their internal state (ie, shared reference to fields such as credential_provider).
        Copies have their own instances of the following fields
            - `_user_agent_other_info`
        """
        cpy: Config = copy.copy(self)
        cpy._user_agent_other_info = copy.deepcopy(self._user_agent_other_info)
        return cpy


class ErrorDetail:

    def __init__(self,
                 type: str = None,
                 reason: str = None,
                 domain: str = None,
                 metadata: dict = None,
                 **kwargs):
        self.type = type
        self.reason = reason
        self.domain = domain
        self.metadata = metadata

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ErrorDetail':
        if '@type' in d:
            d['type'] = d['@type']
        return cls(**d)


class DatabricksError(IOError):
    """ Generic error from Databricks REST API """
    # Known ErrorDetail types
    _error_info_type = "type.googleapis.com/google.rpc.ErrorInfo"

    def __init__(self,
                 message: str = None,
                 *,
                 error_code: str = None,
                 detail: str = None,
                 status: str = None,
                 scimType: str = None,
                 error: str = None,
                 retry_after_secs: int = None,
                 details: List[Dict[str, any]] = None,
                 **kwargs):
        if error:
            # API 1.2 has different response format, let's adapt
            message = error
        if detail:
            # Handle SCIM error message details
            # @see https://tools.ietf.org/html/rfc7644#section-3.7.3
            if detail == "null":
                message = "SCIM API Internal Error"
            else:
                message = detail
            # add more context from SCIM responses
            message = f"{scimType} {message}".strip(" ")
            error_code = f"SCIM_{status}"
        super().__init__(message if message else error)
        self.error_code = error_code
        self.retry_after_secs = retry_after_secs
        self.details = [ErrorDetail.from_dict(detail) for detail in details] if details else []
        self.kwargs = kwargs

    def get_error_info(self) -> List[ErrorDetail]:
        return self._get_details_by_type(DatabricksError._error_info_type)

    def _get_details_by_type(self, error_type) -> List[ErrorDetail]:
        if self.details == None:
            return []
        return [detail for detail in self.details if detail.type == error_type]


class ApiClient:
    _cfg: Config

    def __init__(self, cfg: Config = None):

        if cfg is None:
            cfg = Config()

        self._cfg = cfg
        # See https://github.com/databricks/databricks-sdk-go/blob/main/client/client.go#L34-L35
        self._debug_truncate_bytes = cfg.debug_truncate_bytes if cfg.debug_truncate_bytes else 96
        self._retry_timeout_seconds = cfg.retry_timeout_seconds if cfg.retry_timeout_seconds else 300
        self._user_agent_base = cfg.user_agent
        self._session = requests.Session()
        self._session.auth = self._authenticate

        # Number of urllib3 connection pools to cache before discarding the least
        # recently used pool. Python requests default value is 10.
        pool_connections = cfg.max_connection_pools
        if pool_connections is None:
            pool_connections = 20

        # The maximum number of connections to save in the pool. Improves performance
        # in multithreaded situations. For now, we're setting it to the same value
        # as connection_pool_size.
        pool_maxsize = cfg.max_connections_per_pool
        if cfg.max_connections_per_pool is None:
            pool_maxsize = pool_connections

        # If pool_block is False, then more connections will are created,
        # but not saved after the first use. Blocks when no free connections are available.
        # urllib3 ensures that no more than pool_maxsize connections are used at a time.
        # Prevents platform from flooding. By default, requests library doesn't block.
        pool_block = True

        # We don't use `max_retries` from HTTPAdapter to align with a more production-ready
        # retry strategy established in the Databricks SDK for Go. See _is_retryable and
        # @retried for more details.
        http_adapter = HTTPAdapter(pool_connections=pool_connections,
                                   pool_maxsize=pool_maxsize,
                                   pool_block=pool_block)
        self._session.mount("https://", http_adapter)

    @property
    def account_id(self) -> str:
        return self._cfg.account_id

    @property
    def is_account_client(self) -> bool:
        return self._cfg.is_account_client

    def _authenticate(self, r: requests.PreparedRequest) -> requests.PreparedRequest:
        headers = self._cfg.authenticate()
        for k, v in headers.items():
            r.headers[k] = v
        return r

    @staticmethod
    def _fix_query_string(query: Optional[dict] = None) -> Optional[dict]:
        # Convert True -> "true" for Databricks APIs to understand booleans.
        # See: https://github.com/databricks/databricks-sdk-py/issues/142
        if query is None:
            return None
        with_fixed_bools = {k: v if type(v) != bool else ('true' if v else 'false') for k, v in query.items()}

        # Query parameters may be nested, e.g.
        # {'filter_by': {'user_ids': [123, 456]}}
        # The HTTP-compatible representation of this is
        # filter_by.user_ids=123&filter_by.user_ids=456
        # To achieve this, we convert the above dictionary to
        # {'filter_by.user_ids': [123, 456]}
        # See the following for more information:
        # https://cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#google.api.HttpRule
        def flatten_dict(d: Dict[str, Any]) -> Dict[str, Any]:
            for k1, v1 in d.items():
                if isinstance(v1, dict):
                    v1 = dict(flatten_dict(v1))
                    for k2, v2 in v1.items():
                        yield f"{k1}.{k2}", v2
                else:
                    yield k1, v1

        flattened = dict(flatten_dict(with_fixed_bools))
        return flattened

    def do(self,
           method: str,
           path: str,
           query: dict = None,
           headers: dict = None,
           body: dict = None,
           raw: bool = False,
           files=None,
           data=None) -> Union[dict, BinaryIO]:
        # Remove extra `/` from path for Files API
        # Once we've fixed the OpenAPI spec, we can remove this
        path = re.sub('^/api/2.0/fs/files//', '/api/2.0/fs/files/', path)
        if headers is None:
            headers = {}
        headers['User-Agent'] = self._user_agent_base
        retryable = retried(timeout=timedelta(seconds=self._retry_timeout_seconds),
                            is_retryable=self._is_retryable)
        return retryable(self._perform)(method,
                                        path,
                                        query=query,
                                        headers=headers,
                                        body=body,
                                        raw=raw,
                                        files=files,
                                        data=data)

    @staticmethod
    def _is_retryable(err: BaseException) -> Optional[str]:
        # this method is Databricks-specific port of urllib3 retries
        # (see https://github.com/urllib3/urllib3/blob/main/src/urllib3/util/retry.py)
        # and Databricks SDK for Go retries
        # (see https://github.com/databricks/databricks-sdk-go/blob/main/apierr/errors.go)
        from urllib3.exceptions import ProxyError
        if isinstance(err, ProxyError):
            err = err.original_error
        if isinstance(err, requests.ConnectionError):
            # corresponds to `connection reset by peer` and `connection refused` errors from Go,
            # which are generally related to the temporary glitches in the networking stack,
            # also caused by endpoint protection software, like ZScaler, to drop connections while
            # not yet authenticated.
            #
            # return a simple string for debug log readability, as `raise TimeoutError(...) from err`
            # will bubble up the original exception in case we reach max retries.
            return f'cannot connect'
        if isinstance(err, requests.Timeout):
            # corresponds to `TLS handshake timeout` and `i/o timeout` in Go.
            #
            # return a simple string for debug log readability, as `raise TimeoutError(...) from err`
            # will bubble up the original exception in case we reach max retries.
            return f'timeout'
        if isinstance(err, DatabricksError):
            message = str(err)
            transient_error_string_matches = [
                "com.databricks.backend.manager.util.UnknownWorkerEnvironmentException",
                "does not have any associated worker environments", "There is no worker environment with id",
                "Unknown worker environment", "ClusterNotReadyException", "Unexpected error",
                "Please try again later or try a faster operation.",
                "RPC token bucket limit has been exceeded",
            ]
            for substring in transient_error_string_matches:
                if substring not in message:
                    continue
                return f'matched {substring}'
        return None

    @staticmethod
    def _parse_retry_after(response: requests.Response) -> Optional[int]:
        retry_after = response.headers.get("Retry-After")
        if retry_after is None:
            return None
        # If the request is throttled, try parse the `Retry-After` header and sleep
        # for the specified number of seconds. Note that this header can contain either
        # an integer or a RFC1123 datetime string.
        # See https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Retry-After
        #
        # For simplicity, we only try to parse it as an integer, as this is what Databricks
        # platform returns. Otherwise, we fall back and don't sleep.
        try:
            return int(retry_after)
        except ValueError:
            logger.debug(f'Invalid Retry-After header received: {retry_after}. Defaulting to 1')
            # defaulting to 1 sleep second to make self._is_retryable() simpler
            return 1

    def _perform(self,
                 method: str,
                 path: str,
                 query: dict = None,
                 headers: dict = None,
                 body: dict = None,
                 raw: bool = False,
                 files=None,
                 data=None):
        response = self._session.request(method,
                                         f"{self._cfg.host}{path}",
                                         params=self._fix_query_string(query),
                                         json=body,
                                         headers=headers,
                                         files=files,
                                         data=data,
                                         stream=raw)
        try:
            self._record_request_log(response, raw=raw or data is not None or files is not None)
            if not response.ok: # internally calls response.raise_for_status()
                # TODO: experiment with traceback pruning for better readability
                # See https://stackoverflow.com/a/58821552/277035
                payload = response.json()
                raise self._make_nicer_error(response=response, **payload) from None
            if raw:
                return StreamingResponse(response)
            if not len(response.content):
                return {}
            return response.json()
        except requests.exceptions.JSONDecodeError:
            message = self._make_sense_from_html(response.text)
            if not message:
                message = response.reason
            raise self._make_nicer_error(response=response, message=message) from None

    @staticmethod
    def _make_sense_from_html(txt: str) -> str:
        matchers = [r'<pre>(.*)</pre>', r'<title>(.*)</title>']
        for attempt in matchers:
            expr = re.compile(attempt, re.MULTILINE)
            match = expr.search(txt)
            if not match:
                continue
            return match.group(1).strip()
        return txt

    def _make_nicer_error(self, *, response: requests.Response, **kwargs) -> DatabricksError:
        status_code = response.status_code
        message = kwargs.get('message', 'request failed')
        is_http_unauthorized_or_forbidden = status_code in (401, 403)
        is_too_many_requests_or_unavailable = status_code in (429, 503)
        if is_http_unauthorized_or_forbidden:
            message = self._cfg.wrap_debug_info(message)
        if is_too_many_requests_or_unavailable:
            kwargs['retry_after_secs'] = self._parse_retry_after(response)
        kwargs['message'] = message
        return DatabricksError(**kwargs)

    def _record_request_log(self, response: requests.Response, raw=False):
        if not logger.isEnabledFor(logging.DEBUG):
            return
        request = response.request
        url = urllib.parse.urlparse(request.url)
        query = ''
        if url.query:
            query = f'?{urllib.parse.unquote(url.query)}'
        sb = [f'{request.method} {urllib.parse.unquote(url.path)}{query}']
        if self._cfg.debug_headers:
            if self._cfg.host:
                sb.append(f'> * Host: {self._cfg.host}')
            for k, v in request.headers.items():
                sb.append(f'> * {k}: {self._only_n_bytes(v, self._debug_truncate_bytes)}')
        if request.body:
            sb.append("> [raw stream]" if raw else self._redacted_dump("> ", request.body))
        sb.append(f'< {response.status_code} {response.reason}')
        if raw and response.headers.get('Content-Type', None) != 'application/json':
            # Raw streams with `Transfer-Encoding: chunked` do not have `Content-Type` header
            sb.append("< [raw stream]")
        elif response.content:
            sb.append(self._redacted_dump("< ", response.content))
        logger.debug("\n".join(sb))

    @staticmethod
    def _mask(m: Dict[str, any]):
        for k in m:
            if k in {'bytes_value', 'string_value', 'token_value', 'value', 'content'}:
                m[k] = "**REDACTED**"

    @staticmethod
    def _map_keys(m: Dict[str, any]) -> List[str]:
        keys = list(m.keys())
        keys.sort()
        return keys

    @staticmethod
    def _only_n_bytes(j: str, num_bytes: int = 96) -> str:
        diff = len(j.encode('utf-8')) - num_bytes
        if diff > 0:
            return f"{j[:num_bytes]}... ({diff} more bytes)"
        return j

    def _recursive_marshal_dict(self, m, budget) -> dict:
        out = {}
        self._mask(m)
        for k in sorted(m.keys()):
            raw = self._recursive_marshal(m[k], budget)
            out[k] = raw
            budget -= len(str(raw))
        return out

    def _recursive_marshal_list(self, s, budget) -> list:
        out = []
        for i in range(len(s)):
            if i > 0 >= budget:
                out.append("... (%d additional elements)" % (len(s) - len(out)))
                break
            raw = self._recursive_marshal(s[i], budget)
            out.append(raw)
            budget -= len(str(raw))
        return out

    def _recursive_marshal(self, v: any, budget: int) -> any:
        if isinstance(v, dict):
            return self._recursive_marshal_dict(v, budget)
        elif isinstance(v, list):
            return self._recursive_marshal_list(v, budget)
        elif isinstance(v, str):
            return self._only_n_bytes(v, self._debug_truncate_bytes)
        else:
            return v

    def _redacted_dump(self, prefix: str, body: str) -> str:
        if len(body) == 0:
            return ""
        try:
            # Unmarshal body into primitive types.
            tmp = json.loads(body)
            max_bytes = 96
            if self._debug_truncate_bytes > max_bytes:
                max_bytes = self._debug_truncate_bytes
            # Re-marshal body taking redaction and character limit into account.
            raw = self._recursive_marshal(tmp, max_bytes)
            return "\n".join([f'{prefix}{line}' for line in json.dumps(raw, indent=2).split("\n")])
        except JSONDecodeError:
            return f'{prefix}[non-JSON document of {len(body)} bytes]'


class StreamingResponse(BinaryIO):
    _response: requests.Response
    _buffer: bytes
    _content: Union[Iterator[bytes], None]
    _chunk_size: Union[int, None]
    _closed: bool = False

    def fileno(self) -> int:
        pass

    def flush(self) -> int:
        pass

    def __init__(self, response: requests.Response, chunk_size: Union[int, None] = None):
        self._response = response
        self._buffer = b''
        self._content = None
        self._chunk_size = chunk_size

    def _open(self) -> None:
        if self._closed:
            raise ValueError("I/O operation on closed file")
        if not self._content:
            self._content = self._response.iter_content(chunk_size=self._chunk_size)

    def __enter__(self) -> BinaryIO:
        self._open()
        return self

    def set_chunk_size(self, chunk_size: Union[int, None]) -> None:
        self._chunk_size = chunk_size

    def close(self) -> None:
        self._response.close()
        self._closed = True

    def isatty(self) -> bool:
        return False

    def read(self, n: int = -1) -> bytes:
        self._open()
        read_everything = n < 0
        remaining_bytes = n
        res = b''
        while remaining_bytes > 0 or read_everything:
            if len(self._buffer) == 0:
                try:
                    self._buffer = next(self._content)
                except StopIteration:
                    break
            bytes_available = len(self._buffer)
            to_read = bytes_available if read_everything else min(remaining_bytes, bytes_available)
            res += self._buffer[:to_read]
            self._buffer = self._buffer[to_read:]
            remaining_bytes -= to_read
        return res

    def readable(self) -> bool:
        return self._content is not None

    def readline(self, __limit: int = ...) -> bytes:
        raise NotImplementedError()

    def readlines(self, __hint: int = ...) -> List[bytes]:
        raise NotImplementedError()

    def seek(self, __offset: int, __whence: int = ...) -> int:
        raise NotImplementedError()

    def seekable(self) -> bool:
        return False

    def tell(self) -> int:
        raise NotImplementedError()

    def truncate(self, __size: Union[int, None] = ...) -> int:
        raise NotImplementedError()

    def writable(self) -> bool:
        return False

    def write(self, s: Union[bytes, bytearray]) -> int:
        raise NotImplementedError()

    def writelines(self, lines: Iterable[bytes]) -> None:
        raise NotImplementedError()

    def __next__(self) -> bytes:
        return self.read(1)

    def __iter__(self) -> Iterator[bytes]:
        return self._content

    def __exit__(self, t: Union[Type[BaseException], None], value: Union[BaseException, None],
                 traceback: Union[TracebackType, None]) -> None:
        self._content = None
        self._buffer = b''
        self.close()
