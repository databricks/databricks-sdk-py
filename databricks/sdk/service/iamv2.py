# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.
# ruff: noqa: F811, F841
# F401 is intentionally NOT covered: `make fmt` uses `ruff check --fix-only`
# to strip the fat-import header below; ignoring F401 would defeat that.

from __future__ import annotations
from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Any, Iterator, Optional


import logging

from databricks.sdk.service._internal import (
    _enum,
    _from_dict,
    _int64,
    _repeated_dict,
    _repeated_enum,
)
from databricks.sdk.common.types.fieldmask import FieldMask


_LOG = logging.getLogger("databricks.sdk")


# all definitions in this file are in alphabetical order


@dataclass
class DirectGroupMember:
    """A user, service principal, or group that's a direct member of a group."""

    principal_id: int
    """The Databricks ID of the member."""

    display_name: Optional[str] = None
    """The member's display name."""

    external_id: Optional[str] = None
    """The ID of the member in your identity provider (IdP)."""

    group_id: Optional[int] = None
    """The Databricks ID of the group."""

    membership_source: Optional[GroupMembershipSource] = None
    """Where the membership comes from."""

    name: Optional[str] = None
    """The resource name of the membership, in one of these formats:
    
    - Account APIs: ``accounts/{account_id}/groups/{group_id}/direct-members/{principal_id}``
    - Workspace APIs: ``groups/{group_id}/direct-members/{principal_id}``"""

    parent: Optional[str] = None
    """The resource name of the group, in one of these formats:
    
    - Account APIs: ``accounts/{account_id}/groups/{group_id}``
    - Workspace APIs: ``groups/{group_id}``"""

    principal_type: Optional[PrincipalType] = None
    """Whether the member is a user, service principal, or group."""

    def as_dict(self) -> dict:
        """Serializes the DirectGroupMember into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.display_name is not None:
            body["display_name"] = self.display_name
        if self.external_id is not None:
            body["external_id"] = self.external_id
        if self.group_id is not None:
            body["group_id"] = self.group_id
        if self.membership_source is not None:
            body["membership_source"] = self.membership_source.value
        if self.name is not None:
            body["name"] = self.name
        if self.parent is not None:
            body["parent"] = self.parent
        if self.principal_id is not None:
            body["principal_id"] = self.principal_id
        if self.principal_type is not None:
            body["principal_type"] = self.principal_type.value
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the DirectGroupMember into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.display_name is not None:
            body["display_name"] = self.display_name
        if self.external_id is not None:
            body["external_id"] = self.external_id
        if self.group_id is not None:
            body["group_id"] = self.group_id
        if self.membership_source is not None:
            body["membership_source"] = self.membership_source
        if self.name is not None:
            body["name"] = self.name
        if self.parent is not None:
            body["parent"] = self.parent
        if self.principal_id is not None:
            body["principal_id"] = self.principal_id
        if self.principal_type is not None:
            body["principal_type"] = self.principal_type
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> DirectGroupMember:
        """Deserializes the DirectGroupMember from a dictionary."""
        return cls(
            display_name=d.get("display_name", None),
            external_id=d.get("external_id", None),
            group_id=_int64(d, "group_id"),
            membership_source=_enum(d, "membership_source", GroupMembershipSource),
            name=d.get("name", None),
            parent=d.get("parent", None),
            principal_id=_int64(d, "principal_id"),
            principal_type=_enum(d, "principal_type", PrincipalType),
        )


class Entitlement(Enum):
    """A permission to use part of a Databricks workspace."""

    ALLOW_CLUSTER_CREATE = "ALLOW_CLUSTER_CREATE"
    ALLOW_INSTANCE_POOL_CREATE = "ALLOW_INSTANCE_POOL_CREATE"
    DATABRICKS_SQL_ACCESS = "DATABRICKS_SQL_ACCESS"
    WORKSPACE_ACCESS = "WORKSPACE_ACCESS"
    WORKSPACE_ADMIN = "WORKSPACE_ADMIN"
    WORKSPACE_CONSUME = "WORKSPACE_CONSUME"


@dataclass
class ExactMatchRule:
    """A rule that matches a group by its ID in your identity provider (IdP)."""

    external_id: str
    """The ID of the group in your IdP, not its Databricks ID. It's matched exactly, including case."""

    def as_dict(self) -> dict:
        """Serializes the ExactMatchRule into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.external_id is not None:
            body["external_id"] = self.external_id
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ExactMatchRule into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.external_id is not None:
            body["external_id"] = self.external_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ExactMatchRule:
        """Deserializes the ExactMatchRule from a dictionary."""
        return cls(external_id=d.get("external_id", None))


@dataclass
class ExternalGroup:
    """A group from your identity provider (IdP), identified by its ID in your IdP. This resource is
    read-only. Getting an external group syncs its name and parent groups from your IdP, and adds it
    to your account if it isn't already there. If your account has group visibility filters, the
    group must match them."""

    account_id: Optional[str] = None
    """The ID of the account that contains the group."""

    display_name: Optional[str] = None
    """The name of the group, from your IdP. It's the same as the group's ``group_name``."""

    external_group_id: Optional[str] = None
    """The ID of the group in your IdP."""

    internal_id: Optional[str] = None
    """The Databricks ID of the group. Use it as the ``group_id`` in the group APIs."""

    name: Optional[str] = None
    """The resource name of the external group, in one of these formats:
    
    - Account APIs: ``accounts/{account_id}/external-groups/{external_group_id}``
    - Workspace APIs: ``external-groups/{external_group_id}``"""

    def as_dict(self) -> dict:
        """Serializes the ExternalGroup into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.account_id is not None:
            body["account_id"] = self.account_id
        if self.display_name is not None:
            body["display_name"] = self.display_name
        if self.external_group_id is not None:
            body["external_group_id"] = self.external_group_id
        if self.internal_id is not None:
            body["internal_id"] = self.internal_id
        if self.name is not None:
            body["name"] = self.name
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ExternalGroup into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.account_id is not None:
            body["account_id"] = self.account_id
        if self.display_name is not None:
            body["display_name"] = self.display_name
        if self.external_group_id is not None:
            body["external_group_id"] = self.external_group_id
        if self.internal_id is not None:
            body["internal_id"] = self.internal_id
        if self.name is not None:
            body["name"] = self.name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ExternalGroup:
        """Deserializes the ExternalGroup from a dictionary."""
        return cls(
            account_id=d.get("account_id", None),
            display_name=d.get("display_name", None),
            external_group_id=d.get("external_group_id", None),
            internal_id=d.get("internal_id", None),
            name=d.get("name", None),
        )


@dataclass
class ExternalServicePrincipal:
    """A service principal from your identity provider (IdP), identified by its ID in your IdP. This
    resource is read-only and requires Microsoft Entra ID as your IdP. Getting an external service
    principal syncs its details and group memberships from your IdP, and adds it to your account if
    it isn't already there."""

    account_id: Optional[str] = None
    """The ID of the account that contains the service principal."""

    account_sp_status: Optional[State] = None
    """Whether the service principal is active in the account."""

    application_id: Optional[str] = None
    """The service principal's application ID, from your IdP."""

    display_name: Optional[str] = None
    """The service principal's display name, from your IdP."""

    external_service_principal_id: Optional[str] = None
    """The ID of the service principal in your IdP."""

    internal_id: Optional[str] = None
    """The Databricks ID of the service principal. Use it as the ``service_principal_id`` in the
    service principal APIs."""

    name: Optional[str] = None
    """The resource name of the external service principal, in one of these formats:
    
    - Account APIs:
      ``accounts/{account_id}/external-service-principals/{external_service_principal_id}``
    - Workspace APIs: ``external-service-principals/{external_service_principal_id}``"""

    def as_dict(self) -> dict:
        """Serializes the ExternalServicePrincipal into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.account_id is not None:
            body["account_id"] = self.account_id
        if self.account_sp_status is not None:
            body["account_sp_status"] = self.account_sp_status.value
        if self.application_id is not None:
            body["application_id"] = self.application_id
        if self.display_name is not None:
            body["display_name"] = self.display_name
        if self.external_service_principal_id is not None:
            body["external_service_principal_id"] = self.external_service_principal_id
        if self.internal_id is not None:
            body["internal_id"] = self.internal_id
        if self.name is not None:
            body["name"] = self.name
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ExternalServicePrincipal into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.account_id is not None:
            body["account_id"] = self.account_id
        if self.account_sp_status is not None:
            body["account_sp_status"] = self.account_sp_status
        if self.application_id is not None:
            body["application_id"] = self.application_id
        if self.display_name is not None:
            body["display_name"] = self.display_name
        if self.external_service_principal_id is not None:
            body["external_service_principal_id"] = self.external_service_principal_id
        if self.internal_id is not None:
            body["internal_id"] = self.internal_id
        if self.name is not None:
            body["name"] = self.name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ExternalServicePrincipal:
        """Deserializes the ExternalServicePrincipal from a dictionary."""
        return cls(
            account_id=d.get("account_id", None),
            account_sp_status=_enum(d, "account_sp_status", State),
            application_id=d.get("application_id", None),
            display_name=d.get("display_name", None),
            external_service_principal_id=d.get("external_service_principal_id", None),
            internal_id=d.get("internal_id", None),
            name=d.get("name", None),
        )


@dataclass
class ExternalUser:
    """A user from your identity provider (IdP), identified by their ID in your IdP. This resource is
    read-only. Getting an external user syncs the user's details and group memberships from your
    IdP, and adds the user to your account if they aren't already there."""

    account_id: Optional[str] = None
    """The ID of the account that contains the user."""

    account_user_status: Optional[State] = None
    """Whether the user is active in the account."""

    display_name: Optional[str] = None
    """The user's given and family names from your IdP, separated by a space."""

    external_user_id: Optional[str] = None
    """The ID of the user in your IdP."""

    full_name: Optional[FullName] = None
    """The user's name, from your IdP."""

    internal_id: Optional[str] = None
    """The Databricks ID of the user. Use it as the ``user_id`` in the user APIs."""

    name: Optional[str] = None
    """The resource name of the external user, in one of these formats:
    
    - Account APIs: ``accounts/{account_id}/external-users/{external_user_id}``
    - Workspace APIs: ``external-users/{external_user_id}``"""

    username: Optional[str] = None
    """The user's username, which is their email address."""

    def as_dict(self) -> dict:
        """Serializes the ExternalUser into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.account_id is not None:
            body["account_id"] = self.account_id
        if self.account_user_status is not None:
            body["account_user_status"] = self.account_user_status.value
        if self.display_name is not None:
            body["display_name"] = self.display_name
        if self.external_user_id is not None:
            body["external_user_id"] = self.external_user_id
        if self.full_name:
            body["full_name"] = self.full_name.as_dict()
        if self.internal_id is not None:
            body["internal_id"] = self.internal_id
        if self.name is not None:
            body["name"] = self.name
        if self.username is not None:
            body["username"] = self.username
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ExternalUser into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.account_id is not None:
            body["account_id"] = self.account_id
        if self.account_user_status is not None:
            body["account_user_status"] = self.account_user_status
        if self.display_name is not None:
            body["display_name"] = self.display_name
        if self.external_user_id is not None:
            body["external_user_id"] = self.external_user_id
        if self.full_name:
            body["full_name"] = self.full_name
        if self.internal_id is not None:
            body["internal_id"] = self.internal_id
        if self.name is not None:
            body["name"] = self.name
        if self.username is not None:
            body["username"] = self.username
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ExternalUser:
        """Deserializes the ExternalUser from a dictionary."""
        return cls(
            account_id=d.get("account_id", None),
            account_user_status=_enum(d, "account_user_status", State),
            display_name=d.get("display_name", None),
            external_user_id=d.get("external_user_id", None),
            full_name=_from_dict(d, "full_name", FullName),
            internal_id=d.get("internal_id", None),
            name=d.get("name", None),
            username=d.get("username", None),
        )


@dataclass
class FullName:
    """A user's name, from your identity provider (IdP)."""

    family_name: Optional[str] = None
    """The user's family (last) name."""

    given_name: Optional[str] = None
    """The user's given (first) name."""

    def as_dict(self) -> dict:
        """Serializes the FullName into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.family_name is not None:
            body["family_name"] = self.family_name
        if self.given_name is not None:
            body["given_name"] = self.given_name
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the FullName into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.family_name is not None:
            body["family_name"] = self.family_name
        if self.given_name is not None:
            body["given_name"] = self.given_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> FullName:
        """Deserializes the FullName from a dictionary."""
        return cls(family_name=d.get("family_name", None), given_name=d.get("given_name", None))


@dataclass
class Group:
    """A group in your Databricks account."""

    account_id: Optional[str] = None
    """The ID of the account that contains the group."""

    external_id: Optional[str] = None
    """The ID of the group in your identity provider (IdP)."""

    group_id: Optional[str] = None
    """The Databricks ID of the group."""

    group_name: Optional[str] = None
    """The name of the group."""

    name: Optional[str] = None
    """The resource name of the group, in one of these formats:
    
    - Account APIs: ``accounts/{account_id}/groups/{group_id}``
    - Workspace APIs: ``groups/{group_id}``"""

    parent: Optional[str] = None
    """The resource name of the account that contains the group, in the format
    ``accounts/{account_id}``. Workspace APIs return the same format."""

    def as_dict(self) -> dict:
        """Serializes the Group into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.account_id is not None:
            body["account_id"] = self.account_id
        if self.external_id is not None:
            body["external_id"] = self.external_id
        if self.group_id is not None:
            body["group_id"] = self.group_id
        if self.group_name is not None:
            body["group_name"] = self.group_name
        if self.name is not None:
            body["name"] = self.name
        if self.parent is not None:
            body["parent"] = self.parent
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the Group into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.account_id is not None:
            body["account_id"] = self.account_id
        if self.external_id is not None:
            body["external_id"] = self.external_id
        if self.group_id is not None:
            body["group_id"] = self.group_id
        if self.group_name is not None:
            body["group_name"] = self.group_name
        if self.name is not None:
            body["name"] = self.name
        if self.parent is not None:
            body["parent"] = self.parent
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> Group:
        """Deserializes the Group from a dictionary."""
        return cls(
            account_id=d.get("account_id", None),
            external_id=d.get("external_id", None),
            group_id=d.get("group_id", None),
            group_name=d.get("group_name", None),
            name=d.get("name", None),
            parent=d.get("parent", None),
        )


