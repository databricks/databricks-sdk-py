``w.data_classification``: DataClassification.v1
================================================
.. currentmodule:: databricks.sdk.service.dataclassification

.. py:class:: DataClassificationAPI

    Manage data classification for Unity Catalog catalogs. Data classification automatically identifies and
    tags sensitive data (PII) in Unity Catalog tables. Each catalog can have at most one configuration
    resource that controls scanning behavior and auto-tagging rules.

    .. py:method:: create_catalog_config(parent: str, catalog_config: CatalogConfig) -> CatalogConfig

        Create Data Classification configuration for a catalog.

        Creates a new config resource, which enables Data Classification for the specified catalog. The
        catalog must not already have a config. Creating the config starts a scan of the selected schemas and
        schedules recurring scans.

        :param parent: str
          Name of the catalog to enable, in the format catalogs/{catalog_name}.
        :param catalog_config: :class:`CatalogConfig`
          The configuration to create.

        :returns: :class:`CatalogConfig`
        

    .. py:method:: delete_catalog_config(name: str)

        Delete Data Classification configuration for a catalog.

        Deleting the config disables Data Classification for the catalog and stops its scheduled scans. Tags
        that auto-tagging already applied to columns are not removed. Deleting a config that does not exist
        succeeds.

        :param name: str
          Resource name of the config, in the format catalogs/{catalog_name}/config.


        

    .. py:method:: get_catalog_config(name: str) -> CatalogConfig

        Get the Data Classification configuration for a catalog.

        :param name: str
          Resource name of the config, in the format catalogs/{catalog_name}/config.

        :returns: :class:`CatalogConfig`
        

    .. py:method:: rescan_catalog(name: str) -> RescanCatalogResponse

        Rescan the tables in a catalog's Data Classification scope that changed since their last scan.

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
        

    .. py:method:: update_catalog_config(name: str, catalog_config: CatalogConfig, update_mask: FieldMask) -> CatalogConfig

        Update the Data Classification configuration for a catalog.

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
        