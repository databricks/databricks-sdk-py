``a.log_delivery``: Log delivery configurations
===============================================
.. currentmodule:: databricks.sdk.service.billing

.. py:class:: LogDeliveryAPI

    These APIs manage log delivery configurations for this account. The two supported log types for this API
    are _billable usage logs_ and _audit logs_. This feature is in Public Preview. This feature works with all
    account ID types.
    
    Log delivery works with all account types. However, if your account is on the E2 version of the platform
    or on a select custom plan that allows multiple workspaces per account, you can optionally configure
    different storage destinations for each workspace. Log delivery status is also provided to know the latest
    status of log delivery attempts. The high-level flow of billable usage delivery:
    
    1. **Create storage**: In AWS, [create a new AWS S3 bucket] with a specific bucket policy. Using
    Databricks APIs, call the Account API to create a [storage configuration object](:method:Storage/Create)
    that uses the bucket name. 2. **Create credentials**: In AWS, create the appropriate AWS IAM role. For
    full details, including the required IAM role policies and trust relationship, see [Billable usage log
    delivery]. Using Databricks APIs, call the Account API to create a [credential configuration
    object](:method:Credentials/Create) that uses the IAM role"s ARN. 3. **Create log delivery
    configuration**: Using Databricks APIs, call the Account API to [create a log delivery
    configuration](:method:LogDelivery/Create) that uses the credential and storage configuration objects from
    previous steps. You can specify if the logs should include all events of that log type in your account
    (_Account level_ delivery) or only events for a specific set of workspaces (_workspace level_ delivery).
    Account level log delivery applies to all current and future workspaces plus account level logs, while
    workspace level log delivery solely delivers logs related to the specified workspaces. You can create
    multiple types of delivery configurations per account.
    
    For billable usage delivery: * For more information about billable usage logs, see [Billable usage log
    delivery]. For the CSV schema, see the [Usage page]. * The delivery location is
    `<bucket-name>/<prefix>/billable-usage/csv/`, where `<prefix>` is the name of the optional delivery path
    prefix you set up during log delivery configuration. Files are named
    `workspaceId=<workspace-id>-usageMonth=<month>.csv`. * All billable usage logs apply to specific
    workspaces (_workspace level_ logs). You can aggregate usage for your entire account by creating an
    _account level_ delivery configuration that delivers logs for all current and future workspaces in your
    account. * The files are delivered daily by overwriting the month's CSV file for each workspace.
    
    For audit log delivery: * For more information about about audit log delivery, see [Audit log delivery],
    which includes information about the used JSON schema. * The delivery location is
    `<bucket-name>/<delivery-path-prefix>/workspaceId=<workspaceId>/date=<yyyy-mm-dd>/auditlogs_<internal-id>.json`.
    Files may get overwritten with the same content multiple times to achieve exactly-once delivery. * If the
    audit log delivery configuration included specific workspace IDs, only _workspace-level_ audit logs for
    those workspaces are delivered. If the log delivery configuration applies to the entire account (_account
    level_ delivery configuration), the audit log delivery includes workspace-level audit logs for all
    workspaces in the account as well as account-level audit logs. See [Audit log delivery] for details. *
    Auditable events are typically available in logs within 15 minutes.
    
    [Audit log delivery]: https://docs.databricks.com/administration-guide/account-settings/audit-logs.html
    [Billable usage log delivery]: https://docs.databricks.com/administration-guide/account-settings/billable-usage-delivery.html
    [Usage page]: https://docs.databricks.com/administration-guide/account-settings/usage.html
    [create a new AWS S3 bucket]: https://docs.databricks.com/administration-guide/account-api/aws-storage.html

    .. py:method:: create( [, log_delivery_configuration: Optional[CreateLogDeliveryConfigurationParams]]) -> WrappedLogDeliveryConfiguration


        Usage:

        .. code-block::

            import os
            import time
            
            from databricks.sdk import AccountClient
            from databricks.sdk.service import billing, provisioning
            
            a = AccountClient()
            
            bucket = a.storage.create(storage_configuration_name=f'sdk-{time.time_ns()}',
                                      root_bucket_info=provisioning.RootBucketInfo(bucket_name=f'sdk-{time.time_ns()}'))
            
            creds = a.credentials.create(
                credentials_name=f'sdk-{time.time_ns()}',
                aws_credentials=provisioning.CreateCredentialAwsCredentials(sts_role=provisioning.CreateCredentialStsRole(
                    role_arn=os.environ["TEST_LOGDELIVERY_ARN"])))
            
            created = a.log_delivery.create(log_delivery_configuration=billing.CreateLogDeliveryConfigurationParams(
                config_name=f'sdk-{time.time_ns()}',
                credentials_id=creds.credentials_id,
                storage_configuration_id=bucket.storage_configuration_id,
                log_type=billing.LogType.AUDIT_LOGS,
                output_format=billing.OutputFormat.JSON))
            
            # cleanup
            a.storage.delete(storage_configuration_id=bucket.storage_configuration_id)
            a.credentials.delete(credentials_id=creds.credentials_id)
            a.log_delivery.patch_status(log_delivery_configuration_id=created.log_delivery_configuration.config_id,
                                        status=billing.LogDeliveryConfigStatus.DISABLED)

        Create a new log delivery configuration.
        
        Creates a new Databricks log delivery configuration to enable delivery of the specified type of logs
        to your storage location. This requires that you already created a [credential
        object](:method:Credentials/Create) (which encapsulates a cross-account service IAM role) and a
        [storage configuration object](:method:Storage/Create) (which encapsulates an S3 bucket).
        
        For full details, including the required IAM role policies and bucket policies, see [Deliver and
        access billable usage logs] or [Configure audit logging].
        
        **Note**: There is a limit on the number of log delivery configurations available per account (each
        limit applies separately to each log type including billable usage and audit logs). You can create a
        maximum of two enabled account-level delivery configurations (configurations without a workspace
        filter) per type. Additionally, you can create two enabled workspace-level delivery configurations per
        workspace for each log type, which means that the same workspace ID can occur in the workspace filter
        for no more than two delivery configurations per log type.
        
        You cannot delete a log delivery configuration, but you can disable it (see [Enable or disable log
        delivery configuration](:method:LogDelivery/PatchStatus)).
        
        [Configure audit logging]: https://docs.databricks.com/administration-guide/account-settings/audit-logs.html
        [Deliver and access billable usage logs]: https://docs.databricks.com/administration-guide/account-settings/billable-usage-delivery.html
        
        :param log_delivery_configuration: :class:`CreateLogDeliveryConfigurationParams` (optional)
        
        :returns: :class:`WrappedLogDeliveryConfiguration`
        

    .. py:method:: get(log_delivery_configuration_id: str) -> WrappedLogDeliveryConfiguration


        Usage:

        .. code-block::

            import os
            import time
            
            from databricks.sdk import AccountClient
            from databricks.sdk.service import billing, provisioning
            
            a = AccountClient()
            
            bucket = a.storage.create(storage_configuration_name=f'sdk-{time.time_ns()}',
                                      root_bucket_info=provisioning.RootBucketInfo(bucket_name=f'sdk-{time.time_ns()}'))
            
            creds = a.credentials.create(
                credentials_name=f'sdk-{time.time_ns()}',
                aws_credentials=provisioning.CreateCredentialAwsCredentials(sts_role=provisioning.CreateCredentialStsRole(
                    role_arn=os.environ["TEST_LOGDELIVERY_ARN"])))
            
            created = a.log_delivery.create(log_delivery_configuration=billing.CreateLogDeliveryConfigurationParams(
                config_name=f'sdk-{time.time_ns()}',
                credentials_id=creds.credentials_id,
                storage_configuration_id=bucket.storage_configuration_id,
                log_type=billing.LogType.AUDIT_LOGS,
                output_format=billing.OutputFormat.JSON))
            
            by_id = a.log_delivery.get(log_delivery_configuration_id=created.log_delivery_configuration.config_id)
            
            # cleanup
            a.storage.delete(storage_configuration_id=bucket.storage_configuration_id)
            a.credentials.delete(credentials_id=creds.credentials_id)
            a.log_delivery.patch_status(log_delivery_configuration_id=created.log_delivery_configuration.config_id,
                                        status=billing.LogDeliveryConfigStatus.DISABLED)

        Get log delivery configuration.
        
        Gets a Databricks log delivery configuration object for an account, both specified by ID.
        
        :param log_delivery_configuration_id: str
          Databricks log delivery configuration ID
        
        :returns: :class:`WrappedLogDeliveryConfiguration`
        

    .. py:method:: list( [, credentials_id: Optional[str], status: Optional[LogDeliveryConfigStatus], storage_configuration_id: Optional[str]]) -> Iterator[LogDeliveryConfiguration]


        Usage:

        .. code-block::

            from databricks.sdk import AccountClient
            from databricks.sdk.service import billing
            
            a = AccountClient()
            
            all = a.log_delivery.list(billing.ListLogDeliveryRequest())

        Get all log delivery configurations.
        
        Gets all Databricks log delivery configurations associated with an account specified by ID.
        
        :param credentials_id: str (optional)
          Filter by credential configuration ID.
        :param status: :class:`LogDeliveryConfigStatus` (optional)
          Filter by status `ENABLED` or `DISABLED`.
        :param storage_configuration_id: str (optional)
          Filter by storage configuration ID.
        
        :returns: Iterator over :class:`LogDeliveryConfiguration`
        

    .. py:method:: patch_status(log_delivery_configuration_id: str, status: LogDeliveryConfigStatus)

        Enable or disable log delivery configuration.
        
        Enables or disables a log delivery configuration. Deletion of delivery configurations is not
        supported, so disable log delivery configurations that are no longer needed. Note that you can't
        re-enable a delivery configuration if this would violate the delivery configuration limits described
        under [Create log delivery](:method:LogDelivery/Create).
        
        :param log_delivery_configuration_id: str
          Databricks log delivery configuration ID
        :param status: :class:`LogDeliveryConfigStatus`
          Status of log delivery configuration. Set to `ENABLED` (enabled) or `DISABLED` (disabled). Defaults
          to `ENABLED`. You can [enable or disable the
          configuration](#operation/patch-log-delivery-config-status) later. Deletion of a configuration is
          not supported, so disable a log delivery configuration that is no longer needed.
        
        :returns: :class:`PatchStatusResponse`
        