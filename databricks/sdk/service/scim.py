# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

from dataclasses import dataclass
from enum import Enum
from typing import Optional, Dict, List

__all__ = [
    
    'ComplexValue',
    'DeleteGroupRequest',
    'DeleteServicePrincipalRequest',
    'DeleteUserRequest',
    'FetchGroupRequest',
    'FetchServicePrincipalRequest',
    'FetchUserRequest',
    'Group',
    'ListGroupsRequest',
    'ListGroupsResponse',
    'ListGroupsSortOrder',
    'ListServicePrincipalResponse',
    'ListServicePrincipalsRequest',
    'ListServicePrincipalsSortOrder',
    'ListUsersRequest',
    'ListUsersResponse',
    'ListUsersSortOrder',
    'Name',
    'PartialUpdate',
    'Patch',
    'PatchOp',
    'ServicePrincipal',
    'User',
    
    'CurrentUser',
    'Groups',
    'ServicePrincipals',
    'Users',
]

# all definitions in this file are in alphabetical order

@dataclass
class ComplexValue:
    
    
    display: str = None
    
    primary: bool = None
    
    type: str = None
    
    value: str = None

    def as_request(self) -> (dict, dict):
        complexValue_query, complexValue_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.display:
            complexValue_body['display'] = self.display
        if self.primary:
            complexValue_body['primary'] = self.primary
        if self.type:
            complexValue_body['type'] = self.type
        if self.value:
            complexValue_body['value'] = self.value
        
        return complexValue_query, complexValue_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ComplexValue':
        return cls(
            display=d.get('display', None),
            primary=d.get('primary', None),
            type=d.get('type', None),
            value=d.get('value', None),
        )



@dataclass
class DeleteGroupRequest:
    
    # Unique ID for a group in the <Workspace>.
    id: str # path

    def as_request(self) -> (dict, dict):
        deleteGroupRequest_query, deleteGroupRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.id:
            deleteGroupRequest_body['id'] = self.id
        
        return deleteGroupRequest_query, deleteGroupRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'DeleteGroupRequest':
        return cls(
            id=d.get('id', None),
        )



@dataclass
class DeleteServicePrincipalRequest:
    
    # Unique ID for a service principal in the <Workspace>.
    id: str # path

    def as_request(self) -> (dict, dict):
        deleteServicePrincipalRequest_query, deleteServicePrincipalRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.id:
            deleteServicePrincipalRequest_body['id'] = self.id
        
        return deleteServicePrincipalRequest_query, deleteServicePrincipalRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'DeleteServicePrincipalRequest':
        return cls(
            id=d.get('id', None),
        )



@dataclass
class DeleteUserRequest:
    
    # Unique ID for a user in the <Workspace>.
    id: str # path

    def as_request(self) -> (dict, dict):
        deleteUserRequest_query, deleteUserRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.id:
            deleteUserRequest_body['id'] = self.id
        
        return deleteUserRequest_query, deleteUserRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'DeleteUserRequest':
        return cls(
            id=d.get('id', None),
        )



@dataclass
class FetchGroupRequest:
    
    # Unique ID for a group in the <Workspace>.
    id: str # path

    def as_request(self) -> (dict, dict):
        fetchGroupRequest_query, fetchGroupRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.id:
            fetchGroupRequest_body['id'] = self.id
        
        return fetchGroupRequest_query, fetchGroupRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'FetchGroupRequest':
        return cls(
            id=d.get('id', None),
        )



@dataclass
class FetchServicePrincipalRequest:
    
    # Unique ID for a service principal in the <Workspace>.
    id: str # path

    def as_request(self) -> (dict, dict):
        fetchServicePrincipalRequest_query, fetchServicePrincipalRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.id:
            fetchServicePrincipalRequest_body['id'] = self.id
        
        return fetchServicePrincipalRequest_query, fetchServicePrincipalRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'FetchServicePrincipalRequest':
        return cls(
            id=d.get('id', None),
        )



@dataclass
class FetchUserRequest:
    
    # Unique ID for a user in the <Workspace>.
    id: str # path

    def as_request(self) -> (dict, dict):
        fetchUserRequest_query, fetchUserRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.id:
            fetchUserRequest_body['id'] = self.id
        
        return fetchUserRequest_query, fetchUserRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'FetchUserRequest':
        return cls(
            id=d.get('id', None),
        )



