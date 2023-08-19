Securable Tags
==============
.. py:class:: SecurableTagsAPI

    Tags are attributes containing keys and values that can be applied to different entities in Unity Catalog.
    Tags are useful for organizing and categorizing different entities within a metastore. SecurableTags are
    attached to Unity Catalog securable entities.

    .. py:method:: list(securable_type, full_name)

        Get tags for a securable.
        
        Gets tag assignments for an entity. The caller must be either the owner of the securable, or a
        metastore admin, or have at least USE / SELECT privilege on the associated securable.
        
        :param securable_type: :class:`ListSecurableType`
          The type of the unity catalog securable entity.
        :param full_name: str
          The fully qualified name of the unity catalog securable entity.
        
        :returns: Iterator over :class:`TagSecurableAssignment`
        

    .. py:method:: update(changes, securable_type, full_name)

        Update tags for a securable.
        
        Update tag assignments for an entity The caller must be either the owner of the securable, or a
        metastore admin, or have at least USE / SELECT and APPLY_TAG privilege on the associated securable.
        
        :param changes: :class:`TagChanges`
          Desired changes to be made to the tag assignments on the entity
        :param securable_type: :class:`UpdateSecurableType`
          The type of the unity catalog securable entity.
        :param full_name: str
          The fully qualified name of the unity catalog securable entity.
        
        :returns: :class:`TagSecurableAssignmentsList`
        