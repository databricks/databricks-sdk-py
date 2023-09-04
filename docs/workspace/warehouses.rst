SQL Warehouses
==============
.. py:class:: WarehousesAPI

    A SQL warehouse is a compute resource that lets you run SQL commands on data objects within Databricks
    SQL. Compute resources are infrastructure resources that provide processing capabilities in the cloud.

    .. py:method:: create( [, auto_stop_mins, channel, cluster_size, creator_name, enable_photon, enable_serverless_compute, instance_profile_arn, max_num_clusters, min_num_clusters, name, spot_instance_policy, tags, warehouse_type])

        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            created = w.warehouses.create(name=f'sdk-{time.time_ns()}',
                                          cluster_size="2X-Small",
                                          max_num_clusters=1,
                                          auto_stop_mins=10).result()
            
            # cleanup
            w.warehouses.delete(id=created.id)

        Create a warehouse.
        
        Creates a new SQL warehouse.
        
        :param auto_stop_mins: int (optional)
          The amount of time in minutes that a SQL warehouse must be idle (i.e., no RUNNING queries) before it
          is automatically stopped.
          
          Supported values: - Must be == 0 or >= 10 mins - 0 indicates no autostop.
          
          Defaults to 120 mins
        :param channel: :class:`Channel` (optional)
          Channel Details
        :param cluster_size: str (optional)
          Size of the clusters allocated for this warehouse. Increasing the size of a spark cluster allows you
          to run larger queries on it. If you want to increase the number of concurrent queries, please tune
          max_num_clusters.
          
          Supported values: - 2X-Small - X-Small - Small - Medium - Large - X-Large - 2X-Large - 3X-Large -
          4X-Large
        :param creator_name: str (optional)
          warehouse creator name
        :param enable_photon: bool (optional)
          Configures whether the warehouse should use Photon optimized clusters.
          
          Defaults to false.
        :param enable_serverless_compute: bool (optional)
          Configures whether the warehouse should use serverless compute
        :param instance_profile_arn: str (optional)
          Deprecated. Instance profile used to pass IAM role to the cluster
        :param max_num_clusters: int (optional)
          Maximum number of clusters that the autoscaler will create to handle concurrent queries.
          
          Supported values: - Must be >= min_num_clusters - Must be <= 30.
          
          Defaults to min_clusters if unset.
        :param min_num_clusters: int (optional)
          Minimum number of available clusters that will be maintained for this SQL warehouse. Increasing this
          will ensure that a larger number of clusters are always running and therefore may reduce the cold
          start time for new queries. This is similar to reserved vs. revocable cores in a resource manager.
          
          Supported values: - Must be > 0 - Must be <= min(max_num_clusters, 30)
          
          Defaults to 1
        :param name: str (optional)
          Logical name for the cluster.
          
          Supported values: - Must be unique within an org. - Must be less than 100 characters.
        :param spot_instance_policy: :class:`SpotInstancePolicy` (optional)
          Configurations whether the warehouse should use spot instances.
        :param tags: :class:`EndpointTags` (optional)
          A set of key-value pairs that will be tagged on all resources (e.g., AWS instances and EBS volumes)
          associated with this SQL warehouse.
          
          Supported values: - Number of tags < 45.
        :param warehouse_type: :class:`CreateWarehouseRequestWarehouseType` (optional)
          Warehouse type: `PRO` or `CLASSIC`. If you want to use serverless compute, you must set to `PRO` and
          also set the field `enable_serverless_compute` to `true`.
        
        :returns:
          Long-running operation waiter for :class:`GetWarehouseResponse`.
          See :method:wait_get_warehouse_running for more details.
        

    .. py:method:: delete(id)

        Delete a warehouse.
        
        Deletes a SQL warehouse.
        
        :param id: str
          Required. Id of the SQL warehouse.
        
        
        

    .. py:method:: edit(id [, auto_stop_mins, channel, cluster_size, creator_name, enable_photon, enable_serverless_compute, instance_profile_arn, max_num_clusters, min_num_clusters, name, spot_instance_policy, tags, warehouse_type])

        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            created = w.warehouses.create(name=f'sdk-{time.time_ns()}',
                                          cluster_size="2X-Small",
                                          max_num_clusters=1,
                                          auto_stop_mins=10).result()
            
            _ = w.warehouses.edit(id=created.id,
                                  name=f'sdk-{time.time_ns()}',
                                  cluster_size="2X-Small",
                                  max_num_clusters=1,
                                  auto_stop_mins=10)
            
            # cleanup
            w.warehouses.delete(id=created.id)

        Update a warehouse.
        
        Updates the configuration for a SQL warehouse.
        
        :param id: str
          Required. Id of the warehouse to configure.
        :param auto_stop_mins: int (optional)
          The amount of time in minutes that a SQL warehouse must be idle (i.e., no RUNNING queries) before it
          is automatically stopped.
          
          Supported values: - Must be == 0 or >= 10 mins - 0 indicates no autostop.
          
          Defaults to 120 mins
        :param channel: :class:`Channel` (optional)
          Channel Details
        :param cluster_size: str (optional)
          Size of the clusters allocated for this warehouse. Increasing the size of a spark cluster allows you
          to run larger queries on it. If you want to increase the number of concurrent queries, please tune
          max_num_clusters.
          
          Supported values: - 2X-Small - X-Small - Small - Medium - Large - X-Large - 2X-Large - 3X-Large -
          4X-Large
        :param creator_name: str (optional)
          warehouse creator name
        :param enable_photon: bool (optional)
          Configures whether the warehouse should use Photon optimized clusters.
          
          Defaults to false.
        :param enable_serverless_compute: bool (optional)
          Configures whether the warehouse should use serverless compute.
        :param instance_profile_arn: str (optional)
          Deprecated. Instance profile used to pass IAM role to the cluster
        :param max_num_clusters: int (optional)
          Maximum number of clusters that the autoscaler will create to handle concurrent queries.
          
          Supported values: - Must be >= min_num_clusters - Must be <= 30.
          
          Defaults to min_clusters if unset.
        :param min_num_clusters: int (optional)
          Minimum number of available clusters that will be maintained for this SQL warehouse. Increasing this
          will ensure that a larger number of clusters are always running and therefore may reduce the cold
          start time for new queries. This is similar to reserved vs. revocable cores in a resource manager.
          
          Supported values: - Must be > 0 - Must be <= min(max_num_clusters, 30)
          
          Defaults to 1
        :param name: str (optional)
          Logical name for the cluster.
          
          Supported values: - Must be unique within an org. - Must be less than 100 characters.
        :param spot_instance_policy: :class:`SpotInstancePolicy` (optional)
          Configurations whether the warehouse should use spot instances.
        :param tags: :class:`EndpointTags` (optional)
          A set of key-value pairs that will be tagged on all resources (e.g., AWS instances and EBS volumes)
          associated with this SQL warehouse.
          
          Supported values: - Number of tags < 45.
        :param warehouse_type: :class:`EditWarehouseRequestWarehouseType` (optional)
          Warehouse type: `PRO` or `CLASSIC`. If you want to use serverless compute, you must set to `PRO` and
          also set the field `enable_serverless_compute` to `true`.
        
        :returns:
          Long-running operation waiter for :class:`GetWarehouseResponse`.
          See :method:wait_get_warehouse_running for more details.
        

    .. py:method:: get(id)

        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            created = w.warehouses.create(name=f'sdk-{time.time_ns()}',
                                          cluster_size="2X-Small",
                                          max_num_clusters=1,
                                          auto_stop_mins=10).result()
            
            wh = w.warehouses.get(id=created.id)
            
            # cleanup
            w.warehouses.delete(id=created.id)

        Get warehouse info.
        
        Gets the information for a single SQL warehouse.
        
        :param id: str
          Required. Id of the SQL warehouse.
        
        :returns: :class:`GetWarehouseResponse`
        

    .. py:method:: get_permission_levels(warehouse_id)

        Get SQL warehouse permission levels.
        
        Gets the permission levels that a user can have on an object.
        
        :param warehouse_id: str
          The SQL warehouse for which to get or manage permissions.
        
        :returns: :class:`GetWarehousePermissionLevelsResponse`
        

    .. py:method:: get_permissions(warehouse_id)

        Get SQL warehouse permissions.
        
        Gets the permissions of a SQL warehouse. SQL warehouses can inherit permissions from their root
        object.
        
        :param warehouse_id: str
          The SQL warehouse for which to get or manage permissions.
        
        :returns: :class:`WarehousePermissions`
        

    .. py:method:: get_workspace_warehouse_config()

        Get the workspace configuration.
        
        Gets the workspace level configuration that is shared by all SQL warehouses in a workspace.
        
        :returns: :class:`GetWorkspaceWarehouseConfigResponse`
        

    .. py:method:: list( [, run_as_user_id])

        Usage:

        .. code-block::

            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import sql
            
            w = WorkspaceClient()
            
            all = w.warehouses.list(sql.ListWarehousesRequest())

        List warehouses.
        
        Lists all SQL warehouses that a user has manager permissions on.
        
        :param run_as_user_id: int (optional)
          Service Principal which will be used to fetch the list of warehouses. If not specified, the user
          from the session header is used.
        
        :returns: Iterator over :class:`EndpointInfo`
        

    .. py:method:: set_permissions(warehouse_id [, access_control_list])

        Set SQL warehouse permissions.
        
        Sets permissions on a SQL warehouse. SQL warehouses can inherit permissions from their root object.
        
        :param warehouse_id: str
          The SQL warehouse for which to get or manage permissions.
        :param access_control_list: List[:class:`WarehouseAccessControlRequest`] (optional)
        
        :returns: :class:`WarehousePermissions`
        

    .. py:method:: set_workspace_warehouse_config( [, channel, config_param, data_access_config, enabled_warehouse_types, global_param, google_service_account, instance_profile_arn, security_policy, sql_configuration_parameters])

        Set the workspace configuration.
        
        Sets the workspace level configuration that is shared by all SQL warehouses in a workspace.
        
        :param channel: :class:`Channel` (optional)
          Optional: Channel selection details
        :param config_param: :class:`RepeatedEndpointConfPairs` (optional)
          Deprecated: Use sql_configuration_parameters
        :param data_access_config: List[:class:`EndpointConfPair`] (optional)
          Spark confs for external hive metastore configuration JSON serialized size must be less than <= 512K
        :param enabled_warehouse_types: List[:class:`WarehouseTypePair`] (optional)
          List of Warehouse Types allowed in this workspace (limits allowed value of the type field in
          CreateWarehouse and EditWarehouse). Note: Some types cannot be disabled, they don't need to be
          specified in SetWorkspaceWarehouseConfig. Note: Disabling a type may cause existing warehouses to be
          converted to another type. Used by frontend to save specific type availability in the warehouse
          create and edit form UI.
        :param global_param: :class:`RepeatedEndpointConfPairs` (optional)
          Deprecated: Use sql_configuration_parameters
        :param google_service_account: str (optional)
          GCP only: Google Service Account used to pass to cluster to access Google Cloud Storage
        :param instance_profile_arn: str (optional)
          AWS Only: Instance profile used to pass IAM role to the cluster
        :param security_policy: :class:`SetWorkspaceWarehouseConfigRequestSecurityPolicy` (optional)
          Security policy for warehouses
        :param sql_configuration_parameters: :class:`RepeatedEndpointConfPairs` (optional)
          SQL configuration parameters
        
        
        

    .. py:method:: start(id)

        Start a warehouse.
        
        Starts a SQL warehouse.
        
        :param id: str
          Required. Id of the SQL warehouse.
        
        :returns:
          Long-running operation waiter for :class:`GetWarehouseResponse`.
          See :method:wait_get_warehouse_running for more details.
        

    .. py:method:: stop(id)

        Stop a warehouse.
        
        Stops a SQL warehouse.
        
        :param id: str
          Required. Id of the SQL warehouse.
        
        :returns:
          Long-running operation waiter for :class:`GetWarehouseResponse`.
          See :method:wait_get_warehouse_stopped for more details.
        

    .. py:method:: update_permissions(warehouse_id [, access_control_list])

        Update SQL warehouse permissions.
        
        Updates the permissions on a SQL warehouse. SQL warehouses can inherit permissions from their root
        object.
        
        :param warehouse_id: str
          The SQL warehouse for which to get or manage permissions.
        :param access_control_list: List[:class:`WarehouseAccessControlRequest`] (optional)
        
        :returns: :class:`WarehousePermissions`
        