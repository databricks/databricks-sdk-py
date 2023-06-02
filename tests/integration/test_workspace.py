import base64


def test_workspace_direct_download(w, random):
    from databricks.sdk.service.workspace import Language
    my_notebook = f'/Users/{w.current_user.me().user_name}/{random(12)}.py'
    w.workspace.import_(my_notebook,
                        content=base64.b64encode(b'print(1)').decode(),
                        language=Language.PYTHON)

    content = w.workspace.direct_download(my_notebook)
    assert content == b'# Databricks notebook source\nprint(1)'

    w.workspace.delete(my_notebook)
