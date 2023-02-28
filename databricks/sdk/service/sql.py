# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Any, Iterator
import time
import random
import logging
from ..errors import OperationTimeout, OperationFailed

_LOG = logging.getLogger('databricks.sdk.service.sql')

# all definitions in this file are in alphabetical order


@dataclass
class AccessControl:
    group_name: str
    permission_level: 'PermissionLevel'
    user_name: str

    def as_dict(self) -> dict:
        body = {}
        if self.group_name: body['group_name'] = self.group_name
        if self.permission_level: body['permission_level'] = self.permission_level.value
        if self.user_name: body['user_name'] = self.user_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'AccessControl':
        return cls(
            group_name=d.get('group_name', None),
            permission_level=PermissionLevel(d['permission_level']) if 'permission_level' in d else None,
            user_name=d.get('user_name', None))


@dataclass
class Alert:
    created_at: str
    id: str
    last_triggered_at: str
    name: str
    options: 'AlertOptions'
    parent: str
    query: 'Query'
    rearm: int
    state: 'AlertState'
    updated_at: str
    user: 'User'

    def as_dict(self) -> dict:
        body = {}
        if self.created_at: body['created_at'] = self.created_at
        if self.id: body['id'] = self.id
        if self.last_triggered_at: body['last_triggered_at'] = self.last_triggered_at
        if self.name: body['name'] = self.name
        if self.options: body['options'] = self.options.as_dict()
        if self.parent: body['parent'] = self.parent
        if self.query: body['query'] = self.query.as_dict()
        if self.rearm: body['rearm'] = self.rearm
        if self.state: body['state'] = self.state.value
        if self.updated_at: body['updated_at'] = self.updated_at
        if self.user: body['user'] = self.user.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Alert':
        return cls(created_at=d.get('created_at', None),
                   id=d.get('id', None),
                   last_triggered_at=d.get('last_triggered_at', None),
                   name=d.get('name', None),
                   options=AlertOptions.from_dict(d['options']) if 'options' in d else None,
                   parent=d.get('parent', None),
                   query=Query.from_dict(d['query']) if 'query' in d else None,
                   rearm=d.get('rearm', None),
                   state=AlertState(d['state']) if 'state' in d else None,
                   updated_at=d.get('updated_at', None),
                   user=User.from_dict(d['user']) if 'user' in d else None)


@dataclass
class AlertOptions:
    """Alert configuration options."""

    column: str
    custom_body: str
    custom_subject: str
    muted: bool
    op: str
    schedule_failures: int
    value: str

    def as_dict(self) -> dict:
        body = {}
        if self.column: body['column'] = self.column
        if self.custom_body: body['custom_body'] = self.custom_body
        if self.custom_subject: body['custom_subject'] = self.custom_subject
        if self.muted: body['muted'] = self.muted
        if self.op: body['op'] = self.op
        if self.schedule_failures: body['schedule_failures'] = self.schedule_failures
        if self.value: body['value'] = self.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'AlertOptions':
        return cls(column=d.get('column', None),
                   custom_body=d.get('custom_body', None),
                   custom_subject=d.get('custom_subject', None),
                   muted=d.get('muted', None),
                   op=d.get('op', None),
                   schedule_failures=d.get('schedule_failures', None),
                   value=d.get('value', None))


class AlertState(Enum):
    """State of the alert. Possible values are: `unknown` (yet to be evaluated), `triggered` (evaluated
    and fulfilled trigger conditions), or `ok` (evaluated and did not fulfill trigger conditions)."""

    ok = 'ok'
    triggered = 'triggered'
    unknown = 'unknown'


@dataclass
class CancelExecutionRequest:
    """Cancel statement execution"""

    statement_id: str


@dataclass
class Channel:
    dbsql_version: str
    name: 'ChannelName'

    def as_dict(self) -> dict:
        body = {}
        if self.dbsql_version: body['dbsql_version'] = self.dbsql_version
        if self.name: body['name'] = self.name.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Channel':
        return cls(dbsql_version=d.get('dbsql_version', None),
                   name=ChannelName(d['name']) if 'name' in d else None)


@dataclass
class ChannelInfo:
    """Channel information for the SQL warehouse at the time of query execution"""

    dbsql_version: str
    name: 'ChannelName'

    def as_dict(self) -> dict:
        body = {}
        if self.dbsql_version: body['dbsql_version'] = self.dbsql_version
        if self.name: body['name'] = self.name.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ChannelInfo':
        return cls(dbsql_version=d.get('dbsql_version', None),
                   name=ChannelName(d['name']) if 'name' in d else None)


class ChannelName(Enum):
    """Name of the channel"""

    CHANNEL_NAME_CURRENT = 'CHANNEL_NAME_CURRENT'
    CHANNEL_NAME_CUSTOM = 'CHANNEL_NAME_CUSTOM'
    CHANNEL_NAME_PREVIEW = 'CHANNEL_NAME_PREVIEW'
    CHANNEL_NAME_PREVIOUS = 'CHANNEL_NAME_PREVIOUS'
    CHANNEL_NAME_UNSPECIFIED = 'CHANNEL_NAME_UNSPECIFIED'


@dataclass
class ChunkInfo:
    """Describes metadata for a particular chunk, within a result set; this structure is used both
    within a manifest, and when fetching individual chunk data or links."""

    byte_count: int
    chunk_index: int
    next_chunk_index: int
    next_chunk_internal_link: str
    row_count: int
    row_offset: int

    def as_dict(self) -> dict:
        body = {}
        if self.byte_count: body['byte_count'] = self.byte_count
        if self.chunk_index: body['chunk_index'] = self.chunk_index
        if self.next_chunk_index: body['next_chunk_index'] = self.next_chunk_index
        if self.next_chunk_internal_link: body['next_chunk_internal_link'] = self.next_chunk_internal_link
        if self.row_count: body['row_count'] = self.row_count
        if self.row_offset: body['row_offset'] = self.row_offset
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ChunkInfo':
        return cls(byte_count=d.get('byte_count', None),
                   chunk_index=d.get('chunk_index', None),
                   next_chunk_index=d.get('next_chunk_index', None),
                   next_chunk_internal_link=d.get('next_chunk_internal_link', None),
                   row_count=d.get('row_count', None),
                   row_offset=d.get('row_offset', None))


@dataclass
class ColumnInfo:
    name: str
    position: int
    type_interval_type: str
    type_name: 'ColumnInfoTypeName'
    type_precision: int
    type_scale: int
    type_text: str

    def as_dict(self) -> dict:
        body = {}
        if self.name: body['name'] = self.name
        if self.position: body['position'] = self.position
        if self.type_interval_type: body['type_interval_type'] = self.type_interval_type
        if self.type_name: body['type_name'] = self.type_name.value
        if self.type_precision: body['type_precision'] = self.type_precision
        if self.type_scale: body['type_scale'] = self.type_scale
        if self.type_text: body['type_text'] = self.type_text
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ColumnInfo':
        return cls(name=d.get('name', None),
                   position=d.get('position', None),
                   type_interval_type=d.get('type_interval_type', None),
                   type_name=ColumnInfoTypeName(d['type_name']) if 'type_name' in d else None,
                   type_precision=d.get('type_precision', None),
                   type_scale=d.get('type_scale', None),
                   type_text=d.get('type_text', None))


class ColumnInfoTypeName(Enum):
    """Name of type (INT, STRUCT, MAP, and so on)"""

    ARRAY = 'ARRAY'
    BINARY = 'BINARY'
    BOOLEAN = 'BOOLEAN'
    BYTE = 'BYTE'
    CHAR = 'CHAR'
    DATE = 'DATE'
    DECIMAL = 'DECIMAL'
    DOUBLE = 'DOUBLE'
    FLOAT = 'FLOAT'
    INT = 'INT'
    INTERVAL = 'INTERVAL'
    LONG = 'LONG'
    MAP = 'MAP'
    NULL = 'NULL'
    SHORT = 'SHORT'
    STRING = 'STRING'
    STRUCT = 'STRUCT'
    TIMESTAMP = 'TIMESTAMP'
    USER_DEFINED_TYPE = 'USER_DEFINED_TYPE'


@dataclass
class CreateAlert:
    name: str
    options: 'AlertOptions'
    parent: str
    query_id: str
    rearm: int

    def as_dict(self) -> dict:
        body = {}
        if self.name: body['name'] = self.name
        if self.options: body['options'] = self.options.as_dict()
        if self.parent: body['parent'] = self.parent
        if self.query_id: body['query_id'] = self.query_id
        if self.rearm: body['rearm'] = self.rearm
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateAlert':
        return cls(name=d.get('name', None),
                   options=AlertOptions.from_dict(d['options']) if 'options' in d else None,
                   parent=d.get('parent', None),
                   query_id=d.get('query_id', None),
                   rearm=d.get('rearm', None))


@dataclass
class CreateDashboardRequest:
    """Create a dashboard object"""

    dashboard_filters_enabled: bool
    is_draft: bool
    is_trashed: bool
    name: str
    parent: str
    tags: 'List[str]'
    widgets: 'List[Widget]'

    def as_dict(self) -> dict:
        body = {}
        if self.dashboard_filters_enabled: body['dashboard_filters_enabled'] = self.dashboard_filters_enabled
        if self.is_draft: body['is_draft'] = self.is_draft
        if self.is_trashed: body['is_trashed'] = self.is_trashed
        if self.name: body['name'] = self.name
        if self.parent: body['parent'] = self.parent
        if self.tags: body['tags'] = [v for v in self.tags]
        if self.widgets: body['widgets'] = [v.as_dict() for v in self.widgets]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateDashboardRequest':
        return cls(dashboard_filters_enabled=d.get('dashboard_filters_enabled', None),
                   is_draft=d.get('is_draft', None),
                   is_trashed=d.get('is_trashed', None),
                   name=d.get('name', None),
                   parent=d.get('parent', None),
                   tags=d.get('tags', None),
                   widgets=[Widget.from_dict(v)
                            for v in d['widgets']] if 'widgets' in d and d['widgets'] is not None else None)


@dataclass
class CreateRefreshSchedule:
    alert_id: str
    cron: str
    data_source_id: str

    def as_dict(self) -> dict:
        body = {}
        if self.alert_id: body['alert_id'] = self.alert_id
        if self.cron: body['cron'] = self.cron
        if self.data_source_id: body['data_source_id'] = self.data_source_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateRefreshSchedule':
        return cls(alert_id=d.get('alert_id', None),
                   cron=d.get('cron', None),
                   data_source_id=d.get('data_source_id', None))


@dataclass
class CreateSubscription:
    alert_id: str
    destination_id: str
    user_id: int

    def as_dict(self) -> dict:
        body = {}
        if self.alert_id: body['alert_id'] = self.alert_id
        if self.destination_id: body['destination_id'] = self.destination_id
        if self.user_id: body['user_id'] = self.user_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateSubscription':
        return cls(alert_id=d.get('alert_id', None),
                   destination_id=d.get('destination_id', None),
                   user_id=d.get('user_id', None))


@dataclass
class CreateWarehouseRequest:
    auto_stop_mins: int
    channel: 'Channel'
    cluster_size: str
    creator_name: str
    enable_photon: bool
    enable_serverless_compute: bool
    instance_profile_arn: str
    max_num_clusters: int
    min_num_clusters: int
    name: str
    spot_instance_policy: 'SpotInstancePolicy'
    tags: 'EndpointTags'
    warehouse_type: 'WarehouseType'

    def as_dict(self) -> dict:
        body = {}
        if self.auto_stop_mins: body['auto_stop_mins'] = self.auto_stop_mins
        if self.channel: body['channel'] = self.channel.as_dict()
        if self.cluster_size: body['cluster_size'] = self.cluster_size
        if self.creator_name: body['creator_name'] = self.creator_name
        if self.enable_photon: body['enable_photon'] = self.enable_photon
        if self.enable_serverless_compute: body['enable_serverless_compute'] = self.enable_serverless_compute
        if self.instance_profile_arn: body['instance_profile_arn'] = self.instance_profile_arn
        if self.max_num_clusters: body['max_num_clusters'] = self.max_num_clusters
        if self.min_num_clusters: body['min_num_clusters'] = self.min_num_clusters
        if self.name: body['name'] = self.name
        if self.spot_instance_policy: body['spot_instance_policy'] = self.spot_instance_policy.value
        if self.tags: body['tags'] = self.tags.as_dict()
        if self.warehouse_type: body['warehouse_type'] = self.warehouse_type.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateWarehouseRequest':
        return cls(auto_stop_mins=d.get('auto_stop_mins', None),
                   channel=Channel.from_dict(d['channel']) if 'channel' in d else None,
                   cluster_size=d.get('cluster_size', None),
                   creator_name=d.get('creator_name', None),
                   enable_photon=d.get('enable_photon', None),
                   enable_serverless_compute=d.get('enable_serverless_compute', None),
                   instance_profile_arn=d.get('instance_profile_arn', None),
                   max_num_clusters=d.get('max_num_clusters', None),
                   min_num_clusters=d.get('min_num_clusters', None),
                   name=d.get('name', None),
                   spot_instance_policy=SpotInstancePolicy(d['spot_instance_policy'])
                   if 'spot_instance_policy' in d else None,
                   tags=EndpointTags.from_dict(d['tags']) if 'tags' in d else None,
                   warehouse_type=WarehouseType(d['warehouse_type']) if 'warehouse_type' in d else None)


@dataclass
class CreateWarehouseResponse:
    id: str

    def as_dict(self) -> dict:
        body = {}
        if self.id: body['id'] = self.id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateWarehouseResponse':
        return cls(id=d.get('id', None))


@dataclass
class Dashboard:
    """A JSON representing a dashboard containing widgets of visualizations and text boxes."""

    can_edit: bool
    created_at: str
    dashboard_filters_enabled: bool
    id: str
    is_archived: bool
    is_draft: bool
    is_favorite: bool
    name: str
    options: 'DashboardOptions'
    parent: str
    permission_tier: 'PermissionLevel'
    slug: str
    tags: 'List[str]'
    updated_at: str
    user: 'User'
    user_id: int
    widgets: 'List[Widget]'

    def as_dict(self) -> dict:
        body = {}
        if self.can_edit: body['can_edit'] = self.can_edit
        if self.created_at: body['created_at'] = self.created_at
        if self.dashboard_filters_enabled: body['dashboard_filters_enabled'] = self.dashboard_filters_enabled
        if self.id: body['id'] = self.id
        if self.is_archived: body['is_archived'] = self.is_archived
        if self.is_draft: body['is_draft'] = self.is_draft
        if self.is_favorite: body['is_favorite'] = self.is_favorite
        if self.name: body['name'] = self.name
        if self.options: body['options'] = self.options.as_dict()
        if self.parent: body['parent'] = self.parent
        if self.permission_tier: body['permission_tier'] = self.permission_tier.value
        if self.slug: body['slug'] = self.slug
        if self.tags: body['tags'] = [v for v in self.tags]
        if self.updated_at: body['updated_at'] = self.updated_at
        if self.user: body['user'] = self.user.as_dict()
        if self.user_id: body['user_id'] = self.user_id
        if self.widgets: body['widgets'] = [v.as_dict() for v in self.widgets]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Dashboard':
        return cls(can_edit=d.get('can_edit', None),
                   created_at=d.get('created_at', None),
                   dashboard_filters_enabled=d.get('dashboard_filters_enabled', None),
                   id=d.get('id', None),
                   is_archived=d.get('is_archived', None),
                   is_draft=d.get('is_draft', None),
                   is_favorite=d.get('is_favorite', None),
                   name=d.get('name', None),
                   options=DashboardOptions.from_dict(d['options']) if 'options' in d else None,
                   parent=d.get('parent', None),
                   permission_tier=PermissionLevel(d['permission_tier']) if 'permission_tier' in d else None,
                   slug=d.get('slug', None),
                   tags=d.get('tags', None),
                   updated_at=d.get('updated_at', None),
                   user=User.from_dict(d['user']) if 'user' in d else None,
                   user_id=d.get('user_id', None),
                   widgets=[Widget.from_dict(v)
                            for v in d['widgets']] if 'widgets' in d and d['widgets'] is not None else None)


@dataclass
class DashboardOptions:
    moved_to_trash_at: str

    def as_dict(self) -> dict:
        body = {}
        if self.moved_to_trash_at: body['moved_to_trash_at'] = self.moved_to_trash_at
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'DashboardOptions':
        return cls(moved_to_trash_at=d.get('moved_to_trash_at', None))


