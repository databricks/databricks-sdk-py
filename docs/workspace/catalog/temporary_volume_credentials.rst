``w.temporary_volume_credentials``: Temporary Volume Credentials
================================================================
.. currentmodule:: databricks.sdk.service.catalog

.. py:class:: TemporaryVolumeCredentialsAPI

    Temporary Volume Credentials refer to short-lived, downscoped credentials used to access cloud storage
    locations where volume data is stored in Databricks. These credentials are employed to provide secure and
    time-limited access to data in cloud environments such as AWS, Azure, and Google Cloud. Each cloud
    provider has its own type of credentials: AWS uses temporary session tokens via AWS Security Token Service
    (STS), Azure utilizes Shared Access Signatures (SAS) for its data storage services, and Google Cloud
    supports temporary credentials through OAuth 2.0.

    Temporary volume credentials ensure that data access is limited in scope and duration, reducing the risk
    of unauthorized access or misuse. To use the temporary volume credentials API, a metastore admin needs to
    enable the external_access_enabled flag (off by default) at the metastore level, and user needs to be
    granted the EXTERNAL USE SCHEMA permission at the schema level by catalog owner. Note that EXTERNAL USE
    SCHEMA is a schema level permission that can only be granted by catalog owner explicitly and is not
    included in schema ownership or ALL PRIVILEGES on the schema for security reasons.

    .. py:method:: generate_temporary_volume_credentials( [, operation: Optional[VolumeOperation], volume_id: Optional[str]]) -> GenerateTemporaryVolumeCredentialResponse

        Get a short-lived credential for directly accessing the volume data on cloud storage. The metastore
        must have **external_access_enabled** flag set to true (default false). The caller must have the
        **EXTERNAL_USE_SCHEMA** privilege on the parent schema and this privilege can only be granted by
        catalog owners.

        :param operation: :class:`VolumeOperation` (optional)
          The operation performed against the volume data, either READ_VOLUME or WRITE_VOLUME. If WRITE_VOLUME
          is specified, the credentials returned will have write permissions, otherwise, it will be read only.
        :param volume_id: str (optional)
          Id of the volume to read or write.

        :returns: :class:`GenerateTemporaryVolumeCredentialResponse`
        