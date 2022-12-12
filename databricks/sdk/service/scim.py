# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

from dataclasses import dataclass
from enum import Enum
from typing import Optional, Dict, List, Any


# all definitions in this file are in alphabetical order


@dataclass
class ComplexValue:

    display: str

    primary: bool

    type: str

    value: str

    def as_request(self) -> (dict, dict):
        complexValue_query, complexValue_body = {}, {}
        if self.display:
            complexValue_body["display"] = self.display
        if self.primary:
            complexValue_body["primary"] = self.primary
        if self.type:
            complexValue_body["type"] = self.type
        if self.value:
            complexValue_body["value"] = self.value

        return complexValue_query, complexValue_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ComplexValue":
        return cls(
            display=d.get("display", None),
            primary=d.get("primary", None),
            type=d.get("type", None),
            value=d.get("value", None),
        )


@dataclass
class DeleteGroupRequest:
    """Delete a group"""

    # Unique ID for a group in the Databricks Account.
    id: str  # path

    def as_request(self) -> (dict, dict):
        deleteGroupRequest_query, deleteGroupRequest_body = {}, {}
        if self.id:
            deleteGroupRequest_body["id"] = self.id

        return deleteGroupRequest_query, deleteGroupRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "DeleteGroupRequest":
        return cls(
            id=d.get("id", None),
        )


@dataclass
class DeleteServicePrincipalRequest:
    """Delete a service principal"""

    # Unique ID for a service principal in the Databricks Account.
    id: str  # path

    def as_request(self) -> (dict, dict):
        deleteServicePrincipalRequest_query, deleteServicePrincipalRequest_body = {}, {}
        if self.id:
            deleteServicePrincipalRequest_body["id"] = self.id

        return deleteServicePrincipalRequest_query, deleteServicePrincipalRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "DeleteServicePrincipalRequest":
        return cls(
            id=d.get("id", None),
        )


@dataclass
class DeleteUserRequest:
    """Delete a user"""

    # Unique ID for a user in the Databricks Account.
    id: str  # path

    def as_request(self) -> (dict, dict):
        deleteUserRequest_query, deleteUserRequest_body = {}, {}
        if self.id:
            deleteUserRequest_body["id"] = self.id

        return deleteUserRequest_query, deleteUserRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "DeleteUserRequest":
        return cls(
            id=d.get("id", None),
        )


@dataclass
class GetGroupRequest:
    """Get group details"""

    # Unique ID for a group in the Databricks Account.
    id: str  # path

    def as_request(self) -> (dict, dict):
        getGroupRequest_query, getGroupRequest_body = {}, {}
        if self.id:
            getGroupRequest_body["id"] = self.id

        return getGroupRequest_query, getGroupRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "GetGroupRequest":
        return cls(
            id=d.get("id", None),
        )


@dataclass
class GetServicePrincipalRequest:
    """Get service principal details"""

    # Unique ID for a service principal in the Databricks Account.
    id: str  # path

    def as_request(self) -> (dict, dict):
        getServicePrincipalRequest_query, getServicePrincipalRequest_body = {}, {}
        if self.id:
            getServicePrincipalRequest_body["id"] = self.id

        return getServicePrincipalRequest_query, getServicePrincipalRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "GetServicePrincipalRequest":
        return cls(
            id=d.get("id", None),
        )


@dataclass
class GetUserRequest:
    """Get user details"""

    # Unique ID for a user in the Databricks Account.
    id: str  # path

    def as_request(self) -> (dict, dict):
        getUserRequest_query, getUserRequest_body = {}, {}
        if self.id:
            getUserRequest_body["id"] = self.id

        return getUserRequest_query, getUserRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "GetUserRequest":
        return cls(
            id=d.get("id", None),
        )


