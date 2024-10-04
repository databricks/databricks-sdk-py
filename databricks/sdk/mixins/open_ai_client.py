from databricks.sdk.service.serving import ServingEndpointsAPI


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
                "Open AI is not installed. Please install the Databricks SDK with the following command `pip isntall databricks-sdk[openai]`"
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
                "Langchain Open AI is not installed. Please install the Databricks SDK with the following command `pip isntall databricks-sdk[openai]` and ensure you are using python>3.7"
            )

        return ChatOpenAI(
            model=model,
            openai_api_base=self._api._cfg.host + "/serving-endpoints",
            api_key="no-token", # Passing in a placeholder to pass validations, this will not be used
            http_client=self._get_authorized_http_client())
