Clusters
========
.. py:class:: ClustersExt

    

    .. py:method:: change_owner(cluster_id, owner_username)

        Usage:

        .. code-block::

            import os
            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            latest = w.clusters.select_spark_version(latest=True)
            
            cluster_name = f'sdk-{time.time_ns()}'
            
            other_owner = w.users.create(user_name=f'sdk-{time.time_ns()}@example.com')
            
            clstr = w.clusters.create(cluster_name=cluster_name,
                                      spark_version=latest,
                                      instance_pool_id=os.environ["TEST_INSTANCE_POOL_ID"],
                                      autotermination_minutes=15,
                                      num_workers=1).result()
            
            w.clusters.change_owner(cluster_id=clstr.cluster_id, owner_username=other_owner.user_name)
            
            # cleanup
            w.users.delete(delete=other_owner.id)
            w.clusters.permanent_delete(permanent_delete=clstr.cluster_id)

        Change cluster owner.
        
        Change the owner of the cluster. You must be an admin to perform this operation.
        
        :param cluster_id: str
          <needs content added>
        :param owner_username: str
          New owner of the cluster_id after this RPC.
        
        
        

    .. py:method:: create(spark_version [, apply_policy_default_values, autoscale, autotermination_minutes, aws_attributes, azure_attributes, cluster_log_conf, cluster_name, cluster_source, custom_tags, driver_instance_pool_id, driver_node_type_id, enable_elastic_disk, enable_local_disk_encryption, gcp_attributes, init_scripts, instance_pool_id, node_type_id, num_workers, policy_id, runtime_engine, spark_conf, spark_env_vars, ssh_public_keys, workload_type])

        Usage:

        .. code-block::

            import os
            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            latest = w.clusters.select_spark_version(latest=True)
            
            cluster_name = f'sdk-{time.time_ns()}'
            
            clstr = w.clusters.create(cluster_name=cluster_name,
                                      spark_version=latest,
                                      instance_pool_id=os.environ["TEST_INSTANCE_POOL_ID"],
                                      autotermination_minutes=15,
                                      num_workers=1).result()
            
            # cleanup
            w.clusters.permanent_delete(permanent_delete=clstr.cluster_id)

        Create new cluster.
        
        Creates a new Spark cluster. This method will acquire new instances from the cloud provider if
        necessary. This method is asynchronous; the returned `cluster_id` can be used to poll the cluster
        status. When this method returns, the cluster will be in a `PENDING` state. The cluster will be usable
        once it enters a `RUNNING` state.
        
        Note: Databricks may not be able to acquire some of the requested nodes, due to cloud provider
        limitations (account limits, spot price, etc.) or transient network issues.
        
        If Databricks acquires at least 85% of the requested on-demand nodes, cluster creation will succeed.
        Otherwise the cluster will terminate with an informative error message.
        
        :param spark_version: str
          The Spark version of the cluster, e.g. `3.3.x-scala2.11`. A list of available Spark versions can be
          retrieved by using the :method:clusters/sparkVersions API call.
        :param apply_policy_default_values: bool (optional)
          Note: This field won't be true for webapp requests. Only API users will check this field.
        :param autoscale: :class:`AutoScale` (optional)
          Parameters needed in order to automatically scale clusters up and down based on load. Note:
          autoscaling works best with DB runtime versions 3.0 or later.
        :param autotermination_minutes: int (optional)
          Automatically terminates the cluster after it is inactive for this time in minutes. If not set, this
          cluster will not be automatically terminated. If specified, the threshold must be between 10 and
          10000 minutes. Users can also set this value to 0 to explicitly disable automatic termination.
        :param aws_attributes: :class:`AwsAttributes` (optional)
          Attributes related to clusters running on Amazon Web Services. If not specified at cluster creation,
          a set of default values will be used.
        :param azure_attributes: :class:`AzureAttributes` (optional)
          Attributes related to clusters running on Microsoft Azure. If not specified at cluster creation, a
          set of default values will be used.
        :param cluster_log_conf: :class:`ClusterLogConf` (optional)
          The configuration for delivering spark logs to a long-term storage destination. Two kinds of
          destinations (dbfs and s3) are supported. Only one destination can be specified for one cluster. If
          the conf is given, the logs will be delivered to the destination every `5 mins`. The destination of
          driver logs is `$destination/$clusterId/driver`, while the destination of executor logs is
          `$destination/$clusterId/executor`.
        :param cluster_name: str (optional)
          Cluster name requested by the user. This doesn't have to be unique. If not specified at creation,
          the cluster name will be an empty string.
        :param cluster_source: :class:`ClusterSource` (optional)
          Determines whether the cluster was created by a user through the UI, created by the Databricks Jobs
          Scheduler, or through an API request. This is the same as cluster_creator, but read only.
        :param custom_tags: Dict[str,str] (optional)
          Additional tags for cluster resources. Databricks will tag all cluster resources (e.g., AWS
          instances and EBS volumes) with these tags in addition to `default_tags`. Notes:
          
          - Currently, Databricks allows at most 45 custom tags
          
          - Clusters can only reuse cloud resources if the resources' tags are a subset of the cluster tags
        :param driver_instance_pool_id: str (optional)
          The optional ID of the instance pool for the driver of the cluster belongs. The pool cluster uses
          the instance pool with id (instance_pool_id) if the driver pool is not assigned.
        :param driver_node_type_id: str (optional)
          The node type of the Spark driver. Note that this field is optional; if unset, the driver node type
          will be set as the same value as `node_type_id` defined above.
        :param enable_elastic_disk: bool (optional)
          Autoscaling Local Storage: when enabled, this cluster will dynamically acquire additional disk space
          when its Spark workers are running low on disk space. This feature requires specific AWS permissions
          to function correctly - refer to the User Guide for more details.
        :param enable_local_disk_encryption: bool (optional)
          Whether to enable LUKS on cluster VMs' local disks
        :param gcp_attributes: :class:`GcpAttributes` (optional)
          Attributes related to clusters running on Google Cloud Platform. If not specified at cluster
          creation, a set of default values will be used.
        :param init_scripts: List[:class:`InitScriptInfo`] (optional)
          The configuration for storing init scripts. Any number of destinations can be specified. The scripts
          are executed sequentially in the order provided. If `cluster_log_conf` is specified, init script
          logs are sent to `<destination>/<cluster-ID>/init_scripts`.
        :param instance_pool_id: str (optional)
          The optional ID of the instance pool to which the cluster belongs.
        :param node_type_id: str (optional)
          This field encodes, through a single value, the resources available to each of the Spark nodes in
          this cluster. For example, the Spark nodes can be provisioned and optimized for memory or compute
          intensive workloads. A list of available node types can be retrieved by using the
          :method:clusters/listNodeTypes API call.
        :param num_workers: int (optional)
          Number of worker nodes that this cluster should have. A cluster has one Spark Driver and
          `num_workers` Executors for a total of `num_workers` + 1 Spark nodes.
          
          Note: When reading the properties of a cluster, this field reflects the desired number of workers
          rather than the actual current number of workers. For instance, if a cluster is resized from 5 to 10
          workers, this field will immediately be updated to reflect the target size of 10 workers, whereas
          the workers listed in `spark_info` will gradually increase from 5 to 10 as the new nodes are
          provisioned.
        :param policy_id: str (optional)
          The ID of the cluster policy used to create the cluster if applicable.
        :param runtime_engine: :class:`RuntimeEngine` (optional)
          Decides which runtime engine to be use, e.g. Standard vs. Photon. If unspecified, the runtime engine
          is inferred from spark_version.
        :param spark_conf: Dict[str,str] (optional)
          An object containing a set of optional, user-specified Spark configuration key-value pairs. Users
          can also pass in a string of extra JVM options to the driver and the executors via
          `spark.driver.extraJavaOptions` and `spark.executor.extraJavaOptions` respectively.
        :param spark_env_vars: Dict[str,str] (optional)
          An object containing a set of optional, user-specified environment variable key-value pairs. Please
          note that key-value pair of the form (X,Y) will be exported as is (i.e., `export X='Y'`) while
          launching the driver and workers.
          
          In order to specify an additional set of `SPARK_DAEMON_JAVA_OPTS`, we recommend appending them to
          `$SPARK_DAEMON_JAVA_OPTS` as shown in the example below. This ensures that all default databricks
          managed environmental variables are included as well.
          
          Example Spark environment variables: `{"SPARK_WORKER_MEMORY": "28000m", "SPARK_LOCAL_DIRS":
          "/local_disk0"}` or `{"SPARK_DAEMON_JAVA_OPTS": "$SPARK_DAEMON_JAVA_OPTS
          -Dspark.shuffle.service.enabled=true"}`
        :param ssh_public_keys: List[str] (optional)
          SSH public key contents that will be added to each Spark node in this cluster. The corresponding
          private keys can be used to login with the user name `ubuntu` on port `2200`. Up to 10 keys can be
          specified.
        :param workload_type: :class:`WorkloadType` (optional)
        
        :returns:
          long-running operation waiter for :class:`ClusterInfo`.
          See :method:wait_get_cluster_running for more details.
        

    .. py:method:: delete(cluster_id)

        Usage:

        .. code-block::

            import os
            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            latest = w.clusters.select_spark_version(latest=True)
            
            cluster_name = f'sdk-{time.time_ns()}'
            
            clstr = w.clusters.create(cluster_name=cluster_name,
                                      spark_version=latest,
                                      instance_pool_id=os.environ["TEST_INSTANCE_POOL_ID"],
                                      autotermination_minutes=15,
                                      num_workers=1).result()
            
            _ = w.clusters.delete(delete=clstr.cluster_id).result()
            
            # cleanup
            w.clusters.permanent_delete(permanent_delete=clstr.cluster_id)

        Terminate cluster.
        
        Terminates the Spark cluster with the specified ID. The cluster is removed asynchronously. Once the
        termination has completed, the cluster will be in a `TERMINATED` state. If the cluster is already in a
        `TERMINATING` or `TERMINATED` state, nothing will happen.
        
        :param cluster_id: str
          The cluster to be terminated.
        
        :returns:
          long-running operation waiter for :class:`ClusterInfo`.
          See :method:wait_get_cluster_terminated for more details.
        

    .. py:method:: edit(cluster_id, spark_version [, apply_policy_default_values, autoscale, autotermination_minutes, aws_attributes, azure_attributes, cluster_log_conf, cluster_name, cluster_source, custom_tags, data_security_mode, docker_image, driver_instance_pool_id, driver_node_type_id, enable_elastic_disk, enable_local_disk_encryption, gcp_attributes, init_scripts, instance_pool_id, node_type_id, num_workers, policy_id, runtime_engine, single_user_name, spark_conf, spark_env_vars, ssh_public_keys, workload_type])

        Usage:

        .. code-block::

            import os
            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            cluster_name = f'sdk-{time.time_ns()}'
            
            latest = w.clusters.select_spark_version(latest=True)
            
            clstr = w.clusters.create(cluster_name=cluster_name,
                                      spark_version=latest,
                                      instance_pool_id=os.environ["TEST_INSTANCE_POOL_ID"],
                                      autotermination_minutes=15,
                                      num_workers=1).result()
            
            _ = w.clusters.edit(cluster_id=clstr.cluster_id,
                                spark_version=latest,
                                cluster_name=cluster_name,
                                instance_pool_id=os.environ["TEST_INSTANCE_POOL_ID"],
                                autotermination_minutes=10,
                                num_workers=2).result()
            
            # cleanup
            w.clusters.permanent_delete(permanent_delete=clstr.cluster_id)

        Update cluster configuration.
        
        Updates the configuration of a cluster to match the provided attributes and size. A cluster can be
        updated if it is in a `RUNNING` or `TERMINATED` state.
        
        If a cluster is updated while in a `RUNNING` state, it will be restarted so that the new attributes
        can take effect.
        
        If a cluster is updated while in a `TERMINATED` state, it will remain `TERMINATED`. The next time it
        is started using the `clusters/start` API, the new attributes will take effect. Any attempt to update
        a cluster in any other state will be rejected with an `INVALID_STATE` error code.
        
        Clusters created by the Databricks Jobs service cannot be edited.
        
        :param cluster_id: str
          ID of the cluser
        :param spark_version: str
          The Spark version of the cluster, e.g. `3.3.x-scala2.11`. A list of available Spark versions can be
          retrieved by using the :method:clusters/sparkVersions API call.
        :param apply_policy_default_values: bool (optional)
          Note: This field won't be true for webapp requests. Only API users will check this field.
        :param autoscale: :class:`AutoScale` (optional)
          Parameters needed in order to automatically scale clusters up and down based on load. Note:
          autoscaling works best with DB runtime versions 3.0 or later.
        :param autotermination_minutes: int (optional)
          Automatically terminates the cluster after it is inactive for this time in minutes. If not set, this
          cluster will not be automatically terminated. If specified, the threshold must be between 10 and
          10000 minutes. Users can also set this value to 0 to explicitly disable automatic termination.
        :param aws_attributes: :class:`AwsAttributes` (optional)
          Attributes related to clusters running on Amazon Web Services. If not specified at cluster creation,
          a set of default values will be used.
        :param azure_attributes: :class:`AzureAttributes` (optional)
          Attributes related to clusters running on Microsoft Azure. If not specified at cluster creation, a
          set of default values will be used.
        :param cluster_log_conf: :class:`ClusterLogConf` (optional)
          The configuration for delivering spark logs to a long-term storage destination. Two kinds of
          destinations (dbfs and s3) are supported. Only one destination can be specified for one cluster. If
          the conf is given, the logs will be delivered to the destination every `5 mins`. The destination of
          driver logs is `$destination/$clusterId/driver`, while the destination of executor logs is
          `$destination/$clusterId/executor`.
        :param cluster_name: str (optional)
          Cluster name requested by the user. This doesn't have to be unique. If not specified at creation,
          the cluster name will be an empty string.
        :param cluster_source: :class:`ClusterSource` (optional)
          Determines whether the cluster was created by a user through the UI, created by the Databricks Jobs
          Scheduler, or through an API request. This is the same as cluster_creator, but read only.
        :param custom_tags: Dict[str,str] (optional)
          Additional tags for cluster resources. Databricks will tag all cluster resources (e.g., AWS
          instances and EBS volumes) with these tags in addition to `default_tags`. Notes:
          
          - Currently, Databricks allows at most 45 custom tags
          
          - Clusters can only reuse cloud resources if the resources' tags are a subset of the cluster tags
        :param data_security_mode: :class:`DataSecurityMode` (optional)
          This describes an enum
        :param docker_image: :class:`DockerImage` (optional)
        :param driver_instance_pool_id: str (optional)
          The optional ID of the instance pool for the driver of the cluster belongs. The pool cluster uses
          the instance pool with id (instance_pool_id) if the driver pool is not assigned.
        :param driver_node_type_id: str (optional)
          The node type of the Spark driver. Note that this field is optional; if unset, the driver node type
          will be set as the same value as `node_type_id` defined above.
        :param enable_elastic_disk: bool (optional)
          Autoscaling Local Storage: when enabled, this cluster will dynamically acquire additional disk space
          when its Spark workers are running low on disk space. This feature requires specific AWS permissions
          to function correctly - refer to the User Guide for more details.
        :param enable_local_disk_encryption: bool (optional)
          Whether to enable LUKS on cluster VMs' local disks
        :param gcp_attributes: :class:`GcpAttributes` (optional)
          Attributes related to clusters running on Google Cloud Platform. If not specified at cluster
          creation, a set of default values will be used.
        :param init_scripts: List[:class:`InitScriptInfo`] (optional)
          The configuration for storing init scripts. Any number of destinations can be specified. The scripts
          are executed sequentially in the order provided. If `cluster_log_conf` is specified, init script
          logs are sent to `<destination>/<cluster-ID>/init_scripts`.
        :param instance_pool_id: str (optional)
          The optional ID of the instance pool to which the cluster belongs.
        :param node_type_id: str (optional)
          This field encodes, through a single value, the resources available to each of the Spark nodes in
          this cluster. For example, the Spark nodes can be provisioned and optimized for memory or compute
          intensive workloads. A list of available node types can be retrieved by using the
          :method:clusters/listNodeTypes API call.
        :param num_workers: int (optional)
          Number of worker nodes that this cluster should have. A cluster has one Spark Driver and
          `num_workers` Executors for a total of `num_workers` + 1 Spark nodes.
          
          Note: When reading the properties of a cluster, this field reflects the desired number of workers
          rather than the actual current number of workers. For instance, if a cluster is resized from 5 to 10
          workers, this field will immediately be updated to reflect the target size of 10 workers, whereas
          the workers listed in `spark_info` will gradually increase from 5 to 10 as the new nodes are
          provisioned.
        :param policy_id: str (optional)
          The ID of the cluster policy used to create the cluster if applicable.
        :param runtime_engine: :class:`RuntimeEngine` (optional)
          Decides which runtime engine to be use, e.g. Standard vs. Photon. If unspecified, the runtime engine
          is inferred from spark_version.
        :param single_user_name: str (optional)
          Single user name if data_security_mode is `SINGLE_USER`
        :param spark_conf: Dict[str,str] (optional)
          An object containing a set of optional, user-specified Spark configuration key-value pairs. Users
          can also pass in a string of extra JVM options to the driver and the executors via
          `spark.driver.extraJavaOptions` and `spark.executor.extraJavaOptions` respectively.
        :param spark_env_vars: Dict[str,str] (optional)
          An object containing a set of optional, user-specified environment variable key-value pairs. Please
          note that key-value pair of the form (X,Y) will be exported as is (i.e., `export X='Y'`) while
          launching the driver and workers.
          
          In order to specify an additional set of `SPARK_DAEMON_JAVA_OPTS`, we recommend appending them to
          `$SPARK_DAEMON_JAVA_OPTS` as shown in the example below. This ensures that all default databricks
          managed environmental variables are included as well.
          
          Example Spark environment variables: `{"SPARK_WORKER_MEMORY": "28000m", "SPARK_LOCAL_DIRS":
          "/local_disk0"}` or `{"SPARK_DAEMON_JAVA_OPTS": "$SPARK_DAEMON_JAVA_OPTS
          -Dspark.shuffle.service.enabled=true"}`
        :param ssh_public_keys: List[str] (optional)
          SSH public key contents that will be added to each Spark node in this cluster. The corresponding
          private keys can be used to login with the user name `ubuntu` on port `2200`. Up to 10 keys can be
          specified.
        :param workload_type: :class:`WorkloadType` (optional)
        
        :returns:
          long-running operation waiter for :class:`ClusterInfo`.
          See :method:wait_get_cluster_running for more details.
        

    .. py:method:: ensure_cluster_is_running(cluster_id)

        Usage:

        .. code-block::

            import os
            
            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import compute
            
            w = WorkspaceClient()
            
            cluster_id = os.environ["TEST_DEFAULT_CLUSTER_ID"]
            
            context = w.command_execution.create(cluster_id=cluster_id, language=compute.Language.python).result()
            
            w.clusters.ensure_cluster_is_running(cluster_id)
            
            # cleanup
            w.command_execution.destroy(cluster_id=cluster_id, context_id=context.id)

        Ensures that given cluster is running, regardless of the current state

    .. py:method:: events(cluster_id [, end_time, event_types, limit, offset, order, start_time])

        Usage:

        .. code-block::

            import os
            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            latest = w.clusters.select_spark_version(latest=True)
            
            cluster_name = f'sdk-{time.time_ns()}'
            
            clstr = w.clusters.create(cluster_name=cluster_name,
                                      spark_version=latest,
                                      instance_pool_id=os.environ["TEST_INSTANCE_POOL_ID"],
                                      autotermination_minutes=15,
                                      num_workers=1).result()
            
            events = w.clusters.events(cluster_id=clstr.cluster_id)
            
            # cleanup
            w.clusters.permanent_delete(permanent_delete=clstr.cluster_id)

        List cluster activity events.
        
        Retrieves a list of events about the activity of a cluster. This API is paginated. If there are more
        events to read, the response includes all the nparameters necessary to request the next page of
        events.
        
        :param cluster_id: str
          The ID of the cluster to retrieve events about.
        :param end_time: int (optional)
          The end time in epoch milliseconds. If empty, returns events up to the current time.
        :param event_types: List[:class:`EventType`] (optional)
          An optional set of event types to filter on. If empty, all event types are returned.
        :param limit: int (optional)
          The maximum number of events to include in a page of events. Defaults to 50, and maximum allowed
          value is 500.
        :param offset: int (optional)
          The offset in the result set. Defaults to 0 (no offset). When an offset is specified and the results
          are requested in descending order, the end_time field is required.
        :param order: :class:`GetEventsOrder` (optional)
          The order to list events in; either "ASC" or "DESC". Defaults to "DESC".
        :param start_time: int (optional)
          The start time in epoch milliseconds. If empty, returns events starting from the beginning of time.
        
        :returns: Iterator over :class:`ClusterEvent`
        

    .. py:method:: get(cluster_id)

        Usage:

        .. code-block::

            import os
            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            latest = w.clusters.select_spark_version(latest=True)
            
            cluster_name = f'sdk-{time.time_ns()}'
            
            clstr = w.clusters.create(cluster_name=cluster_name,
                                      spark_version=latest,
                                      instance_pool_id=os.environ["TEST_INSTANCE_POOL_ID"],
                                      autotermination_minutes=15,
                                      num_workers=1).result()
            
            by_id = w.clusters.get(get=clstr.cluster_id)
            
            # cleanup
            w.clusters.permanent_delete(permanent_delete=clstr.cluster_id)

        Get cluster info.
        
        Retrieves the information for a cluster given its identifier. Clusters can be described while they are
        running, or up to 60 days after they are terminated.
        
        :param cluster_id: str
          The cluster about which to retrieve information.
        
        :returns: :class:`ClusterInfo`
        

    .. py:method:: list( [, can_use_client])

        Usage:

        .. code-block::

            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import compute
            
            w = WorkspaceClient()
            
            all = w.clusters.list(compute.ListClustersRequest())

        List all clusters.
        
        Return information about all pinned clusters, active clusters, up to 200 of the most recently
        terminated all-purpose clusters in the past 30 days, and up to 30 of the most recently terminated job
        clusters in the past 30 days.
        
        For example, if there is 1 pinned cluster, 4 active clusters, 45 terminated all-purpose clusters in
        the past 30 days, and 50 terminated job clusters in the past 30 days, then this API returns the 1
        pinned cluster, 4 active clusters, all 45 terminated all-purpose clusters, and the 30 most recently
        terminated job clusters.
        
        :param can_use_client: str (optional)
          Filter clusters based on what type of client it can be used for. Could be either NOTEBOOKS or JOBS.
          No input for this field will get all clusters in the workspace without filtering on its supported
          client
        
        :returns: Iterator over :class:`ClusterInfo`
        

    .. py:method:: list_node_types()

        Usage:

        .. code-block::

            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            nodes = w.clusters.list_node_types()

        List node types.
        
        Returns a list of supported Spark node types. These node types can be used to launch a cluster.
        
        :returns: :class:`ListNodeTypesResponse`
        

    .. py:method:: list_zones()

        List availability zones.
        
        Returns a list of availability zones where clusters can be created in (For example, us-west-2a). These
        zones can be used to launch a cluster.
        
        :returns: :class:`ListAvailableZonesResponse`
        

    .. py:method:: permanent_delete(cluster_id)

        Permanently delete cluster.
        
        Permanently deletes a Spark cluster. This cluster is terminated and resources are asynchronously
        removed.
        
        In addition, users will no longer see permanently deleted clusters in the cluster list, and API users
        can no longer perform any action on permanently deleted clusters.
        
        :param cluster_id: str
          The cluster to be deleted.
        
        
        

    .. py:method:: pin(cluster_id)

        Usage:

        .. code-block::

            import os
            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            latest = w.clusters.select_spark_version(latest=True)
            
            cluster_name = f'sdk-{time.time_ns()}'
            
            clstr = w.clusters.create(cluster_name=cluster_name,
                                      spark_version=latest,
                                      instance_pool_id=os.environ["TEST_INSTANCE_POOL_ID"],
                                      autotermination_minutes=15,
                                      num_workers=1).result()
            
            w.clusters.pin(pin=clstr.cluster_id)
            
            # cleanup
            w.clusters.permanent_delete(permanent_delete=clstr.cluster_id)

        Pin cluster.
        
        Pinning a cluster ensures that the cluster will always be returned by the ListClusters API. Pinning a
        cluster that is already pinned will have no effect. This API can only be called by workspace admins.
        
        :param cluster_id: str
          <needs content added>
        
        
        

    .. py:method:: resize(cluster_id [, autoscale, num_workers])

        Usage:

        .. code-block::

            import os
            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            latest = w.clusters.select_spark_version(latest=True)
            
            cluster_name = f'sdk-{time.time_ns()}'
            
            clstr = w.clusters.create(cluster_name=cluster_name,
                                      spark_version=latest,
                                      instance_pool_id=os.environ["TEST_INSTANCE_POOL_ID"],
                                      autotermination_minutes=15,
                                      num_workers=1).result()
            
            by_id = w.clusters.resize(cluster_id=clstr.cluster_id, num_workers=1).result()
            
            # cleanup
            w.clusters.permanent_delete(permanent_delete=clstr.cluster_id)

        Resize cluster.
        
        Resizes a cluster to have a desired number of workers. This will fail unless the cluster is in a
        `RUNNING` state.
        
        :param cluster_id: str
          The cluster to be resized.
        :param autoscale: :class:`AutoScale` (optional)
          Parameters needed in order to automatically scale clusters up and down based on load. Note:
          autoscaling works best with DB runtime versions 3.0 or later.
        :param num_workers: int (optional)
          Number of worker nodes that this cluster should have. A cluster has one Spark Driver and
          `num_workers` Executors for a total of `num_workers` + 1 Spark nodes.
          
          Note: When reading the properties of a cluster, this field reflects the desired number of workers
          rather than the actual current number of workers. For instance, if a cluster is resized from 5 to 10
          workers, this field will immediately be updated to reflect the target size of 10 workers, whereas
          the workers listed in `spark_info` will gradually increase from 5 to 10 as the new nodes are
          provisioned.
        
        :returns:
          long-running operation waiter for :class:`ClusterInfo`.
          See :method:wait_get_cluster_running for more details.
        

    .. py:method:: restart(cluster_id [, restart_user])

        Usage:

        .. code-block::

            import os
            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            latest = w.clusters.select_spark_version(latest=True)
            
            cluster_name = f'sdk-{time.time_ns()}'
            
            clstr = w.clusters.create(cluster_name=cluster_name,
                                      spark_version=latest,
                                      instance_pool_id=os.environ["TEST_INSTANCE_POOL_ID"],
                                      autotermination_minutes=15,
                                      num_workers=1).result()
            
            _ = w.clusters.restart(cluster_id=clstr.cluster_id).result()
            
            # cleanup
            w.clusters.permanent_delete(permanent_delete=clstr.cluster_id)

        Restart cluster.
        
        Restarts a Spark cluster with the supplied ID. If the cluster is not currently in a `RUNNING` state,
        nothing will happen.
        
        :param cluster_id: str
          The cluster to be started.
        :param restart_user: str (optional)
          <needs content added>
        
        :returns:
          long-running operation waiter for :class:`ClusterInfo`.
          See :method:wait_get_cluster_running for more details.
        

    .. py:method:: select_node_type(min_memory_gb, gb_per_core, min_cores, min_gpus, local_disk, local_disk_min_size, category, photon_worker_capable, photon_driver_capable, graviton, is_io_cache_enabled, support_port_forwarding, fleet)

        Usage:

        .. code-block::

            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            smallest = w.clusters.select_node_type(local_disk=True)

        Selects smallest available node type given the conditions.

        :param min_memory_gb: int
        :param gb_per_core: int
        :param min_cores: int
        :param min_gpus: int
        :param local_disk: bool
        :param local_disk_min_size: bool
        :param category: bool
        :param photon_worker_capable: bool
        :param photon_driver_capable: bool
        :param graviton: bool
        :param is_io_cache_enabled: bool

        :returns: `node_type` compatible string
        

    .. py:method:: select_spark_version(long_term_support, beta, latest, ml, genomics, gpu, scala, spark_version, photon, graviton)

        Usage:

        .. code-block::

            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            latest = w.clusters.select_spark_version(latest=True)

        Selects the latest Databricks Runtime Version.

        :param long_term_support: bool
        :param beta: bool
        :param latest: bool
        :param ml: bool
        :param gpu: bool
        :param scala: bool
        :param spark_version: bool
        :param photon: bool
        :param graviton: bool

        :returns: `spark_version` compatible string
        

    .. py:method:: spark_versions()

        List available Spark versions.
        
        Returns the list of available Spark versions. These versions can be used to launch a cluster.
        
        :returns: :class:`GetSparkVersionsResponse`
        

    .. py:method:: start(cluster_id)

        Usage:

        .. code-block::

            import os
            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            latest = w.clusters.select_spark_version(latest=True)
            
            cluster_name = f'sdk-{time.time_ns()}'
            
            clstr = w.clusters.create(cluster_name=cluster_name,
                                      spark_version=latest,
                                      instance_pool_id=os.environ["TEST_INSTANCE_POOL_ID"],
                                      autotermination_minutes=15,
                                      num_workers=1).result()
            
            _ = w.clusters.start(start=clstr.cluster_id).result()
            
            # cleanup
            w.clusters.permanent_delete(permanent_delete=clstr.cluster_id)

        Start terminated cluster.
        
        Starts a terminated Spark cluster with the supplied ID. This works similar to `createCluster` except:
        
        * The previous cluster id and attributes are preserved. * The cluster starts with the last specified
        cluster size. * If the previous cluster was an autoscaling cluster, the current cluster starts with
        the minimum number of nodes. * If the cluster is not currently in a `TERMINATED` state, nothing will
        happen. * Clusters launched to run a job cannot be started.
        
        :param cluster_id: str
          The cluster to be started.
        
        :returns:
          long-running operation waiter for :class:`ClusterInfo`.
          See :method:wait_get_cluster_running for more details.
        

    .. py:method:: unpin(cluster_id)

        Usage:

        .. code-block::

            import os
            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            latest = w.clusters.select_spark_version(latest=True)
            
            cluster_name = f'sdk-{time.time_ns()}'
            
            clstr = w.clusters.create(cluster_name=cluster_name,
                                      spark_version=latest,
                                      instance_pool_id=os.environ["TEST_INSTANCE_POOL_ID"],
                                      autotermination_minutes=15,
                                      num_workers=1).result()
            
            w.clusters.unpin(unpin=clstr.cluster_id)
            
            # cleanup
            w.clusters.permanent_delete(permanent_delete=clstr.cluster_id)

        Unpin cluster.
        
        Unpinning a cluster will allow the cluster to eventually be removed from the ListClusters API.
        Unpinning a cluster that is not pinned will have no effect. This API can only be called by workspace
        admins.
        
        :param cluster_id: str
          <needs content added>
        
        
        