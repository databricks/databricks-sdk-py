``w.settings.default_warehouse_id``: Default Warehouse Id
=========================================================
.. currentmodule:: databricks.sdk.service.settings

.. py:class:: DefaultWarehouseIdAPI

    Warehouse to be selected by default for users in this workspace. Covers SQL workloads only and can be
    overridden by users.

    .. py:method:: delete( [, etag: Optional[str]]) -> DeleteDefaultWarehouseIdResponse

        Reverts the Default Warehouse Id setting to its default value.
        
        :param etag: str (optional)
          etag used for versioning. The response is at least as fresh as the eTag provided. This is used for
          optimistic concurrency control as a way to help prevent simultaneous writes of a setting overwriting
          each other. It is strongly suggested that systems make use of the etag in the read -> delete pattern
          to perform setting deletions in order to avoid race conditions. That is, get an etag from a GET
          request, and pass it with the DELETE request to identify the rule set version you are deleting.
        
        :returns: :class:`DeleteDefaultWarehouseIdResponse`
        

    .. py:method:: get( [, etag: Optional[str]]) -> DefaultWarehouseId

        Gets the Default Warehouse Id setting.
        
        :param etag: str (optional)
          etag used for versioning. The response is at least as fresh as the eTag provided. This is used for
          optimistic concurrency control as a way to help prevent simultaneous writes of a setting overwriting
          each other. It is strongly suggested that systems make use of the etag in the read -> delete pattern
          to perform setting deletions in order to avoid race conditions. That is, get an etag from a GET
          request, and pass it with the DELETE request to identify the rule set version you are deleting.
        
        :returns: :class:`DefaultWarehouseId`
        

    .. py:method:: update(allow_missing: bool, setting: DefaultWarehouseId, field_mask: str) -> DefaultWarehouseId

        Updates the Default Warehouse Id setting.
        
        :param allow_missing: bool
          This should always be set to true for Settings API. Added for AIP compliance.
        :param setting: :class:`DefaultWarehouseId`
        :param field_mask: str
          The field mask must be a single string, with multiple fields separated by commas (no spaces). The
          field path is relative to the resource object, using a dot (`.`) to navigate sub-fields (e.g.,
          `author.given_name`). Specification of elements in sequence or map fields is not allowed, as only
          the entire collection field can be specified. Field names must exactly match the resource field
          names.
          
          A field mask of `*` indicates full replacement. It’s recommended to always explicitly list the
          fields being updated and avoid using `*` wildcards, as it can lead to unintended results if the API
          changes in the future.
        
        :returns: :class:`DefaultWarehouseId`
        