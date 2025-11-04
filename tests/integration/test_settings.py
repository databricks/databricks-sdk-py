def test_workspace_conf(w):  # type: ignore[no-untyped-def]
    w.workspace_conf.set_status({"enableResultsDownloading": "false"})
    conf = w.workspace_conf.get_status(keys="enableResultsDownloading")
    assert conf["enableResultsDownloading"] == "false"
    w.workspace_conf.set_status({"enableResultsDownloading": "true"})
    conf = w.workspace_conf.get_status(keys="enableResultsDownloading")
    assert conf["enableResultsDownloading"] == "true"
