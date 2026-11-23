# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.
# ruff: noqa: F811, F841
# F401 is intentionally NOT covered: `make fmt` uses `ruff check --fix-only`
# to strip the fat-import header below; ignoring F401 would defeat that.

from __future__ import annotations
from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Any, Optional


import logging

from databricks.sdk.service._internal import (
    _enum,
    _from_dict,
    _repeated_dict,
)
from databricks.sdk.common.types.fieldmask import FieldMask


_LOG = logging.getLogger("databricks.sdk")


# all definitions in this file are in alphabetical order


@dataclass
class AutoTaggingConfig:
    """Auto-tagging configuration for a classification tag. When enabled, detected columns are
    automatically tagged with Unity Catalog tags."""

    classification_tag: str
    """The Classification Tag. For built-in classes this is a system tag (e.g., "class.name",
    "class.location"); for custom classes it is a user-defined governance tag key. The built-in tags
    are listed at
    https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-classification-tags."""

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
    One Resource" pattern: at most one CatalogConfig exists per catalog.

    - Full CRUD operations are supported: Create enables Data Classification, Delete disables it
    - It has no unique identifier of its own and uses its parent catalog's identifier (catalog_name)"""

    auto_tag_configs: Optional[List[AutoTaggingConfig]] = None
    """Auto-tagging configurations that apply to this catalog. Each entry overrides the metastore-level
    auto-tagging setting for its classification tag; tags without an entry inherit the
    metastore-level setting."""

    excluded_schemas: Optional[CatalogConfigSchemaNames] = None
    """Schemas to exclude from the scan, each named relative to the parent catalog. If specified, all
    schemas except the specified ones will be scanned, including schemas created later. Mutually
    exclusive with ``included_schemas``: only one may be set per request. If neither
    ``included_schemas`` nor ``excluded_schemas`` is set, all schemas are scanned."""

    included_schemas: Optional[CatalogConfigSchemaNames] = None
    """Schemas to include in the scan, each named relative to the parent catalog. If specified, only
    listed schemas will be scanned. Schemas created later are not scanned until you add them to the
    list. Mutually exclusive with ``excluded_schemas``: only one may be set per request. If neither
    ``included_schemas`` nor ``excluded_schemas`` is set, all schemas are scanned."""

    name: Optional[str] = None
    """Resource name in the format: catalogs/{catalog_name}/config."""

    def as_dict(self) -> dict:
        """Serializes the CatalogConfig into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.auto_tag_configs:
            body["auto_tag_configs"] = [v.as_dict() for v in self.auto_tag_configs]
        if self.excluded_schemas:
            body["excluded_schemas"] = self.excluded_schemas.as_dict()
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
        if self.excluded_schemas:
            body["excluded_schemas"] = self.excluded_schemas
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
            excluded_schemas=_from_dict(d, "excluded_schemas", CatalogConfigSchemaNames),
            included_schemas=_from_dict(d, "included_schemas", CatalogConfigSchemaNames),
            name=d.get("name", None),
        )


@dataclass
class CatalogConfigSchemaNames:
    """Wrapper message for a list of schema names."""

    names: List[str]
    """Schema names, each relative to the parent catalog. Must not be empty."""

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


@dataclass
class RescanCatalogResponse:
    """Response for RescanCatalog. Empty for now; a named message lets later versions add fields."""

    def as_dict(self) -> dict:
        """Serializes the RescanCatalogResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the RescanCatalogResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> RescanCatalogResponse:
        """Deserializes the RescanCatalogResponse from a dictionary."""
        return cls()


class DataClassificationAPI:
    """Manage data classification for Unity Catalog catalogs. Data classification automatically identifies and
    tags sensitive data (PII) in Unity Catalog tables. Each catalog can have at most one configuration
    resource that controls scanning behavior and auto-tagging rules."""

    def __init__(self, api_client):
        self._api = api_client

    def create_catalog_config(self, parent: str, catalog_config: CatalogConfig) -> CatalogConfig:
        """Create Data Classification configuration for a catalog.

        Creates a new config resource, which enables Data Classification for the specified catalog. The
        catalog must not already have a config. Creating the config starts a scan of the selected schemas and
        schedules recurring scans.

        :param parent: str
          Name of the catalog to enable, in the format catalogs/{catalog_name}.
        :param catalog_config: :class:`CatalogConfig`
          The configuration to create.

        :returns: :class:`CatalogConfig`
        """

        body = catalog_config.as_dict()
        query = {}
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("POST", f"/api/data-classification/v1/{parent}/config", body=body, headers=headers)
        return CatalogConfig.from_dict(res)

    def delete_catalog_config(self, name: str):
        """Delete Data Classification configuration for a catalog.

        Deleting the config disables Data Classification for the catalog and stops its scheduled scans. Tags
        that auto-tagging already applied to columns are not removed. Deleting a config that does not exist
        succeeds.

        :param name: str
          Resource name of the config, in the format catalogs/{catalog_name}/config.


        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        self._api.do("DELETE", f"/api/data-classification/v1/{name}", headers=headers)

    def get_catalog_config(self, name: str) -> CatalogConfig:
        """Get the Data Classification configuration for a catalog.

        :param name: str
          Resource name of the config, in the format catalogs/{catalog_name}/config.

        :returns: :class:`CatalogConfig`
        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("GET", f"/api/data-classification/v1/{name}", headers=headers)
        return CatalogConfig.from_dict(res)

    def rescan_catalog(self, name: str) -> RescanCatalogResponse:
        """Rescan the tables in a catalog's Data Classification scope that changed since their last scan.

        The rescan uses the catalog's current classifiers and follows its config (schema selection) and SKIP
        tags. Tables with no commits since their last scan are skipped. Views and tables without a Delta
        commit history keep their regular rescan schedule. The call returns once the rescan is scheduled;
        scanning runs in the background. If a scan of the catalog is running, the call cancels it and starts a
        new run.

        - Data Classification must be enabled for the catalog.
        - The call must come from the workspace where Data Classification was enabled.

        :param name: str
          Resource name of the catalog, in the format: catalogs/{catalog_name}.

        :returns: :class:`RescanCatalogResponse`
        """

        body = {}
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("POST", f"/api/data-classification/v1/{name}/rescan", body=body, headers=headers)
        return RescanCatalogResponse.from_dict(res)

    def update_catalog_config(self, name: str, catalog_config: CatalogConfig, update_mask: FieldMask) -> CatalogConfig:
        """Update the Data Classification configuration for a catalog.

        The config must already exist for the catalog. Only the fields named in ``update_mask`` change; the
        other fields keep their current values.

        :param name: str
          Resource name in the format: catalogs/{catalog_name}/config.
        :param catalog_config: :class:`CatalogConfig`
          The configuration to apply to the catalog. The name field in catalog_config identifies which
          resource to update.
        :param update_mask: FieldMask
          Comma-separated list of the fields of catalog_config to update, for example ``included_schemas`` or
          ``auto_tag_configs``.

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
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("PATCH", f"/api/data-classification/v1/{name}", query=query, body=body, headers=headers)
        return CatalogConfig.from_dict(res)
