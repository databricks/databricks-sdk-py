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

    def as_request(self) -> (dict, dict):
        accessControl_query, accessControl_body = {}, {}
        if self.group_name:
            accessControl_body["group_name"] = self.group_name
        if self.permission_level:
            accessControl_body["permission_level"] = self.permission_level.value
        if self.user_name:
            accessControl_body["user_name"] = self.user_name

        return accessControl_query, accessControl_body

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
    # Number of seconds after being triggered before the alert rearms itself and
    # can be triggered again. If `null`, alert will never be triggered again.
    rearm: int
    # State of the alert. Possible values are: `unknown` (yet to be evaluated),
    # `triggered` (evaluated and fulfilled trigger conditions), or `ok`
    # (evaluated and did not fulfill trigger conditions).
    state: "AlertState"
    # Timestamp when the alert was last updated.
    updated_at: str

    user: "User"

    def as_request(self) -> (dict, dict):
        alert_query, alert_body = {}, {}
        if self.created_at:
            alert_body["created_at"] = self.created_at
        if self.id:
            alert_body["id"] = self.id
        if self.last_triggered_at:
            alert_body["last_triggered_at"] = self.last_triggered_at
        if self.name:
            alert_body["name"] = self.name
        if self.options:
            alert_body["options"] = self.options.as_request()[1]
        if self.query:
            alert_body["query"] = self.query.as_request()[1]
        if self.rearm:
            alert_body["rearm"] = self.rearm
        if self.state:
            alert_body["state"] = self.state.value
        if self.updated_at:
            alert_body["updated_at"] = self.updated_at
        if self.user:
            alert_body["user"] = self.user.as_request()[1]

        return alert_query, alert_body

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
    # Custom body of alert notification, if it exists. See [here] for custom
    # templating instructions.
    #
    # [here]: https://docs.databricks.com/sql/user/alerts/index.html
    custom_body: str
    # Custom subject of alert notification, if it exists. This includes email
    # subject, Slack notification header, etc. See [here] for custom templating
    # instructions.
    #
    # [here]: https://docs.databricks.com/sql/user/alerts/index.html
    custom_subject: str
    # Whether or not the alert is muted. If an alert is muted, it will not
    # notify users and alert destinations when triggered.
    muted: bool
    # Operator used to compare in alert evaluation: `>`, `>=`, `<`, `<=`, `==`,
    # `!=`
    op: str
    # Number of failures encountered during alert refresh. This counter is used
    # for sending aggregated alert failure email notifications.
    schedule_failures: int
    # Value used to compare in alert evaluation.
    value: str

    def as_request(self) -> (dict, dict):
        alertOptions_query, alertOptions_body = {}, {}
        if self.column:
            alertOptions_body["column"] = self.column
        if self.custom_body:
            alertOptions_body["custom_body"] = self.custom_body
        if self.custom_subject:
            alertOptions_body["custom_subject"] = self.custom_subject
        if self.muted:
            alertOptions_body["muted"] = self.muted
        if self.op:
            alertOptions_body["op"] = self.op
        if self.schedule_failures:
            alertOptions_body["schedule_failures"] = self.schedule_failures
        if self.value:
            alertOptions_body["value"] = self.value

        return alertOptions_query, alertOptions_body

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
    """State of the alert. Possible values are: `unknown` (yet to be evaluated),
    `triggered` (evaluated and fulfilled trigger conditions), or `ok` (evaluated
    and did not fulfill trigger conditions)."""

    ok = "ok"
    triggered = "triggered"
    unknown = "unknown"


@dataclass
class Channel:

    dbsql_version: str

    name: "ChannelName"

    def as_request(self) -> (dict, dict):
        channel_query, channel_body = {}, {}
        if self.dbsql_version:
            channel_body["dbsql_version"] = self.dbsql_version
        if self.name:
            channel_body["name"] = self.name.value

        return channel_query, channel_body

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

    def as_request(self) -> (dict, dict):
        channelInfo_query, channelInfo_body = {}, {}
        if self.dbsql_version:
            channelInfo_body["dbsql_version"] = self.dbsql_version
        if self.name:
            channelInfo_body["name"] = self.name.value

        return channelInfo_query, channelInfo_body

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

    # In the web application, query filters that share a name are coupled to a
    # single selection box if this value is true.
    dashboard_filters_enabled: bool
    # Draft dashboards only appear in list views for their owners.
    is_draft: bool
    # Indicates whether the dashboard is trashed. Trashed dashboards don't
    # appear in list views.
    is_trashed: bool
    # The title of this dashboard that appears in list views and at the top of
    # the dashboard page.
    name: str

    tags: "List[str]"
    # An array of widget objects. A complete description of widget objects can
    # be found in the response to [Retrieve A Dashboard
    # Definition](#operation/sql-analytics-fetch-dashboard). Databricks does not
    # recommend creating new widgets via this API.
    widgets: "List[Widget]"

    def as_request(self) -> (dict, dict):
        createDashboardRequest_query, createDashboardRequest_body = {}, {}
        if self.dashboard_filters_enabled:
            createDashboardRequest_body[
                "dashboard_filters_enabled"
            ] = self.dashboard_filters_enabled
        if self.is_draft:
            createDashboardRequest_body["is_draft"] = self.is_draft
        if self.is_trashed:
            createDashboardRequest_body["is_trashed"] = self.is_trashed
        if self.name:
            createDashboardRequest_body["name"] = self.name
        if self.tags:
            createDashboardRequest_body["tags"] = [v for v in self.tags]
        if self.widgets:
            createDashboardRequest_body["widgets"] = [
                v.as_request()[1] for v in self.widgets
            ]

        return createDashboardRequest_query, createDashboardRequest_body

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
    # ID of the SQL warehouse to refresh with. If `null`, query's SQL warehouse
    # will be used to refresh.
    data_source_id: str

    def as_request(self) -> (dict, dict):
        createRefreshSchedule_query, createRefreshSchedule_body = {}, {}
        if self.alert_id:
            createRefreshSchedule_body["alert_id"] = self.alert_id
        if self.cron:
            createRefreshSchedule_body["cron"] = self.cron
        if self.data_source_id:
            createRefreshSchedule_body["data_source_id"] = self.data_source_id

        return createRefreshSchedule_query, createRefreshSchedule_body

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
    # ID of the alert subscriber (if subscribing an alert destination). Alert
    # destinations can be configured by admins through the UI. See
    # [here](/sql/admin/alert-destinations.html).
    destination_id: str
    # ID of the alert subscriber (if subscribing a user).
    user_id: int

    def as_request(self) -> (dict, dict):
        createSubscription_query, createSubscription_body = {}, {}
        if self.alert_id:
            createSubscription_body["alert_id"] = self.alert_id
        if self.destination_id:
            createSubscription_body["destination_id"] = self.destination_id
        if self.user_id:
            createSubscription_body["user_id"] = self.user_id

        return createSubscription_query, createSubscription_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "CreateSubscription":
        return cls(
            alert_id=d.get("alert_id", None),
            destination_id=d.get("destination_id", None),
            user_id=d.get("user_id", None),
        )


@dataclass
class CreateWarehouseRequest:

    # The amount of time in minutes that a SQL Endpoint must be idle (i.e., no
    # RUNNING queries) before it is automatically stopped.
    #
    # Supported values: - Must be == 0 or >= 10 mins - 0 indicates no autostop.
    #
    # Defaults to 120 mins
    auto_stop_mins: int
    # Channel Details
    channel: "Channel"
    # Size of the clusters allocated for this endpoint. Increasing the size of a
    # spark cluster allows you to run larger queries on it. If you want to
    # increase the number of concurrent queries, please tune max_num_clusters.
    #
    # Supported values: - 2X-Small - X-Small - Small - Medium - Large - X-Large
    # - 2X-Large - 3X-Large - 4X-Large
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
    # Maximum number of clusters that the autoscaler will create to handle
    # concurrent queries.
    #
    # Supported values: - Must be >= min_num_clusters - Must be <= 30.
    #
    # Defaults to min_clusters if unset.
    max_num_clusters: int
    # Minimum number of available clusters that will be maintained for this SQL
    # Endpoint. Increasing this will ensure that a larger number of clusters are
    # always running and therefore may reduce the cold start time for new
    # queries. This is similar to reserved vs. revocable cores in a resource
    # manager.
    #
    # Supported values: - Must be > 0 - Must be <= min(max_num_clusters, 30)
    #
    # Defaults to 1
    min_num_clusters: int
    # Logical name for the cluster.
    #
    # Supported values: - Must be unique within an org. - Must be less than 100
    # characters.
    name: str
    # Configurations whether the warehouse should use spot instances.
    spot_instance_policy: "SpotInstancePolicy"
    # A set of key-value pairs that will be tagged on all resources (e.g., AWS
    # instances and EBS volumes) associated with this SQL Endpoints.
    #
    # Supported values: - Number of tags < 45.
    tags: "EndpointTags"

    warehouse_type: "WarehouseType"

    def as_request(self) -> (dict, dict):
        createWarehouseRequest_query, createWarehouseRequest_body = {}, {}
        if self.auto_stop_mins:
            createWarehouseRequest_body["auto_stop_mins"] = self.auto_stop_mins
        if self.channel:
            createWarehouseRequest_body["channel"] = self.channel.as_request()[1]
        if self.cluster_size:
            createWarehouseRequest_body["cluster_size"] = self.cluster_size
        if self.creator_name:
            createWarehouseRequest_body["creator_name"] = self.creator_name
        if self.enable_photon:
            createWarehouseRequest_body["enable_photon"] = self.enable_photon
        if self.enable_serverless_compute:
            createWarehouseRequest_body[
                "enable_serverless_compute"
            ] = self.enable_serverless_compute
        if self.instance_profile_arn:
            createWarehouseRequest_body[
                "instance_profile_arn"
            ] = self.instance_profile_arn
        if self.max_num_clusters:
            createWarehouseRequest_body["max_num_clusters"] = self.max_num_clusters
        if self.min_num_clusters:
            createWarehouseRequest_body["min_num_clusters"] = self.min_num_clusters
        if self.name:
            createWarehouseRequest_body["name"] = self.name
        if self.spot_instance_policy:
            createWarehouseRequest_body[
                "spot_instance_policy"
            ] = self.spot_instance_policy.value
        if self.tags:
            createWarehouseRequest_body["tags"] = self.tags.as_request()[1]
        if self.warehouse_type:
            createWarehouseRequest_body["warehouse_type"] = self.warehouse_type.value

        return createWarehouseRequest_query, createWarehouseRequest_body

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

    def as_request(self) -> (dict, dict):
        createWarehouseResponse_query, createWarehouseResponse_body = {}, {}
        if self.id:
            createWarehouseResponse_body["id"] = self.id

        return createWarehouseResponse_query, createWarehouseResponse_body

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
    # In the web application, query filters that share a name are coupled to a
    # single selection box if this value is `true`.
    dashboard_filters_enabled: bool
    # The ID for this dashboard.
    id: str
    # Indicates whether a dashboard is trashed. Trashed dashboards won't appear
    # in list views. If this boolean is `true`, the `options` property for this
    # dashboard includes a `moved_to_trash_at` timestamp. Items in trash are
    # permanently deleted after 30 days.
    is_archived: bool
    # Whether a dashboard is a draft. Draft dashboards only appear in list views
    # for their owners.
    is_draft: bool
    # Indicates whether this query object appears in the current user's
    # favorites list. This flag determines whether the star icon for favorites
    # is selected.
    is_favorite: bool
    # The title of the dashboard that appears in list views and at the top of
    # the dashboard page.
    name: str

    options: "DashboardOptions"
    # This describes an enum
    permission_tier: "PermissionLevel"
    # URL slug. Usually mirrors the query name with dashes (`-`) instead of
    # spaces. Appears in the URL for this query.
    slug: str

    tags: "List[str]"
    # Timestamp when this dashboard was last updated.
    updated_at: str

    user: "User"
    # The ID of the user that created and owns this dashboard.
    user_id: int

    widgets: "List[Widget]"

    def as_request(self) -> (dict, dict):
        dashboard_query, dashboard_body = {}, {}
        if self.can_edit:
            dashboard_body["can_edit"] = self.can_edit
        if self.created_at:
            dashboard_body["created_at"] = self.created_at
        if self.dashboard_filters_enabled:
            dashboard_body["dashboard_filters_enabled"] = self.dashboard_filters_enabled
        if self.id:
            dashboard_body["id"] = self.id
        if self.is_archived:
            dashboard_body["is_archived"] = self.is_archived
        if self.is_draft:
            dashboard_body["is_draft"] = self.is_draft
        if self.is_favorite:
            dashboard_body["is_favorite"] = self.is_favorite
        if self.name:
            dashboard_body["name"] = self.name
        if self.options:
            dashboard_body["options"] = self.options.as_request()[1]
        if self.permission_tier:
            dashboard_body["permission_tier"] = self.permission_tier.value
        if self.slug:
            dashboard_body["slug"] = self.slug
        if self.tags:
            dashboard_body["tags"] = [v for v in self.tags]
        if self.updated_at:
            dashboard_body["updated_at"] = self.updated_at
        if self.user:
            dashboard_body["user"] = self.user.as_request()[1]
        if self.user_id:
            dashboard_body["user_id"] = self.user_id
        if self.widgets:
            dashboard_body["widgets"] = [v.as_request()[1] for v in self.widgets]

        return dashboard_query, dashboard_body

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

    # The timestamp when this dashboard was moved to trash. Only present when
    # the `is_archived` property is `true`. Trashed items are deleted after
    # thirty days.
    moved_to_trash_at: str

    def as_request(self) -> (dict, dict):
        dashboardOptions_query, dashboardOptions_body = {}, {}
        if self.moved_to_trash_at:
            dashboardOptions_body["moved_to_trash_at"] = self.moved_to_trash_at

        return dashboardOptions_query, dashboardOptions_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "DashboardOptions":
        return cls(
            moved_to_trash_at=d.get("moved_to_trash_at", None),
        )


