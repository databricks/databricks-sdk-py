``w.entity_tag_assignments``: Entity Tag Assignments
====================================================
.. currentmodule:: databricks.sdk.service.catalog

.. py:class:: EntityTagAssignmentsAPI

    Tags are attributes that include keys and optional values that you can use to organize and categorize
    entities in Unity Catalog. Entity tagging is currently supported on catalogs, schemas, tables (including
    views), columns, volumes. With these APIs, users can create, update, delete, and list tag assignments
    across Unity Catalog entities

    .. py:method:: create(tag_assignment: EntityTagAssignment) -> EntityTagAssignment

        Creates a tag assignment for an Unity Catalog entity.

        To add tags to Unity Catalog entities, you must own the entity or have the following privileges: -
        **APPLY TAG** on the entity - **USE SCHEMA** on the entity's parent schema - **USE CATALOG** on the
        entity's parent catalog

        To add a governed tag to Unity Catalog entities, you must also have the **ASSIGN** or **MANAGE**
        permission on the tag policy. See [Manage tag policy permissions].

        [Manage tag policy permissions]: https://docs.databricks.com/aws/en/admin/tag-policies/manage-permissions

        :param tag_assignment: :class:`EntityTagAssignment`

        :returns: :class:`EntityTagAssignment`
        

    .. py:method:: delete(entity_type: str, entity_name: str, tag_key: str)

        Deletes a tag assignment for an Unity Catalog entity by its key.

        To delete tags from Unity Catalog entities, you must own the entity or have the following privileges:
        - **APPLY TAG** on the entity - **USE_SCHEMA** on the entity's parent schema - **USE_CATALOG** on the
        entity's parent catalog

        To delete a governed tag from Unity Catalog entities, you must also have the **ASSIGN** or **MANAGE**
        permission on the tag policy. See [Manage tag policy permissions].

        [Manage tag policy permissions]: https://docs.databricks.com/aws/en/admin/tag-policies/manage-permissions

        :param entity_type: str
          The type of the entity to which the tag is assigned. Allowed values are: catalogs, schemas, tables,
          columns, volumes.
        :param entity_name: str
          The fully qualified name of the entity to which the tag is assigned
        :param tag_key: str
          Required. The key of the tag to delete


        

    .. py:method:: get(entity_type: str, entity_name: str, tag_key: str) -> EntityTagAssignment

        Gets a tag assignment for an Unity Catalog entity by tag key.

        :param entity_type: str
          The type of the entity to which the tag is assigned. Allowed values are: catalogs, schemas, tables,
          columns, volumes.
        :param entity_name: str
          The fully qualified name of the entity to which the tag is assigned
        :param tag_key: str
          Required. The key of the tag

        :returns: :class:`EntityTagAssignment`
        

    .. py:method:: list(entity_type: str, entity_name: str [, max_results: Optional[int], page_token: Optional[str]]) -> Iterator[EntityTagAssignment]

        List tag assignments for an Unity Catalog entity

        :param entity_type: str
          The type of the entity to which the tag is assigned. Allowed values are: catalogs, schemas, tables,
          columns, volumes.
        :param entity_name: str
          The fully qualified name of the entity to which the tag is assigned
        :param max_results: int (optional)
          Optional. Maximum number of tag assignments to return in a single page
        :param page_token: str (optional)
          Optional. Pagination token to retrieve the next page of results

        :returns: Iterator over :class:`EntityTagAssignment`
        

    .. py:method:: update(entity_type: str, entity_name: str, tag_key: str, tag_assignment: EntityTagAssignment, update_mask: str) -> EntityTagAssignment

        Updates an existing tag assignment for an Unity Catalog entity.

        To update tags to Unity Catalog entities, you must own the entity or have the following privileges: -
        **APPLY TAG** on the entity - **USE SCHEMA** on the entity's parent schema - **USE CATALOG** on the
        entity's parent catalog

        To update a governed tag to Unity Catalog entities, you must also have the **ASSIGN** or **MANAGE**
        permission on the tag policy. See [Manage tag policy permissions].

        [Manage tag policy permissions]: https://docs.databricks.com/aws/en/admin/tag-policies/manage-permissions

        :param entity_type: str
          The type of the entity to which the tag is assigned. Allowed values are: catalogs, schemas, tables,
          columns, volumes.
        :param entity_name: str
          The fully qualified name of the entity to which the tag is assigned
        :param tag_key: str
          The key of the tag
        :param tag_assignment: :class:`EntityTagAssignment`
        :param update_mask: str
          The field mask must be a single string, with multiple fields separated by commas (no spaces). The
          field path is relative to the resource object, using a dot (`.`) to navigate sub-fields (e.g.,
          `author.given_name`). Specification of elements in sequence or map fields is not allowed, as only
          the entire collection field can be specified. Field names must exactly match the resource field
          names.

          A field mask of `*` indicates full replacement. It’s recommended to always explicitly list the
          fields being updated and avoid using `*` wildcards, as it can lead to unintended results if the API
          changes in the future.

        :returns: :class:`EntityTagAssignment`
        