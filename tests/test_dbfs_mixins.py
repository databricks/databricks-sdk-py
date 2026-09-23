import base64
import io

import pytest

from databricks.sdk import WorkspaceClient
from databricks.sdk.mixins.files import DbfsExt, _DbfsPath, _LocalPath, _VolumesPath


def test_dbfs_upload_chunks_payload_through_http_api(config, requests_mock):
    chunk_size = 1024 * 1024
    payload = b"a" * chunk_size + b"tail"
    requests_mock.post("http://localhost/api/2.0/dbfs/create", json={"handle": 123})
    requests_mock.post("http://localhost/api/2.0/dbfs/add-block", json={})
    requests_mock.post("http://localhost/api/2.0/dbfs/close", json={})

    WorkspaceClient(config=config).dbfs.upload("/tmp/payload.bin", io.BytesIO(payload), overwrite=True)

    create_request, first_block, second_block, close_request = requests_mock.request_history
    assert create_request.json() == {"overwrite": True, "path": "/tmp/payload.bin"}
    assert first_block.url == "http://localhost/api/2.0/dbfs/add-block"
    assert second_block.url == "http://localhost/api/2.0/dbfs/add-block"
    assert base64.b64decode(first_block.json()["data"]) == payload[:chunk_size]
    assert base64.b64decode(second_block.json()["data"]) == payload[chunk_size:]
    assert first_block.json()["handle"] == 123
    assert second_block.json()["handle"] == 123
    assert close_request.json() == {"handle": 123}


def test_copy_routes_dbfs_source_to_volumes_http_api(config, requests_mock):
    source_path = "/tmp/source.txt"
    target_path = "/Volumes/main/default/volume/copied.txt"
    target_url = f"http://localhost/api/2.0/fs/files{target_path}"
    target_directory_url = f"http://localhost/api/2.0/fs/directories{target_path}"
    payload = b"hello"
    not_found = {"error_code": "RESOURCE_DOES_NOT_EXIST", "message": "not found"}
    requests_mock.head(target_url, status_code=404, json=not_found)
    requests_mock.head(target_directory_url, status_code=404, json=not_found)
    requests_mock.get(
        "http://localhost/api/2.0/dbfs/get-status",
        json={"path": source_path, "is_dir": False, "file_size": len(payload)},
    )

    def read_chunk(request, _context):
        offset = int(request.qs["offset"][0])
        length = int(request.qs["length"][0])
        chunk = payload[offset : offset + length]
        return {"bytes_read": len(chunk), "data": base64.b64encode(chunk).decode()}

    requests_mock.get("http://localhost/api/2.0/dbfs/read", json=read_chunk)
    uploaded = {}

    def capture_upload(request, _context):
        body = request.body
        uploaded["body"] = body.read() if hasattr(body, "read") else body
        return ""

    requests_mock.put(target_url, text=capture_upload)

    WorkspaceClient(config=config).dbfs.copy(source_path, target_path)

    status_requests = [request for request in requests_mock.request_history if "/dbfs/get-status" in request.url]
    read_requests = [request for request in requests_mock.request_history if "/dbfs/read" in request.url]
    upload_request = requests_mock.request_history[-1]
    assert len(status_requests) == 2
    assert all(request.qs == {"path": [source_path]} for request in status_requests)
    assert [request.qs["offset"] for request in read_requests] == [["0"], [str(len(payload))]]
    assert all(request.qs["length"] == [str(1024 * 1024)] for request in read_requests)
    assert upload_request.method == "PUT"
    assert upload_request.url == f"{target_url}?overwrite=false"
    assert upload_request.headers["Content-Type"] == "application/octet-stream"
    assert uploaded["body"] == payload


def test_move_routes_volume_to_local_and_deletes_remote_source(config, requests_mock, tmp_path):
    source_path = "/Volumes/main/default/volume/source.txt"
    source_url = f"http://localhost/api/2.0/fs/files{source_path}"
    source_directory_url = f"http://localhost/api/2.0/fs/directories{source_path}"
    payload = b"moved from a volume"
    requests_mock.head(
        source_directory_url,
        status_code=404,
        json={"error_code": "RESOURCE_DOES_NOT_EXIST", "message": "not a directory"},
    )
    requests_mock.get(
        source_url,
        content=payload,
        headers={
            "Content-Length": str(len(payload)),
            "Content-Type": "application/octet-stream",
            "Last-Modified": "Wed, 10 Sep 2025 12:00:00 GMT",
        },
    )
    requests_mock.delete(source_url, status_code=204)

    WorkspaceClient(config=config).dbfs.move_(source_path, f"file:{tmp_path}", recursive=True)

    assert (tmp_path / "source.txt").read_bytes() == payload
    assert [request.method for request in requests_mock.request_history] == [
        "HEAD",
        "HEAD",
        "GET",
        "HEAD",
        "DELETE",
    ]
    assert requests_mock.request_history[-1].url == source_url


def test_move_within_dbfs_uses_dbfs_move_http_api(config, requests_mock):
    requests_mock.post("http://localhost/api/2.0/dbfs/move", json={})

    WorkspaceClient(config=config).dbfs.move_("/tmp/source", "/tmp/destination")

    request = requests_mock.last_request
    assert request.json() == {
        "destination_path": "/tmp/destination",
        "source_path": "/tmp/source",
    }


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
    client = WorkspaceClient(config=config)
    client.dbfs._path(f"file:{tmp_path}/test_dir").mkdir()
    assert client.dbfs.exists(f"file:{tmp_path}/test_dir")


def test_dbfs_exists_maps_not_found_http_response_to_false(config, requests_mock):
    requests_mock.get(
        "http://localhost/api/2.0/dbfs/get-status",
        status_code=404,
        json={"error_code": "RESOURCE_DOES_NOT_EXIST", "message": "not found"},
    )

    exists = WorkspaceClient(config=config).dbfs.exists("/abc/def/ghi")

    assert exists is False
    assert requests_mock.last_request.qs == {"path": ["/abc/def/ghi"]}


def test_volume_exists_reads_file_metadata_over_http(config, requests_mock):
    path = "/Volumes/abc/def/ghi"
    requests_mock.head(
        f"http://localhost/api/2.0/fs/files{path}",
        headers={
            "Content-Length": "4",
            "Content-Type": "application/octet-stream",
            "Last-Modified": "Wed, 10 Sep 2025 12:00:00 GMT",
        },
    )

    exists = WorkspaceClient(config=config).dbfs.exists(path)

    assert exists is True
    assert requests_mock.last_request.method == "HEAD"
