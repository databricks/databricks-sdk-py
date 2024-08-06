import io

from databricks.sdk.service.workspace import ImportFormat, Language


def test_workspace_recursive_list(w, workspace_dir, random):
    # create a file in the directory
    file = f'{workspace_dir}/file-{random(12)}.py'
    w.workspace.upload(file, io.BytesIO(b'print(1)'))
    # create a subdirectory
    subdirectory = f'{workspace_dir}/subdir-{random(12)}'
    w.workspace.mkdirs(subdirectory)
    # create a file in the subdirectory
    subfile = f'{subdirectory}/subfile-{random(12)}.py'
    w.workspace.upload(subfile, io.BytesIO(b'print(2)'))
    # list the directory recursively
    names = []
    for i in w.workspace.list(workspace_dir, recursive=True):
        names.append(i.path)
    assert len(names) == 2


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
