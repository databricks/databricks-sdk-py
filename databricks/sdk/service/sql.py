# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

from dataclasses import dataclass
from enum import Enum
from typing import Optional, Dict, List, Any


# all definitions in this file are in alphabetical order


@dataclass
class AccessControl:

    group_name: str
    # This describes an enum
    permission_level: "PermissionLevel"

    user_name: str

    def as_dict(self) -> dict:
        body = {}
        if self.group_name:
            body["group_name"] = self.group_name
        if self.permission_level:
            body["permission_level"] = self.permission_level.value
        if self.user_name:
            body["user_name"] = self.user_name

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "AccessControl":
        return cls(
            group_name=d.get("group_name", None),
            permission_level=PermissionLevel(d["permission_level"])
            if "permission_level" in d
            else None,
            user_name=d.get("user_name", None),
        )


@dataclass
class Alert:

    # Timestamp when the alert was created.
    created_at: str
    # ID of the alert.
    id: str
    # Timestamp when the alert was last triggered.
    last_triggered_at: str
    # Name of the alert.
    name: str
    # Alert configuration options.
    options: "AlertOptions"

    query: "Query"
    # Number of seconds after being triggered before the alert rearms itself and can be triggered again. If `null`,
    # alert will never be triggered again.
    rearm: int
    # State of the alert. Possible values are: `unknown` (yet to be evaluated), `triggered` (evaluated and fulfilled
    # trigger conditions), or `ok` (evaluated and did not fulfill trigger conditions).
    state: "AlertState"
    # Timestamp when the alert was last updated.
    updated_at: str

    user: "User"

    def as_dict(self) -> dict:
        body = {}
        if self.created_at:
            body["created_at"] = self.created_at
        if self.id:
            body["id"] = self.id
        if self.last_triggered_at:
            body["last_triggered_at"] = self.last_triggered_at
        if self.name:
            body["name"] = self.name
        if self.options:
            body["options"] = self.options.as_dict()
        if self.query:
            body["query"] = self.query.as_dict()
        if self.rearm:
            body["rearm"] = self.rearm
        if self.state:
            body["state"] = self.state.value
        if self.updated_at:
            body["updated_at"] = self.updated_at
        if self.user:
            body["user"] = self.user.as_dict()

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "Alert":
        return cls(
            created_at=d.get("created_at", None),
            id=d.get("id", None),
            last_triggered_at=d.get("last_triggered_at", None),
            name=d.get("name", None),
            options=AlertOptions.from_dict(d["options"]) if "options" in d else None,
            query=Query.from_dict(d["query"]) if "query" in d else None,
            rearm=d.get("rearm", None),
            state=AlertState(d["state"]) if "state" in d else None,
            updated_at=d.get("updated_at", None),
            user=User.from_dict(d["user"]) if "user" in d else None,
        )


@dataclass
class AlertOptions:
    """Alert configuration options."""

    # Name of column in the query result to compare in alert evaluation.
    column: str
    # Custom body of alert notification, if it exists. See [here] for custom templating instructions.
    #
    # [here]: https://docs.databricks.com/sql/user/alerts/index.html
    custom_body: str
    # Custom subject of alert notification, if it exists. This includes email subject, Slack notification header, etc.
    # See [here] for custom templating instructions.
    #
    # [here]: https://docs.databricks.com/sql/user/alerts/index.html
    custom_subject: str
    # Whether or not the alert is muted. If an alert is muted, it will not notify users and alert destinations when
    # triggered.
    muted: bool
    # Operator used to compare in alert evaluation: `>`, `>=`, `<`, `<=`, `==`, `!=`
    op: str
    # Number of failures encountered during alert refresh. This counter is used for sending aggregated alert failure
    # email notifications.
    schedule_failures: int
    # Value used to compare in alert evaluation.
    value: str

    def as_dict(self) -> dict:
        body = {}
        if self.column:
            body["column"] = self.column
        if self.custom_body:
            body["custom_body"] = self.custom_body
        if self.custom_subject:
            body["custom_subject"] = self.custom_subject
        if self.muted:
            body["muted"] = self.muted
        if self.op:
            body["op"] = self.op
        if self.schedule_failures:
            body["schedule_failures"] = self.schedule_failures
        if self.value:
            body["value"] = self.value

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "AlertOptions":
        return cls(
            column=d.get("column", None),
            custom_body=d.get("custom_body", None),
            custom_subject=d.get("custom_subject", None),
            muted=d.get("muted", None),
            op=d.get("op", None),
            schedule_failures=d.get("schedule_failures", None),
            value=d.get("value", None),
        )


class AlertState(Enum):
    """State of the alert. Possible values are: `unknown` (yet to be evaluated), `triggered` (evaluated and fulfilled
    trigger conditions), or `ok` (evaluated and did not fulfill trigger conditions)."""

    ok = "ok"
    triggered = "triggered"
    unknown = "unknown"


@dataclass
class Channel:

    dbsql_version: str

    name: "ChannelName"

    def as_dict(self) -> dict:
        body = {}
        if self.dbsql_version:
            body["dbsql_version"] = self.dbsql_version
        if self.name:
            body["name"] = self.name.value

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "Channel":
        return cls(
            dbsql_version=d.get("dbsql_version", None),
            name=ChannelName(d["name"]) if "name" in d else None,
        )


@dataclass
class ChannelInfo:
    """Channel information for the SQL warehouse at the time of query execution"""

    # DBSQL Version the channel is mapped to
    dbsql_version: str
    # Name of the channel
    name: "ChannelName"

    def as_dict(self) -> dict:
        body = {}
        if self.dbsql_version:
            body["dbsql_version"] = self.dbsql_version
        if self.name:
            body["name"] = self.name.value

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ChannelInfo":
        return cls(
            dbsql_version=d.get("dbsql_version", None),
            name=ChannelName(d["name"]) if "name" in d else None,
        )


class ChannelName(Enum):
    """Name of the channel"""

    CHANNEL_NAME_CURRENT = "CHANNEL_NAME_CURRENT"
    CHANNEL_NAME_CUSTOM = "CHANNEL_NAME_CUSTOM"
    CHANNEL_NAME_PREVIEW = "CHANNEL_NAME_PREVIEW"
    CHANNEL_NAME_PREVIOUS = "CHANNEL_NAME_PREVIOUS"
    CHANNEL_NAME_UNSPECIFIED = "CHANNEL_NAME_UNSPECIFIED"


@dataclass
class CreateDashboardRequest:
    """Create a dashboard object"""

    # In the web application, query filters that share a name are coupled to a single selection box if this value is
    # true.
    dashboard_filters_enabled: bool
    # Draft dashboards only appear in list views for their owners.
    is_draft: bool
    # Indicates whether the dashboard is trashed. Trashed dashboards don't appear in list views.
    is_trashed: bool
    # The title of this dashboard that appears in list views and at the top of the dashboard page.
    name: str

    tags: "List[str]"
    # An array of widget objects. A complete description of widget objects can be found in the response to [Retrieve A
    # Dashboard Definition](#operation/sql-analytics-fetch-dashboard). Databricks does not recommend creating new
    # widgets via this API.
    widgets: "List[Widget]"

    def as_dict(self) -> dict:
        body = {}
        if self.dashboard_filters_enabled:
            body["dashboard_filters_enabled"] = self.dashboard_filters_enabled
        if self.is_draft:
            body["is_draft"] = self.is_draft
        if self.is_trashed:
            body["is_trashed"] = self.is_trashed
        if self.name:
            body["name"] = self.name
        if self.tags:
            body["tags"] = [v for v in self.tags]
        if self.widgets:
            body["widgets"] = [v.as_dict() for v in self.widgets]

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "CreateDashboardRequest":
        return cls(
            dashboard_filters_enabled=d.get("dashboard_filters_enabled", None),
            is_draft=d.get("is_draft", None),
            is_trashed=d.get("is_trashed", None),
            name=d.get("name", None),
            tags=d.get("tags", None),
            widgets=[Widget.from_dict(v) for v in d["widgets"]]
            if "widgets" in d
            else None,
        )


@dataclass
class CreateRefreshSchedule:

    alert_id: str  # path
    # Cron string representing the refresh schedule.
    cron: str
    # ID of the SQL warehouse to refresh with. If `null`, query's SQL warehouse will be used to refresh.
    data_source_id: str

    def as_dict(self) -> dict:
        body = {}
        if self.alert_id:
            body["alert_id"] = self.alert_id
        if self.cron:
            body["cron"] = self.cron
        if self.data_source_id:
            body["data_source_id"] = self.data_source_id

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "CreateRefreshSchedule":
        return cls(
            alert_id=d.get("alert_id", None),
            cron=d.get("cron", None),
            data_source_id=d.get("data_source_id", None),
        )


@dataclass
class CreateSubscription:

    # ID of the alert.
    alert_id: str  # path
    # ID of the alert subscriber (if subscribing an alert destination). Alert destinations can be configured by admins
    # through the UI. See [here](/sql/admin/alert-destinations.html).
    destination_id: str
    # ID of the alert subscriber (if subscribing a user).
    user_id: int

    def as_dict(self) -> dict:
        body = {}
        if self.alert_id:
            body["alert_id"] = self.alert_id
        if self.destination_id:
            body["destination_id"] = self.destination_id
        if self.user_id:
            body["user_id"] = self.user_id

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "CreateSubscription":
        return cls(
            alert_id=d.get("alert_id", None),
            destination_id=d.get("destination_id", None),
            user_id=d.get("user_id", None),
        )


@dataclass
class CreateWarehouseRequest:

    # The amount of time in minutes that a SQL Endpoint must be idle (i.e., no RUNNING queries) before it is
    # automatically stopped.
    #
    # Supported values: - Must be == 0 or >= 10 mins - 0 indicates no autostop.
    #
    # Defaults to 120 mins
    auto_stop_mins: int
    # Channel Details
    channel: "Channel"
    # Size of the clusters allocated for this endpoint. Increasing the size of a spark cluster allows you to run larger
    # queries on it. If you want to increase the number of concurrent queries, please tune max_num_clusters.
    #
    # Supported values: - 2X-Small - X-Small - Small - Medium - Large - X-Large - 2X-Large - 3X-Large - 4X-Large
    cluster_size: str
    # endpoint creator name
    creator_name: str
    # Configures whether the endpoint should use Photon optimized clusters.
    #
    # Defaults to false.
    enable_photon: bool
    # Configures whether the endpoint should use Serverless Compute (aka Nephos)
    #
    # Defaults to value in global endpoint settings
    enable_serverless_compute: bool
    # Deprecated. Instance profile used to pass IAM role to the cluster
    instance_profile_arn: str
    # Maximum number of clusters that the autoscaler will create to handle concurrent queries.
    #
    # Supported values: - Must be >= min_num_clusters - Must be <= 30.
    #
    # Defaults to min_clusters if unset.
    max_num_clusters: int
    # Minimum number of available clusters that will be maintained for this SQL Endpoint. Increasing this will ensure
    # that a larger number of clusters are always running and therefore may reduce the cold start time for new queries.
    # This is similar to reserved vs. revocable cores in a resource manager.
    #
    # Supported values: - Must be > 0 - Must be <= min(max_num_clusters, 30)
    #
    # Defaults to 1
    min_num_clusters: int
    # Logical name for the cluster.
    #
    # Supported values: - Must be unique within an org. - Must be less than 100 characters.
    name: str
    # Configurations whether the warehouse should use spot instances.
    spot_instance_policy: "SpotInstancePolicy"
    # A set of key-value pairs that will be tagged on all resources (e.g., AWS instances and EBS volumes) associated
    # with this SQL Endpoints.
    #
    # Supported values: - Number of tags < 45.
    tags: "EndpointTags"

    warehouse_type: "WarehouseType"

    def as_dict(self) -> dict:
        body = {}
        if self.auto_stop_mins:
            body["auto_stop_mins"] = self.auto_stop_mins
        if self.channel:
            body["channel"] = self.channel.as_dict()
        if self.cluster_size:
            body["cluster_size"] = self.cluster_size
        if self.creator_name:
            body["creator_name"] = self.creator_name
        if self.enable_photon:
            body["enable_photon"] = self.enable_photon
        if self.enable_serverless_compute:
            body["enable_serverless_compute"] = self.enable_serverless_compute
        if self.instance_profile_arn:
            body["instance_profile_arn"] = self.instance_profile_arn
        if self.max_num_clusters:
            body["max_num_clusters"] = self.max_num_clusters
        if self.min_num_clusters:
            body["min_num_clusters"] = self.min_num_clusters
        if self.name:
            body["name"] = self.name
        if self.spot_instance_policy:
            body["spot_instance_policy"] = self.spot_instance_policy.value
        if self.tags:
            body["tags"] = self.tags.as_dict()
        if self.warehouse_type:
            body["warehouse_type"] = self.warehouse_type.value

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "CreateWarehouseRequest":
        return cls(
            auto_stop_mins=d.get("auto_stop_mins", None),
            channel=Channel.from_dict(d["channel"]) if "channel" in d else None,
            cluster_size=d.get("cluster_size", None),
            creator_name=d.get("creator_name", None),
            enable_photon=d.get("enable_photon", None),
            enable_serverless_compute=d.get("enable_serverless_compute", None),
            instance_profile_arn=d.get("instance_profile_arn", None),
            max_num_clusters=d.get("max_num_clusters", None),
            min_num_clusters=d.get("min_num_clusters", None),
            name=d.get("name", None),
            spot_instance_policy=SpotInstancePolicy(d["spot_instance_policy"])
            if "spot_instance_policy" in d
            else None,
            tags=EndpointTags.from_dict(d["tags"]) if "tags" in d else None,
            warehouse_type=WarehouseType(d["warehouse_type"])
            if "warehouse_type" in d
            else None,
        )


@dataclass
class CreateWarehouseResponse:

    # Id for the SQL warehouse. This value is unique across all SQL warehouses.
    id: str

    def as_dict(self) -> dict:
        body = {}
        if self.id:
            body["id"] = self.id

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "CreateWarehouseResponse":
        return cls(
            id=d.get("id", None),
        )


@dataclass
class Dashboard:
    """A JSON representing a dashboard containing widgets of visualizations and
    text boxes."""

    # Whether the authenticated user can edit the query definition.
    can_edit: bool
    # Timestamp when this dashboard was created.
    created_at: str
    # In the web application, query filters that share a name are coupled to a single selection box if this value is
    # `true`.
    dashboard_filters_enabled: bool
    # The ID for this dashboard.
    id: str
    # Indicates whether a dashboard is trashed. Trashed dashboards won't appear in list views. If this boolean is
    # `true`, the `options` property for this dashboard includes a `moved_to_trash_at` timestamp. Items in trash are
    # permanently deleted after 30 days.
    is_archived: bool
    # Whether a dashboard is a draft. Draft dashboards only appear in list views for their owners.
    is_draft: bool
    # Indicates whether this query object appears in the current user's favorites list. This flag determines whether the
    # star icon for favorites is selected.
    is_favorite: bool
    # The title of the dashboard that appears in list views and at the top of the dashboard page.
    name: str

    options: "DashboardOptions"
    # This describes an enum
    permission_tier: "PermissionLevel"
    # URL slug. Usually mirrors the query name with dashes (`-`) instead of spaces. Appears in the URL for this query.
    slug: str

    tags: "List[str]"
    # Timestamp when this dashboard was last updated.
    updated_at: str

    user: "User"
    # The ID of the user that created and owns this dashboard.
    user_id: int

    widgets: "List[Widget]"

    def as_dict(self) -> dict:
        body = {}
        if self.can_edit:
            body["can_edit"] = self.can_edit
        if self.created_at:
            body["created_at"] = self.created_at
        if self.dashboard_filters_enabled:
            body["dashboard_filters_enabled"] = self.dashboard_filters_enabled
        if self.id:
            body["id"] = self.id
        if self.is_archived:
            body["is_archived"] = self.is_archived
        if self.is_draft:
            body["is_draft"] = self.is_draft
        if self.is_favorite:
            body["is_favorite"] = self.is_favorite
        if self.name:
            body["name"] = self.name
        if self.options:
            body["options"] = self.options.as_dict()
        if self.permission_tier:
            body["permission_tier"] = self.permission_tier.value
        if self.slug:
            body["slug"] = self.slug
        if self.tags:
            body["tags"] = [v for v in self.tags]
        if self.updated_at:
            body["updated_at"] = self.updated_at
        if self.user:
            body["user"] = self.user.as_dict()
        if self.user_id:
            body["user_id"] = self.user_id
        if self.widgets:
            body["widgets"] = [v.as_dict() for v in self.widgets]

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "Dashboard":
        return cls(
            can_edit=d.get("can_edit", None),
            created_at=d.get("created_at", None),
            dashboard_filters_enabled=d.get("dashboard_filters_enabled", None),
            id=d.get("id", None),
            is_archived=d.get("is_archived", None),
            is_draft=d.get("is_draft", None),
            is_favorite=d.get("is_favorite", None),
            name=d.get("name", None),
            options=DashboardOptions.from_dict(d["options"])
            if "options" in d
            else None,
            permission_tier=PermissionLevel(d["permission_tier"])
            if "permission_tier" in d
            else None,
            slug=d.get("slug", None),
            tags=d.get("tags", None),
            updated_at=d.get("updated_at", None),
            user=User.from_dict(d["user"]) if "user" in d else None,
            user_id=d.get("user_id", None),
            widgets=[Widget.from_dict(v) for v in d["widgets"]]
            if "widgets" in d
            else None,
        )


