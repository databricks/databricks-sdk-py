# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

import logging
from dataclasses import dataclass
from typing import Dict, Iterator, List

from ._internal import _from_dict, _repeated

_LOG = logging.getLogger('databricks.sdk')

# all definitions in this file are in alphabetical order


@dataclass
class CreateTokenRequest:
    comment: str = None
    lifetime_seconds: int = None

    def as_dict(self) -> dict:
        body = {}
        if self.comment: body['comment'] = self.comment
        if self.lifetime_seconds: body['lifetime_seconds'] = self.lifetime_seconds
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateTokenRequest':
        return cls(comment=d.get('comment', None), lifetime_seconds=d.get('lifetime_seconds', None))


@dataclass
class CreateTokenResponse:
    token_info: 'PublicTokenInfo' = None
    token_value: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.token_info: body['token_info'] = self.token_info.as_dict()
        if self.token_value: body['token_value'] = self.token_value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateTokenResponse':
        return cls(token_info=_from_dict(d, 'token_info', PublicTokenInfo),
                   token_value=d.get('token_value', None))


@dataclass
class ListTokensResponse:
    token_infos: 'List[PublicTokenInfo]' = None

    def as_dict(self) -> dict:
        body = {}
        if self.token_infos: body['token_infos'] = [v.as_dict() for v in self.token_infos]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListTokensResponse':
        return cls(token_infos=_repeated(d, 'token_infos', PublicTokenInfo))


@dataclass
class PublicTokenInfo:
    comment: str = None
    creation_time: int = None
    expiry_time: int = None
    token_id: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.comment: body['comment'] = self.comment
        if self.creation_time: body['creation_time'] = self.creation_time
        if self.expiry_time: body['expiry_time'] = self.expiry_time
        if self.token_id: body['token_id'] = self.token_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'PublicTokenInfo':
        return cls(comment=d.get('comment', None),
                   creation_time=d.get('creation_time', None),
                   expiry_time=d.get('expiry_time', None),
                   token_id=d.get('token_id', None))


@dataclass
class RevokeTokenRequest:
    token_id: str

    def as_dict(self) -> dict:
        body = {}
        if self.token_id: body['token_id'] = self.token_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'RevokeTokenRequest':
        return cls(token_id=d.get('token_id', None))


class TokensAPI:
    """The Token API allows you to create, list, and revoke tokens that can be used to authenticate and access
    Databricks REST APIs."""

    def __init__(self, api_client):
        self._api = api_client

    def create(self, *, comment: str = None, lifetime_seconds: int = None, **kwargs) -> CreateTokenResponse:
        """Create a user token.
        
        Creates and returns a token for a user. If this call is made through token authentication, it creates
        a token with the same client ID as the authenticated token. If the user's token quota is exceeded,
        this call returns an error **QUOTA_EXCEEDED**."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = CreateTokenRequest(comment=comment, lifetime_seconds=lifetime_seconds)
        body = request.as_dict()

        json = self._api.do('POST', '/api/2.0/token/create', body=body)
        return CreateTokenResponse.from_dict(json)

    def delete(self, token_id: str, **kwargs):
        """Revoke token.
        
        Revokes an access token.
        
        If a token with the specified ID is not valid, this call returns an error **RESOURCE_DOES_NOT_EXIST**."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = RevokeTokenRequest(token_id=token_id)
        body = request.as_dict()
        self._api.do('POST', '/api/2.0/token/delete', body=body)

    def list(self) -> Iterator[PublicTokenInfo]:
        """List tokens.
        
        Lists all the valid tokens for a user-workspace pair."""

        json = self._api.do('GET', '/api/2.0/token/list')
        return [PublicTokenInfo.from_dict(v) for v in json.get('token_infos', [])]
