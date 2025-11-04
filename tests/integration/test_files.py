import io
import logging
import pathlib
import platform
import time
from typing import Callable, List, Tuple, Union

import pytest  # type: ignore[import-not-found]

from databricks.sdk.core import DatabricksError
from databricks.sdk.service.catalog import VolumeType


def test_local_io(random):  # type: ignore[no-untyped-def]
    if platform.system() == "Windows":
        dummy_file = f"C:\\Windows\\Temp\\{random()}"
    else:
        dummy_file = f"/tmp/{random()}"
    to_write = random(1024 * 1024 * 2.5).encode()
    with open(dummy_file, "wb") as f:
        written = f.write(to_write)
        assert len(to_write) == written

    f = open(dummy_file, "rb")  # type: ignore[assignment]
    assert f.read() == to_write
    f.close()


def test_dbfs_io(w, random):  # type: ignore[no-untyped-def]
    dummy_file = f"/tmp/{random()}"
    to_write = random(1024 * 1024 * 1.5).encode()
    with w.dbfs.open(dummy_file, write=True) as f:
        written = f.write(to_write)
        assert len(to_write) == written

    f = w.dbfs.open(dummy_file, read=True)
    from_dbfs = f.read()
    assert from_dbfs == to_write
    f.close()


@pytest.fixture
def junk(w, random):  # type: ignore[no-untyped-def]

    def inner(path: str, size=256) -> bytes:  # type: ignore[no-untyped-def]
        to_write = random(size).encode()
        with w.dbfs.open(path, write=True) as f:
            written = f.write(to_write)
            assert len(to_write) == written
            return to_write  # type: ignore[no-any-return]

    return inner


@pytest.fixture
def ls(w):  # type: ignore[no-untyped-def]

    def inner(root: str, recursive=False) -> List[str]:  # type: ignore[no-untyped-def]
        return [f.path.removeprefix(root) for f in w.dbfs.list(root, recursive=recursive)]

    return inner


def test_recursive_listing(w, random, junk, ls):  # type: ignore[no-untyped-def]
    root = f"/tmp/{random()}"
    junk(f"{root}/01")
    junk(f"{root}/a/02")
    junk(f"{root}/a/b/03")

    assert ["/01", "/a"] == ls(root)
    assert ["/01", "/a/02", "/a/b/03"] == ls(root, recursive=True)

    w.dbfs.delete(root, recursive=True)


def test_cp_dbfs_folder_to_folder_non_recursive(w, random, junk, ls):  # type: ignore[no-untyped-def]
    root = f"/tmp/{random()}"
    junk(f"{root}/01")
    junk(f"{root}/a/02")
    junk(f"{root}/a/b/03")
    new_root = f"/tmp/{random()}"

    w.dbfs.copy(root, new_root)

    assert ["/01"] == ls(new_root, recursive=True)


def test_cp_dbfs_folder_to_folder_recursive(w, random, junk, ls):  # type: ignore[no-untyped-def]
    root = f"/tmp/{random()}"
    junk(f"{root}/01")
    junk(f"{root}/a/02")
    junk(f"{root}/a/b/03")
    new_root = f"/tmp/{random()}"

    w.dbfs.copy(root, new_root, recursive=True, overwrite=True)

    assert ["/01", "/a/02", "/a/b/03"] == ls(new_root, recursive=True)


def test_cp_dbfs_folder_to_existing_folder_recursive(w, random, junk, ls):  # type: ignore[no-untyped-def]
    root = f"/tmp/{random()}"
    junk(f"{root}/01")
    junk(f"{root}/a/02")
    junk(f"{root}/a/b/03")
    new_root = f"/tmp/{random()}"

    w.dbfs.mkdirs(new_root)
    w.dbfs.copy(root, new_root, recursive=True, overwrite=True)

    base = root.split("/")[-1]
    assert [f"/{base}/01", f"/{base}/a/02", f"/{base}/a/b/03"] == ls(new_root, recursive=True)


