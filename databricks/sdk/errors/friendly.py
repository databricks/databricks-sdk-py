import logging
import requests

from .customizer import _ErrorCustomizer

logger = logging.getLogger("databricks.sdk")


class _FriendlyErrorCustomizer(_ErrorCustomizer):
    """An error customizer that adds helpful resolution steps to common error messages."""

    # Common error patterns and their helpful resolutions
    ERROR_PATTERNS = {
        "Missing required field: cluster_id": (
            "No cluster is configured for this operation. "
            "To resolve this:\n"
            "  1. Set the cluster_id when initializing the WorkspaceClient:\n"
            "     WorkspaceClient(cluster_id='your-cluster-id')\n"
            "  2. Or set the DATABRICKS_CLUSTER_ID environment variable\n"
            "  3. Or configure it in your ~/.databrickscfg file\n"
            "For more details, see: https://docs.databricks.com/en/dev-tools/sdk-python.html"
        ),
        "Missing required field: host": (
            "No Databricks host is configured. "
            "To resolve this:\n"
            "  1. Set the host when initializing the WorkspaceClient:\n"
            "     WorkspaceClient(host='https://your-workspace.cloud.databricks.com')\n"
            "  2. Or set the DATABRICKS_HOST environment variable\n"
            "  3. Or configure it in your ~/.databrickscfg file"
        ),
        "Missing required field: token": (
            "No authentication token is configured. "
            "To resolve this:\n"
            "  1. Set the token when initializing the WorkspaceClient:\n"
            "     WorkspaceClient(token='your-access-token')\n"
            "  2. Or set the DATABRICKS_TOKEN environment variable\n"
            "  3. Or configure it in your ~/.databrickscfg file\n"
            "  4. Or use other authentication methods (see docs)"
        ),
        "Unauthorized": (
            "Authentication failed. "
            "To resolve this:\n"
            "  1. Verify your access token is valid and not expired\n"
            "  2. Check that the token has the required permissions\n"
            "  3. Ensure you're using the correct workspace URL\n"
            "  4. For more help, see: https://docs.databricks.com/en/dev-tools/auth.html"
        ),
    }

    def customize_error(self, response: requests.Response, kwargs: dict):
        message = kwargs.get("message", "")
        if not message:
            return

        for pattern, resolution in self.ERROR_PATTERNS.items():
            if pattern in message:
                # Add the resolution hint to the message
                kwargs["message"] = f"{message}\n\nResolution: {resolution}"
                logger.debug(f"Added friendly error hint for pattern: {pattern}")
                return
