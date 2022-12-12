# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

from dataclasses import dataclass
from enum import Enum
from typing import Optional, Dict, List, Any


# all definitions in this file are in alphabetical order


@dataclass
class GetStatus:
    """Check configuration status"""

    keys: str  # query

    def as_request(self) -> (dict, dict):
        getStatus_query, getStatus_body = {}, {}
        if self.keys:
            getStatus_query["keys"] = self.keys

        return getStatus_query, getStatus_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "GetStatus":
        return cls(
            keys=d.get("keys", None),
        )


WorkspaceConf = Dict[str, str]


class WorkspaceConfAPI:
    def __init__(self, api_client):
        self._api = api_client

    def get_status(self, request: GetStatus) -> WorkspaceConf:
        """Check configuration status.

        Gets the configuration status for a workspace."""
        query, body = request.as_request()
        json = self._api.do("GET", "/api/2.0/workspace-conf", query=query, body=body)
        return WorkspaceConf.from_dict(json)

    def set_status(self, request: WorkspaceConf):
        """Enable/disable features.

        Sets the configuration status for a workspace, including enabling or
        disabling it."""
        query, body = request.as_request()
        self._api.do("PATCH", "/api/2.0/workspace-conf", query=query, body=body)