@dataclass
class DashboardOptions:

    # The timestamp when this dashboard was moved to trash. Only present when the `is_archived` property is `true`.
    # Trashed items are deleted after thirty days.
    moved_to_trash_at: str

    def as_dict(self) -> dict:
        body = {}
        if self.moved_to_trash_at:
            body["moved_to_trash_at"] = self.moved_to_trash_at

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "DashboardOptions":
        return cls(
            moved_to_trash_at=d.get("moved_to_trash_at", None),
        )


@dataclass
class DataSource:
    """A JSON object representing a DBSQL data source / SQL warehouse."""

    # The unique identifier for this data source / SQL warehouse. Can be used when creating / modifying queries and
    # dashboards.
    id: str
    # The string name of this data source / SQL warehouse as it appears in the Databricks SQL web application.
    name: str
    # <needs content>
    pause_reason: str
    # <needs content>
    paused: int
    # <needs content>
    supports_auto_limit: bool
    # <needs content>
    syntax: str
    # <needs content>
    type: str
    # <needs content>
    view_only: bool
    # <needs content>
    warehouse_id: str

    def as_dict(self) -> dict:
        body = {}
        if self.id:
            body["id"] = self.id
        if self.name:
            body["name"] = self.name
        if self.pause_reason:
            body["pause_reason"] = self.pause_reason
        if self.paused:
            body["paused"] = self.paused
        if self.supports_auto_limit:
            body["supports_auto_limit"] = self.supports_auto_limit
        if self.syntax:
            body["syntax"] = self.syntax
        if self.type:
            body["type"] = self.type
        if self.view_only:
            body["view_only"] = self.view_only
        if self.warehouse_id:
            body["warehouse_id"] = self.warehouse_id

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "DataSource":
        return cls(
            id=d.get("id", None),
            name=d.get("name", None),
            pause_reason=d.get("pause_reason", None),
            paused=d.get("paused", None),
            supports_auto_limit=d.get("supports_auto_limit", None),
            syntax=d.get("syntax", None),
            type=d.get("type", None),
            view_only=d.get("view_only", None),
            warehouse_id=d.get("warehouse_id", None),
        )


@dataclass
class DeleteAlertRequest:
    """Delete an alert"""

    alert_id: str  # path

    def as_dict(self) -> dict:
        body = {}
        if self.alert_id:
            body["alert_id"] = self.alert_id

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "DeleteAlertRequest":
        return cls(
            alert_id=d.get("alert_id", None),
        )


@dataclass
class DeleteDashboardRequest:
    """Remove a dashboard"""

    dashboard_id: str  # path

    def as_dict(self) -> dict:
        body = {}
        if self.dashboard_id:
            body["dashboard_id"] = self.dashboard_id

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "DeleteDashboardRequest":
        return cls(
            dashboard_id=d.get("dashboard_id", None),
        )


@dataclass
class DeleteQueryRequest:
    """Delete a query"""

    query_id: str  # path

    def as_dict(self) -> dict:
        body = {}
        if self.query_id:
            body["query_id"] = self.query_id

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "DeleteQueryRequest":
        return cls(
            query_id=d.get("query_id", None),
        )


@dataclass
class DeleteScheduleRequest:
    """Delete a refresh schedule"""

    alert_id: str  # path

    schedule_id: str  # path

    def as_dict(self) -> dict:
        body = {}
        if self.alert_id:
            body["alert_id"] = self.alert_id
        if self.schedule_id:
            body["schedule_id"] = self.schedule_id

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "DeleteScheduleRequest":
        return cls(
            alert_id=d.get("alert_id", None),
            schedule_id=d.get("schedule_id", None),
        )


@dataclass
class DeleteWarehouseRequest:
    """Delete a warehouse"""

    # Required. Id of the SQL warehouse.
    id: str  # path

    def as_dict(self) -> dict:
        body = {}
        if self.id:
            body["id"] = self.id

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "DeleteWarehouseRequest":
        return cls(
            id=d.get("id", None),
        )


@dataclass
class Destination:
    """Alert destination subscribed to the alert, if it exists. Alert destinations
    can be configured by admins through the UI. See [here].

    [here]: https://docs.databricks.com/sql/admin/alert-destinations.html"""

    # ID of the alert destination.
    id: str
    # Name of the alert destination.
    name: str
    # Type of the alert destination.
    type: "DestinationType"

    def as_dict(self) -> dict:
        body = {}
        if self.id:
            body["id"] = self.id
        if self.name:
            body["name"] = self.name
        if self.type:
            body["type"] = self.type.value

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "Destination":
        return cls(
            id=d.get("id", None),
            name=d.get("name", None),
            type=DestinationType(d["type"]) if "type" in d else None,
        )


class DestinationType(Enum):
    """Type of the alert destination."""

    email = "email"
    hangouts_chat = "hangouts_chat"
    mattermost = "mattermost"
    microsoft_teams = "microsoft_teams"
    pagerduty = "pagerduty"
    slack = "slack"
    webhook = "webhook"


@dataclass
class EditAlert:

    alert_id: str  # path
    # Name of the alert.
    name: str
    # Alert configuration options.
    options: "AlertOptions"
    # ID of the query evaluated by the alert.
    query_id: str
    # Number of seconds after being triggered before the alert rearms itself and can be triggered again. If `null`,
    # alert will never be triggered again.
    rearm: int

    def as_dict(self) -> dict:
        body = {}
        if self.alert_id:
            body["alert_id"] = self.alert_id
        if self.name:
            body["name"] = self.name
        if self.options:
            body["options"] = self.options.as_dict()
        if self.query_id:
            body["query_id"] = self.query_id
        if self.rearm:
            body["rearm"] = self.rearm

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "EditAlert":
        return cls(
            alert_id=d.get("alert_id", None),
            name=d.get("name", None),
            options=AlertOptions.from_dict(d["options"]) if "options" in d else None,
            query_id=d.get("query_id", None),
            rearm=d.get("rearm", None),
        )


@dataclass
class EditWarehouseRequest:

    # The amount of time in minutes that a SQL Endpoint must be idle (i.e., no RUNNING queries) before it is
    # automatically stopped.
    #
    # Supported values: - Must be == 0 or >= 10 mins - 0 indicates no autostop.
    #
    # Defaults to 120 mins
    auto_stop_mins: int
    # Channel Details
    channel: "Channel"
    # Size of the clusters allocated for this endpoint. Increasing the size of a spark cluster allows you to run larger
    # queries on it. If you want to increase the number of concurrent queries, please tune max_num_clusters.
    #
    # Supported values: - 2X-Small - X-Small - Small - Medium - Large - X-Large - 2X-Large - 3X-Large - 4X-Large
    cluster_size: str
    # endpoint creator name
    creator_name: str
    # Configures whether the endpoint should use Databricks Compute (aka Nephos)
    #
    # Deprecated: Use enable_serverless_compute TODO(SC-79930): Remove the field once clients are updated
    enable_databricks_compute: bool
    # Configures whether the endpoint should use Photon optimized clusters.
    #
    # Defaults to false.
    enable_photon: bool
    # Configures whether the endpoint should use Serverless Compute (aka Nephos)
    #
    # Defaults to value in global endpoint settings
    enable_serverless_compute: bool
    # Required. Id of the warehouse to configure.
    id: str  # path
    # Deprecated. Instance profile used to pass IAM role to the cluster
    instance_profile_arn: str
    # Maximum number of clusters that the autoscaler will create to handle concurrent queries.
    #
    # Supported values: - Must be >= min_num_clusters - Must be <= 30.
    #
    # Defaults to min_clusters if unset.
    max_num_clusters: int
    # Minimum number of available clusters that will be maintained for this SQL Endpoint. Increasing this will ensure
    # that a larger number of clusters are always running and therefore may reduce the cold start time for new queries.
    # This is similar to reserved vs. revocable cores in a resource manager.
    #
    # Supported values: - Must be > 0 - Must be <= min(max_num_clusters, 30)
    #
    # Defaults to 1
    min_num_clusters: int
    # Logical name for the cluster.
    #
    # Supported values: - Must be unique within an org. - Must be less than 100 characters.
    name: str
    # Configurations whether the warehouse should use spot instances.
    spot_instance_policy: "SpotInstancePolicy"
    # A set of key-value pairs that will be tagged on all resources (e.g., AWS instances and EBS volumes) associated
    # with this SQL Endpoints.
    #
    # Supported values: - Number of tags < 45.
    tags: "EndpointTags"

    warehouse_type: "WarehouseType"

    def as_dict(self) -> dict:
        body = {}
        if self.auto_stop_mins:
            body["auto_stop_mins"] = self.auto_stop_mins
        if self.channel:
            body["channel"] = self.channel.as_dict()
        if self.cluster_size:
            body["cluster_size"] = self.cluster_size
        if self.creator_name:
            body["creator_name"] = self.creator_name
        if self.enable_databricks_compute:
            body["enable_databricks_compute"] = self.enable_databricks_compute
        if self.enable_photon:
            body["enable_photon"] = self.enable_photon
        if self.enable_serverless_compute:
            body["enable_serverless_compute"] = self.enable_serverless_compute
        if self.id:
            body["id"] = self.id
        if self.instance_profile_arn:
            body["instance_profile_arn"] = self.instance_profile_arn
        if self.max_num_clusters:
            body["max_num_clusters"] = self.max_num_clusters
        if self.min_num_clusters:
            body["min_num_clusters"] = self.min_num_clusters
        if self.name:
            body["name"] = self.name
        if self.spot_instance_policy:
            body["spot_instance_policy"] = self.spot_instance_policy.value
        if self.tags:
            body["tags"] = self.tags.as_dict()
        if self.warehouse_type:
            body["warehouse_type"] = self.warehouse_type.value

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "EditWarehouseRequest":
        return cls(
            auto_stop_mins=d.get("auto_stop_mins", None),
            channel=Channel.from_dict(d["channel"]) if "channel" in d else None,
            cluster_size=d.get("cluster_size", None),
            creator_name=d.get("creator_name", None),
            enable_databricks_compute=d.get("enable_databricks_compute", None),
            enable_photon=d.get("enable_photon", None),
            enable_serverless_compute=d.get("enable_serverless_compute", None),
            id=d.get("id", None),
            instance_profile_arn=d.get("instance_profile_arn", None),
            max_num_clusters=d.get("max_num_clusters", None),
            min_num_clusters=d.get("min_num_clusters", None),
            name=d.get("name", None),
            spot_instance_policy=SpotInstancePolicy(d["spot_instance_policy"])
            if "spot_instance_policy" in d
            else None,
            tags=EndpointTags.from_dict(d["tags"]) if "tags" in d else None,
            warehouse_type=WarehouseType(d["warehouse_type"])
            if "warehouse_type" in d
            else None,
        )


@dataclass
class EndpointConfPair:

    key: str

    value: str

    def as_dict(self) -> dict:
        body = {}
        if self.key:
            body["key"] = self.key
        if self.value:
            body["value"] = self.value

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "EndpointConfPair":
        return cls(
            key=d.get("key", None),
            value=d.get("value", None),
        )


@dataclass
class EndpointHealth:

    # Details about errors that are causing current degraded/failed status.
    details: str
    # The reason for failure to bring up clusters for this endpoint. This is available when status is 'FAILED' and
    # sometimes when it is DEGRADED.
    failure_reason: "TerminationReason"
    # Deprecated. split into summary and details for security
    message: str
    # Health status of the endpoint.
    status: "Status"
    # A short summary of the health status in case of degraded/failed endpoints.
    summary: str

    def as_dict(self) -> dict:
        body = {}
        if self.details:
            body["details"] = self.details
        if self.failure_reason:
            body["failure_reason"] = self.failure_reason.as_dict()
        if self.message:
            body["message"] = self.message
        if self.status:
            body["status"] = self.status.value
        if self.summary:
            body["summary"] = self.summary

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "EndpointHealth":
        return cls(
            details=d.get("details", None),
            failure_reason=TerminationReason.from_dict(d["failure_reason"])
            if "failure_reason" in d
            else None,
            message=d.get("message", None),
            status=Status(d["status"]) if "status" in d else None,
            summary=d.get("summary", None),
        )


