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
        

    .. py:method:: create_catalog(catalog: Catalog) -> Catalog

        Register a Database in UC.

        :param catalog: :class:`Catalog`

        :returns: :class:`Catalog`
        

    .. py:method:: create_database(parent: str, database: Database [, database_id: Optional[str]]) -> CreateDatabaseOperation

        Create a Database.

        Creates a database in the specified branch. A branch can have multiple databases.

        :param parent: str
          The Branch where this Database will be created. Format: projects/{project_id}/branches/{branch_id}
        :param database: :class:`Database`
          The desired specification of a Database.
        :param database_id: str (optional)
          The ID to use for the Database, which will become the final component of the database's resource
          name. This ID becomes the database name in postgres.

          This value should be 4-63 characters, and only use characters available in DNS names, as defined by
          RFC-1123

          If database_id is not specified in the request, it is generated automatically.

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
        

    .. py:method:: create_synced_table(synced_table: SyncedTable) -> SyncedTable

        Create a Synced Table.

        :param synced_table: :class:`SyncedTable`

        :returns: :class:`SyncedTable`
        

    .. py:method:: create_table(table: Table) -> Table

        Create a Table (non-synced database table for Autoscaling v2 Lakebase projects).

        :param table: :class:`Table`

        :returns: :class:`Table`
        

    .. py:method:: delete_branch(name: str) -> DeleteBranchOperation

        Deletes the specified database branch.

        :param name: str
          The full resource path of the branch to delete. Format: projects/{project_id}/branches/{branch_id}

        :returns: :class:`Operation`
        

    .. py:method:: delete_catalog(name: str)

        Delete a Database Catalog.

        :param name: str


        

    .. py:method:: delete_database(name: str) -> DeleteDatabaseOperation

        Delete a Database.

        :param name: str
          The resource name of the postgres database. Format:
          projects/{project_id}/branches/{branch_id}/databases/{database_id}

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
        

    .. py:method:: delete_synced_table(name: str)

        Delete a Synced Table.

        :param name: str
          Full three-part (catalog, schema, table) name of the synced table.


        

    .. py:method:: delete_table(name: str)

        Delete a Table (non-synced database table for Autoscaling v2 Lakebase projects).

        :param name: str
          Full three-part (catalog, schema, table) name of the table.


        

    .. py:method:: disable_forward_etl(parent: str [, pg_database_oid: Optional[int], pg_schema_oid: Optional[int], tenant_id: Optional[str], timeline_id: Optional[str]]) -> DisableForwardEtlResponse

        Disable Forward ETL for a branch.

        :param parent: str
          The Branch to disable Forward ETL for. Format: projects/{project_id}/branches/{branch_id}
        :param pg_database_oid: int (optional)
          PostgreSQL database OID to disable.
        :param pg_schema_oid: int (optional)
          PostgreSQL schema OID to disable.
        :param tenant_id: str (optional)
          Tenant ID (dashless UUID format).
        :param timeline_id: str (optional)
          Timeline ID (dashless UUID format).

        :returns: :class:`DisableForwardEtlResponse`
        

    .. py:method:: generate_database_credential(endpoint: str [, claims: Optional[List[RequestedClaims]], expire_time: Optional[Timestamp], group_name: Optional[str], ttl: Optional[Duration]]) -> DatabaseCredential

        Generate OAuth credentials for a Postgres database.

        :param endpoint: str
          This field is not yet supported. The endpoint for which this credential will be generated. Format:
          projects/{project_id}/branches/{branch_id}/endpoints/{endpoint_id}
        :param claims: List[:class:`RequestedClaims`] (optional)
          The returned token will be scoped to UC tables with the specified permissions.
        :param expire_time: Timestamp (optional)
          Timestamp in UTC of when this credential should expire. Expire time should be within 1 hour of the
          current time.
        :param group_name: str (optional)
          Databricks workspace group name. When provided, credentials are generated with permissions scoped to
          this group.
        :param ttl: Duration (optional)
          The requested time-to-live for the generated credential token. Maximum allowed duration is 1 hour.

        :returns: :class:`DatabaseCredential`
        

    .. py:method:: get_branch(name: str) -> Branch

        Retrieves information about the specified database branch.

        :param name: str
          The full resource path of the branch to retrieve. Format: projects/{project_id}/branches/{branch_id}

        :returns: :class:`Branch`
        

    .. py:method:: get_catalog(name: str) -> Catalog

        Get a Database Catalog.

        :param name: str

        :returns: :class:`Catalog`
        

    .. py:method:: get_compute_instance(name: str) -> ComputeInstance

        Lists the specific compute instance under an endpoint. Note: ComputeInstances are managed via the
        parent Endpoint resource, and cannot be created, updated, or deleted directly.

        :param name: str
          The full resource path of the compute instance to retrieve. Format:
          projects/{project_id}/branches/{branch_id}/endpoints/{endpoint_id}/compute-instances/{compute_instance_id}

        :returns: :class:`ComputeInstance`
        

    .. py:method:: get_database(name: str) -> Database

        Get a Database.

        :param name: str
          The name of the Database to retrieve. Format:
          projects/{project_id}/branches/{branch_id}/databases/{database_id}

        :returns: :class:`Database`
        

    .. py:method:: get_endpoint(name: str) -> Endpoint

        Retrieves information about the specified compute endpoint, including its connection details and
        operational state.

        :param name: str
          The full resource path of the endpoint to retrieve. Format:
          projects/{project_id}/branches/{branch_id}/endpoints/{endpoint_id}

        :returns: :class:`Endpoint`
        

    .. py:method:: get_forward_etl_metadata(parent: str [, tenant_id: Optional[str], timeline_id: Optional[str]]) -> ForwardEtlMetadata

        Get Forward ETL metadata (database and schema OIDs).

        :param parent: str
          The Branch to get metadata for. Format: projects/{project_id}/branches/{branch_id}
        :param tenant_id: str (optional)
          Tenant ID (dashless UUID format).
        :param timeline_id: str (optional)
          Timeline ID (dashless UUID format).

        :returns: :class:`ForwardEtlMetadata`
        

    .. py:method:: get_forward_etl_status(parent: str [, tenant_id: Optional[str], timeline_id: Optional[str]]) -> ForwardEtlStatus

        Get Forward ETL configuration and status for a branch.

        :param parent: str
          The Branch to get Forward ETL status for. Format: projects/{project_id}/branches/{branch_id}
        :param tenant_id: str (optional)
          Tenant ID (dashless UUID format).
        :param timeline_id: str (optional)
          Timeline ID (dashless UUID format).

        :returns: :class:`ForwardEtlStatus`
        

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
        

    .. py:method:: get_synced_table(name: str) -> SyncedTable

        Get a Synced Table.

        :param name: str
          Full three-part (catalog, schema, table) name of the synced table.

        :returns: :class:`SyncedTable`
        

    .. py:method:: get_table(name: str) -> Table

        Get a Table (non-synced database table for Autoscaling v2 Lakebase projects).

        :param name: str
          Full three-part (catalog, schema, table) name of the table.

        :returns: :class:`Table`
        

    .. py:method:: list_branches(parent: str [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[Branch]

        Returns a paginated list of database branches in the project.

        :param parent: str
          The Project that owns this collection of branches. Format: projects/{project_id}
        :param page_size: int (optional)
          Upper bound for items returned. Cannot be negative.
        :param page_token: str (optional)
          Page token from a previous response. If not provided, returns the first page.

        :returns: Iterator over :class:`Branch`
        

    .. py:method:: list_compute_instances(parent: str [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[ComputeInstance]

        Lists all compute instances that have been created under the specified endpoint. Note:
        ComputeInstances are managed via the parent Endpoint resource, and cannot be created, updated, or
        deleted directly.

        :param parent: str
          The parent, which owns the compute instances.
        :param page_size: int (optional)
          The maximum number of compute instances to return. The service may return fewer than this value.

          If unspecified, at most 50 compute instances will be returned. The maximum value is 1000; values
          above 1000 will be coerced to 1000.
        :param page_token: str (optional)
          A page token, received from a previous `ListInstances` call. Provide this to retrieve the subsequent
          page.

          When paginating, all other parameters provided to `ListInstances` must match the call that provided
          the page token.

        :returns: Iterator over :class:`ComputeInstance`
        

    .. py:method:: list_databases(parent: str [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[Database]

        List Databases.

        :param parent: str
          The Branch that owns this collection of databases. Format:
          projects/{project_id}/branches/{branch_id}
        :param page_size: int (optional)
          Upper bound for items returned.
        :param page_token: str (optional)
          Pagination token to go to the next page of Databases. Requests first page if absent.

        :returns: Iterator over :class:`Database`
        

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
          Upper bound for items returned. Cannot be negative. The maximum value is 100.
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
        

    .. py:method:: update_database(name: str, database: Database, update_mask: FieldMask) -> UpdateDatabaseOperation

        Update a Database.

        :param name: str
          The resource name of the database. Format:
          projects/{project_id}/branches/{branch_id}/databases/{database_id}
        :param database: :class:`Database`
          The Database to update.

          The database's `name` field is used to identify the database to update. Format:
          projects/{project_id}/branches/{branch_id}/databases/{database_id}
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
        

    .. py:method:: update_role(name: str, role: Role, update_mask: FieldMask) -> UpdateRoleOperation

        Update a role for a branch.

        :param name: str
          Output only. The full resource path of the role. Format:
          projects/{project_id}/branches/{branch_id}/roles/{role_id}
        :param role: :class:`Role`
          The Postgres Role to update.

          The role's `name` field is used to identify the role to update. Format:
          projects/{project_id}/branches/{branch_id}/roles/{role_id}
        :param update_mask: FieldMask
          The list of fields to update in Postgres Role. If unspecified, all fields will be updated when
          possible.

        :returns: :class:`Operation`
        