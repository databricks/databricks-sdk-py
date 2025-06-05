``a.billable_usage``: Billable usage download
=============================================
.. currentmodule:: databricks.sdk.service.billing

.. py:class:: BillableUsageAPI

    This API allows you to download billable usage logs for the specified account and date range. This feature
    works with all account types.

    .. py:method:: download(start_month: str, end_month: str [, personal_data: Optional[bool]]) -> DownloadResponse


        Usage:

        .. code-block::

            from databricks.sdk import AccountClient
            
            a = AccountClient()
            
            resp = a.billable_usage.download(start_month="2024-08", end_month="2024-09")

        Return billable usage logs.
        
        Returns billable usage logs in CSV format for the specified account and date range. For the data
        schema, see [CSV file schema]. Note that this method might take multiple minutes to complete.
        
        **Warning**: Depending on the queried date range, the number of workspaces in the account, the size of
        the response and the internet speed of the caller, this API may hit a timeout after a few minutes. If
        you experience this, try to mitigate by calling the API with narrower date ranges.
        
        [CSV file schema]: https://docs.databricks.com/administration-guide/account-settings/usage-analysis.html#schema
        
        :param start_month: str
          Format: `YYYY-MM`. First month to return billable usage logs for. This field is required.
        :param end_month: str
          Format: `YYYY-MM`. Last month to return billable usage logs for. This field is required.
        :param personal_data: bool (optional)
          Specify whether to include personally identifiable information in the billable usage logs, for
          example the email addresses of cluster creators. Handle this information with care. Defaults to
          false.
        
        :returns: :class:`DownloadResponse`
        