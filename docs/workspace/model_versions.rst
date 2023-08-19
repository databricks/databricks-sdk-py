Model Versions
==============
.. py:class:: ModelVersionsAPI

    Databricks provides a hosted version of MLflow Model Registry in Unity Catalog. Models in Unity Catalog
    provide centralized access control, auditing, lineage, and discovery of ML models across Databricks
    workspaces.
    
    This API reference documents the REST endpoints for managing model versions in Unity Catalog. For more
    details, see the [registered models API docs](/api/workspace/registeredmodels).

    .. py:method:: delete(full_name, version)

        Delete a Model Version.
        
        Deletes a model version from the specified registered model. Any aliases assigned to the model version
        will also be deleted.
        
        The caller must be a metastore admin or an owner of the parent registered model. For the latter case,
        the caller must also be the owner or have the **USE_CATALOG** privilege on the parent catalog and the
        **USE_SCHEMA** privilege on the parent schema.
        
        :param full_name: str
          The three-level (fully qualified) name of the model version
        :param version: int
          The integer version number of the model version
        
        
        

    .. py:method:: get(full_name, version)

        Get a Model Version.
        
        Get a model version.
        
        The caller must be a metastore admin or an owner of (or have the **EXECUTE** privilege on) the parent
        registered model. For the latter case, the caller must also be the owner or have the **USE_CATALOG**
        privilege on the parent catalog and the **USE_SCHEMA** privilege on the parent schema.
        
        :param full_name: str
          The three-level (fully qualified) name of the model version
        :param version: int
          The integer version number of the model version
        
        :returns: :class:`RegisteredModelInfo`
        

    .. py:method:: list(full_name [, max_results, page_token])

        List Model Versions.
        
        List model versions. You can list model versions under a particular schema, or list all model versions
        in the current metastore.
        
        The returned models are filtered based on the privileges of the calling user. For example, the
        metastore admin is able to list all the model versions. A regular user needs to be the owner or have
        the **EXECUTE** privilege on the parent registered model to recieve the model versions in the
        response. For the latter case, the caller must also be the owner or have the **USE_CATALOG** privilege
        on the parent catalog and the **USE_SCHEMA** privilege on the parent schema.
        
        There is no guarantee of a specific ordering of the elements in the response.
        
        :param full_name: str
          The full three-level name of the registered model under which to list model versions
        :param max_results: int (optional)
          Max number of model versions to return
        :param page_token: str (optional)
          Opaque token to send for the next page of results (pagination).
        
        :returns: Iterator over :class:`ModelVersionInfo`
        

    .. py:method:: update(full_name, version [, comment])

        Update a Model Version.
        
        Updates the specified model version.
        
        The caller must be a metastore admin or an owner of the parent registered model. For the latter case,
        the caller must also be the owner or have the **USE_CATALOG** privilege on the parent catalog and the
        **USE_SCHEMA** privilege on the parent schema.
        
        Currently only the comment of the model version can be updated.
        
        :param full_name: str
          The three-level (fully qualified) name of the model version
        :param version: int
          The integer version number of the model version
        :param comment: str (optional)
          The comment attached to the model version
        
        :returns: :class:`ModelVersionInfo`
        