@dataclass
class EndpointInfo:

    # The amount of time in minutes that a SQL Endpoint must be idle (i.e., no RUNNING queries) before it is
    # automatically stopped.
    #
    # Supported values: - Must be == 0 or >= 10 mins - 0 indicates no autostop.
    #
    # Defaults to 120 mins
    auto_stop_mins: int
    # Channel Details
    channel: "Channel"
    # Size of the clusters allocated for this endpoint. Increasing the size of a spark cluster allows you to run larger
    # queries on it. If you want to increase the number of concurrent queries, please tune max_num_clusters.
    #
    # Supported values: - 2X-Small - X-Small - Small - Medium - Large - X-Large - 2X-Large - 3X-Large - 4X-Large
    cluster_size: str
    # endpoint creator name
    creator_name: str
    # Configures whether the endpoint should use Databricks Compute (aka Nephos)
    #
    # Deprecated: Use enable_serverless_compute TODO(SC-79930): Remove the field once clients are updated
    enable_databricks_compute: bool
    # Configures whether the endpoint should use Photon optimized clusters.
    #
    # Defaults to false.
    enable_photon: bool
    # Configures whether the endpoint should use Serverless Compute (aka Nephos)
    #
    # Defaults to value in global endpoint settings
    enable_serverless_compute: bool
    # Optional health status. Assume the endpoint is healthy if this field is not set.
    health: "EndpointHealth"
    # unique identifier for endpoint
    id: str
    # Deprecated. Instance profile used to pass IAM role to the cluster
    instance_profile_arn: str
    # the jdbc connection string for this endpoint
    jdbc_url: str
    # Maximum number of clusters that the autoscaler will create to handle concurrent queries.
    #
    # Supported values: - Must be >= min_num_clusters - Must be <= 30.
    #
    # Defaults to min_clusters if unset.
    max_num_clusters: int
    # Minimum number of available clusters that will be maintained for this SQL Endpoint. Increasing this will ensure
    # that a larger number of clusters are always running and therefore may reduce the cold start time for new queries.
    # This is similar to reserved vs. revocable cores in a resource manager.
    #
    # Supported values: - Must be > 0 - Must be <= min(max_num_clusters, 30)
    #
    # Defaults to 1
    min_num_clusters: int
    # Logical name for the cluster.
    #
    # Supported values: - Must be unique within an org. - Must be less than 100 characters.
    name: str
    # current number of active sessions for the endpoint
    num_active_sessions: int
    # current number of clusters running for the service
    num_clusters: int
    # ODBC parameters for the sql endpoint
    odbc_params: "OdbcParams"
    # Configurations whether the warehouse should use spot instances.
    spot_instance_policy: "SpotInstancePolicy"
    # State of the warehouse
    state: "State"
    # A set of key-value pairs that will be tagged on all resources (e.g., AWS instances and EBS volumes) associated
    # with this SQL Endpoints.
    #
    # Supported values: - Number of tags < 45.
    tags: "EndpointTags"

    warehouse_type: "WarehouseType"

    def as_dict(self) -> dict:
        body = {}
        if self.auto_stop_mins:
            body["auto_stop_mins"] = self.auto_stop_mins
        if self.channel:
            body["channel"] = self.channel.as_dict()
        if self.cluster_size:
            body["cluster_size"] = self.cluster_size
        if self.creator_name:
            body["creator_name"] = self.creator_name
        if self.enable_databricks_compute:
            body["enable_databricks_compute"] = self.enable_databricks_compute
        if self.enable_photon:
            body["enable_photon"] = self.enable_photon
        if self.enable_serverless_compute:
            body["enable_serverless_compute"] = self.enable_serverless_compute
        if self.health:
            body["health"] = self.health.as_dict()
        if self.id:
            body["id"] = self.id
        if self.instance_profile_arn:
            body["instance_profile_arn"] = self.instance_profile_arn
        if self.jdbc_url:
            body["jdbc_url"] = self.jdbc_url
        if self.max_num_clusters:
            body["max_num_clusters"] = self.max_num_clusters
        if self.min_num_clusters:
            body["min_num_clusters"] = self.min_num_clusters
        if self.name:
            body["name"] = self.name
        if self.num_active_sessions:
            body["num_active_sessions"] = self.num_active_sessions
        if self.num_clusters:
            body["num_clusters"] = self.num_clusters
        if self.odbc_params:
            body["odbc_params"] = self.odbc_params.as_dict()
        if self.spot_instance_policy:
            body["spot_instance_policy"] = self.spot_instance_policy.value
        if self.state:
            body["state"] = self.state.value
        if self.tags:
            body["tags"] = self.tags.as_dict()
        if self.warehouse_type:
            body["warehouse_type"] = self.warehouse_type.value

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "EndpointInfo":
        return cls(
            auto_stop_mins=d.get("auto_stop_mins", None),
            channel=Channel.from_dict(d["channel"]) if "channel" in d else None,
            cluster_size=d.get("cluster_size", None),
            creator_name=d.get("creator_name", None),
            enable_databricks_compute=d.get("enable_databricks_compute", None),
            enable_photon=d.get("enable_photon", None),
            enable_serverless_compute=d.get("enable_serverless_compute", None),
            health=EndpointHealth.from_dict(d["health"]) if "health" in d else None,
            id=d.get("id", None),
            instance_profile_arn=d.get("instance_profile_arn", None),
            jdbc_url=d.get("jdbc_url", None),
            max_num_clusters=d.get("max_num_clusters", None),
            min_num_clusters=d.get("min_num_clusters", None),
            name=d.get("name", None),
            num_active_sessions=d.get("num_active_sessions", None),
            num_clusters=d.get("num_clusters", None),
            odbc_params=OdbcParams.from_dict(d["odbc_params"])
            if "odbc_params" in d
            else None,
            spot_instance_policy=SpotInstancePolicy(d["spot_instance_policy"])
            if "spot_instance_policy" in d
            else None,
            state=State(d["state"]) if "state" in d else None,
            tags=EndpointTags.from_dict(d["tags"]) if "tags" in d else None,
            warehouse_type=WarehouseType(d["warehouse_type"])
            if "warehouse_type" in d
            else None,
        )


@dataclass
class EndpointTagPair:

    key: str

    value: str

    def as_dict(self) -> dict:
        body = {}
        if self.key:
            body["key"] = self.key
        if self.value:
            body["value"] = self.value

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "EndpointTagPair":
        return cls(
            key=d.get("key", None),
            value=d.get("value", None),
        )


@dataclass
class EndpointTags:

    custom_tags: "List[EndpointTagPair]"

    def as_dict(self) -> dict:
        body = {}
        if self.custom_tags:
            body["custom_tags"] = [v.as_dict() for v in self.custom_tags]

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "EndpointTags":
        return cls(
            custom_tags=[EndpointTagPair.from_dict(v) for v in d["custom_tags"]]
            if "custom_tags" in d
            else None,
        )


@dataclass
class GetAlertRequest:
    """Get an alert"""

    alert_id: str  # path

    def as_dict(self) -> dict:
        body = {}
        if self.alert_id:
            body["alert_id"] = self.alert_id

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "GetAlertRequest":
        return cls(
            alert_id=d.get("alert_id", None),
        )


@dataclass
class GetDashboardRequest:
    """Retrieve a definition"""

    dashboard_id: str  # path

    def as_dict(self) -> dict:
        body = {}
        if self.dashboard_id:
            body["dashboard_id"] = self.dashboard_id

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "GetDashboardRequest":
        return cls(
            dashboard_id=d.get("dashboard_id", None),
        )


@dataclass
class GetDbsqlPermissionRequest:
    """Get object ACL"""

    # Object ID. An ACL is returned for the object with this UUID.
    objectId: str  # path
    # The type of object permissions to check.
    objectType: "ObjectTypePlural"  # path

    def as_dict(self) -> dict:
        body = {}
        if self.objectId:
            body["objectId"] = self.objectId
        if self.objectType:
            body["objectType"] = self.objectType.value

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "GetDbsqlPermissionRequest":
        return cls(
            objectId=d.get("objectId", None),
            objectType=ObjectTypePlural(d["objectType"]) if "objectType" in d else None,
        )


@dataclass
class GetQueryRequest:
    """Get a query definition."""

    query_id: str  # path

    def as_dict(self) -> dict:
        body = {}
        if self.query_id:
            body["query_id"] = self.query_id

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "GetQueryRequest":
        return cls(
            query_id=d.get("query_id", None),
        )


@dataclass
class GetResponse:

    access_control_list: "List[AccessControl]"
    # A singular noun object type.
    object_id: "ObjectType"
    # An object's type and UUID, separated by a forward slash (/) character.
    object_type: str

    def as_dict(self) -> dict:
        body = {}
        if self.access_control_list:
            body["access_control_list"] = [
                v.as_dict() for v in self.access_control_list
            ]
        if self.object_id:
            body["object_id"] = self.object_id.value
        if self.object_type:
            body["object_type"] = self.object_type

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "GetResponse":
        return cls(
            access_control_list=[
                AccessControl.from_dict(v) for v in d["access_control_list"]
            ]
            if "access_control_list" in d
            else None,
            object_id=ObjectType(d["object_id"]) if "object_id" in d else None,
            object_type=d.get("object_type", None),
        )


@dataclass
class GetSubscriptionsRequest:
    """Get an alert's subscriptions"""

    alert_id: str  # path

    def as_dict(self) -> dict:
        body = {}
        if self.alert_id:
            body["alert_id"] = self.alert_id

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "GetSubscriptionsRequest":
        return cls(
            alert_id=d.get("alert_id", None),
        )


@dataclass
class GetWarehouseRequest:
    """Get warehouse info"""

    # Required. Id of the SQL warehouse.
    id: str  # path

    def as_dict(self) -> dict:
        body = {}
        if self.id:
            body["id"] = self.id

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "GetWarehouseRequest":
        return cls(
            id=d.get("id", None),
        )


@dataclass
class GetWarehouseResponse:

    # The amount of time in minutes that a SQL Endpoint must be idle (i.e., no RUNNING queries) before it is
    # automatically stopped.
    #
    # Supported values: - Must be == 0 or >= 10 mins - 0 indicates no autostop.
    #
    # Defaults to 120 mins
    auto_stop_mins: int
    # Channel Details
    channel: "Channel"
    # Size of the clusters allocated for this endpoint. Increasing the size of a spark cluster allows you to run larger
    # queries on it. If you want to increase the number of concurrent queries, please tune max_num_clusters.
    #
    # Supported values: - 2X-Small - X-Small - Small - Medium - Large - X-Large - 2X-Large - 3X-Large - 4X-Large
    cluster_size: str
    # endpoint creator name
    creator_name: str
    # Configures whether the endpoint should use Databricks Compute (aka Nephos)
    #
    # Deprecated: Use enable_serverless_compute TODO(SC-79930): Remove the field once clients are updated
    enable_databricks_compute: bool
    # Configures whether the endpoint should use Photon optimized clusters.
    #
    # Defaults to false.
    enable_photon: bool
    # Configures whether the endpoint should use Serverless Compute (aka Nephos)
    #
    # Defaults to value in global endpoint settings
    enable_serverless_compute: bool
    # Optional health status. Assume the endpoint is healthy if this field is not set.
    health: "EndpointHealth"
    # unique identifier for endpoint
    id: str
    # Deprecated. Instance profile used to pass IAM role to the cluster
    instance_profile_arn: str
    # the jdbc connection string for this endpoint
    jdbc_url: str
    # Maximum number of clusters that the autoscaler will create to handle concurrent queries.
    #
    # Supported values: - Must be >= min_num_clusters - Must be <= 30.
    #
    # Defaults to min_clusters if unset.
    max_num_clusters: int
    # Minimum number of available clusters that will be maintained for this SQL Endpoint. Increasing this will ensure
    # that a larger number of clusters are always running and therefore may reduce the cold start time for new queries.
    # This is similar to reserved vs. revocable cores in a resource manager.
    #
    # Supported values: - Must be > 0 - Must be <= min(max_num_clusters, 30)
    #
    # Defaults to 1
    min_num_clusters: int
    # Logical name for the cluster.
    #
    # Supported values: - Must be unique within an org. - Must be less than 100 characters.
    name: str
    # current number of active sessions for the endpoint
    num_active_sessions: int
    # current number of clusters running for the service
    num_clusters: int
    # ODBC parameters for the sql endpoint
    odbc_params: "OdbcParams"
    # Configurations whether the warehouse should use spot instances.
    spot_instance_policy: "SpotInstancePolicy"
    # State of the warehouse
    state: "State"
    # A set of key-value pairs that will be tagged on all resources (e.g., AWS instances and EBS volumes) associated
    # with this SQL Endpoints.
    #
    # Supported values: - Number of tags < 45.
    tags: "EndpointTags"

    warehouse_type: "WarehouseType"

    def as_dict(self) -> dict:
        body = {}
        if self.auto_stop_mins:
            body["auto_stop_mins"] = self.auto_stop_mins
        if self.channel:
            body["channel"] = self.channel.as_dict()
        if self.cluster_size:
            body["cluster_size"] = self.cluster_size
        if self.creator_name:
            body["creator_name"] = self.creator_name
        if self.enable_databricks_compute:
            body["enable_databricks_compute"] = self.enable_databricks_compute
        if self.enable_photon:
            body["enable_photon"] = self.enable_photon
        if self.enable_serverless_compute:
            body["enable_serverless_compute"] = self.enable_serverless_compute
        if self.health:
            body["health"] = self.health.as_dict()
        if self.id:
            body["id"] = self.id
        if self.instance_profile_arn:
            body["instance_profile_arn"] = self.instance_profile_arn
        if self.jdbc_url:
            body["jdbc_url"] = self.jdbc_url
        if self.max_num_clusters:
            body["max_num_clusters"] = self.max_num_clusters
        if self.min_num_clusters:
            body["min_num_clusters"] = self.min_num_clusters
        if self.name:
            body["name"] = self.name
        if self.num_active_sessions:
            body["num_active_sessions"] = self.num_active_sessions
        if self.num_clusters:
            body["num_clusters"] = self.num_clusters
        if self.odbc_params:
            body["odbc_params"] = self.odbc_params.as_dict()
        if self.spot_instance_policy:
            body["spot_instance_policy"] = self.spot_instance_policy.value
        if self.state:
            body["state"] = self.state.value
        if self.tags:
            body["tags"] = self.tags.as_dict()
        if self.warehouse_type:
            body["warehouse_type"] = self.warehouse_type.value

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "GetWarehouseResponse":
        return cls(
            auto_stop_mins=d.get("auto_stop_mins", None),
            channel=Channel.from_dict(d["channel"]) if "channel" in d else None,
            cluster_size=d.get("cluster_size", None),
            creator_name=d.get("creator_name", None),
            enable_databricks_compute=d.get("enable_databricks_compute", None),
            enable_photon=d.get("enable_photon", None),
            enable_serverless_compute=d.get("enable_serverless_compute", None),
            health=EndpointHealth.from_dict(d["health"]) if "health" in d else None,
            id=d.get("id", None),
            instance_profile_arn=d.get("instance_profile_arn", None),
            jdbc_url=d.get("jdbc_url", None),
            max_num_clusters=d.get("max_num_clusters", None),
            min_num_clusters=d.get("min_num_clusters", None),
            name=d.get("name", None),
            num_active_sessions=d.get("num_active_sessions", None),
            num_clusters=d.get("num_clusters", None),
            odbc_params=OdbcParams.from_dict(d["odbc_params"])
            if "odbc_params" in d
            else None,
            spot_instance_policy=SpotInstancePolicy(d["spot_instance_policy"])
            if "spot_instance_policy" in d
            else None,
            state=State(d["state"]) if "state" in d else None,
            tags=EndpointTags.from_dict(d["tags"]) if "tags" in d else None,
            warehouse_type=WarehouseType(d["warehouse_type"])
            if "warehouse_type" in d
            else None,
        )


@dataclass
class GetWorkspaceWarehouseConfigResponse:

    # Optional: Channel selection details
    channel: "Channel"
    # Deprecated: Use sql_configuration_parameters
    config_param: "RepeatedEndpointConfPairs"
    # Spark confs for external hive metastore configuration JSON serialized size must be less than <= 512K
    data_access_config: "List[EndpointConfPair]"
    # Enable Serverless compute for SQL Endpoints
    #
    # Deprecated: Use enable_serverless_compute TODO(SC-79930): Remove the field once clients are updated
    enable_databricks_compute: bool
    # Enable Serverless compute for SQL Endpoints
    enable_serverless_compute: bool
    # List of Warehouse Types allowed in this workspace (limits allowed value of the type field in CreateWarehouse and
    # EditWarehouse). Note: Some types cannot be disabled, they don't need to be specified in
    # SetWorkspaceWarehouseConfig. Note: Disabling a type may cause existing warehouses to be converted to another type.
    # Used by frontend to save specific type availability in the warehouse create and edit form UI.
    enabled_warehouse_types: "List[WarehouseTypePair]"
    # Deprecated: Use sql_configuration_parameters
    global_param: "RepeatedEndpointConfPairs"
    # GCP only: Google Service Account used to pass to cluster to access Google Cloud Storage
    google_service_account: str
    # AWS Only: Instance profile used to pass IAM role to the cluster
    instance_profile_arn: str
    # Security policy for endpoints
    security_policy: "GetWorkspaceWarehouseConfigResponseSecurityPolicy"
    # SQL configuration parameters
    sql_configuration_parameters: "RepeatedEndpointConfPairs"

    def as_dict(self) -> dict:
        body = {}
        if self.channel:
            body["channel"] = self.channel.as_dict()
        if self.config_param:
            body["config_param"] = self.config_param.as_dict()
        if self.data_access_config:
            body["data_access_config"] = [v.as_dict() for v in self.data_access_config]
        if self.enable_databricks_compute:
            body["enable_databricks_compute"] = self.enable_databricks_compute
        if self.enable_serverless_compute:
            body["enable_serverless_compute"] = self.enable_serverless_compute
        if self.enabled_warehouse_types:
            body["enabled_warehouse_types"] = [
                v.as_dict() for v in self.enabled_warehouse_types
            ]
        if self.global_param:
            body["global_param"] = self.global_param.as_dict()
        if self.google_service_account:
            body["google_service_account"] = self.google_service_account
        if self.instance_profile_arn:
            body["instance_profile_arn"] = self.instance_profile_arn
        if self.security_policy:
            body["security_policy"] = self.security_policy.value
        if self.sql_configuration_parameters:
            body[
                "sql_configuration_parameters"
            ] = self.sql_configuration_parameters.as_dict()

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "GetWorkspaceWarehouseConfigResponse":
        return cls(
            channel=Channel.from_dict(d["channel"]) if "channel" in d else None,
            config_param=RepeatedEndpointConfPairs.from_dict(d["config_param"])
            if "config_param" in d
            else None,
            data_access_config=[
                EndpointConfPair.from_dict(v) for v in d["data_access_config"]
            ]
            if "data_access_config" in d
            else None,
            enable_databricks_compute=d.get("enable_databricks_compute", None),
            enable_serverless_compute=d.get("enable_serverless_compute", None),
            enabled_warehouse_types=[
                WarehouseTypePair.from_dict(v) for v in d["enabled_warehouse_types"]
            ]
            if "enabled_warehouse_types" in d
            else None,
            global_param=RepeatedEndpointConfPairs.from_dict(d["global_param"])
            if "global_param" in d
            else None,
            google_service_account=d.get("google_service_account", None),
            instance_profile_arn=d.get("instance_profile_arn", None),
            security_policy=GetWorkspaceWarehouseConfigResponseSecurityPolicy(
                d["security_policy"]
            )
            if "security_policy" in d
            else None,
            sql_configuration_parameters=RepeatedEndpointConfPairs.from_dict(
                d["sql_configuration_parameters"]
            )
            if "sql_configuration_parameters" in d
            else None,
        )


