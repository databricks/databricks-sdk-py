import io

from databricks.sdk.workspace.v2.workspace import ImportFormat, Language
from databricks.sdk.workspace.v2.client import WorkspaceClient
from databricks.sdk.iam.v2.client import CurrentUserClient

def test_workspace_recursive_list(w, workspace_dir, random):
    wc = WorkspaceClient(config=w)
    # create a file in the directory
    file = f"{workspace_dir}/file-{random(12)}.py"
    wc.upload(file, io.BytesIO(b"print(1)"))
    # create a subdirectory
    subdirectory = f"{workspace_dir}/subdir-{random(12)}"
    wc.mkdirs(subdirectory)
    # create a file in the subdirectory
    subfile = f"{subdirectory}/subfile-{random(12)}.py"
    wc.upload(subfile, io.BytesIO(b"print(2)"))
    # list the directory recursively
    names = []
    for i in wc.list(workspace_dir, recursive=True):
        names.append(i.path)
    assert len(names) == 2


def test_workspace_upload_download_notebooks(w, random):
    wc = WorkspaceClient(config=w)
    cuc = CurrentUserClient(config=w)
    
    notebook = f"/Users/{cuc.me().user_name}/notebook-{random(12)}.py"
    
    wc.upload(notebook, io.BytesIO(b"print(1)"))
    with wc.download(notebook) as f:
        content = f.read()
        assert content == b"# Databricks notebook source\nprint(1)"

    wc.delete(notebook)


def test_workspace_unzip_notebooks(w, random):
    wc = WorkspaceClient(config=w)
    cuc = CurrentUserClient(config=w)
    
    notebook = f"/Users/{cuc.me().user_name}/notebook-{random(12)}.py"

    # Big notebooks can be gzipped during transfer by the API (out of our control)
    # Creating some large content to trigger this behaviour
    notebook_content = ("print(1)\n" * 1000).strip("\n")

    wc.upload(notebook, io.BytesIO(bytes(notebook_content, "utf-8")))
    with wc.download(notebook) as f:
        content = f.read()
        expected_content = bytes(f"# Databricks notebook source\n{notebook_content}", "utf-8")
        assert content == expected_content

    wc.delete(notebook)


def test_workspace_download_connection_closed(w, random):
    wc = WorkspaceClient(config=w)
    cuc = CurrentUserClient(config=w)
    
    notebook = f"/Users/{cuc.me().user_name}/notebook-{random(12)}.py"

    wc.upload(notebook, io.BytesIO(b"print(1)"))

    for n in range(30):
        with wc.download(notebook) as f:
            content = f.read()
            assert content == b"# Databricks notebook source\nprint(1)"

    wc.delete(notebook)


def test_workspace_upload_download_files(w, random):
    wc = WorkspaceClient(config=w)
    cuc = CurrentUserClient(config=w)
    
    py_file = f"/Users/{cuc.me().user_name}/file-{random(12)}.py"

    wc.upload(py_file, io.BytesIO(b"print(1)"), format=ImportFormat.AUTO)
    with wc.download(py_file) as f:
        content = f.read()
        assert content == b"print(1)"

    wc.delete(py_file)


def test_workspace_upload_download_txt_files(w, random):
    wc = WorkspaceClient(config=w)
    cuc = CurrentUserClient(config=w)
    
    txt_file = f"/Users/{cuc.me().user_name}/txt-{random(12)}.txt"

    wc.upload(txt_file, io.BytesIO(b"print(1)"), format=ImportFormat.AUTO)
    with wc.download(txt_file) as f:
        content = f.read()
        assert content == b"print(1)"

    wc.delete(txt_file)


def test_workspace_upload_download_notebooks_no_extension(w, random):
    wc = WorkspaceClient(config=w)
    cuc = CurrentUserClient(config=w)
    
    nb = f"/Users/{cuc.me().user_name}/notebook-{random(12)}"

    wc.upload(
        nb,
        io.BytesIO(b"print(1)"),
        format=ImportFormat.SOURCE,
        language=Language.PYTHON,
    )
    with wc.download(nb) as f:
        content = f.read()
        assert content == b"# Databricks notebook source\nprint(1)"

    wc.delete(nb)
