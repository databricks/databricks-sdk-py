``w.volumes``: Volumes
======================
.. currentmodule:: databricks.sdk.service.catalog

.. py:class:: VolumesAPI

    Volumes are a Unity Catalog (UC) capability for accessing, storing, governing, organizing and processing
    files. Use cases include running machine learning on unstructured data such as image, audio, video, or PDF
    files, organizing data sets during the data exploration stages in data science, working with libraries
    that require access to the local file system on cluster machines, storing library and config files of
    arbitrary formats such as .whl or .txt centrally and providing secure access across workspaces to it, or
    transforming and querying non-tabular data files in ETL.

    .. py:method:: create(catalog_name: str, schema_name: str, name: str, volume_type: VolumeType [, comment: Optional[str], storage_location: Optional[str]]) -> VolumeInfo


        Usage:

        .. code-block::

            import os
            import time
            
            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import catalog
            
            w = WorkspaceClient()
            
            storage_credential = w.storage_credentials.create(
                name=f"sdk-{time.time_ns()}",
                aws_iam_role=catalog.AwsIamRoleRequest(role_arn=os.environ["TEST_METASTORE_DATA_ACCESS_ARN"]),
                comment="created via SDK",
            )
            
            external_location = w.external_locations.create(
                name=f"sdk-{time.time_ns()}",
                credential_name=storage_credential.name,
                comment="created via SDK",
                url="s3://" + os.environ["TEST_BUCKET"] + "/" + f"sdk-{time.time_ns()}",
            )
            
            created_catalog = w.catalogs.create(name=f"sdk-{time.time_ns()}")
            
            created_schema = w.schemas.create(name=f"sdk-{time.time_ns()}", catalog_name=created_catalog.name)
            
            created_volume = w.volumes.create(
                catalog_name=created_catalog.name,
                schema_name=created_schema.name,
                name=f"sdk-{time.time_ns()}",
                storage_location=external_location.url,
                volume_type=catalog.VolumeType.EXTERNAL,
            )
            
            # cleanup
            w.storage_credentials.delete(name=storage_credential.name)
            w.external_locations.delete(name=external_location.name)
            w.schemas.delete(full_name=created_schema.full_name)
            w.catalogs.delete(name=created_catalog.name, force=True)
            w.volumes.delete(name=created_volume.full_name)

        Creates a new volume.
        
        The user could create either an external volume or a managed volume. An external volume will be
        created in the specified external location, while a managed volume will be located in the default
        location which is specified by the parent schema, or the parent catalog, or the Metastore.
        
        For the volume creation to succeed, the user must satisfy following conditions: - The caller must be a
        metastore admin, or be the owner of the parent catalog and schema, or have the **USE_CATALOG**
        privilege on the parent catalog and the **USE_SCHEMA** privilege on the parent schema. - The caller
        must have **CREATE VOLUME** privilege on the parent schema.
        
        For an external volume, following conditions also need to satisfy - The caller must have **CREATE
        EXTERNAL VOLUME** privilege on the external location. - There are no other tables, nor volumes
        existing in the specified storage location. - The specified storage location is not under the location
        of other tables, nor volumes, or catalogs or schemas.
        
        :param catalog_name: str
          The name of the catalog where the schema and the volume are
        :param schema_name: str
          The name of the schema where the volume is
        :param name: str
          The name of the volume
        :param volume_type: :class:`VolumeType`
        :param comment: str (optional)
          The comment attached to the volume
        :param storage_location: str (optional)
          The storage location on the cloud
        
        :returns: :class:`VolumeInfo`
        

    .. py:method:: delete(name: str)

        Deletes a volume from the specified parent catalog and schema.
        
        The caller must be a metastore admin or an owner of the volume. For the latter case, the caller must
        also be the owner or have the **USE_CATALOG** privilege on the parent catalog and the **USE_SCHEMA**
        privilege on the parent schema.
        
        :param name: str
          The three-level (fully qualified) name of the volume
        
        
        

    .. py:method:: list(catalog_name: str, schema_name: str [, include_browse: Optional[bool], max_results: Optional[int], page_token: Optional[str]]) -> Iterator[VolumeInfo]


        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            created_catalog = w.catalogs.create(name=f"sdk-{time.time_ns()}")
            
            created_schema = w.schemas.create(name=f"sdk-{time.time_ns()}", catalog_name=created_catalog.name)
            
            all_volumes = w.volumes.list(catalog_name=created_catalog.name, schema_name=created_schema.name)
            
            # cleanup
            w.schemas.delete(full_name=created_schema.full_name)
            w.catalogs.delete(name=created_catalog.name, force=True)

        Gets an array of volumes for the current metastore under the parent catalog and schema.
        
        The returned volumes are filtered based on the privileges of the calling user. For example, the
        metastore admin is able to list all the volumes. A regular user needs to be the owner or have the
        **READ VOLUME** privilege on the volume to recieve the volumes in the response. For the latter case,
        the caller must also be the owner or have the **USE_CATALOG** privilege on the parent catalog and the
        **USE_SCHEMA** privilege on the parent schema.
        
        There is no guarantee of a specific ordering of the elements in the array.
        
        :param catalog_name: str
          The identifier of the catalog
        :param schema_name: str
          The identifier of the schema
        :param include_browse: bool (optional)
          Whether to include volumes in the response for which the principal can only access selective
          metadata for
        :param max_results: int (optional)
          Maximum number of volumes to return (page length).
          
          If not set, the page length is set to a server configured value (10000, as of 1/29/2024). - when set
          to a value greater than 0, the page length is the minimum of this value and a server configured
          value (10000, as of 1/29/2024); - when set to 0, the page length is set to a server configured value
          (10000, as of 1/29/2024) (recommended); - when set to a value less than 0, an invalid parameter
          error is returned;
          
          Note: this parameter controls only the maximum number of volumes to return. The actual number of
          volumes returned in a page may be smaller than this value, including 0, even if there are more
          pages.
        :param page_token: str (optional)
          Opaque token returned by a previous request. It must be included in the request to retrieve the next
          page of results (pagination).
        
        :returns: Iterator over :class:`VolumeInfo`
        

    .. py:method:: read(name: str [, include_browse: Optional[bool]]) -> VolumeInfo


        Usage:

        .. code-block::

            import os
            import time
            
            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import catalog
            
            w = WorkspaceClient()
            
            storage_credential = w.storage_credentials.create(
                name=f"sdk-{time.time_ns()}",
                aws_iam_role=catalog.AwsIamRoleRequest(role_arn=os.environ["TEST_METASTORE_DATA_ACCESS_ARN"]),
                comment="created via SDK",
            )
            
            external_location = w.external_locations.create(
                name=f"sdk-{time.time_ns()}",
                credential_name=storage_credential.name,
                comment="created via SDK",
                url="s3://" + os.environ["TEST_BUCKET"] + "/" + f"sdk-{time.time_ns()}",
            )
            
            created_catalog = w.catalogs.create(name=f"sdk-{time.time_ns()}")
            
            created_schema = w.schemas.create(name=f"sdk-{time.time_ns()}", catalog_name=created_catalog.name)
            
            created_volume = w.volumes.create(
                catalog_name=created_catalog.name,
                schema_name=created_schema.name,
                name=f"sdk-{time.time_ns()}",
                storage_location=external_location.url,
                volume_type=catalog.VolumeType.EXTERNAL,
            )
            
            loaded_volume = w.volumes.read(name=created_volume.full_name)
            
            # cleanup
            w.storage_credentials.delete(name=storage_credential.name)
            w.external_locations.delete(name=external_location.name)
            w.schemas.delete(full_name=created_schema.full_name)
            w.catalogs.delete(name=created_catalog.name, force=True)
            w.volumes.delete(name=created_volume.full_name)

        Gets a volume from the metastore for a specific catalog and schema.
        
        The caller must be a metastore admin or an owner of (or have the **READ VOLUME** privilege on) the
        volume. For the latter case, the caller must also be the owner or have the **USE_CATALOG** privilege
        on the parent catalog and the **USE_SCHEMA** privilege on the parent schema.
        
        :param name: str
          The three-level (fully qualified) name of the volume
        :param include_browse: bool (optional)
          Whether to include volumes in the response for which the principal can only access selective
          metadata for
        
        :returns: :class:`VolumeInfo`
        

    .. py:method:: update(name: str [, comment: Optional[str], new_name: Optional[str], owner: Optional[str]]) -> VolumeInfo


        Usage:

        .. code-block::

            import os
            import time
            
            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import catalog
            
            w = WorkspaceClient()
            
            storage_credential = w.storage_credentials.create(
                name=f"sdk-{time.time_ns()}",
                aws_iam_role=catalog.AwsIamRoleRequest(role_arn=os.environ["TEST_METASTORE_DATA_ACCESS_ARN"]),
                comment="created via SDK",
            )
            
            external_location = w.external_locations.create(
                name=f"sdk-{time.time_ns()}",
                credential_name=storage_credential.name,
                comment="created via SDK",
                url="s3://" + os.environ["TEST_BUCKET"] + "/" + f"sdk-{time.time_ns()}",
            )
            
            created_catalog = w.catalogs.create(name=f"sdk-{time.time_ns()}")
            
            created_schema = w.schemas.create(name=f"sdk-{time.time_ns()}", catalog_name=created_catalog.name)
            
            created_volume = w.volumes.create(
                catalog_name=created_catalog.name,
                schema_name=created_schema.name,
                name=f"sdk-{time.time_ns()}",
                storage_location=external_location.url,
                volume_type=catalog.VolumeType.EXTERNAL,
            )
            
            loaded_volume = w.volumes.read(name=created_volume.full_name)
            
            _ = w.volumes.update(name=loaded_volume.full_name, comment="Updated volume comment")
            
            # cleanup
            w.storage_credentials.delete(name=storage_credential.name)
            w.external_locations.delete(name=external_location.name)
            w.schemas.delete(full_name=created_schema.full_name)
            w.catalogs.delete(name=created_catalog.name, force=True)
            w.volumes.delete(name=created_volume.full_name)

        Updates the specified volume under the specified parent catalog and schema.
        
        The caller must be a metastore admin or an owner of the volume. For the latter case, the caller must
        also be the owner or have the **USE_CATALOG** privilege on the parent catalog and the **USE_SCHEMA**
        privilege on the parent schema.
        
        Currently only the name, the owner or the comment of the volume could be updated.
        
        :param name: str
          The three-level (fully qualified) name of the volume
        :param comment: str (optional)
          The comment attached to the volume
        :param new_name: str (optional)
          New name for the volume.
        :param owner: str (optional)
          The identifier of the user who owns the volume
        
        :returns: :class:`VolumeInfo`
        