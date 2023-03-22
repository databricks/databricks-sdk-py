# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

import logging
from dataclasses import dataclass
from enum import Enum
from typing import Dict, Iterator, List

from ._internal import _enum, _from_dict, _repeated

_LOG = logging.getLogger('databricks.sdk')

# all definitions in this file are in alphabetical order


@dataclass
class AclItem:
    principal: str
    permission: 'AclPermission'

    def as_dict(self) -> dict:
        body = {}
        if self.permission: body['permission'] = self.permission.value
        if self.principal: body['principal'] = self.principal
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
        if self.dns_name: body['dns_name'] = self.dns_name
        if self.resource_id: body['resource_id'] = self.resource_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'AzureKeyVaultSecretScopeMetadata':
        return cls(dns_name=d.get('dns_name', None), resource_id=d.get('resource_id', None))


@dataclass
class CreateScope:
    scope: str
    initial_manage_principal: str = None
    keyvault_metadata: 'AzureKeyVaultSecretScopeMetadata' = None
    scope_backend_type: 'ScopeBackendType' = None

    def as_dict(self) -> dict:
        body = {}
        if self.initial_manage_principal: body['initial_manage_principal'] = self.initial_manage_principal
        if self.keyvault_metadata: body['keyvault_metadata'] = self.keyvault_metadata.as_dict()
        if self.scope: body['scope'] = self.scope
        if self.scope_backend_type: body['scope_backend_type'] = self.scope_backend_type.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateScope':
        return cls(initial_manage_principal=d.get('initial_manage_principal', None),
                   keyvault_metadata=_from_dict(d, 'keyvault_metadata', AzureKeyVaultSecretScopeMetadata),
                   scope=d.get('scope', None),
                   scope_backend_type=_enum(d, 'scope_backend_type', ScopeBackendType))


@dataclass
class DeleteAcl:
    scope: str
    principal: str

    def as_dict(self) -> dict:
        body = {}
        if self.principal: body['principal'] = self.principal
        if self.scope: body['scope'] = self.scope
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'DeleteAcl':
        return cls(principal=d.get('principal', None), scope=d.get('scope', None))


@dataclass
class DeleteScope:
    scope: str

    def as_dict(self) -> dict:
        body = {}
        if self.scope: body['scope'] = self.scope
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
        if self.key: body['key'] = self.key
        if self.scope: body['scope'] = self.scope
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'DeleteSecret':
        return cls(key=d.get('key', None), scope=d.get('scope', None))


@dataclass
class GetAcl:
    """Get secret ACL details"""

    scope: str
    principal: str


@dataclass
class ListAcls:
    """Lists ACLs"""

    scope: str


@dataclass
class ListAclsResponse:
    items: 'List[AclItem]' = None

    def as_dict(self) -> dict:
        body = {}
        if self.items: body['items'] = [v.as_dict() for v in self.items]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListAclsResponse':
        return cls(items=_repeated(d, 'items', AclItem))


@dataclass
class ListScopesResponse:
    scopes: 'List[SecretScope]' = None

    def as_dict(self) -> dict:
        body = {}
        if self.scopes: body['scopes'] = [v.as_dict() for v in self.scopes]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListScopesResponse':
        return cls(scopes=_repeated(d, 'scopes', SecretScope))


@dataclass
class ListSecrets:
    """List secret keys"""

    scope: str


@dataclass
class ListSecretsResponse:
    secrets: 'List[SecretMetadata]' = None

    def as_dict(self) -> dict:
        body = {}
        if self.secrets: body['secrets'] = [v.as_dict() for v in self.secrets]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListSecretsResponse':
        return cls(secrets=_repeated(d, 'secrets', SecretMetadata))


@dataclass
class PutAcl:
    scope: str
    principal: str
    permission: 'AclPermission'

    def as_dict(self) -> dict:
        body = {}
        if self.permission: body['permission'] = self.permission.value
        if self.principal: body['principal'] = self.principal
        if self.scope: body['scope'] = self.scope
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
    bytes_value: str = None
    string_value: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.bytes_value: body['bytes_value'] = self.bytes_value
        if self.key: body['key'] = self.key
        if self.scope: body['scope'] = self.scope
        if self.string_value: body['string_value'] = self.string_value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'PutSecret':
        return cls(bytes_value=d.get('bytes_value', None),
                   key=d.get('key', None),
                   scope=d.get('scope', None),
                   string_value=d.get('string_value', None))


class ScopeBackendType(Enum):

    AZURE_KEYVAULT = 'AZURE_KEYVAULT'
    DATABRICKS = 'DATABRICKS'


@dataclass
class SecretMetadata:
    key: str = None
    last_updated_timestamp: int = None

    def as_dict(self) -> dict:
        body = {}
        if self.key: body['key'] = self.key
        if self.last_updated_timestamp: body['last_updated_timestamp'] = self.last_updated_timestamp
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'SecretMetadata':
        return cls(key=d.get('key', None), last_updated_timestamp=d.get('last_updated_timestamp', None))


