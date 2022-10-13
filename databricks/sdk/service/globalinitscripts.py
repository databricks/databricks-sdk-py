# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

from dataclasses import dataclass
from enum import Enum
from typing import Optional, Dict, List

__all__ = [
    
    'CreateScriptResponse',
    'DeleteScriptRequest',
    'GetScriptRequest',
    'GlobalInitScriptCreateRequest',
    'GlobalInitScriptDetails',
    'GlobalInitScriptDetailsWithContent',
    'GlobalInitScriptUpdateRequest',
    'GlobalInitScriptsAPI',
]

# all definitions in this file are in alphabetical order

@dataclass
class CreateScriptResponse:
    
    # The global init script ID.
    script_id: str = None

    def as_request(self) -> (dict, dict):
        createScriptResponse_query, createScriptResponse_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.script_id:
            createScriptResponse_body['script_id'] = self.script_id
        
        return createScriptResponse_query, createScriptResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateScriptResponse':
        return cls(
            script_id=d.get('script_id', None),
        )



@dataclass
class DeleteScriptRequest:
    
    # The ID of the global init script.
    script_id: str # path

    def as_request(self) -> (dict, dict):
        deleteScriptRequest_query, deleteScriptRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.script_id:
            deleteScriptRequest_body['script_id'] = self.script_id
        
        return deleteScriptRequest_query, deleteScriptRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'DeleteScriptRequest':
        return cls(
            script_id=d.get('script_id', None),
        )



@dataclass
class GetScriptRequest:
    
    # The ID of the global init script.
    script_id: str # path

    def as_request(self) -> (dict, dict):
        getScriptRequest_query, getScriptRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.script_id:
            getScriptRequest_body['script_id'] = self.script_id
        
        return getScriptRequest_query, getScriptRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetScriptRequest':
        return cls(
            script_id=d.get('script_id', None),
        )



@dataclass
class GlobalInitScriptCreateRequest:
    
    
    name: str
    
    script: str
    
    enabled: bool = None
    
    position: int = None

    def as_request(self) -> (dict, dict):
        globalInitScriptCreateRequest_query, globalInitScriptCreateRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.enabled:
            globalInitScriptCreateRequest_body['enabled'] = self.enabled
        if self.name:
            globalInitScriptCreateRequest_body['name'] = self.name
        if self.position:
            globalInitScriptCreateRequest_body['position'] = self.position
        if self.script:
            globalInitScriptCreateRequest_body['script'] = self.script
        
        return globalInitScriptCreateRequest_query, globalInitScriptCreateRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GlobalInitScriptCreateRequest':
        return cls(
            enabled=d.get('enabled', None),
            name=d.get('name', None),
            position=d.get('position', None),
            script=d.get('script', None),
        )



@dataclass
class GlobalInitScriptDetails:
    
    # Time when the script was created, represented as a Unix timestamp in
    # milliseconds.
    created_at: int = None
    # The username of the user who created the script.
    created_by: str = None
    
    enabled: bool = None
    
    name: str = None
    
    position: int = None
    # The global init script ID.
    script_id: str = None
    # Time when the script was updated, represented as a Unix timestamp in
    # milliseconds.
    updated_at: int = None
    # The username of the user who last updated the script
    updated_by: str = None

    def as_request(self) -> (dict, dict):
        globalInitScriptDetails_query, globalInitScriptDetails_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.created_at:
            globalInitScriptDetails_body['created_at'] = self.created_at
        if self.created_by:
            globalInitScriptDetails_body['created_by'] = self.created_by
        if self.enabled:
            globalInitScriptDetails_body['enabled'] = self.enabled
        if self.name:
            globalInitScriptDetails_body['name'] = self.name
        if self.position:
            globalInitScriptDetails_body['position'] = self.position
        if self.script_id:
            globalInitScriptDetails_body['script_id'] = self.script_id
        if self.updated_at:
            globalInitScriptDetails_body['updated_at'] = self.updated_at
        if self.updated_by:
            globalInitScriptDetails_body['updated_by'] = self.updated_by
        
        return globalInitScriptDetails_query, globalInitScriptDetails_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GlobalInitScriptDetails':
        return cls(
            created_at=d.get('created_at', None),
            created_by=d.get('created_by', None),
            enabled=d.get('enabled', None),
            name=d.get('name', None),
            position=d.get('position', None),
            script_id=d.get('script_id', None),
            updated_at=d.get('updated_at', None),
            updated_by=d.get('updated_by', None),
        )



