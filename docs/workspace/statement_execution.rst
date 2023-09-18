Statement Execution
===================
.. py:class:: StatementExecutionExt

    
    Execute SQL statements in a stateless manner.

    Primary use-case of :py:meth:`iterate_rows` and :py:meth:`execute` methods is oriented at executing SQL queries in
    a stateless manner straight away from Databricks SDK for Python, without requiring any external dependencies.
    Results are fetched in JSON format through presigned external links. This is perfect for serverless applications
    like AWS Lambda, Azure Functions, or any other containerised short-lived applications, where container startup
    time is faster with the smaller dependency set.

    .. code-block:

        for (pickup_zip, dropoff_zip) in w.statement_execution.iterate_rows(warehouse_id,
            'SELECT pickup_zip, dropoff_zip FROM nyctaxi.trips LIMIT 10', catalog='samples'):
            print(f'pickup_zip={pickup_zip}, dropoff_zip={dropoff_zip}')

    Method :py:meth:`iterate_rows` returns an iterator of objects, that resemble :class:`pyspark.sql.Row` APIs, but full
    compatibility is not the goal of this implementation.

    .. code-block::

        iterate_rows = functools.partial(w.statement_execution.iterate_rows, warehouse_id, catalog='samples')
        for row in iterate_rows('SELECT * FROM nyctaxi.trips LIMIT 10'):
            pickup_time, dropoff_time = row[0], row[1]
            pickup_zip = row.pickup_zip
            dropoff_zip = row['dropoff_zip']
            all_fields = row.as_dict()
            print(f'{pickup_zip}@{pickup_time} -> {dropoff_zip}@{dropoff_time}: {all_fields}')

    When you only need to execute the query and have no need to iterate over results, use the :py:meth:`execute`.

    .. code-block::

        w.statement_execution.execute(warehouse_id, 'CREATE TABLE foo AS SELECT * FROM range(10)')

    Applications, that need to a more traditional SQL Python APIs with cursors, efficient data transfer of hundreds of
    megabytes or gigabytes of data serialized in Apache Arrow format, and low result fetching latency, should use
    the stateful Databricks SQL Connector for Python.
    

    .. py:method:: cancel_execution(statement_id)

        Cancel statement execution.
        
        Requests that an executing statement be canceled. Callers must poll for status to see the terminal
        state.
        
        :param statement_id: str
        
        
        

    .. py:method:: execute(warehouse_id, statement [, byte_limit, catalog, schema, timeout])

        Usage:

        .. code-block::

            import os
            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            table_name = f'sdk-{time.time_ns()}'
            
            created_catalog = w.catalogs.create(name=f'sdk-{time.time_ns()}')
            
            created_schema = w.schemas.create(name=f'sdk-{time.time_ns()}', catalog_name=created_catalog.name)
            
            _ = w.statement_execution.execute(warehouse_id=os.environ["TEST_DEFAULT_WAREHOUSE_ID"],
                                              catalog=created_catalog.name,
                                              schema=created_schema.name,
                                              statement="CREATE TABLE %s AS SELECT 2+2 as four" % (table_name)).result()
            
            # cleanup
            w.schemas.delete(full_name=created_schema.full_name)
            w.catalogs.delete(name=created_catalog.name, force=True)

        (Experimental) Execute a SQL statement and block until results are ready,
        including starting the warehouse if needed.

        This is a high-level implementation that works with fetching records in JSON format.
        It can be considered as a quick way to run SQL queries by just depending on
        Databricks SDK for Python without the need of any other compiled library dependencies.

        This method is a higher-level wrapper over :py:meth:`execute_statement` and fetches results
        in JSON format through the external link disposition, with client-side polling until
        the statement succeeds in execution. Whenever the statement is failed, cancelled, or
        closed, this method raises `DatabricksError` with the state message and the relevant
        error code.

        To seamlessly iterate over the rows from query results, please use :py:meth:`iterate_rows`.

        :param warehouse_id: str
          Warehouse upon which to execute a statement.
        :param statement: str
          SQL statement to execute
        :param byte_limit: int (optional)
          Applies the given byte limit to the statement's result size. Byte counts are based on internal
          representations and may not match measurable sizes in the JSON format.
        :param catalog: str (optional)
          Sets default catalog for statement execution, similar to `USE CATALOG` in SQL.
        :param schema: str (optional)
          Sets default schema for statement execution, similar to `USE SCHEMA` in SQL.
        :param timeout: timedelta (optional)
          Timeout after which the query is cancelled. If timeout is less than 50 seconds,
          it is handled on the server side. If the timeout is greater than 50 seconds,
          Databricks SDK for Python cancels the statement execution and throws `TimeoutError`.
        :return: ExecuteStatementResponse
        

    .. py:method:: execute_statement( [, byte_limit, catalog, disposition, format, on_wait_timeout, parameters, row_limit, schema, statement, wait_timeout, warehouse_id])

        Execute a SQL statement.
        
        Execute a SQL statement, and if flagged as such, await its result for a specified time.
        
        :param byte_limit: int (optional)
          Applies the given byte limit to the statement's result size. Byte counts are based on internal
          representations and may not match measurable sizes in the requested `format`.
        :param catalog: str (optional)
          Sets default catalog for statement execution, similar to [`USE CATALOG`] in SQL.
          
          [`USE CATALOG`]: https://docs.databricks.com/sql/language-manual/sql-ref-syntax-ddl-use-catalog.html
        :param disposition: :class:`Disposition` (optional)
          The fetch disposition provides two modes of fetching results: `INLINE` and `EXTERNAL_LINKS`.
          
          Statements executed with `INLINE` disposition will return result data inline, in `JSON_ARRAY`
          format, in a series of chunks. If a given statement produces a result set with a size larger than 16
          MiB, that statement execution is aborted, and no result set will be available.
          
          **NOTE** Byte limits are computed based upon internal representations of the result set data, and
          may not match the sizes visible in JSON responses.
          
          Statements executed with `EXTERNAL_LINKS` disposition will return result data as external links:
          URLs that point to cloud storage internal to the workspace. Using `EXTERNAL_LINKS` disposition
          allows statements to generate arbitrarily sized result sets for fetching up to 100 GiB. The
          resulting links have two important properties:
          
          1. They point to resources _external_ to the Databricks compute; therefore any associated
          authentication information (typically a personal access token, OAuth token, or similar) _must be
          removed_ when fetching from these links.
          
          2. These are presigned URLs with a specific expiration, indicated in the response. The behavior when
          attempting to use an expired link is cloud specific.
        :param format: :class:`Format` (optional)
          Statement execution supports three result formats: `JSON_ARRAY` (default), `ARROW_STREAM`, and
          `CSV`.
          
          When specifying `format=JSON_ARRAY`, result data will be formatted as an array of arrays of values,
          where each value is either the *string representation* of a value, or `null`. For example, the
          output of `SELECT concat('id-', id) AS strCol, id AS intCol, null AS nullCol FROM range(3)` would
          look like this:
          
          ``` [ [ "id-1", "1", null ], [ "id-2", "2", null ], [ "id-3", "3", null ], ] ```
          
          `JSON_ARRAY` is supported with `INLINE` and `EXTERNAL_LINKS` dispositions.
          
          `INLINE` `JSON_ARRAY` data can be found at the path `StatementResponse.result.data_array`.
          
          For `EXTERNAL_LINKS` `JSON_ARRAY` results, each URL points to a file in cloud storage that contains
          compact JSON with no indentation or extra whitespace.
          
          When specifying `format=ARROW_STREAM`, each chunk in the result will be formatted as Apache Arrow
          Stream. See the [Apache Arrow streaming format].
          
          IMPORTANT: The format `ARROW_STREAM` is supported only with `EXTERNAL_LINKS` disposition.
          
          When specifying `format=CSV`, each chunk in the result will be a CSV according to [RFC 4180]
          standard. All the columns values will have *string representation* similar to the `JSON_ARRAY`
          format, and `null` values will be encoded as “null”. Only the first chunk in the result would
          contain a header row with column names. For example, the output of `SELECT concat('id-', id) AS
          strCol, id AS intCol, null as nullCol FROM range(3)` would look like this:
          
          ``` strCol,intCol,nullCol id-1,1,null id-2,2,null id-3,3,null ```
          
          IMPORTANT: The format `CSV` is supported only with `EXTERNAL_LINKS` disposition.
          
          [Apache Arrow streaming format]: https://arrow.apache.org/docs/format/Columnar.html#ipc-streaming-format
          [RFC 4180]: https://www.rfc-editor.org/rfc/rfc4180
        :param on_wait_timeout: :class:`TimeoutAction` (optional)
          When in synchronous mode with `wait_timeout > 0s` it determines the action taken when the timeout is
          reached:
          
          `CONTINUE` → the statement execution continues asynchronously and the call returns a statement ID
          immediately.
          
          `CANCEL` → the statement execution is canceled and the call returns immediately with a `CANCELED`
          state.
        :param parameters: List[:class:`StatementParameterListItem`] (optional)
          A list of parameters to pass into a SQL statement containing parameter markers. A parameter consists
          of a name, a value, and optionally a type. To represent a NULL value, the `value` field may be
          omitted. If the `type` field is omitted, the value is interpreted as a string.
          
          If the type is given, parameters will be checked for type correctness according to the given type. A
          value is correct if the provided string can be converted to the requested type using the `cast`
          function. The exact semantics are described in the section [`cast` function] of the SQL language
          reference.
          
          For example, the following statement contains two parameters, `my_id` and `my_date`:
          
          SELECT * FROM my_table WHERE name = :my_name AND date = :my_date
          
          The parameters can be passed in the request body as follows:
          
          { ..., "statement": "SELECT * FROM my_table WHERE name = :my_name AND date = :my_date",
          "parameters": [ { "name": "my_name", "value": "the name" }, { "name": "my_date", "value":
          "2020-01-01", "type": "DATE" } ] }
          
          Currently, positional parameters denoted by a `?` marker are not supported by the SQL Statement
          Execution API.
          
          Also see the section [Parameter markers] of the SQL language reference.
          
          [Parameter markers]: https://docs.databricks.com/sql/language-manual/sql-ref-parameter-marker.html
          [`cast` function]: https://docs.databricks.com/sql/language-manual/functions/cast.html
        :param row_limit: int (optional)
          Applies the given row limit to the statement's result set with identical semantics as the SQL
          `LIMIT` clause.
        :param schema: str (optional)
          Sets default schema for statement execution, similar to [`USE SCHEMA`] in SQL.
          
          [`USE SCHEMA`]: https://docs.databricks.com/sql/language-manual/sql-ref-syntax-ddl-use-schema.html
        :param statement: str (optional)
          SQL statement to execute
        :param wait_timeout: str (optional)
          The time in seconds the API service will wait for the statement's result set as `Ns`, where `N` can
          be set to 0 or to a value between 5 and 50. When set to '0s' the statement will execute in
          asynchronous mode.
        :param warehouse_id: str (optional)
          Warehouse upon which to execute a statement. See also [What are SQL
          warehouses?](/sql/admin/warehouse-type.html)
        
        :returns: :class:`ExecuteStatementResponse`
        

    .. py:method:: get_statement(statement_id)

        Get status, manifest, and result first chunk.
        
        This request can be used to poll for the statement's status. When the `status.state` field is
        `SUCCEEDED` it will also return the result manifest and the first chunk of the result data. When the
        statement is in the terminal states `CANCELED`, `CLOSED` or `FAILED`, it returns HTTP 200 with the
        state set. After at least 12 hours in terminal state, the statement is removed from the warehouse and
        further calls will receive an HTTP 404 response.
        
        **NOTE** This call currently may take up to 5 seconds to get the latest status and result.
        
        :param statement_id: str
        
        :returns: :class:`GetStatementResponse`
        

    .. py:method:: get_statement_result_chunk_n(statement_id, chunk_index)

        Get result chunk by index.
        
        After the statement execution has `SUCCEEDED`, the result data can be fetched by chunks. Whereas the
        first chuck with `chunk_index=0` is typically fetched through a `get status` request, subsequent
        chunks can be fetched using a `get result` request. The response structure is identical to the nested
        `result` element described in the `get status` request, and similarly includes the `next_chunk_index`
        and `next_chunk_internal_link` fields for simple iteration through the result set.
        
        :param statement_id: str
        :param chunk_index: int
        
        :returns: :class:`ResultData`
        

    .. py:method:: iterate_rows(warehouse_id, statement [, byte_limit, catalog, schema, timeout])

        Usage:

        .. code-block::

            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            all_warehouses = w.warehouses.list()
            assert len(w.warehouses.list()) > 0, 'at least one SQL warehouse required'
            warehouse_id = all_warehouses[0].id
            
            for (pickup_zip, dropoff_zip) in w.statement_execution.iterate_rows(
                    warehouse_id, 'SELECT pickup_zip, dropoff_zip FROM nyctaxi.trips LIMIT 10',
                    catalog='samples'):
                print(f'pickup_zip={pickup_zip}, dropoff_zip={dropoff_zip}')

        (Experimental) Execute a query and iterate over all available records.

        This method is a wrapper over :py:meth:`execute` with the handling of chunked result
        processing and deserialization of those into separate rows, which are yielded from
        a returned iterator. Every row API resembles those of :class:`pyspark.sql.Row`,
        but full compatibility is not the goal of this implementation.

        .. code-block::

            iterate_rows = functools.partial(w.statement_execution.iterate_rows, warehouse_id, catalog='samples')
            for row in iterate_rows('SELECT * FROM nyctaxi.trips LIMIT 10'):
                pickup_time, dropoff_time = row[0], row[1]
                pickup_zip = row.pickup_zip
                dropoff_zip = row['dropoff_zip']
                all_fields = row.as_dict()
                print(f'{pickup_zip}@{pickup_time} -> {dropoff_zip}@{dropoff_time}: {all_fields}')

        :param warehouse_id: str
          Warehouse upon which to execute a statement.
        :param statement: str
          SQL statement to execute
        :param byte_limit: int (optional)
          Applies the given byte limit to the statement's result size. Byte counts are based on internal
          representations and may not match measurable sizes in the JSON format.
        :param catalog: str (optional)
          Sets default catalog for statement execution, similar to `USE CATALOG` in SQL.
        :param schema: str (optional)
          Sets default schema for statement execution, similar to `USE SCHEMA` in SQL.
        :param timeout: timedelta (optional)
          Timeout after which the query is cancelled. If timeout is less than 50 seconds,
          it is handled on the server side. If the timeout is greater than 50 seconds,
          Databricks SDK for Python cancels the statement execution and throws `TimeoutError`.
        :return: Iterator[Row]
        