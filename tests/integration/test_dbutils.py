import base64
import logging

import pytest

from databricks.sdk.core import DatabricksError
from databricks.sdk.errors import NotFound
from databricks.sdk.service.catalog import VolumeType


@pytest.fixture(scope='session')
def dbfs_volume(ucws, random):
    schema = ucws.schemas.create('dbfs-' + random(), 'main')
    volume = ucws.volumes.create('main', schema.name, 'dbfs-test', VolumeType.MANAGED)
    yield '/Volumes/' + volume.full_name.replace(".", "/")
    ucws.volumes.delete(volume.full_name)
    ucws.schemas.delete(schema.full_name)


def test_rest_dbfs_ls(w, env_or_skip):
    from databricks.sdk.runtime import dbutils

    x = dbutils.fs.ls('/')

    assert len(x) > 1


def test_proxy_dbfs_mounts(w, env_or_skip):
    w.config.cluster_id = env_or_skip("TEST_DEFAULT_CLUSTER_ID")

    x = w.dbutils.fs.mounts()

    assert len(x) > 1


def test_dbutils_dbfs_put_head_small(w):
    fs = w.dbutils.fs
    _test_put(fs, 'dbfs:/tmp')


def test_dbutils_volumes_put_head_small(ucws, dbfs_volume):
    fs = ucws.dbutils.fs
    _test_put(fs, dbfs_volume)


def _test_put(fs, base_path):
    path = base_path + "/dbc_qa_file"
    fs.put(path, "test", True)
    output = fs.head(path)
    assert output == "test"


def test_dbutils_dbfs_put_head_large(w):
    fs = w.dbutils.fs
    _test_large_put(fs, 'dbfs:/tmp')


def test_dbutils_volumes_put_head_large(ucws, dbfs_volume):
    fs = ucws.dbutils.fs
    _test_large_put(fs, dbfs_volume)


def _test_large_put(fs, base_path):
    path = base_path + "/dbc_qa_large_file"
    fs.put(path, "test" * 20000, True)
    output = fs.head(path)
    assert output == ("test" * 20000)[:65536]


def test_dbutils_dbfs_cp_file(w, random):
    fs = w.dbutils.fs
    _test_cp_file(fs, 'dbfs:/tmp', random)


def test_dbutils_volumes_cp_file(ucws, dbfs_volume, random):
    fs = ucws.dbutils.fs
    _test_cp_file(fs, dbfs_volume, random)


def _test_cp_file(fs, base_path, random):
    path = base_path + "/dbc_qa_file-" + random()
    fs.put(path, "test", True)
    fs.cp(path, path + "_copy")
    output = fs.head(path + "_copy")
    assert output == "test"
    assert len(fs.ls(path)) == 1


def test_dbutils_dbfs_cp_dir(w, random):
    fs = w.dbutils.fs
    _test_cp_dir(fs, 'dbfs:/tmp', random)


def test_dbutils_volumes_cp_dir(ucws, dbfs_volume, random):
    fs = ucws.dbutils.fs
    _test_cp_dir(fs, dbfs_volume, random)


def _test_cp_dir(fs, base_path, random):
    path = base_path + "/dbc_qa_dir-" + random()
    fs.mkdirs(path)
    fs.put(path + "/file1", "test1", True)
    fs.put(path + "/file2", "test2", True)
    fs.cp(path, path + "_copy")
    output = fs.ls(path + "_copy")
    assert len(output) == 2
    assert output[0].path == path + "_copy/file1"
    assert output[1].path == path + "_copy/file2"


def test_dbutils_dbfs_mv_file(w, random):
    fs = w.dbutils.fs
    _test_mv_file(fs, 'dbfs:/tmp', random)


def test_dbutils_volumes_mv_file(ucws, dbfs_volume, random):
    fs = ucws.dbutils.fs
    _test_mv_file(fs, dbfs_volume, random)


