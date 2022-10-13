# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

from dataclasses import dataclass
from enum import Enum
from typing import Optional, Dict, List

__all__ = [
    
    'AccessControl',
    'Alert',
    'AlertOptions',
    'CreateRefreshSchedule',
    'CreateSubscription',
    'Dashboard',
    'DashboardOptions',
    'DataSource',
    'Destination',
    'DestinationType',
    'EditAlert',
    'Parameter',
    'ParameterType',
    'PermissionLevel',
    'Query',
    'QueryInterval',
    'QueryOptions',
    'QueryPostContent',
    'RefreshSchedule',
    'Subscription',
    'Success',
    'SuccessMessage',
    'TagString',
    'User',
    'Visualization',
    'Widget',
    'WidgetOptions',
    'AlertCreatedAt',
    'AlertId',
    'AlertLastTriggeredAt',
    'AlertName',
    'AlertQueryId',
    'AlertRearm',
    'AlertState',
    'AlertSubscriptionDestinationId',
    'AlertSubscriptionId',
    'AlertSubscriptionUserId',
    'AlertUpdatedAt',
    'CreateDashboardRequest',
    'DeleteAlertRequest',
    'DeleteDashboardRequest',
    'DeleteQueryRequest',
    'DeleteScheduleRequest',
    'GetAlertRequest',
    'GetDashboardRequest',
    'GetPermissionsRequest',
    'GetPermissionsResponse',
    'GetQueryRequest',
    'GetSubscriptionsRequest',
    'ListDashboardsOrder',
    'ListDashboardsRequest',
    'ListDashboardsResponse',
    'ListQueriesRequest',
    'ListQueriesResponse',
    'ListSchedulesRequest',
    'ObjectId',
    'ObjectType',
    'ObjectTypeAndId',
    'ObjectTypePlural',
    'OwnableObjectType',
    'RefreshScheduleCron',
    'RefreshScheduleDataSourceId',
    'RefreshScheduleId',
    'RestoreDashboardRequest',
    'RestoreQueryRequest',
    'SetPermissionsRequest',
    'SetPermissionsResponse',
    'TransferOwnershipObjectId',
    'TransferOwnershipRequest',
    'UnsubscribeRequest',
    
    'Alerts',
    'Dashboards',
    'DataSources',
    'DbsqlPermissions',
    'Queries',
]

# all definitions in this file are in alphabetical order

@dataclass
class AccessControl:
    
    
    group_name: str = None
    
    permission_level: 'PermissionLevel' = None
    
    user_name: str = None

    def as_request(self) -> (dict, dict):
        accessControl_query, accessControl_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.group_name:
            accessControl_body['group_name'] = self.group_name
        if self.permission_level:
            accessControl_body['permission_level'] = self.permission_level.value
        if self.user_name:
            accessControl_body['user_name'] = self.user_name
        
        return accessControl_query, accessControl_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'AccessControl':
        return cls(
            group_name=d.get('group_name', None),
            permission_level=PermissionLevel(d['permission_level']) if 'permission_level' in d else None,
            user_name=d.get('user_name', None),
        )



@dataclass
class Alert:
    
    
    created_at: str = None
    # ID of the alert.
    id: str = None
    
    last_triggered_at: str = None
    # Name of the alert.
    name: str = None
    
    options: 'AlertOptions' = None
    
    query: 'Query' = None
    
    rearm: int = None
    
    state: 'AlertState' = None
    
    updated_at: str = None
    
    user: 'User' = None

    def as_request(self) -> (dict, dict):
        alert_query, alert_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.created_at:
            alert_body['created_at'] = self.created_at
        if self.id:
            alert_body['id'] = self.id
        if self.last_triggered_at:
            alert_body['last_triggered_at'] = self.last_triggered_at
        if self.name:
            alert_body['name'] = self.name
        if self.options:
            alert_body['options'] = self.options.as_request()[1]
        if self.query:
            alert_body['query'] = self.query.as_request()[1]
        if self.rearm:
            alert_body['rearm'] = self.rearm
        if self.state:
            alert_body['state'] = self.state.value
        if self.updated_at:
            alert_body['updated_at'] = self.updated_at
        if self.user:
            alert_body['user'] = self.user.as_request()[1]
        
        return alert_query, alert_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Alert':
        return cls(
            created_at=d.get('created_at', None),
            id=d.get('id', None),
            last_triggered_at=d.get('last_triggered_at', None),
            name=d.get('name', None),
            options=AlertOptions.from_dict(d['options']) if 'options' in d else None,
            query=Query.from_dict(d['query']) if 'query' in d else None,
            rearm=d.get('rearm', None),
            state=AlertState(d['state']) if 'state' in d else None,
            updated_at=d.get('updated_at', None),
            user=User.from_dict(d['user']) if 'user' in d else None,
        )



@dataclass
class AlertOptions:
    """Alert configuration options."""
    # Name of column in the query result to compare in alert evaluation.
    column: str
    # Operator used to compare in alert evaluation: `>`, `>=`, `<`, `<=`, `==`,
    # `!=`
    op: str
    # Value used to compare in alert evaluation.
    value: str
    # Custom body of alert notification, if it exists. See `%(alertsLink)s` for
    # custom templating instructions.
    custom_body: str = None
    # Custom subject of alert notification, if it exists. This includes email
    # subject, Slack notification header, etc. See `%(alertsLink)s` for custom
    # templating instructions.
    custom_subject: str = None
    # Whether or not the alert is muted. If an alert is muted, it will not
    # notify users and alert destinations when triggered.
    muted: bool = None
    # Number of failures encountered during alert refresh. This counter is used
    # for sending aggregated alert failure email notifications.
    schedule_failures: int = None

    def as_request(self) -> (dict, dict):
        alertOptions_query, alertOptions_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.column:
            alertOptions_body['column'] = self.column
        if self.custom_body:
            alertOptions_body['custom_body'] = self.custom_body
        if self.custom_subject:
            alertOptions_body['custom_subject'] = self.custom_subject
        if self.muted:
            alertOptions_body['muted'] = self.muted
        if self.op:
            alertOptions_body['op'] = self.op
        if self.schedule_failures:
            alertOptions_body['schedule_failures'] = self.schedule_failures
        if self.value:
            alertOptions_body['value'] = self.value
        
        return alertOptions_query, alertOptions_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'AlertOptions':
        return cls(
            column=d.get('column', None),
            custom_body=d.get('custom_body', None),
            custom_subject=d.get('custom_subject', None),
            muted=d.get('muted', None),
            op=d.get('op', None),
            schedule_failures=d.get('schedule_failures', None),
            value=d.get('value', None),
        )



@dataclass
class CreateRefreshSchedule:
    
    
    alert_id: str # path
    
    cron: str
    
    data_source_id: str = None

    def as_request(self) -> (dict, dict):
        createRefreshSchedule_query, createRefreshSchedule_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.alert_id:
            createRefreshSchedule_body['alert_id'] = self.alert_id
        if self.cron:
            createRefreshSchedule_body['cron'] = self.cron
        if self.data_source_id:
            createRefreshSchedule_body['data_source_id'] = self.data_source_id
        
        return createRefreshSchedule_query, createRefreshSchedule_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateRefreshSchedule':
        return cls(
            alert_id=d.get('alert_id', None),
            cron=d.get('cron', None),
            data_source_id=d.get('data_source_id', None),
        )



