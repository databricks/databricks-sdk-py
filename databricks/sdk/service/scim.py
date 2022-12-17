# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Any


# all definitions in this file are in alphabetical order


@dataclass
class ComplexValue:

    display: str

    primary: bool

    type: str

    value: str

    def as_dict(self) -> dict:
        body = {}
        if self.display:
            body["display"] = self.display
        if self.primary:
            body["primary"] = self.primary
        if self.type:
            body["type"] = self.type
        if self.value:
            body["value"] = self.value

        return body

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

    def as_dict(self) -> dict:
        body = {}
        if self.id:
            body["id"] = self.id

        return body

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

    def as_dict(self) -> dict:
        body = {}
        if self.id:
            body["id"] = self.id

        return body

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

    def as_dict(self) -> dict:
        body = {}
        if self.id:
            body["id"] = self.id

        return body

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

    def as_dict(self) -> dict:
        body = {}
        if self.id:
            body["id"] = self.id

        return body

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

    def as_dict(self) -> dict:
        body = {}
        if self.id:
            body["id"] = self.id

        return body

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

    def as_dict(self) -> dict:
        body = {}
        if self.id:
            body["id"] = self.id

        return body

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

    def as_dict(self) -> dict:
        body = {}
        if self.displayName:
            body["displayName"] = self.displayName
        if self.entitlements:
            body["entitlements"] = [v.as_dict() for v in self.entitlements]
        if self.externalId:
            body["externalId"] = self.externalId
        if self.groups:
            body["groups"] = [v.as_dict() for v in self.groups]
        if self.id:
            body["id"] = self.id
        if self.members:
            body["members"] = [v.as_dict() for v in self.members]
        if self.roles:
            body["roles"] = [v.as_dict() for v in self.roles]

        return body

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
    # Query by which the results have to be filtered. Supported operators are equals(`eq`), contains(`co`), starts
    # with(`sw`) and not equals(`ne`). Additionally, simple expressions can be formed using logical operators - `and`
    # and `or`. The [SCIM RFC] has more details but we currently only support simple expressions.
    #
    # [SCIM RFC]: https://tools.ietf.org/html/rfc7644#section-3.4.2.2
    filter: str  # query
    # Attribute to sort the results.
    sortBy: str  # query
    # The order to sort the results.
    sortOrder: "ListSortOrder"  # query
    # Specifies the index of the first result. First item is number 1.
    startIndex: int  # query

    def as_dict(self) -> dict:
        body = {}
        if self.attributes:
            body["attributes"] = self.attributes
        if self.count:
            body["count"] = self.count
        if self.excludedAttributes:
            body["excludedAttributes"] = self.excludedAttributes
        if self.filter:
            body["filter"] = self.filter
        if self.sortBy:
            body["sortBy"] = self.sortBy
        if self.sortOrder:
            body["sortOrder"] = self.sortOrder.value
        if self.startIndex:
            body["startIndex"] = self.startIndex

        return body

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
    # Starting index of all the results that matched the request filters. First item is number 1.
    startIndex: int
    # Total results that match the request filters.
    totalResults: int

    def as_dict(self) -> dict:
        body = {}
        if self.itemsPerPage:
            body["itemsPerPage"] = self.itemsPerPage
        if self.Resources:
            body["Resources"] = [v.as_dict() for v in self.Resources]
        if self.startIndex:
            body["startIndex"] = self.startIndex
        if self.totalResults:
            body["totalResults"] = self.totalResults

        return body

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
    # Starting index of all the results that matched the request filters. First item is number 1.
    startIndex: int
    # Total results that match the request filters.
    totalResults: int

    def as_dict(self) -> dict:
        body = {}
        if self.itemsPerPage:
            body["itemsPerPage"] = self.itemsPerPage
        if self.Resources:
            body["Resources"] = [v.as_dict() for v in self.Resources]
        if self.startIndex:
            body["startIndex"] = self.startIndex
        if self.totalResults:
            body["totalResults"] = self.totalResults

        return body

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
    # Query by which the results have to be filtered. Supported operators are equals(`eq`), contains(`co`), starts
    # with(`sw`) and not equals(`ne`). Additionally, simple expressions can be formed using logical operators - `and`
    # and `or`. The [SCIM RFC] has more details but we currently only support simple expressions.
    #
    # [SCIM RFC]: https://tools.ietf.org/html/rfc7644#section-3.4.2.2
    filter: str  # query
    # Attribute to sort the results.
    sortBy: str  # query
    # The order to sort the results.
    sortOrder: "ListSortOrder"  # query
    # Specifies the index of the first result. First item is number 1.
    startIndex: int  # query

    def as_dict(self) -> dict:
        body = {}
        if self.attributes:
            body["attributes"] = self.attributes
        if self.count:
            body["count"] = self.count
        if self.excludedAttributes:
            body["excludedAttributes"] = self.excludedAttributes
        if self.filter:
            body["filter"] = self.filter
        if self.sortBy:
            body["sortBy"] = self.sortBy
        if self.sortOrder:
            body["sortOrder"] = self.sortOrder.value
        if self.startIndex:
            body["startIndex"] = self.startIndex

        return body

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
    # Query by which the results have to be filtered. Supported operators are equals(`eq`), contains(`co`), starts
    # with(`sw`) and not equals(`ne`). Additionally, simple expressions can be formed using logical operators - `and`
    # and `or`. The [SCIM RFC] has more details but we currently only support simple expressions.
    #
    # [SCIM RFC]: https://tools.ietf.org/html/rfc7644#section-3.4.2.2
    filter: str  # query
    # Attribute to sort the results. Multi-part paths are supported. For example, `userName`, `name.givenName`, and
    # `emails`.
    sortBy: str  # query
    # The order to sort the results.
    sortOrder: "ListSortOrder"  # query
    # Specifies the index of the first result. First item is number 1.
    startIndex: int  # query

    def as_dict(self) -> dict:
        body = {}
        if self.attributes:
            body["attributes"] = self.attributes
        if self.count:
            body["count"] = self.count
        if self.excludedAttributes:
            body["excludedAttributes"] = self.excludedAttributes
        if self.filter:
            body["filter"] = self.filter
        if self.sortBy:
            body["sortBy"] = self.sortBy
        if self.sortOrder:
            body["sortOrder"] = self.sortOrder.value
        if self.startIndex:
            body["startIndex"] = self.startIndex

        return body

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
    # Starting index of all the results that matched the request filters. First item is number 1.
    startIndex: int
    # Total results that match the request filters.
    totalResults: int

    def as_dict(self) -> dict:
        body = {}
        if self.itemsPerPage:
            body["itemsPerPage"] = self.itemsPerPage
        if self.Resources:
            body["Resources"] = [v.as_dict() for v in self.Resources]
        if self.startIndex:
            body["startIndex"] = self.startIndex
        if self.totalResults:
            body["totalResults"] = self.totalResults

        return body

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

    def as_dict(self) -> dict:
        body = {}
        if self.familyName:
            body["familyName"] = self.familyName
        if self.givenName:
            body["givenName"] = self.givenName

        return body

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

    def as_dict(self) -> dict:
        body = {}
        if self.id:
            body["id"] = self.id
        if self.operations:
            body["operations"] = [v.as_dict() for v in self.operations]

        return body

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

    def as_dict(self) -> dict:
        body = {}
        if self.op:
            body["op"] = self.op.value
        if self.path:
            body["path"] = self.path
        if self.value:
            body["value"] = self.value

        return body

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

    def as_dict(self) -> dict:
        body = {}
        if self.active:
            body["active"] = self.active
        if self.applicationId:
            body["applicationId"] = self.applicationId
        if self.displayName:
            body["displayName"] = self.displayName
        if self.entitlements:
            body["entitlements"] = [v.as_dict() for v in self.entitlements]
        if self.externalId:
            body["externalId"] = self.externalId
        if self.groups:
            body["groups"] = [v.as_dict() for v in self.groups]
        if self.id:
            body["id"] = self.id
        if self.roles:
            body["roles"] = [v.as_dict() for v in self.roles]

        return body

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
    # String that represents a concatenation of given and family names. For example `John Smith`.
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

    def as_dict(self) -> dict:
        body = {}
        if self.active:
            body["active"] = self.active
        if self.displayName:
            body["displayName"] = self.displayName
        if self.emails:
            body["emails"] = [v.as_dict() for v in self.emails]
        if self.entitlements:
            body["entitlements"] = [v.as_dict() for v in self.entitlements]
        if self.externalId:
            body["externalId"] = self.externalId
        if self.groups:
            body["groups"] = [v.as_dict() for v in self.groups]
        if self.id:
            body["id"] = self.id
        if self.name:
            body["name"] = self.name.as_dict()
        if self.roles:
            body["roles"] = [v.as_dict() for v in self.roles]
        if self.userName:
            body["userName"] = self.userName

        return body

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

    def create(
        self,
        id: str,
        id: str,
        *,
        display_name: str = None,
        entitlements: List[ComplexValue] = None,
        external_id: str = None,
        groups: List[ComplexValue] = None,
        members: List[ComplexValue] = None,
        roles: List[ComplexValue] = None,
        **kwargs,
    ) -> Group:
        """Create a new group.

        Creates a group in the Databricks Account with a unique name, using the
        supplied group details."""
        request = kwargs.get("request", None)
        if not request:  # request is not given through keyed args
            request = Group(
                display_name=display_name,
                entitlements=entitlements,
                external_id=external_id,
                groups=groups,
                id=id,
                members=members,
                roles=roles,
            )
        body = request.as_dict()

        json = self._api.do("POST", f"/api/2.0/accounts//scim/v2/Groups", body=body)
        return Group.from_dict(json)

    def delete(self, id: str, **kwargs):
        """Delete a group.

        Deletes a group from the Databricks Account."""
        request = kwargs.get("request", None)
        if not request:  # request is not given through keyed args
            request = DeleteGroupRequest(id=id)

        self._api.do("DELETE", f"/api/2.0/accounts//scim/v2/Groups/{request.id}")

    def get(self, id: str, **kwargs) -> Group:
        """Get group details.

        Gets the information for a specific group in the Databricks Account."""
        request = kwargs.get("request", None)
        if not request:  # request is not given through keyed args
            request = GetGroupRequest(id=id)

        json = self._api.do("GET", f"/api/2.0/accounts//scim/v2/Groups/{request.id}")
        return Group.from_dict(json)

    def list(
        self,
        *,
        attributes: str = None,
        count: int = None,
        excluded_attributes: str = None,
        filter: str = None,
        sort_by: str = None,
        sort_order: ListSortOrder = None,
        start_index: int = None,
        **kwargs,
    ) -> ListGroupsResponse:
        """List group details.

        Gets all details of the groups associated with the Databricks Account."""
        request = kwargs.get("request", None)
        if not request:  # request is not given through keyed args
            request = ListGroupsRequest(
                attributes=attributes,
                count=count,
                excluded_attributes=excluded_attributes,
                filter=filter,
                sort_by=sort_by,
                sort_order=sort_order,
                start_index=start_index,
            )

        query = {}
        if attributes:
            query["attributes"] = request.attributes
        if count:
            query["count"] = request.count
        if excluded_attributes:
            query["excludedAttributes"] = request.excluded_attributes
        if filter:
            query["filter"] = request.filter
        if sort_by:
            query["sortBy"] = request.sort_by
        if sort_order:
            query["sortOrder"] = request.sort_order.value
        if start_index:
            query["startIndex"] = request.start_index

        json = self._api.do("GET", f"/api/2.0/accounts//scim/v2/Groups", query=query)
        return ListGroupsResponse.from_dict(json)

    def patch(
        self,
        id: str,
        id: str,
        id: str,
        id: str,
        id: str,
        id: str,
        *,
        operations: List[Patch] = None,
        **kwargs,
    ):
        """Update group details.

        Partially updates the details of a group."""
        request = kwargs.get("request", None)
        if not request:  # request is not given through keyed args
            request = PartialUpdate(id=id, operations=operations)
        body = request.as_dict()

        self._api.do(
            "PATCH", f"/api/2.0/accounts//scim/v2/Groups/{request.id}", body=body
        )

    def update(
        self,
        id: str,
        id: str,
        *,
        display_name: str = None,
        entitlements: List[ComplexValue] = None,
        external_id: str = None,
        groups: List[ComplexValue] = None,
        members: List[ComplexValue] = None,
        roles: List[ComplexValue] = None,
        **kwargs,
    ):
        """Replace a group.

        Updates the details of a group by replacing the entire group entity."""
        request = kwargs.get("request", None)
        if not request:  # request is not given through keyed args
            request = Group(
                display_name=display_name,
                entitlements=entitlements,
                external_id=external_id,
                groups=groups,
                id=id,
                members=members,
                roles=roles,
            )
        body = request.as_dict()

        self._api.do(
            "PUT", f"/api/2.0/accounts//scim/v2/Groups/{request.id}", body=body
        )


