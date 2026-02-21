from urllib import parse

import requests

from .platform import PermissionDenied


def _unified_private_link_error_message():
    """Returns a unified error message for private link validation errors across all clouds."""
    return (
        "The requested workspace has Private Link enabled and is not accessible from the current network. "
        "Ensure that Private Link is properly configured for your cloud provider and that your device has "
        "access to the appropriate endpoint:\n\n"
        "  • AWS: Ensure AWS PrivateLink is configured and you have access to the AWS VPC endpoint. "
        "See https://docs.databricks.com/en/security/network/classic/privatelink.html\n"
        "  • Azure: Ensure Azure Private Link is configured and you have access to the Azure Private Link endpoint. "
        "See https://learn.microsoft.com/en-us/azure/databricks/security/network/classic/private-link-standard#authentication-troubleshooting\n"
        "  • GCP: Ensure Private Service Connect is configured and you have access to the GCP VPC endpoint. "
        "See https://docs.gcp.databricks.com/en/security/network/classic/private-service-connect.html"
    )


class PrivateLinkValidationError(PermissionDenied):
    """Raised when a user tries to access a Private Link-enabled workspace, but the user's network does not have access
    to the workspace."""


def _is_private_link_redirect(resp: requests.Response) -> bool:
    parsed = parse.urlparse(resp.url)
    return parsed.path == "/login.html" and "error=private-link-validation-error" in parsed.query


def _get_private_link_validation_error() -> PrivateLinkValidationError:
    return PrivateLinkValidationError(
        message=_unified_private_link_error_message(),
        error_code="PRIVATE_LINK_VALIDATION_ERROR",
        status_code=403,
    )
