import json as js
from dataclasses import dataclass
from typing import Dict, Optional

from databricks.sdk.service.serving import ExternalFunctionRequestHttpMethod
from databricks.sdk.service.serving import \
    ExternalFunctionResponse as ExternalFunctionResponseAPI
from databricks.sdk.service.serving import ServingEndpointsAPI


@dataclass
class ExternalFunctionResponse(ExternalFunctionResponseAPI):
    text: Dict[str, any] = None
    """The content of the response"""

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ExternalFunctionResponse':
        """Deserializes the ExternalFunctionResponse from a dictionary."""
        return cls(status_code=200, text=d)


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
            api_key="no-token", # Passing in a placeholder to pass validations, this will not be used
            http_client=self._get_authorized_http_client())

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
            api_key="no-token", # Passing in a placeholder to pass validations, this will not be used
            http_client=self._get_authorized_http_client())

    def http_request(self,
                     conn: str,
                     method: ExternalFunctionRequestHttpMethod,
                     path: str,
                     *,
                     headers: Optional[Dict[str, str]] = None,
                     json: Optional[Dict[str, str]] = None,
                     params: Optional[Dict[str, str]] = None) -> ExternalFunctionResponse:
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
        :returns: :class:`ExternalFunctionResponse`
        """

        body = {}
        if conn is not None: body['connection_name'] = conn
        if headers is not None: body['headers'] = js.dumps(headers)
        if json is not None: body['json'] = js.dumps(json)
        if method is not None: body['method'] = method.value
        if params is not None: body['params'] = js.dumps(params)
        if path is not None: body['path'] = path
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        res = self._api.do('POST', '/api/2.0/external-function', body=body, headers=headers)
        return ExternalFunctionResponse.from_dict(res)
