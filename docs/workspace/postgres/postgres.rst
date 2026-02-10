``w.postgres``: Postgres
========================
.. currentmodule:: databricks.sdk.service.postgres

.. py:class:: PostgresAPI

    Use the Postgres API to create and manage Lakebase Autoscaling Postgres infrastructure, including
    projects, branches, compute endpoints, and roles.

    This API manages database infrastructure only. To query or modify data, use the Data API or direct SQL
    connections.

    **About resource IDs and names**

    Resources are identified by hierarchical resource names like
    `projects/{project_id}/branches/{branch_id}/endpoints/{endpoint_id}`. The `name` field on each resource
    contains this full path and is output-only. Note that `name` refers to this resource path, not the
    user-visible `display_name`.

    .. py:method:: create_branch(parent: str, branch: Branch, branch_id: str) -> CreateBranchOperation

        Creates a new database branch in the project.

        :param parent: str
          The Project where this Branch will be created. Format: projects/{project_id}
        :param branch: :class:`Branch`
          The Branch to create.
        :param branch_id: str
          The ID to use for the Branch. This becomes the final component of the branch's resource name. The ID
          is required and must be 1-63 characters long, start with a lowercase letter, and contain only
          lowercase letters, numbers, and hyphens. For example, `development` becomes
          `projects/my-app/branches/development`.

        :returns: :class:`Operation`
        

    .. py:method:: create_endpoint(parent: str, endpoint: Endpoint, endpoint_id: str) -> CreateEndpointOperation

        Creates a new compute endpoint in the branch.

        :param parent: str
          The Branch where this Endpoint will be created. Format: projects/{project_id}/branches/{branch_id}
        :param endpoint: :class:`Endpoint`
          The Endpoint to create.
        :param endpoint_id: str
          The ID to use for the Endpoint. This becomes the final component of the endpoint's resource name.
          The ID is required and must be 1-63 characters long, start with a lowercase letter, and contain only
          lowercase letters, numbers, and hyphens. For example, `primary` becomes
          `projects/my-app/branches/development/endpoints/primary`.

        :returns: :class:`Operation`
        

    .. py:method:: create_project(project: Project, project_id: str) -> CreateProjectOperation

        Creates a new Lakebase Autoscaling Postgres database project, which contains branches and compute
        endpoints.

        :param project: :class:`Project`
          The Project to create.
        :param project_id: str
          The ID to use for the Project. This becomes the final component of the project's resource name. The
          ID is required and must be 1-63 characters long, start with a lowercase letter, and contain only
          lowercase letters, numbers, and hyphens. For example, `my-app` becomes `projects/my-app`.

        :returns: :class:`Operation`
        

    .. py:method:: create_role(parent: str, role: Role [, role_id: Optional[str]]) -> CreateRoleOperation

        Creates a new Postgres role in the branch.

        :param parent: str
          The Branch where this Role is created. Format: projects/{project_id}/branches/{branch_id}
        :param role: :class:`Role`
          The desired specification of a Role.
        :param role_id: str (optional)
          The ID to use for the Role, which will become the final component of the role's resource name. This
          ID becomes the role in Postgres.

          This value should be 4-63 characters, and valid characters are lowercase letters, numbers, and
          hyphens, as defined by RFC 1123.

          If role_id is not specified in the request, it is generated automatically.

        :returns: :class:`Operation`
        

    .. py:method:: delete_branch(name: str) -> DeleteBranchOperation

        Deletes the specified database branch.

        :param name: str
          The full resource path of the branch to delete. Format: projects/{project_id}/branches/{branch_id}

        :returns: :class:`Operation`
        

    .. py:method:: delete_endpoint(name: str) -> DeleteEndpointOperation

        Deletes the specified compute endpoint.

        :param name: str
          The full resource path of the endpoint to delete. Format:
          projects/{project_id}/branches/{branch_id}/endpoints/{endpoint_id}

        :returns: :class:`Operation`
        

    .. py:method:: delete_project(name: str) -> DeleteProjectOperation

        Deletes the specified database project.

        :param name: str
          The full resource path of the project to delete. Format: projects/{project_id}

        :returns: :class:`Operation`
        

    .. py:method:: delete_role(name: str [, reassign_owned_to: Optional[str]]) -> DeleteRoleOperation

        Deletes the specified Postgres role.

        :param name: str
          The full resource path of the role to delete. Format:
          projects/{project_id}/branches/{branch_id}/roles/{role_id}
        :param reassign_owned_to: str (optional)
          Reassign objects. If this is set, all objects owned by the role are reassigned to the role specified
          in this parameter.

          NOTE: setting this requires spinning up a compute to succeed, since it involves running SQL queries.

          TODO: #LKB-7187 implement reassign_owned_to on LBM side. This might end-up being a synchronous query
          when this parameter is used.

        :returns: :class:`Operation`
        

    .. py:method:: generate_database_credential(endpoint: str [, claims: Optional[List[RequestedClaims]]]) -> DatabaseCredential

        Generate OAuth credentials for a Postgres database.

        :param endpoint: str
          This field is not yet supported. The endpoint for which this credential will be generated. Format:
          projects/{project_id}/branches/{branch_id}/endpoints/{endpoint_id}
        :param claims: List[:class:`RequestedClaims`] (optional)
          The returned token will be scoped to UC tables with the specified permissions.

        :returns: :class:`DatabaseCredential`
        

    .. py:method:: get_branch(name: str) -> Branch

        Retrieves information about the specified database branch.

        :param name: str
          The full resource path of the branch to retrieve. Format: projects/{project_id}/branches/{branch_id}

        :returns: :class:`Branch`
        

    .. py:method:: get_endpoint(name: str) -> Endpoint

        Retrieves information about the specified compute endpoint, including its connection details and
        operational state.

        :param name: str
          The full resource path of the endpoint to retrieve. Format:
          projects/{project_id}/branches/{branch_id}/endpoints/{endpoint_id}

        :returns: :class:`Endpoint`
        

    .. py:method:: get_operation(name: str) -> Operation

        Retrieves the status of a long-running operation.

        :param name: str
          The name of the operation resource.

        :returns: :class:`Operation`
        

    .. py:method:: get_project(name: str) -> Project

        Retrieves information about the specified database project.

        :param name: str
          The full resource path of the project to retrieve. Format: projects/{project_id}

        :returns: :class:`Project`
        

    .. py:method:: get_role(name: str) -> Role

        Retrieves information about the specified Postgres role, including its authentication method and
        permissions.

        :param name: str
          The full resource path of the role to retrieve. Format:
          projects/{project_id}/branches/{branch_id}/roles/{role_id}

        :returns: :class:`Role`
        

    .. py:method:: list_branches(parent: str [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[Branch]

        Returns a paginated list of database branches in the project.

        :param parent: str
          The Project that owns this collection of branches. Format: projects/{project_id}
        :param page_size: int (optional)
          Upper bound for items returned. Cannot be negative.
        :param page_token: str (optional)
          Page token from a previous response. If not provided, returns the first page.

        :returns: Iterator over :class:`Branch`
        

    .. py:method:: list_endpoints(parent: str [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[Endpoint]

        Returns a paginated list of compute endpoints in the branch.

        :param parent: str
          The Branch that owns this collection of endpoints. Format:
          projects/{project_id}/branches/{branch_id}
        :param page_size: int (optional)
          Upper bound for items returned. Cannot be negative.
        :param page_token: str (optional)
          Page token from a previous response. If not provided, returns the first page.

        :returns: Iterator over :class:`Endpoint`
        

    .. py:method:: list_projects( [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[Project]

        Returns a paginated list of database projects in the workspace that the user has permission to access.

        :param page_size: int (optional)
          Upper bound for items returned. Cannot be negative.
        :param page_token: str (optional)
          Page token from a previous response. If not provided, returns the first page.

        :returns: Iterator over :class:`Project`
        

    .. py:method:: list_roles(parent: str [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[Role]

        Returns a paginated list of Postgres roles in the branch.

        :param parent: str
          The Branch that owns this collection of roles. Format: projects/{project_id}/branches/{branch_id}
        :param page_size: int (optional)
          Upper bound for items returned. Cannot be negative.
        :param page_token: str (optional)
          Page token from a previous response. If not provided, returns the first page.

        :returns: Iterator over :class:`Role`
        

    .. py:method:: update_branch(name: str, branch: Branch, update_mask: FieldMask) -> UpdateBranchOperation

        Updates the specified database branch. You can set this branch as the project's default branch, or
        protect/unprotect it.

        :param name: str
          Output only. The full resource path of the branch. Format:
          projects/{project_id}/branches/{branch_id}
        :param branch: :class:`Branch`
          The Branch to update.

          The branch's `name` field is used to identify the branch to update. Format:
          projects/{project_id}/branches/{branch_id}
        :param update_mask: FieldMask
          The list of fields to update. If unspecified, all fields will be updated when possible.

        :returns: :class:`Operation`
        

    .. py:method:: update_endpoint(name: str, endpoint: Endpoint, update_mask: FieldMask) -> UpdateEndpointOperation

        Updates the specified compute endpoint. You can update autoscaling limits, suspend timeout, or
        enable/disable the compute endpoint.

        :param name: str
          Output only. The full resource path of the endpoint. Format:
          projects/{project_id}/branches/{branch_id}/endpoints/{endpoint_id}
        :param endpoint: :class:`Endpoint`
          The Endpoint to update.

          The endpoint's `name` field is used to identify the endpoint to update. Format:
          projects/{project_id}/branches/{branch_id}/endpoints/{endpoint_id}
        :param update_mask: FieldMask
          The list of fields to update. If unspecified, all fields will be updated when possible.

        :returns: :class:`Operation`
        

    .. py:method:: update_project(name: str, project: Project, update_mask: FieldMask) -> UpdateProjectOperation

        Updates the specified database project.

        :param name: str
          Output only. The full resource path of the project. Format: projects/{project_id}
        :param project: :class:`Project`
          The Project to update.

          The project's `name` field is used to identify the project to update. Format: projects/{project_id}
        :param update_mask: FieldMask
          The list of fields to update. If unspecified, all fields will be updated when possible.

        :returns: :class:`Operation`
        