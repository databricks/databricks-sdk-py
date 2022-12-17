# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

from dataclasses import dataclass
from enum import Enum
from typing import Optional, Dict, List, Any


# all definitions in this file are in alphabetical order


@dataclass
class CreateOboTokenRequest:

    # Application ID of the service principal.
    application_id: str
    # Comment that describes the purpose of the token.
    comment: str
    # The number of seconds before the token expires.
    lifetime_seconds: int

    def as_dict(self) -> dict:
        body = {}
        if self.application_id:
            body["application_id"] = self.application_id
        if self.comment:
            body["comment"] = self.comment
        if self.lifetime_seconds:
            body["lifetime_seconds"] = self.lifetime_seconds

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "CreateOboTokenRequest":
        return cls(
            application_id=d.get("application_id", None),
            comment=d.get("comment", None),
            lifetime_seconds=d.get("lifetime_seconds", None),
        )


@dataclass
class CreateOboTokenResponse:

    token_info: "TokenInfo"
    # Value of the token.
    token_value: str

    def as_dict(self) -> dict:
        body = {}
        if self.token_info:
            body["token_info"] = self.token_info.as_dict()
        if self.token_value:
            body["token_value"] = self.token_value

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "CreateOboTokenResponse":
        return cls(
            token_info=TokenInfo.from_dict(d["token_info"])
            if "token_info" in d
            else None,
            token_value=d.get("token_value", None),
        )


@dataclass
class Delete:
    """Delete a token"""

    # The ID of the token to get.
    token_id: str  # path

    def as_dict(self) -> dict:
        body = {}
        if self.token_id:
            body["token_id"] = self.token_id

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "Delete":
        return cls(
            token_id=d.get("token_id", None),
        )


@dataclass
class Get:
    """Get token info"""

    # The ID of the token to get.
    token_id: str  # path

    def as_dict(self) -> dict:
        body = {}
        if self.token_id:
            body["token_id"] = self.token_id

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "Get":
        return cls(
            token_id=d.get("token_id", None),
        )


@dataclass
class List:
    """List all tokens"""

    # User ID of the user that created the token.
    created_by_id: str  # query
    # Username of the user that created the token.
    created_by_username: str  # query

    def as_dict(self) -> dict:
        body = {}
        if self.created_by_id:
            body["created_by_id"] = self.created_by_id
        if self.created_by_username:
            body["created_by_username"] = self.created_by_username

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "List":
        return cls(
            created_by_id=d.get("created_by_id", None),
            created_by_username=d.get("created_by_username", None),
        )


@dataclass
class ListTokensResponse:

    token_infos: "List[TokenInfo]"

    def as_dict(self) -> dict:
        body = {}
        if self.token_infos:
            body["token_infos"] = [v.as_dict() for v in self.token_infos]

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ListTokensResponse":
        return cls(
            token_infos=[TokenInfo.from_dict(v) for v in d["token_infos"]]
            if "token_infos" in d
            else None,
        )


@dataclass
class TokenInfo:

    # Comment that describes the purpose of the token, specified by the token creator.
    comment: str
    # User ID of the user that created the token.
    created_by_id: int
    # Username of the user that created the token.
    created_by_username: str
    # Timestamp when the token was created.
    creation_time: int
    # Timestamp when the token expires.
    expiry_time: int
    # User ID of the user that owns the token.
    owner_id: int
    # ID of the token.
    token_id: str

    def as_dict(self) -> dict:
        body = {}
        if self.comment:
            body["comment"] = self.comment
        if self.created_by_id:
            body["created_by_id"] = self.created_by_id
        if self.created_by_username:
            body["created_by_username"] = self.created_by_username
        if self.creation_time:
            body["creation_time"] = self.creation_time
        if self.expiry_time:
            body["expiry_time"] = self.expiry_time
        if self.owner_id:
            body["owner_id"] = self.owner_id
        if self.token_id:
            body["token_id"] = self.token_id

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "TokenInfo":
        return cls(
            comment=d.get("comment", None),
            created_by_id=d.get("created_by_id", None),
            created_by_username=d.get("created_by_username", None),
            creation_time=d.get("creation_time", None),
            expiry_time=d.get("expiry_time", None),
            owner_id=d.get("owner_id", None),
            token_id=d.get("token_id", None),
        )


class TokenManagementAPI:
    def __init__(self, api_client):
        self._api = api_client

    def create_obo_token(
        self,
        application_id: str,
        lifetime_seconds: int,
        *,
        comment: str = None,
        **kwargs,
    ) -> CreateOboTokenResponse:
        """Create on-behalf token.

        Creates a token on behalf of a service principal."""

        request = kwargs.get("request", None)
        if not request:
            request = CreateOboTokenRequest(
                application_id=application_id,
                comment=comment,
                lifetime_seconds=lifetime_seconds,
            )
        body = request.as_dict()

        json = self._api.do(
            "POST", "/api/2.0/token-management/on-behalf-of/tokens", body=body
        )
        return CreateOboTokenResponse.from_dict(json)

    def delete(self, token_id: str, **kwargs):
        """Delete a token.

        Deletes a token, specified by its ID."""

        request = kwargs.get("request", None)
        if not request:
            request = Delete(token_id=token_id)
        body = request.as_dict()

        self._api.do(
            "DELETE", f"/api/2.0/token-management/tokens/{token_id}", body=body
        )

    def get(self, token_id: str, **kwargs) -> TokenInfo:
        """Get token info.

        Gets information about a token, specified by its ID."""

        request = kwargs.get("request", None)
        if not request:
            request = Get(token_id=token_id)
        body = request.as_dict()

        json = self._api.do(
            "GET", f"/api/2.0/token-management/tokens/{token_id}", body=body
        )
        return TokenInfo.from_dict(json)

    def list(
        self, *, created_by_id: str = None, created_by_username: str = None, **kwargs
    ) -> ListTokensResponse:
        """List all tokens.

        Lists all tokens associated with the specified workspace or user."""

        request = kwargs.get("request", None)
        if not request:
            request = List(
                created_by_id=created_by_id, created_by_username=created_by_username
            )
        body = request.as_dict()

        query = {}
        if created_by_id:
            query["created_by_id"] = request.created_by_id
        if created_by_username:
            query["created_by_username"] = request.created_by_username

        json = self._api.do(
            "GET", "/api/2.0/token-management/tokens", query=query, body=body
        )
        return ListTokensResponse.from_dict(json)