class GetWorkspaceWarehouseConfigResponseSecurityPolicy(Enum):
    """Security policy for endpoints"""

    DATA_ACCESS_CONTROL = "DATA_ACCESS_CONTROL"
    NONE = "NONE"
    PASSTHROUGH = "PASSTHROUGH"


@dataclass
class ListDashboardsRequest:
    """Get dashboard objects"""

    # Name of dashboard attribute to order by.
    order: "ListOrder"  # query
    # Page number to retrieve.
    page: int  # query
    # Number of dashboards to return per page.
    page_size: int  # query
    # Full text search term.
    q: str  # query

    def as_dict(self) -> dict:
        body = {}
        if self.order:
            body["order"] = self.order.value
        if self.page:
            body["page"] = self.page
        if self.page_size:
            body["page_size"] = self.page_size
        if self.q:
            body["q"] = self.q

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ListDashboardsRequest":
        return cls(
            order=ListOrder(d["order"]) if "order" in d else None,
            page=d.get("page", None),
            page_size=d.get("page_size", None),
            q=d.get("q", None),
        )


class ListOrder(Enum):

    created_at = "created_at"
    name = "name"


@dataclass
class ListQueriesRequest:
    """Get a list of queries"""

    # Name of query attribute to order by. Default sort order is ascending. Append a dash (`-`) to order descending
    # instead.
    #
    # - `name`: The name of the query.
    #
    # - `created_at`: The timestamp the query was created.
    #
    # - `schedule`: The refresh interval for each query. For example: "Every 5 Hours" or "Every 5 Minutes". "Never" is
    # treated as the highest value for sorting.
    #
    # - `runtime`: The time it took to run this query. This is blank for parameterized queries. A blank value is treated
    # as the highest value for sorting.
    #
    # - `executed_at`: The timestamp when the query was last run.
    #
    # - `created_by`: The user name of the user that created the query.
    order: str  # query
    # Page number to retrieve.
    page: int  # query
    # Number of queries to return per page.
    page_size: int  # query
    # Full text search term
    q: str  # query

    def as_dict(self) -> dict:
        body = {}
        if self.order:
            body["order"] = self.order
        if self.page:
            body["page"] = self.page
        if self.page_size:
            body["page_size"] = self.page_size
        if self.q:
            body["q"] = self.q

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ListQueriesRequest":
        return cls(
            order=d.get("order", None),
            page=d.get("page", None),
            page_size=d.get("page_size", None),
            q=d.get("q", None),
        )


@dataclass
class ListQueriesResponse:

    # Whether there is another page of results.
    has_next_page: bool
    # A token that can be used to get the next page of results.
    next_page_token: str

    res: "List[QueryInfo]"

    def as_dict(self) -> dict:
        body = {}
        if self.has_next_page:
            body["has_next_page"] = self.has_next_page
        if self.next_page_token:
            body["next_page_token"] = self.next_page_token
        if self.res:
            body["res"] = [v.as_dict() for v in self.res]

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ListQueriesResponse":
        return cls(
            has_next_page=d.get("has_next_page", None),
            next_page_token=d.get("next_page_token", None),
            res=[QueryInfo.from_dict(v) for v in d["res"]] if "res" in d else None,
        )


@dataclass
class ListQueryHistoryRequest:
    """List Queries"""

    # A filter to limit query history results. This field is optional.
    filter_by: "QueryFilter"  # query
    # Whether to include metrics about query.
    include_metrics: bool  # query
    # Limit the number of results returned in one page. The default is 100.
    max_results: int  # query
    # A token that can be used to get the next page of results.
    page_token: str  # query

    def as_dict(self) -> dict:
        body = {}
        if self.filter_by:
            body["filter_by"] = self.filter_by.as_dict()
        if self.include_metrics:
            body["include_metrics"] = self.include_metrics
        if self.max_results:
            body["max_results"] = self.max_results
        if self.page_token:
            body["page_token"] = self.page_token

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ListQueryHistoryRequest":
        return cls(
            filter_by=QueryFilter.from_dict(d["filter_by"])
            if "filter_by" in d
            else None,
            include_metrics=d.get("include_metrics", None),
            max_results=d.get("max_results", None),
            page_token=d.get("page_token", None),
        )


@dataclass
class ListResponse:

    # The total number of dashboards.
    count: int
    # The current page being displayed.
    page: int
    # The number of dashboards per page.
    page_size: int
    # List of dashboards returned.
    results: "List[Dashboard]"

    def as_dict(self) -> dict:
        body = {}
        if self.count:
            body["count"] = self.count
        if self.page:
            body["page"] = self.page
        if self.page_size:
            body["page_size"] = self.page_size
        if self.results:
            body["results"] = [v.as_dict() for v in self.results]

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ListResponse":
        return cls(
            count=d.get("count", None),
            page=d.get("page", None),
            page_size=d.get("page_size", None),
            results=[Dashboard.from_dict(v) for v in d["results"]]
            if "results" in d
            else None,
        )


@dataclass
class ListSchedulesRequest:
    """Get refresh schedules"""

    alert_id: str  # path

    def as_dict(self) -> dict:
        body = {}
        if self.alert_id:
            body["alert_id"] = self.alert_id

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ListSchedulesRequest":
        return cls(
            alert_id=d.get("alert_id", None),
        )


@dataclass
class ListWarehousesRequest:
    """List warehouses"""

    # Service Principal which will be used to fetch the list of endpoints. If not specified, the user from the session
    # header is used.
    run_as_user_id: int  # query

    def as_dict(self) -> dict:
        body = {}
        if self.run_as_user_id:
            body["run_as_user_id"] = self.run_as_user_id

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ListWarehousesRequest":
        return cls(
            run_as_user_id=d.get("run_as_user_id", None),
        )


@dataclass
class ListWarehousesResponse:

    # A list of warehouses and their configurations.
    warehouses: "List[EndpointInfo]"

    def as_dict(self) -> dict:
        body = {}
        if self.warehouses:
            body["warehouses"] = [v.as_dict() for v in self.warehouses]

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ListWarehousesResponse":
        return cls(
            warehouses=[EndpointInfo.from_dict(v) for v in d["warehouses"]]
            if "warehouses" in d
            else None,
        )


class ObjectType(Enum):
    """A singular noun object type."""

    alert = "alert"
    dashboard = "dashboard"
    data_source = "data_source"
    query = "query"


class ObjectTypePlural(Enum):
    """Always a plural of the object type."""

    alerts = "alerts"
    dashboards = "dashboards"
    data_sources = "data_sources"
    queries = "queries"


@dataclass
class OdbcParams:

    hostname: str

    path: str

    port: int

    protocol: str

    def as_dict(self) -> dict:
        body = {}
        if self.hostname:
            body["hostname"] = self.hostname
        if self.path:
            body["path"] = self.path
        if self.port:
            body["port"] = self.port
        if self.protocol:
            body["protocol"] = self.protocol

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "OdbcParams":
        return cls(
            hostname=d.get("hostname", None),
            path=d.get("path", None),
            port=d.get("port", None),
            protocol=d.get("protocol", None),
        )


class OwnableObjectType(Enum):
    """The singular form of the type of object which can be owned."""

    alert = "alert"
    dashboard = "dashboard"
    query = "query"


@dataclass
class Parameter:

    # The literal parameter marker that appears between double curly braces in the query text.
    name: str
    # The text displayed in a parameter picking widget.
    title: str
    # Parameters can have several different types.
    type: "ParameterType"
    # The default value for this parameter.
    value: Any

    def as_dict(self) -> dict:
        body = {}
        if self.name:
            body["name"] = self.name
        if self.title:
            body["title"] = self.title
        if self.type:
            body["type"] = self.type.value
        if self.value:
            body["value"] = self.value

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "Parameter":
        return cls(
            name=d.get("name", None),
            title=d.get("title", None),
            type=ParameterType(d["type"]) if "type" in d else None,
            value=d.get("value", None),
        )


class ParameterType(Enum):
    """Parameters can have several different types."""

    datetime = "datetime"
    number = "number"
    text = "text"


class PermissionLevel(Enum):
    """This describes an enum"""

    CAN_MANAGE = "CAN_MANAGE"
    CAN_RUN = "CAN_RUN"
    CAN_VIEW = "CAN_VIEW"


class PlansState(Enum):
    """Whether plans exist for the execution, or the reason why they are missing"""

    EMPTY = "EMPTY"
    EXISTS = "EXISTS"
    IGNORED_LARGE_PLANS_SIZE = "IGNORED_LARGE_PLANS_SIZE"
    IGNORED_SMALL_DURATION = "IGNORED_SMALL_DURATION"
    IGNORED_SPARK_PLAN_TYPE = "IGNORED_SPARK_PLAN_TYPE"
    UNKNOWN = "UNKNOWN"


@dataclass
class Query:

    # Describes whether the authenticated user is allowed to edit the definition of this query.
    can_edit: bool
    # The timestamp when this query was created.
    created_at: str
    # Data Source ID. The UUID that uniquely identifies this data source / SQL warehouse across the API.
    data_source_id: str
    # General description that conveys additional information about this query such as usage notes.
    description: str

    id: str
    # Indicates whether the query is trashed. Trashed queries can't be used in dashboards, or appear in search results.
    # If this boolean is `true`, the `options` property for this query includes a `moved_to_trash_at` timestamp. Trashed
    # queries are permanently deleted after 30 days.
    is_archived: bool
    # Whether the query is a draft. Draft queries only appear in list views for their owners. Visualizations from draft
    # queries cannot appear on dashboards.
    is_draft: bool
    # Whether this query object appears in the current user's favorites list. This flag determines whether the star icon
    # for favorites is selected.
    is_favorite: bool
    # Text parameter types are not safe from SQL injection for all types of data source. Set this Boolean parameter to
    # `true` if a query either does not use any text type parameters or uses a data source type where text type
    # parameters are handled safely.
    is_safe: bool

    last_modified_by: "User"
    # The ID of the user who last saved changes to this query.
    last_modified_by_id: int
    # If there is a cached result for this query and user, this field includes the query result ID. If this query uses
    # parameters, this field is always null.
    latest_query_data_id: str
    # The title of this query that appears in list views, widget headings, and on the query page.
    name: str

    options: "QueryOptions"
    # This describes an enum
    permission_tier: "PermissionLevel"
    # The text of the query to be run.
    query: str
    # A SHA-256 hash of the query text along with the authenticated user ID.
    query_hash: str

    schedule: "QueryInterval"

    tags: "List[str]"
    # The timestamp at which this query was last updated.
    updated_at: str

    user: "User"
    # The ID of the user who created this query.
    user_id: int

    visualizations: "List[Visualization]"

    def as_dict(self) -> dict:
        body = {}
        if self.can_edit:
            body["can_edit"] = self.can_edit
        if self.created_at:
            body["created_at"] = self.created_at
        if self.data_source_id:
            body["data_source_id"] = self.data_source_id
        if self.description:
            body["description"] = self.description
        if self.id:
            body["id"] = self.id
        if self.is_archived:
            body["is_archived"] = self.is_archived
        if self.is_draft:
            body["is_draft"] = self.is_draft
        if self.is_favorite:
            body["is_favorite"] = self.is_favorite
        if self.is_safe:
            body["is_safe"] = self.is_safe
        if self.last_modified_by:
            body["last_modified_by"] = self.last_modified_by.as_dict()
        if self.last_modified_by_id:
            body["last_modified_by_id"] = self.last_modified_by_id
        if self.latest_query_data_id:
            body["latest_query_data_id"] = self.latest_query_data_id
        if self.name:
            body["name"] = self.name
        if self.options:
            body["options"] = self.options.as_dict()
        if self.permission_tier:
            body["permission_tier"] = self.permission_tier.value
        if self.query:
            body["query"] = self.query
        if self.query_hash:
            body["query_hash"] = self.query_hash
        if self.schedule:
            body["schedule"] = self.schedule.as_dict()
        if self.tags:
            body["tags"] = [v for v in self.tags]
        if self.updated_at:
            body["updated_at"] = self.updated_at
        if self.user:
            body["user"] = self.user.as_dict()
        if self.user_id:
            body["user_id"] = self.user_id
        if self.visualizations:
            body["visualizations"] = [v.as_dict() for v in self.visualizations]

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "Query":
        return cls(
            can_edit=d.get("can_edit", None),
            created_at=d.get("created_at", None),
            data_source_id=d.get("data_source_id", None),
            description=d.get("description", None),
            id=d.get("id", None),
            is_archived=d.get("is_archived", None),
            is_draft=d.get("is_draft", None),
            is_favorite=d.get("is_favorite", None),
            is_safe=d.get("is_safe", None),
            last_modified_by=User.from_dict(d["last_modified_by"])
            if "last_modified_by" in d
            else None,
            last_modified_by_id=d.get("last_modified_by_id", None),
            latest_query_data_id=d.get("latest_query_data_id", None),
            name=d.get("name", None),
            options=QueryOptions.from_dict(d["options"]) if "options" in d else None,
            permission_tier=PermissionLevel(d["permission_tier"])
            if "permission_tier" in d
            else None,
            query=d.get("query", None),
            query_hash=d.get("query_hash", None),
            schedule=QueryInterval.from_dict(d["schedule"])
            if "schedule" in d
            else None,
            tags=d.get("tags", None),
            updated_at=d.get("updated_at", None),
            user=User.from_dict(d["user"]) if "user" in d else None,
            user_id=d.get("user_id", None),
            visualizations=[Visualization.from_dict(v) for v in d["visualizations"]]
            if "visualizations" in d
            else None,
        )


@dataclass
class QueryFilter:
    """A filter to limit query history results. This field is optional."""

    query_start_time_range: "TimeRange"

    statuses: "List[QueryStatus]"
    # A list of user IDs who ran the queries.
    user_ids: "List[int]"
    # A list of warehouse IDs.
    warehouse_ids: "List[str]"

    def as_dict(self) -> dict:
        body = {}
        if self.query_start_time_range:
            body["query_start_time_range"] = self.query_start_time_range.as_dict()
        if self.statuses:
            body["statuses"] = [v for v in self.statuses]
        if self.user_ids:
            body["user_ids"] = [v for v in self.user_ids]
        if self.warehouse_ids:
            body["warehouse_ids"] = [v for v in self.warehouse_ids]

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "QueryFilter":
        return cls(
            query_start_time_range=TimeRange.from_dict(d["query_start_time_range"])
            if "query_start_time_range" in d
            else None,
            statuses=d.get("statuses", None),
            user_ids=d.get("user_ids", None),
            warehouse_ids=d.get("warehouse_ids", None),
        )


