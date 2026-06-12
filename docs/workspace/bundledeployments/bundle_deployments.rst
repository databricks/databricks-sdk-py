``w.bundle_deployments``: BundleDeployments.v1
==============================================
.. currentmodule:: databricks.sdk.service.bundledeployments

.. py:class:: BundleDeploymentsAPI

    Service for managing bundle deployment metadata.

    .. py:method:: complete_version(name: str, completion_reason: VersionComplete [, force: Optional[bool]]) -> Version

        Marks a version as complete and releases the deployment lock.

        The server atomically: 1. Sets the version status to the provided terminal status. 2. Sets
        `complete_time` to the current server timestamp. 3. Releases the lock on the parent deployment. 4.
        Updates the parent deployment's `status` and `last_version_id`.

        :param name: str
          The name of the version to complete. Format: deployments/{deployment_id}/versions/{version_id}
        :param completion_reason: :class:`VersionComplete`
          The reason for completing the version. Must be a terminal reason: VERSION_COMPLETE_SUCCESS,
          VERSION_COMPLETE_FAILURE, or VERSION_COMPLETE_FORCE_ABORT.
        :param force: bool (optional)
          If true, force-completes the version even if the caller is not the original creator. The
          completion_reason must be VERSION_COMPLETE_FORCE_ABORT when force is true.

        :returns: :class:`Version`
        

    .. py:method:: create_deployment(deployment: Deployment, deployment_id: str) -> Deployment

        Creates a new deployment in the workspace.

        The caller must provide a `deployment_id` which becomes the final component of the deployment's
        resource name. If a deployment with the same ID already exists, the server returns `ALREADY_EXISTS`.

        :param deployment: :class:`Deployment`
          The deployment to create.
        :param deployment_id: str
          The ID to use for the deployment, which will become the final component of the deployment's resource
          name (i.e. `deployments/{deployment_id}`).

        :returns: :class:`Deployment`
        

    .. py:method:: create_operation(parent: str, operation: Operation, resource_key: str) -> Operation

        Creates a resource operation under a version.

        The caller must provide a `resource_key` which becomes the final component of the operation's name. If
        an operation with the same key already exists under the version, the server returns `ALREADY_EXISTS`.

        On success the server also updates the corresponding deployment-level Resource (creating it if this is
        the first operation for that resource_key, or removing it if action_type is DELETE).

        :param parent: str
          The parent version where this operation will be recorded. Format:
          deployments/{deployment_id}/versions/{version_id}
        :param operation: :class:`Operation`
          The resource operation to create.
        :param resource_key: str
          The key identifying the resource this operation applies to. Becomes the final component of the
          operation's name.

        :returns: :class:`Operation`
        

    .. py:method:: create_version(parent: str, version: Version, version_id: str) -> Version

        Creates a new version under a deployment.

        Creating a version acquires an exclusive lock on the deployment, preventing concurrent deploys. The
        caller provides a `version_id` which the server validates equals `last_version_id + 1` on the
        deployment.

        :param parent: str
          The parent deployment where this version will be created. Format: deployments/{deployment_id}
        :param version: :class:`Version`
          The version to create.
        :param version_id: str
          The version ID the caller expects to create. The server validates this equals `last_version_id + 1`
          on the deployment. If it doesn't match, the server returns `ABORTED`.

        :returns: :class:`Version`
        

    .. py:method:: delete_deployment(name: str)

        Deletes a deployment.

        The deployment is marked as deleted. It and all its children (versions and their operations) will be
        permanently deleted after the retention policy expires. If the deployment has an in-progress version,
        the server returns `RESOURCE_CONFLICT`.

        :param name: str
          Resource name of the deployment to delete. Format: deployments/{deployment_id}


        

    .. py:method:: get_deployment(name: str) -> Deployment

        Retrieves a deployment by its resource name.

        :param name: str
          Resource name of the deployment to retrieve. Format: deployments/{deployment_id}

        :returns: :class:`Deployment`
        

    .. py:method:: get_operation(name: str) -> Operation

        Retrieves a resource operation by its resource name.

        :param name: str
          The name of the resource operation to retrieve. Format:
          deployments/{deployment_id}/versions/{version_id}/operations/{resource_key}

        :returns: :class:`Operation`
        

    .. py:method:: get_resource(name: str) -> Resource

        Retrieves a deployment resource by its resource name.

        :param name: str
          The name of the resource to retrieve. Format: deployments/{deployment_id}/resources/{resource_key}

        :returns: :class:`Resource`
        

    .. py:method:: get_version(name: str) -> Version

        Retrieves a version by its resource name.

        :param name: str
          The name of the version to retrieve. Format: deployments/{deployment_id}/versions/{version_id}

        :returns: :class:`Version`
        

    .. py:method:: heartbeat(name: str) -> HeartbeatResponse

        Sends a heartbeat to renew the lock held by a version.

        The server validates that the version is the active (non-terminal) version on the parent deployment
        and resets the lock expiry. If the lock has already expired or the version is no longer active, the
        server returns `ABORTED`.

        :param name: str
          The version whose lock to renew. Format: deployments/{deployment_id}/versions/{version_id}

        :returns: :class:`HeartbeatResponse`
        

    .. py:method:: list_deployments( [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[Deployment]

        Lists deployments in the workspace.

        :param page_size: int (optional)
          The maximum number of deployments to return. The service may return fewer than this value. If
          unspecified, at most 50 deployments will be returned. The maximum value is 1000; values above 1000
          will be coerced to 1000.
        :param page_token: str (optional)
          A page token, received from a previous `ListDeployments` call. Provide this to retrieve the
          subsequent page.

        :returns: Iterator over :class:`Deployment`
        

    .. py:method:: list_operations(parent: str [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[Operation]

        Lists resource operations under a version.

        :param parent: str
          The parent version. Format: deployments/{deployment_id}/versions/{version_id}
        :param page_size: int (optional)
          The maximum number of operations to return. The service may return fewer than this value. If
          unspecified, at most 50 operations will be returned. The maximum value is 1000; values above 1000
          will be coerced to 1000.
        :param page_token: str (optional)
          A page token, received from a previous `ListOperations` call. Provide this to retrieve the
          subsequent page.

        :returns: Iterator over :class:`Operation`
        

    .. py:method:: list_resources(parent: str [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[Resource]

        Lists resources under a deployment.

        :param parent: str
          The parent deployment. Format: deployments/{deployment_id}
        :param page_size: int (optional)
          The maximum number of resources to return. The service may return fewer than this value. If
          unspecified, at most 50 resources will be returned. The maximum value is 1000; values above 1000
          will be coerced to 1000.
        :param page_token: str (optional)
          A page token, received from a previous `ListResources` call. Provide this to retrieve the subsequent
          page.

        :returns: Iterator over :class:`Resource`
        

    .. py:method:: list_versions(parent: str [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[Version]

        Lists versions under a deployment, ordered by version_id descending (most recent first).

        :param parent: str
          The parent deployment. Format: deployments/{deployment_id}
        :param page_size: int (optional)
          The maximum number of versions to return. The service may return fewer than this value. If
          unspecified, at most 50 versions will be returned. The maximum value is 1000; values above 1000 will
          be coerced to 1000.
        :param page_token: str (optional)
          A page token, received from a previous `ListVersions` call. Provide this to retrieve the subsequent
          page.

        :returns: Iterator over :class:`Version`
        