@dataclass
class DataSource:
    """A JSON object representing a DBSQL data source / SQL warehouse."""

    # The unique identifier for this data source / SQL warehouse. Can be used
    # when creating / modifying queries and dashboards.
    id: str
    # The string name of this data source / SQL warehouse as it appears in the
    # Databricks SQL web application.
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

    def as_request(self) -> (dict, dict):
        dataSource_query, dataSource_body = {}, {}
        if self.id:
            dataSource_body["id"] = self.id
        if self.name:
            dataSource_body["name"] = self.name
        if self.pause_reason:
            dataSource_body["pause_reason"] = self.pause_reason
        if self.paused:
            dataSource_body["paused"] = self.paused
        if self.supports_auto_limit:
            dataSource_body["supports_auto_limit"] = self.supports_auto_limit
        if self.syntax:
            dataSource_body["syntax"] = self.syntax
        if self.type:
            dataSource_body["type"] = self.type
        if self.view_only:
            dataSource_body["view_only"] = self.view_only
        if self.warehouse_id:
            dataSource_body["warehouse_id"] = self.warehouse_id

        return dataSource_query, dataSource_body

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

    def as_request(self) -> (dict, dict):
        deleteAlertRequest_query, deleteAlertRequest_body = {}, {}
        if self.alert_id:
            deleteAlertRequest_body["alert_id"] = self.alert_id

        return deleteAlertRequest_query, deleteAlertRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "DeleteAlertRequest":
        return cls(
            alert_id=d.get("alert_id", None),
        )


@dataclass
class DeleteDashboardRequest:
    """Remove a dashboard"""

    dashboard_id: str  # path

    def as_request(self) -> (dict, dict):
        deleteDashboardRequest_query, deleteDashboardRequest_body = {}, {}
        if self.dashboard_id:
            deleteDashboardRequest_body["dashboard_id"] = self.dashboard_id

        return deleteDashboardRequest_query, deleteDashboardRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "DeleteDashboardRequest":
        return cls(
            dashboard_id=d.get("dashboard_id", None),
        )


