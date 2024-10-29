``a.storage``: Storage configurations
=====================================
.. currentmodule:: databricks.sdk.service.provisioning

.. py:class:: StorageAPI

    These APIs manage storage configurations for this workspace. A root storage S3 bucket in your account is
required to store objects like cluster logs, notebook revisions, and job results. You can also use the
root storage S3 bucket for storage of non-production DBFS data. A storage configuration encapsulates this
bucket information, and its ID is used when creating a new workspace.

    .. py:method:: create(storage_configuration_name: str, root_bucket_info: RootBucketInfo) -> StorageConfiguration


        Usage:

        .. code-block::

            import os
            import time
            
            from databricks.sdk import AccountClient
            from databricks.sdk.service import provisioning
            
            a = AccountClient()
            
            storage = a.storage.create(
                storage_configuration_name=f'sdk-{time.time_ns()}',
                root_bucket_info=provisioning.RootBucketInfo(bucket_name=os.environ["TEST_ROOT_BUCKET"]))
            
            # cleanup
            a.storage.delete(storage_configuration_id=storage.storage_configuration_id)

        Create new storage configuration.

Creates new storage configuration for an account, specified by ID. Uploads a storage configuration
object that represents the root AWS S3 bucket in your account. Databricks stores related workspace
assets including DBFS, cluster logs, and job results. For the AWS S3 bucket, you need to configure the
required bucket policy.

For information about how to create a new workspace with this API, see [Create a new workspace using
the Account API]

[Create a new workspace using the Account API]: http://docs.databricks.com/administration-guide/account-api/new-workspace.html

:param storage_configuration_name: str
  The human-readable name of the storage configuration.
:param root_bucket_info: :class:`RootBucketInfo`
  Root S3 bucket information.

:returns: :class:`StorageConfiguration`


    .. py:method:: delete(storage_configuration_id: str)

        Delete storage configuration.

Deletes a Databricks storage configuration. You cannot delete a storage configuration that is
associated with any workspace.

:param storage_configuration_id: str
  Databricks Account API storage configuration ID.




    .. py:method:: get(storage_configuration_id: str) -> StorageConfiguration


        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import AccountClient
            from databricks.sdk.service import provisioning
            
            a = AccountClient()
            
            storage = a.storage.create(storage_configuration_name=f'sdk-{time.time_ns()}',
                                       root_bucket_info=provisioning.RootBucketInfo(bucket_name=f'sdk-{time.time_ns()}'))
            
            by_id = a.storage.get(storage_configuration_id=storage.storage_configuration_id)

        Get storage configuration.

Gets a Databricks storage configuration for an account, both specified by ID.

:param storage_configuration_id: str
  Databricks Account API storage configuration ID.

:returns: :class:`StorageConfiguration`


    .. py:method:: list() -> Iterator[StorageConfiguration]


        Usage:

        .. code-block::

            from databricks.sdk import AccountClient
            
            a = AccountClient()
            
            configs = a.storage.list()

        Get all storage configurations.

Gets a list of all Databricks storage configurations for your account, specified by ID.

:returns: Iterator over :class:`StorageConfiguration`
