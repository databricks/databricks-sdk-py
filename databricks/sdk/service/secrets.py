# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

from dataclasses import dataclass
from enum import Enum
from typing import Optional, Dict, List, Any


# all definitions in this file are in alphabetical order


@dataclass
class AclItem:

    # The permission level applied to the principal.
    permission: "AclPermission"
    # The principal in which the permission is applied.
    principal: str

    def as_dict(self) -> dict:
        body = {}
        if self.permission:
            body["permission"] = self.permission.value
        if self.principal:
            body["principal"] = self.principal

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "AclItem":
        return cls(
            permission=AclPermission(d["permission"]) if "permission" in d else None,
            principal=d.get("principal", None),
        )


class AclPermission(Enum):

    MANAGE = "MANAGE"
    READ = "READ"
    WRITE = "WRITE"


@dataclass
class AzureKeyVaultSecretScopeMetadata:

    # The DNS of the KeyVault
    dns_name: str
    # The resource id of the azure KeyVault that user wants to associate the
    # scope with.
    resource_id: str

    def as_dict(self) -> dict:
        body = {}
        if self.dns_name:
            body["dns_name"] = self.dns_name
        if self.resource_id:
            body["resource_id"] = self.resource_id

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "AzureKeyVaultSecretScopeMetadata":
        return cls(
            dns_name=d.get("dns_name", None),
            resource_id=d.get("resource_id", None),
        )


@dataclass
class CreateScope:

    # The principal that is initially granted `MANAGE` permission to the created
    # scope.
    initial_manage_principal: str
    # The metadata for the secret scope if the type is `AZURE_KEYVAULT`
    keyvault_metadata: "AzureKeyVaultSecretScopeMetadata"
    # Scope name requested by the user. Scope names are unique.
    scope: str
    # The backend type the scope will be created with. If not specified, will
    # default to `DATABRICKS`
    scope_backend_type: "ScopeBackendType"

    def as_dict(self) -> dict:
        body = {}
        if self.initial_manage_principal:
            body["initial_manage_principal"] = self.initial_manage_principal
        if self.keyvault_metadata:
            body["keyvault_metadata"] = self.keyvault_metadata.as_dict()
        if self.scope:
            body["scope"] = self.scope
        if self.scope_backend_type:
            body["scope_backend_type"] = self.scope_backend_type.value

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "CreateScope":
        return cls(
            initial_manage_principal=d.get("initial_manage_principal", None),
            keyvault_metadata=AzureKeyVaultSecretScopeMetadata.from_dict(
                d["keyvault_metadata"]
            )
            if "keyvault_metadata" in d
            else None,
            scope=d.get("scope", None),
            scope_backend_type=ScopeBackendType(d["scope_backend_type"])
            if "scope_backend_type" in d
            else None,
        )


@dataclass
class DeleteAcl:

    # The principal to remove an existing ACL from.
    principal: str
    # The name of the scope to remove permissions from.
    scope: str

    def as_dict(self) -> dict:
        body = {}
        if self.principal:
            body["principal"] = self.principal
        if self.scope:
            body["scope"] = self.scope

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "DeleteAcl":
        return cls(
            principal=d.get("principal", None),
            scope=d.get("scope", None),
        )


@dataclass
class DeleteScope:

    # Name of the scope to delete.
    scope: str

    def as_dict(self) -> dict:
        body = {}
        if self.scope:
            body["scope"] = self.scope

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "DeleteScope":
        return cls(
            scope=d.get("scope", None),
        )


@dataclass
class DeleteSecret:

    # Name of the secret to delete.
    key: str
    # The name of the scope that contains the secret to delete.
    scope: str

    def as_dict(self) -> dict:
        body = {}
        if self.key:
            body["key"] = self.key
        if self.scope:
            body["scope"] = self.scope

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "DeleteSecret":
        return cls(
            key=d.get("key", None),
            scope=d.get("scope", None),
        )


@dataclass
class GetAcl:
    """Get secret ACL details"""

    # The principal to fetch ACL information for.
    principal: str  # query
    # The name of the scope to fetch ACL information from.
    scope: str  # query

    def as_dict(self) -> dict:
        body = {}
        if self.principal:
            body["principal"] = self.principal
        if self.scope:
            body["scope"] = self.scope

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "GetAcl":
        return cls(
            principal=d.get("principal", None),
            scope=d.get("scope", None),
        )