class AccountServicePrincipalsAPI:
    def __init__(self, api_client):
        self._api = api_client

    def create(
        self,
        id: str,
        id: str,
        *,
        active: bool = None,
        application_id: str = None,
        display_name: str = None,
        entitlements: List[ComplexValue] = None,
        external_id: str = None,
        groups: List[ComplexValue] = None,
        roles: List[ComplexValue] = None,
        **kwargs,
    ) -> ServicePrincipal:
        """Create a service principal.

        Creates a new service principal in the Databricks Account."""
        request = kwargs.get("request", None)
        if not request:  # request is not given through keyed args
            request = ServicePrincipal(
                active=active,
                application_id=application_id,
                display_name=display_name,
                entitlements=entitlements,
                external_id=external_id,
                groups=groups,
                id=id,
                roles=roles,
            )
        body = request.as_dict()

        json = self._api.do(
            "POST", f"/api/2.0/accounts//scim/v2/ServicePrincipals", body=body
        )
        return ServicePrincipal.from_dict(json)

    def delete(self, id: str, **kwargs):
        """Delete a service principal.

        Delete a single service principal in the Databricks Account."""
        request = kwargs.get("request", None)
        if not request:  # request is not given through keyed args
            request = DeleteServicePrincipalRequest(id=id)

        self._api.do(
            "DELETE", f"/api/2.0/accounts//scim/v2/ServicePrincipals/{request.id}"
        )

    def get(self, id: str, **kwargs) -> ServicePrincipal:
        """Get service principal details.

        Gets the details for a single service principal define in the Databricks
        Account."""
        request = kwargs.get("request", None)
        if not request:  # request is not given through keyed args
            request = GetServicePrincipalRequest(id=id)

        json = self._api.do(
            "GET", f"/api/2.0/accounts//scim/v2/ServicePrincipals/{request.id}"
        )
        return ServicePrincipal.from_dict(json)

    def list(
        self,
        *,
        attributes: str = None,
        count: int = None,
        excluded_attributes: str = None,
        filter: str = None,
        sort_by: str = None,
        sort_order: ListSortOrder = None,
        start_index: int = None,
        **kwargs,
    ) -> ListServicePrincipalResponse:
        """List service principals.

        Gets the set of service principals associated with a Databricks Account."""
        request = kwargs.get("request", None)
        if not request:  # request is not given through keyed args
            request = ListServicePrincipalsRequest(
                attributes=attributes,
                count=count,
                excluded_attributes=excluded_attributes,
                filter=filter,
                sort_by=sort_by,
                sort_order=sort_order,
                start_index=start_index,
            )

        query = {}
        if attributes:
            query["attributes"] = request.attributes
        if count:
            query["count"] = request.count
        if excluded_attributes:
            query["excludedAttributes"] = request.excluded_attributes
        if filter:
            query["filter"] = request.filter
        if sort_by:
            query["sortBy"] = request.sort_by
        if sort_order:
            query["sortOrder"] = request.sort_order.value
        if start_index:
            query["startIndex"] = request.start_index

        json = self._api.do(
            "GET", f"/api/2.0/accounts//scim/v2/ServicePrincipals", query=query
        )
        return ListServicePrincipalResponse.from_dict(json)

    def patch(
        self,
        id: str,
        id: str,
        id: str,
        id: str,
        id: str,
        id: str,
        *,
        operations: List[Patch] = None,
        **kwargs,
    ):
        """Update service principal details.

        Partially updates the details of a single service principal in the
        Databricks Account."""
        request = kwargs.get("request", None)
        if not request:  # request is not given through keyed args
            request = PartialUpdate(id=id, operations=operations)
        body = request.as_dict()

        self._api.do(
            "PATCH",
            f"/api/2.0/accounts//scim/v2/ServicePrincipals/{request.id}",
            body=body,
        )

    def update(
        self,
        id: str,
        id: str,
        *,
        active: bool = None,
        application_id: str = None,
        display_name: str = None,
        entitlements: List[ComplexValue] = None,
        external_id: str = None,
        groups: List[ComplexValue] = None,
        roles: List[ComplexValue] = None,
        **kwargs,
    ):
        """Replace service principal.

        Updates the details of a single service principal.

        This action replaces the existing service principal with the same name."""
        request = kwargs.get("request", None)
        if not request:  # request is not given through keyed args
            request = ServicePrincipal(
                active=active,
                application_id=application_id,
                display_name=display_name,
                entitlements=entitlements,
                external_id=external_id,
                groups=groups,
                id=id,
                roles=roles,
            )
        body = request.as_dict()

        self._api.do(
            "PUT",
            f"/api/2.0/accounts//scim/v2/ServicePrincipals/{request.id}",
            body=body,
        )


