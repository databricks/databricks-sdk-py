import base64
import logging
import os

import pytest

from databricks.sdk.core import DatabricksError
from databricks.sdk.errors import NotFound


def test_rest_dbfs_ls(w, env_or_skip):
    from databricks.sdk.runtime import dbutils

    x = dbutils.fs.ls('/')

    assert len(x) > 1


def test_proxy_dbfs_mounts(w, env_or_skip):
    w.config.cluster_id = env_or_skip("TEST_DEFAULT_CLUSTER_ID")

    x = w.dbutils.fs.mounts()

    assert len(x) > 1


@pytest.fixture(params=['dbfs', 'volumes'])
def fs_and_base_path(request, ucws, volume):
    if request.param == 'dbfs':
        fs = ucws.dbutils.fs
        base_path = '/tmp'
    else:
        fs = ucws.dbutils.fs
        base_path = volume
    return fs, base_path


def test_put(fs_and_base_path):
    fs, base_path = fs_and_base_path
    path = base_path + "/dbc_qa_file"
    fs.put(path, "test", True)
    output = fs.head(path)
    assert output == "test"


def test_large_put(fs_and_base_path):
    fs, base_path = fs_and_base_path
    path = base_path + "/dbc_qa_large_file"
    fs.put(path, "test" * 20000, True)
    output = fs.head(path)
    assert output == ("test" * 20000)[:65536]


def test_put_local_path(w, random, tmp_path):
    to_write = random(1024 * 1024 * 2)
    tmp_path = tmp_path / "tmp_file"
    w.dbutils.fs.put(f'file:{tmp_path}', to_write, True)
    assert w.dbutils.fs.head(f'file:{tmp_path}', 1024 * 1024 * 2) == to_write


def test_cp_file(fs_and_base_path, random):
    fs, base_path = fs_and_base_path
    path = base_path + "/dbc_qa_file-" + random()
    fs.put(path, "test", True)
    fs.cp(path, path + "_copy")
    output = fs.head(path + "_copy")
    assert output == "test"
    assert len(fs.ls(path)) == 1


def test_cp_dir(fs_and_base_path, random):
    fs, base_path = fs_and_base_path
    path = base_path + "/dbc_qa_dir-" + random()
    fs.mkdirs(path)
    fs.put(path + "/file1", "test1", True)
    fs.put(path + "/file2", "test2", True)
    fs.cp(path, path + "_copy")
    output = fs.ls(path + "_copy")
    assert len(output) == 2
    assert output[0].path == path + "_copy/file1"
    assert output[1].path == path + "_copy/file2"


def test_ls_file(fs_and_base_path, random):
    fs, base_path = fs_and_base_path
    path = base_path + "/dbc_qa_file-" + random()
    fs.put(path, "test", True)
    output = fs.ls(path)
    assert len(output) == 1
    assert output[0].path == path


def test_ls_dir(fs_and_base_path, random):
    fs, base_path = fs_and_base_path
    path = base_path + "/dbc_qa_dir-" + random()
    fs.mkdirs(path)
    fs.put(path + "/file1", "test1", True)
    fs.put(path + "/file2", "test2", True)
    output = fs.ls(path)
    assert len(output) == 2
    assert output[0].path == path + "/file1"
    assert output[1].path == path + "/file2"


def test_mv_file(fs_and_base_path, random):
    fs, base_path = fs_and_base_path
    path = base_path + "/dbc_qa_file-" + random()
    fs.put(path, "test", True)
    fs.mv(path, path + "_moved")
    output = fs.head(path + "_moved")
    assert output == "test"
    with pytest.raises(NotFound):
        fs.ls(path)


def test_mv_dir(fs_and_base_path, random):
    fs, base_path = fs_and_base_path
    path = base_path + "/dbc_qa_dir-" + random()
    fs.mkdirs(path)
    fs.put(path + "/file1", "test1", True)
    fs.put(path + "/file2", "test2", True)
    # DBFS can do recursive mv as a single API call, but Volumes cannot
    kw = {'recurse': True} if '/Volumes' in path else {}
    fs.mv(path, path + "_moved", **kw)
    output = fs.ls(path + "_moved")
    assert len(output) == 2
    assert output[0].path == path + "_moved/file1"
    assert output[1].path == path + "_moved/file2"
    with pytest.raises(NotFound):
        fs.ls(path)


def test_mv_local_to_remote(fs_and_base_path, random, tmp_path):
    fs, base_path = fs_and_base_path
    path = base_path + "/dbc_qa_file-" + random()
    with open(tmp_path / "test", "w") as f:
        f.write("test")
    fs.mv('file:' + str(tmp_path / "test"), path)
    output = fs.head(path)
    assert output == "test"
    assert os.listdir(tmp_path) == []


def test_mv_remote_to_local(fs_and_base_path, random, tmp_path):
    fs, base_path = fs_and_base_path
    path = base_path + "/dbc_qa_file-" + random()
    fs.put(path, "test", True)
    fs.mv(path, 'file:' + str(tmp_path / "test"))
    with open(tmp_path / "test", "r") as f:
        output = f.read()
    assert output == "test"
    with pytest.raises(NotFound):
        fs.ls(path)


def test_rm_file(fs_and_base_path, random):
    fs, base_path = fs_and_base_path
    path = base_path + "/dbc_qa_file-" + random()
    fs.put(path, "test", True)
    fs.rm(path)
    with pytest.raises(NotFound):
        fs.ls(path)


def test_rm_dir(fs_and_base_path, random):
    fs, base_path = fs_and_base_path
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
