# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

import logging
from dataclasses import dataclass
from typing import Dict, Iterator, List

from ._internal import _from_dict, _repeated

_LOG = logging.getLogger('databricks.sdk')

# all definitions in this file are in alphabetical order


@dataclass
class CreateRepo:
    url: str
    provider: str
    path: str = None
    sparse_checkout: 'SparseCheckout' = None

    def as_dict(self) -> dict:
        body = {}
        if self.path: body['path'] = self.path
        if self.provider: body['provider'] = self.provider
        if self.sparse_checkout: body['sparse_checkout'] = self.sparse_checkout.as_dict()
        if self.url: body['url'] = self.url
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateRepo':
        return cls(path=d.get('path', None),
                   provider=d.get('provider', None),
                   sparse_checkout=_from_dict(d, 'sparse_checkout', SparseCheckout),
                   url=d.get('url', None))


@dataclass
class Delete:
    """Delete a repo"""

    repo_id: int


@dataclass
class Get:
    """Get a repo"""

    repo_id: int


@dataclass
class ListRequest:
    """Get repos"""

    next_page_token: str = None
    path_prefix: str = None


@dataclass
class ListReposResponse:
    next_page_token: str = None
    repos: 'List[RepoInfo]' = None

    def as_dict(self) -> dict:
        body = {}
        if self.next_page_token: body['next_page_token'] = self.next_page_token
        if self.repos: body['repos'] = [v.as_dict() for v in self.repos]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListReposResponse':
        return cls(next_page_token=d.get('next_page_token', None), repos=_repeated(d, 'repos', RepoInfo))


@dataclass
class RepoInfo:
    branch: str = None
    head_commit_id: str = None
    id: int = None
    path: str = None
    provider: str = None
    sparse_checkout: 'SparseCheckout' = None
    url: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.branch: body['branch'] = self.branch
        if self.head_commit_id: body['head_commit_id'] = self.head_commit_id
        if self.id: body['id'] = self.id
        if self.path: body['path'] = self.path
        if self.provider: body['provider'] = self.provider
        if self.sparse_checkout: body['sparse_checkout'] = self.sparse_checkout.as_dict()
        if self.url: body['url'] = self.url
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'RepoInfo':
        return cls(branch=d.get('branch', None),
                   head_commit_id=d.get('head_commit_id', None),
                   id=d.get('id', None),
                   path=d.get('path', None),
                   provider=d.get('provider', None),
                   sparse_checkout=_from_dict(d, 'sparse_checkout', SparseCheckout),
                   url=d.get('url', None))


@dataclass
class SparseCheckout:
    patterns: 'List[str]' = None

    def as_dict(self) -> dict:
        body = {}
        if self.patterns: body['patterns'] = [v for v in self.patterns]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'SparseCheckout':
        return cls(patterns=d.get('patterns', None))


@dataclass
class SparseCheckoutUpdate:
    patterns: 'List[str]' = None

    def as_dict(self) -> dict:
        body = {}
        if self.patterns: body['patterns'] = [v for v in self.patterns]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'SparseCheckoutUpdate':
        return cls(patterns=d.get('patterns', None))


@dataclass
class UpdateRepo:
    repo_id: int
    branch: str = None
    sparse_checkout: 'SparseCheckoutUpdate' = None
    tag: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.branch: body['branch'] = self.branch
        if self.repo_id: body['repo_id'] = self.repo_id
        if self.sparse_checkout: body['sparse_checkout'] = self.sparse_checkout.as_dict()
        if self.tag: body['tag'] = self.tag
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'UpdateRepo':
        return cls(branch=d.get('branch', None),
                   repo_id=d.get('repo_id', None),
                   sparse_checkout=_from_dict(d, 'sparse_checkout', SparseCheckoutUpdate),
                   tag=d.get('tag', None))


class ReposAPI:
    """The Repos API allows users to manage their git repos. Users can use the API to access all repos that they
    have manage permissions on.
    
    Databricks Repos is a visual Git client in Databricks. It supports common Git operations such a cloning a
    repository, committing and pushing, pulling, branch management, and visual comparison of diffs when
    committing.
    
    Within Repos you can develop code in notebooks or other files and follow data science and engineering code
    development best practices using Git for version control, collaboration, and CI/CD."""

    def __init__(self, api_client):
        self._api = api_client

    def create(self,
               url: str,
               provider: str,
               *,
               path: str = None,
               sparse_checkout: SparseCheckout = None,
               **kwargs) -> RepoInfo:
        """Create a repo.
        
        Creates a repo in the workspace and links it to the remote Git repo specified. Note that repos created
        programmatically must be linked to a remote Git repo, unlike repos created in the browser."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = CreateRepo(path=path, provider=provider, sparse_checkout=sparse_checkout, url=url)
        body = request.as_dict()

        json = self._api.do('POST', '/api/2.0/repos', body=body)
        return RepoInfo.from_dict(json)

    def delete(self, repo_id: int, **kwargs):
        """Delete a repo.
        
        Deletes the specified repo."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = Delete(repo_id=repo_id)

        self._api.do('DELETE', f'/api/2.0/repos/{request.repo_id}')

    def get(self, repo_id: int, **kwargs) -> RepoInfo:
        """Get a repo.
        
        Returns the repo with the given repo ID."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = Get(repo_id=repo_id)

        json = self._api.do('GET', f'/api/2.0/repos/{request.repo_id}')
        return RepoInfo.from_dict(json)

    def list(self, *, next_page_token: str = None, path_prefix: str = None, **kwargs) -> Iterator[RepoInfo]:
        """Get repos.
        
        Returns repos that the calling user has Manage permissions on. Results are paginated with each page
        containing twenty repos."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = ListRequest(next_page_token=next_page_token, path_prefix=path_prefix)

        query = {}
        if next_page_token: query['next_page_token'] = request.next_page_token
        if path_prefix: query['path_prefix'] = request.path_prefix

        while True:
            json = self._api.do('GET', '/api/2.0/repos', query=query)
            if 'repos' not in json or not json['repos']:
                return
            for v in json['repos']:
                yield RepoInfo.from_dict(v)
            if 'next_page_token' not in json or not json['next_page_token']:
                return
            query['next_page_token'] = json['next_page_token']

    def update(self,
               repo_id: int,
               *,
               branch: str = None,
               sparse_checkout: SparseCheckoutUpdate = None,
               tag: str = None,
               **kwargs):
        """Update a repo.
        
        Updates the repo to a different branch or tag, or updates the repo to the latest commit on the same
        branch."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = UpdateRepo(branch=branch, repo_id=repo_id, sparse_checkout=sparse_checkout, tag=tag)
        body = request.as_dict()
        self._api.do('PATCH', f'/api/2.0/repos/{request.repo_id}', body=body)