@dataclass
class DataSource:
    """A JSON object representing a DBSQL data source / SQL warehouse."""

    id: str
    name: str
    pause_reason: str
    paused: int
    supports_auto_limit: bool
    syntax: str
    type: str
    view_only: bool
    warehouse_id: str

    def as_dict(self) -> dict:
        body = {}
        if self.id: body['id'] = self.id
        if self.name: body['name'] = self.name
        if self.pause_reason: body['pause_reason'] = self.pause_reason
        if self.paused: body['paused'] = self.paused
        if self.supports_auto_limit: body['supports_auto_limit'] = self.supports_auto_limit
        if self.syntax: body['syntax'] = self.syntax
        if self.type: body['type'] = self.type
        if self.view_only: body['view_only'] = self.view_only
        if self.warehouse_id: body['warehouse_id'] = self.warehouse_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'DataSource':
        return cls(id=d.get('id', None),
                   name=d.get('name', None),
                   pause_reason=d.get('pause_reason', None),
                   paused=d.get('paused', None),
                   supports_auto_limit=d.get('supports_auto_limit', None),
                   syntax=d.get('syntax', None),
                   type=d.get('type', None),
                   view_only=d.get('view_only', None),
                   warehouse_id=d.get('warehouse_id', None))


@dataclass
class DeleteAlertRequest:
    """Delete an alert"""

    alert_id: str


@dataclass
class DeleteDashboardRequest:
    """Remove a dashboard"""

    dashboard_id: str


@dataclass
class DeleteQueryRequest:
    """Delete a query"""

    query_id: str


@dataclass
class DeleteScheduleRequest:
    """[DEPRECATED] Delete a refresh schedule"""

    alert_id: str
    schedule_id: str


@dataclass
class DeleteWarehouseRequest:
    """Delete a warehouse"""

    id: str


@dataclass
class Destination:
    """Alert destination subscribed to the alert, if it exists. Alert destinations can be configured by
    admins through the UI. See [here].
    
    [here]: https://docs.databricks.com/sql/admin/alert-destinations.html"""

    id: str
    name: str
    type: 'DestinationType'

    def as_dict(self) -> dict:
        body = {}
        if self.id: body['id'] = self.id
        if self.name: body['name'] = self.name
        if self.type: body['type'] = self.type.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Destination':
        return cls(id=d.get('id', None),
                   name=d.get('name', None),
                   type=DestinationType(d['type']) if 'type' in d else None)


class DestinationType(Enum):
    """Type of the alert destination."""

    email = 'email'
    hangouts_chat = 'hangouts_chat'
    mattermost = 'mattermost'
    microsoft_teams = 'microsoft_teams'
    pagerduty = 'pagerduty'
    slack = 'slack'
    webhook = 'webhook'


class Disposition(Enum):
    """The fetch disposition provides for two modes of fetching results: INLINE, and EXTERNAL_LINKS.
    
    Statements executed with INLINE disposition will return result data inline, in JSON_ARRAY
    format, in a series of chunks. INLINE disposition result sets are constrained to 4 MiB
    (megabytes) of total data, and will typically be split into chunks of <= 4 MiB per chunk. If a
    given statement produces a result set with a size larger than 16 MiB, that statement execution
    is aborted, and no result set will be available.
    
    **NOTE** Byte limits are computed based upon internal representations of the result set data,
    and may not match the sizes visible in JSON responses.
    
    Statements executed with EXTERNAL_LINKS disposition will return result data as external links:
    URLs that point to cloud storage within the workspace's configured DBFS. Using EXTERNAL_LINKS
    disposition allows statements to generate arbitrarily sized result sets for fetching. The
    resulting links have two important properties:
    
    1. They point to resources _external_ to the Databricks compute; therefore any associated
    authentication information (typically a PAT token, OAuth token, or similar) _must be removed_
    when fetching from these links.
    
    2. These are presigned URLs with a specific expiration, indicated in the response. The behavior
    when attempting to use an expired link is cloud specific."""

    EXTERNAL_LINKS = 'EXTERNAL_LINKS'
    INLINE = 'INLINE'


@dataclass
class EditAlert:
    alert_id: str
    name: str
    options: 'AlertOptions'
    query_id: str
    rearm: int

    def as_dict(self) -> dict:
        body = {}
        if self.alert_id: body['alert_id'] = self.alert_id
        if self.name: body['name'] = self.name
        if self.options: body['options'] = self.options.as_dict()
        if self.query_id: body['query_id'] = self.query_id
        if self.rearm: body['rearm'] = self.rearm
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'EditAlert':
        return cls(alert_id=d.get('alert_id', None),
                   name=d.get('name', None),
                   options=AlertOptions.from_dict(d['options']) if 'options' in d else None,
                   query_id=d.get('query_id', None),
                   rearm=d.get('rearm', None))


@dataclass
class EditWarehouseRequest:
    auto_stop_mins: int
    channel: 'Channel'
    cluster_size: str
    creator_name: str
    enable_databricks_compute: bool
    enable_photon: bool
    enable_serverless_compute: bool
    id: str
    instance_profile_arn: str
    max_num_clusters: int
    min_num_clusters: int
    name: str
    spot_instance_policy: 'SpotInstancePolicy'
    tags: 'EndpointTags'
    warehouse_type: 'WarehouseType'

    def as_dict(self) -> dict:
        body = {}
        if self.auto_stop_mins: body['auto_stop_mins'] = self.auto_stop_mins
        if self.channel: body['channel'] = self.channel.as_dict()
        if self.cluster_size: body['cluster_size'] = self.cluster_size
        if self.creator_name: body['creator_name'] = self.creator_name
        if self.enable_databricks_compute: body['enable_databricks_compute'] = self.enable_databricks_compute
        if self.enable_photon: body['enable_photon'] = self.enable_photon
        if self.enable_serverless_compute: body['enable_serverless_compute'] = self.enable_serverless_compute
        if self.id: body['id'] = self.id
        if self.instance_profile_arn: body['instance_profile_arn'] = self.instance_profile_arn
        if self.max_num_clusters: body['max_num_clusters'] = self.max_num_clusters
        if self.min_num_clusters: body['min_num_clusters'] = self.min_num_clusters
        if self.name: body['name'] = self.name
        if self.spot_instance_policy: body['spot_instance_policy'] = self.spot_instance_policy.value
        if self.tags: body['tags'] = self.tags.as_dict()
        if self.warehouse_type: body['warehouse_type'] = self.warehouse_type.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'EditWarehouseRequest':
        return cls(auto_stop_mins=d.get('auto_stop_mins', None),
                   channel=Channel.from_dict(d['channel']) if 'channel' in d else None,
                   cluster_size=d.get('cluster_size', None),
                   creator_name=d.get('creator_name', None),
                   enable_databricks_compute=d.get('enable_databricks_compute', None),
                   enable_photon=d.get('enable_photon', None),
                   enable_serverless_compute=d.get('enable_serverless_compute', None),
                   id=d.get('id', None),
                   instance_profile_arn=d.get('instance_profile_arn', None),
                   max_num_clusters=d.get('max_num_clusters', None),
                   min_num_clusters=d.get('min_num_clusters', None),
                   name=d.get('name', None),
                   spot_instance_policy=SpotInstancePolicy(d['spot_instance_policy'])
                   if 'spot_instance_policy' in d else None,
                   tags=EndpointTags.from_dict(d['tags']) if 'tags' in d else None,
                   warehouse_type=WarehouseType(d['warehouse_type']) if 'warehouse_type' in d else None)


@dataclass
class EndpointConfPair:
    key: str
    value: str

    def as_dict(self) -> dict:
        body = {}
        if self.key: body['key'] = self.key
        if self.value: body['value'] = self.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'EndpointConfPair':
        return cls(key=d.get('key', None), value=d.get('value', None))


@dataclass
class EndpointHealth:
    details: str
    failure_reason: 'TerminationReason'
    message: str
    status: 'Status'
    summary: str

    def as_dict(self) -> dict:
        body = {}
        if self.details: body['details'] = self.details
        if self.failure_reason: body['failure_reason'] = self.failure_reason.as_dict()
        if self.message: body['message'] = self.message
        if self.status: body['status'] = self.status.value
        if self.summary: body['summary'] = self.summary
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'EndpointHealth':
        return cls(details=d.get('details', None),
                   failure_reason=TerminationReason.from_dict(d['failure_reason'])
                   if 'failure_reason' in d else None,
                   message=d.get('message', None),
                   status=Status(d['status']) if 'status' in d else None,
                   summary=d.get('summary', None))


@dataclass
class EndpointInfo:
    auto_stop_mins: int
    channel: 'Channel'
    cluster_size: str
    creator_name: str
    enable_databricks_compute: bool
    enable_photon: bool
    enable_serverless_compute: bool
    health: 'EndpointHealth'
    id: str
    instance_profile_arn: str
    jdbc_url: str
    max_num_clusters: int
    min_num_clusters: int
    name: str
    num_active_sessions: int
    num_clusters: int
    odbc_params: 'OdbcParams'
    spot_instance_policy: 'SpotInstancePolicy'
    state: 'State'
    tags: 'EndpointTags'
    warehouse_type: 'WarehouseType'

    def as_dict(self) -> dict:
        body = {}
        if self.auto_stop_mins: body['auto_stop_mins'] = self.auto_stop_mins
        if self.channel: body['channel'] = self.channel.as_dict()
        if self.cluster_size: body['cluster_size'] = self.cluster_size
        if self.creator_name: body['creator_name'] = self.creator_name
        if self.enable_databricks_compute: body['enable_databricks_compute'] = self.enable_databricks_compute
        if self.enable_photon: body['enable_photon'] = self.enable_photon
        if self.enable_serverless_compute: body['enable_serverless_compute'] = self.enable_serverless_compute
        if self.health: body['health'] = self.health.as_dict()
        if self.id: body['id'] = self.id
        if self.instance_profile_arn: body['instance_profile_arn'] = self.instance_profile_arn
        if self.jdbc_url: body['jdbc_url'] = self.jdbc_url
        if self.max_num_clusters: body['max_num_clusters'] = self.max_num_clusters
        if self.min_num_clusters: body['min_num_clusters'] = self.min_num_clusters
        if self.name: body['name'] = self.name
        if self.num_active_sessions: body['num_active_sessions'] = self.num_active_sessions
        if self.num_clusters: body['num_clusters'] = self.num_clusters
        if self.odbc_params: body['odbc_params'] = self.odbc_params.as_dict()
        if self.spot_instance_policy: body['spot_instance_policy'] = self.spot_instance_policy.value
        if self.state: body['state'] = self.state.value
        if self.tags: body['tags'] = self.tags.as_dict()
        if self.warehouse_type: body['warehouse_type'] = self.warehouse_type.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'EndpointInfo':
        return cls(auto_stop_mins=d.get('auto_stop_mins', None),
                   channel=Channel.from_dict(d['channel']) if 'channel' in d else None,
                   cluster_size=d.get('cluster_size', None),
                   creator_name=d.get('creator_name', None),
                   enable_databricks_compute=d.get('enable_databricks_compute', None),
                   enable_photon=d.get('enable_photon', None),
                   enable_serverless_compute=d.get('enable_serverless_compute', None),
                   health=EndpointHealth.from_dict(d['health']) if 'health' in d else None,
                   id=d.get('id', None),
                   instance_profile_arn=d.get('instance_profile_arn', None),
                   jdbc_url=d.get('jdbc_url', None),
                   max_num_clusters=d.get('max_num_clusters', None),
                   min_num_clusters=d.get('min_num_clusters', None),
                   name=d.get('name', None),
                   num_active_sessions=d.get('num_active_sessions', None),
                   num_clusters=d.get('num_clusters', None),
                   odbc_params=OdbcParams.from_dict(d['odbc_params']) if 'odbc_params' in d else None,
                   spot_instance_policy=SpotInstancePolicy(d['spot_instance_policy'])
                   if 'spot_instance_policy' in d else None,
                   state=State(d['state']) if 'state' in d else None,
                   tags=EndpointTags.from_dict(d['tags']) if 'tags' in d else None,
                   warehouse_type=WarehouseType(d['warehouse_type']) if 'warehouse_type' in d else None)


@dataclass
class EndpointTagPair:
    key: str
    value: str

    def as_dict(self) -> dict:
        body = {}
        if self.key: body['key'] = self.key
        if self.value: body['value'] = self.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'EndpointTagPair':
        return cls(key=d.get('key', None), value=d.get('value', None))


@dataclass
class EndpointTags:
    custom_tags: 'List[EndpointTagPair]'

    def as_dict(self) -> dict:
        body = {}
        if self.custom_tags: body['custom_tags'] = [v.as_dict() for v in self.custom_tags]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'EndpointTags':
        return cls(custom_tags=[EndpointTagPair.from_dict(v) for v in d['custom_tags']]
                   if 'custom_tags' in d and d['custom_tags'] is not None else None)


@dataclass
class ExecuteStatementRequest:
    catalog: str
    disposition: 'Disposition'
    format: 'Format'
    on_wait_timeout: 'TimeoutAction'
    schema: str
    statement: str
    wait_timeout: str
    warehouse_id: str

    def as_dict(self) -> dict:
        body = {}
        if self.catalog: body['catalog'] = self.catalog
        if self.disposition: body['disposition'] = self.disposition.value
        if self.format: body['format'] = self.format.value
        if self.on_wait_timeout: body['on_wait_timeout'] = self.on_wait_timeout.value
        if self.schema: body['schema'] = self.schema
        if self.statement: body['statement'] = self.statement
        if self.wait_timeout: body['wait_timeout'] = self.wait_timeout
        if self.warehouse_id: body['warehouse_id'] = self.warehouse_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ExecuteStatementRequest':
        return cls(catalog=d.get('catalog', None),
                   disposition=Disposition(d['disposition']) if 'disposition' in d else None,
                   format=Format(d['format']) if 'format' in d else None,
                   on_wait_timeout=TimeoutAction(d['on_wait_timeout']) if 'on_wait_timeout' in d else None,
                   schema=d.get('schema', None),
                   statement=d.get('statement', None),
                   wait_timeout=d.get('wait_timeout', None),
                   warehouse_id=d.get('warehouse_id', None))


@dataclass
class ExecuteStatementResponse:
    manifest: 'ResultManifest'
    result: 'ResultData'
    statement_id: str
    status: 'StatementStatus'

    def as_dict(self) -> dict:
        body = {}
        if self.manifest: body['manifest'] = self.manifest.as_dict()
        if self.result: body['result'] = self.result.as_dict()
        if self.statement_id: body['statement_id'] = self.statement_id
        if self.status: body['status'] = self.status.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ExecuteStatementResponse':
        return cls(manifest=ResultManifest.from_dict(d['manifest']) if 'manifest' in d else None,
                   result=ResultData.from_dict(d['result']) if 'result' in d else None,
                   statement_id=d.get('statement_id', None),
                   status=StatementStatus.from_dict(d['status']) if 'status' in d else None)


@dataclass
class ExternalLink:
    byte_count: int
    chunk_index: int
    expiration: str
    external_link: str
    next_chunk_index: int
    next_chunk_internal_link: str
    row_count: int
    row_offset: int

    def as_dict(self) -> dict:
        body = {}
        if self.byte_count: body['byte_count'] = self.byte_count
        if self.chunk_index: body['chunk_index'] = self.chunk_index
        if self.expiration: body['expiration'] = self.expiration
        if self.external_link: body['external_link'] = self.external_link
        if self.next_chunk_index: body['next_chunk_index'] = self.next_chunk_index
        if self.next_chunk_internal_link: body['next_chunk_internal_link'] = self.next_chunk_internal_link
        if self.row_count: body['row_count'] = self.row_count
        if self.row_offset: body['row_offset'] = self.row_offset
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ExternalLink':
        return cls(byte_count=d.get('byte_count', None),
                   chunk_index=d.get('chunk_index', None),
                   expiration=d.get('expiration', None),
                   external_link=d.get('external_link', None),
                   next_chunk_index=d.get('next_chunk_index', None),
                   next_chunk_internal_link=d.get('next_chunk_internal_link', None),
                   row_count=d.get('row_count', None),
                   row_offset=d.get('row_offset', None))


class Format(Enum):
    """Statement execution supports two result formats: `JSON_ARRAY` (default), and `ARROW_STREAM`.
    
    **NOTE**
    
    Currently `JSON_ARRAY` is only available for requests with `disposition=INLINE`, and
    `ARROW_STREAM` is only available for requests with `disposition=EXTERNAL_LINKS`.
    
    When specifying `format=JSON_ARRAY`, result data will be formatted as arrays of arrays of
    values, where each value is either the *string representation* of a value, or `null`. For
    example, the output of `SELECT concat('id-', id) AS strId, id AS intId FROM range(3)` would look
    like this:
    
    ``` [ [ "id-1", "1" ], [ "id-2", "2" ], [ "id-3", "3" ], ] ```
    
    INLINE JSON_ARRAY data can be found within `StatementResponse.result.chunk.data_array` or
    `ResultData.chunk.data_array`.
    
    When specifying `format=ARROW_STREAM`, results fetched through `ResultData.external_links` will
    be chunks of result data, formatted as Apache Arrow Stream. See
    [https://arrow.apache.org/docs/format/Columnar.html#ipc-streaming-format] for more details."""

    ARROW_STREAM = 'ARROW_STREAM'
    JSON_ARRAY = 'JSON_ARRAY'


@dataclass
class GetAlertRequest:
    """Get an alert"""

    alert_id: str


@dataclass
class GetDashboardRequest:
    """Retrieve a definition"""

    dashboard_id: str


