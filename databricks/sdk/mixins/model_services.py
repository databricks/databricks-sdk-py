class ModelServicesExt:
    """Extension for querying Unity Catalog model services (v3 ``system.ai.*`` models) via the AI Gateway."""

    def __init__(self, api_client):
        self._api = api_client

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

    def get_open_ai_client(self, **kwargs):
        """Create an OpenAI client configured for querying Unity Catalog model services via the AI Gateway.

        Returns an OpenAI client instance that is pre-configured to send requests to the
        Databricks AI Gateway. The client uses Databricks authentication to query model
        services within the workspace associated with the current WorkspaceClient instance.
        A model service is queried by passing its UC three-level name as the ``model``
        parameter.

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
            OpenAI: An OpenAI client instance configured for querying Unity Catalog model services.

        Raises:
            ImportError: If the OpenAI library is not installed.
            ValueError: If any reserved Databricks parameters are provided in kwargs.

        Example:
            >>> client = workspace_client.model_services.get_open_ai_client()
            >>> client.chat.completions.create(
            ...     model="system.ai.claude-sonnet-4-5",
            ...     messages=[{"role": "user", "content": "Hello!"}],
            ...     max_tokens=256,
            ... )
        """
        try:
            from openai import OpenAI
        except Exception:
            raise ImportError(
                "Open AI is not installed. Please install the Databricks SDK with the following command `pip install databricks-sdk[openai]`"
            )

        # Check for reserved parameters that should not be overridden
        reserved_params = {"base_url", "api_key", "http_client"}
        conflicting_params = reserved_params.intersection(kwargs.keys())
        if conflicting_params:
            raise ValueError(
                f"Cannot override reserved Databricks parameters: {', '.join(sorted(conflicting_params))}. "
                f"These parameters are automatically configured for Databricks Model Serving."
            )

        # Default parameters that are required for Databricks integration
        client_params = {
            "base_url": self._api._cfg.host + "/ai-gateway/mlflow/v1",
            "api_key": "no-token",  # Passing in a placeholder to pass validations, this will not be used
            "http_client": self._get_authorized_http_client(),
        }

        # Update with any additional parameters passed by the user
        client_params.update(kwargs)

        return OpenAI(**client_params)

    def get_langchain_chat_open_ai_client(self, model):
        try:
            from langchain_openai import ChatOpenAI
        except Exception:
            raise ImportError(
                "Langchain Open AI is not installed. Please install the Databricks SDK with the following command `pip install databricks-sdk[openai]` and ensure you are using python>3.7"
            )

        return ChatOpenAI(
            model=model,
            openai_api_base=self._api._cfg.host + "/ai-gateway/mlflow/v1",
            api_key="no-token",  # Passing in a placeholder to pass validations, this will not be used
            http_client=self._get_authorized_http_client(),
        )
