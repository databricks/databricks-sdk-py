``w.external_metadata``: External Metadata
==========================================
.. currentmodule:: databricks.sdk.service.catalog

.. py:class:: ExternalMetadataAPI

    External Metadata objects enable customers to register and manage metadata about external systems within
    Unity Catalog.

    These APIs provide a standardized way to create, update, retrieve, list, and delete external metadata
    objects. Fine-grained authorization ensures that only users with appropriate permissions can view and
    manage external metadata objects.

    .. py:method:: create_external_metadata(external_metadata: ExternalMetadata) -> ExternalMetadata

        Creates a new external metadata object in the parent metastore if the caller is a metastore admin or
        has the **CREATE_EXTERNAL_METADATA** privilege. Grants **BROWSE** to all account users upon creation
        by default.

        :param external_metadata: :class:`ExternalMetadata`

        :returns: :class:`ExternalMetadata`
        

    .. py:method:: delete_external_metadata(name: str)

        Deletes the external metadata object that matches the supplied name. The caller must be a metastore
        admin, the owner of the external metadata object, or a user that has the **MANAGE** privilege.

        :param name: str


        

    .. py:method:: get_external_metadata(name: str) -> ExternalMetadata

        Gets the specified external metadata object in a metastore. The caller must be a metastore admin, the
        owner of the external metadata object, or a user that has the **BROWSE** privilege.

        :param name: str

        :returns: :class:`ExternalMetadata`
        

    .. py:method:: list_external_metadata( [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[ExternalMetadata]

        Gets an array of external metadata objects in the metastore. If the caller is the metastore admin, all
        external metadata objects will be retrieved. Otherwise, only external metadata objects that the caller
        has **BROWSE** on will be retrieved. There is no guarantee of a specific ordering of the elements in
        the array.

        :param page_size: int (optional)
          Specifies the maximum number of external metadata objects to return in a single response. The value
          must be less than or equal to 1000.
        :param page_token: str (optional)
          Opaque pagination token to go to next page based on previous query.

        :returns: Iterator over :class:`ExternalMetadata`
        

    .. py:method:: update_external_metadata(name: str, external_metadata: ExternalMetadata, update_mask: str) -> ExternalMetadata

        Updates the external metadata object that matches the supplied name. The caller can only update either
        the owner or other metadata fields in one request. The caller must be a metastore admin, the owner of
        the external metadata object, or a user that has the **MODIFY** privilege. If the caller is updating
        the owner, they must also have the **MANAGE** privilege.

        :param name: str
          Name of the external metadata object.
        :param external_metadata: :class:`ExternalMetadata`
        :param update_mask: str
          The field mask must be a single string, with multiple fields separated by commas (no spaces). The
          field path is relative to the resource object, using a dot (`.`) to navigate sub-fields (e.g.,
          `author.given_name`). Specification of elements in sequence or map fields is not allowed, as only
          the entire collection field can be specified. Field names must exactly match the resource field
          names.

          A field mask of `*` indicates full replacement. It’s recommended to always explicitly list the
          fields being updated and avoid using `*` wildcards, as it can lead to unintended results if the API
          changes in the future.

        :returns: :class:`ExternalMetadata`
        