# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

from __future__ import annotations

import logging
from dataclasses import dataclass
from enum import Enum
from typing import Dict, Iterator, List, Optional

from ._internal import _enum, _from_dict, _repeated_dict

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
class CreateScheduleRequest:
    cron_schedule: CronSchedule
    """The cron expression describing the frequency of the periodic refresh for this schedule."""

    dashboard_id: Optional[str] = None
    """UUID identifying the dashboard to which the schedule belongs."""

    display_name: Optional[str] = None
    """The display name for schedule."""

    pause_status: Optional[SchedulePauseStatus] = None
    """The status indicates whether this schedule is paused or not."""

    def as_dict(self) -> dict:
        """Serializes the CreateScheduleRequest into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.cron_schedule: body['cron_schedule'] = self.cron_schedule.as_dict()
        if self.dashboard_id is not None: body['dashboard_id'] = self.dashboard_id
        if self.display_name is not None: body['display_name'] = self.display_name
        if self.pause_status is not None: body['pause_status'] = self.pause_status.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> CreateScheduleRequest:
        """Deserializes the CreateScheduleRequest from a dictionary."""
        return cls(cron_schedule=_from_dict(d, 'cron_schedule', CronSchedule),
                   dashboard_id=d.get('dashboard_id', None),
                   display_name=d.get('display_name', None),
                   pause_status=_enum(d, 'pause_status', SchedulePauseStatus))


@dataclass
class CreateSubscriptionRequest:
    subscriber: Subscriber
    """Subscriber details for users and destinations to be added as subscribers to the schedule."""

    dashboard_id: Optional[str] = None
    """UUID identifying the dashboard to which the subscription belongs."""

    schedule_id: Optional[str] = None
    """UUID identifying the schedule to which the subscription belongs."""

    def as_dict(self) -> dict:
        """Serializes the CreateSubscriptionRequest into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.dashboard_id is not None: body['dashboard_id'] = self.dashboard_id
        if self.schedule_id is not None: body['schedule_id'] = self.schedule_id
        if self.subscriber: body['subscriber'] = self.subscriber.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> CreateSubscriptionRequest:
        """Deserializes the CreateSubscriptionRequest from a dictionary."""
        return cls(dashboard_id=d.get('dashboard_id', None),
                   schedule_id=d.get('schedule_id', None),
                   subscriber=_from_dict(d, 'subscriber', Subscriber))


@dataclass
class CronSchedule:
    quartz_cron_expression: str
    """A cron expression using quartz syntax. EX: `0 0 8 * * ?` represents everyday at 8am. See [Cron
    Trigger] for details.
    
    [Cron Trigger]: http://www.quartz-scheduler.org/documentation/quartz-2.3.0/tutorials/crontrigger.html"""

    timezone_id: str
    """A Java timezone id. The schedule will be resolved with respect to this timezone. See [Java
    TimeZone] for details.
    
    [Java TimeZone]: https://docs.oracle.com/javase/7/docs/api/java/util/TimeZone.html"""

    def as_dict(self) -> dict:
        """Serializes the CronSchedule into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.quartz_cron_expression is not None:
            body['quartz_cron_expression'] = self.quartz_cron_expression
        if self.timezone_id is not None: body['timezone_id'] = self.timezone_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> CronSchedule:
        """Deserializes the CronSchedule from a dictionary."""
        return cls(quartz_cron_expression=d.get('quartz_cron_expression', None),
                   timezone_id=d.get('timezone_id', None))


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


class DashboardView(Enum):

    DASHBOARD_VIEW_BASIC = 'DASHBOARD_VIEW_BASIC'
    DASHBOARD_VIEW_FULL = 'DASHBOARD_VIEW_FULL'


@dataclass
class DeleteScheduleResponse:

    def as_dict(self) -> dict:
        """Serializes the DeleteScheduleResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> DeleteScheduleResponse:
        """Deserializes the DeleteScheduleResponse from a dictionary."""
        return cls()


