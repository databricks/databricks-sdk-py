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
    ``projects/{project_id}/branches/{branch_id}/endpoints/{endpoint_id}``. The ``name`` field on each
    resource contains this full path and is output-only. Note that ``name`` refers to this resource path, not
    the user-visible ``display_name``.

    .. py:method:: create_branch(parent: str, branch: Branch, branch_id: str [, replace_existing: Optional[bool]]) -> CreateBranchOperation

        Creates a new database branch in the project.

        :param parent: str
          The Project where this Branch will be created. Format: projects/{project_id}
        :param branch: :class:`Branch`
          The Branch to create.
        :param branch_id: str
          The ID to use for the Branch. This becomes the final component of the branch's resource name. The ID
          is required and must be 1-63 characters long, start with a lowercase letter, and contain only
          lowercase letters, numbers, and hyphens. For example, ``development`` becomes
          ``projects/my-app/branches/development``.
        :param replace_existing: bool (optional)
          If true, update the branch if it already exists instead of returning an error.

        :returns: :class:`Operation`
        

    .. py:method:: create_catalog(catalog: Catalog, catalog_id: str) -> CreateCatalogOperation

        Register a Postgres database in the Unity Catalog.

        :param catalog: :class:`Catalog`
        :param catalog_id: str
          The ID in the Unity Catalog. It becomes the full resource name, for example "my_catalog" becomes
          "catalogs/my_catalog".

        :returns: :class:`Operation`
        

    .. py:method:: create_cdf_config(parent: str, cdf_config: CdfConfig [, cdf_config_id: Optional[str]]) -> CreateCdfConfigOperation

        Create a CDF configuration that materializes the change data feed for all tables in a Postgres schema
        as open-format Delta tables in Unity Catalog. Once created, each table's change history is
        continuously written to its corresponding Lakehouse table.

        :param parent: str
          The parent database under which to create the CdfConfig. Format:
          projects/{project}/branches/{branch}/databases/{database}
        :param cdf_config: :class:`CdfConfig`
          The CdfConfig to create. The catalog, schema, and postgres_schema fields are required; all other
          fields are output only and ignored on input.
        :param cdf_config_id: str (optional)
          The user-specified id for the CdfConfig, forming the final segment of its resource name. Must match
          the pattern ``[a-z][a-z0-9_]{0,62}``. Defaults to the Postgres schema name when omitted.

        :returns: :class:`Operation`
        

    .. py:method:: create_data_api(parent: str, data_api: DataApi) -> CreateDataApiOperation

        Enable Data API for a database.

        :param parent: str
          Parent database: projects/{project_id}/branches/{branch_id}/databases/{database_id}
        :param data_api: :class:`DataApi`
          The Data API configuration to create.

        :returns: :class:`Operation`
        

    .. py:method:: create_database(parent: str, database: Database [, database_id: Optional[str], replace_existing: Optional[bool]]) -> CreateDatabaseOperation

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
        :param replace_existing: bool (optional)
          If true, update the database if it already exists instead of returning an error.

        :returns: :class:`Operation`
        

    .. py:method:: create_endpoint(parent: str, endpoint: Endpoint, endpoint_id: str [, replace_existing: Optional[bool]]) -> CreateEndpointOperation

        Creates a new compute endpoint in the branch.

        :param parent: str
          The Branch where this Endpoint will be created. Format: projects/{project_id}/branches/{branch_id}
        :param endpoint: :class:`Endpoint`
          The Endpoint to create.
        :param endpoint_id: str
          The ID to use for the Endpoint. This becomes the final component of the endpoint's resource name.
          The ID is required and must be 1-63 characters long, start with a lowercase letter, and contain only
          lowercase letters, numbers, and hyphens. For example, ``primary`` becomes
          ``projects/my-app/branches/development/endpoints/primary``.
        :param replace_existing: bool (optional)
          If true, update the endpoint if it already exists instead of returning an error.

        :returns: :class:`Operation`
        

    .. py:method:: create_project(project: Project, project_id: str) -> CreateProjectOperation

        Creates a new Lakebase Autoscaling Postgres database project, which contains branches and compute
        endpoints.

        :param project: :class:`Project`
          The Project to create.
        :param project_id: str
          The ID to use for the Project. This becomes the final component of the project's resource name. The
          ID is required and must be 1-63 characters long, start with a lowercase letter, and contain only
          lowercase letters, numbers, and hyphens. For example, ``my-app`` becomes ``projects/my-app``.

        :returns: :class:`Operation`
        

    .. py:method:: create_replication_group_preview(parent: str, replication_group_preview: ReplicationGroupPreview, replication_group_preview_id: str [, request_id: Optional[str]]) -> CreateReplicationGroupPreviewOperation

        Creates a new replication group for the project.

        :param parent: str
        :param replication_group_preview: :class:`ReplicationGroupPreview`
        :param replication_group_preview_id: str
        :param request_id: str (optional)

        :returns: :class:`Operation`
        

    .. py:method:: create_role(parent: str, role: Role [, replace_existing: Optional[bool], role_id: Optional[str]]) -> CreateRoleOperation

        Creates a new Postgres role in the branch.

        :param parent: str
          The Branch where this Role is created. Format: projects/{project_id}/branches/{branch_id}
        :param role: :class:`Role`
          The desired specification of a Role.
        :param replace_existing: bool (optional)
          If true, update the role if it already exists instead of returning an error.

          When the role already exists, the provided ``role`` spec fully replaces the existing one:
          ``membership_roles`` is overwritten, not merged. Leaving ``membership_roles`` empty clears all of
          the role's existing memberships, including ``DATABRICKS_SUPERUSER``. Always send the complete
          desired list of memberships when using this field.
        :param role_id: str (optional)
          The ID to use for the Role, which will become the final component of the role's resource name. This
          ID becomes the role in Postgres.

          This value should be 4-63 characters, and valid characters are lowercase letters, numbers, and
          hyphens, as defined by RFC 1123.

          If role_id is not specified in the request, it is generated automatically.

        :returns: :class:`Operation`
        

    .. py:method:: create_snapshot(parent: str, snapshot: Snapshot, snapshot_id: str) -> CreateSnapshotOperation

        Creates a snapshot, an immutable point-in-time copy of a branch's data, within the project.

        :param parent: str
          The project in which to create the snapshot. Format: projects/{project_id}
        :param snapshot: :class:`Snapshot`
          The snapshot to create.
        :param snapshot_id: str
          Client-chosen ID for the snapshot. It becomes the final segment of the snapshot resource name and
          cannot be changed after creation.

        :returns: :class:`Operation`
        

    .. py:method:: create_synced_table(synced_table: SyncedTable, synced_table_id: str) -> CreateSyncedTableOperation

        Create a Synced Table.

        :param synced_table: :class:`SyncedTable`
        :param synced_table_id: str
          The ID to use for the Synced Table. This becomes the final component of the SyncedTable's resource
          name. ID is required and is the synced table name, containing (catalog, schema, table) tuple.
          Elements of the tuple are the UC entity names.

          Example: "{catalog}.{schema}.{table}"

          synced_table_id represents both of the following:

          1. An online VIEW virtual table in the Unity Catalog accessible via the Lakehouse Federation.
          2. Postgres table named "{table}" in schema "{schema}" in the connected Postgres database

        :returns: :class:`Operation`
        

    .. py:method:: create_table(table: Table) -> Table

        Create a Table (non-synced database table for Autoscaling v2 Lakebase projects).

        :param table: :class:`Table`

        :returns: :class:`Table`
        

    .. py:method:: delete_branch(name: str [, allow_missing: Optional[bool], purge: Optional[bool]]) -> DeleteBranchOperation

        Deletes the specified database branch.

        :param name: str
          The full resource path of the branch to delete. Format: projects/{project_id}/branches/{branch_id}
        :param allow_missing: bool (optional)
          If true, if branch does not exists, the request will succeed and no action will be taken. If false
          (default value) and branch does not exists, the request will fail with NOT_FOUND error.
        :param purge: bool (optional)
          If true, permanently delete the branch; if false, soft delete.

        :returns: :class:`Operation`
        

    .. py:method:: delete_catalog(name: str) -> DeleteCatalogOperation

        Delete a Database Catalog.

        :param name: str
          The full resource path of the catalog to delete.

          Format: "catalogs/{catalog_id}".

        :returns: :class:`Operation`
        

    .. py:method:: delete_cdf_config(name: str [, force: Optional[bool]]) -> DeleteCdfConfigOperation

        Delete a CDF configuration and stop materializing the change data feed. When force=true, also drops
        the Delta tables in Unity Catalog. When force=false (default), the existing tables are preserved at
        their last state.

        :param name: str
          The resource name of the CdfConfig to delete. Format:
          projects/{project}/branches/{branch}/databases/{database}/cdf-configs/{cdf_config}
        :param force: bool (optional)
          When true, also drops the replicated Delta tables in Unity Catalog. When false (the default), the
          replicated tables are preserved at their last synced state.

        :returns: :class:`Operation`
        

    .. py:method:: delete_data_api(name: str) -> DeleteDataApiOperation

        Disable Data API for a database.

        :param name: str
          Resource name: projects/{project_id}/branches/{branch_id}/databases/{database_id}/data-api

        :returns: :class:`Operation`
        

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
        

    .. py:method:: delete_forward_etl_configuration(parent: str [, pg_database_oid: Optional[int], pg_schema_oid: Optional[int], tenant_id: Optional[str], timeline_id: Optional[str]]) -> DeleteForwardEtlConfigurationResponse

        Hard delete a Forward ETL configuration and all associated table mappings. Unlike DisableForwardEtl,
        this permanently removes the config and mapping rows.

        :param parent: str
          The Branch to delete Forward ETL configuration for. Format:
          projects/{project_id}/branches/{branch_id}
        :param pg_database_oid: int (optional)
          PostgreSQL database OID to delete configuration for.
        :param pg_schema_oid: int (optional)
          PostgreSQL schema OID to delete configuration for.
        :param tenant_id: str (optional)
          Tenant ID (dashless UUID format).
        :param timeline_id: str (optional)
          Timeline ID (dashless UUID format).

        :returns: :class:`DeleteForwardEtlConfigurationResponse`
        

    .. py:method:: delete_project(name: str [, purge: Optional[bool]]) -> DeleteProjectOperation

        Deletes the specified database project.

        :param name: str
          The full resource path of the project to delete. Format: projects/{project_id}
        :param purge: bool (optional)
          If true, permanently deletes the project (hard delete). If false or unset, performs a soft delete.

        :returns: :class:`Operation`
        

    .. py:method:: delete_recovery_branch_preview(name: str [, request_id: Optional[str]]) -> DeleteRecoveryBranchPreviewOperation

        Deletes the specified recovery branch after reconciliation is complete.

        :param name: str
        :param request_id: str (optional)

        :returns: :class:`Operation`
        

    .. py:method:: delete_replication_group_preview(name: str [, etag: Optional[str], request_id: Optional[str]]) -> DeleteReplicationGroupPreviewOperation

        Deletes the specified replication group.

        :param name: str
        :param etag: str (optional)
        :param request_id: str (optional)

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

        :returns: :class:`Operation`
        

    .. py:method:: delete_snapshot(name: str) -> DeleteSnapshotOperation

        Deletes the specified snapshot.

        :param name: str
          The resource name of the snapshot to delete. Format: projects/{project_id}/snapshots/{snapshot_id}

        :returns: :class:`Operation`
        

    .. py:method:: delete_synced_table(name: str) -> DeleteSyncedTableOperation

        Delete a Synced Table.

        :param name: str
          The Full resource name of the synced table, of the format
          "synced_tables/{catalog}.{schema}.{table}", where (catalog, schema, table) are the UC entity names.

        :returns: :class:`Operation`
        

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
        

    .. py:method:: failover_replication_group_preview(name: str, target_workspace: str [, etag: Optional[str], request_id: Optional[str]]) -> FailoverReplicationGroupPreviewOperation

        Fails over the replication group to a target workspace, promoting the secondary to primary.

        :param name: str
        :param target_workspace: str
        :param etag: str (optional)
        :param request_id: str (optional)

        :returns: :class:`Operation`
        

    .. py:method:: generate_database_credential(endpoint: str [, claims: Optional[List[RequestedClaims]], expire_time: Optional[Timestamp], group_name: Optional[str], ttl: Optional[Duration]]) -> DatabaseCredential

        Generate OAuth credentials for a Postgres database.

        :param endpoint: str
          The endpoint resource name for which this credential will be generated. Format:
          projects/{project_id}/branches/{branch_id}/endpoints/{endpoint_id}
        :param claims: List[:class:`RequestedClaims`] (optional)
          The returned token will be scoped to UC tables with the specified permissions.
        :param expire_time: Timestamp (optional)
          Timestamp in UTC of when this credential should expire. Must be at least 300 seconds (5 minutes) and
          at most 1 hour from the current time.
        :param group_name: str (optional)
          The display name of a ``Databricks`` workspace group. When set, the returned credential is scoped to
          this group, so the caller connects directly as the group's Postgres role. The caller must be a
          member of the group. When omitted, the credential is scoped to the caller's own identity.
        :param ttl: Duration (optional)
          The requested time-to-live for the generated credential token. Must be at least 300 seconds (5
          minutes) and at most 3600 seconds (1 hour).

        :returns: :class:`DatabaseCredential`
        

    .. py:method:: get_branch(name: str) -> Branch

        Retrieves information about the specified database branch.

        :param name: str
          The full resource path of the branch to retrieve. Format: projects/{project_id}/branches/{branch_id}

        :returns: :class:`Branch`
        

    .. py:method:: get_catalog(name: str) -> Catalog

        Get a Database Catalog.

        :param name: str
          The full resource path of the catalog to retrieve.

          Format: "catalogs/{catalog_id}".

        :returns: :class:`Catalog`
        

    .. py:method:: get_cdf_config(name: str) -> CdfConfig

        Get a single Lakebase CDF configuration, including the source Postgres schema, target Unity Catalog
        schema, and the identity under which writes are authorized.

        :param name: str
          The resource name of the CdfConfig to retrieve. Format:
          projects/{project}/branches/{branch}/databases/{database}/cdf-configs/{cdf_config}

        :returns: :class:`CdfConfig`
        

    .. py:method:: get_cdf_status(name: str) -> CdfStatus

        Get the CDF status of a single table within a Lakebase CDF configuration, including its current state
        and the last committed position in the feed.

        :param name: str
          The resource name of the CdfStatus to retrieve. Format:
          projects/{project}/branches/{branch}/databases/{database}/cdf-configs/{cdf_config}/cdf-statuses/{cdf_status}

        :returns: :class:`CdfStatus`
        

    .. py:method:: get_compute_instance(name: str) -> ComputeInstance

        Lists the specific compute instance under an endpoint. Note: ComputeInstances are managed via the
        parent Endpoint resource, and cannot be created, updated, or deleted directly.

        :param name: str
          The full resource path of the compute instance to retrieve. Format:
          projects/{project_id}/branches/{branch_id}/endpoints/{endpoint_id}/compute-instances/{compute_instance_id}

        :returns: :class:`ComputeInstance`
        

    .. py:method:: get_data_api(name: str) -> DataApi

        Get Data API configuration for a database.

        :param name: str
          Resource name: projects/{project_id}/branches/{branch_id}/databases/{database_id}/data-api

        :returns: :class:`DataApi`
        

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
        

    .. py:method:: get_recovery_branch_preview(name: str) -> RecoveryBranchPreview

        Retrieves information about the specified recovery branch.

        :param name: str

        :returns: :class:`RecoveryBranchPreview`
        

    .. py:method:: get_replication_group_preview(name: str) -> ReplicationGroupPreview

        Retrieves information about the specified replication group.

        :param name: str

        :returns: :class:`ReplicationGroupPreview`
        

    .. py:method:: get_role(name: str) -> Role

        Retrieves information about the specified Postgres role, including its authentication method and
        permissions.

        :param name: str
          The full resource path of the role to retrieve. Format:
          projects/{project_id}/branches/{branch_id}/roles/{role_id}

        :returns: :class:`Role`
        

    .. py:method:: get_snapshot(name: str) -> Snapshot

        Retrieves information about the specified snapshot.

        :param name: str
          The resource name of the snapshot to retrieve. Format: projects/{project_id}/snapshots/{snapshot_id}

        :returns: :class:`Snapshot`
        

    .. py:method:: get_snapshot_schedule(name: str) -> SnapshotSchedule

        Retrieves the snapshot schedule for a branch. A branch with no configured schedule returns an empty
        schedule (not NOT_FOUND).

        :param name: str
          The resource name of the branch's snapshot schedule. Format:
          projects/{project_id}/branches/{branch_id}/snapshot-schedule

        :returns: :class:`SnapshotSchedule`
        

    .. py:method:: get_synced_table(name: str) -> SyncedTable

        Get a Synced Table.

        :param name: str
          The Full resource name of the synced table. Format: "synced_tables/{catalog}.{schema}.{table}",
          where (catalog, schema, table) are the entity names in the Unity Catalog.

        :returns: :class:`SyncedTable`
        

    .. py:method:: get_table(name: str) -> Table

        Get a Table (non-synced database table for Autoscaling v2 Lakebase projects).

        :param name: str
          Full three-part (catalog, schema, table) name of the table.

        :returns: :class:`Table`
        

    .. py:method:: inspect_recovery_branch_preview(name: str, branch_id: str [, request_id: Optional[str]]) -> InspectRecoveryBranchPreviewOperation

        Materializes a temporary inspection branch from the specified recovery branch for data examination.

        :param name: str
          The recovery branch from which to create the inspection branch.
        :param branch_id: str
          Caller-supplied id for the inspection Branch this custom method materializes.
        :param request_id: str (optional)

        :returns: :class:`Operation`
        

    .. py:method:: list_branches(parent: str [, page_size: Optional[int], page_token: Optional[str], show_deleted: Optional[bool]]) -> Iterator[Branch]

        Returns a paginated list of database branches in the project.

        :param parent: str
          The Project that owns this collection of branches. Format: projects/{project_id}
        :param page_size: int (optional)
          Upper bound for items returned. Cannot be negative.
        :param page_token: str (optional)
          Page token from a previous response. If not provided, returns the first page.
        :param show_deleted: bool (optional)
          Whether to include soft-deleted branches in the response. When true, deleted branches are included
          alongside active branches. Purged branches are never returned.

        :returns: Iterator over :class:`Branch`
        

    .. py:method:: list_cdf_configs(parent: str [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[CdfConfig]

        List all CDF configurations for a Lakebase database. Each configuration maps a Postgres schema to a
        Unity Catalog schema where the change data feed is materialized.

        :param parent: str
          The parent database to list CdfConfigs for. Format:
          projects/{project}/branches/{branch}/databases/{database}
        :param page_size: int (optional)
          Maximum number of CdfConfigs to return.
        :param page_token: str (optional)
          Pagination token returned by a previous ListCdfConfigs call. Empty on the first page.

        :returns: Iterator over :class:`CdfConfig`
        

    .. py:method:: list_cdf_statuses(parent: str [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[CdfStatus]

        List the per-table CDF statuses within a Lakebase CDF configuration. Each status shows whether a
        table's change data feed is snapshotting, streaming, or skipped.

        :param parent: str
          The parent CdfConfig to list CdfStatuses for. Format:
          projects/{project}/branches/{branch}/databases/{database}/cdf-configs/{cdf_config}
        :param page_size: int (optional)
          Maximum number of CdfStatuses to return.
        :param page_token: str (optional)
          Pagination token returned by a previous ListCdfStatuses call. Empty on the first page.

        :returns: Iterator over :class:`CdfStatus`
        

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
          A page token, received from a previous ``ListInstances`` call. Provide this to retrieve the
          subsequent page.

          When paginating, all other parameters provided to ``ListInstances`` must match the call that
          provided the page token.

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
        

    .. py:method:: list_projects( [, page_size: Optional[int], page_token: Optional[str], show_deleted: Optional[bool]]) -> Iterator[Project]

        Returns a paginated list of database projects in the workspace that the user has permission to access.

        :param page_size: int (optional)
          Upper bound for items returned. Cannot be negative. The maximum value is 100.
        :param page_token: str (optional)
          Page token from a previous response. If not provided, returns the first page.
        :param show_deleted: bool (optional)
          Whether to include soft-deleted projects in the response. When true, soft-deleted projects are
          included alongside active projects. Hard-deleted and already-purged projects are never returned.

        :returns: Iterator over :class:`Project`
        

    .. py:method:: list_recovery_branch_previews(parent: str [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[RecoveryBranchPreview]

        Returns a paginated list of recovery branches for the project.

        :param parent: str
        :param page_size: int (optional)
        :param page_token: str (optional)

        :returns: Iterator over :class:`RecoveryBranchPreview`
        

    .. py:method:: list_replication_group_previews(parent: str [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[ReplicationGroupPreview]

        Returns a paginated list of replication groups for the project.

        :param parent: str
        :param page_size: int (optional)
        :param page_token: str (optional)

        :returns: Iterator over :class:`ReplicationGroupPreview`
        

    .. py:method:: list_roles(parent: str [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[Role]

        Returns a paginated list of Postgres roles in the branch.

        :param parent: str
          The Branch that owns this collection of roles. Format: projects/{project_id}/branches/{branch_id}
        :param page_size: int (optional)
          Upper bound for items returned. Cannot be negative.
        :param page_token: str (optional)
          Page token from a previous response. If not provided, returns the first page.

        :returns: Iterator over :class:`Role`
        

    .. py:method:: list_snapshots(parent: str [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[Snapshot]

        Returns a paginated list of snapshots in the project.

        :param parent: str
          The project that owns the snapshots. Format: projects/{project_id}
        :param page_size: int (optional)
          Maximum number of snapshots to return per page.
        :param page_token: str (optional)
          Page token from a previous response; omit for the first page.

        :returns: Iterator over :class:`Snapshot`
        

    .. py:method:: switchover_replication_group_preview(name: str, target_workspace: str [, etag: Optional[str], request_id: Optional[str]]) -> SwitchoverReplicationGroupPreviewOperation

        Switches over the replication group to a target workspace with a coordinated failover.

        :param name: str
        :param target_workspace: str
        :param etag: str (optional)
        :param request_id: str (optional)

        :returns: :class:`Operation`
        

    .. py:method:: undelete_branch(name: str) -> UndeleteBranchOperation

        Undeletes the specified database branch.

        :param name: str
          The full resource path of the branch to undelete. Format: projects/{project_id}/branches/{branch_id}

        :returns: :class:`Operation`
        

    .. py:method:: undelete_project(name: str) -> UndeleteProjectOperation

        Undeletes a soft-deleted project.

        :param name: str
          The full resource path of the project to undelete. Format: projects/{project_id}

        :returns: :class:`Operation`
        

    .. py:method:: update_branch(name: str, branch: Branch, update_mask: FieldMask) -> UpdateBranchOperation

        Updates the specified database branch. You can set this branch as the project's default branch, or
        protect/unprotect it.

        :param name: str
          Output only. The full resource path of the branch. Format:
          projects/{project_id}/branches/{branch_id}
        :param branch: :class:`Branch`
          The Branch to update.

          The branch's ``name`` field is used to identify the branch to update. Format:
          projects/{project_id}/branches/{branch_id}
        :param update_mask: FieldMask
          The list of fields to update.

        :returns: :class:`Operation`
        

    .. py:method:: update_data_api(name: str, data_api: DataApi, update_mask: FieldMask) -> UpdateDataApiOperation

        Update Data API configuration for a database.

        :param name: str
          Resource name: projects/{project_id}/branches/{branch_id}/databases/{database_id}/data-api
        :param data_api: :class:`DataApi`
          The Data API configuration to update. The data_api's ``name`` field identifies the resource.
        :param update_mask: FieldMask
          The list of fields to update.

        :returns: :class:`Operation`
        

    .. py:method:: update_database(name: str, database: Database, update_mask: FieldMask) -> UpdateDatabaseOperation

        Update a Database.

        :param name: str
          The resource name of the database. Format:
          projects/{project_id}/branches/{branch_id}/databases/{database_id}
        :param database: :class:`Database`
          The Database to update.

          The database's ``name`` field is used to identify the database to update. Format:
          projects/{project_id}/branches/{branch_id}/databases/{database_id}
        :param update_mask: FieldMask
          The list of fields to update.

        :returns: :class:`Operation`
        

    .. py:method:: update_endpoint(name: str, endpoint: Endpoint, update_mask: FieldMask) -> UpdateEndpointOperation

        Updates the specified compute endpoint. You can update autoscaling limits, suspend timeout, or
        enable/disable the compute endpoint.

        :param name: str
          Output only. The full resource path of the endpoint. Format:
          projects/{project_id}/branches/{branch_id}/endpoints/{endpoint_id}
        :param endpoint: :class:`Endpoint`
          The Endpoint to update.

          The endpoint's ``name`` field is used to identify the endpoint to update. Format:
          projects/{project_id}/branches/{branch_id}/endpoints/{endpoint_id}
        :param update_mask: FieldMask
          The list of fields to update.

        :returns: :class:`Operation`
        

    .. py:method:: update_project(name: str, project: Project, update_mask: FieldMask) -> UpdateProjectOperation

        Updates the specified database project.

        :param name: str
          Output only. The full resource path of the project. Format: projects/{project_id}
        :param project: :class:`Project`
          The Project to update.

          The project's ``name`` field is used to identify the project to update. Format:
          projects/{project_id}
        :param update_mask: FieldMask
          The list of fields to update.

        :returns: :class:`Operation`
        

    .. py:method:: update_replication_group_preview(name: str, replication_group_preview: ReplicationGroupPreview, update_mask: FieldMask [, request_id: Optional[str]]) -> UpdateReplicationGroupPreviewOperation

        Updates the specified replication group.

        :param name: str
          The resource name of the replication group. Format:
          projects/{project_id}/preview/replication-groups/{replication_group_id}
        :param replication_group_preview: :class:`ReplicationGroupPreview`
        :param update_mask: FieldMask
          The field mask must be a single string, with multiple fields separated by commas (no spaces). The
          field path is relative to the resource object, using a dot (``.``) to navigate sub-fields (e.g.,
          ``author.given_name``). Specification of elements in sequence or map fields is not allowed, as only
          the entire collection field can be specified. Field names must exactly match the resource field
          names.

          A field mask of ``*`` indicates full replacement. It’s recommended to always explicitly list the
          fields being updated and avoid using ``*`` wildcards, as it can lead to unintended results if the
          API changes in the future.
        :param request_id: str (optional)

        :returns: :class:`Operation`
        

    .. py:method:: update_role(name: str, role: Role, update_mask: FieldMask) -> UpdateRoleOperation

        Update a role for a branch.

        :param name: str
          Output only. The full resource path of the role. Format:
          projects/{project_id}/branches/{branch_id}/roles/{role_id}
        :param role: :class:`Role`
          The Postgres Role to update.

          The role's ``name`` field is used to identify the role to update. Format:
          projects/{project_id}/branches/{branch_id}/roles/{role_id}
        :param update_mask: FieldMask
          The list of fields to update.

        :returns: :class:`Operation`
        

    .. py:method:: update_snapshot_schedule(name: str, snapshot_schedule: SnapshotSchedule, update_mask: FieldMask) -> SnapshotSchedule

        Sets the snapshot schedule for a branch. The ``schedule`` field is replaced wholesale; an empty
        schedule disables automatic snapshots.

        :param name: str
          The resource name of the branch's snapshot schedule. Format:
          projects/{project_id}/branches/{branch_id}/snapshot-schedule
        :param snapshot_schedule: :class:`SnapshotSchedule`
          The snapshot schedule to set. Its ``name`` identifies the branch. Format:
          projects/{project_id}/branches/{branch_id}/snapshot-schedule
        :param update_mask: FieldMask
          Fields to update. The only updatable path is ``schedule``, which replaces the entire set of
          cadences.

        :returns: :class:`SnapshotSchedule`
        