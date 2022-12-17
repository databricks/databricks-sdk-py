# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Any


# all definitions in this file are in alphabetical order


@dataclass
class CreateTokenRequest:

    # Optional description to attach to the token.
    comment: str
    # The lifetime of the token, in seconds.
    #
    # If the ifetime is not specified, this token remains valid indefinitely.
    lifetime_seconds: int

    def as_dict(self) -> dict:
        body = {}
        if self.comment:
            body["comment"] = self.comment
        if self.lifetime_seconds:
            body["lifetime_seconds"] = self.lifetime_seconds

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "CreateTokenRequest":
        return cls(
            comment=d.get("comment", None),
            lifetime_seconds=d.get("lifetime_seconds", None),
        )


@dataclass
class CreateTokenResponse:

    # The information for the new token.
    token_info: "PublicTokenInfo"
    # The value of the new token.
    token_value: str

    def as_dict(self) -> dict:
        body = {}
        if self.token_info:
            body["token_info"] = self.token_info.as_dict()
        if self.token_value:
            body["token_value"] = self.token_value

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "CreateTokenResponse":
        return cls(
            token_info=PublicTokenInfo.from_dict(d["token_info"])
            if "token_info" in d
            else None,
            token_value=d.get("token_value", None),
        )


@dataclass
class ListTokensResponse:

    # The information for each token.
    token_infos: "List[PublicTokenInfo]"

    def as_dict(self) -> dict:
        body = {}
        if self.token_infos:
            body["token_infos"] = [v.as_dict() for v in self.token_infos]

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ListTokensResponse":
        return cls(
            token_infos=[PublicTokenInfo.from_dict(v) for v in d["token_infos"]]
            if "token_infos" in d
            else None,
        )


@dataclass
class PublicTokenInfo:

    # Comment the token was created with, if applicable.
    comment: str
    # Server time (in epoch milliseconds) when the token was created.
    creation_time: int
    # Server time (in epoch milliseconds) when the token will expire, or -1 if not applicable.
    expiry_time: int
    # The ID of this token.
    token_id: str

    def as_dict(self) -> dict:
        body = {}
        if self.comment:
            body["comment"] = self.comment
        if self.creation_time:
            body["creation_time"] = self.creation_time
        if self.expiry_time:
            body["expiry_time"] = self.expiry_time
        if self.token_id:
            body["token_id"] = self.token_id

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "PublicTokenInfo":
        return cls(
            comment=d.get("comment", None),
            creation_time=d.get("creation_time", None),
            expiry_time=d.get("expiry_time", None),
            token_id=d.get("token_id", None),
        )


@dataclass
class RevokeTokenRequest:

    # The ID of the token to be revoked.
    token_id: str

    def as_dict(self) -> dict:
        body = {}
        if self.token_id:
            body["token_id"] = self.token_id

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "RevokeTokenRequest":
        return cls(
            token_id=d.get("token_id", None),
        )


class TokensAPI:
    def __init__(self, api_client):
        self._api = api_client

    def create(
        self, *, comment: str = None, lifetime_seconds: int = None, **kwargs
    ) -> CreateTokenResponse:
        """Create a user token.

        Creates and returns a token for a user. If this call is made through
        token authentication, it creates a token with the same client ID as the
        authenticated token. If the user's token quota is exceeded, this call
        returns an error **QUOTA_EXCEEDED**."""
        request = kwargs.get("request", None)
        if not request:  # request is not given through keyed args
            request = CreateTokenRequest(
                comment=comment, lifetime_seconds=lifetime_seconds
            )
        body = request.as_dict()

        json = self._api.do("POST", "/api/2.0/token/create", body=body)
        return CreateTokenResponse.from_dict(json)

    def delete(self, token_id: str, **kwargs):
        """Revoke token.

        Revokes an access token.

        If a token with the specified ID is not valid, this call returns an
        error **RESOURCE_DOES_NOT_EXIST**."""
        request = kwargs.get("request", None)
        if not request:  # request is not given through keyed args
            request = RevokeTokenRequest(token_id=token_id)
        body = request.as_dict()

        self._api.do("POST", "/api/2.0/token/delete", body=body)

    def list(self) -> ListTokensResponse:
        """List tokens.

        Lists all the valid tokens for a user-workspace pair."""

        json = self._api.do("GET", "/api/2.0/token/list")
        return ListTokensResponse.from_dict(json)