@dataclass
class QueryInfo:

    # Channel information for the SQL warehouse at the time of query execution
    channel_used: "ChannelInfo"
    # Total execution time of the query from the client’s point of view, in milliseconds.
    duration: int
    # Alias for `warehouse_id`.
    endpoint_id: str
    # Message describing why the query could not complete.
    error_message: str
    # The ID of the user whose credentials were used to run the query.
    executed_as_user_id: int
    # The email address or username of the user whose credentials were used to run the query.
    executed_as_user_name: str
    # The time execution of the query ended.
    execution_end_time_ms: int
    # Whether more updates for the query are expected.
    is_final: bool
    # A key that can be used to look up query details.
    lookup_key: str
    # Metrics about query execution.
    metrics: "QueryMetrics"
    # Whether plans exist for the execution, or the reason why they are missing
    plans_state: "PlansState"
    # The time the query ended.
    query_end_time_ms: int
    # The query ID.
    query_id: str
    # The time the query started.
    query_start_time_ms: int
    # The text of the query.
    query_text: str
    # The number of results returned by the query.
    rows_produced: int
    # URL to the query plan.
    spark_ui_url: str
    # Type of statement for this query
    statement_type: "QueryStatementType"
    # This describes an enum
    status: "QueryStatus"
    # The ID of the user who ran the query.
    user_id: int
    # The email address or username of the user who ran the query.
    user_name: str
    # Warehouse ID.
    warehouse_id: str

    def as_dict(self) -> dict:
        body = {}
        if self.channel_used:
            body["channel_used"] = self.channel_used.as_dict()
        if self.duration:
            body["duration"] = self.duration
        if self.endpoint_id:
            body["endpoint_id"] = self.endpoint_id
        if self.error_message:
            body["error_message"] = self.error_message
        if self.executed_as_user_id:
            body["executed_as_user_id"] = self.executed_as_user_id
        if self.executed_as_user_name:
            body["executed_as_user_name"] = self.executed_as_user_name
        if self.execution_end_time_ms:
            body["execution_end_time_ms"] = self.execution_end_time_ms
        if self.is_final:
            body["is_final"] = self.is_final
        if self.lookup_key:
            body["lookup_key"] = self.lookup_key
        if self.metrics:
            body["metrics"] = self.metrics.as_dict()
        if self.plans_state:
            body["plans_state"] = self.plans_state.value
        if self.query_end_time_ms:
            body["query_end_time_ms"] = self.query_end_time_ms
        if self.query_id:
            body["query_id"] = self.query_id
        if self.query_start_time_ms:
            body["query_start_time_ms"] = self.query_start_time_ms
        if self.query_text:
            body["query_text"] = self.query_text
        if self.rows_produced:
            body["rows_produced"] = self.rows_produced
        if self.spark_ui_url:
            body["spark_ui_url"] = self.spark_ui_url
        if self.statement_type:
            body["statement_type"] = self.statement_type.value
        if self.status:
            body["status"] = self.status.value
        if self.user_id:
            body["user_id"] = self.user_id
        if self.user_name:
            body["user_name"] = self.user_name
        if self.warehouse_id:
            body["warehouse_id"] = self.warehouse_id

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "QueryInfo":
        return cls(
            channel_used=ChannelInfo.from_dict(d["channel_used"])
            if "channel_used" in d
            else None,
            duration=d.get("duration", None),
            endpoint_id=d.get("endpoint_id", None),
            error_message=d.get("error_message", None),
            executed_as_user_id=d.get("executed_as_user_id", None),
            executed_as_user_name=d.get("executed_as_user_name", None),
            execution_end_time_ms=d.get("execution_end_time_ms", None),
            is_final=d.get("is_final", None),
            lookup_key=d.get("lookup_key", None),
            metrics=QueryMetrics.from_dict(d["metrics"]) if "metrics" in d else None,
            plans_state=PlansState(d["plans_state"]) if "plans_state" in d else None,
            query_end_time_ms=d.get("query_end_time_ms", None),
            query_id=d.get("query_id", None),
            query_start_time_ms=d.get("query_start_time_ms", None),
            query_text=d.get("query_text", None),
            rows_produced=d.get("rows_produced", None),
            spark_ui_url=d.get("spark_ui_url", None),
            statement_type=QueryStatementType(d["statement_type"])
            if "statement_type" in d
            else None,
            status=QueryStatus(d["status"]) if "status" in d else None,
            user_id=d.get("user_id", None),
            user_name=d.get("user_name", None),
            warehouse_id=d.get("warehouse_id", None),
        )


@dataclass
class QueryInterval:

    # For weekly runs, the day of the week to start the run.
    day_of_week: str
    # Integer number of seconds between runs.
    interval: int
    # For daily, weekly, and monthly runs, the time of day to start the run.
    time: str
    # A date after which this schedule no longer applies.
    until: str

    def as_dict(self) -> dict:
        body = {}
        if self.day_of_week:
            body["day_of_week"] = self.day_of_week
        if self.interval:
            body["interval"] = self.interval
        if self.time:
            body["time"] = self.time
        if self.until:
            body["until"] = self.until

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "QueryInterval":
        return cls(
            day_of_week=d.get("day_of_week", None),
            interval=d.get("interval", None),
            time=d.get("time", None),
            until=d.get("until", None),
        )


@dataclass
class QueryList:

    # The total number of queries.
    count: int
    # The page number that is currently displayed.
    page: int
    # The number of queries per page.
    page_size: int
    # List of queries returned.
    results: "List[Query]"

    def as_dict(self) -> dict:
        body = {}
        if self.count:
            body["count"] = self.count
        if self.page:
            body["page"] = self.page
        if self.page_size:
            body["page_size"] = self.page_size
        if self.results:
            body["results"] = [v.as_dict() for v in self.results]

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "QueryList":
        return cls(
            count=d.get("count", None),
            page=d.get("page", None),
            page_size=d.get("page_size", None),
            results=[Query.from_dict(v) for v in d["results"]]
            if "results" in d
            else None,
        )


@dataclass
class QueryMetrics:
    """Metrics about query execution."""

    # Time spent loading metadata and optimizing the query, in milliseconds.
    compilation_time_ms: int
    # Time spent executing the query, in milliseconds.
    execution_time_ms: int
    # Total amount of data sent over the network, in bytes.
    network_sent_bytes: int
    # Total execution time for all individual Photon query engine tasks in the query, in milliseconds.
    photon_total_time_ms: int
    # Time spent waiting to execute the query because the SQL warehouse is already running the maximum number of
    # concurrent queries, in milliseconds.
    queued_overload_time_ms: int
    # Time waiting for compute resources to be provisioned for the SQL warehouse, in milliseconds.
    queued_provisioning_time_ms: int
    # Total size of data read by the query, in bytes.
    read_bytes: int
    # Size of persistent data read from the cache, in bytes.
    read_cache_bytes: int
    # Number of files read after pruning.
    read_files_count: int
    # Number of partitions read after pruning.
    read_partitions_count: int
    # Size of persistent data read from cloud object storage on your cloud tenant, in bytes.
    read_remote_bytes: int
    # Time spent fetching the query results after the execution finished, in milliseconds.
    result_fetch_time_ms: int
    # true if the query result was fetched from cache, false otherwise.
    result_from_cache: bool
    # Total number of rows returned by the query.
    rows_produced_count: int
    # Total number of rows read by the query.
    rows_read_count: int
    # Size of data temporarily written to disk while executing the query, in bytes.
    spill_to_disk_bytes: int
    # Sum of execution time for all of the query’s tasks, in milliseconds.
    task_total_time_ms: int
    # Number of files that would have been read without pruning.
    total_files_count: int
    # Number of partitions that would have been read without pruning.
    total_partitions_count: int
    # Total execution time of the query from the client’s point of view, in milliseconds.
    total_time_ms: int
    # Size pf persistent data written to cloud object storage in your cloud tenant, in bytes.
    write_remote_bytes: int

    def as_dict(self) -> dict:
        body = {}
        if self.compilation_time_ms:
            body["compilation_time_ms"] = self.compilation_time_ms
        if self.execution_time_ms:
            body["execution_time_ms"] = self.execution_time_ms
        if self.network_sent_bytes:
            body["network_sent_bytes"] = self.network_sent_bytes
        if self.photon_total_time_ms:
            body["photon_total_time_ms"] = self.photon_total_time_ms
        if self.queued_overload_time_ms:
            body["queued_overload_time_ms"] = self.queued_overload_time_ms
        if self.queued_provisioning_time_ms:
            body["queued_provisioning_time_ms"] = self.queued_provisioning_time_ms
        if self.read_bytes:
            body["read_bytes"] = self.read_bytes
        if self.read_cache_bytes:
            body["read_cache_bytes"] = self.read_cache_bytes
        if self.read_files_count:
            body["read_files_count"] = self.read_files_count
        if self.read_partitions_count:
            body["read_partitions_count"] = self.read_partitions_count
        if self.read_remote_bytes:
            body["read_remote_bytes"] = self.read_remote_bytes
        if self.result_fetch_time_ms:
            body["result_fetch_time_ms"] = self.result_fetch_time_ms
        if self.result_from_cache:
            body["result_from_cache"] = self.result_from_cache
        if self.rows_produced_count:
            body["rows_produced_count"] = self.rows_produced_count
        if self.rows_read_count:
            body["rows_read_count"] = self.rows_read_count
        if self.spill_to_disk_bytes:
            body["spill_to_disk_bytes"] = self.spill_to_disk_bytes
        if self.task_total_time_ms:
            body["task_total_time_ms"] = self.task_total_time_ms
        if self.total_files_count:
            body["total_files_count"] = self.total_files_count
        if self.total_partitions_count:
            body["total_partitions_count"] = self.total_partitions_count
        if self.total_time_ms:
            body["total_time_ms"] = self.total_time_ms
        if self.write_remote_bytes:
            body["write_remote_bytes"] = self.write_remote_bytes

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "QueryMetrics":
        return cls(
            compilation_time_ms=d.get("compilation_time_ms", None),
            execution_time_ms=d.get("execution_time_ms", None),
            network_sent_bytes=d.get("network_sent_bytes", None),
            photon_total_time_ms=d.get("photon_total_time_ms", None),
            queued_overload_time_ms=d.get("queued_overload_time_ms", None),
            queued_provisioning_time_ms=d.get("queued_provisioning_time_ms", None),
            read_bytes=d.get("read_bytes", None),
            read_cache_bytes=d.get("read_cache_bytes", None),
            read_files_count=d.get("read_files_count", None),
            read_partitions_count=d.get("read_partitions_count", None),
            read_remote_bytes=d.get("read_remote_bytes", None),
            result_fetch_time_ms=d.get("result_fetch_time_ms", None),
            result_from_cache=d.get("result_from_cache", None),
            rows_produced_count=d.get("rows_produced_count", None),
            rows_read_count=d.get("rows_read_count", None),
            spill_to_disk_bytes=d.get("spill_to_disk_bytes", None),
            task_total_time_ms=d.get("task_total_time_ms", None),
            total_files_count=d.get("total_files_count", None),
            total_partitions_count=d.get("total_partitions_count", None),
            total_time_ms=d.get("total_time_ms", None),
            write_remote_bytes=d.get("write_remote_bytes", None),
        )


@dataclass
class QueryOptions:

    # The timestamp when this query was moved to trash. Only present when the `is_archived` property is `true`. Trashed
    # items are deleted after thirty days.
    moved_to_trash_at: str

    parameters: "List[Parameter]"

    def as_dict(self) -> dict:
        body = {}
        if self.moved_to_trash_at:
            body["moved_to_trash_at"] = self.moved_to_trash_at
        if self.parameters:
            body["parameters"] = [v.as_dict() for v in self.parameters]

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "QueryOptions":
        return cls(
            moved_to_trash_at=d.get("moved_to_trash_at", None),
            parameters=[Parameter.from_dict(v) for v in d["parameters"]]
            if "parameters" in d
            else None,
        )


@dataclass
class QueryPostContent:

    # The ID of the data source / SQL warehouse where this query will run.
    data_source_id: str
    # General description that can convey additional information about this query such as usage notes.
    description: str
    # The name or title of this query to display in list views.
    name: str
    # Exclusively used for storing a list parameter definitions. A parameter is an object with `title`, `name`, `type`,
    # and `value` properties. The `value` field here is the default value. It can be overridden at runtime.
    options: Any
    # The text of the query.
    query: str

    query_id: str  # path
    # JSON object that describes the scheduled execution frequency. A schedule object includes `interval`, `time`,
    # `day_of_week`, and `until` fields. If a scheduled is supplied, then only `interval` is required. All other field
    # can be `null`.
    schedule: "QueryInterval"

    def as_dict(self) -> dict:
        body = {}
        if self.data_source_id:
            body["data_source_id"] = self.data_source_id
        if self.description:
            body["description"] = self.description
        if self.name:
            body["name"] = self.name
        if self.options:
            body["options"] = self.options
        if self.query:
            body["query"] = self.query
        if self.query_id:
            body["query_id"] = self.query_id
        if self.schedule:
            body["schedule"] = self.schedule.as_dict()

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "QueryPostContent":
        return cls(
            data_source_id=d.get("data_source_id", None),
            description=d.get("description", None),
            name=d.get("name", None),
            options=d.get("options", None),
            query=d.get("query", None),
            query_id=d.get("query_id", None),
            schedule=QueryInterval.from_dict(d["schedule"])
            if "schedule" in d
            else None,
        )


class QueryStatementType(Enum):
    """Type of statement for this query"""

    ALTER = "ALTER"
    ANALYZE = "ANALYZE"
    COPY = "COPY"
    CREATE = "CREATE"
    DELETE = "DELETE"
    DESCRIBE = "DESCRIBE"
    DROP = "DROP"
    EXPLAIN = "EXPLAIN"
    GRANT = "GRANT"
    INSERT = "INSERT"
    MERGE = "MERGE"
    OPTIMIZE = "OPTIMIZE"
    OTHER = "OTHER"
    REFRESH = "REFRESH"
    REPLACE = "REPLACE"
    REVOKE = "REVOKE"
    SELECT = "SELECT"
    SET = "SET"
    SHOW = "SHOW"
    TRUNCATE = "TRUNCATE"
    UPDATE = "UPDATE"
    USE = "USE"


class QueryStatus(Enum):
    """This describes an enum"""

    CANCELED = "CANCELED"
    FAILED = "FAILED"
    FINISHED = "FINISHED"
    QUEUED = "QUEUED"
    RUNNING = "RUNNING"


@dataclass
class RefreshSchedule:

    # Cron string representing the refresh schedule.
    cron: str
    # ID of the SQL warehouse to refresh with. If `null`, query's SQL warehouse will be used to refresh.
    data_source_id: str
    # ID of the refresh schedule.
    id: str

    def as_dict(self) -> dict:
        body = {}
        if self.cron:
            body["cron"] = self.cron
        if self.data_source_id:
            body["data_source_id"] = self.data_source_id
        if self.id:
            body["id"] = self.id

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "RefreshSchedule":
        return cls(
            cron=d.get("cron", None),
            data_source_id=d.get("data_source_id", None),
            id=d.get("id", None),
        )


@dataclass
class RepeatedEndpointConfPairs:

    # Deprecated: Use configuration_pairs
    config_pair: "List[EndpointConfPair]"

    configuration_pairs: "List[EndpointConfPair]"

    def as_dict(self) -> dict:
        body = {}
        if self.config_pair:
            body["config_pair"] = [v.as_dict() for v in self.config_pair]
        if self.configuration_pairs:
            body["configuration_pairs"] = [
                v.as_dict() for v in self.configuration_pairs
            ]

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "RepeatedEndpointConfPairs":
        return cls(
            config_pair=[EndpointConfPair.from_dict(v) for v in d["config_pair"]]
            if "config_pair" in d
            else None,
            configuration_pairs=[
                EndpointConfPair.from_dict(v) for v in d["configuration_pairs"]
            ]
            if "configuration_pairs" in d
            else None,
        )


