``w.temporary_table_credentials``: Temporary Table Credentials
==============================================================
.. currentmodule:: databricks.sdk.service.catalog

.. py:class:: TemporaryTableCredentialsAPI

    Temporary Table Credentials refer to short-lived, downscoped credentials used to access cloud storage
    locationswhere table data is stored in Databricks. These credentials are employed to provide secure and
    time-limitedaccess to data in cloud environments such as AWS, Azure, and Google Cloud. Each cloud provider
    has its own typeof credentials: AWS uses temporary session tokens via AWS Security Token Service (STS),
    Azure utilizesShared Access Signatures (SAS) for its data storage services, and Google Cloud supports
    temporary credentialsthrough OAuth 2.0.Temporary table credentials ensure that data access is limited in
    scope and duration, reducing the risk ofunauthorized access or misuse. To use the temporary table
    credentials API, a metastore admin needs to enable the external_access_enabled flag (off by default) at
    the metastore level, and user needs to be granted the EXTERNAL USE SCHEMA permission at the schema level
    by catalog admin. Note that EXTERNAL USE SCHEMA is a schema level permission that can only be granted by
    catalog admin explicitly and is not included in schema ownership or ALL PRIVILEGES on the schema for
    security reason.

    .. py:method:: generate_temporary_table_credentials( [, operation: Optional[TableOperation], table_id: Optional[str]]) -> GenerateTemporaryTableCredentialResponse

        Generate a temporary table credential.
        
        Get a short-lived credential for directly accessing the table data on cloud storage. The metastore
        must have external_access_enabled flag set to true (default false). The caller must have
        EXTERNAL_USE_SCHEMA privilege on the parent schema and this privilege can only be granted by catalog
        owners.
        
        :param operation: :class:`TableOperation` (optional)
          The operation performed against the table data, either READ or READ_WRITE. If READ_WRITE is
          specified, the credentials returned will have write permissions, otherwise, it will be read only.
        :param table_id: str (optional)
          UUID of the table to read or write.
        
        :returns: :class:`GenerateTemporaryTableCredentialResponse`
        