``a.o_auth_published_apps``: OAuth Published App
================================================
.. currentmodule:: databricks.sdk.service.oauth2

.. py:class:: OAuthPublishedAppsAPI

    These APIs enable administrators to view all the available published OAuth applications in Databricks.
    Administrators can add the published OAuth applications to their account through the OAuth Published App
    Integration APIs.

    .. py:method:: list( [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[PublishedAppOutput]

        Get all the published OAuth apps.
        
        Get all the available published OAuth apps in Databricks.
        
        :param page_size: int (optional)
          The max number of OAuth published apps to return in one page.
        :param page_token: str (optional)
          A token that can be used to get the next page of results.
        
        :returns: Iterator over :class:`PublishedAppOutput`
        