import base64
import datetime
import functools
import json
import logging
import random
import time
from datetime import timedelta
from typing import Any, Dict, Iterator, List, Optional

from databricks.sdk.core import DatabricksError
from databricks.sdk.service.sql import (ColumnInfoTypeName, Disposition,
                                        ExecuteStatementResponse, Format,
                                        StatementExecutionAPI, StatementState,
                                        StatementStatus)

_LOG = logging.getLogger("databricks.sdk")


class _RowCreator(tuple):

    def __new__(cls, fields):
        instance = super().__new__(cls, fields)
        return instance

    def __repr__(self):
        field_values = ", ".join(f"{field}={getattr(self, field)}" for field in self)
        return f"{self.__class__.__name__}({field_values})"


class Row(tuple):

    def __new__(cls, columns: List[str], values: List[Any]) -> 'Row':
        row = tuple.__new__(cls, values)
        row.__columns__ = columns
        return row

    # Python SDK convention
    def as_dict(self) -> Dict[str, any]:
        return dict(zip(self.__columns__, self))

    # PySpark convention
    asDict = as_dict

    # PySpark convention
    def __contains__(self, item):
        return item in self.__columns__

    def __getitem__(self, col):
        if isinstance(col, (int, slice)):
            return super().__getitem__(col)
        # if columns are named `2 + 2`, for example
        return self.__getattr__(col)

    def __getattr__(self, col):
        try:
            idx = self.__columns__.index(col)
            return self[idx]
        except IndexError:
            raise AttributeError(col)
        except ValueError:
            raise AttributeError(col)

    def __repr__(self):
        return f"Row({', '.join(f'{k}={v}' for (k, v) in zip(self.__columns__, self))})"