@dataclass
class GlobalInitScriptDetailsWithContent:
    
    # Time when the script was created, represented as a Unix timestamp in
    # milliseconds.
    created_at: int = None
    # The username of the user who created the script.
    created_by: str = None
    
    enabled: bool = None
    
    name: str = None
    
    position: int = None
    
    script: str = None
    # The global init script ID.
    script_id: str = None
    # Time when the script was updated, represented as a Unix timestamp in
    # milliseconds.
    updated_at: int = None
    # The username of the user who last updated the script
    updated_by: str = None

    def as_request(self) -> (dict, dict):
        globalInitScriptDetailsWithContent_query, globalInitScriptDetailsWithContent_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.created_at:
            globalInitScriptDetailsWithContent_body['created_at'] = self.created_at
        if self.created_by:
            globalInitScriptDetailsWithContent_body['created_by'] = self.created_by
        if self.enabled:
            globalInitScriptDetailsWithContent_body['enabled'] = self.enabled
        if self.name:
            globalInitScriptDetailsWithContent_body['name'] = self.name
        if self.position:
            globalInitScriptDetailsWithContent_body['position'] = self.position
        if self.script:
            globalInitScriptDetailsWithContent_body['script'] = self.script
        if self.script_id:
            globalInitScriptDetailsWithContent_body['script_id'] = self.script_id
        if self.updated_at:
            globalInitScriptDetailsWithContent_body['updated_at'] = self.updated_at
        if self.updated_by:
            globalInitScriptDetailsWithContent_body['updated_by'] = self.updated_by
        
        return globalInitScriptDetailsWithContent_query, globalInitScriptDetailsWithContent_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GlobalInitScriptDetailsWithContent':
        return cls(
            created_at=d.get('created_at', None),
            created_by=d.get('created_by', None),
            enabled=d.get('enabled', None),
            name=d.get('name', None),
            position=d.get('position', None),
            script=d.get('script', None),
            script_id=d.get('script_id', None),
            updated_at=d.get('updated_at', None),
            updated_by=d.get('updated_by', None),
        )



@dataclass
class GlobalInitScriptUpdateRequest:
    
    # The ID of the global init script.
    script_id: str # path
    
    enabled: bool = None
    
    name: str = None
    
    position: int = None
    
    script: str = None

    def as_request(self) -> (dict, dict):
        globalInitScriptUpdateRequest_query, globalInitScriptUpdateRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.enabled:
            globalInitScriptUpdateRequest_body['enabled'] = self.enabled
        if self.name:
            globalInitScriptUpdateRequest_body['name'] = self.name
        if self.position:
            globalInitScriptUpdateRequest_body['position'] = self.position
        if self.script:
            globalInitScriptUpdateRequest_body['script'] = self.script
        if self.script_id:
            globalInitScriptUpdateRequest_body['script_id'] = self.script_id
        
        return globalInitScriptUpdateRequest_query, globalInitScriptUpdateRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GlobalInitScriptUpdateRequest':
        return cls(
            enabled=d.get('enabled', None),
            name=d.get('name', None),
            position=d.get('position', None),
            script=d.get('script', None),
            script_id=d.get('script_id', None),
        )

















class GlobalInitScriptsAPI:
    def __init__(self, api_client):
        self._api = api_client
    
    def createScript(self, request: GlobalInitScriptCreateRequest) -> CreateScriptResponse:
        """Create init script
        
        Creates a new global init script in this workspace."""
        query, body = request.as_request()
        json = self._api.do('POST', '/api/2.0/global-init-scripts', query=query, body=body)
        return CreateScriptResponse.from_dict(json)
    
    def deleteScript(self, request: DeleteScriptRequest):
        """Delete init script
        
        Deletes a global init script."""
        query, body = request.as_request()
        self._api.do('DELETE', f'/api/2.0/global-init-scripts/{request.script_id}', query=query, body=body)
        
    
    def getScript(self, request: GetScriptRequest) -> GlobalInitScriptDetailsWithContent:
        """Get an init script
        
        Gets all the details of a script, including its Base64-encoded contents."""
        query, body = request.as_request()
        json = self._api.do('GET', f'/api/2.0/global-init-scripts/{request.script_id}', query=query, body=body)
        return GlobalInitScriptDetailsWithContent.from_dict(json)
    
    def updateScript(self, request: GlobalInitScriptUpdateRequest):
        """Update init script
        
        Updates a global init script, specifying only the fields to change. All
        fields are optional. Unspecified fields retain their current value."""
        query, body = request.as_request()
        self._api.do('PATCH', f'/api/2.0/global-init-scripts/{request.script_id}', query=query, body=body)
        
    
    def get_all_scripts(self) -> List[GlobalInitScriptDetails]:
        """Get init scripts
        
        "Get a list of all global init scripts for this workspace. This returns
        all properties for each script but **not** the script contents. To
        retrieve the contents of a script, use the [get a global init
        script](#operation/get-script) operation."""
        json = self._api.do('GET', '/api/2.0/global-init-scripts')
        return [GlobalInitScriptDetails.from_dict(v) for v in json]
    