@dataclass
class Group:

    # String that represents a human-readable group name
    displayName: str

    entitlements: "List[ComplexValue]"

    externalId: str

    groups: "List[ComplexValue]"
    # Databricks group ID
    id: str  # path

    members: "List[ComplexValue]"

    roles: "List[ComplexValue]"

    def as_request(self) -> (dict, dict):
        group_query, group_body = {}, {}
        if self.displayName:
            group_body["displayName"] = self.displayName
        if self.entitlements:
            group_body["entitlements"] = [v.as_request()[1] for v in self.entitlements]
        if self.externalId:
            group_body["externalId"] = self.externalId
        if self.groups:
            group_body["groups"] = [v.as_request()[1] for v in self.groups]
        if self.id:
            group_body["id"] = self.id
        if self.members:
            group_body["members"] = [v.as_request()[1] for v in self.members]
        if self.roles:
            group_body["roles"] = [v.as_request()[1] for v in self.roles]

        return group_query, group_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "Group":
        return cls(
            displayName=d.get("displayName", None),
            entitlements=[ComplexValue.from_dict(v) for v in d["entitlements"]]
            if "entitlements" in d
            else None,
            externalId=d.get("externalId", None),
            groups=[ComplexValue.from_dict(v) for v in d["groups"]]
            if "groups" in d
            else None,
            id=d.get("id", None),
            members=[ComplexValue.from_dict(v) for v in d["members"]]
            if "members" in d
            else None,
            roles=[ComplexValue.from_dict(v) for v in d["roles"]]
            if "roles" in d
            else None,
        )


@dataclass
class ListGroupsRequest:
    """List group details"""

    # Comma-separated list of attributes to return in response.
    attributes: str  # query
    # Desired number of results per page.
    count: int  # query
    # Comma-separated list of attributes to exclude in response.
    excludedAttributes: str  # query
    # Query by which the results have to be filtered. Supported operators are
    # equals(`eq`), contains(`co`), starts with(`sw`) and not equals(`ne`).
    # Additionally, simple expressions can be formed using logical operators -
    # `and` and `or`. The [SCIM RFC] has more details but we currently only
    # support simple expressions.
    #
    # [SCIM RFC]: https://tools.ietf.org/html/rfc7644#section-3.4.2.2
    filter: str  # query
    # Attribute to sort the results.
    sortBy: str  # query
    # The order to sort the results.
    sortOrder: "ListSortOrder"  # query
    # Specifies the index of the first result. First item is number 1.
    startIndex: int  # query

    def as_request(self) -> (dict, dict):
        listGroupsRequest_query, listGroupsRequest_body = {}, {}
        if self.attributes:
            listGroupsRequest_query["attributes"] = self.attributes
        if self.count:
            listGroupsRequest_query["count"] = self.count
        if self.excludedAttributes:
            listGroupsRequest_query["excludedAttributes"] = self.excludedAttributes
        if self.filter:
            listGroupsRequest_query["filter"] = self.filter
        if self.sortBy:
            listGroupsRequest_query["sortBy"] = self.sortBy
        if self.sortOrder:
            listGroupsRequest_query["sortOrder"] = self.sortOrder.value
        if self.startIndex:
            listGroupsRequest_query["startIndex"] = self.startIndex

        return listGroupsRequest_query, listGroupsRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ListGroupsRequest":
        return cls(
            attributes=d.get("attributes", None),
            count=d.get("count", None),
            excludedAttributes=d.get("excludedAttributes", None),
            filter=d.get("filter", None),
            sortBy=d.get("sortBy", None),
            sortOrder=ListSortOrder(d["sortOrder"]) if "sortOrder" in d else None,
            startIndex=d.get("startIndex", None),
        )


@dataclass
class ListGroupsResponse:

    # Total results returned in the response.
    itemsPerPage: int
    # User objects returned in the response.
    Resources: "List[Group]"
    # Starting index of all the results that matched the request filters. First
    # item is number 1.
    startIndex: int
    # Total results that match the request filters.
    totalResults: int

    def as_request(self) -> (dict, dict):
        listGroupsResponse_query, listGroupsResponse_body = {}, {}
        if self.itemsPerPage:
            listGroupsResponse_body["itemsPerPage"] = self.itemsPerPage
        if self.Resources:
            listGroupsResponse_body["Resources"] = [
                v.as_request()[1] for v in self.Resources
            ]
        if self.startIndex:
            listGroupsResponse_body["startIndex"] = self.startIndex
        if self.totalResults:
            listGroupsResponse_body["totalResults"] = self.totalResults

        return listGroupsResponse_query, listGroupsResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ListGroupsResponse":
        return cls(
            itemsPerPage=d.get("itemsPerPage", None),
            Resources=[Group.from_dict(v) for v in d["Resources"]]
            if "Resources" in d
            else None,
            startIndex=d.get("startIndex", None),
            totalResults=d.get("totalResults", None),
        )


