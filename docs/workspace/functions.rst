Functions
=========
.. py:class:: FunctionsAPI

    Functions implement User-Defined Functions (UDFs) in Unity Catalog.
    
    The function implementation can be any SQL expression or Query, and it can be invoked wherever a table
    reference is allowed in a query. In Unity Catalog, a function resides at the same level as a table, so it
    can be referenced with the form __catalog_name__.__schema_name__.__function_name__.

    .. py:method:: create(name, catalog_name, schema_name, input_params, data_type, full_data_type, return_params, routine_body, routine_definition, routine_dependencies, parameter_style, is_deterministic, sql_data_access, is_null_call, security_type, specific_name [, comment, external_language, external_name, properties, sql_path])

        Create a function.
        
        Creates a new function
        
        The user must have the following permissions in order for the function to be created: -
        **USE_CATALOG** on the function's parent catalog - **USE_SCHEMA** and **CREATE_FUNCTION** on the
        function's parent schema
        
        :param name: str
          Name of function, relative to parent schema.
        :param catalog_name: str
          Name of parent catalog.
        :param schema_name: str
          Name of parent schema relative to its parent catalog.
        :param input_params: List[:class:`FunctionParameterInfo`]
          The array of __FunctionParameterInfo__ definitions of the function's parameters.
        :param data_type: :class:`ColumnTypeName`
          Scalar function return data type.
        :param full_data_type: str
          Pretty printed function data type.
        :param return_params: List[:class:`FunctionParameterInfo`]
          Table function return parameters.
        :param routine_body: :class:`CreateFunctionRoutineBody`
          Function language. When **EXTERNAL** is used, the language of the routine function should be
          specified in the __external_language__ field, and the __return_params__ of the function cannot be
          used (as **TABLE** return type is not supported), and the __sql_data_access__ field must be
          **NO_SQL**.
        :param routine_definition: str
          Function body.
        :param routine_dependencies: List[:class:`Dependency`]
          Function dependencies.
        :param parameter_style: :class:`CreateFunctionParameterStyle`
          Function parameter style. **S** is the value for SQL.
        :param is_deterministic: bool
          Whether the function is deterministic.
        :param sql_data_access: :class:`CreateFunctionSqlDataAccess`
          Function SQL data access.
        :param is_null_call: bool
          Function null call.
        :param security_type: :class:`CreateFunctionSecurityType`
          Function security type.
        :param specific_name: str
          Specific name of the function; Reserved for future use.
        :param comment: str (optional)
          User-provided free-form text description.
        :param external_language: str (optional)
          External function language.
        :param external_name: str (optional)
          External function name.
        :param properties: Dict[str,str] (optional)
          A map of key-value properties attached to the securable.
        :param sql_path: str (optional)
          List of schemes whose objects can be referenced without qualification.
        
        :returns: :class:`FunctionInfo`
        

    .. py:method:: delete(name [, force])

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
        
        
        

    .. py:method:: get(name)

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
        
        :returns: :class:`FunctionInfo`
        

    .. py:method:: list(catalog_name, schema_name)

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
        
        :returns: Iterator over :class:`FunctionInfo`
        

    .. py:method:: update(name [, owner])

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
        