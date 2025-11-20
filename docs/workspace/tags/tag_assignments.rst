``w.tag_assignments``: Tag Assignments
======================================
.. currentmodule:: databricks.sdk.service.tags

.. py:class:: TagAssignmentsAPI

    Manage tag assignments on workspace-scoped objects.

    .. py:method:: create_tag_assignment(tag_assignment: TagAssignment) -> TagAssignment

        Create a tag assignment

        :param tag_assignment: :class:`TagAssignment`

        :returns: :class:`TagAssignment`
        

    .. py:method:: delete_tag_assignment(entity_type: str, entity_id: str, tag_key: str)

        Delete a tag assignment

        :param entity_type: str
          The type of entity to which the tag is assigned. Allowed value is dashboards
        :param entity_id: str
          The identifier of the entity to which the tag is assigned
        :param tag_key: str
          The key of the tag. The characters , . : / - = and leading/trailing spaces are not allowed


        

    .. py:method:: get_tag_assignment(entity_type: str, entity_id: str, tag_key: str) -> TagAssignment

        Get a tag assignment

        :param entity_type: str
          The type of entity to which the tag is assigned. Allowed value is dashboards
        :param entity_id: str
          The identifier of the entity to which the tag is assigned
        :param tag_key: str
          The key of the tag. The characters , . : / - = and leading/trailing spaces are not allowed

        :returns: :class:`TagAssignment`
        

    .. py:method:: list_tag_assignments(entity_type: str, entity_id: str [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[TagAssignment]

        List the tag assignments for an entity

        :param entity_type: str
          The type of entity to which the tag is assigned. Allowed value is dashboards
        :param entity_id: str
          The identifier of the entity to which the tag is assigned
        :param page_size: int (optional)
          Optional. Maximum number of tag assignments to return in a single page
        :param page_token: str (optional)
          Pagination token to go to the next page of tag assignments. Requests first page if absent.

        :returns: Iterator over :class:`TagAssignment`
        

    .. py:method:: update_tag_assignment(entity_type: str, entity_id: str, tag_key: str, tag_assignment: TagAssignment, update_mask: str) -> TagAssignment

        Update a tag assignment

        :param entity_type: str
          The type of entity to which the tag is assigned. Allowed value is dashboards
        :param entity_id: str
          The identifier of the entity to which the tag is assigned
        :param tag_key: str
          The key of the tag. The characters , . : / - = and leading/trailing spaces are not allowed
        :param tag_assignment: :class:`TagAssignment`
        :param update_mask: str
          The field mask must be a single string, with multiple fields separated by commas (no spaces). The
          field path is relative to the resource object, using a dot (`.`) to navigate sub-fields (e.g.,
          `author.given_name`). Specification of elements in sequence or map fields is not allowed, as only
          the entire collection field can be specified. Field names must exactly match the resource field
          names.

          A field mask of `*` indicates full replacement. It’s recommended to always explicitly list the
          fields being updated and avoid using `*` wildcards, as it can lead to unintended results if the API
          changes in the future.

        :returns: :class:`TagAssignment`
        