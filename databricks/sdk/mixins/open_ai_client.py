from databricks.sdk.service.serving import ServingEndpointsAPI


class ServingEndpointsExt(ServingEndpointsAPI):

    def get_open_ai_client(self):
        auth_headers = self._api._cfg.authenticate()

        try:
            token = auth_headers["Authorization"][len("Bearer "):]
        except Exception:
            raise ValueError("Unable to extract authorization token for OpenAI Client")

        from openai import OpenAI
        return OpenAI(base_url=self._api._cfg.host + "/serving-endpoints", api_key=token)

    def get_langchain_chat_open_ai_client(self, model):
        auth_headers = self._api._cfg.authenticate()

        try:
            token = auth_headers["Authorization"][len("Bearer "):]
        except Exception:
            raise ValueError("Unable to extract authorization token for Langchain OpenAI Client")

        from langchain_openai import ChatOpenAI
        return ChatOpenAI(model=model,
                          openai_api_base=self._api._cfg.host + "/serving-endpoints",
                          openai_api_key=token)
