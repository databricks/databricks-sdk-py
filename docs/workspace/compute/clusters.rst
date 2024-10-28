``w.clusters``: Clusters
========================
.. currentmodule:: databricks.sdk.service.compute

.. py:class:: ClustersExt

    The Clusters API allows you to create, start, edit, list, terminate, and delete clusters.
    
    Databricks maps cluster node instance types to compute units known as DBUs. See the instance type pricing
    page for a list of the supported instance types and their corresponding DBUs.
    
    A Databricks cluster is a set of computation resources and configurations on which you run data
    engineering, data science, and data analytics workloads, such as production ETL pipelines, streaming
    analytics, ad-hoc analytics, and machine learning.
    
    You run these workloads as a set of commands in a notebook or as an automated job. Databricks makes a
    distinction between all-purpose clusters and job clusters. You use all-purpose clusters to analyze data
    collaboratively using interactive notebooks. You use job clusters to run fast and robust automated jobs.
    
    You can create an all-purpose cluster using the UI, CLI, or REST API. You can manually terminate and
    restart an all-purpose cluster. Multiple users can share such clusters to do collaborative interactive
    analysis.
    
    IMPORTANT: Databricks retains cluster configuration information for terminated clusters for 30 days. To
    keep an all-purpose cluster configuration even after it has been terminated for more than 30 days, an
    administrator can pin a cluster to the cluster list.

    .. py:method:: change_owner(cluster_id: str, owner_username: str)


        Usage:

        .. code-block::

            import os
            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            latest = w.clusters.select_spark_version(latest=True, long_term_support=True)
            
            cluster_name = f'sdk-{time.time_ns()}'
            
            other_owner = w.users.create(user_name=f'sdk-{time.time_ns()}@example.com')
            
            clstr = w.clusters.create(cluster_name=cluster_name,
                                      spark_version=latest,
                                      instance_pool_id=os.environ["TEST_INSTANCE_POOL_ID"],
                                      autotermination_minutes=15,
                                      num_workers=1).result()
            
            w.clusters.change_owner(cluster_id=clstr.cluster_id, owner_username=other_owner.user_name)
            
            # cleanup
            w.users.delete(id=other_owner.id)
            w.clusters.permanent_delete(cluster_id=clstr.cluster_id)

        Change cluster owner.
        
        Change the owner of the cluster. You must be an admin and the cluster must be terminated to perform
        this operation. The service principal application ID can be supplied as an argument to
        `owner_username`.
        
        :param cluster_id: str
          <needs content added>
        :param owner_username: str
          New owner of the cluster_id after this RPC.
        
        
        

    .. py:method:: create(spark_version: str [, apply_policy_default_values: Optional[bool], autoscale: Optional[AutoScale], autotermination_minutes: Optional[int], aws_attributes: Optional[AwsAttributes], azure_attributes: Optional[AzureAttributes], clone_from: Optional[CloneCluster], cluster_log_conf: Optional[ClusterLogConf], cluster_name: Optional[str], custom_tags: Optional[Dict[str, str]], data_security_mode: Optional[DataSecurityMode], docker_image: Optional[DockerImage], driver_instance_pool_id: Optional[str], driver_node_type_id: Optional[str], enable_elastic_disk: Optional[bool], enable_local_disk_encryption: Optional[bool], gcp_attributes: Optional[GcpAttributes], init_scripts: Optional[List[InitScriptInfo]], instance_pool_id: Optional[str], node_type_id: Optional[str], num_workers: Optional[int], policy_id: Optional[str], runtime_engine: Optional[RuntimeEngine], single_user_name: Optional[str], spark_conf: Optional[Dict[str, str]], spark_env_vars: Optional[Dict[str, str]], ssh_public_keys: Optional[List[str]], workload_type: Optional[WorkloadType]]) -> Wait[ClusterDetails]


        Usage:

        .. code-block::

            import os
            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            latest = w.clusters.select_spark_version(latest=True, long_term_support=True)
            
            cluster_name = f'sdk-{time.time_ns()}'
            
            clstr = w.clusters.create(cluster_name=cluster_name,
                                      spark_version=latest,
                                      instance_pool_id=os.environ["TEST_INSTANCE_POOL_ID"],
                                      autotermination_minutes=15,
                                      num_workers=1).result()
            
            # cleanup
            w.clusters.permanent_delete(cluster_id=clstr.cluster_id)

        Create new cluster.
        
        Creates a new Spark cluster. This method will acquire new instances from the cloud provider if
        necessary. Note: Databricks may not be able to acquire some of the requested nodes, due to cloud
        provider limitations (account limits, spot price, etc.) or transient network issues.
        
        If Databricks acquires at least 85% of the requested on-demand nodes, cluster creation will succeed.
        Otherwise the cluster will terminate with an informative error message.
        
        Rather than authoring the cluster's JSON definition from scratch, Databricks recommends filling out
        the [create compute UI] and then copying the generated JSON definition from the UI.
        
        [create compute UI]: https://docs.databricks.com/compute/configure.html
        
        :param spark_version: str
          The Spark version of the cluster, e.g. `3.3.x-scala2.11`. A list of available Spark versions can be
          retrieved by using the :method:clusters/sparkVersions API call.
        :param apply_policy_default_values: bool (optional)
          When set to true, fixed and default values from the policy will be used for fields that are omitted.
          When set to false, only fixed values from the policy will be applied.
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
        :param clone_from: :class:`CloneCluster` (optional)
          When specified, this clones libraries from a source cluster during the creation of a new cluster.
        :param cluster_log_conf: :class:`ClusterLogConf` (optional)
          The configuration for delivering spark logs to a long-term storage destination. Two kinds of
          destinations (dbfs and s3) are supported. Only one destination can be specified for one cluster. If
          the conf is given, the logs will be delivered to the destination every `5 mins`. The destination of
          driver logs is `$destination/$clusterId/driver`, while the destination of executor logs is
          `$destination/$clusterId/executor`.
        :param cluster_name: str (optional)
          Cluster name requested by the user. This doesn't have to be unique. If not specified at creation,
          the cluster name will be an empty string.
        :param custom_tags: Dict[str,str] (optional)
          Additional tags for cluster resources. Databricks will tag all cluster resources (e.g., AWS
          instances and EBS volumes) with these tags in addition to `default_tags`. Notes:
          
          - Currently, Databricks allows at most 45 custom tags
          
          - Clusters can only reuse cloud resources if the resources' tags are a subset of the cluster tags
        :param data_security_mode: :class:`DataSecurityMode` (optional)
          Data security mode decides what data governance model to use when accessing data from a cluster.
          
          * `NONE`: No security isolation for multiple users sharing the cluster. Data governance features are
          not available in this mode. * `SINGLE_USER`: A secure cluster that can only be exclusively used by a
          single user specified in `single_user_name`. Most programming languages, cluster features and data
          governance features are available in this mode. * `USER_ISOLATION`: A secure cluster that can be
          shared by multiple users. Cluster users are fully isolated so that they cannot see each other's data
          and credentials. Most data governance features are supported in this mode. But programming languages
          and cluster features might be limited.
          
          The following modes are deprecated starting with Databricks Runtime 15.0 and will be removed for
          future Databricks Runtime versions:
          
          * `LEGACY_TABLE_ACL`: This mode is for users migrating from legacy Table ACL clusters. *
          `LEGACY_PASSTHROUGH`: This mode is for users migrating from legacy Passthrough on high concurrency
          clusters. * `LEGACY_SINGLE_USER`: This mode is for users migrating from legacy Passthrough on
          standard clusters. * `LEGACY_SINGLE_USER_STANDARD`: This mode provides a way that doesn’t have UC
          nor passthrough enabled.
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
          Determines the cluster's runtime engine, either standard or Photon.
          
          This field is not compatible with legacy `spark_version` values that contain `-photon-`. Remove
          `-photon-` from the `spark_version` and set `runtime_engine` to `PHOTON`.
          
          If left unspecified, the runtime engine defaults to standard unless the spark_version contains
          -photon-, in which case Photon will be used.
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
          Long-running operation waiter for :class:`ClusterDetails`.
          See :method:wait_get_cluster_running for more details.
        

    .. py:method:: create_and_wait(spark_version: str [, apply_policy_default_values: Optional[bool], autoscale: Optional[AutoScale], autotermination_minutes: Optional[int], aws_attributes: Optional[AwsAttributes], azure_attributes: Optional[AzureAttributes], clone_from: Optional[CloneCluster], cluster_log_conf: Optional[ClusterLogConf], cluster_name: Optional[str], custom_tags: Optional[Dict[str, str]], data_security_mode: Optional[DataSecurityMode], docker_image: Optional[DockerImage], driver_instance_pool_id: Optional[str], driver_node_type_id: Optional[str], enable_elastic_disk: Optional[bool], enable_local_disk_encryption: Optional[bool], gcp_attributes: Optional[GcpAttributes], init_scripts: Optional[List[InitScriptInfo]], instance_pool_id: Optional[str], node_type_id: Optional[str], num_workers: Optional[int], policy_id: Optional[str], runtime_engine: Optional[RuntimeEngine], single_user_name: Optional[str], spark_conf: Optional[Dict[str, str]], spark_env_vars: Optional[Dict[str, str]], ssh_public_keys: Optional[List[str]], workload_type: Optional[WorkloadType], timeout: datetime.timedelta = 0:20:00]) -> ClusterDetails


    .. py:method:: delete(cluster_id: str) -> Wait[ClusterDetails]


        Usage:

        .. code-block::

            import os
            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            latest = w.clusters.select_spark_version(latest=True, long_term_support=True)
            
            cluster_name = f'sdk-{time.time_ns()}'
            
            clstr = w.clusters.create(cluster_name=cluster_name,
                                      spark_version=latest,
                                      instance_pool_id=os.environ["TEST_INSTANCE_POOL_ID"],
                                      autotermination_minutes=15,
                                      num_workers=1).result()
            
            _ = w.clusters.delete(cluster_id=clstr.cluster_id).result()
            
            # cleanup
            w.clusters.permanent_delete(cluster_id=clstr.cluster_id)

        Terminate cluster.
        
        Terminates the Spark cluster with the specified ID. The cluster is removed asynchronously. Once the
        termination has completed, the cluster will be in a `TERMINATED` state. If the cluster is already in a
        `TERMINATING` or `TERMINATED` state, nothing will happen.
        
        :param cluster_id: str
          The cluster to be terminated.
        
        :returns:
          Long-running operation waiter for :class:`ClusterDetails`.
          See :method:wait_get_cluster_terminated for more details.
        

    .. py:method:: delete_and_wait(cluster_id: str, timeout: datetime.timedelta = 0:20:00) -> ClusterDetails


    .. py:method:: edit(cluster_id: str, spark_version: str [, apply_policy_default_values: Optional[bool], autoscale: Optional[AutoScale], autotermination_minutes: Optional[int], aws_attributes: Optional[AwsAttributes], azure_attributes: Optional[AzureAttributes], cluster_log_conf: Optional[ClusterLogConf], cluster_name: Optional[str], custom_tags: Optional[Dict[str, str]], data_security_mode: Optional[DataSecurityMode], docker_image: Optional[DockerImage], driver_instance_pool_id: Optional[str], driver_node_type_id: Optional[str], enable_elastic_disk: Optional[bool], enable_local_disk_encryption: Optional[bool], gcp_attributes: Optional[GcpAttributes], init_scripts: Optional[List[InitScriptInfo]], instance_pool_id: Optional[str], node_type_id: Optional[str], num_workers: Optional[int], policy_id: Optional[str], runtime_engine: Optional[RuntimeEngine], single_user_name: Optional[str], spark_conf: Optional[Dict[str, str]], spark_env_vars: Optional[Dict[str, str]], ssh_public_keys: Optional[List[str]], workload_type: Optional[WorkloadType]]) -> Wait[ClusterDetails]


        Usage:

        .. code-block::

            import os
            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            cluster_name = f'sdk-{time.time_ns()}'
            
            latest = w.clusters.select_spark_version(latest=True, long_term_support=True)
            
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
            w.clusters.permanent_delete(cluster_id=clstr.cluster_id)

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
          When set to true, fixed and default values from the policy will be used for fields that are omitted.
          When set to false, only fixed values from the policy will be applied.
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
        :param custom_tags: Dict[str,str] (optional)
          Additional tags for cluster resources. Databricks will tag all cluster resources (e.g., AWS
          instances and EBS volumes) with these tags in addition to `default_tags`. Notes:
          
          - Currently, Databricks allows at most 45 custom tags
          
          - Clusters can only reuse cloud resources if the resources' tags are a subset of the cluster tags
        :param data_security_mode: :class:`DataSecurityMode` (optional)
          Data security mode decides what data governance model to use when accessing data from a cluster.
          
          * `NONE`: No security isolation for multiple users sharing the cluster. Data governance features are
          not available in this mode. * `SINGLE_USER`: A secure cluster that can only be exclusively used by a
          single user specified in `single_user_name`. Most programming languages, cluster features and data
          governance features are available in this mode. * `USER_ISOLATION`: A secure cluster that can be
          shared by multiple users. Cluster users are fully isolated so that they cannot see each other's data
          and credentials. Most data governance features are supported in this mode. But programming languages
          and cluster features might be limited.
          
          The following modes are deprecated starting with Databricks Runtime 15.0 and will be removed for
          future Databricks Runtime versions:
          
          * `LEGACY_TABLE_ACL`: This mode is for users migrating from legacy Table ACL clusters. *
          `LEGACY_PASSTHROUGH`: This mode is for users migrating from legacy Passthrough on high concurrency
          clusters. * `LEGACY_SINGLE_USER`: This mode is for users migrating from legacy Passthrough on
          standard clusters. * `LEGACY_SINGLE_USER_STANDARD`: This mode provides a way that doesn’t have UC
          nor passthrough enabled.
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
          Determines the cluster's runtime engine, either standard or Photon.
          
          This field is not compatible with legacy `spark_version` values that contain `-photon-`. Remove
          `-photon-` from the `spark_version` and set `runtime_engine` to `PHOTON`.
          
          If left unspecified, the runtime engine defaults to standard unless the spark_version contains
          -photon-, in which case Photon will be used.
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
          Long-running operation waiter for :class:`ClusterDetails`.
          See :method:wait_get_cluster_running for more details.
        

    .. py:method:: edit_and_wait(cluster_id: str, spark_version: str [, apply_policy_default_values: Optional[bool], autoscale: Optional[AutoScale], autotermination_minutes: Optional[int], aws_attributes: Optional[AwsAttributes], azure_attributes: Optional[AzureAttributes], cluster_log_conf: Optional[ClusterLogConf], cluster_name: Optional[str], custom_tags: Optional[Dict[str, str]], data_security_mode: Optional[DataSecurityMode], docker_image: Optional[DockerImage], driver_instance_pool_id: Optional[str], driver_node_type_id: Optional[str], enable_elastic_disk: Optional[bool], enable_local_disk_encryption: Optional[bool], gcp_attributes: Optional[GcpAttributes], init_scripts: Optional[List[InitScriptInfo]], instance_pool_id: Optional[str], node_type_id: Optional[str], num_workers: Optional[int], policy_id: Optional[str], runtime_engine: Optional[RuntimeEngine], single_user_name: Optional[str], spark_conf: Optional[Dict[str, str]], spark_env_vars: Optional[Dict[str, str]], ssh_public_keys: Optional[List[str]], workload_type: Optional[WorkloadType], timeout: datetime.timedelta = 0:20:00]) -> ClusterDetails


    .. py:method:: ensure_cluster_is_running(cluster_id: str)


        Usage:

        .. code-block::

            import os
            
            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import compute
            
            w = WorkspaceClient()
            
            cluster_id = os.environ["TEST_DEFAULT_CLUSTER_ID"]
            
            context = w.command_execution.create(cluster_id=cluster_id, language=compute.Language.PYTHON).result()
            
            w.clusters.ensure_cluster_is_running(cluster_id)
            
            # cleanup
            w.command_execution.destroy(cluster_id=cluster_id, context_id=context.id)

        Ensures that given cluster is running, regardless of the current state

    .. py:method:: events(cluster_id: str [, end_time: Optional[int], event_types: Optional[List[EventType]], limit: Optional[int], offset: Optional[int], order: Optional[GetEventsOrder], start_time: Optional[int]]) -> Iterator[ClusterEvent]


        Usage:

        .. code-block::

            import os
            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            latest = w.clusters.select_spark_version(latest=True, long_term_support=True)
            
            cluster_name = f'sdk-{time.time_ns()}'
            
            clstr = w.clusters.create(cluster_name=cluster_name,
                                      spark_version=latest,
                                      instance_pool_id=os.environ["TEST_INSTANCE_POOL_ID"],
                                      autotermination_minutes=15,
                                      num_workers=1).result()
            
            events = w.clusters.events(cluster_id=clstr.cluster_id)
            
            # cleanup
            w.clusters.permanent_delete(cluster_id=clstr.cluster_id)

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
        

    .. py:method:: get(cluster_id: str) -> ClusterDetails


        Usage:

        .. code-block::

            import os
            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            latest = w.clusters.select_spark_version(latest=True, long_term_support=True)
            
            cluster_name = f'sdk-{time.time_ns()}'
            
            clstr = w.clusters.create(cluster_name=cluster_name,
                                      spark_version=latest,
                                      instance_pool_id=os.environ["TEST_INSTANCE_POOL_ID"],
                                      autotermination_minutes=15,
                                      num_workers=1).result()
            
            by_id = w.clusters.get(cluster_id=clstr.cluster_id)
            
            # cleanup
            w.clusters.permanent_delete(cluster_id=clstr.cluster_id)

        Get cluster info.
        
        Retrieves the information for a cluster given its identifier. Clusters can be described while they are
        running, or up to 60 days after they are terminated.
        
        :param cluster_id: str
          The cluster about which to retrieve information.
        
        :returns: :class:`ClusterDetails`
        

    .. py:method:: get_permission_levels(cluster_id: str) -> GetClusterPermissionLevelsResponse

        Get cluster permission levels.
        
        Gets the permission levels that a user can have on an object.
        
        :param cluster_id: str
          The cluster for which to get or manage permissions.
        
        :returns: :class:`GetClusterPermissionLevelsResponse`
        

    .. py:method:: get_permissions(cluster_id: str) -> ClusterPermissions

        Get cluster permissions.
        
        Gets the permissions of a cluster. Clusters can inherit permissions from their root object.
        
        :param cluster_id: str
          The cluster for which to get or manage permissions.
        
        :returns: :class:`ClusterPermissions`
        

    .. py:method:: list( [, filter_by: Optional[ListClustersFilterBy], page_size: Optional[int], page_token: Optional[str], sort_by: Optional[ListClustersSortBy]]) -> Iterator[ClusterDetails]


        Usage:

        .. code-block::

            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import compute
            
            w = WorkspaceClient()
            
            all = w.clusters.list(compute.ListClustersRequest())

        List clusters.
        
        Return information about all pinned and active clusters, and all clusters terminated within the last
        30 days. Clusters terminated prior to this period are not included.
        
        :param filter_by: :class:`ListClustersFilterBy` (optional)
          Filters to apply to the list of clusters.
        :param page_size: int (optional)
          Use this field to specify the maximum number of results to be returned by the server. The server may
          further constrain the maximum number of results returned in a single page.
        :param page_token: str (optional)
          Use next_page_token or prev_page_token returned from the previous request to list the next or
          previous page of clusters respectively.
        :param sort_by: :class:`ListClustersSortBy` (optional)
          Sort the list of clusters by a specific criteria.
        
        :returns: Iterator over :class:`ClusterDetails`
        

    .. py:method:: list_node_types() -> ListNodeTypesResponse


        Usage:

        .. code-block::

            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            nodes = w.clusters.list_node_types()

        List node types.
        
        Returns a list of supported Spark node types. These node types can be used to launch a cluster.
        
        :returns: :class:`ListNodeTypesResponse`
        

    .. py:method:: list_zones() -> ListAvailableZonesResponse

        List availability zones.
        
        Returns a list of availability zones where clusters can be created in (For example, us-west-2a). These
        zones can be used to launch a cluster.
        
        :returns: :class:`ListAvailableZonesResponse`
        

    .. py:method:: permanent_delete(cluster_id: str)

        Permanently delete cluster.
        
        Permanently deletes a Spark cluster. This cluster is terminated and resources are asynchronously
        removed.
        
        In addition, users will no longer see permanently deleted clusters in the cluster list, and API users
        can no longer perform any action on permanently deleted clusters.
        
        :param cluster_id: str
          The cluster to be deleted.
        
        
        

    .. py:method:: pin(cluster_id: str)


        Usage:

        .. code-block::

            import os
            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            latest = w.clusters.select_spark_version(latest=True, long_term_support=True)
            
            cluster_name = f'sdk-{time.time_ns()}'
            
            clstr = w.clusters.create(cluster_name=cluster_name,
                                      spark_version=latest,
                                      instance_pool_id=os.environ["TEST_INSTANCE_POOL_ID"],
                                      autotermination_minutes=15,
                                      num_workers=1).result()
            
            w.clusters.pin(cluster_id=clstr.cluster_id)
            
            # cleanup
            w.clusters.permanent_delete(cluster_id=clstr.cluster_id)

        Pin cluster.
        
        Pinning a cluster ensures that the cluster will always be returned by the ListClusters API. Pinning a
        cluster that is already pinned will have no effect. This API can only be called by workspace admins.
        
        :param cluster_id: str
          <needs content added>
        
        
        

    .. py:method:: resize(cluster_id: str [, autoscale: Optional[AutoScale], num_workers: Optional[int]]) -> Wait[ClusterDetails]


        Usage:

        .. code-block::

            import os
            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            latest = w.clusters.select_spark_version(latest=True, long_term_support=True)
            
            cluster_name = f'sdk-{time.time_ns()}'
            
            clstr = w.clusters.create(cluster_name=cluster_name,
                                      spark_version=latest,
                                      instance_pool_id=os.environ["TEST_INSTANCE_POOL_ID"],
                                      autotermination_minutes=15,
                                      num_workers=1).result()
            
            by_id = w.clusters.resize(cluster_id=clstr.cluster_id, num_workers=1).result()
            
            # cleanup
            w.clusters.permanent_delete(cluster_id=clstr.cluster_id)

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
          Long-running operation waiter for :class:`ClusterDetails`.
          See :method:wait_get_cluster_running for more details.
        

    .. py:method:: resize_and_wait(cluster_id: str [, autoscale: Optional[AutoScale], num_workers: Optional[int], timeout: datetime.timedelta = 0:20:00]) -> ClusterDetails


    .. py:method:: restart(cluster_id: str [, restart_user: Optional[str]]) -> Wait[ClusterDetails]


        Usage:

        .. code-block::

            import os
            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            latest = w.clusters.select_spark_version(latest=True, long_term_support=True)
            
            cluster_name = f'sdk-{time.time_ns()}'
            
            clstr = w.clusters.create(cluster_name=cluster_name,
                                      spark_version=latest,
                                      instance_pool_id=os.environ["TEST_INSTANCE_POOL_ID"],
                                      autotermination_minutes=15,
                                      num_workers=1).result()
            
            _ = w.clusters.restart(cluster_id=clstr.cluster_id).result()
            
            # cleanup
            w.clusters.permanent_delete(cluster_id=clstr.cluster_id)

        Restart cluster.
        
        Restarts a Spark cluster with the supplied ID. If the cluster is not currently in a `RUNNING` state,
        nothing will happen.
        
        :param cluster_id: str
          The cluster to be started.
        :param restart_user: str (optional)
          <needs content added>
        
        :returns:
          Long-running operation waiter for :class:`ClusterDetails`.
          See :method:wait_get_cluster_running for more details.
        

    .. py:method:: restart_and_wait(cluster_id: str [, restart_user: Optional[str], timeout: datetime.timedelta = 0:20:00]) -> ClusterDetails


    .. py:method:: select_node_type(min_memory_gb: int, gb_per_core: int, min_cores: int, min_gpus: int, local_disk: bool, local_disk_min_size: int, category: str, photon_worker_capable: bool, photon_driver_capable: bool, graviton: bool, is_io_cache_enabled: bool, support_port_forwarding: bool, fleet: str) -> str


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
        :param support_port_forwarding: bool
        :param fleet: bool

        :returns: `node_type` compatible string
        

    .. py:method:: select_spark_version(long_term_support: bool = False, beta: bool = False, latest: bool = True, ml: bool = False, genomics: bool = False, gpu: bool = False, scala: str = 2.12, spark_version: str, photon: bool = False, graviton: bool = False) -> str


        Usage:

        .. code-block::

            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            latest = w.clusters.select_spark_version(latest=True, long_term_support=True)

        Selects the latest Databricks Runtime Version.

        :param long_term_support: bool
        :param beta: bool
        :param latest: bool
        :param ml: bool
        :param genomics: bool
        :param gpu: bool
        :param scala: str
        :param spark_version: str
        :param photon: bool
        :param graviton: bool

        :returns: `spark_version` compatible string
        

    .. py:method:: set_permissions(cluster_id: str [, access_control_list: Optional[List[ClusterAccessControlRequest]]]) -> ClusterPermissions

        Set cluster permissions.
        
        Sets permissions on a cluster. Clusters can inherit permissions from their root object.
        
        :param cluster_id: str
          The cluster for which to get or manage permissions.
        :param access_control_list: List[:class:`ClusterAccessControlRequest`] (optional)
        
        :returns: :class:`ClusterPermissions`
        

    .. py:method:: spark_versions() -> GetSparkVersionsResponse

        List available Spark versions.
        
        Returns the list of available Spark versions. These versions can be used to launch a cluster.
        
        :returns: :class:`GetSparkVersionsResponse`
        

    .. py:method:: start(cluster_id: str) -> Wait[ClusterDetails]


        Usage:

        .. code-block::

            import os
            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            latest = w.clusters.select_spark_version(latest=True, long_term_support=True)
            
            cluster_name = f'sdk-{time.time_ns()}'
            
            clstr = w.clusters.create(cluster_name=cluster_name,
                                      spark_version=latest,
                                      instance_pool_id=os.environ["TEST_INSTANCE_POOL_ID"],
                                      autotermination_minutes=15,
                                      num_workers=1).result()
            
            _ = w.clusters.start(cluster_id=clstr.cluster_id).result()
            
            # cleanup
            w.clusters.permanent_delete(cluster_id=clstr.cluster_id)

        Start terminated cluster.
        
        Starts a terminated Spark cluster with the supplied ID. This works similar to `createCluster` except:
        
        * The previous cluster id and attributes are preserved. * The cluster starts with the last specified
        cluster size. * If the previous cluster was an autoscaling cluster, the current cluster starts with
        the minimum number of nodes. * If the cluster is not currently in a `TERMINATED` state, nothing will
        happen. * Clusters launched to run a job cannot be started.
        
        :param cluster_id: str
          The cluster to be started.
        
        :returns:
          Long-running operation waiter for :class:`ClusterDetails`.
          See :method:wait_get_cluster_running for more details.
        

    .. py:method:: start_and_wait(cluster_id: str, timeout: datetime.timedelta = 0:20:00) -> ClusterDetails


    .. py:method:: unpin(cluster_id: str)


        Usage:

        .. code-block::

            import os
            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            latest = w.clusters.select_spark_version(latest=True, long_term_support=True)
            
            cluster_name = f'sdk-{time.time_ns()}'
            
            clstr = w.clusters.create(cluster_name=cluster_name,
                                      spark_version=latest,
                                      instance_pool_id=os.environ["TEST_INSTANCE_POOL_ID"],
                                      autotermination_minutes=15,
                                      num_workers=1).result()
            
            w.clusters.unpin(cluster_id=clstr.cluster_id)
            
            # cleanup
            w.clusters.permanent_delete(cluster_id=clstr.cluster_id)

        Unpin cluster.
        
        Unpinning a cluster will allow the cluster to eventually be removed from the ListClusters API.
        Unpinning a cluster that is not pinned will have no effect. This API can only be called by workspace
        admins.
        
        :param cluster_id: str
          <needs content added>
        
        
        

    .. py:method:: update(cluster_id: str, update_mask: str [, cluster: Optional[UpdateClusterResource]]) -> Wait[ClusterDetails]

        Update cluster configuration (partial).
        
        Updates the configuration of a cluster to match the partial set of attributes and size. Denote which
        fields to update using the `update_mask` field in the request body. A cluster can be updated if it is
        in a `RUNNING` or `TERMINATED` state. If a cluster is updated while in a `RUNNING` state, it will be
        restarted so that the new attributes can take effect. If a cluster is updated while in a `TERMINATED`
        state, it will remain `TERMINATED`. The updated attributes will take effect the next time the cluster
        is started using the `clusters/start` API. Attempts to update a cluster in any other state will be
        rejected with an `INVALID_STATE` error code. Clusters created by the Databricks Jobs service cannot be
        updated.
        
        :param cluster_id: str
          ID of the cluster.
        :param update_mask: str
          Specifies which fields of the cluster will be updated. This is required in the POST request. The
          update mask should be supplied as a single string. To specify multiple fields, separate them with
          commas (no spaces). To delete a field from a cluster configuration, add it to the `update_mask`
          string but omit it from the `cluster` object.
        :param cluster: :class:`UpdateClusterResource` (optional)
          The cluster to be updated.
        
        :returns:
          Long-running operation waiter for :class:`ClusterDetails`.
          See :method:wait_get_cluster_running for more details.
        

    .. py:method:: update_and_wait(cluster_id: str, update_mask: str [, cluster: Optional[UpdateClusterResource], timeout: datetime.timedelta = 0:20:00]) -> ClusterDetails


    .. py:method:: update_permissions(cluster_id: str [, access_control_list: Optional[List[ClusterAccessControlRequest]]]) -> ClusterPermissions

        Update cluster permissions.
        
        Updates the permissions on a cluster. Clusters can inherit permissions from their root object.
        
        :param cluster_id: str
          The cluster for which to get or manage permissions.
        :param access_control_list: List[:class:`ClusterAccessControlRequest`] (optional)
        
        :returns: :class:`ClusterPermissions`
        

    .. py:method:: wait_get_cluster_running(cluster_id: str, timeout: datetime.timedelta = 0:20:00, callback: Optional[Callable[[ClusterDetails], None]]) -> ClusterDetails


    .. py:method:: wait_get_cluster_terminated(cluster_id: str, timeout: datetime.timedelta = 0:20:00, callback: Optional[Callable[[ClusterDetails], None]]) -> ClusterDetails
