Artifact Allowlists
===================
.. py:class:: ArtifactAllowlistsAPI

    In Databricks Runtime 13.3 and above, you can add libraries and init scripts to the `allowlist` in UC so
    that users can leverage these artifacts on compute configured with shared access mode.

    .. py:method:: get(artifact_type)

        Get an artifact allowlist.
        
        Get the artifact allowlist of a certain artifact type. The caller must be a metastore admin or have
        the **MANAGE ALLOWLIST** privilege on the metastore.
        
        :param artifact_type: :class:`ArtifactType`
          The artifact type of the allowlist.
        
        :returns: :class:`ArtifactAllowlistInfo`
        

    .. py:method:: update(artifact_type, artifact_matchers)

        Set an artifact allowlist.
        
        Set the artifact allowlist of a certain artifact type. The whole artifact allowlist is replaced with
        the new allowlist. The caller must be a metastore admin or have the **MANAGE ALLOWLIST** privilege on
        the metastore.
        
        :param artifact_type: :class:`ArtifactType`
          The artifact type of the allowlist.
        :param artifact_matchers: List[:class:`ArtifactMatcher`]
          A list of allowed artifact match patterns.
        
        :returns: :class:`ArtifactAllowlistInfo`
        