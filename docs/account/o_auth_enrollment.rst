OAuth Enrollment
================
.. py:class:: OAuthEnrollmentAPI

    These APIs enable administrators to enroll OAuth for their accounts, which is required for adding/using
    any OAuth published/custom application integration.
    
    **Note:** Your account must be on the E2 version to use these APIs, this is because OAuth is only
    supported on the E2 version.

    .. py:method:: create( [, enable_all_published_apps])

        Create OAuth Enrollment request.
        
        Create an OAuth Enrollment request to enroll OAuth for this account and optionally enable the OAuth
        integration for all the partner applications in the account.
        
        The parter applications are: - Power BI - Tableau Desktop - Databricks CLI
        
        The enrollment is executed asynchronously, so the API will return 204 immediately. The actual
        enrollment take a few minutes, you can check the status via API :method:OAuthEnrollment/get.
        
        :param enable_all_published_apps: bool (optional)
          If true, enable OAuth for all the published applications in the account.
        
        
        

    .. py:method:: get()

        Get OAuth enrollment status.
        
        Gets the OAuth enrollment status for this Account.
        
        You can only add/use the OAuth published/custom application integrations when OAuth enrollment status
        is enabled.
        
        :returns: :class:`OAuthEnrollmentStatus`
        