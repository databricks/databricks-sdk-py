# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

import logging
from dataclasses import dataclass
from enum import Enum
from typing import Dict, Iterator, List, Optional

from ._internal import _enum, _from_dict, _repeated

_LOG = logging.getLogger('databricks.sdk')

# all definitions in this file are in alphabetical order


@dataclass
class AclItem:
    principal: str
    permission: 'AclPermission'

    def as_dict(self) -> dict:
        body = {}
        if self.permission is not None: body['permission'] = self.permission.value
        if self.principal is not None: body['principal'] = self.principal
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'AclItem':
        return cls(permission=_enum(d, 'permission', AclPermission), principal=d.get('principal', None))


class AclPermission(Enum):

    MANAGE = 'MANAGE'
    READ = 'READ'
    WRITE = 'WRITE'


@dataclass
class AzureKeyVaultSecretScopeMetadata:
    resource_id: str
    dns_name: str

    def as_dict(self) -> dict:
        body = {}
        if self.dns_name is not None: body['dns_name'] = self.dns_name
        if self.resource_id is not None: body['resource_id'] = self.resource_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'AzureKeyVaultSecretScopeMetadata':
        return cls(dns_name=d.get('dns_name', None), resource_id=d.get('resource_id', None))


@dataclass
class CreateCredentials:
    git_provider: str
    git_username: Optional[str] = None
    personal_access_token: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.git_provider is not None: body['git_provider'] = self.git_provider
        if self.git_username is not None: body['git_username'] = self.git_username
        if self.personal_access_token is not None: body['personal_access_token'] = self.personal_access_token
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateCredentials':
        return cls(git_provider=d.get('git_provider', None),
                   git_username=d.get('git_username', None),
                   personal_access_token=d.get('personal_access_token', None))


@dataclass
class CreateCredentialsResponse:
    credential_id: Optional[int] = None
    git_provider: Optional[str] = None
    git_username: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.credential_id is not None: body['credential_id'] = self.credential_id
        if self.git_provider is not None: body['git_provider'] = self.git_provider
        if self.git_username is not None: body['git_username'] = self.git_username
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateCredentialsResponse':
        return cls(credential_id=d.get('credential_id', None),
                   git_provider=d.get('git_provider', None),
                   git_username=d.get('git_username', None))


