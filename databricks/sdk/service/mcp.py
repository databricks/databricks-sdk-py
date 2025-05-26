from mcp.client.auth import OAuthClientProvider, TokenStorage
from mcp.shared.auth import OAuthToken

class DatabricksTokenStorage(TokenStorage):
    def __init__(self, config):
        self.config = config

    async def get_tokens(self) -> OAuthToken| None:
        headers = self.config.authenticate()
        token = headers["Authorization"].split("Bearer ")[1]
        return OAuthToken(access_token=token, expires_in=60)
    
class MCP:
    def __init__(self, config):
        self._config = config
        self.databricks_token_storage = DatabricksTokenStorage(config)

    def oauth_provider(self):
        return OAuthClientProvider(
            server_url="",
            client_metadata=None,
            storage=self.databricks_token_storage,
            redirect_handler=None,
            callback_handler=None,
        )