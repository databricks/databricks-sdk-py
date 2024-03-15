# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

from __future__ import annotations

import logging
from dataclasses import dataclass
from enum import Enum
from typing import Dict, Optional

from ._internal import _enum

_LOG = logging.getLogger('databricks.sdk')

# all definitions in this file are in alphabetical order


@dataclass
class CreateDashboardRequest:
    display_name: str
    """The display name of the dashboard."""

    parent_path: Optional[str] = None
    """The workspace path of the folder containing the dashboard. Includes leading slash and no
    trailing slash."""

    serialized_dashboard: Optional[str] = None
    """The contents of the dashboard in serialized string form."""

    warehouse_id: Optional[str] = None
    """The warehouse ID used to run the dashboard."""

    def as_dict(self) -> dict:
        """Serializes the CreateDashboardRequest into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.display_name is not None: body['display_name'] = self.display_name
        if self.parent_path is not None: body['parent_path'] = self.parent_path
        if self.serialized_dashboard is not None: body['serialized_dashboard'] = self.serialized_dashboard
        if self.warehouse_id is not None: body['warehouse_id'] = self.warehouse_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> CreateDashboardRequest:
        """Deserializes the CreateDashboardRequest from a dictionary."""
        return cls(display_name=d.get('display_name', None),
                   parent_path=d.get('parent_path', None),
                   serialized_dashboard=d.get('serialized_dashboard', None),
                   warehouse_id=d.get('warehouse_id', None))


@dataclass
class Dashboard:
    create_time: Optional[str] = None
    """The timestamp of when the dashboard was created."""

    dashboard_id: Optional[str] = None
    """UUID identifying the dashboard."""

    display_name: Optional[str] = None
    """The display name of the dashboard."""

    etag: Optional[str] = None
    """The etag for the dashboard. Can be optionally provided on updates to ensure that the dashboard
    has not been modified since the last read."""

    lifecycle_state: Optional[LifecycleState] = None
    """The state of the dashboard resource. Used for tracking trashed status."""

    parent_path: Optional[str] = None
    """The workspace path of the folder containing the dashboard. Includes leading slash and no
    trailing slash."""

    path: Optional[str] = None
    """The workspace path of the dashboard asset, including the file name."""

    serialized_dashboard: Optional[str] = None
    """The contents of the dashboard in serialized string form."""

    update_time: Optional[str] = None
    """The timestamp of when the dashboard was last updated by the user."""

    warehouse_id: Optional[str] = None
    """The warehouse ID used to run the dashboard."""

    def as_dict(self) -> dict:
        """Serializes the Dashboard into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.create_time is not None: body['create_time'] = self.create_time
        if self.dashboard_id is not None: body['dashboard_id'] = self.dashboard_id
        if self.display_name is not None: body['display_name'] = self.display_name
        if self.etag is not None: body['etag'] = self.etag
        if self.lifecycle_state is not None: body['lifecycle_state'] = self.lifecycle_state.value
        if self.parent_path is not None: body['parent_path'] = self.parent_path
        if self.path is not None: body['path'] = self.path
        if self.serialized_dashboard is not None: body['serialized_dashboard'] = self.serialized_dashboard
        if self.update_time is not None: body['update_time'] = self.update_time
        if self.warehouse_id is not None: body['warehouse_id'] = self.warehouse_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> Dashboard:
        """Deserializes the Dashboard from a dictionary."""
        return cls(create_time=d.get('create_time', None),
                   dashboard_id=d.get('dashboard_id', None),
                   display_name=d.get('display_name', None),
                   etag=d.get('etag', None),
                   lifecycle_state=_enum(d, 'lifecycle_state', LifecycleState),
                   parent_path=d.get('parent_path', None),
                   path=d.get('path', None),
                   serialized_dashboard=d.get('serialized_dashboard', None),
                   update_time=d.get('update_time', None),
                   warehouse_id=d.get('warehouse_id', None))


