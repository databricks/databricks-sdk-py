``w.model_versions``: Model Versions
====================================
.. currentmodule:: databricks.sdk.service.catalog

.. py:class:: ModelVersionsAPI

    Databricks provides a hosted version of MLflow Model Registry in Unity Catalog. Models in Unity Catalog
    provide centralized access control, auditing, lineage, and discovery of ML models across Databricks
    workspaces.

    This API reference documents the REST endpoints for managing model versions in Unity Catalog. For more
    details, see the [registered models API docs](/api/workspace/registeredmodels).

    .. py:method:: delete(full_name: str, version: int)

        Deletes a model version from the specified registered model. Any aliases assigned to the model version
        will also be deleted.

        The caller must be a metastore admin or an owner of the parent registered model. For the latter case,
        the caller must also be the owner or have the **USE_CATALOG** privilege on the parent catalog and the
        **USE_SCHEMA** privilege on the parent schema.

        :param full_name: str
          The three-level (fully qualified) name of the model version
        :param version: int
          The integer version number of the model version


        

    .. py:method:: get(full_name: str, version: int [, include_aliases: Optional[bool], include_browse: Optional[bool]]) -> ModelVersionInfo

        Get a model version.

        The caller must be a metastore admin or an owner of (or have the **EXECUTE** privilege on) the parent
        registered model. For the latter case, the caller must also be the owner or have the **USE_CATALOG**
        privilege on the parent catalog and the **USE_SCHEMA** privilege on the parent schema.

        :param full_name: str
          The three-level (fully qualified) name of the model version
        :param version: int
          The integer version number of the model version
        :param include_aliases: bool (optional)
          Whether to include aliases associated with the model version in the response
        :param include_browse: bool (optional)
          Whether to include model versions in the response for which the principal can only access selective
          metadata for

        :returns: :class:`ModelVersionInfo`
        

    .. py:method:: get_by_alias(full_name: str, alias: str [, include_aliases: Optional[bool]]) -> ModelVersionInfo

        Get a model version by alias.

        The caller must be a metastore admin or an owner of (or have the **EXECUTE** privilege on) the
        registered model. For the latter case, the caller must also be the owner or have the **USE_CATALOG**
        privilege on the parent catalog and the **USE_SCHEMA** privilege on the parent schema.

        :param full_name: str
          The three-level (fully qualified) name of the registered model
        :param alias: str
          The name of the alias
        :param include_aliases: bool (optional)
          Whether to include aliases associated with the model version in the response

        :returns: :class:`ModelVersionInfo`
        

    .. py:method:: list(full_name: str [, include_browse: Optional[bool], max_results: Optional[int], page_token: Optional[str]]) -> Iterator[ModelVersionInfo]

        List model versions. You can list model versions under a particular schema, or list all model versions
        in the current metastore.

        The returned models are filtered based on the privileges of the calling user. For example, the
        metastore admin is able to list all the model versions. A regular user needs to be the owner or have
        the **EXECUTE** privilege on the parent registered model to recieve the model versions in the
        response. For the latter case, the caller must also be the owner or have the **USE_CATALOG** privilege
        on the parent catalog and the **USE_SCHEMA** privilege on the parent schema.

        There is no guarantee of a specific ordering of the elements in the response. The elements in the
        response will not contain any aliases or tags.

        :param full_name: str
          The full three-level name of the registered model under which to list model versions
        :param include_browse: bool (optional)
          Whether to include model versions in the response for which the principal can only access selective
          metadata for
        :param max_results: int (optional)
          Maximum number of model versions to return. If not set, the page length is set to a server
          configured value (100, as of 1/3/2024). - when set to a value greater than 0, the page length is the
          minimum of this value and a server configured value(1000, as of 1/3/2024); - when set to 0, the page
          length is set to a server configured value (100, as of 1/3/2024) (recommended); - when set to a
          value less than 0, an invalid parameter error is returned;
        :param page_token: str (optional)
          Opaque pagination token to go to next page based on previous query.

        :returns: Iterator over :class:`ModelVersionInfo`
        

    .. py:method:: update(full_name: str, version: int [, aliases: Optional[List[RegisteredModelAlias]], catalog_name: Optional[str], comment: Optional[str], created_at: Optional[int], created_by: Optional[str], id: Optional[str], metastore_id: Optional[str], model_name: Optional[str], model_version_dependencies: Optional[DependencyList], run_id: Optional[str], run_workspace_id: Optional[int], schema_name: Optional[str], source: Optional[str], status: Optional[ModelVersionInfoStatus], storage_location: Optional[str], updated_at: Optional[int], updated_by: Optional[str]]) -> ModelVersionInfo

        Updates the specified model version.

        The caller must be a metastore admin or an owner of the parent registered model. For the latter case,
        the caller must also be the owner or have the **USE_CATALOG** privilege on the parent catalog and the
        **USE_SCHEMA** privilege on the parent schema.

        Currently only the comment of the model version can be updated.

        :param full_name: str
          The three-level (fully qualified) name of the model version
        :param version: int
          The integer version number of the model version
        :param aliases: List[:class:`RegisteredModelAlias`] (optional)
          List of aliases associated with the model version
        :param catalog_name: str (optional)
          The name of the catalog containing the model version
        :param comment: str (optional)
          The comment attached to the model version
        :param created_at: int (optional)
        :param created_by: str (optional)
          The identifier of the user who created the model version
        :param id: str (optional)
          The unique identifier of the model version
        :param metastore_id: str (optional)
          The unique identifier of the metastore containing the model version
        :param model_name: str (optional)
          The name of the parent registered model of the model version, relative to parent schema
        :param model_version_dependencies: :class:`DependencyList` (optional)
          Model version dependencies, for feature-store packaged models
        :param run_id: str (optional)
          MLflow run ID used when creating the model version, if ``source`` was generated by an experiment run
          stored in an MLflow tracking server
        :param run_workspace_id: int (optional)
          ID of the Databricks workspace containing the MLflow run that generated this model version, if
          applicable
        :param schema_name: str (optional)
          The name of the schema containing the model version, relative to parent catalog
        :param source: str (optional)
          URI indicating the location of the source artifacts (files) for the model version
        :param status: :class:`ModelVersionInfoStatus` (optional)
          Current status of the model version. Newly created model versions start in PENDING_REGISTRATION
          status, then move to READY status once the model version files are uploaded and the model version is
          finalized. Only model versions in READY status can be loaded for inference or served.
        :param storage_location: str (optional)
          The storage location on the cloud under which model version data files are stored
        :param updated_at: int (optional)
        :param updated_by: str (optional)
          The identifier of the user who updated the model version last time

        :returns: :class:`ModelVersionInfo`
        