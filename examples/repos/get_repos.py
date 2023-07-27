import time

from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

root = f'sdk-{time.time_ns()}'

ri = w.repos.create(path=root, url="https://github.com/shreyas-goenka/empty-repo.git", provider="github")

by_id = w.repos.get(repo_id=ri.id)

# cleanup
w.repos.delete(repo_id=ri.id)