class LifecycleState(Enum):

    ACTIVE = 'ACTIVE'
    TRASHED = 'TRASHED'


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


@dataclass
class PublishedDashboard:
    display_name: Optional[str] = None
    """The display name of the published dashboard."""

    embed_credentials: Optional[bool] = None
    """Indicates whether credentials are embedded in the published dashboard."""

    revision_create_time: Optional[str] = None
    """The timestamp of when the published dashboard was last revised."""

    warehouse_id: Optional[str] = None
    """The warehouse ID used to run the published dashboard."""

    def as_dict(self) -> dict:
        """Serializes the PublishedDashboard into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.display_name is not None: body['display_name'] = self.display_name
        if self.embed_credentials is not None: body['embed_credentials'] = self.embed_credentials
        if self.revision_create_time is not None: body['revision_create_time'] = self.revision_create_time
        if self.warehouse_id is not None: body['warehouse_id'] = self.warehouse_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> PublishedDashboard:
        """Deserializes the PublishedDashboard from a dictionary."""
        return cls(display_name=d.get('display_name', None),
                   embed_credentials=d.get('embed_credentials', None),
                   revision_create_time=d.get('revision_create_time', None),
                   warehouse_id=d.get('warehouse_id', None))


@dataclass
class TrashDashboardResponse:

    def as_dict(self) -> dict:
        """Serializes the TrashDashboardResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> TrashDashboardResponse:
        """Deserializes the TrashDashboardResponse from a dictionary."""
        return cls()


