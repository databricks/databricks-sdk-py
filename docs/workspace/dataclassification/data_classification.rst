``w.data_classification``: DataClassification.v1
================================================
.. currentmodule:: databricks.sdk.service.dataclassification

.. py:class:: DataClassificationAPI

    Manage data classification for Unity Catalog catalogs. Data classification automatically identifies and
    tags sensitive data (PII) in Unity Catalog tables. Each catalog can have at most one configuration
    resource that controls scanning behavior and auto-tagging rules.

    .. py:method:: create_catalog_config(parent: str, catalog_config: CatalogConfig) -> CatalogConfig

        Create Data Classification configuration for a catalog.

        Creates a new config resource, which enables Data Classification for the specified catalog. - The
        config must not already exist for the catalog.

        :param parent: str
          Parent resource in the format: catalogs/{catalog_name}
        :param catalog_config: :class:`CatalogConfig`
          The configuration to create.

        :returns: :class:`CatalogConfig`
        

    .. py:method:: delete_catalog_config(name: str)

        Delete Data Classification configuration for a catalog.

        :param name: str
          Resource name in the format: catalogs/{catalog_name}/config


        

    .. py:method:: get_catalog_config(name: str) -> CatalogConfig

        Get the Data Classification configuration for a catalog.

        :param name: str
          Resource name in the format: catalogs/{catalog_name}/config

        :returns: :class:`CatalogConfig`
        

    .. py:method:: update_catalog_config(name: str, catalog_config: CatalogConfig, update_mask: FieldMask) -> CatalogConfig

        Update the Data Classification configuration for a catalog. - The config must already exist for the
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
        