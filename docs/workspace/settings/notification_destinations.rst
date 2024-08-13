``w.notification_destinations``: Notification Destinations
==========================================================
.. currentmodule:: databricks.sdk.service.settings

.. py:class:: NotificationDestinationsAPI

    The notification destinations API lets you programmatically manage a workspace's notification
    destinations. Notification destinations are used to send notifications for query alerts and jobs to
    destinations outside of Databricks. Only workspace admins can create, update, and delete notification
    destinations.

    .. py:method:: create( [, config: Optional[Config], display_name: Optional[str]]) -> NotificationDestination

        Create a notification destination.
        
        Creates a notification destination. Requires workspace admin permissions.
        
        :param config: :class:`Config` (optional)
          The configuration for the notification destination. Must wrap EXACTLY one of the nested configs.
        :param display_name: str (optional)
          The display name for the notification destination.
        
        :returns: :class:`NotificationDestination`
        

    .. py:method:: delete(id: str)

        Delete a notification destination.
        
        Deletes a notification destination. Requires workspace admin permissions.
        
        :param id: str
        
        
        

    .. py:method:: get(id: str) -> NotificationDestination

        Get a notification destination.
        
        Gets a notification destination.
        
        :param id: str
        
        :returns: :class:`NotificationDestination`
        

    .. py:method:: list( [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[ListNotificationDestinationsResult]

        List notification destinations.
        
        Lists notification destinations.
        
        :param page_size: int (optional)
        :param page_token: str (optional)
        
        :returns: Iterator over :class:`ListNotificationDestinationsResult`
        

    .. py:method:: update(id: str [, config: Optional[Config], display_name: Optional[str]]) -> NotificationDestination

        Update a notification destination.
        
        Updates a notification destination. Requires workspace admin permissions. At least one field is
        required in the request body.
        
        :param id: str
        :param config: :class:`Config` (optional)
          The configuration for the notification destination. Must wrap EXACTLY one of the nested configs.
        :param display_name: str (optional)
          The display name for the notification destination.
        
        :returns: :class:`NotificationDestination`
        