# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

from __future__ import annotations

import logging
from dataclasses import dataclass
from enum import Enum
from typing import Dict, Iterator, List, Optional

from ._internal import _enum, _from_dict, _repeated_dict, _repeated_enum

_LOG = logging.getLogger('databricks.sdk')

# all definitions in this file are in alphabetical order


@dataclass
class CreateIpAccessList:
    """Details required to configure a block list or allow list."""

    label: str
    """Label for the IP access list. This **cannot** be empty."""

    list_type: ListType
    """Type of IP access list. Valid values are as follows and are case-sensitive:
    
    * `ALLOW`: An allow list. Include this IP or range. * `BLOCK`: A block list. Exclude this IP or
    range. IP addresses in the block list are excluded even if they are included in an allow list."""

    ip_addresses: Optional[List[str]] = None

    def as_dict(self) -> dict:
        """Serializes the CreateIpAccessList into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.ip_addresses: body['ip_addresses'] = [v for v in self.ip_addresses]
        if self.label is not None: body['label'] = self.label
        if self.list_type is not None: body['list_type'] = self.list_type.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> CreateIpAccessList:
        """Deserializes the CreateIpAccessList from a dictionary."""
        return cls(ip_addresses=d.get('ip_addresses', None),
                   label=d.get('label', None),
                   list_type=_enum(d, 'list_type', ListType))


@dataclass
class CreateIpAccessListResponse:
    """An IP access list was successfully created."""

    ip_access_list: Optional[IpAccessListInfo] = None
    """Definition of an IP Access list"""

    def as_dict(self) -> dict:
        """Serializes the CreateIpAccessListResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.ip_access_list: body['ip_access_list'] = self.ip_access_list.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> CreateIpAccessListResponse:
        """Deserializes the CreateIpAccessListResponse from a dictionary."""
        return cls(ip_access_list=_from_dict(d, 'ip_access_list', IpAccessListInfo))


@dataclass
class CreateNetworkConnectivityConfigRequest:
    name: str
    """The name of the network connectivity configuration. The name can contain alphanumeric
    characters, hyphens, and underscores. The length must be between 3 and 30 characters. The name
    must match the regular expression `^[0-9a-zA-Z-_]{3,30}$`."""

    region: str
    """The Azure region for this network connectivity configuration. Only workspaces in the same Azure
    region can be attached to this network connectivity configuration."""

    def as_dict(self) -> dict:
        """Serializes the CreateNetworkConnectivityConfigRequest into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.name is not None: body['name'] = self.name
        if self.region is not None: body['region'] = self.region
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> CreateNetworkConnectivityConfigRequest:
        """Deserializes the CreateNetworkConnectivityConfigRequest from a dictionary."""
        return cls(name=d.get('name', None), region=d.get('region', None))


@dataclass
class CreateOboTokenRequest:
    application_id: str
    """Application ID of the service principal."""

    lifetime_seconds: int
    """The number of seconds before the token expires."""

    comment: Optional[str] = None
    """Comment that describes the purpose of the token."""

    def as_dict(self) -> dict:
        """Serializes the CreateOboTokenRequest into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.application_id is not None: body['application_id'] = self.application_id
        if self.comment is not None: body['comment'] = self.comment
        if self.lifetime_seconds is not None: body['lifetime_seconds'] = self.lifetime_seconds
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> CreateOboTokenRequest:
        """Deserializes the CreateOboTokenRequest from a dictionary."""
        return cls(application_id=d.get('application_id', None),
                   comment=d.get('comment', None),
                   lifetime_seconds=d.get('lifetime_seconds', None))


@dataclass
class CreateOboTokenResponse:
    token_info: Optional[TokenInfo] = None

    token_value: Optional[str] = None
    """Value of the token."""

    def as_dict(self) -> dict:
        """Serializes the CreateOboTokenResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.token_info: body['token_info'] = self.token_info.as_dict()
        if self.token_value is not None: body['token_value'] = self.token_value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> CreateOboTokenResponse:
        """Deserializes the CreateOboTokenResponse from a dictionary."""
        return cls(token_info=_from_dict(d, 'token_info', TokenInfo), token_value=d.get('token_value', None))


@dataclass
class CreatePrivateEndpointRuleRequest:
    resource_id: str
    """The Azure resource ID of the target resource."""

    group_id: CreatePrivateEndpointRuleRequestGroupId
    """The sub-resource type (group ID) of the target resource. Note that to connect to workspace root
    storage (root DBFS), you need two endpoints, one for `blob` and one for `dfs`."""

    network_connectivity_config_id: Optional[str] = None
    """Your Network Connectvity Configuration ID."""

    def as_dict(self) -> dict:
        """Serializes the CreatePrivateEndpointRuleRequest into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.group_id is not None: body['group_id'] = self.group_id.value
        if self.network_connectivity_config_id is not None:
            body['network_connectivity_config_id'] = self.network_connectivity_config_id
        if self.resource_id is not None: body['resource_id'] = self.resource_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> CreatePrivateEndpointRuleRequest:
        """Deserializes the CreatePrivateEndpointRuleRequest from a dictionary."""
        return cls(group_id=_enum(d, 'group_id', CreatePrivateEndpointRuleRequestGroupId),
                   network_connectivity_config_id=d.get('network_connectivity_config_id', None),
                   resource_id=d.get('resource_id', None))


class CreatePrivateEndpointRuleRequestGroupId(Enum):
    """The sub-resource type (group ID) of the target resource. Note that to connect to workspace root
    storage (root DBFS), you need two endpoints, one for `blob` and one for `dfs`."""

    BLOB = 'blob'
    DFS = 'dfs'
    MYSQL_SERVER = 'mysqlServer'
    SQL_SERVER = 'sqlServer'


@dataclass
class CreateTokenRequest:
    comment: Optional[str] = None
    """Optional description to attach to the token."""

    lifetime_seconds: Optional[int] = None
    """The lifetime of the token, in seconds.
    
    If the ifetime is not specified, this token remains valid indefinitely."""

    def as_dict(self) -> dict:
        """Serializes the CreateTokenRequest into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.comment is not None: body['comment'] = self.comment
        if self.lifetime_seconds is not None: body['lifetime_seconds'] = self.lifetime_seconds
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> CreateTokenRequest:
        """Deserializes the CreateTokenRequest from a dictionary."""
        return cls(comment=d.get('comment', None), lifetime_seconds=d.get('lifetime_seconds', None))


@dataclass
class CreateTokenResponse:
    token_info: Optional[PublicTokenInfo] = None
    """The information for the new token."""

    token_value: Optional[str] = None
    """The value of the new token."""

    def as_dict(self) -> dict:
        """Serializes the CreateTokenResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.token_info: body['token_info'] = self.token_info.as_dict()
        if self.token_value is not None: body['token_value'] = self.token_value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> CreateTokenResponse:
        """Deserializes the CreateTokenResponse from a dictionary."""
        return cls(token_info=_from_dict(d, 'token_info', PublicTokenInfo),
                   token_value=d.get('token_value', None))


@dataclass
class DefaultNamespaceSetting:
    """This represents the setting configuration for the default namespace in the Databricks workspace.
    Setting the default catalog for the workspace determines the catalog that is used when queries
    do not reference a fully qualified 3 level name. For example, if the default catalog is set to
    'retail_prod' then a query 'SELECT * FROM myTable' would reference the object
    'retail_prod.default.myTable' (the schema 'default' is always assumed). This setting requires a
    restart of clusters and SQL warehouses to take effect. Additionally, the default namespace only
    applies when using Unity Catalog-enabled compute."""

    namespace: StringMessage

    etag: Optional[str] = None
    """etag used for versioning. The response is at least as fresh as the eTag provided. This is used
    for optimistic concurrency control as a way to help prevent simultaneous writes of a setting
    overwriting each other. It is strongly suggested that systems make use of the etag in the read
    -> update pattern to perform setting updates in order to avoid race conditions. That is, get an
    etag from a GET request, and pass it with the PATCH request to identify the setting version you
    are updating."""

    setting_name: Optional[str] = None
    """Name of the corresponding setting. This field is populated in the response, but it will not be
    respected even if it's set in the request body. The setting name in the path parameter will be
    respected instead. Setting name is required to be 'default' if the setting only has one instance
    per workspace."""

    def as_dict(self) -> dict:
        """Serializes the DefaultNamespaceSetting into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.etag is not None: body['etag'] = self.etag
        if self.namespace: body['namespace'] = self.namespace.as_dict()
        if self.setting_name is not None: body['setting_name'] = self.setting_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> DefaultNamespaceSetting:
        """Deserializes the DefaultNamespaceSetting from a dictionary."""
        return cls(etag=d.get('etag', None),
                   namespace=_from_dict(d, 'namespace', StringMessage),
                   setting_name=d.get('setting_name', None))


@dataclass
class DeleteDefaultWorkspaceNamespaceResponse:
    etag: str
    """etag used for versioning. The response is at least as fresh as the eTag provided. This is used
    for optimistic concurrency control as a way to help prevent simultaneous writes of a setting
    overwriting each other. It is strongly suggested that systems make use of the etag in the read
    -> update pattern to perform setting updates in order to avoid race conditions. That is, get an
    etag from a GET request, and pass it with the PATCH request to identify the setting version you
    are updating."""

    def as_dict(self) -> dict:
        """Serializes the DeleteDefaultWorkspaceNamespaceResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.etag is not None: body['etag'] = self.etag
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> DeleteDefaultWorkspaceNamespaceResponse:
        """Deserializes the DeleteDefaultWorkspaceNamespaceResponse from a dictionary."""
        return cls(etag=d.get('etag', None))


@dataclass
class DeletePersonalComputeSettingResponse:
    etag: str
    """etag used for versioning. The response is at least as fresh as the eTag provided. This is used
    for optimistic concurrency control as a way to help prevent simultaneous writes of a setting
    overwriting each other. It is strongly suggested that systems make use of the etag in the read
    -> update pattern to perform setting updates in order to avoid race conditions. That is, get an
    etag from a GET request, and pass it with the PATCH request to identify the setting version you
    are updating."""

    def as_dict(self) -> dict:
        """Serializes the DeletePersonalComputeSettingResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.etag is not None: body['etag'] = self.etag
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> DeletePersonalComputeSettingResponse:
        """Deserializes the DeletePersonalComputeSettingResponse from a dictionary."""
        return cls(etag=d.get('etag', None))


@dataclass
class ExchangeToken:
    credential: Optional[str] = None
    """The requested token."""

    credential_eol_time: Optional[int] = None
    """The end-of-life timestamp of the token. The value is in milliseconds since the Unix epoch."""

    owner_id: Optional[int] = None
    """User ID of the user that owns this token."""

    scopes: Optional[List[str]] = None
    """The scopes of access granted in the token."""

    token_type: Optional[TokenType] = None
    """The type of token request. As of now, only `AZURE_ACTIVE_DIRECTORY_TOKEN` is supported."""

    def as_dict(self) -> dict:
        """Serializes the ExchangeToken into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.credential is not None: body['credential'] = self.credential
        if self.credential_eol_time is not None: body['credentialEolTime'] = self.credential_eol_time
        if self.owner_id is not None: body['ownerId'] = self.owner_id
        if self.scopes: body['scopes'] = [v for v in self.scopes]
        if self.token_type is not None: body['tokenType'] = self.token_type.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ExchangeToken:
        """Deserializes the ExchangeToken from a dictionary."""
        return cls(credential=d.get('credential', None),
                   credential_eol_time=d.get('credentialEolTime', None),
                   owner_id=d.get('ownerId', None),
                   scopes=d.get('scopes', None),
                   token_type=_enum(d, 'tokenType', TokenType))


