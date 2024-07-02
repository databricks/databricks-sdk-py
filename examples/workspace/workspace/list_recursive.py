from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

names = []
for i in w.workspace.list(f'/Users/{w.current_user.me().user_name}', recursive=True):
    names.append(i.path)
assert len(names) > 0