@dataclass
class SecretScope:
    backend_type: 'ScopeBackendType' = None
    keyvault_metadata: 'AzureKeyVaultSecretScopeMetadata' = None
    name: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.backend_type: body['backend_type'] = self.backend_type.value
        if self.keyvault_metadata: body['keyvault_metadata'] = self.keyvault_metadata.as_dict()
        if self.name: body['name'] = self.name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'SecretScope':
        return cls(backend_type=_enum(d, 'backend_type', ScopeBackendType),
                   keyvault_metadata=_from_dict(d, 'keyvault_metadata', AzureKeyVaultSecretScopeMetadata),
                   name=d.get('name', None))


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
                     initial_manage_principal: str = None,
                     keyvault_metadata: AzureKeyVaultSecretScopeMetadata = None,
                     scope_backend_type: ScopeBackendType = None,
                     **kwargs):
        """Create a new secret scope.
        
        The scope name must consist of alphanumeric characters, dashes, underscores, and periods, and may not
        exceed 128 characters. The maximum number of scopes in a workspace is 100."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = CreateScope(initial_manage_principal=initial_manage_principal,
                                  keyvault_metadata=keyvault_metadata,
                                  scope=scope,
                                  scope_backend_type=scope_backend_type)
        body = request.as_dict()
        self._api.do('POST', '/api/2.0/secrets/scopes/create', body=body)

    def delete_acl(self, scope: str, principal: str, **kwargs):
        """Delete an ACL.
        
        Deletes the given ACL on the given scope.
        
        Users must have the `MANAGE` permission to invoke this API. Throws `RESOURCE_DOES_NOT_EXIST` if no
        such secret scope, principal, or ACL exists. Throws `PERMISSION_DENIED` if the user does not have
        permission to make this API call."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = DeleteAcl(principal=principal, scope=scope)
        body = request.as_dict()
        self._api.do('POST', '/api/2.0/secrets/acls/delete', body=body)

    def delete_scope(self, scope: str, **kwargs):
        """Delete a secret scope.
        
        Deletes a secret scope.
        
        Throws `RESOURCE_DOES_NOT_EXIST` if the scope does not exist. Throws `PERMISSION_DENIED` if the user
        does not have permission to make this API call."""
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
        if the user does not have permission to make this API call."""
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
        user does not have permission to make this API call."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GetAcl(principal=principal, scope=scope)

        query = {}
        if principal: query['principal'] = request.principal
        if scope: query['scope'] = request.scope

        json = self._api.do('GET', '/api/2.0/secrets/acls/get', query=query)
        return AclItem.from_dict(json)

    def list_acls(self, scope: str, **kwargs) -> Iterator[AclItem]:
        """Lists ACLs.
        
        List the ACLs for a given secret scope. Users must have the `MANAGE` permission to invoke this API.
        
        Throws `RESOURCE_DOES_NOT_EXIST` if no such secret scope exists. Throws `PERMISSION_DENIED` if the
        user does not have permission to make this API call."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = ListAcls(scope=scope)

        query = {}
        if scope: query['scope'] = request.scope

        json = self._api.do('GET', '/api/2.0/secrets/acls/list', query=query)
        return [AclItem.from_dict(v) for v in json.get('items', [])]

    def list_scopes(self) -> Iterator[SecretScope]:
        """List all scopes.
        
        Lists all secret scopes available in the workspace.
        
        Throws `PERMISSION_DENIED` if the user does not have permission to make this API call."""

        json = self._api.do('GET', '/api/2.0/secrets/scopes/list')
        return [SecretScope.from_dict(v) for v in json.get('scopes', [])]

    def list_secrets(self, scope: str, **kwargs) -> Iterator[SecretMetadata]:
        """List secret keys.
        
        Lists the secret keys that are stored at this scope. This is a metadata-only operation; secret data
        cannot be retrieved using this API. Users need the READ permission to make this call.
        
        The lastUpdatedTimestamp returned is in milliseconds since epoch. Throws `RESOURCE_DOES_NOT_EXIST` if
        no such secret scope exists. Throws `PERMISSION_DENIED` if the user does not have permission to make
        this API call."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = ListSecrets(scope=scope)

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
        permission for the principal already exists. Throws `INVALID_PARAMETER_VALUE` if the permission is
        invalid. Throws `PERMISSION_DENIED` if the user does not have permission to make this API call."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = PutAcl(permission=permission, principal=principal, scope=scope)
        body = request.as_dict()
        self._api.do('POST', '/api/2.0/secrets/acls/put', body=body)

    def put_secret(self,
                   scope: str,
                   key: str,
                   *,
                   bytes_value: str = None,
                   string_value: str = None,
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
        API call."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = PutSecret(bytes_value=bytes_value, key=key, scope=scope, string_value=string_value)
        body = request.as_dict()
        self._api.do('POST', '/api/2.0/secrets/put', body=body)
