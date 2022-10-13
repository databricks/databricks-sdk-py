# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

from dataclasses import dataclass
from enum import Enum
from typing import Optional, Dict, List

__all__ = [
    
    'GetStatusRequest',
    'WorkspaceConf',
    
    'WorkspaceConf',
]

# all definitions in this file are in alphabetical order

@dataclass
class GetStatusRequest:
    
    
    keys: str # query

    def as_request(self) -> (dict, dict):
        getStatusRequest_query, getStatusRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.keys:
            getStatusRequest_query['keys'] = self.keys
        
        return getStatusRequest_query, getStatusRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetStatusRequest':
        return cls(
            keys=d.get('keys', None),
        )



type WorkspaceConf 'Dict[str,str]'


class WorkspaceConfAPI:
    def __init__(self, api_client):
        self._api = api_client
    
    def getStatus(self, request: GetStatusRequest) -> WorkspaceConf:
        """Check configuration status
        
        Gets the configuration status for a workspace."""
        query, body = request.as_request()
        json = self._api.do('GET', '/api/2.0/workspace-conf', query=query, body=body)
        return WorkspaceConf.from_dict(json)
    
    def setStatus(self, request: WorkspaceConf):
        """Enable/disable features
        
        Sets the configuration status for a workspace, including enabling or
        disabling it."""
        query, body = request.as_request()
        self._api.do('PATCH', '/api/2.0/workspace-conf', query=query, body=body)
        
    