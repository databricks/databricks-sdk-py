# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

from dataclasses import dataclass
from enum import Enum
from typing import Optional, Dict, List

__all__ = [
    
    'CreateOboTokenRequest',
    'CreateOboTokenResponse',
    'DeleteTokenRequest',
    'GetTokenInfoRequest',
    'ListAllTokensRequest',
    'ListTokensResponse',
    'TokenInfo',
    'ApplicationId',
    'Comment',
    'CommentInput',
    'CreatedById',
    'CreatedByUsername',
    'CreationTime',
    'ExpiryTime',
    'LifetimeSeconds',
    'OwnerId',
    'TokenId',
    'TokenValue',
    
    'TokenManagement',
]

# all definitions in this file are in alphabetical order

@dataclass
class CreateOboTokenRequest:
    
    
    application_id: str
    
    comment: str
    
    lifetime_seconds: any /* MISSING TYPE */

    def as_request(self) -> (dict, dict):
        createOboTokenRequest_query, createOboTokenRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.application_id:
            createOboTokenRequest_body['application_id'] = self.application_id
        if self.comment:
            createOboTokenRequest_body['comment'] = self.comment
        if self.lifetime_seconds:
            createOboTokenRequest_body['lifetime_seconds'] = self.lifetime_seconds
        
        return createOboTokenRequest_query, createOboTokenRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateOboTokenRequest':
        return cls(
            application_id=d.get('application_id', None),
            comment=d.get('comment', None),
            lifetime_seconds=d.get('lifetime_seconds', None),
        )



@dataclass
class CreateOboTokenResponse:
    
    
    token_info: 'TokenInfo' = None
    
    token_value: str = None

    def as_request(self) -> (dict, dict):
        createOboTokenResponse_query, createOboTokenResponse_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.token_info:
            createOboTokenResponse_body['token_info'] = self.token_info.as_request()[1]
        if self.token_value:
            createOboTokenResponse_body['token_value'] = self.token_value
        
        return createOboTokenResponse_query, createOboTokenResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateOboTokenResponse':
        return cls(
            token_info=TokenInfo.from_dict(d['token_info']) if 'token_info' in d else None,
            token_value=d.get('token_value', None),
        )



@dataclass
class DeleteTokenRequest:
    
    # The ID of the token to get.
    token_id: str # path

    def as_request(self) -> (dict, dict):
        deleteTokenRequest_query, deleteTokenRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.token_id:
            deleteTokenRequest_body['token_id'] = self.token_id
        
        return deleteTokenRequest_query, deleteTokenRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'DeleteTokenRequest':
        return cls(
            token_id=d.get('token_id', None),
        )



@dataclass
class GetTokenInfoRequest:
    
    # The ID of the token to get.
    token_id: str # path

    def as_request(self) -> (dict, dict):
        getTokenInfoRequest_query, getTokenInfoRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.token_id:
            getTokenInfoRequest_body['token_id'] = self.token_id
        
        return getTokenInfoRequest_query, getTokenInfoRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetTokenInfoRequest':
        return cls(
            token_id=d.get('token_id', None),
        )



@dataclass
class ListAllTokensRequest:
    
    # User ID of the user that created the token.
    created_by_id: str = None # query
    # Username of the user that created the token.
    created_by_username: str = None # query

    def as_request(self) -> (dict, dict):
        listAllTokensRequest_query, listAllTokensRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.created_by_id:
            listAllTokensRequest_query['created_by_id'] = self.created_by_id
        if self.created_by_username:
            listAllTokensRequest_query['created_by_username'] = self.created_by_username
        
        return listAllTokensRequest_query, listAllTokensRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListAllTokensRequest':
        return cls(
            created_by_id=d.get('created_by_id', None),
            created_by_username=d.get('created_by_username', None),
        )



@dataclass
class ListTokensResponse:
    
    
    token_infos: 'List[TokenInfo]' = None

    def as_request(self) -> (dict, dict):
        listTokensResponse_query, listTokensResponse_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.token_infos:
            listTokensResponse_body['token_infos'] = [v.as_request()[1] for v in self.token_infos]
        
        return listTokensResponse_query, listTokensResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListTokensResponse':
        return cls(
            token_infos=[TokenInfo.from_dict(v) for v in d['token_infos']] if 'token_infos' in d else None,
        )



@dataclass
class TokenInfo:
    
    
    comment: str = None
    
    created_by_id: int = None
    
    created_by_username: str = None
    
    creation_time: int = None
    
    expiry_time: int = None
    
    owner_id: int = None
    
    token_id: str = None

    def as_request(self) -> (dict, dict):
        tokenInfo_query, tokenInfo_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.comment:
            tokenInfo_body['comment'] = self.comment
        if self.created_by_id:
            tokenInfo_body['created_by_id'] = self.created_by_id
        if self.created_by_username:
            tokenInfo_body['created_by_username'] = self.created_by_username
        if self.creation_time:
            tokenInfo_body['creation_time'] = self.creation_time
        if self.expiry_time:
            tokenInfo_body['expiry_time'] = self.expiry_time
        if self.owner_id:
            tokenInfo_body['owner_id'] = self.owner_id
        if self.token_id:
            tokenInfo_body['token_id'] = self.token_id
        
        return tokenInfo_query, tokenInfo_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'TokenInfo':
        return cls(
            comment=d.get('comment', None),
            created_by_id=d.get('created_by_id', None),
            created_by_username=d.get('created_by_username', None),
            creation_time=d.get('creation_time', None),
            expiry_time=d.get('expiry_time', None),
            owner_id=d.get('owner_id', None),
            token_id=d.get('token_id', None),
        )

























class TokenManagementAPI:
    def __init__(self, api_client):
        self._api = api_client
    
    def createOboToken(self, request: CreateOboTokenRequest) -> CreateOboTokenResponse:
        """Create on-behalf token
        
        Creates a token on behalf of a service principal."""
        query, body = request.as_request()
        json = self._api.do('POST', '/api/2.0/token-management/on-behalf-of/tokens', query=query, body=body)
        return CreateOboTokenResponse.from_dict(json)
    
    def deleteToken(self, request: DeleteTokenRequest):
        """Delete a token
        
        Deletes a token, specified by its ID."""
        query, body = request.as_request()
        self._api.do('DELETE', f'/api/2.0/token-management/tokens/{request.token_id}', query=query, body=body)
        
    
    def getTokenInfo(self, request: GetTokenInfoRequest) -> TokenInfo:
        """Get token info
        
        Gets information about a token, specified by its ID."""
        query, body = request.as_request()
        json = self._api.do('GET', f'/api/2.0/token-management/tokens/{request.token_id}', query=query, body=body)
        return TokenInfo.from_dict(json)
    
    def listAllTokens(self, request: ListAllTokensRequest) -> ListTokensResponse:
        """List all tokens
        
        Lists all tokens associated with the specified workspace or user."""
        query, body = request.as_request()
        json = self._api.do('GET', '/api/2.0/token-management/tokens', query=query, body=body)
        return ListTokensResponse.from_dict(json)
    