import configparser
import copy
import logging
import os
import pathlib
import platform
import sys
import urllib.parse
from typing import Dict, Iterable, Optional

import requests

from .azure import AzureEnvironment
from .clock import Clock, RealClock
from .credentials_provider import CredentialsProvider, DefaultCredentials
from .environments import (ALL_ENVS, DEFAULT_ENVIRONMENT, Cloud,
                           DatabricksEnvironment)
from .oauth import OidcEndpoints
from .version import __version__

logger = logging.getLogger('databricks.sdk')


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
    host: str = ConfigAttribute(env='DATABRICKS_HOST')
    account_id: str = ConfigAttribute(env='DATABRICKS_ACCOUNT_ID')
    token: str = ConfigAttribute(env='DATABRICKS_TOKEN', auth='pat', sensitive=True)
    username: str = ConfigAttribute(env='DATABRICKS_USERNAME', auth='basic')
    password: str = ConfigAttribute(env='DATABRICKS_PASSWORD', auth='basic', sensitive=True)
    client_id: str = ConfigAttribute(env='DATABRICKS_CLIENT_ID', auth='oauth')
    client_secret: str = ConfigAttribute(env='DATABRICKS_CLIENT_SECRET', auth='oauth', sensitive=True)
    profile: str = ConfigAttribute(env='DATABRICKS_CONFIG_PROFILE')
    config_file: str = ConfigAttribute(env='DATABRICKS_CONFIG_FILE')
    google_service_account: str = ConfigAttribute(env='DATABRICKS_GOOGLE_SERVICE_ACCOUNT', auth='google')
    google_credentials: str = ConfigAttribute(env='GOOGLE_CREDENTIALS', auth='google', sensitive=True)
    azure_workspace_resource_id: str = ConfigAttribute(env='DATABRICKS_AZURE_RESOURCE_ID', auth='azure')
    azure_use_msi: bool = ConfigAttribute(env='ARM_USE_MSI', auth='azure')
    azure_client_secret: str = ConfigAttribute(env='ARM_CLIENT_SECRET', auth='azure', sensitive=True)
    azure_client_id: str = ConfigAttribute(env='ARM_CLIENT_ID', auth='azure')
    azure_tenant_id: str = ConfigAttribute(env='ARM_TENANT_ID', auth='azure')
    azure_environment: str = ConfigAttribute(env='ARM_ENVIRONMENT')
    databricks_cli_path: str = ConfigAttribute(env='DATABRICKS_CLI_PATH')
    auth_type: str = ConfigAttribute(env='DATABRICKS_AUTH_TYPE')
    cluster_id: str = ConfigAttribute(env='DATABRICKS_CLUSTER_ID')
    warehouse_id: str = ConfigAttribute(env='DATABRICKS_WAREHOUSE_ID')
    skip_verify: bool = ConfigAttribute()
    http_timeout_seconds: float = ConfigAttribute()
    debug_truncate_bytes: int = ConfigAttribute(env='DATABRICKS_DEBUG_TRUNCATE_BYTES')
    debug_headers: bool = ConfigAttribute(env='DATABRICKS_DEBUG_HEADERS')
    rate_limit: int = ConfigAttribute(env='DATABRICKS_RATE_LIMIT')
    retry_timeout_seconds: int = ConfigAttribute()
    metadata_service_url = ConfigAttribute(env='DATABRICKS_METADATA_SERVICE_URL',
                                           auth='metadata-service',
                                           sensitive=True)
    max_connection_pools: int = ConfigAttribute()
    max_connections_per_pool: int = ConfigAttribute()
    databricks_environment: Optional[DatabricksEnvironment] = None

    def __init__(self,
                 *,
                 credentials_provider: CredentialsProvider = None,
                 product="unknown",
                 product_version="0.0.0",
                 clock: Clock = None,
                 **kwargs):
        self._inner = {}
        self._user_agent_other_info = []
        self._credentials_provider = credentials_provider if credentials_provider else DefaultCredentials()
        if 'databricks_environment' in kwargs:
            self.databricks_environment = kwargs['databricks_environment']
            del kwargs['databricks_environment']
        self._clock = clock if clock is not None else RealClock()
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

    def _get_azure_environment_name(self) -> str:
        if not self.azure_environment:
            return "PUBLIC"
        env = self.azure_environment.upper()
        # Compatibility with older versions of the SDK that allowed users to specify AzurePublicCloud or AzureChinaCloud
        if env.startswith("AZURE"):
            env = env[len("AZURE"):]
        if env.endswith("CLOUD"):
            env = env[:-len("CLOUD")]
        return env

    @property
    def environment(self) -> DatabricksEnvironment:
        """Returns the environment based on configuration."""
        if self.databricks_environment:
            return self.databricks_environment
        if self.host:
            for environment in ALL_ENVS:
                if self.host.endswith(environment.dns_zone):
                    return environment
        if self.azure_workspace_resource_id:
            azure_env = self._get_azure_environment_name()
            for environment in ALL_ENVS:
                if environment.cloud != Cloud.AZURE:
                    continue
                if environment.azure_environment.name != azure_env:
                    continue
                if environment.dns_zone.startswith(".dev") or environment.dns_zone.startswith(".staging"):
                    continue
                return environment
        return DEFAULT_ENVIRONMENT

    @property
    def is_azure(self) -> bool:
        return self.environment.cloud == Cloud.AZURE

    @property
    def is_gcp(self) -> bool:
        return self.environment.cloud == Cloud.GCP

    @property
    def is_aws(self) -> bool:
        return self.environment.cloud == Cloud.AWS

    @property
    def is_account_client(self) -> bool:
        if not self.host:
            return False
        return self.host.startswith("https://accounts.") or self.host.startswith("https://accounts-dod.")

    @property
    def arm_environment(self) -> AzureEnvironment:
        return self.environment.azure_environment

    @property
    def effective_azure_login_app_id(self):
        return self.environment.azure_application_id

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
        if self.is_azure and self.azure_client_id:
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

    @property
    def clock(self) -> Clock:
        return self._clock

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

    def deep_copy(self):
        """Creates a deep copy of the config object.
        """
        return copy.deepcopy(self)