@dataclass
class ExchangeTokenRequest:
    partition_id: PartitionId

    token_type: List[TokenType]

    scopes: List[str]
    """Array of scopes for the token request."""

    def as_dict(self) -> dict:
        """Serializes the ExchangeTokenRequest into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.partition_id: body['partitionId'] = self.partition_id.as_dict()
        if self.scopes: body['scopes'] = [v for v in self.scopes]
        if self.token_type: body['tokenType'] = [v.value for v in self.token_type]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ExchangeTokenRequest:
        """Deserializes the ExchangeTokenRequest from a dictionary."""
        return cls(partition_id=_from_dict(d, 'partitionId', PartitionId),
                   scopes=d.get('scopes', None),
                   token_type=_repeated_enum(d, 'tokenType', TokenType))


@dataclass
class ExchangeTokenResponse:
    values: Optional[List[ExchangeToken]] = None

    def as_dict(self) -> dict:
        """Serializes the ExchangeTokenResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.values: body['values'] = [v.as_dict() for v in self.values]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ExchangeTokenResponse:
        """Deserializes the ExchangeTokenResponse from a dictionary."""
        return cls(values=_repeated_dict(d, 'values', ExchangeToken))


@dataclass
class FetchIpAccessListResponse:
    """An IP access list was successfully returned."""

    ip_access_list: Optional[IpAccessListInfo] = None
    """Definition of an IP Access list"""

    def as_dict(self) -> dict:
        """Serializes the FetchIpAccessListResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.ip_access_list: body['ip_access_list'] = self.ip_access_list.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> FetchIpAccessListResponse:
        """Deserializes the FetchIpAccessListResponse from a dictionary."""
        return cls(ip_access_list=_from_dict(d, 'ip_access_list', IpAccessListInfo))


@dataclass
class GetIpAccessListResponse:
    ip_access_list: Optional[IpAccessListInfo] = None
    """Definition of an IP Access list"""

    def as_dict(self) -> dict:
        """Serializes the GetIpAccessListResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.ip_access_list: body['ip_access_list'] = self.ip_access_list.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> GetIpAccessListResponse:
        """Deserializes the GetIpAccessListResponse from a dictionary."""
        return cls(ip_access_list=_from_dict(d, 'ip_access_list', IpAccessListInfo))


@dataclass
class GetIpAccessListsResponse:
    """IP access lists were successfully returned."""

    ip_access_lists: Optional[List[IpAccessListInfo]] = None

    def as_dict(self) -> dict:
        """Serializes the GetIpAccessListsResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.ip_access_lists: body['ip_access_lists'] = [v.as_dict() for v in self.ip_access_lists]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> GetIpAccessListsResponse:
        """Deserializes the GetIpAccessListsResponse from a dictionary."""
        return cls(ip_access_lists=_repeated_dict(d, 'ip_access_lists', IpAccessListInfo))


@dataclass
class GetTokenPermissionLevelsResponse:
    permission_levels: Optional[List[TokenPermissionsDescription]] = None
    """Specific permission levels"""

    def as_dict(self) -> dict:
        """Serializes the GetTokenPermissionLevelsResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.permission_levels: body['permission_levels'] = [v.as_dict() for v in self.permission_levels]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> GetTokenPermissionLevelsResponse:
        """Deserializes the GetTokenPermissionLevelsResponse from a dictionary."""
        return cls(permission_levels=_repeated_dict(d, 'permission_levels', TokenPermissionsDescription))


@dataclass
class IpAccessListInfo:
    """Definition of an IP Access list"""

    address_count: Optional[int] = None
    """Total number of IP or CIDR values."""

    created_at: Optional[int] = None
    """Creation timestamp in milliseconds."""

    created_by: Optional[int] = None
    """User ID of the user who created this list."""

    enabled: Optional[bool] = None
    """Specifies whether this IP access list is enabled."""

    ip_addresses: Optional[List[str]] = None

    label: Optional[str] = None
    """Label for the IP access list. This **cannot** be empty."""

    list_id: Optional[str] = None
    """Universally unique identifier (UUID) of the IP access list."""

    list_type: Optional[ListType] = None
    """Type of IP access list. Valid values are as follows and are case-sensitive:
    
    * `ALLOW`: An allow list. Include this IP or range. * `BLOCK`: A block list. Exclude this IP or
    range. IP addresses in the block list are excluded even if they are included in an allow list."""

    updated_at: Optional[int] = None
    """Update timestamp in milliseconds."""

    updated_by: Optional[int] = None
    """User ID of the user who updated this list."""

    def as_dict(self) -> dict:
        """Serializes the IpAccessListInfo into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.address_count is not None: body['address_count'] = self.address_count
        if self.created_at is not None: body['created_at'] = self.created_at
        if self.created_by is not None: body['created_by'] = self.created_by
        if self.enabled is not None: body['enabled'] = self.enabled
        if self.ip_addresses: body['ip_addresses'] = [v for v in self.ip_addresses]
        if self.label is not None: body['label'] = self.label
        if self.list_id is not None: body['list_id'] = self.list_id
        if self.list_type is not None: body['list_type'] = self.list_type.value
        if self.updated_at is not None: body['updated_at'] = self.updated_at
        if self.updated_by is not None: body['updated_by'] = self.updated_by
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> IpAccessListInfo:
        """Deserializes the IpAccessListInfo from a dictionary."""
        return cls(address_count=d.get('address_count', None),
                   created_at=d.get('created_at', None),
                   created_by=d.get('created_by', None),
                   enabled=d.get('enabled', None),
                   ip_addresses=d.get('ip_addresses', None),
                   label=d.get('label', None),
                   list_id=d.get('list_id', None),
                   list_type=_enum(d, 'list_type', ListType),
                   updated_at=d.get('updated_at', None),
                   updated_by=d.get('updated_by', None))


@dataclass
class ListIpAccessListResponse:
    """IP access lists were successfully returned."""

    ip_access_lists: Optional[List[IpAccessListInfo]] = None

    def as_dict(self) -> dict:
        """Serializes the ListIpAccessListResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.ip_access_lists: body['ip_access_lists'] = [v.as_dict() for v in self.ip_access_lists]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ListIpAccessListResponse:
        """Deserializes the ListIpAccessListResponse from a dictionary."""
        return cls(ip_access_lists=_repeated_dict(d, 'ip_access_lists', IpAccessListInfo))


@dataclass
class ListNccAzurePrivateEndpointRulesResponse:
    items: Optional[List[NccAzurePrivateEndpointRule]] = None

    next_page_token: Optional[str] = None
    """A token that can be used to get the next page of results. If null, there are no more results to
    show."""

    def as_dict(self) -> dict:
        """Serializes the ListNccAzurePrivateEndpointRulesResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.items: body['items'] = [v.as_dict() for v in self.items]
        if self.next_page_token is not None: body['next_page_token'] = self.next_page_token
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ListNccAzurePrivateEndpointRulesResponse:
        """Deserializes the ListNccAzurePrivateEndpointRulesResponse from a dictionary."""
        return cls(items=_repeated_dict(d, 'items', NccAzurePrivateEndpointRule),
                   next_page_token=d.get('next_page_token', None))


@dataclass
class ListNetworkConnectivityConfigurationsResponse:
    items: Optional[List[NetworkConnectivityConfiguration]] = None

    next_page_token: Optional[str] = None
    """A token that can be used to get the next page of results. If null, there are no more results to
    show."""

    def as_dict(self) -> dict:
        """Serializes the ListNetworkConnectivityConfigurationsResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.items: body['items'] = [v.as_dict() for v in self.items]
        if self.next_page_token is not None: body['next_page_token'] = self.next_page_token
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ListNetworkConnectivityConfigurationsResponse:
        """Deserializes the ListNetworkConnectivityConfigurationsResponse from a dictionary."""
        return cls(items=_repeated_dict(d, 'items', NetworkConnectivityConfiguration),
                   next_page_token=d.get('next_page_token', None))


