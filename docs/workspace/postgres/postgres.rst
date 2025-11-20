``w.postgres``: Postgres
========================
.. currentmodule:: databricks.sdk.service.postgres

.. py:class:: PostgresAPI

    The Postgres API provides access to a Postgres database via REST API or direct SQL.

    .. py:method:: create_database_branch(parent: str, database_branch: DatabaseBranch [, database_branch_id: Optional[str]]) -> CreateDatabaseBranchOperation

        Create a Database Branch.

        :param parent: str
          The Database Project where this Database Branch will be created. Format: projects/{project_id}
        :param database_branch: :class:`DatabaseBranch`
          The Database Branch to create.
        :param database_branch_id: str (optional)
          The ID to use for the Database Branch, which will become the final component of the branch's
          resource name.

          This value should be 4-63 characters, and valid characters are /[a-z][0-9]-/.

        :returns: :class:`Operation`
        

    .. py:method:: create_database_catalog(catalog: DatabaseCatalog) -> DatabaseCatalog

        Create a Database Catalog.

        :param catalog: :class:`DatabaseCatalog`

        :returns: :class:`DatabaseCatalog`
        

    .. py:method:: create_database_endpoint(parent: str, database_endpoint: DatabaseEndpoint [, database_endpoint_id: Optional[str]]) -> CreateDatabaseEndpointOperation

        Create a Database Endpoint.

        :param parent: str
          The Database Branch where this Database Endpoint will be created. Format:
          projects/{project_id}/branches/{branch_id}
        :param database_endpoint: :class:`DatabaseEndpoint`
          The Database Endpoint to create.
        :param database_endpoint_id: str (optional)
          The ID to use for the Database Endpoint, which will become the final component of the endpoint's
          resource name.

          This value should be 4-63 characters, and valid characters are /[a-z][0-9]-/.

        :returns: :class:`Operation`
        

    .. py:method:: create_database_project(database_project: DatabaseProject [, database_project_id: Optional[str]]) -> CreateDatabaseProjectOperation

        Create a Database Project.

        :param database_project: :class:`DatabaseProject`
          The Database Project to create
        :param database_project_id: str (optional)
          The ID to use for the Database Project, which will become the final component of the project's
          resource name.

          This value should be 4-63 characters, and valid characters are /[a-z][0-9]-/.

        :returns: :class:`Operation`
        

    .. py:method:: delete_database_branch(name: str)

        Delete a Database Branch.

        :param name: str
          The name of the Database Branch to delete. Format: projects/{project_id}/branches/{branch_id}


        

    .. py:method:: delete_database_endpoint(name: str)

        Delete a Database Endpoint.

        :param name: str
          The name of the Database Endpoint to delete. Format:
          projects/{project_id}/branches/{branch_id}/endpoints/{endpoint_id}


        

    .. py:method:: delete_database_project(name: str)

        Delete a Database Project.

        :param name: str
          The name of the Database Project to delete. Format: projects/{project_id}


        

    .. py:method:: get_database_branch(name: str) -> DatabaseBranch

        Get a Database Branch.

        :param name: str
          The name of the Database Branch to retrieve. Format: projects/{project_id}/branches/{branch_id}

        :returns: :class:`DatabaseBranch`
        

    .. py:method:: get_database_endpoint(name: str) -> DatabaseEndpoint

        Get a Database Endpoint.

        :param name: str
          The name of the Database Endpoint to retrieve. Format:
          projects/{project_id}/branches/{branch_id}/endpoints/{endpoint_id}

        :returns: :class:`DatabaseEndpoint`
        

    .. py:method:: get_database_operation(name: str) -> Operation

        Get a Database Operation.

        :param name: str
          The name of the operation resource.

        :returns: :class:`Operation`
        

    .. py:method:: get_database_project(name: str) -> DatabaseProject

        Get a Database Project.

        :param name: str
          The name of the Database Project to retrieve. Format: projects/{project_id}

        :returns: :class:`DatabaseProject`
        

    .. py:method:: list_database_branches(parent: str [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[DatabaseBranch]

        List Database Branches.

        :param parent: str
          The Database Project, which owns this collection of branches. Format: projects/{project_id}
        :param page_size: int (optional)
          Upper bound for items returned.
        :param page_token: str (optional)
          Pagination token to go to the next page of Database Branches. Requests first page if absent.

        :returns: Iterator over :class:`DatabaseBranch`
        

    .. py:method:: list_database_endpoints(parent: str [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[DatabaseEndpoint]

        List Database Endpoints.

        :param parent: str
          The Database Branch, which owns this collection of endpoints. Format:
          projects/{project_id}/branches/{branch_id}
        :param page_size: int (optional)
          Upper bound for items returned.
        :param page_token: str (optional)
          Pagination token to go to the next page of Database Branches. Requests first page if absent.

        :returns: Iterator over :class:`DatabaseEndpoint`
        

    .. py:method:: list_database_projects( [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[DatabaseProject]

        List Database Projects.

        :param page_size: int (optional)
          Upper bound for items returned.
        :param page_token: str (optional)
          Pagination token to go to the next page of Database Projects. Requests first page if absent.

        :returns: Iterator over :class:`DatabaseProject`
        

    .. py:method:: restart_database_endpoint(name: str) -> RestartDatabaseEndpointOperation

        Restart a Database Endpoint.

        :param name: str
          The name of the Database Endpoint to restart. Format:
          projects/{project_id}/branches/{branch_id}/endpoints/{endpoint_id}

        :returns: :class:`Operation`
        

    .. py:method:: update_database_branch(name: str, database_branch: DatabaseBranch, update_mask: str) -> UpdateDatabaseBranchOperation

        Update a Database Branch.

        :param name: str
          The resource name of the branch. Format: projects/{project_id}/branches/{branch_id}
        :param database_branch: :class:`DatabaseBranch`
          The Database Branch to update.

          The branch's `name` field is used to identify the branch to update. Format:
          projects/{project_id}/branches/{branch_id}
        :param update_mask: str
          The list of fields to update. If unspecified, all fields will be updated when possible.

        :returns: :class:`Operation`
        

    .. py:method:: update_database_endpoint(name: str, database_endpoint: DatabaseEndpoint, update_mask: str) -> UpdateDatabaseEndpointOperation

        Update a Database Endpoint.

        :param name: str
          The resource name of the endpoint. Format:
          projects/{project_id}/branches/{branch_id}/endpoints/{endpoint_id}
        :param database_endpoint: :class:`DatabaseEndpoint`
          The Database Endpoint to update.

          The endpoints's `name` field is used to identify the endpoint to update. Format:
          projects/{project_id}/branches/{branch_id}/endpoints/{endpoint_id}
        :param update_mask: str
          The list of fields to update. If unspecified, all fields will be updated when possible.

        :returns: :class:`Operation`
        

    .. py:method:: update_database_project(name: str, database_project: DatabaseProject, update_mask: str) -> UpdateDatabaseProjectOperation

        Update a Database Project.

        :param name: str
          The resource name of the project. Format: projects/{project_id}
        :param database_project: :class:`DatabaseProject`
          The Database Project to update.

          The project's `name` field is used to identify the project to update. Format: projects/{project_id}
        :param update_mask: str
          The list of fields to update. If unspecified, all fields will be updated when possible.

        :returns: :class:`Operation`
        