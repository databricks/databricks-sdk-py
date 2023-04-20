def test_moving_dbfs_file_to_local_dir(config, tmp_path, mocker):
    from databricks.sdk import WorkspaceClient
    from databricks.sdk.service.files import FileInfo, ReadResponse

    get_status = mocker.patch('databricks.sdk.service.files.DbfsAPI.get_status',
                              return_value=FileInfo(path='a', is_dir=False, file_size=4))

    def fake_read(path: str, *, length: int = None, offset: int = None):
        assert path == 'a'
        assert length == 1048576
        if not offset:
            return ReadResponse(bytes_read=4, data='aGVsbG8=')
        return ReadResponse(bytes_read=0)

    mocker.patch('databricks.sdk.service.files.DbfsAPI.read', wraps=fake_read)
    delete = mocker.patch('databricks.sdk.service.files.DbfsAPI.delete')

    w = WorkspaceClient(config=config)
    w.dbfs.move_('a', f'file:{tmp_path}', recursive=True)

    get_status.assert_called_with('a')
    delete.assert_called_with('a', recursive=True)

    with (tmp_path / 'a').open('rb') as f:
        assert f.read() == b'hello'


def test_moving_local_dir_to_dbfs(config, tmp_path, mocker):
    from databricks.sdk import WorkspaceClient
    from databricks.sdk.core import DatabricksError
    from databricks.sdk.service.files import CreateResponse

    with (tmp_path / 'a').open('wb') as f:
        f.write(b'hello')

    mocker.patch('databricks.sdk.service.files.DbfsAPI.create', return_value=CreateResponse(123))

    def fake(path: str):
        assert path == 'a'
        raise DatabricksError('nope', error_code='RESOURCE_DOES_NOT_EXIST')

    mocker.patch('databricks.sdk.service.files.DbfsAPI.get_status', wraps=fake)
    add_block = mocker.patch('databricks.sdk.service.files.DbfsAPI.add_block')
    close = mocker.patch('databricks.sdk.service.files.DbfsAPI.close')

    w = WorkspaceClient(config=config)
    w.dbfs.move_(f'file:{tmp_path}', 'a', recursive=True)

    close.assert_called_with(123)
    add_block.assert_called_with(123, 'aGVsbG8=')
    assert not (tmp_path / 'a').exists()
