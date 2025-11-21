``a.storage``: Storage configurations
=====================================
.. currentmodule:: databricks.sdk.service.provisioning

.. py:class:: StorageAPI

    These APIs manage storage configurations for this workspace. A root storage S3 bucket in your account is
    required to store objects like cluster logs, notebook revisions, and job results. You can also use the
    root storage S3 bucket for storage of non-production DBFS data. A storage configuration encapsulates this
    bucket information, and its ID is used when creating a new workspace.

    .. py:method:: create(storage_configuration_name: str, root_bucket_info: RootBucketInfo [, role_arn: Optional[str]]) -> StorageConfiguration


        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import AccountClient
            from databricks.sdk.service import provisioning
            
            a = AccountClient()
            
            bucket = a.storage.create(
                storage_configuration_name=f"sdk-{time.time_ns()}",
                root_bucket_info=provisioning.RootBucketInfo(bucket_name=f"sdk-{time.time_ns()}"),
            )
            
            # cleanup
            a.storage.delete(storage_configuration_id=bucket.storage_configuration_id)

        Creates a Databricks storage configuration for an account.

        :param storage_configuration_name: str
          The human-readable name of the storage configuration.
        :param root_bucket_info: :class:`RootBucketInfo`
          Root S3 bucket information.
        :param role_arn: str (optional)
          Optional IAM role that is used to access the workspace catalog which is created during workspace
          creation for UC by Default. If a storage configuration with this field populated is used to create a
          workspace, then a workspace catalog is created together with the workspace. The workspace catalog
          shares the root bucket with internal workspace storage (including DBFS root) but uses a dedicated
          bucket path prefix.

        :returns: :class:`StorageConfiguration`
        

    .. py:method:: delete(storage_configuration_id: str) -> StorageConfiguration

        Deletes a Databricks storage configuration. You cannot delete a storage configuration that is
        associated with any workspace.

        :param storage_configuration_id: str

        :returns: :class:`StorageConfiguration`
        

    .. py:method:: get(storage_configuration_id: str) -> StorageConfiguration


        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import AccountClient
            from databricks.sdk.service import provisioning
            
            a = AccountClient()
            
            storage = a.storage.create(
                storage_configuration_name=f"sdk-{time.time_ns()}",
                root_bucket_info=provisioning.RootBucketInfo(bucket_name=f"sdk-{time.time_ns()}"),
            )
            
            by_id = a.storage.get(storage_configuration_id=storage.storage_configuration_id)

        Gets a Databricks storage configuration for an account, both specified by ID.

        :param storage_configuration_id: str

        :returns: :class:`StorageConfiguration`
        

    .. py:method:: list() -> Iterator[StorageConfiguration]


        Usage:

        .. code-block::

            from databricks.sdk import AccountClient
            
            a = AccountClient()
            
            configs = a.storage.list()

        Lists Databricks storage configurations for an account, specified by ID.


        :returns: Iterator over :class:`StorageConfiguration`
        