@dataclass
class RestoreDashboardRequest:
    """Restore a dashboard"""

    dashboard_id: str  # path

    def as_dict(self) -> dict:
        body = {}
        if self.dashboard_id:
            body["dashboard_id"] = self.dashboard_id

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "RestoreDashboardRequest":
        return cls(
            dashboard_id=d.get("dashboard_id", None),
        )


@dataclass
class RestoreQueryRequest:
    """Restore a query"""

    query_id: str  # path

    def as_dict(self) -> dict:
        body = {}
        if self.query_id:
            body["query_id"] = self.query_id

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "RestoreQueryRequest":
        return cls(
            query_id=d.get("query_id", None),
        )


@dataclass
class SetRequest:
    """Set object ACL"""

    access_control_list: "List[AccessControl]"
    # Object ID. The ACL for the object with this UUID is overwritten by this request's POST content.
    objectId: str  # path
    # The type of object permission to set.
    objectType: "ObjectTypePlural"  # path

    def as_dict(self) -> dict:
        body = {}
        if self.access_control_list:
            body["access_control_list"] = [
                v.as_dict() for v in self.access_control_list
            ]
        if self.objectId:
            body["objectId"] = self.objectId
        if self.objectType:
            body["objectType"] = self.objectType.value

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "SetRequest":
        return cls(
            access_control_list=[
                AccessControl.from_dict(v) for v in d["access_control_list"]
            ]
            if "access_control_list" in d
            else None,
            objectId=d.get("objectId", None),
            objectType=ObjectTypePlural(d["objectType"]) if "objectType" in d else None,
        )


@dataclass
class SetResponse:

    access_control_list: "List[AccessControl]"
    # A singular noun object type.
    object_id: "ObjectType"
    # An object's type and UUID, separated by a forward slash (/) character.
    object_type: str

    def as_dict(self) -> dict:
        body = {}
        if self.access_control_list:
            body["access_control_list"] = [
                v.as_dict() for v in self.access_control_list
            ]
        if self.object_id:
            body["object_id"] = self.object_id.value
        if self.object_type:
            body["object_type"] = self.object_type

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "SetResponse":
        return cls(
            access_control_list=[
                AccessControl.from_dict(v) for v in d["access_control_list"]
            ]
            if "access_control_list" in d
            else None,
            object_id=ObjectType(d["object_id"]) if "object_id" in d else None,
            object_type=d.get("object_type", None),
        )


@dataclass
class SetWorkspaceWarehouseConfigRequest:

    # Optional: Channel selection details
    channel: "Channel"
    # Deprecated: Use sql_configuration_parameters
    config_param: "RepeatedEndpointConfPairs"
    # Spark confs for external hive metastore configuration JSON serialized size must be less than <= 512K
    data_access_config: "List[EndpointConfPair]"
    # Enable Serverless compute for SQL Endpoints
    #
    # Deprecated: Use enable_serverless_compute TODO(SC-79930): Remove the field once clients are updated
    enable_databricks_compute: bool
    # Enable Serverless compute for SQL Endpoints
    enable_serverless_compute: bool
    # List of Warehouse Types allowed in this workspace (limits allowed value of the type field in CreateWarehouse and
    # EditWarehouse). Note: Some types cannot be disabled, they don't need to be specified in
    # SetWorkspaceWarehouseConfig. Note: Disabling a type may cause existing warehouses to be converted to another type.
    # Used by frontend to save specific type availability in the warehouse create and edit form UI.
    enabled_warehouse_types: "List[WarehouseTypePair]"
    # Deprecated: Use sql_configuration_parameters
    global_param: "RepeatedEndpointConfPairs"
    # GCP only: Google Service Account used to pass to cluster to access Google Cloud Storage
    google_service_account: str
    # AWS Only: Instance profile used to pass IAM role to the cluster
    instance_profile_arn: str
    # Security policy for endpoints
    security_policy: "SetWorkspaceWarehouseConfigRequestSecurityPolicy"
    # Internal. Used by frontend to save Serverless Compute agreement value.
    serverless_agreement: bool
    # SQL configuration parameters
    sql_configuration_parameters: "RepeatedEndpointConfPairs"

    def as_dict(self) -> dict:
        body = {}
        if self.channel:
            body["channel"] = self.channel.as_dict()
        if self.config_param:
            body["config_param"] = self.config_param.as_dict()
        if self.data_access_config:
            body["data_access_config"] = [v.as_dict() for v in self.data_access_config]
        if self.enable_databricks_compute:
            body["enable_databricks_compute"] = self.enable_databricks_compute
        if self.enable_serverless_compute:
            body["enable_serverless_compute"] = self.enable_serverless_compute
        if self.enabled_warehouse_types:
            body["enabled_warehouse_types"] = [
                v.as_dict() for v in self.enabled_warehouse_types
            ]
        if self.global_param:
            body["global_param"] = self.global_param.as_dict()
        if self.google_service_account:
            body["google_service_account"] = self.google_service_account
        if self.instance_profile_arn:
            body["instance_profile_arn"] = self.instance_profile_arn
        if self.security_policy:
            body["security_policy"] = self.security_policy.value
        if self.serverless_agreement:
            body["serverless_agreement"] = self.serverless_agreement
        if self.sql_configuration_parameters:
            body[
                "sql_configuration_parameters"
            ] = self.sql_configuration_parameters.as_dict()

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "SetWorkspaceWarehouseConfigRequest":
        return cls(
            channel=Channel.from_dict(d["channel"]) if "channel" in d else None,
            config_param=RepeatedEndpointConfPairs.from_dict(d["config_param"])
            if "config_param" in d
            else None,
            data_access_config=[
                EndpointConfPair.from_dict(v) for v in d["data_access_config"]
            ]
            if "data_access_config" in d
            else None,
            enable_databricks_compute=d.get("enable_databricks_compute", None),
            enable_serverless_compute=d.get("enable_serverless_compute", None),
            enabled_warehouse_types=[
                WarehouseTypePair.from_dict(v) for v in d["enabled_warehouse_types"]
            ]
            if "enabled_warehouse_types" in d
            else None,
            global_param=RepeatedEndpointConfPairs.from_dict(d["global_param"])
            if "global_param" in d
            else None,
            google_service_account=d.get("google_service_account", None),
            instance_profile_arn=d.get("instance_profile_arn", None),
            security_policy=SetWorkspaceWarehouseConfigRequestSecurityPolicy(
                d["security_policy"]
            )
            if "security_policy" in d
            else None,
            serverless_agreement=d.get("serverless_agreement", None),
            sql_configuration_parameters=RepeatedEndpointConfPairs.from_dict(
                d["sql_configuration_parameters"]
            )
            if "sql_configuration_parameters" in d
            else None,
        )


class SetWorkspaceWarehouseConfigRequestSecurityPolicy(Enum):
    """Security policy for endpoints"""

    DATA_ACCESS_CONTROL = "DATA_ACCESS_CONTROL"
    NONE = "NONE"
    PASSTHROUGH = "PASSTHROUGH"


class SpotInstancePolicy(Enum):
    """Configurations whether the warehouse should use spot instances."""

    COST_OPTIMIZED = "COST_OPTIMIZED"
    POLICY_UNSPECIFIED = "POLICY_UNSPECIFIED"
    RELIABILITY_OPTIMIZED = "RELIABILITY_OPTIMIZED"


@dataclass
class StartRequest:
    """Start a warehouse"""

    # Required. Id of the SQL warehouse.
    id: str  # path

    def as_dict(self) -> dict:
        body = {}
        if self.id:
            body["id"] = self.id

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "StartRequest":
        return cls(
            id=d.get("id", None),
        )


class State(Enum):
    """State of the warehouse"""

    DELETED = "DELETED"
    DELETING = "DELETING"
    RUNNING = "RUNNING"
    STARTING = "STARTING"
    STOPPED = "STOPPED"
    STOPPING = "STOPPING"


class Status(Enum):
    """Health status of the endpoint."""

    DEGRADED = "DEGRADED"
    FAILED = "FAILED"
    HEALTHY = "HEALTHY"
    STATUS_UNSPECIFIED = "STATUS_UNSPECIFIED"


@dataclass
class StopRequest:
    """Stop a warehouse"""

    # Required. Id of the SQL warehouse.
    id: str  # path

    def as_dict(self) -> dict:
        body = {}
        if self.id:
            body["id"] = self.id

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "StopRequest":
        return cls(
            id=d.get("id", None),
        )


@dataclass
class Subscription:

    # ID of the alert.
    alert_id: str
    # Alert destination subscribed to the alert, if it exists. Alert destinations can be configured by admins through
    # the UI. See [here].
    #
    # [here]: https://docs.databricks.com/sql/admin/alert-destinations.html
    destination: "Destination"
    # ID of the alert subscription.
    id: str

    user: "User"

    def as_dict(self) -> dict:
        body = {}
        if self.alert_id:
            body["alert_id"] = self.alert_id
        if self.destination:
            body["destination"] = self.destination.as_dict()
        if self.id:
            body["id"] = self.id
        if self.user:
            body["user"] = self.user.as_dict()

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "Subscription":
        return cls(
            alert_id=d.get("alert_id", None),
            destination=Destination.from_dict(d["destination"])
            if "destination" in d
            else None,
            id=d.get("id", None),
            user=User.from_dict(d["user"]) if "user" in d else None,
        )


@dataclass
class Success:

    message: "SuccessMessage"

    def as_dict(self) -> dict:
        body = {}
        if self.message:
            body["message"] = self.message.value

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "Success":
        return cls(
            message=SuccessMessage(d["message"]) if "message" in d else None,
        )


class SuccessMessage(Enum):

    Success = "Success"


@dataclass
class TerminationReason:

    # status code indicating why the cluster was terminated
    code: "TerminationReasonCode"
    # list of parameters that provide additional information about why the cluster was terminated
    parameters: "Dict[str,str]"
    # type of the termination
    type: "TerminationReasonType"

    def as_dict(self) -> dict:
        body = {}
        if self.code:
            body["code"] = self.code.value
        if self.parameters:
            body["parameters"] = self.parameters
        if self.type:
            body["type"] = self.type.value

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "TerminationReason":
        return cls(
            code=TerminationReasonCode(d["code"]) if "code" in d else None,
            parameters=d.get("parameters", None),
            type=TerminationReasonType(d["type"]) if "type" in d else None,
        )


class TerminationReasonCode(Enum):
    """status code indicating why the cluster was terminated"""

    ABUSE_DETECTED = "ABUSE_DETECTED"
    ATTACH_PROJECT_FAILURE = "ATTACH_PROJECT_FAILURE"
    AWS_AUTHORIZATION_FAILURE = "AWS_AUTHORIZATION_FAILURE"
    AWS_INSUFFICIENT_FREE_ADDRESSES_IN_SUBNET_FAILURE = (
        "AWS_INSUFFICIENT_FREE_ADDRESSES_IN_SUBNET_FAILURE"
    )
    AWS_INSUFFICIENT_INSTANCE_CAPACITY_FAILURE = (
        "AWS_INSUFFICIENT_INSTANCE_CAPACITY_FAILURE"
    )
    AWS_MAX_SPOT_INSTANCE_COUNT_EXCEEDED_FAILURE = (
        "AWS_MAX_SPOT_INSTANCE_COUNT_EXCEEDED_FAILURE"
    )
    AWS_REQUEST_LIMIT_EXCEEDED = "AWS_REQUEST_LIMIT_EXCEEDED"
    AWS_UNSUPPORTED_FAILURE = "AWS_UNSUPPORTED_FAILURE"
    AZURE_BYOK_KEY_PERMISSION_FAILURE = "AZURE_BYOK_KEY_PERMISSION_FAILURE"
    AZURE_EPHEMERAL_DISK_FAILURE = "AZURE_EPHEMERAL_DISK_FAILURE"
    AZURE_INVALID_DEPLOYMENT_TEMPLATE = "AZURE_INVALID_DEPLOYMENT_TEMPLATE"
    AZURE_OPERATION_NOT_ALLOWED_EXCEPTION = "AZURE_OPERATION_NOT_ALLOWED_EXCEPTION"
    AZURE_QUOTA_EXCEEDED_EXCEPTION = "AZURE_QUOTA_EXCEEDED_EXCEPTION"
    AZURE_RESOURCE_MANAGER_THROTTLING = "AZURE_RESOURCE_MANAGER_THROTTLING"
    AZURE_RESOURCE_PROVIDER_THROTTLING = "AZURE_RESOURCE_PROVIDER_THROTTLING"
    AZURE_UNEXPECTED_DEPLOYMENT_TEMPLATE_FAILURE = (
        "AZURE_UNEXPECTED_DEPLOYMENT_TEMPLATE_FAILURE"
    )
    AZURE_VM_EXTENSION_FAILURE = "AZURE_VM_EXTENSION_FAILURE"
    AZURE_VNET_CONFIGURATION_FAILURE = "AZURE_VNET_CONFIGURATION_FAILURE"
    BOOTSTRAP_TIMEOUT = "BOOTSTRAP_TIMEOUT"
    BOOTSTRAP_TIMEOUT_CLOUD_PROVIDER_EXCEPTION = (
        "BOOTSTRAP_TIMEOUT_CLOUD_PROVIDER_EXCEPTION"
    )
    CLOUD_PROVIDER_DISK_SETUP_FAILURE = "CLOUD_PROVIDER_DISK_SETUP_FAILURE"
    CLOUD_PROVIDER_LAUNCH_FAILURE = "CLOUD_PROVIDER_LAUNCH_FAILURE"
    CLOUD_PROVIDER_RESOURCE_STOCKOUT = "CLOUD_PROVIDER_RESOURCE_STOCKOUT"
    CLOUD_PROVIDER_SHUTDOWN = "CLOUD_PROVIDER_SHUTDOWN"
    COMMUNICATION_LOST = "COMMUNICATION_LOST"
    CONTAINER_LAUNCH_FAILURE = "CONTAINER_LAUNCH_FAILURE"
    CONTROL_PLANE_REQUEST_FAILURE = "CONTROL_PLANE_REQUEST_FAILURE"
    DATABASE_CONNECTION_FAILURE = "DATABASE_CONNECTION_FAILURE"
    DBFS_COMPONENT_UNHEALTHY = "DBFS_COMPONENT_UNHEALTHY"
    DOCKER_IMAGE_PULL_FAILURE = "DOCKER_IMAGE_PULL_FAILURE"
    DRIVER_UNREACHABLE = "DRIVER_UNREACHABLE"
    DRIVER_UNRESPONSIVE = "DRIVER_UNRESPONSIVE"
    EXECUTION_COMPONENT_UNHEALTHY = "EXECUTION_COMPONENT_UNHEALTHY"
    GCP_QUOTA_EXCEEDED = "GCP_QUOTA_EXCEEDED"
    GCP_SERVICE_ACCOUNT_DELETED = "GCP_SERVICE_ACCOUNT_DELETED"
    GLOBAL_INIT_SCRIPT_FAILURE = "GLOBAL_INIT_SCRIPT_FAILURE"
    HIVE_METASTORE_PROVISIONING_FAILURE = "HIVE_METASTORE_PROVISIONING_FAILURE"
    IMAGE_PULL_PERMISSION_DENIED = "IMAGE_PULL_PERMISSION_DENIED"
    INACTIVITY = "INACTIVITY"
    INIT_SCRIPT_FAILURE = "INIT_SCRIPT_FAILURE"
    INSTANCE_POOL_CLUSTER_FAILURE = "INSTANCE_POOL_CLUSTER_FAILURE"
    INSTANCE_UNREACHABLE = "INSTANCE_UNREACHABLE"
    INTERNAL_ERROR = "INTERNAL_ERROR"
    INVALID_ARGUMENT = "INVALID_ARGUMENT"
    INVALID_SPARK_IMAGE = "INVALID_SPARK_IMAGE"
    IP_EXHAUSTION_FAILURE = "IP_EXHAUSTION_FAILURE"
    JOB_FINISHED = "JOB_FINISHED"
    K8S_AUTOSCALING_FAILURE = "K8S_AUTOSCALING_FAILURE"
    K8S_DBR_CLUSTER_LAUNCH_TIMEOUT = "K8S_DBR_CLUSTER_LAUNCH_TIMEOUT"
    METASTORE_COMPONENT_UNHEALTHY = "METASTORE_COMPONENT_UNHEALTHY"
    NEPHOS_RESOURCE_MANAGEMENT = "NEPHOS_RESOURCE_MANAGEMENT"
    NETWORK_CONFIGURATION_FAILURE = "NETWORK_CONFIGURATION_FAILURE"
    NFS_MOUNT_FAILURE = "NFS_MOUNT_FAILURE"
    NPIP_TUNNEL_SETUP_FAILURE = "NPIP_TUNNEL_SETUP_FAILURE"
    NPIP_TUNNEL_TOKEN_FAILURE = "NPIP_TUNNEL_TOKEN_FAILURE"
    REQUEST_REJECTED = "REQUEST_REJECTED"
    REQUEST_THROTTLED = "REQUEST_THROTTLED"
    SECRET_RESOLUTION_ERROR = "SECRET_RESOLUTION_ERROR"
    SECURITY_DAEMON_REGISTRATION_EXCEPTION = "SECURITY_DAEMON_REGISTRATION_EXCEPTION"
    SELF_BOOTSTRAP_FAILURE = "SELF_BOOTSTRAP_FAILURE"
    SKIPPED_SLOW_NODES = "SKIPPED_SLOW_NODES"
    SLOW_IMAGE_DOWNLOAD = "SLOW_IMAGE_DOWNLOAD"
    SPARK_ERROR = "SPARK_ERROR"
    SPARK_IMAGE_DOWNLOAD_FAILURE = "SPARK_IMAGE_DOWNLOAD_FAILURE"
    SPARK_STARTUP_FAILURE = "SPARK_STARTUP_FAILURE"
    SPOT_INSTANCE_TERMINATION = "SPOT_INSTANCE_TERMINATION"
    STORAGE_DOWNLOAD_FAILURE = "STORAGE_DOWNLOAD_FAILURE"
    STS_CLIENT_SETUP_FAILURE = "STS_CLIENT_SETUP_FAILURE"
    SUBNET_EXHAUSTED_FAILURE = "SUBNET_EXHAUSTED_FAILURE"
    TEMPORARILY_UNAVAILABLE = "TEMPORARILY_UNAVAILABLE"
    TRIAL_EXPIRED = "TRIAL_EXPIRED"
    UNEXPECTED_LAUNCH_FAILURE = "UNEXPECTED_LAUNCH_FAILURE"
    UNKNOWN = "UNKNOWN"
    UNSUPPORTED_INSTANCE_TYPE = "UNSUPPORTED_INSTANCE_TYPE"
    UPDATE_INSTANCE_PROFILE_FAILURE = "UPDATE_INSTANCE_PROFILE_FAILURE"
    USER_REQUEST = "USER_REQUEST"
    WORKER_SETUP_FAILURE = "WORKER_SETUP_FAILURE"
    WORKSPACE_CANCELLED_ERROR = "WORKSPACE_CANCELLED_ERROR"
    WORKSPACE_CONFIGURATION_ERROR = "WORKSPACE_CONFIGURATION_ERROR"


