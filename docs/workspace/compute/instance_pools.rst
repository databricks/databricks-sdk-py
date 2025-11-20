``w.instance_pools``: Instance Pools
====================================
.. currentmodule:: databricks.sdk.service.compute

.. py:class:: InstancePoolsAPI

    Instance Pools API are used to create, edit, delete and list instance pools by using ready-to-use cloud
    instances which reduces a cluster start and auto-scaling times.

    Databricks pools reduce cluster start and auto-scaling times by maintaining a set of idle, ready-to-use
    instances. When a cluster is attached to a pool, cluster nodes are created using the pool’s idle
    instances. If the pool has no idle instances, the pool expands by allocating a new instance from the
    instance provider in order to accommodate the cluster’s request. When a cluster releases an instance, it
    returns to the pool and is free for another cluster to use. Only clusters attached to a pool can use that
    pool’s idle instances.

    You can specify a different pool for the driver node and worker nodes, or use the same pool for both.

    Databricks does not charge DBUs while instances are idle in the pool. Instance provider billing does
    apply. See pricing.

    .. py:method:: create(instance_pool_name: str, node_type_id: str [, aws_attributes: Optional[InstancePoolAwsAttributes], azure_attributes: Optional[InstancePoolAzureAttributes], custom_tags: Optional[Dict[str, str]], disk_spec: Optional[DiskSpec], enable_auto_alternate_node_types: Optional[bool], enable_elastic_disk: Optional[bool], gcp_attributes: Optional[InstancePoolGcpAttributes], idle_instance_autotermination_minutes: Optional[int], max_capacity: Optional[int], min_idle_instances: Optional[int], node_type_flexibility: Optional[NodeTypeFlexibility], preloaded_docker_images: Optional[List[DockerImage]], preloaded_spark_versions: Optional[List[str]], remote_disk_throughput: Optional[int], total_initial_remote_disk_size: Optional[int]]) -> CreateInstancePoolResponse


        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            smallest = w.clusters.select_node_type(local_disk=True)
            
            created = w.instance_pools.create(instance_pool_name=f"sdk-{time.time_ns()}", node_type_id=smallest)
            
            # cleanup
            w.instance_pools.delete(instance_pool_id=created.instance_pool_id)

        Creates a new instance pool using idle and ready-to-use cloud instances.

        :param instance_pool_name: str
          Pool name requested by the user. Pool name must be unique. Length must be between 1 and 100
          characters.
        :param node_type_id: str
          This field encodes, through a single value, the resources available to each of the Spark nodes in
          this cluster. For example, the Spark nodes can be provisioned and optimized for memory or compute
          intensive workloads. A list of available node types can be retrieved by using the
          :method:clusters/listNodeTypes API call.
        :param aws_attributes: :class:`InstancePoolAwsAttributes` (optional)
          Attributes related to instance pools running on Amazon Web Services. If not specified at pool
          creation, a set of default values will be used.
        :param azure_attributes: :class:`InstancePoolAzureAttributes` (optional)
          Attributes related to instance pools running on Azure. If not specified at pool creation, a set of
          default values will be used.
        :param custom_tags: Dict[str,str] (optional)
          Additional tags for pool resources. Databricks will tag all pool resources (e.g., AWS instances and
          EBS volumes) with these tags in addition to `default_tags`. Notes:

          - Currently, Databricks allows at most 45 custom tags
        :param disk_spec: :class:`DiskSpec` (optional)
          Defines the specification of the disks that will be attached to all spark containers.
        :param enable_auto_alternate_node_types: bool (optional)
          For pools with node type flexibility (Fleet-V2), whether auto generated alternate node type ids are
          enabled. This field should not be true if node_type_flexibility is set.
        :param enable_elastic_disk: bool (optional)
          Autoscaling Local Storage: when enabled, this instances in this pool will dynamically acquire
          additional disk space when its Spark workers are running low on disk space. In AWS, this feature
          requires specific AWS permissions to function correctly - refer to the User Guide for more details.
        :param gcp_attributes: :class:`InstancePoolGcpAttributes` (optional)
          Attributes related to instance pools running on Google Cloud Platform. If not specified at pool
          creation, a set of default values will be used.
        :param idle_instance_autotermination_minutes: int (optional)
          Automatically terminates the extra instances in the pool cache after they are inactive for this time
          in minutes if min_idle_instances requirement is already met. If not set, the extra pool instances
          will be automatically terminated after a default timeout. If specified, the threshold must be
          between 0 and 10000 minutes. Users can also set this value to 0 to instantly remove idle instances
          from the cache if min cache size could still hold.
        :param max_capacity: int (optional)
          Maximum number of outstanding instances to keep in the pool, including both instances used by
          clusters and idle instances. Clusters that require further instance provisioning will fail during
          upsize requests.
        :param min_idle_instances: int (optional)
          Minimum number of idle instances to keep in the instance pool
        :param node_type_flexibility: :class:`NodeTypeFlexibility` (optional)
          For pools with node type flexibility (Fleet-V2), this object contains the information about the
          alternate node type ids to use when attempting to launch a cluster if the node type id is not
          available. This field should not be set if enable_auto_alternate_node_types is true.
        :param preloaded_docker_images: List[:class:`DockerImage`] (optional)
          Custom Docker Image BYOC
        :param preloaded_spark_versions: List[str] (optional)
          A list containing at most one preloaded Spark image version for the pool. Pool-backed clusters
          started with the preloaded Spark version will start faster. A list of available Spark versions can
          be retrieved by using the :method:clusters/sparkVersions API call.
        :param remote_disk_throughput: int (optional)
          If set, what the configurable throughput (in Mb/s) for the remote disk is. Currently only supported
          for GCP HYPERDISK_BALANCED types.
        :param total_initial_remote_disk_size: int (optional)
          If set, what the total initial volume size (in GB) of the remote disks should be. Currently only
          supported for GCP HYPERDISK_BALANCED types.

        :returns: :class:`CreateInstancePoolResponse`
        

    .. py:method:: delete(instance_pool_id: str)

        Deletes the instance pool permanently. The idle instances in the pool are terminated asynchronously.

        :param instance_pool_id: str
          The instance pool to be terminated.


        

    .. py:method:: edit(instance_pool_id: str, instance_pool_name: str, node_type_id: str [, custom_tags: Optional[Dict[str, str]], enable_auto_alternate_node_types: Optional[bool], idle_instance_autotermination_minutes: Optional[int], max_capacity: Optional[int], min_idle_instances: Optional[int], node_type_flexibility: Optional[NodeTypeFlexibility], remote_disk_throughput: Optional[int], total_initial_remote_disk_size: Optional[int]])


        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            smallest = w.clusters.select_node_type(local_disk=True)
            
            created = w.instance_pools.create(instance_pool_name=f"sdk-{time.time_ns()}", node_type_id=smallest)
            
            w.instance_pools.edit(
                instance_pool_id=created.instance_pool_id,
                instance_pool_name=f"sdk-{time.time_ns()}",
                node_type_id=smallest,
            )
            
            # cleanup
            w.instance_pools.delete(instance_pool_id=created.instance_pool_id)

        Modifies the configuration of an existing instance pool.

        :param instance_pool_id: str
          Instance pool ID
        :param instance_pool_name: str
          Pool name requested by the user. Pool name must be unique. Length must be between 1 and 100
          characters.
        :param node_type_id: str
          This field encodes, through a single value, the resources available to each of the Spark nodes in
          this cluster. For example, the Spark nodes can be provisioned and optimized for memory or compute
          intensive workloads. A list of available node types can be retrieved by using the
          :method:clusters/listNodeTypes API call.
        :param custom_tags: Dict[str,str] (optional)
          Additional tags for pool resources. Databricks will tag all pool resources (e.g., AWS instances and
          EBS volumes) with these tags in addition to `default_tags`. Notes:

          - Currently, Databricks allows at most 45 custom tags
        :param enable_auto_alternate_node_types: bool (optional)
          For pools with node type flexibility (Fleet-V2), whether auto generated alternate node type ids are
          enabled. This field should not be true if node_type_flexibility is set.
        :param idle_instance_autotermination_minutes: int (optional)
          Automatically terminates the extra instances in the pool cache after they are inactive for this time
          in minutes if min_idle_instances requirement is already met. If not set, the extra pool instances
          will be automatically terminated after a default timeout. If specified, the threshold must be
          between 0 and 10000 minutes. Users can also set this value to 0 to instantly remove idle instances
          from the cache if min cache size could still hold.
        :param max_capacity: int (optional)
          Maximum number of outstanding instances to keep in the pool, including both instances used by
          clusters and idle instances. Clusters that require further instance provisioning will fail during
          upsize requests.
        :param min_idle_instances: int (optional)
          Minimum number of idle instances to keep in the instance pool
        :param node_type_flexibility: :class:`NodeTypeFlexibility` (optional)
          For pools with node type flexibility (Fleet-V2), this object contains the information about the
          alternate node type ids to use when attempting to launch a cluster if the node type id is not
          available. This field should not be set if enable_auto_alternate_node_types is true.
        :param remote_disk_throughput: int (optional)
          If set, what the configurable throughput (in Mb/s) for the remote disk is. Currently only supported
          for GCP HYPERDISK_BALANCED types.
        :param total_initial_remote_disk_size: int (optional)
          If set, what the total initial volume size (in GB) of the remote disks should be. Currently only
          supported for GCP HYPERDISK_BALANCED types.


        

    .. py:method:: get(instance_pool_id: str) -> GetInstancePool


        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            smallest = w.clusters.select_node_type(local_disk=True)
            
            created = w.instance_pools.create(instance_pool_name=f"sdk-{time.time_ns()}", node_type_id=smallest)
            
            by_id = w.instance_pools.get(instance_pool_id=created.instance_pool_id)
            
            # cleanup
            w.instance_pools.delete(instance_pool_id=created.instance_pool_id)

        Retrieve the information for an instance pool based on its identifier.

        :param instance_pool_id: str
          The canonical unique identifier for the instance pool.

        :returns: :class:`GetInstancePool`
        

    .. py:method:: get_permission_levels(instance_pool_id: str) -> GetInstancePoolPermissionLevelsResponse

        Gets the permission levels that a user can have on an object.

        :param instance_pool_id: str
          The instance pool for which to get or manage permissions.

        :returns: :class:`GetInstancePoolPermissionLevelsResponse`
        

    .. py:method:: get_permissions(instance_pool_id: str) -> InstancePoolPermissions

        Gets the permissions of an instance pool. Instance pools can inherit permissions from their root
        object.

        :param instance_pool_id: str
          The instance pool for which to get or manage permissions.

        :returns: :class:`InstancePoolPermissions`
        

    .. py:method:: list() -> Iterator[InstancePoolAndStats]


        Usage:

        .. code-block::

            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            all = w.instance_pools.list()

        Gets a list of instance pools with their statistics.


        :returns: Iterator over :class:`InstancePoolAndStats`
        

    .. py:method:: set_permissions(instance_pool_id: str [, access_control_list: Optional[List[InstancePoolAccessControlRequest]]]) -> InstancePoolPermissions

        Sets permissions on an object, replacing existing permissions if they exist. Deletes all direct
        permissions if none are specified. Objects can inherit permissions from their root object.

        :param instance_pool_id: str
          The instance pool for which to get or manage permissions.
        :param access_control_list: List[:class:`InstancePoolAccessControlRequest`] (optional)

        :returns: :class:`InstancePoolPermissions`
        

    .. py:method:: update_permissions(instance_pool_id: str [, access_control_list: Optional[List[InstancePoolAccessControlRequest]]]) -> InstancePoolPermissions

        Updates the permissions on an instance pool. Instance pools can inherit permissions from their root
        object.

        :param instance_pool_id: str
          The instance pool for which to get or manage permissions.
        :param access_control_list: List[:class:`InstancePoolAccessControlRequest`] (optional)

        :returns: :class:`InstancePoolPermissions`
        