@dataclass
class DeleteSubscriptionResponse:

    def as_dict(self) -> dict:
        """Serializes the DeleteSubscriptionResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> DeleteSubscriptionResponse:
        """Deserializes the DeleteSubscriptionResponse from a dictionary."""
        return cls()


class LifecycleState(Enum):

    ACTIVE = 'ACTIVE'
    TRASHED = 'TRASHED'


@dataclass
class ListDashboardsResponse:
    dashboards: Optional[List[Dashboard]] = None

    next_page_token: Optional[str] = None
    """A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted,
    there are no subsequent dashboards."""

    def as_dict(self) -> dict:
        """Serializes the ListDashboardsResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.dashboards: body['dashboards'] = [v.as_dict() for v in self.dashboards]
        if self.next_page_token is not None: body['next_page_token'] = self.next_page_token
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ListDashboardsResponse:
        """Deserializes the ListDashboardsResponse from a dictionary."""
        return cls(dashboards=_repeated_dict(d, 'dashboards', Dashboard),
                   next_page_token=d.get('next_page_token', None))


@dataclass
class ListSchedulesResponse:
    next_page_token: Optional[str] = None
    """A token that can be used as a `page_token` in subsequent requests to retrieve the next page of
    results. If this field is omitted, there are no subsequent schedules."""

    schedules: Optional[List[Schedule]] = None

    def as_dict(self) -> dict:
        """Serializes the ListSchedulesResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.next_page_token is not None: body['next_page_token'] = self.next_page_token
        if self.schedules: body['schedules'] = [v.as_dict() for v in self.schedules]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ListSchedulesResponse:
        """Deserializes the ListSchedulesResponse from a dictionary."""
        return cls(next_page_token=d.get('next_page_token', None),
                   schedules=_repeated_dict(d, 'schedules', Schedule))


@dataclass
class ListSubscriptionsResponse:
    next_page_token: Optional[str] = None
    """A token that can be used as a `page_token` in subsequent requests to retrieve the next page of
    results. If this field is omitted, there are no subsequent subscriptions."""

    subscriptions: Optional[List[Subscription]] = None

    def as_dict(self) -> dict:
        """Serializes the ListSubscriptionsResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.next_page_token is not None: body['next_page_token'] = self.next_page_token
        if self.subscriptions: body['subscriptions'] = [v.as_dict() for v in self.subscriptions]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ListSubscriptionsResponse:
        """Deserializes the ListSubscriptionsResponse from a dictionary."""
        return cls(next_page_token=d.get('next_page_token', None),
                   subscriptions=_repeated_dict(d, 'subscriptions', Subscription))