class GroupMembershipSource(Enum):
    """Where a group membership comes from."""

    IDENTITY_PROVIDER = "IDENTITY_PROVIDER"
    INTERNAL = "INTERNAL"


@dataclass
class IdentityVisibilityFilter:
    """An account-level rule that controls which groups from your identity provider (IdP) can be found
    in directory search and group pickers when automatic identity management is on. Filters apply to
    every workspace in the account.

    If you have no group filters, all groups are visible. Otherwise, a group is visible if it or any
    of its parent groups matches at least one filter. A group is also visible if it or any of its
    parent groups is already in your account. Local Databricks groups are always visible.

    You can only create group filters. Filters don't affect provisioning or sign-in for users and
    service principals. You can't change a filter: to change a rule, delete it and create a new one."""

    principal_type: PrincipalType
    """The type of principal the filter applies to. Set it to ``GROUP``. Other types aren't supported."""

    exact: Optional[ExactMatchRule] = None
    """Matches a group by its ID in your IdP."""

    name: Optional[str] = None
    """The resource name of the filter, in the format
    ``accounts/{account_id}/identity-visibility-filters/{identity_visibility_filter_id}``."""

    prefix: Optional[PrefixMatchRule] = None
    """Matches groups whose display name starts with a prefix."""

    regex: Optional[RegexMatchRule] = None
    """Matches groups whose display name matches a regular expression."""

    def as_dict(self) -> dict:
        """Serializes the IdentityVisibilityFilter into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.exact:
            body["exact"] = self.exact.as_dict()
        if self.name is not None:
            body["name"] = self.name
        if self.prefix:
            body["prefix"] = self.prefix.as_dict()
        if self.principal_type is not None:
            body["principal_type"] = self.principal_type.value
        if self.regex:
            body["regex"] = self.regex.as_dict()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the IdentityVisibilityFilter into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.exact:
            body["exact"] = self.exact
        if self.name is not None:
            body["name"] = self.name
        if self.prefix:
            body["prefix"] = self.prefix
        if self.principal_type is not None:
            body["principal_type"] = self.principal_type
        if self.regex:
            body["regex"] = self.regex
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> IdentityVisibilityFilter:
        """Deserializes the IdentityVisibilityFilter from a dictionary."""
        return cls(
            exact=_from_dict(d, "exact", ExactMatchRule),
            name=d.get("name", None),
            prefix=_from_dict(d, "prefix", PrefixMatchRule),
            principal_type=_enum(d, "principal_type", PrincipalType),
            regex=_from_dict(d, "regex", RegexMatchRule),
        )


@dataclass
class ListDirectGroupMembersResponse:
    """A page of direct members of a group."""

    direct_group_members: Optional[List[DirectGroupMember]] = None
    """The members on this page."""

    next_page_token: Optional[str] = None
    """The token for the next page. Not set on the last page."""

    def as_dict(self) -> dict:
        """Serializes the ListDirectGroupMembersResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.direct_group_members:
            body["direct_group_members"] = [v.as_dict() for v in self.direct_group_members]
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ListDirectGroupMembersResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.direct_group_members:
            body["direct_group_members"] = self.direct_group_members
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ListDirectGroupMembersResponse:
        """Deserializes the ListDirectGroupMembersResponse from a dictionary."""
        return cls(
            direct_group_members=_repeated_dict(d, "direct_group_members", DirectGroupMember),
            next_page_token=d.get("next_page_token", None),
        )


@dataclass
class ListGroupsResponse:
    """A page of groups."""

    groups: Optional[List[Group]] = None
    """The groups on this page."""

    next_page_token: Optional[str] = None
    """The token for the next page. Not set on the last page."""

    def as_dict(self) -> dict:
        """Serializes the ListGroupsResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.groups:
            body["groups"] = [v.as_dict() for v in self.groups]
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ListGroupsResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.groups:
            body["groups"] = self.groups
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ListGroupsResponse:
        """Deserializes the ListGroupsResponse from a dictionary."""
        return cls(groups=_repeated_dict(d, "groups", Group), next_page_token=d.get("next_page_token", None))


@dataclass
class ListIdentityVisibilityFiltersResponse:
    """A page of group visibility filters."""

    identity_visibility_filters: Optional[List[IdentityVisibilityFilter]] = None
    """The filters on this page. These are the rules, not the groups they match."""

    next_page_token: Optional[str] = None
    """The token for the next page. Not set on the last page."""

    def as_dict(self) -> dict:
        """Serializes the ListIdentityVisibilityFiltersResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.identity_visibility_filters:
            body["identity_visibility_filters"] = [v.as_dict() for v in self.identity_visibility_filters]
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ListIdentityVisibilityFiltersResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.identity_visibility_filters:
            body["identity_visibility_filters"] = self.identity_visibility_filters
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ListIdentityVisibilityFiltersResponse:
        """Deserializes the ListIdentityVisibilityFiltersResponse from a dictionary."""
        return cls(
            identity_visibility_filters=_repeated_dict(d, "identity_visibility_filters", IdentityVisibilityFilter),
            next_page_token=d.get("next_page_token", None),
        )


@dataclass
class ListServicePrincipalsResponse:
    """A page of service principals."""

    next_page_token: Optional[str] = None
    """The token for the next page. Not set on the last page."""

    service_principals: Optional[List[ServicePrincipal]] = None
    """The service principals on this page."""

    def as_dict(self) -> dict:
        """Serializes the ListServicePrincipalsResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        if self.service_principals:
            body["service_principals"] = [v.as_dict() for v in self.service_principals]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ListServicePrincipalsResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        if self.service_principals:
            body["service_principals"] = self.service_principals
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ListServicePrincipalsResponse:
        """Deserializes the ListServicePrincipalsResponse from a dictionary."""
        return cls(
            next_page_token=d.get("next_page_token", None),
            service_principals=_repeated_dict(d, "service_principals", ServicePrincipal),
        )


@dataclass
class ListTransitiveParentGroupsResponse:
    """A page of the groups a principal belongs to."""

    next_page_token: Optional[str] = None
    """The token for the next page. Not set on the last page."""

    transitive_parent_groups: Optional[List[TransitiveParentGroup]] = None
    """The groups on this page."""

    def as_dict(self) -> dict:
        """Serializes the ListTransitiveParentGroupsResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        if self.transitive_parent_groups:
            body["transitive_parent_groups"] = [v.as_dict() for v in self.transitive_parent_groups]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ListTransitiveParentGroupsResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        if self.transitive_parent_groups:
            body["transitive_parent_groups"] = self.transitive_parent_groups
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ListTransitiveParentGroupsResponse:
        """Deserializes the ListTransitiveParentGroupsResponse from a dictionary."""
        return cls(
            next_page_token=d.get("next_page_token", None),
            transitive_parent_groups=_repeated_dict(d, "transitive_parent_groups", TransitiveParentGroup),
        )


@dataclass
class ListUsersResponse:
    """A page of users."""

    next_page_token: Optional[str] = None
    """The token for the next page. Not set on the last page."""

    users: Optional[List[User]] = None
    """The users on this page."""

    def as_dict(self) -> dict:
        """Serializes the ListUsersResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        if self.users:
            body["users"] = [v.as_dict() for v in self.users]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ListUsersResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        if self.users:
            body["users"] = self.users
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ListUsersResponse:
        """Deserializes the ListUsersResponse from a dictionary."""
        return cls(next_page_token=d.get("next_page_token", None), users=_repeated_dict(d, "users", User))


@dataclass
class ListWorkspaceAssignmentDetailsResponse:
    """Response message for listing workspace assignment details."""

    next_page_token: Optional[str] = None
    """A token, which can be sent as page_token to retrieve the next page. If this field is omitted,
    there are no subsequent pages."""

    workspace_assignment_details: Optional[List[WorkspaceAssignmentDetail]] = None

    def as_dict(self) -> dict:
        """Serializes the ListWorkspaceAssignmentDetailsResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        if self.workspace_assignment_details:
            body["workspace_assignment_details"] = [v.as_dict() for v in self.workspace_assignment_details]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ListWorkspaceAssignmentDetailsResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        if self.workspace_assignment_details:
            body["workspace_assignment_details"] = self.workspace_assignment_details
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ListWorkspaceAssignmentDetailsResponse:
        """Deserializes the ListWorkspaceAssignmentDetailsResponse from a dictionary."""
        return cls(
            next_page_token=d.get("next_page_token", None),
            workspace_assignment_details=_repeated_dict(d, "workspace_assignment_details", WorkspaceAssignmentDetail),
        )


@dataclass
class ListWorkspaceAssignmentsResponse:
    """A page of workspace assignments."""

    next_page_token: Optional[str] = None
    """The token for the next page. Not set on the last page."""

    workspace_assignments: Optional[List[WorkspaceAssignment]] = None
    """The assignments on this page."""

    def as_dict(self) -> dict:
        """Serializes the ListWorkspaceAssignmentsResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        if self.workspace_assignments:
            body["workspace_assignments"] = [v.as_dict() for v in self.workspace_assignments]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ListWorkspaceAssignmentsResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        if self.workspace_assignments:
            body["workspace_assignments"] = self.workspace_assignments
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ListWorkspaceAssignmentsResponse:
        """Deserializes the ListWorkspaceAssignmentsResponse from a dictionary."""
        return cls(
            next_page_token=d.get("next_page_token", None),
            workspace_assignments=_repeated_dict(d, "workspace_assignments", WorkspaceAssignment),
        )


@dataclass
class PrefixMatchRule:
    """A rule that matches groups whose display name starts with a prefix. Matching is case-sensitive.
    For example, the prefix ``data-`` matches ``data-platform``."""

    display_name_prefix: str
    """The prefix to match. It must contain at least one non-whitespace character. Leading and trailing
    spaces are kept."""

    def as_dict(self) -> dict:
        """Serializes the PrefixMatchRule into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.display_name_prefix is not None:
            body["display_name_prefix"] = self.display_name_prefix
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the PrefixMatchRule into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.display_name_prefix is not None:
            body["display_name_prefix"] = self.display_name_prefix
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> PrefixMatchRule:
        """Deserializes the PrefixMatchRule from a dictionary."""
        return cls(display_name_prefix=d.get("display_name_prefix", None))


class PrincipalType(Enum):
    """The type of a principal."""

    GROUP = "GROUP"
    SERVICE_PRINCIPAL = "SERVICE_PRINCIPAL"
    USER = "USER"


@dataclass
class RegexMatchRule:
    """A rule that matches groups whose whole display name matches an RE2 regular expression. Matching
    is case-sensitive. To match part of a name, add ``.*``, for example ``.*-admins``."""

    display_name_regex: str
    """The RE2 regular expression to match against the whole display name. At most 255 characters."""

    def as_dict(self) -> dict:
        """Serializes the RegexMatchRule into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.display_name_regex is not None:
            body["display_name_regex"] = self.display_name_regex
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the RegexMatchRule into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.display_name_regex is not None:
            body["display_name_regex"] = self.display_name_regex
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> RegexMatchRule:
        """Deserializes the RegexMatchRule from a dictionary."""
        return cls(display_name_regex=d.get("display_name_regex", None))


@dataclass
class ResolveGroupResponse:
    """The response to resolving a group."""

    group: Optional[Group] = None
    """The resolved group."""

    def as_dict(self) -> dict:
        """Serializes the ResolveGroupResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.group:
            body["group"] = self.group.as_dict()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ResolveGroupResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.group:
            body["group"] = self.group
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ResolveGroupResponse:
        """Deserializes the ResolveGroupResponse from a dictionary."""
        return cls(group=_from_dict(d, "group", Group))


@dataclass
class ResolveServicePrincipalResponse:
    """The response to resolving a service principal."""

    service_principal: Optional[ServicePrincipal] = None
    """The resolved service principal."""

    def as_dict(self) -> dict:
        """Serializes the ResolveServicePrincipalResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.service_principal:
            body["service_principal"] = self.service_principal.as_dict()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ResolveServicePrincipalResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.service_principal:
            body["service_principal"] = self.service_principal
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ResolveServicePrincipalResponse:
        """Deserializes the ResolveServicePrincipalResponse from a dictionary."""
        return cls(service_principal=_from_dict(d, "service_principal", ServicePrincipal))


@dataclass
class ResolveUserResponse:
    """The response to resolving a user."""

    user: Optional[User] = None
    """The resolved user."""

    def as_dict(self) -> dict:
        """Serializes the ResolveUserResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.user:
            body["user"] = self.user.as_dict()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ResolveUserResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.user:
            body["user"] = self.user
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ResolveUserResponse:
        """Deserializes the ResolveUserResponse from a dictionary."""
        return cls(user=_from_dict(d, "user", User))


