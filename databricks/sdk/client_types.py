from enum import Enum
from typing import Optional


class HostType(Enum):
    """Enum representing the type of Databricks host."""

    ACCOUNTS = "accounts"
    WORKSPACE = "workspace"
    UNIFIED = "unified"

    @staticmethod
    def from_api_value(value: str) -> Optional["HostType"]:
        """Normalize a host_type string from the API to a HostType enum value.

        Maps "workspace" -> WORKSPACE, "account" -> ACCOUNTS, "unified" -> UNIFIED.
        Returns None for unrecognized or empty values.
        """
        if not value:
            return None
        normalized = value.lower()
        if normalized == "workspace":
            return HostType.WORKSPACE
        if normalized == "account":
            return HostType.ACCOUNTS
        if normalized == "unified":
            return HostType.UNIFIED
        return None


class ClientType(Enum):
    """Enum representing the type of client configuration."""

    ACCOUNT = "account"
    WORKSPACE = "workspace"