@dataclass
class MigrateDashboardRequest:
    source_dashboard_id: str
    """UUID of the dashboard to be migrated."""

    display_name: Optional[str] = None
    """Display name for the new Lakeview dashboard."""

    parent_path: Optional[str] = None
    """The workspace path of the folder to contain the migrated Lakeview dashboard."""

    def as_dict(self) -> dict:
        """Serializes the MigrateDashboardRequest into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.display_name is not None: body['display_name'] = self.display_name
        if self.parent_path is not None: body['parent_path'] = self.parent_path
        if self.source_dashboard_id is not None: body['source_dashboard_id'] = self.source_dashboard_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> MigrateDashboardRequest:
        """Deserializes the MigrateDashboardRequest from a dictionary."""
        return cls(display_name=d.get('display_name', None),
                   parent_path=d.get('parent_path', None),
                   source_dashboard_id=d.get('source_dashboard_id', None))


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
class Schedule:
    cron_schedule: CronSchedule
    """The cron expression describing the frequency of the periodic refresh for this schedule."""

    create_time: Optional[str] = None
    """A timestamp indicating when the schedule was created."""

    dashboard_id: Optional[str] = None
    """UUID identifying the dashboard to which the schedule belongs."""

    display_name: Optional[str] = None
    """The display name for schedule."""

    etag: Optional[str] = None
    """The etag for the schedule. Must be left empty on create, must be provided on updates to ensure
    that the schedule has not been modified since the last read, and can be optionally provided on
    delete."""

    pause_status: Optional[SchedulePauseStatus] = None
    """The status indicates whether this schedule is paused or not."""

    schedule_id: Optional[str] = None
    """UUID identifying the schedule."""

    update_time: Optional[str] = None
    """A timestamp indicating when the schedule was last updated."""

    def as_dict(self) -> dict:
        """Serializes the Schedule into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.create_time is not None: body['create_time'] = self.create_time
        if self.cron_schedule: body['cron_schedule'] = self.cron_schedule.as_dict()
        if self.dashboard_id is not None: body['dashboard_id'] = self.dashboard_id
        if self.display_name is not None: body['display_name'] = self.display_name
        if self.etag is not None: body['etag'] = self.etag
        if self.pause_status is not None: body['pause_status'] = self.pause_status.value
        if self.schedule_id is not None: body['schedule_id'] = self.schedule_id
        if self.update_time is not None: body['update_time'] = self.update_time
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> Schedule:
        """Deserializes the Schedule from a dictionary."""
        return cls(create_time=d.get('create_time', None),
                   cron_schedule=_from_dict(d, 'cron_schedule', CronSchedule),
                   dashboard_id=d.get('dashboard_id', None),
                   display_name=d.get('display_name', None),
                   etag=d.get('etag', None),
                   pause_status=_enum(d, 'pause_status', SchedulePauseStatus),
                   schedule_id=d.get('schedule_id', None),
                   update_time=d.get('update_time', None))


class SchedulePauseStatus(Enum):

    PAUSED = 'PAUSED'
    UNPAUSED = 'UNPAUSED'


@dataclass
class Subscriber:
    destination_subscriber: Optional[SubscriptionSubscriberDestination] = None
    """The destination to receive the subscription email. This parameter is mutually exclusive with
    `user_subscriber`."""

    user_subscriber: Optional[SubscriptionSubscriberUser] = None
    """The user to receive the subscription email. This parameter is mutually exclusive with
    `destination_subscriber`."""

    def as_dict(self) -> dict:
        """Serializes the Subscriber into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.destination_subscriber: body['destination_subscriber'] = self.destination_subscriber.as_dict()
        if self.user_subscriber: body['user_subscriber'] = self.user_subscriber.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> Subscriber:
        """Deserializes the Subscriber from a dictionary."""
        return cls(destination_subscriber=_from_dict(d, 'destination_subscriber',
                                                     SubscriptionSubscriberDestination),
                   user_subscriber=_from_dict(d, 'user_subscriber', SubscriptionSubscriberUser))


@dataclass
class Subscription:
    subscriber: Subscriber
    """Subscriber details for users and destinations to be added as subscribers to the schedule."""

    create_time: Optional[str] = None
    """A timestamp indicating when the subscription was created."""

    created_by_user_id: Optional[int] = None
    """UserId of the user who adds subscribers (users or notification destinations) to the dashboard's
    schedule."""

    dashboard_id: Optional[str] = None
    """UUID identifying the dashboard to which the subscription belongs."""

    etag: Optional[str] = None
    """The etag for the subscription. Must be left empty on create, can be optionally provided on
    delete to ensure that the subscription has not been deleted since the last read."""

    schedule_id: Optional[str] = None
    """UUID identifying the schedule to which the subscription belongs."""

    subscription_id: Optional[str] = None
    """UUID identifying the subscription."""

    update_time: Optional[str] = None
    """A timestamp indicating when the subscription was last updated."""

    def as_dict(self) -> dict:
        """Serializes the Subscription into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.create_time is not None: body['create_time'] = self.create_time
        if self.created_by_user_id is not None: body['created_by_user_id'] = self.created_by_user_id
        if self.dashboard_id is not None: body['dashboard_id'] = self.dashboard_id
        if self.etag is not None: body['etag'] = self.etag
        if self.schedule_id is not None: body['schedule_id'] = self.schedule_id
        if self.subscriber: body['subscriber'] = self.subscriber.as_dict()
        if self.subscription_id is not None: body['subscription_id'] = self.subscription_id
        if self.update_time is not None: body['update_time'] = self.update_time
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> Subscription:
        """Deserializes the Subscription from a dictionary."""
        return cls(create_time=d.get('create_time', None),
                   created_by_user_id=d.get('created_by_user_id', None),
                   dashboard_id=d.get('dashboard_id', None),
                   etag=d.get('etag', None),
                   schedule_id=d.get('schedule_id', None),
                   subscriber=_from_dict(d, 'subscriber', Subscriber),
                   subscription_id=d.get('subscription_id', None),
                   update_time=d.get('update_time', None))


