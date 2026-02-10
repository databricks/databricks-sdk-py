# Syncing with Upstream Databricks SDK

This repository is a fork of the [Databricks Python SDK](https://github.com/databricks/databricks-sdk-py) maintained for StackQL provider development. We periodically sync with upstream to incorporate SDK updates while maintaining our own provider-specific code.

## Initial Setup

If you're setting up this repository for the first time:

```bash
# Clone the repository
git clone git@github.com:stackql/stackql-provider-databricks.git
cd stackql-provider-databricks

# Add upstream remote
git remote add upstream https://github.com/databricks/databricks-sdk-py.git

# Fetch upstream branches
git fetch upstream

# Switch to the working branch
git checkout stackql-provider
```

## Pulling Upstream Changes

To sync with the latest Databricks SDK updates:

```bash
# Ensure you're on the stackql-provider branch
git checkout stackql-provider

# Fetch the latest changes from upstream
git fetch upstream

# Merge upstream main into your branch
git merge upstream/main

# If there are conflicts, resolve them, then:
# git add <resolved-files>
# git commit

# Push the updated branch to origin
git push origin stackql-provider
```

## Resolving Merge Conflicts

If you encounter conflicts during the merge:

1. Git will list the conflicting files
2. Open each file and look for conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`)
3. Resolve conflicts by choosing the appropriate code or combining both versions
4. Stage the resolved files: `git add <file>`
5. Complete the merge: `git commit`
6. Push changes: `git push origin stackql-provider`

## Checking Sync Status

To see how far behind upstream you are:

```bash
git fetch upstream
git log stackql-provider..upstream/main --oneline
```

## Branch Strategy

- **`main`**: Mirrors the upstream repository (untouched)
- **`stackql-provider`**: Our working branch with StackQL-specific modifications
- Never create pull requests to upstream - this is a permanent fork

## Verifying Remotes

To confirm your remotes are configured correctly:

```bash
git remote -v
```

Should show:
```
origin    git@github.com:stackql/stackql-provider-databricks.git (fetch)
origin    git@github.com:stackql/stackql-provider-databricks.git (push)
upstream  https://github.com/databricks/databricks-sdk-py.git (fetch)
upstream  https://github.com/databricks/databricks-sdk-py.git (push)
```
