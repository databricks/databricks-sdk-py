``w.environments``: Environments.v1
===================================
.. currentmodule:: databricks.sdk.service.environments

.. py:class:: EnvironmentsAPI

    APIs to manage environment resources.

    The Environments API provides management capabilities for different types of environments including
    workspace-level base environments that define the environment version and dependencies to be used in
    serverless notebooks and jobs.

    .. py:method:: create_workspace_base_environment(workspace_base_environment: WorkspaceBaseEnvironment [, request_id: Optional[str], workspace_base_environment_id: Optional[str]]) -> CreateWorkspaceBaseEnvironmentOperation

        Creates a new WorkspaceBaseEnvironment. This is a long-running operation. The operation will
        asynchronously generate a materialized environment to optimize dependency resolution and is only
        marked as done when the materialized environment has been successfully generated or has failed.

        :param workspace_base_environment: :class:`WorkspaceBaseEnvironment`
          Required. The workspace base environment to create.
        :param request_id: str (optional)
          A unique identifier for this request. A random UUID is recommended. This request is only idempotent
          if a request_id is provided.
        :param workspace_base_environment_id: str (optional)
          The ID to use for the workspace base environment, which will become the final component of the
          resource name. This value should be 4-63 characters, and valid characters are /[a-z][0-9]-/.

        :returns: :class:`Operation`
        

    .. py:method:: delete_workspace_base_environment(name: str)

        Deletes a WorkspaceBaseEnvironment. Deleting a base environment may impact linked notebooks and jobs.
        This operation is irreversible and should be performed only when you are certain the environment is no
        longer needed.

        :param name: str
          Required. The resource name of the workspace base environment to delete. Format:
          workspace-base-environments/{workspace_base_environment}


        

    .. py:method:: get_default_workspace_base_environment(name: str) -> DefaultWorkspaceBaseEnvironment

        Gets the default WorkspaceBaseEnvironment configuration for the workspace. Returns the current default
        base environment settings for both CPU and GPU compute.

        :param name: str
          A static resource name of the default workspace base environment. Format:
          default-workspace-base-environment

        :returns: :class:`DefaultWorkspaceBaseEnvironment`
        

    .. py:method:: get_operation(name: str) -> Operation

        Gets the status of a long-running operation. Clients can use this method to poll the operation result.

        :param name: str
          The name of the operation resource.

        :returns: :class:`Operation`
        

    .. py:method:: get_workspace_base_environment(name: str) -> WorkspaceBaseEnvironment

        Retrieves a WorkspaceBaseEnvironment by its name.

        :param name: str
          Required. The resource name of the workspace base environment to retrieve. Format:
          workspace-base-environments/{workspace_base_environment}

        :returns: :class:`WorkspaceBaseEnvironment`
        

    .. py:method:: list_workspace_base_environments( [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[WorkspaceBaseEnvironment]

        Lists all WorkspaceBaseEnvironments in the workspace.

        :param page_size: int (optional)
          The maximum number of environments to return per page. Default is 1000.
        :param page_token: str (optional)
          Page token for pagination. Received from a previous ListWorkspaceBaseEnvironments call.

        :returns: Iterator over :class:`WorkspaceBaseEnvironment`
        

    .. py:method:: refresh_workspace_base_environment(name: str) -> RefreshWorkspaceBaseEnvironmentOperation

        Refreshes the materialized environment for a WorkspaceBaseEnvironment. This is a long-running
        operation. The operation will asynchronously regenerate the materialized environment and is only
        marked as done when the materialized environment has been successfully generated or has failed. The
        existing materialized environment remains available until it expires.

        :param name: str
          Required. The resource name of the workspace base environment to delete. Format:
          workspace-base-environments/{workspace_base_environment}

        :returns: :class:`Operation`
        

    .. py:method:: update_default_workspace_base_environment(name: str, default_workspace_base_environment: DefaultWorkspaceBaseEnvironment, update_mask: FieldMask) -> DefaultWorkspaceBaseEnvironment

        Updates the default WorkspaceBaseEnvironment configuration for the workspace. Sets the specified base
        environments as the workspace defaults for CPU and/or GPU compute.

        :param name: str
          The resource name of this singleton resource. Format: default-workspace-base-environment
        :param default_workspace_base_environment: :class:`DefaultWorkspaceBaseEnvironment`
          Required. The default workspace base environment configuration to update.
        :param update_mask: FieldMask
          Field mask specifying which fields to update. To specify multiple fields in the field mask, use
          comma as the separator (no space). The special value '*' indicate that all fields should be updated
          (full replacement). Valid field paths: cpu_workspace_base_environment,
          gpu_workspace_base_environment

        :returns: :class:`DefaultWorkspaceBaseEnvironment`
        

    .. py:method:: update_workspace_base_environment(name: str, workspace_base_environment: WorkspaceBaseEnvironment) -> UpdateWorkspaceBaseEnvironmentOperation

        Updates an existing WorkspaceBaseEnvironment. This is a long-running operation. The operation will
        asynchronously regenerate the materialized environment and is only marked as done when the
        materialized environment has been successfully generated or has failed. The existing materialized
        environment remains available until it expires.

        :param name: str
        :param workspace_base_environment: :class:`WorkspaceBaseEnvironment`
          Required. The workspace base environment with updated fields. The name field is used to identify the
          environment to update.

        :returns: :class:`Operation`
        