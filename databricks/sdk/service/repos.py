# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Any


# all definitions in this file are in alphabetical order


@dataclass
class CreateRepo:

    # Desired path for the repo in the workspace. Must be in the format /Repos/{folder}/{repo-name}.
    path: str
    # Git provider. This field is case-insensitive. The available Git providers are gitHub, bitbucketCloud, gitLab,
    # azureDevOpsServices, gitHubEnterprise, bitbucketServer, gitLabEnterpriseEdition and awsCodeCommit.
    provider: str
    # URL of the Git repository to be linked.
    url: str

    def as_dict(self) -> dict:
        body = {}
        if self.path:
            body["path"] = self.path
        if self.provider:
            body["provider"] = self.provider
        if self.url:
            body["url"] = self.url

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "CreateRepo":
        return cls(
            path=d.get("path", None),
            provider=d.get("provider", None),
            url=d.get("url", None),
        )


@dataclass
class Delete:
    """Delete a repo"""

    # The ID for the corresponding repo to access.
    repo_id: int  # path

    def as_dict(self) -> dict:
        body = {}
        if self.repo_id:
            body["repo_id"] = self.repo_id

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "Delete":
        return cls(
            repo_id=d.get("repo_id", None),
        )


@dataclass
class Get:
    """Get a repo"""

    # The ID for the corresponding repo to access.
    repo_id: int  # path

    def as_dict(self) -> dict:
        body = {}
        if self.repo_id:
            body["repo_id"] = self.repo_id

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "Get":
        return cls(
            repo_id=d.get("repo_id", None),
        )


@dataclass
class ListRequest:
    """Get repos"""

    # Token used to get the next page of results. If not specified, returns the first page of results as well as a next
    # page token if there are more results.
    next_page_token: str  # query
    # Filters repos that have paths starting with the given path prefix.
    path_prefix: str  # query

    def as_dict(self) -> dict:
        body = {}
        if self.next_page_token:
            body["next_page_token"] = self.next_page_token
        if self.path_prefix:
            body["path_prefix"] = self.path_prefix

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ListRequest":
        return cls(
            next_page_token=d.get("next_page_token", None),
            path_prefix=d.get("path_prefix", None),
        )


@dataclass
class ListReposResponse:

    # Token that can be specified as a query parameter to the GET /repos endpoint to retrieve the next page of results.
    next_page_token: str

    repos: "List[RepoInfo]"

    def as_dict(self) -> dict:
        body = {}
        if self.next_page_token:
            body["next_page_token"] = self.next_page_token
        if self.repos:
            body["repos"] = [v.as_dict() for v in self.repos]

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ListReposResponse":
        return cls(
            next_page_token=d.get("next_page_token", None),
            repos=[RepoInfo.from_dict(v) for v in d["repos"]] if "repos" in d else None,
        )


@dataclass
class RepoInfo:

    # Branch that the local version of the repo is checked out to.
    branch: str
    # SHA-1 hash representing the commit ID of the current HEAD of the repo.
    head_commit_id: str
    # ID of the repo object in the workspace.
    id: int
    # Desired path for the repo in the workspace. Must be in the format /Repos/{folder}/{repo-name}.
    path: str
    # Git provider. This field is case-insensitive. The available Git providers are gitHub, bitbucketCloud, gitLab,
    # azureDevOpsServices, gitHubEnterprise, bitbucketServer, gitLabEnterpriseEdition and awsCodeCommit.
    provider: str
    # URL of the Git repository to be linked.
    url: str

    def as_dict(self) -> dict:
        body = {}
        if self.branch:
            body["branch"] = self.branch
        if self.head_commit_id:
            body["head_commit_id"] = self.head_commit_id
        if self.id:
            body["id"] = self.id
        if self.path:
            body["path"] = self.path
        if self.provider:
            body["provider"] = self.provider
        if self.url:
            body["url"] = self.url

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "RepoInfo":
        return cls(
            branch=d.get("branch", None),
            head_commit_id=d.get("head_commit_id", None),
            id=d.get("id", None),
            path=d.get("path", None),
            provider=d.get("provider", None),
            url=d.get("url", None),
        )


@dataclass
class UpdateRepo:

    # Branch that the local version of the repo is checked out to.
    branch: str
    # The ID for the corresponding repo to access.
    repo_id: int  # path
    # Tag that the local version of the repo is checked out to. Updating the repo to a tag puts the repo in a detached
    # HEAD state. Before committing new changes, you must update the repo to a branch instead of the detached HEAD.
    tag: str

    def as_dict(self) -> dict:
        body = {}
        if self.branch:
            body["branch"] = self.branch
        if self.repo_id:
            body["repo_id"] = self.repo_id
        if self.tag:
            body["tag"] = self.tag

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "UpdateRepo":
        return cls(
            branch=d.get("branch", None),
            repo_id=d.get("repo_id", None),
            tag=d.get("tag", None),
        )


class ReposAPI:
    def __init__(self, api_client):
        self._api = api_client

    def create(
        self, url: str, provider: str, *, path: str = None, **kwargs
    ) -> RepoInfo:
        """Create a repo.

        Creates a repo in the workspace and links it to the remote Git repo
        specified. Note that repos created programmatically must be linked to a
        remote Git repo, unlike repos created in the browser."""
        request = kwargs.get("request", None)
        if not request:  # request is not given through keyed args
            request = CreateRepo(path=path, provider=provider, url=url)
        body = request.as_dict()

        json = self._api.do("POST", "/api/2.0/repos", body=body)
        return RepoInfo.from_dict(json)

    def delete(self, repo_id: int, **kwargs):
        """Delete a repo.

        Deletes the specified repo."""
        request = kwargs.get("request", None)
        if not request:  # request is not given through keyed args
            request = Delete(repo_id=repo_id)

        self._api.do("DELETE", f"/api/2.0/repos/{request.repo_id}")

    def get(self, repo_id: int, **kwargs) -> RepoInfo:
        """Get a repo.

        Returns the repo with the given repo ID."""
        request = kwargs.get("request", None)
        if not request:  # request is not given through keyed args
            request = Get(repo_id=repo_id)

        json = self._api.do("GET", f"/api/2.0/repos/{request.repo_id}")
        return RepoInfo.from_dict(json)

    def list(
        self, *, next_page_token: str = None, path_prefix: str = None, **kwargs
    ) -> ListReposResponse:
        """Get repos.

        Returns repos that the calling user has Manage permissions on. Results
        are paginated with each page containing twenty repos."""
        request = kwargs.get("request", None)
        if not request:  # request is not given through keyed args
            request = ListRequest(
                next_page_token=next_page_token, path_prefix=path_prefix
            )

        query = {}
        if next_page_token:
            query["next_page_token"] = request.next_page_token
        if path_prefix:
            query["path_prefix"] = request.path_prefix

        json = self._api.do("GET", "/api/2.0/repos", query=query)
        return ListReposResponse.from_dict(json)

    def update(self, repo_id: int, *, branch: str = None, tag: str = None, **kwargs):
        """Update a repo.

        Updates the repo to a different branch or tag, or updates the repo to
        the latest commit on the same branch."""
        request = kwargs.get("request", None)
        if not request:  # request is not given through keyed args
            request = UpdateRepo(branch=branch, repo_id=repo_id, tag=tag)
        body = request.as_dict()

        self._api.do("PATCH", f"/api/2.0/repos/{request.repo_id}", body=body)
