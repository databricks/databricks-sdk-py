import json as js
from typing import Dict, Optional

from requests import Response

from databricks.sdk.service.serving import (ExternalFunctionRequestHttpMethod,
                                            HttpRequestResponse,
                                            ServingEndpointsAPI)


def _get_bearer_auth(authenticate_func):
    """Create an httpx Auth class that uses Databricks authentication.

    This auth class works with both httpx.Client and httpx.AsyncClient.
    The auth_flow generator pattern is automatically wrapped by httpx for
    both sync and async operations.
    """
    import httpx

    class BearerAuth(httpx.Auth):
        def __init__(self, get_headers_func):
            self.get_headers_func = get_headers_func

        def auth_flow(self, request: httpx.Request):
            auth_headers = self.get_headers_func()
            request.headers["Authorization"] = auth_headers["Authorization"]
            yield request

    return BearerAuth(authenticate_func)


class ServingEndpointsExt(ServingEndpointsAPI):

    _OPENAI_RESERVED_PARAMS = {"base_url", "api_key", "http_client"}

    def _check_reserved_openai_params(self, kwargs):
        conflicting_params = self._OPENAI_RESERVED_PARAMS.intersection(kwargs.keys())
        if conflicting_params:
            raise ValueError(
                f"Cannot override reserved Databricks parameters: {', '.join(sorted(conflicting_params))}. "
                f"These parameters are automatically configured for Databricks Model Serving."
            )

    def _build_openai_client_params(self, http_client, kwargs):
        client_params = {
            "base_url": self._api._cfg.host + "/serving-endpoints",
            "api_key": "no-token",
            "http_client": http_client,
        }
        client_params.update(kwargs)
        return client_params

    def _get_authorized_http_client(self):
        import httpx

        databricks_token_auth = _get_bearer_auth(self._api._cfg.authenticate)
        return httpx.Client(auth=databricks_token_auth)

    def _get_authorized_async_http_client(self): 
        import httpx

        databricks_token_auth = _get_bearer_auth(self._api._cfg.authenticate)
        return httpx.AsyncClient(auth=databricks_token_auth)

    def get_open_ai_client(self, **kwargs):
        """Create an OpenAI client configured for Databricks Model Serving.

        Returns an OpenAI client instance that is pre-configured to send requests to
        Databricks Model Serving endpoints. The client uses Databricks authentication
        to query endpoints within the workspace associated with the current WorkspaceClient
        instance.

        Args:
            **kwargs: Additional parameters to pass to the OpenAI client constructor.
                Common parameters include:
                - timeout (float): Request timeout in seconds (e.g., 30.0)
                - max_retries (int): Maximum number of retries for failed requests (e.g., 3)
                - default_headers (dict): Additional headers to include with requests
                - default_query (dict): Additional query parameters to include with requests

                Any parameter accepted by the OpenAI client constructor can be passed here,
                except for the following parameters which are reserved for Databricks integration:
                base_url, api_key, http_client

        Returns:
            OpenAI: An OpenAI client instance configured for Databricks Model Serving.

        Raises:
            ImportError: If the OpenAI library is not installed.
            ValueError: If any reserved Databricks parameters are provided in kwargs.

        Example:
            >>> client = workspace_client.serving_endpoints.get_open_ai_client()
            >>> # With custom timeout and retries
            >>> client = workspace_client.serving_endpoints.get_open_ai_client(
            ...     timeout=30.0,
            ...     max_retries=5
            ... )
        """
        try:
            from openai import OpenAI
        except Exception:
            raise ImportError(
                "OpenAI is not installed. Please install the Databricks SDK with the following command `pip install databricks-sdk[openai]`"
            )

        self._check_reserved_openai_params(kwargs)
        client_params = self._build_openai_client_params(self._get_authorized_http_client(), kwargs)
        return OpenAI(**client_params)

    def get_async_open_ai_client(self, **kwargs):
        """Create an AsyncOpenAI client configured for Databricks Model Serving.

        Returns an AsyncOpenAI client instance that is pre-configured to send requests to
        Databricks Model Serving endpoints. The client uses Databricks authentication
        to query endpoints within the workspace associated with the current WorkspaceClient
        instance.

        This client is suitable for async/await patterns and concurrent API calls.

        Args:
            **kwargs: Additional parameters to pass to the AsyncOpenAI client constructor.
                Common parameters include:
                - timeout (float): Request timeout in seconds (e.g., 30.0)
                - max_retries (int): Maximum number of retries for failed requests (e.g., 3)
                - default_headers (dict): Additional headers to include with requests
                - default_query (dict): Additional query parameters to include with requests

                Any parameter accepted by the AsyncOpenAI client constructor can be passed here,
                except for the following parameters which are reserved for Databricks integration:
                base_url, api_key, http_client

        Returns:
            AsyncOpenAI: An AsyncOpenAI client instance configured for Databricks Model Serving.

        Raises:
            ImportError: If the OpenAI library is not installed.
            ValueError: If any reserved Databricks parameters are provided in kwargs.

        Example:
            >>> client = workspace_client.serving_endpoints.get_async_open_ai_client()
            >>> # With custom timeout and retries
            >>> client = workspace_client.serving_endpoints.get_async_open_ai_client(
            ...     timeout=30.0,
            ...     max_retries=5
            ... )
            >>> # Use with async/await
            >>> response = await client.chat.completions.create(
            ...     model="databricks-meta-llama-3-1-70b-instruct",
            ...     messages=[{"role": "user", "content": "Hello!"}]
            ... )
        """
        try:
            from openai import AsyncOpenAI
        except Exception:
            raise ImportError(
                "OpenAI is not installed. Please install the Databricks SDK with the following command `pip install databricks-sdk[openai]`"
            )

        self._check_reserved_openai_params(kwargs)
        client_params = self._build_openai_client_params(self._get_authorized_async_http_client(), kwargs)
        return AsyncOpenAI(**client_params)

    def get_langchain_chat_open_ai_client(self, model):
        """Create a LangChain ChatOpenAI client configured for Databricks Model Serving.

        Returns a ChatOpenAI instance that is pre-configured to send requests to
        Databricks Model Serving endpoints. The client uses Databricks authentication
        for both synchronous and asynchronous operations.

        Args:
            model: The name of the model serving endpoint to use.

        Returns:
            ChatOpenAI: A LangChain ChatOpenAI client instance configured for Databricks.

        Raises:
            ImportError: If langchain-openai is not installed.
        """
        try:
            from langchain_openai import ChatOpenAI
        except Exception:
            raise ImportError(
                "Langchain OpenAI is not installed. Please install the Databricks SDK with the following command `pip install databricks-sdk[openai]` and ensure you are using python>3.7"
            )

        return ChatOpenAI(
            model=model,
            openai_api_base=self._api._cfg.host + "/serving-endpoints",
            api_key="no-token",  # Passing in a placeholder to pass validations, this will not be used
            http_client=self._get_authorized_http_client(),
            http_async_client=self._get_authorized_async_http_client(),
        )

    def http_request(
        self,
        conn: str,
        method: ExternalFunctionRequestHttpMethod,
        path: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        json: Optional[Dict[str, str]] = None,
        params: Optional[Dict[str, str]] = None,
    ) -> Response:
        """Make external services call using the credentials stored in UC Connection.
        **NOTE:** Experimental: This API may change or be removed in a future release without warning.
        :param conn: str
          The connection name to use. This is required to identify the external connection.
        :param method: :class:`ExternalFunctionRequestHttpMethod`
          The HTTP method to use (e.g., 'GET', 'POST'). This is required.
        :param path: str
          The relative path for the API endpoint. This is required.
        :param headers: Dict[str,str] (optional)
          Additional headers for the request. If not provided, only auth headers from connections would be
          passed.
        :param json: Dict[str,str] (optional)
          JSON payload for the request.
        :param params: Dict[str,str] (optional)
          Query parameters for the request.
        :returns: :class:`Response`
        """
        response = Response()
        response.status_code = 200

        # We currently don't call super.http_request because we need to pass in response_headers
        # This is a temporary fix to get the headers we need for the MCP session id
        # TODO: Remove this once we have a better way to get back the response headers
        headers_to_capture = ["mcp-session-id"]
        res = self._api.do(
            "POST",
            "/api/2.0/external-function",
            body={
                "connection_name": conn,
                "method": method.value,
                "path": path,
                "headers": js.dumps(headers) if headers is not None else None,
                "json": js.dumps(json) if json is not None else None,
                "params": js.dumps(params) if params is not None else None,
            },
            headers={"Accept": "text/plain", "Content-Type": "application/json"},
            raw=True,
            response_headers=headers_to_capture,
        )

        # Create HttpRequestResponse from the raw response
        server_response = HttpRequestResponse.from_dict(res)

        # Read the content from the HttpRequestResponse object
        if hasattr(server_response, "contents") and hasattr(server_response.contents, "read"):
            raw_content = server_response.contents.read()  # Read the bytes
        else:
            raise ValueError("Invalid response from the server.")

        # Set the raw content
        if isinstance(raw_content, bytes):
            response._content = raw_content
        else:
            raise ValueError("Contents must be bytes.")

        # Copy headers from raw response to Response
        for header_name in headers_to_capture:
            if header_name in res:
                response.headers[header_name] = res[header_name]

        return response