@dataclass
class Group:
    
    # String that represents a human-readable group name
    displayName: str = None
    
    entitlements: 'List[ComplexValue]' = None
    
    externalId: str = None
    
    groups: 'List[ComplexValue]' = None
    # Databricks group ID
    id: str = None
    
    members: 'List[ComplexValue]' = None
    
    roles: 'List[ComplexValue]' = None

    def as_request(self) -> (dict, dict):
        group_query, group_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.displayName:
            group_body['displayName'] = self.displayName
        if self.entitlements:
            group_body['entitlements'] = [v.as_request()[1] for v in self.entitlements]
        if self.externalId:
            group_body['externalId'] = self.externalId
        if self.groups:
            group_body['groups'] = [v.as_request()[1] for v in self.groups]
        if self.id:
            group_body['id'] = self.id
        if self.members:
            group_body['members'] = [v.as_request()[1] for v in self.members]
        if self.roles:
            group_body['roles'] = [v.as_request()[1] for v in self.roles]
        
        return group_query, group_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Group':
        return cls(
            displayName=d.get('displayName', None),
            entitlements=[ComplexValue.from_dict(v) for v in d['entitlements']] if 'entitlements' in d else None,
            externalId=d.get('externalId', None),
            groups=[ComplexValue.from_dict(v) for v in d['groups']] if 'groups' in d else None,
            id=d.get('id', None),
            members=[ComplexValue.from_dict(v) for v in d['members']] if 'members' in d else None,
            roles=[ComplexValue.from_dict(v) for v in d['roles']] if 'roles' in d else None,
        )



@dataclass
class ListGroupsRequest:
    
    # Comma-separated list of attributes to return in response.
    attributes: str = None # query
    # Desired number of results per page.
    count: int = None # query
    # Comma-separated list of attributes to exclude in response.
    excludedAttributes: str = None # query
    # Query by which the results have to be filtered. Supported operators are
    # equals(`eq`), contains(`co`), starts with(`sw`) and not equals(`ne`).
    # Additionally, simple expressions can be formed using logical operators -
    # `and` and `or`. The [SCIM
    # RFC](https://tools.ietf.org/html/rfc7644#section-3.4.2.2) has more details
    # but we currently only support simple expressions.
    filter: str = None # query
    # Attribute to sort the results.
    sortBy: str = None # query
    # The order to sort the results.
    sortOrder: 'ListGroupsSortOrder' = None # query
    # Specifies the index of the first result. First item is number 1.
    startIndex: int = None # query

    def as_request(self) -> (dict, dict):
        listGroupsRequest_query, listGroupsRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.attributes:
            listGroupsRequest_query['attributes'] = self.attributes
        if self.count:
            listGroupsRequest_query['count'] = self.count
        if self.excludedAttributes:
            listGroupsRequest_query['excludedAttributes'] = self.excludedAttributes
        if self.filter:
            listGroupsRequest_query['filter'] = self.filter
        if self.sortBy:
            listGroupsRequest_query['sortBy'] = self.sortBy
        if self.sortOrder:
            listGroupsRequest_query['sortOrder'] = self.sortOrder.value
        if self.startIndex:
            listGroupsRequest_query['startIndex'] = self.startIndex
        
        return listGroupsRequest_query, listGroupsRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListGroupsRequest':
        return cls(
            attributes=d.get('attributes', None),
            count=d.get('count', None),
            excludedAttributes=d.get('excludedAttributes', None),
            filter=d.get('filter', None),
            sortBy=d.get('sortBy', None),
            sortOrder=ListGroupsSortOrder(d['sortOrder']) if 'sortOrder' in d else None,
            startIndex=d.get('startIndex', None),
        )