def test_cp_dbfs_file_to_non_existing_location(w, random, junk):  # type: ignore[no-untyped-def]
    root = f"/tmp/{random()}"
    payload = junk(f"{root}/01")
    copy_destination = f"{root}/{random()}"

    w.dbfs.copy(f"{root}/01", copy_destination)

    with w.dbfs.open(copy_destination, read=True) as f:
        assert f.read() == payload


def test_cp_dbfs_file_to_existing_folder(w, random, junk):  # type: ignore[no-untyped-def]
    root = f"/tmp/{random()}"
    payload = junk(f"{root}/01")
    w.dbfs.mkdirs(f"{root}/02")
    w.dbfs.copy(f"{root}/01", f"{root}/02")

    with w.dbfs.open(f"{root}/02/01", read=True) as f:
        assert f.read() == payload


def test_cp_dbfs_file_to_existing_location(w, random, junk):  # type: ignore[no-untyped-def]
    root = f"/tmp/{random()}"
    junk(f"{root}/01")
    junk(f"{root}/02")
    with pytest.raises(DatabricksError) as ei:
        w.dbfs.copy(f"{root}/01", f"{root}/02")
    assert "A file or directory already exists" in str(ei.value)


def test_cp_dbfs_file_to_existing_location_with_overwrite(w, random, junk):  # type: ignore[no-untyped-def]
    root = f"/tmp/{random()}"
    payload = junk(f"{root}/01")
    junk(f"{root}/02")

    w.dbfs.copy(f"{root}/01", f"{root}/02", overwrite=True)

    with w.dbfs.open(f"{root}/02", read=True) as f:
        assert f.read() == payload


def test_move_within_dbfs(w, random, junk):  # type: ignore[no-untyped-def]
    root = f"/tmp/{random()}"
    payload = junk(f"{root}/01")

    w.dbfs.move_(f"{root}/01", f"{root}/02")

    assert w.dbfs.exists(f"{root}/01") is False
    with w.dbfs.open(f"{root}/02", read=True) as f:
        assert f.read() == payload


def test_move_from_dbfs_to_local(w, random, junk, tmp_path):  # type: ignore[no-untyped-def]
    root = pathlib.Path(f"/tmp/{random()}")
    payload_01 = junk(f"{root}/01")
    payload_02 = junk(f"{root}/a/02")
    payload_03 = junk(f"{root}/a/b/03")

    w.dbfs.move_(root, f"file:{tmp_path}", recursive=True)

    assert w.dbfs.exists(root) is False
    with (tmp_path / root.name / "01").open("rb") as f:
        assert f.read() == payload_01
    with (tmp_path / root.name / "a/02").open("rb") as f:
        assert f.read() == payload_02
    with (tmp_path / root.name / "a/b/03").open("rb") as f:
        assert f.read() == payload_03


def test_dbfs_upload_download(w, random, junk, tmp_path):  # type: ignore[no-untyped-def]
    root = pathlib.Path(f"/tmp/{random()}")

    f = io.BytesIO(b"some text data")
    w.dbfs.upload(f"{root}/01", f)

    with w.dbfs.download(f"{root}/01") as f:
        assert f.read() == b"some text data"


class ResourceWithCleanup:
    cleanup: Callable[[], None]

    def __init__(self, cleanup):  # type: ignore[no-untyped-def]
        self.cleanup = cleanup

    def __enter__(self):  # type: ignore[no-untyped-def]
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):  # type: ignore[no-untyped-def]
        self.cleanup()

    @staticmethod
    def create_schema(w, catalog, schema):  # type: ignore[no-untyped-def]
        res = w.schemas.create(catalog_name=catalog, name=schema)
        return ResourceWithCleanup(lambda: w.schemas.delete(res.full_name))  # type: ignore[no-untyped-call]

    @staticmethod
    def create_volume(w, catalog, schema, volume):  # type: ignore[no-untyped-def]
        res = w.volumes.create(
            catalog_name=catalog,
            schema_name=schema,
            name=volume,
            volume_type=VolumeType.MANAGED,
        )
        return ResourceWithCleanup(lambda: w.volumes.delete(res.full_name))  # type: ignore[no-untyped-call]


