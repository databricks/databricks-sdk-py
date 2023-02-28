import pathlib

import pytest

from databricks.sdk.client import DatabricksError


def test_local_io(random):
    dummy_file = f'/tmp/{random()}'
    to_write = random(1024 * 1024 * 2.5).encode()
    with open(dummy_file, 'wb') as f:
        written = f.write(to_write)
        assert len(to_write) == written

    f = open(dummy_file, 'rb')
    assert f.read() == to_write
    f.close()


def test_dbfs_io(w, random):
    dummy_file = f'/tmp/{random()}'
    to_write = random(1024 * 1024 * 1.5).encode()
    with w.dbfs.open(dummy_file, write=True) as f:
        written = f.write(to_write)
        assert len(to_write) == written

    f = w.dbfs.open(dummy_file, read=True)
    from_dbfs = f.read()
    assert from_dbfs == to_write
    f.close()


@pytest.fixture
def junk(w, random):

    def inner(path: str, size=256) -> bytes:
        to_write = random(size).encode()
        with w.dbfs.open(path, write=True) as f:
            written = f.write(to_write)
            assert len(to_write) == written
            return to_write

    return inner


@pytest.fixture
def ls(w):

    def inner(root: str, recursive=False) -> list[str]:
        return [f.path.removeprefix(root) for f in w.dbfs.list(root, recursive=recursive)]

    return inner


def test_recursive_listing(w, random, junk, ls):
    root = f'/tmp/{random()}'
    junk(f'{root}/01')
    junk(f'{root}/a/02')
    junk(f'{root}/a/b/03')

    assert ['/01', '/a'] == ls(root)
    assert ['/01', '/a/02', '/a/b/03'] == ls(root, recursive=True)

    w.dbfs.delete(root, recursive=True)


def test_cp_dbfs_folder_to_folder_non_recursive(w, random, junk, ls):
    root = f'/tmp/{random()}'
    junk(f'{root}/01')
    junk(f'{root}/a/02')
    junk(f'{root}/a/b/03')
    new_root = f'/tmp/{random()}'

    w.dbfs.copy(root, new_root)

    assert ['/01'] == ls(new_root, recursive=True)


def test_cp_dbfs_folder_to_folder_recursive(w, random, junk, ls):
    root = f'/tmp/{random()}'
    junk(f'{root}/01')
    junk(f'{root}/a/02')
    junk(f'{root}/a/b/03')
    new_root = f'/tmp/{random()}'

    w.dbfs.copy(root, new_root, recursive=True, overwrite=True)

    assert ['/01', '/a/02', '/a/b/03'] == ls(new_root, recursive=True)


def test_cp_dbfs_folder_to_existing_folder_recursive(w, random, junk, ls):
    root = f'/tmp/{random()}'
    junk(f'{root}/01')
    junk(f'{root}/a/02')
    junk(f'{root}/a/b/03')
    new_root = f'/tmp/{random()}'

    w.dbfs.mkdirs(new_root)
    w.dbfs.copy(root, new_root, recursive=True, overwrite=True)

    base = root.split('/')[-1]
    assert [f'/{base}/01', f'/{base}/a/02', f'/{base}/a/b/03'] == ls(new_root, recursive=True)


def test_cp_dbfs_file_to_non_existing_location(w, random, junk):
    root = f'/tmp/{random()}'
    payload = junk(f'{root}/01')
    copy_destination = f'{root}/{random()}'

    w.dbfs.copy(f'{root}/01', copy_destination)

    with w.dbfs.open(copy_destination, read=True) as f:
        assert f.read() == payload


def test_cp_dbfs_file_to_existing_folder(w, random, junk):
    root = f'/tmp/{random()}'
    payload = junk(f'{root}/01')
    w.dbfs.mkdirs(f'{root}/02')
    w.dbfs.copy(f'{root}/01', f'{root}/02')

    with w.dbfs.open(f'{root}/02/01', read=True) as f:
        assert f.read() == payload


def test_cp_dbfs_file_to_existing_location(w, random, junk):
    root = f'/tmp/{random()}'
    junk(f'{root}/01')
    junk(f'{root}/02')
    with pytest.raises(DatabricksError) as ei:
        w.dbfs.copy(f'{root}/01', f'{root}/02')
    assert 'A file or directory already exists' in str(ei.value)


def test_cp_dbfs_file_to_existing_location_with_overwrite(w, random, junk):
    root = f'/tmp/{random()}'
    payload = junk(f'{root}/01')
    junk(f'{root}/02')

    w.dbfs.copy(f'{root}/01', f'{root}/02', overwrite=True)

    with w.dbfs.open(f'{root}/02', read=True) as f:
        assert f.read() == payload


def test_move_within_dbfs(w, random, junk):
    root = f'/tmp/{random()}'
    payload = junk(f'{root}/01')

    w.dbfs.move_(f'{root}/01', f'{root}/02')

    assert w.dbfs.exists(f'{root}/01') is False
    with w.dbfs.open(f'{root}/02', read=True) as f:
        assert f.read() == payload


def test_move_from_dbfs_to_local(w, random, junk, tmp_path):
    root = pathlib.Path(f'/tmp/{random()}')
    payload_01 = junk(f'{root}/01')
    payload_02 = junk(f'{root}/a/02')
    payload_03 = junk(f'{root}/a/b/03')

    w.dbfs.move_(root, f'file:{tmp_path}', recursive=True)

    assert w.dbfs.exists(root) is False
    with (tmp_path / root.name / '01').open('rb') as f:
        assert f.read() == payload_01
    with (tmp_path / root.name / 'a/02').open('rb') as f:
        assert f.read() == payload_02
    with (tmp_path / root.name / 'a/b/03').open('rb') as f:
        assert f.read() == payload_03