@dataclass
class DeleteQueryRequest:
    """Delete a query"""

    query_id: str  # path

    def as_request(self) -> (dict, dict):
        deleteQueryRequest_query, deleteQueryRequest_body = {}, {}
        if self.query_id:
            deleteQueryRequest_body["query_id"] = self.query_id

        return deleteQueryRequest_query, deleteQueryRequest_body

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

    def as_request(self) -> (dict, dict):
        deleteScheduleRequest_query, deleteScheduleRequest_body = {}, {}
        if self.alert_id:
            deleteScheduleRequest_body["alert_id"] = self.alert_id
        if self.schedule_id:
            deleteScheduleRequest_body["schedule_id"] = self.schedule_id

        return deleteScheduleRequest_query, deleteScheduleRequest_body

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

    def as_request(self) -> (dict, dict):
        deleteWarehouseRequest_query, deleteWarehouseRequest_body = {}, {}
        if self.id:
            deleteWarehouseRequest_body["id"] = self.id

        return deleteWarehouseRequest_query, deleteWarehouseRequest_body

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

    def as_request(self) -> (dict, dict):
        destination_query, destination_body = {}, {}
        if self.id:
            destination_body["id"] = self.id
        if self.name:
            destination_body["name"] = self.name
        if self.type:
            destination_body["type"] = self.type.value

        return destination_query, destination_body

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
    # Number of seconds after being triggered before the alert rearms itself and
    # can be triggered again. If `null`, alert will never be triggered again.
    rearm: int

    def as_request(self) -> (dict, dict):
        editAlert_query, editAlert_body = {}, {}
        if self.alert_id:
            editAlert_body["alert_id"] = self.alert_id
        if self.name:
            editAlert_body["name"] = self.name
        if self.options:
            editAlert_body["options"] = self.options.as_request()[1]
        if self.query_id:
            editAlert_body["query_id"] = self.query_id
        if self.rearm:
            editAlert_body["rearm"] = self.rearm

        return editAlert_query, editAlert_body

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

    # The amount of time in minutes that a SQL Endpoint must be idle (i.e., no
    # RUNNING queries) before it is automatically stopped.
    #
    # Supported values: - Must be == 0 or >= 10 mins - 0 indicates no autostop.
    #
    # Defaults to 120 mins
    auto_stop_mins: int
    # Channel Details
    channel: "Channel"
    # Size of the clusters allocated for this endpoint. Increasing the size of a
    # spark cluster allows you to run larger queries on it. If you want to
    # increase the number of concurrent queries, please tune max_num_clusters.
    #
    # Supported values: - 2X-Small - X-Small - Small - Medium - Large - X-Large
    # - 2X-Large - 3X-Large - 4X-Large
    cluster_size: str
    # endpoint creator name
    creator_name: str
    # Configures whether the endpoint should use Databricks Compute (aka Nephos)
    #
    # Deprecated: Use enable_serverless_compute TODO(SC-79930): Remove the field
    # once clients are updated
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
    # Maximum number of clusters that the autoscaler will create to handle
    # concurrent queries.
    #
    # Supported values: - Must be >= min_num_clusters - Must be <= 30.
    #
    # Defaults to min_clusters if unset.
    max_num_clusters: int
    # Minimum number of available clusters that will be maintained for this SQL
    # Endpoint. Increasing this will ensure that a larger number of clusters are
    # always running and therefore may reduce the cold start time for new
    # queries. This is similar to reserved vs. revocable cores in a resource
    # manager.
    #
    # Supported values: - Must be > 0 - Must be <= min(max_num_clusters, 30)
    #
    # Defaults to 1
    min_num_clusters: int
    # Logical name for the cluster.
    #
    # Supported values: - Must be unique within an org. - Must be less than 100
    # characters.
    name: str
    # Configurations whether the warehouse should use spot instances.
    spot_instance_policy: "SpotInstancePolicy"
    # A set of key-value pairs that will be tagged on all resources (e.g., AWS
    # instances and EBS volumes) associated with this SQL Endpoints.
    #
    # Supported values: - Number of tags < 45.
    tags: "EndpointTags"

    warehouse_type: "WarehouseType"

    def as_request(self) -> (dict, dict):
        editWarehouseRequest_query, editWarehouseRequest_body = {}, {}
        if self.auto_stop_mins:
            editWarehouseRequest_body["auto_stop_mins"] = self.auto_stop_mins
        if self.channel:
            editWarehouseRequest_body["channel"] = self.channel.as_request()[1]
        if self.cluster_size:
            editWarehouseRequest_body["cluster_size"] = self.cluster_size
        if self.creator_name:
            editWarehouseRequest_body["creator_name"] = self.creator_name
        if self.enable_databricks_compute:
            editWarehouseRequest_body[
                "enable_databricks_compute"
            ] = self.enable_databricks_compute
        if self.enable_photon:
            editWarehouseRequest_body["enable_photon"] = self.enable_photon
        if self.enable_serverless_compute:
            editWarehouseRequest_body[
                "enable_serverless_compute"
            ] = self.enable_serverless_compute
        if self.id:
            editWarehouseRequest_body["id"] = self.id
        if self.instance_profile_arn:
            editWarehouseRequest_body[
                "instance_profile_arn"
            ] = self.instance_profile_arn
        if self.max_num_clusters:
            editWarehouseRequest_body["max_num_clusters"] = self.max_num_clusters
        if self.min_num_clusters:
            editWarehouseRequest_body["min_num_clusters"] = self.min_num_clusters
        if self.name:
            editWarehouseRequest_body["name"] = self.name
        if self.spot_instance_policy:
            editWarehouseRequest_body[
                "spot_instance_policy"
            ] = self.spot_instance_policy.value
        if self.tags:
            editWarehouseRequest_body["tags"] = self.tags.as_request()[1]
        if self.warehouse_type:
            editWarehouseRequest_body["warehouse_type"] = self.warehouse_type.value

        return editWarehouseRequest_query, editWarehouseRequest_body

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

    def as_request(self) -> (dict, dict):
        endpointConfPair_query, endpointConfPair_body = {}, {}
        if self.key:
            endpointConfPair_body["key"] = self.key
        if self.value:
            endpointConfPair_body["value"] = self.value

        return endpointConfPair_query, endpointConfPair_body

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
    # The reason for failure to bring up clusters for this endpoint. This is
    # available when status is 'FAILED' and sometimes when it is DEGRADED.
    failure_reason: "TerminationReason"
    # Deprecated. split into summary and details for security
    message: str
    # Health status of the endpoint.
    status: "Status"
    # A short summary of the health status in case of degraded/failed endpoints.
    summary: str

    def as_request(self) -> (dict, dict):
        endpointHealth_query, endpointHealth_body = {}, {}
        if self.details:
            endpointHealth_body["details"] = self.details
        if self.failure_reason:
            endpointHealth_body["failure_reason"] = self.failure_reason.as_request()[1]
        if self.message:
            endpointHealth_body["message"] = self.message
        if self.status:
            endpointHealth_body["status"] = self.status.value
        if self.summary:
            endpointHealth_body["summary"] = self.summary

        return endpointHealth_query, endpointHealth_body

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

    # The amount of time in minutes that a SQL Endpoint must be idle (i.e., no
    # RUNNING queries) before it is automatically stopped.
    #
    # Supported values: - Must be == 0 or >= 10 mins - 0 indicates no autostop.
    #
    # Defaults to 120 mins
    auto_stop_mins: int
    # Channel Details
    channel: "Channel"
    # Size of the clusters allocated for this endpoint. Increasing the size of a
    # spark cluster allows you to run larger queries on it. If you want to
    # increase the number of concurrent queries, please tune max_num_clusters.
    #
    # Supported values: - 2X-Small - X-Small - Small - Medium - Large - X-Large
    # - 2X-Large - 3X-Large - 4X-Large
    cluster_size: str
    # endpoint creator name
    creator_name: str
    # Configures whether the endpoint should use Databricks Compute (aka Nephos)
    #
    # Deprecated: Use enable_serverless_compute TODO(SC-79930): Remove the field
    # once clients are updated
    enable_databricks_compute: bool
    # Configures whether the endpoint should use Photon optimized clusters.
    #
    # Defaults to false.
    enable_photon: bool
    # Configures whether the endpoint should use Serverless Compute (aka Nephos)
    #
    # Defaults to value in global endpoint settings
    enable_serverless_compute: bool
    # Optional health status. Assume the endpoint is healthy if this field is
    # not set.
    health: "EndpointHealth"
    # unique identifier for endpoint
    id: str
    # Deprecated. Instance profile used to pass IAM role to the cluster
    instance_profile_arn: str
    # the jdbc connection string for this endpoint
    jdbc_url: str
    # Maximum number of clusters that the autoscaler will create to handle
    # concurrent queries.
    #
    # Supported values: - Must be >= min_num_clusters - Must be <= 30.
    #
    # Defaults to min_clusters if unset.
    max_num_clusters: int
    # Minimum number of available clusters that will be maintained for this SQL
    # Endpoint. Increasing this will ensure that a larger number of clusters are
    # always running and therefore may reduce the cold start time for new
    # queries. This is similar to reserved vs. revocable cores in a resource
    # manager.
    #
    # Supported values: - Must be > 0 - Must be <= min(max_num_clusters, 30)
    #
    # Defaults to 1
    min_num_clusters: int
    # Logical name for the cluster.
    #
    # Supported values: - Must be unique within an org. - Must be less than 100
    # characters.
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
    # A set of key-value pairs that will be tagged on all resources (e.g., AWS
    # instances and EBS volumes) associated with this SQL Endpoints.
    #
    # Supported values: - Number of tags < 45.
    tags: "EndpointTags"

    warehouse_type: "WarehouseType"

    def as_request(self) -> (dict, dict):
        endpointInfo_query, endpointInfo_body = {}, {}
        if self.auto_stop_mins:
            endpointInfo_body["auto_stop_mins"] = self.auto_stop_mins
        if self.channel:
            endpointInfo_body["channel"] = self.channel.as_request()[1]
        if self.cluster_size:
            endpointInfo_body["cluster_size"] = self.cluster_size
        if self.creator_name:
            endpointInfo_body["creator_name"] = self.creator_name
        if self.enable_databricks_compute:
            endpointInfo_body[
                "enable_databricks_compute"
            ] = self.enable_databricks_compute
        if self.enable_photon:
            endpointInfo_body["enable_photon"] = self.enable_photon
        if self.enable_serverless_compute:
            endpointInfo_body[
                "enable_serverless_compute"
            ] = self.enable_serverless_compute
        if self.health:
            endpointInfo_body["health"] = self.health.as_request()[1]
        if self.id:
            endpointInfo_body["id"] = self.id
        if self.instance_profile_arn:
            endpointInfo_body["instance_profile_arn"] = self.instance_profile_arn
        if self.jdbc_url:
            endpointInfo_body["jdbc_url"] = self.jdbc_url
        if self.max_num_clusters:
            endpointInfo_body["max_num_clusters"] = self.max_num_clusters
        if self.min_num_clusters:
            endpointInfo_body["min_num_clusters"] = self.min_num_clusters
        if self.name:
            endpointInfo_body["name"] = self.name
        if self.num_active_sessions:
            endpointInfo_body["num_active_sessions"] = self.num_active_sessions
        if self.num_clusters:
            endpointInfo_body["num_clusters"] = self.num_clusters
        if self.odbc_params:
            endpointInfo_body["odbc_params"] = self.odbc_params.as_request()[1]
        if self.spot_instance_policy:
            endpointInfo_body["spot_instance_policy"] = self.spot_instance_policy.value
        if self.state:
            endpointInfo_body["state"] = self.state.value
        if self.tags:
            endpointInfo_body["tags"] = self.tags.as_request()[1]
        if self.warehouse_type:
            endpointInfo_body["warehouse_type"] = self.warehouse_type.value

        return endpointInfo_query, endpointInfo_body

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

    def as_request(self) -> (dict, dict):
        endpointTagPair_query, endpointTagPair_body = {}, {}
        if self.key:
            endpointTagPair_body["key"] = self.key
        if self.value:
            endpointTagPair_body["value"] = self.value

        return endpointTagPair_query, endpointTagPair_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "EndpointTagPair":
        return cls(
            key=d.get("key", None),
            value=d.get("value", None),
        )


@dataclass
class EndpointTags:

    custom_tags: "List[EndpointTagPair]"

    def as_request(self) -> (dict, dict):
        endpointTags_query, endpointTags_body = {}, {}
        if self.custom_tags:
            endpointTags_body["custom_tags"] = [
                v.as_request()[1] for v in self.custom_tags
            ]

        return endpointTags_query, endpointTags_body

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

    def as_request(self) -> (dict, dict):
        getAlertRequest_query, getAlertRequest_body = {}, {}
        if self.alert_id:
            getAlertRequest_body["alert_id"] = self.alert_id

        return getAlertRequest_query, getAlertRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "GetAlertRequest":
        return cls(
            alert_id=d.get("alert_id", None),
        )


@dataclass
class GetDashboardRequest:
    """Retrieve a definition"""

    dashboard_id: str  # path

    def as_request(self) -> (dict, dict):
        getDashboardRequest_query, getDashboardRequest_body = {}, {}
        if self.dashboard_id:
            getDashboardRequest_body["dashboard_id"] = self.dashboard_id

        return getDashboardRequest_query, getDashboardRequest_body

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

    def as_request(self) -> (dict, dict):
        getDbsqlPermissionRequest_query, getDbsqlPermissionRequest_body = {}, {}
        if self.objectId:
            getDbsqlPermissionRequest_body["objectId"] = self.objectId
        if self.objectType:
            getDbsqlPermissionRequest_body["objectType"] = self.objectType.value

        return getDbsqlPermissionRequest_query, getDbsqlPermissionRequest_body

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

    def as_request(self) -> (dict, dict):
        getQueryRequest_query, getQueryRequest_body = {}, {}
        if self.query_id:
            getQueryRequest_body["query_id"] = self.query_id

        return getQueryRequest_query, getQueryRequest_body

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

    def as_request(self) -> (dict, dict):
        getResponse_query, getResponse_body = {}, {}
        if self.access_control_list:
            getResponse_body["access_control_list"] = [
                v.as_request()[1] for v in self.access_control_list
            ]
        if self.object_id:
            getResponse_body["object_id"] = self.object_id.value
        if self.object_type:
            getResponse_body["object_type"] = self.object_type

        return getResponse_query, getResponse_body

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

    def as_request(self) -> (dict, dict):
        getSubscriptionsRequest_query, getSubscriptionsRequest_body = {}, {}
        if self.alert_id:
            getSubscriptionsRequest_body["alert_id"] = self.alert_id

        return getSubscriptionsRequest_query, getSubscriptionsRequest_body

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

    def as_request(self) -> (dict, dict):
        getWarehouseRequest_query, getWarehouseRequest_body = {}, {}
        if self.id:
            getWarehouseRequest_body["id"] = self.id

        return getWarehouseRequest_query, getWarehouseRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "GetWarehouseRequest":
        return cls(
            id=d.get("id", None),
        )


