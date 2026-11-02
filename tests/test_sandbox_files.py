import io
from urllib.parse import parse_qs, urlsplit

import pytest

from databricks.sdk import WorkspaceClient
from databricks.sdk.errors import NotFound, PermissionDenied

from .conftest import noop_credentials


_HOST = "https://example.cloud.databricks.com"
_FILES_URL = f"{_HOST}/api/2.0/sandbox-files/sandboxes/box"


def _sandbox(*, workspace_id=None):
    workspace = WorkspaceClient(
        host=_HOST,
        workspace_id=workspace_id,
        credentials_strategy=noop_credentials,
    )
    return workspace.sandbox


def _query_parameters(request):
    return parse_qs(urlsplit(request.url).query, keep_blank_values=True)


def _entry(name):
    return {
        "name": name,
        "path": f"/tmp/{name}",
        "file_type": "SANDBOX_FILE_TYPE_FILE",
        "size": "1",
        "mode": 0o644,
        "permissions": "-rw-r--r--",
        "owner": "sandbox",
        "group": "sandbox",
        "modify_time": "2023-11-14T22:13:20.123456789Z",
    }


def test_unary_operations_use_generated_sandbox_methods(requests_mock):
    requests_mock.post(f"{_FILES_URL}/paths:rename", json={})
    requests_mock.post(f"{_FILES_URL}/directories:make", json={})
    requests_mock.post(f"{_FILES_URL}/paths:remove", json={})
    requests_mock.get(f"{_FILES_URL}/paths:describe", json={"file": _entry("item")})
    requests_mock.get(f"{_FILES_URL}/directory-entries", json={"contents": [_entry("child")]})
    sandbox = _sandbox()

    sandbox.rename_path("sandboxes/box", "/tmp/source", "/tmp/destination")
    sandbox.create_directory("sandboxes/box", "/tmp/directory", parents=False)
    sandbox.delete_path("sandboxes/box", "/tmp/old", recursive=True)
    metadata = sandbox.get_metadata("sandboxes/box", "/tmp/item")
    contents = list(sandbox.list_directory_contents("sandboxes/box", "/tmp/directory", page_size=10))

    assert metadata.file.path == "/tmp/item"
    assert [entry.name for entry in contents] == ["child"]
    rename, create, delete, metadata_request, listing = requests_mock.request_history
    assert rename.json() == {"source": "/tmp/source", "destination": "/tmp/destination"}
    assert create.json() == {"path": "/tmp/directory", "parents": False}
    assert delete.json() == {"path": "/tmp/old", "recursive": True}
    assert _query_parameters(metadata_request) == {"path": ["/tmp/item"]}
    assert _query_parameters(listing) == {"path": ["/tmp/directory"], "page_size": ["10"]}


def test_list_directory_contents_follows_generated_pagination(requests_mock):
    requests_mock.get(
        f"{_FILES_URL}/directory-entries",
        [
            {"json": {"contents": [_entry("first")], "next_page_token": "next"}},
            {"json": {"contents": [_entry("second")]}},
        ],
    )

    names = [entry.name for entry in _sandbox().list_directory_contents("sandboxes/box", "/tmp")]

    assert names == ["first", "second"]
    assert _query_parameters(requests_mock.request_history[1])["page_token"] == ["next"]


def test_upload_file_streams_bytes_to_transfer_endpoint(requests_mock):
    payload = b"raw file contents\x00\xff"
    contents = io.BytesIO(payload)
    uploaded = {}

    def capture_upload(request, context):
        assert request.body is contents
        uploaded["body"] = request.body.read()
        context.status_code = 204
        return ""

    requests_mock.put(f"{_FILES_URL}/content", text=capture_upload)

    _sandbox(workspace_id="123").upload_file(
        parent="sandboxes/box",
        path="/tmp/report ?#%.bin",
        contents=contents,
    )

    request = requests_mock.last_request
    assert uploaded["body"] == payload
    assert _query_parameters(request) == {"path": ["/tmp/report ?#%.bin"]}
    assert request.headers["Content-Type"] == "application/octet-stream"
    assert request.headers["X-Databricks-Workspace-Id"] == "123"


