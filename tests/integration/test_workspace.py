import io

from databricks.sdk.service.workspace import ExportFormat, Language


def test_workspace_upload_download_notebooks(w, random):
    nb = f'/Users/{w.current_user.me().user_name}/{random(12)}'

    w.workspace.upload(nb, io.BytesIO(b'print(1)'), format=ExportFormat.SOURCE, language=Language.PYTHON)
    with w.workspace.download(nb) as f:
        content = f.read()
        assert content == b'# Databricks notebook source\nprint(1)'

    w.workspace.delete(nb)


def test_workspace_upload_download_notebooks_python_files(w, random):
    py = f'/Users/{w.current_user.me().user_name}/{random(12)}.py'

    w.workspace.upload(py, io.BytesIO(b'print(1)'))
    with w.workspace.download(py) as f:
        content = f.read()
        assert content == b'print(1)'

    w.workspace.delete(py)