@dataclass
class ListGroupsResponse:
    
    # User objects returned in the response.
    Resources: 'List[Group]' = None
    # Total results returned in the response.
    itemsPerPage: int = None
    # Starting index of all the results that matched the request filters. First
    # item is number 1.
    startIndex: int = None
    # Total results that match the request filters.
    totalResults: int = None

    def as_request(self) -> (dict, dict):
        listGroupsResponse_query, listGroupsResponse_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.Resources:
            listGroupsResponse_body['Resources'] = [v.as_request()[1] for v in self.Resources]
        if self.itemsPerPage:
            listGroupsResponse_body['itemsPerPage'] = self.itemsPerPage
        if self.startIndex:
            listGroupsResponse_body['startIndex'] = self.startIndex
        if self.totalResults:
            listGroupsResponse_body['totalResults'] = self.totalResults
        
        return listGroupsResponse_query, listGroupsResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListGroupsResponse':
        return cls(
            Resources=[Group.from_dict(v) for v in d['Resources']] if 'Resources' in d else None,
            itemsPerPage=d.get('itemsPerPage', None),
            startIndex=d.get('startIndex', None),
            totalResults=d.get('totalResults', None),
        )



class ListGroupsSortOrder(Enum):
    
    
    ascending = 'ascending'
    descending = 'descending'

@dataclass
class ListServicePrincipalResponse:
    
    # User objects returned in the response.
    Resources: 'List[ServicePrincipal]' = None
    # Total results returned in the response.
    itemsPerPage: int = None
    # Starting index of all the results that matched the request filters. First
    # item is number 1.
    startIndex: int = None
    # Total results that match the request filters.
    totalResults: int = None

    def as_request(self) -> (dict, dict):
        listServicePrincipalResponse_query, listServicePrincipalResponse_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.Resources:
            listServicePrincipalResponse_body['Resources'] = [v.as_request()[1] for v in self.Resources]
        if self.itemsPerPage:
            listServicePrincipalResponse_body['itemsPerPage'] = self.itemsPerPage
        if self.startIndex:
            listServicePrincipalResponse_body['startIndex'] = self.startIndex
        if self.totalResults:
            listServicePrincipalResponse_body['totalResults'] = self.totalResults
        
        return listServicePrincipalResponse_query, listServicePrincipalResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListServicePrincipalResponse':
        return cls(
            Resources=[ServicePrincipal.from_dict(v) for v in d['Resources']] if 'Resources' in d else None,
            itemsPerPage=d.get('itemsPerPage', None),
            startIndex=d.get('startIndex', None),
            totalResults=d.get('totalResults', None),
        )



@dataclass
class ListServicePrincipalsRequest:
    
    # Comma-separated list of attributes to return in response.
    attributes: str = None # query
    # Desired number of results per page.
    count: int = None # query
    # Comma-separated list of attributes to exclude in response.
    excludedAttributes: str = None # query
    # Query by which the results have to be filtered. Supported operators are
    # equals(`eq`), contains(`co`), starts with(`sw`) and not equals(`ne`).
    # Additionally, simple expressions can be formed using logical operators -
    # `and` and `or`. The [SCIM
    # RFC](https://tools.ietf.org/html/rfc7644#section-3.4.2.2) has more details
    # but we currently only support simple expressions.
    filter: str = None # query
    # Attribute to sort the results.
    sortBy: str = None # query
    # The order to sort the results.
    sortOrder: 'ListServicePrincipalsSortOrder' = None # query
    # Specifies the index of the first result. First item is number 1.
    startIndex: int = None # query

    def as_request(self) -> (dict, dict):
        listServicePrincipalsRequest_query, listServicePrincipalsRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.attributes:
            listServicePrincipalsRequest_query['attributes'] = self.attributes
        if self.count:
            listServicePrincipalsRequest_query['count'] = self.count
        if self.excludedAttributes:
            listServicePrincipalsRequest_query['excludedAttributes'] = self.excludedAttributes
        if self.filter:
            listServicePrincipalsRequest_query['filter'] = self.filter
        if self.sortBy:
            listServicePrincipalsRequest_query['sortBy'] = self.sortBy
        if self.sortOrder:
            listServicePrincipalsRequest_query['sortOrder'] = self.sortOrder.value
        if self.startIndex:
            listServicePrincipalsRequest_query['startIndex'] = self.startIndex
        
        return listServicePrincipalsRequest_query, listServicePrincipalsRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListServicePrincipalsRequest':
        return cls(
            attributes=d.get('attributes', None),
            count=d.get('count', None),
            excludedAttributes=d.get('excludedAttributes', None),
            filter=d.get('filter', None),
            sortBy=d.get('sortBy', None),
            sortOrder=ListServicePrincipalsSortOrder(d['sortOrder']) if 'sortOrder' in d else None,
            startIndex=d.get('startIndex', None),
        )



