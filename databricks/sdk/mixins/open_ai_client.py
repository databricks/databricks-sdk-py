import json as js
from typing import Dict, Optional

from requests import Response

from databricks.sdk.service.serving import (ExternalFunctionRequestHttpMethod,
                                            HttpRequestResponse,
                                            ServingEndpointsAPI)


class ServingEndpointsExt(ServingEndpointsAPI):

    # Using the HTTP Client to pass in the databricks authorization
    # This method will be called on every invocation, so when using with model serving will always get the refreshed token
    def _get_authorized_http_client(self):
        import httpx

        class BearerAuth(httpx.Auth):

            def __init__(self, get_headers_func):
                self.get_headers_func = get_headers_func

            def auth_flow(self, request: httpx.Request) -> httpx.Request:
                auth_headers = self.get_headers_func()
                request.headers["Authorization"] = auth_headers["Authorization"]
                yield request

        databricks_token_auth = BearerAuth(self._api._cfg.authenticate)

        # Create an HTTP client with Bearer Token authentication
        http_client = httpx.Client(auth=databricks_token_auth)
        return http_client

    def get_open_ai_client(self):
        try:
            from openai import OpenAI
        except Exception:
            raise ImportError(
                "Open AI is not installed. Please install the Databricks SDK with the following command `pip install databricks-sdk[openai]`"
            )

        return OpenAI(
            base_url=self._api._cfg.host + "/serving-endpoints",
            api_key="no-token",  # Passing in a placeholder to pass validations, this will not be used
            http_client=self._get_authorized_http_client(),
        )

    def get_langchain_chat_open_ai_client(self, model):
        try:
            from langchain_openai import ChatOpenAI
        except Exception:
            raise ImportError(
                "Langchain Open AI is not installed. Please install the Databricks SDK with the following command `pip install databricks-sdk[openai]` and ensure you are using python>3.7"
            )

        return ChatOpenAI(
            model=model,
            openai_api_base=self._api._cfg.host + "/serving-endpoints",
            api_key="no-token",  # Passing in a placeholder to pass validations, this will not be used
            http_client=self._get_authorized_http_client(),
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
