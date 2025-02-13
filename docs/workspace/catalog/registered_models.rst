``w.registered_models``: Registered Models
==========================================
.. currentmodule:: databricks.sdk.service.catalog

.. py:class:: RegisteredModelsAPI

    Databricks provides a hosted version of MLflow Model Registry in Unity Catalog. Models in Unity Catalog
    provide centralized access control, auditing, lineage, and discovery of ML models across Databricks
    workspaces.
    
    An MLflow registered model resides in the third layer of Unity Catalog’s three-level namespace.
    Registered models contain model versions, which correspond to actual ML models (MLflow models). Creating
    new model versions currently requires use of the MLflow Python client. Once model versions are created,
    you can load them for batch inference using MLflow Python client APIs, or deploy them for real-time
    serving using Databricks Model Serving.
    
    All operations on registered models and model versions require USE_CATALOG permissions on the enclosing
    catalog and USE_SCHEMA permissions on the enclosing schema. In addition, the following additional
    privileges are required for various operations:
    
    * To create a registered model, users must additionally have the CREATE_MODEL permission on the target
    schema. * To view registered model or model version metadata, model version data files, or invoke a model
    version, users must additionally have the EXECUTE permission on the registered model * To update
    registered model or model version tags, users must additionally have APPLY TAG permissions on the
    registered model * To update other registered model or model version metadata (comments, aliases) create a
    new model version, or update permissions on the registered model, users must be owners of the registered
    model.
    
    Note: The securable type for models is "FUNCTION". When using REST APIs (e.g. tagging, grants) that
    specify a securable type, use "FUNCTION" as the securable type.

    .. py:method:: create(catalog_name: str, schema_name: str, name: str [, comment: Optional[str], storage_location: Optional[str]]) -> RegisteredModelInfo

        Create a Registered Model.
        
        Creates a new registered model in Unity Catalog.
        
        File storage for model versions in the registered model will be located in the default location which
        is specified by the parent schema, or the parent catalog, or the Metastore.
        
        For registered model creation to succeed, the user must satisfy the following conditions: - The caller
        must be a metastore admin, or be the owner of the parent catalog and schema, or have the
        **USE_CATALOG** privilege on the parent catalog and the **USE_SCHEMA** privilege on the parent schema.
        - The caller must have the **CREATE MODEL** or **CREATE FUNCTION** privilege on the parent schema.
        
        :param catalog_name: str
          The name of the catalog where the schema and the registered model reside
        :param schema_name: str
          The name of the schema where the registered model resides
        :param name: str
          The name of the registered model
        :param comment: str (optional)
          The comment attached to the registered model
        :param storage_location: str (optional)
          The storage location on the cloud under which model version data files are stored
        
        :returns: :class:`RegisteredModelInfo`
        

    .. py:method:: delete(full_name: str)

        Delete a Registered Model.
        
        Deletes a registered model and all its model versions from the specified parent catalog and schema.
        
        The caller must be a metastore admin or an owner of the registered model. For the latter case, the
        caller must also be the owner or have the **USE_CATALOG** privilege on the parent catalog and the
        **USE_SCHEMA** privilege on the parent schema.
        
        :param full_name: str
          The three-level (fully qualified) name of the registered model
        
        
        

    .. py:method:: delete_alias(full_name: str, alias: str)

        Delete a Registered Model Alias.
        
        Deletes a registered model alias.
        
        The caller must be a metastore admin or an owner of the registered model. For the latter case, the
        caller must also be the owner or have the **USE_CATALOG** privilege on the parent catalog and the
        **USE_SCHEMA** privilege on the parent schema.
        
        :param full_name: str
          The three-level (fully qualified) name of the registered model
        :param alias: str
          The name of the alias
        
        
        

    .. py:method:: get(full_name: str [, include_aliases: Optional[bool], include_browse: Optional[bool]]) -> RegisteredModelInfo

        Get a Registered Model.
        
        Get a registered model.
        
        The caller must be a metastore admin or an owner of (or have the **EXECUTE** privilege on) the
        registered model. For the latter case, the caller must also be the owner or have the **USE_CATALOG**
        privilege on the parent catalog and the **USE_SCHEMA** privilege on the parent schema.
        
        :param full_name: str
          The three-level (fully qualified) name of the registered model
        :param include_aliases: bool (optional)
          Whether to include registered model aliases in the response
        :param include_browse: bool (optional)
          Whether to include registered models in the response for which the principal can only access
          selective metadata for
        
        :returns: :class:`RegisteredModelInfo`
        

    .. py:method:: list( [, catalog_name: Optional[str], include_browse: Optional[bool], max_results: Optional[int], page_token: Optional[str], schema_name: Optional[str]]) -> Iterator[RegisteredModelInfo]

        List Registered Models.
        
        List registered models. You can list registered models under a particular schema, or list all
        registered models in the current metastore.
        
        The returned models are filtered based on the privileges of the calling user. For example, the
        metastore admin is able to list all the registered models. A regular user needs to be the owner or
        have the **EXECUTE** privilege on the registered model to recieve the registered models in the
        response. For the latter case, the caller must also be the owner or have the **USE_CATALOG** privilege
        on the parent catalog and the **USE_SCHEMA** privilege on the parent schema.
        
        There is no guarantee of a specific ordering of the elements in the response.
        
        :param catalog_name: str (optional)
          The identifier of the catalog under which to list registered models. If specified, schema_name must
          be specified.
        :param include_browse: bool (optional)
          Whether to include registered models in the response for which the principal can only access
          selective metadata for
        :param max_results: int (optional)
          Max number of registered models to return.
          
          If both catalog and schema are specified: - when max_results is not specified, the page length is
          set to a server configured value (10000, as of 4/2/2024). - when set to a value greater than 0, the
          page length is the minimum of this value and a server configured value (10000, as of 4/2/2024); -
          when set to 0, the page length is set to a server configured value (10000, as of 4/2/2024); - when
          set to a value less than 0, an invalid parameter error is returned;
          
          If neither schema nor catalog is specified: - when max_results is not specified, the page length is
          set to a server configured value (100, as of 4/2/2024). - when set to a value greater than 0, the
          page length is the minimum of this value and a server configured value (1000, as of 4/2/2024); -
          when set to 0, the page length is set to a server configured value (100, as of 4/2/2024); - when set
          to a value less than 0, an invalid parameter error is returned;
        :param page_token: str (optional)
          Opaque token to send for the next page of results (pagination).
        :param schema_name: str (optional)
          The identifier of the schema under which to list registered models. If specified, catalog_name must
          be specified.
        
        :returns: Iterator over :class:`RegisteredModelInfo`
        

    .. py:method:: set_alias(full_name: str, alias: str, version_num: int) -> RegisteredModelAlias

        Set a Registered Model Alias.
        
        Set an alias on the specified registered model.
        
        The caller must be a metastore admin or an owner of the registered model. For the latter case, the
        caller must also be the owner or have the **USE_CATALOG** privilege on the parent catalog and the
        **USE_SCHEMA** privilege on the parent schema.
        
        :param full_name: str
          Full name of the registered model
        :param alias: str
          The name of the alias
        :param version_num: int
          The version number of the model version to which the alias points
        
        :returns: :class:`RegisteredModelAlias`
        

    .. py:method:: update(full_name: str [, comment: Optional[str], new_name: Optional[str], owner: Optional[str]]) -> RegisteredModelInfo

        Update a Registered Model.
        
        Updates the specified registered model.
        
        The caller must be a metastore admin or an owner of the registered model. For the latter case, the
        caller must also be the owner or have the **USE_CATALOG** privilege on the parent catalog and the
        **USE_SCHEMA** privilege on the parent schema.
        
        Currently only the name, the owner or the comment of the registered model can be updated.
        
        :param full_name: str
          The three-level (fully qualified) name of the registered model
        :param comment: str (optional)
          The comment attached to the registered model
        :param new_name: str (optional)
          New name for the registered model.
        :param owner: str (optional)
          The identifier of the user who owns the registered model
        
        :returns: :class:`RegisteredModelInfo`
        