@dataclass
class ListTokensResponse:
    token_infos: Optional[List[TokenInfo]] = None

    def as_dict(self) -> dict:
        """Serializes the ListTokensResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.token_infos: body['token_infos'] = [v.as_dict() for v in self.token_infos]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ListTokensResponse:
        """Deserializes the ListTokensResponse from a dictionary."""
        return cls(token_infos=_repeated_dict(d, 'token_infos', TokenInfo))


class ListType(Enum):
    """Type of IP access list. Valid values are as follows and are case-sensitive:
    
    * `ALLOW`: An allow list. Include this IP or range. * `BLOCK`: A block list. Exclude this IP or
    range. IP addresses in the block list are excluded even if they are included in an allow list."""

    ALLOW = 'ALLOW'
    BLOCK = 'BLOCK'


@dataclass
class NccAzurePrivateEndpointRule:
    connection_state: Optional[NccAzurePrivateEndpointRuleConnectionState] = None
    """The current status of this private endpoint. The private endpoint rules are effective only if
    the connection state is `ESTABLISHED`. Remember that you must approve new endpoints on your
    resources in the Azure portal before they take effect.
    
    The possible values are: - INIT: (deprecated) The endpoint has been created and pending
    approval. - PENDING: The endpoint has been created and pending approval. - ESTABLISHED: The
    endpoint has been approved and is ready to use in your serverless compute resources. - REJECTED:
    Connection was rejected by the private link resource owner. - DISCONNECTED: Connection was
    removed by the private link resource owner, the private endpoint becomes informative and should
    be deleted for clean-up."""

    creation_time: Optional[int] = None
    """Time in epoch milliseconds when this object was created."""

    deactivated: Optional[bool] = None
    """Whether this private endpoint is deactivated."""

    deactivated_at: Optional[int] = None
    """Time in epoch milliseconds when this object was deactivated."""

    endpoint_name: Optional[str] = None
    """The name of the Azure private endpoint resource."""

    group_id: Optional[NccAzurePrivateEndpointRuleGroupId] = None
    """The sub-resource type (group ID) of the target resource. Note that to connect to workspace root
    storage (root DBFS), you need two endpoints, one for `blob` and one for `dfs`."""

    network_connectivity_config_id: Optional[str] = None
    """The ID of a network connectivity configuration, which is the parent resource of this private
    endpoint rule object."""

    resource_id: Optional[str] = None
    """The Azure resource ID of the target resource."""

    rule_id: Optional[str] = None
    """The ID of a private endpoint rule."""

    updated_time: Optional[int] = None
    """Time in epoch milliseconds when this object was updated."""

    def as_dict(self) -> dict:
        """Serializes the NccAzurePrivateEndpointRule into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.connection_state is not None: body['connection_state'] = self.connection_state.value
        if self.creation_time is not None: body['creation_time'] = self.creation_time
        if self.deactivated is not None: body['deactivated'] = self.deactivated
        if self.deactivated_at is not None: body['deactivated_at'] = self.deactivated_at
        if self.endpoint_name is not None: body['endpoint_name'] = self.endpoint_name
        if self.group_id is not None: body['group_id'] = self.group_id.value
        if self.network_connectivity_config_id is not None:
            body['network_connectivity_config_id'] = self.network_connectivity_config_id
        if self.resource_id is not None: body['resource_id'] = self.resource_id
        if self.rule_id is not None: body['rule_id'] = self.rule_id
        if self.updated_time is not None: body['updated_time'] = self.updated_time
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> NccAzurePrivateEndpointRule:
        """Deserializes the NccAzurePrivateEndpointRule from a dictionary."""
        return cls(connection_state=_enum(d, 'connection_state', NccAzurePrivateEndpointRuleConnectionState),
                   creation_time=d.get('creation_time', None),
                   deactivated=d.get('deactivated', None),
                   deactivated_at=d.get('deactivated_at', None),
                   endpoint_name=d.get('endpoint_name', None),
                   group_id=_enum(d, 'group_id', NccAzurePrivateEndpointRuleGroupId),
                   network_connectivity_config_id=d.get('network_connectivity_config_id', None),
                   resource_id=d.get('resource_id', None),
                   rule_id=d.get('rule_id', None),
                   updated_time=d.get('updated_time', None))


class NccAzurePrivateEndpointRuleConnectionState(Enum):
    """The current status of this private endpoint. The private endpoint rules are effective only if
    the connection state is `ESTABLISHED`. Remember that you must approve new endpoints on your
    resources in the Azure portal before they take effect.
    
    The possible values are: - INIT: (deprecated) The endpoint has been created and pending
    approval. - PENDING: The endpoint has been created and pending approval. - ESTABLISHED: The
    endpoint has been approved and is ready to use in your serverless compute resources. - REJECTED:
    Connection was rejected by the private link resource owner. - DISCONNECTED: Connection was
    removed by the private link resource owner, the private endpoint becomes informative and should
    be deleted for clean-up."""

    DISCONNECTED = 'DISCONNECTED'
    ESTABLISHED = 'ESTABLISHED'
    INIT = 'INIT'
    PENDING = 'PENDING'
    REJECTED = 'REJECTED'


class NccAzurePrivateEndpointRuleGroupId(Enum):
    """The sub-resource type (group ID) of the target resource. Note that to connect to workspace root
    storage (root DBFS), you need two endpoints, one for `blob` and one for `dfs`."""

    BLOB = 'blob'
    DFS = 'dfs'
    MYSQL_SERVER = 'mysqlServer'
    SQL_SERVER = 'sqlServer'


@dataclass
class NccAzureServiceEndpointRule:
    """The stable Azure service endpoints. You can configure the firewall of your Azure resources to
    allow traffic from your Databricks serverless compute resources."""

    subnets: Optional[List[str]] = None
    """The list of subnets from which Databricks network traffic originates when accessing your Azure
    resources."""

    target_region: Optional[str] = None
    """The Azure region in which this service endpoint rule applies."""

    target_services: Optional[List[str]] = None
    """The Azure services to which this service endpoint rule applies to."""

    def as_dict(self) -> dict:
        """Serializes the NccAzureServiceEndpointRule into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.subnets: body['subnets'] = [v for v in self.subnets]
        if self.target_region is not None: body['target_region'] = self.target_region
        if self.target_services: body['target_services'] = [v for v in self.target_services]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> NccAzureServiceEndpointRule:
        """Deserializes the NccAzureServiceEndpointRule from a dictionary."""
        return cls(subnets=d.get('subnets', None),
                   target_region=d.get('target_region', None),
                   target_services=d.get('target_services', None))


@dataclass
class NccEgressConfig:
    """The network connectivity rules that apply to network traffic from your serverless compute
    resources."""

    default_rules: Optional[NccEgressDefaultRules] = None
    """The network connectivity rules that are applied by default without resource specific
    configurations. You can find the stable network information of your serverless compute resources
    here."""

    target_rules: Optional[NccEgressTargetRules] = None
    """The network connectivity rules that configured for each destinations. These rules override
    default rules."""

    def as_dict(self) -> dict:
        """Serializes the NccEgressConfig into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.default_rules: body['default_rules'] = self.default_rules.as_dict()
        if self.target_rules: body['target_rules'] = self.target_rules.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> NccEgressConfig:
        """Deserializes the NccEgressConfig from a dictionary."""
        return cls(default_rules=_from_dict(d, 'default_rules', NccEgressDefaultRules),
                   target_rules=_from_dict(d, 'target_rules', NccEgressTargetRules))


@dataclass
class NccEgressDefaultRules:
    """The network connectivity rules that are applied by default without resource specific
    configurations. You can find the stable network information of your serverless compute resources
    here."""

    azure_service_endpoint_rule: Optional[NccAzureServiceEndpointRule] = None
    """The stable Azure service endpoints. You can configure the firewall of your Azure resources to
    allow traffic from your Databricks serverless compute resources."""

    def as_dict(self) -> dict:
        """Serializes the NccEgressDefaultRules into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.azure_service_endpoint_rule:
            body['azure_service_endpoint_rule'] = self.azure_service_endpoint_rule.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> NccEgressDefaultRules:
        """Deserializes the NccEgressDefaultRules from a dictionary."""
        return cls(azure_service_endpoint_rule=_from_dict(d, 'azure_service_endpoint_rule',
                                                          NccAzureServiceEndpointRule))


@dataclass
class NccEgressTargetRules:
    """The network connectivity rules that configured for each destinations. These rules override
    default rules."""

    azure_private_endpoint_rules: Optional[List[NccAzurePrivateEndpointRule]] = None

    def as_dict(self) -> dict:
        """Serializes the NccEgressTargetRules into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.azure_private_endpoint_rules:
            body['azure_private_endpoint_rules'] = [v.as_dict() for v in self.azure_private_endpoint_rules]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> NccEgressTargetRules:
        """Deserializes the NccEgressTargetRules from a dictionary."""
        return cls(azure_private_endpoint_rules=_repeated_dict(d, 'azure_private_endpoint_rules',
                                                               NccAzurePrivateEndpointRule))


@dataclass
class NetworkConnectivityConfiguration:
    account_id: Optional[str] = None
    """The Databricks account ID that hosts the credential."""

    creation_time: Optional[int] = None
    """Time in epoch milliseconds when this object was created."""

    egress_config: Optional[NccEgressConfig] = None
    """The network connectivity rules that apply to network traffic from your serverless compute
    resources."""

    name: Optional[str] = None
    """The name of the network connectivity configuration. The name can contain alphanumeric
    characters, hyphens, and underscores. The length must be between 3 and 30 characters. The name
    must match the regular expression `^[0-9a-zA-Z-_]{3,30}$`."""

    network_connectivity_config_id: Optional[str] = None
    """Databricks network connectivity configuration ID."""

    region: Optional[str] = None
    """The Azure region for this network connectivity configuration. Only workspaces in the same Azure
    region can be attached to this network connectivity configuration."""

    updated_time: Optional[int] = None
    """Time in epoch milliseconds when this object was updated."""

    def as_dict(self) -> dict:
        """Serializes the NetworkConnectivityConfiguration into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.account_id is not None: body['account_id'] = self.account_id
        if self.creation_time is not None: body['creation_time'] = self.creation_time
        if self.egress_config: body['egress_config'] = self.egress_config.as_dict()
        if self.name is not None: body['name'] = self.name
        if self.network_connectivity_config_id is not None:
            body['network_connectivity_config_id'] = self.network_connectivity_config_id
        if self.region is not None: body['region'] = self.region
        if self.updated_time is not None: body['updated_time'] = self.updated_time
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> NetworkConnectivityConfiguration:
        """Deserializes the NetworkConnectivityConfiguration from a dictionary."""
        return cls(account_id=d.get('account_id', None),
                   creation_time=d.get('creation_time', None),
                   egress_config=_from_dict(d, 'egress_config', NccEgressConfig),
                   name=d.get('name', None),
                   network_connectivity_config_id=d.get('network_connectivity_config_id', None),
                   region=d.get('region', None),
                   updated_time=d.get('updated_time', None))


@dataclass
class PartitionId:
    workspace_id: Optional[int] = None
    """The ID of the workspace."""

    def as_dict(self) -> dict:
        """Serializes the PartitionId into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.workspace_id is not None: body['workspaceId'] = self.workspace_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> PartitionId:
        """Deserializes the PartitionId from a dictionary."""
        return cls(workspace_id=d.get('workspaceId', None))


@dataclass
class PersonalComputeMessage:
    value: PersonalComputeMessageEnum
    """ON: Grants all users in all workspaces access to the Personal Compute default policy, allowing
    all users to create single-machine compute resources. DELEGATE: Moves access control for the
    Personal Compute default policy to individual workspaces and requires a workspace’s users or
    groups to be added to the ACLs of that workspace’s Personal Compute default policy before they
    will be able to create compute resources through that policy."""

    def as_dict(self) -> dict:
        """Serializes the PersonalComputeMessage into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.value is not None: body['value'] = self.value.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> PersonalComputeMessage:
        """Deserializes the PersonalComputeMessage from a dictionary."""
        return cls(value=_enum(d, 'value', PersonalComputeMessageEnum))


class PersonalComputeMessageEnum(Enum):
    """ON: Grants all users in all workspaces access to the Personal Compute default policy, allowing
    all users to create single-machine compute resources. DELEGATE: Moves access control for the
    Personal Compute default policy to individual workspaces and requires a workspace’s users or
    groups to be added to the ACLs of that workspace’s Personal Compute default policy before they
    will be able to create compute resources through that policy."""

    DELEGATE = 'DELEGATE'
    ON = 'ON'


@dataclass
class PersonalComputeSetting:
    personal_compute: PersonalComputeMessage

    etag: Optional[str] = None
    """etag used for versioning. The response is at least as fresh as the eTag provided. This is used
    for optimistic concurrency control as a way to help prevent simultaneous writes of a setting
    overwriting each other. It is strongly suggested that systems make use of the etag in the read
    -> update pattern to perform setting updates in order to avoid race conditions. That is, get an
    etag from a GET request, and pass it with the PATCH request to identify the setting version you
    are updating."""

    setting_name: Optional[str] = None
    """Name of the corresponding setting. This field is populated in the response, but it will not be
    respected even if it's set in the request body. The setting name in the path parameter will be
    respected instead."""

    def as_dict(self) -> dict:
        """Serializes the PersonalComputeSetting into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.etag is not None: body['etag'] = self.etag
        if self.personal_compute: body['personal_compute'] = self.personal_compute.as_dict()
        if self.setting_name is not None: body['setting_name'] = self.setting_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> PersonalComputeSetting:
        """Deserializes the PersonalComputeSetting from a dictionary."""
        return cls(etag=d.get('etag', None),
                   personal_compute=_from_dict(d, 'personal_compute', PersonalComputeMessage),
                   setting_name=d.get('setting_name', None))


