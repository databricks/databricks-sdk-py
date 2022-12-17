import dataclasses
import requests
import requests.auth
from requests.adapters import HTTPAdapter

from urllib3.util.retry import Retry
from typing import (Dict, List, )
from abc import ABC, abstractmethod
from os import getenv
import threading
import logging
import pathlib
import configparser
import platform
import urllib.parse
import subprocess
from .oauth import ClientCredentials, Refreshable, Token
from .azure import ENVIRONMENTS, ARM_DATABRICKS_RESOURCE_ID, AzureEnvironment

logger = logging.getLogger(__name__)


class DatabricksError(Exception):

    def __init__(self,
                 message: str = None,
                 error_code: str = None,
                 detail: str = None,
                 status: str = None,
                 scimType: str = None,
                 error: str = None):
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
        super().__init__(message if message else error)
        self.error_code = error_code


class DatabricksAuth(ABC, requests.auth.AuthBase):

    @abstractmethod
    def is_configured(self) -> bool:
        pass

    @property
    @abstractmethod
    def name(self):
        pass


class Basic(DatabricksAuth, requests.auth.HTTPBasicAuth):

    def __init__(self, cfg: 'Config'):
        super().__init__(cfg.username, cfg.password)

    @property
    def name(self):
        return "basic"

    def is_configured(self) -> bool:
        return self.username and self.password


class Pat(DatabricksAuth):

    def __init__(self, cfg: 'Config'):
        self.token = cfg.token

    @property
    def name(self):
        return "pat"

    def is_configured(self) -> bool:
        return self.token is not None

    def __call__(self, r):
        r.headers["Authorization"] = f"Bearer {self.token}"
        return r


class OAuthM2M(DatabricksAuth):
    src: ClientCredentials = None

    def __init__(self, cfg: 'Config'):
        if not cfg.is_aws:
            return
        if not cfg.host or not cfg.client_id or not cfg.client_secret:
            return
        resp = requests.get(f"{cfg.host}/oidc/.well-known/oauth-authorization-server")
        if not resp.ok:
            return
        self.src = ClientCredentials(client_id=cfg.client_id,
                                     client_secret=cfg.client_secret,
                                     token_url=resp.json()["token_endpoint"],
                                     scopes=["all-apis"],
                                     use_header=True)

    @property
    def name(self):
        return "oauth-m2m"

    def is_configured(self) -> bool:
        return self.src is not None

    def __call__(self, r):
        token = self.src.token()
        r.headers["Authorization"] = f"{token.token_type} {token.access_token}"
        return r


class AzureServicePrincipal(DatabricksAuth):
    inner: ClientCredentials = None
    cloud: ClientCredentials = None

    def __init__(self, cfg: 'Config'):
        if not cfg.is_azure:
            return
        if not cfg.azure_client_id or not cfg.azure_client_secret or not cfg.azure_tenant_id or not cfg.azure_workspace_resource_id:
            return
        if not cfg.host:
            cfg.host = self._resolve_host(cfg)
        logger.info("Configured AAD token for Service Principal (%s)", cfg.azure_client_id)
        self.resource_id = cfg.azure_workspace_resource_id
        self.inner = self.token_source_for(cfg, ARM_DATABRICKS_RESOURCE_ID)
        self.cloud = self.token_source_for(cfg, cfg.arm_environment.service_management_endpoint)

    def _resolve_host(self, cfg) -> str:
        arm = cfg.arm_environment.resource_manager_endpoint
        token = self.token_source_for(cfg, arm).token()
        resp = requests.get(f"{arm}{cfg.azure_workspace_resource_id}?api-version=2018-04-01",
                            headers={"Authorization": f"Bearer {token.access_token}"})
        if not resp.ok:
            raise DatabricksError(f"Cannot resolve Azure Databricks workspace: {resp.content}")
        return f"https://{resp.json()['properties']['workspaceUrl']}"

    @staticmethod
    def token_source_for(cfg: 'Config', resource: str):
        aad_endpoint = cfg.arm_environment.active_directory_endpoint
        return ClientCredentials(client_id=cfg.azure_client_id,
                                 client_secret=cfg.azure_client_secret,
                                 token_url=f"{aad_endpoint}{cfg.azure_tenant_id}/oauth2/token",
                                 endpoint_params={"resource": resource},
                                 use_params=True)

    @property
    def name(self):
        return "azure-client-secret"

    def is_configured(self) -> bool:
        return self.inner is not None and self.cloud is not None

    def __call__(self, r):
        r.headers["X-Databricks-Azure-Workspace-Resource-Id"] = self.resource_id
        r.headers["X-Databricks-Azure-SP-Management-Token"] = self.cloud.token().access_token
        r.headers["Authorization"] = f"Bearer {self.inner.token().access_token}"
        return r


