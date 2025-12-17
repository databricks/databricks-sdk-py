import re
from typing import BinaryIO
from urllib.parse import urlencode

from ._base_client import _BaseClient
from .config import *
# To preserve backwards compatibility (as these definitions were previously in this module)
from .credentials_provider import *
from .errors import DatabricksError, _ErrorCustomizer
from .oauth import retrieve_token

__all__ = ["Config", "DatabricksError"]

logger = logging.getLogger("databricks.sdk")

URL_ENCODED_CONTENT_TYPE = "application/x-www-form-urlencoded"
JWT_BEARER_GRANT_TYPE = "urn:ietf:params:oauth:grant-type:jwt-bearer"
OIDC_TOKEN_PATH = "/oidc/v1/token"


class ApiClient:

    def __init__(self, cfg: Config):
        self._cfg = cfg

        # Create header factory that includes both auth and org ID headers
        def combined_header_factory():
            headers = cfg.authenticate()
            # Add X-Databricks-Org-Id header for workspace clients on unified hosts
            if cfg.workspace_id and cfg.host_type == HostType.UNIFIED:
                headers["X-Databricks-Org-Id"] = cfg.workspace_id
            return headers

        self._api_client = _BaseClient(
            debug_truncate_bytes=cfg.debug_truncate_bytes,
            retry_timeout_seconds=cfg.retry_timeout_seconds,
            user_agent_base=cfg.user_agent,
            header_factory=combined_header_factory,
            max_connection_pools=cfg.max_connection_pools,
            max_connections_per_pool=cfg.max_connections_per_pool,
            pool_block=True,
            http_timeout_seconds=cfg.http_timeout_seconds,
            extra_error_customizers=[_AddDebugErrorCustomizer(cfg)],
            clock=cfg.clock,
        )

    @property
    def account_id(self) -> str:
        return self._cfg.account_id

    @property
    def is_account_client(self) -> bool:
        return self._cfg.is_account_client

    def get_oauth_token(self, auth_details: str) -> Token:
        if not self._cfg.auth_type:
            self._cfg.authenticate()
        original_token = self._cfg.oauth_token()
        headers = {"Content-Type": URL_ENCODED_CONTENT_TYPE}
        params = urlencode(
            {
                "grant_type": JWT_BEARER_GRANT_TYPE,
                "authorization_details": auth_details,
                "assertion": original_token.access_token,
            }
        )
        return retrieve_token(
            client_id=self._cfg.client_id,
            client_secret=self._cfg.client_secret,
            token_url=self._cfg.host + OIDC_TOKEN_PATH,
            params=params,
            headers=headers,
        )

    def do(
        self,
        method: str,
        path: Optional[str] = None,
        url: Optional[str] = None,
        query: Optional[dict] = None,
        headers: Optional[dict] = None,
        body: Optional[dict] = None,
        raw: bool = False,
        files=None,
        data=None,
        auth: Optional[Callable[[requests.PreparedRequest], requests.PreparedRequest]] = None,
        response_headers: Optional[List[str]] = None,
    ) -> Union[dict, list, BinaryIO]:
        if url is None:
            # Remove extra `/` from path for Files API
            # Once we've fixed the OpenAPI spec, we can remove this
            path = re.sub("^/api/2.0/fs/files//", "/api/2.0/fs/files/", path)
            url = f"{self._cfg.host}{path}"
        return self._api_client.do(
            method=method,
            url=url,
            query=query,
            headers=headers,
            body=body,
            raw=raw,
            files=files,
            data=data,
            auth=auth,
            response_headers=response_headers,
        )


class _AddDebugErrorCustomizer(_ErrorCustomizer):
    """An error customizer that adds debug information about the configuration to unauthenticated and
    unauthorized errors."""

    def __init__(self, cfg: Config):
        self._cfg = cfg

    def customize_error(self, response: requests.Response, kwargs: dict):
        if response.status_code in (401, 403):
            message = kwargs.get("message", "request failed")
            kwargs["message"] = self._cfg.wrap_debug_info(message)
