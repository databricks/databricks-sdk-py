import pytest

from databricks.sdk import WorkspaceClient
from databricks.sdk.service.sql import (ColumnInfo, ColumnInfoTypeName,
                                        Disposition, ExecuteStatementResponse,
                                        ExternalLink, Format,
                                        GetStatementResponse, ResultData,
                                        ResultManifest, ResultSchema,
                                        StatementState, StatementStatus,
                                        timedelta)


def test_execute_poll_succeeds(config, mocker):
    w = WorkspaceClient(config=config)

    execute_statement = mocker.patch('databricks.sdk.service.sql.StatementExecutionAPI.execute_statement',
                                     return_value=ExecuteStatementResponse(
                                         status=StatementStatus(state=StatementState.PENDING),
                                         statement_id='bcd',
                                     ))

    get_statement = mocker.patch('databricks.sdk.service.sql.StatementExecutionAPI.get_statement',
                                 return_value=GetStatementResponse(
                                     manifest=ResultManifest(),
                                     result=ResultData(byte_count=100500),
                                     statement_id='bcd',
                                     status=StatementStatus(state=StatementState.SUCCEEDED)))

    response = w.statement_execution.execute('abc', 'SELECT 2+2')

    assert response.status.state == StatementState.SUCCEEDED
    assert response.result.byte_count == 100500
    execute_statement.assert_called_with(warehouse_id='abc',
                                         statement='SELECT 2+2',
                                         disposition=Disposition.EXTERNAL_LINKS,
                                         format=Format.JSON_ARRAY,
                                         byte_limit=None,
                                         catalog=None,
                                         schema=None,
                                         wait_timeout=None)
    get_statement.assert_called_with('bcd')


def test_execute_poll_waits(config, mocker):
    w = WorkspaceClient(config=config)

    mocker.patch('databricks.sdk.service.sql.StatementExecutionAPI.execute_statement',
                 return_value=ExecuteStatementResponse(status=StatementStatus(state=StatementState.PENDING),
                                                       statement_id='bcd',
                                                       ))

    runs = []

    def _get_statement(statement_id):
        assert statement_id == 'bcd'
        if len(runs) == 0:
            runs.append(1)
            return GetStatementResponse(status=StatementStatus(state=StatementState.RUNNING),
                                        statement_id='bcd')

        return GetStatementResponse(manifest=ResultManifest(),
                                    result=ResultData(byte_count=100500),
                                    statement_id='bcd',
                                    status=StatementStatus(state=StatementState.SUCCEEDED))

    mocker.patch('databricks.sdk.service.sql.StatementExecutionAPI.get_statement', wraps=_get_statement)

    response = w.statement_execution.execute('abc', 'SELECT 2+2')

    assert response.status.state == StatementState.SUCCEEDED
    assert response.result.byte_count == 100500


def test_execute_poll_timeouts_on_client(config, mocker):
    w = WorkspaceClient(config=config)

    mocker.patch('databricks.sdk.service.sql.StatementExecutionAPI.execute_statement',
                 return_value=ExecuteStatementResponse(status=StatementStatus(state=StatementState.PENDING),
                                                       statement_id='bcd',
                                                       ))

    mocker.patch('databricks.sdk.service.sql.StatementExecutionAPI.get_statement',
                 return_value=GetStatementResponse(status=StatementStatus(state=StatementState.RUNNING),
                                                   statement_id='bcd'))

    cancel_execution = mocker.patch('databricks.sdk.service.sql.StatementExecutionAPI.cancel_execution')

    with pytest.raises(TimeoutError):
        w.statement_execution.execute('abc', 'SELECT 2+2', timeout=timedelta(seconds=1))

    cancel_execution.assert_called_with('bcd')


def test_fetch_all_no_chunks(config, mocker):
    w = WorkspaceClient(config=config)

    mocker.patch('databricks.sdk.service.sql.StatementExecutionAPI.execute_statement',
                 return_value=ExecuteStatementResponse(
                     status=StatementStatus(state=StatementState.SUCCEEDED),
                     manifest=ResultManifest(schema=ResultSchema(columns=[
                         ColumnInfo(name='id', type_name=ColumnInfoTypeName.INT),
                         ColumnInfo(name='now', type_name=ColumnInfoTypeName.TIMESTAMP),
                     ])),
                     result=ResultData(external_links=[ExternalLink(external_link='https://singed-url')]),
                     statement_id='bcd',
                 ))

    raw_response = mocker.Mock()
    raw_response.json = lambda: [["1", "2023-09-01T13:21:53Z"], ["2", "2023-09-01T13:21:53Z"]]

    http_get = mocker.patch('requests.sessions.Session.get', return_value=raw_response)

    rows = list(w.statement_execution.iterate_rows('abc', 'SELECT id, NOW() AS now FROM range(2)'))

    assert len(rows) == 2

    http_get.assert_called_with('https://singed-url')


def test_fetch_all_two_chunks(config, mocker):
    w = WorkspaceClient(config=config)

    mocker.patch('databricks.sdk.service.sql.StatementExecutionAPI.execute_statement',
                 return_value=ExecuteStatementResponse(
                     status=StatementStatus(state=StatementState.SUCCEEDED),
                     manifest=ResultManifest(schema=ResultSchema(columns=[
                         ColumnInfo(name='id', type_name=ColumnInfoTypeName.INT),
                         ColumnInfo(name='now', type_name=ColumnInfoTypeName.TIMESTAMP),
                     ])),
                     result=ResultData(
                         external_links=[ExternalLink(external_link='https://first', next_chunk_index=1)]),
                     statement_id='bcd',
                 ))

    next_chunk = mocker.patch(
        'databricks.sdk.service.sql.StatementExecutionAPI.get_statement_result_chunk_n',
        return_value=ResultData(external_links=[ExternalLink(external_link='https://second')]))

    raw_response = mocker.Mock()
    raw_response.json = lambda: [["1", "2023-09-01T13:21:53Z"], ["2", "2023-09-01T13:21:53Z"]]
    http_get = mocker.patch('requests.sessions.Session.get', return_value=raw_response)

    rows = list(w.statement_execution.iterate_rows('abc', 'SELECT id, NOW() AS now FROM range(2)'))

    assert len(rows) == 4

    assert [c.args for c in http_get.call_args_list] == [('https://first', ), ('https://second', )]
    next_chunk.assert_called_with('bcd', 1)
