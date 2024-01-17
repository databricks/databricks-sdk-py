import io
import logging

from databricks.sdk.service.workspace import ImportFormat, Language

_LOG = logging.getLogger('databricks.sdk')

def test_workspace_recursive_list_parallel_xx():
    from databricks.sdk import WorkspaceClient
    w = WorkspaceClient(profile='demo')
    for i in w.workspace.list(f'/Users/serge.smertin@databricks.com', threads=20, recursive=True):
        _LOG.info(f'FOUND: {i}')
    _LOG.info('DONE')


def test_workspace_recursive_list_parallel(w):
    for i in w.workspace._parallel_recursive_listing(f'/Users', threads=20):
        print(f'FOUND: {i}')
    print('DONE')

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


def test_workspace_unzip_notebooks(w, random):
    notebook = f'/Users/{w.current_user.me().user_name}/notebook-{random(12)}.py'

    # Big notebooks can be gzipped during transfer by the API (out of our control)
    # Creating some large content to trigger this behaviour
    notebook_content = ('print(1)\n' * 1000).strip('\n')

    w.workspace.upload(notebook, io.BytesIO(bytes(notebook_content, 'utf-8')))
    with w.workspace.download(notebook) as f:
        content = f.read()
        expected_content = bytes(f'# Databricks notebook source\n{notebook_content}', 'utf-8')
        assert content == expected_content

    w.workspace.delete(notebook)


def test_workspace_download_connection_closed(w, random):
    notebook = f'/Users/{w.current_user.me().user_name}/notebook-{random(12)}.py'

    w.workspace.upload(notebook, io.BytesIO(b'print(1)'))

    for n in range(30):
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
