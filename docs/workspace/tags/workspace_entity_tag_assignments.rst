``w.workspace_entity_tag_assignments``: Tag Assignments
=======================================================
.. currentmodule:: databricks.sdk.service.tags

.. py:class:: WorkspaceEntityTagAssignmentsAPI

    Manage tag assignments on workspace-scoped objects.

    .. py:method:: create_tag_assignment(tag_assignment: TagAssignment) -> TagAssignment

        Create a tag assignment

        :param tag_assignment: :class:`TagAssignment`

        :returns: :class:`TagAssignment`
        

    .. py:method:: delete_tag_assignment(entity_type: str, entity_id: str, tag_key: str)

        Delete a tag assignment

        :param entity_type: str
          The type of entity to which the tag is assigned. Allowed values are apps, dashboards, geniespaces,
          notebooks
        :param entity_id: str
          The identifier of the entity to which the tag is assigned. For apps, the entity_id is the app name
        :param tag_key: str
          The key of the tag. The characters , . : / - = and leading/trailing spaces are not allowed


        

    .. py:method:: get_tag_assignment(entity_type: str, entity_id: str, tag_key: str) -> TagAssignment

        Get a tag assignment

        :param entity_type: str
          The type of entity to which the tag is assigned. Allowed values are apps, dashboards, geniespaces,
          notebooks
        :param entity_id: str
          The identifier of the entity to which the tag is assigned. For apps, the entity_id is the app name
        :param tag_key: str
          The key of the tag. The characters , . : / - = and leading/trailing spaces are not allowed

        :returns: :class:`TagAssignment`
        

    .. py:method:: list_tag_assignments(entity_type: str, entity_id: str [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[TagAssignment]

        List the tag assignments for an entity

        :param entity_type: str
          The type of entity to which the tag is assigned. Allowed values are apps, dashboards, geniespaces,
          notebooks
        :param entity_id: str
          The identifier of the entity to which the tag is assigned. For apps, the entity_id is the app name
        :param page_size: int (optional)
          Optional. Maximum number of tag assignments to return in a single page
        :param page_token: str (optional)
          Pagination token to go to the next page of tag assignments. Requests first page if absent.

        :returns: Iterator over :class:`TagAssignment`
        

    .. py:method:: update_tag_assignment(entity_type: str, entity_id: str, tag_key: str, tag_assignment: TagAssignment, update_mask: str) -> TagAssignment

        Update a tag assignment

        :param entity_type: str
          The type of entity to which the tag is assigned. Allowed values are apps, dashboards, geniespaces,
          notebooks
        :param entity_id: str
          The identifier of the entity to which the tag is assigned. For apps, the entity_id is the app name
        :param tag_key: str
          The key of the tag. The characters , . : / - = and leading/trailing spaces are not allowed
        :param tag_assignment: :class:`TagAssignment`
        :param update_mask: str
          The comma-separated list of fields to update. Only ``tag_value`` can be updated, because the entity
          type, entity ID and tag key identify the tag assignment.

        :returns: :class:`TagAssignment`
        