@dataclass
class GetDbsqlPermissionRequest:
    """Get object ACL"""

    object_id: str
    object_type: 'ObjectTypePlural'


@dataclass
class GetQueryRequest:
    """Get a query definition."""

    query_id: str


@dataclass
class GetResponse:
    access_control_list: 'List[AccessControl]'
    object_id: 'ObjectType'
    object_type: str

    def as_dict(self) -> dict:
        body = {}
        if self.access_control_list:
            body['access_control_list'] = [v.as_dict() for v in self.access_control_list]
        if self.object_id: body['object_id'] = self.object_id.value
        if self.object_type: body['object_type'] = self.object_type
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetResponse':
        return cls(access_control_list=[AccessControl.from_dict(v) for v in d['access_control_list']]
                   if 'access_control_list' in d and d['access_control_list'] is not None else None,
                   object_id=ObjectType(d['object_id']) if 'object_id' in d else None,
                   object_type=d.get('object_type', None))


@dataclass
class GetStatementRequest:
    """Get status, manifest, and result first chunk"""

    statement_id: str


@dataclass
class GetStatementResponse:
    manifest: 'ResultManifest'
    result: 'ResultData'
    statement_id: str
    status: 'StatementStatus'

    def as_dict(self) -> dict:
        body = {}
        if self.manifest: body['manifest'] = self.manifest.as_dict()
        if self.result: body['result'] = self.result.as_dict()
        if self.statement_id: body['statement_id'] = self.statement_id
        if self.status: body['status'] = self.status.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetStatementResponse':
        return cls(manifest=ResultManifest.from_dict(d['manifest']) if 'manifest' in d else None,
                   result=ResultData.from_dict(d['result']) if 'result' in d else None,
                   statement_id=d.get('statement_id', None),
                   status=StatementStatus.from_dict(d['status']) if 'status' in d else None)


@dataclass
class GetStatementResultChunkNRequest:
    """Get result chunk by index"""

    chunk_index: int
    row_offset: int
    statement_id: str


@dataclass
class GetSubscriptionsRequest:
    """[DEPRECATED] Get an alert's subscriptions"""

    alert_id: str


@dataclass
class GetWarehouseRequest:
    """Get warehouse info"""

    id: str


@dataclass
class GetWarehouseResponse:
    auto_stop_mins: int
    channel: 'Channel'
    cluster_size: str
    creator_name: str
    enable_databricks_compute: bool
    enable_photon: bool
    enable_serverless_compute: bool
    health: 'EndpointHealth'
    id: str
    instance_profile_arn: str
    jdbc_url: str
    max_num_clusters: int
    min_num_clusters: int
    name: str
    num_active_sessions: int
    num_clusters: int
    odbc_params: 'OdbcParams'
    spot_instance_policy: 'SpotInstancePolicy'
    state: 'State'
    tags: 'EndpointTags'
    warehouse_type: 'WarehouseType'

    def as_dict(self) -> dict:
        body = {}
        if self.auto_stop_mins: body['auto_stop_mins'] = self.auto_stop_mins
        if self.channel: body['channel'] = self.channel.as_dict()
        if self.cluster_size: body['cluster_size'] = self.cluster_size
        if self.creator_name: body['creator_name'] = self.creator_name
        if self.enable_databricks_compute: body['enable_databricks_compute'] = self.enable_databricks_compute
        if self.enable_photon: body['enable_photon'] = self.enable_photon
        if self.enable_serverless_compute: body['enable_serverless_compute'] = self.enable_serverless_compute
        if self.health: body['health'] = self.health.as_dict()
        if self.id: body['id'] = self.id
        if self.instance_profile_arn: body['instance_profile_arn'] = self.instance_profile_arn
        if self.jdbc_url: body['jdbc_url'] = self.jdbc_url
        if self.max_num_clusters: body['max_num_clusters'] = self.max_num_clusters
        if self.min_num_clusters: body['min_num_clusters'] = self.min_num_clusters
        if self.name: body['name'] = self.name
        if self.num_active_sessions: body['num_active_sessions'] = self.num_active_sessions
        if self.num_clusters: body['num_clusters'] = self.num_clusters
        if self.odbc_params: body['odbc_params'] = self.odbc_params.as_dict()
        if self.spot_instance_policy: body['spot_instance_policy'] = self.spot_instance_policy.value
        if self.state: body['state'] = self.state.value
        if self.tags: body['tags'] = self.tags.as_dict()
        if self.warehouse_type: body['warehouse_type'] = self.warehouse_type.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetWarehouseResponse':
        return cls(auto_stop_mins=d.get('auto_stop_mins', None),
                   channel=Channel.from_dict(d['channel']) if 'channel' in d else None,
                   cluster_size=d.get('cluster_size', None),
                   creator_name=d.get('creator_name', None),
                   enable_databricks_compute=d.get('enable_databricks_compute', None),
                   enable_photon=d.get('enable_photon', None),
                   enable_serverless_compute=d.get('enable_serverless_compute', None),
                   health=EndpointHealth.from_dict(d['health']) if 'health' in d else None,
                   id=d.get('id', None),
                   instance_profile_arn=d.get('instance_profile_arn', None),
                   jdbc_url=d.get('jdbc_url', None),
                   max_num_clusters=d.get('max_num_clusters', None),
                   min_num_clusters=d.get('min_num_clusters', None),
                   name=d.get('name', None),
                   num_active_sessions=d.get('num_active_sessions', None),
                   num_clusters=d.get('num_clusters', None),
                   odbc_params=OdbcParams.from_dict(d['odbc_params']) if 'odbc_params' in d else None,
                   spot_instance_policy=SpotInstancePolicy(d['spot_instance_policy'])
                   if 'spot_instance_policy' in d else None,
                   state=State(d['state']) if 'state' in d else None,
                   tags=EndpointTags.from_dict(d['tags']) if 'tags' in d else None,
                   warehouse_type=WarehouseType(d['warehouse_type']) if 'warehouse_type' in d else None)


@dataclass
class GetWorkspaceWarehouseConfigResponse:
    channel: 'Channel'
    config_param: 'RepeatedEndpointConfPairs'
    data_access_config: 'List[EndpointConfPair]'
    enable_databricks_compute: bool
    enable_serverless_compute: bool
    enabled_warehouse_types: 'List[WarehouseTypePair]'
    global_param: 'RepeatedEndpointConfPairs'
    google_service_account: str
    instance_profile_arn: str
    security_policy: 'GetWorkspaceWarehouseConfigResponseSecurityPolicy'
    sql_configuration_parameters: 'RepeatedEndpointConfPairs'

    def as_dict(self) -> dict:
        body = {}
        if self.channel: body['channel'] = self.channel.as_dict()
        if self.config_param: body['config_param'] = self.config_param.as_dict()
        if self.data_access_config:
            body['data_access_config'] = [v.as_dict() for v in self.data_access_config]
        if self.enable_databricks_compute: body['enable_databricks_compute'] = self.enable_databricks_compute
        if self.enable_serverless_compute: body['enable_serverless_compute'] = self.enable_serverless_compute
        if self.enabled_warehouse_types:
            body['enabled_warehouse_types'] = [v.as_dict() for v in self.enabled_warehouse_types]
        if self.global_param: body['global_param'] = self.global_param.as_dict()
        if self.google_service_account: body['google_service_account'] = self.google_service_account
        if self.instance_profile_arn: body['instance_profile_arn'] = self.instance_profile_arn
        if self.security_policy: body['security_policy'] = self.security_policy.value
        if self.sql_configuration_parameters:
            body['sql_configuration_parameters'] = self.sql_configuration_parameters.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetWorkspaceWarehouseConfigResponse':
        return cls(
            channel=Channel.from_dict(d['channel']) if 'channel' in d else None,
            config_param=RepeatedEndpointConfPairs.from_dict(d['config_param'])
            if 'config_param' in d else None,
            data_access_config=[EndpointConfPair.from_dict(v) for v in d['data_access_config']]
            if 'data_access_config' in d and d['data_access_config'] is not None else None,
            enable_databricks_compute=d.get('enable_databricks_compute', None),
            enable_serverless_compute=d.get('enable_serverless_compute', None),
            enabled_warehouse_types=[WarehouseTypePair.from_dict(v) for v in d['enabled_warehouse_types']]
            if 'enabled_warehouse_types' in d and d['enabled_warehouse_types'] is not None else None,
            global_param=RepeatedEndpointConfPairs.from_dict(d['global_param'])
            if 'global_param' in d else None,
            google_service_account=d.get('google_service_account', None),
            instance_profile_arn=d.get('instance_profile_arn', None),
            security_policy=GetWorkspaceWarehouseConfigResponseSecurityPolicy(d['security_policy'])
            if 'security_policy' in d else None,
            sql_configuration_parameters=RepeatedEndpointConfPairs.from_dict(
                d['sql_configuration_parameters']) if 'sql_configuration_parameters' in d else None)


class GetWorkspaceWarehouseConfigResponseSecurityPolicy(Enum):
    """Security policy for endpoints"""

    DATA_ACCESS_CONTROL = 'DATA_ACCESS_CONTROL'
    NONE = 'NONE'
    PASSTHROUGH = 'PASSTHROUGH'


@dataclass
class ListDashboardsRequest:
    """Get dashboard objects"""

    order: 'ListOrder'
    page: int
    page_size: int
    q: str


class ListOrder(Enum):

    created_at = 'created_at'
    name = 'name'


@dataclass
class ListQueriesRequest:
    """Get a list of queries"""

    order: str
    page: int
    page_size: int
    q: str


@dataclass
class ListQueriesResponse:
    has_next_page: bool
    next_page_token: str
    res: 'List[QueryInfo]'

    def as_dict(self) -> dict:
        body = {}
        if self.has_next_page: body['has_next_page'] = self.has_next_page
        if self.next_page_token: body['next_page_token'] = self.next_page_token
        if self.res: body['res'] = [v.as_dict() for v in self.res]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListQueriesResponse':
        return cls(has_next_page=d.get('has_next_page', None),
                   next_page_token=d.get('next_page_token', None),
                   res=[QueryInfo.from_dict(v)
                        for v in d['res']] if 'res' in d and d['res'] is not None else None)


@dataclass
class ListQueryHistoryRequest:
    """List Queries"""

    filter_by: 'QueryFilter'
    include_metrics: bool
    max_results: int
    page_token: str


@dataclass
class ListResponse:
    count: int
    page: int
    page_size: int
    results: 'List[Dashboard]'

    def as_dict(self) -> dict:
        body = {}
        if self.count: body['count'] = self.count
        if self.page: body['page'] = self.page
        if self.page_size: body['page_size'] = self.page_size
        if self.results: body['results'] = [v.as_dict() for v in self.results]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListResponse':
        return cls(count=d.get('count', None),
                   page=d.get('page', None),
                   page_size=d.get('page_size', None),
                   results=[Dashboard.from_dict(v)
                            for v in d['results']] if 'results' in d and d['results'] is not None else None)


@dataclass
class ListSchedulesRequest:
    """[DEPRECATED] Get refresh schedules"""

    alert_id: str


@dataclass
class ListWarehousesRequest:
    """List warehouses"""

    run_as_user_id: int


@dataclass
class ListWarehousesResponse:
    warehouses: 'List[EndpointInfo]'

    def as_dict(self) -> dict:
        body = {}
        if self.warehouses: body['warehouses'] = [v.as_dict() for v in self.warehouses]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListWarehousesResponse':
        return cls(warehouses=[EndpointInfo.from_dict(v) for v in d['warehouses']]
                   if 'warehouses' in d and d['warehouses'] is not None else None)


class ObjectType(Enum):
    """A singular noun object type."""

    alert = 'alert'
    dashboard = 'dashboard'
    data_source = 'data_source'
    query = 'query'


class ObjectTypePlural(Enum):
    """Always a plural of the object type."""

    alerts = 'alerts'
    dashboards = 'dashboards'
    data_sources = 'data_sources'
    queries = 'queries'


@dataclass
class OdbcParams:
    hostname: str
    path: str
    port: int
    protocol: str

    def as_dict(self) -> dict:
        body = {}
        if self.hostname: body['hostname'] = self.hostname
        if self.path: body['path'] = self.path
        if self.port: body['port'] = self.port
        if self.protocol: body['protocol'] = self.protocol
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'OdbcParams':
        return cls(hostname=d.get('hostname', None),
                   path=d.get('path', None),
                   port=d.get('port', None),
                   protocol=d.get('protocol', None))


class OwnableObjectType(Enum):
    """The singular form of the type of object which can be owned."""

    alert = 'alert'
    dashboard = 'dashboard'
    query = 'query'


@dataclass
class Parameter:
    name: str
    title: str
    type: 'ParameterType'
    value: Any

    def as_dict(self) -> dict:
        body = {}
        if self.name: body['name'] = self.name
        if self.title: body['title'] = self.title
        if self.type: body['type'] = self.type.value
        if self.value: body['value'] = self.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Parameter':
        return cls(name=d.get('name', None),
                   title=d.get('title', None),
                   type=ParameterType(d['type']) if 'type' in d else None,
                   value=d.get('value', None))


class ParameterType(Enum):
    """Parameters can have several different types."""

    datetime = 'datetime'
    number = 'number'
    text = 'text'


class PermissionLevel(Enum):
    """This describes an enum"""

    CAN_MANAGE = 'CAN_MANAGE'
    CAN_RUN = 'CAN_RUN'
    CAN_VIEW = 'CAN_VIEW'


class PlansState(Enum):
    """Whether plans exist for the execution, or the reason why they are missing"""

    EMPTY = 'EMPTY'
    EXISTS = 'EXISTS'
    IGNORED_LARGE_PLANS_SIZE = 'IGNORED_LARGE_PLANS_SIZE'
    IGNORED_SMALL_DURATION = 'IGNORED_SMALL_DURATION'
    IGNORED_SPARK_PLAN_TYPE = 'IGNORED_SPARK_PLAN_TYPE'
    UNKNOWN = 'UNKNOWN'


@dataclass
class Query:
    can_edit: bool
    created_at: str
    data_source_id: str
    description: str
    id: str
    is_archived: bool
    is_draft: bool
    is_favorite: bool
    is_safe: bool
    last_modified_by: 'User'
    last_modified_by_id: int
    latest_query_data_id: str
    name: str
    options: 'QueryOptions'
    parent: str
    permission_tier: 'PermissionLevel'
    query: str
    query_hash: str
    schedule: 'QueryInterval'
    tags: 'List[str]'
    updated_at: str
    user: 'User'
    user_id: int
    visualizations: 'List[Visualization]'

    def as_dict(self) -> dict:
        body = {}
        if self.can_edit: body['can_edit'] = self.can_edit
        if self.created_at: body['created_at'] = self.created_at
        if self.data_source_id: body['data_source_id'] = self.data_source_id
        if self.description: body['description'] = self.description
        if self.id: body['id'] = self.id
        if self.is_archived: body['is_archived'] = self.is_archived
        if self.is_draft: body['is_draft'] = self.is_draft
        if self.is_favorite: body['is_favorite'] = self.is_favorite
        if self.is_safe: body['is_safe'] = self.is_safe
        if self.last_modified_by: body['last_modified_by'] = self.last_modified_by.as_dict()
        if self.last_modified_by_id: body['last_modified_by_id'] = self.last_modified_by_id
        if self.latest_query_data_id: body['latest_query_data_id'] = self.latest_query_data_id
        if self.name: body['name'] = self.name
        if self.options: body['options'] = self.options.as_dict()
        if self.parent: body['parent'] = self.parent
        if self.permission_tier: body['permission_tier'] = self.permission_tier.value
        if self.query: body['query'] = self.query
        if self.query_hash: body['query_hash'] = self.query_hash
        if self.schedule: body['schedule'] = self.schedule.as_dict()
        if self.tags: body['tags'] = [v for v in self.tags]
        if self.updated_at: body['updated_at'] = self.updated_at
        if self.user: body['user'] = self.user.as_dict()
        if self.user_id: body['user_id'] = self.user_id
        if self.visualizations: body['visualizations'] = [v.as_dict() for v in self.visualizations]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Query':
        return cls(
            can_edit=d.get('can_edit', None),
            created_at=d.get('created_at', None),
            data_source_id=d.get('data_source_id', None),
            description=d.get('description', None),
            id=d.get('id', None),
            is_archived=d.get('is_archived', None),
            is_draft=d.get('is_draft', None),
            is_favorite=d.get('is_favorite', None),
            is_safe=d.get('is_safe', None),
            last_modified_by=User.from_dict(d['last_modified_by']) if 'last_modified_by' in d else None,
            last_modified_by_id=d.get('last_modified_by_id', None),
            latest_query_data_id=d.get('latest_query_data_id', None),
            name=d.get('name', None),
            options=QueryOptions.from_dict(d['options']) if 'options' in d else None,
            parent=d.get('parent', None),
            permission_tier=PermissionLevel(d['permission_tier']) if 'permission_tier' in d else None,
            query=d.get('query', None),
            query_hash=d.get('query_hash', None),
            schedule=QueryInterval.from_dict(d['schedule']) if 'schedule' in d else None,
            tags=d.get('tags', None),
            updated_at=d.get('updated_at', None),
            user=User.from_dict(d['user']) if 'user' in d else None,
            user_id=d.get('user_id', None),
            visualizations=[Visualization.from_dict(v) for v in d['visualizations']]
            if 'visualizations' in d and d['visualizations'] is not None else None)


