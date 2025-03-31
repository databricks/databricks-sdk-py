import pytest

from databricks.sdk.databricks.errors import NotFound
from databricks.sdk.files.v2.mixin import (DbfsExt, _DbfsPath, _LocalPath,
                                           _VolumesPath)


def test_moving_dbfs_file_to_local_dir(config, tmp_path, mocker):
    from databricks.sdk.files.v2.client import DbfsClient
    from databricks.sdk.files.v2.files import FileInfo, ReadResponse

    get_status = mocker.patch(
        "databricks.sdk.files.v2.files.DbfsAPI.get_status",
        return_value=FileInfo(path="a", is_dir=False, file_size=4),
    )

    def fake_read(path: str, *, length: int = None, offset: int = None):
        assert path == "a"
        assert length == 1048576
        if not offset:
            return ReadResponse(bytes_read=4, data="aGVsbG8=")
        return ReadResponse(bytes_read=0)

    mocker.patch("databricks.sdk.files.v2.files.DbfsAPI.read", wraps=fake_read)
    delete = mocker.patch("databricks.sdk.files.v2.files.DbfsAPI.delete")

    jc = DbfsClient(config=config)
    jc.move_("a", f"file:{tmp_path}", recursive=True)

    get_status.assert_called_with("a")
    delete.assert_called_with("a", recursive=True)

    with (tmp_path / "a").open("rb") as f:
        assert f.read() == b"hello"


def test_moving_local_dir_to_dbfs(config, tmp_path, mocker):
    from databricks.sdk.files.v2.client import DbfsClient
    from databricks.sdk.files.v2.files import CreateResponse

    with (tmp_path / "a").open("wb") as f:
        f.write(b"hello")

    mocker.patch(
        "databricks.sdk.files.v2.files.DbfsAPI.create",
        return_value=CreateResponse(123),
    )

    get_status = mocker.patch(
        "databricks.sdk.files.v2.files.DbfsAPI.get_status",
        side_effect=NotFound(),
    )
    add_block = mocker.patch("databricks.sdk.files.v2.files.DbfsAPI.add_block")
    close = mocker.patch("databricks.sdk.files.v2.files.DbfsAPI.close")

    dc = DbfsClient(config=config)
    dc.move_(f"file:{tmp_path}", "a", recursive=True)

    get_status.assert_called_with("a")
    close.assert_called_with(123)
    add_block.assert_called_with(123, "aGVsbG8=")
    assert not (tmp_path / "a").exists()


@pytest.mark.parametrize(
    "path,expected_type",
    [
        ("/path/to/file", _DbfsPath),
        ("/Volumes/path/to/file", _VolumesPath),
        ("dbfs:/path/to/file", _DbfsPath),
        ("dbfs:/Volumes/path/to/file", _VolumesPath),
        ("file:/path/to/file", _LocalPath),
        ("file:/Volumes/path/to/file", _LocalPath),
    ],
)
def test_fs_path(config, path, expected_type):
    dbfs_ext = DbfsExt(config)
    assert isinstance(dbfs_ext._path(path), expected_type)


def test_fs_path_invalid(config):
    dbfs_ext = DbfsExt(config)
    with pytest.raises(ValueError) as e:
        dbfs_ext._path("s3://path/to/file")
    assert 'unsupported scheme "s3"' in str(e.value)


def test_dbfs_local_path_mkdir(config, tmp_path):
    from databricks.sdk.files.v2.client import DbfsClient

    dc = DbfsClient(config=config)
    dc._path(f"file:{tmp_path}/test_dir").mkdir()
    assert dc.exists(f"file:{tmp_path}/test_dir")


def test_dbfs_exists(config, mocker):
    from databricks.sdk.files.v2.client import DbfsClient

    get_status = mocker.patch(
        "databricks.sdk.files.v2.files.DbfsAPI.get_status",
        side_effect=NotFound(),
    )

    client = DbfsClient(config=config)
    client.exists("/abc/def/ghi")

    get_status.assert_called_with("/abc/def/ghi")


def test_volume_exists(config, mocker):
    from databricks.sdk.files.v2.client import DbfsClient

    get_metadata = mocker.patch("databricks.sdk.files.v2.files.FilesAPI.get_metadata")

    client = DbfsClient(config=config)
    client.exists("/Volumes/abc/def/ghi")

    get_metadata.assert_called_with("/Volumes/abc/def/ghi")