@dataclass
class CreateSubscription:
    
    
    alert_id: str # path
    
    destination_id: str = None
    
    user_id: int = None

    def as_request(self) -> (dict, dict):
        createSubscription_query, createSubscription_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.alert_id:
            createSubscription_body['alert_id'] = self.alert_id
        if self.destination_id:
            createSubscription_body['destination_id'] = self.destination_id
        if self.user_id:
            createSubscription_body['user_id'] = self.user_id
        
        return createSubscription_query, createSubscription_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateSubscription':
        return cls(
            alert_id=d.get('alert_id', None),
            destination_id=d.get('destination_id', None),
            user_id=d.get('user_id', None),
        )



@dataclass
class Dashboard:
    """A JSON representing a dashboard containing widgets of visualizations and
    text boxes."""
    # Whether the authenticated user can edit the query definition.
    can_edit: bool = None
    # Timestamp when this dashboard was created.
    created_at: str = None
    # In the web application, query filters that share a name are coupled to a
    # single selection box if this value is `true`.
    dashboard_filters_enabled: bool = None
    # The ID for this dashboard.
    id: str = None
    # Indicates whether a dashboard is trashed. Trashed dashboards won't appear
    # in list views. If this boolean is `true`, the `options` property for this
    # dashboard includes a `moved_to_trash_at` timestamp. Items in trash are
    # permanently deleted after 30 days.
    is_archived: bool = None
    # Whether a dashboard is a draft. Draft dashboards only appear in list views
    # for their owners.
    is_draft: bool = None
    # Indicates whether this query object appears in the current user's
    # favorites list. This flag determines whether the star icon for favorites
    # is selected.
    is_favorite: bool = None
    # The title of the dashboard that appears in list views and at the top of
    # the dashboard page.
    name: str = None
    
    options: 'DashboardOptions' = None
    
    permission_tier: 'PermissionLevel' = None
    # URL slug. Usually mirrors the query name with dashes (`-`) instead of
    # spaces. Appears in the URL for this query.
    slug: str = None
    
    tags: 'List[str]' = None
    # Timestamp when this dashboard was last updated.
    updated_at: str = None
    
    user: 'User' = None
    # The ID of the user that created and owns this dashboard.
    user_id: int = None
    
    widgets: 'List[Widget]' = None

    def as_request(self) -> (dict, dict):
        dashboard_query, dashboard_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.can_edit:
            dashboard_body['can_edit'] = self.can_edit
        if self.created_at:
            dashboard_body['created_at'] = self.created_at
        if self.dashboard_filters_enabled:
            dashboard_body['dashboard_filters_enabled'] = self.dashboard_filters_enabled
        if self.id:
            dashboard_body['id'] = self.id
        if self.is_archived:
            dashboard_body['is_archived'] = self.is_archived
        if self.is_draft:
            dashboard_body['is_draft'] = self.is_draft
        if self.is_favorite:
            dashboard_body['is_favorite'] = self.is_favorite
        if self.name:
            dashboard_body['name'] = self.name
        if self.options:
            dashboard_body['options'] = self.options.as_request()[1]
        if self.permission_tier:
            dashboard_body['permission_tier'] = self.permission_tier.value
        if self.slug:
            dashboard_body['slug'] = self.slug
        if self.tags:
            dashboard_body['tags'] = [v for v in self.tags]
        if self.updated_at:
            dashboard_body['updated_at'] = self.updated_at
        if self.user:
            dashboard_body['user'] = self.user.as_request()[1]
        if self.user_id:
            dashboard_body['user_id'] = self.user_id
        if self.widgets:
            dashboard_body['widgets'] = [v.as_request()[1] for v in self.widgets]
        
        return dashboard_query, dashboard_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Dashboard':
        return cls(
            can_edit=d.get('can_edit', None),
            created_at=d.get('created_at', None),
            dashboard_filters_enabled=d.get('dashboard_filters_enabled', None),
            id=d.get('id', None),
            is_archived=d.get('is_archived', None),
            is_draft=d.get('is_draft', None),
            is_favorite=d.get('is_favorite', None),
            name=d.get('name', None),
            options=DashboardOptions.from_dict(d['options']) if 'options' in d else None,
            permission_tier=PermissionLevel(d['permission_tier']) if 'permission_tier' in d else None,
            slug=d.get('slug', None),
            tags=d.get('tags', None),
            updated_at=d.get('updated_at', None),
            user=User.from_dict(d['user']) if 'user' in d else None,
            user_id=d.get('user_id', None),
            widgets=[Widget.from_dict(v) for v in d['widgets']] if 'widgets' in d else None,
        )



@dataclass
class DashboardOptions:
    
    # The timestamp when this dashboard was moved to trash. Only present when
    # the `is_archived` property is `true`. Trashed items are deleted after
    # thirty days.
    moved_to_trash_at: str = None

    def as_request(self) -> (dict, dict):
        dashboardOptions_query, dashboardOptions_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.moved_to_trash_at:
            dashboardOptions_body['moved_to_trash_at'] = self.moved_to_trash_at
        
        return dashboardOptions_query, dashboardOptions_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'DashboardOptions':
        return cls(
            moved_to_trash_at=d.get('moved_to_trash_at', None),
        )



@dataclass
class DataSource:
    """A JSON object representing a DBSQL data source / SQL warehouse."""
    # The unique identifier for this data source / SQL warehouse. Can be used
    # when creating / modifying queries and dashboards.
    id: str = None
    # The string name of this data source / SQL warehouse as it appears in the
    # Databricks SQL web application.
    name: str = None
    # <needs content>
    pause_reason: str = None
    # <needs content>
    paused: any /* MISSING TYPE */ = None
    # <needs content>
    supports_auto_limit: bool = None
    # <needs content>
    syntax: str = None
    # <needs content>
    type: str = None
    # <needs content>
    view_only: bool = None
    # <needs content>
    warehouse_id: str = None

    def as_request(self) -> (dict, dict):
        dataSource_query, dataSource_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.id:
            dataSource_body['id'] = self.id
        if self.name:
            dataSource_body['name'] = self.name
        if self.pause_reason:
            dataSource_body['pause_reason'] = self.pause_reason
        if self.paused:
            dataSource_body['paused'] = self.paused
        if self.supports_auto_limit:
            dataSource_body['supports_auto_limit'] = self.supports_auto_limit
        if self.syntax:
            dataSource_body['syntax'] = self.syntax
        if self.type:
            dataSource_body['type'] = self.type
        if self.view_only:
            dataSource_body['view_only'] = self.view_only
        if self.warehouse_id:
            dataSource_body['warehouse_id'] = self.warehouse_id
        
        return dataSource_query, dataSource_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'DataSource':
        return cls(
            id=d.get('id', None),
            name=d.get('name', None),
            pause_reason=d.get('pause_reason', None),
            paused=d.get('paused', None),
            supports_auto_limit=d.get('supports_auto_limit', None),
            syntax=d.get('syntax', None),
            type=d.get('type', None),
            view_only=d.get('view_only', None),
            warehouse_id=d.get('warehouse_id', None),
        )



@dataclass
class Destination:
    """Alert destination subscribed to the alert, if it exists. Alert destinations
    can be configured by admins through the UI. See `%(alertDestinationsLink)s`."""
    # ID of the alert destination.
    id: str = None
    # Name of the alert destination.
    name: str = None
    # Type of the alert destination.
    type: 'DestinationType' = None

    def as_request(self) -> (dict, dict):
        destination_query, destination_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.id:
            destination_body['id'] = self.id
        if self.name:
            destination_body['name'] = self.name
        if self.type:
            destination_body['type'] = self.type.value
        
        return destination_query, destination_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Destination':
        return cls(
            id=d.get('id', None),
            name=d.get('name', None),
            type=DestinationType(d['type']) if 'type' in d else None,
        )



