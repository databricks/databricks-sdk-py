# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

import logging
from dataclasses import dataclass
from typing import Dict

_LOG = logging.getLogger('databricks.sdk')

# all definitions in this file are in alphabetical order


@dataclass
class GetStatus:
    """Check configuration status"""

    keys: str


WorkspaceConf = Dict[str, str]


class WorkspaceConfAPI:
    """This API allows updating known workspace settings for advanced users."""

    def __init__(self, api_client):
        self._api = api_client

    def get_status(self, keys: str, **kwargs) -> WorkspaceConf:
        """Check configuration status.
        
        Gets the configuration status for a workspace."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GetStatus(keys=keys)

        query = {}
        if keys: query['keys'] = request.keys

        json = self._api.do('GET', '/api/2.0/workspace-conf', query=query)
        return WorkspaceConf.from_dict(json)

    def set_status(self, **kwargs):
        """Enable/disable features.
        
        Sets the configuration status for a workspace, including enabling or disabling it."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = Dict[str, str]()

        self._api.do('PATCH', '/api/2.0/workspace-conf')