@dataclass
class UpdateDashboardRequest:
    dashboard_id: Optional[str] = None
    """UUID identifying the dashboard."""

    display_name: Optional[str] = None
    """The display name of the dashboard."""

    etag: Optional[str] = None
    """The etag for the dashboard. Can be optionally provided on updates to ensure that the dashboard
    has not been modified since the last read."""

    serialized_dashboard: Optional[str] = None
    """The contents of the dashboard in serialized string form."""

    warehouse_id: Optional[str] = None
    """The warehouse ID used to run the dashboard."""

    def as_dict(self) -> dict:
        """Serializes the UpdateDashboardRequest into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.dashboard_id is not None: body['dashboard_id'] = self.dashboard_id
        if self.display_name is not None: body['display_name'] = self.display_name
        if self.etag is not None: body['etag'] = self.etag
        if self.serialized_dashboard is not None: body['serialized_dashboard'] = self.serialized_dashboard
        if self.warehouse_id is not None: body['warehouse_id'] = self.warehouse_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> UpdateDashboardRequest:
        """Deserializes the UpdateDashboardRequest from a dictionary."""
        return cls(dashboard_id=d.get('dashboard_id', None),
                   display_name=d.get('display_name', None),
                   etag=d.get('etag', None),
                   serialized_dashboard=d.get('serialized_dashboard', None),
                   warehouse_id=d.get('warehouse_id', None))


class LakeviewAPI:
    """These APIs provide specific management operations for Lakeview dashboards. Generic resource management can
    be done with Workspace API (import, export, get-status, list, delete)."""

    def __init__(self, api_client):
        self._api = api_client

    def create(self,
               display_name: str,
               *,
               parent_path: Optional[str] = None,
               serialized_dashboard: Optional[str] = None,
               warehouse_id: Optional[str] = None) -> Dashboard:
        """Create dashboard.
        
        Create a draft dashboard.
        
        :param display_name: str
          The display name of the dashboard.
        :param parent_path: str (optional)
          The workspace path of the folder containing the dashboard. Includes leading slash and no trailing
          slash.
        :param serialized_dashboard: str (optional)
          The contents of the dashboard in serialized string form.
        :param warehouse_id: str (optional)
          The warehouse ID used to run the dashboard.
        
        :returns: :class:`Dashboard`
        """
        body = {}
        if display_name is not None: body['display_name'] = display_name
        if parent_path is not None: body['parent_path'] = parent_path
        if serialized_dashboard is not None: body['serialized_dashboard'] = serialized_dashboard
        if warehouse_id is not None: body['warehouse_id'] = warehouse_id
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        res = self._api.do('POST', '/api/2.0/lakeview/dashboards', body=body, headers=headers)
        return Dashboard.from_dict(res)

    def get(self, dashboard_id: str) -> Dashboard:
        """Get dashboard.
        
        Get a draft dashboard.
        
        :param dashboard_id: str
          UUID identifying the dashboard.
        
        :returns: :class:`Dashboard`
        """

        headers = {'Accept': 'application/json', }

        res = self._api.do('GET', f'/api/2.0/lakeview/dashboards/{dashboard_id}', headers=headers)
        return Dashboard.from_dict(res)

    def get_published(self, dashboard_id: str) -> PublishedDashboard:
        """Get published dashboard.
        
        Get the current published dashboard.
        
        :param dashboard_id: str
          UUID identifying the dashboard to be published.
        
        :returns: :class:`PublishedDashboard`
        """

        headers = {'Accept': 'application/json', }

        res = self._api.do('GET', f'/api/2.0/lakeview/dashboards/{dashboard_id}/published', headers=headers)
        return PublishedDashboard.from_dict(res)

    def publish(self,
                dashboard_id: str,
                *,
                embed_credentials: Optional[bool] = None,
                warehouse_id: Optional[str] = None) -> PublishedDashboard:
        """Publish dashboard.
        
        Publish the current draft dashboard.
        
        :param dashboard_id: str
          UUID identifying the dashboard to be published.
        :param embed_credentials: bool (optional)
          Flag to indicate if the publisher's credentials should be embedded in the published dashboard. These
          embedded credentials will be used to execute the published dashboard's queries.
        :param warehouse_id: str (optional)
          The ID of the warehouse that can be used to override the warehouse which was set in the draft.
        
        :returns: :class:`PublishedDashboard`
        """
        body = {}
        if embed_credentials is not None: body['embed_credentials'] = embed_credentials
        if warehouse_id is not None: body['warehouse_id'] = warehouse_id
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        res = self._api.do('POST',
                           f'/api/2.0/lakeview/dashboards/{dashboard_id}/published',
                           body=body,
                           headers=headers)
        return PublishedDashboard.from_dict(res)

    def trash(self, dashboard_id: str):
        """Trash dashboard.
        
        Trash a dashboard.
        
        :param dashboard_id: str
          UUID identifying the dashboard.
        
        
        """

        headers = {'Accept': 'application/json', }

        self._api.do('DELETE', f'/api/2.0/lakeview/dashboards/{dashboard_id}', headers=headers)

    def update(self,
               dashboard_id: str,
               *,
               display_name: Optional[str] = None,
               etag: Optional[str] = None,
               serialized_dashboard: Optional[str] = None,
               warehouse_id: Optional[str] = None) -> Dashboard:
        """Update dashboard.
        
        Update a draft dashboard.
        
        :param dashboard_id: str
          UUID identifying the dashboard.
        :param display_name: str (optional)
          The display name of the dashboard.
        :param etag: str (optional)
          The etag for the dashboard. Can be optionally provided on updates to ensure that the dashboard has
          not been modified since the last read.
        :param serialized_dashboard: str (optional)
          The contents of the dashboard in serialized string form.
        :param warehouse_id: str (optional)
          The warehouse ID used to run the dashboard.
        
        :returns: :class:`Dashboard`
        """
        body = {}
        if display_name is not None: body['display_name'] = display_name
        if etag is not None: body['etag'] = etag
        if serialized_dashboard is not None: body['serialized_dashboard'] = serialized_dashboard
        if warehouse_id is not None: body['warehouse_id'] = warehouse_id
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        res = self._api.do('PATCH',
                           f'/api/2.0/lakeview/dashboards/{dashboard_id}',
                           body=body,
                           headers=headers)
        return Dashboard.from_dict(res)