@dataclass
class PublicTokenInfo:
    comment: Optional[str] = None
    """Comment the token was created with, if applicable."""

    creation_time: Optional[int] = None
    """Server time (in epoch milliseconds) when the token was created."""

    expiry_time: Optional[int] = None
    """Server time (in epoch milliseconds) when the token will expire, or -1 if not applicable."""

    token_id: Optional[str] = None
    """The ID of this token."""

    def as_dict(self) -> dict:
        """Serializes the PublicTokenInfo into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.comment is not None: body['comment'] = self.comment
        if self.creation_time is not None: body['creation_time'] = self.creation_time
        if self.expiry_time is not None: body['expiry_time'] = self.expiry_time
        if self.token_id is not None: body['token_id'] = self.token_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> PublicTokenInfo:
        """Deserializes the PublicTokenInfo from a dictionary."""
        return cls(comment=d.get('comment', None),
                   creation_time=d.get('creation_time', None),
                   expiry_time=d.get('expiry_time', None),
                   token_id=d.get('token_id', None))


@dataclass
class ReplaceIpAccessList:
    """Details required to replace an IP access list."""

    label: str
    """Label for the IP access list. This **cannot** be empty."""

    list_type: ListType
    """Type of IP access list. Valid values are as follows and are case-sensitive:
    
    * `ALLOW`: An allow list. Include this IP or range. * `BLOCK`: A block list. Exclude this IP or
    range. IP addresses in the block list are excluded even if they are included in an allow list."""

    enabled: bool
    """Specifies whether this IP access list is enabled."""

    ip_access_list_id: Optional[str] = None
    """The ID for the corresponding IP access list to modify"""

    ip_addresses: Optional[List[str]] = None

    def as_dict(self) -> dict:
        """Serializes the ReplaceIpAccessList into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.enabled is not None: body['enabled'] = self.enabled
        if self.ip_access_list_id is not None: body['ip_access_list_id'] = self.ip_access_list_id
        if self.ip_addresses: body['ip_addresses'] = [v for v in self.ip_addresses]
        if self.label is not None: body['label'] = self.label
        if self.list_type is not None: body['list_type'] = self.list_type.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ReplaceIpAccessList:
        """Deserializes the ReplaceIpAccessList from a dictionary."""
        return cls(enabled=d.get('enabled', None),
                   ip_access_list_id=d.get('ip_access_list_id', None),
                   ip_addresses=d.get('ip_addresses', None),
                   label=d.get('label', None),
                   list_type=_enum(d, 'list_type', ListType))


@dataclass
class RevokeTokenRequest:
    token_id: str
    """The ID of the token to be revoked."""

    def as_dict(self) -> dict:
        """Serializes the RevokeTokenRequest into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.token_id is not None: body['token_id'] = self.token_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> RevokeTokenRequest:
        """Deserializes the RevokeTokenRequest from a dictionary."""
        return cls(token_id=d.get('token_id', None))


@dataclass
class StringMessage:
    value: Optional[str] = None
    """Represents a generic string value."""

    def as_dict(self) -> dict:
        """Serializes the StringMessage into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.value is not None: body['value'] = self.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> StringMessage:
        """Deserializes the StringMessage from a dictionary."""
        return cls(value=d.get('value', None))


@dataclass
class TokenAccessControlRequest:
    group_name: Optional[str] = None
    """name of the group"""

    permission_level: Optional[TokenPermissionLevel] = None
    """Permission level"""

    service_principal_name: Optional[str] = None
    """Application ID of an active service principal. Setting this field requires the
    `servicePrincipal/user` role."""

    user_name: Optional[str] = None
    """name of the user"""

    def as_dict(self) -> dict:
        """Serializes the TokenAccessControlRequest into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.group_name is not None: body['group_name'] = self.group_name
        if self.permission_level is not None: body['permission_level'] = self.permission_level.value
        if self.service_principal_name is not None:
            body['service_principal_name'] = self.service_principal_name
        if self.user_name is not None: body['user_name'] = self.user_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> TokenAccessControlRequest:
        """Deserializes the TokenAccessControlRequest from a dictionary."""
        return cls(group_name=d.get('group_name', None),
                   permission_level=_enum(d, 'permission_level', TokenPermissionLevel),
                   service_principal_name=d.get('service_principal_name', None),
                   user_name=d.get('user_name', None))


@dataclass
class TokenAccessControlResponse:
    all_permissions: Optional[List[TokenPermission]] = None
    """All permissions."""

    display_name: Optional[str] = None
    """Display name of the user or service principal."""

    group_name: Optional[str] = None
    """name of the group"""

    service_principal_name: Optional[str] = None
    """Name of the service principal."""

    user_name: Optional[str] = None
    """name of the user"""

    def as_dict(self) -> dict:
        """Serializes the TokenAccessControlResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.all_permissions: body['all_permissions'] = [v.as_dict() for v in self.all_permissions]
        if self.display_name is not None: body['display_name'] = self.display_name
        if self.group_name is not None: body['group_name'] = self.group_name
        if self.service_principal_name is not None:
            body['service_principal_name'] = self.service_principal_name
        if self.user_name is not None: body['user_name'] = self.user_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> TokenAccessControlResponse:
        """Deserializes the TokenAccessControlResponse from a dictionary."""
        return cls(all_permissions=_repeated_dict(d, 'all_permissions', TokenPermission),
                   display_name=d.get('display_name', None),
                   group_name=d.get('group_name', None),
                   service_principal_name=d.get('service_principal_name', None),
                   user_name=d.get('user_name', None))


@dataclass
class TokenInfo:
    comment: Optional[str] = None
    """Comment that describes the purpose of the token, specified by the token creator."""

    created_by_id: Optional[int] = None
    """User ID of the user that created the token."""

    created_by_username: Optional[str] = None
    """Username of the user that created the token."""

    creation_time: Optional[int] = None
    """Timestamp when the token was created."""

    expiry_time: Optional[int] = None
    """Timestamp when the token expires."""

    owner_id: Optional[int] = None
    """User ID of the user that owns the token."""

    token_id: Optional[str] = None
    """ID of the token."""

    def as_dict(self) -> dict:
        """Serializes the TokenInfo into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.comment is not None: body['comment'] = self.comment
        if self.created_by_id is not None: body['created_by_id'] = self.created_by_id
        if self.created_by_username is not None: body['created_by_username'] = self.created_by_username
        if self.creation_time is not None: body['creation_time'] = self.creation_time
        if self.expiry_time is not None: body['expiry_time'] = self.expiry_time
        if self.owner_id is not None: body['owner_id'] = self.owner_id
        if self.token_id is not None: body['token_id'] = self.token_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> TokenInfo:
        """Deserializes the TokenInfo from a dictionary."""
        return cls(comment=d.get('comment', None),
                   created_by_id=d.get('created_by_id', None),
                   created_by_username=d.get('created_by_username', None),
                   creation_time=d.get('creation_time', None),
                   expiry_time=d.get('expiry_time', None),
                   owner_id=d.get('owner_id', None),
                   token_id=d.get('token_id', None))


@dataclass
class TokenPermission:
    inherited: Optional[bool] = None

    inherited_from_object: Optional[List[str]] = None

    permission_level: Optional[TokenPermissionLevel] = None
    """Permission level"""

    def as_dict(self) -> dict:
        """Serializes the TokenPermission into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.inherited is not None: body['inherited'] = self.inherited
        if self.inherited_from_object: body['inherited_from_object'] = [v for v in self.inherited_from_object]
        if self.permission_level is not None: body['permission_level'] = self.permission_level.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> TokenPermission:
        """Deserializes the TokenPermission from a dictionary."""
        return cls(inherited=d.get('inherited', None),
                   inherited_from_object=d.get('inherited_from_object', None),
                   permission_level=_enum(d, 'permission_level', TokenPermissionLevel))


class TokenPermissionLevel(Enum):
    """Permission level"""

    CAN_USE = 'CAN_USE'


@dataclass
class TokenPermissions:
    access_control_list: Optional[List[TokenAccessControlResponse]] = None

    object_id: Optional[str] = None

    object_type: Optional[str] = None

    def as_dict(self) -> dict:
        """Serializes the TokenPermissions into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.access_control_list:
            body['access_control_list'] = [v.as_dict() for v in self.access_control_list]
        if self.object_id is not None: body['object_id'] = self.object_id
        if self.object_type is not None: body['object_type'] = self.object_type
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> TokenPermissions:
        """Deserializes the TokenPermissions from a dictionary."""
        return cls(access_control_list=_repeated_dict(d, 'access_control_list', TokenAccessControlResponse),
                   object_id=d.get('object_id', None),
                   object_type=d.get('object_type', None))


@dataclass
class TokenPermissionsDescription:
    description: Optional[str] = None

    permission_level: Optional[TokenPermissionLevel] = None
    """Permission level"""

    def as_dict(self) -> dict:
        """Serializes the TokenPermissionsDescription into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.description is not None: body['description'] = self.description
        if self.permission_level is not None: body['permission_level'] = self.permission_level.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> TokenPermissionsDescription:
        """Deserializes the TokenPermissionsDescription from a dictionary."""
        return cls(description=d.get('description', None),
                   permission_level=_enum(d, 'permission_level', TokenPermissionLevel))


