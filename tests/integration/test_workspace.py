import io

from databricks.sdk.service.workspace import ImportFormat, Language


def test_workspace_recursive_list(w, random):
    names = []
    for i in w.workspace.list(f'/Users/{w.current_user.me().user_name}', recursive=True):
        names.append(i.path)
    assert len(names) > 0


def test_workspace_upload_download_notebooks(w, random):
    notebook = f'/Users/{w.current_user.me().user_name}/notebook-{random(12)}.py'

    w.workspace.upload(notebook, io.BytesIO(b'print(1)'))
    with w.workspace.download(notebook) as f:
        content = f.read()
        assert content == b'# Databricks notebook source\nprint(1)'

    w.workspace.delete(notebook)


def test_workspace_upload_download_files(w, random):
    py_file = f'/Users/{w.current_user.me().user_name}/file-{random(12)}.py'

    w.workspace.upload(py_file, io.BytesIO(b'print(1)'), format=ImportFormat.AUTO)
    with w.workspace.download(py_file) as f:
        content = f.read()
        assert content == b'print(1)'

    w.workspace.delete(py_file)


def test_workspace_upload_download_txt_files(w, random):
    txt_file = f'/Users/{w.current_user.me().user_name}/txt-{random(12)}.txt'

    w.workspace.upload(txt_file, io.BytesIO(b'print(1)'), format=ImportFormat.AUTO)
    with w.workspace.download(txt_file) as f:
        content = f.read()
        assert content == b'print(1)'

    w.workspace.delete(txt_file)


def test_workspace_upload_download_notebooks_no_extension(w, random):
    nb = f'/Users/{w.current_user.me().user_name}/notebook-{random(12)}'

    w.workspace.upload(nb, io.BytesIO(b'print(1)'), format=ImportFormat.SOURCE, language=Language.PYTHON)
    with w.workspace.download(nb) as f:
        content = f.read()
        assert content == b'# Databricks notebook source\nprint(1)'

    w.workspace.delete(nb)