class AccountUsersAPI:
    def __init__(self, api_client):
        self._api = api_client

    def create(
        self,
        id: str,
        id: str,
        *,
        active: bool = None,
        display_name: str = None,
        emails: List[ComplexValue] = None,
        entitlements: List[ComplexValue] = None,
        external_id: str = None,
        groups: List[ComplexValue] = None,
        name: Name = None,
        roles: List[ComplexValue] = None,
        user_name: str = None,
        **kwargs,
    ) -> User:
        """Create a new user.

        Creates a new user in the Databricks Account. This new user will also be
        added to the Databricks account."""
        request = kwargs.get("request", None)
        if not request:  # request is not given through keyed args
            request = User(
                active=active,
                display_name=display_name,
                emails=emails,
                entitlements=entitlements,
                external_id=external_id,
                groups=groups,
                id=id,
                name=name,
                roles=roles,
                user_name=user_name,
            )
        body = request.as_dict()

        json = self._api.do("POST", f"/api/2.0/accounts//scim/v2/Users", body=body)
        return User.from_dict(json)

    def delete(self, id: str, **kwargs):
        """Delete a user.

        Deletes a user. Deleting a user from a Databricks Account also removes
        objects associated with the user."""
        request = kwargs.get("request", None)
        if not request:  # request is not given through keyed args
            request = DeleteUserRequest(id=id)

        self._api.do("DELETE", f"/api/2.0/accounts//scim/v2/Users/{request.id}")

    def get(self, id: str, **kwargs) -> User:
        """Get user details.

        Gets information for a specific user in Databricks Account."""
        request = kwargs.get("request", None)
        if not request:  # request is not given through keyed args
            request = GetUserRequest(id=id)

        json = self._api.do("GET", f"/api/2.0/accounts//scim/v2/Users/{request.id}")
        return User.from_dict(json)

    def list(
        self,
        *,
        attributes: str = None,
        count: int = None,
        excluded_attributes: str = None,
        filter: str = None,
        sort_by: str = None,
        sort_order: ListSortOrder = None,
        start_index: int = None,
        **kwargs,
    ) -> ListUsersResponse:
        """List users.

        Gets details for all the users associated with a Databricks Account."""
        request = kwargs.get("request", None)
        if not request:  # request is not given through keyed args
            request = ListUsersRequest(
                attributes=attributes,
                count=count,
                excluded_attributes=excluded_attributes,
                filter=filter,
                sort_by=sort_by,
                sort_order=sort_order,
                start_index=start_index,
            )

        query = {}
        if attributes:
            query["attributes"] = request.attributes
        if count:
            query["count"] = request.count
        if excluded_attributes:
            query["excludedAttributes"] = request.excluded_attributes
        if filter:
            query["filter"] = request.filter
        if sort_by:
            query["sortBy"] = request.sort_by
        if sort_order:
            query["sortOrder"] = request.sort_order.value
        if start_index:
            query["startIndex"] = request.start_index

        json = self._api.do("GET", f"/api/2.0/accounts//scim/v2/Users", query=query)
        return ListUsersResponse.from_dict(json)

    def patch(
        self,
        id: str,
        id: str,
        id: str,
        id: str,
        id: str,
        id: str,
        *,
        operations: List[Patch] = None,
        **kwargs,
    ):
        """Update user details.

        Partially updates a user resource by applying the supplied operations on
        specific user attributes."""
        request = kwargs.get("request", None)
        if not request:  # request is not given through keyed args
            request = PartialUpdate(id=id, operations=operations)
        body = request.as_dict()

        self._api.do(
            "PATCH", f"/api/2.0/accounts//scim/v2/Users/{request.id}", body=body
        )

    def update(
        self,
        id: str,
        id: str,
        *,
        active: bool = None,
        display_name: str = None,
        emails: List[ComplexValue] = None,
        entitlements: List[ComplexValue] = None,
        external_id: str = None,
        groups: List[ComplexValue] = None,
        name: Name = None,
        roles: List[ComplexValue] = None,
        user_name: str = None,
        **kwargs,
    ):
        """Replace a user.

        Replaces a user's information with the data supplied in request."""
        request = kwargs.get("request", None)
        if not request:  # request is not given through keyed args
            request = User(
                active=active,
                display_name=display_name,
                emails=emails,
                entitlements=entitlements,
                external_id=external_id,
                groups=groups,
                id=id,
                name=name,
                roles=roles,
                user_name=user_name,
            )
        body = request.as_dict()

        self._api.do("PUT", f"/api/2.0/accounts//scim/v2/Users/{request.id}", body=body)


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

    def create(
        self,
        id: str,
        id: str,
        *,
        display_name: str = None,
        entitlements: List[ComplexValue] = None,
        external_id: str = None,
        groups: List[ComplexValue] = None,
        members: List[ComplexValue] = None,
        roles: List[ComplexValue] = None,
        **kwargs,
    ) -> Group:
        """Create a new group.

        Creates a group in the Databricks Workspace with a unique name, using
        the supplied group details."""
        request = kwargs.get("request", None)
        if not request:  # request is not given through keyed args
            request = Group(
                display_name=display_name,
                entitlements=entitlements,
                external_id=external_id,
                groups=groups,
                id=id,
                members=members,
                roles=roles,
            )
        body = request.as_dict()

        json = self._api.do("POST", "/api/2.0/preview/scim/v2/Groups", body=body)
        return Group.from_dict(json)

    def delete(self, id: str, **kwargs):
        """Delete a group.

        Deletes a group from the Databricks Workspace."""
        request = kwargs.get("request", None)
        if not request:  # request is not given through keyed args
            request = DeleteGroupRequest(id=id)

        self._api.do("DELETE", f"/api/2.0/preview/scim/v2/Groups/{request.id}")

    def get(self, id: str, **kwargs) -> Group:
        """Get group details.

        Gets the information for a specific group in the Databricks Workspace."""
        request = kwargs.get("request", None)
        if not request:  # request is not given through keyed args
            request = GetGroupRequest(id=id)

        json = self._api.do("GET", f"/api/2.0/preview/scim/v2/Groups/{request.id}")
        return Group.from_dict(json)

    def list(
        self,
        *,
        attributes: str = None,
        count: int = None,
        excluded_attributes: str = None,
        filter: str = None,
        sort_by: str = None,
        sort_order: ListSortOrder = None,
        start_index: int = None,
        **kwargs,
    ) -> ListGroupsResponse:
        """List group details.

        Gets all details of the groups associated with the Databricks Workspace."""
        request = kwargs.get("request", None)
        if not request:  # request is not given through keyed args
            request = ListGroupsRequest(
                attributes=attributes,
                count=count,
                excluded_attributes=excluded_attributes,
                filter=filter,
                sort_by=sort_by,
                sort_order=sort_order,
                start_index=start_index,
            )

        query = {}
        if attributes:
            query["attributes"] = request.attributes
        if count:
            query["count"] = request.count
        if excluded_attributes:
            query["excludedAttributes"] = request.excluded_attributes
        if filter:
            query["filter"] = request.filter
        if sort_by:
            query["sortBy"] = request.sort_by
        if sort_order:
            query["sortOrder"] = request.sort_order.value
        if start_index:
            query["startIndex"] = request.start_index

        json = self._api.do("GET", "/api/2.0/preview/scim/v2/Groups", query=query)
        return ListGroupsResponse.from_dict(json)

    def patch(
        self,
        id: str,
        id: str,
        id: str,
        id: str,
        id: str,
        id: str,
        *,
        operations: List[Patch] = None,
        **kwargs,
    ):
        """Update group details.

        Partially updates the details of a group."""
        request = kwargs.get("request", None)
        if not request:  # request is not given through keyed args
            request = PartialUpdate(id=id, operations=operations)
        body = request.as_dict()

        self._api.do(
            "PATCH", f"/api/2.0/preview/scim/v2/Groups/{request.id}", body=body
        )

    def update(
        self,
        id: str,
        id: str,
        *,
        display_name: str = None,
        entitlements: List[ComplexValue] = None,
        external_id: str = None,
        groups: List[ComplexValue] = None,
        members: List[ComplexValue] = None,
        roles: List[ComplexValue] = None,
        **kwargs,
    ):
        """Replace a group.

        Updates the details of a group by replacing the entire group entity."""
        request = kwargs.get("request", None)
        if not request:  # request is not given through keyed args
            request = Group(
                display_name=display_name,
                entitlements=entitlements,
                external_id=external_id,
                groups=groups,
                id=id,
                members=members,
                roles=roles,
            )
        body = request.as_dict()

        self._api.do("PUT", f"/api/2.0/preview/scim/v2/Groups/{request.id}", body=body)