@dataclass
class GetWarehouseResponse:

    # The amount of time in minutes that a SQL Endpoint must be idle (i.e., no
    # RUNNING queries) before it is automatically stopped.
    #
    # Supported values: - Must be == 0 or >= 10 mins - 0 indicates no autostop.
    #
    # Defaults to 120 mins
    auto_stop_mins: int
    # Channel Details
    channel: "Channel"
    # Size of the clusters allocated for this endpoint. Increasing the size of a
    # spark cluster allows you to run larger queries on it. If you want to
    # increase the number of concurrent queries, please tune max_num_clusters.
    #
    # Supported values: - 2X-Small - X-Small - Small - Medium - Large - X-Large
    # - 2X-Large - 3X-Large - 4X-Large
    cluster_size: str
    # endpoint creator name
    creator_name: str
    # Configures whether the endpoint should use Databricks Compute (aka Nephos)
    #
    # Deprecated: Use enable_serverless_compute TODO(SC-79930): Remove the field
    # once clients are updated
    enable_databricks_compute: bool
    # Configures whether the endpoint should use Photon optimized clusters.
    #
    # Defaults to false.
    enable_photon: bool
    # Configures whether the endpoint should use Serverless Compute (aka Nephos)
    #
    # Defaults to value in global endpoint settings
    enable_serverless_compute: bool
    # Optional health status. Assume the endpoint is healthy if this field is
    # not set.
    health: "EndpointHealth"
    # unique identifier for endpoint
    id: str
    # Deprecated. Instance profile used to pass IAM role to the cluster
    instance_profile_arn: str
    # the jdbc connection string for this endpoint
    jdbc_url: str
    # Maximum number of clusters that the autoscaler will create to handle
    # concurrent queries.
    #
    # Supported values: - Must be >= min_num_clusters - Must be <= 30.
    #
    # Defaults to min_clusters if unset.
    max_num_clusters: int
    # Minimum number of available clusters that will be maintained for this SQL
    # Endpoint. Increasing this will ensure that a larger number of clusters are
    # always running and therefore may reduce the cold start time for new
    # queries. This is similar to reserved vs. revocable cores in a resource
    # manager.
    #
    # Supported values: - Must be > 0 - Must be <= min(max_num_clusters, 30)
    #
    # Defaults to 1
    min_num_clusters: int
    # Logical name for the cluster.
    #
    # Supported values: - Must be unique within an org. - Must be less than 100
    # characters.
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
    # A set of key-value pairs that will be tagged on all resources (e.g., AWS
    # instances and EBS volumes) associated with this SQL Endpoints.
    #
    # Supported values: - Number of tags < 45.
    tags: "EndpointTags"

    warehouse_type: "WarehouseType"

    def as_request(self) -> (dict, dict):
        getWarehouseResponse_query, getWarehouseResponse_body = {}, {}
        if self.auto_stop_mins:
            getWarehouseResponse_body["auto_stop_mins"] = self.auto_stop_mins
        if self.channel:
            getWarehouseResponse_body["channel"] = self.channel.as_request()[1]
        if self.cluster_size:
            getWarehouseResponse_body["cluster_size"] = self.cluster_size
        if self.creator_name:
            getWarehouseResponse_body["creator_name"] = self.creator_name
        if self.enable_databricks_compute:
            getWarehouseResponse_body[
                "enable_databricks_compute"
            ] = self.enable_databricks_compute
        if self.enable_photon:
            getWarehouseResponse_body["enable_photon"] = self.enable_photon
        if self.enable_serverless_compute:
            getWarehouseResponse_body[
                "enable_serverless_compute"
            ] = self.enable_serverless_compute
        if self.health:
            getWarehouseResponse_body["health"] = self.health.as_request()[1]
        if self.id:
            getWarehouseResponse_body["id"] = self.id
        if self.instance_profile_arn:
            getWarehouseResponse_body[
                "instance_profile_arn"
            ] = self.instance_profile_arn
        if self.jdbc_url:
            getWarehouseResponse_body["jdbc_url"] = self.jdbc_url
        if self.max_num_clusters:
            getWarehouseResponse_body["max_num_clusters"] = self.max_num_clusters
        if self.min_num_clusters:
            getWarehouseResponse_body["min_num_clusters"] = self.min_num_clusters
        if self.name:
            getWarehouseResponse_body["name"] = self.name
        if self.num_active_sessions:
            getWarehouseResponse_body["num_active_sessions"] = self.num_active_sessions
        if self.num_clusters:
            getWarehouseResponse_body["num_clusters"] = self.num_clusters
        if self.odbc_params:
            getWarehouseResponse_body["odbc_params"] = self.odbc_params.as_request()[1]
        if self.spot_instance_policy:
            getWarehouseResponse_body[
                "spot_instance_policy"
            ] = self.spot_instance_policy.value
        if self.state:
            getWarehouseResponse_body["state"] = self.state.value
        if self.tags:
            getWarehouseResponse_body["tags"] = self.tags.as_request()[1]
        if self.warehouse_type:
            getWarehouseResponse_body["warehouse_type"] = self.warehouse_type.value

        return getWarehouseResponse_query, getWarehouseResponse_body

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
    # Spark confs for external hive metastore configuration JSON serialized size
    # must be less than <= 512K
    data_access_config: "List[EndpointConfPair]"
    # Enable Serverless compute for SQL Endpoints
    #
    # Deprecated: Use enable_serverless_compute TODO(SC-79930): Remove the field
    # once clients are updated
    enable_databricks_compute: bool
    # Enable Serverless compute for SQL Endpoints
    enable_serverless_compute: bool
    # List of Warehouse Types allowed in this workspace (limits allowed value of
    # the type field in CreateWarehouse and EditWarehouse). Note: Some types
    # cannot be disabled, they don't need to be specified in
    # SetWorkspaceWarehouseConfig. Note: Disabling a type may cause existing
    # warehouses to be converted to another type. Used by frontend to save
    # specific type availability in the warehouse create and edit form UI.
    enabled_warehouse_types: "List[WarehouseTypePair]"
    # Deprecated: Use sql_configuration_parameters
    global_param: "RepeatedEndpointConfPairs"
    # GCP only: Google Service Account used to pass to cluster to access Google
    # Cloud Storage
    google_service_account: str
    # AWS Only: Instance profile used to pass IAM role to the cluster
    instance_profile_arn: str
    # Security policy for endpoints
    security_policy: "GetWorkspaceWarehouseConfigResponseSecurityPolicy"
    # SQL configuration parameters
    sql_configuration_parameters: "RepeatedEndpointConfPairs"

    def as_request(self) -> (dict, dict):
        (
            getWorkspaceWarehouseConfigResponse_query,
            getWorkspaceWarehouseConfigResponse_body,
        ) = ({}, {})
        if self.channel:
            getWorkspaceWarehouseConfigResponse_body[
                "channel"
            ] = self.channel.as_request()[1]
        if self.config_param:
            getWorkspaceWarehouseConfigResponse_body[
                "config_param"
            ] = self.config_param.as_request()[1]
        if self.data_access_config:
            getWorkspaceWarehouseConfigResponse_body["data_access_config"] = [
                v.as_request()[1] for v in self.data_access_config
            ]
        if self.enable_databricks_compute:
            getWorkspaceWarehouseConfigResponse_body[
                "enable_databricks_compute"
            ] = self.enable_databricks_compute
        if self.enable_serverless_compute:
            getWorkspaceWarehouseConfigResponse_body[
                "enable_serverless_compute"
            ] = self.enable_serverless_compute
        if self.enabled_warehouse_types:
            getWorkspaceWarehouseConfigResponse_body["enabled_warehouse_types"] = [
                v.as_request()[1] for v in self.enabled_warehouse_types
            ]
        if self.global_param:
            getWorkspaceWarehouseConfigResponse_body[
                "global_param"
            ] = self.global_param.as_request()[1]
        if self.google_service_account:
            getWorkspaceWarehouseConfigResponse_body[
                "google_service_account"
            ] = self.google_service_account
        if self.instance_profile_arn:
            getWorkspaceWarehouseConfigResponse_body[
                "instance_profile_arn"
            ] = self.instance_profile_arn
        if self.security_policy:
            getWorkspaceWarehouseConfigResponse_body[
                "security_policy"
            ] = self.security_policy.value
        if self.sql_configuration_parameters:
            getWorkspaceWarehouseConfigResponse_body[
                "sql_configuration_parameters"
            ] = self.sql_configuration_parameters.as_request()[1]

        return (
            getWorkspaceWarehouseConfigResponse_query,
            getWorkspaceWarehouseConfigResponse_body,
        )

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

    def as_request(self) -> (dict, dict):
        listDashboardsRequest_query, listDashboardsRequest_body = {}, {}
        if self.order:
            listDashboardsRequest_query["order"] = self.order.value
        if self.page:
            listDashboardsRequest_query["page"] = self.page
        if self.page_size:
            listDashboardsRequest_query["page_size"] = self.page_size
        if self.q:
            listDashboardsRequest_query["q"] = self.q

        return listDashboardsRequest_query, listDashboardsRequest_body

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
    order: str  # query
    # Page number to retrieve.
    page: int  # query
    # Number of queries to return per page.
    page_size: int  # query
    # Full text search term
    q: str  # query

    def as_request(self) -> (dict, dict):
        listQueriesRequest_query, listQueriesRequest_body = {}, {}
        if self.order:
            listQueriesRequest_query["order"] = self.order
        if self.page:
            listQueriesRequest_query["page"] = self.page
        if self.page_size:
            listQueriesRequest_query["page_size"] = self.page_size
        if self.q:
            listQueriesRequest_query["q"] = self.q

        return listQueriesRequest_query, listQueriesRequest_body

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

    def as_request(self) -> (dict, dict):
        listQueriesResponse_query, listQueriesResponse_body = {}, {}
        if self.has_next_page:
            listQueriesResponse_body["has_next_page"] = self.has_next_page
        if self.next_page_token:
            listQueriesResponse_body["next_page_token"] = self.next_page_token
        if self.res:
            listQueriesResponse_body["res"] = [v.as_request()[1] for v in self.res]

        return listQueriesResponse_query, listQueriesResponse_body

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

    def as_request(self) -> (dict, dict):
        listQueryHistoryRequest_query, listQueryHistoryRequest_body = {}, {}
        if self.filter_by:
            listQueryHistoryRequest_query["filter_by"] = self.filter_by.as_request()[1]
        if self.include_metrics:
            listQueryHistoryRequest_query["include_metrics"] = self.include_metrics
        if self.max_results:
            listQueryHistoryRequest_query["max_results"] = self.max_results
        if self.page_token:
            listQueryHistoryRequest_query["page_token"] = self.page_token

        return listQueryHistoryRequest_query, listQueryHistoryRequest_body

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

    def as_request(self) -> (dict, dict):
        listResponse_query, listResponse_body = {}, {}
        if self.count:
            listResponse_body["count"] = self.count
        if self.page:
            listResponse_body["page"] = self.page
        if self.page_size:
            listResponse_body["page_size"] = self.page_size
        if self.results:
            listResponse_body["results"] = [v.as_request()[1] for v in self.results]

        return listResponse_query, listResponse_body

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

    def as_request(self) -> (dict, dict):
        listSchedulesRequest_query, listSchedulesRequest_body = {}, {}
        if self.alert_id:
            listSchedulesRequest_body["alert_id"] = self.alert_id

        return listSchedulesRequest_query, listSchedulesRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ListSchedulesRequest":
        return cls(
            alert_id=d.get("alert_id", None),
        )


