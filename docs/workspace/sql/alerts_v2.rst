``w.alerts_v2``: Alerts V2
==========================
.. currentmodule:: databricks.sdk.service.sql

.. py:class:: AlertsV2API

    New version of SQL Alerts

    .. py:method:: create_alert(alert: AlertV2) -> AlertV2

        Creates an alert that runs ``query_text`` on the given schedule and evaluates the result against the
        configured condition.

        :param alert: :class:`AlertV2`

        :returns: :class:`AlertV2`
        

    .. py:method:: get_alert(id: str) -> AlertV2

        Gets an alert.

        :param id: str
          ID of the alert to retrieve, as returned in the alert's ``id`` field.

        :returns: :class:`AlertV2`
        

    .. py:method:: list_alerts( [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[AlertV2]

        Gets a list of alerts accessible to the user, ordered by creation time.

        :param page_size: int (optional)
          Maximum number of alerts to return per page. Values above 100 are coerced to 100.
        :param page_token: str (optional)
          Page token returned as ``next_page_token`` by a previous call. Omit it to retrieve the first page.

        :returns: Iterator over :class:`AlertV2`
        

    .. py:method:: trash_alert(id: str [, purge: Optional[bool]])

        Moves an alert to the trash. Trashed alerts immediately disappear from list views, and can no longer
        trigger. You can restore a trashed alert through the UI. A trashed alert is permanently deleted after
        30 days.

        :param id: str
          ID of the alert to move to the trash.
        :param purge: bool (optional)
          Whether to permanently delete the alert. If not set, the alert will only be soft deleted.


        

    .. py:method:: update_alert(id: str, alert: AlertV2, update_mask: str) -> AlertV2

        Updates an alert. Only the fields listed in ``update_mask`` are changed; all other fields keep their
        current values.

        :param id: str
          The canonical identifier of the alert to retrieve information about.
        :param alert: :class:`AlertV2`
        :param update_mask: str
          Comma-separated list of the alert fields to update, for example ``display_name,query_text`` or
          ``schedule.pause_status``. Only the listed fields are changed; all other fields keep their current
          values. ``parent_path`` cannot be updated.

        :returns: :class:`AlertV2`
        