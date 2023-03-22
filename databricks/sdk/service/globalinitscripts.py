# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

import logging
from dataclasses import dataclass
from typing import Dict, Iterator, List

from ._internal import _repeated

_LOG = logging.getLogger('databricks.sdk')

# all definitions in this file are in alphabetical order


@dataclass
class CreateResponse:
    script_id: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.script_id: body['script_id'] = self.script_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateResponse':
        return cls(script_id=d.get('script_id', None))


@dataclass
class Delete:
    """Delete init script"""

    script_id: str


@dataclass
class Get:
    """Get an init script"""

    script_id: str


@dataclass
class GlobalInitScriptCreateRequest:
    name: str
    script: str
    enabled: bool = None
    position: int = None

    def as_dict(self) -> dict:
        body = {}
        if self.enabled: body['enabled'] = self.enabled
        if self.name: body['name'] = self.name
        if self.position: body['position'] = self.position
        if self.script: body['script'] = self.script
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GlobalInitScriptCreateRequest':
        return cls(enabled=d.get('enabled', None),
                   name=d.get('name', None),
                   position=d.get('position', None),
                   script=d.get('script', None))


@dataclass
class GlobalInitScriptDetails:
    created_at: int = None
    created_by: str = None
    enabled: bool = None
    name: str = None
    position: int = None
    script_id: str = None
    updated_at: int = None
    updated_by: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.created_at: body['created_at'] = self.created_at
        if self.created_by: body['created_by'] = self.created_by
        if self.enabled: body['enabled'] = self.enabled
        if self.name: body['name'] = self.name
        if self.position: body['position'] = self.position
        if self.script_id: body['script_id'] = self.script_id
        if self.updated_at: body['updated_at'] = self.updated_at
        if self.updated_by: body['updated_by'] = self.updated_by
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GlobalInitScriptDetails':
        return cls(created_at=d.get('created_at', None),
                   created_by=d.get('created_by', None),
                   enabled=d.get('enabled', None),
                   name=d.get('name', None),
                   position=d.get('position', None),
                   script_id=d.get('script_id', None),
                   updated_at=d.get('updated_at', None),
                   updated_by=d.get('updated_by', None))


@dataclass
class GlobalInitScriptDetailsWithContent:
    created_at: int = None
    created_by: str = None
    enabled: bool = None
    name: str = None
    position: int = None
    script: str = None
    script_id: str = None
    updated_at: int = None
    updated_by: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.created_at: body['created_at'] = self.created_at
        if self.created_by: body['created_by'] = self.created_by
        if self.enabled: body['enabled'] = self.enabled
        if self.name: body['name'] = self.name
        if self.position: body['position'] = self.position
        if self.script: body['script'] = self.script
        if self.script_id: body['script_id'] = self.script_id
        if self.updated_at: body['updated_at'] = self.updated_at
        if self.updated_by: body['updated_by'] = self.updated_by
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GlobalInitScriptDetailsWithContent':
        return cls(created_at=d.get('created_at', None),
                   created_by=d.get('created_by', None),
                   enabled=d.get('enabled', None),
                   name=d.get('name', None),
                   position=d.get('position', None),
                   script=d.get('script', None),
                   script_id=d.get('script_id', None),
                   updated_at=d.get('updated_at', None),
                   updated_by=d.get('updated_by', None))


@dataclass
class GlobalInitScriptUpdateRequest:
    name: str
    script: str
    script_id: str
    enabled: bool = None
    position: int = None

    def as_dict(self) -> dict:
        body = {}
        if self.enabled: body['enabled'] = self.enabled
        if self.name: body['name'] = self.name
        if self.position: body['position'] = self.position
        if self.script: body['script'] = self.script
        if self.script_id: body['script_id'] = self.script_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GlobalInitScriptUpdateRequest':
        return cls(enabled=d.get('enabled', None),
                   name=d.get('name', None),
                   position=d.get('position', None),
                   script=d.get('script', None),
                   script_id=d.get('script_id', None))


@dataclass
class ListGlobalInitScriptsResponse:
    scripts: 'List[GlobalInitScriptDetails]' = None

    def as_dict(self) -> dict:
        body = {}
        if self.scripts: body['scripts'] = [v.as_dict() for v in self.scripts]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListGlobalInitScriptsResponse':
        return cls(scripts=_repeated(d, 'scripts', GlobalInitScriptDetails))


class GlobalInitScriptsAPI:
    """The Global Init Scripts API enables Workspace administrators to configure global initialization scripts
    for their workspace. These scripts run on every node in every cluster in the workspace.
    
    **Important:** Existing clusters must be restarted to pick up any changes made to global init scripts.
    Global init scripts are run in order. If the init script returns with a bad exit code, the Apache Spark
    container fails to launch and init scripts with later position are skipped. If enough containers fail, the
    entire cluster fails with a `GLOBAL_INIT_SCRIPT_FAILURE` error code."""

    def __init__(self, api_client):
        self._api = api_client

    def create(self,
               name: str,
               script: str,
               *,
               enabled: bool = None,
               position: int = None,
               **kwargs) -> CreateResponse:
        """Create init script.
        
        Creates a new global init script in this workspace."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GlobalInitScriptCreateRequest(enabled=enabled,
                                                    name=name,
                                                    position=position,
                                                    script=script)
        body = request.as_dict()

        json = self._api.do('POST', '/api/2.0/global-init-scripts', body=body)
        return CreateResponse.from_dict(json)

    def delete(self, script_id: str, **kwargs):
        """Delete init script.
        
        Deletes a global init script."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = Delete(script_id=script_id)

        self._api.do('DELETE', f'/api/2.0/global-init-scripts/{request.script_id}')

    def get(self, script_id: str, **kwargs) -> GlobalInitScriptDetailsWithContent:
        """Get an init script.
        
        Gets all the details of a script, including its Base64-encoded contents."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = Get(script_id=script_id)

        json = self._api.do('GET', f'/api/2.0/global-init-scripts/{request.script_id}')
        return GlobalInitScriptDetailsWithContent.from_dict(json)

    def list(self) -> Iterator[GlobalInitScriptDetails]:
        """Get init scripts.
        
        "Get a list of all global init scripts for this workspace. This returns all properties for each script
        but **not** the script contents. To retrieve the contents of a script, use the [get a global init
        script](#operation/get-script) operation."""

        json = self._api.do('GET', '/api/2.0/global-init-scripts')
        return [GlobalInitScriptDetails.from_dict(v) for v in json.get('scripts', [])]

    def update(self,
               name: str,
               script: str,
               script_id: str,
               *,
               enabled: bool = None,
               position: int = None,
               **kwargs):
        """Update init script.
        
        Updates a global init script, specifying only the fields to change. All fields are optional.
        Unspecified fields retain their current value."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GlobalInitScriptUpdateRequest(enabled=enabled,
                                                    name=name,
                                                    position=position,
                                                    script=script,
                                                    script_id=script_id)
        body = request.as_dict()
        self._api.do('PATCH', f'/api/2.0/global-init-scripts/{request.script_id}', body=body)
