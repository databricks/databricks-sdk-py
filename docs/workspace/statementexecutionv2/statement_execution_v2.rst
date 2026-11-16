``w.statement_execution_v2``: StatementExecution.v2
===================================================
.. currentmodule:: databricks.sdk.service.statementexecutionv2

.. py:class:: StatementExecutionV2API

    The Statement Execution API v2 can be used to execute SQL statements on a SQL warehouse and fetch the
    result. It works the same as the Statement Execution API (v1), except that ``warehouse_id`` is a path
    parameter on every call, including polling, fetching result chunks, and canceling. Routing on the
    warehouse ID gives lower latency and higher concurrency.

    Version 2 currently supports `Lakehouse//RT
    <https://docs.databricks.com/compute/sql-warehouse/real-time.html>`__ warehouses only. For other warehouse
    types, use the Statement Execution API (v1). You can also run statements on Lakehouse//RT warehouses with
    version 1, but version 2 is optimized for them.

    .. py:method:: cancel_statement(warehouse_id: str, statement_id: str) -> CancelStatementResponse

        Requests that an executing statement be canceled. Callers must poll for status to see the terminal
        state. The cancel response is empty; receiving a response indicates successful receipt.

        :param warehouse_id: str
          The ID of the SQL warehouse that ran the statement.
        :param statement_id: str
          The statement ID is returned upon successfully submitting a SQL statement, and is a required
          reference for all subsequent calls.

        :returns: :class:`CancelStatementResponse`
        

    .. py:method:: execute_statement(warehouse_id: str, statement: str [, byte_limit: Optional[int], catalog: Optional[str], disposition: Optional[FetchDisposition], format: Optional[Format], on_wait_timeout: Optional[TimeoutAction], parameters: Optional[List[StatementParameter]], query_tags: Optional[List[QueryTag]], row_limit: Optional[int], schema: Optional[str], wait_timeout: Optional[str]]) -> StatementResponse

        Execute a SQL statement and optionally await its results for a specified time.

        **Use case: small result sets with INLINE + JSON_ARRAY**

        For flows that generate small and predictable result sets (<= 25 MiB), ``INLINE`` responses of
        ``JSON_ARRAY`` result data are typically the simplest way to execute and fetch result data.

        **Use case: large result sets with EXTERNAL_LINKS**

        Using ``EXTERNAL_LINKS`` to fetch result data allows you to fetch large result sets efficiently. The
        main differences from using ``INLINE`` disposition are that the result data is accessed with
        short-lived cloud-storage URLs, and that there are 3 supported formats: ``JSON_ARRAY``,
        ``ARROW_STREAM`` and ``CSV`` compared to only ``JSON_ARRAY`` with ``INLINE``.

        **External-link URLs**

        External links point to data stored within your workspace's internal cloud storage. The URLs are valid
        for only a short period, <= 15 minutes. Alongside each ``external_link`` is an expiration field
        indicating the time at which the URL is no longer valid. In ``EXTERNAL_LINKS`` mode, chunks can be
        resolved and fetched multiple times and in parallel.

        **Warning: Databricks strongly recommends that you protect the URLs that are returned by the
        ``EXTERNAL_LINKS`` disposition.**

        When you use the ``EXTERNAL_LINKS`` disposition, a short-lived cloud-storage URL is generated to
        download the results. The URL contains temporary access credentials, so protect it and do not set an
        ``Authorization`` header in the download request.

        The ``EXTERNAL_LINKS`` disposition can be disabled upon request by creating a `support case
        <https://docs.databricks.com/resources/support.html>`__.

        See also `Security best practices
        <https://docs.databricks.com/sql/admin/sql-execution-tutorial.html#security-best-practices>`__.

        StatementResponse contains ``statement_id`` and ``status``; other fields might be absent or present
        depending on context. If the SQL warehouse fails to execute the provided statement, a 200 response is
        returned with ``status.state`` set to ``FAILED`` (in contrast to a failure when accepting the request,
        which results in a non-200 response). Details of the error can be found at ``status.error`` in case of
        execution failures.

        :param warehouse_id: str
          The ID of the SQL warehouse to run the statement on. Currently, only `Lakehouse//RT
          <https://docs.databricks.com/compute/sql-warehouse/real-time.html>`__ warehouses are supported. See
          also `What are SQL warehouses? <https://docs.databricks.com/sql/admin/warehouse-type.html>`__.
        :param statement: str
          The SQL statement to execute. The statement can optionally be parameterized, see ``parameters``. The
          maximum query text size is 16 MiB.
        :param byte_limit: int (optional)
          Applies the given byte limit to the statement's result size. Byte counts are based on internal data
          representations and might not match the final size in the requested ``format``. If the result was
          truncated due to the byte limit, then ``truncated`` in the response is set to ``true``. When using
          ``EXTERNAL_LINKS`` disposition, a default ``byte_limit`` of 100 GiB is applied if ``byte_limit`` is
          not explicitly set.
        :param catalog: str (optional)
          Sets default catalog for statement execution, similar to `USE CATALOG
          <https://docs.databricks.com/sql/language-manual/sql-ref-syntax-ddl-use-catalog.html>`__ in SQL.
        :param disposition: :class:`FetchDisposition` (optional)
          The fetch disposition provides two modes of fetching results: ``INLINE`` and ``EXTERNAL_LINKS``.

          Statements executed with ``INLINE`` disposition will return result data inline, in ``JSON_ARRAY``
          format, in a series of chunks. If a given statement produces a result set with a size larger than 25
          MiB, that statement execution is aborted, and no result set will be available.

          **NOTE** Byte limits are computed based upon internal representations of the result set data, and
          might not match the sizes visible in JSON responses.

          Statements executed with ``EXTERNAL_LINKS`` disposition will return result data as external links:
          URLs that point to cloud storage internal to the workspace. Using ``EXTERNAL_LINKS`` disposition
          allows statements to generate arbitrarily sized result sets for fetching up to 100 GiB. The
          resulting links have two important properties:

          1. They point to resources *external* to the Databricks compute; therefore any associated
             authentication information (typically a personal access token, OAuth token, or similar) *must be
             removed* when fetching from these links.
          2. These are short-lived cloud-storage URLs with a specific expiration, indicated in the response.
             The behavior when attempting to use an expired link is cloud specific.
        :param format: :class:`Format` (optional)
          Statement execution supports three result formats: ``JSON_ARRAY``, ``ARROW_STREAM``, and ``CSV``.
          Set ``format`` explicitly: on Lakehouse//RT warehouses, an omitted ``format`` with the ``INLINE``
          disposition currently returns Arrow data rather than ``JSON_ARRAY``.

          Important: The formats ``ARROW_STREAM`` and ``CSV`` are supported only with ``EXTERNAL_LINKS``
          disposition. ``JSON_ARRAY`` is supported in ``INLINE`` and ``EXTERNAL_LINKS`` disposition.

          When specifying ``format=JSON_ARRAY``, result data will be formatted as an array of arrays of
          values, where each value is either the *string representation* of a value, or ``null``. For example,
          the output of ``SELECT concat('id-', id) AS strCol, id AS intCol, null AS nullCol FROM range(3)``
          would look like this:

          .. code-block::

             [
             [ "id-1", "1", null ],
             [ "id-2", "2", null ],
             [ "id-3", "3", null ],
             ]

          When specifying ``format=JSON_ARRAY`` and ``disposition=EXTERNAL_LINKS``, each chunk in the result
          contains compact JSON with no indentation or extra whitespace.

          When specifying ``format=ARROW_STREAM`` and ``disposition=EXTERNAL_LINKS``, each chunk in the result
          will be formatted as Apache Arrow Stream. See the `Apache Arrow streaming format
          <https://arrow.apache.org/docs/format/Columnar.html#ipc-streaming-format>`__.

          When specifying ``format=CSV`` and ``disposition=EXTERNAL_LINKS``, each chunk in the result will be
          a CSV according to `RFC 4180 <https://www.rfc-editor.org/rfc/rfc4180>`__ standard. All column values
          will have *string representation* similar to the ``JSON_ARRAY`` format, and ``null`` values will be
          encoded as “null”. Only the first chunk in the result would contain a header row with column
          names. For example, the output of ``SELECT concat('id-', id) AS strCol, id AS intCol, null as
          nullCol FROM range(3)`` would look like this:

          .. code-block::

             strCol,intCol,nullCol
             id-1,1,null
             id-2,2,null
             id-3,3,null
        :param on_wait_timeout: :class:`TimeoutAction` (optional)
          When ``wait_timeout > 0s``, the call will block up to the specified time. If the statement execution
          doesn't finish within this time, ``on_wait_timeout`` determines whether the execution should
          continue or be canceled. When set to ``CONTINUE``, the statement execution continues asynchronously
          and the call returns a statement ID which can be used for polling the statement status. When set to
          ``CANCEL``, the statement execution is canceled and the call returns with a ``CANCELED`` state.
          Lakehouse//RT warehouses currently don't support ``CANCEL``: the statement keeps running as with
          ``CONTINUE``.
        :param parameters: List[:class:`StatementParameter`] (optional)
          A list of parameters to pass into a SQL statement containing parameter markers. A parameter consists
          of a name, a value, and optionally a type. To represent a NULL value, the ``value`` field may be
          omitted or set to ``null`` explicitly. If the ``type`` field is omitted, the value is interpreted as
          a string.

          If the type is given, parameters will be checked for type correctness according to the given type. A
          value is correct if the provided string can be converted to the requested type using the ``cast``
          function. The exact semantics are described in the section `cast function
          <https://docs.databricks.com/sql/language-manual/functions/cast.html>`__ of the SQL language
          reference.

          For example, the following statement contains two parameters, ``my_name`` and ``my_date``:

          .. code-block::

             SELECT * FROM my_table WHERE name = :my_name AND date = :my_date

          The parameters can be passed in the request body as follows:

          ``{ ..., "statement": "SELECT * FROM my_table WHERE name = :my_name AND date = :my_date",
          "parameters": [ { "name": "my_name", "value": "the name" }, { "name": "my_date", "value":
          "2020-01-01", "type": "DATE" } ] }``

          Currently, positional parameters denoted by a ``?`` marker are not supported by the Databricks SQL
          Statement Execution API.

          Also see the section `Parameter markers
          <https://docs.databricks.com/sql/language-manual/sql-ref-parameter-marker.html>`__ of the SQL
          language reference.
        :param query_tags: List[:class:`QueryTag`] (optional)
          An array of query tags to annotate a SQL statement. A query tag consists of a non-empty key and,
          optionally, a value. To represent a NULL value, either omit the ``value`` field or manually set it
          to ``null`` or white space. Refer to the SQL language reference for the format specification of
          query tags. There's no significance to the order of tags. Only one value per key will be recorded. A
          sequence in excess of 20 query tags will be coerced to 20. Example:

          { ..., "query_tags": [ { "key": "team", "value": "eng" }, { "key": "some key only tag" } ] }
        :param row_limit: int (optional)
          Applies the given row limit to the statement's result set, but unlike the ``LIMIT`` clause in SQL,
          it also sets the ``truncated`` field in the response to indicate whether the result was trimmed due
          to the limit or not.
        :param schema: str (optional)
          Sets default schema for statement execution, similar to `USE SCHEMA
          <https://docs.databricks.com/sql/language-manual/sql-ref-syntax-ddl-use-schema.html>`__ in SQL.
        :param wait_timeout: str (optional)
          The time in seconds the call will wait for the statement's result set as ``Ns``, where ``N`` can be
          set to 0 or to a value between 5 and 50.

          When set to ``0s``, the statement will execute in asynchronous mode and the call will not wait for
          the execution to finish. In this case, the call returns directly with ``PENDING`` state and a
          statement ID which can be used for polling the statement status.

          When set between 5 and 50 seconds, the call will behave synchronously up to this timeout and wait
          for the statement execution to finish. If the execution finishes within this time, the call returns
          immediately with a manifest and result data (or a ``FAILED`` state in case of an execution error).
          If the statement takes longer to execute, ``on_wait_timeout`` determines what should happen after
          the timeout is reached.

        :returns: :class:`StatementResponse`
        

    .. py:method:: get_result_data(warehouse_id: str, statement_id: str, chunk_index: int) -> ResultData

        After the statement execution has ``SUCCEEDED``, this request can be used to fetch any chunk by index.
        Whereas the first chunk with ``chunk_index=0`` is typically fetched with the execute or the get-status
        request, this request can be used to fetch subsequent chunks. The response structure is identical to
        the nested ``result`` element of those responses, and similarly includes the ``next_chunk_index``
        field for simple iteration through the result set. Depending on ``disposition``, the response returns
        chunks of data either inline, or as links.

        :param warehouse_id: str
          The ID of the SQL warehouse that ran the statement.
        :param statement_id: str
          The statement ID is returned upon successfully submitting a SQL statement, and is a required
          reference for all subsequent calls.
        :param chunk_index: int
          The zero-based index of the result chunk to fetch.

        :returns: :class:`ResultData`
        

    .. py:method:: get_statement_result(warehouse_id: str, statement_id: str) -> StatementResponse

        This request can be used to poll for the statement's status. StatementResponse contains
        ``statement_id`` and ``status``; other fields might be absent or present depending on context. When
        the ``status.state`` field is ``SUCCEEDED`` it will also return the result manifest and the first
        chunk of the result data. When the statement is in the terminal states ``CANCELED``, ``CLOSED`` or
        ``FAILED``, it returns HTTP 200 with the state set. After at least 12 hours in a terminal state, the
        statement is removed from the warehouse and further calls will receive an HTTP 404 response.

        **NOTE** This call currently might take up to 5 seconds to get the latest status and result.

        :param warehouse_id: str
          The ID of the SQL warehouse that ran the statement.
        :param statement_id: str
          The statement ID is returned upon successfully submitting a SQL statement, and is a required
          reference for all subsequent calls.

        :returns: :class:`StatementResponse`
        