@dataclass
class CreateRepo:
    url: str
    provider: str
    path: Optional[str] = None
    sparse_checkout: Optional['SparseCheckout'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.path is not None: body['path'] = self.path
        if self.provider is not None: body['provider'] = self.provider
        if self.sparse_checkout: body['sparse_checkout'] = self.sparse_checkout.as_dict()
        if self.url is not None: body['url'] = self.url
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateRepo':
        return cls(path=d.get('path', None),
                   provider=d.get('provider', None),
                   sparse_checkout=_from_dict(d, 'sparse_checkout', SparseCheckout),
                   url=d.get('url', None))


@dataclass
class CreateScope:
    scope: str
    backend_azure_keyvault: Optional['AzureKeyVaultSecretScopeMetadata'] = None
    initial_manage_principal: Optional[str] = None
    scope_backend_type: Optional['ScopeBackendType'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.backend_azure_keyvault: body['backend_azure_keyvault'] = self.backend_azure_keyvault.as_dict()
        if self.initial_manage_principal is not None:
            body['initial_manage_principal'] = self.initial_manage_principal
        if self.scope is not None: body['scope'] = self.scope
        if self.scope_backend_type is not None: body['scope_backend_type'] = self.scope_backend_type.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateScope':
        return cls(backend_azure_keyvault=_from_dict(d, 'backend_azure_keyvault',
                                                     AzureKeyVaultSecretScopeMetadata),
                   initial_manage_principal=d.get('initial_manage_principal', None),
                   scope=d.get('scope', None),
                   scope_backend_type=_enum(d, 'scope_backend_type', ScopeBackendType))


@dataclass
class CredentialInfo:
    credential_id: Optional[int] = None
    git_provider: Optional[str] = None
    git_username: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.credential_id is not None: body['credential_id'] = self.credential_id
        if self.git_provider is not None: body['git_provider'] = self.git_provider
        if self.git_username is not None: body['git_username'] = self.git_username
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CredentialInfo':
        return cls(credential_id=d.get('credential_id', None),
                   git_provider=d.get('git_provider', None),
                   git_username=d.get('git_username', None))


@dataclass
class Delete:
    path: str
    recursive: Optional[bool] = None

    def as_dict(self) -> dict:
        body = {}
        if self.path is not None: body['path'] = self.path
        if self.recursive is not None: body['recursive'] = self.recursive
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Delete':
        return cls(path=d.get('path', None), recursive=d.get('recursive', None))


@dataclass
class DeleteAcl:
    scope: str
    principal: str

    def as_dict(self) -> dict:
        body = {}
        if self.principal is not None: body['principal'] = self.principal
        if self.scope is not None: body['scope'] = self.scope
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'DeleteAcl':
        return cls(principal=d.get('principal', None), scope=d.get('scope', None))


@dataclass
class DeleteGitCredentialRequest:
    """Delete a credential"""

    credential_id: int


@dataclass
class DeleteRepoRequest:
    """Delete a repo"""

    repo_id: int


@dataclass
class DeleteScope:
    scope: str

    def as_dict(self) -> dict:
        body = {}
        if self.scope is not None: body['scope'] = self.scope
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'DeleteScope':
        return cls(scope=d.get('scope', None))


@dataclass
class DeleteSecret:
    scope: str
    key: str

    def as_dict(self) -> dict:
        body = {}
        if self.key is not None: body['key'] = self.key
        if self.scope is not None: body['scope'] = self.scope
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'DeleteSecret':
        return cls(key=d.get('key', None), scope=d.get('scope', None))


class ExportFormat(Enum):

    DBC = 'DBC'
    HTML = 'HTML'
    JUPYTER = 'JUPYTER'
    R_MARKDOWN = 'R_MARKDOWN'
    SOURCE = 'SOURCE'


@dataclass
class ExportRequest:
    """Export a workspace object"""

    path: str
    format: Optional['ExportFormat'] = None


@dataclass
class ExportResponse:
    content: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.content is not None: body['content'] = self.content
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ExportResponse':
        return cls(content=d.get('content', None))


@dataclass
class GetAclRequest:
    """Get secret ACL details"""

    scope: str
    principal: str


@dataclass
class GetCredentialsResponse:
    credentials: Optional['List[CredentialInfo]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.credentials: body['credentials'] = [v.as_dict() for v in self.credentials]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetCredentialsResponse':
        return cls(credentials=_repeated(d, 'credentials', CredentialInfo))


@dataclass
class GetGitCredentialRequest:
    """Get a credential entry"""

    credential_id: int


@dataclass
class GetRepoRequest:
    """Get a repo"""

    repo_id: int


@dataclass
class GetStatusRequest:
    """Get status"""

    path: str


@dataclass
class Import:
    path: str
    content: Optional[str] = None
    format: Optional['ImportFormat'] = None
    language: Optional['Language'] = None
    overwrite: Optional[bool] = None

    def as_dict(self) -> dict:
        body = {}
        if self.content is not None: body['content'] = self.content
        if self.format is not None: body['format'] = self.format.value
        if self.language is not None: body['language'] = self.language.value
        if self.overwrite is not None: body['overwrite'] = self.overwrite
        if self.path is not None: body['path'] = self.path
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Import':
        return cls(content=d.get('content', None),
                   format=_enum(d, 'format', ImportFormat),
                   language=_enum(d, 'language', Language),
                   overwrite=d.get('overwrite', None),
                   path=d.get('path', None))


class ImportFormat(Enum):
    """This specifies the format of the file to be imported.
    
    The value is case sensitive.
    
    - `AUTO`: The item is imported depending on an analysis of the item's extension and the header
    content provided in the request. If the item is imported as a notebook, then the item's
    extension is automatically removed. - `SOURCE`: The notebook is imported as source code. -
    `HTML`: The notebook is imported as an HTML file. - `JUPYTER`: The notebook is imported as a
    Jupyter/IPython Notebook file. - `DBC`: The notebook is imported in Databricks archive format.
    Required for directories. - `R_MARKDOWN`: The notebook is imported from R Markdown format."""

    AUTO = 'AUTO'
    DBC = 'DBC'
    HTML = 'HTML'
    JUPYTER = 'JUPYTER'
    R_MARKDOWN = 'R_MARKDOWN'
    SOURCE = 'SOURCE'


class Language(Enum):
    """The language of the object. This value is set only if the object type is `NOTEBOOK`."""

    PYTHON = 'PYTHON'
    R = 'R'
    SCALA = 'SCALA'
    SQL = 'SQL'


@dataclass
class ListAclsRequest:
    """Lists ACLs"""

    scope: str


@dataclass
class ListAclsResponse:
    items: Optional['List[AclItem]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.items: body['items'] = [v.as_dict() for v in self.items]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListAclsResponse':
        return cls(items=_repeated(d, 'items', AclItem))


@dataclass
class ListReposRequest:
    """Get repos"""

    next_page_token: Optional[str] = None
    path_prefix: Optional[str] = None


@dataclass
class ListReposResponse:
    next_page_token: Optional[str] = None
    repos: Optional['List[RepoInfo]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.next_page_token is not None: body['next_page_token'] = self.next_page_token
        if self.repos: body['repos'] = [v.as_dict() for v in self.repos]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListReposResponse':
        return cls(next_page_token=d.get('next_page_token', None), repos=_repeated(d, 'repos', RepoInfo))


@dataclass
class ListResponse:
    objects: Optional['List[ObjectInfo]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.objects: body['objects'] = [v.as_dict() for v in self.objects]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListResponse':
        return cls(objects=_repeated(d, 'objects', ObjectInfo))


@dataclass
class ListScopesResponse:
    scopes: Optional['List[SecretScope]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.scopes: body['scopes'] = [v.as_dict() for v in self.scopes]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListScopesResponse':
        return cls(scopes=_repeated(d, 'scopes', SecretScope))


@dataclass
class ListSecretsRequest:
    """List secret keys"""

    scope: str


@dataclass
class ListSecretsResponse:
    secrets: Optional['List[SecretMetadata]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.secrets: body['secrets'] = [v.as_dict() for v in self.secrets]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListSecretsResponse':
        return cls(secrets=_repeated(d, 'secrets', SecretMetadata))


@dataclass
class ListWorkspaceRequest:
    """List contents"""

    path: str
    notebooks_modified_after: Optional[int] = None


@dataclass
class Mkdirs:
    path: str

    def as_dict(self) -> dict:
        body = {}
        if self.path is not None: body['path'] = self.path
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Mkdirs':
        return cls(path=d.get('path', None))


@dataclass
class ObjectInfo:
    created_at: Optional[int] = None
    language: Optional['Language'] = None
    modified_at: Optional[int] = None
    object_id: Optional[int] = None
    object_type: Optional['ObjectType'] = None
    path: Optional[str] = None
    size: Optional[int] = None

    def as_dict(self) -> dict:
        body = {}
        if self.created_at is not None: body['created_at'] = self.created_at
        if self.language is not None: body['language'] = self.language.value
        if self.modified_at is not None: body['modified_at'] = self.modified_at
        if self.object_id is not None: body['object_id'] = self.object_id
        if self.object_type is not None: body['object_type'] = self.object_type.value
        if self.path is not None: body['path'] = self.path
        if self.size is not None: body['size'] = self.size
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ObjectInfo':
        return cls(created_at=d.get('created_at', None),
                   language=_enum(d, 'language', Language),
                   modified_at=d.get('modified_at', None),
                   object_id=d.get('object_id', None),
                   object_type=_enum(d, 'object_type', ObjectType),
                   path=d.get('path', None),
                   size=d.get('size', None))


class ObjectType(Enum):
    """The type of the object in workspace.
    
    - `NOTEBOOK`: document that contains runnable code, visualizations, and explanatory text. -
    `DIRECTORY`: directory - `LIBRARY`: library - `FILE`: file - `REPO`: repository"""

    DIRECTORY = 'DIRECTORY'
    FILE = 'FILE'
    LIBRARY = 'LIBRARY'
    NOTEBOOK = 'NOTEBOOK'
    REPO = 'REPO'


@dataclass
class PutAcl:
    scope: str
    principal: str
    permission: 'AclPermission'

    def as_dict(self) -> dict:
        body = {}
        if self.permission is not None: body['permission'] = self.permission.value
        if self.principal is not None: body['principal'] = self.principal
        if self.scope is not None: body['scope'] = self.scope
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'PutAcl':
        return cls(permission=_enum(d, 'permission', AclPermission),
                   principal=d.get('principal', None),
                   scope=d.get('scope', None))


@dataclass
class PutSecret:
    scope: str
    key: str
    bytes_value: Optional[str] = None
    string_value: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.bytes_value is not None: body['bytes_value'] = self.bytes_value
        if self.key is not None: body['key'] = self.key
        if self.scope is not None: body['scope'] = self.scope
        if self.string_value is not None: body['string_value'] = self.string_value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'PutSecret':
        return cls(bytes_value=d.get('bytes_value', None),
                   key=d.get('key', None),
                   scope=d.get('scope', None),
                   string_value=d.get('string_value', None))


@dataclass
class RepoInfo:
    branch: Optional[str] = None
    head_commit_id: Optional[str] = None
    id: Optional[int] = None
    path: Optional[str] = None
    provider: Optional[str] = None
    sparse_checkout: Optional['SparseCheckout'] = None
    url: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.branch is not None: body['branch'] = self.branch
        if self.head_commit_id is not None: body['head_commit_id'] = self.head_commit_id
        if self.id is not None: body['id'] = self.id
        if self.path is not None: body['path'] = self.path
        if self.provider is not None: body['provider'] = self.provider
        if self.sparse_checkout: body['sparse_checkout'] = self.sparse_checkout.as_dict()
        if self.url is not None: body['url'] = self.url
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


class ScopeBackendType(Enum):

    AZURE_KEYVAULT = 'AZURE_KEYVAULT'
    DATABRICKS = 'DATABRICKS'


@dataclass
class SecretMetadata:
    key: Optional[str] = None
    last_updated_timestamp: Optional[int] = None

    def as_dict(self) -> dict:
        body = {}
        if self.key is not None: body['key'] = self.key
        if self.last_updated_timestamp is not None:
            body['last_updated_timestamp'] = self.last_updated_timestamp
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'SecretMetadata':
        return cls(key=d.get('key', None), last_updated_timestamp=d.get('last_updated_timestamp', None))


@dataclass
class SecretScope:
    backend_type: Optional['ScopeBackendType'] = None
    keyvault_metadata: Optional['AzureKeyVaultSecretScopeMetadata'] = None
    name: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.backend_type is not None: body['backend_type'] = self.backend_type.value
        if self.keyvault_metadata: body['keyvault_metadata'] = self.keyvault_metadata.as_dict()
        if self.name is not None: body['name'] = self.name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'SecretScope':
        return cls(backend_type=_enum(d, 'backend_type', ScopeBackendType),
                   keyvault_metadata=_from_dict(d, 'keyvault_metadata', AzureKeyVaultSecretScopeMetadata),
                   name=d.get('name', None))


@dataclass
class SparseCheckout:
    patterns: Optional['List[str]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.patterns: body['patterns'] = [v for v in self.patterns]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'SparseCheckout':
        return cls(patterns=d.get('patterns', None))


@dataclass
class SparseCheckoutUpdate:
    patterns: Optional['List[str]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.patterns: body['patterns'] = [v for v in self.patterns]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'SparseCheckoutUpdate':
        return cls(patterns=d.get('patterns', None))


@dataclass
class UpdateCredentials:
    credential_id: Optional[int] = None
    git_provider: Optional[str] = None
    git_username: Optional[str] = None
    personal_access_token: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.credential_id is not None: body['credential_id'] = self.credential_id
        if self.git_provider is not None: body['git_provider'] = self.git_provider
        if self.git_username is not None: body['git_username'] = self.git_username
        if self.personal_access_token is not None: body['personal_access_token'] = self.personal_access_token
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'UpdateCredentials':
        return cls(credential_id=d.get('credential_id', None),
                   git_provider=d.get('git_provider', None),
                   git_username=d.get('git_username', None),
                   personal_access_token=d.get('personal_access_token', None))


@dataclass
class UpdateRepo:
    branch: Optional[str] = None
    repo_id: Optional[int] = None
    sparse_checkout: Optional['SparseCheckoutUpdate'] = None
    tag: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.branch is not None: body['branch'] = self.branch
        if self.repo_id is not None: body['repo_id'] = self.repo_id
        if self.sparse_checkout: body['sparse_checkout'] = self.sparse_checkout.as_dict()
        if self.tag is not None: body['tag'] = self.tag
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'UpdateRepo':
        return cls(branch=d.get('branch', None),
                   repo_id=d.get('repo_id', None),
                   sparse_checkout=_from_dict(d, 'sparse_checkout', SparseCheckoutUpdate),
                   tag=d.get('tag', None))


class GitCredentialsAPI:
    """Registers personal access token for Databricks to do operations on behalf of the user.
    
    See [more info].
    
    [more info]: https://docs.databricks.com/repos/get-access-tokens-from-git-provider.html"""

    def __init__(self, api_client):
        self._api = api_client

    def create(self,
               git_provider: str,
               *,
               git_username: Optional[str] = None,
               personal_access_token: Optional[str] = None,
               **kwargs) -> CreateCredentialsResponse:
        """Create a credential entry.
        
        Creates a Git credential entry for the user. Only one Git credential per user is supported, so any
        attempts to create credentials if an entry already exists will fail. Use the PATCH endpoint to update
        existing credentials, or the DELETE endpoint to delete existing credentials.
        
        :param git_provider: str
          Git provider. This field is case-insensitive. The available Git providers are gitHub,
          bitbucketCloud, gitLab, azureDevOpsServices, gitHubEnterprise, bitbucketServer,
          gitLabEnterpriseEdition and awsCodeCommit.
        :param git_username: str (optional)
          Git username.
        :param personal_access_token: str (optional)
          The personal access token used to authenticate to the corresponding Git provider.
        
        :returns: :class:`CreateCredentialsResponse`
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = CreateCredentials(git_provider=git_provider,
                                        git_username=git_username,
                                        personal_access_token=personal_access_token)
        body = request.as_dict()

        json = self._api.do('POST', '/api/2.0/git-credentials', body=body)
        return CreateCredentialsResponse.from_dict(json)

    def delete(self, credential_id: int, **kwargs):
        """Delete a credential.
        
        Deletes the specified Git credential.
        
        :param credential_id: int
          The ID for the corresponding credential to access.
        
        
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = DeleteGitCredentialRequest(credential_id=credential_id)

        self._api.do('DELETE', f'/api/2.0/git-credentials/{request.credential_id}')

    def get(self, credential_id: int, **kwargs) -> CredentialInfo:
        """Get a credential entry.
        
        Gets the Git credential with the specified credential ID.
        
        :param credential_id: int
          The ID for the corresponding credential to access.
        
        :returns: :class:`CredentialInfo`
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GetGitCredentialRequest(credential_id=credential_id)

        json = self._api.do('GET', f'/api/2.0/git-credentials/{request.credential_id}')
        return CredentialInfo.from_dict(json)

    def list(self) -> Iterator[CredentialInfo]:
        """Get Git credentials.
        
        Lists the calling user's Git credentials. One credential per user is supported.
        
        :returns: Iterator over :class:`CredentialInfo`
        """

        json = self._api.do('GET', '/api/2.0/git-credentials')
        return [CredentialInfo.from_dict(v) for v in json.get('credentials', [])]

    def update(self,
               credential_id: int,
               *,
               git_provider: Optional[str] = None,
               git_username: Optional[str] = None,
               personal_access_token: Optional[str] = None,
               **kwargs):
        """Update a credential.
        
        Updates the specified Git credential.
        
        :param credential_id: int
          The ID for the corresponding credential to access.
        :param git_provider: str (optional)
          Git provider. This field is case-insensitive. The available Git providers are gitHub,
          bitbucketCloud, gitLab, azureDevOpsServices, gitHubEnterprise, bitbucketServer,
          gitLabEnterpriseEdition and awsCodeCommit.
        :param git_username: str (optional)
          Git username.
        :param personal_access_token: str (optional)
          The personal access token used to authenticate to the corresponding Git provider.
        
        
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = UpdateCredentials(credential_id=credential_id,
                                        git_provider=git_provider,
                                        git_username=git_username,
                                        personal_access_token=personal_access_token)
        body = request.as_dict()
        self._api.do('PATCH', f'/api/2.0/git-credentials/{request.credential_id}', body=body)


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
               path: Optional[str] = None,
               sparse_checkout: Optional[SparseCheckout] = None,
               **kwargs) -> RepoInfo:
        """Create a repo.
        
        Creates a repo in the workspace and links it to the remote Git repo specified. Note that repos created
        programmatically must be linked to a remote Git repo, unlike repos created in the browser.
        
        :param url: str
          URL of the Git repository to be linked.
        :param provider: str
          Git provider. This field is case-insensitive. The available Git providers are gitHub,
          bitbucketCloud, gitLab, azureDevOpsServices, gitHubEnterprise, bitbucketServer,
          gitLabEnterpriseEdition and awsCodeCommit.
        :param path: str (optional)
          Desired path for the repo in the workspace. Must be in the format /Repos/{folder}/{repo-name}.
        :param sparse_checkout: :class:`SparseCheckout` (optional)
          If specified, the repo will be created with sparse checkout enabled. You cannot enable/disable
          sparse checkout after the repo is created.
        
        :returns: :class:`RepoInfo`
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = CreateRepo(path=path, provider=provider, sparse_checkout=sparse_checkout, url=url)
        body = request.as_dict()

        json = self._api.do('POST', '/api/2.0/repos', body=body)
        return RepoInfo.from_dict(json)

    def delete(self, repo_id: int, **kwargs):
        """Delete a repo.
        
        Deletes the specified repo.
        
        :param repo_id: int
          The ID for the corresponding repo to access.
        
        
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = DeleteRepoRequest(repo_id=repo_id)

        self._api.do('DELETE', f'/api/2.0/repos/{request.repo_id}')

    def get(self, repo_id: int, **kwargs) -> RepoInfo:
        """Get a repo.
        
        Returns the repo with the given repo ID.
        
        :param repo_id: int
          The ID for the corresponding repo to access.
        
        :returns: :class:`RepoInfo`
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GetRepoRequest(repo_id=repo_id)

        json = self._api.do('GET', f'/api/2.0/repos/{request.repo_id}')
        return RepoInfo.from_dict(json)

    def list(self,
             *,
             next_page_token: Optional[str] = None,
             path_prefix: Optional[str] = None,
             **kwargs) -> Iterator[RepoInfo]:
        """Get repos.
        
        Returns repos that the calling user has Manage permissions on. Results are paginated with each page
        containing twenty repos.
        
        :param next_page_token: str (optional)
          Token used to get the next page of results. If not specified, returns the first page of results as
          well as a next page token if there are more results.
        :param path_prefix: str (optional)
          Filters repos that have paths starting with the given path prefix.
        
        :returns: Iterator over :class:`RepoInfo`
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = ListReposRequest(next_page_token=next_page_token, path_prefix=path_prefix)

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
               branch: Optional[str] = None,
               sparse_checkout: Optional[SparseCheckoutUpdate] = None,
               tag: Optional[str] = None,
               **kwargs):
        """Update a repo.
        
        Updates the repo to a different branch or tag, or updates the repo to the latest commit on the same
        branch.
        
        :param repo_id: int
          The ID for the corresponding repo to access.
        :param branch: str (optional)
          Branch that the local version of the repo is checked out to.
        :param sparse_checkout: :class:`SparseCheckoutUpdate` (optional)
          If specified, update the sparse checkout settings. The update will fail if sparse checkout is not
          enabled for the repo.
        :param tag: str (optional)
          Tag that the local version of the repo is checked out to. Updating the repo to a tag puts the repo
          in a detached HEAD state. Before committing new changes, you must update the repo to a branch
          instead of the detached HEAD.
        
        
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = UpdateRepo(branch=branch, repo_id=repo_id, sparse_checkout=sparse_checkout, tag=tag)
        body = request.as_dict()
        self._api.do('PATCH', f'/api/2.0/repos/{request.repo_id}', body=body)


class SecretsAPI:
    """The Secrets API allows you to manage secrets, secret scopes, and access permissions.
    
    Sometimes accessing data requires that you authenticate to external data sources through JDBC. Instead of
    directly entering your credentials into a notebook, use Databricks secrets to store your credentials and
    reference them in notebooks and jobs.
    
    Administrators, secret creators, and users granted permission can read Databricks secrets. While
    Databricks makes an effort to redact secret values that might be displayed in notebooks, it is not
    possible to prevent such users from reading secrets."""

    def __init__(self, api_client):
        self._api = api_client

    def create_scope(self,
                     scope: str,
                     *,
                     backend_azure_keyvault: Optional[AzureKeyVaultSecretScopeMetadata] = None,
                     initial_manage_principal: Optional[str] = None,
                     scope_backend_type: Optional[ScopeBackendType] = None,
                     **kwargs):
        """Create a new secret scope.
        
        The scope name must consist of alphanumeric characters, dashes, underscores, and periods, and may not
        exceed 128 characters. The maximum number of scopes in a workspace is 100.
        
        :param scope: str
          Scope name requested by the user. Scope names are unique.
        :param backend_azure_keyvault: :class:`AzureKeyVaultSecretScopeMetadata` (optional)
          The metadata for the secret scope if the type is `AZURE_KEYVAULT`
        :param initial_manage_principal: str (optional)
          The principal that is initially granted `MANAGE` permission to the created scope.
        :param scope_backend_type: :class:`ScopeBackendType` (optional)
          The backend type the scope will be created with. If not specified, will default to `DATABRICKS`
        
        
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = CreateScope(backend_azure_keyvault=backend_azure_keyvault,
                                  initial_manage_principal=initial_manage_principal,
                                  scope=scope,
                                  scope_backend_type=scope_backend_type)
        body = request.as_dict()
        self._api.do('POST', '/api/2.0/secrets/scopes/create', body=body)

    def delete_acl(self, scope: str, principal: str, **kwargs):
        """Delete an ACL.
        
        Deletes the given ACL on the given scope.
        
        Users must have the `MANAGE` permission to invoke this API. Throws `RESOURCE_DOES_NOT_EXIST` if no
        such secret scope, principal, or ACL exists. Throws `PERMISSION_DENIED` if the user does not have
        permission to make this API call.
        
        :param scope: str
          The name of the scope to remove permissions from.
        :param principal: str
          The principal to remove an existing ACL from.
        
        
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = DeleteAcl(principal=principal, scope=scope)
        body = request.as_dict()
        self._api.do('POST', '/api/2.0/secrets/acls/delete', body=body)

    def delete_scope(self, scope: str, **kwargs):
        """Delete a secret scope.
        
        Deletes a secret scope.
        
        Throws `RESOURCE_DOES_NOT_EXIST` if the scope does not exist. Throws `PERMISSION_DENIED` if the user
        does not have permission to make this API call.
        
        :param scope: str
          Name of the scope to delete.
        
        
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = DeleteScope(scope=scope)
        body = request.as_dict()
        self._api.do('POST', '/api/2.0/secrets/scopes/delete', body=body)

    def delete_secret(self, scope: str, key: str, **kwargs):
        """Delete a secret.
        
        Deletes the secret stored in this secret scope. You must have `WRITE` or `MANAGE` permission on the
        secret scope.
        
        Throws `RESOURCE_DOES_NOT_EXIST` if no such secret scope or secret exists. Throws `PERMISSION_DENIED`
        if the user does not have permission to make this API call.
        
        :param scope: str
          The name of the scope that contains the secret to delete.
        :param key: str
          Name of the secret to delete.
        
        
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = DeleteSecret(key=key, scope=scope)
        body = request.as_dict()
        self._api.do('POST', '/api/2.0/secrets/delete', body=body)

    def get_acl(self, scope: str, principal: str, **kwargs) -> AclItem:
        """Get secret ACL details.
        
        Gets the details about the given ACL, such as the group and permission. Users must have the `MANAGE`
        permission to invoke this API.
        
        Throws `RESOURCE_DOES_NOT_EXIST` if no such secret scope exists. Throws `PERMISSION_DENIED` if the
        user does not have permission to make this API call.
        
        :param scope: str
          The name of the scope to fetch ACL information from.
        :param principal: str
          The principal to fetch ACL information for.
        
        :returns: :class:`AclItem`
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GetAclRequest(principal=principal, scope=scope)

        query = {}
        if principal: query['principal'] = request.principal
        if scope: query['scope'] = request.scope

        json = self._api.do('GET', '/api/2.0/secrets/acls/get', query=query)
        return AclItem.from_dict(json)

    def list_acls(self, scope: str, **kwargs) -> Iterator[AclItem]:
        """Lists ACLs.
        
        List the ACLs for a given secret scope. Users must have the `MANAGE` permission to invoke this API.
        
        Throws `RESOURCE_DOES_NOT_EXIST` if no such secret scope exists. Throws `PERMISSION_DENIED` if the
        user does not have permission to make this API call.
        
        :param scope: str
          The name of the scope to fetch ACL information from.
        
        :returns: Iterator over :class:`AclItem`
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = ListAclsRequest(scope=scope)

        query = {}
        if scope: query['scope'] = request.scope

        json = self._api.do('GET', '/api/2.0/secrets/acls/list', query=query)
        return [AclItem.from_dict(v) for v in json.get('items', [])]

    def list_scopes(self) -> Iterator[SecretScope]:
        """List all scopes.
        
        Lists all secret scopes available in the workspace.
        
        Throws `PERMISSION_DENIED` if the user does not have permission to make this API call.
        
        :returns: Iterator over :class:`SecretScope`
        """

        json = self._api.do('GET', '/api/2.0/secrets/scopes/list')
        return [SecretScope.from_dict(v) for v in json.get('scopes', [])]

    def list_secrets(self, scope: str, **kwargs) -> Iterator[SecretMetadata]:
        """List secret keys.
        
        Lists the secret keys that are stored at this scope. This is a metadata-only operation; secret data
        cannot be retrieved using this API. Users need the READ permission to make this call.
        
        The lastUpdatedTimestamp returned is in milliseconds since epoch. Throws `RESOURCE_DOES_NOT_EXIST` if
        no such secret scope exists. Throws `PERMISSION_DENIED` if the user does not have permission to make
        this API call.
        
        :param scope: str
          The name of the scope to list secrets within.
        
        :returns: Iterator over :class:`SecretMetadata`
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = ListSecretsRequest(scope=scope)

        query = {}
        if scope: query['scope'] = request.scope

        json = self._api.do('GET', '/api/2.0/secrets/list', query=query)
        return [SecretMetadata.from_dict(v) for v in json.get('secrets', [])]

    def put_acl(self, scope: str, principal: str, permission: AclPermission, **kwargs):
        """Create/update an ACL.
        
        Creates or overwrites the Access Control List (ACL) associated with the given principal (user or
        group) on the specified scope point.
        
        In general, a user or group will use the most powerful permission available to them, and permissions
        are ordered as follows:
        
        * `MANAGE` - Allowed to change ACLs, and read and write to this secret scope. * `WRITE` - Allowed to
        read and write to this secret scope. * `READ` - Allowed to read this secret scope and list what
        secrets are available.
        
        Note that in general, secret values can only be read from within a command on a cluster (for example,
        through a notebook). There is no API to read the actual secret value material outside of a cluster.
        However, the user's permission will be applied based on who is executing the command, and they must
        have at least READ permission.
        
        Users must have the `MANAGE` permission to invoke this API.
        
        The principal is a user or group name corresponding to an existing Databricks principal to be granted
        or revoked access.
        
        Throws `RESOURCE_DOES_NOT_EXIST` if no such secret scope exists. Throws `RESOURCE_ALREADY_EXISTS` if a
        permission for the principal already exists. Throws `INVALID_PARAMETER_VALUE` if the permission or
        principal is invalid. Throws `PERMISSION_DENIED` if the user does not have permission to make this API
        call.
        
        :param scope: str
          The name of the scope to apply permissions to.
        :param principal: str
          The principal in which the permission is applied.
        :param permission: :class:`AclPermission`
          The permission level applied to the principal.
        
        
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = PutAcl(permission=permission, principal=principal, scope=scope)
        body = request.as_dict()
        self._api.do('POST', '/api/2.0/secrets/acls/put', body=body)

    def put_secret(self,
                   scope: str,
                   key: str,
                   *,
                   bytes_value: Optional[str] = None,
                   string_value: Optional[str] = None,
                   **kwargs):
        """Add a secret.
        
        Inserts a secret under the provided scope with the given name. If a secret already exists with the
        same name, this command overwrites the existing secret's value. The server encrypts the secret using
        the secret scope's encryption settings before storing it.
        
        You must have `WRITE` or `MANAGE` permission on the secret scope. The secret key must consist of
        alphanumeric characters, dashes, underscores, and periods, and cannot exceed 128 characters. The
        maximum allowed secret value size is 128 KB. The maximum number of secrets in a given scope is 1000.
        
        The input fields "string_value" or "bytes_value" specify the type of the secret, which will determine
        the value returned when the secret value is requested. Exactly one must be specified.
        
        Throws `RESOURCE_DOES_NOT_EXIST` if no such secret scope exists. Throws `RESOURCE_LIMIT_EXCEEDED` if
        maximum number of secrets in scope is exceeded. Throws `INVALID_PARAMETER_VALUE` if the key name or
        value length is invalid. Throws `PERMISSION_DENIED` if the user does not have permission to make this
        API call.
        
        :param scope: str
          The name of the scope to which the secret will be associated with.
        :param key: str
          A unique name to identify the secret.
        :param bytes_value: str (optional)
          If specified, value will be stored as bytes.
        :param string_value: str (optional)
          If specified, note that the value will be stored in UTF-8 (MB4) form.
        
        
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = PutSecret(bytes_value=bytes_value, key=key, scope=scope, string_value=string_value)
        body = request.as_dict()
        self._api.do('POST', '/api/2.0/secrets/put', body=body)


class WorkspaceAPI:
    """The Workspace API allows you to list, import, export, and delete notebooks and folders.
    
    A notebook is a web-based interface to a document that contains runnable code, visualizations, and
    explanatory text."""

    def __init__(self, api_client):
        self._api = api_client

    def delete(self, path: str, *, recursive: Optional[bool] = None, **kwargs):
        """Delete a workspace object.
        
        Deletes an object or a directory (and optionally recursively deletes all objects in the directory). *
        If `path` does not exist, this call returns an error `RESOURCE_DOES_NOT_EXIST`. * If `path` is a
        non-empty directory and `recursive` is set to `false`, this call returns an error
        `DIRECTORY_NOT_EMPTY`.
        
        Object deletion cannot be undone and deleting a directory recursively is not atomic.
        
        :param path: str
          The absolute path of the notebook or directory.
        :param recursive: bool (optional)
          The flag that specifies whether to delete the object recursively. It is `false` by default. Please
          note this deleting directory is not atomic. If it fails in the middle, some of objects under this
          directory may be deleted and cannot be undone.
        
        
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = Delete(path=path, recursive=recursive)
        body = request.as_dict()
        self._api.do('POST', '/api/2.0/workspace/delete', body=body)

    def export(self, path: str, *, format: Optional[ExportFormat] = None, **kwargs) -> ExportResponse:
        """Export a workspace object.
        
        Exports an object or the contents of an entire directory.
        
        If `path` does not exist, this call returns an error `RESOURCE_DOES_NOT_EXIST`.
        
        If the exported data would exceed size limit, this call returns `MAX_NOTEBOOK_SIZE_EXCEEDED`.
        Currently, this API does not support exporting a library.
        
        :param path: str
          The absolute path of the object or directory. Exporting a directory is only supported for the `DBC`
          and `SOURCE` format.
        :param format: :class:`ExportFormat` (optional)
          This specifies the format of the exported file. By default, this is `SOURCE`.
          
          The value is case sensitive.
          
          - `SOURCE`: The notebook is exported as source code. - `HTML`: The notebook is exported as an HTML
          file. - `JUPYTER`: The notebook is exported as a Jupyter/IPython Notebook file. - `DBC`: The
          notebook is exported in Databricks archive format. - `R_MARKDOWN`: The notebook is exported to R
          Markdown format.
        
        :returns: :class:`ExportResponse`
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = ExportRequest(format=format, path=path)

        query = {}
        if format: query['format'] = request.format.value
        if path: query['path'] = request.path

        json = self._api.do('GET', '/api/2.0/workspace/export', query=query)
        return ExportResponse.from_dict(json)

    def get_status(self, path: str, **kwargs) -> ObjectInfo:
        """Get status.
        
        Gets the status of an object or a directory. If `path` does not exist, this call returns an error
        `RESOURCE_DOES_NOT_EXIST`.
        
        :param path: str
          The absolute path of the notebook or directory.
        
        :returns: :class:`ObjectInfo`
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GetStatusRequest(path=path)

        query = {}
        if path: query['path'] = request.path

        json = self._api.do('GET', '/api/2.0/workspace/get-status', query=query)
        return ObjectInfo.from_dict(json)

    def import_(self,
                path: str,
                *,
                content: Optional[str] = None,
                format: Optional[ImportFormat] = None,
                language: Optional[Language] = None,
                overwrite: Optional[bool] = None,
                **kwargs):
        """Import a workspace object.
        
        Imports a workspace object (for example, a notebook or file) or the contents of an entire directory.
        If `path` already exists and `overwrite` is set to `false`, this call returns an error
        `RESOURCE_ALREADY_EXISTS`. One can only use `DBC` format to import a directory.
        
        :param path: str
          The absolute path of the object or directory. Importing a directory is only supported for the `DBC`
          format.
        :param content: str (optional)
          The base64-encoded content. This has a limit of 10 MB.
          
          If the limit (10MB) is exceeded, exception with error code **MAX_NOTEBOOK_SIZE_EXCEEDED** is thrown.
          This parameter might be absent, and instead a posted file is used.
        :param format: :class:`ImportFormat` (optional)
          This specifies the format of the file to be imported.
          
          The value is case sensitive.
          
          - `AUTO`: The item is imported depending on an analysis of the item's extension and the header
          content provided in the request. If the item is imported as a notebook, then the item's extension is
          automatically removed. - `SOURCE`: The notebook is imported as source code. - `HTML`: The notebook
          is imported as an HTML file. - `JUPYTER`: The notebook is imported as a Jupyter/IPython Notebook
          file. - `DBC`: The notebook is imported in Databricks archive format. Required for directories. -
          `R_MARKDOWN`: The notebook is imported from R Markdown format.
        :param language: :class:`Language` (optional)
          The language of the object. This value is set only if the object type is `NOTEBOOK`.
        :param overwrite: bool (optional)
          The flag that specifies whether to overwrite existing object. It is `false` by default. For `DBC`
          format, `overwrite` is not supported since it may contain a directory.
        
        
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = Import(content=content,
                             format=format,
                             language=language,
                             overwrite=overwrite,
                             path=path)
        body = request.as_dict()
        self._api.do('POST', '/api/2.0/workspace/import', body=body)

    def list(self,
             path: str,
             *,
             notebooks_modified_after: Optional[int] = None,
             **kwargs) -> Iterator[ObjectInfo]:
        """List contents.
        
        Lists the contents of a directory, or the object if it is not a directory. If the input path does not
        exist, this call returns an error `RESOURCE_DOES_NOT_EXIST`.
        
        :param path: str
          The absolute path of the notebook or directory.
        :param notebooks_modified_after: int (optional)
          UTC timestamp in milliseconds
        
        :returns: Iterator over :class:`ObjectInfo`
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = ListWorkspaceRequest(notebooks_modified_after=notebooks_modified_after, path=path)

        query = {}
        if notebooks_modified_after: query['notebooks_modified_after'] = request.notebooks_modified_after
        if path: query['path'] = request.path

        json = self._api.do('GET', '/api/2.0/workspace/list', query=query)
        return [ObjectInfo.from_dict(v) for v in json.get('objects', [])]

    def mkdirs(self, path: str, **kwargs):
        """Create a directory.
        
        Creates the specified directory (and necessary parent directories if they do not exist). If there is
        an object (not a directory) at any prefix of the input path, this call returns an error
        `RESOURCE_ALREADY_EXISTS`.
        
        Note that if this operation fails it may have succeeded in creating some of the necessary parent
        directories.
        
        :param path: str
          The absolute path of the directory. If the parent directories do not exist, it will also create
          them. If the directory already exists, this command will do nothing and succeed.
        
        
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = Mkdirs(path=path)
        body = request.as_dict()
        self._api.do('POST', '/api/2.0/workspace/mkdirs', body=body)