@dataclass
class TokenPermissionsRequest:
    access_control_list: Optional[List[TokenAccessControlRequest]] = None

    def as_dict(self) -> dict:
        """Serializes the TokenPermissionsRequest into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.access_control_list:
            body['access_control_list'] = [v.as_dict() for v in self.access_control_list]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> TokenPermissionsRequest:
        """Deserializes the TokenPermissionsRequest from a dictionary."""
        return cls(access_control_list=_repeated_dict(d, 'access_control_list', TokenAccessControlRequest))


class TokenType(Enum):
    """The type of token request. As of now, only `AZURE_ACTIVE_DIRECTORY_TOKEN` is supported."""

    AZURE_ACTIVE_DIRECTORY_TOKEN = 'AZURE_ACTIVE_DIRECTORY_TOKEN'


@dataclass
class UpdateIpAccessList:
    """Details required to update an IP access list."""

    enabled: Optional[bool] = None
    """Specifies whether this IP access list is enabled."""

    ip_access_list_id: Optional[str] = None
    """The ID for the corresponding IP access list to modify"""

    ip_addresses: Optional[List[str]] = None

    label: Optional[str] = None
    """Label for the IP access list. This **cannot** be empty."""

    list_type: Optional[ListType] = None
    """Type of IP access list. Valid values are as follows and are case-sensitive:
    
    * `ALLOW`: An allow list. Include this IP or range. * `BLOCK`: A block list. Exclude this IP or
    range. IP addresses in the block list are excluded even if they are included in an allow list."""

    def as_dict(self) -> dict:
        """Serializes the UpdateIpAccessList into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.enabled is not None: body['enabled'] = self.enabled
        if self.ip_access_list_id is not None: body['ip_access_list_id'] = self.ip_access_list_id
        if self.ip_addresses: body['ip_addresses'] = [v for v in self.ip_addresses]
        if self.label is not None: body['label'] = self.label
        if self.list_type is not None: body['list_type'] = self.list_type.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> UpdateIpAccessList:
        """Deserializes the UpdateIpAccessList from a dictionary."""
        return cls(enabled=d.get('enabled', None),
                   ip_access_list_id=d.get('ip_access_list_id', None),
                   ip_addresses=d.get('ip_addresses', None),
                   label=d.get('label', None),
                   list_type=_enum(d, 'list_type', ListType))


WorkspaceConf = Dict[str, str]


class AccountIpAccessListsAPI:
    """The Accounts IP Access List API enables account admins to configure IP access lists for access to the
    account console.
    
    Account IP Access Lists affect web application access and REST API access to the account console and
    account APIs. If the feature is disabled for the account, all access is allowed for this account. There is
    support for allow lists (inclusion) and block lists (exclusion).
    
    When a connection is attempted: 1. **First, all block lists are checked.** If the connection IP address
    matches any block list, the connection is rejected. 2. **If the connection was not rejected by block
    lists**, the IP address is compared with the allow lists.
    
    If there is at least one allow list for the account, the connection is allowed only if the IP address
    matches an allow list. If there are no allow lists for the account, all IP addresses are allowed.
    
    For all allow lists and block lists combined, the account supports a maximum of 1000 IP/CIDR values, where
    one CIDR counts as a single value.
    
    After changes to the account-level IP access lists, it can take a few minutes for changes to take effect."""

    def __init__(self, api_client):
        self._api = api_client

    def create(self,
               label: str,
               list_type: ListType,
               *,
               ip_addresses: Optional[List[str]] = None) -> CreateIpAccessListResponse:
        """Create access list.
        
        Creates an IP access list for the account.
        
        A list can be an allow list or a block list. See the top of this file for a description of how the
        server treats allow lists and block lists at runtime.
        
        When creating or updating an IP access list:
        
        * For all allow lists and block lists combined, the API supports a maximum of 1000 IP/CIDR values,
        where one CIDR counts as a single value. Attempts to exceed that number return error 400 with
        `error_code` value `QUOTA_EXCEEDED`. * If the new list would block the calling user's current IP,
        error 400 is returned with `error_code` value `INVALID_STATE`.
        
        It can take a few minutes for the changes to take effect.
        
        :param label: str
          Label for the IP access list. This **cannot** be empty.
        :param list_type: :class:`ListType`
          Type of IP access list. Valid values are as follows and are case-sensitive:
          
          * `ALLOW`: An allow list. Include this IP or range. * `BLOCK`: A block list. Exclude this IP or
          range. IP addresses in the block list are excluded even if they are included in an allow list.
        :param ip_addresses: List[str] (optional)
        
        :returns: :class:`CreateIpAccessListResponse`
        """
        body = {}
        if ip_addresses is not None: body['ip_addresses'] = [v for v in ip_addresses]
        if label is not None: body['label'] = label
        if list_type is not None: body['list_type'] = list_type.value
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        res = self._api.do('POST',
                           f'/api/2.0/accounts/{self._api.account_id}/ip-access-lists',
                           body=body,
                           headers=headers)
        return CreateIpAccessListResponse.from_dict(res)

    def delete(self, ip_access_list_id: str):
        """Delete access list.
        
        Deletes an IP access list, specified by its list ID.
        
        :param ip_access_list_id: str
        
        
        """

        headers = {'Accept': 'application/json', }
        self._api.do('DELETE',
                     f'/api/2.0/accounts/{self._api.account_id}/ip-access-lists/{ip_access_list_id}',
                     headers=headers)

    def get(self, ip_access_list_id: str) -> GetIpAccessListResponse:
        """Get IP access list.
        
        Gets an IP access list, specified by its list ID.
        
        :param ip_access_list_id: str
        
        :returns: :class:`GetIpAccessListResponse`
        """

        headers = {'Accept': 'application/json', }
        res = self._api.do('GET',
                           f'/api/2.0/accounts/{self._api.account_id}/ip-access-lists/{ip_access_list_id}',
                           headers=headers)
        return GetIpAccessListResponse.from_dict(res)

    def list(self) -> Iterator[IpAccessListInfo]:
        """Get access lists.
        
        Gets all IP access lists for the specified account.
        
        :returns: Iterator over :class:`IpAccessListInfo`
        """

        headers = {'Accept': 'application/json', }
        json = self._api.do('GET',
                            f'/api/2.0/accounts/{self._api.account_id}/ip-access-lists',
                            headers=headers)
        parsed = GetIpAccessListsResponse.from_dict(json).ip_access_lists
        return parsed if parsed is not None else []

    def replace(self,
                ip_access_list_id: str,
                label: str,
                list_type: ListType,
                enabled: bool,
                *,
                ip_addresses: Optional[List[str]] = None):
        """Replace access list.
        
        Replaces an IP access list, specified by its ID.
        
        A list can include allow lists and block lists. See the top of this file for a description of how the
        server treats allow lists and block lists at run time. When replacing an IP access list: * For all
        allow lists and block lists combined, the API supports a maximum of 1000 IP/CIDR values, where one
        CIDR counts as a single value. Attempts to exceed that number return error 400 with `error_code` value
        `QUOTA_EXCEEDED`. * If the resulting list would block the calling user's current IP, error 400 is
        returned with `error_code` value `INVALID_STATE`. It can take a few minutes for the changes to take
        effect.
        
        :param ip_access_list_id: str
        :param label: str
          Label for the IP access list. This **cannot** be empty.
        :param list_type: :class:`ListType`
          Type of IP access list. Valid values are as follows and are case-sensitive:
          
          * `ALLOW`: An allow list. Include this IP or range. * `BLOCK`: A block list. Exclude this IP or
          range. IP addresses in the block list are excluded even if they are included in an allow list.
        :param enabled: bool
          Specifies whether this IP access list is enabled.
        :param ip_addresses: List[str] (optional)
        
        
        """
        body = {}
        if enabled is not None: body['enabled'] = enabled
        if ip_addresses is not None: body['ip_addresses'] = [v for v in ip_addresses]
        if label is not None: body['label'] = label
        if list_type is not None: body['list_type'] = list_type.value
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        self._api.do('PUT',
                     f'/api/2.0/accounts/{self._api.account_id}/ip-access-lists/{ip_access_list_id}',
                     body=body,
                     headers=headers)

    def update(self,
               ip_access_list_id: str,
               *,
               enabled: Optional[bool] = None,
               ip_addresses: Optional[List[str]] = None,
               label: Optional[str] = None,
               list_type: Optional[ListType] = None):
        """Update access list.
        
        Updates an existing IP access list, specified by its ID.
        
        A list can include allow lists and block lists. See the top of this file for a description of how the
        server treats allow lists and block lists at run time.
        
        When updating an IP access list:
        
        * For all allow lists and block lists combined, the API supports a maximum of 1000 IP/CIDR values,
        where one CIDR counts as a single value. Attempts to exceed that number return error 400 with
        `error_code` value `QUOTA_EXCEEDED`. * If the updated list would block the calling user's current IP,
        error 400 is returned with `error_code` value `INVALID_STATE`.
        
        It can take a few minutes for the changes to take effect.
        
        :param ip_access_list_id: str
        :param enabled: bool (optional)
          Specifies whether this IP access list is enabled.
        :param ip_addresses: List[str] (optional)
        :param label: str (optional)
          Label for the IP access list. This **cannot** be empty.
        :param list_type: :class:`ListType` (optional)
          Type of IP access list. Valid values are as follows and are case-sensitive:
          
          * `ALLOW`: An allow list. Include this IP or range. * `BLOCK`: A block list. Exclude this IP or
          range. IP addresses in the block list are excluded even if they are included in an allow list.
        
        
        """
        body = {}
        if enabled is not None: body['enabled'] = enabled
        if ip_addresses is not None: body['ip_addresses'] = [v for v in ip_addresses]
        if label is not None: body['label'] = label
        if list_type is not None: body['list_type'] = list_type.value
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        self._api.do('PATCH',
                     f'/api/2.0/accounts/{self._api.account_id}/ip-access-lists/{ip_access_list_id}',
                     body=body,
                     headers=headers)