@dataclass
class QueryEditContent:
    data_source_id: str
    description: str
    name: str
    options: Any
    query: str
    query_id: str
    schedule: 'QueryInterval'

    def as_dict(self) -> dict:
        body = {}
        if self.data_source_id: body['data_source_id'] = self.data_source_id
        if self.description: body['description'] = self.description
        if self.name: body['name'] = self.name
        if self.options: body['options'] = self.options
        if self.query: body['query'] = self.query
        if self.query_id: body['query_id'] = self.query_id
        if self.schedule: body['schedule'] = self.schedule.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'QueryEditContent':
        return cls(data_source_id=d.get('data_source_id', None),
                   description=d.get('description', None),
                   name=d.get('name', None),
                   options=d.get('options', None),
                   query=d.get('query', None),
                   query_id=d.get('query_id', None),
                   schedule=QueryInterval.from_dict(d['schedule']) if 'schedule' in d else None)


@dataclass
class QueryFilter:
    """A filter to limit query history results. This field is optional."""

    query_start_time_range: 'TimeRange'
    statuses: 'List[QueryStatus]'
    user_ids: 'List[int]'
    warehouse_ids: 'List[str]'

    def as_dict(self) -> dict:
        body = {}
        if self.query_start_time_range: body['query_start_time_range'] = self.query_start_time_range.as_dict()
        if self.statuses: body['statuses'] = [v for v in self.statuses]
        if self.user_ids: body['user_ids'] = [v for v in self.user_ids]
        if self.warehouse_ids: body['warehouse_ids'] = [v for v in self.warehouse_ids]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'QueryFilter':
        return cls(query_start_time_range=TimeRange.from_dict(d['query_start_time_range'])
                   if 'query_start_time_range' in d else None,
                   statuses=d.get('statuses', None),
                   user_ids=d.get('user_ids', None),
                   warehouse_ids=d.get('warehouse_ids', None))


@dataclass
class QueryInfo:
    channel_used: 'ChannelInfo'
    duration: int
    endpoint_id: str
    error_message: str
    executed_as_user_id: int
    executed_as_user_name: str
    execution_end_time_ms: int
    is_final: bool
    lookup_key: str
    metrics: 'QueryMetrics'
    plans_state: 'PlansState'
    query_end_time_ms: int
    query_id: str
    query_start_time_ms: int
    query_text: str
    rows_produced: int
    spark_ui_url: str
    statement_type: 'QueryStatementType'
    status: 'QueryStatus'
    user_id: int
    user_name: str
    warehouse_id: str

    def as_dict(self) -> dict:
        body = {}
        if self.channel_used: body['channel_used'] = self.channel_used.as_dict()
        if self.duration: body['duration'] = self.duration
        if self.endpoint_id: body['endpoint_id'] = self.endpoint_id
        if self.error_message: body['error_message'] = self.error_message
        if self.executed_as_user_id: body['executed_as_user_id'] = self.executed_as_user_id
        if self.executed_as_user_name: body['executed_as_user_name'] = self.executed_as_user_name
        if self.execution_end_time_ms: body['execution_end_time_ms'] = self.execution_end_time_ms
        if self.is_final: body['is_final'] = self.is_final
        if self.lookup_key: body['lookup_key'] = self.lookup_key
        if self.metrics: body['metrics'] = self.metrics.as_dict()
        if self.plans_state: body['plans_state'] = self.plans_state.value
        if self.query_end_time_ms: body['query_end_time_ms'] = self.query_end_time_ms
        if self.query_id: body['query_id'] = self.query_id
        if self.query_start_time_ms: body['query_start_time_ms'] = self.query_start_time_ms
        if self.query_text: body['query_text'] = self.query_text
        if self.rows_produced: body['rows_produced'] = self.rows_produced
        if self.spark_ui_url: body['spark_ui_url'] = self.spark_ui_url
        if self.statement_type: body['statement_type'] = self.statement_type.value
        if self.status: body['status'] = self.status.value
        if self.user_id: body['user_id'] = self.user_id
        if self.user_name: body['user_name'] = self.user_name
        if self.warehouse_id: body['warehouse_id'] = self.warehouse_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'QueryInfo':
        return cls(channel_used=ChannelInfo.from_dict(d['channel_used']) if 'channel_used' in d else None,
                   duration=d.get('duration', None),
                   endpoint_id=d.get('endpoint_id', None),
                   error_message=d.get('error_message', None),
                   executed_as_user_id=d.get('executed_as_user_id', None),
                   executed_as_user_name=d.get('executed_as_user_name', None),
                   execution_end_time_ms=d.get('execution_end_time_ms', None),
                   is_final=d.get('is_final', None),
                   lookup_key=d.get('lookup_key', None),
                   metrics=QueryMetrics.from_dict(d['metrics']) if 'metrics' in d else None,
                   plans_state=PlansState(d['plans_state']) if 'plans_state' in d else None,
                   query_end_time_ms=d.get('query_end_time_ms', None),
                   query_id=d.get('query_id', None),
                   query_start_time_ms=d.get('query_start_time_ms', None),
                   query_text=d.get('query_text', None),
                   rows_produced=d.get('rows_produced', None),
                   spark_ui_url=d.get('spark_ui_url', None),
                   statement_type=QueryStatementType(d['statement_type']) if 'statement_type' in d else None,
                   status=QueryStatus(d['status']) if 'status' in d else None,
                   user_id=d.get('user_id', None),
                   user_name=d.get('user_name', None),
                   warehouse_id=d.get('warehouse_id', None))


@dataclass
class QueryInterval:
    day_of_week: str
    interval: int
    time: str
    until: str

    def as_dict(self) -> dict:
        body = {}
        if self.day_of_week: body['day_of_week'] = self.day_of_week
        if self.interval: body['interval'] = self.interval
        if self.time: body['time'] = self.time
        if self.until: body['until'] = self.until
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'QueryInterval':
        return cls(day_of_week=d.get('day_of_week', None),
                   interval=d.get('interval', None),
                   time=d.get('time', None),
                   until=d.get('until', None))


@dataclass
class QueryList:
    count: int
    page: int
    page_size: int
    results: 'List[Query]'

    def as_dict(self) -> dict:
        body = {}
        if self.count: body['count'] = self.count
        if self.page: body['page'] = self.page
        if self.page_size: body['page_size'] = self.page_size
        if self.results: body['results'] = [v.as_dict() for v in self.results]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'QueryList':
        return cls(count=d.get('count', None),
                   page=d.get('page', None),
                   page_size=d.get('page_size', None),
                   results=[Query.from_dict(v)
                            for v in d['results']] if 'results' in d and d['results'] is not None else None)


@dataclass
class QueryMetrics:
    """Metrics about query execution."""

    compilation_time_ms: int
    execution_time_ms: int
    network_sent_bytes: int
    photon_total_time_ms: int
    queued_overload_time_ms: int
    queued_provisioning_time_ms: int
    read_bytes: int
    read_cache_bytes: int
    read_files_count: int
    read_partitions_count: int
    read_remote_bytes: int
    result_fetch_time_ms: int
    result_from_cache: bool
    rows_produced_count: int
    rows_read_count: int
    spill_to_disk_bytes: int
    task_total_time_ms: int
    total_files_count: int
    total_partitions_count: int
    total_time_ms: int
    write_remote_bytes: int

    def as_dict(self) -> dict:
        body = {}
        if self.compilation_time_ms: body['compilation_time_ms'] = self.compilation_time_ms
        if self.execution_time_ms: body['execution_time_ms'] = self.execution_time_ms
        if self.network_sent_bytes: body['network_sent_bytes'] = self.network_sent_bytes
        if self.photon_total_time_ms: body['photon_total_time_ms'] = self.photon_total_time_ms
        if self.queued_overload_time_ms: body['queued_overload_time_ms'] = self.queued_overload_time_ms
        if self.queued_provisioning_time_ms:
            body['queued_provisioning_time_ms'] = self.queued_provisioning_time_ms
        if self.read_bytes: body['read_bytes'] = self.read_bytes
        if self.read_cache_bytes: body['read_cache_bytes'] = self.read_cache_bytes
        if self.read_files_count: body['read_files_count'] = self.read_files_count
        if self.read_partitions_count: body['read_partitions_count'] = self.read_partitions_count
        if self.read_remote_bytes: body['read_remote_bytes'] = self.read_remote_bytes
        if self.result_fetch_time_ms: body['result_fetch_time_ms'] = self.result_fetch_time_ms
        if self.result_from_cache: body['result_from_cache'] = self.result_from_cache
        if self.rows_produced_count: body['rows_produced_count'] = self.rows_produced_count
        if self.rows_read_count: body['rows_read_count'] = self.rows_read_count
        if self.spill_to_disk_bytes: body['spill_to_disk_bytes'] = self.spill_to_disk_bytes
        if self.task_total_time_ms: body['task_total_time_ms'] = self.task_total_time_ms
        if self.total_files_count: body['total_files_count'] = self.total_files_count
        if self.total_partitions_count: body['total_partitions_count'] = self.total_partitions_count
        if self.total_time_ms: body['total_time_ms'] = self.total_time_ms
        if self.write_remote_bytes: body['write_remote_bytes'] = self.write_remote_bytes
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'QueryMetrics':
        return cls(compilation_time_ms=d.get('compilation_time_ms', None),
                   execution_time_ms=d.get('execution_time_ms', None),
                   network_sent_bytes=d.get('network_sent_bytes', None),
                   photon_total_time_ms=d.get('photon_total_time_ms', None),
                   queued_overload_time_ms=d.get('queued_overload_time_ms', None),
                   queued_provisioning_time_ms=d.get('queued_provisioning_time_ms', None),
                   read_bytes=d.get('read_bytes', None),
                   read_cache_bytes=d.get('read_cache_bytes', None),
                   read_files_count=d.get('read_files_count', None),
                   read_partitions_count=d.get('read_partitions_count', None),
                   read_remote_bytes=d.get('read_remote_bytes', None),
                   result_fetch_time_ms=d.get('result_fetch_time_ms', None),
                   result_from_cache=d.get('result_from_cache', None),
                   rows_produced_count=d.get('rows_produced_count', None),
                   rows_read_count=d.get('rows_read_count', None),
                   spill_to_disk_bytes=d.get('spill_to_disk_bytes', None),
                   task_total_time_ms=d.get('task_total_time_ms', None),
                   total_files_count=d.get('total_files_count', None),
                   total_partitions_count=d.get('total_partitions_count', None),
                   total_time_ms=d.get('total_time_ms', None),
                   write_remote_bytes=d.get('write_remote_bytes', None))


@dataclass
class QueryOptions:
    moved_to_trash_at: str
    parameters: 'List[Parameter]'

    def as_dict(self) -> dict:
        body = {}
        if self.moved_to_trash_at: body['moved_to_trash_at'] = self.moved_to_trash_at
        if self.parameters: body['parameters'] = [v.as_dict() for v in self.parameters]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'QueryOptions':
        return cls(moved_to_trash_at=d.get('moved_to_trash_at', None),
                   parameters=[Parameter.from_dict(v) for v in d['parameters']]
                   if 'parameters' in d and d['parameters'] is not None else None)


@dataclass
class QueryPostContent:
    data_source_id: str
    description: str
    name: str
    options: Any
    parent: str
    query: str
    schedule: 'QueryInterval'

    def as_dict(self) -> dict:
        body = {}
        if self.data_source_id: body['data_source_id'] = self.data_source_id
        if self.description: body['description'] = self.description
        if self.name: body['name'] = self.name
        if self.options: body['options'] = self.options
        if self.parent: body['parent'] = self.parent
        if self.query: body['query'] = self.query
        if self.schedule: body['schedule'] = self.schedule.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'QueryPostContent':
        return cls(data_source_id=d.get('data_source_id', None),
                   description=d.get('description', None),
                   name=d.get('name', None),
                   options=d.get('options', None),
                   parent=d.get('parent', None),
                   query=d.get('query', None),
                   schedule=QueryInterval.from_dict(d['schedule']) if 'schedule' in d else None)


class QueryStatementType(Enum):
    """Type of statement for this query"""

    ALTER = 'ALTER'
    ANALYZE = 'ANALYZE'
    COPY = 'COPY'
    CREATE = 'CREATE'
    DELETE = 'DELETE'
    DESCRIBE = 'DESCRIBE'
    DROP = 'DROP'
    EXPLAIN = 'EXPLAIN'
    GRANT = 'GRANT'
    INSERT = 'INSERT'
    MERGE = 'MERGE'
    OPTIMIZE = 'OPTIMIZE'
    OTHER = 'OTHER'
    REFRESH = 'REFRESH'
    REPLACE = 'REPLACE'
    REVOKE = 'REVOKE'
    SELECT = 'SELECT'
    SET = 'SET'
    SHOW = 'SHOW'
    TRUNCATE = 'TRUNCATE'
    UPDATE = 'UPDATE'
    USE = 'USE'


class QueryStatus(Enum):
    """This describes an enum"""

    CANCELED = 'CANCELED'
    FAILED = 'FAILED'
    FINISHED = 'FINISHED'
    QUEUED = 'QUEUED'
    RUNNING = 'RUNNING'


@dataclass
class RefreshSchedule:
    cron: str
    data_source_id: str
    id: str

    def as_dict(self) -> dict:
        body = {}
        if self.cron: body['cron'] = self.cron
        if self.data_source_id: body['data_source_id'] = self.data_source_id
        if self.id: body['id'] = self.id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'RefreshSchedule':
        return cls(cron=d.get('cron', None),
                   data_source_id=d.get('data_source_id', None),
                   id=d.get('id', None))


@dataclass
class RepeatedEndpointConfPairs:
    config_pair: 'List[EndpointConfPair]'
    configuration_pairs: 'List[EndpointConfPair]'

    def as_dict(self) -> dict:
        body = {}
        if self.config_pair: body['config_pair'] = [v.as_dict() for v in self.config_pair]
        if self.configuration_pairs:
            body['configuration_pairs'] = [v.as_dict() for v in self.configuration_pairs]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'RepeatedEndpointConfPairs':
        return cls(config_pair=[EndpointConfPair.from_dict(v) for v in d['config_pair']]
                   if 'config_pair' in d and d['config_pair'] is not None else None,
                   configuration_pairs=[EndpointConfPair.from_dict(v) for v in d['configuration_pairs']]
                   if 'configuration_pairs' in d and d['configuration_pairs'] is not None else None)


@dataclass
class RestoreDashboardRequest:
    """Restore a dashboard"""

    dashboard_id: str


@dataclass
class RestoreQueryRequest:
    """Restore a query"""

    query_id: str


@dataclass
class ResultData:
    """Result data chunks are delivered in either the `chunk` field when using INLINE disposition, or
    in the `external_link` field when using EXTERNAL_LINKS disposition. Exactly one of these will be
    set."""

    byte_count: int
    chunk_index: int
    data_array: 'List[List[str]]'
    external_links: 'List[ExternalLink]'
    next_chunk_index: int
    next_chunk_internal_link: str
    row_count: int
    row_offset: int

    def as_dict(self) -> dict:
        body = {}
        if self.byte_count: body['byte_count'] = self.byte_count
        if self.chunk_index: body['chunk_index'] = self.chunk_index
        if self.data_array: body['data_array'] = [v for v in self.data_array]
        if self.external_links: body['external_links'] = [v.as_dict() for v in self.external_links]
        if self.next_chunk_index: body['next_chunk_index'] = self.next_chunk_index
        if self.next_chunk_internal_link: body['next_chunk_internal_link'] = self.next_chunk_internal_link
        if self.row_count: body['row_count'] = self.row_count
        if self.row_offset: body['row_offset'] = self.row_offset
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ResultData':
        return cls(byte_count=d.get('byte_count', None),
                   chunk_index=d.get('chunk_index', None),
                   data_array=d.get('data_array', None),
                   external_links=[ExternalLink.from_dict(v) for v in d['external_links']]
                   if 'external_links' in d and d['external_links'] is not None else None,
                   next_chunk_index=d.get('next_chunk_index', None),
                   next_chunk_internal_link=d.get('next_chunk_internal_link', None),
                   row_count=d.get('row_count', None),
                   row_offset=d.get('row_offset', None))