@dataclass
class SubscriptionSubscriberDestination:
    destination_id: str
    """The canonical identifier of the destination to receive email notification."""

    def as_dict(self) -> dict:
        """Serializes the SubscriptionSubscriberDestination into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.destination_id is not None: body['destination_id'] = self.destination_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> SubscriptionSubscriberDestination:
        """Deserializes the SubscriptionSubscriberDestination from a dictionary."""
        return cls(destination_id=d.get('destination_id', None))


@dataclass
class SubscriptionSubscriberUser:
    user_id: int
    """UserId of the subscriber."""

    def as_dict(self) -> dict:
        """Serializes the SubscriptionSubscriberUser into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.user_id is not None: body['user_id'] = self.user_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> SubscriptionSubscriberUser:
        """Deserializes the SubscriptionSubscriberUser from a dictionary."""
        return cls(user_id=d.get('user_id', None))


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
class UnpublishDashboardResponse:

    def as_dict(self) -> dict:
        """Serializes the UnpublishDashboardResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> UnpublishDashboardResponse:
        """Deserializes the UnpublishDashboardResponse from a dictionary."""
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


@dataclass
class UpdateScheduleRequest:
    cron_schedule: CronSchedule
    """The cron expression describing the frequency of the periodic refresh for this schedule."""

    dashboard_id: Optional[str] = None
    """UUID identifying the dashboard to which the schedule belongs."""

    display_name: Optional[str] = None
    """The display name for schedule."""

    etag: Optional[str] = None
    """The etag for the schedule. Must be left empty on create, must be provided on updates to ensure
    that the schedule has not been modified since the last read, and can be optionally provided on
    delete."""

    pause_status: Optional[SchedulePauseStatus] = None
    """The status indicates whether this schedule is paused or not."""

    schedule_id: Optional[str] = None
    """UUID identifying the schedule."""

    def as_dict(self) -> dict:
        """Serializes the UpdateScheduleRequest into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.cron_schedule: body['cron_schedule'] = self.cron_schedule.as_dict()
        if self.dashboard_id is not None: body['dashboard_id'] = self.dashboard_id
        if self.display_name is not None: body['display_name'] = self.display_name
        if self.etag is not None: body['etag'] = self.etag
        if self.pause_status is not None: body['pause_status'] = self.pause_status.value
        if self.schedule_id is not None: body['schedule_id'] = self.schedule_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> UpdateScheduleRequest:
        """Deserializes the UpdateScheduleRequest from a dictionary."""
        return cls(cron_schedule=_from_dict(d, 'cron_schedule', CronSchedule),
                   dashboard_id=d.get('dashboard_id', None),
                   display_name=d.get('display_name', None),
                   etag=d.get('etag', None),
                   pause_status=_enum(d, 'pause_status', SchedulePauseStatus),
                   schedule_id=d.get('schedule_id', None))


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

    def create_schedule(self,
                        dashboard_id: str,
                        cron_schedule: CronSchedule,
                        *,
                        display_name: Optional[str] = None,
                        pause_status: Optional[SchedulePauseStatus] = None) -> Schedule:
        """Create dashboard schedule.
        
        :param dashboard_id: str
          UUID identifying the dashboard to which the schedule belongs.
        :param cron_schedule: :class:`CronSchedule`
          The cron expression describing the frequency of the periodic refresh for this schedule.
        :param display_name: str (optional)
          The display name for schedule.
        :param pause_status: :class:`SchedulePauseStatus` (optional)
          The status indicates whether this schedule is paused or not.
        
        :returns: :class:`Schedule`
        """
        body = {}
        if cron_schedule is not None: body['cron_schedule'] = cron_schedule.as_dict()
        if display_name is not None: body['display_name'] = display_name
        if pause_status is not None: body['pause_status'] = pause_status.value
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        res = self._api.do('POST',
                           f'/api/2.0/lakeview/dashboards/{dashboard_id}/schedules',
                           body=body,
                           headers=headers)
        return Schedule.from_dict(res)

    def create_subscription(self, dashboard_id: str, schedule_id: str,
                            subscriber: Subscriber) -> Subscription:
        """Create schedule subscription.
        
        :param dashboard_id: str
          UUID identifying the dashboard to which the subscription belongs.
        :param schedule_id: str
          UUID identifying the schedule to which the subscription belongs.
        :param subscriber: :class:`Subscriber`
          Subscriber details for users and destinations to be added as subscribers to the schedule.
        
        :returns: :class:`Subscription`
        """
        body = {}
        if subscriber is not None: body['subscriber'] = subscriber.as_dict()
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        res = self._api.do(
            'POST',
            f'/api/2.0/lakeview/dashboards/{dashboard_id}/schedules/{schedule_id}/subscriptions',
            body=body,
            headers=headers)
        return Subscription.from_dict(res)

    def delete_schedule(self, dashboard_id: str, schedule_id: str, *, etag: Optional[str] = None):
        """Delete dashboard schedule.
        
        :param dashboard_id: str
          UUID identifying the dashboard to which the schedule belongs.
        :param schedule_id: str
          UUID identifying the schedule.
        :param etag: str (optional)
          The etag for the schedule. Optionally, it can be provided to verify that the schedule has not been
          modified from its last retrieval.
        
        
        """

        query = {}
        if etag is not None: query['etag'] = etag
        headers = {'Accept': 'application/json', }

        self._api.do('DELETE',
                     f'/api/2.0/lakeview/dashboards/{dashboard_id}/schedules/{schedule_id}',
                     query=query,
                     headers=headers)

    def delete_subscription(self,
                            dashboard_id: str,
                            schedule_id: str,
                            subscription_id: str,
                            *,
                            etag: Optional[str] = None):
        """Delete schedule subscription.
        
        :param dashboard_id: str
          UUID identifying the dashboard which the subscription belongs.
        :param schedule_id: str
          UUID identifying the schedule which the subscription belongs.
        :param subscription_id: str
          UUID identifying the subscription.
        :param etag: str (optional)
          The etag for the subscription. Can be optionally provided to ensure that the subscription has not
          been modified since the last read.
        
        
        """

        query = {}
        if etag is not None: query['etag'] = etag
        headers = {'Accept': 'application/json', }

        self._api.do(
            'DELETE',
            f'/api/2.0/lakeview/dashboards/{dashboard_id}/schedules/{schedule_id}/subscriptions/{subscription_id}',
            query=query,
            headers=headers)

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

    def get_schedule(self, dashboard_id: str, schedule_id: str) -> Schedule:
        """Get dashboard schedule.
        
        :param dashboard_id: str
          UUID identifying the dashboard to which the schedule belongs.
        :param schedule_id: str
          UUID identifying the schedule.
        
        :returns: :class:`Schedule`
        """

        headers = {'Accept': 'application/json', }

        res = self._api.do('GET',
                           f'/api/2.0/lakeview/dashboards/{dashboard_id}/schedules/{schedule_id}',
                           headers=headers)
        return Schedule.from_dict(res)

    def get_subscription(self, dashboard_id: str, schedule_id: str, subscription_id: str) -> Subscription:
        """Get schedule subscription.
        
        :param dashboard_id: str
          UUID identifying the dashboard which the subscription belongs.
        :param schedule_id: str
          UUID identifying the schedule which the subscription belongs.
        :param subscription_id: str
          UUID identifying the subscription.
        
        :returns: :class:`Subscription`
        """

        headers = {'Accept': 'application/json', }

        res = self._api.do(
            'GET',
            f'/api/2.0/lakeview/dashboards/{dashboard_id}/schedules/{schedule_id}/subscriptions/{subscription_id}',
            headers=headers)
        return Subscription.from_dict(res)

    def list(self,
             *,
             page_size: Optional[int] = None,
             page_token: Optional[str] = None,
             show_trashed: Optional[bool] = None,
             view: Optional[DashboardView] = None) -> Iterator[Dashboard]:
        """List dashboards.
        
        :param page_size: int (optional)
          The number of dashboards to return per page.
        :param page_token: str (optional)
          A page token, received from a previous `ListDashboards` call. This token can be used to retrieve the
          subsequent page.
        :param show_trashed: bool (optional)
          The flag to include dashboards located in the trash. If unspecified, only active dashboards will be
          returned.
        :param view: :class:`DashboardView` (optional)
          Indicates whether to include all metadata from the dashboard in the response. If unset, the response
          defaults to `DASHBOARD_VIEW_BASIC` which only includes summary metadata from the dashboard.
        
        :returns: Iterator over :class:`Dashboard`
        """

        query = {}
        if page_size is not None: query['page_size'] = page_size
        if page_token is not None: query['page_token'] = page_token
        if show_trashed is not None: query['show_trashed'] = show_trashed
        if view is not None: query['view'] = view.value
        headers = {'Accept': 'application/json', }

        while True:
            json = self._api.do('GET', '/api/2.0/lakeview/dashboards', query=query, headers=headers)
            if 'dashboards' in json:
                for v in json['dashboards']:
                    yield Dashboard.from_dict(v)
            if 'next_page_token' not in json or not json['next_page_token']:
                return
            query['page_token'] = json['next_page_token']

    def list_schedules(self,
                       dashboard_id: str,
                       *,
                       page_size: Optional[int] = None,
                       page_token: Optional[str] = None) -> Iterator[Schedule]:
        """List dashboard schedules.
        
        :param dashboard_id: str
          UUID identifying the dashboard to which the schedule belongs.
        :param page_size: int (optional)
          The number of schedules to return per page.
        :param page_token: str (optional)
          A page token, received from a previous `ListSchedules` call. Use this to retrieve the subsequent
          page.
        
        :returns: Iterator over :class:`Schedule`
        """

        query = {}
        if page_size is not None: query['page_size'] = page_size
        if page_token is not None: query['page_token'] = page_token
        headers = {'Accept': 'application/json', }

        while True:
            json = self._api.do('GET',
                                f'/api/2.0/lakeview/dashboards/{dashboard_id}/schedules',
                                query=query,
                                headers=headers)
            if 'schedules' in json:
                for v in json['schedules']:
                    yield Schedule.from_dict(v)
            if 'next_page_token' not in json or not json['next_page_token']:
                return
            query['page_token'] = json['next_page_token']

    def list_subscriptions(self,
                           dashboard_id: str,
                           schedule_id: str,
                           *,
                           page_size: Optional[int] = None,
                           page_token: Optional[str] = None) -> Iterator[Subscription]:
        """List schedule subscriptions.
        
        :param dashboard_id: str
          UUID identifying the dashboard to which the subscription belongs.
        :param schedule_id: str
          UUID identifying the schedule to which the subscription belongs.
        :param page_size: int (optional)
          The number of subscriptions to return per page.
        :param page_token: str (optional)
          A page token, received from a previous `ListSubscriptions` call. Use this to retrieve the subsequent
          page.
        
        :returns: Iterator over :class:`Subscription`
        """

        query = {}
        if page_size is not None: query['page_size'] = page_size
        if page_token is not None: query['page_token'] = page_token
        headers = {'Accept': 'application/json', }

        while True:
            json = self._api.do(
                'GET',
                f'/api/2.0/lakeview/dashboards/{dashboard_id}/schedules/{schedule_id}/subscriptions',
                query=query,
                headers=headers)
            if 'subscriptions' in json:
                for v in json['subscriptions']:
                    yield Subscription.from_dict(v)
            if 'next_page_token' not in json or not json['next_page_token']:
                return
            query['page_token'] = json['next_page_token']

    def migrate(self,
                source_dashboard_id: str,
                *,
                display_name: Optional[str] = None,
                parent_path: Optional[str] = None) -> Dashboard:
        """Migrate dashboard.
        
        Migrates a classic SQL dashboard to Lakeview.
        
        :param source_dashboard_id: str
          UUID of the dashboard to be migrated.
        :param display_name: str (optional)
          Display name for the new Lakeview dashboard.
        :param parent_path: str (optional)
          The workspace path of the folder to contain the migrated Lakeview dashboard.
        
        :returns: :class:`Dashboard`
        """
        body = {}
        if display_name is not None: body['display_name'] = display_name
        if parent_path is not None: body['parent_path'] = parent_path
        if source_dashboard_id is not None: body['source_dashboard_id'] = source_dashboard_id
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        res = self._api.do('POST', '/api/2.0/lakeview/dashboards/migrate', body=body, headers=headers)
        return Dashboard.from_dict(res)

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

    def unpublish(self, dashboard_id: str):
        """Unpublish dashboard.
        
        Unpublish the dashboard.
        
        :param dashboard_id: str
          UUID identifying the dashboard to be published.
        
        
        """

        headers = {'Accept': 'application/json', }

        self._api.do('DELETE', f'/api/2.0/lakeview/dashboards/{dashboard_id}/published', headers=headers)

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

    def update_schedule(self,
                        dashboard_id: str,
                        schedule_id: str,
                        cron_schedule: CronSchedule,
                        *,
                        display_name: Optional[str] = None,
                        etag: Optional[str] = None,
                        pause_status: Optional[SchedulePauseStatus] = None) -> Schedule:
        """Update dashboard schedule.
        
        :param dashboard_id: str
          UUID identifying the dashboard to which the schedule belongs.
        :param schedule_id: str
          UUID identifying the schedule.
        :param cron_schedule: :class:`CronSchedule`
          The cron expression describing the frequency of the periodic refresh for this schedule.
        :param display_name: str (optional)
          The display name for schedule.
        :param etag: str (optional)
          The etag for the schedule. Must be left empty on create, must be provided on updates to ensure that
          the schedule has not been modified since the last read, and can be optionally provided on delete.
        :param pause_status: :class:`SchedulePauseStatus` (optional)
          The status indicates whether this schedule is paused or not.
        
        :returns: :class:`Schedule`
        """
        body = {}
        if cron_schedule is not None: body['cron_schedule'] = cron_schedule.as_dict()
        if display_name is not None: body['display_name'] = display_name
        if etag is not None: body['etag'] = etag
        if pause_status is not None: body['pause_status'] = pause_status.value
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        res = self._api.do('PUT',
                           f'/api/2.0/lakeview/dashboards/{dashboard_id}/schedules/{schedule_id}',
                           body=body,
                           headers=headers)
        return Schedule.from_dict(res)
