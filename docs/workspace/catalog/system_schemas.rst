``w.system_schemas``: SystemSchemas
===================================
.. currentmodule:: databricks.sdk.service.catalog

.. py:class:: SystemSchemasAPI

    A system schema is a schema that lives within the system catalog. A system schema may contain information
    about customer usage of Unity Catalog such as audit-logs, billing-logs, lineage information, etc.

    .. py:method:: disable(metastore_id: str, schema_name: str)

        Disables the system schema and removes it from the system catalog. The caller must be an account admin
        or a metastore admin.

        :param metastore_id: str
          The metastore ID under which the system schema lives.
        :param schema_name: str
          Full name of the system schema.


        

    .. py:method:: enable(metastore_id: str, schema_name: str [, catalog_name: Optional[str]])

        Enables the system schema and adds it to the system catalog. The caller must be an account admin or a
        metastore admin.

        :param metastore_id: str
          The metastore ID under which the system schema lives.
        :param schema_name: str
          Full name of the system schema.
        :param catalog_name: str (optional)
          the catalog for which the system schema is to enabled in


        

    .. py:method:: list(metastore_id: str [, max_results: Optional[int], page_token: Optional[str]]) -> Iterator[SystemSchemaInfo]

        Gets an array of system schemas for a metastore. The caller must be an account admin or a metastore
        admin.

        NOTE: we recommend using max_results=0 to use the paginated version of this API. Unpaginated calls
        will be deprecated soon.

        PAGINATION BEHAVIOR: When using pagination (max_results >= 0), a page may contain zero results while
        still providing a next_page_token. Clients must continue reading pages until next_page_token is
        absent, which is the only indication that the end of results has been reached.

        :param metastore_id: str
          The ID for the metastore in which the system schema resides.
        :param max_results: int (optional)
          Maximum number of schemas to return. - When set to 0, the page length is set to a server configured
          value (recommended); - When set to a value greater than 0, the page length is the minimum of this
          value and a server configured value; - When set to a value less than 0, an invalid parameter error
          is returned; - If not set, all the schemas are returned (not recommended).
        :param page_token: str (optional)
          Opaque pagination token to go to next page based on previous query.

        :returns: Iterator over :class:`SystemSchemaInfo`
        