class ListServicePrincipalsSortOrder(Enum):
    
    
    ascending = 'ascending'
    descending = 'descending'

@dataclass
class ListUsersRequest:
    
    # Comma-separated list of attributes to return in response.
    attributes: str = None # query
    # Desired number of results per page.
    count: int = None # query
    # Comma-separated list of attributes to exclude in response.
    excludedAttributes: str = None # query
    # Query by which the results have to be filtered. Supported operators are
    # equals(`eq`), contains(`co`), starts with(`sw`) and not equals(`ne`).
    # Additionally, simple expressions can be formed using logical operators -
    # `and` and `or`. The [SCIM
    # RFC](https://tools.ietf.org/html/rfc7644#section-3.4.2.2) has more details
    # but we currently only support simple expressions.
    filter: str = None # query
    # Attribute to sort the results. Multi-part paths are supported. For
    # example, `userName`, `name.givenName`, and `emails`.
    sortBy: str = None # query
    # The order to sort the results.
    sortOrder: 'ListUsersSortOrder' = None # query
    # Specifies the index of the first result. First item is number 1.
    startIndex: int = None # query

    def as_request(self) -> (dict, dict):
        listUsersRequest_query, listUsersRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.attributes:
            listUsersRequest_query['attributes'] = self.attributes
        if self.count:
            listUsersRequest_query['count'] = self.count
        if self.excludedAttributes:
            listUsersRequest_query['excludedAttributes'] = self.excludedAttributes
        if self.filter:
            listUsersRequest_query['filter'] = self.filter
        if self.sortBy:
            listUsersRequest_query['sortBy'] = self.sortBy
        if self.sortOrder:
            listUsersRequest_query['sortOrder'] = self.sortOrder.value
        if self.startIndex:
            listUsersRequest_query['startIndex'] = self.startIndex
        
        return listUsersRequest_query, listUsersRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListUsersRequest':
        return cls(
            attributes=d.get('attributes', None),
            count=d.get('count', None),
            excludedAttributes=d.get('excludedAttributes', None),
            filter=d.get('filter', None),
            sortBy=d.get('sortBy', None),
            sortOrder=ListUsersSortOrder(d['sortOrder']) if 'sortOrder' in d else None,
            startIndex=d.get('startIndex', None),
        )



@dataclass
class ListUsersResponse:
    
    # User objects returned in the response.
    Resources: 'List[User]' = None
    # Total results returned in the response.
    itemsPerPage: int = None
    # Starting index of all the results that matched the request filters. First
    # item is number 1.
    startIndex: int = None
    # Total results that match the request filters.
    totalResults: int = None

    def as_request(self) -> (dict, dict):
        listUsersResponse_query, listUsersResponse_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.Resources:
            listUsersResponse_body['Resources'] = [v.as_request()[1] for v in self.Resources]
        if self.itemsPerPage:
            listUsersResponse_body['itemsPerPage'] = self.itemsPerPage
        if self.startIndex:
            listUsersResponse_body['startIndex'] = self.startIndex
        if self.totalResults:
            listUsersResponse_body['totalResults'] = self.totalResults
        
        return listUsersResponse_query, listUsersResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListUsersResponse':
        return cls(
            Resources=[User.from_dict(v) for v in d['Resources']] if 'Resources' in d else None,
            itemsPerPage=d.get('itemsPerPage', None),
            startIndex=d.get('startIndex', None),
            totalResults=d.get('totalResults', None),
        )



class ListUsersSortOrder(Enum):
    
    
    ascending = 'ascending'
    descending = 'descending'

