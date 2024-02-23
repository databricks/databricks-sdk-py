``w.system_schemas``: SystemSchemas
===================================
.. currentmodule:: databricks.sdk.service.catalog

.. py:class:: SystemSchemasAPI

    A system schema is a schema that lives within the system catalog. A system schema may contain information
    about customer usage of Unity Catalog such as audit-logs, billing-logs, lineage information, etc.

    .. py:method:: disable(metastore_id: str, schema_name: DisableSchemaName)

        Disable a system schema.
        
        Disables the system schema and removes it from the system catalog. The caller must be an account admin
        or a metastore admin.
        
        :param metastore_id: str
          The metastore ID under which the system schema lives.
        :param schema_name: :class:`DisableSchemaName`
          Full name of the system schema.
        
        
        

    .. py:method:: enable(metastore_id: str, schema_name: EnableSchemaName)

        Enable a system schema.
        
        Enables the system schema and adds it to the system catalog. The caller must be an account admin or a
        metastore admin.
        
        :param metastore_id: str
          The metastore ID under which the system schema lives.
        :param schema_name: :class:`EnableSchemaName`
          Full name of the system schema.
        
        
        

    .. py:method:: list(metastore_id: str) -> Iterator[SystemSchemaInfo]

        List system schemas.
        
        Gets an array of system schemas for a metastore. The caller must be an account admin or a metastore
        admin.
        
        :param metastore_id: str
          The ID for the metastore in which the system schema resides.
        
        :returns: Iterator over :class:`SystemSchemaInfo`
        