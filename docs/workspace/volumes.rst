Volumes
=======
.. py:class:: VolumesAPI

    Volumes are a Unity Catalog (UC) capability for accessing, storing, governing, organizing and processing
    files. Use cases include running machine learning on unstructured data such as image, audio, video, or PDF
    files, organizing data sets during the data exploration stages in data science, working with libraries
    that require access to the local file system on cluster machines, storing library and config files of
    arbitrary formats such as .whl or .txt centrally and providing secure access across workspaces to it, or
    transforming and querying non-tabular data files in ETL.

    .. py:method:: create(catalog_name, name, schema_name, volume_type [, comment, storage_location])

        Usage:

        .. code-block::

            import os
            import time
            
            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import catalog
            
            w = WorkspaceClient()
            
            storage_credential = w.storage_credentials.create(
                name=f'sdk-{time.time_ns()}',
                aws_iam_role=catalog.AwsIamRole(role_arn=os.environ["TEST_METASTORE_DATA_ACCESS_ARN"]),
                comment="created via SDK")
            
            external_location = w.external_locations.create(name=f'sdk-{time.time_ns()}',
                                                            credential_name=storage_credential.name,
                                                            comment="created via SDK",
                                                            url="s3://" + os.environ["TEST_BUCKET"] + "/" +
                                                            f'sdk-{time.time_ns()}')
            
            created_catalog = w.catalogs.create(name=f'sdk-{time.time_ns()}')
            
            created_schema = w.schemas.create(name=f'sdk-{time.time_ns()}', catalog_name=created_catalog.name)
            
            created_volume = w.volumes.create(catalog_name=created_catalog.name,
                                              schema_name=created_schema.name,
                                              name=f'sdk-{time.time_ns()}',
                                              storage_location=external_location.url,
                                              volume_type=catalog.VolumeType.EXTERNAL)
            
            # cleanup
            w.schemas.delete(full_name=created_schema.full_name)
            w.catalogs.delete(name=created_catalog.name, force=True)
            w.volumes.delete(full_name_arg=created_volume.full_name)

        Create a Volume.
        
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
        :param name: str
          The name of the volume
        :param schema_name: str
          The name of the schema where the volume is
        :param volume_type: :class:`VolumeType`
        :param comment: str (optional)
          The comment attached to the volume
        :param storage_location: str (optional)
          The storage location on the cloud
        
        :returns: :class:`VolumeInfo`
        

    .. py:method:: delete(full_name_arg)

        Delete a Volume.
        
        Deletes a volume from the specified parent catalog and schema.
        
        The caller must be a metastore admin or an owner of the volume. For the latter case, the caller must
        also be the owner or have the **USE_CATALOG** privilege on the parent catalog and the **USE_SCHEMA**
        privilege on the parent schema.
        
        :param full_name_arg: str
          The three-level (fully qualified) name of the volume
        
        
        

    .. py:method:: list(catalog_name, schema_name)

        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            created_catalog = w.catalogs.create(name=f'sdk-{time.time_ns()}')
            
            created_schema = w.schemas.create(name=f'sdk-{time.time_ns()}', catalog_name=created_catalog.name)
            
            all_volumes = w.volumes.list(catalog_name=created_catalog.name, schema_name=created_schema.name)
            
            # cleanup
            w.schemas.delete(full_name=created_schema.full_name)
            w.catalogs.delete(name=created_catalog.name, force=True)

        List Volumes.
        
        Gets an array of all volumes for the current metastore under the parent catalog and schema.
        
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
        
        :returns: Iterator over :class:`VolumeInfo`
        

    .. py:method:: read(full_name_arg)

        Usage:

        .. code-block::

            import os
            import time
            
            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import catalog
            
            w = WorkspaceClient()
            
            storage_credential = w.storage_credentials.create(
                name=f'sdk-{time.time_ns()}',
                aws_iam_role=catalog.AwsIamRole(role_arn=os.environ["TEST_METASTORE_DATA_ACCESS_ARN"]),
                comment="created via SDK")
            
            external_location = w.external_locations.create(name=f'sdk-{time.time_ns()}',
                                                            credential_name=storage_credential.name,
                                                            comment="created via SDK",
                                                            url="s3://" + os.environ["TEST_BUCKET"] + "/" +
                                                            f'sdk-{time.time_ns()}')
            
            created_catalog = w.catalogs.create(name=f'sdk-{time.time_ns()}')
            
            created_schema = w.schemas.create(name=f'sdk-{time.time_ns()}', catalog_name=created_catalog.name)
            
            created_volume = w.volumes.create(catalog_name=created_catalog.name,
                                              schema_name=created_schema.name,
                                              name=f'sdk-{time.time_ns()}',
                                              storage_location=external_location.url,
                                              volume_type=catalog.VolumeType.EXTERNAL)
            
            loaded_volume = w.volumes.read(full_name_arg=created_volume.full_name)
            
            # cleanup
            w.schemas.delete(full_name=created_schema.full_name)
            w.catalogs.delete(name=created_catalog.name, force=True)
            w.volumes.delete(full_name_arg=created_volume.full_name)

        Get a Volume.
        
        Gets a volume from the metastore for a specific catalog and schema.
        
        The caller must be a metastore admin or an owner of (or have the **READ VOLUME** privilege on) the
        volume. For the latter case, the caller must also be the owner or have the **USE_CATALOG** privilege
        on the parent catalog and the **USE_SCHEMA** privilege on the parent schema.
        
        :param full_name_arg: str
          The three-level (fully qualified) name of the volume
        
        :returns: :class:`VolumeInfo`
        

    .. py:method:: update(full_name_arg [, comment, name, owner])

        Usage:

        .. code-block::

            import os
            import time
            
            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import catalog
            
            w = WorkspaceClient()
            
            storage_credential = w.storage_credentials.create(
                name=f'sdk-{time.time_ns()}',
                aws_iam_role=catalog.AwsIamRole(role_arn=os.environ["TEST_METASTORE_DATA_ACCESS_ARN"]),
                comment="created via SDK")
            
            external_location = w.external_locations.create(name=f'sdk-{time.time_ns()}',
                                                            credential_name=storage_credential.name,
                                                            comment="created via SDK",
                                                            url="s3://" + os.environ["TEST_BUCKET"] + "/" +
                                                            f'sdk-{time.time_ns()}')
            
            created_catalog = w.catalogs.create(name=f'sdk-{time.time_ns()}')
            
            created_schema = w.schemas.create(name=f'sdk-{time.time_ns()}', catalog_name=created_catalog.name)
            
            created_volume = w.volumes.create(catalog_name=created_catalog.name,
                                              schema_name=created_schema.name,
                                              name=f'sdk-{time.time_ns()}',
                                              storage_location=external_location.url,
                                              volume_type=catalog.VolumeType.EXTERNAL)
            
            loaded_volume = w.volumes.read(full_name_arg=created_volume.full_name)
            
            _ = w.volumes.update(full_name_arg=loaded_volume.full_name, comment="Updated volume comment")
            
            # cleanup
            w.schemas.delete(full_name=created_schema.full_name)
            w.catalogs.delete(name=created_catalog.name, force=True)
            w.volumes.delete(full_name_arg=created_volume.full_name)

        Update a Volume.
        
        Updates the specified volume under the specified parent catalog and schema.
        
        The caller must be a metastore admin or an owner of the volume. For the latter case, the caller must
        also be the owner or have the **USE_CATALOG** privilege on the parent catalog and the **USE_SCHEMA**
        privilege on the parent schema.
        
        Currently only the name, the owner or the comment of the volume could be updated.
        
        :param full_name_arg: str
          The three-level (fully qualified) name of the volume
        :param comment: str (optional)
          The comment attached to the volume
        :param name: str (optional)
          The name of the volume
        :param owner: str (optional)
          The identifier of the user who owns the volume
        
        :returns: :class:`VolumeInfo`
        