@dataclass
class ListServicePrincipalResponse:

    # Total results returned in the response.
    itemsPerPage: int
    # User objects returned in the response.
    Resources: "List[ServicePrincipal]"
    # Starting index of all the results that matched the request filters. First
    # item is number 1.
    startIndex: int
    # Total results that match the request filters.
    totalResults: int

    def as_request(self) -> (dict, dict):
        listServicePrincipalResponse_query, listServicePrincipalResponse_body = {}, {}
        if self.itemsPerPage:
            listServicePrincipalResponse_body["itemsPerPage"] = self.itemsPerPage
        if self.Resources:
            listServicePrincipalResponse_body["Resources"] = [
                v.as_request()[1] for v in self.Resources
            ]
        if self.startIndex:
            listServicePrincipalResponse_body["startIndex"] = self.startIndex
        if self.totalResults:
            listServicePrincipalResponse_body["totalResults"] = self.totalResults

        return listServicePrincipalResponse_query, listServicePrincipalResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ListServicePrincipalResponse":
        return cls(
            itemsPerPage=d.get("itemsPerPage", None),
            Resources=[ServicePrincipal.from_dict(v) for v in d["Resources"]]
            if "Resources" in d
            else None,
            startIndex=d.get("startIndex", None),
            totalResults=d.get("totalResults", None),
        )


@dataclass
class ListServicePrincipalsRequest:
    """List service principals"""

    # Comma-separated list of attributes to return in response.
    attributes: str  # query
    # Desired number of results per page.
    count: int  # query
    # Comma-separated list of attributes to exclude in response.
    excludedAttributes: str  # query
    # Query by which the results have to be filtered. Supported operators are
    # equals(`eq`), contains(`co`), starts with(`sw`) and not equals(`ne`).
    # Additionally, simple expressions can be formed using logical operators -
    # `and` and `or`. The [SCIM RFC] has more details but we currently only
    # support simple expressions.
    #
    # [SCIM RFC]: https://tools.ietf.org/html/rfc7644#section-3.4.2.2
    filter: str  # query
    # Attribute to sort the results.
    sortBy: str  # query
    # The order to sort the results.
    sortOrder: "ListSortOrder"  # query
    # Specifies the index of the first result. First item is number 1.
    startIndex: int  # query

    def as_request(self) -> (dict, dict):
        listServicePrincipalsRequest_query, listServicePrincipalsRequest_body = {}, {}
        if self.attributes:
            listServicePrincipalsRequest_query["attributes"] = self.attributes
        if self.count:
            listServicePrincipalsRequest_query["count"] = self.count
        if self.excludedAttributes:
            listServicePrincipalsRequest_query[
                "excludedAttributes"
            ] = self.excludedAttributes
        if self.filter:
            listServicePrincipalsRequest_query["filter"] = self.filter
        if self.sortBy:
            listServicePrincipalsRequest_query["sortBy"] = self.sortBy
        if self.sortOrder:
            listServicePrincipalsRequest_query["sortOrder"] = self.sortOrder.value
        if self.startIndex:
            listServicePrincipalsRequest_query["startIndex"] = self.startIndex

        return listServicePrincipalsRequest_query, listServicePrincipalsRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ListServicePrincipalsRequest":
        return cls(
            attributes=d.get("attributes", None),
            count=d.get("count", None),
            excludedAttributes=d.get("excludedAttributes", None),
            filter=d.get("filter", None),
            sortBy=d.get("sortBy", None),
            sortOrder=ListSortOrder(d["sortOrder"]) if "sortOrder" in d else None,
            startIndex=d.get("startIndex", None),
        )


class ListSortOrder(Enum):

    ascending = "ascending"
    descending = "descending"