class DestinationType(Enum):
    """Type of the alert destination."""
    
    email = 'email'
    hangouts_chat = 'hangouts_chat'
    mattermost = 'mattermost'
    microsoft_teams = 'microsoft_teams'
    pagerduty = 'pagerduty'
    slack = 'slack'
    webhook = 'webhook'

@dataclass
class EditAlert:
    
    
    name: str
    
    options: 'AlertOptions'
    
    query_id: str
    
    rearm: int = None

    def as_request(self) -> (dict, dict):
        editAlert_query, editAlert_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.name:
            editAlert_body['name'] = self.name
        if self.options:
            editAlert_body['options'] = self.options.as_request()[1]
        if self.query_id:
            editAlert_body['query_id'] = self.query_id
        if self.rearm:
            editAlert_body['rearm'] = self.rearm
        
        return editAlert_query, editAlert_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'EditAlert':
        return cls(
            name=d.get('name', None),
            options=AlertOptions.from_dict(d['options']) if 'options' in d else None,
            query_id=d.get('query_id', None),
            rearm=d.get('rearm', None),
        )



@dataclass
class Parameter:
    
    # The literal parameter marker that appears between double curly braces in
    # the query text.
    name: str = None
    # The text displayed in a parameter picking widget.
    title: str = None
    # Parameters can have several different types.
    type: 'ParameterType' = None
    # The default value for this parameter.
    value: str = None

    def as_request(self) -> (dict, dict):
        parameter_query, parameter_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.name:
            parameter_body['name'] = self.name
        if self.title:
            parameter_body['title'] = self.title
        if self.type:
            parameter_body['type'] = self.type.value
        if self.value:
            parameter_body['value'] = self.value
        
        return parameter_query, parameter_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Parameter':
        return cls(
            name=d.get('name', None),
            title=d.get('title', None),
            type=ParameterType(d['type']) if 'type' in d else None,
            value=d.get('value', None),
        )



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

@dataclass
class Query:
    
    # Describes whether the authenticated user is allowed to edit the definition
    # of this query.
    can_edit: bool = None
    # The timestamp when this query was created.
    created_at: str = None
    # Data Source ID. The UUID that uniquely identifies this data source / SQL
    # warehouse across the API.
    data_source_id: str = None
    # General description that conveys additional information about this query
    # such as usage notes.
    description: str = None
    
    id: str = None
    # Indicates whether the query is trashed. Trashed queries can't be used in
    # dashboards, or appear in search results. If this boolean is `true`, the
    # `options` property for this query includes a `moved_to_trash_at`
    # timestamp. Trashed queries are permanently deleted after 30 days.
    is_archived: bool = None
    # Whether the query is a draft. Draft queries only appear in list views for
    # their owners. Visualizations from draft queries cannot appear on
    # dashboards.
    is_draft: bool = None
    # Whether this query object appears in the current user's favorites list.
    # This flag determines whether the star icon for favorites is selected.
    is_favorite: bool = None
    # Text parameter types are not safe from SQL injection for all types of data
    # source. Set this Boolean parameter to `true` if a query either does not
    # use any text type parameters or uses a data source type where text type
    # parameters are handled safely.
    is_safe: bool = None
    
    last_modified_by: 'User' = None
    # The ID of the user who last saved changes to this query.
    last_modified_by_id: int = None
    # If there is a cached result for this query and user, this field includes
    # the query result ID. If this query uses parameters, this field is always
    # null.
    latest_query_data_id: str = None
    # The title of this query that appears in list views, widget headings, and
    # on the query page.
    name: str = None
    
    options: 'QueryOptions' = None
    
    permission_tier: 'PermissionLevel' = None
    # The text of the query to be run.
    query: str = None
    # A SHA-256 hash of the query text along with the authenticated user ID.
    query_hash: str = None
    
    schedule: 'QueryInterval' = None
    
    tags: 'List[str]' = None
    # The timestamp at which this query was last updated.
    updated_at: str = None
    
    user: 'User' = None
    # The ID of the user who created this query.
    user_id: int = None
    
    visualizations: 'List[Visualization]' = None

    def as_request(self) -> (dict, dict):
        query_query, query_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.can_edit:
            query_body['can_edit'] = self.can_edit
        if self.created_at:
            query_body['created_at'] = self.created_at
        if self.data_source_id:
            query_body['data_source_id'] = self.data_source_id
        if self.description:
            query_body['description'] = self.description
        if self.id:
            query_body['id'] = self.id
        if self.is_archived:
            query_body['is_archived'] = self.is_archived
        if self.is_draft:
            query_body['is_draft'] = self.is_draft
        if self.is_favorite:
            query_body['is_favorite'] = self.is_favorite
        if self.is_safe:
            query_body['is_safe'] = self.is_safe
        if self.last_modified_by:
            query_body['last_modified_by'] = self.last_modified_by.as_request()[1]
        if self.last_modified_by_id:
            query_body['last_modified_by_id'] = self.last_modified_by_id
        if self.latest_query_data_id:
            query_body['latest_query_data_id'] = self.latest_query_data_id
        if self.name:
            query_body['name'] = self.name
        if self.options:
            query_body['options'] = self.options.as_request()[1]
        if self.permission_tier:
            query_body['permission_tier'] = self.permission_tier.value
        if self.query:
            query_body['query'] = self.query
        if self.query_hash:
            query_body['query_hash'] = self.query_hash
        if self.schedule:
            query_body['schedule'] = self.schedule.as_request()[1]
        if self.tags:
            query_body['tags'] = [v for v in self.tags]
        if self.updated_at:
            query_body['updated_at'] = self.updated_at
        if self.user:
            query_body['user'] = self.user.as_request()[1]
        if self.user_id:
            query_body['user_id'] = self.user_id
        if self.visualizations:
            query_body['visualizations'] = [v.as_request()[1] for v in self.visualizations]
        
        return query_query, query_body

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
            permission_tier=PermissionLevel(d['permission_tier']) if 'permission_tier' in d else None,
            query=d.get('query', None),
            query_hash=d.get('query_hash', None),
            schedule=QueryInterval.from_dict(d['schedule']) if 'schedule' in d else None,
            tags=d.get('tags', None),
            updated_at=d.get('updated_at', None),
            user=User.from_dict(d['user']) if 'user' in d else None,
            user_id=d.get('user_id', None),
            visualizations=[Visualization.from_dict(v) for v in d['visualizations']] if 'visualizations' in d else None,
        )



@dataclass
class QueryInterval:
    
    # For weekly runs, the day of the week to start the run.
    day_of_week: any /* MISSING TYPE */ = None
    # Integer number of seconds between runs.
    interval: int = None
    # For daily, weekly, and monthly runs, the time of day to start the run.
    time: any /* MISSING TYPE */ = None
    # A date after which this schedule no longer applies.
    until: any /* MISSING TYPE */ = None

    def as_request(self) -> (dict, dict):
        queryInterval_query, queryInterval_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.day_of_week:
            queryInterval_body['day_of_week'] = self.day_of_week
        if self.interval:
            queryInterval_body['interval'] = self.interval
        if self.time:
            queryInterval_body['time'] = self.time
        if self.until:
            queryInterval_body['until'] = self.until
        
        return queryInterval_query, queryInterval_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'QueryInterval':
        return cls(
            day_of_week=d.get('day_of_week', None),
            interval=d.get('interval', None),
            time=d.get('time', None),
            until=d.get('until', None),
        )