@dataclass
class ServicePrincipal:
    """A service principal in your Databricks account."""

    display_name: str
    """The service principal's display name."""

    account_sp_status: State
    """Whether the service principal is active in the account."""

    account_id: Optional[str] = None
    """The ID of the account that contains the service principal."""

    application_id: Optional[str] = None
    """The service principal's application ID, a UUID. If you don't set it when you create the service
    principal, Databricks generates one. It must be unique in the account and can't be changed."""

    external_id: Optional[str] = None
    """The ID of the service principal in your identity provider (IdP)."""

    name: Optional[str] = None
    """The resource name of the service principal, in one of these formats:
    
    - Account APIs: ``accounts/{account_id}/service-principals/{service_principal_id}``
    - Workspace APIs: ``service-principals/{service_principal_id}``"""

    parent: Optional[str] = None
    """The resource name of the account that contains the service principal, in the format
    ``accounts/{account_id}``. Workspace APIs return the same format."""

    service_principal_id: Optional[str] = None
    """The Databricks ID of the service principal."""

    def as_dict(self) -> dict:
        """Serializes the ServicePrincipal into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.account_id is not None:
            body["account_id"] = self.account_id
        if self.account_sp_status is not None:
            body["account_sp_status"] = self.account_sp_status.value
        if self.application_id is not None:
            body["application_id"] = self.application_id
        if self.display_name is not None:
            body["display_name"] = self.display_name
        if self.external_id is not None:
            body["external_id"] = self.external_id
        if self.name is not None:
            body["name"] = self.name
        if self.parent is not None:
            body["parent"] = self.parent
        if self.service_principal_id is not None:
            body["service_principal_id"] = self.service_principal_id
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ServicePrincipal into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.account_id is not None:
            body["account_id"] = self.account_id
        if self.account_sp_status is not None:
            body["account_sp_status"] = self.account_sp_status
        if self.application_id is not None:
            body["application_id"] = self.application_id
        if self.display_name is not None:
            body["display_name"] = self.display_name
        if self.external_id is not None:
            body["external_id"] = self.external_id
        if self.name is not None:
            body["name"] = self.name
        if self.parent is not None:
            body["parent"] = self.parent
        if self.service_principal_id is not None:
            body["service_principal_id"] = self.service_principal_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ServicePrincipal:
        """Deserializes the ServicePrincipal from a dictionary."""
        return cls(
            account_id=d.get("account_id", None),
            account_sp_status=_enum(d, "account_sp_status", State),
            application_id=d.get("application_id", None),
            display_name=d.get("display_name", None),
            external_id=d.get("external_id", None),
            name=d.get("name", None),
            parent=d.get("parent", None),
            service_principal_id=d.get("service_principal_id", None),
        )


class State(Enum):
    """Whether a user or service principal is active in an account or workspace."""

    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"


@dataclass
class TransitiveParentGroup:
    """A group that a principal belongs to, either directly or through another group."""

    account_id: Optional[str] = None
    """The ID of the account that contains the group."""

    external_id: Optional[str] = None
    """The ID of the group in your identity provider (IdP)."""

    group_id: Optional[str] = None
    """The Databricks ID of the group."""

    name: Optional[str] = None
    """The resource name of the parent group, in one of these formats:
    
    - Account APIs:
      ``accounts/{account_id}/principals/{principal_id}/transitive-parent-groups/{group_id}``
    - Workspace APIs: ``principals/{principal_id}/transitive-parent-groups/{group_id}``"""

    def as_dict(self) -> dict:
        """Serializes the TransitiveParentGroup into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.account_id is not None:
            body["account_id"] = self.account_id
        if self.external_id is not None:
            body["external_id"] = self.external_id
        if self.group_id is not None:
            body["group_id"] = self.group_id
        if self.name is not None:
            body["name"] = self.name
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the TransitiveParentGroup into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.account_id is not None:
            body["account_id"] = self.account_id
        if self.external_id is not None:
            body["external_id"] = self.external_id
        if self.group_id is not None:
            body["group_id"] = self.group_id
        if self.name is not None:
            body["name"] = self.name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> TransitiveParentGroup:
        """Deserializes the TransitiveParentGroup from a dictionary."""
        return cls(
            account_id=d.get("account_id", None),
            external_id=d.get("external_id", None),
            group_id=d.get("group_id", None),
            name=d.get("name", None),
        )


@dataclass
class User:
    """A user in your Databricks account."""

    username: str
    """The user's username, which is their email address. It can't be changed after the user is
    created."""

    full_name: UserFullName
    """The user's name."""

    account_user_status: State
    """Whether the user is active in the account. New users are active unless you set this to
    ``INACTIVE``."""

    account_id: Optional[str] = None
    """The ID of the account that contains the user."""

    external_id: Optional[str] = None
    """The ID of the user in your identity provider (IdP)."""

    name: Optional[str] = None
    """The resource name of the user, in one of these formats:
    
    - Account APIs: ``accounts/{account_id}/users/{user_id}``
    - Workspace APIs: ``users/{user_id}``"""

    parent: Optional[str] = None
    """The resource name of the account that contains the user, in the format
    ``accounts/{account_id}``. Workspace APIs return the same format."""

    user_id: Optional[str] = None
    """The Databricks ID of the user."""

    def as_dict(self) -> dict:
        """Serializes the User into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.account_id is not None:
            body["account_id"] = self.account_id
        if self.account_user_status is not None:
            body["account_user_status"] = self.account_user_status.value
        if self.external_id is not None:
            body["external_id"] = self.external_id
        if self.full_name:
            body["full_name"] = self.full_name.as_dict()
        if self.name is not None:
            body["name"] = self.name
        if self.parent is not None:
            body["parent"] = self.parent
        if self.user_id is not None:
            body["user_id"] = self.user_id
        if self.username is not None:
            body["username"] = self.username
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the User into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.account_id is not None:
            body["account_id"] = self.account_id
        if self.account_user_status is not None:
            body["account_user_status"] = self.account_user_status
        if self.external_id is not None:
            body["external_id"] = self.external_id
        if self.full_name:
            body["full_name"] = self.full_name
        if self.name is not None:
            body["name"] = self.name
        if self.parent is not None:
            body["parent"] = self.parent
        if self.user_id is not None:
            body["user_id"] = self.user_id
        if self.username is not None:
            body["username"] = self.username
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> User:
        """Deserializes the User from a dictionary."""
        return cls(
            account_id=d.get("account_id", None),
            account_user_status=_enum(d, "account_user_status", State),
            external_id=d.get("external_id", None),
            full_name=_from_dict(d, "full_name", UserFullName),
            name=d.get("name", None),
            parent=d.get("parent", None),
            user_id=d.get("user_id", None),
            username=d.get("username", None),
        )


@dataclass
class UserFullName:
    """A user's name."""

    family_name: Optional[str] = None
    """The user's family (last) name."""

    given_name: Optional[str] = None
    """The user's given (first) name."""

    def as_dict(self) -> dict:
        """Serializes the UserFullName into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.family_name is not None:
            body["family_name"] = self.family_name
        if self.given_name is not None:
            body["given_name"] = self.given_name
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the UserFullName into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.family_name is not None:
            body["family_name"] = self.family_name
        if self.given_name is not None:
            body["given_name"] = self.given_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> UserFullName:
        """Deserializes the UserFullName from a dictionary."""
        return cls(family_name=d.get("family_name", None), given_name=d.get("given_name", None))


@dataclass
class WorkspaceAccessDetail:
    """The details of a principal's access to a workspace."""

    access_type: Optional[WorkspaceAccessDetailAccessType] = None

    account_id: Optional[str] = None
    """The account ID parent of the workspace where the principal has access."""

    name: Optional[str] = None
    """The resource name of the workspace access detail. The format depends on the API that returned
    it:
    
    - Account-scoped:
      accounts/{account_id}/workspaces/{workspace_id}/workspace-access-details/{principal_id}
    - Workspace-scoped: workspace-access-details/{principal_id}"""

    permissions: Optional[List[WorkspacePermission]] = None
    """The permissions granted to the principal in the workspace."""

    principal_id: Optional[int] = None
    """The internal ID of the principal (user/sp/group) in Databricks."""

    principal_type: Optional[PrincipalType] = None

    status: Optional[State] = None
    """The activity status of the principal in the workspace. Not applicable for groups at the moment."""

    workspace_id: Optional[int] = None
    """The workspace ID where the principal has access."""

    def as_dict(self) -> dict:
        """Serializes the WorkspaceAccessDetail into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.access_type is not None:
            body["access_type"] = self.access_type.value
        if self.account_id is not None:
            body["account_id"] = self.account_id
        if self.name is not None:
            body["name"] = self.name
        if self.permissions:
            body["permissions"] = [v.value for v in self.permissions]
        if self.principal_id is not None:
            body["principal_id"] = self.principal_id
        if self.principal_type is not None:
            body["principal_type"] = self.principal_type.value
        if self.status is not None:
            body["status"] = self.status.value
        if self.workspace_id is not None:
            body["workspace_id"] = self.workspace_id
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the WorkspaceAccessDetail into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.access_type is not None:
            body["access_type"] = self.access_type
        if self.account_id is not None:
            body["account_id"] = self.account_id
        if self.name is not None:
            body["name"] = self.name
        if self.permissions:
            body["permissions"] = self.permissions
        if self.principal_id is not None:
            body["principal_id"] = self.principal_id
        if self.principal_type is not None:
            body["principal_type"] = self.principal_type
        if self.status is not None:
            body["status"] = self.status
        if self.workspace_id is not None:
            body["workspace_id"] = self.workspace_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> WorkspaceAccessDetail:
        """Deserializes the WorkspaceAccessDetail from a dictionary."""
        return cls(
            access_type=_enum(d, "access_type", WorkspaceAccessDetailAccessType),
            account_id=d.get("account_id", None),
            name=d.get("name", None),
            permissions=_repeated_enum(d, "permissions", WorkspacePermission),
            principal_id=_int64(d, "principal_id"),
            principal_type=_enum(d, "principal_type", PrincipalType),
            status=_enum(d, "status", State),
            workspace_id=_int64(d, "workspace_id"),
        )


class WorkspaceAccessDetailAccessType(Enum):
    """The type of access the principal has to the workspace."""

    DIRECT = "DIRECT"
    INDIRECT = "INDIRECT"


class WorkspaceAccessDetailView(Enum):
    """Controls what fields are returned in the GetWorkspaceAccessDetail response."""

    BASIC = "BASIC"
    FULL = "FULL"


@dataclass
class WorkspaceAssignment:
    """A principal's direct assignment to a workspace, and the entitlements it grants there.

    Only principals assigned directly to the workspace have an assignment. A principal that gets
    access only through a group doesn't. Creating an assignment gives the principal access to the
    workspace, and deleting it removes that direct access. These APIs replace managing workspace
    assignments through SCIM and the permission assignment APIs. They require a workspace with
    identity federation enabled. You can't assign, change, or unassign principals that Databricks
    manages.

    ``entitlements`` is the only field you set. ``effective_entitlements`` also includes the
    entitlements the principal gets through its groups. An assignment must grant at least one
    entitlement. To remove a principal's direct access, delete the assignment."""

    principal_id: int
    """The Databricks ID of the assigned user, service principal, or group. It can't be changed after
    the assignment is created."""

    account_id: Optional[str] = None
    """The ID of the account that contains the workspace."""

    effective_entitlements: Optional[List[Entitlement]] = None
    """Every entitlement the principal has in the workspace, granted directly or through a group. List
    responses leave it empty."""

    entitlements: Optional[List[Entitlement]] = None
    """The entitlements granted directly by this assignment. Create and update set exactly this list,
    even if the principal also gets some of these entitlements through a group. List responses leave
    it empty."""

    name: Optional[str] = None
    """The resource name of the assignment, in one of these formats:
    
    - Account APIs:
      ``accounts/{account_id}/workspaces/{workspace_id}/workspace-assignments/{principal_id}``
    - Workspace APIs: ``workspace-assignments/{principal_id}``"""

    parent: Optional[str] = None
    """The resource name of the workspace, in the format
    ``accounts/{account_id}/workspaces/{workspace_id}``. Workspace APIs return the same format."""

    principal_type: Optional[PrincipalType] = None
    """Whether the assigned principal is a user, service principal, or group."""

    workspace_id: Optional[int] = None
    """The ID of the workspace."""

    def as_dict(self) -> dict:
        """Serializes the WorkspaceAssignment into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.account_id is not None:
            body["account_id"] = self.account_id
        if self.effective_entitlements:
            body["effective_entitlements"] = [v.value for v in self.effective_entitlements]
        if self.entitlements:
            body["entitlements"] = [v.value for v in self.entitlements]
        if self.name is not None:
            body["name"] = self.name
        if self.parent is not None:
            body["parent"] = self.parent
        if self.principal_id is not None:
            body["principal_id"] = self.principal_id
        if self.principal_type is not None:
            body["principal_type"] = self.principal_type.value
        if self.workspace_id is not None:
            body["workspace_id"] = self.workspace_id
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the WorkspaceAssignment into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.account_id is not None:
            body["account_id"] = self.account_id
        if self.effective_entitlements:
            body["effective_entitlements"] = self.effective_entitlements
        if self.entitlements:
            body["entitlements"] = self.entitlements
        if self.name is not None:
            body["name"] = self.name
        if self.parent is not None:
            body["parent"] = self.parent
        if self.principal_id is not None:
            body["principal_id"] = self.principal_id
        if self.principal_type is not None:
            body["principal_type"] = self.principal_type
        if self.workspace_id is not None:
            body["workspace_id"] = self.workspace_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> WorkspaceAssignment:
        """Deserializes the WorkspaceAssignment from a dictionary."""
        return cls(
            account_id=d.get("account_id", None),
            effective_entitlements=_repeated_enum(d, "effective_entitlements", Entitlement),
            entitlements=_repeated_enum(d, "entitlements", Entitlement),
            name=d.get("name", None),
            parent=d.get("parent", None),
            principal_id=_int64(d, "principal_id"),
            principal_type=_enum(d, "principal_type", PrincipalType),
            workspace_id=_int64(d, "workspace_id"),
        )


@dataclass
class WorkspaceAssignmentDetail:
    """The direct assignment of a provisioned account-level principal (user, service principal, or
    group) to a workspace, together with the entitlements that assignment grants in the workspace.

    This resource covers only principals assigned directly to the workspace. Principals that inherit
    workspace access through a group are not represented here. See WorkspaceAccessDetail and
    WorkspaceIdentityDetail for the effective, direct-or-indirect view. Creating the resource
    assigns the principal to the workspace, and deleting it removes the assignment.

    ``entitlements`` is the only client-settable field. It holds the entitlements granted directly
    on this assignment, including any the principal also holds through a group.
    ``effective_entitlements`` is the read-only union of those and any granted through group
    membership.

    A direct assignment always carries at least one directly-assigned entitlement, because the
    assignment is what grants it. Create and update both reject an empty ``entitlements`` set. To
    remove a principal's assignment entirely, delete the resource.

    This resource replaces workspace assignment previously managed through the workspace SCIM and
    permission-assignment APIs, and is intended for account and workspace admins."""

    principal_id: int
    """The internal ID of the principal (user/sp/group) in Databricks."""

    account_id: Optional[str] = None
    """The account ID parent of the workspace where the principal is assigned"""

    effective_entitlements: Optional[List[Entitlement]] = None
    """Every entitlement the principal holds in this workspace, whether granted directly or through
    group membership. Get responses populate this field. List responses leave it empty."""

    entitlements: Optional[List[Entitlement]] = None
    """Entitlements granted directly to the principal on this workspace. This is the only
    client-settable field. Create and update manage exactly this set, including entitlements the
    principal also holds through a group. List responses leave this field empty. Get a single
    principal to read its entitlements."""

    principal_type: Optional[PrincipalType] = None

    workspace_id: Optional[int] = None
    """The workspace ID where the principal is assigned."""

    def as_dict(self) -> dict:
        """Serializes the WorkspaceAssignmentDetail into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.account_id is not None:
            body["account_id"] = self.account_id
        if self.effective_entitlements:
            body["effective_entitlements"] = [v.value for v in self.effective_entitlements]
        if self.entitlements:
            body["entitlements"] = [v.value for v in self.entitlements]
        if self.principal_id is not None:
            body["principal_id"] = self.principal_id
        if self.principal_type is not None:
            body["principal_type"] = self.principal_type.value
        if self.workspace_id is not None:
            body["workspace_id"] = self.workspace_id
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the WorkspaceAssignmentDetail into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.account_id is not None:
            body["account_id"] = self.account_id
        if self.effective_entitlements:
            body["effective_entitlements"] = self.effective_entitlements
        if self.entitlements:
            body["entitlements"] = self.entitlements
        if self.principal_id is not None:
            body["principal_id"] = self.principal_id
        if self.principal_type is not None:
            body["principal_type"] = self.principal_type
        if self.workspace_id is not None:
            body["workspace_id"] = self.workspace_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> WorkspaceAssignmentDetail:
        """Deserializes the WorkspaceAssignmentDetail from a dictionary."""
        return cls(
            account_id=d.get("account_id", None),
            effective_entitlements=_repeated_enum(d, "effective_entitlements", Entitlement),
            entitlements=_repeated_enum(d, "entitlements", Entitlement),
            principal_id=_int64(d, "principal_id"),
            principal_type=_enum(d, "principal_type", PrincipalType),
            workspace_id=_int64(d, "workspace_id"),
        )