@dataclass
class ResultManifest:
    """The result manifest provides schema and metadata for the result set."""

    chunks: 'List[ChunkInfo]'
    format: 'Format'
    schema: 'ResultSchema'
    total_byte_count: int
    total_chunk_count: int
    total_row_count: int

    def as_dict(self) -> dict:
        body = {}
        if self.chunks: body['chunks'] = [v.as_dict() for v in self.chunks]
        if self.format: body['format'] = self.format.value
        if self.schema: body['schema'] = self.schema.as_dict()
        if self.total_byte_count: body['total_byte_count'] = self.total_byte_count
        if self.total_chunk_count: body['total_chunk_count'] = self.total_chunk_count
        if self.total_row_count: body['total_row_count'] = self.total_row_count
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ResultManifest':
        return cls(chunks=[ChunkInfo.from_dict(v)
                           for v in d['chunks']] if 'chunks' in d and d['chunks'] is not None else None,
                   format=Format(d['format']) if 'format' in d else None,
                   schema=ResultSchema.from_dict(d['schema']) if 'schema' in d else None,
                   total_byte_count=d.get('total_byte_count', None),
                   total_chunk_count=d.get('total_chunk_count', None),
                   total_row_count=d.get('total_row_count', None))


@dataclass
class ResultSchema:
    """Schema is an ordered list of column descriptions."""

    column_count: int
    columns: 'List[ColumnInfo]'

    def as_dict(self) -> dict:
        body = {}
        if self.column_count: body['column_count'] = self.column_count
        if self.columns: body['columns'] = [v.as_dict() for v in self.columns]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ResultSchema':
        return cls(column_count=d.get('column_count', None),
                   columns=[ColumnInfo.from_dict(v)
                            for v in d['columns']] if 'columns' in d and d['columns'] is not None else None)


@dataclass
class ServiceError:
    error_code: 'ServiceErrorCode'
    message: str

    def as_dict(self) -> dict:
        body = {}
        if self.error_code: body['error_code'] = self.error_code.value
        if self.message: body['message'] = self.message
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ServiceError':
        return cls(error_code=ServiceErrorCode(d['error_code']) if 'error_code' in d else None,
                   message=d.get('message', None))


class ServiceErrorCode(Enum):

    ABORTED = 'ABORTED'
    ALREADY_EXISTS = 'ALREADY_EXISTS'
    BAD_REQUEST = 'BAD_REQUEST'
    CANCELLED = 'CANCELLED'
    DEADLINE_EXCEEDED = 'DEADLINE_EXCEEDED'
    INTERNAL_ERROR = 'INTERNAL_ERROR'
    IO_ERROR = 'IO_ERROR'
    NOT_FOUND = 'NOT_FOUND'
    RESOURCE_EXHAUSTED = 'RESOURCE_EXHAUSTED'
    SERVICE_UNDER_MAINTENANCE = 'SERVICE_UNDER_MAINTENANCE'
    TEMPORARILY_UNAVAILABLE = 'TEMPORARILY_UNAVAILABLE'
    UNAUTHENTICATED = 'UNAUTHENTICATED'
    UNKNOWN = 'UNKNOWN'
    WORKSPACE_TEMPORARILY_UNAVAILABLE = 'WORKSPACE_TEMPORARILY_UNAVAILABLE'


@dataclass
class SetRequest:
    """Set object ACL"""

    access_control_list: 'List[AccessControl]'
    object_id: str
    object_type: 'ObjectTypePlural'

    def as_dict(self) -> dict:
        body = {}
        if self.access_control_list:
            body['access_control_list'] = [v.as_dict() for v in self.access_control_list]
        if self.object_id: body['objectId'] = self.object_id
        if self.object_type: body['objectType'] = self.object_type.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'SetRequest':
        return cls(access_control_list=[AccessControl.from_dict(v) for v in d['access_control_list']]
                   if 'access_control_list' in d and d['access_control_list'] is not None else None,
                   object_id=d.get('objectId', None),
                   object_type=ObjectTypePlural(d['objectType']) if 'objectType' in d else None)


@dataclass
class SetResponse:
    access_control_list: 'List[AccessControl]'
    object_id: 'ObjectType'
    object_type: str

    def as_dict(self) -> dict:
        body = {}
        if self.access_control_list:
            body['access_control_list'] = [v.as_dict() for v in self.access_control_list]
        if self.object_id: body['object_id'] = self.object_id.value
        if self.object_type: body['object_type'] = self.object_type
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'SetResponse':
        return cls(access_control_list=[AccessControl.from_dict(v) for v in d['access_control_list']]
                   if 'access_control_list' in d and d['access_control_list'] is not None else None,
                   object_id=ObjectType(d['object_id']) if 'object_id' in d else None,
                   object_type=d.get('object_type', None))


@dataclass
class SetWorkspaceWarehouseConfigRequest:
    channel: 'Channel'
    config_param: 'RepeatedEndpointConfPairs'
    data_access_config: 'List[EndpointConfPair]'
    enable_databricks_compute: bool
    enable_serverless_compute: bool
    enabled_warehouse_types: 'List[WarehouseTypePair]'
    global_param: 'RepeatedEndpointConfPairs'
    google_service_account: str
    instance_profile_arn: str
    security_policy: 'SetWorkspaceWarehouseConfigRequestSecurityPolicy'
    serverless_agreement: bool
    sql_configuration_parameters: 'RepeatedEndpointConfPairs'

    def as_dict(self) -> dict:
        body = {}
        if self.channel: body['channel'] = self.channel.as_dict()
        if self.config_param: body['config_param'] = self.config_param.as_dict()
        if self.data_access_config:
            body['data_access_config'] = [v.as_dict() for v in self.data_access_config]
        if self.enable_databricks_compute: body['enable_databricks_compute'] = self.enable_databricks_compute
        if self.enable_serverless_compute: body['enable_serverless_compute'] = self.enable_serverless_compute
        if self.enabled_warehouse_types:
            body['enabled_warehouse_types'] = [v.as_dict() for v in self.enabled_warehouse_types]
        if self.global_param: body['global_param'] = self.global_param.as_dict()
        if self.google_service_account: body['google_service_account'] = self.google_service_account
        if self.instance_profile_arn: body['instance_profile_arn'] = self.instance_profile_arn
        if self.security_policy: body['security_policy'] = self.security_policy.value
        if self.serverless_agreement: body['serverless_agreement'] = self.serverless_agreement
        if self.sql_configuration_parameters:
            body['sql_configuration_parameters'] = self.sql_configuration_parameters.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'SetWorkspaceWarehouseConfigRequest':
        return cls(
            channel=Channel.from_dict(d['channel']) if 'channel' in d else None,
            config_param=RepeatedEndpointConfPairs.from_dict(d['config_param'])
            if 'config_param' in d else None,
            data_access_config=[EndpointConfPair.from_dict(v) for v in d['data_access_config']]
            if 'data_access_config' in d and d['data_access_config'] is not None else None,
            enable_databricks_compute=d.get('enable_databricks_compute', None),
            enable_serverless_compute=d.get('enable_serverless_compute', None),
            enabled_warehouse_types=[WarehouseTypePair.from_dict(v) for v in d['enabled_warehouse_types']]
            if 'enabled_warehouse_types' in d and d['enabled_warehouse_types'] is not None else None,
            global_param=RepeatedEndpointConfPairs.from_dict(d['global_param'])
            if 'global_param' in d else None,
            google_service_account=d.get('google_service_account', None),
            instance_profile_arn=d.get('instance_profile_arn', None),
            security_policy=SetWorkspaceWarehouseConfigRequestSecurityPolicy(d['security_policy'])
            if 'security_policy' in d else None,
            serverless_agreement=d.get('serverless_agreement', None),
            sql_configuration_parameters=RepeatedEndpointConfPairs.from_dict(
                d['sql_configuration_parameters']) if 'sql_configuration_parameters' in d else None)


class SetWorkspaceWarehouseConfigRequestSecurityPolicy(Enum):
    """Security policy for endpoints"""

    DATA_ACCESS_CONTROL = 'DATA_ACCESS_CONTROL'
    NONE = 'NONE'
    PASSTHROUGH = 'PASSTHROUGH'


class SpotInstancePolicy(Enum):
    """Configurations whether the warehouse should use spot instances."""

    COST_OPTIMIZED = 'COST_OPTIMIZED'
    POLICY_UNSPECIFIED = 'POLICY_UNSPECIFIED'
    RELIABILITY_OPTIMIZED = 'RELIABILITY_OPTIMIZED'


@dataclass
class StartRequest:
    """Start a warehouse"""

    id: str


class State(Enum):
    """State of the warehouse"""

    DELETED = 'DELETED'
    DELETING = 'DELETING'
    RUNNING = 'RUNNING'
    STARTING = 'STARTING'
    STOPPED = 'STOPPED'
    STOPPING = 'STOPPING'


class StatementState(Enum):
    """Statement execution state: - `PENDING`: waiting for warehouse - `RUNNING`: running -
    `SUCCEEDED`: execution was successful, result data available for fetch - `FAILED`: execution
    failed; reason for failure described in accomanying error message - `CANCELED`: user canceled;
    can come from explicit cancel call, or timeout with `on_wait_timeout=CANCEL` - `CLOSED`:
    execution successful, and statement closed; result no longer available for fetch"""

    CANCELED = 'CANCELED'
    CLOSED = 'CLOSED'
    FAILED = 'FAILED'
    PENDING = 'PENDING'
    RUNNING = 'RUNNING'
    SUCCEEDED = 'SUCCEEDED'


@dataclass
class StatementStatus:
    """Status response includes execution state and if relevant, error information."""

    error: 'ServiceError'
    state: 'StatementState'

    def as_dict(self) -> dict:
        body = {}
        if self.error: body['error'] = self.error.as_dict()
        if self.state: body['state'] = self.state.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'StatementStatus':
        return cls(error=ServiceError.from_dict(d['error']) if 'error' in d else None,
                   state=StatementState(d['state']) if 'state' in d else None)


class Status(Enum):
    """Health status of the endpoint."""

    DEGRADED = 'DEGRADED'
    FAILED = 'FAILED'
    HEALTHY = 'HEALTHY'
    STATUS_UNSPECIFIED = 'STATUS_UNSPECIFIED'


@dataclass
class StopRequest:
    """Stop a warehouse"""

    id: str


@dataclass
class Subscription:
    alert_id: str
    destination: 'Destination'
    id: str
    user: 'User'

    def as_dict(self) -> dict:
        body = {}
        if self.alert_id: body['alert_id'] = self.alert_id
        if self.destination: body['destination'] = self.destination.as_dict()
        if self.id: body['id'] = self.id
        if self.user: body['user'] = self.user.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Subscription':
        return cls(alert_id=d.get('alert_id', None),
                   destination=Destination.from_dict(d['destination']) if 'destination' in d else None,
                   id=d.get('id', None),
                   user=User.from_dict(d['user']) if 'user' in d else None)


@dataclass
class Success:
    message: 'SuccessMessage'

    def as_dict(self) -> dict:
        body = {}
        if self.message: body['message'] = self.message.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Success':
        return cls(message=SuccessMessage(d['message']) if 'message' in d else None)


class SuccessMessage(Enum):

    Success = 'Success'


@dataclass
class TerminationReason:
    code: 'TerminationReasonCode'
    parameters: 'Dict[str,str]'
    type: 'TerminationReasonType'

    def as_dict(self) -> dict:
        body = {}
        if self.code: body['code'] = self.code.value
        if self.parameters: body['parameters'] = self.parameters
        if self.type: body['type'] = self.type.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'TerminationReason':
        return cls(code=TerminationReasonCode(d['code']) if 'code' in d else None,
                   parameters=d.get('parameters', None),
                   type=TerminationReasonType(d['type']) if 'type' in d else None)


class TerminationReasonCode(Enum):
    """status code indicating why the cluster was terminated"""

    ABUSE_DETECTED = 'ABUSE_DETECTED'
    ATTACH_PROJECT_FAILURE = 'ATTACH_PROJECT_FAILURE'
    AWS_AUTHORIZATION_FAILURE = 'AWS_AUTHORIZATION_FAILURE'
    AWS_INSUFFICIENT_FREE_ADDRESSES_IN_SUBNET_FAILURE = 'AWS_INSUFFICIENT_FREE_ADDRESSES_IN_SUBNET_FAILURE'
    AWS_INSUFFICIENT_INSTANCE_CAPACITY_FAILURE = 'AWS_INSUFFICIENT_INSTANCE_CAPACITY_FAILURE'
    AWS_MAX_SPOT_INSTANCE_COUNT_EXCEEDED_FAILURE = 'AWS_MAX_SPOT_INSTANCE_COUNT_EXCEEDED_FAILURE'
    AWS_REQUEST_LIMIT_EXCEEDED = 'AWS_REQUEST_LIMIT_EXCEEDED'
    AWS_UNSUPPORTED_FAILURE = 'AWS_UNSUPPORTED_FAILURE'
    AZURE_BYOK_KEY_PERMISSION_FAILURE = 'AZURE_BYOK_KEY_PERMISSION_FAILURE'
    AZURE_EPHEMERAL_DISK_FAILURE = 'AZURE_EPHEMERAL_DISK_FAILURE'
    AZURE_INVALID_DEPLOYMENT_TEMPLATE = 'AZURE_INVALID_DEPLOYMENT_TEMPLATE'
    AZURE_OPERATION_NOT_ALLOWED_EXCEPTION = 'AZURE_OPERATION_NOT_ALLOWED_EXCEPTION'
    AZURE_QUOTA_EXCEEDED_EXCEPTION = 'AZURE_QUOTA_EXCEEDED_EXCEPTION'
    AZURE_RESOURCE_MANAGER_THROTTLING = 'AZURE_RESOURCE_MANAGER_THROTTLING'
    AZURE_RESOURCE_PROVIDER_THROTTLING = 'AZURE_RESOURCE_PROVIDER_THROTTLING'
    AZURE_UNEXPECTED_DEPLOYMENT_TEMPLATE_FAILURE = 'AZURE_UNEXPECTED_DEPLOYMENT_TEMPLATE_FAILURE'
    AZURE_VM_EXTENSION_FAILURE = 'AZURE_VM_EXTENSION_FAILURE'
    AZURE_VNET_CONFIGURATION_FAILURE = 'AZURE_VNET_CONFIGURATION_FAILURE'
    BOOTSTRAP_TIMEOUT = 'BOOTSTRAP_TIMEOUT'
    BOOTSTRAP_TIMEOUT_CLOUD_PROVIDER_EXCEPTION = 'BOOTSTRAP_TIMEOUT_CLOUD_PROVIDER_EXCEPTION'
    CLOUD_PROVIDER_DISK_SETUP_FAILURE = 'CLOUD_PROVIDER_DISK_SETUP_FAILURE'
    CLOUD_PROVIDER_LAUNCH_FAILURE = 'CLOUD_PROVIDER_LAUNCH_FAILURE'
    CLOUD_PROVIDER_RESOURCE_STOCKOUT = 'CLOUD_PROVIDER_RESOURCE_STOCKOUT'
    CLOUD_PROVIDER_SHUTDOWN = 'CLOUD_PROVIDER_SHUTDOWN'
    COMMUNICATION_LOST = 'COMMUNICATION_LOST'
    CONTAINER_LAUNCH_FAILURE = 'CONTAINER_LAUNCH_FAILURE'
    CONTROL_PLANE_REQUEST_FAILURE = 'CONTROL_PLANE_REQUEST_FAILURE'
    DATABASE_CONNECTION_FAILURE = 'DATABASE_CONNECTION_FAILURE'
    DBFS_COMPONENT_UNHEALTHY = 'DBFS_COMPONENT_UNHEALTHY'
    DOCKER_IMAGE_PULL_FAILURE = 'DOCKER_IMAGE_PULL_FAILURE'
    DRIVER_UNREACHABLE = 'DRIVER_UNREACHABLE'
    DRIVER_UNRESPONSIVE = 'DRIVER_UNRESPONSIVE'
    EXECUTION_COMPONENT_UNHEALTHY = 'EXECUTION_COMPONENT_UNHEALTHY'
    GCP_QUOTA_EXCEEDED = 'GCP_QUOTA_EXCEEDED'
    GCP_SERVICE_ACCOUNT_DELETED = 'GCP_SERVICE_ACCOUNT_DELETED'
    GLOBAL_INIT_SCRIPT_FAILURE = 'GLOBAL_INIT_SCRIPT_FAILURE'
    HIVE_METASTORE_PROVISIONING_FAILURE = 'HIVE_METASTORE_PROVISIONING_FAILURE'
    IMAGE_PULL_PERMISSION_DENIED = 'IMAGE_PULL_PERMISSION_DENIED'
    INACTIVITY = 'INACTIVITY'
    INIT_SCRIPT_FAILURE = 'INIT_SCRIPT_FAILURE'
    INSTANCE_POOL_CLUSTER_FAILURE = 'INSTANCE_POOL_CLUSTER_FAILURE'
    INSTANCE_UNREACHABLE = 'INSTANCE_UNREACHABLE'
    INTERNAL_ERROR = 'INTERNAL_ERROR'
    INVALID_ARGUMENT = 'INVALID_ARGUMENT'
    INVALID_SPARK_IMAGE = 'INVALID_SPARK_IMAGE'
    IP_EXHAUSTION_FAILURE = 'IP_EXHAUSTION_FAILURE'
    JOB_FINISHED = 'JOB_FINISHED'
    K8S_AUTOSCALING_FAILURE = 'K8S_AUTOSCALING_FAILURE'
    K8S_DBR_CLUSTER_LAUNCH_TIMEOUT = 'K8S_DBR_CLUSTER_LAUNCH_TIMEOUT'
    METASTORE_COMPONENT_UNHEALTHY = 'METASTORE_COMPONENT_UNHEALTHY'
    NEPHOS_RESOURCE_MANAGEMENT = 'NEPHOS_RESOURCE_MANAGEMENT'
    NETWORK_CONFIGURATION_FAILURE = 'NETWORK_CONFIGURATION_FAILURE'
    NFS_MOUNT_FAILURE = 'NFS_MOUNT_FAILURE'
    NPIP_TUNNEL_SETUP_FAILURE = 'NPIP_TUNNEL_SETUP_FAILURE'
    NPIP_TUNNEL_TOKEN_FAILURE = 'NPIP_TUNNEL_TOKEN_FAILURE'
    REQUEST_REJECTED = 'REQUEST_REJECTED'
    REQUEST_THROTTLED = 'REQUEST_THROTTLED'
    SECRET_RESOLUTION_ERROR = 'SECRET_RESOLUTION_ERROR'
    SECURITY_DAEMON_REGISTRATION_EXCEPTION = 'SECURITY_DAEMON_REGISTRATION_EXCEPTION'
    SELF_BOOTSTRAP_FAILURE = 'SELF_BOOTSTRAP_FAILURE'
    SKIPPED_SLOW_NODES = 'SKIPPED_SLOW_NODES'
    SLOW_IMAGE_DOWNLOAD = 'SLOW_IMAGE_DOWNLOAD'
    SPARK_ERROR = 'SPARK_ERROR'
    SPARK_IMAGE_DOWNLOAD_FAILURE = 'SPARK_IMAGE_DOWNLOAD_FAILURE'
    SPARK_STARTUP_FAILURE = 'SPARK_STARTUP_FAILURE'
    SPOT_INSTANCE_TERMINATION = 'SPOT_INSTANCE_TERMINATION'
    STORAGE_DOWNLOAD_FAILURE = 'STORAGE_DOWNLOAD_FAILURE'
    STS_CLIENT_SETUP_FAILURE = 'STS_CLIENT_SETUP_FAILURE'
    SUBNET_EXHAUSTED_FAILURE = 'SUBNET_EXHAUSTED_FAILURE'
    TEMPORARILY_UNAVAILABLE = 'TEMPORARILY_UNAVAILABLE'
    TRIAL_EXPIRED = 'TRIAL_EXPIRED'
    UNEXPECTED_LAUNCH_FAILURE = 'UNEXPECTED_LAUNCH_FAILURE'
    UNKNOWN = 'UNKNOWN'
    UNSUPPORTED_INSTANCE_TYPE = 'UNSUPPORTED_INSTANCE_TYPE'
    UPDATE_INSTANCE_PROFILE_FAILURE = 'UPDATE_INSTANCE_PROFILE_FAILURE'
    USER_REQUEST = 'USER_REQUEST'
    WORKER_SETUP_FAILURE = 'WORKER_SETUP_FAILURE'
    WORKSPACE_CANCELLED_ERROR = 'WORKSPACE_CANCELLED_ERROR'
    WORKSPACE_CONFIGURATION_ERROR = 'WORKSPACE_CONFIGURATION_ERROR'