class AccountSettingsAPI:
    """The Personal Compute enablement setting lets you control which users can use the Personal Compute default
    policy to create compute resources. By default all users in all workspaces have access (ON), but you can
    change the setting to instead let individual workspaces configure access control (DELEGATE).
    
    There is only one instance of this setting per account. Since this setting has a default value, this
    setting is present on all accounts even though it's never set on a given account. Deletion reverts the
    value of the setting back to the default value."""

    def __init__(self, api_client):
        self._api = api_client

    def delete_personal_compute_setting(self, etag: str) -> DeletePersonalComputeSettingResponse:
        """Delete Personal Compute setting.
        
        Reverts back the Personal Compute setting value to default (ON)
        
        :param etag: str
          etag used for versioning. The response is at least as fresh as the eTag provided. This is used for
          optimistic concurrency control as a way to help prevent simultaneous writes of a setting overwriting
          each other. It is strongly suggested that systems make use of the etag in the read -> delete pattern
          to perform setting deletions in order to avoid race conditions. That is, get an etag from a GET
          request, and pass it with the DELETE request to identify the rule set version you are deleting.
        
        :returns: :class:`DeletePersonalComputeSettingResponse`
        """

        query = {}
        if etag is not None: query['etag'] = etag
        headers = {'Accept': 'application/json', }
        res = self._api.do(
            'DELETE',
            f'/api/2.0/accounts/{self._api.account_id}/settings/types/dcp_acct_enable/names/default',
            query=query,
            headers=headers)
        return DeletePersonalComputeSettingResponse.from_dict(res)

    def read_personal_compute_setting(self, etag: str) -> PersonalComputeSetting:
        """Get Personal Compute setting.
        
        Gets the value of the Personal Compute setting.
        
        :param etag: str
          etag used for versioning. The response is at least as fresh as the eTag provided. This is used for
          optimistic concurrency control as a way to help prevent simultaneous writes of a setting overwriting
          each other. It is strongly suggested that systems make use of the etag in the read -> delete pattern
          to perform setting deletions in order to avoid race conditions. That is, get an etag from a GET
          request, and pass it with the DELETE request to identify the rule set version you are deleting.
        
        :returns: :class:`PersonalComputeSetting`
        """

        query = {}
        if etag is not None: query['etag'] = etag
        headers = {'Accept': 'application/json', }
        res = self._api.do(
            'GET',
            f'/api/2.0/accounts/{self._api.account_id}/settings/types/dcp_acct_enable/names/default',
            query=query,
            headers=headers)
        return PersonalComputeSetting.from_dict(res)

    def update_personal_compute_setting(
            self,
            *,
            allow_missing: Optional[bool] = None,
            setting: Optional[PersonalComputeSetting] = None) -> PersonalComputeSetting:
        """Update Personal Compute setting.
        
        Updates the value of the Personal Compute setting.
        
        :param allow_missing: bool (optional)
          This should always be set to true for Settings RPCs. Added for AIP compliance.
        :param setting: :class:`PersonalComputeSetting` (optional)
        
        :returns: :class:`PersonalComputeSetting`
        """
        body = {}
        if allow_missing is not None: body['allow_missing'] = allow_missing
        if setting is not None: body['setting'] = setting.as_dict()
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        res = self._api.do(
            'PATCH',
            f'/api/2.0/accounts/{self._api.account_id}/settings/types/dcp_acct_enable/names/default',
            body=body,
            headers=headers)
        return PersonalComputeSetting.from_dict(res)


class CredentialsManagerAPI:
    """Credentials manager interacts with with Identity Providers to to perform token exchanges using stored
    credentials and refresh tokens."""

    def __init__(self, api_client):
        self._api = api_client

    def exchange_token(self, partition_id: PartitionId, token_type: List[TokenType],
                       scopes: List[str]) -> ExchangeTokenResponse:
        """Exchange token.
        
        Exchange tokens with an Identity Provider to get a new access token. It allowes specifying scopes to
        determine token permissions.
        
        :param partition_id: :class:`PartitionId`
        :param token_type: List[:class:`TokenType`]
        :param scopes: List[str]
          Array of scopes for the token request.
        
        :returns: :class:`ExchangeTokenResponse`
        """
        body = {}
        if partition_id is not None: body['partitionId'] = partition_id.as_dict()
        if scopes is not None: body['scopes'] = [v for v in scopes]
        if token_type is not None: body['tokenType'] = [v.value for v in token_type]
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        res = self._api.do('POST',
                           '/api/2.0/credentials-manager/exchange-tokens/token',
                           body=body,
                           headers=headers)
        return ExchangeTokenResponse.from_dict(res)


class IpAccessListsAPI:
    """IP Access List enables admins to configure IP access lists.
    
    IP access lists affect web application access and REST API access to this workspace only. If the feature
    is disabled for a workspace, all access is allowed for this workspace. There is support for allow lists
    (inclusion) and block lists (exclusion).
    
    When a connection is attempted: 1. **First, all block lists are checked.** If the connection IP address
    matches any block list, the connection is rejected. 2. **If the connection was not rejected by block
    lists**, the IP address is compared with the allow lists.
    
    If there is at least one allow list for the workspace, the connection is allowed only if the IP address
    matches an allow list. If there are no allow lists for the workspace, all IP addresses are allowed.
    
    For all allow lists and block lists combined, the workspace supports a maximum of 1000 IP/CIDR values,
    where one CIDR counts as a single value.
    
    After changes to the IP access list feature, it can take a few minutes for changes to take effect."""

    def __init__(self, api_client):
        self._api = api_client

    def create(self,
               label: str,
               list_type: ListType,
               *,
               ip_addresses: Optional[List[str]] = None) -> CreateIpAccessListResponse:
        """Create access list.
        
        Creates an IP access list for this workspace.
        
        A list can be an allow list or a block list. See the top of this file for a description of how the
        server treats allow lists and block lists at runtime.
        
        When creating or updating an IP access list:
        
        * For all allow lists and block lists combined, the API supports a maximum of 1000 IP/CIDR values,
        where one CIDR counts as a single value. Attempts to exceed that number return error 400 with
        `error_code` value `QUOTA_EXCEEDED`. * If the new list would block the calling user's current IP,
        error 400 is returned with `error_code` value `INVALID_STATE`.
        
        It can take a few minutes for the changes to take effect. **Note**: Your new IP access list has no
        effect until you enable the feature. See :method:workspaceconf/setStatus
        
        :param label: str
          Label for the IP access list. This **cannot** be empty.
        :param list_type: :class:`ListType`
          Type of IP access list. Valid values are as follows and are case-sensitive:
          
          * `ALLOW`: An allow list. Include this IP or range. * `BLOCK`: A block list. Exclude this IP or
          range. IP addresses in the block list are excluded even if they are included in an allow list.
        :param ip_addresses: List[str] (optional)
        
        :returns: :class:`CreateIpAccessListResponse`
        """
        body = {}
        if ip_addresses is not None: body['ip_addresses'] = [v for v in ip_addresses]
        if label is not None: body['label'] = label
        if list_type is not None: body['list_type'] = list_type.value
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        res = self._api.do('POST', '/api/2.0/ip-access-lists', body=body, headers=headers)
        return CreateIpAccessListResponse.from_dict(res)

    def delete(self, ip_access_list_id: str):
        """Delete access list.
        
        Deletes an IP access list, specified by its list ID.
        
        :param ip_access_list_id: str
          The ID for the corresponding IP access list to modify
        
        
        """

        headers = {'Accept': 'application/json', }
        self._api.do('DELETE', f'/api/2.0/ip-access-lists/{ip_access_list_id}', headers=headers)

    def get(self, ip_access_list_id: str) -> FetchIpAccessListResponse:
        """Get access list.
        
        Gets an IP access list, specified by its list ID.
        
        :param ip_access_list_id: str
          The ID for the corresponding IP access list to modify
        
        :returns: :class:`FetchIpAccessListResponse`
        """

        headers = {'Accept': 'application/json', }
        res = self._api.do('GET', f'/api/2.0/ip-access-lists/{ip_access_list_id}', headers=headers)
        return FetchIpAccessListResponse.from_dict(res)

    def list(self) -> Iterator[IpAccessListInfo]:
        """Get access lists.
        
        Gets all IP access lists for the specified workspace.
        
        :returns: Iterator over :class:`IpAccessListInfo`
        """

        headers = {'Accept': 'application/json', }
        json = self._api.do('GET', '/api/2.0/ip-access-lists', headers=headers)
        parsed = ListIpAccessListResponse.from_dict(json).ip_access_lists
        return parsed if parsed is not None else []

    def replace(self,
                ip_access_list_id: str,
                label: str,
                list_type: ListType,
                enabled: bool,
                *,
                ip_addresses: Optional[List[str]] = None):
        """Replace access list.
        
        Replaces an IP access list, specified by its ID.
        
        A list can include allow lists and block lists. See the top of this file for a description of how the
        server treats allow lists and block lists at run time. When replacing an IP access list: * For all
        allow lists and block lists combined, the API supports a maximum of 1000 IP/CIDR values, where one
        CIDR counts as a single value. Attempts to exceed that number return error 400 with `error_code` value
        `QUOTA_EXCEEDED`. * If the resulting list would block the calling user's current IP, error 400 is
        returned with `error_code` value `INVALID_STATE`. It can take a few minutes for the changes to take
        effect. Note that your resulting IP access list has no effect until you enable the feature. See
        :method:workspaceconf/setStatus.
        
        :param ip_access_list_id: str
          The ID for the corresponding IP access list to modify
        :param label: str
          Label for the IP access list. This **cannot** be empty.
        :param list_type: :class:`ListType`
          Type of IP access list. Valid values are as follows and are case-sensitive:
          
          * `ALLOW`: An allow list. Include this IP or range. * `BLOCK`: A block list. Exclude this IP or
          range. IP addresses in the block list are excluded even if they are included in an allow list.
        :param enabled: bool
          Specifies whether this IP access list is enabled.
        :param ip_addresses: List[str] (optional)
        
        
        """
        body = {}
        if enabled is not None: body['enabled'] = enabled
        if ip_addresses is not None: body['ip_addresses'] = [v for v in ip_addresses]
        if label is not None: body['label'] = label
        if list_type is not None: body['list_type'] = list_type.value
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        self._api.do('PUT', f'/api/2.0/ip-access-lists/{ip_access_list_id}', body=body, headers=headers)

    def update(self,
               ip_access_list_id: str,
               *,
               enabled: Optional[bool] = None,
               ip_addresses: Optional[List[str]] = None,
               label: Optional[str] = None,
               list_type: Optional[ListType] = None):
        """Update access list.
        
        Updates an existing IP access list, specified by its ID.
        
        A list can include allow lists and block lists. See the top of this file for a description of how the
        server treats allow lists and block lists at run time.
        
        When updating an IP access list:
        
        * For all allow lists and block lists combined, the API supports a maximum of 1000 IP/CIDR values,
        where one CIDR counts as a single value. Attempts to exceed that number return error 400 with
        `error_code` value `QUOTA_EXCEEDED`. * If the updated list would block the calling user's current IP,
        error 400 is returned with `error_code` value `INVALID_STATE`.
        
        It can take a few minutes for the changes to take effect. Note that your resulting IP access list has
        no effect until you enable the feature. See :method:workspaceconf/setStatus.
        
        :param ip_access_list_id: str
          The ID for the corresponding IP access list to modify
        :param enabled: bool (optional)
          Specifies whether this IP access list is enabled.
        :param ip_addresses: List[str] (optional)
        :param label: str (optional)
          Label for the IP access list. This **cannot** be empty.
        :param list_type: :class:`ListType` (optional)
          Type of IP access list. Valid values are as follows and are case-sensitive:
          
          * `ALLOW`: An allow list. Include this IP or range. * `BLOCK`: A block list. Exclude this IP or
          range. IP addresses in the block list are excluded even if they are included in an allow list.
        
        
        """
        body = {}
        if enabled is not None: body['enabled'] = enabled
        if ip_addresses is not None: body['ip_addresses'] = [v for v in ip_addresses]
        if label is not None: body['label'] = label
        if list_type is not None: body['list_type'] = list_type.value
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        self._api.do('PATCH', f'/api/2.0/ip-access-lists/{ip_access_list_id}', body=body, headers=headers)


