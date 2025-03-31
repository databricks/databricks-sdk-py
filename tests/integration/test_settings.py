from databricks.sdk.settings.v2.client import WorkspaceConfClient

def test_workspace_conf(w):
    wcc = WorkspaceConfClient(config=w)
    wcc.set_status({"enableResultsDownloading": "false"})
    conf = wcc.get_status(keys="enableResultsDownloading")
    assert conf["enableResultsDownloading"] == "false"
    wcc.set_status({"enableResultsDownloading": "true"})
    conf = wcc.get_status(keys="enableResultsDownloading")
    assert conf["enableResultsDownloading"] == "true"
