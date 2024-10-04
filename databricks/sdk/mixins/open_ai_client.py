from databricks.sdk.service.serving import ServingEndpointsAPI


class ServingEndpointsExt(ServingEndpointsAPI):

    def get_open_api_client(self):
        auth_headers = self._api._cfg.authenticate()

        try:
            token = auth_headers["Authorization"][len("Bearer "):]
        except Exception:
            raise ValueError("Unable to extract authorization token for OpenAI Client")

        from openai import OpenAI
        return OpenAI(base_url=self._api._cfg.host + "/serving-endpoints", api_key=token)
