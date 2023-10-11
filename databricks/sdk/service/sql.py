# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

import logging
import random
import time
from dataclasses import dataclass
from datetime import timedelta
from enum import Enum
from typing import Any, Callable, Dict, Iterator, List, Optional

from ..errors import OperationFailed
from ._internal import Wait, _enum, _from_dict, _repeated

_LOG = logging.getLogger('databricks.sdk')

# all definitions in this file are in alphabetical order


@dataclass
class AccessControl:
    group_name: Optional[str] = None
    permission_level: Optional['PermissionLevel'] = None
    user_name: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.group_name is not None: body['group_name'] = self.group_name
        if self.permission_level is not None: body['permission_level'] = self.permission_level.value
        if self.user_name is not None: body['user_name'] = self.user_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'AccessControl':
        return cls(group_name=d.get('group_name', None),
                   permission_level=_enum(d, 'permission_level', PermissionLevel),
                   user_name=d.get('user_name', None))


@dataclass
class Alert:
    created_at: Optional[str] = None
    id: Optional[str] = None
    last_triggered_at: Optional[str] = None
    name: Optional[str] = None
    options: Optional['AlertOptions'] = None
    parent: Optional[str] = None
    query: Optional['AlertQuery'] = None
    rearm: Optional[int] = None
    state: Optional['AlertState'] = None
    updated_at: Optional[str] = None
    user: Optional['User'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.created_at is not None: body['created_at'] = self.created_at
        if self.id is not None: body['id'] = self.id
        if self.last_triggered_at is not None: body['last_triggered_at'] = self.last_triggered_at
        if self.name is not None: body['name'] = self.name
        if self.options: body['options'] = self.options.as_dict()
        if self.parent is not None: body['parent'] = self.parent
        if self.query: body['query'] = self.query.as_dict()
        if self.rearm is not None: body['rearm'] = self.rearm
        if self.state is not None: body['state'] = self.state.value
        if self.updated_at is not None: body['updated_at'] = self.updated_at
        if self.user: body['user'] = self.user.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Alert':
        return cls(created_at=d.get('created_at', None),
                   id=d.get('id', None),
                   last_triggered_at=d.get('last_triggered_at', None),
                   name=d.get('name', None),
                   options=_from_dict(d, 'options', AlertOptions),
                   parent=d.get('parent', None),
                   query=_from_dict(d, 'query', AlertQuery),
                   rearm=d.get('rearm', None),
                   state=_enum(d, 'state', AlertState),
                   updated_at=d.get('updated_at', None),
                   user=_from_dict(d, 'user', User))


@dataclass
class AlertOptions:
    """Alert configuration options."""

    column: str
    op: str
    value: Any
    custom_body: Optional[str] = None
    custom_subject: Optional[str] = None
    empty_result_state: Optional['AlertOptionsEmptyResultState'] = None
    muted: Optional[bool] = None

    def as_dict(self) -> dict:
        body = {}
        if self.column is not None: body['column'] = self.column
        if self.custom_body is not None: body['custom_body'] = self.custom_body
        if self.custom_subject is not None: body['custom_subject'] = self.custom_subject
        if self.empty_result_state is not None: body['empty_result_state'] = self.empty_result_state.value
        if self.muted is not None: body['muted'] = self.muted
        if self.op is not None: body['op'] = self.op
        if self.value: body['value'] = self.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'AlertOptions':
        return cls(column=d.get('column', None),
                   custom_body=d.get('custom_body', None),
                   custom_subject=d.get('custom_subject', None),
                   empty_result_state=_enum(d, 'empty_result_state', AlertOptionsEmptyResultState),
                   muted=d.get('muted', None),
                   op=d.get('op', None),
                   value=d.get('value', None))


class AlertOptionsEmptyResultState(Enum):
    """State that alert evaluates to when query result is empty."""

    OK = 'ok'
    TRIGGERED = 'triggered'
    UNKNOWN = 'unknown'


@dataclass
class AlertQuery:
    created_at: Optional[str] = None
    data_source_id: Optional[str] = None
    description: Optional[str] = None
    id: Optional[str] = None
    is_archived: Optional[bool] = None
    is_draft: Optional[bool] = None
    is_safe: Optional[bool] = None
    name: Optional[str] = None
    options: Optional['QueryOptions'] = None
    query: Optional[str] = None
    tags: Optional['List[str]'] = None
    updated_at: Optional[str] = None
    user_id: Optional[int] = None

    def as_dict(self) -> dict:
        body = {}
        if self.created_at is not None: body['created_at'] = self.created_at
        if self.data_source_id is not None: body['data_source_id'] = self.data_source_id
        if self.description is not None: body['description'] = self.description
        if self.id is not None: body['id'] = self.id
        if self.is_archived is not None: body['is_archived'] = self.is_archived
        if self.is_draft is not None: body['is_draft'] = self.is_draft
        if self.is_safe is not None: body['is_safe'] = self.is_safe
        if self.name is not None: body['name'] = self.name
        if self.options: body['options'] = self.options.as_dict()
        if self.query is not None: body['query'] = self.query
        if self.tags: body['tags'] = [v for v in self.tags]
        if self.updated_at is not None: body['updated_at'] = self.updated_at
        if self.user_id is not None: body['user_id'] = self.user_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'AlertQuery':
        return cls(created_at=d.get('created_at', None),
                   data_source_id=d.get('data_source_id', None),
                   description=d.get('description', None),
                   id=d.get('id', None),
                   is_archived=d.get('is_archived', None),
                   is_draft=d.get('is_draft', None),
                   is_safe=d.get('is_safe', None),
                   name=d.get('name', None),
                   options=_from_dict(d, 'options', QueryOptions),
                   query=d.get('query', None),
                   tags=d.get('tags', None),
                   updated_at=d.get('updated_at', None),
                   user_id=d.get('user_id', None))


class AlertState(Enum):
    """State of the alert. Possible values are: `unknown` (yet to be evaluated), `triggered` (evaluated
    and fulfilled trigger conditions), or `ok` (evaluated and did not fulfill trigger conditions)."""

    OK = 'ok'
    TRIGGERED = 'triggered'
    UNKNOWN = 'unknown'


@dataclass
class BaseChunkInfo:
    """Describes metadata for a particular chunk, within a result set; this structure is used both
    within a manifest, and when fetching individual chunk data or links."""

    byte_count: Optional[int] = None
    chunk_index: Optional[int] = None
    row_count: Optional[int] = None
    row_offset: Optional[int] = None

    def as_dict(self) -> dict:
        body = {}
        if self.byte_count is not None: body['byte_count'] = self.byte_count
        if self.chunk_index is not None: body['chunk_index'] = self.chunk_index
        if self.row_count is not None: body['row_count'] = self.row_count
        if self.row_offset is not None: body['row_offset'] = self.row_offset
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'BaseChunkInfo':
        return cls(byte_count=d.get('byte_count', None),
                   chunk_index=d.get('chunk_index', None),
                   row_count=d.get('row_count', None),
                   row_offset=d.get('row_offset', None))


@dataclass
class Channel:
    dbsql_version: Optional[str] = None
    name: Optional['ChannelName'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.dbsql_version is not None: body['dbsql_version'] = self.dbsql_version
        if self.name is not None: body['name'] = self.name.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Channel':
        return cls(dbsql_version=d.get('dbsql_version', None), name=_enum(d, 'name', ChannelName))


@dataclass
class ChannelInfo:
    """Channel information for the SQL warehouse at the time of query execution"""

    dbsql_version: Optional[str] = None
    name: Optional['ChannelName'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.dbsql_version is not None: body['dbsql_version'] = self.dbsql_version
        if self.name is not None: body['name'] = self.name.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ChannelInfo':
        return cls(dbsql_version=d.get('dbsql_version', None), name=_enum(d, 'name', ChannelName))


class ChannelName(Enum):

    CHANNEL_NAME_CURRENT = 'CHANNEL_NAME_CURRENT'
    CHANNEL_NAME_CUSTOM = 'CHANNEL_NAME_CUSTOM'
    CHANNEL_NAME_PREVIEW = 'CHANNEL_NAME_PREVIEW'
    CHANNEL_NAME_PREVIOUS = 'CHANNEL_NAME_PREVIOUS'
    CHANNEL_NAME_UNSPECIFIED = 'CHANNEL_NAME_UNSPECIFIED'


@dataclass
class ColumnInfo:
    name: Optional[str] = None
    position: Optional[int] = None
    type_interval_type: Optional[str] = None
    type_name: Optional['ColumnInfoTypeName'] = None
    type_precision: Optional[int] = None
    type_scale: Optional[int] = None
    type_text: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.name is not None: body['name'] = self.name
        if self.position is not None: body['position'] = self.position
        if self.type_interval_type is not None: body['type_interval_type'] = self.type_interval_type
        if self.type_name is not None: body['type_name'] = self.type_name.value
        if self.type_precision is not None: body['type_precision'] = self.type_precision
        if self.type_scale is not None: body['type_scale'] = self.type_scale
        if self.type_text is not None: body['type_text'] = self.type_text
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ColumnInfo':
        return cls(name=d.get('name', None),
                   position=d.get('position', None),
                   type_interval_type=d.get('type_interval_type', None),
                   type_name=_enum(d, 'type_name', ColumnInfoTypeName),
                   type_precision=d.get('type_precision', None),
                   type_scale=d.get('type_scale', None),
                   type_text=d.get('type_text', None))


class ColumnInfoTypeName(Enum):
    """The name of the base data type. This doesn't include details for complex types such as STRUCT,
    MAP or ARRAY."""

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
    query_id: str
    parent: Optional[str] = None
    rearm: Optional[int] = None

    def as_dict(self) -> dict:
        body = {}
        if self.name is not None: body['name'] = self.name
        if self.options: body['options'] = self.options.as_dict()
        if self.parent is not None: body['parent'] = self.parent
        if self.query_id is not None: body['query_id'] = self.query_id
        if self.rearm is not None: body['rearm'] = self.rearm
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateAlert':
        return cls(name=d.get('name', None),
                   options=_from_dict(d, 'options', AlertOptions),
                   parent=d.get('parent', None),
                   query_id=d.get('query_id', None),
                   rearm=d.get('rearm', None))


@dataclass
class CreateWarehouseRequest:
    auto_stop_mins: Optional[int] = None
    channel: Optional['Channel'] = None
    cluster_size: Optional[str] = None
    creator_name: Optional[str] = None
    enable_photon: Optional[bool] = None
    enable_serverless_compute: Optional[bool] = None
    instance_profile_arn: Optional[str] = None
    max_num_clusters: Optional[int] = None
    min_num_clusters: Optional[int] = None
    name: Optional[str] = None
    spot_instance_policy: Optional['SpotInstancePolicy'] = None
    tags: Optional['EndpointTags'] = None
    warehouse_type: Optional['CreateWarehouseRequestWarehouseType'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.auto_stop_mins is not None: body['auto_stop_mins'] = self.auto_stop_mins
        if self.channel: body['channel'] = self.channel.as_dict()
        if self.cluster_size is not None: body['cluster_size'] = self.cluster_size
        if self.creator_name is not None: body['creator_name'] = self.creator_name
        if self.enable_photon is not None: body['enable_photon'] = self.enable_photon
        if self.enable_serverless_compute is not None:
            body['enable_serverless_compute'] = self.enable_serverless_compute
        if self.instance_profile_arn is not None: body['instance_profile_arn'] = self.instance_profile_arn
        if self.max_num_clusters is not None: body['max_num_clusters'] = self.max_num_clusters
        if self.min_num_clusters is not None: body['min_num_clusters'] = self.min_num_clusters
        if self.name is not None: body['name'] = self.name
        if self.spot_instance_policy is not None:
            body['spot_instance_policy'] = self.spot_instance_policy.value
        if self.tags: body['tags'] = self.tags.as_dict()
        if self.warehouse_type is not None: body['warehouse_type'] = self.warehouse_type.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateWarehouseRequest':
        return cls(auto_stop_mins=d.get('auto_stop_mins', None),
                   channel=_from_dict(d, 'channel', Channel),
                   cluster_size=d.get('cluster_size', None),
                   creator_name=d.get('creator_name', None),
                   enable_photon=d.get('enable_photon', None),
                   enable_serverless_compute=d.get('enable_serverless_compute', None),
                   instance_profile_arn=d.get('instance_profile_arn', None),
                   max_num_clusters=d.get('max_num_clusters', None),
                   min_num_clusters=d.get('min_num_clusters', None),
                   name=d.get('name', None),
                   spot_instance_policy=_enum(d, 'spot_instance_policy', SpotInstancePolicy),
                   tags=_from_dict(d, 'tags', EndpointTags),
                   warehouse_type=_enum(d, 'warehouse_type', CreateWarehouseRequestWarehouseType))


class CreateWarehouseRequestWarehouseType(Enum):
    """Warehouse type: `PRO` or `CLASSIC`. If you want to use serverless compute, you must set to `PRO`
    and also set the field `enable_serverless_compute` to `true`."""

    CLASSIC = 'CLASSIC'
    PRO = 'PRO'
    TYPE_UNSPECIFIED = 'TYPE_UNSPECIFIED'


@dataclass
class CreateWarehouseResponse:
    id: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.id is not None: body['id'] = self.id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateWarehouseResponse':
        return cls(id=d.get('id', None))


@dataclass
class CreateWidget:
    dashboard_id: str
    options: 'WidgetOptions'
    width: int
    id: Optional[str] = None
    text: Optional[str] = None
    visualization_id: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.dashboard_id is not None: body['dashboard_id'] = self.dashboard_id
        if self.id is not None: body['id'] = self.id
        if self.options: body['options'] = self.options.as_dict()
        if self.text is not None: body['text'] = self.text
        if self.visualization_id is not None: body['visualization_id'] = self.visualization_id
        if self.width is not None: body['width'] = self.width
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateWidget':
        return cls(dashboard_id=d.get('dashboard_id', None),
                   id=d.get('id', None),
                   options=_from_dict(d, 'options', WidgetOptions),
                   text=d.get('text', None),
                   visualization_id=d.get('visualization_id', None),
                   width=d.get('width', None))


@dataclass
class Dashboard:
    """A JSON representing a dashboard containing widgets of visualizations and text boxes."""

    can_edit: Optional[bool] = None
    created_at: Optional[str] = None
    dashboard_filters_enabled: Optional[bool] = None
    id: Optional[str] = None
    is_archived: Optional[bool] = None
    is_draft: Optional[bool] = None
    is_favorite: Optional[bool] = None
    name: Optional[str] = None
    options: Optional['DashboardOptions'] = None
    parent: Optional[str] = None
    permission_tier: Optional['PermissionLevel'] = None
    slug: Optional[str] = None
    tags: Optional['List[str]'] = None
    updated_at: Optional[str] = None
    user: Optional['User'] = None
    user_id: Optional[int] = None
    widgets: Optional['List[Widget]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.can_edit is not None: body['can_edit'] = self.can_edit
        if self.created_at is not None: body['created_at'] = self.created_at
        if self.dashboard_filters_enabled is not None:
            body['dashboard_filters_enabled'] = self.dashboard_filters_enabled
        if self.id is not None: body['id'] = self.id
        if self.is_archived is not None: body['is_archived'] = self.is_archived
        if self.is_draft is not None: body['is_draft'] = self.is_draft
        if self.is_favorite is not None: body['is_favorite'] = self.is_favorite
        if self.name is not None: body['name'] = self.name
        if self.options: body['options'] = self.options.as_dict()
        if self.parent is not None: body['parent'] = self.parent
        if self.permission_tier is not None: body['permission_tier'] = self.permission_tier.value
        if self.slug is not None: body['slug'] = self.slug
        if self.tags: body['tags'] = [v for v in self.tags]
        if self.updated_at is not None: body['updated_at'] = self.updated_at
        if self.user: body['user'] = self.user.as_dict()
        if self.user_id is not None: body['user_id'] = self.user_id
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
                   options=_from_dict(d, 'options', DashboardOptions),
                   parent=d.get('parent', None),
                   permission_tier=_enum(d, 'permission_tier', PermissionLevel),
                   slug=d.get('slug', None),
                   tags=d.get('tags', None),
                   updated_at=d.get('updated_at', None),
                   user=_from_dict(d, 'user', User),
                   user_id=d.get('user_id', None),
                   widgets=_repeated(d, 'widgets', Widget))


@dataclass
class DashboardOptions:
    moved_to_trash_at: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.moved_to_trash_at is not None: body['moved_to_trash_at'] = self.moved_to_trash_at
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'DashboardOptions':
        return cls(moved_to_trash_at=d.get('moved_to_trash_at', None))


@dataclass
class DataSource:
    """A JSON object representing a DBSQL data source / SQL warehouse."""

    id: Optional[str] = None
    name: Optional[str] = None
    pause_reason: Optional[str] = None
    paused: Optional[int] = None
    supports_auto_limit: Optional[bool] = None
    syntax: Optional[str] = None
    type: Optional[str] = None
    view_only: Optional[bool] = None
    warehouse_id: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.id is not None: body['id'] = self.id
        if self.name is not None: body['name'] = self.name
        if self.pause_reason is not None: body['pause_reason'] = self.pause_reason
        if self.paused is not None: body['paused'] = self.paused
        if self.supports_auto_limit is not None: body['supports_auto_limit'] = self.supports_auto_limit
        if self.syntax is not None: body['syntax'] = self.syntax
        if self.type is not None: body['type'] = self.type
        if self.view_only is not None: body['view_only'] = self.view_only
        if self.warehouse_id is not None: body['warehouse_id'] = self.warehouse_id
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


class Disposition(Enum):
    """The fetch disposition provides two modes of fetching results: `INLINE` and `EXTERNAL_LINKS`.
    
    Statements executed with `INLINE` disposition will return result data inline, in `JSON_ARRAY`
    format, in a series of chunks. If a given statement produces a result set with a size larger
    than 25 MiB, that statement execution is aborted, and no result set will be available.
    
    **NOTE** Byte limits are computed based upon internal representations of the result set data,
    and might not match the sizes visible in JSON responses.
    
    Statements executed with `EXTERNAL_LINKS` disposition will return result data as external links:
    URLs that point to cloud storage internal to the workspace. Using `EXTERNAL_LINKS` disposition
    allows statements to generate arbitrarily sized result sets for fetching up to 100 GiB. The
    resulting links have two important properties:
    
    1. They point to resources _external_ to the Databricks compute; therefore any associated
    authentication information (typically a personal access token, OAuth token, or similar) _must be
    removed_ when fetching from these links.
    
    2. These are presigned URLs with a specific expiration, indicated in the response. The behavior
    when attempting to use an expired link is cloud specific."""

    EXTERNAL_LINKS = 'EXTERNAL_LINKS'
    INLINE = 'INLINE'


@dataclass
class EditAlert:
    name: str
    options: 'AlertOptions'
    query_id: str
    alert_id: Optional[str] = None
    rearm: Optional[int] = None

    def as_dict(self) -> dict:
        body = {}
        if self.alert_id is not None: body['alert_id'] = self.alert_id
        if self.name is not None: body['name'] = self.name
        if self.options: body['options'] = self.options.as_dict()
        if self.query_id is not None: body['query_id'] = self.query_id
        if self.rearm is not None: body['rearm'] = self.rearm
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'EditAlert':
        return cls(alert_id=d.get('alert_id', None),
                   name=d.get('name', None),
                   options=_from_dict(d, 'options', AlertOptions),
                   query_id=d.get('query_id', None),
                   rearm=d.get('rearm', None))


@dataclass
class EditWarehouseRequest:
    auto_stop_mins: Optional[int] = None
    channel: Optional['Channel'] = None
    cluster_size: Optional[str] = None
    creator_name: Optional[str] = None
    enable_photon: Optional[bool] = None
    enable_serverless_compute: Optional[bool] = None
    id: Optional[str] = None
    instance_profile_arn: Optional[str] = None
    max_num_clusters: Optional[int] = None
    min_num_clusters: Optional[int] = None
    name: Optional[str] = None
    spot_instance_policy: Optional['SpotInstancePolicy'] = None
    tags: Optional['EndpointTags'] = None
    warehouse_type: Optional['EditWarehouseRequestWarehouseType'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.auto_stop_mins is not None: body['auto_stop_mins'] = self.auto_stop_mins
        if self.channel: body['channel'] = self.channel.as_dict()
        if self.cluster_size is not None: body['cluster_size'] = self.cluster_size
        if self.creator_name is not None: body['creator_name'] = self.creator_name
        if self.enable_photon is not None: body['enable_photon'] = self.enable_photon
        if self.enable_serverless_compute is not None:
            body['enable_serverless_compute'] = self.enable_serverless_compute
        if self.id is not None: body['id'] = self.id
        if self.instance_profile_arn is not None: body['instance_profile_arn'] = self.instance_profile_arn
        if self.max_num_clusters is not None: body['max_num_clusters'] = self.max_num_clusters
        if self.min_num_clusters is not None: body['min_num_clusters'] = self.min_num_clusters
        if self.name is not None: body['name'] = self.name
        if self.spot_instance_policy is not None:
            body['spot_instance_policy'] = self.spot_instance_policy.value
        if self.tags: body['tags'] = self.tags.as_dict()
        if self.warehouse_type is not None: body['warehouse_type'] = self.warehouse_type.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'EditWarehouseRequest':
        return cls(auto_stop_mins=d.get('auto_stop_mins', None),
                   channel=_from_dict(d, 'channel', Channel),
                   cluster_size=d.get('cluster_size', None),
                   creator_name=d.get('creator_name', None),
                   enable_photon=d.get('enable_photon', None),
                   enable_serverless_compute=d.get('enable_serverless_compute', None),
                   id=d.get('id', None),
                   instance_profile_arn=d.get('instance_profile_arn', None),
                   max_num_clusters=d.get('max_num_clusters', None),
                   min_num_clusters=d.get('min_num_clusters', None),
                   name=d.get('name', None),
                   spot_instance_policy=_enum(d, 'spot_instance_policy', SpotInstancePolicy),
                   tags=_from_dict(d, 'tags', EndpointTags),
                   warehouse_type=_enum(d, 'warehouse_type', EditWarehouseRequestWarehouseType))


class EditWarehouseRequestWarehouseType(Enum):
    """Warehouse type: `PRO` or `CLASSIC`. If you want to use serverless compute, you must set to `PRO`
    and also set the field `enable_serverless_compute` to `true`."""

    CLASSIC = 'CLASSIC'
    PRO = 'PRO'
    TYPE_UNSPECIFIED = 'TYPE_UNSPECIFIED'


@dataclass
class EndpointConfPair:
    key: Optional[str] = None
    value: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.key is not None: body['key'] = self.key
        if self.value is not None: body['value'] = self.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'EndpointConfPair':
        return cls(key=d.get('key', None), value=d.get('value', None))


@dataclass
class EndpointHealth:
    details: Optional[str] = None
    failure_reason: Optional['TerminationReason'] = None
    message: Optional[str] = None
    status: Optional['Status'] = None
    summary: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.details is not None: body['details'] = self.details
        if self.failure_reason: body['failure_reason'] = self.failure_reason.as_dict()
        if self.message is not None: body['message'] = self.message
        if self.status is not None: body['status'] = self.status.value
        if self.summary is not None: body['summary'] = self.summary
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'EndpointHealth':
        return cls(details=d.get('details', None),
                   failure_reason=_from_dict(d, 'failure_reason', TerminationReason),
                   message=d.get('message', None),
                   status=_enum(d, 'status', Status),
                   summary=d.get('summary', None))


@dataclass
class EndpointInfo:
    auto_stop_mins: Optional[int] = None
    channel: Optional['Channel'] = None
    cluster_size: Optional[str] = None
    creator_name: Optional[str] = None
    enable_photon: Optional[bool] = None
    enable_serverless_compute: Optional[bool] = None
    health: Optional['EndpointHealth'] = None
    id: Optional[str] = None
    instance_profile_arn: Optional[str] = None
    jdbc_url: Optional[str] = None
    max_num_clusters: Optional[int] = None
    min_num_clusters: Optional[int] = None
    name: Optional[str] = None
    num_active_sessions: Optional[int] = None
    num_clusters: Optional[int] = None
    odbc_params: Optional['OdbcParams'] = None
    spot_instance_policy: Optional['SpotInstancePolicy'] = None
    state: Optional['State'] = None
    tags: Optional['EndpointTags'] = None
    warehouse_type: Optional['EndpointInfoWarehouseType'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.auto_stop_mins is not None: body['auto_stop_mins'] = self.auto_stop_mins
        if self.channel: body['channel'] = self.channel.as_dict()
        if self.cluster_size is not None: body['cluster_size'] = self.cluster_size
        if self.creator_name is not None: body['creator_name'] = self.creator_name
        if self.enable_photon is not None: body['enable_photon'] = self.enable_photon
        if self.enable_serverless_compute is not None:
            body['enable_serverless_compute'] = self.enable_serverless_compute
        if self.health: body['health'] = self.health.as_dict()
        if self.id is not None: body['id'] = self.id
        if self.instance_profile_arn is not None: body['instance_profile_arn'] = self.instance_profile_arn
        if self.jdbc_url is not None: body['jdbc_url'] = self.jdbc_url
        if self.max_num_clusters is not None: body['max_num_clusters'] = self.max_num_clusters
        if self.min_num_clusters is not None: body['min_num_clusters'] = self.min_num_clusters
        if self.name is not None: body['name'] = self.name
        if self.num_active_sessions is not None: body['num_active_sessions'] = self.num_active_sessions
        if self.num_clusters is not None: body['num_clusters'] = self.num_clusters
        if self.odbc_params: body['odbc_params'] = self.odbc_params.as_dict()
        if self.spot_instance_policy is not None:
            body['spot_instance_policy'] = self.spot_instance_policy.value
        if self.state is not None: body['state'] = self.state.value
        if self.tags: body['tags'] = self.tags.as_dict()
        if self.warehouse_type is not None: body['warehouse_type'] = self.warehouse_type.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'EndpointInfo':
        return cls(auto_stop_mins=d.get('auto_stop_mins', None),
                   channel=_from_dict(d, 'channel', Channel),
                   cluster_size=d.get('cluster_size', None),
                   creator_name=d.get('creator_name', None),
                   enable_photon=d.get('enable_photon', None),
                   enable_serverless_compute=d.get('enable_serverless_compute', None),
                   health=_from_dict(d, 'health', EndpointHealth),
                   id=d.get('id', None),
                   instance_profile_arn=d.get('instance_profile_arn', None),
                   jdbc_url=d.get('jdbc_url', None),
                   max_num_clusters=d.get('max_num_clusters', None),
                   min_num_clusters=d.get('min_num_clusters', None),
                   name=d.get('name', None),
                   num_active_sessions=d.get('num_active_sessions', None),
                   num_clusters=d.get('num_clusters', None),
                   odbc_params=_from_dict(d, 'odbc_params', OdbcParams),
                   spot_instance_policy=_enum(d, 'spot_instance_policy', SpotInstancePolicy),
                   state=_enum(d, 'state', State),
                   tags=_from_dict(d, 'tags', EndpointTags),
                   warehouse_type=_enum(d, 'warehouse_type', EndpointInfoWarehouseType))


class EndpointInfoWarehouseType(Enum):
    """Warehouse type: `PRO` or `CLASSIC`. If you want to use serverless compute, you must set to `PRO`
    and also set the field `enable_serverless_compute` to `true`."""

    CLASSIC = 'CLASSIC'
    PRO = 'PRO'
    TYPE_UNSPECIFIED = 'TYPE_UNSPECIFIED'


@dataclass
class EndpointTagPair:
    key: Optional[str] = None
    value: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.key is not None: body['key'] = self.key
        if self.value is not None: body['value'] = self.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'EndpointTagPair':
        return cls(key=d.get('key', None), value=d.get('value', None))


@dataclass
class EndpointTags:
    custom_tags: Optional['List[EndpointTagPair]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.custom_tags: body['custom_tags'] = [v.as_dict() for v in self.custom_tags]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'EndpointTags':
        return cls(custom_tags=_repeated(d, 'custom_tags', EndpointTagPair))


@dataclass
class ExecuteStatementRequest:
    statement: str
    warehouse_id: str
    byte_limit: Optional[int] = None
    catalog: Optional[str] = None
    disposition: Optional['Disposition'] = None
    format: Optional['Format'] = None
    on_wait_timeout: Optional['ExecuteStatementRequestOnWaitTimeout'] = None
    parameters: Optional['List[StatementParameterListItem]'] = None
    row_limit: Optional[int] = None
    schema: Optional[str] = None
    wait_timeout: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.byte_limit is not None: body['byte_limit'] = self.byte_limit
        if self.catalog is not None: body['catalog'] = self.catalog
        if self.disposition is not None: body['disposition'] = self.disposition.value
        if self.format is not None: body['format'] = self.format.value
        if self.on_wait_timeout is not None: body['on_wait_timeout'] = self.on_wait_timeout.value
        if self.parameters: body['parameters'] = [v.as_dict() for v in self.parameters]
        if self.row_limit is not None: body['row_limit'] = self.row_limit
        if self.schema is not None: body['schema'] = self.schema
        if self.statement is not None: body['statement'] = self.statement
        if self.wait_timeout is not None: body['wait_timeout'] = self.wait_timeout
        if self.warehouse_id is not None: body['warehouse_id'] = self.warehouse_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ExecuteStatementRequest':
        return cls(byte_limit=d.get('byte_limit', None),
                   catalog=d.get('catalog', None),
                   disposition=_enum(d, 'disposition', Disposition),
                   format=_enum(d, 'format', Format),
                   on_wait_timeout=_enum(d, 'on_wait_timeout', ExecuteStatementRequestOnWaitTimeout),
                   parameters=_repeated(d, 'parameters', StatementParameterListItem),
                   row_limit=d.get('row_limit', None),
                   schema=d.get('schema', None),
                   statement=d.get('statement', None),
                   wait_timeout=d.get('wait_timeout', None),
                   warehouse_id=d.get('warehouse_id', None))


class ExecuteStatementRequestOnWaitTimeout(Enum):
    """When `wait_timeout > 0s`, the call will block up to the specified time. If the statement
    execution doesn't finish within this time, `on_wait_timeout` determines whether the execution
    should continue or be canceled. When set to `CONTINUE`, the statement execution continues
    asynchronously and the call returns a statement ID which can be used for polling with
    :method:statementexecution/getStatement. When set to `CANCEL`, the statement execution is
    canceled and the call returns with a `CANCELED` state."""

    CANCEL = 'CANCEL'
    CONTINUE = 'CONTINUE'


@dataclass
class ExecuteStatementResponse:
    manifest: Optional['ResultManifest'] = None
    result: Optional['ResultData'] = None
    statement_id: Optional[str] = None
    status: Optional['StatementStatus'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.manifest: body['manifest'] = self.manifest.as_dict()
        if self.result: body['result'] = self.result.as_dict()
        if self.statement_id is not None: body['statement_id'] = self.statement_id
        if self.status: body['status'] = self.status.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ExecuteStatementResponse':
        return cls(manifest=_from_dict(d, 'manifest', ResultManifest),
                   result=_from_dict(d, 'result', ResultData),
                   statement_id=d.get('statement_id', None),
                   status=_from_dict(d, 'status', StatementStatus))


@dataclass
class ExternalLink:
    byte_count: Optional[int] = None
    chunk_index: Optional[int] = None
    expiration: Optional[str] = None
    external_link: Optional[str] = None
    next_chunk_index: Optional[int] = None
    next_chunk_internal_link: Optional[str] = None
    row_count: Optional[int] = None
    row_offset: Optional[int] = None

    def as_dict(self) -> dict:
        body = {}
        if self.byte_count is not None: body['byte_count'] = self.byte_count
        if self.chunk_index is not None: body['chunk_index'] = self.chunk_index
        if self.expiration is not None: body['expiration'] = self.expiration
        if self.external_link is not None: body['external_link'] = self.external_link
        if self.next_chunk_index is not None: body['next_chunk_index'] = self.next_chunk_index
        if self.next_chunk_internal_link is not None:
            body['next_chunk_internal_link'] = self.next_chunk_internal_link
        if self.row_count is not None: body['row_count'] = self.row_count
        if self.row_offset is not None: body['row_offset'] = self.row_offset
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

    ARROW_STREAM = 'ARROW_STREAM'
    CSV = 'CSV'
    JSON_ARRAY = 'JSON_ARRAY'


@dataclass
class GetResponse:
    access_control_list: Optional['List[AccessControl]'] = None
    object_id: Optional[str] = None
    object_type: Optional['ObjectType'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.access_control_list:
            body['access_control_list'] = [v.as_dict() for v in self.access_control_list]
        if self.object_id is not None: body['object_id'] = self.object_id
        if self.object_type is not None: body['object_type'] = self.object_type.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetResponse':
        return cls(access_control_list=_repeated(d, 'access_control_list', AccessControl),
                   object_id=d.get('object_id', None),
                   object_type=_enum(d, 'object_type', ObjectType))


@dataclass
class GetStatementResponse:
    manifest: Optional['ResultManifest'] = None
    result: Optional['ResultData'] = None
    statement_id: Optional[str] = None
    status: Optional['StatementStatus'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.manifest: body['manifest'] = self.manifest.as_dict()
        if self.result: body['result'] = self.result.as_dict()
        if self.statement_id is not None: body['statement_id'] = self.statement_id
        if self.status: body['status'] = self.status.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetStatementResponse':
        return cls(manifest=_from_dict(d, 'manifest', ResultManifest),
                   result=_from_dict(d, 'result', ResultData),
                   statement_id=d.get('statement_id', None),
                   status=_from_dict(d, 'status', StatementStatus))


@dataclass
class GetWarehousePermissionLevelsResponse:
    permission_levels: Optional['List[WarehousePermissionsDescription]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.permission_levels: body['permission_levels'] = [v.as_dict() for v in self.permission_levels]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetWarehousePermissionLevelsResponse':
        return cls(permission_levels=_repeated(d, 'permission_levels', WarehousePermissionsDescription))


@dataclass
class GetWarehouseResponse:
    auto_stop_mins: Optional[int] = None
    channel: Optional['Channel'] = None
    cluster_size: Optional[str] = None
    creator_name: Optional[str] = None
    enable_photon: Optional[bool] = None
    enable_serverless_compute: Optional[bool] = None
    health: Optional['EndpointHealth'] = None
    id: Optional[str] = None
    instance_profile_arn: Optional[str] = None
    jdbc_url: Optional[str] = None
    max_num_clusters: Optional[int] = None
    min_num_clusters: Optional[int] = None
    name: Optional[str] = None
    num_active_sessions: Optional[int] = None
    num_clusters: Optional[int] = None
    odbc_params: Optional['OdbcParams'] = None
    spot_instance_policy: Optional['SpotInstancePolicy'] = None
    state: Optional['State'] = None
    tags: Optional['EndpointTags'] = None
    warehouse_type: Optional['GetWarehouseResponseWarehouseType'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.auto_stop_mins is not None: body['auto_stop_mins'] = self.auto_stop_mins
        if self.channel: body['channel'] = self.channel.as_dict()
        if self.cluster_size is not None: body['cluster_size'] = self.cluster_size
        if self.creator_name is not None: body['creator_name'] = self.creator_name
        if self.enable_photon is not None: body['enable_photon'] = self.enable_photon
        if self.enable_serverless_compute is not None:
            body['enable_serverless_compute'] = self.enable_serverless_compute
        if self.health: body['health'] = self.health.as_dict()
        if self.id is not None: body['id'] = self.id
        if self.instance_profile_arn is not None: body['instance_profile_arn'] = self.instance_profile_arn
        if self.jdbc_url is not None: body['jdbc_url'] = self.jdbc_url
        if self.max_num_clusters is not None: body['max_num_clusters'] = self.max_num_clusters
        if self.min_num_clusters is not None: body['min_num_clusters'] = self.min_num_clusters
        if self.name is not None: body['name'] = self.name
        if self.num_active_sessions is not None: body['num_active_sessions'] = self.num_active_sessions
        if self.num_clusters is not None: body['num_clusters'] = self.num_clusters
        if self.odbc_params: body['odbc_params'] = self.odbc_params.as_dict()
        if self.spot_instance_policy is not None:
            body['spot_instance_policy'] = self.spot_instance_policy.value
        if self.state is not None: body['state'] = self.state.value
        if self.tags: body['tags'] = self.tags.as_dict()
        if self.warehouse_type is not None: body['warehouse_type'] = self.warehouse_type.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetWarehouseResponse':
        return cls(auto_stop_mins=d.get('auto_stop_mins', None),
                   channel=_from_dict(d, 'channel', Channel),
                   cluster_size=d.get('cluster_size', None),
                   creator_name=d.get('creator_name', None),
                   enable_photon=d.get('enable_photon', None),
                   enable_serverless_compute=d.get('enable_serverless_compute', None),
                   health=_from_dict(d, 'health', EndpointHealth),
                   id=d.get('id', None),
                   instance_profile_arn=d.get('instance_profile_arn', None),
                   jdbc_url=d.get('jdbc_url', None),
                   max_num_clusters=d.get('max_num_clusters', None),
                   min_num_clusters=d.get('min_num_clusters', None),
                   name=d.get('name', None),
                   num_active_sessions=d.get('num_active_sessions', None),
                   num_clusters=d.get('num_clusters', None),
                   odbc_params=_from_dict(d, 'odbc_params', OdbcParams),
                   spot_instance_policy=_enum(d, 'spot_instance_policy', SpotInstancePolicy),
                   state=_enum(d, 'state', State),
                   tags=_from_dict(d, 'tags', EndpointTags),
                   warehouse_type=_enum(d, 'warehouse_type', GetWarehouseResponseWarehouseType))


class GetWarehouseResponseWarehouseType(Enum):
    """Warehouse type: `PRO` or `CLASSIC`. If you want to use serverless compute, you must set to `PRO`
    and also set the field `enable_serverless_compute` to `true`."""

    CLASSIC = 'CLASSIC'
    PRO = 'PRO'
    TYPE_UNSPECIFIED = 'TYPE_UNSPECIFIED'


@dataclass
class GetWorkspaceWarehouseConfigResponse:
    channel: Optional['Channel'] = None
    config_param: Optional['RepeatedEndpointConfPairs'] = None
    data_access_config: Optional['List[EndpointConfPair]'] = None
    enabled_warehouse_types: Optional['List[WarehouseTypePair]'] = None
    global_param: Optional['RepeatedEndpointConfPairs'] = None
    google_service_account: Optional[str] = None
    instance_profile_arn: Optional[str] = None
    security_policy: Optional['GetWorkspaceWarehouseConfigResponseSecurityPolicy'] = None
    sql_configuration_parameters: Optional['RepeatedEndpointConfPairs'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.channel: body['channel'] = self.channel.as_dict()
        if self.config_param: body['config_param'] = self.config_param.as_dict()
        if self.data_access_config:
            body['data_access_config'] = [v.as_dict() for v in self.data_access_config]
        if self.enabled_warehouse_types:
            body['enabled_warehouse_types'] = [v.as_dict() for v in self.enabled_warehouse_types]
        if self.global_param: body['global_param'] = self.global_param.as_dict()
        if self.google_service_account is not None:
            body['google_service_account'] = self.google_service_account
        if self.instance_profile_arn is not None: body['instance_profile_arn'] = self.instance_profile_arn
        if self.security_policy is not None: body['security_policy'] = self.security_policy.value
        if self.sql_configuration_parameters:
            body['sql_configuration_parameters'] = self.sql_configuration_parameters.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetWorkspaceWarehouseConfigResponse':
        return cls(channel=_from_dict(d, 'channel', Channel),
                   config_param=_from_dict(d, 'config_param', RepeatedEndpointConfPairs),
                   data_access_config=_repeated(d, 'data_access_config', EndpointConfPair),
                   enabled_warehouse_types=_repeated(d, 'enabled_warehouse_types', WarehouseTypePair),
                   global_param=_from_dict(d, 'global_param', RepeatedEndpointConfPairs),
                   google_service_account=d.get('google_service_account', None),
                   instance_profile_arn=d.get('instance_profile_arn', None),
                   security_policy=_enum(d, 'security_policy',
                                         GetWorkspaceWarehouseConfigResponseSecurityPolicy),
                   sql_configuration_parameters=_from_dict(d, 'sql_configuration_parameters',
                                                           RepeatedEndpointConfPairs))


class GetWorkspaceWarehouseConfigResponseSecurityPolicy(Enum):
    """Security policy for warehouses"""

    DATA_ACCESS_CONTROL = 'DATA_ACCESS_CONTROL'
    NONE = 'NONE'
    PASSTHROUGH = 'PASSTHROUGH'


class ListOrder(Enum):

    CREATED_AT = 'created_at'
    NAME = 'name'


@dataclass
class ListQueriesResponse:
    has_next_page: Optional[bool] = None
    next_page_token: Optional[str] = None
    res: Optional['List[QueryInfo]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.has_next_page is not None: body['has_next_page'] = self.has_next_page
        if self.next_page_token is not None: body['next_page_token'] = self.next_page_token
        if self.res: body['res'] = [v.as_dict() for v in self.res]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListQueriesResponse':
        return cls(has_next_page=d.get('has_next_page', None),
                   next_page_token=d.get('next_page_token', None),
                   res=_repeated(d, 'res', QueryInfo))


@dataclass
class ListResponse:
    count: Optional[int] = None
    page: Optional[int] = None
    page_size: Optional[int] = None
    results: Optional['List[Dashboard]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.count is not None: body['count'] = self.count
        if self.page is not None: body['page'] = self.page
        if self.page_size is not None: body['page_size'] = self.page_size
        if self.results: body['results'] = [v.as_dict() for v in self.results]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListResponse':
        return cls(count=d.get('count', None),
                   page=d.get('page', None),
                   page_size=d.get('page_size', None),
                   results=_repeated(d, 'results', Dashboard))


@dataclass
class ListWarehousesResponse:
    warehouses: Optional['List[EndpointInfo]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.warehouses: body['warehouses'] = [v.as_dict() for v in self.warehouses]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListWarehousesResponse':
        return cls(warehouses=_repeated(d, 'warehouses', EndpointInfo))


class ObjectType(Enum):
    """A singular noun object type."""

    ALERT = 'alert'
    DASHBOARD = 'dashboard'
    DATA_SOURCE = 'data_source'
    QUERY = 'query'


class ObjectTypePlural(Enum):
    """Always a plural of the object type."""

    ALERTS = 'alerts'
    DASHBOARDS = 'dashboards'
    DATA_SOURCES = 'data_sources'
    QUERIES = 'queries'


@dataclass
class OdbcParams:
    hostname: Optional[str] = None
    path: Optional[str] = None
    port: Optional[int] = None
    protocol: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.hostname is not None: body['hostname'] = self.hostname
        if self.path is not None: body['path'] = self.path
        if self.port is not None: body['port'] = self.port
        if self.protocol is not None: body['protocol'] = self.protocol
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'OdbcParams':
        return cls(hostname=d.get('hostname', None),
                   path=d.get('path', None),
                   port=d.get('port', None),
                   protocol=d.get('protocol', None))


class OwnableObjectType(Enum):
    """The singular form of the type of object which can be owned."""

    ALERT = 'alert'
    DASHBOARD = 'dashboard'
    QUERY = 'query'


@dataclass
class Parameter:
    name: Optional[str] = None
    title: Optional[str] = None
    type: Optional['ParameterType'] = None
    value: Optional[Any] = None

    def as_dict(self) -> dict:
        body = {}
        if self.name is not None: body['name'] = self.name
        if self.title is not None: body['title'] = self.title
        if self.type is not None: body['type'] = self.type.value
        if self.value: body['value'] = self.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Parameter':
        return cls(name=d.get('name', None),
                   title=d.get('title', None),
                   type=_enum(d, 'type', ParameterType),
                   value=d.get('value', None))


class ParameterType(Enum):
    """Parameters can have several different types."""

    DATETIME = 'datetime'
    NUMBER = 'number'
    TEXT = 'text'


class PermissionLevel(Enum):
    """* `CAN_VIEW`: Can view the query * `CAN_RUN`: Can run the query * `CAN_MANAGE`: Can manage the
    query"""

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
    can_edit: Optional[bool] = None
    created_at: Optional[str] = None
    data_source_id: Optional[str] = None
    description: Optional[str] = None
    id: Optional[str] = None
    is_archived: Optional[bool] = None
    is_draft: Optional[bool] = None
    is_favorite: Optional[bool] = None
    is_safe: Optional[bool] = None
    last_modified_by: Optional['User'] = None
    last_modified_by_id: Optional[int] = None
    latest_query_data_id: Optional[str] = None
    name: Optional[str] = None
    options: Optional['QueryOptions'] = None
    parent: Optional[str] = None
    permission_tier: Optional['PermissionLevel'] = None
    query: Optional[str] = None
    query_hash: Optional[str] = None
    run_as_role: Optional['RunAsRole'] = None
    tags: Optional['List[str]'] = None
    updated_at: Optional[str] = None
    user: Optional['User'] = None
    user_id: Optional[int] = None
    visualizations: Optional['List[Visualization]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.can_edit is not None: body['can_edit'] = self.can_edit
        if self.created_at is not None: body['created_at'] = self.created_at
        if self.data_source_id is not None: body['data_source_id'] = self.data_source_id
        if self.description is not None: body['description'] = self.description
        if self.id is not None: body['id'] = self.id
        if self.is_archived is not None: body['is_archived'] = self.is_archived
        if self.is_draft is not None: body['is_draft'] = self.is_draft
        if self.is_favorite is not None: body['is_favorite'] = self.is_favorite
        if self.is_safe is not None: body['is_safe'] = self.is_safe
        if self.last_modified_by: body['last_modified_by'] = self.last_modified_by.as_dict()
        if self.last_modified_by_id is not None: body['last_modified_by_id'] = self.last_modified_by_id
        if self.latest_query_data_id is not None: body['latest_query_data_id'] = self.latest_query_data_id
        if self.name is not None: body['name'] = self.name
        if self.options: body['options'] = self.options.as_dict()
        if self.parent is not None: body['parent'] = self.parent
        if self.permission_tier is not None: body['permission_tier'] = self.permission_tier.value
        if self.query is not None: body['query'] = self.query
        if self.query_hash is not None: body['query_hash'] = self.query_hash
        if self.run_as_role is not None: body['run_as_role'] = self.run_as_role.value
        if self.tags: body['tags'] = [v for v in self.tags]
        if self.updated_at is not None: body['updated_at'] = self.updated_at
        if self.user: body['user'] = self.user.as_dict()
        if self.user_id is not None: body['user_id'] = self.user_id
        if self.visualizations: body['visualizations'] = [v.as_dict() for v in self.visualizations]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Query':
        return cls(can_edit=d.get('can_edit', None),
                   created_at=d.get('created_at', None),
                   data_source_id=d.get('data_source_id', None),
                   description=d.get('description', None),
                   id=d.get('id', None),
                   is_archived=d.get('is_archived', None),
                   is_draft=d.get('is_draft', None),
                   is_favorite=d.get('is_favorite', None),
                   is_safe=d.get('is_safe', None),
                   last_modified_by=_from_dict(d, 'last_modified_by', User),
                   last_modified_by_id=d.get('last_modified_by_id', None),
                   latest_query_data_id=d.get('latest_query_data_id', None),
                   name=d.get('name', None),
                   options=_from_dict(d, 'options', QueryOptions),
                   parent=d.get('parent', None),
                   permission_tier=_enum(d, 'permission_tier', PermissionLevel),
                   query=d.get('query', None),
                   query_hash=d.get('query_hash', None),
                   run_as_role=_enum(d, 'run_as_role', RunAsRole),
                   tags=d.get('tags', None),
                   updated_at=d.get('updated_at', None),
                   user=_from_dict(d, 'user', User),
                   user_id=d.get('user_id', None),
                   visualizations=_repeated(d, 'visualizations', Visualization))


@dataclass
class QueryEditContent:
    data_source_id: Optional[str] = None
    description: Optional[str] = None
    name: Optional[str] = None
    options: Optional[Any] = None
    query: Optional[str] = None
    query_id: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.data_source_id is not None: body['data_source_id'] = self.data_source_id
        if self.description is not None: body['description'] = self.description
        if self.name is not None: body['name'] = self.name
        if self.options: body['options'] = self.options
        if self.query is not None: body['query'] = self.query
        if self.query_id is not None: body['query_id'] = self.query_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'QueryEditContent':
        return cls(data_source_id=d.get('data_source_id', None),
                   description=d.get('description', None),
                   name=d.get('name', None),
                   options=d.get('options', None),
                   query=d.get('query', None),
                   query_id=d.get('query_id', None))


@dataclass
class QueryFilter:
    """A filter to limit query history results. This field is optional."""

    query_start_time_range: Optional['TimeRange'] = None
    statuses: Optional['List[QueryStatus]'] = None
    user_ids: Optional['List[int]'] = None
    warehouse_ids: Optional['List[str]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.query_start_time_range: body['query_start_time_range'] = self.query_start_time_range.as_dict()
        if self.statuses: body['statuses'] = [v.value for v in self.statuses]
        if self.user_ids: body['user_ids'] = [v for v in self.user_ids]
        if self.warehouse_ids: body['warehouse_ids'] = [v for v in self.warehouse_ids]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'QueryFilter':
        return cls(query_start_time_range=_from_dict(d, 'query_start_time_range', TimeRange),
                   statuses=d.get('statuses', None),
                   user_ids=d.get('user_ids', None),
                   warehouse_ids=d.get('warehouse_ids', None))


@dataclass
class QueryInfo:
    can_subscribe_to_live_query: Optional[bool] = None
    channel_used: Optional['ChannelInfo'] = None
    duration: Optional[int] = None
    endpoint_id: Optional[str] = None
    error_message: Optional[str] = None
    executed_as_user_id: Optional[int] = None
    executed_as_user_name: Optional[str] = None
    execution_end_time_ms: Optional[int] = None
    is_final: Optional[bool] = None
    lookup_key: Optional[str] = None
    metrics: Optional['QueryMetrics'] = None
    plans_state: Optional['PlansState'] = None
    query_end_time_ms: Optional[int] = None
    query_id: Optional[str] = None
    query_start_time_ms: Optional[int] = None
    query_text: Optional[str] = None
    rows_produced: Optional[int] = None
    spark_ui_url: Optional[str] = None
    statement_type: Optional['QueryStatementType'] = None
    status: Optional['QueryStatus'] = None
    user_id: Optional[int] = None
    user_name: Optional[str] = None
    warehouse_id: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.can_subscribe_to_live_query is not None:
            body['canSubscribeToLiveQuery'] = self.can_subscribe_to_live_query
        if self.channel_used: body['channel_used'] = self.channel_used.as_dict()
        if self.duration is not None: body['duration'] = self.duration
        if self.endpoint_id is not None: body['endpoint_id'] = self.endpoint_id
        if self.error_message is not None: body['error_message'] = self.error_message
        if self.executed_as_user_id is not None: body['executed_as_user_id'] = self.executed_as_user_id
        if self.executed_as_user_name is not None: body['executed_as_user_name'] = self.executed_as_user_name
        if self.execution_end_time_ms is not None: body['execution_end_time_ms'] = self.execution_end_time_ms
        if self.is_final is not None: body['is_final'] = self.is_final
        if self.lookup_key is not None: body['lookup_key'] = self.lookup_key
        if self.metrics: body['metrics'] = self.metrics.as_dict()
        if self.plans_state is not None: body['plans_state'] = self.plans_state.value
        if self.query_end_time_ms is not None: body['query_end_time_ms'] = self.query_end_time_ms
        if self.query_id is not None: body['query_id'] = self.query_id
        if self.query_start_time_ms is not None: body['query_start_time_ms'] = self.query_start_time_ms
        if self.query_text is not None: body['query_text'] = self.query_text
        if self.rows_produced is not None: body['rows_produced'] = self.rows_produced
        if self.spark_ui_url is not None: body['spark_ui_url'] = self.spark_ui_url
        if self.statement_type is not None: body['statement_type'] = self.statement_type.value
        if self.status is not None: body['status'] = self.status.value
        if self.user_id is not None: body['user_id'] = self.user_id
        if self.user_name is not None: body['user_name'] = self.user_name
        if self.warehouse_id is not None: body['warehouse_id'] = self.warehouse_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'QueryInfo':
        return cls(can_subscribe_to_live_query=d.get('canSubscribeToLiveQuery', None),
                   channel_used=_from_dict(d, 'channel_used', ChannelInfo),
                   duration=d.get('duration', None),
                   endpoint_id=d.get('endpoint_id', None),
                   error_message=d.get('error_message', None),
                   executed_as_user_id=d.get('executed_as_user_id', None),
                   executed_as_user_name=d.get('executed_as_user_name', None),
                   execution_end_time_ms=d.get('execution_end_time_ms', None),
                   is_final=d.get('is_final', None),
                   lookup_key=d.get('lookup_key', None),
                   metrics=_from_dict(d, 'metrics', QueryMetrics),
                   plans_state=_enum(d, 'plans_state', PlansState),
                   query_end_time_ms=d.get('query_end_time_ms', None),
                   query_id=d.get('query_id', None),
                   query_start_time_ms=d.get('query_start_time_ms', None),
                   query_text=d.get('query_text', None),
                   rows_produced=d.get('rows_produced', None),
                   spark_ui_url=d.get('spark_ui_url', None),
                   statement_type=_enum(d, 'statement_type', QueryStatementType),
                   status=_enum(d, 'status', QueryStatus),
                   user_id=d.get('user_id', None),
                   user_name=d.get('user_name', None),
                   warehouse_id=d.get('warehouse_id', None))


@dataclass
class QueryList:
    count: Optional[int] = None
    page: Optional[int] = None
    page_size: Optional[int] = None
    results: Optional['List[Query]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.count is not None: body['count'] = self.count
        if self.page is not None: body['page'] = self.page
        if self.page_size is not None: body['page_size'] = self.page_size
        if self.results: body['results'] = [v.as_dict() for v in self.results]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'QueryList':
        return cls(count=d.get('count', None),
                   page=d.get('page', None),
                   page_size=d.get('page_size', None),
                   results=_repeated(d, 'results', Query))


@dataclass
class QueryMetrics:
    """Metrics about query execution."""

    compilation_time_ms: Optional[int] = None
    execution_time_ms: Optional[int] = None
    metadata_time_ms: Optional[int] = None
    network_sent_bytes: Optional[int] = None
    overloading_queue_start_timestamp: Optional[int] = None
    photon_total_time_ms: Optional[int] = None
    planning_phases: Optional['List[Any]'] = None
    planning_time_ms: Optional[int] = None
    provisioning_queue_start_timestamp: Optional[int] = None
    pruned_bytes: Optional[int] = None
    pruned_files_count: Optional[int] = None
    query_compilation_start_timestamp: Optional[int] = None
    query_execution_time_ms: Optional[int] = None
    read_bytes: Optional[int] = None
    read_cache_bytes: Optional[int] = None
    read_files_count: Optional[int] = None
    read_partitions_count: Optional[int] = None
    read_remote_bytes: Optional[int] = None
    result_fetch_time_ms: Optional[int] = None
    result_from_cache: Optional[bool] = None
    rows_produced_count: Optional[int] = None
    rows_read_count: Optional[int] = None
    spill_to_disk_bytes: Optional[int] = None
    task_total_time_ms: Optional[int] = None
    total_time_ms: Optional[int] = None
    write_remote_bytes: Optional[int] = None

    def as_dict(self) -> dict:
        body = {}
        if self.compilation_time_ms is not None: body['compilation_time_ms'] = self.compilation_time_ms
        if self.execution_time_ms is not None: body['execution_time_ms'] = self.execution_time_ms
        if self.metadata_time_ms is not None: body['metadata_time_ms'] = self.metadata_time_ms
        if self.network_sent_bytes is not None: body['network_sent_bytes'] = self.network_sent_bytes
        if self.overloading_queue_start_timestamp is not None:
            body['overloading_queue_start_timestamp'] = self.overloading_queue_start_timestamp
        if self.photon_total_time_ms is not None: body['photon_total_time_ms'] = self.photon_total_time_ms
        if self.planning_phases: body['planning_phases'] = [v for v in self.planning_phases]
        if self.planning_time_ms is not None: body['planning_time_ms'] = self.planning_time_ms
        if self.provisioning_queue_start_timestamp is not None:
            body['provisioning_queue_start_timestamp'] = self.provisioning_queue_start_timestamp
        if self.pruned_bytes is not None: body['pruned_bytes'] = self.pruned_bytes
        if self.pruned_files_count is not None: body['pruned_files_count'] = self.pruned_files_count
        if self.query_compilation_start_timestamp is not None:
            body['query_compilation_start_timestamp'] = self.query_compilation_start_timestamp
        if self.query_execution_time_ms is not None:
            body['query_execution_time_ms'] = self.query_execution_time_ms
        if self.read_bytes is not None: body['read_bytes'] = self.read_bytes
        if self.read_cache_bytes is not None: body['read_cache_bytes'] = self.read_cache_bytes
        if self.read_files_count is not None: body['read_files_count'] = self.read_files_count
        if self.read_partitions_count is not None: body['read_partitions_count'] = self.read_partitions_count
        if self.read_remote_bytes is not None: body['read_remote_bytes'] = self.read_remote_bytes
        if self.result_fetch_time_ms is not None: body['result_fetch_time_ms'] = self.result_fetch_time_ms
        if self.result_from_cache is not None: body['result_from_cache'] = self.result_from_cache
        if self.rows_produced_count is not None: body['rows_produced_count'] = self.rows_produced_count
        if self.rows_read_count is not None: body['rows_read_count'] = self.rows_read_count
        if self.spill_to_disk_bytes is not None: body['spill_to_disk_bytes'] = self.spill_to_disk_bytes
        if self.task_total_time_ms is not None: body['task_total_time_ms'] = self.task_total_time_ms
        if self.total_time_ms is not None: body['total_time_ms'] = self.total_time_ms
        if self.write_remote_bytes is not None: body['write_remote_bytes'] = self.write_remote_bytes
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'QueryMetrics':
        return cls(compilation_time_ms=d.get('compilation_time_ms', None),
                   execution_time_ms=d.get('execution_time_ms', None),
                   metadata_time_ms=d.get('metadata_time_ms', None),
                   network_sent_bytes=d.get('network_sent_bytes', None),
                   overloading_queue_start_timestamp=d.get('overloading_queue_start_timestamp', None),
                   photon_total_time_ms=d.get('photon_total_time_ms', None),
                   planning_phases=d.get('planning_phases', None),
                   planning_time_ms=d.get('planning_time_ms', None),
                   provisioning_queue_start_timestamp=d.get('provisioning_queue_start_timestamp', None),
                   pruned_bytes=d.get('pruned_bytes', None),
                   pruned_files_count=d.get('pruned_files_count', None),
                   query_compilation_start_timestamp=d.get('query_compilation_start_timestamp', None),
                   query_execution_time_ms=d.get('query_execution_time_ms', None),
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
                   total_time_ms=d.get('total_time_ms', None),
                   write_remote_bytes=d.get('write_remote_bytes', None))


@dataclass
class QueryOptions:
    moved_to_trash_at: Optional[str] = None
    parameters: Optional['List[Parameter]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.moved_to_trash_at is not None: body['moved_to_trash_at'] = self.moved_to_trash_at
        if self.parameters: body['parameters'] = [v.as_dict() for v in self.parameters]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'QueryOptions':
        return cls(moved_to_trash_at=d.get('moved_to_trash_at', None),
                   parameters=_repeated(d, 'parameters', Parameter))


@dataclass
class QueryPostContent:
    data_source_id: Optional[str] = None
    description: Optional[str] = None
    name: Optional[str] = None
    options: Optional[Any] = None
    parent: Optional[str] = None
    query: Optional[str] = None
    run_as_role: Optional['RunAsRole'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.data_source_id is not None: body['data_source_id'] = self.data_source_id
        if self.description is not None: body['description'] = self.description
        if self.name is not None: body['name'] = self.name
        if self.options: body['options'] = self.options
        if self.parent is not None: body['parent'] = self.parent
        if self.query is not None: body['query'] = self.query
        if self.run_as_role is not None: body['run_as_role'] = self.run_as_role.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'QueryPostContent':
        return cls(data_source_id=d.get('data_source_id', None),
                   description=d.get('description', None),
                   name=d.get('name', None),
                   options=d.get('options', None),
                   parent=d.get('parent', None),
                   query=d.get('query', None),
                   run_as_role=_enum(d, 'run_as_role', RunAsRole))


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
    """Query status with one the following values: * `QUEUED`: Query has been received and queued. *
    `RUNNING`: Query has started. * `CANCELED`: Query has been cancelled by the user. * `FAILED`:
    Query has failed. * `FINISHED`: Query has completed."""

    CANCELED = 'CANCELED'
    FAILED = 'FAILED'
    FINISHED = 'FINISHED'
    QUEUED = 'QUEUED'
    RUNNING = 'RUNNING'


@dataclass
class RepeatedEndpointConfPairs:
    config_pair: Optional['List[EndpointConfPair]'] = None
    configuration_pairs: Optional['List[EndpointConfPair]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.config_pair: body['config_pair'] = [v.as_dict() for v in self.config_pair]
        if self.configuration_pairs:
            body['configuration_pairs'] = [v.as_dict() for v in self.configuration_pairs]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'RepeatedEndpointConfPairs':
        return cls(config_pair=_repeated(d, 'config_pair', EndpointConfPair),
                   configuration_pairs=_repeated(d, 'configuration_pairs', EndpointConfPair))


@dataclass
class ResultData:
    """Contains the result data of a single chunk when using `INLINE` disposition. When using
    `EXTERNAL_LINKS` disposition, the array `external_links` is used instead to provide presigned
    URLs to the result data in cloud storage. Exactly one of these alternatives is used. (While the
    `external_links` array prepares the API to return multiple links in a single response. Currently
    only a single link is returned.)"""

    byte_count: Optional[int] = None
    chunk_index: Optional[int] = None
    data_array: Optional['List[List[str]]'] = None
    external_links: Optional['List[ExternalLink]'] = None
    next_chunk_index: Optional[int] = None
    next_chunk_internal_link: Optional[str] = None
    row_count: Optional[int] = None
    row_offset: Optional[int] = None

    def as_dict(self) -> dict:
        body = {}
        if self.byte_count is not None: body['byte_count'] = self.byte_count
        if self.chunk_index is not None: body['chunk_index'] = self.chunk_index
        if self.data_array: body['data_array'] = [v for v in self.data_array]
        if self.external_links: body['external_links'] = [v.as_dict() for v in self.external_links]
        if self.next_chunk_index is not None: body['next_chunk_index'] = self.next_chunk_index
        if self.next_chunk_internal_link is not None:
            body['next_chunk_internal_link'] = self.next_chunk_internal_link
        if self.row_count is not None: body['row_count'] = self.row_count
        if self.row_offset is not None: body['row_offset'] = self.row_offset
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ResultData':
        return cls(byte_count=d.get('byte_count', None),
                   chunk_index=d.get('chunk_index', None),
                   data_array=d.get('data_array', None),
                   external_links=_repeated(d, 'external_links', ExternalLink),
                   next_chunk_index=d.get('next_chunk_index', None),
                   next_chunk_internal_link=d.get('next_chunk_internal_link', None),
                   row_count=d.get('row_count', None),
                   row_offset=d.get('row_offset', None))


@dataclass
class ResultManifest:
    """The result manifest provides schema and metadata for the result set."""

    chunks: Optional['List[BaseChunkInfo]'] = None
    format: Optional['Format'] = None
    schema: Optional['ResultSchema'] = None
    total_byte_count: Optional[int] = None
    total_chunk_count: Optional[int] = None
    total_row_count: Optional[int] = None
    truncated: Optional[bool] = None

    def as_dict(self) -> dict:
        body = {}
        if self.chunks: body['chunks'] = [v.as_dict() for v in self.chunks]
        if self.format is not None: body['format'] = self.format.value
        if self.schema: body['schema'] = self.schema.as_dict()
        if self.total_byte_count is not None: body['total_byte_count'] = self.total_byte_count
        if self.total_chunk_count is not None: body['total_chunk_count'] = self.total_chunk_count
        if self.total_row_count is not None: body['total_row_count'] = self.total_row_count
        if self.truncated is not None: body['truncated'] = self.truncated
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ResultManifest':
        return cls(chunks=_repeated(d, 'chunks', BaseChunkInfo),
                   format=_enum(d, 'format', Format),
                   schema=_from_dict(d, 'schema', ResultSchema),
                   total_byte_count=d.get('total_byte_count', None),
                   total_chunk_count=d.get('total_chunk_count', None),
                   total_row_count=d.get('total_row_count', None),
                   truncated=d.get('truncated', None))


@dataclass
class ResultSchema:
    """The schema is an ordered list of column descriptions."""

    column_count: Optional[int] = None
    columns: Optional['List[ColumnInfo]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.column_count is not None: body['column_count'] = self.column_count
        if self.columns: body['columns'] = [v.as_dict() for v in self.columns]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ResultSchema':
        return cls(column_count=d.get('column_count', None), columns=_repeated(d, 'columns', ColumnInfo))


class RunAsRole(Enum):
    """Run as role"""

    OWNER = 'owner'
    VIEWER = 'viewer'


@dataclass
class ServiceError:
    error_code: Optional['ServiceErrorCode'] = None
    message: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.error_code is not None: body['error_code'] = self.error_code.value
        if self.message is not None: body['message'] = self.message
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ServiceError':
        return cls(error_code=_enum(d, 'error_code', ServiceErrorCode), message=d.get('message', None))


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
class SetResponse:
    access_control_list: Optional['List[AccessControl]'] = None
    object_id: Optional[str] = None
    object_type: Optional['ObjectType'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.access_control_list:
            body['access_control_list'] = [v.as_dict() for v in self.access_control_list]
        if self.object_id is not None: body['object_id'] = self.object_id
        if self.object_type is not None: body['object_type'] = self.object_type.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'SetResponse':
        return cls(access_control_list=_repeated(d, 'access_control_list', AccessControl),
                   object_id=d.get('object_id', None),
                   object_type=_enum(d, 'object_type', ObjectType))


@dataclass
class SetWorkspaceWarehouseConfigRequest:
    channel: Optional['Channel'] = None
    config_param: Optional['RepeatedEndpointConfPairs'] = None
    data_access_config: Optional['List[EndpointConfPair]'] = None
    enabled_warehouse_types: Optional['List[WarehouseTypePair]'] = None
    global_param: Optional['RepeatedEndpointConfPairs'] = None
    google_service_account: Optional[str] = None
    instance_profile_arn: Optional[str] = None
    security_policy: Optional['SetWorkspaceWarehouseConfigRequestSecurityPolicy'] = None
    sql_configuration_parameters: Optional['RepeatedEndpointConfPairs'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.channel: body['channel'] = self.channel.as_dict()
        if self.config_param: body['config_param'] = self.config_param.as_dict()
        if self.data_access_config:
            body['data_access_config'] = [v.as_dict() for v in self.data_access_config]
        if self.enabled_warehouse_types:
            body['enabled_warehouse_types'] = [v.as_dict() for v in self.enabled_warehouse_types]
        if self.global_param: body['global_param'] = self.global_param.as_dict()
        if self.google_service_account is not None:
            body['google_service_account'] = self.google_service_account
        if self.instance_profile_arn is not None: body['instance_profile_arn'] = self.instance_profile_arn
        if self.security_policy is not None: body['security_policy'] = self.security_policy.value
        if self.sql_configuration_parameters:
            body['sql_configuration_parameters'] = self.sql_configuration_parameters.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'SetWorkspaceWarehouseConfigRequest':
        return cls(channel=_from_dict(d, 'channel', Channel),
                   config_param=_from_dict(d, 'config_param', RepeatedEndpointConfPairs),
                   data_access_config=_repeated(d, 'data_access_config', EndpointConfPair),
                   enabled_warehouse_types=_repeated(d, 'enabled_warehouse_types', WarehouseTypePair),
                   global_param=_from_dict(d, 'global_param', RepeatedEndpointConfPairs),
                   google_service_account=d.get('google_service_account', None),
                   instance_profile_arn=d.get('instance_profile_arn', None),
                   security_policy=_enum(d, 'security_policy',
                                         SetWorkspaceWarehouseConfigRequestSecurityPolicy),
                   sql_configuration_parameters=_from_dict(d, 'sql_configuration_parameters',
                                                           RepeatedEndpointConfPairs))


class SetWorkspaceWarehouseConfigRequestSecurityPolicy(Enum):
    """Security policy for warehouses"""

    DATA_ACCESS_CONTROL = 'DATA_ACCESS_CONTROL'
    NONE = 'NONE'
    PASSTHROUGH = 'PASSTHROUGH'


class SpotInstancePolicy(Enum):
    """Configurations whether the warehouse should use spot instances."""

    COST_OPTIMIZED = 'COST_OPTIMIZED'
    POLICY_UNSPECIFIED = 'POLICY_UNSPECIFIED'
    RELIABILITY_OPTIMIZED = 'RELIABILITY_OPTIMIZED'


class State(Enum):
    """State of the warehouse"""

    DELETED = 'DELETED'
    DELETING = 'DELETING'
    RUNNING = 'RUNNING'
    STARTING = 'STARTING'
    STOPPED = 'STOPPED'
    STOPPING = 'STOPPING'


@dataclass
class StatementParameterListItem:
    name: str
    type: Optional[str] = None
    value: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.name is not None: body['name'] = self.name
        if self.type is not None: body['type'] = self.type
        if self.value is not None: body['value'] = self.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'StatementParameterListItem':
        return cls(name=d.get('name', None), type=d.get('type', None), value=d.get('value', None))


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
    """The status response includes execution state and if relevant, error information."""

    error: Optional['ServiceError'] = None
    state: Optional['StatementState'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.error: body['error'] = self.error.as_dict()
        if self.state is not None: body['state'] = self.state.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'StatementStatus':
        return cls(error=_from_dict(d, 'error', ServiceError), state=_enum(d, 'state', StatementState))


class Status(Enum):
    """Health status of the warehouse."""

    DEGRADED = 'DEGRADED'
    FAILED = 'FAILED'
    HEALTHY = 'HEALTHY'
    STATUS_UNSPECIFIED = 'STATUS_UNSPECIFIED'


@dataclass
class Success:
    message: Optional['SuccessMessage'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.message is not None: body['message'] = self.message.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Success':
        return cls(message=_enum(d, 'message', SuccessMessage))


class SuccessMessage(Enum):

    SUCCESS = 'Success'


@dataclass
class TerminationReason:
    code: Optional['TerminationReasonCode'] = None
    parameters: Optional['Dict[str,str]'] = None
    type: Optional['TerminationReasonType'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.code is not None: body['code'] = self.code.value
        if self.parameters: body['parameters'] = self.parameters
        if self.type is not None: body['type'] = self.type.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'TerminationReason':
        return cls(code=_enum(d, 'code', TerminationReasonCode),
                   parameters=d.get('parameters', None),
                   type=_enum(d, 'type', TerminationReasonType))


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
    end_time_ms: Optional[int] = None
    start_time_ms: Optional[int] = None

    def as_dict(self) -> dict:
        body = {}
        if self.end_time_ms is not None: body['end_time_ms'] = self.end_time_ms
        if self.start_time_ms is not None: body['start_time_ms'] = self.start_time_ms
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'TimeRange':
        return cls(end_time_ms=d.get('end_time_ms', None), start_time_ms=d.get('start_time_ms', None))


@dataclass
class TransferOwnershipObjectId:
    new_owner: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.new_owner is not None: body['new_owner'] = self.new_owner
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'TransferOwnershipObjectId':
        return cls(new_owner=d.get('new_owner', None))


@dataclass
class User:
    email: Optional[str] = None
    id: Optional[int] = None
    name: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.email is not None: body['email'] = self.email
        if self.id is not None: body['id'] = self.id
        if self.name is not None: body['name'] = self.name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'User':
        return cls(email=d.get('email', None), id=d.get('id', None), name=d.get('name', None))


@dataclass
class Visualization:
    """The visualization description API changes frequently and is unsupported. You can duplicate a
    visualization by copying description objects received _from the API_ and then using them to
    create a new one with a POST request to the same endpoint. Databricks does not recommend
    constructing ad-hoc visualizations entirely in JSON."""

    created_at: Optional[str] = None
    description: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None
    options: Optional[Any] = None
    type: Optional[str] = None
    updated_at: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.created_at is not None: body['created_at'] = self.created_at
        if self.description is not None: body['description'] = self.description
        if self.id is not None: body['id'] = self.id
        if self.name is not None: body['name'] = self.name
        if self.options: body['options'] = self.options
        if self.type is not None: body['type'] = self.type
        if self.updated_at is not None: body['updated_at'] = self.updated_at
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


@dataclass
class WarehouseAccessControlRequest:
    group_name: Optional[str] = None
    permission_level: Optional['WarehousePermissionLevel'] = None
    service_principal_name: Optional[str] = None
    user_name: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.group_name is not None: body['group_name'] = self.group_name
        if self.permission_level is not None: body['permission_level'] = self.permission_level.value
        if self.service_principal_name is not None:
            body['service_principal_name'] = self.service_principal_name
        if self.user_name is not None: body['user_name'] = self.user_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'WarehouseAccessControlRequest':
        return cls(group_name=d.get('group_name', None),
                   permission_level=_enum(d, 'permission_level', WarehousePermissionLevel),
                   service_principal_name=d.get('service_principal_name', None),
                   user_name=d.get('user_name', None))


@dataclass
class WarehouseAccessControlResponse:
    all_permissions: Optional['List[WarehousePermission]'] = None
    display_name: Optional[str] = None
    group_name: Optional[str] = None
    service_principal_name: Optional[str] = None
    user_name: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.all_permissions: body['all_permissions'] = [v.as_dict() for v in self.all_permissions]
        if self.display_name is not None: body['display_name'] = self.display_name
        if self.group_name is not None: body['group_name'] = self.group_name
        if self.service_principal_name is not None:
            body['service_principal_name'] = self.service_principal_name
        if self.user_name is not None: body['user_name'] = self.user_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'WarehouseAccessControlResponse':
        return cls(all_permissions=_repeated(d, 'all_permissions', WarehousePermission),
                   display_name=d.get('display_name', None),
                   group_name=d.get('group_name', None),
                   service_principal_name=d.get('service_principal_name', None),
                   user_name=d.get('user_name', None))


@dataclass
class WarehousePermission:
    inherited: Optional[bool] = None
    inherited_from_object: Optional['List[str]'] = None
    permission_level: Optional['WarehousePermissionLevel'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.inherited is not None: body['inherited'] = self.inherited
        if self.inherited_from_object: body['inherited_from_object'] = [v for v in self.inherited_from_object]
        if self.permission_level is not None: body['permission_level'] = self.permission_level.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'WarehousePermission':
        return cls(inherited=d.get('inherited', None),
                   inherited_from_object=d.get('inherited_from_object', None),
                   permission_level=_enum(d, 'permission_level', WarehousePermissionLevel))


class WarehousePermissionLevel(Enum):
    """Permission level"""

    CAN_MANAGE = 'CAN_MANAGE'
    CAN_USE = 'CAN_USE'
    IS_OWNER = 'IS_OWNER'


@dataclass
class WarehousePermissions:
    access_control_list: Optional['List[WarehouseAccessControlResponse]'] = None
    object_id: Optional[str] = None
    object_type: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.access_control_list:
            body['access_control_list'] = [v.as_dict() for v in self.access_control_list]
        if self.object_id is not None: body['object_id'] = self.object_id
        if self.object_type is not None: body['object_type'] = self.object_type
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'WarehousePermissions':
        return cls(access_control_list=_repeated(d, 'access_control_list', WarehouseAccessControlResponse),
                   object_id=d.get('object_id', None),
                   object_type=d.get('object_type', None))


@dataclass
class WarehousePermissionsDescription:
    description: Optional[str] = None
    permission_level: Optional['WarehousePermissionLevel'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.description is not None: body['description'] = self.description
        if self.permission_level is not None: body['permission_level'] = self.permission_level.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'WarehousePermissionsDescription':
        return cls(description=d.get('description', None),
                   permission_level=_enum(d, 'permission_level', WarehousePermissionLevel))


@dataclass
class WarehousePermissionsRequest:
    access_control_list: Optional['List[WarehouseAccessControlRequest]'] = None
    warehouse_id: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.access_control_list:
            body['access_control_list'] = [v.as_dict() for v in self.access_control_list]
        if self.warehouse_id is not None: body['warehouse_id'] = self.warehouse_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'WarehousePermissionsRequest':
        return cls(access_control_list=_repeated(d, 'access_control_list', WarehouseAccessControlRequest),
                   warehouse_id=d.get('warehouse_id', None))


@dataclass
class WarehouseTypePair:
    enabled: Optional[bool] = None
    warehouse_type: Optional['WarehouseTypePairWarehouseType'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.enabled is not None: body['enabled'] = self.enabled
        if self.warehouse_type is not None: body['warehouse_type'] = self.warehouse_type.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'WarehouseTypePair':
        return cls(enabled=d.get('enabled', None),
                   warehouse_type=_enum(d, 'warehouse_type', WarehouseTypePairWarehouseType))


class WarehouseTypePairWarehouseType(Enum):
    """Warehouse type: `PRO` or `CLASSIC`."""

    CLASSIC = 'CLASSIC'
    PRO = 'PRO'
    TYPE_UNSPECIFIED = 'TYPE_UNSPECIFIED'


@dataclass
class Widget:
    id: Optional[str] = None
    options: Optional['WidgetOptions'] = None
    visualization: Optional['Visualization'] = None
    width: Optional[int] = None

    def as_dict(self) -> dict:
        body = {}
        if self.id is not None: body['id'] = self.id
        if self.options: body['options'] = self.options.as_dict()
        if self.visualization: body['visualization'] = self.visualization.as_dict()
        if self.width is not None: body['width'] = self.width
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Widget':
        return cls(id=d.get('id', None),
                   options=_from_dict(d, 'options', WidgetOptions),
                   visualization=_from_dict(d, 'visualization', Visualization),
                   width=d.get('width', None))


@dataclass
class WidgetOptions:
    created_at: Optional[str] = None
    description: Optional[str] = None
    is_hidden: Optional[bool] = None
    parameter_mappings: Optional[Any] = None
    position: Optional['WidgetPosition'] = None
    title: Optional[str] = None
    updated_at: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.created_at is not None: body['created_at'] = self.created_at
        if self.description is not None: body['description'] = self.description
        if self.is_hidden is not None: body['isHidden'] = self.is_hidden
        if self.parameter_mappings: body['parameterMappings'] = self.parameter_mappings
        if self.position: body['position'] = self.position.as_dict()
        if self.title is not None: body['title'] = self.title
        if self.updated_at is not None: body['updated_at'] = self.updated_at
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'WidgetOptions':
        return cls(created_at=d.get('created_at', None),
                   description=d.get('description', None),
                   is_hidden=d.get('isHidden', None),
                   parameter_mappings=d.get('parameterMappings', None),
                   position=_from_dict(d, 'position', WidgetPosition),
                   title=d.get('title', None),
                   updated_at=d.get('updated_at', None))


@dataclass
class WidgetPosition:
    """Coordinates of this widget on a dashboard. This portion of the API changes frequently and is
    unsupported."""

    auto_height: Optional[bool] = None
    col: Optional[int] = None
    row: Optional[int] = None
    size_x: Optional[int] = None
    size_y: Optional[int] = None

    def as_dict(self) -> dict:
        body = {}
        if self.auto_height is not None: body['autoHeight'] = self.auto_height
        if self.col is not None: body['col'] = self.col
        if self.row is not None: body['row'] = self.row
        if self.size_x is not None: body['sizeX'] = self.size_x
        if self.size_y is not None: body['sizeY'] = self.size_y
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'WidgetPosition':
        return cls(auto_height=d.get('autoHeight', None),
                   col=d.get('col', None),
                   row=d.get('row', None),
                   size_x=d.get('sizeX', None),
                   size_y=d.get('sizeY', None))


class AlertsAPI:
    """The alerts API can be used to perform CRUD operations on alerts. An alert is a Databricks SQL object that
    periodically runs a query, evaluates a condition of its result, and notifies one or more users and/or
    notification destinations if the condition was met. Alerts can be scheduled using the `sql_task` type of
    the Jobs API, e.g. :method:jobs/create."""

    def __init__(self, api_client):
        self._api = api_client

    def create(self,
               name: str,
               options: AlertOptions,
               query_id: str,
               *,
               parent: Optional[str] = None,
               rearm: Optional[int] = None) -> Alert:
        """Create an alert.
        
        Creates an alert. An alert is a Databricks SQL object that periodically runs a query, evaluates a
        condition of its result, and notifies users or notification destinations if the condition was met.
        
        :param name: str
          Name of the alert.
        :param options: :class:`AlertOptions`
          Alert configuration options.
        :param query_id: str
          Query ID.
        :param parent: str (optional)
          The identifier of the workspace folder containing the object.
        :param rearm: int (optional)
          Number of seconds after being triggered before the alert rearms itself and can be triggered again.
          If `null`, alert will never be triggered again.
        
        :returns: :class:`Alert`
        """
        body = {}
        if name is not None: body['name'] = name
        if options is not None: body['options'] = options.as_dict()
        if parent is not None: body['parent'] = parent
        if query_id is not None: body['query_id'] = query_id
        if rearm is not None: body['rearm'] = rearm
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        res = self._api.do('POST', '/api/2.0/preview/sql/alerts', body=body, headers=headers)
        return Alert.from_dict(res)

    def delete(self, alert_id: str):
        """Delete an alert.
        
        Deletes an alert. Deleted alerts are no longer accessible and cannot be restored. **Note:** Unlike
        queries and dashboards, alerts cannot be moved to the trash.
        
        :param alert_id: str
        
        
        """

        headers = {'Accept': 'application/json', }
        self._api.do('DELETE', f'/api/2.0/preview/sql/alerts/{alert_id}', headers=headers)

    def get(self, alert_id: str) -> Alert:
        """Get an alert.
        
        Gets an alert.
        
        :param alert_id: str
        
        :returns: :class:`Alert`
        """

        headers = {'Accept': 'application/json', }
        res = self._api.do('GET', f'/api/2.0/preview/sql/alerts/{alert_id}', headers=headers)
        return Alert.from_dict(res)

    def list(self) -> Iterator['Alert']:
        """Get alerts.
        
        Gets a list of alerts.
        
        :returns: Iterator over :class:`Alert`
        """

        headers = {'Accept': 'application/json', }
        res = self._api.do('GET', '/api/2.0/preview/sql/alerts', headers=headers)
        return [Alert.from_dict(v) for v in res]

    def update(self,
               name: str,
               options: AlertOptions,
               query_id: str,
               alert_id: str,
               *,
               rearm: Optional[int] = None):
        """Update an alert.
        
        Updates an alert.
        
        :param name: str
          Name of the alert.
        :param options: :class:`AlertOptions`
          Alert configuration options.
        :param query_id: str
          Query ID.
        :param alert_id: str
        :param rearm: int (optional)
          Number of seconds after being triggered before the alert rearms itself and can be triggered again.
          If `null`, alert will never be triggered again.
        
        
        """
        body = {}
        if name is not None: body['name'] = name
        if options is not None: body['options'] = options.as_dict()
        if query_id is not None: body['query_id'] = query_id
        if rearm is not None: body['rearm'] = rearm
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        self._api.do('PUT', f'/api/2.0/preview/sql/alerts/{alert_id}', body=body, headers=headers)


class DashboardWidgetsAPI:
    """This is an evolving API that facilitates the addition and removal of widgets from existing dashboards
    within the Databricks Workspace. Data structures may change over time."""

    def __init__(self, api_client):
        self._api = api_client

    def create(self,
               dashboard_id: str,
               options: WidgetOptions,
               width: int,
               *,
               text: Optional[str] = None,
               visualization_id: Optional[str] = None) -> Widget:
        """Add widget to a dashboard.
        
        :param dashboard_id: str
          Dashboard ID returned by :method:dashboards/create.
        :param options: :class:`WidgetOptions`
        :param width: int
          Width of a widget
        :param text: str (optional)
          If this is a textbox widget, the application displays this text. This field is ignored if the widget
          contains a visualization in the `visualization` field.
        :param visualization_id: str (optional)
          Query Vizualization ID returned by :method:queryvisualizations/create.
        
        :returns: :class:`Widget`
        """
        body = {}
        if dashboard_id is not None: body['dashboard_id'] = dashboard_id
        if options is not None: body['options'] = options.as_dict()
        if text is not None: body['text'] = text
        if visualization_id is not None: body['visualization_id'] = visualization_id
        if width is not None: body['width'] = width
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        res = self._api.do('POST', '/api/2.0/preview/sql/widgets', body=body, headers=headers)
        return Widget.from_dict(res)

    def delete(self, id: str):
        """Remove widget.
        
        :param id: str
        
        
        """

        headers = {'Accept': 'application/json', }
        self._api.do('DELETE', f'/api/2.0/preview/sql/widgets/{id}', headers=headers)

    def update(self,
               dashboard_id: str,
               options: WidgetOptions,
               width: int,
               id: str,
               *,
               text: Optional[str] = None,
               visualization_id: Optional[str] = None) -> Widget:
        """Update existing widget.
        
        :param dashboard_id: str
          Dashboard ID returned by :method:dashboards/create.
        :param options: :class:`WidgetOptions`
        :param width: int
          Width of a widget
        :param id: str
        :param text: str (optional)
          If this is a textbox widget, the application displays this text. This field is ignored if the widget
          contains a visualization in the `visualization` field.
        :param visualization_id: str (optional)
          Query Vizualization ID returned by :method:queryvisualizations/create.
        
        :returns: :class:`Widget`
        """
        body = {}
        if dashboard_id is not None: body['dashboard_id'] = dashboard_id
        if options is not None: body['options'] = options.as_dict()
        if text is not None: body['text'] = text
        if visualization_id is not None: body['visualization_id'] = visualization_id
        if width is not None: body['width'] = width
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        res = self._api.do('POST', f'/api/2.0/preview/sql/widgets/{id}', body=body, headers=headers)
        return Widget.from_dict(res)


class DashboardsAPI:
    """In general, there is little need to modify dashboards using the API. However, it can be useful to use
    dashboard objects to look-up a collection of related query IDs. The API can also be used to duplicate
    multiple dashboards at once since you can get a dashboard definition with a GET request and then POST it
    to create a new one. Dashboards can be scheduled using the `sql_task` type of the Jobs API, e.g.
    :method:jobs/create."""

    def __init__(self, api_client):
        self._api = api_client

    def create(self,
               name: str,
               *,
               dashboard_filters_enabled: Optional[bool] = None,
               is_favorite: Optional[bool] = None,
               parent: Optional[str] = None,
               run_as_role: Optional[RunAsRole] = None,
               tags: Optional[List[str]] = None) -> Dashboard:
        """Create a dashboard object.
        
        :param name: str
          The title of this dashboard that appears in list views and at the top of the dashboard page.
        :param dashboard_filters_enabled: bool (optional)
          Indicates whether the dashboard filters are enabled
        :param is_favorite: bool (optional)
          Indicates whether this query object should appear in the current user's favorites list. The
          application uses this flag to determine whether or not the "favorite star " should selected.
        :param parent: str (optional)
          The identifier of the workspace folder containing the object.
        :param run_as_role: :class:`RunAsRole` (optional)
          Run as role
        :param tags: List[str] (optional)
        
        :returns: :class:`Dashboard`
        """
        body = {}
        if dashboard_filters_enabled is not None:
            body['dashboard_filters_enabled'] = dashboard_filters_enabled
        if is_favorite is not None: body['is_favorite'] = is_favorite
        if name is not None: body['name'] = name
        if parent is not None: body['parent'] = parent
        if run_as_role is not None: body['run_as_role'] = run_as_role.value
        if tags is not None: body['tags'] = [v for v in tags]
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        res = self._api.do('POST', '/api/2.0/preview/sql/dashboards', body=body, headers=headers)
        return Dashboard.from_dict(res)

    def delete(self, dashboard_id: str):
        """Remove a dashboard.
        
        Moves a dashboard to the trash. Trashed dashboards do not appear in list views or searches, and cannot
        be shared.
        
        :param dashboard_id: str
        
        
        """

        headers = {'Accept': 'application/json', }
        self._api.do('DELETE', f'/api/2.0/preview/sql/dashboards/{dashboard_id}', headers=headers)

    def get(self, dashboard_id: str) -> Dashboard:
        """Retrieve a definition.
        
        Returns a JSON representation of a dashboard object, including its visualization and query objects.
        
        :param dashboard_id: str
        
        :returns: :class:`Dashboard`
        """

        headers = {'Accept': 'application/json', }
        res = self._api.do('GET', f'/api/2.0/preview/sql/dashboards/{dashboard_id}', headers=headers)
        return Dashboard.from_dict(res)

    def list(self,
             *,
             order: Optional[ListOrder] = None,
             page: Optional[int] = None,
             page_size: Optional[int] = None,
             q: Optional[str] = None) -> Iterator['Dashboard']:
        """Get dashboard objects.
        
        Fetch a paginated list of dashboard objects.
        
        :param order: :class:`ListOrder` (optional)
          Name of dashboard attribute to order by.
        :param page: int (optional)
          Page number to retrieve.
        :param page_size: int (optional)
          Number of dashboards to return per page.
        :param q: str (optional)
          Full text search term.
        
        :returns: Iterator over :class:`Dashboard`
        """

        query = {}
        if order is not None: query['order'] = order.value
        if page is not None: query['page'] = page
        if page_size is not None: query['page_size'] = page_size
        if q is not None: query['q'] = q
        headers = {'Accept': 'application/json', }

        # deduplicate items that may have been added during iteration
        seen = set()
        query['page'] = 1
        while True:
            json = self._api.do('GET', '/api/2.0/preview/sql/dashboards', query=query, headers=headers)
            if 'results' not in json or not json['results']:
                return
            for v in json['results']:
                i = v['id']
                if i in seen:
                    continue
                seen.add(i)
                yield Dashboard.from_dict(v)
            query['page'] += 1

    def restore(self, dashboard_id: str):
        """Restore a dashboard.
        
        A restored dashboard appears in list views and searches and can be shared.
        
        :param dashboard_id: str
        
        
        """

        headers = {'Accept': 'application/json', }
        self._api.do('POST', f'/api/2.0/preview/sql/dashboards/trash/{dashboard_id}', headers=headers)


class DataSourcesAPI:
    """This API is provided to assist you in making new query objects. When creating a query object, you may
    optionally specify a `data_source_id` for the SQL warehouse against which it will run. If you don't
    already know the `data_source_id` for your desired SQL warehouse, this API will help you find it.
    
    This API does not support searches. It returns the full list of SQL warehouses in your workspace. We
    advise you to use any text editor, REST client, or `grep` to search the response from this API for the
    name of your SQL warehouse as it appears in Databricks SQL."""

    def __init__(self, api_client):
        self._api = api_client

    def list(self) -> Iterator['DataSource']:
        """Get a list of SQL warehouses.
        
        Retrieves a full list of SQL warehouses available in this workspace. All fields that appear in this
        API response are enumerated for clarity. However, you need only a SQL warehouse's `id` to create new
        queries against it.
        
        :returns: Iterator over :class:`DataSource`
        """

        headers = {'Accept': 'application/json', }
        res = self._api.do('GET', '/api/2.0/preview/sql/data_sources', headers=headers)
        return [DataSource.from_dict(v) for v in res]


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

    def get(self, object_type: ObjectTypePlural, object_id: str) -> GetResponse:
        """Get object ACL.
        
        Gets a JSON representation of the access control list (ACL) for a specified object.
        
        :param object_type: :class:`ObjectTypePlural`
          The type of object permissions to check.
        :param object_id: str
          Object ID. An ACL is returned for the object with this UUID.
        
        :returns: :class:`GetResponse`
        """

        headers = {'Accept': 'application/json', }
        res = self._api.do('GET',
                           f'/api/2.0/preview/sql/permissions/{object_type.value}/{object_id}',
                           headers=headers)
        return GetResponse.from_dict(res)

    def set(self,
            object_type: ObjectTypePlural,
            object_id: str,
            *,
            access_control_list: Optional[List[AccessControl]] = None) -> SetResponse:
        """Set object ACL.
        
        Sets the access control list (ACL) for a specified object. This operation will complete rewrite the
        ACL.
        
        :param object_type: :class:`ObjectTypePlural`
          The type of object permission to set.
        :param object_id: str
          Object ID. The ACL for the object with this UUID is overwritten by this request's POST content.
        :param access_control_list: List[:class:`AccessControl`] (optional)
        
        :returns: :class:`SetResponse`
        """
        body = {}
        if access_control_list is not None:
            body['access_control_list'] = [v.as_dict() for v in access_control_list]
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        res = self._api.do('POST',
                           f'/api/2.0/preview/sql/permissions/{object_type.value}/{object_id}',
                           body=body,
                           headers=headers)
        return SetResponse.from_dict(res)

    def transfer_ownership(self,
                           object_type: OwnableObjectType,
                           object_id: TransferOwnershipObjectId,
                           *,
                           new_owner: Optional[str] = None) -> Success:
        """Transfer object ownership.
        
        Transfers ownership of a dashboard, query, or alert to an active user. Requires an admin API key.
        
        :param object_type: :class:`OwnableObjectType`
          The type of object on which to change ownership.
        :param object_id: :class:`TransferOwnershipObjectId`
          The ID of the object on which to change ownership.
        :param new_owner: str (optional)
          Email address for the new owner, who must exist in the workspace.
        
        :returns: :class:`Success`
        """
        body = {}
        if new_owner is not None: body['new_owner'] = new_owner
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        res = self._api.do('POST',
                           f'/api/2.0/preview/sql/permissions/{object_type.value}/{object_id}/transfer',
                           body=body,
                           headers=headers)
        return Success.from_dict(res)


class QueriesAPI:
    """These endpoints are used for CRUD operations on query definitions. Query definitions include the target
    SQL warehouse, query text, name, description, tags, parameters, and visualizations. Queries can be
    scheduled using the `sql_task` type of the Jobs API, e.g. :method:jobs/create."""

    def __init__(self, api_client):
        self._api = api_client

    def create(self,
               *,
               data_source_id: Optional[str] = None,
               description: Optional[str] = None,
               name: Optional[str] = None,
               options: Optional[Any] = None,
               parent: Optional[str] = None,
               query: Optional[str] = None,
               run_as_role: Optional[RunAsRole] = None) -> Query:
        """Create a new query definition.
        
        Creates a new query definition. Queries created with this endpoint belong to the authenticated user
        making the request.
        
        The `data_source_id` field specifies the ID of the SQL warehouse to run this query against. You can
        use the Data Sources API to see a complete list of available SQL warehouses. Or you can copy the
        `data_source_id` from an existing query.
        
        **Note**: You cannot add a visualization until you create the query.
        
        :param data_source_id: str (optional)
          Data source ID.
        :param description: str (optional)
          General description that conveys additional information about this query such as usage notes.
        :param name: str (optional)
          The title of this query that appears in list views, widget headings, and on the query page.
        :param options: Any (optional)
          Exclusively used for storing a list parameter definitions. A parameter is an object with `title`,
          `name`, `type`, and `value` properties. The `value` field here is the default value. It can be
          overridden at runtime.
        :param parent: str (optional)
          The identifier of the workspace folder containing the object.
        :param query: str (optional)
          The text of the query to be run.
        :param run_as_role: :class:`RunAsRole` (optional)
          Run as role
        
        :returns: :class:`Query`
        """
        body = {}
        if data_source_id is not None: body['data_source_id'] = data_source_id
        if description is not None: body['description'] = description
        if name is not None: body['name'] = name
        if options is not None: body['options'] = options
        if parent is not None: body['parent'] = parent
        if query is not None: body['query'] = query
        if run_as_role is not None: body['run_as_role'] = run_as_role.value
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        res = self._api.do('POST', '/api/2.0/preview/sql/queries', body=body, headers=headers)
        return Query.from_dict(res)

    def delete(self, query_id: str):
        """Delete a query.
        
        Moves a query to the trash. Trashed queries immediately disappear from searches and list views, and
        they cannot be used for alerts. The trash is deleted after 30 days.
        
        :param query_id: str
        
        
        """

        headers = {'Accept': 'application/json', }
        self._api.do('DELETE', f'/api/2.0/preview/sql/queries/{query_id}', headers=headers)

    def get(self, query_id: str) -> Query:
        """Get a query definition.
        
        Retrieve a query object definition along with contextual permissions information about the currently
        authenticated user.
        
        :param query_id: str
        
        :returns: :class:`Query`
        """

        headers = {'Accept': 'application/json', }
        res = self._api.do('GET', f'/api/2.0/preview/sql/queries/{query_id}', headers=headers)
        return Query.from_dict(res)

    def list(self,
             *,
             order: Optional[str] = None,
             page: Optional[int] = None,
             page_size: Optional[int] = None,
             q: Optional[str] = None) -> Iterator['Query']:
        """Get a list of queries.
        
        Gets a list of queries. Optionally, this list can be filtered by a search term.
        
        :param order: str (optional)
          Name of query attribute to order by. Default sort order is ascending. Append a dash (`-`) to order
          descending instead.
          
          - `name`: The name of the query.
          
          - `created_at`: The timestamp the query was created.
          
          - `runtime`: The time it took to run this query. This is blank for parameterized queries. A blank
          value is treated as the highest value for sorting.
          
          - `executed_at`: The timestamp when the query was last run.
          
          - `created_by`: The user name of the user that created the query.
        :param page: int (optional)
          Page number to retrieve.
        :param page_size: int (optional)
          Number of queries to return per page.
        :param q: str (optional)
          Full text search term
        
        :returns: Iterator over :class:`Query`
        """

        query = {}
        if order is not None: query['order'] = order
        if page is not None: query['page'] = page
        if page_size is not None: query['page_size'] = page_size
        if q is not None: query['q'] = q
        headers = {'Accept': 'application/json', }

        # deduplicate items that may have been added during iteration
        seen = set()
        query['page'] = 1
        while True:
            json = self._api.do('GET', '/api/2.0/preview/sql/queries', query=query, headers=headers)
            if 'results' not in json or not json['results']:
                return
            for v in json['results']:
                i = v['id']
                if i in seen:
                    continue
                seen.add(i)
                yield Query.from_dict(v)
            query['page'] += 1

    def restore(self, query_id: str):
        """Restore a query.
        
        Restore a query that has been moved to the trash. A restored query appears in list views and searches.
        You can use restored queries for alerts.
        
        :param query_id: str
        
        
        """

        headers = {'Accept': 'application/json', }
        self._api.do('POST', f'/api/2.0/preview/sql/queries/trash/{query_id}', headers=headers)

    def update(self,
               query_id: str,
               *,
               data_source_id: Optional[str] = None,
               description: Optional[str] = None,
               name: Optional[str] = None,
               options: Optional[Any] = None,
               query: Optional[str] = None) -> Query:
        """Change a query definition.
        
        Modify this query definition.
        
        **Note**: You cannot undo this operation.
        
        :param query_id: str
        :param data_source_id: str (optional)
          Data source ID.
        :param description: str (optional)
          General description that conveys additional information about this query such as usage notes.
        :param name: str (optional)
          The title of this query that appears in list views, widget headings, and on the query page.
        :param options: Any (optional)
          Exclusively used for storing a list parameter definitions. A parameter is an object with `title`,
          `name`, `type`, and `value` properties. The `value` field here is the default value. It can be
          overridden at runtime.
        :param query: str (optional)
          The text of the query to be run.
        
        :returns: :class:`Query`
        """
        body = {}
        if data_source_id is not None: body['data_source_id'] = data_source_id
        if description is not None: body['description'] = description
        if name is not None: body['name'] = name
        if options is not None: body['options'] = options
        if query is not None: body['query'] = query
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        res = self._api.do('POST', f'/api/2.0/preview/sql/queries/{query_id}', body=body, headers=headers)
        return Query.from_dict(res)


class QueryHistoryAPI:
    """Access the history of queries through SQL warehouses."""

    def __init__(self, api_client):
        self._api = api_client

    def list(self,
             *,
             filter_by: Optional[QueryFilter] = None,
             include_metrics: Optional[bool] = None,
             max_results: Optional[int] = None,
             page_token: Optional[str] = None) -> Iterator['QueryInfo']:
        """List Queries.
        
        List the history of queries through SQL warehouses.
        
        You can filter by user ID, warehouse ID, status, and time range.
        
        :param filter_by: :class:`QueryFilter` (optional)
          A filter to limit query history results. This field is optional.
        :param include_metrics: bool (optional)
          Whether to include metrics about query.
        :param max_results: int (optional)
          Limit the number of results returned in one page. The default is 100.
        :param page_token: str (optional)
          A token that can be used to get the next page of results.
        
        :returns: Iterator over :class:`QueryInfo`
        """

        query = {}
        if filter_by is not None: query['filter_by'] = filter_by.as_dict()
        if include_metrics is not None: query['include_metrics'] = include_metrics
        if max_results is not None: query['max_results'] = max_results
        if page_token is not None: query['page_token'] = page_token
        headers = {'Accept': 'application/json', }

        while True:
            json = self._api.do('GET', '/api/2.0/sql/history/queries', query=query, headers=headers)
            if 'res' not in json or not json['res']:
                return
            for v in json['res']:
                yield QueryInfo.from_dict(v)
            if 'next_page_token' not in json or not json['next_page_token']:
                return
            query['page_token'] = json['next_page_token']


class QueryVisualizationsAPI:
    """This is an evolving API that facilitates the addition and removal of vizualisations from existing queries
    within the Databricks Workspace. Data structures may change over time."""

    def __init__(self, api_client):
        self._api = api_client

    def create(self,
               query_id: str,
               type: str,
               options: Any,
               *,
               description: Optional[str] = None,
               name: Optional[str] = None) -> Visualization:
        """Add visualization to a query.
        
        :param query_id: str
          The identifier returned by :method:queries/create
        :param type: str
          The type of visualization: chart, table, pivot table, and so on.
        :param options: Any
          The options object varies widely from one visualization type to the next and is unsupported.
          Databricks does not recommend modifying visualization settings in JSON.
        :param description: str (optional)
          A short description of this visualization. This is not displayed in the UI.
        :param name: str (optional)
          The name of the visualization that appears on dashboards and the query screen.
        
        :returns: :class:`Visualization`
        """
        body = {}
        if description is not None: body['description'] = description
        if name is not None: body['name'] = name
        if options is not None: body['options'] = options
        if query_id is not None: body['query_id'] = query_id
        if type is not None: body['type'] = type
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        res = self._api.do('POST', '/api/2.0/preview/sql/visualizations', body=body, headers=headers)
        return Visualization.from_dict(res)

    def delete(self, id: str):
        """Remove visualization.
        
        :param id: str
        
        
        """

        headers = {'Accept': 'application/json', }
        self._api.do('DELETE', f'/api/2.0/preview/sql/visualizations/{id}', headers=headers)

    def update(self,
               id: str,
               *,
               created_at: Optional[str] = None,
               description: Optional[str] = None,
               name: Optional[str] = None,
               options: Optional[Any] = None,
               type: Optional[str] = None,
               updated_at: Optional[str] = None) -> Visualization:
        """Edit existing visualization.
        
        :param id: str
          The UUID for this visualization.
        :param created_at: str (optional)
        :param description: str (optional)
          A short description of this visualization. This is not displayed in the UI.
        :param name: str (optional)
          The name of the visualization that appears on dashboards and the query screen.
        :param options: Any (optional)
          The options object varies widely from one visualization type to the next and is unsupported.
          Databricks does not recommend modifying visualization settings in JSON.
        :param type: str (optional)
          The type of visualization: chart, table, pivot table, and so on.
        :param updated_at: str (optional)
        
        :returns: :class:`Visualization`
        """
        body = {}
        if created_at is not None: body['created_at'] = created_at
        if description is not None: body['description'] = description
        if name is not None: body['name'] = name
        if options is not None: body['options'] = options
        if type is not None: body['type'] = type
        if updated_at is not None: body['updated_at'] = updated_at
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        res = self._api.do('POST', f'/api/2.0/preview/sql/visualizations/{id}', body=body, headers=headers)
        return Visualization.from_dict(res)


class StatementExecutionAPI:
    """The Databricks SQL Statement Execution API can be used to execute SQL statements on a SQL warehouse and
    fetch the result.
    
    **Getting started**
    
    We suggest beginning with the [Databricks SQL Statement Execution API tutorial].
    
    **Overview of statement execution and result fetching**
    
    Statement execution begins by issuing a :method:statementexecution/executeStatement request with a valid
    SQL statement and warehouse ID, along with optional parameters such as the data catalog and output format.
    If no other parameters are specified, the server will wait for up to 10s before returning a response. If
    the statement has completed within this timespan, the response will include the result data as a JSON
    array and metadata. Otherwise, if no result is available after the 10s timeout expired, the response will
    provide the statement ID that can be used to poll for results by using a
    :method:statementexecution/getStatement request.
    
    You can specify whether the call should behave synchronously, asynchronously or start synchronously with a
    fallback to asynchronous execution. This is controlled with the `wait_timeout` and `on_wait_timeout`
    settings. If `wait_timeout` is set between 5-50 seconds (default: 10s), the call waits for results up to
    the specified timeout; when set to `0s`, the call is asynchronous and responds immediately with a
    statement ID. The `on_wait_timeout` setting specifies what should happen when the timeout is reached while
    the statement execution has not yet finished. This can be set to either `CONTINUE`, to fallback to
    asynchronous mode, or it can be set to `CANCEL`, which cancels the statement.
    
    In summary: - Synchronous mode - `wait_timeout=30s` and `on_wait_timeout=CANCEL` - The call waits up to 30
    seconds; if the statement execution finishes within this time, the result data is returned directly in the
    response. If the execution takes longer than 30 seconds, the execution is canceled and the call returns
    with a `CANCELED` state. - Asynchronous mode - `wait_timeout=0s` (`on_wait_timeout` is ignored) - The call
    doesn't wait for the statement to finish but returns directly with a statement ID. The status of the
    statement execution can be polled by issuing :method:statementexecution/getStatement with the statement
    ID. Once the execution has succeeded, this call also returns the result and metadata in the response. -
    Hybrid mode (default) - `wait_timeout=10s` and `on_wait_timeout=CONTINUE` - The call waits for up to 10
    seconds; if the statement execution finishes within this time, the result data is returned directly in the
    response. If the execution takes longer than 10 seconds, a statement ID is returned. The statement ID can
    be used to fetch status and results in the same way as in the asynchronous mode.
    
    Depending on the size, the result can be split into multiple chunks. If the statement execution is
    successful, the statement response contains a manifest and the first chunk of the result. The manifest
    contains schema information and provides metadata for each chunk in the result. Result chunks can be
    retrieved by index with :method:statementexecution/getStatementResultChunkN which may be called in any
    order and in parallel. For sequential fetching, each chunk, apart from the last, also contains a
    `next_chunk_index` and `next_chunk_internal_link` that point to the next chunk.
    
    A statement can be canceled with :method:statementexecution/cancelExecution.
    
    **Fetching result data: format and disposition**
    
    To specify the format of the result data, use the `format` field, which can be set to one of the following
    options: `JSON_ARRAY` (JSON), `ARROW_STREAM` ([Apache Arrow Columnar]), or `CSV`.
    
    There are two ways to receive statement results, controlled by the `disposition` setting, which can be
    either `INLINE` or `EXTERNAL_LINKS`:
    
    - `INLINE`: In this mode, the result data is directly included in the response. It's best suited for
    smaller results. This mode can only be used with the `JSON_ARRAY` format.
    
    - `EXTERNAL_LINKS`: In this mode, the response provides links that can be used to download the result data
    in chunks separately. This approach is ideal for larger results and offers higher throughput. This mode
    can be used with all the formats: `JSON_ARRAY`, `ARROW_STREAM`, and `CSV`.
    
    By default, the API uses `format=JSON_ARRAY` and `disposition=INLINE`.
    
    **Limits and limitations**
    
    Note: The byte limit for INLINE disposition is based on internal storage metrics and will not exactly
    match the byte count of the actual payload.
    
    - Statements with `disposition=INLINE` are limited to 25 MiB and will fail when this limit is exceeded. -
    Statements with `disposition=EXTERNAL_LINKS` are limited to 100 GiB. Result sets larger than this limit
    will be truncated. Truncation is indicated by the `truncated` field in the result manifest. - The maximum
    query text size is 16 MiB. - Cancelation might silently fail. A successful response from a cancel request
    indicates that the cancel request was successfully received and sent to the processing engine. However, an
    outstanding statement might have already completed execution when the cancel request arrives. Polling for
    status until a terminal state is reached is a reliable way to determine the final state. - Wait timeouts
    are approximate, occur server-side, and cannot account for things such as caller delays and network
    latency from caller to service. - The system will auto-close a statement after one hour if the client
    stops polling and thus you must poll at least once an hour. - The results are only available for one hour
    after success; polling does not extend this.
    
    [Apache Arrow Columnar]: https://arrow.apache.org/overview/
    [Databricks SQL Statement Execution API tutorial]: https://docs.databricks.com/sql/api/sql-execution-tutorial.html"""

    def __init__(self, api_client):
        self._api = api_client

    def cancel_execution(self, statement_id: str):
        """Cancel statement execution.
        
        Requests that an executing statement be canceled. Callers must poll for status to see the terminal
        state.
        
        :param statement_id: str
        
        
        """

        headers = {}
        self._api.do('POST', f'/api/2.0/sql/statements/{statement_id}/cancel', headers=headers)

    def execute_statement(self,
                          statement: str,
                          warehouse_id: str,
                          *,
                          byte_limit: Optional[int] = None,
                          catalog: Optional[str] = None,
                          disposition: Optional[Disposition] = None,
                          format: Optional[Format] = None,
                          on_wait_timeout: Optional[ExecuteStatementRequestOnWaitTimeout] = None,
                          parameters: Optional[List[StatementParameterListItem]] = None,
                          row_limit: Optional[int] = None,
                          schema: Optional[str] = None,
                          wait_timeout: Optional[str] = None) -> ExecuteStatementResponse:
        """Execute a SQL statement.
        
        :param statement: str
          The SQL statement to execute. The statement can optionally be parameterized, see `parameters`.
        :param warehouse_id: str
          Warehouse upon which to execute a statement. See also [What are SQL
          warehouses?](/sql/admin/warehouse-type.html)
        :param byte_limit: int (optional)
          Applies the given byte limit to the statement's result size. Byte counts are based on internal data
          representations and might not match the final size in the requested `format`. If the result was
          truncated due to the byte limit, then `truncated` in the response is set to `true`. When using
          `EXTERNAL_LINKS` disposition, a default `byte_limit` of 100 GiB is applied if `byte_limit` is not
          explcitly set.
        :param catalog: str (optional)
          Sets default catalog for statement execution, similar to [`USE CATALOG`] in SQL.
          
          [`USE CATALOG`]: https://docs.databricks.com/sql/language-manual/sql-ref-syntax-ddl-use-catalog.html
        :param disposition: :class:`Disposition` (optional)
          The fetch disposition provides two modes of fetching results: `INLINE` and `EXTERNAL_LINKS`.
          
          Statements executed with `INLINE` disposition will return result data inline, in `JSON_ARRAY`
          format, in a series of chunks. If a given statement produces a result set with a size larger than 25
          MiB, that statement execution is aborted, and no result set will be available.
          
          **NOTE** Byte limits are computed based upon internal representations of the result set data, and
          might not match the sizes visible in JSON responses.
          
          Statements executed with `EXTERNAL_LINKS` disposition will return result data as external links:
          URLs that point to cloud storage internal to the workspace. Using `EXTERNAL_LINKS` disposition
          allows statements to generate arbitrarily sized result sets for fetching up to 100 GiB. The
          resulting links have two important properties:
          
          1. They point to resources _external_ to the Databricks compute; therefore any associated
          authentication information (typically a personal access token, OAuth token, or similar) _must be
          removed_ when fetching from these links.
          
          2. These are presigned URLs with a specific expiration, indicated in the response. The behavior when
          attempting to use an expired link is cloud specific.
        :param format: :class:`Format` (optional)
          Statement execution supports three result formats: `JSON_ARRAY` (default), `ARROW_STREAM`, and
          `CSV`.
          
          Important: The formats `ARROW_STREAM` and `CSV` are supported only with `EXTERNAL_LINKS`
          disposition. `JSON_ARRAY` is supported in `INLINE` and `EXTERNAL_LINKS` disposition.
          
          When specifying `format=JSON_ARRAY`, result data will be formatted as an array of arrays of values,
          where each value is either the *string representation* of a value, or `null`. For example, the
          output of `SELECT concat('id-', id) AS strCol, id AS intCol, null AS nullCol FROM range(3)` would
          look like this:
          
          ``` [ [ "id-1", "1", null ], [ "id-2", "2", null ], [ "id-3", "3", null ], ] ```
          
          When specifying `format=JSON_ARRAY` and `disposition=EXTERNAL_LINKS`, each chunk in the result
          contains compact JSON with no indentation or extra whitespace.
          
          When specifying `format=ARROW_STREAM` and `disposition=EXTERNAL_LINKS`, each chunk in the result
          will be formatted as Apache Arrow Stream. See the [Apache Arrow streaming format].
          
          When specifying `format=CSV` and `disposition=EXTERNAL_LINKS`, each chunk in the result will be a
          CSV according to [RFC 4180] standard. All the columns values will have *string representation*
          similar to the `JSON_ARRAY` format, and `null` values will be encoded as “null”. Only the first
          chunk in the result would contain a header row with column names. For example, the output of `SELECT
          concat('id-', id) AS strCol, id AS intCol, null as nullCol FROM range(3)` would look like this:
          
          ``` strCol,intCol,nullCol id-1,1,null id-2,2,null id-3,3,null ```
          
          [Apache Arrow streaming format]: https://arrow.apache.org/docs/format/Columnar.html#ipc-streaming-format
          [RFC 4180]: https://www.rfc-editor.org/rfc/rfc4180
        :param on_wait_timeout: :class:`ExecuteStatementRequestOnWaitTimeout` (optional)
          When `wait_timeout > 0s`, the call will block up to the specified time. If the statement execution
          doesn't finish within this time, `on_wait_timeout` determines whether the execution should continue
          or be canceled. When set to `CONTINUE`, the statement execution continues asynchronously and the
          call returns a statement ID which can be used for polling with
          :method:statementexecution/getStatement. When set to `CANCEL`, the statement execution is canceled
          and the call returns with a `CANCELED` state.
        :param parameters: List[:class:`StatementParameterListItem`] (optional)
          A list of parameters to pass into a SQL statement containing parameter markers. A parameter consists
          of a name, a value, and optionally a type. To represent a NULL value, the `value` field may be
          omitted or set to `null` explicitly. If the `type` field is omitted, the value is interpreted as a
          string.
          
          If the type is given, parameters will be checked for type correctness according to the given type. A
          value is correct if the provided string can be converted to the requested type using the `cast`
          function. The exact semantics are described in the section [`cast` function] of the SQL language
          reference.
          
          For example, the following statement contains two parameters, `my_name` and `my_date`:
          
          SELECT * FROM my_table WHERE name = :my_name AND date = :my_date
          
          The parameters can be passed in the request body as follows:
          
          { ..., "statement": "SELECT * FROM my_table WHERE name = :my_name AND date = :my_date",
          "parameters": [ { "name": "my_name", "value": "the name" }, { "name": "my_date", "value":
          "2020-01-01", "type": "DATE" } ] }
          
          Currently, positional parameters denoted by a `?` marker are not supported by the Databricks SQL
          Statement Execution API.
          
          Also see the section [Parameter markers] of the SQL language reference.
          
          [Parameter markers]: https://docs.databricks.com/sql/language-manual/sql-ref-parameter-marker.html
          [`cast` function]: https://docs.databricks.com/sql/language-manual/functions/cast.html
        :param row_limit: int (optional)
          Applies the given row limit to the statement's result set, but unlike the `LIMIT` clause in SQL, it
          also sets the `truncated` field in the response to indicate whether the result was trimmed due to
          the limit or not.
        :param schema: str (optional)
          Sets default schema for statement execution, similar to [`USE SCHEMA`] in SQL.
          
          [`USE SCHEMA`]: https://docs.databricks.com/sql/language-manual/sql-ref-syntax-ddl-use-schema.html
        :param wait_timeout: str (optional)
          The time in seconds the call will wait for the statement's result set as `Ns`, where `N` can be set
          to 0 or to a value between 5 and 50.
          
          When set to `0s`, the statement will execute in asynchronous mode and the call will not wait for the
          execution to finish. In this case, the call returns directly with `PENDING` state and a statement ID
          which can be used for polling with :method:statementexecution/getStatement.
          
          When set between 5 and 50 seconds, the call will behave synchronously up to this timeout and wait
          for the statement execution to finish. If the execution finishes within this time, the call returns
          immediately with a manifest and result data (or a `FAILED` state in case of an execution error). If
          the statement takes longer to execute, `on_wait_timeout` determines what should happen after the
          timeout is reached.
        
        :returns: :class:`ExecuteStatementResponse`
        """
        body = {}
        if byte_limit is not None: body['byte_limit'] = byte_limit
        if catalog is not None: body['catalog'] = catalog
        if disposition is not None: body['disposition'] = disposition.value
        if format is not None: body['format'] = format.value
        if on_wait_timeout is not None: body['on_wait_timeout'] = on_wait_timeout.value
        if parameters is not None: body['parameters'] = [v.as_dict() for v in parameters]
        if row_limit is not None: body['row_limit'] = row_limit
        if schema is not None: body['schema'] = schema
        if statement is not None: body['statement'] = statement
        if wait_timeout is not None: body['wait_timeout'] = wait_timeout
        if warehouse_id is not None: body['warehouse_id'] = warehouse_id
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        res = self._api.do('POST', '/api/2.0/sql/statements/', body=body, headers=headers)
        return ExecuteStatementResponse.from_dict(res)

    def get_statement(self, statement_id: str) -> GetStatementResponse:
        """Get status, manifest, and result first chunk.
        
        This request can be used to poll for the statement's status. When the `status.state` field is
        `SUCCEEDED` it will also return the result manifest and the first chunk of the result data. When the
        statement is in the terminal states `CANCELED`, `CLOSED` or `FAILED`, it returns HTTP 200 with the
        state set. After at least 12 hours in terminal state, the statement is removed from the warehouse and
        further calls will receive an HTTP 404 response.
        
        **NOTE** This call currently might take up to 5 seconds to get the latest status and result.
        
        :param statement_id: str
        
        :returns: :class:`GetStatementResponse`
        """

        headers = {'Accept': 'application/json', }
        res = self._api.do('GET', f'/api/2.0/sql/statements/{statement_id}', headers=headers)
        return GetStatementResponse.from_dict(res)

    def get_statement_result_chunk_n(self, statement_id: str, chunk_index: int) -> ResultData:
        """Get result chunk by index.
        
        After the statement execution has `SUCCEEDED`, this request can be used to fetch any chunk by index.
        Whereas the first chunk with `chunk_index=0` is typically fetched with
        :method:statementexecution/executeStatement or :method:statementexecution/getStatement, this request
        can be used to fetch subsequent chunks. The response structure is identical to the nested `result`
        element described in the :method:statementexecution/getStatement request, and similarly includes the
        `next_chunk_index` and `next_chunk_internal_link` fields for simple iteration through the result set.
        
        :param statement_id: str
        :param chunk_index: int
        
        :returns: :class:`ResultData`
        """

        headers = {'Accept': 'application/json', }
        res = self._api.do('GET',
                           f'/api/2.0/sql/statements/{statement_id}/result/chunks/{chunk_index}',
                           headers=headers)
        return ResultData.from_dict(res)


class WarehousesAPI:
    """A SQL warehouse is a compute resource that lets you run SQL commands on data objects within Databricks
    SQL. Compute resources are infrastructure resources that provide processing capabilities in the cloud."""

    def __init__(self, api_client):
        self._api = api_client

    def wait_get_warehouse_running(
            self,
            id: str,
            timeout=timedelta(minutes=20),
            callback: Optional[Callable[[GetWarehouseResponse], None]] = None) -> GetWarehouseResponse:
        deadline = time.time() + timeout.total_seconds()
        target_states = (State.RUNNING, )
        failure_states = (State.STOPPED, State.DELETED, )
        status_message = 'polling...'
        attempt = 1
        while time.time() < deadline:
            poll = self.get(id=id)
            status = poll.state
            status_message = f'current status: {status}'
            if poll.health:
                status_message = poll.health.summary
            if status in target_states:
                return poll
            if callback:
                callback(poll)
            if status in failure_states:
                msg = f'failed to reach RUNNING, got {status}: {status_message}'
                raise OperationFailed(msg)
            prefix = f"id={id}"
            sleep = attempt
            if sleep > 10:
                # sleep 10s max per attempt
                sleep = 10
            _LOG.debug(f'{prefix}: ({status}) {status_message} (sleeping ~{sleep}s)')
            time.sleep(sleep + random.random())
            attempt += 1
        raise TimeoutError(f'timed out after {timeout}: {status_message}')

    def wait_get_warehouse_stopped(
            self,
            id: str,
            timeout=timedelta(minutes=20),
            callback: Optional[Callable[[GetWarehouseResponse], None]] = None) -> GetWarehouseResponse:
        deadline = time.time() + timeout.total_seconds()
        target_states = (State.STOPPED, )
        status_message = 'polling...'
        attempt = 1
        while time.time() < deadline:
            poll = self.get(id=id)
            status = poll.state
            status_message = f'current status: {status}'
            if poll.health:
                status_message = poll.health.summary
            if status in target_states:
                return poll
            if callback:
                callback(poll)
            prefix = f"id={id}"
            sleep = attempt
            if sleep > 10:
                # sleep 10s max per attempt
                sleep = 10
            _LOG.debug(f'{prefix}: ({status}) {status_message} (sleeping ~{sleep}s)')
            time.sleep(sleep + random.random())
            attempt += 1
        raise TimeoutError(f'timed out after {timeout}: {status_message}')

    def create(
            self,
            *,
            auto_stop_mins: Optional[int] = None,
            channel: Optional[Channel] = None,
            cluster_size: Optional[str] = None,
            creator_name: Optional[str] = None,
            enable_photon: Optional[bool] = None,
            enable_serverless_compute: Optional[bool] = None,
            instance_profile_arn: Optional[str] = None,
            max_num_clusters: Optional[int] = None,
            min_num_clusters: Optional[int] = None,
            name: Optional[str] = None,
            spot_instance_policy: Optional[SpotInstancePolicy] = None,
            tags: Optional[EndpointTags] = None,
            warehouse_type: Optional[CreateWarehouseRequestWarehouseType] = None
    ) -> Wait[GetWarehouseResponse]:
        """Create a warehouse.
        
        Creates a new SQL warehouse.
        
        :param auto_stop_mins: int (optional)
          The amount of time in minutes that a SQL warehouse must be idle (i.e., no RUNNING queries) before it
          is automatically stopped.
          
          Supported values: - Must be == 0 or >= 10 mins - 0 indicates no autostop.
          
          Defaults to 120 mins
        :param channel: :class:`Channel` (optional)
          Channel Details
        :param cluster_size: str (optional)
          Size of the clusters allocated for this warehouse. Increasing the size of a spark cluster allows you
          to run larger queries on it. If you want to increase the number of concurrent queries, please tune
          max_num_clusters.
          
          Supported values: - 2X-Small - X-Small - Small - Medium - Large - X-Large - 2X-Large - 3X-Large -
          4X-Large
        :param creator_name: str (optional)
          warehouse creator name
        :param enable_photon: bool (optional)
          Configures whether the warehouse should use Photon optimized clusters.
          
          Defaults to false.
        :param enable_serverless_compute: bool (optional)
          Configures whether the warehouse should use serverless compute
        :param instance_profile_arn: str (optional)
          Deprecated. Instance profile used to pass IAM role to the cluster
        :param max_num_clusters: int (optional)
          Maximum number of clusters that the autoscaler will create to handle concurrent queries.
          
          Supported values: - Must be >= min_num_clusters - Must be <= 30.
          
          Defaults to min_clusters if unset.
        :param min_num_clusters: int (optional)
          Minimum number of available clusters that will be maintained for this SQL warehouse. Increasing this
          will ensure that a larger number of clusters are always running and therefore may reduce the cold
          start time for new queries. This is similar to reserved vs. revocable cores in a resource manager.
          
          Supported values: - Must be > 0 - Must be <= min(max_num_clusters, 30)
          
          Defaults to 1
        :param name: str (optional)
          Logical name for the cluster.
          
          Supported values: - Must be unique within an org. - Must be less than 100 characters.
        :param spot_instance_policy: :class:`SpotInstancePolicy` (optional)
          Configurations whether the warehouse should use spot instances.
        :param tags: :class:`EndpointTags` (optional)
          A set of key-value pairs that will be tagged on all resources (e.g., AWS instances and EBS volumes)
          associated with this SQL warehouse.
          
          Supported values: - Number of tags < 45.
        :param warehouse_type: :class:`CreateWarehouseRequestWarehouseType` (optional)
          Warehouse type: `PRO` or `CLASSIC`. If you want to use serverless compute, you must set to `PRO` and
          also set the field `enable_serverless_compute` to `true`.
        
        :returns:
          Long-running operation waiter for :class:`GetWarehouseResponse`.
          See :method:wait_get_warehouse_running for more details.
        """
        body = {}
        if auto_stop_mins is not None: body['auto_stop_mins'] = auto_stop_mins
        if channel is not None: body['channel'] = channel.as_dict()
        if cluster_size is not None: body['cluster_size'] = cluster_size
        if creator_name is not None: body['creator_name'] = creator_name
        if enable_photon is not None: body['enable_photon'] = enable_photon
        if enable_serverless_compute is not None:
            body['enable_serverless_compute'] = enable_serverless_compute
        if instance_profile_arn is not None: body['instance_profile_arn'] = instance_profile_arn
        if max_num_clusters is not None: body['max_num_clusters'] = max_num_clusters
        if min_num_clusters is not None: body['min_num_clusters'] = min_num_clusters
        if name is not None: body['name'] = name
        if spot_instance_policy is not None: body['spot_instance_policy'] = spot_instance_policy.value
        if tags is not None: body['tags'] = tags.as_dict()
        if warehouse_type is not None: body['warehouse_type'] = warehouse_type.value
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        op_response = self._api.do('POST', '/api/2.0/sql/warehouses', body=body, headers=headers)
        return Wait(self.wait_get_warehouse_running,
                    response=CreateWarehouseResponse.from_dict(op_response),
                    id=op_response['id'])

    def create_and_wait(
        self,
        *,
        auto_stop_mins: Optional[int] = None,
        channel: Optional[Channel] = None,
        cluster_size: Optional[str] = None,
        creator_name: Optional[str] = None,
        enable_photon: Optional[bool] = None,
        enable_serverless_compute: Optional[bool] = None,
        instance_profile_arn: Optional[str] = None,
        max_num_clusters: Optional[int] = None,
        min_num_clusters: Optional[int] = None,
        name: Optional[str] = None,
        spot_instance_policy: Optional[SpotInstancePolicy] = None,
        tags: Optional[EndpointTags] = None,
        warehouse_type: Optional[CreateWarehouseRequestWarehouseType] = None,
        timeout=timedelta(minutes=20)
    ) -> GetWarehouseResponse:
        return self.create(auto_stop_mins=auto_stop_mins,
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
                           warehouse_type=warehouse_type).result(timeout=timeout)

    def delete(self, id: str):
        """Delete a warehouse.
        
        Deletes a SQL warehouse.
        
        :param id: str
          Required. Id of the SQL warehouse.
        
        
        """

        headers = {'Accept': 'application/json', }
        self._api.do('DELETE', f'/api/2.0/sql/warehouses/{id}', headers=headers)

    def edit(
            self,
            id: str,
            *,
            auto_stop_mins: Optional[int] = None,
            channel: Optional[Channel] = None,
            cluster_size: Optional[str] = None,
            creator_name: Optional[str] = None,
            enable_photon: Optional[bool] = None,
            enable_serverless_compute: Optional[bool] = None,
            instance_profile_arn: Optional[str] = None,
            max_num_clusters: Optional[int] = None,
            min_num_clusters: Optional[int] = None,
            name: Optional[str] = None,
            spot_instance_policy: Optional[SpotInstancePolicy] = None,
            tags: Optional[EndpointTags] = None,
            warehouse_type: Optional[EditWarehouseRequestWarehouseType] = None) -> Wait[GetWarehouseResponse]:
        """Update a warehouse.
        
        Updates the configuration for a SQL warehouse.
        
        :param id: str
          Required. Id of the warehouse to configure.
        :param auto_stop_mins: int (optional)
          The amount of time in minutes that a SQL warehouse must be idle (i.e., no RUNNING queries) before it
          is automatically stopped.
          
          Supported values: - Must be == 0 or >= 10 mins - 0 indicates no autostop.
          
          Defaults to 120 mins
        :param channel: :class:`Channel` (optional)
          Channel Details
        :param cluster_size: str (optional)
          Size of the clusters allocated for this warehouse. Increasing the size of a spark cluster allows you
          to run larger queries on it. If you want to increase the number of concurrent queries, please tune
          max_num_clusters.
          
          Supported values: - 2X-Small - X-Small - Small - Medium - Large - X-Large - 2X-Large - 3X-Large -
          4X-Large
        :param creator_name: str (optional)
          warehouse creator name
        :param enable_photon: bool (optional)
          Configures whether the warehouse should use Photon optimized clusters.
          
          Defaults to false.
        :param enable_serverless_compute: bool (optional)
          Configures whether the warehouse should use serverless compute.
        :param instance_profile_arn: str (optional)
          Deprecated. Instance profile used to pass IAM role to the cluster
        :param max_num_clusters: int (optional)
          Maximum number of clusters that the autoscaler will create to handle concurrent queries.
          
          Supported values: - Must be >= min_num_clusters - Must be <= 30.
          
          Defaults to min_clusters if unset.
        :param min_num_clusters: int (optional)
          Minimum number of available clusters that will be maintained for this SQL warehouse. Increasing this
          will ensure that a larger number of clusters are always running and therefore may reduce the cold
          start time for new queries. This is similar to reserved vs. revocable cores in a resource manager.
          
          Supported values: - Must be > 0 - Must be <= min(max_num_clusters, 30)
          
          Defaults to 1
        :param name: str (optional)
          Logical name for the cluster.
          
          Supported values: - Must be unique within an org. - Must be less than 100 characters.
        :param spot_instance_policy: :class:`SpotInstancePolicy` (optional)
          Configurations whether the warehouse should use spot instances.
        :param tags: :class:`EndpointTags` (optional)
          A set of key-value pairs that will be tagged on all resources (e.g., AWS instances and EBS volumes)
          associated with this SQL warehouse.
          
          Supported values: - Number of tags < 45.
        :param warehouse_type: :class:`EditWarehouseRequestWarehouseType` (optional)
          Warehouse type: `PRO` or `CLASSIC`. If you want to use serverless compute, you must set to `PRO` and
          also set the field `enable_serverless_compute` to `true`.
        
        :returns:
          Long-running operation waiter for :class:`GetWarehouseResponse`.
          See :method:wait_get_warehouse_running for more details.
        """
        body = {}
        if auto_stop_mins is not None: body['auto_stop_mins'] = auto_stop_mins
        if channel is not None: body['channel'] = channel.as_dict()
        if cluster_size is not None: body['cluster_size'] = cluster_size
        if creator_name is not None: body['creator_name'] = creator_name
        if enable_photon is not None: body['enable_photon'] = enable_photon
        if enable_serverless_compute is not None:
            body['enable_serverless_compute'] = enable_serverless_compute
        if instance_profile_arn is not None: body['instance_profile_arn'] = instance_profile_arn
        if max_num_clusters is not None: body['max_num_clusters'] = max_num_clusters
        if min_num_clusters is not None: body['min_num_clusters'] = min_num_clusters
        if name is not None: body['name'] = name
        if spot_instance_policy is not None: body['spot_instance_policy'] = spot_instance_policy.value
        if tags is not None: body['tags'] = tags.as_dict()
        if warehouse_type is not None: body['warehouse_type'] = warehouse_type.value
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        self._api.do('POST', f'/api/2.0/sql/warehouses/{id}/edit', body=body, headers=headers)
        return Wait(self.wait_get_warehouse_running, id=id)

    def edit_and_wait(
        self,
        id: str,
        *,
        auto_stop_mins: Optional[int] = None,
        channel: Optional[Channel] = None,
        cluster_size: Optional[str] = None,
        creator_name: Optional[str] = None,
        enable_photon: Optional[bool] = None,
        enable_serverless_compute: Optional[bool] = None,
        instance_profile_arn: Optional[str] = None,
        max_num_clusters: Optional[int] = None,
        min_num_clusters: Optional[int] = None,
        name: Optional[str] = None,
        spot_instance_policy: Optional[SpotInstancePolicy] = None,
        tags: Optional[EndpointTags] = None,
        warehouse_type: Optional[EditWarehouseRequestWarehouseType] = None,
        timeout=timedelta(minutes=20)
    ) -> GetWarehouseResponse:
        return self.edit(auto_stop_mins=auto_stop_mins,
                         channel=channel,
                         cluster_size=cluster_size,
                         creator_name=creator_name,
                         enable_photon=enable_photon,
                         enable_serverless_compute=enable_serverless_compute,
                         id=id,
                         instance_profile_arn=instance_profile_arn,
                         max_num_clusters=max_num_clusters,
                         min_num_clusters=min_num_clusters,
                         name=name,
                         spot_instance_policy=spot_instance_policy,
                         tags=tags,
                         warehouse_type=warehouse_type).result(timeout=timeout)

    def get(self, id: str) -> GetWarehouseResponse:
        """Get warehouse info.
        
        Gets the information for a single SQL warehouse.
        
        :param id: str
          Required. Id of the SQL warehouse.
        
        :returns: :class:`GetWarehouseResponse`
        """

        headers = {'Accept': 'application/json', }
        res = self._api.do('GET', f'/api/2.0/sql/warehouses/{id}', headers=headers)
        return GetWarehouseResponse.from_dict(res)

    def get_permission_levels(self, warehouse_id: str) -> GetWarehousePermissionLevelsResponse:
        """Get SQL warehouse permission levels.
        
        Gets the permission levels that a user can have on an object.
        
        :param warehouse_id: str
          The SQL warehouse for which to get or manage permissions.
        
        :returns: :class:`GetWarehousePermissionLevelsResponse`
        """

        headers = {'Accept': 'application/json', }
        res = self._api.do('GET',
                           f'/api/2.0/permissions/warehouses/{warehouse_id}/permissionLevels',
                           headers=headers)
        return GetWarehousePermissionLevelsResponse.from_dict(res)

    def get_permissions(self, warehouse_id: str) -> WarehousePermissions:
        """Get SQL warehouse permissions.
        
        Gets the permissions of a SQL warehouse. SQL warehouses can inherit permissions from their root
        object.
        
        :param warehouse_id: str
          The SQL warehouse for which to get or manage permissions.
        
        :returns: :class:`WarehousePermissions`
        """

        headers = {'Accept': 'application/json', }
        res = self._api.do('GET', f'/api/2.0/permissions/warehouses/{warehouse_id}', headers=headers)
        return WarehousePermissions.from_dict(res)

    def get_workspace_warehouse_config(self) -> GetWorkspaceWarehouseConfigResponse:
        """Get the workspace configuration.
        
        Gets the workspace level configuration that is shared by all SQL warehouses in a workspace.
        
        :returns: :class:`GetWorkspaceWarehouseConfigResponse`
        """

        headers = {'Accept': 'application/json', }
        res = self._api.do('GET', '/api/2.0/sql/config/warehouses', headers=headers)
        return GetWorkspaceWarehouseConfigResponse.from_dict(res)

    def list(self, *, run_as_user_id: Optional[int] = None) -> Iterator['EndpointInfo']:
        """List warehouses.
        
        Lists all SQL warehouses that a user has manager permissions on.
        
        :param run_as_user_id: int (optional)
          Service Principal which will be used to fetch the list of warehouses. If not specified, the user
          from the session header is used.
        
        :returns: Iterator over :class:`EndpointInfo`
        """

        query = {}
        if run_as_user_id is not None: query['run_as_user_id'] = run_as_user_id
        headers = {'Accept': 'application/json', }
        json = self._api.do('GET', '/api/2.0/sql/warehouses', query=query, headers=headers)
        parsed = ListWarehousesResponse.from_dict(json).warehouses
        return parsed if parsed is not None else []

    def set_permissions(self,
                        warehouse_id: str,
                        *,
                        access_control_list: Optional[List[WarehouseAccessControlRequest]] = None
                        ) -> WarehousePermissions:
        """Set SQL warehouse permissions.
        
        Sets permissions on a SQL warehouse. SQL warehouses can inherit permissions from their root object.
        
        :param warehouse_id: str
          The SQL warehouse for which to get or manage permissions.
        :param access_control_list: List[:class:`WarehouseAccessControlRequest`] (optional)
        
        :returns: :class:`WarehousePermissions`
        """
        body = {}
        if access_control_list is not None:
            body['access_control_list'] = [v.as_dict() for v in access_control_list]
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        res = self._api.do('PUT',
                           f'/api/2.0/permissions/warehouses/{warehouse_id}',
                           body=body,
                           headers=headers)
        return WarehousePermissions.from_dict(res)

    def set_workspace_warehouse_config(
            self,
            *,
            channel: Optional[Channel] = None,
            config_param: Optional[RepeatedEndpointConfPairs] = None,
            data_access_config: Optional[List[EndpointConfPair]] = None,
            enabled_warehouse_types: Optional[List[WarehouseTypePair]] = None,
            global_param: Optional[RepeatedEndpointConfPairs] = None,
            google_service_account: Optional[str] = None,
            instance_profile_arn: Optional[str] = None,
            security_policy: Optional[SetWorkspaceWarehouseConfigRequestSecurityPolicy] = None,
            sql_configuration_parameters: Optional[RepeatedEndpointConfPairs] = None):
        """Set the workspace configuration.
        
        Sets the workspace level configuration that is shared by all SQL warehouses in a workspace.
        
        :param channel: :class:`Channel` (optional)
          Optional: Channel selection details
        :param config_param: :class:`RepeatedEndpointConfPairs` (optional)
          Deprecated: Use sql_configuration_parameters
        :param data_access_config: List[:class:`EndpointConfPair`] (optional)
          Spark confs for external hive metastore configuration JSON serialized size must be less than <= 512K
        :param enabled_warehouse_types: List[:class:`WarehouseTypePair`] (optional)
          List of Warehouse Types allowed in this workspace (limits allowed value of the type field in
          CreateWarehouse and EditWarehouse). Note: Some types cannot be disabled, they don't need to be
          specified in SetWorkspaceWarehouseConfig. Note: Disabling a type may cause existing warehouses to be
          converted to another type. Used by frontend to save specific type availability in the warehouse
          create and edit form UI.
        :param global_param: :class:`RepeatedEndpointConfPairs` (optional)
          Deprecated: Use sql_configuration_parameters
        :param google_service_account: str (optional)
          GCP only: Google Service Account used to pass to cluster to access Google Cloud Storage
        :param instance_profile_arn: str (optional)
          AWS Only: Instance profile used to pass IAM role to the cluster
        :param security_policy: :class:`SetWorkspaceWarehouseConfigRequestSecurityPolicy` (optional)
          Security policy for warehouses
        :param sql_configuration_parameters: :class:`RepeatedEndpointConfPairs` (optional)
          SQL configuration parameters
        
        
        """
        body = {}
        if channel is not None: body['channel'] = channel.as_dict()
        if config_param is not None: body['config_param'] = config_param.as_dict()
        if data_access_config is not None:
            body['data_access_config'] = [v.as_dict() for v in data_access_config]
        if enabled_warehouse_types is not None:
            body['enabled_warehouse_types'] = [v.as_dict() for v in enabled_warehouse_types]
        if global_param is not None: body['global_param'] = global_param.as_dict()
        if google_service_account is not None: body['google_service_account'] = google_service_account
        if instance_profile_arn is not None: body['instance_profile_arn'] = instance_profile_arn
        if security_policy is not None: body['security_policy'] = security_policy.value
        if sql_configuration_parameters is not None:
            body['sql_configuration_parameters'] = sql_configuration_parameters.as_dict()
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        self._api.do('PUT', '/api/2.0/sql/config/warehouses', body=body, headers=headers)

    def start(self, id: str) -> Wait[GetWarehouseResponse]:
        """Start a warehouse.
        
        Starts a SQL warehouse.
        
        :param id: str
          Required. Id of the SQL warehouse.
        
        :returns:
          Long-running operation waiter for :class:`GetWarehouseResponse`.
          See :method:wait_get_warehouse_running for more details.
        """

        headers = {'Accept': 'application/json', }
        self._api.do('POST', f'/api/2.0/sql/warehouses/{id}/start', headers=headers)
        return Wait(self.wait_get_warehouse_running, id=id)

    def start_and_wait(self, id: str, timeout=timedelta(minutes=20)) -> GetWarehouseResponse:
        return self.start(id=id).result(timeout=timeout)

    def stop(self, id: str) -> Wait[GetWarehouseResponse]:
        """Stop a warehouse.
        
        Stops a SQL warehouse.
        
        :param id: str
          Required. Id of the SQL warehouse.
        
        :returns:
          Long-running operation waiter for :class:`GetWarehouseResponse`.
          See :method:wait_get_warehouse_stopped for more details.
        """

        headers = {'Accept': 'application/json', }
        self._api.do('POST', f'/api/2.0/sql/warehouses/{id}/stop', headers=headers)
        return Wait(self.wait_get_warehouse_stopped, id=id)

    def stop_and_wait(self, id: str, timeout=timedelta(minutes=20)) -> GetWarehouseResponse:
        return self.stop(id=id).result(timeout=timeout)

    def update_permissions(self,
                           warehouse_id: str,
                           *,
                           access_control_list: Optional[List[WarehouseAccessControlRequest]] = None
                           ) -> WarehousePermissions:
        """Update SQL warehouse permissions.
        
        Updates the permissions on a SQL warehouse. SQL warehouses can inherit permissions from their root
        object.
        
        :param warehouse_id: str
          The SQL warehouse for which to get or manage permissions.
        :param access_control_list: List[:class:`WarehouseAccessControlRequest`] (optional)
        
        :returns: :class:`WarehousePermissions`
        """
        body = {}
        if access_control_list is not None:
            body['access_control_list'] = [v.as_dict() for v in access_control_list]
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        res = self._api.do('PATCH',
                           f'/api/2.0/permissions/warehouses/{warehouse_id}',
                           body=body,
                           headers=headers)
        return WarehousePermissions.from_dict(res)
