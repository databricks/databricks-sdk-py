import io
from urllib.parse import parse_qs, urlsplit

import pytest

from databricks.sdk import WorkspaceClient
from databricks.sdk.service.workspace import ExportFormat, ObjectType


def test_recursive_list_traverses_directories_through_workspace_http_api(config, requests_mock):
    requests_mock.get(
        "http://localhost/api/2.0/workspace/list",
        response_list=[
            {
                "json": {
                    "objects": [
                        {"object_type": "DIRECTORY", "path": "/root/nested"},
                        {"object_type": "NOTEBOOK", "path": "/root/top.py"},
                    ]
                }
            },
            {
                "json": {
                    "objects": [
                        {"object_type": "DIRECTORY", "path": "/root/nested/empty"},
                        {"object_type": "FILE", "path": "/root/nested/data.bin"},
                    ]
                }
            },
            {"json": {"objects": []}},
        ],
    )
    workspace = WorkspaceClient(config=config).workspace

    objects = list(workspace.list("/root", notebooks_modified_after=123, recursive=True))

    assert [(obj.path, obj.object_type) for obj in objects] == [
        ("/root/top.py", ObjectType.NOTEBOOK),
        ("/root/nested/data.bin", ObjectType.FILE),
    ]
    assert [parse_qs(urlsplit(request.url).query) for request in requests_mock.request_history] == [
        {"notebooks_modified_after": ["123"], "path": ["/root"]},
        {"notebooks_modified_after": ["123"], "path": ["/root/nested"]},
        {"notebooks_modified_after": ["123"], "path": ["/root/nested/empty"]},
    ]


def test_upload_and_download_use_workspace_http_wire_format(config, requests_mock):
    uploaded = {}

    def capture_upload(request, _context):
        uploaded["body"] = request.body
        return ""

    requests_mock.post("http://localhost/api/2.0/workspace/import", text=capture_upload)
    requests_mock.get(
        "http://localhost/api/2.0/workspace/export",
        content=b"print('downloaded')\n",
    )
    workspace = WorkspaceClient(config=config).workspace

    workspace.upload(
        "/Users/sdk/example.py",
        io.BytesIO(b"print('uploaded')\n"),
        overwrite=True,
    )
    download = workspace.download("/Users/sdk/example.py", format=ExportFormat.AUTO)
    with download as stream:
        assert stream.read() == b"print('downloaded')\n"
    with pytest.raises(ValueError, match="I/O operation on closed file"):
        download.read()

    upload_request, download_request = requests_mock.request_history
    assert upload_request.method == "POST"
    assert upload_request.url == "http://localhost/api/2.0/workspace/import"
    assert upload_request.headers["Content-Type"].startswith("multipart/form-data; boundary=")
    assert b'name="path"' in uploaded["body"]
    assert b"/Users/sdk/example.py" in uploaded["body"]
    assert b'name="language"' in uploaded["body"]
    assert b"PYTHON" in uploaded["body"]
    assert b'name="overwrite"' in uploaded["body"]
    assert b"true" in uploaded["body"]
    assert b'name="content"' in uploaded["body"]
    assert b"print('uploaded')\n" in uploaded["body"]

    assert download_request.method == "GET"
    assert download_request.url.startswith("http://localhost/api/2.0/workspace/export?")
    assert parse_qs(urlsplit(download_request.url).query) == {
        "direct_download": ["true"],
        "format": ["AUTO"],
        "path": ["/Users/sdk/example.py"],
    }