@dataclass
class ListWarehousesRequest:
    """List warehouses"""

    # Service Principal which will be used to fetch the list of endpoints. If
    # not specified, the user from the session header is used.
    run_as_user_id: int  # query

    def as_request(self) -> (dict, dict):
        listWarehousesRequest_query, listWarehousesRequest_body = {}, {}
        if self.run_as_user_id:
            listWarehousesRequest_query["run_as_user_id"] = self.run_as_user_id

        return listWarehousesRequest_query, listWarehousesRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ListWarehousesRequest":
        return cls(
            run_as_user_id=d.get("run_as_user_id", None),
        )


@dataclass
class ListWarehousesResponse:

    # A list of warehouses and their configurations.
    warehouses: "List[EndpointInfo]"

    def as_request(self) -> (dict, dict):
        listWarehousesResponse_query, listWarehousesResponse_body = {}, {}
        if self.warehouses:
            listWarehousesResponse_body["warehouses"] = [
                v.as_request()[1] for v in self.warehouses
            ]

        return listWarehousesResponse_query, listWarehousesResponse_body

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

    def as_request(self) -> (dict, dict):
        odbcParams_query, odbcParams_body = {}, {}
        if self.hostname:
            odbcParams_body["hostname"] = self.hostname
        if self.path:
            odbcParams_body["path"] = self.path
        if self.port:
            odbcParams_body["port"] = self.port
        if self.protocol:
            odbcParams_body["protocol"] = self.protocol

        return odbcParams_query, odbcParams_body

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

    # The literal parameter marker that appears between double curly braces in
    # the query text.
    name: str
    # The text displayed in a parameter picking widget.
    title: str
    # Parameters can have several different types.
    type: "ParameterType"
    # The default value for this parameter.
    value: Any

    def as_request(self) -> (dict, dict):
        parameter_query, parameter_body = {}, {}
        if self.name:
            parameter_body["name"] = self.name
        if self.title:
            parameter_body["title"] = self.title
        if self.type:
            parameter_body["type"] = self.type.value
        if self.value:
            parameter_body["value"] = self.value

        return parameter_query, parameter_body

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

    # Describes whether the authenticated user is allowed to edit the definition
    # of this query.
    can_edit: bool
    # The timestamp when this query was created.
    created_at: str
    # Data Source ID. The UUID that uniquely identifies this data source / SQL
    # warehouse across the API.
    data_source_id: str
    # General description that conveys additional information about this query
    # such as usage notes.
    description: str

    id: str
    # Indicates whether the query is trashed. Trashed queries can't be used in
    # dashboards, or appear in search results. If this boolean is `true`, the
    # `options` property for this query includes a `moved_to_trash_at`
    # timestamp. Trashed queries are permanently deleted after 30 days.
    is_archived: bool
    # Whether the query is a draft. Draft queries only appear in list views for
    # their owners. Visualizations from draft queries cannot appear on
    # dashboards.
    is_draft: bool
    # Whether this query object appears in the current user's favorites list.
    # This flag determines whether the star icon for favorites is selected.
    is_favorite: bool
    # Text parameter types are not safe from SQL injection for all types of data
    # source. Set this Boolean parameter to `true` if a query either does not
    # use any text type parameters or uses a data source type where text type
    # parameters are handled safely.
    is_safe: bool

    last_modified_by: "User"
    # The ID of the user who last saved changes to this query.
    last_modified_by_id: int
    # If there is a cached result for this query and user, this field includes
    # the query result ID. If this query uses parameters, this field is always
    # null.
    latest_query_data_id: str
    # The title of this query that appears in list views, widget headings, and
    # on the query page.
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

    def as_request(self) -> (dict, dict):
        query_query, query_body = {}, {}
        if self.can_edit:
            query_body["can_edit"] = self.can_edit
        if self.created_at:
            query_body["created_at"] = self.created_at
        if self.data_source_id:
            query_body["data_source_id"] = self.data_source_id
        if self.description:
            query_body["description"] = self.description
        if self.id:
            query_body["id"] = self.id
        if self.is_archived:
            query_body["is_archived"] = self.is_archived
        if self.is_draft:
            query_body["is_draft"] = self.is_draft
        if self.is_favorite:
            query_body["is_favorite"] = self.is_favorite
        if self.is_safe:
            query_body["is_safe"] = self.is_safe
        if self.last_modified_by:
            query_body["last_modified_by"] = self.last_modified_by.as_request()[1]
        if self.last_modified_by_id:
            query_body["last_modified_by_id"] = self.last_modified_by_id
        if self.latest_query_data_id:
            query_body["latest_query_data_id"] = self.latest_query_data_id
        if self.name:
            query_body["name"] = self.name
        if self.options:
            query_body["options"] = self.options.as_request()[1]
        if self.permission_tier:
            query_body["permission_tier"] = self.permission_tier.value
        if self.query:
            query_body["query"] = self.query
        if self.query_hash:
            query_body["query_hash"] = self.query_hash
        if self.schedule:
            query_body["schedule"] = self.schedule.as_request()[1]
        if self.tags:
            query_body["tags"] = [v for v in self.tags]
        if self.updated_at:
            query_body["updated_at"] = self.updated_at
        if self.user:
            query_body["user"] = self.user.as_request()[1]
        if self.user_id:
            query_body["user_id"] = self.user_id
        if self.visualizations:
            query_body["visualizations"] = [
                v.as_request()[1] for v in self.visualizations
            ]

        return query_query, query_body

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

    def as_request(self) -> (dict, dict):
        queryFilter_query, queryFilter_body = {}, {}
        if self.query_start_time_range:
            queryFilter_body[
                "query_start_time_range"
            ] = self.query_start_time_range.as_request()[1]
        if self.statuses:
            queryFilter_body["statuses"] = [v for v in self.statuses]
        if self.user_ids:
            queryFilter_body["user_ids"] = [v for v in self.user_ids]
        if self.warehouse_ids:
            queryFilter_body["warehouse_ids"] = [v for v in self.warehouse_ids]

        return queryFilter_query, queryFilter_body

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
    # Total execution time of the query from the client’s point of view, in
    # milliseconds.
    duration: int
    # Alias for `warehouse_id`.
    endpoint_id: str
    # Message describing why the query could not complete.
    error_message: str
    # The ID of the user whose credentials were used to run the query.
    executed_as_user_id: int
    # The email address or username of the user whose credentials were used to
    # run the query.
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

    def as_request(self) -> (dict, dict):
        queryInfo_query, queryInfo_body = {}, {}
        if self.channel_used:
            queryInfo_body["channel_used"] = self.channel_used.as_request()[1]
        if self.duration:
            queryInfo_body["duration"] = self.duration
        if self.endpoint_id:
            queryInfo_body["endpoint_id"] = self.endpoint_id
        if self.error_message:
            queryInfo_body["error_message"] = self.error_message
        if self.executed_as_user_id:
            queryInfo_body["executed_as_user_id"] = self.executed_as_user_id
        if self.executed_as_user_name:
            queryInfo_body["executed_as_user_name"] = self.executed_as_user_name
        if self.execution_end_time_ms:
            queryInfo_body["execution_end_time_ms"] = self.execution_end_time_ms
        if self.is_final:
            queryInfo_body["is_final"] = self.is_final
        if self.lookup_key:
            queryInfo_body["lookup_key"] = self.lookup_key
        if self.metrics:
            queryInfo_body["metrics"] = self.metrics.as_request()[1]
        if self.plans_state:
            queryInfo_body["plans_state"] = self.plans_state.value
        if self.query_end_time_ms:
            queryInfo_body["query_end_time_ms"] = self.query_end_time_ms
        if self.query_id:
            queryInfo_body["query_id"] = self.query_id
        if self.query_start_time_ms:
            queryInfo_body["query_start_time_ms"] = self.query_start_time_ms
        if self.query_text:
            queryInfo_body["query_text"] = self.query_text
        if self.rows_produced:
            queryInfo_body["rows_produced"] = self.rows_produced
        if self.spark_ui_url:
            queryInfo_body["spark_ui_url"] = self.spark_ui_url
        if self.statement_type:
            queryInfo_body["statement_type"] = self.statement_type.value
        if self.status:
            queryInfo_body["status"] = self.status.value
        if self.user_id:
            queryInfo_body["user_id"] = self.user_id
        if self.user_name:
            queryInfo_body["user_name"] = self.user_name
        if self.warehouse_id:
            queryInfo_body["warehouse_id"] = self.warehouse_id

        return queryInfo_query, queryInfo_body

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

    def as_request(self) -> (dict, dict):
        queryInterval_query, queryInterval_body = {}, {}
        if self.day_of_week:
            queryInterval_body["day_of_week"] = self.day_of_week
        if self.interval:
            queryInterval_body["interval"] = self.interval
        if self.time:
            queryInterval_body["time"] = self.time
        if self.until:
            queryInterval_body["until"] = self.until

        return queryInterval_query, queryInterval_body

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

    def as_request(self) -> (dict, dict):
        queryList_query, queryList_body = {}, {}
        if self.count:
            queryList_body["count"] = self.count
        if self.page:
            queryList_body["page"] = self.page
        if self.page_size:
            queryList_body["page_size"] = self.page_size
        if self.results:
            queryList_body["results"] = [v.as_request()[1] for v in self.results]

        return queryList_query, queryList_body

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
    # Total execution time for all individual Photon query engine tasks in the
    # query, in milliseconds.
    photon_total_time_ms: int
    # Time spent waiting to execute the query because the SQL warehouse is
    # already running the maximum number of concurrent queries, in milliseconds.
    queued_overload_time_ms: int
    # Time waiting for compute resources to be provisioned for the SQL
    # warehouse, in milliseconds.
    queued_provisioning_time_ms: int
    # Total size of data read by the query, in bytes.
    read_bytes: int
    # Size of persistent data read from the cache, in bytes.
    read_cache_bytes: int
    # Number of files read after pruning.
    read_files_count: int
    # Number of partitions read after pruning.
    read_partitions_count: int
    # Size of persistent data read from cloud object storage on your cloud
    # tenant, in bytes.
    read_remote_bytes: int
    # Time spent fetching the query results after the execution finished, in
    # milliseconds.
    result_fetch_time_ms: int
    # true if the query result was fetched from cache, false otherwise.
    result_from_cache: bool
    # Total number of rows returned by the query.
    rows_produced_count: int
    # Total number of rows read by the query.
    rows_read_count: int
    # Size of data temporarily written to disk while executing the query, in
    # bytes.
    spill_to_disk_bytes: int
    # Sum of execution time for all of the query’s tasks, in milliseconds.
    task_total_time_ms: int
    # Number of files that would have been read without pruning.
    total_files_count: int
    # Number of partitions that would have been read without pruning.
    total_partitions_count: int
    # Total execution time of the query from the client’s point of view, in
    # milliseconds.
    total_time_ms: int
    # Size pf persistent data written to cloud object storage in your cloud
    # tenant, in bytes.
    write_remote_bytes: int

    def as_request(self) -> (dict, dict):
        queryMetrics_query, queryMetrics_body = {}, {}
        if self.compilation_time_ms:
            queryMetrics_body["compilation_time_ms"] = self.compilation_time_ms
        if self.execution_time_ms:
            queryMetrics_body["execution_time_ms"] = self.execution_time_ms
        if self.network_sent_bytes:
            queryMetrics_body["network_sent_bytes"] = self.network_sent_bytes
        if self.photon_total_time_ms:
            queryMetrics_body["photon_total_time_ms"] = self.photon_total_time_ms
        if self.queued_overload_time_ms:
            queryMetrics_body["queued_overload_time_ms"] = self.queued_overload_time_ms
        if self.queued_provisioning_time_ms:
            queryMetrics_body[
                "queued_provisioning_time_ms"
            ] = self.queued_provisioning_time_ms
        if self.read_bytes:
            queryMetrics_body["read_bytes"] = self.read_bytes
        if self.read_cache_bytes:
            queryMetrics_body["read_cache_bytes"] = self.read_cache_bytes
        if self.read_files_count:
            queryMetrics_body["read_files_count"] = self.read_files_count
        if self.read_partitions_count:
            queryMetrics_body["read_partitions_count"] = self.read_partitions_count
        if self.read_remote_bytes:
            queryMetrics_body["read_remote_bytes"] = self.read_remote_bytes
        if self.result_fetch_time_ms:
            queryMetrics_body["result_fetch_time_ms"] = self.result_fetch_time_ms
        if self.result_from_cache:
            queryMetrics_body["result_from_cache"] = self.result_from_cache
        if self.rows_produced_count:
            queryMetrics_body["rows_produced_count"] = self.rows_produced_count
        if self.rows_read_count:
            queryMetrics_body["rows_read_count"] = self.rows_read_count
        if self.spill_to_disk_bytes:
            queryMetrics_body["spill_to_disk_bytes"] = self.spill_to_disk_bytes
        if self.task_total_time_ms:
            queryMetrics_body["task_total_time_ms"] = self.task_total_time_ms
        if self.total_files_count:
            queryMetrics_body["total_files_count"] = self.total_files_count
        if self.total_partitions_count:
            queryMetrics_body["total_partitions_count"] = self.total_partitions_count
        if self.total_time_ms:
            queryMetrics_body["total_time_ms"] = self.total_time_ms
        if self.write_remote_bytes:
            queryMetrics_body["write_remote_bytes"] = self.write_remote_bytes

        return queryMetrics_query, queryMetrics_body

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

    # The timestamp when this query was moved to trash. Only present when the
    # `is_archived` property is `true`. Trashed items are deleted after thirty
    # days.
    moved_to_trash_at: str

    parameters: "List[Parameter]"

    def as_request(self) -> (dict, dict):
        queryOptions_query, queryOptions_body = {}, {}
        if self.moved_to_trash_at:
            queryOptions_body["moved_to_trash_at"] = self.moved_to_trash_at
        if self.parameters:
            queryOptions_body["parameters"] = [
                v.as_request()[1] for v in self.parameters
            ]

        return queryOptions_query, queryOptions_body

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
    # General description that can convey additional information about this
    # query such as usage notes.
    description: str
    # The name or title of this query to display in list views.
    name: str
    # Exclusively used for storing a list parameter definitions. A parameter is
    # an object with `title`, `name`, `type`, and `value` properties. The
    # `value` field here is the default value. It can be overridden at runtime.
    options: Any
    # The text of the query.
    query: str

    query_id: str  # path
    # JSON object that describes the scheduled execution frequency. A schedule
    # object includes `interval`, `time`, `day_of_week`, and `until` fields. If
    # a scheduled is supplied, then only `interval` is required. All other field
    # can be `null`.
    schedule: "QueryInterval"

    def as_request(self) -> (dict, dict):
        queryPostContent_query, queryPostContent_body = {}, {}
        if self.data_source_id:
            queryPostContent_body["data_source_id"] = self.data_source_id
        if self.description:
            queryPostContent_body["description"] = self.description
        if self.name:
            queryPostContent_body["name"] = self.name
        if self.options:
            queryPostContent_body["options"] = self.options
        if self.query:
            queryPostContent_body["query"] = self.query
        if self.query_id:
            queryPostContent_body["query_id"] = self.query_id
        if self.schedule:
            queryPostContent_body["schedule"] = self.schedule.as_request()[1]

        return queryPostContent_query, queryPostContent_body

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
    # ID of the SQL warehouse to refresh with. If `null`, query's SQL warehouse
    # will be used to refresh.
    data_source_id: str
    # ID of the refresh schedule.
    id: str

    def as_request(self) -> (dict, dict):
        refreshSchedule_query, refreshSchedule_body = {}, {}
        if self.cron:
            refreshSchedule_body["cron"] = self.cron
        if self.data_source_id:
            refreshSchedule_body["data_source_id"] = self.data_source_id
        if self.id:
            refreshSchedule_body["id"] = self.id

        return refreshSchedule_query, refreshSchedule_body

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

    def as_request(self) -> (dict, dict):
        repeatedEndpointConfPairs_query, repeatedEndpointConfPairs_body = {}, {}
        if self.config_pair:
            repeatedEndpointConfPairs_body["config_pair"] = [
                v.as_request()[1] for v in self.config_pair
            ]
        if self.configuration_pairs:
            repeatedEndpointConfPairs_body["configuration_pairs"] = [
                v.as_request()[1] for v in self.configuration_pairs
            ]

        return repeatedEndpointConfPairs_query, repeatedEndpointConfPairs_body

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

    def as_request(self) -> (dict, dict):
        restoreDashboardRequest_query, restoreDashboardRequest_body = {}, {}
        if self.dashboard_id:
            restoreDashboardRequest_body["dashboard_id"] = self.dashboard_id

        return restoreDashboardRequest_query, restoreDashboardRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "RestoreDashboardRequest":
        return cls(
            dashboard_id=d.get("dashboard_id", None),
        )