class NetworkConnectivityAPI:
    """These APIs provide configurations for the network connectivity of your workspaces for serverless compute
    resources. This API provides stable subnets for your workspace so that you can configure your firewalls on
    your Azure Storage accounts to allow access from Databricks. You can also use the API to provision private
    endpoints for Databricks to privately connect serverless compute resources to your Azure resources using
    Azure Private Link. See [configure serverless secure connectivity].
    
    [configure serverless secure connectivity]: https://learn.microsoft.com/azure/databricks/security/network/serverless-network-security"""

    def __init__(self, api_client):
        self._api = api_client

    def create_network_connectivity_configuration(self, name: str,
                                                  region: str) -> NetworkConnectivityConfiguration:
        """Create a network connectivity configuration.
        
        Creates a network connectivity configuration (NCC), which provides stable Azure service subnets when
        accessing your Azure Storage accounts. You can also use a network connectivity configuration to create
        Databricks-managed private endpoints so that Databricks serverless compute resources privately access
        your resources.
        
        **IMPORTANT**: After you create the network connectivity configuration, you must assign one or more
        workspaces to the new network connectivity configuration. You can share one network connectivity
        configuration with multiple workspaces from the same Azure region within the same Databricks account.
        See [configure serverless secure connectivity].
        
        [configure serverless secure connectivity]: https://learn.microsoft.com/azure/databricks/security/network/serverless-network-security
        
        :param name: str
          The name of the network connectivity configuration. The name can contain alphanumeric characters,
          hyphens, and underscores. The length must be between 3 and 30 characters. The name must match the
          regular expression `^[0-9a-zA-Z-_]{3,30}$`.
        :param region: str
          The Azure region for this network connectivity configuration. Only workspaces in the same Azure
          region can be attached to this network connectivity configuration.
        
        :returns: :class:`NetworkConnectivityConfiguration`
        """
        body = {}
        if name is not None: body['name'] = name
        if region is not None: body['region'] = region
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        res = self._api.do('POST',
                           f'/api/2.0/accounts/{self._api.account_id}/network-connectivity-configs',
                           body=body,
                           headers=headers)
        return NetworkConnectivityConfiguration.from_dict(res)

    def create_private_endpoint_rule(
            self, network_connectivity_config_id: str, resource_id: str,
            group_id: CreatePrivateEndpointRuleRequestGroupId) -> NccAzurePrivateEndpointRule:
        """Create a private endpoint rule.
        
        Create a private endpoint rule for the specified network connectivity config object. Once the object
        is created, Databricks asynchronously provisions a new Azure private endpoint to your specified Azure
        resource.
        
        **IMPORTANT**: You must use Azure portal or other Azure tools to approve the private endpoint to
        complete the connection. To get the information of the private endpoint created, make a `GET` request
        on the new private endpoint rule. See [serverless private link].
        
        [serverless private link]: https://learn.microsoft.com/azure/databricks/security/network/serverless-network-security/serverless-private-link
        
        :param network_connectivity_config_id: str
          Your Network Connectvity Configuration ID.
        :param resource_id: str
          The Azure resource ID of the target resource.
        :param group_id: :class:`CreatePrivateEndpointRuleRequestGroupId`
          The sub-resource type (group ID) of the target resource. Note that to connect to workspace root
          storage (root DBFS), you need two endpoints, one for `blob` and one for `dfs`.
        
        :returns: :class:`NccAzurePrivateEndpointRule`
        """
        body = {}
        if group_id is not None: body['group_id'] = group_id.value
        if resource_id is not None: body['resource_id'] = resource_id
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        res = self._api.do(
            'POST',
            f'/api/2.0/accounts/{self._api.account_id}/network-connectivity-configs/{network_connectivity_config_id}/private-endpoint-rules',
            body=body,
            headers=headers)
        return NccAzurePrivateEndpointRule.from_dict(res)

    def delete_network_connectivity_configuration(self, network_connectivity_config_id: str):
        """Delete a network connectivity configuration.
        
        Deletes a network connectivity configuration.
        
        :param network_connectivity_config_id: str
          Your Network Connectvity Configuration ID.
        
        
        """

        headers = {'Accept': 'application/json', }
        self._api.do(
            'DELETE',
            f'/api/2.0/accounts/{self._api.account_id}/network-connectivity-configs/{network_connectivity_config_id}',
            headers=headers)

    def delete_private_endpoint_rule(self, network_connectivity_config_id: str,
                                     private_endpoint_rule_id: str) -> NccAzurePrivateEndpointRule:
        """Delete a private endpoint rule.
        
        Initiates deleting a private endpoint rule. The private endpoint will be deactivated and will be
        purged after seven days of deactivation. When a private endpoint is in deactivated state,
        `deactivated` field is set to `true` and the private endpoint is not available to your serverless
        compute resources.
        
        :param network_connectivity_config_id: str
          Your Network Connectvity Configuration ID.
        :param private_endpoint_rule_id: str
          Your private endpoint rule ID.
        
        :returns: :class:`NccAzurePrivateEndpointRule`
        """

        headers = {'Accept': 'application/json', }
        res = self._api.do(
            'DELETE',
            f'/api/2.0/accounts/{self._api.account_id}/network-connectivity-configs/{network_connectivity_config_id}/private-endpoint-rules/{private_endpoint_rule_id}',
            headers=headers)
        return NccAzurePrivateEndpointRule.from_dict(res)

    def get_network_connectivity_configuration(
            self, network_connectivity_config_id: str) -> NetworkConnectivityConfiguration:
        """Get a network connectivity configuration.
        
        Gets a network connectivity configuration.
        
        :param network_connectivity_config_id: str
          Your Network Connectvity Configuration ID.
        
        :returns: :class:`NetworkConnectivityConfiguration`
        """

        headers = {'Accept': 'application/json', }
        res = self._api.do(
            'GET',
            f'/api/2.0/accounts/{self._api.account_id}/network-connectivity-configs/{network_connectivity_config_id}',
            headers=headers)
        return NetworkConnectivityConfiguration.from_dict(res)

    def get_private_endpoint_rule(self, network_connectivity_config_id: str,
                                  private_endpoint_rule_id: str) -> NccAzurePrivateEndpointRule:
        """Get a private endpoint rule.
        
        Gets the private endpoint rule.
        
        :param network_connectivity_config_id: str
          Your Network Connectvity Configuration ID.
        :param private_endpoint_rule_id: str
          Your private endpoint rule ID.
        
        :returns: :class:`NccAzurePrivateEndpointRule`
        """

        headers = {'Accept': 'application/json', }
        res = self._api.do(
            'GET',
            f'/api/2.0/accounts/{self._api.account_id}/network-connectivity-configs/{network_connectivity_config_id}/private-endpoint-rules/{private_endpoint_rule_id}',
            headers=headers)
        return NccAzurePrivateEndpointRule.from_dict(res)

    def list_network_connectivity_configurations(self,
                                                 *,
                                                 page_token: Optional[str] = None
                                                 ) -> Iterator[NetworkConnectivityConfiguration]:
        """List network connectivity configurations.
        
        Gets an array of network connectivity configurations.
        
        :param page_token: str (optional)
          Pagination token to go to next page based on previous query.
        
        :returns: Iterator over :class:`NetworkConnectivityConfiguration`
        """

        query = {}
        if page_token is not None: query['page_token'] = page_token
        headers = {'Accept': 'application/json', }

        while True:
            json = self._api.do('GET',
                                f'/api/2.0/accounts/{self._api.account_id}/network-connectivity-configs',
                                query=query,
                                headers=headers)
            if 'items' not in json or not json['items']:
                return
            for v in json['items']:
                yield NetworkConnectivityConfiguration.from_dict(v)
            if 'next_page_token' not in json or not json['next_page_token']:
                return
            query['page_token'] = json['next_page_token']

    def list_private_endpoint_rules(
            self,
            network_connectivity_config_id: str,
            *,
            page_token: Optional[str] = None) -> Iterator[NccAzurePrivateEndpointRule]:
        """List private endpoint rules.
        
        Gets an array of private endpoint rules.
        
        :param network_connectivity_config_id: str
          Your Network Connectvity Configuration ID.
        :param page_token: str (optional)
          Pagination token to go to next page based on previous query.
        
        :returns: Iterator over :class:`NccAzurePrivateEndpointRule`
        """

        query = {}
        if page_token is not None: query['page_token'] = page_token
        headers = {'Accept': 'application/json', }

        while True:
            json = self._api.do(
                'GET',
                f'/api/2.0/accounts/{self._api.account_id}/network-connectivity-configs/{network_connectivity_config_id}/private-endpoint-rules',
                query=query,
                headers=headers)
            if 'items' not in json or not json['items']:
                return
            for v in json['items']:
                yield NccAzurePrivateEndpointRule.from_dict(v)
            if 'next_page_token' not in json or not json['next_page_token']:
                return
            query['page_token'] = json['next_page_token']