@dataclass
class QueryOptions:
    
    # The timestamp when this query was moved to trash. Only present when the
    # `is_archived` property is `true`. Trashed items are deleted after thirty
    # days.
    moved_to_trash_at: str = None
    
    parameters: 'List[Parameter]' = None

    def as_request(self) -> (dict, dict):
        queryOptions_query, queryOptions_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.moved_to_trash_at:
            queryOptions_body['moved_to_trash_at'] = self.moved_to_trash_at
        if self.parameters:
            queryOptions_body['parameters'] = [v.as_request()[1] for v in self.parameters]
        
        return queryOptions_query, queryOptions_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'QueryOptions':
        return cls(
            moved_to_trash_at=d.get('moved_to_trash_at', None),
            parameters=[Parameter.from_dict(v) for v in d['parameters']] if 'parameters' in d else None,
        )



@dataclass
class QueryPostContent:
    
    
    query_id: str # path
    # The ID of the data source / SQL warehouse where this query will run.
    data_source_id: str = None
    # General description that can convey additional information about this
    # query such as usage notes.
    description: str = None
    # The name or title of this query to display in list views.
    name: str = None
    # Exclusively used for storing a list parameter definitions. A parameter is
    # an object with `title`, `name`, `type`, and `value` properties. The
    # `value` field here is the default value. It can be overridden at runtime.
    options: any /* MISSING TYPE */ = None
    # The text of the query.
    query: str = None
    # JSON object that describes the scheduled execution frequency. A schedule
    # object includes `interval`, `time`, `day_of_week`, and `until` fields. If
    # a scheduled is supplied, then only `interval` is required. All other field
    # can be `null`.
    schedule: 'QueryInterval' = None

    def as_request(self) -> (dict, dict):
        queryPostContent_query, queryPostContent_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.data_source_id:
            queryPostContent_body['data_source_id'] = self.data_source_id
        if self.description:
            queryPostContent_body['description'] = self.description
        if self.name:
            queryPostContent_body['name'] = self.name
        if self.options:
            queryPostContent_body['options'] = self.options
        if self.query:
            queryPostContent_body['query'] = self.query
        if self.query_id:
            queryPostContent_body['query_id'] = self.query_id
        if self.schedule:
            queryPostContent_body['schedule'] = self.schedule.as_request()[1]
        
        return queryPostContent_query, queryPostContent_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'QueryPostContent':
        return cls(
            data_source_id=d.get('data_source_id', None),
            description=d.get('description', None),
            name=d.get('name', None),
            options=d.get('options', None),
            query=d.get('query', None),
            query_id=d.get('query_id', None),
            schedule=QueryInterval.from_dict(d['schedule']) if 'schedule' in d else None,
        )



@dataclass
class RefreshSchedule:
    
    
    cron: str = None
    
    data_source_id: str = None
    
    id: str = None

    def as_request(self) -> (dict, dict):
        refreshSchedule_query, refreshSchedule_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.cron:
            refreshSchedule_body['cron'] = self.cron
        if self.data_source_id:
            refreshSchedule_body['data_source_id'] = self.data_source_id
        if self.id:
            refreshSchedule_body['id'] = self.id
        
        return refreshSchedule_query, refreshSchedule_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'RefreshSchedule':
        return cls(
            cron=d.get('cron', None),
            data_source_id=d.get('data_source_id', None),
            id=d.get('id', None),
        )



@dataclass
class Subscription:
    
    
    alert_id: str = None
    
    destination: 'Destination' = None
    
    id: str = None
    
    user: 'User' = None

    def as_request(self) -> (dict, dict):
        subscription_query, subscription_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.alert_id:
            subscription_body['alert_id'] = self.alert_id
        if self.destination:
            subscription_body['destination'] = self.destination.as_request()[1]
        if self.id:
            subscription_body['id'] = self.id
        if self.user:
            subscription_body['user'] = self.user.as_request()[1]
        
        return subscription_query, subscription_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Subscription':
        return cls(
            alert_id=d.get('alert_id', None),
            destination=Destination.from_dict(d['destination']) if 'destination' in d else None,
            id=d.get('id', None),
            user=User.from_dict(d['user']) if 'user' in d else None,
        )



@dataclass
class Success:
    
    
    message: 'SuccessMessage' = None

    def as_request(self) -> (dict, dict):
        success_query, success_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.message:
            success_body['message'] = self.message.value
        
        return success_query, success_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Success':
        return cls(
            message=SuccessMessage(d['message']) if 'message' in d else None,
        )



class SuccessMessage(Enum):
    
    
    Success = 'Success'



@dataclass
class User:
    
    
    email: str = None
    
    id: int = None
    # Whether this user is an admin in the Databricks workspace.
    is_db_admin: bool = None
    
    name: str = None
    # The URL for the gravatar profile picture tied to this user's email
    # address.
    profile_image_url: str = None

    def as_request(self) -> (dict, dict):
        user_query, user_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.email:
            user_body['email'] = self.email
        if self.id:
            user_body['id'] = self.id
        if self.is_db_admin:
            user_body['is_db_admin'] = self.is_db_admin
        if self.name:
            user_body['name'] = self.name
        if self.profile_image_url:
            user_body['profile_image_url'] = self.profile_image_url
        
        return user_query, user_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'User':
        return cls(
            email=d.get('email', None),
            id=d.get('id', None),
            is_db_admin=d.get('is_db_admin', None),
            name=d.get('name', None),
            profile_image_url=d.get('profile_image_url', None),
        )



@dataclass
class Visualization:
    """The visualization description API changes frequently and is unsupported. You
    can duplicate a visualization by copying description objects received _from
    the API_ and then using them to create a new one with a POST request to the
    same endpoint. Databricks does not recommend constructing ad-hoc
    visualizations entirely in JSON."""
    
    created_at: str = None
    # A short description of this visualization. This is not displayed in the
    # UI.
    description: str = None
    # The UUID for this visualization.
    id: str = None
    # The name of the visualization that appears on dashboards and the query
    # screen.
    name: str = None
    # The options object varies widely from one visualization type to the next
    # and is unsupported. Databricks does not recommend modifying visualization
    # settings in JSON.
    options: any /* MISSING TYPE */ = None
    # The type of visualization: chart, table, pivot table, and so on.
    type: str = None
    
    updated_at: str = None

    def as_request(self) -> (dict, dict):
        visualization_query, visualization_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.created_at:
            visualization_body['created_at'] = self.created_at
        if self.description:
            visualization_body['description'] = self.description
        if self.id:
            visualization_body['id'] = self.id
        if self.name:
            visualization_body['name'] = self.name
        if self.options:
            visualization_body['options'] = self.options
        if self.type:
            visualization_body['type'] = self.type
        if self.updated_at:
            visualization_body['updated_at'] = self.updated_at
        
        return visualization_query, visualization_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Visualization':
        return cls(
            created_at=d.get('created_at', None),
            description=d.get('description', None),
            id=d.get('id', None),
            name=d.get('name', None),
            options=d.get('options', None),
            type=d.get('type', None),
            updated_at=d.get('updated_at', None),
        )



@dataclass
class Widget:
    
    # The unique ID for this widget.
    id: int = None
    
    options: 'WidgetOptions' = None
    
    visualization: 'Visualization' = None
    # Unused field.
    width: int = None

    def as_request(self) -> (dict, dict):
        widget_query, widget_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.id:
            widget_body['id'] = self.id
        if self.options:
            widget_body['options'] = self.options.as_request()[1]
        if self.visualization:
            widget_body['visualization'] = self.visualization.as_request()[1]
        if self.width:
            widget_body['width'] = self.width
        
        return widget_query, widget_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Widget':
        return cls(
            id=d.get('id', None),
            options=WidgetOptions.from_dict(d['options']) if 'options' in d else None,
            visualization=Visualization.from_dict(d['visualization']) if 'visualization' in d else None,
            width=d.get('width', None),
        )