@dataclass
class RestoreQueryRequest:
    """Restore a query"""

    query_id: str  # path

    def as_request(self) -> (dict, dict):
        restoreQueryRequest_query, restoreQueryRequest_body = {}, {}
        if self.query_id:
            restoreQueryRequest_body["query_id"] = self.query_id

        return restoreQueryRequest_query, restoreQueryRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "RestoreQueryRequest":
        return cls(
            query_id=d.get("query_id", None),
        )


@dataclass
class SetRequest:
    """Set object ACL"""

    access_control_list: "List[AccessControl]"
    # Object ID. The ACL for the object with this UUID is overwritten by this
    # request's POST content.
    objectId: str  # path
    # The type of object permission to set.
    objectType: "ObjectTypePlural"  # path

    def as_request(self) -> (dict, dict):
        setRequest_query, setRequest_body = {}, {}
        if self.access_control_list:
            setRequest_body["access_control_list"] = [
                v.as_request()[1] for v in self.access_control_list
            ]
        if self.objectId:
            setRequest_body["objectId"] = self.objectId
        if self.objectType:
            setRequest_body["objectType"] = self.objectType.value

        return setRequest_query, setRequest_body

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

    def as_request(self) -> (dict, dict):
        setResponse_query, setResponse_body = {}, {}
        if self.access_control_list:
            setResponse_body["access_control_list"] = [
                v.as_request()[1] for v in self.access_control_list
            ]
        if self.object_id:
            setResponse_body["object_id"] = self.object_id.value
        if self.object_type:
            setResponse_body["object_type"] = self.object_type

        return setResponse_query, setResponse_body

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
    # Spark confs for external hive metastore configuration JSON serialized size
    # must be less than <= 512K
    data_access_config: "List[EndpointConfPair]"
    # Enable Serverless compute for SQL Endpoints
    #
    # Deprecated: Use enable_serverless_compute TODO(SC-79930): Remove the field
    # once clients are updated
    enable_databricks_compute: bool
    # Enable Serverless compute for SQL Endpoints
    enable_serverless_compute: bool
    # List of Warehouse Types allowed in this workspace (limits allowed value of
    # the type field in CreateWarehouse and EditWarehouse). Note: Some types
    # cannot be disabled, they don't need to be specified in
    # SetWorkspaceWarehouseConfig. Note: Disabling a type may cause existing
    # warehouses to be converted to another type. Used by frontend to save
    # specific type availability in the warehouse create and edit form UI.
    enabled_warehouse_types: "List[WarehouseTypePair]"
    # Deprecated: Use sql_configuration_parameters
    global_param: "RepeatedEndpointConfPairs"
    # GCP only: Google Service Account used to pass to cluster to access Google
    # Cloud Storage
    google_service_account: str
    # AWS Only: Instance profile used to pass IAM role to the cluster
    instance_profile_arn: str
    # Security policy for endpoints
    security_policy: "SetWorkspaceWarehouseConfigRequestSecurityPolicy"
    # Internal. Used by frontend to save Serverless Compute agreement value.
    serverless_agreement: bool
    # SQL configuration parameters
    sql_configuration_parameters: "RepeatedEndpointConfPairs"

    def as_request(self) -> (dict, dict):
        (
            setWorkspaceWarehouseConfigRequest_query,
            setWorkspaceWarehouseConfigRequest_body,
        ) = ({}, {})
        if self.channel:
            setWorkspaceWarehouseConfigRequest_body[
                "channel"
            ] = self.channel.as_request()[1]
        if self.config_param:
            setWorkspaceWarehouseConfigRequest_body[
                "config_param"
            ] = self.config_param.as_request()[1]
        if self.data_access_config:
            setWorkspaceWarehouseConfigRequest_body["data_access_config"] = [
                v.as_request()[1] for v in self.data_access_config
            ]
        if self.enable_databricks_compute:
            setWorkspaceWarehouseConfigRequest_body[
                "enable_databricks_compute"
            ] = self.enable_databricks_compute
        if self.enable_serverless_compute:
            setWorkspaceWarehouseConfigRequest_body[
                "enable_serverless_compute"
            ] = self.enable_serverless_compute
        if self.enabled_warehouse_types:
            setWorkspaceWarehouseConfigRequest_body["enabled_warehouse_types"] = [
                v.as_request()[1] for v in self.enabled_warehouse_types
            ]
        if self.global_param:
            setWorkspaceWarehouseConfigRequest_body[
                "global_param"
            ] = self.global_param.as_request()[1]
        if self.google_service_account:
            setWorkspaceWarehouseConfigRequest_body[
                "google_service_account"
            ] = self.google_service_account
        if self.instance_profile_arn:
            setWorkspaceWarehouseConfigRequest_body[
                "instance_profile_arn"
            ] = self.instance_profile_arn
        if self.security_policy:
            setWorkspaceWarehouseConfigRequest_body[
                "security_policy"
            ] = self.security_policy.value
        if self.serverless_agreement:
            setWorkspaceWarehouseConfigRequest_body[
                "serverless_agreement"
            ] = self.serverless_agreement
        if self.sql_configuration_parameters:
            setWorkspaceWarehouseConfigRequest_body[
                "sql_configuration_parameters"
            ] = self.sql_configuration_parameters.as_request()[1]

        return (
            setWorkspaceWarehouseConfigRequest_query,
            setWorkspaceWarehouseConfigRequest_body,
        )

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

    def as_request(self) -> (dict, dict):
        startRequest_query, startRequest_body = {}, {}
        if self.id:
            startRequest_body["id"] = self.id

        return startRequest_query, startRequest_body

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

    def as_request(self) -> (dict, dict):
        stopRequest_query, stopRequest_body = {}, {}
        if self.id:
            stopRequest_body["id"] = self.id

        return stopRequest_query, stopRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "StopRequest":
        return cls(
            id=d.get("id", None),
        )