@dataclass
class ListAcls:
    """Lists ACLs"""

    # The name of the scope to fetch ACL information from.
    scope: str  # query

    def as_dict(self) -> dict:
        body = {}
        if self.scope:
            body["scope"] = self.scope

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ListAcls":
        return cls(
            scope=d.get("scope", None),
        )


@dataclass
class ListAclsResponse:

    # The associated ACLs rule applied to principals in the given scope.
    items: "List[AclItem]"

    def as_dict(self) -> dict:
        body = {}
        if self.items:
            body["items"] = [v.as_dict() for v in self.items]

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ListAclsResponse":
        return cls(
            items=[AclItem.from_dict(v) for v in d["items"]] if "items" in d else None,
        )


@dataclass
class ListScopesResponse:

    # The available secret scopes.
    scopes: "List[SecretScope]"

    def as_dict(self) -> dict:
        body = {}
        if self.scopes:
            body["scopes"] = [v.as_dict() for v in self.scopes]

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ListScopesResponse":
        return cls(
            scopes=[SecretScope.from_dict(v) for v in d["scopes"]]
            if "scopes" in d
            else None,
        )


@dataclass
class ListSecrets:
    """List secret keys"""

    # The name of the scope to list secrets within.
    scope: str  # query

    def as_dict(self) -> dict:
        body = {}
        if self.scope:
            body["scope"] = self.scope

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ListSecrets":
        return cls(
            scope=d.get("scope", None),
        )


@dataclass
class ListSecretsResponse:

    # Metadata information of all secrets contained within the given scope.
    secrets: "List[SecretMetadata]"

    def as_dict(self) -> dict:
        body = {}
        if self.secrets:
            body["secrets"] = [v.as_dict() for v in self.secrets]

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ListSecretsResponse":
        return cls(
            secrets=[SecretMetadata.from_dict(v) for v in d["secrets"]]
            if "secrets" in d
            else None,
        )


@dataclass
class PutAcl:

    # The permission level applied to the principal.
    permission: "AclPermission"
    # The principal in which the permission is applied.
    principal: str
    # The name of the scope to apply permissions to.
    scope: str

    def as_dict(self) -> dict:
        body = {}
        if self.permission:
            body["permission"] = self.permission.value
        if self.principal:
            body["principal"] = self.principal
        if self.scope:
            body["scope"] = self.scope

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "PutAcl":
        return cls(
            permission=AclPermission(d["permission"]) if "permission" in d else None,
            principal=d.get("principal", None),
            scope=d.get("scope", None),
        )


@dataclass
class PutSecret:

    # If specified, value will be stored as bytes.
    bytes_value: str
    # A unique name to identify the secret.
    key: str
    # The name of the scope to which the secret will be associated with.
    scope: str
    # If specified, note that the value will be stored in UTF-8 (MB4) form.
    string_value: str

    def as_dict(self) -> dict:
        body = {}
        if self.bytes_value:
            body["bytes_value"] = self.bytes_value
        if self.key:
            body["key"] = self.key
        if self.scope:
            body["scope"] = self.scope
        if self.string_value:
            body["string_value"] = self.string_value

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "PutSecret":
        return cls(
            bytes_value=d.get("bytes_value", None),
            key=d.get("key", None),
            scope=d.get("scope", None),
            string_value=d.get("string_value", None),
        )


class ScopeBackendType(Enum):

    AZURE_KEYVAULT = "AZURE_KEYVAULT"
    DATABRICKS = "DATABRICKS"


@dataclass
class SecretMetadata:

    # A unique name to identify the secret.
    key: str
    # The last updated timestamp (in milliseconds) for the secret.
    last_updated_timestamp: int

    def as_dict(self) -> dict:
        body = {}
        if self.key:
            body["key"] = self.key
        if self.last_updated_timestamp:
            body["last_updated_timestamp"] = self.last_updated_timestamp

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "SecretMetadata":
        return cls(
            key=d.get("key", None),
            last_updated_timestamp=d.get("last_updated_timestamp", None),
        )


@dataclass
class SecretScope:

    # The type of secret scope backend.
    backend_type: "ScopeBackendType"
    # The metadata for the secret scope if the type is `AZURE_KEYVAULT`
    keyvault_metadata: "AzureKeyVaultSecretScopeMetadata"
    # A unique name to identify the secret scope.
    name: str

    def as_dict(self) -> dict:
        body = {}
        if self.backend_type:
            body["backend_type"] = self.backend_type.value
        if self.keyvault_metadata:
            body["keyvault_metadata"] = self.keyvault_metadata.as_dict()
        if self.name:
            body["name"] = self.name

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "SecretScope":
        return cls(
            backend_type=ScopeBackendType(d["backend_type"])
            if "backend_type" in d
            else None,
            keyvault_metadata=AzureKeyVaultSecretScopeMetadata.from_dict(
                d["keyvault_metadata"]
            )
            if "keyvault_metadata" in d
            else None,
            name=d.get("name", None),
        )


