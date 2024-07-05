``w.lakeview``: Lakeview
========================
.. currentmodule:: databricks.sdk.service.dashboards

.. py:class:: LakeviewAPI

    These APIs provide specific management operations for Lakeview dashboards. Generic resource management can
    be done with Workspace API (import, export, get-status, list, delete).

    .. py:method:: create(display_name: str [, parent_path: Optional[str], serialized_dashboard: Optional[str], warehouse_id: Optional[str]]) -> Dashboard

        Create dashboard.
        
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
        

    .. py:method:: create_schedule(dashboard_id: str, cron_schedule: CronSchedule [, display_name: Optional[str], pause_status: Optional[SchedulePauseStatus]]) -> Schedule

        Create dashboard schedule.
        
        :param dashboard_id: str
          UUID identifying the dashboard to which the schedule belongs.
        :param cron_schedule: :class:`CronSchedule`
          The cron expression describing the frequency of the periodic refresh for this schedule.
        :param display_name: str (optional)
          The display name for schedule.
        :param pause_status: :class:`SchedulePauseStatus` (optional)
          The status indicates whether this schedule is paused or not.
        
        :returns: :class:`Schedule`
        

    .. py:method:: create_subscription(dashboard_id: str, schedule_id: str, subscriber: Subscriber) -> Subscription

        Create schedule subscription.
        
        :param dashboard_id: str
          UUID identifying the dashboard to which the subscription belongs.
        :param schedule_id: str
          UUID identifying the schedule to which the subscription belongs.
        :param subscriber: :class:`Subscriber`
          Subscriber details for users and destinations to be added as subscribers to the schedule.
        
        :returns: :class:`Subscription`
        

    .. py:method:: delete_schedule(dashboard_id: str, schedule_id: str [, etag: Optional[str]])

        Delete dashboard schedule.
        
        :param dashboard_id: str
          UUID identifying the dashboard to which the schedule belongs.
        :param schedule_id: str
          UUID identifying the schedule.
        :param etag: str (optional)
          The etag for the schedule. Optionally, it can be provided to verify that the schedule has not been
          modified from its last retrieval.
        
        
        

    .. py:method:: delete_subscription(dashboard_id: str, schedule_id: str, subscription_id: str [, etag: Optional[str]])

        Delete schedule subscription.
        
        :param dashboard_id: str
          UUID identifying the dashboard which the subscription belongs.
        :param schedule_id: str
          UUID identifying the schedule which the subscription belongs.
        :param subscription_id: str
          UUID identifying the subscription.
        :param etag: str (optional)
          The etag for the subscription. Can be optionally provided to ensure that the subscription has not
          been modified since the last read.
        
        
        

    .. py:method:: get(dashboard_id: str) -> Dashboard

        Get dashboard.
        
        Get a draft dashboard.
        
        :param dashboard_id: str
          UUID identifying the dashboard.
        
        :returns: :class:`Dashboard`
        

    .. py:method:: get_published(dashboard_id: str) -> PublishedDashboard

        Get published dashboard.
        
        Get the current published dashboard.
        
        :param dashboard_id: str
          UUID identifying the dashboard to be published.
        
        :returns: :class:`PublishedDashboard`
        

    .. py:method:: get_schedule(dashboard_id: str, schedule_id: str) -> Schedule

        Get dashboard schedule.
        
        :param dashboard_id: str
          UUID identifying the dashboard to which the schedule belongs.
        :param schedule_id: str
          UUID identifying the schedule.
        
        :returns: :class:`Schedule`
        

    .. py:method:: get_subscription(dashboard_id: str, schedule_id: str, subscription_id: str) -> Subscription

        Get schedule subscription.
        
        :param dashboard_id: str
          UUID identifying the dashboard which the subscription belongs.
        :param schedule_id: str
          UUID identifying the schedule which the subscription belongs.
        :param subscription_id: str
          UUID identifying the subscription.
        
        :returns: :class:`Subscription`
        

    .. py:method:: list( [, page_size: Optional[int], page_token: Optional[str], show_trashed: Optional[bool], view: Optional[DashboardView]]) -> Iterator[Dashboard]

        List dashboards.
        
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
        

    .. py:method:: list_schedules(dashboard_id: str [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[Schedule]

        List dashboard schedules.
        
        :param dashboard_id: str
          UUID identifying the dashboard to which the schedule belongs.
        :param page_size: int (optional)
          The number of schedules to return per page.
        :param page_token: str (optional)
          A page token, received from a previous `ListSchedules` call. Use this to retrieve the subsequent
          page.
        
        :returns: Iterator over :class:`Schedule`
        

    .. py:method:: list_subscriptions(dashboard_id: str, schedule_id: str [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[Subscription]

        List schedule subscriptions.
        
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
        

    .. py:method:: migrate(source_dashboard_id: str [, display_name: Optional[str], parent_path: Optional[str]]) -> Dashboard

        Migrate dashboard.
        
        Migrates a classic SQL dashboard to Lakeview.
        
        :param source_dashboard_id: str
          UUID of the dashboard to be migrated.
        :param display_name: str (optional)
          Display name for the new Lakeview dashboard.
        :param parent_path: str (optional)
          The workspace path of the folder to contain the migrated Lakeview dashboard.
        
        :returns: :class:`Dashboard`
        

    .. py:method:: publish(dashboard_id: str [, embed_credentials: Optional[bool], warehouse_id: Optional[str]]) -> PublishedDashboard

        Publish dashboard.
        
        Publish the current draft dashboard.
        
        :param dashboard_id: str
          UUID identifying the dashboard to be published.
        :param embed_credentials: bool (optional)
          Flag to indicate if the publisher's credentials should be embedded in the published dashboard. These
          embedded credentials will be used to execute the published dashboard's queries.
        :param warehouse_id: str (optional)
          The ID of the warehouse that can be used to override the warehouse which was set in the draft.
        
        :returns: :class:`PublishedDashboard`
        

    .. py:method:: trash(dashboard_id: str)

        Trash dashboard.
        
        Trash a dashboard.
        
        :param dashboard_id: str
          UUID identifying the dashboard.
        
        
        

    .. py:method:: unpublish(dashboard_id: str)

        Unpublish dashboard.
        
        Unpublish the dashboard.
        
        :param dashboard_id: str
          UUID identifying the dashboard to be published.
        
        
        

    .. py:method:: update(dashboard_id: str [, display_name: Optional[str], etag: Optional[str], serialized_dashboard: Optional[str], warehouse_id: Optional[str]]) -> Dashboard

        Update dashboard.
        
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
        

    .. py:method:: update_schedule(dashboard_id: str, schedule_id: str, cron_schedule: CronSchedule [, display_name: Optional[str], etag: Optional[str], pause_status: Optional[SchedulePauseStatus]]) -> Schedule

        Update dashboard schedule.
        
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
        