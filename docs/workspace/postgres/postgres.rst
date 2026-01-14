``w.postgres``: Postgres
========================
.. currentmodule:: databricks.sdk.service.postgres

.. py:class:: PostgresAPI

    The Postgres API provides access to a Postgres database via REST API or direct SQL.

    .. py:method:: create_branch(parent: str, branch: Branch, branch_id: str) -> CreateBranchOperation

        Create a Branch.

        :param parent: str
          The Project where this Branch will be created. Format: projects/{project_id}
        :param branch: :class:`Branch`
          The Branch to create.
        :param branch_id: str
          The ID to use for the Branch, which will become the final component of the branch's resource name.

          This value should be 4-63 characters, and valid characters are /[a-z][0-9]-/.

        :returns: :class:`Operation`
        

    .. py:method:: create_endpoint(parent: str, endpoint: Endpoint, endpoint_id: str) -> CreateEndpointOperation

        Create an Endpoint.

        :param parent: str
          The Branch where this Endpoint will be created. Format: projects/{project_id}/branches/{branch_id}
        :param endpoint: :class:`Endpoint`
          The Endpoint to create.
        :param endpoint_id: str
          The ID to use for the Endpoint, which will become the final component of the endpoint's resource
          name.

          This value should be 4-63 characters, and valid characters are /[a-z][0-9]-/.

        :returns: :class:`Operation`
        

    .. py:method:: create_project(project: Project, project_id: str) -> CreateProjectOperation

        Create a Project.

        :param project: :class:`Project`
          The Project to create.
        :param project_id: str
          The ID to use for the Project, which will become the final component of the project's resource name.

          This value should be 4-63 characters, and valid characters are /[a-z][0-9]-/.

        :returns: :class:`Operation`
        

    .. py:method:: create_role(parent: str, role: Role, role_id: str) -> CreateRoleOperation

        Create a role for a branch.

        :param parent: str
          The Branch where this Role is created. Format: projects/{project_id}/branches/{branch_id}
        :param role: :class:`Role`
          The desired specification of a Role.
        :param role_id: str
          The ID to use for the Role, which will become the final component of the branch's resource name.
          This ID becomes the role in postgres.

          This value should be 4-63 characters, and only use characters available in DNS names, as defined by
          RFC-1123

        :returns: :class:`Operation`
        

    .. py:method:: delete_branch(name: str) -> DeleteBranchOperation

        Delete a Branch.

        :param name: str
          The name of the Branch to delete. Format: projects/{project_id}/branches/{branch_id}

        :returns: :class:`Operation`
        

    .. py:method:: delete_endpoint(name: str) -> DeleteEndpointOperation

        Delete an Endpoint.

        :param name: str
          The name of the Endpoint to delete. Format:
          projects/{project_id}/branches/{branch_id}/endpoints/{endpoint_id}

        :returns: :class:`Operation`
        

    .. py:method:: delete_project(name: str) -> DeleteProjectOperation

        Delete a Project.

        :param name: str
          The name of the Project to delete. Format: projects/{project_id}

        :returns: :class:`Operation`
        

    .. py:method:: delete_role(name: str [, reassign_owned_to: Optional[str]]) -> DeleteRoleOperation

        Delete a role in a branch.

        :param name: str
          The resource name of the postgres role. Format:
          projects/{project_id}/branch/{branch_id}/roles/{role_id}
        :param reassign_owned_to: str (optional)
          Reassign objects. If this is set, all objects owned by the role are reassigned to the role specified
          in this parameter.

          NOTE: setting this requires spinning up a compute to succeed, since it involves running SQL queries.

          TODO: #LKB-7187 implement reassign_owned_to on LBM side. This might end-up being a synchronous query
          when this parameter is used.

        :returns: :class:`Operation`
        

    .. py:method:: get_branch(name: str) -> Branch

        Get a Branch.

        :param name: str
          The name of the Branch to retrieve. Format: projects/{project_id}/branches/{branch_id}

        :returns: :class:`Branch`
        

    .. py:method:: get_endpoint(name: str) -> Endpoint

        Get an Endpoint.

        :param name: str
          The name of the Endpoint to retrieve. Format:
          projects/{project_id}/branches/{branch_id}/endpoints/{endpoint_id}

        :returns: :class:`Endpoint`
        

    .. py:method:: get_operation(name: str) -> Operation

        Get an Operation.

        :param name: str
          The name of the operation resource.

        :returns: :class:`Operation`
        

    .. py:method:: get_project(name: str) -> Project

        Get a Project.

        :param name: str
          The name of the Project to retrieve. Format: projects/{project_id}

        :returns: :class:`Project`
        

    .. py:method:: get_role(name: str) -> Role

        Get a Role.

        :param name: str
          The name of the Role to retrieve. Format: projects/{project_id}/branches/{branch_id}/roles/{role_id}

        :returns: :class:`Role`
        

    .. py:method:: list_branches(parent: str [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[Branch]

        List Branches.

        :param parent: str
          The Project that owns this collection of branches. Format: projects/{project_id}
        :param page_size: int (optional)
          Upper bound for items returned.
        :param page_token: str (optional)
          Pagination token to go to the next page of Branches. Requests first page if absent.

        :returns: Iterator over :class:`Branch`
        

    .. py:method:: list_endpoints(parent: str [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[Endpoint]

        List Endpoints.

        :param parent: str
          The Branch that owns this collection of endpoints. Format:
          projects/{project_id}/branches/{branch_id}
        :param page_size: int (optional)
          Upper bound for items returned.
        :param page_token: str (optional)
          Pagination token to go to the next page of Endpoints. Requests first page if absent.

        :returns: Iterator over :class:`Endpoint`
        

    .. py:method:: list_projects( [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[Project]

        List Projects.

        :param page_size: int (optional)
          Upper bound for items returned.
        :param page_token: str (optional)
          Pagination token to go to the next page of Projects. Requests first page if absent.

        :returns: Iterator over :class:`Project`
        

    .. py:method:: list_roles(parent: str [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[Role]

        List Roles.

        :param parent: str
          The Branch that owns this collection of roles. Format: projects/{project_id}/branches/{branch_id}
        :param page_size: int (optional)
          Upper bound for items returned.
        :param page_token: str (optional)
          Pagination token to go to the next page of Roles. Requests first page if absent.

        :returns: Iterator over :class:`Role`
        

    .. py:method:: update_branch(name: str, branch: Branch, update_mask: FieldMask) -> UpdateBranchOperation

        Update a Branch.

        :param name: str
          The resource name of the branch. Format: projects/{project_id}/branches/{branch_id}
        :param branch: :class:`Branch`
          The Branch to update.

          The branch's `name` field is used to identify the branch to update. Format:
          projects/{project_id}/branches/{branch_id}
        :param update_mask: FieldMask
          The list of fields to update. If unspecified, all fields will be updated when possible.

        :returns: :class:`Operation`
        

    .. py:method:: update_endpoint(name: str, endpoint: Endpoint, update_mask: FieldMask) -> UpdateEndpointOperation

        Update an Endpoint.

        :param name: str
          The resource name of the endpoint. Format:
          projects/{project_id}/branches/{branch_id}/endpoints/{endpoint_id}
        :param endpoint: :class:`Endpoint`
          The Endpoint to update.

          The endpoint's `name` field is used to identify the endpoint to update. Format:
          projects/{project_id}/branches/{branch_id}/endpoints/{endpoint_id}
        :param update_mask: FieldMask
          The list of fields to update. If unspecified, all fields will be updated when possible.

        :returns: :class:`Operation`
        

    .. py:method:: update_project(name: str, project: Project, update_mask: FieldMask) -> UpdateProjectOperation

        Update a Project.

        :param name: str
          The resource name of the project. Format: projects/{project_id}
        :param project: :class:`Project`
          The Project to update.

          The project's `name` field is used to identify the project to update. Format: projects/{project_id}
        :param update_mask: FieldMask
          The list of fields to update. If unspecified, all fields will be updated when possible.

        :returns: :class:`Operation`
        