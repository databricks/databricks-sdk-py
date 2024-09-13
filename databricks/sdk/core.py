import re
from datetime import timedelta
from types import TracebackType
from typing import Any, BinaryIO, Iterator, Type
from urllib.parse import urlencode

from requests.adapters import HTTPAdapter

from .casing import Casing
from .config import *
# To preserve backwards compatibility (as these definitions were previously in this module)
from .credentials_provider import *
from .errors import DatabricksError, _ErrorCustomizer, _Parser
from .logger import RoundTrip
from .oauth import retrieve_token
from .retries import retried

__all__ = ['Config', 'DatabricksError']

logger = logging.getLogger('databricks.sdk')

URL_ENCODED_CONTENT_TYPE = "application/x-www-form-urlencoded"
JWT_BEARER_GRANT_TYPE = "urn:ietf:params:oauth:grant-type:jwt-bearer"
OIDC_TOKEN_PATH = "/oidc/v1/token"


class ApiClient:
    _cfg: Config
    _RETRY_AFTER_DEFAULT: int = 1

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

        # Default to 60 seconds
        self._http_timeout_seconds = cfg.http_timeout_seconds if cfg.http_timeout_seconds else 60

        self._error_parser = _Parser(extra_error_customizers=[_AddDebugErrorCustomizer(cfg)])

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

    def get_oauth_token(self, auth_details: str) -> Token:
        if not self._cfg.auth_type:
            self._cfg.authenticate()
        original_token = self._cfg.oauth_token()
        headers = {"Content-Type": URL_ENCODED_CONTENT_TYPE}
        params = urlencode({
            "grant_type": JWT_BEARER_GRANT_TYPE,
            "authorization_details": auth_details,
            "assertion": original_token.access_token
        })
        return retrieve_token(client_id=self._cfg.client_id,
                              client_secret=self._cfg.client_secret,
                              token_url=self._cfg.host + OIDC_TOKEN_PATH,
                              params=params,
                              headers=headers)

    def do(self,
           method: str,
           path: str = None,
           url: str = None,
           query: dict = None,
           headers: dict = None,
           body: dict = None,
           raw: bool = False,
           files=None,
           data=None,
           auth: Callable[[requests.PreparedRequest], requests.PreparedRequest] = None,
           response_headers: List[str] = None) -> Union[dict, BinaryIO]:
        if headers is None:
            headers = {}
        if url is None:
            # Remove extra `/` from path for Files API
            # Once we've fixed the OpenAPI spec, we can remove this
            path = re.sub('^/api/2.0/fs/files//', '/api/2.0/fs/files/', path)
            url = f"{self._cfg.host}{path}"
        headers['User-Agent'] = self._user_agent_base
        retryable = retried(timeout=timedelta(seconds=self._retry_timeout_seconds),
                            is_retryable=self._is_retryable,
                            clock=self._cfg.clock)
        response = retryable(self._perform)(method,
                                            url,
                                            query=query,
                                            headers=headers,
                                            body=body,
                                            raw=raw,
                                            files=files,
                                            data=data,
                                            auth=auth)

        resp = dict()
        for header in response_headers if response_headers else []:
            resp[header] = response.headers.get(Casing.to_header_case(header))
        if raw:
            resp["contents"] = StreamingResponse(response)
            return resp
        if not len(response.content):
            return resp

        jsonResponse = response.json()
        if jsonResponse is None:
            return resp

        if isinstance(jsonResponse, list):
            return jsonResponse

        return {**resp, **jsonResponse}

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

    def _perform(self,
                 method: str,
                 url: str,
                 query: dict = None,
                 headers: dict = None,
                 body: dict = None,
                 raw: bool = False,
                 files=None,
                 data=None,
                 auth: Callable[[requests.PreparedRequest], requests.PreparedRequest] = None):
        response = self._session.request(method,
                                         url,
                                         params=self._fix_query_string(query),
                                         json=body,
                                         headers=headers,
                                         files=files,
                                         data=data,
                                         auth=auth,
                                         stream=raw,
                                         timeout=self._http_timeout_seconds)
        self._record_request_log(response, raw=raw or data is not None or files is not None)
        error = self._error_parser.get_api_error(response)
        if error is not None:
            raise error from None
        return response

    def _record_request_log(self, response: requests.Response, raw: bool = False) -> None:
        if not logger.isEnabledFor(logging.DEBUG):
            return
        logger.debug(RoundTrip(response, self._cfg.debug_headers, self._debug_truncate_bytes, raw).generate())


class _AddDebugErrorCustomizer(_ErrorCustomizer):
    """An error customizer that adds debug information about the configuration to unauthenticated and
    unauthorized errors."""

    def __init__(self, cfg: Config):
        self._cfg = cfg

    def customize_error(self, response: requests.Response, kwargs: dict):
        if response.status_code in (401, 403):
            message = kwargs.get('message', 'request failed')
            kwargs['message'] = self._cfg.wrap_debug_info(message)


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