@dataclass
class Subscription:

    # ID of the alert.
    alert_id: str
    # Alert destination subscribed to the alert, if it exists. Alert
    # destinations can be configured by admins through the UI. See [here].
    #
    # [here]: https://docs.databricks.com/sql/admin/alert-destinations.html
    destination: "Destination"
    # ID of the alert subscription.
    id: str

    user: "User"

    def as_request(self) -> (dict, dict):
        subscription_query, subscription_body = {}, {}
        if self.alert_id:
            subscription_body["alert_id"] = self.alert_id
        if self.destination:
            subscription_body["destination"] = self.destination.as_request()[1]
        if self.id:
            subscription_body["id"] = self.id
        if self.user:
            subscription_body["user"] = self.user.as_request()[1]

        return subscription_query, subscription_body

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

    def as_request(self) -> (dict, dict):
        success_query, success_body = {}, {}
        if self.message:
            success_body["message"] = self.message.value

        return success_query, success_body

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
    # list of parameters that provide additional information about why the
    # cluster was terminated
    parameters: "Dict[str,str]"
    # type of the termination
    type: "TerminationReasonType"

    def as_request(self) -> (dict, dict):
        terminationReason_query, terminationReason_body = {}, {}
        if self.code:
            terminationReason_body["code"] = self.code.value
        if self.parameters:
            terminationReason_body["parameters"] = self.parameters
        if self.type:
            terminationReason_body["type"] = self.type.value

        return terminationReason_query, terminationReason_body

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

    def as_request(self) -> (dict, dict):
        timeRange_query, timeRange_body = {}, {}
        if self.end_time_ms:
            timeRange_body["end_time_ms"] = self.end_time_ms
        if self.start_time_ms:
            timeRange_body["start_time_ms"] = self.start_time_ms

        return timeRange_query, timeRange_body

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

    def as_request(self) -> (dict, dict):
        transferOwnershipObjectId_query, transferOwnershipObjectId_body = {}, {}
        if self.new_owner:
            transferOwnershipObjectId_body["new_owner"] = self.new_owner

        return transferOwnershipObjectId_query, transferOwnershipObjectId_body

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

    def as_request(self) -> (dict, dict):
        transferOwnershipRequest_query, transferOwnershipRequest_body = {}, {}
        if self.new_owner:
            transferOwnershipRequest_body["new_owner"] = self.new_owner
        if self.objectId:
            transferOwnershipRequest_body["objectId"] = self.objectId.as_request()[1]
        if self.objectType:
            transferOwnershipRequest_body["objectType"] = self.objectType.value

        return transferOwnershipRequest_query, transferOwnershipRequest_body

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

    def as_request(self) -> (dict, dict):
        unsubscribeRequest_query, unsubscribeRequest_body = {}, {}
        if self.alert_id:
            unsubscribeRequest_body["alert_id"] = self.alert_id
        if self.subscription_id:
            unsubscribeRequest_body["subscription_id"] = self.subscription_id

        return unsubscribeRequest_query, unsubscribeRequest_body

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
    # The URL for the gravatar profile picture tied to this user's email
    # address.
    profile_image_url: str

    def as_request(self) -> (dict, dict):
        user_query, user_body = {}, {}
        if self.email:
            user_body["email"] = self.email
        if self.id:
            user_body["id"] = self.id
        if self.is_db_admin:
            user_body["is_db_admin"] = self.is_db_admin
        if self.name:
            user_body["name"] = self.name
        if self.profile_image_url:
            user_body["profile_image_url"] = self.profile_image_url

        return user_query, user_body

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
    # A short description of this visualization. This is not displayed in the
    # UI.
    description: str
    # The UUID for this visualization.
    id: str
    # The name of the visualization that appears on dashboards and the query
    # screen.
    name: str
    # The options object varies widely from one visualization type to the next
    # and is unsupported. Databricks does not recommend modifying visualization
    # settings in JSON.
    options: Any
    # The type of visualization: chart, table, pivot table, and so on.
    type: str

    updated_at: str

    def as_request(self) -> (dict, dict):
        visualization_query, visualization_body = {}, {}
        if self.created_at:
            visualization_body["created_at"] = self.created_at
        if self.description:
            visualization_body["description"] = self.description
        if self.id:
            visualization_body["id"] = self.id
        if self.name:
            visualization_body["name"] = self.name
        if self.options:
            visualization_body["options"] = self.options
        if self.type:
            visualization_body["type"] = self.type
        if self.updated_at:
            visualization_body["updated_at"] = self.updated_at

        return visualization_query, visualization_body

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

    # If set to false the specific warehouse type will not be be allowed as a
    # value for warehouse_type in CreateWarehouse and EditWarehouse
    enabled: bool

    warehouse_type: "WarehouseType"

    def as_request(self) -> (dict, dict):
        warehouseTypePair_query, warehouseTypePair_body = {}, {}
        if self.enabled:
            warehouseTypePair_body["enabled"] = self.enabled
        if self.warehouse_type:
            warehouseTypePair_body["warehouse_type"] = self.warehouse_type.value

        return warehouseTypePair_query, warehouseTypePair_body

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
    # The visualization description API changes frequently and is unsupported.
    # You can duplicate a visualization by copying description objects received
    # _from the API_ and then using them to create a new one with a POST request
    # to the same endpoint. Databricks does not recommend constructing ad-hoc
    # visualizations entirely in JSON.
    visualization: "Visualization"
    # Unused field.
    width: int

    def as_request(self) -> (dict, dict):
        widget_query, widget_body = {}, {}
        if self.id:
            widget_body["id"] = self.id
        if self.options:
            widget_body["options"] = self.options.as_request()[1]
        if self.visualization:
            widget_body["visualization"] = self.visualization.as_request()[1]
        if self.width:
            widget_body["width"] = self.width

        return widget_query, widget_body

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
    # The dashboard ID to which this widget belongs. Each widget can belong to
    # one dashboard.
    dashboard_id: str
    # Whether this widget is hidden on the dashboard.
    isHidden: bool
    # How parameters used by the visualization in this widget relate to other
    # widgets on the dashboard. Databricks does not recommend modifying this
    # definition in JSON.
    parameterMappings: Any
    # Coordinates of this widget on a dashboard. This portion of the API changes
    # frequently and is unsupported.
    position: Any
    # If this is a textbox widget, the application displays this text. This
    # field is ignored if the widget contains a visualization in the
    # `visualization` field.
    text: str
    # Timestamp of the last time this object was updated.
    updated_at: str

    def as_request(self) -> (dict, dict):
        widgetOptions_query, widgetOptions_body = {}, {}
        if self.created_at:
            widgetOptions_body["created_at"] = self.created_at
        if self.dashboard_id:
            widgetOptions_body["dashboard_id"] = self.dashboard_id
        if self.isHidden:
            widgetOptions_body["isHidden"] = self.isHidden
        if self.parameterMappings:
            widgetOptions_body["parameterMappings"] = self.parameterMappings
        if self.position:
            widgetOptions_body["position"] = self.position
        if self.text:
            widgetOptions_body["text"] = self.text
        if self.updated_at:
            widgetOptions_body["updated_at"] = self.updated_at

        return widgetOptions_query, widgetOptions_body

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

    def create(self, request: EditAlert) -> Alert:
        """Create an alert.

        Creates an alert. An alert is a Databricks SQL object that periodically
        runs a query, evaluates a condition of its result, and notifies users or
        alert destinations if the condition was met."""
        query, body = request.as_request()
        json = self._api.do(
            "POST", "/api/2.0/preview/sql/alerts", query=query, body=body
        )
        return Alert.from_dict(json)

    def create_schedule(self, request: CreateRefreshSchedule) -> RefreshSchedule:
        """Create a refresh schedule.

        Creates a new refresh schedule for an alert.

        **Note:** The structure of refresh schedules is subject to change."""
        query, body = request.as_request()
        json = self._api.do(
            "POST",
            f"/api/2.0/preview/sql/alerts/{request.alert_id}/refresh-schedules",
            query=query,
            body=body,
        )
        return RefreshSchedule.from_dict(json)

    def delete(self, request: DeleteAlertRequest):
        """Delete an alert.

        Deletes an alert. Deleted alerts are no longer accessible and cannot be
        restored. **Note:** Unlike queries and dashboards, alerts cannot be
        moved to the trash."""
        query, body = request.as_request()
        self._api.do(
            "DELETE",
            f"/api/2.0/preview/sql/alerts/{request.alert_id}",
            query=query,
            body=body,
        )

    def delete_schedule(self, request: DeleteScheduleRequest):
        """Delete a refresh schedule.

        Deletes an alert's refresh schedule. The refresh schedule specifies when
        to refresh and evaluate the associated query result."""
        query, body = request.as_request()
        self._api.do(
            "DELETE",
            f"/api/2.0/preview/sql/alerts/{request.alert_id}/refresh-schedules/{request.schedule_id}",
            query=query,
            body=body,
        )

    def get(self, request: GetAlertRequest) -> Alert:
        """Get an alert.

        Gets an alert."""
        query, body = request.as_request()
        json = self._api.do(
            "GET",
            f"/api/2.0/preview/sql/alerts/{request.alert_id}",
            query=query,
            body=body,
        )
        return Alert.from_dict(json)

    def get_subscriptions(self, request: GetSubscriptionsRequest) -> SubscriptionList:
        """Get an alert's subscriptions.

        Get the subscriptions for an alert. An alert subscription represents
        exactly one recipient being notified whenever the alert is triggered.
        The alert recipient is specified by either the `user` field or the
        `destination` field. The `user` field is ignored if `destination` is
        non-`null`."""
        query, body = request.as_request()
        json = self._api.do(
            "GET",
            f"/api/2.0/preview/sql/alerts/{request.alert_id}/subscriptions",
            query=query,
            body=body,
        )
        return SubscriptionList.from_dict(json)

    def list(self) -> AlertList:
        """Get alerts.

        Gets a list of alerts."""

        json = self._api.do("GET", "/api/2.0/preview/sql/alerts")
        return AlertList.from_dict(json)

    def list_schedules(self, request: ListSchedulesRequest) -> RefreshScheduleList:
        """Get refresh schedules.

        Gets the refresh schedules for the specified alert. Alerts can have
        refresh schedules that specify when to refresh and evaluate the
        associated query result.

        **Note:** Although refresh schedules are returned in a list, only one
        refresh schedule per alert is currently supported. The structure of
        refresh schedules is subject to change."""
        query, body = request.as_request()
        json = self._api.do(
            "GET",
            f"/api/2.0/preview/sql/alerts/{request.alert_id}/refresh-schedules",
            query=query,
            body=body,
        )
        return RefreshScheduleList.from_dict(json)

    def subscribe(self, request: CreateSubscription) -> Subscription:
        """Subscribe to an alert."""
        query, body = request.as_request()
        json = self._api.do(
            "POST",
            f"/api/2.0/preview/sql/alerts/{request.alert_id}/subscriptions",
            query=query,
            body=body,
        )
        return Subscription.from_dict(json)

    def unsubscribe(self, request: UnsubscribeRequest):
        """Unsubscribe to an alert.

        Unsubscribes a user or a destination to an alert."""
        query, body = request.as_request()
        self._api.do(
            "DELETE",
            f"/api/2.0/preview/sql/alerts/{request.alert_id}/subscriptions/{request.subscription_id}",
            query=query,
            body=body,
        )

    def update(self, request: EditAlert):
        """Update an alert.

        Updates an alert."""
        query, body = request.as_request()
        self._api.do(
            "PUT",
            f"/api/2.0/preview/sql/alerts/{request.alert_id}",
            query=query,
            body=body,
        )