class StatementExecutionExt(StatementExecutionAPI):
    """
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
    """

    def __init__(self, api_client):
        super().__init__(api_client)
        self._type_converters = {
            ColumnInfoTypeName.ARRAY: json.loads,
            ColumnInfoTypeName.BINARY: base64.b64decode,
            ColumnInfoTypeName.BOOLEAN: bool,
            ColumnInfoTypeName.CHAR: str,
            ColumnInfoTypeName.DATE: self._parse_date,
            ColumnInfoTypeName.DOUBLE: float,
            ColumnInfoTypeName.FLOAT: float,
            ColumnInfoTypeName.INT: int,
            ColumnInfoTypeName.LONG: int,
            ColumnInfoTypeName.MAP: json.loads,
            ColumnInfoTypeName.NULL: lambda _: None,
            ColumnInfoTypeName.SHORT: int,
            ColumnInfoTypeName.STRING: str,
            ColumnInfoTypeName.STRUCT: json.loads,
            ColumnInfoTypeName.TIMESTAMP: self._parse_timestamp,
        }

    @staticmethod
    def _parse_date(value: str) -> datetime.date:
        year, month, day = value.split('-')
        return datetime.date(int(year), int(month), int(day))

    @staticmethod
    def _parse_timestamp(value: str) -> datetime.datetime:
        # make it work with Python 3.7 to 3.10 as well
        return datetime.datetime.fromisoformat(value.replace('Z', '+00:00'))

    @staticmethod
    def _raise_if_needed(status: StatementStatus):
        if status.state not in [StatementState.FAILED, StatementState.CANCELED, StatementState.CLOSED]:
            return
        err = status.error
        if err is not None:
            message = err.message.strip()
            error_code = err.error_code.value
            raise DatabricksError(message, error_code=error_code)
        raise DatabricksError(status.state.value)

    def execute(self,
                warehouse_id: str,
                statement: str,
                *,
                byte_limit: Optional[int] = None,
                catalog: Optional[str] = None,
                schema: Optional[str] = None,
                timeout: timedelta = timedelta(minutes=20),
                ) -> ExecuteStatementResponse:
        """(Experimental) Execute a SQL statement and block until results are ready,
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
        """
        # The wait_timeout field must be 0 seconds (disables wait),
        # or between 5 seconds and 50 seconds.
        wait_timeout = None
        if 5 <= timeout.total_seconds() <= 50:
            # set server-side timeout
            wait_timeout = f"{timeout.total_seconds()}s"

        _LOG.debug(f"Executing SQL statement: {statement}")

        # format is limited to Format.JSON_ARRAY, but other iterations may include ARROW_STREAM.
        immediate_response = self.execute_statement(warehouse_id=warehouse_id,
                                                    statement=statement,
                                                    catalog=catalog,
                                                    schema=schema,
                                                    disposition=Disposition.EXTERNAL_LINKS,
                                                    format=Format.JSON_ARRAY,
                                                    byte_limit=byte_limit,
                                                    wait_timeout=wait_timeout)

        if immediate_response.status.state == StatementState.SUCCEEDED:
            return immediate_response

        self._raise_if_needed(immediate_response.status)

        attempt = 1
        status_message = "polling..."
        deadline = time.time() + timeout.total_seconds()
        while time.time() < deadline:
            res = self.get_statement(immediate_response.statement_id)
            if res.status.state == StatementState.SUCCEEDED:
                return ExecuteStatementResponse(manifest=res.manifest,
                                                result=res.result,
                                                statement_id=res.statement_id,
                                                status=res.status)
            status_message = f"current status: {res.status.state.value}"
            self._raise_if_needed(res.status)
            sleep = attempt
            if sleep > 10:
                # sleep 10s max per attempt
                sleep = 10
            _LOG.debug(f"SQL statement {res.statement_id}: {status_message} (sleeping ~{sleep}s)")
            time.sleep(sleep + random.random())
            attempt += 1
        self.cancel_execution(immediate_response.statement_id)
        msg = f"timed out after {timeout}: {status_message}"
        raise TimeoutError(msg)

    def iterate_rows(self,
                     warehouse_id: str,
                     statement: str,
                     *,
                     byte_limit: Optional[int] = None,
                     catalog: Optional[str] = None,
                     schema: Optional[str] = None,
                     timeout: timedelta = timedelta(minutes=20),
                     ) -> Iterator[Row]:
        """(Experimental) Execute a query and iterate over all available records.

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
        """
        execute_response = self.execute(warehouse_id,
                                        statement,
                                        byte_limit=byte_limit,
                                        catalog=catalog,
                                        schema=schema,
                                        timeout=timeout)
        if execute_response.result.external_links is None:
            return []
        for row in self._iterate_external_disposition(execute_response):
            yield row

    def _result_schema(self, execute_response: ExecuteStatementResponse):
        col_names = []
        col_conv = []
        for col in execute_response.manifest.schema.columns:
            col_names.append(col.name)
            conv = self._type_converters.get(col.type_name, None)
            if conv is None:
                msg = f"{col.name} has no {col.type_name.value} converter"
                raise ValueError(msg)
            col_conv.append(conv)
        row_factory = functools.partial(Row, col_names)
        return row_factory, col_conv

    def _iterate_external_disposition(self, execute_response: ExecuteStatementResponse) -> Iterator[Row]:
        # ensure that we close the HTTP session after fetching the external links
        result_data = execute_response.result
        row_factory, col_conv = self._result_schema(execute_response)
        with self._api._new_session() as http:
            while True:
                for external_link in result_data.external_links:
                    response = http.get(external_link.external_link)
                    response.raise_for_status()
                    for data in response.json():
                        yield row_factory(col_conv[i](value) for i, value in enumerate(data))

                    if external_link.next_chunk_index is None:
                        return

                    result_data = self.get_statement_result_chunk_n(execute_response.statement_id,
                                                                    external_link.next_chunk_index)

    def _iterate_inline_disposition(self, execute_response: ExecuteStatementResponse) -> Iterator[Row]:
        result_data = execute_response.result
        row_factory, col_conv = self._result_schema(execute_response)
        while True:
            # case for Disposition.INLINE, where we get rows embedded into a response
            for data in result_data.data_array:
                # enumerate() + iterator + tuple constructor makes it more performant
                # on larger humber of records for Python, even though it's less
                # readable code.
                yield row_factory(col_conv[i](value) for i, value in enumerate(data))

            if result_data.next_chunk_index is None:
                return

            result_data = self.get_statement_result_chunk_n(execute_response.statement_id,
                                                            result_data.next_chunk_index)