class TerminationReasonType(Enum):
    """type of the termination"""

    CLIENT_ERROR = 'CLIENT_ERROR'
    CLOUD_FAILURE = 'CLOUD_FAILURE'
    SERVICE_FAULT = 'SERVICE_FAULT'
    SUCCESS = 'SUCCESS'


@dataclass
class TimeRange:
    end_time_ms: int
    start_time_ms: int

    def as_dict(self) -> dict:
        body = {}
        if self.end_time_ms: body['end_time_ms'] = self.end_time_ms
        if self.start_time_ms: body['start_time_ms'] = self.start_time_ms
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'TimeRange':
        return cls(end_time_ms=d.get('end_time_ms', None), start_time_ms=d.get('start_time_ms', None))


class TimeoutAction(Enum):
    """When called in synchronous mode (`wait_timeout > 0s`), determines action when timeout reached:
    
    `CONTINUE` → statement execution continues asynchronously; call returns immediately. `CANCEL`
    → statement execution canceled; call returns immediately with `CANCELED` state."""

    CANCEL = 'CANCEL'
    CONTINUE = 'CONTINUE'


@dataclass
class TransferOwnershipObjectId:
    new_owner: str

    def as_dict(self) -> dict:
        body = {}
        if self.new_owner: body['new_owner'] = self.new_owner
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'TransferOwnershipObjectId':
        return cls(new_owner=d.get('new_owner', None))


@dataclass
class TransferOwnershipRequest:
    """Transfer object ownership"""

    new_owner: str
    object_id: 'TransferOwnershipObjectId'
    object_type: 'OwnableObjectType'

    def as_dict(self) -> dict:
        body = {}
        if self.new_owner: body['new_owner'] = self.new_owner
        if self.object_id: body['objectId'] = self.object_id.as_dict()
        if self.object_type: body['objectType'] = self.object_type.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'TransferOwnershipRequest':
        return cls(new_owner=d.get('new_owner', None),
                   object_id=TransferOwnershipObjectId.from_dict(d['objectId']) if 'objectId' in d else None,
                   object_type=OwnableObjectType(d['objectType']) if 'objectType' in d else None)


@dataclass
class UnsubscribeRequest:
    """[DEPRECATED] Unsubscribe to an alert"""

    alert_id: str
    subscription_id: str


@dataclass
class User:
    email: str
    id: int
    is_db_admin: bool
    name: str
    profile_image_url: str

    def as_dict(self) -> dict:
        body = {}
        if self.email: body['email'] = self.email
        if self.id: body['id'] = self.id
        if self.is_db_admin: body['is_db_admin'] = self.is_db_admin
        if self.name: body['name'] = self.name
        if self.profile_image_url: body['profile_image_url'] = self.profile_image_url
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'User':
        return cls(email=d.get('email', None),
                   id=d.get('id', None),
                   is_db_admin=d.get('is_db_admin', None),
                   name=d.get('name', None),
                   profile_image_url=d.get('profile_image_url', None))


@dataclass
class Visualization:
    """The visualization description API changes frequently and is unsupported. You can duplicate a
    visualization by copying description objects received _from the API_ and then using them to
    create a new one with a POST request to the same endpoint. Databricks does not recommend
    constructing ad-hoc visualizations entirely in JSON."""

    created_at: str
    description: str
    id: str
    name: str
    options: Any
    type: str
    updated_at: str

    def as_dict(self) -> dict:
        body = {}
        if self.created_at: body['created_at'] = self.created_at
        if self.description: body['description'] = self.description
        if self.id: body['id'] = self.id
        if self.name: body['name'] = self.name
        if self.options: body['options'] = self.options
        if self.type: body['type'] = self.type
        if self.updated_at: body['updated_at'] = self.updated_at
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Visualization':
        return cls(created_at=d.get('created_at', None),
                   description=d.get('description', None),
                   id=d.get('id', None),
                   name=d.get('name', None),
                   options=d.get('options', None),
                   type=d.get('type', None),
                   updated_at=d.get('updated_at', None))


class WarehouseType(Enum):

    CLASSIC = 'CLASSIC'
    PRO = 'PRO'
    TYPE_UNSPECIFIED = 'TYPE_UNSPECIFIED'


@dataclass
class WarehouseTypePair:
    enabled: bool
    warehouse_type: 'WarehouseType'

    def as_dict(self) -> dict:
        body = {}
        if self.enabled: body['enabled'] = self.enabled
        if self.warehouse_type: body['warehouse_type'] = self.warehouse_type.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'WarehouseTypePair':
        return cls(enabled=d.get('enabled', None),
                   warehouse_type=WarehouseType(d['warehouse_type']) if 'warehouse_type' in d else None)


@dataclass
class Widget:
    id: int
    options: 'WidgetOptions'
    visualization: 'Visualization'
    width: int

    def as_dict(self) -> dict:
        body = {}
        if self.id: body['id'] = self.id
        if self.options: body['options'] = self.options.as_dict()
        if self.visualization: body['visualization'] = self.visualization.as_dict()
        if self.width: body['width'] = self.width
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Widget':
        return cls(
            id=d.get('id', None),
            options=WidgetOptions.from_dict(d['options']) if 'options' in d else None,
            visualization=Visualization.from_dict(d['visualization']) if 'visualization' in d else None,
            width=d.get('width', None))


@dataclass
class WidgetOptions:
    created_at: str
    dashboard_id: str
    is_hidden: bool
    parameter_mappings: Any
    position: Any
    text: str
    updated_at: str

    def as_dict(self) -> dict:
        body = {}
        if self.created_at: body['created_at'] = self.created_at
        if self.dashboard_id: body['dashboard_id'] = self.dashboard_id
        if self.is_hidden: body['isHidden'] = self.is_hidden
        if self.parameter_mappings: body['parameterMappings'] = self.parameter_mappings
        if self.position: body['position'] = self.position
        if self.text: body['text'] = self.text
        if self.updated_at: body['updated_at'] = self.updated_at
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'WidgetOptions':
        return cls(created_at=d.get('created_at', None),
                   dashboard_id=d.get('dashboard_id', None),
                   is_hidden=d.get('isHidden', None),
                   parameter_mappings=d.get('parameterMappings', None),
                   position=d.get('position', None),
                   text=d.get('text', None),
                   updated_at=d.get('updated_at', None))


class AlertsAPI:
    """The alerts API can be used to perform CRUD operations on alerts. An alert is a Databricks SQL object that
    periodically runs a query, evaluates a condition of its result, and notifies one or more users and/or
    alert destinations if the condition was met.
    
    **Note**: Programmatic operations on refresh schedules via the Databricks SQL API are deprecated. Alert
    refresh schedules can be created, updated, fetched and deleted using Jobs API, e.g. :method:jobs/create."""

    def __init__(self, api_client):
        self._api = api_client

    def create(self,
               name: str,
               options: AlertOptions,
               query_id: str,
               *,
               parent: str = None,
               rearm: int = None,
               **kwargs) -> Alert:
        """Create an alert.
        
        Creates an alert. An alert is a Databricks SQL object that periodically runs a query, evaluates a
        condition of its result, and notifies users or alert destinations if the condition was met."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = CreateAlert(name=name, options=options, parent=parent, query_id=query_id, rearm=rearm)
        body = request.as_dict()

        json = self._api.do('POST', '/api/2.0/preview/sql/alerts', body=body)
        return Alert.from_dict(json)

    def create_schedule(self,
                        cron: str,
                        alert_id: str,
                        *,
                        data_source_id: str = None,
                        **kwargs) -> RefreshSchedule:
        """[DEPRECATED] Create a refresh schedule.
        
        Creates a new refresh schedule for an alert.
        
        **Note:** The structure of refresh schedules is subject to change.
        
        **Note:** This API is deprecated: Use :method:jobs/create to create a job with the alert."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = CreateRefreshSchedule(alert_id=alert_id, cron=cron, data_source_id=data_source_id)
        body = request.as_dict()

        json = self._api.do('POST',
                            f'/api/2.0/preview/sql/alerts/{request.alert_id}/refresh-schedules',
                            body=body)
        return RefreshSchedule.from_dict(json)

    def delete(self, alert_id: str, **kwargs):
        """Delete an alert.
        
        Deletes an alert. Deleted alerts are no longer accessible and cannot be restored. **Note:** Unlike
        queries and dashboards, alerts cannot be moved to the trash."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = DeleteAlertRequest(alert_id=alert_id)

        self._api.do('DELETE', f'/api/2.0/preview/sql/alerts/{request.alert_id}')

    def delete_schedule(self, alert_id: str, schedule_id: str, **kwargs):
        """[DEPRECATED] Delete a refresh schedule.
        
        Deletes an alert's refresh schedule. The refresh schedule specifies when to refresh and evaluate the
        associated query result.
        
        **Note:** This API is deprecated: Use :method:jobs/delete to delete a job for the alert."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = DeleteScheduleRequest(alert_id=alert_id, schedule_id=schedule_id)

        self._api.do(
            'DELETE',
            f'/api/2.0/preview/sql/alerts/{request.alert_id}/refresh-schedules/{request.schedule_id}')

    def get(self, alert_id: str, **kwargs) -> Alert:
        """Get an alert.
        
        Gets an alert."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GetAlertRequest(alert_id=alert_id)

        json = self._api.do('GET', f'/api/2.0/preview/sql/alerts/{request.alert_id}')
        return Alert.from_dict(json)

    def get_subscriptions(self, alert_id: str, **kwargs) -> Iterator[Subscription]:
        """[DEPRECATED] Get an alert's subscriptions.
        
        Get the subscriptions for an alert. An alert subscription represents exactly one recipient being
        notified whenever the alert is triggered. The alert recipient is specified by either the `user` field
        or the `destination` field. The `user` field is ignored if `destination` is non-`null`.
        
        **Note:** This API is deprecated: Use :method:jobs/get to get the subscriptions associated with a job
        for an alert."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GetSubscriptionsRequest(alert_id=alert_id)

        json = self._api.do('GET', f'/api/2.0/preview/sql/alerts/{request.alert_id}/subscriptions')
        return [Subscription.from_dict(v) for v in json]

    def list(self) -> Iterator[Alert]:
        """Get alerts.
        
        Gets a list of alerts."""

        json = self._api.do('GET', '/api/2.0/preview/sql/alerts')
        return [Alert.from_dict(v) for v in json]

    def list_schedules(self, alert_id: str, **kwargs) -> Iterator[RefreshSchedule]:
        """[DEPRECATED] Get refresh schedules.
        
        Gets the refresh schedules for the specified alert. Alerts can have refresh schedules that specify
        when to refresh and evaluate the associated query result.
        
        **Note:** Although refresh schedules are returned in a list, only one refresh schedule per alert is
        currently supported. The structure of refresh schedules is subject to change.
        
        **Note:** This API is deprecated: Use :method:jobs/list to list jobs and filter by the alert."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = ListSchedulesRequest(alert_id=alert_id)

        json = self._api.do('GET', f'/api/2.0/preview/sql/alerts/{request.alert_id}/refresh-schedules')
        return [RefreshSchedule.from_dict(v) for v in json]

    def subscribe(self,
                  alert_id: str,
                  *,
                  destination_id: str = None,
                  user_id: int = None,
                  **kwargs) -> Subscription:
        """[DEPRECATED] Subscribe to an alert.
        
        **Note:** This API is deprecated: Use :method:jobs/update to subscribe to a job for an alert."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = CreateSubscription(alert_id=alert_id, destination_id=destination_id, user_id=user_id)
        body = request.as_dict()

        json = self._api.do('POST',
                            f'/api/2.0/preview/sql/alerts/{request.alert_id}/subscriptions',
                            body=body)
        return Subscription.from_dict(json)

    def unsubscribe(self, alert_id: str, subscription_id: str, **kwargs):
        """[DEPRECATED] Unsubscribe to an alert.
        
        Unsubscribes a user or a destination to an alert.
        
        **Note:** This API is deprecated: Use :method:jobs/update to unsubscribe to a job for an alert."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = UnsubscribeRequest(alert_id=alert_id, subscription_id=subscription_id)

        self._api.do(
            'DELETE',
            f'/api/2.0/preview/sql/alerts/{request.alert_id}/subscriptions/{request.subscription_id}')

    def update(self,
               name: str,
               options: AlertOptions,
               query_id: str,
               alert_id: str,
               *,
               rearm: int = None,
               **kwargs):
        """Update an alert.
        
        Updates an alert."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = EditAlert(alert_id=alert_id, name=name, options=options, query_id=query_id, rearm=rearm)
        body = request.as_dict()
        self._api.do('PUT', f'/api/2.0/preview/sql/alerts/{request.alert_id}', body=body)


