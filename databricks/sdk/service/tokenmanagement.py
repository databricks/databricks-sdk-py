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

    def as_request(self) -> (dict, dict):
        createOboTokenRequest_query, createOboTokenRequest_body = {}, {}
        if self.application_id:
            createOboTokenRequest_body["application_id"] = self.application_id
        if self.comment:
            createOboTokenRequest_body["comment"] = self.comment
        if self.lifetime_seconds:
            createOboTokenRequest_body["lifetime_seconds"] = self.lifetime_seconds

        return createOboTokenRequest_query, createOboTokenRequest_body

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

    def as_request(self) -> (dict, dict):
        createOboTokenResponse_query, createOboTokenResponse_body = {}, {}
        if self.token_info:
            createOboTokenResponse_body["token_info"] = self.token_info.as_request()[1]
        if self.token_value:
            createOboTokenResponse_body["token_value"] = self.token_value

        return createOboTokenResponse_query, createOboTokenResponse_body

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

    def as_request(self) -> (dict, dict):
        delete_query, delete_body = {}, {}
        if self.token_id:
            delete_body["token_id"] = self.token_id

        return delete_query, delete_body

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

    def as_request(self) -> (dict, dict):
        get_query, get_body = {}, {}
        if self.token_id:
            get_body["token_id"] = self.token_id

        return get_query, get_body

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

    def as_request(self) -> (dict, dict):
        list_query, list_body = {}, {}
        if self.created_by_id:
            list_query["created_by_id"] = self.created_by_id
        if self.created_by_username:
            list_query["created_by_username"] = self.created_by_username

        return list_query, list_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "List":
        return cls(
            created_by_id=d.get("created_by_id", None),
            created_by_username=d.get("created_by_username", None),
        )


@dataclass
class ListTokensResponse:

    token_infos: "List[TokenInfo]"

    def as_request(self) -> (dict, dict):
        listTokensResponse_query, listTokensResponse_body = {}, {}
        if self.token_infos:
            listTokensResponse_body["token_infos"] = [
                v.as_request()[1] for v in self.token_infos
            ]

        return listTokensResponse_query, listTokensResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ListTokensResponse":
        return cls(
            token_infos=[TokenInfo.from_dict(v) for v in d["token_infos"]]
            if "token_infos" in d
            else None,
        )


@dataclass
class TokenInfo:

    # Comment that describes the purpose of the token, specified by the token
    # creator.
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

    def as_request(self) -> (dict, dict):
        tokenInfo_query, tokenInfo_body = {}, {}
        if self.comment:
            tokenInfo_body["comment"] = self.comment
        if self.created_by_id:
            tokenInfo_body["created_by_id"] = self.created_by_id
        if self.created_by_username:
            tokenInfo_body["created_by_username"] = self.created_by_username
        if self.creation_time:
            tokenInfo_body["creation_time"] = self.creation_time
        if self.expiry_time:
            tokenInfo_body["expiry_time"] = self.expiry_time
        if self.owner_id:
            tokenInfo_body["owner_id"] = self.owner_id
        if self.token_id:
            tokenInfo_body["token_id"] = self.token_id

        return tokenInfo_query, tokenInfo_body

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
        self, request: CreateOboTokenRequest
    ) -> CreateOboTokenResponse:
        """Create on-behalf token.

        Creates a token on behalf of a service principal."""
        query, body = request.as_request()
        json = self._api.do(
            "POST",
            "/api/2.0/token-management/on-behalf-of/tokens",
            query=query,
            body=body,
        )
        return CreateOboTokenResponse.from_dict(json)

    def delete(self, request: Delete):
        """Delete a token.

        Deletes a token, specified by its ID."""
        query, body = request.as_request()
        self._api.do(
            "DELETE",
            f"/api/2.0/token-management/tokens/{request.token_id}",
            query=query,
            body=body,
        )

    def get(self, request: Get) -> TokenInfo:
        """Get token info.

        Gets information about a token, specified by its ID."""
        query, body = request.as_request()
        json = self._api.do(
            "GET",
            f"/api/2.0/token-management/tokens/{request.token_id}",
            query=query,
            body=body,
        )
        return TokenInfo.from_dict(json)

    def list(self, request: List) -> ListTokensResponse:
        """List all tokens.

        Lists all tokens associated with the specified workspace or user."""
        query, body = request.as_request()
        json = self._api.do(
            "GET", "/api/2.0/token-management/tokens", query=query, body=body
        )
        return ListTokensResponse.from_dict(json)