@dataclass
class WidgetOptions:
    
    # Timestamp when this object was created
    created_at: str = None
    # The dashboard ID to which this widget belongs. Each widget can belong to
    # one dashboard.
    dashboard_id: str = None
    # Whether this widget is hidden on the dashboard.
    isHidden: bool = None
    # How parameters used by the visualization in this widget relate to other
    # widgets on the dashboard. Databricks does not recommend modifying this
    # definition in JSON.
    parameterMappings: any /* MISSING TYPE */ = None
    # Coordinates of this widget on a dashboard. This portion of the API changes
    # frequently and is unsupported.
    position: any /* MISSING TYPE */ = None
    # If this is a textbox widget, the application displays this text. This
    # field is ignored if the widget contains a visualization in the
    # `visualization` field.
    text: str = None
    # Timestamp of the last time this object was updated.
    updated_at: str = None

    def as_request(self) -> (dict, dict):
        widgetOptions_query, widgetOptions_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.created_at:
            widgetOptions_body['created_at'] = self.created_at
        if self.dashboard_id:
            widgetOptions_body['dashboard_id'] = self.dashboard_id
        if self.isHidden:
            widgetOptions_body['isHidden'] = self.isHidden
        if self.parameterMappings:
            widgetOptions_body['parameterMappings'] = self.parameterMappings
        if self.position:
            widgetOptions_body['position'] = self.position
        if self.text:
            widgetOptions_body['text'] = self.text
        if self.updated_at:
            widgetOptions_body['updated_at'] = self.updated_at
        
        return widgetOptions_query, widgetOptions_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'WidgetOptions':
        return cls(
            created_at=d.get('created_at', None),
            dashboard_id=d.get('dashboard_id', None),
            isHidden=d.get('isHidden', None),
            parameterMappings=d.get('parameterMappings', None),
            position=d.get('position', None),
            text=d.get('text', None),
            updated_at=d.get('updated_at', None),
        )















class AlertState(Enum):
    """State of the alert. Possible values are: `unknown` (yet to be evaluated),
    `triggered` (evaluated and fulfilled trigger conditions), or `ok` (evaluated
    and did not fulfill trigger conditions)."""
    
    ok = 'ok'
    triggered = 'triggered'
    unknown = 'unknown'









@dataclass
class CreateDashboardRequest:
    
    # In the web application, query filters that share a name are coupled to a
    # single selection box if this value is true.
    dashboard_filters_enabled: bool = None
    # Draft dashboards only appear in list views for their owners.
    is_draft: bool = None
    # Indicates whether the dashboard is trashed. Trashed dashboards don't
    # appear in list views.
    is_trashed: bool = None
    # The title of this dashboard that appears in list views and at the top of
    # the dashboard page.
    name: str = None
    
    tags: 'List[str]' = None
    # An array of widget objects. A complete description of widget objects can
    # be found in the response to [Retrieve A Dashboard
    # Definition](#operation/sql-analytics-fetch-dashboard). Databricks does not
    # recommend creating new widgets via this API.
    widgets: 'List[Widget]' = None

    def as_request(self) -> (dict, dict):
        createDashboardRequest_query, createDashboardRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.dashboard_filters_enabled:
            createDashboardRequest_body['dashboard_filters_enabled'] = self.dashboard_filters_enabled
        if self.is_draft:
            createDashboardRequest_body['is_draft'] = self.is_draft
        if self.is_trashed:
            createDashboardRequest_body['is_trashed'] = self.is_trashed
        if self.name:
            createDashboardRequest_body['name'] = self.name
        if self.tags:
            createDashboardRequest_body['tags'] = [v for v in self.tags]
        if self.widgets:
            createDashboardRequest_body['widgets'] = [v.as_request()[1] for v in self.widgets]
        
        return createDashboardRequest_query, createDashboardRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateDashboardRequest':
        return cls(
            dashboard_filters_enabled=d.get('dashboard_filters_enabled', None),
            is_draft=d.get('is_draft', None),
            is_trashed=d.get('is_trashed', None),
            name=d.get('name', None),
            tags=d.get('tags', None),
            widgets=[Widget.from_dict(v) for v in d['widgets']] if 'widgets' in d else None,
        )



@dataclass
class DeleteAlertRequest:
    
    
    alert_id: str # path

    def as_request(self) -> (dict, dict):
        deleteAlertRequest_query, deleteAlertRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.alert_id:
            deleteAlertRequest_body['alert_id'] = self.alert_id
        
        return deleteAlertRequest_query, deleteAlertRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'DeleteAlertRequest':
        return cls(
            alert_id=d.get('alert_id', None),
        )



@dataclass
class DeleteDashboardRequest:
    
    
    dashboard_id: str # path

    def as_request(self) -> (dict, dict):
        deleteDashboardRequest_query, deleteDashboardRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.dashboard_id:
            deleteDashboardRequest_body['dashboard_id'] = self.dashboard_id
        
        return deleteDashboardRequest_query, deleteDashboardRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'DeleteDashboardRequest':
        return cls(
            dashboard_id=d.get('dashboard_id', None),
        )



@dataclass
class DeleteQueryRequest:
    
    
    query_id: str # path

    def as_request(self) -> (dict, dict):
        deleteQueryRequest_query, deleteQueryRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.query_id:
            deleteQueryRequest_body['query_id'] = self.query_id
        
        return deleteQueryRequest_query, deleteQueryRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'DeleteQueryRequest':
        return cls(
            query_id=d.get('query_id', None),
        )



@dataclass
class DeleteScheduleRequest:
    
    
    alert_id: str # path
    
    schedule_id: str # path

    def as_request(self) -> (dict, dict):
        deleteScheduleRequest_query, deleteScheduleRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.alert_id:
            deleteScheduleRequest_body['alert_id'] = self.alert_id
        if self.schedule_id:
            deleteScheduleRequest_body['schedule_id'] = self.schedule_id
        
        return deleteScheduleRequest_query, deleteScheduleRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'DeleteScheduleRequest':
        return cls(
            alert_id=d.get('alert_id', None),
            schedule_id=d.get('schedule_id', None),
        )



@dataclass
class GetAlertRequest:
    
    
    alert_id: str # path

    def as_request(self) -> (dict, dict):
        getAlertRequest_query, getAlertRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.alert_id:
            getAlertRequest_body['alert_id'] = self.alert_id
        
        return getAlertRequest_query, getAlertRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetAlertRequest':
        return cls(
            alert_id=d.get('alert_id', None),
        )



@dataclass
class GetDashboardRequest:
    
    
    dashboard_id: str # path

    def as_request(self) -> (dict, dict):
        getDashboardRequest_query, getDashboardRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.dashboard_id:
            getDashboardRequest_body['dashboard_id'] = self.dashboard_id
        
        return getDashboardRequest_query, getDashboardRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetDashboardRequest':
        return cls(
            dashboard_id=d.get('dashboard_id', None),
        )



@dataclass
class GetPermissionsRequest:
    
    # Object ID. An ACL is returned for the object with this UUID.
    objectId: str # path
    # The type of object permissions to check.
    objectType: 'ObjectTypePlural' # path

    def as_request(self) -> (dict, dict):
        getPermissionsRequest_query, getPermissionsRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.objectId:
            getPermissionsRequest_body['objectId'] = self.objectId
        if self.objectType:
            getPermissionsRequest_body['objectType'] = self.objectType.value
        
        return getPermissionsRequest_query, getPermissionsRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetPermissionsRequest':
        return cls(
            objectId=d.get('objectId', None),
            objectType=ObjectTypePlural(d['objectType']) if 'objectType' in d else None,
        )