class TerminationReasonType(Enum):
    """type of the termination"""

    CLIENT_ERROR = "CLIENT_ERROR"
    CLOUD_FAILURE = "CLOUD_FAILURE"
    SERVICE_FAULT = "SERVICE_FAULT"
    SUCCESS = "SUCCESS"


@dataclass
class TimeRange:

    # Limit results to queries that started before this time.
    end_time_ms: int
    # Limit results to queries that started after this time.
    start_time_ms: int

    def as_dict(self) -> dict:
        body = {}
        if self.end_time_ms:
            body["end_time_ms"] = self.end_time_ms
        if self.start_time_ms:
            body["start_time_ms"] = self.start_time_ms

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "TimeRange":
        return cls(
            end_time_ms=d.get("end_time_ms", None),
            start_time_ms=d.get("start_time_ms", None),
        )


@dataclass
class TransferOwnershipObjectId:

    # Email address for the new owner, who must exist in the workspace.
    new_owner: str

    def as_dict(self) -> dict:
        body = {}
        if self.new_owner:
            body["new_owner"] = self.new_owner

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "TransferOwnershipObjectId":
        return cls(
            new_owner=d.get("new_owner", None),
        )


@dataclass
class TransferOwnershipRequest:
    """Transfer object ownership"""

    # Email address for the new owner, who must exist in the workspace.
    new_owner: str
    # The ID of the object on which to change ownership.
    objectId: "TransferOwnershipObjectId"  # path
    # The type of object on which to change ownership.
    objectType: "OwnableObjectType"  # path

    def as_dict(self) -> dict:
        body = {}
        if self.new_owner:
            body["new_owner"] = self.new_owner
        if self.objectId:
            body["objectId"] = self.objectId.as_dict()
        if self.objectType:
            body["objectType"] = self.objectType.value

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "TransferOwnershipRequest":
        return cls(
            new_owner=d.get("new_owner", None),
            objectId=TransferOwnershipObjectId.from_dict(d["objectId"])
            if "objectId" in d
            else None,
            objectType=OwnableObjectType(d["objectType"])
            if "objectType" in d
            else None,
        )


@dataclass
class UnsubscribeRequest:
    """Unsubscribe to an alert"""

    alert_id: str  # path

    subscription_id: str  # path

    def as_dict(self) -> dict:
        body = {}
        if self.alert_id:
            body["alert_id"] = self.alert_id
        if self.subscription_id:
            body["subscription_id"] = self.subscription_id

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "UnsubscribeRequest":
        return cls(
            alert_id=d.get("alert_id", None),
            subscription_id=d.get("subscription_id", None),
        )


@dataclass
class User:

    email: str

    id: int
    # Whether this user is an admin in the Databricks workspace.
    is_db_admin: bool

    name: str
    # The URL for the gravatar profile picture tied to this user's email address.
    profile_image_url: str

    def as_dict(self) -> dict:
        body = {}
        if self.email:
            body["email"] = self.email
        if self.id:
            body["id"] = self.id
        if self.is_db_admin:
            body["is_db_admin"] = self.is_db_admin
        if self.name:
            body["name"] = self.name
        if self.profile_image_url:
            body["profile_image_url"] = self.profile_image_url

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "User":
        return cls(
            email=d.get("email", None),
            id=d.get("id", None),
            is_db_admin=d.get("is_db_admin", None),
            name=d.get("name", None),
            profile_image_url=d.get("profile_image_url", None),
        )


@dataclass
class Visualization:
    """The visualization description API changes frequently and is unsupported. You
    can duplicate a visualization by copying description objects received _from
    the API_ and then using them to create a new one with a POST request to the
    same endpoint. Databricks does not recommend constructing ad-hoc
    visualizations entirely in JSON."""

    created_at: str
    # A short description of this visualization. This is not displayed in the UI.
    description: str
    # The UUID for this visualization.
    id: str
    # The name of the visualization that appears on dashboards and the query screen.
    name: str
    # The options object varies widely from one visualization type to the next and is unsupported. Databricks does not
    # recommend modifying visualization settings in JSON.
    options: Any
    # The type of visualization: chart, table, pivot table, and so on.
    type: str

    updated_at: str

    def as_dict(self) -> dict:
        body = {}
        if self.created_at:
            body["created_at"] = self.created_at
        if self.description:
            body["description"] = self.description
        if self.id:
            body["id"] = self.id
        if self.name:
            body["name"] = self.name
        if self.options:
            body["options"] = self.options
        if self.type:
            body["type"] = self.type
        if self.updated_at:
            body["updated_at"] = self.updated_at

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "Visualization":
        return cls(
            created_at=d.get("created_at", None),
            description=d.get("description", None),
            id=d.get("id", None),
            name=d.get("name", None),
            options=d.get("options", None),
            type=d.get("type", None),
            updated_at=d.get("updated_at", None),
        )


class WarehouseType(Enum):

    CLASSIC = "CLASSIC"
    PRO = "PRO"
    TYPE_UNSPECIFIED = "TYPE_UNSPECIFIED"


@dataclass
class WarehouseTypePair:

    # If set to false the specific warehouse type will not be be allowed as a value for warehouse_type in
    # CreateWarehouse and EditWarehouse
    enabled: bool

    warehouse_type: "WarehouseType"

    def as_dict(self) -> dict:
        body = {}
        if self.enabled:
            body["enabled"] = self.enabled
        if self.warehouse_type:
            body["warehouse_type"] = self.warehouse_type.value

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "WarehouseTypePair":
        return cls(
            enabled=d.get("enabled", None),
            warehouse_type=WarehouseType(d["warehouse_type"])
            if "warehouse_type" in d
            else None,
        )


@dataclass
class Widget:

    # The unique ID for this widget.
    id: int

    options: "WidgetOptions"
    # The visualization description API changes frequently and is unsupported. You can duplicate a visualization by
    # copying description objects received _from the API_ and then using them to create a new one with a POST request to
    # the same endpoint. Databricks does not recommend constructing ad-hoc visualizations entirely in JSON.
    visualization: "Visualization"
    # Unused field.
    width: int

    def as_dict(self) -> dict:
        body = {}
        if self.id:
            body["id"] = self.id
        if self.options:
            body["options"] = self.options.as_dict()
        if self.visualization:
            body["visualization"] = self.visualization.as_dict()
        if self.width:
            body["width"] = self.width

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "Widget":
        return cls(
            id=d.get("id", None),
            options=WidgetOptions.from_dict(d["options"]) if "options" in d else None,
            visualization=Visualization.from_dict(d["visualization"])
            if "visualization" in d
            else None,
            width=d.get("width", None),
        )


@dataclass
class WidgetOptions:

    # Timestamp when this object was created
    created_at: str
    # The dashboard ID to which this widget belongs. Each widget can belong to one dashboard.
    dashboard_id: str
    # Whether this widget is hidden on the dashboard.
    isHidden: bool
    # How parameters used by the visualization in this widget relate to other widgets on the dashboard. Databricks does
    # not recommend modifying this definition in JSON.
    parameterMappings: Any
    # Coordinates of this widget on a dashboard. This portion of the API changes frequently and is unsupported.
    position: Any
    # If this is a textbox widget, the application displays this text. This field is ignored if the widget contains a
    # visualization in the `visualization` field.
    text: str
    # Timestamp of the last time this object was updated.
    updated_at: str

    def as_dict(self) -> dict:
        body = {}
        if self.created_at:
            body["created_at"] = self.created_at
        if self.dashboard_id:
            body["dashboard_id"] = self.dashboard_id
        if self.isHidden:
            body["isHidden"] = self.isHidden
        if self.parameterMappings:
            body["parameterMappings"] = self.parameterMappings
        if self.position:
            body["position"] = self.position
        if self.text:
            body["text"] = self.text
        if self.updated_at:
            body["updated_at"] = self.updated_at

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "WidgetOptions":
        return cls(
            created_at=d.get("created_at", None),
            dashboard_id=d.get("dashboard_id", None),
            isHidden=d.get("isHidden", None),
            parameterMappings=d.get("parameterMappings", None),
            position=d.get("position", None),
            text=d.get("text", None),
            updated_at=d.get("updated_at", None),
        )


class AlertsAPI:
    def __init__(self, api_client):
        self._api = api_client

    def create(
        self,
        name: str,
        options: AlertOptions,
        query_id: str,
        alert_id: str,
        *,
        rearm: int = None,
        **kwargs,
    ) -> Alert:
        """Create an alert.

        Creates an alert. An alert is a Databricks SQL object that periodically
        runs a query, evaluates a condition of its result, and notifies users or
        alert destinations if the condition was met."""
        request = kwargs.get("request", None)
        if not request:  # request is not given through keyed args
            request = EditAlert(
                alert_id=alert_id,
                name=name,
                options=options,
                query_id=query_id,
                rearm=rearm,
            )
        body = request.as_dict()

        json = self._api.do("POST", "/api/2.0/preview/sql/alerts", body=body)
        return Alert.from_dict(json)

    def create_schedule(
        self, cron: str, alert_id: str, *, data_source_id: str = None, **kwargs
    ) -> RefreshSchedule:
        """Create a refresh schedule.

        Creates a new refresh schedule for an alert.

        **Note:** The structure of refresh schedules is subject to change."""
        request = kwargs.get("request", None)
        if not request:  # request is not given through keyed args
            request = CreateRefreshSchedule(
                alert_id=alert_id, cron=cron, data_source_id=data_source_id
            )
        body = request.as_dict()

        json = self._api.do(
            "POST",
            f"/api/2.0/preview/sql/alerts/{request.alert_id}/refresh-schedules",
            body=body,
        )
        return RefreshSchedule.from_dict(json)

    def delete(self, alert_id: str, **kwargs):
        """Delete an alert.

        Deletes an alert. Deleted alerts are no longer accessible and cannot be
        restored. **Note:** Unlike queries and dashboards, alerts cannot be
        moved to the trash."""
        request = kwargs.get("request", None)
        if not request:  # request is not given through keyed args
            request = DeleteAlertRequest(alert_id=alert_id)

        self._api.do("DELETE", f"/api/2.0/preview/sql/alerts/{request.alert_id}")

    def delete_schedule(self, alert_id: str, schedule_id: str, **kwargs):
        """Delete a refresh schedule.

        Deletes an alert's refresh schedule. The refresh schedule specifies when
        to refresh and evaluate the associated query result."""
        request = kwargs.get("request", None)
        if not request:  # request is not given through keyed args
            request = DeleteScheduleRequest(alert_id=alert_id, schedule_id=schedule_id)

        self._api.do(
            "DELETE",
            f"/api/2.0/preview/sql/alerts/{request.alert_id}/refresh-schedules/{request.schedule_id}",
        )

    def get(self, alert_id: str, **kwargs) -> Alert:
        """Get an alert.

        Gets an alert."""
        request = kwargs.get("request", None)
        if not request:  # request is not given through keyed args
            request = GetAlertRequest(alert_id=alert_id)

        json = self._api.do("GET", f"/api/2.0/preview/sql/alerts/{request.alert_id}")
        return Alert.from_dict(json)

    def get_subscriptions(self, alert_id: str, **kwargs) -> SubscriptionList:
        """Get an alert's subscriptions.

        Get the subscriptions for an alert. An alert subscription represents
        exactly one recipient being notified whenever the alert is triggered.
        The alert recipient is specified by either the `user` field or the
        `destination` field. The `user` field is ignored if `destination` is
        non-`null`."""
        request = kwargs.get("request", None)
        if not request:  # request is not given through keyed args
            request = GetSubscriptionsRequest(alert_id=alert_id)

        json = self._api.do(
            "GET", f"/api/2.0/preview/sql/alerts/{request.alert_id}/subscriptions"
        )
        return SubscriptionList.from_dict(json)

    def list(self) -> AlertList:
        """Get alerts.

        Gets a list of alerts."""

        json = self._api.do("GET", "/api/2.0/preview/sql/alerts")
        return AlertList.from_dict(json)

    def list_schedules(self, alert_id: str, **kwargs) -> RefreshScheduleList:
        """Get refresh schedules.

        Gets the refresh schedules for the specified alert. Alerts can have
        refresh schedules that specify when to refresh and evaluate the
        associated query result.

        **Note:** Although refresh schedules are returned in a list, only one
        refresh schedule per alert is currently supported. The structure of
        refresh schedules is subject to change."""
        request = kwargs.get("request", None)
        if not request:  # request is not given through keyed args
            request = ListSchedulesRequest(alert_id=alert_id)

        json = self._api.do(
            "GET", f"/api/2.0/preview/sql/alerts/{request.alert_id}/refresh-schedules"
        )
        return RefreshScheduleList.from_dict(json)

    def subscribe(
        self,
        alert_id: str,
        alert_id: str,
        *,
        destination_id: str = None,
        user_id: int = None,
        **kwargs,
    ) -> Subscription:
        """Subscribe to an alert."""
        request = kwargs.get("request", None)
        if not request:  # request is not given through keyed args
            request = CreateSubscription(
                alert_id=alert_id, destination_id=destination_id, user_id=user_id
            )
        body = request.as_dict()

        json = self._api.do(
            "POST",
            f"/api/2.0/preview/sql/alerts/{request.alert_id}/subscriptions",
            body=body,
        )
        return Subscription.from_dict(json)

    def unsubscribe(self, alert_id: str, subscription_id: str, **kwargs):
        """Unsubscribe to an alert.

        Unsubscribes a user or a destination to an alert."""
        request = kwargs.get("request", None)
        if not request:  # request is not given through keyed args
            request = UnsubscribeRequest(
                alert_id=alert_id, subscription_id=subscription_id
            )

        self._api.do(
            "DELETE",
            f"/api/2.0/preview/sql/alerts/{request.alert_id}/subscriptions/{request.subscription_id}",
        )

    def update(
        self,
        name: str,
        options: AlertOptions,
        query_id: str,
        alert_id: str,
        *,
        rearm: int = None,
        **kwargs,
    ):
        """Update an alert.

        Updates an alert."""
        request = kwargs.get("request", None)
        if not request:  # request is not given through keyed args
            request = EditAlert(
                alert_id=alert_id,
                name=name,
                options=options,
                query_id=query_id,
                rearm=rearm,
            )
        body = request.as_dict()

        self._api.do(
            "PUT", f"/api/2.0/preview/sql/alerts/{request.alert_id}", body=body
        )