@dataclass
class Name:
    
    # Family name of the Databricks user.
    familyName: str = None
    # Given name of the Databricks user.
    givenName: str = None

    def as_request(self) -> (dict, dict):
        name_query, name_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.familyName:
            name_body['familyName'] = self.familyName
        if self.givenName:
            name_body['givenName'] = self.givenName
        
        return name_query, name_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Name':
        return cls(
            familyName=d.get('familyName', None),
            givenName=d.get('givenName', None),
        )



@dataclass
class PartialUpdate:
    
    # Unique ID for a group in the <Workspace>.
    id: str # path
    
    operations: 'List[Patch]' = None

    def as_request(self) -> (dict, dict):
        partialUpdate_query, partialUpdate_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.id:
            partialUpdate_body['id'] = self.id
        if self.operations:
            partialUpdate_body['operations'] = [v.as_request()[1] for v in self.operations]
        
        return partialUpdate_query, partialUpdate_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'PartialUpdate':
        return cls(
            id=d.get('id', None),
            operations=[Patch.from_dict(v) for v in d['operations']] if 'operations' in d else None,
        )



@dataclass
class Patch:
    
    # Type of patch operation.
    op: 'PatchOp' = None
    # Selection of patch operation
    path: str = None
    # Value to modify
    value: str = None

    def as_request(self) -> (dict, dict):
        patch_query, patch_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.op:
            patch_body['op'] = self.op.value
        if self.path:
            patch_body['path'] = self.path
        if self.value:
            patch_body['value'] = self.value
        
        return patch_query, patch_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Patch':
        return cls(
            op=PatchOp(d['op']) if 'op' in d else None,
            path=d.get('path', None),
            value=d.get('value', None),
        )



class PatchOp(Enum):
    """Type of patch operation."""
    
    add = 'add'
    remove = 'remove'
    replace = 'replace'

@dataclass
class ServicePrincipal:
    
    # If this user is active
    active: bool = None
    # UUID relating to the service principal
    applicationId: str = None
    # String that represents a concatenation of given and family names. For
    # example `John Smith`.
    displayName: str = None
    
    entitlements: 'List[ComplexValue]' = None
    
    externalId: str = None
    
    groups: 'List[ComplexValue]' = None
    # Databricks service principal ID.
    id: str = None
    
    roles: 'List[ComplexValue]' = None

    def as_request(self) -> (dict, dict):
        servicePrincipal_query, servicePrincipal_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.active:
            servicePrincipal_body['active'] = self.active
        if self.applicationId:
            servicePrincipal_body['applicationId'] = self.applicationId
        if self.displayName:
            servicePrincipal_body['displayName'] = self.displayName
        if self.entitlements:
            servicePrincipal_body['entitlements'] = [v.as_request()[1] for v in self.entitlements]
        if self.externalId:
            servicePrincipal_body['externalId'] = self.externalId
        if self.groups:
            servicePrincipal_body['groups'] = [v.as_request()[1] for v in self.groups]
        if self.id:
            servicePrincipal_body['id'] = self.id
        if self.roles:
            servicePrincipal_body['roles'] = [v.as_request()[1] for v in self.roles]
        
        return servicePrincipal_query, servicePrincipal_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ServicePrincipal':
        return cls(
            active=d.get('active', None),
            applicationId=d.get('applicationId', None),
            displayName=d.get('displayName', None),
            entitlements=[ComplexValue.from_dict(v) for v in d['entitlements']] if 'entitlements' in d else None,
            externalId=d.get('externalId', None),
            groups=[ComplexValue.from_dict(v) for v in d['groups']] if 'groups' in d else None,
            id=d.get('id', None),
            roles=[ComplexValue.from_dict(v) for v in d['roles']] if 'roles' in d else None,
        )