class DashboardsAPI:
    def __init__(self, api_client):
        self._api = api_client

    def create(self, request: CreateDashboardRequest) -> Dashboard:
        """Create a dashboard object."""
        query, body = request.as_request()
        json = self._api.do(
            "POST", "/api/2.0/preview/sql/dashboards", query=query, body=body
        )
        return Dashboard.from_dict(json)

    def delete(self, request: DeleteDashboardRequest):
        """Remove a dashboard.

        Moves a dashboard to the trash. Trashed dashboards do not appear in list
        views or searches, and cannot be shared."""
        query, body = request.as_request()
        self._api.do(
            "DELETE",
            f"/api/2.0/preview/sql/dashboards/{request.dashboard_id}",
            query=query,
            body=body,
        )

    def get(self, request: GetDashboardRequest) -> Dashboard:
        """Retrieve a definition.

        Returns a JSON representation of a dashboard object, including its
        visualization and query objects."""
        query, body = request.as_request()
        json = self._api.do(
            "GET",
            f"/api/2.0/preview/sql/dashboards/{request.dashboard_id}",
            query=query,
            body=body,
        )
        return Dashboard.from_dict(json)

    def list(self, request: ListDashboardsRequest) -> ListResponse:
        """Get dashboard objects.

        Fetch a paginated list of dashboard objects."""
        query, body = request.as_request()
        json = self._api.do(
            "GET", "/api/2.0/preview/sql/dashboards", query=query, body=body
        )
        return ListResponse.from_dict(json)

    def restore(self, request: RestoreDashboardRequest):
        """Restore a dashboard.

        A restored dashboard appears in list views and searches and can be
        shared."""
        query, body = request.as_request()
        self._api.do(
            "POST",
            f"/api/2.0/preview/sql/dashboards/trash/{request.dashboard_id}",
            query=query,
            body=body,
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

    def get(self, request: GetDbsqlPermissionRequest) -> GetResponse:
        """Get object ACL.

        Gets a JSON representation of the access control list (ACL) for a
        specified object."""
        query, body = request.as_request()
        json = self._api.do(
            "GET",
            f"/api/2.0/preview/sql/permissions/{request.objectType}/{request.objectId}",
            query=query,
            body=body,
        )
        return GetResponse.from_dict(json)

    def set(self, request: SetRequest) -> SetResponse:
        """Set object ACL.

        Sets the access control list (ACL) for a specified object. This
        operation will complete rewrite the ACL."""
        query, body = request.as_request()
        json = self._api.do(
            "POST",
            f"/api/2.0/preview/sql/permissions/{request.objectType}/{request.objectId}",
            query=query,
            body=body,
        )
        return SetResponse.from_dict(json)

    def transfer_ownership(self, request: TransferOwnershipRequest) -> Success:
        """Transfer object ownership.

        Transfers ownership of a dashboard, query, or alert to an active user.
        Requires an admin API key."""
        query, body = request.as_request()
        json = self._api.do(
            "POST",
            f"/api/2.0/preview/sql/permissions/{request.objectType}/{request.objectId}/transfer",
            query=query,
            body=body,
        )
        return Success.from_dict(json)


class QueriesAPI:
    def __init__(self, api_client):
        self._api = api_client

    def create(self, request: QueryPostContent) -> Query:
        """Create a new query definition.

        Creates a new query definition. Queries created with this endpoint
        belong to the authenticated user making the request.

        The `data_source_id` field specifies the ID of the SQL warehouse to run
        this query against. You can use the Data Sources API to see a complete
        list of available SQL warehouses. Or you can copy the `data_source_id`
        from an existing query.

        **Note**: You cannot add a visualization until you create the query."""
        query, body = request.as_request()
        json = self._api.do(
            "POST", "/api/2.0/preview/sql/queries", query=query, body=body
        )
        return Query.from_dict(json)

    def delete(self, request: DeleteQueryRequest):
        """Delete a query.

        Moves a query to the trash. Trashed queries immediately disappear from
        searches and list views, and they cannot be used for alerts. The trash
        is deleted after 30 days."""
        query, body = request.as_request()
        self._api.do(
            "DELETE",
            f"/api/2.0/preview/sql/queries/{request.query_id}",
            query=query,
            body=body,
        )

    def get(self, request: GetQueryRequest) -> Query:
        """Get a query definition.

        Retrieve a query object definition along with contextual permissions
        information about the currently authenticated user."""
        query, body = request.as_request()
        json = self._api.do(
            "GET",
            f"/api/2.0/preview/sql/queries/{request.query_id}",
            query=query,
            body=body,
        )
        return Query.from_dict(json)

    def list(self, request: ListQueriesRequest) -> QueryList:
        """Get a list of queries.

        Gets a list of queries. Optionally, this list can be filtered by a
        search term."""
        query, body = request.as_request()
        json = self._api.do(
            "GET", "/api/2.0/preview/sql/queries", query=query, body=body
        )
        return QueryList.from_dict(json)

    def restore(self, request: RestoreQueryRequest):
        """Restore a query.

        Restore a query that has been moved to the trash. A restored query
        appears in list views and searches. You can use restored queries for
        alerts."""
        query, body = request.as_request()
        self._api.do(
            "POST",
            f"/api/2.0/preview/sql/queries/trash/{request.query_id}",
            query=query,
            body=body,
        )

    def update(self, request: QueryPostContent) -> Query:
        """Change a query definition.

        Modify this query definition.

        **Note**: You cannot undo this operation."""
        query, body = request.as_request()
        json = self._api.do(
            "POST",
            f"/api/2.0/preview/sql/queries/{request.query_id}",
            query=query,
            body=body,
        )
        return Query.from_dict(json)


class QueryHistoryAPI:
    def __init__(self, api_client):
        self._api = api_client

    def list(self, request: ListQueryHistoryRequest) -> ListQueriesResponse:
        """List Queries.

        List the history of queries through SQL warehouses.

        You can filter by user ID, warehouse ID, status, and time range."""
        query, body = request.as_request()
        json = self._api.do(
            "GET", "/api/2.0/sql/history/queries", query=query, body=body
        )
        return ListQueriesResponse.from_dict(json)


class WarehousesAPI:
    def __init__(self, api_client):
        self._api = api_client

    def create(self, request: CreateWarehouseRequest) -> CreateWarehouseResponse:
        """Create a warehouse.

        Creates a new SQL warehouse."""
        query, body = request.as_request()
        json = self._api.do("POST", "/api/2.0/sql/warehouses", query=query, body=body)
        return CreateWarehouseResponse.from_dict(json)

    def delete(self, request: DeleteWarehouseRequest):
        """Delete a warehouse.

        Deletes a SQL warehouse."""
        query, body = request.as_request()
        self._api.do(
            "DELETE", f"/api/2.0/sql/warehouses/{request.id}", query=query, body=body
        )

    def edit(self, request: EditWarehouseRequest):
        """Update a warehouse.

        Updates the configuration for a SQL warehouse."""
        query, body = request.as_request()
        self._api.do(
            "POST", f"/api/2.0/sql/warehouses/{request.id}/edit", query=query, body=body
        )

    def get(self, request: GetWarehouseRequest) -> GetWarehouseResponse:
        """Get warehouse info.

        Gets the information for a single SQL warehouse."""
        query, body = request.as_request()
        json = self._api.do(
            "GET", f"/api/2.0/sql/warehouses/{request.id}", query=query, body=body
        )
        return GetWarehouseResponse.from_dict(json)

    def get_workspace_warehouse_config(self) -> GetWorkspaceWarehouseConfigResponse:
        """Get the workspace configuration.

        Gets the workspace level configuration that is shared by all SQL
        warehouses in a workspace."""

        json = self._api.do("GET", "/api/2.0/sql/config/warehouses")
        return GetWorkspaceWarehouseConfigResponse.from_dict(json)

    def list(self, request: ListWarehousesRequest) -> ListWarehousesResponse:
        """List warehouses.

        Lists all SQL warehouses that a user has manager permissions on."""
        query, body = request.as_request()
        json = self._api.do("GET", "/api/2.0/sql/warehouses", query=query, body=body)
        return ListWarehousesResponse.from_dict(json)

    def set_workspace_warehouse_config(
        self, request: SetWorkspaceWarehouseConfigRequest
    ):
        """Set the workspace configuration.

        Sets the workspace level configuration that is shared by all SQL
        warehouses in a workspace."""
        query, body = request.as_request()
        self._api.do("PUT", "/api/2.0/sql/config/warehouses", query=query, body=body)

    def start(self, request: StartRequest):
        """Start a warehouse.

        Starts a SQL warehouse."""
        query, body = request.as_request()
        self._api.do(
            "POST",
            f"/api/2.0/sql/warehouses/{request.id}/start",
            query=query,
            body=body,
        )

    def stop(self, request: StopRequest):
        """Stop a warehouse.

        Stops a SQL warehouse."""
        query, body = request.as_request()
        self._api.do(
            "POST", f"/api/2.0/sql/warehouses/{request.id}/stop", query=query, body=body
        )