class ServicePrincipalsAPI:
    def __init__(self, api_client):
        self._api = api_client

    def create(
        self,
        id: str,
        id: str,
        *,
        active: bool = None,
        application_id: str = None,
        display_name: str = None,
        entitlements: List[ComplexValue] = None,
        external_id: str = None,
        groups: List[ComplexValue] = None,
        roles: List[ComplexValue] = None,
        **kwargs,
    ) -> ServicePrincipal:
        """Create a service principal.

        Creates a new service principal in the Databricks Workspace."""
        request = kwargs.get("request", None)
        if not request:  # request is not given through keyed args
            request = ServicePrincipal(
                active=active,
                application_id=application_id,
                display_name=display_name,
                entitlements=entitlements,
                external_id=external_id,
                groups=groups,
                id=id,
                roles=roles,
            )
        body = request.as_dict()

        json = self._api.do(
            "POST", "/api/2.0/preview/scim/v2/ServicePrincipals", body=body
        )
        return ServicePrincipal.from_dict(json)

    def delete(self, id: str, **kwargs):
        """Delete a service principal.

        Delete a single service principal in the Databricks Workspace."""
        request = kwargs.get("request", None)
        if not request:  # request is not given through keyed args
            request = DeleteServicePrincipalRequest(id=id)

        self._api.do(
            "DELETE", f"/api/2.0/preview/scim/v2/ServicePrincipals/{request.id}"
        )

    def get(self, id: str, **kwargs) -> ServicePrincipal:
        """Get service principal details.

        Gets the details for a single service principal define in the Databricks
        Workspace."""
        request = kwargs.get("request", None)
        if not request:  # request is not given through keyed args
            request = GetServicePrincipalRequest(id=id)

        json = self._api.do(
            "GET", f"/api/2.0/preview/scim/v2/ServicePrincipals/{request.id}"
        )
        return ServicePrincipal.from_dict(json)

    def list(
        self,
        *,
        attributes: str = None,
        count: int = None,
        excluded_attributes: str = None,
        filter: str = None,
        sort_by: str = None,
        sort_order: ListSortOrder = None,
        start_index: int = None,
        **kwargs,
    ) -> ListServicePrincipalResponse:
        """List service principals.

        Gets the set of service principals associated with a Databricks
        Workspace."""
        request = kwargs.get("request", None)
        if not request:  # request is not given through keyed args
            request = ListServicePrincipalsRequest(
                attributes=attributes,
                count=count,
                excluded_attributes=excluded_attributes,
                filter=filter,
                sort_by=sort_by,
                sort_order=sort_order,
                start_index=start_index,
            )

        query = {}
        if attributes:
            query["attributes"] = request.attributes
        if count:
            query["count"] = request.count
        if excluded_attributes:
            query["excludedAttributes"] = request.excluded_attributes
        if filter:
            query["filter"] = request.filter
        if sort_by:
            query["sortBy"] = request.sort_by
        if sort_order:
            query["sortOrder"] = request.sort_order.value
        if start_index:
            query["startIndex"] = request.start_index

        json = self._api.do(
            "GET", "/api/2.0/preview/scim/v2/ServicePrincipals", query=query
        )
        return ListServicePrincipalResponse.from_dict(json)

    def patch(
        self,
        id: str,
        id: str,
        id: str,
        id: str,
        id: str,
        id: str,
        *,
        operations: List[Patch] = None,
        **kwargs,
    ):
        """Update service principal details.

        Partially updates the details of a single service principal in the
        Databricks Workspace."""
        request = kwargs.get("request", None)
        if not request:  # request is not given through keyed args
            request = PartialUpdate(id=id, operations=operations)
        body = request.as_dict()

        self._api.do(
            "PATCH",
            f"/api/2.0/preview/scim/v2/ServicePrincipals/{request.id}",
            body=body,
        )

    def update(
        self,
        id: str,
        id: str,
        *,
        active: bool = None,
        application_id: str = None,
        display_name: str = None,
        entitlements: List[ComplexValue] = None,
        external_id: str = None,
        groups: List[ComplexValue] = None,
        roles: List[ComplexValue] = None,
        **kwargs,
    ):
        """Replace service principal.

        Updates the details of a single service principal.

        This action replaces the existing service principal with the same name."""
        request = kwargs.get("request", None)
        if not request:  # request is not given through keyed args
            request = ServicePrincipal(
                active=active,
                application_id=application_id,
                display_name=display_name,
                entitlements=entitlements,
                external_id=external_id,
                groups=groups,
                id=id,
                roles=roles,
            )
        body = request.as_dict()

        self._api.do(
            "PUT", f"/api/2.0/preview/scim/v2/ServicePrincipals/{request.id}", body=body
        )


