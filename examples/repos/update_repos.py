import time

from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

root = f'sdk-{time.time_ns()}'

ri = w.repos.create(path=root, url="https://github.com/shreyas-goenka/empty-repo.git", provider="github")

w.repos.update(repo_id=ri.id, branch="foo")

# cleanup
w.repos.delete(repo_id=ri.id)