def test_files_api_upload_download(ucws, files_api, random):  # type: ignore[no-untyped-def]
    w = ucws
    schema = "filesit-" + random()
    volume = "filesit-" + random()
    with ResourceWithCleanup.create_schema(w, "main", schema):  # type: ignore[no-untyped-call]
        with ResourceWithCleanup.create_volume(w, "main", schema, volume):  # type: ignore[no-untyped-call]
            f = io.BytesIO(b"some text data")
            target_file = f"/Volumes/main/{schema}/{volume}/filesit-with-?-and-#-{random()}.txt"
            files_api.upload(target_file, f)
            with files_api.download(target_file).contents as f:
                assert f.read() == b"some text data"


def test_files_api_read_twice_from_one_download(ucws, files_api, random):  # type: ignore[no-untyped-def]
    w = ucws
    schema = "filesit-" + random()
    volume = "filesit-" + random()
    with ResourceWithCleanup.create_schema(w, "main", schema):  # type: ignore[no-untyped-call]
        with ResourceWithCleanup.create_volume(w, "main", schema, volume):  # type: ignore[no-untyped-call]
            f = io.BytesIO(b"some text data")
            target_file = f"/Volumes/main/{schema}/{volume}/filesit-{random()}.txt"
            files_api.upload(target_file, f)

            res = files_api.download(target_file).contents

            with res:
                assert res.read() == b"some text data"

            with pytest.raises(ValueError):
                with res:
                    res.read()


def test_files_api_delete_file(ucws, files_api, random):  # type: ignore[no-untyped-def]
    w = ucws
    schema = "filesit-" + random()
    volume = "filesit-" + random()
    with ResourceWithCleanup.create_schema(w, "main", schema):  # type: ignore[no-untyped-call]
        with ResourceWithCleanup.create_volume(w, "main", schema, volume):  # type: ignore[no-untyped-call]
            f = io.BytesIO(b"some text data")
            target_file = f"/Volumes/main/{schema}/{volume}/filesit-{random()}.txt"
            files_api.upload(target_file, f)
            files_api.delete(target_file)


def test_files_api_get_metadata(ucws, files_api, random):  # type: ignore[no-untyped-def]
    w = ucws
    schema = "filesit-" + random()
    volume = "filesit-" + random()
    with ResourceWithCleanup.create_schema(w, "main", schema):  # type: ignore[no-untyped-call]
        with ResourceWithCleanup.create_volume(w, "main", schema, volume):  # type: ignore[no-untyped-call]
            f = io.BytesIO(b"some text data")
            target_file = f"/Volumes/main/{schema}/{volume}/filesit-{random()}.txt"
            files_api.upload(target_file, f)
            m = files_api.get_metadata(target_file)
            assert m.content_type == "application/octet-stream"
            assert m.content_length == 14
            assert m.last_modified is not None


def test_files_api_create_directory(ucws, files_api, random):  # type: ignore[no-untyped-def]
    w = ucws
    schema = "filesit-" + random()
    volume = "filesit-" + random()
    with ResourceWithCleanup.create_schema(w, "main", schema):  # type: ignore[no-untyped-call]
        with ResourceWithCleanup.create_volume(w, "main", schema, volume):  # type: ignore[no-untyped-call]
            target_directory = f"/Volumes/main/{schema}/{volume}/filesit-{random()}/"
            files_api.create_directory(target_directory)