@dataclass
class GetPermissionsResponse:
    
    
    access_control_list: 'List[AccessControl]' = None
    
    object_id: 'ObjectType' = None
    
    object_type: str = None

    def as_request(self) -> (dict, dict):
        getPermissionsResponse_query, getPermissionsResponse_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.access_control_list:
            getPermissionsResponse_body['access_control_list'] = [v.as_request()[1] for v in self.access_control_list]
        if self.object_id:
            getPermissionsResponse_body['object_id'] = self.object_id.value
        if self.object_type:
            getPermissionsResponse_body['object_type'] = self.object_type
        
        return getPermissionsResponse_query, getPermissionsResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetPermissionsResponse':
        return cls(
            access_control_list=[AccessControl.from_dict(v) for v in d['access_control_list']] if 'access_control_list' in d else None,
            object_id=ObjectType(d['object_id']) if 'object_id' in d else None,
            object_type=d.get('object_type', None),
        )



@dataclass
class GetQueryRequest:
    
    
    query_id: str # path

    def as_request(self) -> (dict, dict):
        getQueryRequest_query, getQueryRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.query_id:
            getQueryRequest_body['query_id'] = self.query_id
        
        return getQueryRequest_query, getQueryRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetQueryRequest':
        return cls(
            query_id=d.get('query_id', None),
        )



@dataclass
class GetSubscriptionsRequest:
    
    
    alert_id: str # path

    def as_request(self) -> (dict, dict):
        getSubscriptionsRequest_query, getSubscriptionsRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.alert_id:
            getSubscriptionsRequest_body['alert_id'] = self.alert_id
        
        return getSubscriptionsRequest_query, getSubscriptionsRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetSubscriptionsRequest':
        return cls(
            alert_id=d.get('alert_id', None),
        )



class ListDashboardsOrder(Enum):
    
    
    created_at = 'created_at'
    name = 'name'

@dataclass
class ListDashboardsRequest:
    
    # Name of dashboard attribute to order by.
    order: 'ListDashboardsOrder' = None # query
    # Page number to retrieve.
    page: int = None # query
    # Number of dashboards to return per page.
    page_size: int = None # query
    # Full text search term.
    q: str = None # query

    def as_request(self) -> (dict, dict):
        listDashboardsRequest_query, listDashboardsRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.order:
            listDashboardsRequest_query['order'] = self.order.value
        if self.page:
            listDashboardsRequest_query['page'] = self.page
        if self.page_size:
            listDashboardsRequest_query['page_size'] = self.page_size
        if self.q:
            listDashboardsRequest_query['q'] = self.q
        
        return listDashboardsRequest_query, listDashboardsRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListDashboardsRequest':
        return cls(
            order=ListDashboardsOrder(d['order']) if 'order' in d else None,
            page=d.get('page', None),
            page_size=d.get('page_size', None),
            q=d.get('q', None),
        )



@dataclass
class ListDashboardsResponse:
    
    # The total number of dashboards.
    count: int = None
    # The current page being displayed.
    page: int = None
    # The number of dashboards per page.
    page_size: int = None
    # List of dashboards returned.
    results: 'List[Dashboard]' = None

    def as_request(self) -> (dict, dict):
        listDashboardsResponse_query, listDashboardsResponse_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.count:
            listDashboardsResponse_body['count'] = self.count
        if self.page:
            listDashboardsResponse_body['page'] = self.page
        if self.page_size:
            listDashboardsResponse_body['page_size'] = self.page_size
        if self.results:
            listDashboardsResponse_body['results'] = [v.as_request()[1] for v in self.results]
        
        return listDashboardsResponse_query, listDashboardsResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListDashboardsResponse':
        return cls(
            count=d.get('count', None),
            page=d.get('page', None),
            page_size=d.get('page_size', None),
            results=[Dashboard.from_dict(v) for v in d['results']] if 'results' in d else None,
        )



@dataclass
class ListQueriesRequest:
    
    # Name of query attribute to order by. Default sort order is ascending.
    # Append a dash (`-`) to order descending instead.
    # 
    # - `name`: The name of the query.
    # 
    # - `created_at`: The timestamp the query was created.
    # 
    # - `schedule`: The refresh interval for each query. For example: "Every 5
    # Hours" or "Every 5 Minutes". "Never" is treated as the highest value for
    # sorting.
    # 
    # - `runtime`: The time it took to run this query. This is blank for
    # parameterized queries. A blank value is treated as the highest value for
    # sorting.
    # 
    # - `executed_at`: The timestamp when the query was last run.
    # 
    # - `created_by`: The user name of the user that created the query.
    order: str = None # query
    # Page number to retrieve.
    page: int = None # query
    # Number of queries to return per page.
    page_size: int = None # query
    # Full text search term
    q: str = None # query

    def as_request(self) -> (dict, dict):
        listQueriesRequest_query, listQueriesRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.order:
            listQueriesRequest_query['order'] = self.order
        if self.page:
            listQueriesRequest_query['page'] = self.page
        if self.page_size:
            listQueriesRequest_query['page_size'] = self.page_size
        if self.q:
            listQueriesRequest_query['q'] = self.q
        
        return listQueriesRequest_query, listQueriesRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListQueriesRequest':
        return cls(
            order=d.get('order', None),
            page=d.get('page', None),
            page_size=d.get('page_size', None),
            q=d.get('q', None),
        )



@dataclass
class ListQueriesResponse:
    
    # The total number of queries.
    count: int = None
    # The page number that is currently displayed.
    page: int = None
    # The number of queries per page.
    page_size: int = None
    # List of queries returned.
    results: 'List[Query]' = None

    def as_request(self) -> (dict, dict):
        listQueriesResponse_query, listQueriesResponse_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.count:
            listQueriesResponse_body['count'] = self.count
        if self.page:
            listQueriesResponse_body['page'] = self.page
        if self.page_size:
            listQueriesResponse_body['page_size'] = self.page_size
        if self.results:
            listQueriesResponse_body['results'] = [v.as_request()[1] for v in self.results]
        
        return listQueriesResponse_query, listQueriesResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListQueriesResponse':
        return cls(
            count=d.get('count', None),
            page=d.get('page', None),
            page_size=d.get('page_size', None),
            results=[Query.from_dict(v) for v in d['results']] if 'results' in d else None,
        )



@dataclass
class ListSchedulesRequest:
    
    
    alert_id: str # path

    def as_request(self) -> (dict, dict):
        listSchedulesRequest_query, listSchedulesRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.alert_id:
            listSchedulesRequest_body['alert_id'] = self.alert_id
        
        return listSchedulesRequest_query, listSchedulesRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListSchedulesRequest':
        return cls(
            alert_id=d.get('alert_id', None),
        )





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

class OwnableObjectType(Enum):
    """The singular form of the type of object which can be owned."""
    
    alert = 'alert'
    dashboard = 'dashboard'
    query = 'query'







@dataclass
class RestoreDashboardRequest:
    
    
    dashboard_id: str # path

    def as_request(self) -> (dict, dict):
        restoreDashboardRequest_query, restoreDashboardRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.dashboard_id:
            restoreDashboardRequest_body['dashboard_id'] = self.dashboard_id
        
        return restoreDashboardRequest_query, restoreDashboardRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'RestoreDashboardRequest':
        return cls(
            dashboard_id=d.get('dashboard_id', None),
        )



