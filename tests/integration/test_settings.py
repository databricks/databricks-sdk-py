def test_workspace_conf(w):
    # The default value is null, so we set to true initially.
    w.workspace_conf.set_status({"enableResultsDownloading": "true"})
    conf = w.workspace_conf.get_status(keys="enableResultsDownloading")
    assert conf["enableResultsDownloading"] == "true"
    w.workspace_conf.set_status({"enableResultsDownloading": "false"})
    conf = w.workspace_conf.get_status(keys="enableResultsDownloading")
    assert conf["enableResultsDownloading"] == "false"
    # Reset to true
    w.workspace_conf.set_status({"enableResultsDownloading": "true"})