class UsersAPI:
    def __init__(self, api_client):
        self._api = api_client

    def create(
        self,
        id: str,
        id: str,
        *,
        active: bool = None,
        display_name: str = None,
        emails: List[ComplexValue] = None,
        entitlements: List[ComplexValue] = None,
        external_id: str = None,
        groups: List[ComplexValue] = None,
        name: Name = None,
        roles: List[ComplexValue] = None,
        user_name: str = None,
        **kwargs,
    ) -> User:
        """Create a new user.

        Creates a new user in the Databricks Workspace. This new user will also
        be added to the Databricks account."""
        request = kwargs.get("request", None)
        if not request:  # request is not given through keyed args
            request = User(
                active=active,
                display_name=display_name,
                emails=emails,
                entitlements=entitlements,
                external_id=external_id,
                groups=groups,
                id=id,
                name=name,
                roles=roles,
                user_name=user_name,
            )
        body = request.as_dict()

        json = self._api.do("POST", "/api/2.0/preview/scim/v2/Users", body=body)
        return User.from_dict(json)

    def delete(self, id: str, **kwargs):
        """Delete a user.

        Deletes a user. Deleting a user from a Databricks Workspace also removes
        objects associated with the user."""
        request = kwargs.get("request", None)
        if not request:  # request is not given through keyed args
            request = DeleteUserRequest(id=id)

        self._api.do("DELETE", f"/api/2.0/preview/scim/v2/Users/{request.id}")

    def get(self, id: str, **kwargs) -> User:
        """Get user details.

        Gets information for a specific user in Databricks Workspace."""
        request = kwargs.get("request", None)
        if not request:  # request is not given through keyed args
            request = GetUserRequest(id=id)

        json = self._api.do("GET", f"/api/2.0/preview/scim/v2/Users/{request.id}")
        return User.from_dict(json)

    def list(
        self,
        *,
        attributes: str = None,
        count: int = None,
        excluded_attributes: str = None,
        filter: str = None,
        sort_by: str = None,
        sort_order: ListSortOrder = None,
        start_index: int = None,
        **kwargs,
    ) -> ListUsersResponse:
        """List users.

        Gets details for all the users associated with a Databricks Workspace."""
        request = kwargs.get("request", None)
        if not request:  # request is not given through keyed args
            request = ListUsersRequest(
                attributes=attributes,
                count=count,
                excluded_attributes=excluded_attributes,
                filter=filter,
                sort_by=sort_by,
                sort_order=sort_order,
                start_index=start_index,
            )

        query = {}
        if attributes:
            query["attributes"] = request.attributes
        if count:
            query["count"] = request.count
        if excluded_attributes:
            query["excludedAttributes"] = request.excluded_attributes
        if filter:
            query["filter"] = request.filter
        if sort_by:
            query["sortBy"] = request.sort_by
        if sort_order:
            query["sortOrder"] = request.sort_order.value
        if start_index:
            query["startIndex"] = request.start_index

        json = self._api.do("GET", "/api/2.0/preview/scim/v2/Users", query=query)
        return ListUsersResponse.from_dict(json)

    def patch(
        self,
        id: str,
        id: str,
        id: str,
        id: str,
        id: str,
        id: str,
        *,
        operations: List[Patch] = None,
        **kwargs,
    ):
        """Update user details.

        Partially updates a user resource by applying the supplied operations on
        specific user attributes."""
        request = kwargs.get("request", None)
        if not request:  # request is not given through keyed args
            request = PartialUpdate(id=id, operations=operations)
        body = request.as_dict()

        self._api.do("PATCH", f"/api/2.0/preview/scim/v2/Users/{request.id}", body=body)

    def update(
        self,
        id: str,
        id: str,
        *,
        active: bool = None,
        display_name: str = None,
        emails: List[ComplexValue] = None,
        entitlements: List[ComplexValue] = None,
        external_id: str = None,
        groups: List[ComplexValue] = None,
        name: Name = None,
        roles: List[ComplexValue] = None,
        user_name: str = None,
        **kwargs,
    ):
        """Replace a user.

        Replaces a user's information with the data supplied in request."""
        request = kwargs.get("request", None)
        if not request:  # request is not given through keyed args
            request = User(
                active=active,
                display_name=display_name,
                emails=emails,
                entitlements=entitlements,
                external_id=external_id,
                groups=groups,
                id=id,
                name=name,
                roles=roles,
                user_name=user_name,
            )
        body = request.as_dict()

        self._api.do("PUT", f"/api/2.0/preview/scim/v2/Users/{request.id}", body=body)
