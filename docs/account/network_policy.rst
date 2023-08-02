Network Policy
==============
.. py:class:: AccountNetworkPolicyAPI

    Network policy is a set of rules that defines what can be accessed from your Databricks network. E.g.: You
    can choose to block your SQL UDF to access internet from your Databricks serverless clusters.
    
    There is only one instance of this setting per account. Since this setting has a default value, this
    setting is present on all accounts even though it's never set on a given account. Deletion reverts the
    value of the setting back to the default value.

    .. py:method:: delete_account_network_policy(etag)

        Delete Account Network Policy.
        
        Reverts back all the account network policies back to default.
        
        :param etag: str
          etag used for versioning. The response is at least as fresh as the eTag provided. This is used for
          optimistic concurrency control as a way to help prevent simultaneous writes of a setting overwriting
          each other. It is strongly suggested that systems make use of the etag in the read -> delete pattern
          to perform setting deletions in order to avoid race conditions. That is, get an etag from a GET
          request, and pass it with the DELETE request to identify the rule set version you are deleting.
        
        :returns: :class:`DeleteAccountNetworkPolicyResponse`
        

    .. py:method:: read_account_network_policy(etag)

        Get Account Network Policy.
        
        Gets the value of Account level Network Policy.
        
        :param etag: str
          etag used for versioning. The response is at least as fresh as the eTag provided. This is used for
          optimistic concurrency control as a way to help prevent simultaneous writes of a setting overwriting
          each other. It is strongly suggested that systems make use of the etag in the read -> delete pattern
          to perform setting deletions in order to avoid race conditions. That is, get an etag from a GET
          request, and pass it with the DELETE request to identify the rule set version you are deleting.
        
        :returns: :class:`AccountNetworkPolicyMessage`
        

    .. py:method:: update_account_network_policy( [, allow_missing, setting])

        Update Account Network Policy.
        
        Updates the policy content of Account level Network Policy.
        
        :param allow_missing: bool (optional)
          This should always be set to true for Settings RPCs. Added for AIP compliance.
        :param setting: :class:`AccountNetworkPolicyMessage` (optional)
        
        :returns: :class:`AccountNetworkPolicyMessage`
        