@dataclass
class ListUsersRequest:
    """List users"""

    # Comma-separated list of attributes to return in response.
    attributes: str  # query
    # Desired number of results per page.
    count: int  # query
    # Comma-separated list of attributes to exclude in response.
    excludedAttributes: str  # query
    # Query by which the results have to be filtered. Supported operators are
    # equals(`eq`), contains(`co`), starts with(`sw`) and not equals(`ne`).
    # Additionally, simple expressions can be formed using logical operators -
    # `and` and `or`. The [SCIM RFC] has more details but we currently only
    # support simple expressions.
    #
    # [SCIM RFC]: https://tools.ietf.org/html/rfc7644#section-3.4.2.2
    filter: str  # query
    # Attribute to sort the results. Multi-part paths are supported. For
    # example, `userName`, `name.givenName`, and `emails`.
    sortBy: str  # query
    # The order to sort the results.
    sortOrder: "ListSortOrder"  # query
    # Specifies the index of the first result. First item is number 1.
    startIndex: int  # query

    def as_request(self) -> (dict, dict):
        listUsersRequest_query, listUsersRequest_body = {}, {}
        if self.attributes:
            listUsersRequest_query["attributes"] = self.attributes
        if self.count:
            listUsersRequest_query["count"] = self.count
        if self.excludedAttributes:
            listUsersRequest_query["excludedAttributes"] = self.excludedAttributes
        if self.filter:
            listUsersRequest_query["filter"] = self.filter
        if self.sortBy:
            listUsersRequest_query["sortBy"] = self.sortBy
        if self.sortOrder:
            listUsersRequest_query["sortOrder"] = self.sortOrder.value
        if self.startIndex:
            listUsersRequest_query["startIndex"] = self.startIndex

        return listUsersRequest_query, listUsersRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ListUsersRequest":
        return cls(
            attributes=d.get("attributes", None),
            count=d.get("count", None),
            excludedAttributes=d.get("excludedAttributes", None),
            filter=d.get("filter", None),
            sortBy=d.get("sortBy", None),
            sortOrder=ListSortOrder(d["sortOrder"]) if "sortOrder" in d else None,
            startIndex=d.get("startIndex", None),
        )


@dataclass
class ListUsersResponse:

    # Total results returned in the response.
    itemsPerPage: int
    # User objects returned in the response.
    Resources: "List[User]"
    # Starting index of all the results that matched the request filters. First
    # item is number 1.
    startIndex: int
    # Total results that match the request filters.
    totalResults: int

    def as_request(self) -> (dict, dict):
        listUsersResponse_query, listUsersResponse_body = {}, {}
        if self.itemsPerPage:
            listUsersResponse_body["itemsPerPage"] = self.itemsPerPage
        if self.Resources:
            listUsersResponse_body["Resources"] = [
                v.as_request()[1] for v in self.Resources
            ]
        if self.startIndex:
            listUsersResponse_body["startIndex"] = self.startIndex
        if self.totalResults:
            listUsersResponse_body["totalResults"] = self.totalResults

        return listUsersResponse_query, listUsersResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ListUsersResponse":
        return cls(
            itemsPerPage=d.get("itemsPerPage", None),
            Resources=[User.from_dict(v) for v in d["Resources"]]
            if "Resources" in d
            else None,
            startIndex=d.get("startIndex", None),
            totalResults=d.get("totalResults", None),
        )


@dataclass
class Name:

    # Family name of the Databricks user.
    familyName: str
    # Given name of the Databricks user.
    givenName: str

    def as_request(self) -> (dict, dict):
        name_query, name_body = {}, {}
        if self.familyName:
            name_body["familyName"] = self.familyName
        if self.givenName:
            name_body["givenName"] = self.givenName

        return name_query, name_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "Name":
        return cls(
            familyName=d.get("familyName", None),
            givenName=d.get("givenName", None),
        )


@dataclass
class PartialUpdate:

    # Unique ID for a group in the Databricks Account.
    id: str  # path

    operations: "List[Patch]"

    def as_request(self) -> (dict, dict):
        partialUpdate_query, partialUpdate_body = {}, {}
        if self.id:
            partialUpdate_body["id"] = self.id
        if self.operations:
            partialUpdate_body["operations"] = [
                v.as_request()[1] for v in self.operations
            ]

        return partialUpdate_query, partialUpdate_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "PartialUpdate":
        return cls(
            id=d.get("id", None),
            operations=[Patch.from_dict(v) for v in d["operations"]]
            if "operations" in d
            else None,
        )


@dataclass
class Patch:

    # Type of patch operation.
    op: "PatchOp"
    # Selection of patch operation
    path: str
    # Value to modify
    value: str

    def as_request(self) -> (dict, dict):
        patch_query, patch_body = {}, {}
        if self.op:
            patch_body["op"] = self.op.value
        if self.path:
            patch_body["path"] = self.path
        if self.value:
            patch_body["value"] = self.value

        return patch_query, patch_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "Patch":
        return cls(
            op=PatchOp(d["op"]) if "op" in d else None,
            path=d.get("path", None),
            value=d.get("value", None),
        )


