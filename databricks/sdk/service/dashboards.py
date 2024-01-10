# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import Dict, Optional

_LOG = logging.getLogger('databricks.sdk')

# all definitions in this file are in alphabetical order


@dataclass
class PublishRequest:
    dashboard_id: Optional[str] = None
    """UUID identifying the dashboard to be published."""

    embed_credentials: Optional[bool] = None
    """Flag to indicate if the publisher's credentials should be embedded in the published dashboard.
    These embedded credentials will be used to execute the published dashboard's queries."""

    warehouse_id: Optional[str] = None
    """The ID of the warehouse that can be used to override the warehouse which was set in the draft."""

    def as_dict(self) -> dict:
        """Serializes the PublishRequest into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.dashboard_id is not None: body['dashboard_id'] = self.dashboard_id
        if self.embed_credentials is not None: body['embed_credentials'] = self.embed_credentials
        if self.warehouse_id is not None: body['warehouse_id'] = self.warehouse_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> PublishRequest:
        """Deserializes the PublishRequest from a dictionary."""
        return cls(dashboard_id=d.get('dashboard_id', None),
                   embed_credentials=d.get('embed_credentials', None),
                   warehouse_id=d.get('warehouse_id', None))


class LakeviewAPI:
    """These APIs provide specific management operations for Lakeview dashboards. Generic resource management can
    be done with Workspace API (import, export, get-status, list, delete)."""

    def __init__(self, api_client):
        self._api = api_client

    def publish(self,
                dashboard_id: str,
                *,
                embed_credentials: Optional[bool] = None,
                warehouse_id: Optional[str] = None):
        """Publish dashboard.
        
        Publish the current draft dashboard.
        
        :param dashboard_id: str
          UUID identifying the dashboard to be published.
        :param embed_credentials: bool (optional)
          Flag to indicate if the publisher's credentials should be embedded in the published dashboard. These
          embedded credentials will be used to execute the published dashboard's queries.
        :param warehouse_id: str (optional)
          The ID of the warehouse that can be used to override the warehouse which was set in the draft.
        
        
        """
        body = {}
        if embed_credentials is not None: body['embed_credentials'] = embed_credentials
        if warehouse_id is not None: body['warehouse_id'] = warehouse_id
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        self._api.do('POST',
                     f'/api/2.0/lakeview/dashboards/{dashboard_id}/published',
                     body=body,
                     headers=headers)