class SettingsAPI:
    """The default namespace setting API allows users to configure the default namespace for a Databricks
    workspace.
    
    Through this API, users can retrieve, set, or modify the default namespace used when queries do not
    reference a fully qualified three-level name. For example, if you use the API to set 'retail_prod' as the
    default catalog, then a query 'SELECT * FROM myTable' would reference the object
    'retail_prod.default.myTable' (the schema 'default' is always assumed).
    
    This setting requires a restart of clusters and SQL warehouses to take effect. Additionally, the default
    namespace only applies when using Unity Catalog-enabled compute."""

    def __init__(self, api_client):
        self._api = api_client

    def delete_default_workspace_namespace(self, etag: str) -> DeleteDefaultWorkspaceNamespaceResponse:
        """Delete the default namespace setting.
        
        Deletes the default namespace setting for the workspace. A fresh etag needs to be provided in DELETE
        requests (as a query parameter). The etag can be retrieved by making a GET request before the DELETE
        request. If the setting is updated/deleted concurrently, DELETE will fail with 409 and the request
        will need to be retried by using the fresh etag in the 409 response.
        
        :param etag: str
          etag used for versioning. The response is at least as fresh as the eTag provided. This is used for
          optimistic concurrency control as a way to help prevent simultaneous writes of a setting overwriting
          each other. It is strongly suggested that systems make use of the etag in the read -> delete pattern
          to perform setting deletions in order to avoid race conditions. That is, get an etag from a GET
          request, and pass it with the DELETE request to identify the rule set version you are deleting.
        
        :returns: :class:`DeleteDefaultWorkspaceNamespaceResponse`
        """

        query = {}
        if etag is not None: query['etag'] = etag
        headers = {'Accept': 'application/json', }
        res = self._api.do('DELETE',
                           '/api/2.0/settings/types/default_namespace_ws/names/default',
                           query=query,
                           headers=headers)
        return DeleteDefaultWorkspaceNamespaceResponse.from_dict(res)

    def read_default_workspace_namespace(self, etag: str) -> DefaultNamespaceSetting:
        """Get the default namespace setting.
        
        Gets the default namespace setting.
        
        :param etag: str
          etag used for versioning. The response is at least as fresh as the eTag provided. This is used for
          optimistic concurrency control as a way to help prevent simultaneous writes of a setting overwriting
          each other. It is strongly suggested that systems make use of the etag in the read -> delete pattern
          to perform setting deletions in order to avoid race conditions. That is, get an etag from a GET
          request, and pass it with the DELETE request to identify the rule set version you are deleting.
        
        :returns: :class:`DefaultNamespaceSetting`
        """

        query = {}
        if etag is not None: query['etag'] = etag
        headers = {'Accept': 'application/json', }
        res = self._api.do('GET',
                           '/api/2.0/settings/types/default_namespace_ws/names/default',
                           query=query,
                           headers=headers)
        return DefaultNamespaceSetting.from_dict(res)

    def update_default_workspace_namespace(
            self,
            *,
            allow_missing: Optional[bool] = None,
            field_mask: Optional[str] = None,
            setting: Optional[DefaultNamespaceSetting] = None) -> DefaultNamespaceSetting:
        """Update the default namespace setting.
        
        Updates the default namespace setting for the workspace. A fresh etag needs to be provided in PATCH
        requests (as part of the setting field). The etag can be retrieved by making a GET request before the
        PATCH request. Note that if the setting does not exist, GET will return a NOT_FOUND error and the etag
        will be present in the error response, which should be set in the PATCH request. If the setting is
        updated concurrently, PATCH will fail with 409 and the request will need to be retried by using the
        fresh etag in the 409 response.
        
        :param allow_missing: bool (optional)
          This should always be set to true for Settings API. Added for AIP compliance.
        :param field_mask: str (optional)
          Field mask is required to be passed into the PATCH request. Field mask specifies which fields of the
          setting payload will be updated. For example, for Default Namespace setting, the field mask is
          supposed to contain fields from the DefaultNamespaceSetting.namespace schema.
          
          The field mask needs to be supplied as single string. To specify multiple fields in the field mask,
          use comma as the seperator (no space).
        :param setting: :class:`DefaultNamespaceSetting` (optional)
          This represents the setting configuration for the default namespace in the Databricks workspace.
          Setting the default catalog for the workspace determines the catalog that is used when queries do
          not reference a fully qualified 3 level name. For example, if the default catalog is set to
          'retail_prod' then a query 'SELECT * FROM myTable' would reference the object
          'retail_prod.default.myTable' (the schema 'default' is always assumed). This setting requires a
          restart of clusters and SQL warehouses to take effect. Additionally, the default namespace only
          applies when using Unity Catalog-enabled compute.
        
        :returns: :class:`DefaultNamespaceSetting`
        """
        body = {}
        if allow_missing is not None: body['allow_missing'] = allow_missing
        if field_mask is not None: body['field_mask'] = field_mask
        if setting is not None: body['setting'] = setting.as_dict()
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        res = self._api.do('PATCH',
                           '/api/2.0/settings/types/default_namespace_ws/names/default',
                           body=body,
                           headers=headers)
        return DefaultNamespaceSetting.from_dict(res)


class TokenManagementAPI:
    """Enables administrators to get all tokens and delete tokens for other users. Admins can either get every
    token, get a specific token by ID, or get all tokens for a particular user."""

    def __init__(self, api_client):
        self._api = api_client

    def create_obo_token(self,
                         application_id: str,
                         lifetime_seconds: int,
                         *,
                         comment: Optional[str] = None) -> CreateOboTokenResponse:
        """Create on-behalf token.
        
        Creates a token on behalf of a service principal.
        
        :param application_id: str
          Application ID of the service principal.
        :param lifetime_seconds: int
          The number of seconds before the token expires.
        :param comment: str (optional)
          Comment that describes the purpose of the token.
        
        :returns: :class:`CreateOboTokenResponse`
        """
        body = {}
        if application_id is not None: body['application_id'] = application_id
        if comment is not None: body['comment'] = comment
        if lifetime_seconds is not None: body['lifetime_seconds'] = lifetime_seconds
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        res = self._api.do('POST',
                           '/api/2.0/token-management/on-behalf-of/tokens',
                           body=body,
                           headers=headers)
        return CreateOboTokenResponse.from_dict(res)

    def delete(self, token_id: str):
        """Delete a token.
        
        Deletes a token, specified by its ID.
        
        :param token_id: str
          The ID of the token to get.
        
        
        """

        headers = {}
        self._api.do('DELETE', f'/api/2.0/token-management/tokens/{token_id}', headers=headers)

    def get(self, token_id: str) -> TokenInfo:
        """Get token info.
        
        Gets information about a token, specified by its ID.
        
        :param token_id: str
          The ID of the token to get.
        
        :returns: :class:`TokenInfo`
        """

        headers = {'Accept': 'application/json', }
        res = self._api.do('GET', f'/api/2.0/token-management/tokens/{token_id}', headers=headers)
        return TokenInfo.from_dict(res)

    def get_permission_levels(self) -> GetTokenPermissionLevelsResponse:
        """Get token permission levels.
        
        Gets the permission levels that a user can have on an object.
        
        :returns: :class:`GetTokenPermissionLevelsResponse`
        """

        headers = {'Accept': 'application/json', }
        res = self._api.do('GET',
                           '/api/2.0/permissions/authorization/tokens/permissionLevels',
                           headers=headers)
        return GetTokenPermissionLevelsResponse.from_dict(res)

    def get_permissions(self) -> TokenPermissions:
        """Get token permissions.
        
        Gets the permissions of all tokens. Tokens can inherit permissions from their root object.
        
        :returns: :class:`TokenPermissions`
        """

        headers = {'Accept': 'application/json', }
        res = self._api.do('GET', '/api/2.0/permissions/authorization/tokens', headers=headers)
        return TokenPermissions.from_dict(res)

    def list(self,
             *,
             created_by_id: Optional[str] = None,
             created_by_username: Optional[str] = None) -> Iterator[TokenInfo]:
        """List all tokens.
        
        Lists all tokens associated with the specified workspace or user.
        
        :param created_by_id: str (optional)
          User ID of the user that created the token.
        :param created_by_username: str (optional)
          Username of the user that created the token.
        
        :returns: Iterator over :class:`TokenInfo`
        """

        query = {}
        if created_by_id is not None: query['created_by_id'] = created_by_id
        if created_by_username is not None: query['created_by_username'] = created_by_username
        headers = {'Accept': 'application/json', }
        json = self._api.do('GET', '/api/2.0/token-management/tokens', query=query, headers=headers)
        parsed = ListTokensResponse.from_dict(json).token_infos
        return parsed if parsed is not None else []

    def set_permissions(
            self,
            *,
            access_control_list: Optional[List[TokenAccessControlRequest]] = None) -> TokenPermissions:
        """Set token permissions.
        
        Sets permissions on all tokens. Tokens can inherit permissions from their root object.
        
        :param access_control_list: List[:class:`TokenAccessControlRequest`] (optional)
        
        :returns: :class:`TokenPermissions`
        """
        body = {}
        if access_control_list is not None:
            body['access_control_list'] = [v.as_dict() for v in access_control_list]
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        res = self._api.do('PUT', '/api/2.0/permissions/authorization/tokens', body=body, headers=headers)
        return TokenPermissions.from_dict(res)

    def update_permissions(
            self,
            *,
            access_control_list: Optional[List[TokenAccessControlRequest]] = None) -> TokenPermissions:
        """Update token permissions.
        
        Updates the permissions on all tokens. Tokens can inherit permissions from their root object.
        
        :param access_control_list: List[:class:`TokenAccessControlRequest`] (optional)
        
        :returns: :class:`TokenPermissions`
        """
        body = {}
        if access_control_list is not None:
            body['access_control_list'] = [v.as_dict() for v in access_control_list]
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        res = self._api.do('PATCH', '/api/2.0/permissions/authorization/tokens', body=body, headers=headers)
        return TokenPermissions.from_dict(res)


class TokensAPI:
    """The Token API allows you to create, list, and revoke tokens that can be used to authenticate and access
    Databricks REST APIs."""

    def __init__(self, api_client):
        self._api = api_client

    def create(self,
               *,
               comment: Optional[str] = None,
               lifetime_seconds: Optional[int] = None) -> CreateTokenResponse:
        """Create a user token.
        
        Creates and returns a token for a user. If this call is made through token authentication, it creates
        a token with the same client ID as the authenticated token. If the user's token quota is exceeded,
        this call returns an error **QUOTA_EXCEEDED**.
        
        :param comment: str (optional)
          Optional description to attach to the token.
        :param lifetime_seconds: int (optional)
          The lifetime of the token, in seconds.
          
          If the ifetime is not specified, this token remains valid indefinitely.
        
        :returns: :class:`CreateTokenResponse`
        """
        body = {}
        if comment is not None: body['comment'] = comment
        if lifetime_seconds is not None: body['lifetime_seconds'] = lifetime_seconds
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        res = self._api.do('POST', '/api/2.0/token/create', body=body, headers=headers)
        return CreateTokenResponse.from_dict(res)

    def delete(self, token_id: str):
        """Revoke token.
        
        Revokes an access token.
        
        If a token with the specified ID is not valid, this call returns an error **RESOURCE_DOES_NOT_EXIST**.
        
        :param token_id: str
          The ID of the token to be revoked.
        
        
        """
        body = {}
        if token_id is not None: body['token_id'] = token_id
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        self._api.do('POST', '/api/2.0/token/delete', body=body, headers=headers)

    def list(self) -> Iterator[TokenInfo]:
        """List tokens.
        
        Lists all the valid tokens for a user-workspace pair.
        
        :returns: Iterator over :class:`TokenInfo`
        """

        headers = {'Accept': 'application/json', }
        json = self._api.do('GET', '/api/2.0/token/list', headers=headers)
        parsed = ListTokensResponse.from_dict(json).token_infos
        return parsed if parsed is not None else []


class WorkspaceConfAPI:
    """This API allows updating known workspace settings for advanced users."""

    def __init__(self, api_client):
        self._api = api_client

    def get_status(self, keys: str) -> WorkspaceConf:
        """Check configuration status.
        
        Gets the configuration status for a workspace.
        
        :param keys: str
        
        :returns: Dict[str,str]
        """

        query = {}
        if keys is not None: query['keys'] = keys
        headers = {'Accept': 'application/json', }
        res = self._api.do('GET', '/api/2.0/workspace-conf', query=query, headers=headers)
        return WorkspaceConf.from_dict(res)

    def set_status(self):
        """Enable/disable features.
        
        Sets the configuration status for a workspace, including enabling or disabling it.
        
        
        
        """

        headers = {'Content-Type': 'application/json', }
        self._api.do('PATCH', '/api/2.0/workspace-conf', headers=headers)
