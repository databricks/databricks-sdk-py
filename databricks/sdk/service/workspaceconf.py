# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

from dataclasses import dataclass
from enum import Enum
from typing import Optional, Dict, List, Any


# all definitions in this file are in alphabetical order


@dataclass
class GetStatus:
    """Check configuration status"""

    keys: str  # query

    def as_dict(self) -> dict:
        body = {}
        if self.keys:
            body["keys"] = self.keys

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "GetStatus":
        return cls(
            keys=d.get("keys", None),
        )


WorkspaceConf = Dict[str, str]


class WorkspaceConfAPI:
    def __init__(self, api_client):
        self._api = api_client

    def get_status(self, keys: str, **kwargs) -> WorkspaceConf:
        """Check configuration status.

        Gets the configuration status for a workspace."""

        request = kwargs.get("request", None)
        if not request:
            request = GetStatus(keys=keys)
        body = request.as_dict()

        query = {}
        if keys:
            query["keys"] = request.keys

        json = self._api.do("GET", "/api/2.0/workspace-conf", query=query, body=body)
        return WorkspaceConf.from_dict(json)

    def set_status(self, **kwargs):
        """Enable/disable features.

        Sets the configuration status for a workspace, including enabling or
        disabling it."""

        request = kwargs.get("request", None)
        if not request:
            request = Dict[str, str]()
        body = request.as_dict()

        self._api.do("PATCH", "/api/2.0/workspace-conf", body=body)