@dataclass
class User:
    
    # If this user is active
    active: bool = None
    # String that represents a concatenation of given and family names. For
    # example `John Smith`.
    displayName: str = None
    # All the emails associated with the Databricks user.
    emails: 'List[ComplexValue]' = None
    
    entitlements: 'List[ComplexValue]' = None
    
    externalId: str = None
    
    groups: 'List[ComplexValue]' = None
    # Databricks user ID.
    id: str = None
    
    name: 'Name' = None
    
    roles: 'List[ComplexValue]' = None
    # Email address of the Databricks user.
    userName: str = None

    def as_request(self) -> (dict, dict):
        user_query, user_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.active:
            user_body['active'] = self.active
        if self.displayName:
            user_body['displayName'] = self.displayName
        if self.emails:
            user_body['emails'] = [v.as_request()[1] for v in self.emails]
        if self.entitlements:
            user_body['entitlements'] = [v.as_request()[1] for v in self.entitlements]
        if self.externalId:
            user_body['externalId'] = self.externalId
        if self.groups:
            user_body['groups'] = [v.as_request()[1] for v in self.groups]
        if self.id:
            user_body['id'] = self.id
        if self.name:
            user_body['name'] = self.name.as_request()[1]
        if self.roles:
            user_body['roles'] = [v.as_request()[1] for v in self.roles]
        if self.userName:
            user_body['userName'] = self.userName
        
        return user_query, user_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'User':
        return cls(
            active=d.get('active', None),
            displayName=d.get('displayName', None),
            emails=[ComplexValue.from_dict(v) for v in d['emails']] if 'emails' in d else None,
            entitlements=[ComplexValue.from_dict(v) for v in d['entitlements']] if 'entitlements' in d else None,
            externalId=d.get('externalId', None),
            groups=[ComplexValue.from_dict(v) for v in d['groups']] if 'groups' in d else None,
            id=d.get('id', None),
            name=Name.from_dict(d['name']) if 'name' in d else None,
            roles=[ComplexValue.from_dict(v) for v in d['roles']] if 'roles' in d else None,
            userName=d.get('userName', None),
        )



class CurrentUserAPI:
    def __init__(self, api_client):
        self._api = api_client
    
    def me(self) -> User:
        """Fetch details about caller identity
        
        Get details about caller identity"""
        
        json = self._api.do('GET', '/api/2.0/preview/scim/v2/Me')
        return User.from_dict(json)
    
class GroupsAPI:
    def __init__(self, api_client):
        self._api = api_client
    
    def deleteGroup(self, request: DeleteGroupRequest):
        """Delete a group in <Workspace>
        
        Remove a group in the <Workspace>."""
        query, body = request.as_request()
        self._api.do('DELETE', f'/api/2.0/preview/scim/v2/Groups/{request.id}', query=query, body=body)
        
    
    def fetchGroup(self, request: FetchGroupRequest) -> Group:
        """Fetch details of a group in <Workspace>
        
        Fetch information of one group in the <Workspace>"""
        query, body = request.as_request()
        json = self._api.do('GET', f'/api/2.0/preview/scim/v2/Groups/{request.id}', query=query, body=body)
        return Group.from_dict(json)
    
    def listGroups(self, request: ListGroupsRequest) -> ListGroupsResponse:
        """Fetch details of multiple groups in <Workspace>
        
        Get all details of the groups associated with the <Workspace>."""
        query, body = request.as_request()
        json = self._api.do('GET', '/api/2.0/preview/scim/v2/Groups', query=query, body=body)
        return ListGroupsResponse.from_dict(json)
    
    def newGroup(self, request: Group) -> Group:
        """Create a new group in <Workspace>
        
        Create one group in the <Workspace> with a unique name"""
        query, body = request.as_request()
        json = self._api.do('POST', '/api/2.0/preview/scim/v2/Groups', query=query, body=body)
        return Group.from_dict(json)
    
    def patchGroup(self, request: PartialUpdate):
        """Update details of a group
        
        Partially update details of a group"""
        query, body = request.as_request()
        self._api.do('PATCH', f'/api/2.0/preview/scim/v2/Groups/{request.id}', query=query, body=body)
        
    
    def replaceGroup(self, request: Group):
        """Update details of a group
        
        Update details of a group by replacing the entire entity"""
        query, body = request.as_request()
        self._api.do('PUT', f'/api/2.0/preview/scim/v2/Groups/{request.id}', query=query, body=body)
        
    
