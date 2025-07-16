``w.external_lineage``: External Lineage
========================================
.. currentmodule:: databricks.sdk.service.catalog

.. py:class:: ExternalLineageAPI

    External Lineage APIs enable defining and managing lineage relationships between Databricks objects and
    external systems. These APIs allow users to capture data flows connecting Databricks tables, models, and
    file paths with external metadata objects.

    With these APIs, users can create, update, delete, and list lineage relationships with support for
    column-level mappings and custom properties.

    .. py:method:: create_external_lineage_relationship(external_lineage_relationship: CreateRequestExternalLineage) -> ExternalLineageRelationship

        Creates an external lineage relationship between a Databricks or external metadata object and another
        external metadata object.

        :param external_lineage_relationship: :class:`CreateRequestExternalLineage`

        :returns: :class:`ExternalLineageRelationship`
        

    .. py:method:: delete_external_lineage_relationship(external_lineage_relationship: DeleteRequestExternalLineage)

        Deletes an external lineage relationship between a Databricks or external metadata object and another
        external metadata object.

        :param external_lineage_relationship: :class:`DeleteRequestExternalLineage`


        

    .. py:method:: list_external_lineage_relationships(object_info: ExternalLineageObject, lineage_direction: LineageDirection [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[ExternalLineageInfo]

        Lists external lineage relationships of a Databricks object or external metadata given a supplied
        direction.

        :param object_info: :class:`ExternalLineageObject`
          The object to query external lineage relationships for. Since this field is a query parameter,
          please flatten the nested fields. For example, if the object is a table, the query parameter should
          look like: `object_info.table.name=main.sales.customers`
        :param lineage_direction: :class:`LineageDirection`
          The lineage direction to filter on.
        :param page_size: int (optional)
          Specifies the maximum number of external lineage relationships to return in a single response. The
          value must be less than or equal to 1000.
        :param page_token: str (optional)
          Opaque pagination token to go to next page based on previous query.

        :returns: Iterator over :class:`ExternalLineageInfo`
        

    .. py:method:: update_external_lineage_relationship(external_lineage_relationship: UpdateRequestExternalLineage, update_mask: str) -> ExternalLineageRelationship

        Updates an external lineage relationship between a Databricks or external metadata object and another
        external metadata object.

        :param external_lineage_relationship: :class:`UpdateRequestExternalLineage`
        :param update_mask: str
          The field mask must be a single string, with multiple fields separated by commas (no spaces). The
          field path is relative to the resource object, using a dot (`.`) to navigate sub-fields (e.g.,
          `author.given_name`). Specification of elements in sequence or map fields is not allowed, as only
          the entire collection field can be specified. Field names must exactly match the resource field
          names.

          A field mask of `*` indicates full replacement. It’s recommended to always explicitly list the
          fields being updated and avoid using `*` wildcards, as it can lead to unintended results if the API
          changes in the future.

        :returns: :class:`ExternalLineageRelationship`
        