class AzureCli(DatabricksAuth, Refreshable):

    def __init__(self, cfg: 'Config'):
        pass

    def is_configured(self) -> bool:
        pass

    @property
    def name(self):
        return "azure-cli"

    def refresh(self) -> Token:
        result = subprocess.run(
            ["az", "account", "get-access-token", "--resource", self.resource, "--output", "json", ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True)
        print(result.returncode, result.stdout, result.stderr)

    def __call__(self, r):
        pass


class DefaultAuth(DatabricksAuth):
    classes: List[DatabricksAuth] = [Pat, Basic, OAuthM2M, AzureServicePrincipal]
    selected: DatabricksAuth = None

    def __init__(self, cfg: 'Config'):
        candidates = []
        for provider in self.classes:
            instance = provider(cfg)
            if instance.is_configured():
                candidates.append(instance)
        if not candidates:
            raise DatabricksError("No auth configured")
        if len(candidates) > 1:
            names = " and ".join(sorted([c.name for c in candidates]))
            raise DatabricksError(f"More than one auth configured: {names}")
        self.selected = candidates[0]

    def is_configured(self) -> bool:
        return self.selected is not None

    @property
    def name(self):
        return self.selected.name

    def __call__(self, r):
        return self.selected.__call__(r)


def known_file_config_loader(cfg: 'Config'):
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
    has_explicit_profile = cfg.profile != ""
    if not has_explicit_profile:
        profile = "DEFAULT"
    if not ini_file.has_section(profile):
        logger.debug("%s has no %s profile configured", config_path, profile)
        return
    logger.info("loading %s profile from %s", profile, config_path)
    for k, v in ini_file.items(profile):
        cfg.__setattr__(k, v) # TODO: fix setting of ints and bools
    cfg.profile = None
    cfg.config_file = None


@dataclasses.dataclass
class Config:
    host: str = getenv("DATABRICKS_HOST")

    credentials: DatabricksAuth = None

    # Databricks Account ID for Accounts API. This field is used in dependencies.
    account_id: str = getenv("DATABRICKS_ACCOUNT_ID")
    username: str = getenv("DATABRICKS_USERNAME")
    password: str = getenv("DATABRICKS_PASSWORD")
    client_id: str = getenv("DATABRICKS_CLIENT_ID")
    client_secret: str = getenv("DATABRICKS_CLIENT_SECRET")
    token: str = getenv("DATABRICKS_TOKEN")

    # Connection profile specified within ~/.databrickscfg.
    profile: str = getenv("DATABRICKS_CONFIG_PROFILE")
    # Location of the Databricks CLI credentials file, that is created
    # by `databricks configure --token` command. By default, it is located
    # in ~/.databrickscfg.
    config_file: str = getenv("DATABRICKS_CONFIG_FILE", "~/.databrickscfg")

    google_service_account: str = getenv("DATABRICKS_GOOGLE_SERVICE_ACCOUNT")
    google_credentials: str = getenv("GOOGLE_CREDENTIALS")

    # Azure Resource Manager ID for Azure Databricks workspace, which is exhanged for a Host
    azure_workspace_resource_id: str = getenv("DATABRICKS_AZURE_RESOURCE_ID")
    azure_use_msi: bool = getenv("ARM_USE_MSI", False)
    azure_client_secret: str = getenv("ARM_CLIENT_SECRET")
    azure_client_id: str = getenv("ARM_CLIENT_ID")
    azure_tenant_id: str = getenv("ARM_TENANT_ID")
    azure_environment: str = getenv("ARM_ENVIRONMENT")
    auth_type: str = None

    # Truncate JSON fields in JSON above this limit. Default is 96.
    debug_truncate_bytes: str = getenv("DATABRICKS_DEBUG_TRUNCATE_BYTES", 96)
    debug_headers: bool = getenv("DATABRICKS_DEBUG_HEADERS", False)
    rate_limit: int = getenv("DATABRICKS_RATE_LIMIT", 15)

    # Number of seconds for HTTP timeout
    http_timeout_seconds: int = 30

    loaders = [known_file_config_loader]
    _lock = threading.Lock()
    _resolved = False

    @property
    def is_azure(self) -> bool:
        return self.azure_workspace_resource_id or ".azuredatabricks.net" in self.host

    @property
    def is_gcp(self) -> bool:
        return ".gcp.databricks.com" in self.host

    @property
    def is_aws(self) -> bool:
        return not self.is_azure and not self.is_gcp

    @property
    def is_accounts(self) -> bool:
        return "https://accounts." in self.host

    @property
    def arm_environment(self) -> AzureEnvironment:
        env = self.azure_environment if self.azure_environment else "PUBLIC"
        try:
            return ENVIRONMENTS[env]
        except KeyError:
            raise DatabricksError(f"Cannot find Azure {env} Environment")

    def auth(self) -> DatabricksAuth:
        self._synchronized(self._resolve)
        if self.credentials:
            return self.credentials
        self._lock.acquire()
        try:
            if self.credentials:
                return self.credentials
            self.credentials = DefaultAuth(self)
            return self.credentials
        finally:
            self._lock.release()

    def to_dict(self) -> Dict[str, any]:
        return {k: v for k, v in dataclasses.asdict(self).items() if v}

    def _resolve(self):
        if self._resolved:
            return
        for loader in self.loaders:
            logger.debug("loading config via %s", loader.__name__)
            loader(self)
        if self.host:
            # fix url to remove trailing slash
            o = urllib.parse.urlparse(self.host)
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
            raise_on_status=False, # return original response when retries have been exhausted
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

    def do(self, method: str, path, query: dict = None, body: dict = None) -> dict:
        response = self.request(method,
                                f"{self._cfg.host}{path}",
                                params=query,
                                json=body,
                                headers={"User-Agent": self._user_agent_base})
        if not response.ok:
            raise DatabricksError(**response.json())
        return response.json()
