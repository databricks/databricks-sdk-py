``w.functions``: Functions
==========================
.. currentmodule:: databricks.sdk.service.catalog

.. py:class:: FunctionsAPI

    Functions implement User-Defined Functions (UDFs) in Unity Catalog.
    
    The function implementation can be any SQL expression or Query, and it can be invoked wherever a table
    reference is allowed in a query. In Unity Catalog, a function resides at the same level as a table, so it
    can be referenced with the form __catalog_name__.__schema_name__.__function_name__.

    .. py:method:: create(function_info: CreateFunction) -> FunctionInfo

        Create a function.
        
        **WARNING: This API is experimental and will change in future versions**
        
        Creates a new function
        
        The user must have the following permissions in order for the function to be created: -
        **USE_CATALOG** on the function's parent catalog - **USE_SCHEMA** and **CREATE_FUNCTION** on the
        function's parent schema
        
        :param function_info: :class:`CreateFunction`
          Partial __FunctionInfo__ specifying the function to be created.
        
        :returns: :class:`FunctionInfo`
        

    .. py:method:: delete(name: str [, force: Optional[bool]])

        Delete a function.
        
        Deletes the function that matches the supplied name. For the deletion to succeed, the user must
        satisfy one of the following conditions: - Is the owner of the function's parent catalog - Is the
        owner of the function's parent schema and have the **USE_CATALOG** privilege on its parent catalog -
        Is the owner of the function itself and have both the **USE_CATALOG** privilege on its parent catalog
        and the **USE_SCHEMA** privilege on its parent schema
        
        :param name: str
          The fully-qualified name of the function (of the form
          __catalog_name__.__schema_name__.__function__name__).
        :param force: bool (optional)
          Force deletion even if the function is notempty.
        
        
        

    .. py:method:: get(name: str [, include_browse: Optional[bool]]) -> FunctionInfo

        Get a function.
        
        Gets a function from within a parent catalog and schema. For the fetch to succeed, the user must
        satisfy one of the following requirements: - Is a metastore admin - Is an owner of the function's
        parent catalog - Have the **USE_CATALOG** privilege on the function's parent catalog and be the owner
        of the function - Have the **USE_CATALOG** privilege on the function's parent catalog, the
        **USE_SCHEMA** privilege on the function's parent schema, and the **EXECUTE** privilege on the
        function itself
        
        :param name: str
          The fully-qualified name of the function (of the form
          __catalog_name__.__schema_name__.__function__name__).
        :param include_browse: bool (optional)
          Whether to include functions in the response for which the principal can only access selective
          metadata for
        
        :returns: :class:`FunctionInfo`
        

    .. py:method:: list(catalog_name: str, schema_name: str [, include_browse: Optional[bool], max_results: Optional[int], page_token: Optional[str]]) -> Iterator[FunctionInfo]

        List functions.
        
        List functions within the specified parent catalog and schema. If the user is a metastore admin, all
        functions are returned in the output list. Otherwise, the user must have the **USE_CATALOG** privilege
        on the catalog and the **USE_SCHEMA** privilege on the schema, and the output list contains only
        functions for which either the user has the **EXECUTE** privilege or the user is the owner. There is
        no guarantee of a specific ordering of the elements in the array.
        
        :param catalog_name: str
          Name of parent catalog for functions of interest.
        :param schema_name: str
          Parent schema of functions.
        :param include_browse: bool (optional)
          Whether to include functions in the response for which the principal can only access selective
          metadata for
        :param max_results: int (optional)
          Maximum number of functions to return. If not set, all the functions are returned (not recommended).
          - when set to a value greater than 0, the page length is the minimum of this value and a server
          configured value; - when set to 0, the page length is set to a server configured value
          (recommended); - when set to a value less than 0, an invalid parameter error is returned;
        :param page_token: str (optional)
          Opaque pagination token to go to next page based on previous query.
        
        :returns: Iterator over :class:`FunctionInfo`
        

    .. py:method:: update(name: str [, owner: Optional[str]]) -> FunctionInfo

        Update a function.
        
        Updates the function that matches the supplied name. Only the owner of the function can be updated. If
        the user is not a metastore admin, the user must be a member of the group that is the new function
        owner. - Is a metastore admin - Is the owner of the function's parent catalog - Is the owner of the
        function's parent schema and has the **USE_CATALOG** privilege on its parent catalog - Is the owner of
        the function itself and has the **USE_CATALOG** privilege on its parent catalog as well as the
        **USE_SCHEMA** privilege on the function's parent schema.
        
        :param name: str
          The fully-qualified name of the function (of the form
          __catalog_name__.__schema_name__.__function__name__).
        :param owner: str (optional)
          Username of current owner of function.
        
        :returns: :class:`FunctionInfo`
        