@dataclass
class WorkspaceIdentityDetail:
    """A user, service principal, or group's status in a workspace, and whether it has access to the
    workspace directly or through a group. Update it to activate or deactivate a user or service
    principal in the workspace."""

    assignment_type: Optional[WorkspaceIdentityDetailAssignmentType] = None
    """Whether the principal is assigned to the workspace directly or has access through a group."""

    name: Optional[str] = None
    """The resource name of the workspace identity detail, in the format
    ``principals/{principal_id}/workspace-identity-detail``."""

    principal_id: Optional[int] = None
    """The Databricks ID of the user, service principal, or group."""

    principal_type: Optional[PrincipalType] = None
    """Whether the principal is a user, service principal, or group."""

    workspace_identity_status: Optional[State] = None
    """Whether the principal is active in the workspace. Groups are always ``ACTIVE``."""

    def as_dict(self) -> dict:
        """Serializes the WorkspaceIdentityDetail into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.assignment_type is not None:
            body["assignment_type"] = self.assignment_type.value
        if self.name is not None:
            body["name"] = self.name
        if self.principal_id is not None:
            body["principal_id"] = self.principal_id
        if self.principal_type is not None:
            body["principal_type"] = self.principal_type.value
        if self.workspace_identity_status is not None:
            body["workspace_identity_status"] = self.workspace_identity_status.value
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the WorkspaceIdentityDetail into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.assignment_type is not None:
            body["assignment_type"] = self.assignment_type
        if self.name is not None:
            body["name"] = self.name
        if self.principal_id is not None:
            body["principal_id"] = self.principal_id
        if self.principal_type is not None:
            body["principal_type"] = self.principal_type
        if self.workspace_identity_status is not None:
            body["workspace_identity_status"] = self.workspace_identity_status
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> WorkspaceIdentityDetail:
        """Deserializes the WorkspaceIdentityDetail from a dictionary."""
        return cls(
            assignment_type=_enum(d, "assignment_type", WorkspaceIdentityDetailAssignmentType),
            name=d.get("name", None),
            principal_id=_int64(d, "principal_id"),
            principal_type=_enum(d, "principal_type", PrincipalType),
            workspace_identity_status=_enum(d, "workspace_identity_status", State),
        )


class WorkspaceIdentityDetailAssignmentType(Enum):
    """How a principal has access to a workspace."""

    DIRECT = "DIRECT"
    INDIRECT = "INDIRECT"


class WorkspacePermission(Enum):
    """The type of permission a principal has to a workspace (admin/user)."""

    ADMIN_PERMISSION = "ADMIN_PERMISSION"
    USER_PERMISSION = "USER_PERMISSION"


class AccountIamV2API:
    """These APIs are used to manage identities and the workspace access of these identities in Databricks."""

    def __init__(self, api_client):
        self._api = api_client

    def create_direct_group_member(self, parent: str, direct_group_member: DirectGroupMember) -> DirectGroupMember:
        """Adds a user, service principal, or group as a direct member of a group.

        If automatic identity management is on and the group has an ``external_id``, its members come from
        your identity provider and can't be changed in Databricks.

        :param parent: str
          The resource name of the group to add the member to, in the format
          ``accounts/{account_id}/groups/{group_id}``.
        :param direct_group_member: :class:`DirectGroupMember`
          The member to add. Set its ``principal_id``.

        :returns: :class:`DirectGroupMember`
        """

        body = direct_group_member.as_dict()
        query = {}
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do("POST", f"/api/2.0/identity/{parent}/direct-members", body=body, headers=headers)
        return DirectGroupMember.from_dict(res)

    def create_group(self, parent: str, group: Group) -> Group:
        """Creates a local group, which is a group that isn't synced from your identity provider (IdP). You
        become a manager of the new group.

        If automatic identity management is on, you can't set ``external_id``. To add a group from your IdP,
        get it as an external group instead.

        :param parent: str
          The resource name of the account to create the group in, in the format ``accounts/{account_id}``.
        :param group: :class:`Group`
          The group to create.

        :returns: :class:`Group`
        """

        body = group.as_dict()
        query = {}
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do("POST", f"/api/2.0/identity/{parent}/groups", body=body, headers=headers)
        return Group.from_dict(res)

    def create_identity_visibility_filter(
        self,
        parent: str,
        identity_visibility_filter: IdentityVisibilityFilter,
        *,
        identity_visibility_filter_id: Optional[str] = None,
    ) -> IdentityVisibilityFilter:
        """Creates a group visibility filter. It applies to every workspace in the account.

        Returns ``ALREADY_EXISTS`` if a filter with the same ID, or the same type and match value, already
        exists. Returns ``RESOURCE_EXHAUSTED`` if the account already has the maximum number of filters of
        that type. You can't change a filter: to change a rule, delete it and create a new one.

        :param parent: str
          The resource name of the account, in the format ``accounts/{account_id}``.
        :param identity_visibility_filter: :class:`IdentityVisibilityFilter`
          The filter to create. Set ``principal_type`` to ``GROUP`` and exactly one of ``exact``, ``prefix``,
          or ``regex``. Databricks sets ``name``, so any value you set is ignored.
        :param identity_visibility_filter_id: str (optional)
          The ID to give the filter, which becomes the last part of its resource name. If you leave it empty,
          Databricks generates one. It can't contain ``/``.

        :returns: :class:`IdentityVisibilityFilter`
        """

        body = identity_visibility_filter.as_dict()
        query = {}
        if identity_visibility_filter_id is not None:
            query["identity_visibility_filter_id"] = identity_visibility_filter_id
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do(
            "POST", f"/api/2.0/identity/{parent}/identity-visibility-filters", query=query, body=body, headers=headers
        )
        return IdentityVisibilityFilter.from_dict(res)

    def create_service_principal(self, parent: str, service_principal: ServicePrincipal) -> ServicePrincipal:
        """Creates a local service principal, which is a service principal that isn't synced from your identity
        provider (IdP).

        If automatic identity management is on, you can't set ``external_id``. To add a service principal from
        your IdP, get it as an external service principal instead.

        :param parent: str
          The resource name of the account to create the service principal in, in the format
          ``accounts/{account_id}``.
        :param service_principal: :class:`ServicePrincipal`
          The service principal to create.

        :returns: :class:`ServicePrincipal`
        """

        body = service_principal.as_dict()
        query = {}
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do("POST", f"/api/2.0/identity/{parent}/service-principals", body=body, headers=headers)
        return ServicePrincipal.from_dict(res)

    def create_user(self, parent: str, user: User) -> User:
        """Creates a local user, which is a user that isn't synced from your identity provider (IdP).

        If automatic identity management is on, you can't set ``external_id``. To add a user from your IdP,
        get them as an external user instead.

        :param parent: str
          The resource name of the account to create the user in, in the format ``accounts/{account_id}``.
        :param user: :class:`User`
          The user to create.

        :returns: :class:`User`
        """

        body = user.as_dict()
        query = {}
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do("POST", f"/api/2.0/identity/{parent}/users", body=body, headers=headers)
        return User.from_dict(res)

    def create_workspace_assignment(
        self, parent: str, workspace_assignment: WorkspaceAssignment
    ) -> WorkspaceAssignment:
        """Assigns a user, service principal, or group directly to a workspace with the given entitlements.
        Returns an error if the principal is already assigned directly.

        Entitlements are granted one at a time. If the request fails partway through, the principal stays
        assigned with only some of the entitlements. Get the assignment afterwards to check which were
        granted.

        :param parent: str
          The resource name of the workspace, in the format
          ``accounts/{account_id}/workspaces/{workspace_id}``.
        :param workspace_assignment: :class:`WorkspaceAssignment`
          The assignment to create. Set its ``principal_id`` and ``entitlements``.

        :returns: :class:`WorkspaceAssignment`
        """

        body = workspace_assignment.as_dict()
        query = {}
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do("POST", f"/api/2.0/identity/{parent}/workspace-assignments", body=body, headers=headers)
        return WorkspaceAssignment.from_dict(res)

    def create_workspace_assignment_detail(
        self, workspace_id: int, workspace_assignment_detail: WorkspaceAssignmentDetail
    ) -> WorkspaceAssignmentDetail:
        """Creates a workspace assignment detail for a principal.

        :param workspace_id: int
          Required. The workspace ID for which the workspace assignment detail is being created.
        :param workspace_assignment_detail: :class:`WorkspaceAssignmentDetail`
          Required. Workspace assignment detail to be created in Databricks.

        :returns: :class:`WorkspaceAssignmentDetail`
        """

        body = workspace_assignment_detail.as_dict()
        query = {}
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do(
            "POST",
            f"/api/2.0/identity/accounts/{self._api.account_id}/workspaces/{workspace_id}/workspace-assignment-details",
            body=body,
            headers=headers,
        )
        return WorkspaceAssignmentDetail.from_dict(res)

    def delete_direct_group_member(self, name: str):
        """Removes a direct member from a group.

        If automatic identity management is on and the group has an ``external_id``, its members come from
        your identity provider and can't be changed in Databricks.

        :param name: str
          The resource name of the membership, in the format
          ``accounts/{account_id}/groups/{group_id}/direct-members/{principal_id}``.


        """

        headers = {
            "Accept": "application/json",
        }

        self._api.do("DELETE", f"/api/2.0/identity/{name}", headers=headers)

    def delete_group(self, name: str):
        """Deletes a group from your account and removes it from the workspaces it's assigned to.

        :param name: str
          The resource name of the group, in the format ``accounts/{account_id}/groups/{group_id}``.


        """

        headers = {
            "Accept": "application/json",
        }

        self._api.do("DELETE", f"/api/2.0/identity/{name}", headers=headers)

    def delete_identity_visibility_filter(self, name: str):
        """Deletes a group visibility filter. Deleting a filter doesn't delete groups or remove access. Groups
        that only this filter matched stop being visible, unless they or a parent group are already in your
        account. If no group filters remain, all groups become visible again. Deleting a filter that doesn't
        exist succeeds.

        :param name: str
          The resource name of the filter, in the format
          ``accounts/{account_id}/identity-visibility-filters/{identity_visibility_filter_id}``.


        """

        headers = {
            "Accept": "application/json",
        }

        self._api.do("DELETE", f"/api/2.0/identity/{name}", headers=headers)

    def delete_service_principal(self, name: str):
        """Deletes a service principal from your account and removes it from the workspaces it's assigned to. You
        can't delete service principals that Databricks manages.

        :param name: str
          The resource name of the service principal, in the format
          ``accounts/{account_id}/service-principals/{service_principal_id}``.


        """

        headers = {
            "Accept": "application/json",
        }

        self._api.do("DELETE", f"/api/2.0/identity/{name}", headers=headers)

    def delete_user(self, name: str):
        """Deletes a user from your account and removes them from the workspaces they're assigned to.

        :param name: str
          The resource name of the user, in the format ``accounts/{account_id}/users/{user_id}``.


        """

        headers = {
            "Accept": "application/json",
        }

        self._api.do("DELETE", f"/api/2.0/identity/{name}", headers=headers)

    def delete_workspace_assignment(self, name: str):
        """Removes a principal's direct assignment to a workspace and revokes the entitlements it granted. The
        principal keeps any access it gets through groups.

        Entitlements are revoked one at a time. If the request fails partway through, the principal stays
        assigned with some of its entitlements. You can retry the request.

        :param name: str
          The resource name of the assignment, in the format
          ``accounts/{account_id}/workspaces/{workspace_id}/workspace-assignments/{principal_id}``.


        """

        headers = {
            "Accept": "application/json",
        }

        self._api.do("DELETE", f"/api/2.0/identity/{name}", headers=headers)

    def delete_workspace_assignment_detail(self, workspace_id: int, principal_id: int):
        """Deletes a workspace assignment detail for a principal, revoking all of its entitlements. Entitlements
        are revoked one at a time rather than atomically. If the request fails partway through, the principal
        stays assigned with some of its original entitlements. Retrying is safe.

        :param workspace_id: int
          The workspace ID where the principal has access.
        :param principal_id: int
          Required. ID of the principal in Databricks to delete workspace assignment for.


        """

        headers = {
            "Accept": "application/json",
        }

        self._api.do(
            "DELETE",
            f"/api/2.0/identity/accounts/{self._api.account_id}/workspaces/{workspace_id}/workspace-assignment-details/{principal_id}",
            headers=headers,
        )

    def get_direct_group_member(self, name: str) -> DirectGroupMember:
        """Gets a direct member of a group, including where the membership comes from. Returns an error if the
        principal isn't a direct member.

        :param name: str
          The resource name of the membership, in the format
          ``accounts/{account_id}/groups/{group_id}/direct-members/{principal_id}``.

        :returns: :class:`DirectGroupMember`
        """

        headers = {
            "Accept": "application/json",
        }

        res = self._api.do("GET", f"/api/2.0/identity/{name}", headers=headers)
        return DirectGroupMember.from_dict(res)

    def get_external_group(self, name: str) -> ExternalGroup:
        """Gets a group by its ID in your identity provider (IdP) and syncs its name and parent groups from your
        IdP. If the group isn't in your account yet, it's added. Requires automatic identity management. If
        your account has group visibility filters, the group must match them.

        :param name: str
          The resource name of the external group, in the format
          ``accounts/{account_id}/external-groups/{external_group_id}``.

        :returns: :class:`ExternalGroup`
        """

        headers = {
            "Accept": "application/json",
        }

        res = self._api.do("GET", f"/api/2.0/identity/{name}", headers=headers)
        return ExternalGroup.from_dict(res)

    def get_external_service_principal(self, name: str) -> ExternalServicePrincipal:
        """Gets a service principal by its ID in your identity provider (IdP) and syncs its details and group
        memberships from your IdP. If the service principal isn't in your account yet, it's added. Requires
        automatic identity management with Microsoft Entra ID as your IdP.

        :param name: str
          The resource name of the external service principal, in the format
          ``accounts/{account_id}/external-service-principals/{external_service_principal_id}``.

        :returns: :class:`ExternalServicePrincipal`
        """

        headers = {
            "Accept": "application/json",
        }

        res = self._api.do("GET", f"/api/2.0/identity/{name}", headers=headers)
        return ExternalServicePrincipal.from_dict(res)

    def get_external_user(self, name: str) -> ExternalUser:
        """Gets a user by their ID in your identity provider (IdP) and syncs their details and group memberships
        from your IdP. If the user isn't in your account yet, they're added. Requires automatic identity
        management.

        :param name: str
          The resource name of the external user, in the format
          ``accounts/{account_id}/external-users/{external_user_id}``.

        :returns: :class:`ExternalUser`
        """

        headers = {
            "Accept": "application/json",
        }

        res = self._api.do("GET", f"/api/2.0/identity/{name}", headers=headers)
        return ExternalUser.from_dict(res)

    def get_group(self, name: str) -> Group:
        """Gets a group by its Databricks ID.

        :param name: str
          The resource name of the group, in the format ``accounts/{account_id}/groups/{group_id}``.

        :returns: :class:`Group`
        """

        headers = {
            "Accept": "application/json",
        }

        res = self._api.do("GET", f"/api/2.0/identity/{name}", headers=headers)
        return Group.from_dict(res)

    def get_identity_visibility_filter(self, name: str) -> IdentityVisibilityFilter:
        """Gets a group visibility filter. It returns the rule, not the groups it matches.

        :param name: str
          The resource name of the filter, in the format
          ``accounts/{account_id}/identity-visibility-filters/{identity_visibility_filter_id}``.

        :returns: :class:`IdentityVisibilityFilter`
        """

        headers = {
            "Accept": "application/json",
        }

        res = self._api.do("GET", f"/api/2.0/identity/{name}", headers=headers)
        return IdentityVisibilityFilter.from_dict(res)

    def get_service_principal(self, name: str) -> ServicePrincipal:
        """Gets a service principal by its Databricks ID.

        :param name: str
          The resource name of the service principal, in the format
          ``accounts/{account_id}/service-principals/{service_principal_id}``.

        :returns: :class:`ServicePrincipal`
        """

        headers = {
            "Accept": "application/json",
        }

        res = self._api.do("GET", f"/api/2.0/identity/{name}", headers=headers)
        return ServicePrincipal.from_dict(res)

    def get_user(self, name: str) -> User:
        """Gets a user by their Databricks ID.

        :param name: str
          The resource name of the user, in the format ``accounts/{account_id}/users/{user_id}``.

        :returns: :class:`User`
        """

        headers = {
            "Accept": "application/json",
        }

        res = self._api.do("GET", f"/api/2.0/identity/{name}", headers=headers)
        return User.from_dict(res)

    def get_workspace_access_detail(
        self, name: str, *, view: Optional[WorkspaceAccessDetailView] = None
    ) -> WorkspaceAccessDetail:
        """Returns the access details for a principal in a workspace. Allows for checking access details for any
        provisioned principal (user, service principal, or group) in a workspace.

        - Provisioned principal here refers to one that has been synced into Databricks from the customer's
          IdP or added explicitly to Databricks via SCIM/UI. Allows for passing in a "view" parameter to
          control what fields are returned (BASIC by default or FULL).

        :param name: str
          The resource name of the workspace access detail. Format:
          accounts/{account_id}/workspaces/{workspace_id}/workspace-access-details/{principal_id}
        :param view: :class:`WorkspaceAccessDetailView` (optional)
          Controls what fields are returned.

        :returns: :class:`WorkspaceAccessDetail`
        """

        query = {}
        if view is not None:
            query["view"] = view.value
        headers = {
            "Accept": "application/json",
        }

        res = self._api.do("GET", f"/api/2.0/identity/{name}", query=query, headers=headers)
        return WorkspaceAccessDetail.from_dict(res)

    def get_workspace_assignment(self, name: str) -> WorkspaceAssignment:
        """Gets a principal's direct assignment to a workspace, including its effective entitlements. Returns an
        error if the principal isn't assigned directly.

        :param name: str
          The resource name of the assignment, in the format
          ``accounts/{account_id}/workspaces/{workspace_id}/workspace-assignments/{principal_id}``.

        :returns: :class:`WorkspaceAssignment`
        """

        headers = {
            "Accept": "application/json",
        }

        res = self._api.do("GET", f"/api/2.0/identity/{name}", headers=headers)
        return WorkspaceAssignment.from_dict(res)

    def get_workspace_assignment_detail(self, workspace_id: int, principal_id: int) -> WorkspaceAssignmentDetail:
        """Returns the assignment details for a principal in a workspace.

        :param workspace_id: int
          Required. The workspace ID for which the assignment details are being requested.
        :param principal_id: int
          Required. The internal ID of the principal (user/sp/group) for which the assignment details are
          being requested.

        :returns: :class:`WorkspaceAssignmentDetail`
        """

        headers = {
            "Accept": "application/json",
        }

        res = self._api.do(
            "GET",
            f"/api/2.0/identity/accounts/{self._api.account_id}/workspaces/{workspace_id}/workspace-assignment-details/{principal_id}",
            headers=headers,
        )
        return WorkspaceAssignmentDetail.from_dict(res)

    def list_direct_group_members(
        self, parent: str, *, page_size: Optional[int] = None, page_token: Optional[str] = None
    ) -> Iterator[DirectGroupMember]:
        """Lists the direct members of a group, sorted by display name, with where each membership comes from.
        Members in your identity provider who haven't been added to Databricks aren't included.

        :param parent: str
          The resource name of the group, in the format ``accounts/{account_id}/groups/{group_id}``.
        :param page_size: int (optional)
          The maximum number of members to return, up to 1000. The default is 1000. A page can contain fewer
          members.
        :param page_token: str (optional)
          The ``next_page_token`` from a previous response, to get the next page.

        :returns: Iterator over :class:`DirectGroupMember`
        """

        query = {}
        if page_size is not None:
            query["page_size"] = page_size
        if page_token is not None:
            query["page_token"] = page_token
        headers = {
            "Accept": "application/json",
        }

        while True:
            json = self._api.do("GET", f"/api/2.0/identity/{parent}/direct-members", query=query, headers=headers)
            if "direct_group_members" in json:
                for v in json["direct_group_members"]:
                    yield DirectGroupMember.from_dict(v)
            if "next_page_token" not in json or not json["next_page_token"]:
                return
            query["page_token"] = json["next_page_token"]

    def list_groups(
        self,
        parent: str,
        *,
        filter: Optional[str] = None,
        page_size: Optional[int] = None,
        page_token: Optional[str] = None,
    ) -> Iterator[Group]:
        """Lists the groups in your account, sorted by Databricks ID. Groups in your identity provider that
        haven't been added to Databricks aren't included.

        :param parent: str
          The resource name of the account to list groups in, in the format ``accounts/{account_id}``.
        :param filter: str (optional)
          Filters groups by ``group_name`` or ``external_id``, for example ``group_name eq "Data engineers"``.
          Put the value in quotes.
        :param page_size: int (optional)
          The maximum number of groups to return, up to 1000. The default is 1000. A page can contain fewer
          groups.
        :param page_token: str (optional)
          The ``next_page_token`` from a previous response, to get the next page.

        :returns: Iterator over :class:`Group`
        """

        query = {}
        if filter is not None:
            query["filter"] = filter
        if page_size is not None:
            query["page_size"] = page_size
        if page_token is not None:
            query["page_token"] = page_token
        headers = {
            "Accept": "application/json",
        }

        while True:
            json = self._api.do("GET", f"/api/2.0/identity/{parent}/groups", query=query, headers=headers)
            if "groups" in json:
                for v in json["groups"]:
                    yield Group.from_dict(v)
            if "next_page_token" not in json or not json["next_page_token"]:
                return
            query["page_token"] = json["next_page_token"]

    def list_identity_visibility_filters(
        self, parent: str, *, page_size: Optional[int] = None, page_token: Optional[str] = None
    ) -> Iterator[IdentityVisibilityFilter]:
        """Lists the group visibility filters in an account. It returns the rules, not the groups they match.

        :param parent: str
          The resource name of the account, in the format ``accounts/{account_id}``.
        :param page_size: int (optional)
          The maximum number of filters to return, up to 1000. The default is 100. A page can contain fewer
          filters.
        :param page_token: str (optional)
          The ``next_page_token`` from a previous response, to get the next page.

        :returns: Iterator over :class:`IdentityVisibilityFilter`
        """

        query = {}
        if page_size is not None:
            query["page_size"] = page_size
        if page_token is not None:
            query["page_token"] = page_token
        headers = {
            "Accept": "application/json",
        }

        while True:
            json = self._api.do(
                "GET", f"/api/2.0/identity/{parent}/identity-visibility-filters", query=query, headers=headers
            )
            if "identity_visibility_filters" in json:
                for v in json["identity_visibility_filters"]:
                    yield IdentityVisibilityFilter.from_dict(v)
            if "next_page_token" not in json or not json["next_page_token"]:
                return
            query["page_token"] = json["next_page_token"]

    def list_service_principals(
        self,
        parent: str,
        *,
        filter: Optional[str] = None,
        page_size: Optional[int] = None,
        page_token: Optional[str] = None,
    ) -> Iterator[ServicePrincipal]:
        """Lists the service principals in your account, sorted by Databricks ID. Service principals in your
        identity provider that haven't been added to Databricks aren't included.

        :param parent: str
          The resource name of the account to list service principals in, in the format
          ``accounts/{account_id}``.
        :param filter: str (optional)
          Filters service principals by ``application_id`` or ``external_id``, for example ``application_id eq
          "<application-id>"``. Put the value in quotes.
        :param page_size: int (optional)
          The maximum number of service principals to return, up to 1000. The default is 1000. A page can
          contain fewer service principals.
        :param page_token: str (optional)
          The ``next_page_token`` from a previous response, to get the next page.

        :returns: Iterator over :class:`ServicePrincipal`
        """

        query = {}
        if filter is not None:
            query["filter"] = filter
        if page_size is not None:
            query["page_size"] = page_size
        if page_token is not None:
            query["page_token"] = page_token
        headers = {
            "Accept": "application/json",
        }

        while True:
            json = self._api.do("GET", f"/api/2.0/identity/{parent}/service-principals", query=query, headers=headers)
            if "service_principals" in json:
                for v in json["service_principals"]:
                    yield ServicePrincipal.from_dict(v)
            if "next_page_token" not in json or not json["next_page_token"]:
                return
            query["page_token"] = json["next_page_token"]

    def list_transitive_parent_groups(
        self, parent: str, *, page_size: Optional[int] = None, page_token: Optional[str] = None
    ) -> ListTransitiveParentGroupsResponse:
        """Lists every group that a user, service principal, or group belongs to, directly or through other
        groups, sorted by Databricks ID. If automatic identity management is on, the principal's group
        memberships are synced from your identity provider first.

        :param parent: str
          The user, service principal, or group whose parent groups to list, in the format
          ``accounts/{account_id}/principals/{principal_id}``.
        :param page_size: int (optional)
          The maximum number of groups to return, up to 1000. The default is 1000. A page can contain fewer
          groups.
        :param page_token: str (optional)
          The ``next_page_token`` from a previous response, to get the next page.

        :returns: :class:`ListTransitiveParentGroupsResponse`
        """

        query = {}
        if page_size is not None:
            query["page_size"] = page_size
        if page_token is not None:
            query["page_token"] = page_token
        headers = {
            "Accept": "application/json",
        }

        res = self._api.do("GET", f"/api/2.0/identity/{parent}/transitive-parent-groups", query=query, headers=headers)
        return ListTransitiveParentGroupsResponse.from_dict(res)

    def list_users(
        self,
        parent: str,
        *,
        filter: Optional[str] = None,
        page_size: Optional[int] = None,
        page_token: Optional[str] = None,
    ) -> Iterator[User]:
        """Lists the users in your account, sorted by Databricks ID. Users in your identity provider who haven't
        been added to Databricks aren't included.

        :param parent: str
          The resource name of the account to list users in, in the format ``accounts/{account_id}``.
        :param filter: str (optional)
          Filters users by ``username`` or ``external_id``, for example ``username eq "someone@example.com"``.
          Put the value in quotes.
        :param page_size: int (optional)
          The maximum number of users to return, up to 1000. The default is 1000. A page can contain fewer
          users.
        :param page_token: str (optional)
          The ``next_page_token`` from a previous response, to get the next page.

        :returns: Iterator over :class:`User`
        """

        query = {}
        if filter is not None:
            query["filter"] = filter
        if page_size is not None:
            query["page_size"] = page_size
        if page_token is not None:
            query["page_token"] = page_token
        headers = {
            "Accept": "application/json",
        }

        while True:
            json = self._api.do("GET", f"/api/2.0/identity/{parent}/users", query=query, headers=headers)
            if "users" in json:
                for v in json["users"]:
                    yield User.from_dict(v)
            if "next_page_token" not in json or not json["next_page_token"]:
                return
            query["page_token"] = json["next_page_token"]

    def list_workspace_assignment_details(
        self, workspace_id: int, *, page_size: Optional[int] = None, page_token: Optional[str] = None
    ) -> Iterator[WorkspaceAssignmentDetail]:
        """Lists workspace assignment details for a workspace. The response omits the per-principal entitlement
        fields (``entitlements`` and ``effective_entitlements``). To read the entitlements for a single
        principal, get that principal's assignment detail.

        :param workspace_id: int
          Required. The workspace ID for which the workspace assignment details are being fetched.
        :param page_size: int (optional)
          The maximum number of workspace assignment details to return. The service may return fewer than this
          value. If not provided, defaults to 1000, which is also the maximum allowed. Requests for more than
          the maximum are clamped to 1000.
        :param page_token: str (optional)
          A page token, received from a previous ListWorkspaceAssignmentDetails call. Provide this to retrieve
          the subsequent page.

        :returns: Iterator over :class:`WorkspaceAssignmentDetail`
        """

        query = {}
        if page_size is not None:
            query["page_size"] = page_size
        if page_token is not None:
            query["page_token"] = page_token
        headers = {
            "Accept": "application/json",
        }

        while True:
            json = self._api.do(
                "GET",
                f"/api/2.0/identity/accounts/{self._api.account_id}/workspaces/{workspace_id}/workspace-assignment-details",
                query=query,
                headers=headers,
            )
            if "workspace_assignment_details" in json:
                for v in json["workspace_assignment_details"]:
                    yield WorkspaceAssignmentDetail.from_dict(v)
            if "next_page_token" not in json or not json["next_page_token"]:
                return
            query["page_token"] = json["next_page_token"]

    def list_workspace_assignments(
        self, parent: str, *, page_size: Optional[int] = None, page_token: Optional[str] = None
    ) -> Iterator[WorkspaceAssignment]:
        """Lists the principals assigned directly to a workspace. The response leaves ``entitlements`` and
        ``effective_entitlements`` empty. To read a principal's entitlements, get its assignment.

        :param parent: str
          The resource name of the workspace, in the format
          ``accounts/{account_id}/workspaces/{workspace_id}``.
        :param page_size: int (optional)
          The maximum number of assignments to return, up to 1000. The default is 1000. A page can contain
          fewer assignments.
        :param page_token: str (optional)
          The ``next_page_token`` from a previous response, to get the next page.

        :returns: Iterator over :class:`WorkspaceAssignment`
        """

        query = {}
        if page_size is not None:
            query["page_size"] = page_size
        if page_token is not None:
            query["page_token"] = page_token
        headers = {
            "Accept": "application/json",
        }

        while True:
            json = self._api.do(
                "GET", f"/api/2.0/identity/{parent}/workspace-assignments", query=query, headers=headers
            )
            if "workspace_assignments" in json:
                for v in json["workspace_assignments"]:
                    yield WorkspaceAssignment.from_dict(v)
            if "next_page_token" not in json or not json["next_page_token"]:
                return
            query["page_token"] = json["next_page_token"]

    def resolve_group(self, external_id: str) -> ResolveGroupResponse:
        """Gets a group by its ID in your identity provider (IdP) and syncs its name and parent groups from your
        IdP. If the group isn't in your account yet, it's added. Requires automatic identity management. If
        your account has group visibility filters, the group must match them.

        :param external_id: str
          The ID of the group in your IdP.

        :returns: :class:`ResolveGroupResponse`
        """

        body = {}
        if external_id is not None:
            body["external_id"] = external_id
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do(
            "POST",
            f"/api/2.0/identity/accounts/{self._api.account_id}/groups/resolve-by-external-id",
            body=body,
            headers=headers,
        )
        return ResolveGroupResponse.from_dict(res)

    def resolve_service_principal(self, external_id: str) -> ResolveServicePrincipalResponse:
        """Gets a service principal by its ID in your identity provider (IdP) and syncs its details and group
        memberships from your IdP. If the service principal isn't in your account yet, it's added. Requires
        automatic identity management with Microsoft Entra ID as your IdP.

        :param external_id: str
          The ID of the service principal in your IdP.

        :returns: :class:`ResolveServicePrincipalResponse`
        """

        body = {}
        if external_id is not None:
            body["external_id"] = external_id
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do(
            "POST",
            f"/api/2.0/identity/accounts/{self._api.account_id}/service-principals/resolve-by-external-id",
            body=body,
            headers=headers,
        )
        return ResolveServicePrincipalResponse.from_dict(res)

    def resolve_user(self, external_id: str) -> ResolveUserResponse:
        """Gets a user by their ID in your identity provider (IdP) and syncs their details and group memberships
        from your IdP. If the user isn't in your account yet, they're added. Requires automatic identity
        management.

        :param external_id: str
          The ID of the user in your IdP.

        :returns: :class:`ResolveUserResponse`
        """

        body = {}
        if external_id is not None:
            body["external_id"] = external_id
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do(
            "POST",
            f"/api/2.0/identity/accounts/{self._api.account_id}/users/resolve-by-external-id",
            body=body,
            headers=headers,
        )
        return ResolveUserResponse.from_dict(res)

    def update_group(self, name: str, group: Group, update_mask: str) -> Group:
        """Updates a group. Only the fields in ``update_mask`` change.

        If automatic identity management is on and the group has an ``external_id``, you can only update
        ``external_id``. The group's other fields come from your identity provider. If your account also has
        group visibility filters, a new ``external_id`` must match them. You can always clear ``external_id``.

        :param name: str
          The resource name of the group, in one of these formats:

          - Account APIs: ``accounts/{account_id}/groups/{group_id}``
          - Workspace APIs: ``groups/{group_id}``
        :param group: :class:`Group`
          The group to update. Its ``name`` identifies the group.
        :param update_mask: str
          The fields to update, separated by commas. You can update ``group_name`` and ``external_id``.

        :returns: :class:`Group`
        """

        body = group.as_dict()
        query = {}
        if update_mask is not None:
            query["update_mask"] = update_mask
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do("PATCH", f"/api/2.0/identity/{name}", query=query, body=body, headers=headers)
        return Group.from_dict(res)

    def update_service_principal(
        self, name: str, service_principal: ServicePrincipal, update_mask: str
    ) -> ServicePrincipal:
        """Updates a service principal. Only the fields in ``update_mask`` change.

        If automatic identity management is on and the service principal has an ``external_id``, you can only
        update ``external_id``. Its other fields come from your identity provider. A service principal can't
        deactivate itself, and you can't update service principals that Databricks manages.

        :param name: str
          The resource name of the service principal, in one of these formats:

          - Account APIs: ``accounts/{account_id}/service-principals/{service_principal_id}``
          - Workspace APIs: ``service-principals/{service_principal_id}``
        :param service_principal: :class:`ServicePrincipal`
          The service principal to update. Its ``name`` identifies the service principal.
        :param update_mask: str
          The fields to update, separated by commas. You can update ``display_name``, ``account_sp_status``,
          and ``external_id``.

        :returns: :class:`ServicePrincipal`
        """

        body = service_principal.as_dict()
        query = {}
        if update_mask is not None:
            query["update_mask"] = update_mask
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do("PATCH", f"/api/2.0/identity/{name}", query=query, body=body, headers=headers)
        return ServicePrincipal.from_dict(res)

    def update_user(self, name: str, user: User, update_mask: str) -> User:
        """Updates a user. Only the fields in ``update_mask`` change.

        If automatic identity management is on and the user has an ``external_id``, you can only update
        ``external_id``. The user's other fields come from your identity provider. You can't deactivate
        yourself or change the status of the account owner.

        :param name: str
          The resource name of the user, in one of these formats:

          - Account APIs: ``accounts/{account_id}/users/{user_id}``
          - Workspace APIs: ``users/{user_id}``
        :param user: :class:`User`
          The user to update. Its ``name`` identifies the user.
        :param update_mask: str
          The fields to update, separated by commas. You can update ``full_name.given_name``,
          ``full_name.family_name``, ``account_user_status``, and ``external_id``.

        :returns: :class:`User`
        """

        body = user.as_dict()
        query = {}
        if update_mask is not None:
            query["update_mask"] = update_mask
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do("PATCH", f"/api/2.0/identity/{name}", query=query, body=body, headers=headers)
        return User.from_dict(res)

    def update_workspace_assignment(
        self, name: str, workspace_assignment: WorkspaceAssignment, update_mask: FieldMask
    ) -> WorkspaceAssignment:
        """Replaces the entitlements of a principal's direct assignment to a workspace. The new list can't be
        empty.

        Entitlements are changed one at a time. If the request fails partway through, only some of the changes
        take effect. Get the assignment afterwards to check the result.

        :param name: str
          The resource name of the assignment, in one of these formats:

          - Account APIs:
            ``accounts/{account_id}/workspaces/{workspace_id}/workspace-assignments/{principal_id}``
          - Workspace APIs: ``workspace-assignments/{principal_id}``
        :param workspace_assignment: :class:`WorkspaceAssignment`
          The assignment to update. Its ``name`` identifies the assignment.
        :param update_mask: FieldMask
          The fields to update. The only supported field is ``entitlements``.

        :returns: :class:`WorkspaceAssignment`
        """

        body = workspace_assignment.as_dict()
        query = {}
        if update_mask is not None:
            query["update_mask"] = update_mask.ToJsonString()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do("PATCH", f"/api/2.0/identity/{name}", query=query, body=body, headers=headers)
        return WorkspaceAssignment.from_dict(res)

    def update_workspace_assignment_detail(
        self,
        workspace_id: int,
        principal_id: int,
        workspace_assignment_detail: WorkspaceAssignmentDetail,
        update_mask: FieldMask,
    ) -> WorkspaceAssignmentDetail:
        """Updates the entitlements of a directly assigned principal in a workspace. Changes are applied one at a
        time rather than atomically. If the request fails partway through, only some of the requested changes
        take effect. Get the assignment detail afterwards to confirm the final state.

        :param workspace_id: int
          Required. The workspace ID for which the workspace assignment detail is being updated.
        :param principal_id: int
          Required. ID of the principal in Databricks.
        :param workspace_assignment_detail: :class:`WorkspaceAssignmentDetail`
          Required. Workspace assignment detail to be updated in Databricks.
        :param update_mask: FieldMask
          Required. The list of fields to update.

        :returns: :class:`WorkspaceAssignmentDetail`
        """

        body = workspace_assignment_detail.as_dict()
        query = {}
        if update_mask is not None:
            query["update_mask"] = update_mask.ToJsonString()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do(
            "PATCH",
            f"/api/2.0/identity/accounts/{self._api.account_id}/workspaces/{workspace_id}/workspace-assignment-details/{principal_id}",
            query=query,
            body=body,
            headers=headers,
        )
        return WorkspaceAssignmentDetail.from_dict(res)


class WorkspaceIamV2API:
    """These APIs are used to manage identities and the workspace access of these identities in Databricks."""

    def __init__(self, api_client):
        self._api = api_client

    def create_direct_group_member_proxy(
        self, parent: str, direct_group_member: DirectGroupMember
    ) -> DirectGroupMember:
        """Adds a user, service principal, or group as a direct member of a group in the account that contains
        this workspace.

        If automatic identity management is on and the group has an ``external_id``, its members come from
        your identity provider and can't be changed in Databricks.

        :param parent: str
          The resource name of the group to add the member to, in the format ``groups/{group_id}``.
        :param direct_group_member: :class:`DirectGroupMember`
          The member to add. Set its ``principal_id``.

        :returns: :class:`DirectGroupMember`
        """

        body = direct_group_member.as_dict()
        query = {}
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("POST", f"/api/2.0/identity/{parent}/direct-members", body=body, headers=headers)
        return DirectGroupMember.from_dict(res)

    def create_group_proxy(self, group: Group, *, parent: Optional[str] = None) -> Group:
        """Creates a local group in the account that contains this workspace. A local group is a group that isn't
        synced from your identity provider (IdP). You become a manager of the new group.

        If automatic identity management is on, you can't set ``external_id``. To add a group from your IdP,
        get it as an external group instead.

        :param group: :class:`Group`
          The group to create.
        :param parent: str (optional)
          The resource name of the account to create the group in, in the format ``accounts/{account_id}``.
          Defaults to the account that contains this workspace. Any other account is rejected.

        :returns: :class:`Group`
        """

        body = group.as_dict()
        query = {}
        if parent is not None:
            query["parent"] = parent
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("POST", "/api/2.0/identity/groups", query=query, body=body, headers=headers)
        return Group.from_dict(res)

    def create_service_principal_proxy(
        self, service_principal: ServicePrincipal, *, parent: Optional[str] = None
    ) -> ServicePrincipal:
        """Creates a local service principal in the account that contains this workspace. A local service
        principal is one that isn't synced from your identity provider (IdP).

        If automatic identity management is on, you can't set ``external_id``. To add a service principal from
        your IdP, get it as an external service principal instead.

        :param service_principal: :class:`ServicePrincipal`
          The service principal to create.
        :param parent: str (optional)
          The resource name of the account to create the service principal in, in the format
          ``accounts/{account_id}``. Defaults to the account that contains this workspace. Any other account
          is rejected.

        :returns: :class:`ServicePrincipal`
        """

        body = service_principal.as_dict()
        query = {}
        if parent is not None:
            query["parent"] = parent
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("POST", "/api/2.0/identity/service-principals", query=query, body=body, headers=headers)
        return ServicePrincipal.from_dict(res)

    def create_user_proxy(self, user: User, *, parent: Optional[str] = None) -> User:
        """Creates a local user in the account that contains this workspace. A local user is a user that isn't
        synced from your identity provider (IdP).

        If automatic identity management is on, you can't set ``external_id``. To add a user from your IdP,
        get them as an external user instead.

        :param user: :class:`User`
          The user to create.
        :param parent: str (optional)
          The resource name of the account to create the user in, in the format ``accounts/{account_id}``.
          Defaults to the account that contains this workspace. Any other account is rejected.

        :returns: :class:`User`
        """

        body = user.as_dict()
        query = {}
        if parent is not None:
            query["parent"] = parent
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("POST", "/api/2.0/identity/users", query=query, body=body, headers=headers)
        return User.from_dict(res)

    def create_workspace_assignment_detail_proxy(
        self, workspace_assignment_detail: WorkspaceAssignmentDetail
    ) -> WorkspaceAssignmentDetail:
        """Creates a workspace assignment detail for a principal in the calling workspace.

        :param workspace_assignment_detail: :class:`WorkspaceAssignmentDetail`
          Required. Workspace assignment detail to be created in Databricks.

        :returns: :class:`WorkspaceAssignmentDetail`
        """

        body = workspace_assignment_detail.as_dict()
        query = {}
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("POST", "/api/2.0/identity/workspace-assignment-details", body=body, headers=headers)
        return WorkspaceAssignmentDetail.from_dict(res)

    def create_workspace_assignment_proxy(
        self, workspace_assignment: WorkspaceAssignment, *, parent: Optional[str] = None
    ) -> WorkspaceAssignment:
        """Assigns a user, service principal, or group directly to this workspace with the given entitlements.
        Returns an error if the principal is already assigned directly.

        Entitlements are granted one at a time. If the request fails partway through, the principal stays
        assigned with only some of the entitlements. Get the assignment afterwards to check which were
        granted.

        :param workspace_assignment: :class:`WorkspaceAssignment`
          The assignment to create. Set its ``principal_id`` and ``entitlements``.
        :param parent: str (optional)
          The resource name of the workspace, in the format
          ``accounts/{account_id}/workspaces/{workspace_id}``. Defaults to this workspace. Any other workspace
          is rejected.

        :returns: :class:`WorkspaceAssignment`
        """

        body = workspace_assignment.as_dict()
        query = {}
        if parent is not None:
            query["parent"] = parent
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("POST", "/api/2.0/identity/workspace-assignments", query=query, body=body, headers=headers)
        return WorkspaceAssignment.from_dict(res)

    def delete_direct_group_member_proxy(self, name: str):
        """Removes a direct member from a group in the account that contains this workspace.

        If automatic identity management is on and the group has an ``external_id``, its members come from
        your identity provider and can't be changed in Databricks.

        :param name: str
          The resource name of the membership, in the format
          ``groups/{group_id}/direct-members/{principal_id}``.


        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        self._api.do("DELETE", f"/api/2.0/identity/{name}", headers=headers)

    def delete_group_proxy(self, name: str):
        """Deletes a group from the account that contains this workspace and removes it from the workspaces it's
        assigned to.

        :param name: str
          The resource name of the group, in the format ``groups/{group_id}``.


        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        self._api.do("DELETE", f"/api/2.0/identity/{name}", headers=headers)

    def delete_service_principal_proxy(self, name: str):
        """Deletes a service principal from the account that contains this workspace and removes it from the
        workspaces it's assigned to. You can't delete service principals that Databricks manages.

        :param name: str
          The resource name of the service principal, in the format
          ``service-principals/{service_principal_id}``.


        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        self._api.do("DELETE", f"/api/2.0/identity/{name}", headers=headers)

    def delete_user_proxy(self, name: str):
        """Deletes a user from the account that contains this workspace and removes them from the workspaces
        they're assigned to.

        :param name: str
          The resource name of the user, in the format ``users/{user_id}``.


        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        self._api.do("DELETE", f"/api/2.0/identity/{name}", headers=headers)

    def delete_workspace_assignment_detail_proxy(self, principal_id: int):
        """Deletes a workspace assignment detail for a principal in the calling workspace, revoking all of its
        entitlements. Entitlements are revoked one at a time rather than atomically. If the request fails
        partway through, the principal stays assigned with some of its original entitlements. Retrying is
        safe.

        :param principal_id: int
          Required. ID of the principal in Databricks to delete workspace assignment for.


        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        self._api.do("DELETE", f"/api/2.0/identity/workspace-assignment-details/{principal_id}", headers=headers)

    def delete_workspace_assignment_proxy(self, name: str):
        """Removes a principal's direct assignment to this workspace and revokes the entitlements it granted. The
        principal keeps any access it gets through groups.

        Entitlements are revoked one at a time. If the request fails partway through, the principal stays
        assigned with some of its entitlements. You can retry the request.

        :param name: str
          The resource name of the assignment, in the format ``workspace-assignments/{principal_id}``.


        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        self._api.do("DELETE", f"/api/2.0/identity/{name}", headers=headers)

    def get_direct_group_member_proxy(self, name: str) -> DirectGroupMember:
        """Gets a direct member of a group in the account that contains this workspace, including where the
        membership comes from. Returns an error if the principal isn't a direct member.

        :param name: str
          The resource name of the membership, in the format
          ``groups/{group_id}/direct-members/{principal_id}``.

        :returns: :class:`DirectGroupMember`
        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("GET", f"/api/2.0/identity/{name}", headers=headers)
        return DirectGroupMember.from_dict(res)

    def get_external_group_proxy(self, name: str) -> ExternalGroup:
        """Gets a group by its ID in your identity provider (IdP) and syncs its name and parent groups from your
        IdP. If the group isn't in the account that contains this workspace yet, it's added. Requires
        automatic identity management. If your account has group visibility filters, the group must match
        them.

        :param name: str
          The resource name of the external group, in the format ``external-groups/{external_group_id}``.

        :returns: :class:`ExternalGroup`
        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("GET", f"/api/2.0/identity/{name}", headers=headers)
        return ExternalGroup.from_dict(res)

    def get_external_service_principal_proxy(self, name: str) -> ExternalServicePrincipal:
        """Gets a service principal by its ID in your identity provider (IdP) and syncs its details and group
        memberships from your IdP. If the service principal isn't in the account that contains this workspace
        yet, it's added. Requires automatic identity management with Microsoft Entra ID as your IdP.

        :param name: str
          The resource name of the external service principal, in the format
          ``external-service-principals/{external_service_principal_id}``.

        :returns: :class:`ExternalServicePrincipal`
        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("GET", f"/api/2.0/identity/{name}", headers=headers)
        return ExternalServicePrincipal.from_dict(res)

    def get_external_user_proxy(self, name: str) -> ExternalUser:
        """Gets a user by their ID in your identity provider (IdP) and syncs their details and group memberships
        from your IdP. If the user isn't in the account that contains this workspace yet, they're added.
        Requires automatic identity management.

        :param name: str
          The resource name of the external user, in the format ``external-users/{external_user_id}``.

        :returns: :class:`ExternalUser`
        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("GET", f"/api/2.0/identity/{name}", headers=headers)
        return ExternalUser.from_dict(res)

    def get_group_proxy(self, name: str) -> Group:
        """Gets a group in the account that contains this workspace by its Databricks ID.

        :param name: str
          The resource name of the group, in the format ``groups/{group_id}``.

        :returns: :class:`Group`
        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("GET", f"/api/2.0/identity/{name}", headers=headers)
        return Group.from_dict(res)

    def get_service_principal_proxy(self, name: str) -> ServicePrincipal:
        """Gets a service principal in the account that contains this workspace by its Databricks ID.

        :param name: str
          The resource name of the service principal, in the format
          ``service-principals/{service_principal_id}``.

        :returns: :class:`ServicePrincipal`
        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("GET", f"/api/2.0/identity/{name}", headers=headers)
        return ServicePrincipal.from_dict(res)

    def get_user_proxy(self, name: str) -> User:
        """Gets a user in the account that contains this workspace by their Databricks ID.

        :param name: str
          The resource name of the user, in the format ``users/{user_id}``.

        :returns: :class:`User`
        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("GET", f"/api/2.0/identity/{name}", headers=headers)
        return User.from_dict(res)

    def get_workspace_access_detail_local(
        self, name: str, *, view: Optional[WorkspaceAccessDetailView] = None
    ) -> WorkspaceAccessDetail:
        """Returns the access details for a principal in the current workspace. Allows for checking access
        details for any provisioned principal (user, service principal, or group) in the current workspace.

        - Provisioned principal here refers to one that has been synced into Databricks from the customer's
          IdP or added explicitly to Databricks via SCIM/UI. Allows for passing in a "view" parameter to
          control what fields are returned (BASIC by default or FULL).

        :param name: str
          The resource name of the workspace access detail. Format: workspace-access-details/{principal_id}
        :param view: :class:`WorkspaceAccessDetailView` (optional)
          Controls what fields are returned.

        :returns: :class:`WorkspaceAccessDetail`
        """

        query = {}
        if view is not None:
            query["view"] = view.value
        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("GET", f"/api/2.0/identity/{name}", query=query, headers=headers)
        return WorkspaceAccessDetail.from_dict(res)

    def get_workspace_assignment_detail_proxy(self, principal_id: int) -> WorkspaceAssignmentDetail:
        """Returns the assignment details for a principal in the calling workspace.

        :param principal_id: int
          Required. The internal ID of the principal (user/sp/group) for which the assignment details are
          being requested.

        :returns: :class:`WorkspaceAssignmentDetail`
        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("GET", f"/api/2.0/identity/workspace-assignment-details/{principal_id}", headers=headers)
        return WorkspaceAssignmentDetail.from_dict(res)

    def get_workspace_assignment_proxy(self, name: str) -> WorkspaceAssignment:
        """Gets a principal's direct assignment to this workspace, including its effective entitlements. Returns
        an error if the principal isn't assigned directly.

        :param name: str
          The resource name of the assignment, in the format ``workspace-assignments/{principal_id}``.

        :returns: :class:`WorkspaceAssignment`
        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("GET", f"/api/2.0/identity/{name}", headers=headers)
        return WorkspaceAssignment.from_dict(res)

    def get_workspace_identity_detail(self, name: str) -> WorkspaceIdentityDetail:
        """Gets a principal's status in this workspace and whether it has access directly or through a group.
        Returns an error if the principal doesn't have access to the workspace.

        :param name: str
          The resource name of the workspace identity detail, in the format
          ``principals/{principal_id}/workspace-identity-detail``.

        :returns: :class:`WorkspaceIdentityDetail`
        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("GET", f"/api/2.0/identity/{name}", headers=headers)
        return WorkspaceIdentityDetail.from_dict(res)

    def list_direct_group_members_proxy(
        self, parent: str, *, page_size: Optional[int] = None, page_token: Optional[str] = None
    ) -> Iterator[DirectGroupMember]:
        """Lists the direct members of a group in the account that contains this workspace, sorted by display
        name, with where each membership comes from. Members in your identity provider who haven't been added
        to Databricks aren't included.

        :param parent: str
          The resource name of the group, in the format ``groups/{group_id}``.
        :param page_size: int (optional)
          The maximum number of members to return, up to 1000. The default is 1000. A page can contain fewer
          members.
        :param page_token: str (optional)
          The ``next_page_token`` from a previous response, to get the next page.

        :returns: Iterator over :class:`DirectGroupMember`
        """

        query = {}
        if page_size is not None:
            query["page_size"] = page_size
        if page_token is not None:
            query["page_token"] = page_token
        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        while True:
            json = self._api.do("GET", f"/api/2.0/identity/{parent}/direct-members", query=query, headers=headers)
            if "direct_group_members" in json:
                for v in json["direct_group_members"]:
                    yield DirectGroupMember.from_dict(v)
            if "next_page_token" not in json or not json["next_page_token"]:
                return
            query["page_token"] = json["next_page_token"]

    def list_groups_proxy(
        self,
        *,
        filter: Optional[str] = None,
        page_size: Optional[int] = None,
        page_token: Optional[str] = None,
        parent: Optional[str] = None,
    ) -> Iterator[Group]:
        """Lists the groups in the account that contains this workspace, sorted by Databricks ID. Groups in your
        identity provider that haven't been added to Databricks aren't included.

        :param filter: str (optional)
          Filters groups by ``group_name`` or ``external_id``, for example ``group_name eq "Data engineers"``.
          Put the value in quotes.
        :param page_size: int (optional)
          The maximum number of groups to return, up to 1000. The default is 1000. A page can contain fewer
          groups.
        :param page_token: str (optional)
          The ``next_page_token`` from a previous response, to get the next page.
        :param parent: str (optional)
          The resource name of the account to list groups in, in the format ``accounts/{account_id}``.
          Defaults to the account that contains this workspace. Any other account is rejected.

        :returns: Iterator over :class:`Group`
        """

        query = {}
        if filter is not None:
            query["filter"] = filter
        if page_size is not None:
            query["page_size"] = page_size
        if page_token is not None:
            query["page_token"] = page_token
        if parent is not None:
            query["parent"] = parent
        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        while True:
            json = self._api.do("GET", "/api/2.0/identity/groups", query=query, headers=headers)
            if "groups" in json:
                for v in json["groups"]:
                    yield Group.from_dict(v)
            if "next_page_token" not in json or not json["next_page_token"]:
                return
            query["page_token"] = json["next_page_token"]

    def list_service_principals_proxy(
        self,
        *,
        filter: Optional[str] = None,
        page_size: Optional[int] = None,
        page_token: Optional[str] = None,
        parent: Optional[str] = None,
    ) -> Iterator[ServicePrincipal]:
        """Lists the service principals in the account that contains this workspace, sorted by Databricks ID.
        Service principals in your identity provider that haven't been added to Databricks aren't included.

        :param filter: str (optional)
          Filters service principals by ``application_id`` or ``external_id``, for example ``application_id eq
          "<application-id>"``. Put the value in quotes.
        :param page_size: int (optional)
          The maximum number of service principals to return, up to 1000. The default is 1000. A page can
          contain fewer service principals.
        :param page_token: str (optional)
          The ``next_page_token`` from a previous response, to get the next page.
        :param parent: str (optional)
          The resource name of the account to list service principals in, in the format
          ``accounts/{account_id}``. Defaults to the account that contains this workspace. Any other account
          is rejected.

        :returns: Iterator over :class:`ServicePrincipal`
        """

        query = {}
        if filter is not None:
            query["filter"] = filter
        if page_size is not None:
            query["page_size"] = page_size
        if page_token is not None:
            query["page_token"] = page_token
        if parent is not None:
            query["parent"] = parent
        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        while True:
            json = self._api.do("GET", "/api/2.0/identity/service-principals", query=query, headers=headers)
            if "service_principals" in json:
                for v in json["service_principals"]:
                    yield ServicePrincipal.from_dict(v)
            if "next_page_token" not in json or not json["next_page_token"]:
                return
            query["page_token"] = json["next_page_token"]

    def list_transitive_parent_groups_proxy(
        self, parent: str, *, page_size: Optional[int] = None, page_token: Optional[str] = None
    ) -> ListTransitiveParentGroupsResponse:
        """Lists every group that a user, service principal, or group belongs to, directly or through other
        groups, in the account that contains this workspace. Results are sorted by Databricks ID. If automatic
        identity management is on, the principal's group memberships are synced from your identity provider
        first.

        :param parent: str
          The user, service principal, or group whose parent groups to list, in the format
          ``principals/{principal_id}``.
        :param page_size: int (optional)
          The maximum number of groups to return, up to 1000. The default is 1000. A page can contain fewer
          groups.
        :param page_token: str (optional)
          The ``next_page_token`` from a previous response, to get the next page.

        :returns: :class:`ListTransitiveParentGroupsResponse`
        """

        query = {}
        if page_size is not None:
            query["page_size"] = page_size
        if page_token is not None:
            query["page_token"] = page_token
        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("GET", f"/api/2.0/identity/{parent}/transitive-parent-groups", query=query, headers=headers)
        return ListTransitiveParentGroupsResponse.from_dict(res)

    def list_users_proxy(
        self,
        *,
        filter: Optional[str] = None,
        page_size: Optional[int] = None,
        page_token: Optional[str] = None,
        parent: Optional[str] = None,
    ) -> Iterator[User]:
        """Lists the users in the account that contains this workspace, sorted by Databricks ID. Users in your
        identity provider who haven't been added to Databricks aren't included.

        :param filter: str (optional)
          Filters users by ``username`` or ``external_id``, for example ``username eq "someone@example.com"``.
          Put the value in quotes.
        :param page_size: int (optional)
          The maximum number of users to return, up to 1000. The default is 1000. A page can contain fewer
          users.
        :param page_token: str (optional)
          The ``next_page_token`` from a previous response, to get the next page.
        :param parent: str (optional)
          The resource name of the account to list users in, in the format ``accounts/{account_id}``. Defaults
          to the account that contains this workspace. Any other account is rejected.

        :returns: Iterator over :class:`User`
        """

        query = {}
        if filter is not None:
            query["filter"] = filter
        if page_size is not None:
            query["page_size"] = page_size
        if page_token is not None:
            query["page_token"] = page_token
        if parent is not None:
            query["parent"] = parent
        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        while True:
            json = self._api.do("GET", "/api/2.0/identity/users", query=query, headers=headers)
            if "users" in json:
                for v in json["users"]:
                    yield User.from_dict(v)
            if "next_page_token" not in json or not json["next_page_token"]:
                return
            query["page_token"] = json["next_page_token"]

    def list_workspace_assignment_details_proxy(
        self, *, page_size: Optional[int] = None, page_token: Optional[str] = None
    ) -> Iterator[WorkspaceAssignmentDetail]:
        """Lists workspace assignment details for the calling workspace. The response omits the per-principal
        entitlement fields (``entitlements`` and ``effective_entitlements``). To read the entitlements for a
        single principal, get that principal's assignment detail.

        :param page_size: int (optional)
          The maximum number of workspace assignment details to return. The service may return fewer than this
          value. If not provided, defaults to 1000, which is also the maximum allowed. Requests for more than
          the maximum are clamped to 1000.
        :param page_token: str (optional)
          A page token from a previous list call. Provide this to retrieve the subsequent page.

        :returns: Iterator over :class:`WorkspaceAssignmentDetail`
        """

        query = {}
        if page_size is not None:
            query["page_size"] = page_size
        if page_token is not None:
            query["page_token"] = page_token
        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        while True:
            json = self._api.do("GET", "/api/2.0/identity/workspace-assignment-details", query=query, headers=headers)
            if "workspace_assignment_details" in json:
                for v in json["workspace_assignment_details"]:
                    yield WorkspaceAssignmentDetail.from_dict(v)
            if "next_page_token" not in json or not json["next_page_token"]:
                return
            query["page_token"] = json["next_page_token"]

    def list_workspace_assignments_proxy(
        self, *, page_size: Optional[int] = None, page_token: Optional[str] = None, parent: Optional[str] = None
    ) -> Iterator[WorkspaceAssignment]:
        """Lists the principals assigned directly to this workspace. The response leaves ``entitlements`` and
        ``effective_entitlements`` empty. To read a principal's entitlements, get its assignment.

        :param page_size: int (optional)
          The maximum number of assignments to return, up to 1000. The default is 1000. A page can contain
          fewer assignments.
        :param page_token: str (optional)
          The ``next_page_token`` from a previous response, to get the next page.
        :param parent: str (optional)
          The resource name of the workspace, in the format
          ``accounts/{account_id}/workspaces/{workspace_id}``. Defaults to this workspace. Any other workspace
          is rejected.

        :returns: Iterator over :class:`WorkspaceAssignment`
        """

        query = {}
        if page_size is not None:
            query["page_size"] = page_size
        if page_token is not None:
            query["page_token"] = page_token
        if parent is not None:
            query["parent"] = parent
        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        while True:
            json = self._api.do("GET", "/api/2.0/identity/workspace-assignments", query=query, headers=headers)
            if "workspace_assignments" in json:
                for v in json["workspace_assignments"]:
                    yield WorkspaceAssignment.from_dict(v)
            if "next_page_token" not in json or not json["next_page_token"]:
                return
            query["page_token"] = json["next_page_token"]

    def resolve_group_proxy(self, external_id: str) -> ResolveGroupResponse:
        """Gets a group by its ID in your identity provider (IdP) and syncs its name and parent groups from your
        IdP. If the group isn't in the account that contains this workspace yet, it's added. Requires
        automatic identity management. If your account has group visibility filters, the group must match
        them.

        :param external_id: str
          The ID of the group in your IdP.

        :returns: :class:`ResolveGroupResponse`
        """

        body = {}
        if external_id is not None:
            body["external_id"] = external_id
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("POST", "/api/2.0/identity/groups/resolve-by-external-id", body=body, headers=headers)
        return ResolveGroupResponse.from_dict(res)

    def resolve_service_principal_proxy(self, external_id: str) -> ResolveServicePrincipalResponse:
        """Gets a service principal by its ID in your identity provider (IdP) and syncs its details and group
        memberships from your IdP. If the service principal isn't in the account that contains this workspace
        yet, it's added. Requires automatic identity management with Microsoft Entra ID as your IdP.

        :param external_id: str
          The ID of the service principal in your IdP.

        :returns: :class:`ResolveServicePrincipalResponse`
        """

        body = {}
        if external_id is not None:
            body["external_id"] = external_id
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do(
            "POST", "/api/2.0/identity/service-principals/resolve-by-external-id", body=body, headers=headers
        )
        return ResolveServicePrincipalResponse.from_dict(res)

    def resolve_user_proxy(self, external_id: str) -> ResolveUserResponse:
        """Gets a user by their ID in your identity provider (IdP) and syncs their details and group memberships
        from your IdP. If the user isn't in the account that contains this workspace yet, they're added.
        Requires automatic identity management.

        :param external_id: str
          The ID of the user in your IdP.

        :returns: :class:`ResolveUserResponse`
        """

        body = {}
        if external_id is not None:
            body["external_id"] = external_id
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("POST", "/api/2.0/identity/users/resolve-by-external-id", body=body, headers=headers)
        return ResolveUserResponse.from_dict(res)

    def update_group_proxy(self, name: str, group: Group, update_mask: str) -> Group:
        """Updates a group in the account that contains this workspace. Only the fields in ``update_mask``
        change.

        If automatic identity management is on and the group has an ``external_id``, you can only update
        ``external_id``. The group's other fields come from your identity provider. If your account also has
        group visibility filters, a new ``external_id`` must match them. You can always clear ``external_id``.

        :param name: str
          The resource name of the group, in one of these formats:

          - Account APIs: ``accounts/{account_id}/groups/{group_id}``
          - Workspace APIs: ``groups/{group_id}``
        :param group: :class:`Group`
          The group to update. Its ``name`` identifies the group.
        :param update_mask: str
          The fields to update, separated by commas. You can update ``group_name`` and ``external_id``.

        :returns: :class:`Group`
        """

        body = group.as_dict()
        query = {}
        if update_mask is not None:
            query["update_mask"] = update_mask
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("PATCH", f"/api/2.0/identity/{name}", query=query, body=body, headers=headers)
        return Group.from_dict(res)

    def update_service_principal_proxy(
        self, name: str, service_principal: ServicePrincipal, update_mask: str
    ) -> ServicePrincipal:
        """Updates a service principal in the account that contains this workspace. Only the fields in
        ``update_mask`` change.

        If automatic identity management is on and the service principal has an ``external_id``, you can only
        update ``external_id``. Its other fields come from your identity provider. A service principal can't
        deactivate itself, and you can't update service principals that Databricks manages.

        :param name: str
          The resource name of the service principal, in one of these formats:

          - Account APIs: ``accounts/{account_id}/service-principals/{service_principal_id}``
          - Workspace APIs: ``service-principals/{service_principal_id}``
        :param service_principal: :class:`ServicePrincipal`
          The service principal to update. Its ``name`` identifies the service principal.
        :param update_mask: str
          The fields to update, separated by commas. You can update ``display_name``, ``account_sp_status``,
          and ``external_id``.

        :returns: :class:`ServicePrincipal`
        """

        body = service_principal.as_dict()
        query = {}
        if update_mask is not None:
            query["update_mask"] = update_mask
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("PATCH", f"/api/2.0/identity/{name}", query=query, body=body, headers=headers)
        return ServicePrincipal.from_dict(res)

    def update_user_proxy(self, name: str, user: User, update_mask: str) -> User:
        """Updates a user in the account that contains this workspace. Only the fields in ``update_mask`` change.

        If automatic identity management is on and the user has an ``external_id``, you can only update
        ``external_id``. The user's other fields come from your identity provider. You can't deactivate
        yourself or change the status of the account owner.

        :param name: str
          The resource name of the user, in one of these formats:

          - Account APIs: ``accounts/{account_id}/users/{user_id}``
          - Workspace APIs: ``users/{user_id}``
        :param user: :class:`User`
          The user to update. Its ``name`` identifies the user.
        :param update_mask: str
          The fields to update, separated by commas. You can update ``full_name.given_name``,
          ``full_name.family_name``, ``account_user_status``, and ``external_id``.

        :returns: :class:`User`
        """

        body = user.as_dict()
        query = {}
        if update_mask is not None:
            query["update_mask"] = update_mask
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("PATCH", f"/api/2.0/identity/{name}", query=query, body=body, headers=headers)
        return User.from_dict(res)

    def update_workspace_assignment_detail_proxy(
        self, principal_id: int, workspace_assignment_detail: WorkspaceAssignmentDetail, update_mask: FieldMask
    ) -> WorkspaceAssignmentDetail:
        """Updates the entitlements of a directly assigned principal in the calling workspace. Changes are
        applied one at a time rather than atomically. If the request fails partway through, only some of the
        requested changes take effect. Get the assignment detail afterwards to confirm the final state.

        :param principal_id: int
          Required. ID of the principal in Databricks.
        :param workspace_assignment_detail: :class:`WorkspaceAssignmentDetail`
          Required. Workspace assignment detail to be updated in Databricks.
        :param update_mask: FieldMask
          Required. The list of fields to update.

        :returns: :class:`WorkspaceAssignmentDetail`
        """

        body = workspace_assignment_detail.as_dict()
        query = {}
        if update_mask is not None:
            query["update_mask"] = update_mask.ToJsonString()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do(
            "PATCH",
            f"/api/2.0/identity/workspace-assignment-details/{principal_id}",
            query=query,
            body=body,
            headers=headers,
        )
        return WorkspaceAssignmentDetail.from_dict(res)

    def update_workspace_assignment_proxy(
        self, name: str, workspace_assignment: WorkspaceAssignment, update_mask: FieldMask
    ) -> WorkspaceAssignment:
        """Replaces the entitlements of a principal's direct assignment to this workspace. The new list can't be
        empty.

        Entitlements are changed one at a time. If the request fails partway through, only some of the changes
        take effect. Get the assignment afterwards to check the result.

        :param name: str
          The resource name of the assignment, in one of these formats:

          - Account APIs:
            ``accounts/{account_id}/workspaces/{workspace_id}/workspace-assignments/{principal_id}``
          - Workspace APIs: ``workspace-assignments/{principal_id}``
        :param workspace_assignment: :class:`WorkspaceAssignment`
          The assignment to update. Its ``name`` identifies the assignment.
        :param update_mask: FieldMask
          The fields to update. The only supported field is ``entitlements``.

        :returns: :class:`WorkspaceAssignment`
        """

        body = workspace_assignment.as_dict()
        query = {}
        if update_mask is not None:
            query["update_mask"] = update_mask.ToJsonString()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("PATCH", f"/api/2.0/identity/{name}", query=query, body=body, headers=headers)
        return WorkspaceAssignment.from_dict(res)

    def update_workspace_identity_detail(
        self, name: str, workspace_identity_detail: WorkspaceIdentityDetail, update_mask: FieldMask
    ) -> WorkspaceIdentityDetail:
        """Activates or deactivates a user or service principal in this workspace. You can only update
        ``workspace_identity_status``. You can't change your own status or the status of a group.

        :param name: str
          The resource name of the workspace identity detail, in the format
          ``principals/{principal_id}/workspace-identity-detail``.
        :param workspace_identity_detail: :class:`WorkspaceIdentityDetail`
          The workspace identity detail to update. Its ``name`` identifies the principal.
        :param update_mask: FieldMask
          The fields to update. The only supported field is ``workspace_identity_status``.

        :returns: :class:`WorkspaceIdentityDetail`
        """

        body = workspace_identity_detail.as_dict()
        query = {}
        if update_mask is not None:
            query["update_mask"] = update_mask.ToJsonString()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("PATCH", f"/api/2.0/identity/{name}", query=query, body=body, headers=headers)
        return WorkspaceIdentityDetail.from_dict(res)