@dataclass
class RestoreQueryRequest:
    
    
    query_id: str # path

    def as_request(self) -> (dict, dict):
        restoreQueryRequest_query, restoreQueryRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.query_id:
            restoreQueryRequest_body['query_id'] = self.query_id
        
        return restoreQueryRequest_query, restoreQueryRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'RestoreQueryRequest':
        return cls(
            query_id=d.get('query_id', None),
        )



@dataclass
class SetPermissionsRequest:
    
    # Object ID. The ACL for the object with this UUID is overwritten by this
    # request's POST content.
    objectId: str # path
    # The type of object permission to set.
    objectType: 'ObjectTypePlural' # path
    
    access_control_list: 'List[AccessControl]' = None

    def as_request(self) -> (dict, dict):
        setPermissionsRequest_query, setPermissionsRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.access_control_list:
            setPermissionsRequest_body['access_control_list'] = [v.as_request()[1] for v in self.access_control_list]
        if self.objectId:
            setPermissionsRequest_body['objectId'] = self.objectId
        if self.objectType:
            setPermissionsRequest_body['objectType'] = self.objectType.value
        
        return setPermissionsRequest_query, setPermissionsRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'SetPermissionsRequest':
        return cls(
            access_control_list=[AccessControl.from_dict(v) for v in d['access_control_list']] if 'access_control_list' in d else None,
            objectId=d.get('objectId', None),
            objectType=ObjectTypePlural(d['objectType']) if 'objectType' in d else None,
        )



@dataclass
class SetPermissionsResponse:
    
    
    access_control_list: 'List[AccessControl]' = None
    
    object_id: 'ObjectType' = None
    
    object_type: str = None

    def as_request(self) -> (dict, dict):
        setPermissionsResponse_query, setPermissionsResponse_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.access_control_list:
            setPermissionsResponse_body['access_control_list'] = [v.as_request()[1] for v in self.access_control_list]
        if self.object_id:
            setPermissionsResponse_body['object_id'] = self.object_id.value
        if self.object_type:
            setPermissionsResponse_body['object_type'] = self.object_type
        
        return setPermissionsResponse_query, setPermissionsResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'SetPermissionsResponse':
        return cls(
            access_control_list=[AccessControl.from_dict(v) for v in d['access_control_list']] if 'access_control_list' in d else None,
            object_id=ObjectType(d['object_id']) if 'object_id' in d else None,
            object_type=d.get('object_type', None),
        )



@dataclass
class TransferOwnershipObjectId:
    
    # Email address for the new owner, who must exist in the workspace.
    new_owner: str = None

    def as_request(self) -> (dict, dict):
        transferOwnershipObjectId_query, transferOwnershipObjectId_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.new_owner:
            transferOwnershipObjectId_body['new_owner'] = self.new_owner
        
        return transferOwnershipObjectId_query, transferOwnershipObjectId_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'TransferOwnershipObjectId':
        return cls(
            new_owner=d.get('new_owner', None),
        )



@dataclass
class TransferOwnershipRequest:
    
    # The ID of the object on which to change ownership.
    objectId: 'TransferOwnershipObjectId' # path
    # The type of object on which to change ownership.
    objectType: 'OwnableObjectType' # path
    # Email address for the new owner, who must exist in the workspace.
    new_owner: str = None

    def as_request(self) -> (dict, dict):
        transferOwnershipRequest_query, transferOwnershipRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.new_owner:
            transferOwnershipRequest_body['new_owner'] = self.new_owner
        if self.objectId:
            transferOwnershipRequest_body['objectId'] = self.objectId.as_request()[1]
        if self.objectType:
            transferOwnershipRequest_body['objectType'] = self.objectType.value
        
        return transferOwnershipRequest_query, transferOwnershipRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'TransferOwnershipRequest':
        return cls(
            new_owner=d.get('new_owner', None),
            objectId=TransferOwnershipObjectId.from_dict(d['objectId']) if 'objectId' in d else None,
            objectType=OwnableObjectType(d['objectType']) if 'objectType' in d else None,
        )



@dataclass
class UnsubscribeRequest:
    
    
    alert_id: str # path
    
    subscription_id: str # path

    def as_request(self) -> (dict, dict):
        unsubscribeRequest_query, unsubscribeRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.alert_id:
            unsubscribeRequest_body['alert_id'] = self.alert_id
        if self.subscription_id:
            unsubscribeRequest_body['subscription_id'] = self.subscription_id
        
        return unsubscribeRequest_query, unsubscribeRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'UnsubscribeRequest':
        return cls(
            alert_id=d.get('alert_id', None),
            subscription_id=d.get('subscription_id', None),
        )



class AlertsAPI:
    def __init__(self, api_client):
        self._api = api_client
    
    def createAlert(self, request: EditAlert) -> Alert:
        """Create an alert
        
        Creates an alert. An alert is a Databricks SQL object that periodically
        runs a query, evaluates a condition of its result, and notifies users or
        alert destinations if the condition was met."""
        query, body = request.as_request()
        json = self._api.do('POST', '/api/2.0/preview/sql/alerts', query=query, body=body)
        return Alert.from_dict(json)
    
    def createSchedule(self, request: CreateRefreshSchedule) -> RefreshSchedule:
        """Create a refresh schedule
        
        Creates a new refresh schedule for an alert.
        
        **Note:** The structure of refresh schedules is subject to change."""
        query, body = request.as_request()
        json = self._api.do('POST', f'/api/2.0/preview/sql/alerts/{request.alert_id}/refresh-schedules', query=query, body=body)
        return RefreshSchedule.from_dict(json)
    
    def deleteAlert(self, request: DeleteAlertRequest):
        """Delete an alert
        
        Deletes an alert. Deleted alerts are no longer accessible and cannot be
        restored. **Note:** Unlike queries and dashboards, alerts cannot be
        moved to the trash."""
        query, body = request.as_request()
        self._api.do('DELETE', f'/api/2.0/preview/sql/alerts/{request.alert_id}', query=query, body=body)
        
    
    def deleteSchedule(self, request: DeleteScheduleRequest):
        """Delete a refresh schedule
        
        Deletes an alert's refresh schedule. The refresh schedule specifies when
        to refresh and evaluate the associated query result."""
        query, body = request.as_request()
        self._api.do('DELETE', f'/api/2.0/preview/sql/alerts/{request.alert_id}/refresh-schedules/{request.schedule_id}', query=query, body=body)
        
    
    def getAlert(self, request: GetAlertRequest) -> Alert:
        """Get an alert
        
        Gets an alert."""
        query, body = request.as_request()
        json = self._api.do('GET', f'/api/2.0/preview/sql/alerts/{request.alert_id}', query=query, body=body)
        return Alert.from_dict(json)
    
    def getSubscriptions(self, request: GetSubscriptionsRequest) -> SubscriptionList:
        """Get an alert's subscriptions
        
        Get the subscriptions for an alert. An alert subscription represents
        exactly one recipient being notified whenever the alert is triggered.
        The alert recipient is specified by either the `user` field or the
        `destination` field. The `user` field is ignored if `destination` is
        non-`null`."""
        query, body = request.as_request()
        json = self._api.do('GET', f'/api/2.0/preview/sql/alerts/{request.alert_id}/subscriptions', query=query, body=body)
        return SubscriptionList.from_dict(json)
    
    def listAlerts(self) -> AlertList:
        """Get alerts
        
        Gets a list of alerts."""
        
        json = self._api.do('GET', '/api/2.0/preview/sql/alerts')
        return AlertList.from_dict(json)
    
    def listSchedules(self, request: ListSchedulesRequest) -> RefreshScheduleList:
        """Get refresh schedules
        
        Gets the refresh schedules for the specified alert. Alerts can have
        refresh schedules that specify when to refresh and evaluate the
        associated query result.
        
        **Note:** Although refresh schedules are returned in a list, only one
        refresh schedule per alert is currently supported. The structure of
        refresh schedules is subject to change."""
        query, body = request.as_request()
        json = self._api.do('GET', f'/api/2.0/preview/sql/alerts/{request.alert_id}/refresh-schedules', query=query, body=body)
        return RefreshScheduleList.from_dict(json)
    
    def subscribe(self, request: CreateSubscription) -> Subscription:
        """Subscribe to an alert"""
        query, body = request.as_request()
        json = self._api.do('POST', f'/api/2.0/preview/sql/alerts/{request.alert_id}/subscriptions', query=query, body=body)
        return Subscription.from_dict(json)
    
    def unsubscribe(self, request: UnsubscribeRequest):
        """Unsubscribe to an alert
        
        Unsubscribes a user or a destination to an alert."""
        query, body = request.as_request()
        self._api.do('DELETE', f'/api/2.0/preview/sql/alerts/{request.alert_id}/subscriptions/{request.subscription_id}', query=query, body=body)
        
    
    def updateAlert(self, request: EditAlert):
        """Update an alert
        
        Updates an alert."""
        query, body = request.as_request()
        self._api.do('PUT', f'/api/2.0/preview/sql/alerts/{request.alert_id}', query=query, body=body)
        
    