class DashboardsAPI:
    """In general, there is little need to modify dashboards using the API. However, it can be useful to use
    dashboard objects to look-up a collection of related query IDs. The API can also be used to duplicate
    multiple dashboards at once since you can get a dashboard definition with a GET request and then POST it
    to create a new one.
    
    **Note**: Programmatic operations on refresh schedules via the Databricks SQL API are deprecated.
    Dashboard refresh schedules can be created, updated, fetched and deleted using Jobs API, e.g.
    :method:jobs/create."""

    def __init__(self, api_client):
        self._api = api_client

    def create(self,
               *,
               dashboard_filters_enabled: bool = None,
               is_draft: bool = None,
               is_trashed: bool = None,
               name: str = None,
               parent: str = None,
               tags: List[str] = None,
               widgets: List[Widget] = None,
               **kwargs) -> Dashboard:
        """Create a dashboard object."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = CreateDashboardRequest(dashboard_filters_enabled=dashboard_filters_enabled,
                                             is_draft=is_draft,
                                             is_trashed=is_trashed,
                                             name=name,
                                             parent=parent,
                                             tags=tags,
                                             widgets=widgets)
        body = request.as_dict()

        json = self._api.do('POST', '/api/2.0/preview/sql/dashboards', body=body)
        return Dashboard.from_dict(json)

    def delete(self, dashboard_id: str, **kwargs):
        """Remove a dashboard.
        
        Moves a dashboard to the trash. Trashed dashboards do not appear in list views or searches, and cannot
        be shared."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = DeleteDashboardRequest(dashboard_id=dashboard_id)

        self._api.do('DELETE', f'/api/2.0/preview/sql/dashboards/{request.dashboard_id}')

    def get(self, dashboard_id: str, **kwargs) -> Dashboard:
        """Retrieve a definition.
        
        Returns a JSON representation of a dashboard object, including its visualization and query objects."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GetDashboardRequest(dashboard_id=dashboard_id)

        json = self._api.do('GET', f'/api/2.0/preview/sql/dashboards/{request.dashboard_id}')
        return Dashboard.from_dict(json)

    def list(self,
             *,
             order: ListOrder = None,
             page: int = None,
             page_size: int = None,
             q: str = None,
             **kwargs) -> Iterator[Dashboard]:
        """Get dashboard objects.
        
        Fetch a paginated list of dashboard objects."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = ListDashboardsRequest(order=order, page=page, page_size=page_size, q=q)

        query = {}
        if order: query['order'] = request.order.value
        if page: query['page'] = request.page
        if page_size: query['page_size'] = request.page_size
        if q: query['q'] = request.q

        # deduplicate items that may have been added during iteration
        seen = set()
        query['page'] = 1
        while True:
            json = self._api.do('GET', '/api/2.0/preview/sql/dashboards', query=query)
            if 'results' not in json or not json['results']:
                return
            for v in json['results']:
                i = v['id']
                if i in seen:
                    continue
                seen.add(i)
                yield Dashboard.from_dict(v)
            query['page'] += 1

    def restore(self, dashboard_id: str, **kwargs):
        """Restore a dashboard.
        
        A restored dashboard appears in list views and searches and can be shared."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = RestoreDashboardRequest(dashboard_id=dashboard_id)

        self._api.do('POST', f'/api/2.0/preview/sql/dashboards/trash/{request.dashboard_id}')


class DataSourcesAPI:
    """This API is provided to assist you in making new query objects. When creating a query object, you may
    optionally specify a `data_source_id` for the SQL warehouse against which it will run. If you don't
    already know the `data_source_id` for your desired SQL warehouse, this API will help you find it.
    
    This API does not support searches. It returns the full list of SQL warehouses in your workspace. We
    advise you to use any text editor, REST client, or `grep` to search the response from this API for the
    name of your SQL warehouse as it appears in Databricks SQL."""

    def __init__(self, api_client):
        self._api = api_client

    def list(self) -> Iterator[DataSource]:
        """Get a list of SQL warehouses.
        
        Retrieves a full list of SQL warehouses available in this workspace. All fields that appear in this
        API response are enumerated for clarity. However, you need only a SQL warehouse's `id` to create new
        queries against it."""

        json = self._api.do('GET', '/api/2.0/preview/sql/data_sources')
        return [DataSource.from_dict(v) for v in json]


class DbsqlPermissionsAPI:
    """The SQL Permissions API is similar to the endpoints of the :method:permissions/set. However, this exposes
    only one endpoint, which gets the Access Control List for a given object. You cannot modify any
    permissions using this API.
    
    There are three levels of permission:
    
    - `CAN_VIEW`: Allows read-only access
    
    - `CAN_RUN`: Allows read access and run access (superset of `CAN_VIEW`)
    
    - `CAN_MANAGE`: Allows all actions: read, run, edit, delete, modify permissions (superset of `CAN_RUN`)"""

    def __init__(self, api_client):
        self._api = api_client

    def get(self, object_type: ObjectTypePlural, object_id: str, **kwargs) -> GetResponse:
        """Get object ACL.
        
        Gets a JSON representation of the access control list (ACL) for a specified object."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GetDbsqlPermissionRequest(object_id=object_id, object_type=object_type)

        json = self._api.do('GET',
                            f'/api/2.0/preview/sql/permissions/{request.object_type}/{request.object_id}')
        return GetResponse.from_dict(json)

    def set(self,
            object_type: ObjectTypePlural,
            object_id: str,
            *,
            access_control_list: List[AccessControl] = None,
            **kwargs) -> SetResponse:
        """Set object ACL.
        
        Sets the access control list (ACL) for a specified object. This operation will complete rewrite the
        ACL."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = SetRequest(access_control_list=access_control_list,
                                 object_id=object_id,
                                 object_type=object_type)
        body = request.as_dict()

        json = self._api.do('POST',
                            f'/api/2.0/preview/sql/permissions/{request.object_type}/{request.object_id}',
                            body=body)
        return SetResponse.from_dict(json)

    def transfer_ownership(self,
                           object_type: OwnableObjectType,
                           object_id: TransferOwnershipObjectId,
                           *,
                           new_owner: str = None,
                           **kwargs) -> Success:
        """Transfer object ownership.
        
        Transfers ownership of a dashboard, query, or alert to an active user. Requires an admin API key."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = TransferOwnershipRequest(new_owner=new_owner,
                                               object_id=object_id,
                                               object_type=object_type)
        body = request.as_dict()

        json = self._api.do(
            'POST',
            f'/api/2.0/preview/sql/permissions/{request.object_type}/{request.object_id}/transfer',
            body=body)
        return Success.from_dict(json)


class QueriesAPI:
    """These endpoints are used for CRUD operations on query definitions. Query definitions include the target
    SQL warehouse, query text, name, description, tags, execution schedule, parameters, and visualizations.
    
    **Note**: Programmatic operations on refresh schedules via the Databricks SQL API are deprecated. Query
    refresh schedules can be created, updated, fetched and deleted using Jobs API, e.g. :method:jobs/create."""

    def __init__(self, api_client):
        self._api = api_client

    def create(self,
               *,
               data_source_id: str = None,
               description: str = None,
               name: str = None,
               options: Any = None,
               parent: str = None,
               query: str = None,
               schedule: QueryInterval = None,
               **kwargs) -> Query:
        """Create a new query definition.
        
        Creates a new query definition. Queries created with this endpoint belong to the authenticated user
        making the request.
        
        The `data_source_id` field specifies the ID of the SQL warehouse to run this query against. You can
        use the Data Sources API to see a complete list of available SQL warehouses. Or you can copy the
        `data_source_id` from an existing query.
        
        **Note**: You cannot add a visualization until you create the query."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = QueryPostContent(data_source_id=data_source_id,
                                       description=description,
                                       name=name,
                                       options=options,
                                       parent=parent,
                                       query=query,
                                       schedule=schedule)
        body = request.as_dict()

        json = self._api.do('POST', '/api/2.0/preview/sql/queries', body=body)
        return Query.from_dict(json)

    def delete(self, query_id: str, **kwargs):
        """Delete a query.
        
        Moves a query to the trash. Trashed queries immediately disappear from searches and list views, and
        they cannot be used for alerts. The trash is deleted after 30 days."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = DeleteQueryRequest(query_id=query_id)

        self._api.do('DELETE', f'/api/2.0/preview/sql/queries/{request.query_id}')

    def get(self, query_id: str, **kwargs) -> Query:
        """Get a query definition.
        
        Retrieve a query object definition along with contextual permissions information about the currently
        authenticated user."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GetQueryRequest(query_id=query_id)

        json = self._api.do('GET', f'/api/2.0/preview/sql/queries/{request.query_id}')
        return Query.from_dict(json)

    def list(self,
             *,
             order: str = None,
             page: int = None,
             page_size: int = None,
             q: str = None,
             **kwargs) -> Iterator[Query]:
        """Get a list of queries.
        
        Gets a list of queries. Optionally, this list can be filtered by a search term."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = ListQueriesRequest(order=order, page=page, page_size=page_size, q=q)

        query = {}
        if order: query['order'] = request.order
        if page: query['page'] = request.page
        if page_size: query['page_size'] = request.page_size
        if q: query['q'] = request.q

        # deduplicate items that may have been added during iteration
        seen = set()
        query['page'] = 1
        while True:
            json = self._api.do('GET', '/api/2.0/preview/sql/queries', query=query)
            if 'results' not in json or not json['results']:
                return
            for v in json['results']:
                i = v['id']
                if i in seen:
                    continue
                seen.add(i)
                yield Query.from_dict(v)
            query['page'] += 1

    def restore(self, query_id: str, **kwargs):
        """Restore a query.
        
        Restore a query that has been moved to the trash. A restored query appears in list views and searches.
        You can use restored queries for alerts."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = RestoreQueryRequest(query_id=query_id)

        self._api.do('POST', f'/api/2.0/preview/sql/queries/trash/{request.query_id}')

    def update(self,
               query_id: str,
               *,
               data_source_id: str = None,
               description: str = None,
               name: str = None,
               options: Any = None,
               query: str = None,
               schedule: QueryInterval = None,
               **kwargs) -> Query:
        """Change a query definition.
        
        Modify this query definition.
        
        **Note**: You cannot undo this operation."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = QueryEditContent(data_source_id=data_source_id,
                                       description=description,
                                       name=name,
                                       options=options,
                                       query=query,
                                       query_id=query_id,
                                       schedule=schedule)
        body = request.as_dict()

        json = self._api.do('POST', f'/api/2.0/preview/sql/queries/{request.query_id}', body=body)
        return Query.from_dict(json)


class QueryHistoryAPI:
    """Access the history of queries through SQL warehouses."""

    def __init__(self, api_client):
        self._api = api_client

    def list(self,
             *,
             filter_by: QueryFilter = None,
             include_metrics: bool = None,
             max_results: int = None,
             page_token: str = None,
             **kwargs) -> Iterator[QueryInfo]:
        """List Queries.
        
        List the history of queries through SQL warehouses.
        
        You can filter by user ID, warehouse ID, status, and time range."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = ListQueryHistoryRequest(filter_by=filter_by,
                                              include_metrics=include_metrics,
                                              max_results=max_results,
                                              page_token=page_token)

        query = {}
        if filter_by: query['filter_by'] = request.filter_by.as_dict()
        if include_metrics: query['include_metrics'] = request.include_metrics
        if max_results: query['max_results'] = request.max_results
        if page_token: query['page_token'] = request.page_token

        while True:
            json = self._api.do('GET', '/api/2.0/sql/history/queries', query=query)
            if 'res' not in json or not json['res']:
                return
            for v in json['res']:
                yield QueryInfo.from_dict(v)
            if 'next_page_token' not in json or not json['next_page_token']:
                return
            query['page_token'] = json['next_page_token']


class StatementExecutionAPI:
    """The SQL Statement Execution API manages the execution of arbitrary SQL statements and the fetching of
    result data.
    
    **Release Status**
    
    This feature is in [Private Preview]. To try it, reach out to your Databricks contact.
    
    **Getting started**
    
    We suggest beginning with the [SQL Statement Execution API tutorial].
    
    **Overview of statement execution and result fetching**
    
    Statement execution begins by calling :method:statementexecution/executeStatement with a valid SQL
    statement and warehouse ID, along with optional parameters such as the data catalog and output format.
    
    When submitting the statement, the call can behave synchronously or asynchronously, based on the
    `wait_timeout` setting. When set between 5-50 seconds (default: 10) the call behaves synchronously; when
    set to `0s`, the call is asynchronous and responds immediately if accepted.
    
    **Call mode: synchronous**
    
    In synchronous mode, when statement execution completes, making the result available within the wait
    timeout, result data is returned in the response. This response will contain `statement_id`, `status`,
    `manifest`, and `result` fields. `status` will confirm success, and `manifest` contains both the result
    data column schema, and metadata about the result set. `result` will contain the first chunk of result
    data according to the specified disposition, and links to fetch any remaining chunks.
    
    If execution does not complete before `wait_timeout`, a response will be returned immediately. The setting
    `on_wait_timeout` determines how the system responds.
    
    By default, `on_wait_timeout=CONTINUE`, and after reaching timeout, a response is sent and statement
    execution continues asynchronously. The response will contain only `statement_id` and `status` fields, and
    caller must now follow the flow described for asynchronous call mode to poll and fetch result.
    
    Alternatively, `on_wait_timeout` can also be set to `CANCEL`; in this case if the timeout is reached
    before execution completes, the underlying statement execution is canceled, and a `CANCELED` status is
    returned in the response.
    
    **Call mode: asynchronous**
    
    In asynchronous mode, or after a timed-out synchronous request continues, a `statement_id` and `status`
    will be returned. In this case polling :method:statementexecution/getStatement calls are required to fetch
    result and metadata.
    
    Next a caller must poll until execution completes (SUCCEEDED, FAILED, etc.). Given a `statement_id`, poll
    by calling :method:statementexecution/getStatement.
    
    When execution has succeeded, the response will contain `status`, `manifest`, and `result` fields. These
    fields and structure are identical to those in the response to a successful synchronous submission.
    `result` will contain the first chunk of result data, either inline or as external links depending on
    disposition. Additional chunks of result data can be fetched by checking for the presence of the
    `next_chunk_internal_link` field, and iteratively `GET` those paths until that field is unset: `GET
    https://$DATABRICKS_HOST/{next_chunk_internal_link}`.
    
    **Fetching result data: format and disposition**
    
    Result data from statement execution is available in two formats: JSON, and [Apache Arrow Columnar].
    Statements producing a result set smaller than 16 MiB can be fetched as `format=JSON_ARRAY`, using the
    `disposition=INLINE`. When a statement executed in INLINE disposition exceeds this limit, execution is
    aborted, and no result can be fetched. Using `format=ARROW_STREAM` and `disposition=EXTERNAL_LINKS` allows
    large result sets to be fetched, and with higher throughput.
    
    The API uses defaults of `format=JSON_ARRAY` and `disposition=INLINE`. We advise explicitly setting format
    and disposition in all production use cases.
    
    **Statement response: statement_id, status, manifest, and result**
    
    The base call :method:statementexecution/getStatement returns a single response combining statement_id,
    status, a result manifest, and a result data chunk or link. The manifest contains the result schema
    definition, and result summary metadata. When using EXTERNAL_LINKS disposition, it also contains a full
    listing of all chunks and their summary metadata.
    
    **Use case: small result sets with INLINE + JSON_ARRAY**
    
    For flows which will generate small and predictable result sets (<= 16 MiB), INLINE downloads of
    JSON_ARRAY result data is typically the simplest way to execute and fetch result data. In this case,
    :method:statementexecution/executeStatement, along with a `warehouse_id` (required) and any other desired
    options. With default parameters, (noteably `wait_timeout=10s`), execution and result fetch are
    synchronous: a small result will be returned in the response, if completed within 10 seconds.
    `wait_timeout` can be extended up to 50 seconds.
    
    When result set in INLINE mode becomes larger, it will transfer results in chunks, each up to 4 MiB. After
    receiving the initial chunk with :method:statementexecution/executeStatement or
    :method:statementexecution/getStatement, subsequent calls are required to iteratively fetch each chunk.
    Each result response contains link to the next chunk, when there are additional chunks remaining; it can
    be found in the field `.next_chunk_internal_link`. This link is an absolute `path` to be joined with your
    `$DATABRICKS_HOST`, and of the form `/api/2.0/sql/statements/{statement_id}/result/chunks/...`. The next
    chunk can be fetched like this `GET https://$DATABRICKS_HOST/{next_chunk_internal_link}`.
    
    When using this mode, each chunk may be fetched once, and in order. If a chunk has no field
    `.next_chunk_internal_link`, that indicates it to be the last chunk, and all chunks have been fetched from
    the result set.
    
    **Use case: large result sets with EXTERNAL_LINKS + ARROW_STREAM**
    
    Using EXTERNAL_LINKS to fetch result data in Arrow format allows you to fetch large result sets
    efficiently. The primary difference from using INLINE disposition is that fetched result chunks contain
    resolved `external_links` URLs, which can be fetched with standard HTTP.
    
    **Presigned URLs**
    
    External links point to data stored within your workspace's internal DBFS, in the form of a presigned URL.
    The URLs are valid for only a short period, <= 15 minutes. Alongside each external_link is an expiration
    field indicating the time at which the URL is no longer valid. In EXTERNAL_LINKS mode, chunks be resolved
    and fetched multiple time, and in parallel.
    
    ----
    
    ### **Warning: drop authorization header when fetching data through external links**
    
    External link URLs do not require an Authorization header or token, and thus all calls to fetch external
    links must remove the Authorization header.
    
    ----
    
    Similar to INLINE mode, callers can iterate through the result set, by using the field
    `next_chunk_internal_link`. Each internal link response will contain an external link to the raw chunk
    data, and additionally contain the next_chunk_internal_link if there are more chunks.
    
    Unlike INLINE mode, when using EXTERNAL_LINKS, chunks may be fetched out of order, and in parallel to
    achieve higher throughput.
    
    **Limits and limitations**
    
    - All byte limits are calculated based on internal storage metrics, and will not match byte counts of
    actual payloads. - INLINE mode statements limited to 16 MiB, and will abort when this limit is exceeded. -
    Cancelation may silently fail: A successful response from a cancel request indicates that the cancel
    request was successfully received and sent to the processing engine. However, for example, an outstanding
    statement may complete execution during signal delivery, with cancel signal arriving too late to be
    meaningful. Polling for status until a terminal state is reached a reliable way to see final state. - Wait
    timeouts are approximate, occur server-side, and cannot account for caller delays, network latency from
    caller to service, and similarly. - After a statement has been submitted and a statement_id produced, that
    statement's status and result will automatically close after either of 2 conditions: - The last result
    chunk is fetched (or resolved to an external link). - Ten (10) minutes pass with no calls to get status or
    fetch result data. Best practice: in asynchronous clients, poll for status regularly (and with backoff) to
    keep the statement open and alive.
    
    **Private Preview limitations**
    
    - `EXTERNAL_LINKS` mode will fail for result sets < 5MB. - After any cancel or close operation, the
    statement will no longer be visible from the API, specifically - After fetching last result chunk
    (including `chunk_index=0`), the statement is closed; a short time after closure, the statement will no
    longer be visible to the API, and further calls may return 404. Thus calling
    :method:statementexecution/getStatement will return a 404 NOT FOUND error. - In practice, this means that
    a CANCEL and subsequent poll will often return a NOT FOUND.
    
    [Apache Arrow Columnar]: https://arrow.apache.org/overview/
    [Private Preview]: https://docs.databricks.com/release-notes/release-types.html
    [SQL Statement Execution API tutorial]: https://docs.databricks.com/sql/api/sql-execution-tutorial.html"""

    def __init__(self, api_client):
        self._api = api_client

    def cancel_execution(self, statement_id: str, **kwargs):
        """Cancel statement execution.
        
        Requests that an executing statement be cancelled. Callers must poll for status to see terminal state."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = CancelExecutionRequest(statement_id=statement_id)

        self._api.do('POST', f'/api/2.0/sql/statements/{request.statement_id}/cancel')

    def execute_statement(self,
                          *,
                          catalog: str = None,
                          disposition: Disposition = None,
                          format: Format = None,
                          on_wait_timeout: TimeoutAction = None,
                          schema: str = None,
                          statement: str = None,
                          wait_timeout: str = None,
                          warehouse_id: str = None,
                          **kwargs) -> ExecuteStatementResponse:
        """Execute an SQL statement.
        
        Execute an SQL statement, and if flagged as such, await its result for a specified time."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = ExecuteStatementRequest(catalog=catalog,
                                              disposition=disposition,
                                              format=format,
                                              on_wait_timeout=on_wait_timeout,
                                              schema=schema,
                                              statement=statement,
                                              wait_timeout=wait_timeout,
                                              warehouse_id=warehouse_id)
        body = request.as_dict()

        json = self._api.do('POST', '/api/2.0/sql/statements/', body=body)
        return ExecuteStatementResponse.from_dict(json)

    def get_statement(self, statement_id: str, **kwargs) -> GetStatementResponse:
        """Get status, manifest, and result first chunk.
        
        Polls for statement status; when status.state=SUCCEEDED will also return result manifest, and the
        first chunk of result data.
        
        **NOTE** This call currently may take up to 5 seconds to get latest status and result."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GetStatementRequest(statement_id=statement_id)

        json = self._api.do('GET', f'/api/2.0/sql/statements/{request.statement_id}')
        return GetStatementResponse.from_dict(json)

    def get_statement_result_chunk_n(self, statement_id: str, chunk_index: int, row_offset: int,
                                     **kwargs) -> ResultData:
        """Get result chunk by index.
        
        After statement execution has SUCCEEDED, result data can be fetched by chunks.
        
        The first chunk (`chunk_index=0`) is typically fetched through `getStatementResult`, and subsequent
        chunks with this call. The response structure is identical to the nested `result` element described in
        getStatementResult, and similarly includes `next_chunk_index` and `next_chunk_internal_link` for
        simple iteration through the result set."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GetStatementResultChunkNRequest(chunk_index=chunk_index,
                                                      row_offset=row_offset,
                                                      statement_id=statement_id)

        query = {}
        if row_offset: query['row_offset'] = request.row_offset

        json = self._api.do(
            'GET',
            f'/api/2.0/sql/statements/{request.statement_id}/result/chunks/{request.chunk_index}',
            query=query)
        return ResultData.from_dict(json)