class PatchOp(Enum):
    """Type of patch operation."""

    add = "add"
    remove = "remove"
    replace = "replace"


@dataclass
class ServicePrincipal:

    # If this user is active
    active: bool
    # UUID relating to the service principal
    applicationId: str
    # String that represents a concatenation of given and family names.
    displayName: str

    entitlements: "List[ComplexValue]"

    externalId: str

    groups: "List[ComplexValue]"
    # Databricks service principal ID.
    id: str  # path

    roles: "List[ComplexValue]"

    def as_request(self) -> (dict, dict):
        servicePrincipal_query, servicePrincipal_body = {}, {}
        if self.active:
            servicePrincipal_body["active"] = self.active
        if self.applicationId:
            servicePrincipal_body["applicationId"] = self.applicationId
        if self.displayName:
            servicePrincipal_body["displayName"] = self.displayName
        if self.entitlements:
            servicePrincipal_body["entitlements"] = [
                v.as_request()[1] for v in self.entitlements
            ]
        if self.externalId:
            servicePrincipal_body["externalId"] = self.externalId
        if self.groups:
            servicePrincipal_body["groups"] = [v.as_request()[1] for v in self.groups]
        if self.id:
            servicePrincipal_body["id"] = self.id
        if self.roles:
            servicePrincipal_body["roles"] = [v.as_request()[1] for v in self.roles]

        return servicePrincipal_query, servicePrincipal_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ServicePrincipal":
        return cls(
            active=d.get("active", None),
            applicationId=d.get("applicationId", None),
            displayName=d.get("displayName", None),
            entitlements=[ComplexValue.from_dict(v) for v in d["entitlements"]]
            if "entitlements" in d
            else None,
            externalId=d.get("externalId", None),
            groups=[ComplexValue.from_dict(v) for v in d["groups"]]
            if "groups" in d
            else None,
            id=d.get("id", None),
            roles=[ComplexValue.from_dict(v) for v in d["roles"]]
            if "roles" in d
            else None,
        )


@dataclass
class User:

    # If this user is active
    active: bool
    # String that represents a concatenation of given and family names. For
    # example `John Smith`.
    displayName: str
    # All the emails associated with the Databricks user.
    emails: "List[ComplexValue]"

    entitlements: "List[ComplexValue]"

    externalId: str

    groups: "List[ComplexValue]"
    # Databricks user ID.
    id: str  # path

    name: "Name"

    roles: "List[ComplexValue]"
    # Email address of the Databricks user.
    userName: str

    def as_request(self) -> (dict, dict):
        user_query, user_body = {}, {}
        if self.active:
            user_body["active"] = self.active
        if self.displayName:
            user_body["displayName"] = self.displayName
        if self.emails:
            user_body["emails"] = [v.as_request()[1] for v in self.emails]
        if self.entitlements:
            user_body["entitlements"] = [v.as_request()[1] for v in self.entitlements]
        if self.externalId:
            user_body["externalId"] = self.externalId
        if self.groups:
            user_body["groups"] = [v.as_request()[1] for v in self.groups]
        if self.id:
            user_body["id"] = self.id
        if self.name:
            user_body["name"] = self.name.as_request()[1]
        if self.roles:
            user_body["roles"] = [v.as_request()[1] for v in self.roles]
        if self.userName:
            user_body["userName"] = self.userName

        return user_query, user_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "User":
        return cls(
            active=d.get("active", None),
            displayName=d.get("displayName", None),
            emails=[ComplexValue.from_dict(v) for v in d["emails"]]
            if "emails" in d
            else None,
            entitlements=[ComplexValue.from_dict(v) for v in d["entitlements"]]
            if "entitlements" in d
            else None,
            externalId=d.get("externalId", None),
            groups=[ComplexValue.from_dict(v) for v in d["groups"]]
            if "groups" in d
            else None,
            id=d.get("id", None),
            name=Name.from_dict(d["name"]) if "name" in d else None,
            roles=[ComplexValue.from_dict(v) for v in d["roles"]]
            if "roles" in d
            else None,
            userName=d.get("userName", None),
        )


