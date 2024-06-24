``w.statement_execution``: Statement Execution
==============================================
.. currentmodule:: databricks.sdk.service.sql

.. py:class:: StatementExecutionAPI

    The Databricks SQL Statement Execution API can be used to execute SQL statements on a SQL warehouse and
    fetch the result.
    
    **Getting started**
    
    We suggest beginning with the [Databricks SQL Statement Execution API tutorial].
    
    **Overview of statement execution and result fetching**
    
    Statement execution begins by issuing a :method:statementexecution/executeStatement request with a valid
    SQL statement and warehouse ID, along with optional parameters such as the data catalog and output format.
    If no other parameters are specified, the server will wait for up to 10s before returning a response. If
    the statement has completed within this timespan, the response will include the result data as a JSON
    array and metadata. Otherwise, if no result is available after the 10s timeout expired, the response will
    provide the statement ID that can be used to poll for results by using a
    :method:statementexecution/getStatement request.
    
    You can specify whether the call should behave synchronously, asynchronously or start synchronously with a
    fallback to asynchronous execution. This is controlled with the `wait_timeout` and `on_wait_timeout`
    settings. If `wait_timeout` is set between 5-50 seconds (default: 10s), the call waits for results up to
    the specified timeout; when set to `0s`, the call is asynchronous and responds immediately with a
    statement ID. The `on_wait_timeout` setting specifies what should happen when the timeout is reached while
    the statement execution has not yet finished. This can be set to either `CONTINUE`, to fallback to
    asynchronous mode, or it can be set to `CANCEL`, which cancels the statement.
    
    In summary: - Synchronous mode - `wait_timeout=30s` and `on_wait_timeout=CANCEL` - The call waits up to 30
    seconds; if the statement execution finishes within this time, the result data is returned directly in the
    response. If the execution takes longer than 30 seconds, the execution is canceled and the call returns
    with a `CANCELED` state. - Asynchronous mode - `wait_timeout=0s` (`on_wait_timeout` is ignored) - The call
    doesn't wait for the statement to finish but returns directly with a statement ID. The status of the
    statement execution can be polled by issuing :method:statementexecution/getStatement with the statement
    ID. Once the execution has succeeded, this call also returns the result and metadata in the response. -
    Hybrid mode (default) - `wait_timeout=10s` and `on_wait_timeout=CONTINUE` - The call waits for up to 10
    seconds; if the statement execution finishes within this time, the result data is returned directly in the
    response. If the execution takes longer than 10 seconds, a statement ID is returned. The statement ID can
    be used to fetch status and results in the same way as in the asynchronous mode.
    
    Depending on the size, the result can be split into multiple chunks. If the statement execution is
    successful, the statement response contains a manifest and the first chunk of the result. The manifest
    contains schema information and provides metadata for each chunk in the result. Result chunks can be
    retrieved by index with :method:statementexecution/getStatementResultChunkN which may be called in any
    order and in parallel. For sequential fetching, each chunk, apart from the last, also contains a
    `next_chunk_index` and `next_chunk_internal_link` that point to the next chunk.
    
    A statement can be canceled with :method:statementexecution/cancelExecution.
    
    **Fetching result data: format and disposition**
    
    To specify the format of the result data, use the `format` field, which can be set to one of the following
    options: `JSON_ARRAY` (JSON), `ARROW_STREAM` ([Apache Arrow Columnar]), or `CSV`.
    
    There are two ways to receive statement results, controlled by the `disposition` setting, which can be
    either `INLINE` or `EXTERNAL_LINKS`:
    
    - `INLINE`: In this mode, the result data is directly included in the response. It's best suited for
    smaller results. This mode can only be used with the `JSON_ARRAY` format.
    
    - `EXTERNAL_LINKS`: In this mode, the response provides links that can be used to download the result data
    in chunks separately. This approach is ideal for larger results and offers higher throughput. This mode
    can be used with all the formats: `JSON_ARRAY`, `ARROW_STREAM`, and `CSV`.
    
    By default, the API uses `format=JSON_ARRAY` and `disposition=INLINE`.
    
    **Limits and limitations**
    
    Note: The byte limit for INLINE disposition is based on internal storage metrics and will not exactly
    match the byte count of the actual payload.
    
    - Statements with `disposition=INLINE` are limited to 25 MiB and will fail when this limit is exceeded. -
    Statements with `disposition=EXTERNAL_LINKS` are limited to 100 GiB. Result sets larger than this limit
    will be truncated. Truncation is indicated by the `truncated` field in the result manifest. - The maximum
    query text size is 16 MiB. - Cancelation might silently fail. A successful response from a cancel request
    indicates that the cancel request was successfully received and sent to the processing engine. However, an
    outstanding statement might have already completed execution when the cancel request arrives. Polling for
    status until a terminal state is reached is a reliable way to determine the final state. - Wait timeouts
    are approximate, occur server-side, and cannot account for things such as caller delays and network
    latency from caller to service. - The system will auto-close a statement after one hour if the client
    stops polling and thus you must poll at least once an hour. - The results are only available for one hour
    after success; polling does not extend this.
    
    [Apache Arrow Columnar]: https://arrow.apache.org/overview/
    [Databricks SQL Statement Execution API tutorial]: https://docs.databricks.com/sql/api/sql-execution-tutorial.html

    .. py:method:: cancel_execution(statement_id: str)

        Cancel statement execution.
        
        Requests that an executing statement be canceled. Callers must poll for status to see the terminal
        state.
        
        :param statement_id: str
          The statement ID is returned upon successfully submitting a SQL statement, and is a required
          reference for all subsequent calls.
        
        
        

    .. py:method:: execute_statement(statement: str, warehouse_id: str [, byte_limit: Optional[int], catalog: Optional[str], disposition: Optional[Disposition], format: Optional[Format], on_wait_timeout: Optional[ExecuteStatementRequestOnWaitTimeout], parameters: Optional[List[StatementParameterListItem]], row_limit: Optional[int], schema: Optional[str], wait_timeout: Optional[str]]) -> ExecuteStatementResponse

        Execute a SQL statement.
        
        :param statement: str
          The SQL statement to execute. The statement can optionally be parameterized, see `parameters`.
        :param warehouse_id: str
          Warehouse upon which to execute a statement. See also [What are SQL warehouses?]
          
          [What are SQL warehouses?]: https://docs.databricks.com/sql/admin/warehouse-type.html
        :param byte_limit: int (optional)
          Applies the given byte limit to the statement's result size. Byte counts are based on internal data
          representations and might not match the final size in the requested `format`. If the result was
          truncated due to the byte limit, then `truncated` in the response is set to `true`. When using
          `EXTERNAL_LINKS` disposition, a default `byte_limit` of 100 GiB is applied if `byte_limit` is not
          explcitly set.
        :param catalog: str (optional)
          Sets default catalog for statement execution, similar to [`USE CATALOG`] in SQL.
          
          [`USE CATALOG`]: https://docs.databricks.com/sql/language-manual/sql-ref-syntax-ddl-use-catalog.html
        :param disposition: :class:`Disposition` (optional)
          The fetch disposition provides two modes of fetching results: `INLINE` and `EXTERNAL_LINKS`.
          
          Statements executed with `INLINE` disposition will return result data inline, in `JSON_ARRAY`
          format, in a series of chunks. If a given statement produces a result set with a size larger than 25
          MiB, that statement execution is aborted, and no result set will be available.
          
          **NOTE** Byte limits are computed based upon internal representations of the result set data, and
          might not match the sizes visible in JSON responses.
          
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
          
          Important: The formats `ARROW_STREAM` and `CSV` are supported only with `EXTERNAL_LINKS`
          disposition. `JSON_ARRAY` is supported in `INLINE` and `EXTERNAL_LINKS` disposition.
          
          When specifying `format=JSON_ARRAY`, result data will be formatted as an array of arrays of values,
          where each value is either the *string representation* of a value, or `null`. For example, the
          output of `SELECT concat('id-', id) AS strCol, id AS intCol, null AS nullCol FROM range(3)` would
          look like this:
          
          ``` [ [ "id-1", "1", null ], [ "id-2", "2", null ], [ "id-3", "3", null ], ] ```
          
          When specifying `format=JSON_ARRAY` and `disposition=EXTERNAL_LINKS`, each chunk in the result
          contains compact JSON with no indentation or extra whitespace.
          
          When specifying `format=ARROW_STREAM` and `disposition=EXTERNAL_LINKS`, each chunk in the result
          will be formatted as Apache Arrow Stream. See the [Apache Arrow streaming format].
          
          When specifying `format=CSV` and `disposition=EXTERNAL_LINKS`, each chunk in the result will be a
          CSV according to [RFC 4180] standard. All the columns values will have *string representation*
          similar to the `JSON_ARRAY` format, and `null` values will be encoded as “null”. Only the first
          chunk in the result would contain a header row with column names. For example, the output of `SELECT
          concat('id-', id) AS strCol, id AS intCol, null as nullCol FROM range(3)` would look like this:
          
          ``` strCol,intCol,nullCol id-1,1,null id-2,2,null id-3,3,null ```
          
          [Apache Arrow streaming format]: https://arrow.apache.org/docs/format/Columnar.html#ipc-streaming-format
          [RFC 4180]: https://www.rfc-editor.org/rfc/rfc4180
        :param on_wait_timeout: :class:`ExecuteStatementRequestOnWaitTimeout` (optional)
          When `wait_timeout > 0s`, the call will block up to the specified time. If the statement execution
          doesn't finish within this time, `on_wait_timeout` determines whether the execution should continue
          or be canceled. When set to `CONTINUE`, the statement execution continues asynchronously and the
          call returns a statement ID which can be used for polling with
          :method:statementexecution/getStatement. When set to `CANCEL`, the statement execution is canceled
          and the call returns with a `CANCELED` state.
        :param parameters: List[:class:`StatementParameterListItem`] (optional)
          A list of parameters to pass into a SQL statement containing parameter markers. A parameter consists
          of a name, a value, and optionally a type. To represent a NULL value, the `value` field may be
          omitted or set to `null` explicitly. If the `type` field is omitted, the value is interpreted as a
          string.
          
          If the type is given, parameters will be checked for type correctness according to the given type. A
          value is correct if the provided string can be converted to the requested type using the `cast`
          function. The exact semantics are described in the section [`cast` function] of the SQL language
          reference.
          
          For example, the following statement contains two parameters, `my_name` and `my_date`:
          
          SELECT * FROM my_table WHERE name = :my_name AND date = :my_date
          
          The parameters can be passed in the request body as follows:
          
          { ..., "statement": "SELECT * FROM my_table WHERE name = :my_name AND date = :my_date",
          "parameters": [ { "name": "my_name", "value": "the name" }, { "name": "my_date", "value":
          "2020-01-01", "type": "DATE" } ] }
          
          Currently, positional parameters denoted by a `?` marker are not supported by the Databricks SQL
          Statement Execution API.
          
          Also see the section [Parameter markers] of the SQL language reference.
          
          [Parameter markers]: https://docs.databricks.com/sql/language-manual/sql-ref-parameter-marker.html
          [`cast` function]: https://docs.databricks.com/sql/language-manual/functions/cast.html
        :param row_limit: int (optional)
          Applies the given row limit to the statement's result set, but unlike the `LIMIT` clause in SQL, it
          also sets the `truncated` field in the response to indicate whether the result was trimmed due to
          the limit or not.
        :param schema: str (optional)
          Sets default schema for statement execution, similar to [`USE SCHEMA`] in SQL.
          
          [`USE SCHEMA`]: https://docs.databricks.com/sql/language-manual/sql-ref-syntax-ddl-use-schema.html
        :param wait_timeout: str (optional)
          The time in seconds the call will wait for the statement's result set as `Ns`, where `N` can be set
          to 0 or to a value between 5 and 50.
          
          When set to `0s`, the statement will execute in asynchronous mode and the call will not wait for the
          execution to finish. In this case, the call returns directly with `PENDING` state and a statement ID
          which can be used for polling with :method:statementexecution/getStatement.
          
          When set between 5 and 50 seconds, the call will behave synchronously up to this timeout and wait
          for the statement execution to finish. If the execution finishes within this time, the call returns
          immediately with a manifest and result data (or a `FAILED` state in case of an execution error). If
          the statement takes longer to execute, `on_wait_timeout` determines what should happen after the
          timeout is reached.
        
        :returns: :class:`ExecuteStatementResponse`
        

    .. py:method:: get_statement(statement_id: str) -> GetStatementResponse

        Get status, manifest, and result first chunk.
        
        This request can be used to poll for the statement's status. When the `status.state` field is
        `SUCCEEDED` it will also return the result manifest and the first chunk of the result data. When the
        statement is in the terminal states `CANCELED`, `CLOSED` or `FAILED`, it returns HTTP 200 with the
        state set. After at least 12 hours in terminal state, the statement is removed from the warehouse and
        further calls will receive an HTTP 404 response.
        
        **NOTE** This call currently might take up to 5 seconds to get the latest status and result.
        
        :param statement_id: str
          The statement ID is returned upon successfully submitting a SQL statement, and is a required
          reference for all subsequent calls.
        
        :returns: :class:`GetStatementResponse`
        

    .. py:method:: get_statement_result_chunk_n(statement_id: str, chunk_index: int) -> ResultData

        Get result chunk by index.
        
        After the statement execution has `SUCCEEDED`, this request can be used to fetch any chunk by index.
        Whereas the first chunk with `chunk_index=0` is typically fetched with
        :method:statementexecution/executeStatement or :method:statementexecution/getStatement, this request
        can be used to fetch subsequent chunks. The response structure is identical to the nested `result`
        element described in the :method:statementexecution/getStatement request, and similarly includes the
        `next_chunk_index` and `next_chunk_internal_link` fields for simple iteration through the result set.
        
        :param statement_id: str
          The statement ID is returned upon successfully submitting a SQL statement, and is a required
          reference for all subsequent calls.
        :param chunk_index: int
        
        :returns: :class:`ResultData`
        