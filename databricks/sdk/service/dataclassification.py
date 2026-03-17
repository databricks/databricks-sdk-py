# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

from __future__ import annotations

import logging
from dataclasses import dataclass
from enum import Enum
from typing import Any, Dict, List, Optional

from databricks.sdk.common.types.fieldmask import FieldMask
from databricks.sdk.service._internal import _enum, _from_dict, _repeated_dict

_LOG = logging.getLogger("databricks.sdk")


# all definitions in this file are in alphabetical order


@dataclass
class AutoTaggingConfig:
    """Auto-tagging configuration for a classification tag. When enabled, detected columns are
    automatically tagged with Unity Catalog tags."""

    classification_tag: str
    """The Classification Tag (e.g., "class.name", "class.location")"""

    auto_tagging_mode: AutoTaggingConfigAutoTaggingMode
    """Whether auto-tagging is enabled or disabled for this classification tag."""

    def as_dict(self) -> dict:
        """Serializes the AutoTaggingConfig into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.auto_tagging_mode is not None:
            body["auto_tagging_mode"] = self.auto_tagging_mode.value
        if self.classification_tag is not None:
            body["classification_tag"] = self.classification_tag
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the AutoTaggingConfig into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.auto_tagging_mode is not None:
            body["auto_tagging_mode"] = self.auto_tagging_mode
        if self.classification_tag is not None:
            body["classification_tag"] = self.classification_tag
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> AutoTaggingConfig:
        """Deserializes the AutoTaggingConfig from a dictionary."""
        return cls(
            auto_tagging_mode=_enum(d, "auto_tagging_mode", AutoTaggingConfigAutoTaggingMode),
            classification_tag=d.get("classification_tag", None),
        )


class AutoTaggingConfigAutoTaggingMode(Enum):
    """Auto-tagging mode."""

    AUTO_TAGGING_DISABLED = "AUTO_TAGGING_DISABLED"
    AUTO_TAGGING_ENABLED = "AUTO_TAGGING_ENABLED"


@dataclass
class CatalogConfig:
    """Data Classification configuration for a Unity Catalog catalog. This message follows the "At Most
    One Resource" pattern: at most one CatalogConfig exists per catalog. - Full CRUD operations are
    supported: Create enables Data Classification, Delete disables it - It has no unique identifier
    of its own and uses its parent catalog's identifier (catalog_name)"""

    auto_tag_configs: Optional[List[AutoTaggingConfig]] = None
    """List of auto-tagging configurations for this catalog. Empty list means no auto-tagging is
    enabled."""

    included_schemas: Optional[CatalogConfigSchemaNames] = None
    """Schemas to include in the scan. Empty list is not supported as it results in a no-op scan. If
    `included_schemas` is not set, all schemas are scanned."""

    name: Optional[str] = None
    """Resource name in the format: catalogs/{catalog_name}/config."""

    def as_dict(self) -> dict:
        """Serializes the CatalogConfig into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.auto_tag_configs:
            body["auto_tag_configs"] = [v.as_dict() for v in self.auto_tag_configs]
        if self.included_schemas:
            body["included_schemas"] = self.included_schemas.as_dict()
        if self.name is not None:
            body["name"] = self.name
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the CatalogConfig into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.auto_tag_configs:
            body["auto_tag_configs"] = self.auto_tag_configs
        if self.included_schemas:
            body["included_schemas"] = self.included_schemas
        if self.name is not None:
            body["name"] = self.name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> CatalogConfig:
        """Deserializes the CatalogConfig from a dictionary."""
        return cls(
            auto_tag_configs=_repeated_dict(d, "auto_tag_configs", AutoTaggingConfig),
            included_schemas=_from_dict(d, "included_schemas", CatalogConfigSchemaNames),
            name=d.get("name", None),
        )


@dataclass
class CatalogConfigSchemaNames:
    """Wrapper message for a list of schema names."""

    names: List[str]

    def as_dict(self) -> dict:
        """Serializes the CatalogConfigSchemaNames into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.names:
            body["names"] = [v for v in self.names]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the CatalogConfigSchemaNames into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.names:
            body["names"] = self.names
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> CatalogConfigSchemaNames:
        """Deserializes the CatalogConfigSchemaNames from a dictionary."""
        return cls(names=d.get("names", None))


class DataClassificationAPI:
    """Manage data classification for Unity Catalog catalogs. Data classification automatically identifies and
    tags sensitive data (PII) in Unity Catalog tables. Each catalog can have at most one configuration
    resource that controls scanning behavior and auto-tagging rules."""

    def __init__(self, api_client):
        self._api = api_client

    def create_catalog_config(self, parent: str, catalog_config: CatalogConfig) -> CatalogConfig:
        """Create Data Classification configuration for a catalog.

        Creates a new config resource, which enables Data Classification for the specified catalog. - The
        config must not already exist for the catalog.

        :param parent: str
          Parent resource in the format: catalogs/{catalog_name}
        :param catalog_config: :class:`CatalogConfig`
          The configuration to create.

        :returns: :class:`CatalogConfig`
        """

        body = catalog_config.as_dict()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Org-Id"] = cfg.workspace_id

        res = self._api.do("POST", f"/api/data-classification/v1/{parent}/config", body=body, headers=headers)
        return CatalogConfig.from_dict(res)

    def delete_catalog_config(self, name: str):
        """Delete Data Classification configuration for a catalog.

        :param name: str
          Resource name in the format: catalogs/{catalog_name}/config


        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Org-Id"] = cfg.workspace_id

        self._api.do("DELETE", f"/api/data-classification/v1/{name}", headers=headers)

    def get_catalog_config(self, name: str) -> CatalogConfig:
        """Get the Data Classification configuration for a catalog.

        :param name: str
          Resource name in the format: catalogs/{catalog_name}/config

        :returns: :class:`CatalogConfig`
        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Org-Id"] = cfg.workspace_id

        res = self._api.do("GET", f"/api/data-classification/v1/{name}", headers=headers)
        return CatalogConfig.from_dict(res)

    def update_catalog_config(self, name: str, catalog_config: CatalogConfig, update_mask: FieldMask) -> CatalogConfig:
        """Update the Data Classification configuration for a catalog. - The config must already exist for the
        catalog. - Updates fields specified in the update_mask. Use update_mask field to perform partial
        updates of the configuration.

        :param name: str
          Resource name in the format: catalogs/{catalog_name}/config.
        :param catalog_config: :class:`CatalogConfig`
          The configuration to apply to the catalog. The name field in catalog_config identifies which
          resource to update.
        :param update_mask: FieldMask
          Field mask specifying which fields to update.

        :returns: :class:`CatalogConfig`
        """

        body = catalog_config.as_dict()
        query = {}
        if update_mask is not None:
            query["update_mask"] = update_mask.ToJsonString()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Org-Id"] = cfg.workspace_id

        res = self._api.do("PATCH", f"/api/data-classification/v1/{name}", query=query, body=body, headers=headers)
        return CatalogConfig.from_dict(res)