class AccountGroupsAPI:
    def __init__(self, api_client):
        self._api = api_client

    def create(self, request: Group) -> Group:
        """Create a new group.

        Creates a group in the Databricks Account with a unique name, using the
        supplied group details."""
        query, body = request.as_request()
        json = self._api.do(
            "POST", f"/api/2.0/accounts//scim/v2/Groups", query=query, body=body
        )
        return Group.from_dict(json)

    def delete(self, request: DeleteGroupRequest):
        """Delete a group.

        Deletes a group from the Databricks Account."""
        query, body = request.as_request()
        self._api.do(
            "DELETE",
            f"/api/2.0/accounts//scim/v2/Groups/{request.id}",
            query=query,
            body=body,
        )

    def get(self, request: GetGroupRequest) -> Group:
        """Get group details.

        Gets the information for a specific group in the Databricks Account."""
        query, body = request.as_request()
        json = self._api.do(
            "GET",
            f"/api/2.0/accounts//scim/v2/Groups/{request.id}",
            query=query,
            body=body,
        )
        return Group.from_dict(json)

    def list(self, request: ListGroupsRequest) -> ListGroupsResponse:
        """List group details.

        Gets all details of the groups associated with the Databricks Account."""
        query, body = request.as_request()
        json = self._api.do(
            "GET", f"/api/2.0/accounts//scim/v2/Groups", query=query, body=body
        )
        return ListGroupsResponse.from_dict(json)

    def patch(self, request: PartialUpdate):
        """Update group details.

        Partially updates the details of a group."""
        query, body = request.as_request()
        self._api.do(
            "PATCH",
            f"/api/2.0/accounts//scim/v2/Groups/{request.id}",
            query=query,
            body=body,
        )

    def update(self, request: Group):
        """Replace a group.

        Updates the details of a group by replacing the entire group entity."""
        query, body = request.as_request()
        self._api.do(
            "PUT",
            f"/api/2.0/accounts//scim/v2/Groups/{request.id}",
            query=query,
            body=body,
        )


class AccountServicePrincipalsAPI:
    def __init__(self, api_client):
        self._api = api_client

    def create(self, request: ServicePrincipal) -> ServicePrincipal:
        """Create a service principal.

        Creates a new service principal in the Databricks Account."""
        query, body = request.as_request()
        json = self._api.do(
            "POST",
            f"/api/2.0/accounts//scim/v2/ServicePrincipals",
            query=query,
            body=body,
        )
        return ServicePrincipal.from_dict(json)

    def delete(self, request: DeleteServicePrincipalRequest):
        """Delete a service principal.

        Delete a single service principal in the Databricks Account."""
        query, body = request.as_request()
        self._api.do(
            "DELETE",
            f"/api/2.0/accounts//scim/v2/ServicePrincipals/{request.id}",
            query=query,
            body=body,
        )

    def get(self, request: GetServicePrincipalRequest) -> ServicePrincipal:
        """Get service principal details.

        Gets the details for a single service principal define in the Databricks
        Account."""
        query, body = request.as_request()
        json = self._api.do(
            "GET",
            f"/api/2.0/accounts//scim/v2/ServicePrincipals/{request.id}",
            query=query,
            body=body,
        )
        return ServicePrincipal.from_dict(json)

    def list(
        self, request: ListServicePrincipalsRequest
    ) -> ListServicePrincipalResponse:
        """List service principals.

        Gets the set of service principals associated with a Databricks Account."""
        query, body = request.as_request()
        json = self._api.do(
            "GET",
            f"/api/2.0/accounts//scim/v2/ServicePrincipals",
            query=query,
            body=body,
        )
        return ListServicePrincipalResponse.from_dict(json)

    def patch(self, request: PartialUpdate):
        """Update service principal details.

        Partially updates the details of a single service principal in the
        Databricks Account."""
        query, body = request.as_request()
        self._api.do(
            "PATCH",
            f"/api/2.0/accounts//scim/v2/ServicePrincipals/{request.id}",
            query=query,
            body=body,
        )

    def update(self, request: ServicePrincipal):
        """Replace service principal.

        Updates the details of a single service principal.

        This action replaces the existing service principal with the same name."""
        query, body = request.as_request()
        self._api.do(
            "PUT",
            f"/api/2.0/accounts//scim/v2/ServicePrincipals/{request.id}",
            query=query,
            body=body,
        )