def _test_mv_file(fs, base_path, random):
    path = base_path + "/dbc_qa_file-" + random()
    fs.put(path, "test", True)
    fs.mv(path, path + "_moved")
    output = fs.head(path + "_moved")
    assert output == "test"
    with pytest.raises(NotFound):
        fs.ls(path)


def test_dbutils_dbfs_mv_dir(w, random):
    fs = w.dbutils.fs
    _test_mv_dir(fs, 'dbfs:/tmp', random)


def test_dbutils_volumes_mv_dir(ucws, dbfs_volume, random):
    fs = ucws.dbutils.fs
    _test_mv_dir(fs, dbfs_volume, random)


def _test_mv_dir(fs, base_path, random):
    path = base_path + "/dbc_qa_dir-" + random()
    fs.mkdirs(path)
    fs.put(path + "/file1", "test1", True)
    fs.put(path + "/file2", "test2", True)
    fs.mv(path, path + "_moved")
    output = fs.ls(path + "_moved")
    assert len(output) == 2
    assert output[0].path == path + "_moved/file1"
    assert output[1].path == path + "_moved/file2"
    with pytest.raises(NotFound):
        fs.ls(path)


def test_dbutils_dbfs_rm_file(w, random):
    fs = w.dbutils.fs
    _test_rm_file(fs, 'dbfs:/tmp', random)


def test_dbutils_volumes_rm_file(ucws, dbfs_volume, random):
    fs = ucws.dbutils.fs
    _test_rm_file(fs, dbfs_volume, random)


def _test_rm_file(fs, base_path, random):
    path = base_path + "/dbc_qa_file-" + random()
    fs.put(path, "test", True)
    fs.rm(path)
    with pytest.raises(NotFound):
        fs.ls(path)


def test_dbutils_dbfs_rm_dir(w, random):
    fs = w.dbutils.fs
    _test_rm_dir(fs, 'dbfs:/tmp', random)


def test_dbutils_volumes_rm_dir(ucws, dbfs_volume, random):
    fs = ucws.dbutils.fs
    _test_rm_dir(fs, dbfs_volume, random)


def _test_rm_dir(fs, base_path, random):
    path = base_path + "/dbc_qa_dir-" + random()
    fs.mkdirs(path)
    fs.put(path + "/file1", "test1", True)
    fs.put(path + "/file2", "test2", True)
    with pytest.raises(IOError):
        fs.rm(path)
    fs.rm(path, recurse=True)
    with pytest.raises(NotFound):
        fs.ls(path)


def test_secrets(w, random):
    random_scope = f'scope-{random()}'
    key_for_string = f'string-{random()}'
    key_for_bytes = f'bytes-{random()}'
    random_value = f'SECRET-{random()}'

    logger = logging.getLogger('foo')
    logger.info(f'Before loading secret: {random_value}')

    w.secrets.create_scope(random_scope)
    w.secrets.put_secret(random_scope, key_for_string, string_value=random_value)
    w.secrets.put_secret(random_scope,
                         key_for_bytes,
                         bytes_value=base64.b64encode(random_value.encode()).decode())

    from databricks.sdk.runtime import dbutils

    all_secrets = {}
    for secret_scope in dbutils.secrets.listScopes():
        scope = secret_scope.name
        for secret_metadata in dbutils.secrets.list(scope):
            key = secret_metadata.key
            try:
                all_secrets[f'{scope}.{key}'] = dbutils.secrets.get(scope, key)
            except DatabricksError as e:
                if e.error_code == 'BAD_REQUEST':
                    pytest.skip('dbconnect is not enabled on this workspace')
                raise e

    logger.info(f'After loading secret: {random_value}')
    logging.getLogger('databricks.sdk').info(f'After loading secret: {random_value}')

    assert all_secrets[f'{random_scope}.{key_for_string}'] == random_value
    assert all_secrets[f'{random_scope}.{key_for_bytes}'] == random_value
