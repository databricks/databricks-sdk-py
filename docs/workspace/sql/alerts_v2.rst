``w.alerts_v2``: Alerts V2
==========================
.. currentmodule:: databricks.sdk.service.sql

.. py:class:: AlertsV2API

    New version of SQL Alerts

    .. py:method:: create_alert(alert: AlertV2) -> AlertV2

        Create Alert

        :param alert: :class:`AlertV2`

        :returns: :class:`AlertV2`
        

    .. py:method:: get_alert(id: str) -> AlertV2

        Gets an alert.

        :param id: str

        :returns: :class:`AlertV2`
        

    .. py:method:: list_alerts( [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[AlertV2]

        Gets a list of alerts accessible to the user, ordered by creation time.

        :param page_size: int (optional)
        :param page_token: str (optional)

        :returns: Iterator over :class:`AlertV2`
        

    .. py:method:: trash_alert(id: str)

        Moves an alert to the trash. Trashed alerts immediately disappear from list views, and can no longer
        trigger. You can restore a trashed alert through the UI. A trashed alert is permanently deleted after
        30 days.

        :param id: str


        

    .. py:method:: update_alert(id: str, alert: AlertV2, update_mask: str) -> AlertV2

        Update alert

        :param id: str
          UUID identifying the alert.
        :param alert: :class:`AlertV2`
        :param update_mask: str
          The field mask must be a single string, with multiple fields separated by commas (no spaces). The
          field path is relative to the resource object, using a dot (`.`) to navigate sub-fields (e.g.,
          `author.given_name`). Specification of elements in sequence or map fields is not allowed, as only
          the entire collection field can be specified. Field names must exactly match the resource field
          names.

          A field mask of `*` indicates full replacement. It’s recommended to always explicitly list the
          fields being updated and avoid using `*` wildcards, as it can lead to unintended results if the API
          changes in the future.

        :returns: :class:`AlertV2`
        