def test_files_api_list_directory_contents(ucws, files_api, random):  # type: ignore[no-untyped-def]
    w = ucws
    schema = "filesit-" + random()
    volume = "filesit-" + random()
    with ResourceWithCleanup.create_schema(w, "main", schema):  # type: ignore[no-untyped-call]
        with ResourceWithCleanup.create_volume(w, "main", schema, volume):  # type: ignore[no-untyped-call]
            target_directory = f"/Volumes/main/{schema}/{volume}/filesit-{random()}"
            files_api.upload(target_directory + "/file1.txt", io.BytesIO(b"some text data"))
            files_api.upload(target_directory + "/file2.txt", io.BytesIO(b"some text data"))
            files_api.upload(target_directory + "/file3.txt", io.BytesIO(b"some text data"))

            result = list(files_api.list_directory_contents(target_directory))
            assert len(result) == 3


def test_files_api_delete_directory(ucws, files_api, random):  # type: ignore[no-untyped-def]
    w = ucws
    schema = "filesit-" + random()
    volume = "filesit-" + random()
    with ResourceWithCleanup.create_schema(w, "main", schema):  # type: ignore[no-untyped-call]
        with ResourceWithCleanup.create_volume(w, "main", schema, volume):  # type: ignore[no-untyped-call]
            target_directory = f"/Volumes/main/{schema}/{volume}/filesit-{random()}/"
            files_api.create_directory(target_directory)
            files_api.delete_directory(target_directory)


def test_files_api_get_directory_metadata(ucws, files_api, random):  # type: ignore[no-untyped-def]
    w = ucws
    schema = "filesit-" + random()
    volume = "filesit-" + random()
    with ResourceWithCleanup.create_schema(w, "main", schema):  # type: ignore[no-untyped-call]
        with ResourceWithCleanup.create_volume(w, "main", schema, volume):  # type: ignore[no-untyped-call]
            target_directory = f"/Volumes/main/{schema}/{volume}/filesit-{random()}/"
            files_api.create_directory(target_directory)
            files_api.get_directory_metadata(target_directory)


@pytest.mark.benchmark
def test_files_api_download_benchmark(ucws, files_api, random):  # type: ignore[no-untyped-def]
    w = ucws
    schema = "filesit-" + random()
    volume = "filesit-" + random()
    with ResourceWithCleanup.create_schema(w, "main", schema):  # type: ignore[no-untyped-call]
        with ResourceWithCleanup.create_volume(w, "main", schema, volume):  # type: ignore[no-untyped-call]
            # Create a 50 MB file
            f = io.BytesIO(bytes(range(256)) * 200000)
            target_file = f"/Volumes/main/{schema}/{volume}/filesit-benchmark-{random()}.txt"
            files_api.upload(target_file, f)

            totals = {}
            for chunk_size_kb in [
                20,
                50,
                100,
                200,
                500,
                1000,
                2000,
                5000,
                10000,
                20000,
                50000,
                None,
            ]:
                chunk_size = chunk_size_kb * 1024 if chunk_size_kb else None
                total = 0
                count = 10
                for i in range(count):
                    start = time.time()
                    f = files_api.download(target_file).contents
                    f.set_chunk_size(chunk_size)  # type: ignore[attr-defined]
                    with f as vf:
                        vf.read()
                    end = time.time()
                    total += end - start  # type: ignore[assignment]
                avg_time = total / count
                logging.info(
                    f"[chunk_size=%s] Average time to download: %f seconds",
                    str(chunk_size_kb) + "kb" if chunk_size_kb else "None",
                    avg_time,
                )
                totals[chunk_size_kb] = avg_time
            logging.info("Benchmark results:")
            best: Tuple[Union[int, None], Union[float, None]] = (None, None)
            for k, v in totals.items():
                if best[1] is None or v < best[1]:
                    best = (k, v)
                logging.info(
                    f"[chunk_size=%s] Average time to download: %f seconds",
                    str(k) + "kb" if k else "None",
                    v,
                )
            min_str = str(best[0]) + "kb" if best[0] else "None"
            logging.info("Fastest chunk size: %s in %f seconds", min_str, best[1])
