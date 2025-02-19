``w.settings.default_namespace``: Default Namespace
===================================================
.. currentmodule:: databricks.sdk.service.settings

.. py:class:: DefaultNamespaceAPI

    The default namespace setting API allows users to configure the default namespace for a Databricks
    workspace.
    
    Through this API, users can retrieve, set, or modify the default namespace used when queries do not
    reference a fully qualified three-level name. For example, if you use the API to set 'retail_prod' as the
    default catalog, then a query 'SELECT * FROM myTable' would reference the object
    'retail_prod.default.myTable' (the schema 'default' is always assumed).
    
    This setting requires a restart of clusters and SQL warehouses to take effect. Additionally, the default
    namespace only applies when using Unity Catalog-enabled compute.

    .. py:method:: delete( [, etag: Optional[str]]) -> DeleteDefaultNamespaceSettingResponse

        Delete the default namespace setting.
        
        Deletes the default namespace setting for the workspace. A fresh etag needs to be provided in `DELETE`
        requests (as a query parameter). The etag can be retrieved by making a `GET` request before the
        `DELETE` request. If the setting is updated/deleted concurrently, `DELETE` fails with 409 and the
        request must be retried by using the fresh etag in the 409 response.
        
        :param etag: str (optional)
          etag used for versioning. The response is at least as fresh as the eTag provided. This is used for
          optimistic concurrency control as a way to help prevent simultaneous writes of a setting overwriting
          each other. It is strongly suggested that systems make use of the etag in the read -> delete pattern
          to perform setting deletions in order to avoid race conditions. That is, get an etag from a GET
          request, and pass it with the DELETE request to identify the rule set version you are deleting.
        
        :returns: :class:`DeleteDefaultNamespaceSettingResponse`
        

    .. py:method:: get( [, etag: Optional[str]]) -> DefaultNamespaceSetting

        Get the default namespace setting.
        
        Gets the default namespace setting.
        
        :param etag: str (optional)
          etag used for versioning. The response is at least as fresh as the eTag provided. This is used for
          optimistic concurrency control as a way to help prevent simultaneous writes of a setting overwriting
          each other. It is strongly suggested that systems make use of the etag in the read -> delete pattern
          to perform setting deletions in order to avoid race conditions. That is, get an etag from a GET
          request, and pass it with the DELETE request to identify the rule set version you are deleting.
        
        :returns: :class:`DefaultNamespaceSetting`
        

    .. py:method:: update(allow_missing: bool, setting: DefaultNamespaceSetting, field_mask: str) -> DefaultNamespaceSetting

        Update the default namespace setting.
        
        Updates the default namespace setting for the workspace. A fresh etag needs to be provided in `PATCH`
        requests (as part of the setting field). The etag can be retrieved by making a `GET` request before
        the `PATCH` request. Note that if the setting does not exist, `GET` returns a NOT_FOUND error and the
        etag is present in the error response, which should be set in the `PATCH` request. If the setting is
        updated concurrently, `PATCH` fails with 409 and the request must be retried by using the fresh etag
        in the 409 response.
        
        :param allow_missing: bool
          This should always be set to true for Settings API. Added for AIP compliance.
        :param setting: :class:`DefaultNamespaceSetting`
          This represents the setting configuration for the default namespace in the Databricks workspace.
          Setting the default catalog for the workspace determines the catalog that is used when queries do
          not reference a fully qualified 3 level name. For example, if the default catalog is set to
          'retail_prod' then a query 'SELECT * FROM myTable' would reference the object
          'retail_prod.default.myTable' (the schema 'default' is always assumed). This setting requires a
          restart of clusters and SQL warehouses to take effect. Additionally, the default namespace only
          applies when using Unity Catalog-enabled compute.
        :param field_mask: str
          The field mask must be a single string, with multiple fields separated by commas (no spaces). The
          field path is relative to the resource object, using a dot (`.`) to navigate sub-fields (e.g.,
          `author.given_name`). Specification of elements in sequence or map fields is not allowed, as only
          the entire collection field can be specified. Field names must exactly match the resource field
          names.
          
          A field mask of `*` indicates full replacement. It’s recommended to always explicitly list the
          fields being updated and avoid using `*` wildcards, as it can lead to unintended results if the API
          changes in the future.
        
        :returns: :class:`DefaultNamespaceSetting`
        