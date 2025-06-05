``a.log_delivery``: Log delivery configurations
===============================================
.. currentmodule:: databricks.sdk.service.billing

.. py:class:: LogDeliveryAPI

    These APIs manage Log delivery configurations for this account. Log delivery configs enable you to
    configure the delivery of the specified type of logs to your storage account.

    .. py:method:: create(log_delivery_configuration: CreateLogDeliveryConfigurationParams) -> WrappedLogDeliveryConfiguration


        Usage:

        .. code-block::

            import os
            import time
            
            from databricks.sdk import AccountClient
            from databricks.sdk.service import billing, provisioning
            
            a = AccountClient()
            
            bucket = a.storage.create(
                storage_configuration_name=f"sdk-{time.time_ns()}",
                root_bucket_info=provisioning.RootBucketInfo(bucket_name=f"sdk-{time.time_ns()}"),
            )
            
            creds = a.credentials.create(
                credentials_name=f"sdk-{time.time_ns()}",
                aws_credentials=provisioning.CreateCredentialAwsCredentials(
                    sts_role=provisioning.CreateCredentialStsRole(role_arn=os.environ["TEST_LOGDELIVERY_ARN"])
                ),
            )
            
            created = a.log_delivery.create(
                log_delivery_configuration=billing.CreateLogDeliveryConfigurationParams(
                    config_name=f"sdk-{time.time_ns()}",
                    credentials_id=creds.credentials_id,
                    storage_configuration_id=bucket.storage_configuration_id,
                    log_type=billing.LogType.AUDIT_LOGS,
                    output_format=billing.OutputFormat.JSON,
                )
            )
            
            # cleanup
            a.storage.delete(storage_configuration_id=bucket.storage_configuration_id)
            a.credentials.delete(credentials_id=creds.credentials_id)
            a.log_delivery.patch_status(
                log_delivery_configuration_id=created.log_delivery_configuration.config_id,
                status=billing.LogDeliveryConfigStatus.DISABLED,
            )

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

        :param log_delivery_configuration: :class:`CreateLogDeliveryConfigurationParams`
          * Log Delivery Configuration

        :returns: :class:`WrappedLogDeliveryConfiguration`
        

    .. py:method:: get(log_delivery_configuration_id: str) -> GetLogDeliveryConfigurationResponse


        Usage:

        .. code-block::

            import os
            import time
            
            from databricks.sdk import AccountClient
            from databricks.sdk.service import billing, provisioning
            
            a = AccountClient()
            
            bucket = a.storage.create(
                storage_configuration_name=f"sdk-{time.time_ns()}",
                root_bucket_info=provisioning.RootBucketInfo(bucket_name=f"sdk-{time.time_ns()}"),
            )
            
            creds = a.credentials.create(
                credentials_name=f"sdk-{time.time_ns()}",
                aws_credentials=provisioning.CreateCredentialAwsCredentials(
                    sts_role=provisioning.CreateCredentialStsRole(role_arn=os.environ["TEST_LOGDELIVERY_ARN"])
                ),
            )
            
            created = a.log_delivery.create(
                log_delivery_configuration=billing.CreateLogDeliveryConfigurationParams(
                    config_name=f"sdk-{time.time_ns()}",
                    credentials_id=creds.credentials_id,
                    storage_configuration_id=bucket.storage_configuration_id,
                    log_type=billing.LogType.AUDIT_LOGS,
                    output_format=billing.OutputFormat.JSON,
                )
            )
            
            by_id = a.log_delivery.get(log_delivery_configuration_id=created.log_delivery_configuration.config_id)
            
            # cleanup
            a.storage.delete(storage_configuration_id=bucket.storage_configuration_id)
            a.credentials.delete(credentials_id=creds.credentials_id)
            a.log_delivery.patch_status(
                log_delivery_configuration_id=created.log_delivery_configuration.config_id,
                status=billing.LogDeliveryConfigStatus.DISABLED,
            )

        Get log delivery configuration.

        Gets a Databricks log delivery configuration object for an account, both specified by ID.

        :param log_delivery_configuration_id: str
          The log delivery configuration id of customer

        :returns: :class:`GetLogDeliveryConfigurationResponse`
        

    .. py:method:: list( [, credentials_id: Optional[str], page_token: Optional[str], status: Optional[LogDeliveryConfigStatus], storage_configuration_id: Optional[str]]) -> Iterator[LogDeliveryConfiguration]


        Usage:

        .. code-block::

            from databricks.sdk import AccountClient
            from databricks.sdk.service import billing
            
            a = AccountClient()
            
            all = a.log_delivery.list(billing.ListLogDeliveryRequest())

        Get all log delivery configurations.

        Gets all Databricks log delivery configurations associated with an account specified by ID.

        :param credentials_id: str (optional)
          The Credentials id to filter the search results with
        :param page_token: str (optional)
          A page token received from a previous get all budget configurations call. This token can be used to
          retrieve the subsequent page. Requests first page if absent.
        :param status: :class:`LogDeliveryConfigStatus` (optional)
          The log delivery status to filter the search results with
        :param storage_configuration_id: str (optional)
          The Storage Configuration id to filter the search results with

        :returns: Iterator over :class:`LogDeliveryConfiguration`
        

    .. py:method:: patch_status(log_delivery_configuration_id: str, status: LogDeliveryConfigStatus)

        Enable or disable log delivery configuration.

        Enables or disables a log delivery configuration. Deletion of delivery configurations is not
        supported, so disable log delivery configurations that are no longer needed. Note that you can't
        re-enable a delivery configuration if this would violate the delivery configuration limits described
        under [Create log delivery](:method:LogDelivery/Create).

        :param log_delivery_configuration_id: str
          The log delivery configuration id of customer
        :param status: :class:`LogDeliveryConfigStatus`
          Status of log delivery configuration. Set to `ENABLED` (enabled) or `DISABLED` (disabled). Defaults
          to `ENABLED`. You can [enable or disable the
          configuration](#operation/patch-log-delivery-config-status) later. Deletion of a configuration is
          not supported, so disable a log delivery configuration that is no longer needed.


        