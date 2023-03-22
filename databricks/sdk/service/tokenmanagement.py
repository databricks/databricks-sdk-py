# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

import logging
from dataclasses import dataclass
from typing import Dict, Iterator, List

from ._internal import _from_dict, _repeated

_LOG = logging.getLogger('databricks.sdk')

# all definitions in this file are in alphabetical order


@dataclass
class CreateOboTokenRequest:
    application_id: str
    lifetime_seconds: int
    comment: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.application_id: body['application_id'] = self.application_id
        if self.comment: body['comment'] = self.comment
        if self.lifetime_seconds: body['lifetime_seconds'] = self.lifetime_seconds
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateOboTokenRequest':
        return cls(application_id=d.get('application_id', None),
                   comment=d.get('comment', None),
                   lifetime_seconds=d.get('lifetime_seconds', None))


@dataclass
class CreateOboTokenResponse:
    token_info: 'TokenInfo' = None
    token_value: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.token_info: body['token_info'] = self.token_info.as_dict()
        if self.token_value: body['token_value'] = self.token_value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateOboTokenResponse':
        return cls(token_info=_from_dict(d, 'token_info', TokenInfo), token_value=d.get('token_value', None))


@dataclass
class Delete:
    """Delete a token"""

    token_id: str


@dataclass
class Get:
    """Get token info"""

    token_id: str


@dataclass
class ListRequest:
    """List all tokens"""

    created_by_id: str = None
    created_by_username: str = None


@dataclass
class ListTokensResponse:
    token_infos: 'List[TokenInfo]' = None

    def as_dict(self) -> dict:
        body = {}
        if self.token_infos: body['token_infos'] = [v.as_dict() for v in self.token_infos]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListTokensResponse':
        return cls(token_infos=_repeated(d, 'token_infos', TokenInfo))


@dataclass
class TokenInfo:
    comment: str = None
    created_by_id: int = None
    created_by_username: str = None
    creation_time: int = None
    expiry_time: int = None
    owner_id: int = None
    token_id: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.comment: body['comment'] = self.comment
        if self.created_by_id: body['created_by_id'] = self.created_by_id
        if self.created_by_username: body['created_by_username'] = self.created_by_username
        if self.creation_time: body['creation_time'] = self.creation_time
        if self.expiry_time: body['expiry_time'] = self.expiry_time
        if self.owner_id: body['owner_id'] = self.owner_id
        if self.token_id: body['token_id'] = self.token_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'TokenInfo':
        return cls(comment=d.get('comment', None),
                   created_by_id=d.get('created_by_id', None),
                   created_by_username=d.get('created_by_username', None),
                   creation_time=d.get('creation_time', None),
                   expiry_time=d.get('expiry_time', None),
                   owner_id=d.get('owner_id', None),
                   token_id=d.get('token_id', None))


class TokenManagementAPI:
    """Enables administrators to get all tokens and delete tokens for other users. Admins can either get every
    token, get a specific token by ID, or get all tokens for a particular user."""

    def __init__(self, api_client):
        self._api = api_client

    def create_obo_token(self,
                         application_id: str,
                         lifetime_seconds: int,
                         *,
                         comment: str = None,
                         **kwargs) -> CreateOboTokenResponse:
        """Create on-behalf token.
        
        Creates a token on behalf of a service principal."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = CreateOboTokenRequest(application_id=application_id,
                                            comment=comment,
                                            lifetime_seconds=lifetime_seconds)
        body = request.as_dict()

        json = self._api.do('POST', '/api/2.0/token-management/on-behalf-of/tokens', body=body)
        return CreateOboTokenResponse.from_dict(json)

    def delete(self, token_id: str, **kwargs):
        """Delete a token.
        
        Deletes a token, specified by its ID."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = Delete(token_id=token_id)

        self._api.do('DELETE', f'/api/2.0/token-management/tokens/{request.token_id}')

    def get(self, token_id: str, **kwargs) -> TokenInfo:
        """Get token info.
        
        Gets information about a token, specified by its ID."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = Get(token_id=token_id)

        json = self._api.do('GET', f'/api/2.0/token-management/tokens/{request.token_id}')
        return TokenInfo.from_dict(json)

    def list(self,
             *,
             created_by_id: str = None,
             created_by_username: str = None,
             **kwargs) -> Iterator[TokenInfo]:
        """List all tokens.
        
        Lists all tokens associated with the specified workspace or user."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = ListRequest(created_by_id=created_by_id, created_by_username=created_by_username)

        query = {}
        if created_by_id: query['created_by_id'] = request.created_by_id
        if created_by_username: query['created_by_username'] = request.created_by_username

        json = self._api.do('GET', '/api/2.0/token-management/tokens', query=query)
        return [TokenInfo.from_dict(v) for v in json.get('token_infos', [])]
