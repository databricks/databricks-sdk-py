from databricks.sdk.service.serving import ServingEndpointsAPI


class ServingEndpointsExt(ServingEndpointsAPI):

    def get_open_ai_client(self):
        auth_headers = self._api._cfg.authenticate()

        try:
            token = auth_headers["Authorization"][len("Bearer "):]
        except Exception:
            raise ValueError("Unable to extract authorization token for OpenAI Client")

        try:
            from openai import OpenAI
        except Exception:
            raise ImportError(
                "Open AI is not installed. Please install the Databricks SDK with the following command `pip isntall databricks-sdk[openai]`"
            )

        return OpenAI(base_url=self._api._cfg.host + "/serving-endpoints", api_key=token)

    def get_langchain_chat_open_ai_client(self, model):
        auth_headers = self._api._cfg.authenticate()

        try:
            from langchain_openai import ChatOpenAI
        except Exception:
            raise ImportError(
                "Langchain Open AI is not installed. Please install the Databricks SDK with the following command `pip isntall databricks-sdk[openai]` and ensure you are using python>3.7"
            )

        try:
            token = auth_headers["Authorization"][len("Bearer "):]
        except Exception:
            raise ValueError("Unable to extract authorization token for Langchain OpenAI Client")

        return ChatOpenAI(model=model,
                          openai_api_base=self._api._cfg.host + "/serving-endpoints",
                          openai_api_key=token)
