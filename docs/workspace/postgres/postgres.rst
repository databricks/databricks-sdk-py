``w.postgres``: Postgres
========================
.. currentmodule:: databricks.sdk.service.postgres

.. py:class:: PostgresAPI

    The Postgres API provides access to a Postgres database via REST API or direct SQL.

    .. py:method:: create_branch(parent: str, branch: Branch [, branch_id: Optional[str]]) -> CreateBranchOperation

        Create a Branch.

        :param parent: str
          The Project where this Branch will be created. Format: projects/{project_id}
        :param branch: :class:`Branch`
          The Branch to create.
        :param branch_id: str (optional)
          The ID to use for the Branch, which will become the final component of the branch's resource name.

          This value should be 4-63 characters, and valid characters are /[a-z][0-9]-/.

        :returns: :class:`Operation`
        

    .. py:method:: create_endpoint(parent: str, endpoint: Endpoint [, endpoint_id: Optional[str]]) -> CreateEndpointOperation

        Create an Endpoint.

        :param parent: str
          The Branch where this Endpoint will be created. Format: projects/{project_id}/branches/{branch_id}
        :param endpoint: :class:`Endpoint`
          The Endpoint to create.
        :param endpoint_id: str (optional)
          The ID to use for the Endpoint, which will become the final component of the endpoint's resource
          name.

          This value should be 4-63 characters, and valid characters are /[a-z][0-9]-/.

        :returns: :class:`Operation`
        

    .. py:method:: create_project(project: Project [, project_id: Optional[str]]) -> CreateProjectOperation

        Create a Project.

        :param project: :class:`Project`
          The Project to create.
        :param project_id: str (optional)
          The ID to use for the Project, which will become the final component of the project's resource name.

          This value should be 4-63 characters, and valid characters are /[a-z][0-9]-/.

        :returns: :class:`Operation`
        

    .. py:method:: delete_branch(name: str)

        Delete a Branch.

        :param name: str
          The name of the Branch to delete. Format: projects/{project_id}/branches/{branch_id}


        

    .. py:method:: delete_endpoint(name: str)

        Delete an Endpoint.

        :param name: str
          The name of the Endpoint to delete. Format:
          projects/{project_id}/branches/{branch_id}/endpoints/{endpoint_id}


        

    .. py:method:: delete_project(name: str)

        Delete a Project.

        :param name: str
          The name of the Project to delete. Format: projects/{project_id}


        

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
        