class WarehousesAPI:
    """A SQL warehouse is a compute resource that lets you run SQL commands on data objects within Databricks
    SQL. Compute resources are infrastructure resources that provide processing capabilities in the cloud."""

    def __init__(self, api_client):
        self._api = api_client

    def create(self,
               *,
               auto_stop_mins: int = None,
               channel: Channel = None,
               cluster_size: str = None,
               creator_name: str = None,
               enable_photon: bool = None,
               enable_serverless_compute: bool = None,
               instance_profile_arn: str = None,
               max_num_clusters: int = None,
               min_num_clusters: int = None,
               name: str = None,
               spot_instance_policy: SpotInstancePolicy = None,
               tags: EndpointTags = None,
               warehouse_type: WarehouseType = None,
               wait=True,
               timeout=20,
               **kwargs) -> GetWarehouseResponse:
        """Create a warehouse.
        
        Creates a new SQL warehouse."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = CreateWarehouseRequest(auto_stop_mins=auto_stop_mins,
                                             channel=channel,
                                             cluster_size=cluster_size,
                                             creator_name=creator_name,
                                             enable_photon=enable_photon,
                                             enable_serverless_compute=enable_serverless_compute,
                                             instance_profile_arn=instance_profile_arn,
                                             max_num_clusters=max_num_clusters,
                                             min_num_clusters=min_num_clusters,
                                             name=name,
                                             spot_instance_policy=spot_instance_policy,
                                             tags=tags,
                                             warehouse_type=warehouse_type)
        body = request.as_dict()
        if wait:
            op_response = self._api.do('POST', '/api/2.0/sql/warehouses', body=body)
            started = time.time()
            target_states = (State.RUNNING, )
            failure_states = (State.STOPPED, State.DELETED, )
            status_message = 'polling...'
            attempt = 1
            while (started + (timeout * 60)) > time.time():
                poll = self.get(id=op_response['id'])
                status = poll.state
                status_message = f'current status: {status}'
                if poll.health:
                    status_message = poll.health.summary
                if status in target_states:
                    return poll
                if status in failure_states:
                    msg = f'failed to reach RUNNING, got {status}: {status_message}'
                    raise OperationFailed(msg)
                prefix = f"warehouses.get(id={op_response['id']})"
                sleep = attempt
                if sleep > 10:
                    # sleep 10s max per attempt
                    sleep = 10
                _LOG.debug(f'{prefix}: ({status}) {status_message} (sleeping ~{sleep}s)')
                time.sleep(sleep + random.random())
                attempt += 1
            raise OperationTimeout(f'timed out after {timeout} minutes: {status_message}')
        self._api.do('POST', '/api/2.0/sql/warehouses', body=body)

    def delete(self, id: str, wait=True, timeout=20, **kwargs) -> GetWarehouseResponse:
        """Delete a warehouse.
        
        Deletes a SQL warehouse."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = DeleteWarehouseRequest(id=id)

        if wait:
            self._api.do('DELETE', f'/api/2.0/sql/warehouses/{request.id}')
            started = time.time()
            target_states = (State.DELETED, )
            status_message = 'polling...'
            attempt = 1
            while (started + (timeout * 60)) > time.time():
                poll = self.get(id=request.id)
                status = poll.state
                status_message = f'current status: {status}'
                if poll.health:
                    status_message = poll.health.summary
                if status in target_states:
                    return poll
                prefix = f"warehouses.get(id={request.id})"
                sleep = attempt
                if sleep > 10:
                    # sleep 10s max per attempt
                    sleep = 10
                _LOG.debug(f'{prefix}: ({status}) {status_message} (sleeping ~{sleep}s)')
                time.sleep(sleep + random.random())
                attempt += 1
            raise OperationTimeout(f'timed out after {timeout} minutes: {status_message}')
        self._api.do('DELETE', f'/api/2.0/sql/warehouses/{request.id}')

    def edit(self,
             id: str,
             *,
             auto_stop_mins: int = None,
             channel: Channel = None,
             cluster_size: str = None,
             creator_name: str = None,
             enable_databricks_compute: bool = None,
             enable_photon: bool = None,
             enable_serverless_compute: bool = None,
             instance_profile_arn: str = None,
             max_num_clusters: int = None,
             min_num_clusters: int = None,
             name: str = None,
             spot_instance_policy: SpotInstancePolicy = None,
             tags: EndpointTags = None,
             warehouse_type: WarehouseType = None,
             wait=True,
             timeout=20,
             **kwargs) -> GetWarehouseResponse:
        """Update a warehouse.
        
        Updates the configuration for a SQL warehouse."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = EditWarehouseRequest(auto_stop_mins=auto_stop_mins,
                                           channel=channel,
                                           cluster_size=cluster_size,
                                           creator_name=creator_name,
                                           enable_databricks_compute=enable_databricks_compute,
                                           enable_photon=enable_photon,
                                           enable_serverless_compute=enable_serverless_compute,
                                           id=id,
                                           instance_profile_arn=instance_profile_arn,
                                           max_num_clusters=max_num_clusters,
                                           min_num_clusters=min_num_clusters,
                                           name=name,
                                           spot_instance_policy=spot_instance_policy,
                                           tags=tags,
                                           warehouse_type=warehouse_type)
        body = request.as_dict()
        if wait:
            self._api.do('POST', f'/api/2.0/sql/warehouses/{request.id}/edit', body=body)
            started = time.time()
            target_states = (State.RUNNING, )
            failure_states = (State.STOPPED, State.DELETED, )
            status_message = 'polling...'
            attempt = 1
            while (started + (timeout * 60)) > time.time():
                poll = self.get(id=request.id)
                status = poll.state
                status_message = f'current status: {status}'
                if poll.health:
                    status_message = poll.health.summary
                if status in target_states:
                    return poll
                if status in failure_states:
                    msg = f'failed to reach RUNNING, got {status}: {status_message}'
                    raise OperationFailed(msg)
                prefix = f"warehouses.get(id={request.id})"
                sleep = attempt
                if sleep > 10:
                    # sleep 10s max per attempt
                    sleep = 10
                _LOG.debug(f'{prefix}: ({status}) {status_message} (sleeping ~{sleep}s)')
                time.sleep(sleep + random.random())
                attempt += 1
            raise OperationTimeout(f'timed out after {timeout} minutes: {status_message}')
        self._api.do('POST', f'/api/2.0/sql/warehouses/{request.id}/edit', body=body)

    def get(self, id: str, wait=False, timeout=20, **kwargs) -> GetWarehouseResponse:
        """Get warehouse info.
        
        Gets the information for a single SQL warehouse."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GetWarehouseRequest(id=id)

        if wait:
            op_response = self._api.do('GET', f'/api/2.0/sql/warehouses/{request.id}')
            started = time.time()
            target_states = (State.RUNNING, )
            failure_states = (State.STOPPED, State.DELETED, )
            status_message = 'polling...'
            attempt = 1
            while (started + (timeout * 60)) > time.time():
                poll = self.get(id=op_response['id'])
                status = poll.state
                status_message = f'current status: {status}'
                if poll.health:
                    status_message = poll.health.summary
                if status in target_states:
                    return poll
                if status in failure_states:
                    msg = f'failed to reach RUNNING, got {status}: {status_message}'
                    raise OperationFailed(msg)
                prefix = f"warehouses.get(id={op_response['id']})"
                sleep = attempt
                if sleep > 10:
                    # sleep 10s max per attempt
                    sleep = 10
                _LOG.debug(f'{prefix}: ({status}) {status_message} (sleeping ~{sleep}s)')
                time.sleep(sleep + random.random())
                attempt += 1
            raise OperationTimeout(f'timed out after {timeout} minutes: {status_message}')

        json = self._api.do('GET', f'/api/2.0/sql/warehouses/{request.id}')
        return GetWarehouseResponse.from_dict(json)

    def get_workspace_warehouse_config(self) -> GetWorkspaceWarehouseConfigResponse:
        """Get the workspace configuration.
        
        Gets the workspace level configuration that is shared by all SQL warehouses in a workspace."""

        json = self._api.do('GET', '/api/2.0/sql/config/warehouses')
        return GetWorkspaceWarehouseConfigResponse.from_dict(json)

    def list(self, *, run_as_user_id: int = None, **kwargs) -> Iterator[EndpointInfo]:
        """List warehouses.
        
        Lists all SQL warehouses that a user has manager permissions on."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = ListWarehousesRequest(run_as_user_id=run_as_user_id)

        query = {}
        if run_as_user_id: query['run_as_user_id'] = request.run_as_user_id

        json = self._api.do('GET', '/api/2.0/sql/warehouses', query=query)
        return [EndpointInfo.from_dict(v) for v in json['warehouses']]

    def set_workspace_warehouse_config(
            self,
            *,
            channel: Channel = None,
            config_param: RepeatedEndpointConfPairs = None,
            data_access_config: List[EndpointConfPair] = None,
            enable_databricks_compute: bool = None,
            enable_serverless_compute: bool = None,
            enabled_warehouse_types: List[WarehouseTypePair] = None,
            global_param: RepeatedEndpointConfPairs = None,
            google_service_account: str = None,
            instance_profile_arn: str = None,
            security_policy: SetWorkspaceWarehouseConfigRequestSecurityPolicy = None,
            serverless_agreement: bool = None,
            sql_configuration_parameters: RepeatedEndpointConfPairs = None,
            **kwargs):
        """Set the workspace configuration.
        
        Sets the workspace level configuration that is shared by all SQL warehouses in a workspace."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = SetWorkspaceWarehouseConfigRequest(
                channel=channel,
                config_param=config_param,
                data_access_config=data_access_config,
                enable_databricks_compute=enable_databricks_compute,
                enable_serverless_compute=enable_serverless_compute,
                enabled_warehouse_types=enabled_warehouse_types,
                global_param=global_param,
                google_service_account=google_service_account,
                instance_profile_arn=instance_profile_arn,
                security_policy=security_policy,
                serverless_agreement=serverless_agreement,
                sql_configuration_parameters=sql_configuration_parameters)
        body = request.as_dict()
        self._api.do('PUT', '/api/2.0/sql/config/warehouses', body=body)

    def start(self, id: str, wait=True, timeout=20, **kwargs) -> GetWarehouseResponse:
        """Start a warehouse.
        
        Starts a SQL warehouse."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = StartRequest(id=id)

        if wait:
            self._api.do('POST', f'/api/2.0/sql/warehouses/{request.id}/start')
            started = time.time()
            target_states = (State.RUNNING, )
            failure_states = (State.STOPPED, State.DELETED, )
            status_message = 'polling...'
            attempt = 1
            while (started + (timeout * 60)) > time.time():
                poll = self.get(id=request.id)
                status = poll.state
                status_message = f'current status: {status}'
                if poll.health:
                    status_message = poll.health.summary
                if status in target_states:
                    return poll
                if status in failure_states:
                    msg = f'failed to reach RUNNING, got {status}: {status_message}'
                    raise OperationFailed(msg)
                prefix = f"warehouses.get(id={request.id})"
                sleep = attempt
                if sleep > 10:
                    # sleep 10s max per attempt
                    sleep = 10
                _LOG.debug(f'{prefix}: ({status}) {status_message} (sleeping ~{sleep}s)')
                time.sleep(sleep + random.random())
                attempt += 1
            raise OperationTimeout(f'timed out after {timeout} minutes: {status_message}')
        self._api.do('POST', f'/api/2.0/sql/warehouses/{request.id}/start')

    def stop(self, id: str, wait=True, timeout=20, **kwargs) -> GetWarehouseResponse:
        """Stop a warehouse.
        
        Stops a SQL warehouse."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = StopRequest(id=id)

        if wait:
            self._api.do('POST', f'/api/2.0/sql/warehouses/{request.id}/stop')
            started = time.time()
            target_states = (State.STOPPED, )
            status_message = 'polling...'
            attempt = 1
            while (started + (timeout * 60)) > time.time():
                poll = self.get(id=request.id)
                status = poll.state
                status_message = f'current status: {status}'
                if poll.health:
                    status_message = poll.health.summary
                if status in target_states:
                    return poll
                prefix = f"warehouses.get(id={request.id})"
                sleep = attempt
                if sleep > 10:
                    # sleep 10s max per attempt
                    sleep = 10
                _LOG.debug(f'{prefix}: ({status}) {status_message} (sleeping ~{sleep}s)')
                time.sleep(sleep + random.random())
                attempt += 1
            raise OperationTimeout(f'timed out after {timeout} minutes: {status_message}')
        self._api.do('POST', f'/api/2.0/sql/warehouses/{request.id}/stop')
