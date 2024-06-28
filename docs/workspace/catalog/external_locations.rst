``w.external_locations``: External Locations
============================================
.. currentmodule:: databricks.sdk.service.catalog

.. py:class:: ExternalLocationsAPI

    An external location is an object that combines a cloud storage path with a storage credential that
    authorizes access to the cloud storage path. Each external location is subject to Unity Catalog
    access-control policies that control which users and groups can access the credential. If a user does not
    have access to an external location in Unity Catalog, the request fails and Unity Catalog does not attempt
    to authenticate to your cloud tenant on the user’s behalf.
    
    Databricks recommends using external locations rather than using storage credentials directly.
    
    To create external locations, you must be a metastore admin or a user with the
    **CREATE_EXTERNAL_LOCATION** privilege.

    .. py:method:: create(name: str, url: str, credential_name: str [, access_point: Optional[str], comment: Optional[str], encryption_details: Optional[EncryptionDetails], read_only: Optional[bool], skip_validation: Optional[bool]]) -> ExternalLocationInfo


        Usage:

        .. code-block::

            import os
            import time
            
            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import catalog
            
            w = WorkspaceClient()
            
            storage_credential = w.storage_credentials.create(
                name=f'sdk-{time.time_ns()}',
                aws_iam_role=catalog.AwsIamRoleRequest(role_arn=os.environ["TEST_METASTORE_DATA_ACCESS_ARN"]),
                comment="created via SDK")
            
            external_location = w.external_locations.create(name=f'sdk-{time.time_ns()}',
                                                            credential_name=storage_credential.name,
                                                            comment="created via SDK",
                                                            url="s3://" + os.environ["TEST_BUCKET"] + "/" +
                                                            f'sdk-{time.time_ns()}')
            
            # cleanup
            w.storage_credentials.delete(name=storage_credential.name)
            w.external_locations.delete(name=external_location.name)

        Create an external location.
        
        Creates a new external location entry in the metastore. The caller must be a metastore admin or have
        the **CREATE_EXTERNAL_LOCATION** privilege on both the metastore and the associated storage
        credential.
        
        :param name: str
          Name of the external location.
        :param url: str
          Path URL of the external location.
        :param credential_name: str
          Name of the storage credential used with this location.
        :param access_point: str (optional)
          The AWS access point to use when accesing s3 for this external location.
        :param comment: str (optional)
          User-provided free-form text description.
        :param encryption_details: :class:`EncryptionDetails` (optional)
          Encryption options that apply to clients connecting to cloud storage.
        :param read_only: bool (optional)
          Indicates whether the external location is read-only.
        :param skip_validation: bool (optional)
          Skips validation of the storage credential associated with the external location.
        
        :returns: :class:`ExternalLocationInfo`
        

    .. py:method:: delete(name: str [, force: Optional[bool]])

        Delete an external location.
        
        Deletes the specified external location from the metastore. The caller must be the owner of the
        external location.
        
        :param name: str
          Name of the external location.
        :param force: bool (optional)
          Force deletion even if there are dependent external tables or mounts.
        
        
        

    .. py:method:: get(name: str [, include_browse: Optional[bool]]) -> ExternalLocationInfo


        Usage:

        .. code-block::

            import os
            import time
            
            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import catalog
            
            w = WorkspaceClient()
            
            credential = w.storage_credentials.create(
                name=f'sdk-{time.time_ns()}',
                aws_iam_role=catalog.AwsIamRole(role_arn=os.environ["TEST_METASTORE_DATA_ACCESS_ARN"]))
            
            created = w.external_locations.create(name=f'sdk-{time.time_ns()}',
                                                  credential_name=credential.name,
                                                  url=f's3://{os.environ["TEST_BUCKET"]}/sdk-{time.time_ns()}')
            
            _ = w.external_locations.get(get=created.name)
            
            # cleanup
            w.storage_credentials.delete(delete=credential.name)
            w.external_locations.delete(delete=created.name)

        Get an external location.
        
        Gets an external location from the metastore. The caller must be either a metastore admin, the owner
        of the external location, or a user that has some privilege on the external location.
        
        :param name: str
          Name of the external location.
        :param include_browse: bool (optional)
          Whether to include external locations in the response for which the principal can only access
          selective metadata for
        
        :returns: :class:`ExternalLocationInfo`
        

    .. py:method:: list( [, include_browse: Optional[bool], max_results: Optional[int], page_token: Optional[str]]) -> Iterator[ExternalLocationInfo]


        Usage:

        .. code-block::

            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import catalog
            
            w = WorkspaceClient()
            
            all = w.external_locations.list(catalog.ListExternalLocationsRequest())

        List external locations.
        
        Gets an array of external locations (__ExternalLocationInfo__ objects) from the metastore. The caller
        must be a metastore admin, the owner of the external location, or a user that has some privilege on
        the external location. There is no guarantee of a specific ordering of the elements in the array.
        
        :param include_browse: bool (optional)
          Whether to include external locations in the response for which the principal can only access
          selective metadata for
        :param max_results: int (optional)
          Maximum number of external locations to return. If not set, all the external locations are returned
          (not recommended). - when set to a value greater than 0, the page length is the minimum of this
          value and a server configured value; - when set to 0, the page length is set to a server configured
          value (recommended); - when set to a value less than 0, an invalid parameter error is returned;
        :param page_token: str (optional)
          Opaque pagination token to go to next page based on previous query.
        
        :returns: Iterator over :class:`ExternalLocationInfo`
        

    .. py:method:: update(name: str [, access_point: Optional[str], comment: Optional[str], credential_name: Optional[str], encryption_details: Optional[EncryptionDetails], force: Optional[bool], isolation_mode: Optional[IsolationMode], new_name: Optional[str], owner: Optional[str], read_only: Optional[bool], skip_validation: Optional[bool], url: Optional[str]]) -> ExternalLocationInfo


        Usage:

        .. code-block::

            import os
            import time
            
            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import catalog
            
            w = WorkspaceClient()
            
            credential = w.storage_credentials.create(
                name=f'sdk-{time.time_ns()}',
                aws_iam_role=catalog.AwsIamRoleRequest(role_arn=os.environ["TEST_METASTORE_DATA_ACCESS_ARN"]))
            
            created = w.external_locations.create(name=f'sdk-{time.time_ns()}',
                                                  credential_name=credential.name,
                                                  url="s3://%s/%s" % (os.environ["TEST_BUCKET"], f'sdk-{time.time_ns()}'))
            
            _ = w.external_locations.update(name=created.name,
                                            credential_name=credential.name,
                                            url="s3://%s/%s" % (os.environ["TEST_BUCKET"], f'sdk-{time.time_ns()}'))
            
            # cleanup
            w.storage_credentials.delete(name=credential.name)
            w.external_locations.delete(name=created.name)

        Update an external location.
        
        Updates an external location in the metastore. The caller must be the owner of the external location,
        or be a metastore admin. In the second case, the admin can only update the name of the external
        location.
        
        :param name: str
          Name of the external location.
        :param access_point: str (optional)
          The AWS access point to use when accesing s3 for this external location.
        :param comment: str (optional)
          User-provided free-form text description.
        :param credential_name: str (optional)
          Name of the storage credential used with this location.
        :param encryption_details: :class:`EncryptionDetails` (optional)
          Encryption options that apply to clients connecting to cloud storage.
        :param force: bool (optional)
          Force update even if changing url invalidates dependent external tables or mounts.
        :param isolation_mode: :class:`IsolationMode` (optional)
          Whether the current securable is accessible from all workspaces or a specific set of workspaces.
        :param new_name: str (optional)
          New name for the external location.
        :param owner: str (optional)
          The owner of the external location.
        :param read_only: bool (optional)
          Indicates whether the external location is read-only.
        :param skip_validation: bool (optional)
          Skips validation of the storage credential associated with the external location.
        :param url: str (optional)
          Path URL of the external location.
        
        :returns: :class:`ExternalLocationInfo`
        