class DashboardsAPI:
    def __init__(self, api_client):
        self._api = api_client
    
    def createDashboard(self, request: CreateDashboardRequest) -> Dashboard:
        """Create a dashboard object"""
        query, body = request.as_request()
        json = self._api.do('POST', '/api/2.0/preview/sql/dashboards', query=query, body=body)
        return Dashboard.from_dict(json)
    
    def deleteDashboard(self, request: DeleteDashboardRequest):
        """Remove a dashboard
        
        Moves a dashboard to the trash. Trashed dashboards do not appear in list
        views or searches, and cannot be shared."""
        query, body = request.as_request()
        self._api.do('DELETE', f'/api/2.0/preview/sql/dashboards/{request.dashboard_id}', query=query, body=body)
        
    
    def getDashboard(self, request: GetDashboardRequest) -> Dashboard:
        """Retrieve a definition
        
        Returns a JSON representation of a dashboard object, including its
        visualization and query objects."""
        query, body = request.as_request()
        json = self._api.do('GET', f'/api/2.0/preview/sql/dashboards/{request.dashboard_id}', query=query, body=body)
        return Dashboard.from_dict(json)
    
    def listDashboards(self, request: ListDashboardsRequest) -> ListDashboardsResponse:
        """Get dashboard objects
        
        Fetch a paginated list of dashboard objects."""
        query, body = request.as_request()
        json = self._api.do('GET', '/api/2.0/preview/sql/dashboards', query=query, body=body)
        return ListDashboardsResponse.from_dict(json)
    
    def restoreDashboard(self, request: RestoreDashboardRequest):
        """Restore a dashboard
        
        A restored dashboard appears in list views and searches and can be
        shared."""
        query, body = request.as_request()
        self._api.do('POST', f'/api/2.0/preview/sql/dashboards/trash/{request.dashboard_id}', query=query, body=body)
        
    
class DataSourcesAPI:
    def __init__(self, api_client):
        self._api = api_client
    
    def listDataSources(self) -> DataSourceList:
        """Get a list of SQL warehouses
        
        Retrieves a full list of SQL warehouses available in this workspace. All
        fields that appear in this API response are enumerated for clarity.
        However, you need only a SQL warehouse's `id` to create new queries
        against it."""
        
        json = self._api.do('GET', '/api/2.0/preview/sql/data_sources')
        return DataSourceList.from_dict(json)
    
class DbsqlPermissionsAPI:
    def __init__(self, api_client):
        self._api = api_client
    
    def getPermissions(self, request: GetPermissionsRequest) -> GetPermissionsResponse:
        """Get object ACL
        
        Gets a JSON representation of the access control list (ACL) for a
        specified object."""
        query, body = request.as_request()
        json = self._api.do('GET', f'/api/2.0/preview/sql/permissions/{request.objectType}/{request.objectId}', query=query, body=body)
        return GetPermissionsResponse.from_dict(json)
    
    def setPermissions(self, request: SetPermissionsRequest) -> SetPermissionsResponse:
        """Set object ACL
        
        Sets the access control list (ACL) for a specified object. This
        operation will complete rewrite the ACL."""
        query, body = request.as_request()
        json = self._api.do('POST', f'/api/2.0/preview/sql/permissions/{request.objectType}/{request.objectId}', query=query, body=body)
        return SetPermissionsResponse.from_dict(json)
    
    def transferOwnership(self, request: TransferOwnershipRequest) -> Success:
        """Transfer object ownership
        
        Transfers ownership of a dashboard, query, or alert to an active user.
        Requires an admin API key."""
        query, body = request.as_request()
        json = self._api.do('POST', f'/api/2.0/preview/sql/permissions/{request.objectType}/{request.objectId}/transfer', query=query, body=body)
        return Success.from_dict(json)
    
class QueriesAPI:
    def __init__(self, api_client):
        self._api = api_client
    
    def createQuery(self, request: QueryPostContent) -> Query:
        """Create a new query definition
        
        Creates a new query definition. Queries created with this endpoint
        belong to the authenticated user making the request.
        
        The `data_source_id` field specifies the ID of the SQL warehouse to run
        this query against. You can use the Data Sources API to see a complete
        list of available SQL warehouses. Or you can copy the `data_source_id`
        from an existing query.
        
        **Note**: You cannot add a visualization until you create the query."""
        query, body = request.as_request()
        json = self._api.do('POST', '/api/2.0/preview/sql/queries', query=query, body=body)
        return Query.from_dict(json)
    
    def deleteQuery(self, request: DeleteQueryRequest):
        """Delete a query
        
        Moves a query to the trash. Trashed queries immediately disappear from
        searches and list views, and they cannot be used for alerts. The trash
        is deleted after 30 days."""
        query, body = request.as_request()
        self._api.do('DELETE', f'/api/2.0/preview/sql/queries/{request.query_id}', query=query, body=body)
        
    
    def getQuery(self, request: GetQueryRequest) -> Query:
        """Get a query definition.
        
        Retrieve a query object definition along with contextual permissions
        information about the currently authenticated user."""
        query, body = request.as_request()
        json = self._api.do('GET', f'/api/2.0/preview/sql/queries/{request.query_id}', query=query, body=body)
        return Query.from_dict(json)
    
    def listQueries(self, request: ListQueriesRequest) -> ListQueriesResponse:
        """Get a list of queries
        
        Gets a list of queries. Optionally, this list can be filtered by a
        search term."""
        query, body = request.as_request()
        json = self._api.do('GET', '/api/2.0/preview/sql/queries', query=query, body=body)
        return ListQueriesResponse.from_dict(json)
    
    def restoreQuery(self, request: RestoreQueryRequest):
        """Restore a query
        
        Restore a query that has been moved to the trash. A restored query
        appears in list views and searches. You can use restored queries for
        alerts."""
        query, body = request.as_request()
        self._api.do('POST', f'/api/2.0/preview/sql/queries/trash/{request.query_id}', query=query, body=body)
        
    
    def update(self, request: QueryPostContent) -> Query:
        """Change a query definition
        
        Modify this query definition.
        
        **Note**: You cannot undo this operation."""
        query, body = request.as_request()
        json = self._api.do('POST', f'/api/2.0/preview/sql/queries/{request.query_id}', query=query, body=body)
        return Query.from_dict(json)
    