class SecretsAPI:
    def __init__(self, api_client):
        self._api = api_client

    def create_scope(
        self,
        scope: str,
        *,
        initial_manage_principal: str = None,
        keyvault_metadata: AzureKeyVaultSecretScopeMetadata = None,
        scope_backend_type: ScopeBackendType = None,
        **kwargs
    ):
        """Create a new secret scope.

        The scope name must consist of alphanumeric characters, dashes,
        underscores, and periods, and may not exceed 128 characters. The maximum
        number of scopes in a workspace is 100."""

        request = kwargs.get("request", None)
        if not request:
            request = CreateScope(
                initial_manage_principal=initial_manage_principal,
                keyvault_metadata=keyvault_metadata,
                scope=scope,
                scope_backend_type=scope_backend_type,
            )
        body = request.as_dict()
        query = {}

        self._api.do("POST", "/api/2.0/secrets/scopes/create", query=query, body=body)

    def delete_acl(self, scope: str, principal: str, **kwargs):
        """Delete an ACL.

        Deletes the given ACL on the given scope.

        Users must have the `MANAGE` permission to invoke this API. Throws
        `RESOURCE_DOES_NOT_EXIST` if no such secret scope, principal, or ACL
        exists. Throws `PERMISSION_DENIED` if the user does not have permission
        to make this API call."""

        request = kwargs.get("request", None)
        if not request:
            request = DeleteAcl(principal=principal, scope=scope)
        body = request.as_dict()
        query = {}

        self._api.do("POST", "/api/2.0/secrets/acls/delete", query=query, body=body)

    def delete_scope(self, scope: str, **kwargs):
        """Delete a secret scope.

        Deletes a secret scope.

        Throws `RESOURCE_DOES_NOT_EXIST` if the scope does not exist. Throws
        `PERMISSION_DENIED` if the user does not have permission to make this
        API call."""

        request = kwargs.get("request", None)
        if not request:
            request = DeleteScope(scope=scope)
        body = request.as_dict()
        query = {}

        self._api.do("POST", "/api/2.0/secrets/scopes/delete", query=query, body=body)

    def delete_secret(self, scope: str, key: str, **kwargs):
        """Delete a secret.

        Deletes the secret stored in this secret scope. You must have `WRITE` or
        `MANAGE` permission on the secret scope.

        Throws `RESOURCE_DOES_NOT_EXIST` if no such secret scope or secret
        exists. Throws `PERMISSION_DENIED` if the user does not have permission
        to make this API call."""

        request = kwargs.get("request", None)
        if not request:
            request = DeleteSecret(key=key, scope=scope)
        body = request.as_dict()
        query = {}

        self._api.do("POST", "/api/2.0/secrets/delete", query=query, body=body)

    def get_acl(self, scope: str, principal: str, **kwargs) -> AclItem:
        """Get secret ACL details.

        Gets the details about the given ACL, such as the group and permission.
        Users must have the `MANAGE` permission to invoke this API.

        Throws `RESOURCE_DOES_NOT_EXIST` if no such secret scope exists. Throws
        `PERMISSION_DENIED` if the user does not have permission to make this
        API call."""

        request = kwargs.get("request", None)
        if not request:
            request = GetAcl(principal=principal, scope=scope)
        body = request.as_dict()
        query = {}
        if principal:
            query["principal"] = principal
        if scope:
            query["scope"] = scope

        json = self._api.do("GET", "/api/2.0/secrets/acls/get", query=query, body=body)
        return AclItem.from_dict(json)

    def list_acls(self, scope: str, **kwargs) -> ListAclsResponse:
        """Lists ACLs.

        List the ACLs for a given secret scope. Users must have the `MANAGE`
        permission to invoke this API.

        Throws `RESOURCE_DOES_NOT_EXIST` if no such secret scope exists. Throws
        `PERMISSION_DENIED` if the user does not have permission to make this
        API call."""

        request = kwargs.get("request", None)
        if not request:
            request = ListAcls(scope=scope)
        body = request.as_dict()
        query = {}
        if scope:
            query["scope"] = scope

        json = self._api.do("GET", "/api/2.0/secrets/acls/list", query=query, body=body)
        return ListAclsResponse.from_dict(json)

    def list_scopes(self) -> ListScopesResponse:
        """List all scopes.

        Lists all secret scopes available in the workspace.

        Throws `PERMISSION_DENIED` if the user does not have permission to make
        this API call."""

        json = self._api.do("GET", "/api/2.0/secrets/scopes/list")
        return ListScopesResponse.from_dict(json)

    def list_secrets(self, scope: str, **kwargs) -> ListSecretsResponse:
        """List secret keys.

        Lists the secret keys that are stored at this scope. This is a
        metadata-only operation; secret data cannot be retrieved using this API.
        Users need the READ permission to make this call.

        The lastUpdatedTimestamp returned is in milliseconds since epoch. Throws
        `RESOURCE_DOES_NOT_EXIST` if no such secret scope exists. Throws
        `PERMISSION_DENIED` if the user does not have permission to make this
        API call."""

        request = kwargs.get("request", None)
        if not request:
            request = ListSecrets(scope=scope)
        body = request.as_dict()
        query = {}
        if scope:
            query["scope"] = scope

        json = self._api.do("GET", "/api/2.0/secrets/list", query=query, body=body)
        return ListSecretsResponse.from_dict(json)

    def put_acl(self, scope: str, principal: str, permission: AclPermission, **kwargs):
        """Create/update an ACL.

        Creates or overwrites the Access Control List (ACL) associated with the
        given principal (user or group) on the specified scope point.

        In general, a user or group will use the most powerful permission
        available to them, and permissions are ordered as follows:

        * `MANAGE` - Allowed to change ACLs, and read and write to this secret
        scope. * `WRITE` - Allowed to read and write to this secret scope. *
        `READ` - Allowed to read this secret scope and list what secrets are
        available.

        Note that in general, secret values can only be read from within a
        command\non a cluster (for example, through a notebook). There is no API
        to read the actual secret value material outside of a cluster. However,
        the user's permission will be applied based on who is executing the
        command, and they must have at least READ permission.

        Users must have the `MANAGE` permission to invoke this API.

        The principal is a user or group name corresponding to an existing
        Databricks principal to be granted or revoked access.

        Throws `RESOURCE_DOES_NOT_EXIST` if no such secret scope exists. Throws
        `RESOURCE_ALREADY_EXISTS` if a permission for the principal already
        exists. Throws `INVALID_PARAMETER_VALUE` if the permission is invalid.
        Throws `PERMISSION_DENIED` if the user does not have permission to make
        this API call."""

        request = kwargs.get("request", None)
        if not request:
            request = PutAcl(permission=permission, principal=principal, scope=scope)
        body = request.as_dict()
        query = {}

        self._api.do("POST", "/api/2.0/secrets/acls/put", query=query, body=body)

    def put_secret(
        self,
        scope: str,
        key: str,
        *,
        bytes_value: str = None,
        string_value: str = None,
        **kwargs
    ):
        """Add a secret.

        Inserts a secret under the provided scope with the given name. If a
        secret already exists with the same name, this command overwrites the
        existing secret's value. The server encrypts the secret using the secret
        scope's encryption settings before storing it.

        You must have `WRITE` or `MANAGE` permission on the secret scope. The
        secret key must consist of alphanumeric characters, dashes, underscores,
        and periods, and cannot exceed 128 characters. The maximum allowed
        secret value size is 128 KB. The maximum number of secrets in a given
        scope is 1000.

        The input fields "string_value" or "bytes_value" specify the type of the
        secret, which will determine the value returned when the secret value is
        requested. Exactly one must be specified.

        Throws `RESOURCE_DOES_NOT_EXIST` if no such secret scope exists. Throws
        `RESOURCE_LIMIT_EXCEEDED` if maximum number of secrets in scope is
        exceeded. Throws `INVALID_PARAMETER_VALUE` if the key name or value
        length is invalid. Throws `PERMISSION_DENIED` if the user does not have
        permission to make this API call."""

        request = kwargs.get("request", None)
        if not request:
            request = PutSecret(
                bytes_value=bytes_value, key=key, scope=scope, string_value=string_value
            )
        body = request.as_dict()
        query = {}

        self._api.do("POST", "/api/2.0/secrets/put", query=query, body=body)