class AccountUsersAPI:
    def __init__(self, api_client):
        self._api = api_client

    def create(self, request: User) -> User:
        """Create a new user.

        Creates a new user in the Databricks Account. This new user will also be
        added to the Databricks account."""
        query, body = request.as_request()
        json = self._api.do(
            "POST", f"/api/2.0/accounts//scim/v2/Users", query=query, body=body
        )
        return User.from_dict(json)

    def delete(self, request: DeleteUserRequest):
        """Delete a user.

        Deletes a user. Deleting a user from a Databricks Account also removes
        objects associated with the user."""
        query, body = request.as_request()
        self._api.do(
            "DELETE",
            f"/api/2.0/accounts//scim/v2/Users/{request.id}",
            query=query,
            body=body,
        )

    def get(self, request: GetUserRequest) -> User:
        """Get user details.

        Gets information for a specific user in Databricks Account."""
        query, body = request.as_request()
        json = self._api.do(
            "GET",
            f"/api/2.0/accounts//scim/v2/Users/{request.id}",
            query=query,
            body=body,
        )
        return User.from_dict(json)

    def list(self, request: ListUsersRequest) -> ListUsersResponse:
        """List users.

        Gets details for all the users associated with a Databricks Account."""
        query, body = request.as_request()
        json = self._api.do(
            "GET", f"/api/2.0/accounts//scim/v2/Users", query=query, body=body
        )
        return ListUsersResponse.from_dict(json)

    def patch(self, request: PartialUpdate):
        """Update user details.

        Partially updates a user resource by applying the supplied operations on
        specific user attributes."""
        query, body = request.as_request()
        self._api.do(
            "PATCH",
            f"/api/2.0/accounts//scim/v2/Users/{request.id}",
            query=query,
            body=body,
        )

    def update(self, request: User):
        """Replace a user.

        Replaces a user's information with the data supplied in request."""
        query, body = request.as_request()
        self._api.do(
            "PUT",
            f"/api/2.0/accounts//scim/v2/Users/{request.id}",
            query=query,
            body=body,
        )


class CurrentUserAPI:
    def __init__(self, api_client):
        self._api = api_client

    def me(self) -> User:
        """Get current user info.

        Get details about the current method caller's identity."""

        json = self._api.do("GET", "/api/2.0/preview/scim/v2/Me")
        return User.from_dict(json)


class GroupsAPI:
    def __init__(self, api_client):
        self._api = api_client

    def create(self, request: Group) -> Group:
        """Create a new group.

        Creates a group in the Databricks Workspace with a unique name, using
        the supplied group details."""
        query, body = request.as_request()
        json = self._api.do(
            "POST", "/api/2.0/preview/scim/v2/Groups", query=query, body=body
        )
        return Group.from_dict(json)

    def delete(self, request: DeleteGroupRequest):
        """Delete a group.

        Deletes a group from the Databricks Workspace."""
        query, body = request.as_request()
        self._api.do(
            "DELETE",
            f"/api/2.0/preview/scim/v2/Groups/{request.id}",
            query=query,
            body=body,
        )

    def get(self, request: GetGroupRequest) -> Group:
        """Get group details.

        Gets the information for a specific group in the Databricks Workspace."""
        query, body = request.as_request()
        json = self._api.do(
            "GET",
            f"/api/2.0/preview/scim/v2/Groups/{request.id}",
            query=query,
            body=body,
        )
        return Group.from_dict(json)

    def list(self, request: ListGroupsRequest) -> ListGroupsResponse:
        """List group details.

        Gets all details of the groups associated with the Databricks Workspace."""
        query, body = request.as_request()
        json = self._api.do(
            "GET", "/api/2.0/preview/scim/v2/Groups", query=query, body=body
        )
        return ListGroupsResponse.from_dict(json)

    def patch(self, request: PartialUpdate):
        """Update group details.

        Partially updates the details of a group."""
        query, body = request.as_request()
        self._api.do(
            "PATCH",
            f"/api/2.0/preview/scim/v2/Groups/{request.id}",
            query=query,
            body=body,
        )

    def update(self, request: Group):
        """Replace a group.

        Updates the details of a group by replacing the entire group entity."""
        query, body = request.as_request()
        self._api.do(
            "PUT",
            f"/api/2.0/preview/scim/v2/Groups/{request.id}",
            query=query,
            body=body,
        )


