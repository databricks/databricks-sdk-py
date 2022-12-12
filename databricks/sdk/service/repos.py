# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

from dataclasses import dataclass
from enum import Enum
from typing import Optional, Dict, List, Any


# all definitions in this file are in alphabetical order


@dataclass
class CreateRepo:

    # Desired path for the repo in the workspace. Must be in the format
    # /Repos/{folder}/{repo-name}.
    path: str
    # Git provider. This field is case-insensitive. The available Git providers
    # are gitHub, bitbucketCloud, gitLab, azureDevOpsServices, gitHubEnterprise,
    # bitbucketServer, gitLabEnterpriseEdition and awsCodeCommit.
    provider: str
    # URL of the Git repository to be linked.
    url: str

    def as_request(self) -> (dict, dict):
        createRepo_query, createRepo_body = {}, {}
        if self.path:
            createRepo_body["path"] = self.path
        if self.provider:
            createRepo_body["provider"] = self.provider
        if self.url:
            createRepo_body["url"] = self.url

        return createRepo_query, createRepo_body

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

    def as_request(self) -> (dict, dict):
        delete_query, delete_body = {}, {}
        if self.repo_id:
            delete_body["repo_id"] = self.repo_id

        return delete_query, delete_body

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

    def as_request(self) -> (dict, dict):
        get_query, get_body = {}, {}
        if self.repo_id:
            get_body["repo_id"] = self.repo_id

        return get_query, get_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "Get":
        return cls(
            repo_id=d.get("repo_id", None),
        )


@dataclass
class List:
    """Get repos"""

    # Token used to get the next page of results. If not specified, returns the
    # first page of results as well as a next page token if there are more
    # results.
    next_page_token: str  # query
    # Filters repos that have paths starting with the given path prefix.
    path_prefix: str  # query

    def as_request(self) -> (dict, dict):
        list_query, list_body = {}, {}
        if self.next_page_token:
            list_query["next_page_token"] = self.next_page_token
        if self.path_prefix:
            list_query["path_prefix"] = self.path_prefix

        return list_query, list_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "List":
        return cls(
            next_page_token=d.get("next_page_token", None),
            path_prefix=d.get("path_prefix", None),
        )


@dataclass
class ListReposResponse:

    # Token that can be specified as a query parameter to the GET /repos
    # endpoint to retrieve the next page of results.
    next_page_token: str

    repos: "List[RepoInfo]"

    def as_request(self) -> (dict, dict):
        listReposResponse_query, listReposResponse_body = {}, {}
        if self.next_page_token:
            listReposResponse_body["next_page_token"] = self.next_page_token
        if self.repos:
            listReposResponse_body["repos"] = [v.as_request()[1] for v in self.repos]

        return listReposResponse_query, listReposResponse_body

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
    # Desired path for the repo in the workspace. Must be in the format
    # /Repos/{folder}/{repo-name}.
    path: str
    # Git provider. This field is case-insensitive. The available Git providers
    # are gitHub, bitbucketCloud, gitLab, azureDevOpsServices, gitHubEnterprise,
    # bitbucketServer, gitLabEnterpriseEdition and awsCodeCommit.
    provider: str
    # URL of the Git repository to be linked.
    url: str

    def as_request(self) -> (dict, dict):
        repoInfo_query, repoInfo_body = {}, {}
        if self.branch:
            repoInfo_body["branch"] = self.branch
        if self.head_commit_id:
            repoInfo_body["head_commit_id"] = self.head_commit_id
        if self.id:
            repoInfo_body["id"] = self.id
        if self.path:
            repoInfo_body["path"] = self.path
        if self.provider:
            repoInfo_body["provider"] = self.provider
        if self.url:
            repoInfo_body["url"] = self.url

        return repoInfo_query, repoInfo_body

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
    # Tag that the local version of the repo is checked out to. Updating the
    # repo to a tag puts the repo in a detached HEAD state. Before committing
    # new changes, you must update the repo to a branch instead of the detached
    # HEAD.
    tag: str

    def as_request(self) -> (dict, dict):
        updateRepo_query, updateRepo_body = {}, {}
        if self.branch:
            updateRepo_body["branch"] = self.branch
        if self.repo_id:
            updateRepo_body["repo_id"] = self.repo_id
        if self.tag:
            updateRepo_body["tag"] = self.tag

        return updateRepo_query, updateRepo_body

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

    def create(self, request: CreateRepo) -> RepoInfo:
        """Create a repo.

        Creates a repo in the workspace and links it to the remote Git repo
        specified. Note that repos created programmatically must be linked to a
        remote Git repo, unlike repos created in the browser."""
        query, body = request.as_request()
        json = self._api.do("POST", "/api/2.0/repos", query=query, body=body)
        return RepoInfo.from_dict(json)

    def delete(self, request: Delete):
        """Delete a repo.

        Deletes the specified repo."""
        query, body = request.as_request()
        self._api.do(
            "DELETE", f"/api/2.0/repos/{request.repo_id}", query=query, body=body
        )

    def get(self, request: Get) -> RepoInfo:
        """Get a repo.

        Returns the repo with the given repo ID."""
        query, body = request.as_request()
        json = self._api.do(
            "GET", f"/api/2.0/repos/{request.repo_id}", query=query, body=body
        )
        return RepoInfo.from_dict(json)

    def list(self, request: List) -> ListReposResponse:
        """Get repos.

        Returns repos that the calling user has Manage permissions on. Results
        are paginated with each page containing twenty repos."""
        query, body = request.as_request()
        json = self._api.do("GET", "/api/2.0/repos", query=query, body=body)
        return ListReposResponse.from_dict(json)

    def update(self, request: UpdateRepo):
        """Update a repo.

        Updates the repo to a different branch or tag, or updates the repo to
        the latest commit on the same branch."""
        query, body = request.as_request()
        self._api.do(
            "PATCH", f"/api/2.0/repos/{request.repo_id}", query=query, body=body
        )