@pytest.mark.parametrize(
    ("operation", "verb", "endpoint", "status_code", "error_code", "error_type"),
    [
        ("get_metadata", "GET", "paths:describe", 404, "NOT_FOUND", NotFound),
        ("download_file", "GET", "content", 404, "NOT_FOUND", NotFound),
        ("upload_file", "PUT", "content", 403, "PERMISSION_DENIED", PermissionDenied),
    ],
)
def test_file_operations_raise_sdk_errors(
    requests_mock, operation, verb, endpoint, status_code, error_code, error_type
):
    requests_mock.register_uri(
        verb,
        f"{_FILES_URL}/{endpoint}",
        status_code=status_code,
        json={"error_code": error_code, "message": "File access failed"},
    )

    kwargs = {"contents": io.BytesIO(b"contents")} if operation == "upload_file" else {}
    with pytest.raises(error_type, match="File access failed"):
        getattr(_sandbox(), operation)(parent="sandboxes/box", path="/tmp/report.bin", **kwargs)


def test_download_file_returns_stream_and_transfer_metadata(requests_mock):
    payload = b"downloaded contents"
    headers = {
        "Content-Length": str(len(payload)),
        "Content-Type": "application/octet-stream",
        "Last-Modified": "Wed, 10 Sep 2025 12:00:00 GMT",
        "ETag": '"file-version"',
        "Accept-Ranges": "bytes",
    }
    requests_mock.get(f"{_FILES_URL}/content", content=payload, headers=headers)

    response = _sandbox(workspace_id="123").download_file("sandboxes/box", "/tmp/report ?#%.bin")

    with response.contents as stream:
        assert stream.read() == payload
    request = requests_mock.last_request
    assert _query_parameters(request) == {"path": ["/tmp/report ?#%.bin"]}
    assert request.headers["Accept"] == "application/octet-stream"
    assert request.headers["X-Databricks-Workspace-Id"] == "123"
    for header in ("Range", "If-Range", "If-Match", "If-None-Match", "If-Modified-Since", "If-Unmodified-Since"):
        assert header not in request.headers
    assert response.content_length == len(payload)
    assert response.content_type == "application/octet-stream"
    assert response.last_modified == "Wed, 10 Sep 2025 12:00:00 GMT"
    assert response.etag == '"file-version"'
    assert response.accept_ranges == "bytes"
    assert response.content_range is None


def test_download_file_returns_partial_stream_and_range_metadata(requests_mock):
    requests_mock.get(
        f"{_FILES_URL}/content",
        status_code=206,
        content=b"part",
        headers={"Content-Length": "4", "Content-Range": "bytes 0-3/100", "ETag": '"file-version"'},
    )

    response = _sandbox().download_file(
        parent="sandboxes/box", path="/tmp/report.bin", byte_range="bytes=0-3", if_range='"file-version"'
    )

    with response.contents as stream:
        assert stream.read() == b"part"
    assert response.content_length == 4
    assert response.content_range == "bytes 0-3/100"
    assert response.etag == '"file-version"'
    assert _query_parameters(requests_mock.last_request) == {
        "path": ["/tmp/report.bin"],
        "byte_range": ["bytes=0-3"],
        "if_range": ['"file-version"'],
    }


@pytest.mark.parametrize(
    ("argument", "value"),
    [
        ("if_match", '"file-version"'),
        ("if_none_match", '"file-version"'),
        ("if_modified_since", "Wed, 10 Sep 2025 12:00:00 GMT"),
        ("if_unmodified_since", "Wed, 10 Sep 2025 12:00:00 GMT"),
    ],
)
def test_download_file_sends_conditional_query_parameters(requests_mock, argument, value):
    requests_mock.get(f"{_FILES_URL}/content", content=b"contents")

    response = _sandbox().download_file("sandboxes/box", "/tmp/report.bin", **{argument: value})

    with response.contents as stream:
        assert stream.read() == b"contents"
    assert _query_parameters(requests_mock.last_request) == {"path": ["/tmp/report.bin"], argument: [value]}
