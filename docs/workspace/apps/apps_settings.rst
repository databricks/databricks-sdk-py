``w.apps_settings``: Apps Settings
==================================
.. currentmodule:: databricks.sdk.service.apps

.. py:class:: AppsSettingsAPI

    Apps Settings manage the settings for the Apps service on a customer's Databricks instance.

    .. py:method:: create_custom_template(template: CustomTemplate) -> CustomTemplate

        Creates a custom template.

        :param template: :class:`CustomTemplate`

        :returns: :class:`CustomTemplate`
        

    .. py:method:: delete_custom_template(name: str) -> CustomTemplate

        Deletes the custom template with the specified name.

        :param name: str
          The name of the custom template.

        :returns: :class:`CustomTemplate`
        

    .. py:method:: get_custom_template(name: str) -> CustomTemplate

        Gets the custom template with the specified name.

        :param name: str
          The name of the custom template.

        :returns: :class:`CustomTemplate`
        

    .. py:method:: list_custom_templates( [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[CustomTemplate]

        Lists all custom templates in the workspace.

        :param page_size: int (optional)
          Upper bound for items returned.
        :param page_token: str (optional)
          Pagination token to go to the next page of custom templates. Requests first page if absent.

        :returns: Iterator over :class:`CustomTemplate`
        

    .. py:method:: update_custom_template(name: str, template: CustomTemplate) -> CustomTemplate

        Updates the custom template with the specified name. Note that the template name cannot be updated.

        :param name: str
          The name of the template. It must contain only alphanumeric characters, hyphens, underscores, and
          whitespaces. It must be unique within the workspace.
        :param template: :class:`CustomTemplate`

        :returns: :class:`CustomTemplate`
        