class DashboardsAPI:
    def __init__(self, api_client):
        self._api = api_client

    def create(
        self,
        *,
        dashboard_filters_enabled: bool = None,
        is_draft: bool = None,
        is_trashed: bool = None,
        name: str = None,
        tags: List[str] = None,
        widgets: List[Widget] = None,
        **kwargs,
    ) -> Dashboard:
        """Create a dashboard object."""
        request = kwargs.get("request", None)
        if not request:  # request is not given through keyed args
            request = CreateDashboardRequest(
                dashboard_filters_enabled=dashboard_filters_enabled,
                is_draft=is_draft,
                is_trashed=is_trashed,
                name=name,
                tags=tags,
                widgets=widgets,
            )
        body = request.as_dict()

        json = self._api.do("POST", "/api/2.0/preview/sql/dashboards", body=body)
        return Dashboard.from_dict(json)

    def delete(self, dashboard_id: str, **kwargs):
        """Remove a dashboard.

        Moves a dashboard to the trash. Trashed dashboards do not appear in list
        views or searches, and cannot be shared."""
        request = kwargs.get("request", None)
        if not request:  # request is not given through keyed args
            request = DeleteDashboardRequest(dashboard_id=dashboard_id)

        self._api.do(
            "DELETE", f"/api/2.0/preview/sql/dashboards/{request.dashboard_id}"
        )

    def get(self, dashboard_id: str, **kwargs) -> Dashboard:
        """Retrieve a definition.

        Returns a JSON representation of a dashboard object, including its
        visualization and query objects."""
        request = kwargs.get("request", None)
        if not request:  # request is not given through keyed args
            request = GetDashboardRequest(dashboard_id=dashboard_id)

        json = self._api.do(
            "GET", f"/api/2.0/preview/sql/dashboards/{request.dashboard_id}"
        )
        return Dashboard.from_dict(json)

    def list(
        self,
        *,
        order: ListOrder = None,
        page: int = None,
        page_size: int = None,
        q: str = None,
        **kwargs,
    ) -> ListResponse:
        """Get dashboard objects.

        Fetch a paginated list of dashboard objects."""
        request = kwargs.get("request", None)
        if not request:  # request is not given through keyed args
            request = ListDashboardsRequest(
                order=order, page=page, page_size=page_size, q=q
            )

        query = {}
        if order:
            query["order"] = request.order.value
        if page:
            query["page"] = request.page
        if page_size:
            query["page_size"] = request.page_size
        if q:
            query["q"] = request.q

        json = self._api.do("GET", "/api/2.0/preview/sql/dashboards", query=query)
        return ListResponse.from_dict(json)

    def restore(self, dashboard_id: str, **kwargs):
        """Restore a dashboard.

        A restored dashboard appears in list views and searches and can be
        shared."""
        request = kwargs.get("request", None)
        if not request:  # request is not given through keyed args
            request = RestoreDashboardRequest(dashboard_id=dashboard_id)

        self._api.do(
            "POST", f"/api/2.0/preview/sql/dashboards/trash/{request.dashboard_id}"
        )


class DataSourcesAPI:
    def __init__(self, api_client):
        self._api = api_client

    def list(self) -> DataSourceList:
        """Get a list of SQL warehouses.

        Retrieves a full list of SQL warehouses available in this workspace. All
        fields that appear in this API response are enumerated for clarity.
        However, you need only a SQL warehouse's `id` to create new queries
        against it."""

        json = self._api.do("GET", "/api/2.0/preview/sql/data_sources")
        return DataSourceList.from_dict(json)


class DbsqlPermissionsAPI:
    def __init__(self, api_client):
        self._api = api_client

    def get(
        self, object_type: ObjectTypePlural, object_id: str, **kwargs
    ) -> GetResponse:
        """Get object ACL.

        Gets a JSON representation of the access control list (ACL) for a
        specified object."""
        request = kwargs.get("request", None)
        if not request:  # request is not given through keyed args
            request = GetDbsqlPermissionRequest(
                object_id=object_id, object_type=object_type
            )

        json = self._api.do(
            "GET",
            f"/api/2.0/preview/sql/permissions/{request.objectType}/{request.objectId}",
        )
        return GetResponse.from_dict(json)

    def set(
        self,
        object_type: ObjectTypePlural,
        object_id: str,
        *,
        access_control_list: List[AccessControl] = None,
        **kwargs,
    ) -> SetResponse:
        """Set object ACL.

        Sets the access control list (ACL) for a specified object. This
        operation will complete rewrite the ACL."""
        request = kwargs.get("request", None)
        if not request:  # request is not given through keyed args
            request = SetRequest(
                access_control_list=access_control_list,
                object_id=object_id,
                object_type=object_type,
            )
        body = request.as_dict()

        json = self._api.do(
            "POST",
            f"/api/2.0/preview/sql/permissions/{request.objectType}/{request.objectId}",
            body=body,
        )
        return SetResponse.from_dict(json)

    def transfer_ownership(
        self,
        object_type: OwnableObjectType,
        object_id: TransferOwnershipObjectId,
        *,
        new_owner: str = None,
        **kwargs,
    ) -> Success:
        """Transfer object ownership.

        Transfers ownership of a dashboard, query, or alert to an active user.
        Requires an admin API key."""
        request = kwargs.get("request", None)
        if not request:  # request is not given through keyed args
            request = TransferOwnershipRequest(
                new_owner=new_owner, object_id=object_id, object_type=object_type
            )
        body = request.as_dict()

        json = self._api.do(
            "POST",
            f"/api/2.0/preview/sql/permissions/{request.objectType}/{request.objectId}/transfer",
            body=body,
        )
        return Success.from_dict(json)


class QueriesAPI:
    def __init__(self, api_client):
        self._api = api_client

    def create(
        self,
        query_id: str,
        *,
        data_source_id: str = None,
        description: str = None,
        name: str = None,
        options: Any = None,
        query: str = None,
        schedule: QueryInterval = None,
        **kwargs,
    ) -> Query:
        """Create a new query definition.

        Creates a new query definition. Queries created with this endpoint
        belong to the authenticated user making the request.

        The `data_source_id` field specifies the ID of the SQL warehouse to run
        this query against. You can use the Data Sources API to see a complete
        list of available SQL warehouses. Or you can copy the `data_source_id`
        from an existing query.

        **Note**: You cannot add a visualization until you create the query."""
        request = kwargs.get("request", None)
        if not request:  # request is not given through keyed args
            request = QueryPostContent(
                data_source_id=data_source_id,
                description=description,
                name=name,
                options=options,
                query=query,
                query_id=query_id,
                schedule=schedule,
            )
        body = request.as_dict()

        json = self._api.do("POST", "/api/2.0/preview/sql/queries", body=body)
        return Query.from_dict(json)

    def delete(self, query_id: str, **kwargs):
        """Delete a query.

        Moves a query to the trash. Trashed queries immediately disappear from
        searches and list views, and they cannot be used for alerts. The trash
        is deleted after 30 days."""
        request = kwargs.get("request", None)
        if not request:  # request is not given through keyed args
            request = DeleteQueryRequest(query_id=query_id)

        self._api.do("DELETE", f"/api/2.0/preview/sql/queries/{request.query_id}")

    def get(self, query_id: str, **kwargs) -> Query:
        """Get a query definition.

        Retrieve a query object definition along with contextual permissions
        information about the currently authenticated user."""
        request = kwargs.get("request", None)
        if not request:  # request is not given through keyed args
            request = GetQueryRequest(query_id=query_id)

        json = self._api.do("GET", f"/api/2.0/preview/sql/queries/{request.query_id}")
        return Query.from_dict(json)

    def list(
        self,
        *,
        order: str = None,
        page: int = None,
        page_size: int = None,
        q: str = None,
        **kwargs,
    ) -> QueryList:
        """Get a list of queries.

        Gets a list of queries. Optionally, this list can be filtered by a
        search term."""
        request = kwargs.get("request", None)
        if not request:  # request is not given through keyed args
            request = ListQueriesRequest(
                order=order, page=page, page_size=page_size, q=q
            )

        query = {}
        if order:
            query["order"] = request.order
        if page:
            query["page"] = request.page
        if page_size:
            query["page_size"] = request.page_size
        if q:
            query["q"] = request.q

        json = self._api.do("GET", "/api/2.0/preview/sql/queries", query=query)
        return QueryList.from_dict(json)

    def restore(self, query_id: str, **kwargs):
        """Restore a query.

        Restore a query that has been moved to the trash. A restored query
        appears in list views and searches. You can use restored queries for
        alerts."""
        request = kwargs.get("request", None)
        if not request:  # request is not given through keyed args
            request = RestoreQueryRequest(query_id=query_id)

        self._api.do("POST", f"/api/2.0/preview/sql/queries/trash/{request.query_id}")

    def update(
        self,
        query_id: str,
        *,
        data_source_id: str = None,
        description: str = None,
        name: str = None,
        options: Any = None,
        query: str = None,
        schedule: QueryInterval = None,
        **kwargs,
    ) -> Query:
        """Change a query definition.

        Modify this query definition.

        **Note**: You cannot undo this operation."""
        request = kwargs.get("request", None)
        if not request:  # request is not given through keyed args
            request = QueryPostContent(
                data_source_id=data_source_id,
                description=description,
                name=name,
                options=options,
                query=query,
                query_id=query_id,
                schedule=schedule,
            )
        body = request.as_dict()

        json = self._api.do(
            "POST", f"/api/2.0/preview/sql/queries/{request.query_id}", body=body
        )
        return Query.from_dict(json)


class QueryHistoryAPI:
    def __init__(self, api_client):
        self._api = api_client

    def list(
        self,
        *,
        filter_by: QueryFilter = None,
        include_metrics: bool = None,
        max_results: int = None,
        page_token: str = None,
        **kwargs,
    ) -> ListQueriesResponse:
        """List Queries.

        List the history of queries through SQL warehouses.

        You can filter by user ID, warehouse ID, status, and time range."""
        request = kwargs.get("request", None)
        if not request:  # request is not given through keyed args
            request = ListQueryHistoryRequest(
                filter_by=filter_by,
                include_metrics=include_metrics,
                max_results=max_results,
                page_token=page_token,
            )

        query = {}
        if filter_by:
            query["filter_by"] = request.filter_by.as_dict()
        if include_metrics:
            query["include_metrics"] = request.include_metrics
        if max_results:
            query["max_results"] = request.max_results
        if page_token:
            query["page_token"] = request.page_token

        json = self._api.do("GET", "/api/2.0/sql/history/queries", query=query)
        return ListQueriesResponse.from_dict(json)


class WarehousesAPI:
    def __init__(self, api_client):
        self._api = api_client

    def create(
        self,
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
        **kwargs,
    ) -> CreateWarehouseResponse:
        """Create a warehouse.

        Creates a new SQL warehouse."""
        request = kwargs.get("request", None)
        if not request:  # request is not given through keyed args
            request = CreateWarehouseRequest(
                auto_stop_mins=auto_stop_mins,
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
                warehouse_type=warehouse_type,
            )
        body = request.as_dict()

        json = self._api.do("POST", "/api/2.0/sql/warehouses", body=body)
        return CreateWarehouseResponse.from_dict(json)

    def delete(self, id: str, **kwargs):
        """Delete a warehouse.

        Deletes a SQL warehouse."""
        request = kwargs.get("request", None)
        if not request:  # request is not given through keyed args
            request = DeleteWarehouseRequest(id=id)

        self._api.do("DELETE", f"/api/2.0/sql/warehouses/{request.id}")

    def edit(
        self,
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
        **kwargs,
    ):
        """Update a warehouse.

        Updates the configuration for a SQL warehouse."""
        request = kwargs.get("request", None)
        if not request:  # request is not given through keyed args
            request = EditWarehouseRequest(
                auto_stop_mins=auto_stop_mins,
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
                warehouse_type=warehouse_type,
            )
        body = request.as_dict()

        self._api.do("POST", f"/api/2.0/sql/warehouses/{request.id}/edit", body=body)

    def get(self, id: str, **kwargs) -> GetWarehouseResponse:
        """Get warehouse info.

        Gets the information for a single SQL warehouse."""
        request = kwargs.get("request", None)
        if not request:  # request is not given through keyed args
            request = GetWarehouseRequest(id=id)

        json = self._api.do("GET", f"/api/2.0/sql/warehouses/{request.id}")
        return GetWarehouseResponse.from_dict(json)

    def get_workspace_warehouse_config(self) -> GetWorkspaceWarehouseConfigResponse:
        """Get the workspace configuration.

        Gets the workspace level configuration that is shared by all SQL
        warehouses in a workspace."""

        json = self._api.do("GET", "/api/2.0/sql/config/warehouses")
        return GetWorkspaceWarehouseConfigResponse.from_dict(json)

    def list(self, *, run_as_user_id: int = None, **kwargs) -> ListWarehousesResponse:
        """List warehouses.

        Lists all SQL warehouses that a user has manager permissions on."""
        request = kwargs.get("request", None)
        if not request:  # request is not given through keyed args
            request = ListWarehousesRequest(run_as_user_id=run_as_user_id)

        query = {}
        if run_as_user_id:
            query["run_as_user_id"] = request.run_as_user_id

        json = self._api.do("GET", "/api/2.0/sql/warehouses", query=query)
        return ListWarehousesResponse.from_dict(json)

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
        **kwargs,
    ):
        """Set the workspace configuration.

        Sets the workspace level configuration that is shared by all SQL
        warehouses in a workspace."""
        request = kwargs.get("request", None)
        if not request:  # request is not given through keyed args
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
                sql_configuration_parameters=sql_configuration_parameters,
            )
        body = request.as_dict()

        self._api.do("PUT", "/api/2.0/sql/config/warehouses", body=body)

    def start(self, id: str, **kwargs):
        """Start a warehouse.

        Starts a SQL warehouse."""
        request = kwargs.get("request", None)
        if not request:  # request is not given through keyed args
            request = StartRequest(id=id)

        self._api.do("POST", f"/api/2.0/sql/warehouses/{request.id}/start")

    def stop(self, id: str, **kwargs):
        """Stop a warehouse.

        Stops a SQL warehouse."""
        request = kwargs.get("request", None)
        if not request:  # request is not given through keyed args
            request = StopRequest(id=id)

        self._api.do("POST", f"/api/2.0/sql/warehouses/{request.id}/stop")