class ServicePrincipalsAPI:
    def __init__(self, api_client):
        self._api = api_client

    def create(self, request: ServicePrincipal) -> ServicePrincipal:
        """Create a service principal.

        Creates a new service principal in the Databricks Workspace."""
        query, body = request.as_request()
        json = self._api.do(
            "POST", "/api/2.0/preview/scim/v2/ServicePrincipals", query=query, body=body
        )
        return ServicePrincipal.from_dict(json)

    def delete(self, request: DeleteServicePrincipalRequest):
        """Delete a service principal.

        Delete a single service principal in the Databricks Workspace."""
        query, body = request.as_request()
        self._api.do(
            "DELETE",
            f"/api/2.0/preview/scim/v2/ServicePrincipals/{request.id}",
            query=query,
            body=body,
        )

    def get(self, request: GetServicePrincipalRequest) -> ServicePrincipal:
        """Get service principal details.

        Gets the details for a single service principal define in the Databricks
        Workspace."""
        query, body = request.as_request()
        json = self._api.do(
            "GET",
            f"/api/2.0/preview/scim/v2/ServicePrincipals/{request.id}",
            query=query,
            body=body,
        )
        return ServicePrincipal.from_dict(json)

    def list(
        self, request: ListServicePrincipalsRequest
    ) -> ListServicePrincipalResponse:
        """List service principals.

        Gets the set of service principals associated with a Databricks
        Workspace."""
        query, body = request.as_request()
        json = self._api.do(
            "GET", "/api/2.0/preview/scim/v2/ServicePrincipals", query=query, body=body
        )
        return ListServicePrincipalResponse.from_dict(json)

    def patch(self, request: PartialUpdate):
        """Update service principal details.

        Partially updates the details of a single service principal in the
        Databricks Workspace."""
        query, body = request.as_request()
        self._api.do(
            "PATCH",
            f"/api/2.0/preview/scim/v2/ServicePrincipals/{request.id}",
            query=query,
            body=body,
        )

    def update(self, request: ServicePrincipal):
        """Replace service principal.

        Updates the details of a single service principal.

        This action replaces the existing service principal with the same name."""
        query, body = request.as_request()
        self._api.do(
            "PUT",
            f"/api/2.0/preview/scim/v2/ServicePrincipals/{request.id}",
            query=query,
            body=body,
        )


class UsersAPI:
    def __init__(self, api_client):
        self._api = api_client

    def create(self, request: User) -> User:
        """Create a new user.

        Creates a new user in the Databricks Workspace. This new user will also
        be added to the Databricks account."""
        query, body = request.as_request()
        json = self._api.do(
            "POST", "/api/2.0/preview/scim/v2/Users", query=query, body=body
        )
        return User.from_dict(json)

    def delete(self, request: DeleteUserRequest):
        """Delete a user.

        Deletes a user. Deleting a user from a Databricks Workspace also removes
        objects associated with the user."""
        query, body = request.as_request()
        self._api.do(
            "DELETE",
            f"/api/2.0/preview/scim/v2/Users/{request.id}",
            query=query,
            body=body,
        )

    def get(self, request: GetUserRequest) -> User:
        """Get user details.

        Gets information for a specific user in Databricks Workspace."""
        query, body = request.as_request()
        json = self._api.do(
            "GET",
            f"/api/2.0/preview/scim/v2/Users/{request.id}",
            query=query,
            body=body,
        )
        return User.from_dict(json)

    def list(self, request: ListUsersRequest) -> ListUsersResponse:
        """List users.

        Gets details for all the users associated with a Databricks Workspace."""
        query, body = request.as_request()
        json = self._api.do(
            "GET", "/api/2.0/preview/scim/v2/Users", query=query, body=body
        )
        return ListUsersResponse.from_dict(json)

    def patch(self, request: PartialUpdate):
        """Update user details.

        Partially updates a user resource by applying the supplied operations on
        specific user attributes."""
        query, body = request.as_request()
        self._api.do(
            "PATCH",
            f"/api/2.0/preview/scim/v2/Users/{request.id}",
            query=query,
            body=body,
        )

    def update(self, request: User):
        """Replace a user.

        Replaces a user's information with the data supplied in request."""
        query, body = request.as_request()
        self._api.do(
            "PUT",
            f"/api/2.0/preview/scim/v2/Users/{request.id}",
            query=query,
            body=body,
        )