class ServicePrincipalsAPI:
    def __init__(self, api_client):
        self._api = api_client
    
    def deleteServicePrincipal(self, request: DeleteServicePrincipalRequest):
        """Delete a service principal in <Workspace>
        
        Delete one service principal"""
        query, body = request.as_request()
        self._api.do('DELETE', f'/api/2.0/preview/scim/v2/ServicePrincipals/{request.id}', query=query, body=body)
        
    
    def fetchServicePrincipal(self, request: FetchServicePrincipalRequest) -> ServicePrincipal:
        """Fetch details of a service principal in <Workspace>
        
        Fetch information of one service principal"""
        query, body = request.as_request()
        json = self._api.do('GET', f'/api/2.0/preview/scim/v2/ServicePrincipals/{request.id}', query=query, body=body)
        return ServicePrincipal.from_dict(json)
    
    def listServicePrincipals(self, request: ListServicePrincipalsRequest) -> ListServicePrincipalResponse:
        """Fetch details of multiple service principals in <Workspace>
        
        Get multiple service principals associated with a <Workspace>."""
        query, body = request.as_request()
        json = self._api.do('GET', '/api/2.0/preview/scim/v2/ServicePrincipals', query=query, body=body)
        return ListServicePrincipalResponse.from_dict(json)
    
    def newServicePrincipal(self, request: ServicePrincipal) -> ServicePrincipal:
        """Create a new service principal in <Workspace>
        
        Create one service principal in the <Workspace>."""
        query, body = request.as_request()
        json = self._api.do('POST', '/api/2.0/preview/scim/v2/ServicePrincipals', query=query, body=body)
        return ServicePrincipal.from_dict(json)
    
    def patchServicePrincipal(self, request: PartialUpdate):
        """Update details of a service principal in <Workspace>
        
        Partially update details of one service principal."""
        query, body = request.as_request()
        self._api.do('PATCH', f'/api/2.0/preview/scim/v2/ServicePrincipals/{request.id}', query=query, body=body)
        
    
    def replaceServicePrincipal(self, request: ServicePrincipal):
        """Replace service principal in <Workspace>
        
        Update details of one service principal."""
        query, body = request.as_request()
        self._api.do('PUT', f'/api/2.0/preview/scim/v2/ServicePrincipals/{request.id}', query=query, body=body)
        
    
class UsersAPI:
    def __init__(self, api_client):
        self._api = api_client
    
    def deleteUser(self, request: DeleteUserRequest):
        """Delete a user in <Workspace>
        
        Delete one user. Deleting a user from a workspace also removes objects
        associated with the user."""
        query, body = request.as_request()
        self._api.do('DELETE', f'/api/2.0/preview/scim/v2/Users/{request.id}', query=query, body=body)
        
    
    def fetchUser(self, request: FetchUserRequest) -> User:
        """Get details of a user in <Workspace>
        
        Fetch information of one user in <Workspace>"""
        query, body = request.as_request()
        json = self._api.do('GET', f'/api/2.0/preview/scim/v2/Users/{request.id}', query=query, body=body)
        return User.from_dict(json)
    
    def listUsers(self, request: ListUsersRequest) -> ListUsersResponse:
        """Fetch details of multiple users in <Workspace>
        
        Get all the users associated with a <Workspace>."""
        query, body = request.as_request()
        json = self._api.do('GET', '/api/2.0/preview/scim/v2/Users', query=query, body=body)
        return ListUsersResponse.from_dict(json)
    
    def newUser(self, request: User) -> User:
        """Create a new user in <Workspace>
        
        Create a user in the <Workspace> who will automatically added to the
        account."""
        query, body = request.as_request()
        json = self._api.do('POST', '/api/2.0/preview/scim/v2/Users', query=query, body=body)
        return User.from_dict(json)
    
    def patchUser(self, request: PartialUpdate):
        """Update details of a user in <Workspace>
        
        Partially update a user resource with operations on specific attributes"""
        query, body = request.as_request()
        self._api.do('PATCH', f'/api/2.0/preview/scim/v2/Users/{request.id}', query=query, body=body)
        
    
    def replaceUser(self, request: User):
        """Update details of a user in <Workspace>
        
        Replaces user with the data supplied in request"""
        query, body = request.as_request()
        self._api.do('PUT', f'/api/2.0/preview/scim/v2/Users/{request.id}', query=query, body=body)
        
    