import databricks.sdk.core as client
import databricks.sdk.dbutils as dbutils
from databricks.sdk.mixins.compute import ClustersExt
from databricks.sdk.mixins.files import DbfsExt
from databricks.sdk.mixins.workspace import WorkspaceExt
from databricks.sdk.service.billing import (BillableUsageAPI, BudgetsAPI,
                                            LogDeliveryAPI)
from databricks.sdk.service.catalog import (AccountMetastoreAssignmentsAPI,
                                            AccountMetastoresAPI,
                                            AccountStorageCredentialsAPI,
                                            ArtifactAllowlistsAPI, CatalogsAPI,
                                            ConnectionsAPI,
                                            ExternalLocationsAPI, FunctionsAPI,
                                            GrantsAPI, MetastoresAPI,
                                            ModelVersionsAPI,
                                            RegisteredModelsAPI, SchemasAPI,
                                            StorageCredentialsAPI,
                                            SystemSchemasAPI,
                                            TableConstraintsAPI, TablesAPI,
                                            VolumesAPI, WorkspaceBindingsAPI)
from databricks.sdk.service.compute import (ClusterPoliciesAPI, ClustersAPI,
                                            CommandExecutionAPI,
                                            GlobalInitScriptsAPI,
                                            InstancePoolsAPI,
                                            InstanceProfilesAPI, LibrariesAPI,
                                            PolicyFamiliesAPI)
from databricks.sdk.service.files import DbfsAPI, FilesAPI
from databricks.sdk.service.iam import (AccountAccessControlAPI,
                                        AccountAccessControlProxyAPI,
                                        AccountGroupsAPI,
                                        AccountServicePrincipalsAPI,
                                        AccountUsersAPI, CurrentUserAPI,
                                        GroupsAPI, PermissionsAPI,
                                        ServicePrincipalsAPI, UsersAPI,
                                        WorkspaceAssignmentAPI)
from databricks.sdk.service.jobs import JobsAPI
from databricks.sdk.service.ml import ExperimentsAPI, ModelRegistryAPI
from databricks.sdk.service.oauth2 import (CustomAppIntegrationAPI,
                                           OAuthPublishedAppsAPI,
                                           PublishedAppIntegrationAPI,
                                           ServicePrincipalSecretsAPI)
from databricks.sdk.service.pipelines import PipelinesAPI
from databricks.sdk.service.provisioning import (CredentialsAPI,
                                                 EncryptionKeysAPI,
                                                 NetworksAPI, PrivateAccessAPI,
                                                 StorageAPI, VpcEndpointsAPI,
                                                 WorkspacesAPI)
from databricks.sdk.service.serving import AppsAPI, ServingEndpointsAPI
from databricks.sdk.service.settings import (AccountIpAccessListsAPI,
                                             AccountSettingsAPI,
                                             CredentialsManagerAPI,
                                             IpAccessListsAPI,
                                             NetworkConnectivityAPI,
                                             SettingsAPI, TokenManagementAPI,
                                             TokensAPI, WorkspaceConfAPI)
from databricks.sdk.service.sharing import (CleanRoomsAPI, ProvidersAPI,
                                            RecipientActivationAPI,
                                            RecipientsAPI, SharesAPI)
from databricks.sdk.service.sql import (AlertsAPI, DashboardsAPI,
                                        DashboardWidgetsAPI, DataSourcesAPI,
                                        DbsqlPermissionsAPI, QueriesAPI,
                                        QueryHistoryAPI,
                                        QueryVisualizationsAPI,
                                        StatementExecutionAPI, WarehousesAPI)
from databricks.sdk.service.workspace import (GitCredentialsAPI, ReposAPI,
                                              SecretsAPI, WorkspaceAPI)


def _make_dbutils(config: client.Config):
    # We try to directly check if we are in runtime, instead of
    # trying to import from databricks.sdk.runtime. This is to prevent
    # remote dbutils from being created without the config, which is both
    # expensive (will need to check all credential providers) and can
    # throw errors (when no env vars are set).
    try:
        from dbruntime import UserNamespaceInitializer
    except ImportError:
        return dbutils.RemoteDbUtils(config)

    # We are in runtime, so we can use the runtime dbutils
    from databricks.sdk.runtime import dbutils as runtime_dbutils
    return runtime_dbutils


class WorkspaceClient:
    """
    The WorkspaceClient is a client for the workspace-level Databricks REST API.
    """

    def __init__(self,
                 *,
                 host: str = None,
                 account_id: str = None,
                 username: str = None,
                 password: str = None,
                 client_id: str = None,
                 client_secret: str = None,
                 token: str = None,
                 profile: str = None,
                 config_file: str = None,
                 azure_workspace_resource_id: str = None,
                 azure_client_secret: str = None,
                 azure_client_id: str = None,
                 azure_tenant_id: str = None,
                 azure_environment: str = None,
                 auth_type: str = None,
                 cluster_id: str = None,
                 google_credentials: str = None,
                 google_service_account: str = None,
                 debug_truncate_bytes: int = None,
                 debug_headers: bool = None,
                 product="unknown",
                 product_version="0.0.0",
                 credentials_provider: client.CredentialsProvider = None,
                 config: client.Config = None):
        if not config:
            config = client.Config(host=host,
                                   account_id=account_id,
                                   username=username,
                                   password=password,
                                   client_id=client_id,
                                   client_secret=client_secret,
                                   token=token,
                                   profile=profile,
                                   config_file=config_file,
                                   azure_workspace_resource_id=azure_workspace_resource_id,
                                   azure_client_secret=azure_client_secret,
                                   azure_client_id=azure_client_id,
                                   azure_tenant_id=azure_tenant_id,
                                   azure_environment=azure_environment,
                                   auth_type=auth_type,
                                   cluster_id=cluster_id,
                                   google_credentials=google_credentials,
                                   google_service_account=google_service_account,
                                   credentials_provider=credentials_provider,
                                   debug_truncate_bytes=debug_truncate_bytes,
                                   debug_headers=debug_headers,
                                   product=product,
                                   product_version=product_version)
        self.config = config.copy()
        self.dbutils = _make_dbutils(self.config)
        self.api_client = client.ApiClient(self.config)
        self.account_access_control_proxy: AccountAccessControlProxyAPI = AccountAccessControlProxyAPI(
            self.api_client)
        """These APIs manage access rules on resources in an account. Currently, only grant rules are
        supported. A grant rule specifies a role assigned to a set of principals. A list of rules
        attached to a resource is called a rule set. A workspace must belong to an account for these
        APIs to work."""

        self.alerts: AlertsAPI = AlertsAPI(self.api_client)
        """The alerts API can be used to perform CRUD operations on alerts. An alert is a Databricks
        SQL object that periodically runs a query, evaluates a condition of its result, and notifies
        one or more users and/or notification destinations if the condition was met. Alerts can be
        scheduled using the `sql_task` type of the Jobs API, e.g. :method:jobs/create."""

        self.apps: AppsAPI = AppsAPI(self.api_client)
        """Lakehouse Apps run directly on a customer’s Databricks instance, integrate with their
        data, use and extend Databricks services, and enable users to interact through single
        sign-on."""

        self.artifact_allowlists: ArtifactAllowlistsAPI = ArtifactAllowlistsAPI(self.api_client)
        """In Databricks Runtime 13.3 and above, you can add libraries and init scripts to the
        `allowlist` in UC so that users can leverage these artifacts on compute configured with
        shared access mode."""

        self.catalogs: CatalogsAPI = CatalogsAPI(self.api_client)
        """A catalog is the first layer of Unity Catalog’s three-level namespace. It’s used to
        organize your data assets. Users can see all catalogs on which they have been assigned the
        USE_CATALOG data permission.
        
        In Unity Catalog, admins and data stewards manage users and their access to data centrally
        across all of the workspaces in a Databricks account. Users in different workspaces can
        share access to the same data, depending on privileges granted centrally in Unity Catalog."""

        self.clean_rooms: CleanRoomsAPI = CleanRoomsAPI(self.api_client)
        """A clean room is a secure, privacy-protecting environment where two or more parties can share
        sensitive enterprise data, including customer data, for measurements, insights, activation
        and other use cases.
        
        To create clean rooms, you must be a metastore admin or a user with the
        **CREATE_CLEAN_ROOM** privilege."""

        self.cluster_policies: ClusterPoliciesAPI = ClusterPoliciesAPI(self.api_client)
        """You can use cluster policies to control users' ability to configure clusters based on a set
        of rules. These rules specify which attributes or attribute values can be used during
        cluster creation. Cluster policies have ACLs that limit their use to specific users and
        groups.
        
        With cluster policies, you can: - Auto-install cluster libraries on the next restart by
        listing them in the policy's "libraries" field. - Limit users to creating clusters with the
        prescribed settings. - Simplify the user interface, enabling more users to create clusters,
        by fixing and hiding some fields. - Manage costs by setting limits on attributes that impact
        the hourly rate.
        
        Cluster policy permissions limit which policies a user can select in the Policy drop-down
        when the user creates a cluster: - A user who has unrestricted cluster create permission can
        select the Unrestricted policy and create fully-configurable clusters. - A user who has both
        unrestricted cluster create permission and access to cluster policies can select the
        Unrestricted policy and policies they have access to. - A user that has access to only
        cluster policies, can select the policies they have access to.
        
        If no policies exist in the workspace, the Policy drop-down doesn't appear. Only admin users
        can create, edit, and delete policies. Admin users also have access to all policies."""

        self.clusters: ClustersExt = ClustersExt(self.api_client)
        """The Clusters API allows you to create, start, edit, list, terminate, and delete clusters.
        
        Databricks maps cluster node instance types to compute units known as DBUs. See the instance
        type pricing page for a list of the supported instance types and their corresponding DBUs.
        
        A Databricks cluster is a set of computation resources and configurations on which you run
        data engineering, data science, and data analytics workloads, such as production ETL
        pipelines, streaming analytics, ad-hoc analytics, and machine learning.
        
        You run these workloads as a set of commands in a notebook or as an automated job.
        Databricks makes a distinction between all-purpose clusters and job clusters. You use
        all-purpose clusters to analyze data collaboratively using interactive notebooks. You use
        job clusters to run fast and robust automated jobs.
        
        You can create an all-purpose cluster using the UI, CLI, or REST API. You can manually
        terminate and restart an all-purpose cluster. Multiple users can share such clusters to do
        collaborative interactive analysis.
        
        IMPORTANT: Databricks retains cluster configuration information for up to 200 all-purpose
        clusters terminated in the last 30 days and up to 30 job clusters recently terminated by the
        job scheduler. To keep an all-purpose cluster configuration even after it has been
        terminated for more than 30 days, an administrator can pin a cluster to the cluster list."""

        self.command_execution: CommandExecutionAPI = CommandExecutionAPI(self.api_client)
        """This API allows execution of Python, Scala, SQL, or R commands on running Databricks
        Clusters."""

        self.connections: ConnectionsAPI = ConnectionsAPI(self.api_client)
        """Connections allow for creating a connection to an external data source.
        
        A connection is an abstraction of an external data source that can be connected from
        Databricks Compute. Creating a connection object is the first step to managing external data
        sources within Unity Catalog, with the second step being creating a data object (catalog,
        schema, or table) using the connection. Data objects derived from a connection can be
        written to or read from similar to other Unity Catalog data objects based on cloud storage.
        Users may create different types of connections with each connection having a unique set of
        configuration options to support credential management and other settings."""

        self.credentials_manager: CredentialsManagerAPI = CredentialsManagerAPI(self.api_client)
        """Credentials manager interacts with with Identity Providers to to perform token exchanges
        using stored credentials and refresh tokens."""

        self.current_user: CurrentUserAPI = CurrentUserAPI(self.api_client)
        """This API allows retrieving information about currently authenticated user or service
        principal."""

        self.dashboard_widgets: DashboardWidgetsAPI = DashboardWidgetsAPI(self.api_client)
        """This is an evolving API that facilitates the addition and removal of widgets from existing
        dashboards within the Databricks Workspace. Data structures may change over time."""

        self.dashboards: DashboardsAPI = DashboardsAPI(self.api_client)
        """In general, there is little need to modify dashboards using the API. However, it can be
        useful to use dashboard objects to look-up a collection of related query IDs. The API can
        also be used to duplicate multiple dashboards at once since you can get a dashboard
        definition with a GET request and then POST it to create a new one. Dashboards can be
        scheduled using the `sql_task` type of the Jobs API, e.g. :method:jobs/create."""

        self.data_sources: DataSourcesAPI = DataSourcesAPI(self.api_client)
        """This API is provided to assist you in making new query objects. When creating a query
        object, you may optionally specify a `data_source_id` for the SQL warehouse against which it
        will run. If you don't already know the `data_source_id` for your desired SQL warehouse,
        this API will help you find it.
        
        This API does not support searches. It returns the full list of SQL warehouses in your
        workspace. We advise you to use any text editor, REST client, or `grep` to search the
        response from this API for the name of your SQL warehouse as it appears in Databricks SQL."""

        self.dbfs: DbfsExt = DbfsExt(self.api_client)
        """DBFS API makes it simple to interact with various data sources without having to include a
        users credentials every time to read a file."""

        self.dbsql_permissions: DbsqlPermissionsAPI = DbsqlPermissionsAPI(self.api_client)
        """The SQL Permissions API is similar to the endpoints of the :method:permissions/set. However,
        this exposes only one endpoint, which gets the Access Control List for a given object. You
        cannot modify any permissions using this API.
        
        There are three levels of permission:
        
        - `CAN_VIEW`: Allows read-only access
        
        - `CAN_RUN`: Allows read access and run access (superset of `CAN_VIEW`)
        
        - `CAN_MANAGE`: Allows all actions: read, run, edit, delete, modify permissions (superset of
        `CAN_RUN`)"""

        self.experiments: ExperimentsAPI = ExperimentsAPI(self.api_client)
        """Experiments are the primary unit of organization in MLflow; all MLflow runs belong to an
        experiment. Each experiment lets you visualize, search, and compare runs, as well as
        download run artifacts or metadata for analysis in other tools. Experiments are maintained
        in a Databricks hosted MLflow tracking server.
        
        Experiments are located in the workspace file tree. You manage experiments using the same
        tools you use to manage other workspace objects such as folders, notebooks, and libraries."""

        self.external_locations: ExternalLocationsAPI = ExternalLocationsAPI(self.api_client)
        """An external location is an object that combines a cloud storage path with a storage
        credential that authorizes access to the cloud storage path. Each external location is
        subject to Unity Catalog access-control policies that control which users and groups can
        access the credential. If a user does not have access to an external location in Unity
        Catalog, the request fails and Unity Catalog does not attempt to authenticate to your cloud
        tenant on the user’s behalf.
        
        Databricks recommends using external locations rather than using storage credentials
        directly.
        
        To create external locations, you must be a metastore admin or a user with the
        **CREATE_EXTERNAL_LOCATION** privilege."""

        self.files: FilesAPI = FilesAPI(self.api_client)
        """The Files API allows you to read, write, and delete files and directories in Unity Catalog
        volumes."""

        self.functions: FunctionsAPI = FunctionsAPI(self.api_client)
        """Functions implement User-Defined Functions (UDFs) in Unity Catalog.
        
        The function implementation can be any SQL expression or Query, and it can be invoked
        wherever a table reference is allowed in a query. In Unity Catalog, a function resides at
        the same level as a table, so it can be referenced with the form
        __catalog_name__.__schema_name__.__function_name__."""

        self.git_credentials: GitCredentialsAPI = GitCredentialsAPI(self.api_client)
        """Registers personal access token for Databricks to do operations on behalf of the user.
        
        See [more info].
        
        [more info]: https://docs.databricks.com/repos/get-access-tokens-from-git-provider.html"""

        self.global_init_scripts: GlobalInitScriptsAPI = GlobalInitScriptsAPI(self.api_client)
        """The Global Init Scripts API enables Workspace administrators to configure global
        initialization scripts for their workspace. These scripts run on every node in every cluster
        in the workspace.
        
        **Important:** Existing clusters must be restarted to pick up any changes made to global
        init scripts. Global init scripts are run in order. If the init script returns with a bad
        exit code, the Apache Spark container fails to launch and init scripts with later position
        are skipped. If enough containers fail, the entire cluster fails with a
        `GLOBAL_INIT_SCRIPT_FAILURE` error code."""

        self.grants: GrantsAPI = GrantsAPI(self.api_client)
        """In Unity Catalog, data is secure by default. Initially, users have no access to data in a
        metastore. Access can be granted by either a metastore admin, the owner of an object, or the
        owner of the catalog or schema that contains the object. Securable objects in Unity Catalog
        are hierarchical and privileges are inherited downward.
        
        Securable objects in Unity Catalog are hierarchical and privileges are inherited downward.
        This means that granting a privilege on the catalog automatically grants the privilege to
        all current and future objects within the catalog. Similarly, privileges granted on a schema
        are inherited by all current and future objects within that schema."""

        self.groups: GroupsAPI = GroupsAPI(self.api_client)
        """Groups simplify identity management, making it easier to assign access to Databricks
        workspace, data, and other securable objects.
        
        It is best practice to assign access to workspaces and access-control policies in Unity
        Catalog to groups, instead of to users individually. All Databricks workspace identities can
        be assigned as members of groups, and members inherit permissions that are assigned to their
        group."""

        self.instance_pools: InstancePoolsAPI = InstancePoolsAPI(self.api_client)
        """Instance Pools API are used to create, edit, delete and list instance pools by using
        ready-to-use cloud instances which reduces a cluster start and auto-scaling times.
        
        Databricks pools reduce cluster start and auto-scaling times by maintaining a set of idle,
        ready-to-use instances. When a cluster is attached to a pool, cluster nodes are created
        using the pool’s idle instances. If the pool has no idle instances, the pool expands by
        allocating a new instance from the instance provider in order to accommodate the cluster’s
        request. When a cluster releases an instance, it returns to the pool and is free for another
        cluster to use. Only clusters attached to a pool can use that pool’s idle instances.
        
        You can specify a different pool for the driver node and worker nodes, or use the same pool
        for both.
        
        Databricks does not charge DBUs while instances are idle in the pool. Instance provider
        billing does apply. See pricing."""

        self.instance_profiles: InstanceProfilesAPI = InstanceProfilesAPI(self.api_client)
        """The Instance Profiles API allows admins to add, list, and remove instance profiles that
        users can launch clusters with. Regular users can list the instance profiles available to
        them. See [Secure access to S3 buckets] using instance profiles for more information.
        
        [Secure access to S3 buckets]: https://docs.databricks.com/administration-guide/cloud-configurations/aws/instance-profiles.html"""

        self.ip_access_lists: IpAccessListsAPI = IpAccessListsAPI(self.api_client)
        """IP Access List enables admins to configure IP access lists.
        
        IP access lists affect web application access and REST API access to this workspace only. If
        the feature is disabled for a workspace, all access is allowed for this workspace. There is
        support for allow lists (inclusion) and block lists (exclusion).
        
        When a connection is attempted: 1. **First, all block lists are checked.** If the connection
        IP address matches any block list, the connection is rejected. 2. **If the connection was
        not rejected by block lists**, the IP address is compared with the allow lists.
        
        If there is at least one allow list for the workspace, the connection is allowed only if the
        IP address matches an allow list. If there are no allow lists for the workspace, all IP
        addresses are allowed.
        
        For all allow lists and block lists combined, the workspace supports a maximum of 1000
        IP/CIDR values, where one CIDR counts as a single value.
        
        After changes to the IP access list feature, it can take a few minutes for changes to take
        effect."""

        self.jobs: JobsAPI = JobsAPI(self.api_client)
        """The Jobs API allows you to create, edit, and delete jobs.
        
        You can use a Databricks job to run a data processing or data analysis task in a Databricks
        cluster with scalable resources. Your job can consist of a single task or can be a large,
        multi-task workflow with complex dependencies. Databricks manages the task orchestration,
        cluster management, monitoring, and error reporting for all of your jobs. You can run your
        jobs immediately or periodically through an easy-to-use scheduling system. You can implement
        job tasks using notebooks, JARS, Delta Live Tables pipelines, or Python, Scala, Spark
        submit, and Java applications.
        
        You should never hard code secrets or store them in plain text. Use the [Secrets CLI] to
        manage secrets in the [Databricks CLI]. Use the [Secrets utility] to reference secrets in
        notebooks and jobs.
        
        [Databricks CLI]: https://docs.databricks.com/dev-tools/cli/index.html
        [Secrets CLI]: https://docs.databricks.com/dev-tools/cli/secrets-cli.html
        [Secrets utility]: https://docs.databricks.com/dev-tools/databricks-utils.html#dbutils-secrets"""

        self.libraries: LibrariesAPI = LibrariesAPI(self.api_client)
        """The Libraries API allows you to install and uninstall libraries and get the status of
        libraries on a cluster.
        
        To make third-party or custom code available to notebooks and jobs running on your clusters,
        you can install a library. Libraries can be written in Python, Java, Scala, and R. You can
        upload Java, Scala, and Python libraries and point to external packages in PyPI, Maven, and
        CRAN repositories.
        
        Cluster libraries can be used by all notebooks running on a cluster. You can install a
        cluster library directly from a public repository such as PyPI or Maven, using a previously
        installed workspace library, or using an init script.
        
        When you install a library on a cluster, a notebook already attached to that cluster will
        not immediately see the new library. You must first detach and then reattach the notebook to
        the cluster.
        
        When you uninstall a library from a cluster, the library is removed only when you restart
        the cluster. Until you restart the cluster, the status of the uninstalled library appears as
        Uninstall pending restart."""

        self.metastores: MetastoresAPI = MetastoresAPI(self.api_client)
        """A metastore is the top-level container of objects in Unity Catalog. It stores data assets
        (tables and views) and the permissions that govern access to them. Databricks account admins
        can create metastores and assign them to Databricks workspaces to control which workloads
        use each metastore. For a workspace to use Unity Catalog, it must have a Unity Catalog
        metastore attached.
        
        Each metastore is configured with a root storage location in a cloud storage account. This
        storage location is used for metadata and managed tables data.
        
        NOTE: This metastore is distinct from the metastore included in Databricks workspaces
        created before Unity Catalog was released. If your workspace includes a legacy Hive
        metastore, the data in that metastore is available in a catalog named hive_metastore."""

        self.model_registry: ModelRegistryAPI = ModelRegistryAPI(self.api_client)
        """Note: This API reference documents APIs for the Workspace Model Registry. Databricks
        recommends using [Models in Unity Catalog](/api/workspace/registeredmodels) instead. Models
        in Unity Catalog provides centralized model governance, cross-workspace access, lineage, and
        deployment. Workspace Model Registry will be deprecated in the future.
        
        The Workspace Model Registry is a centralized model repository and a UI and set of APIs that
        enable you to manage the full lifecycle of MLflow Models."""

        self.model_versions: ModelVersionsAPI = ModelVersionsAPI(self.api_client)
        """Databricks provides a hosted version of MLflow Model Registry in Unity Catalog. Models in
        Unity Catalog provide centralized access control, auditing, lineage, and discovery of ML
        models across Databricks workspaces.
        
        This API reference documents the REST endpoints for managing model versions in Unity
        Catalog. For more details, see the [registered models API
        docs](/api/workspace/registeredmodels)."""

        self.permissions: PermissionsAPI = PermissionsAPI(self.api_client)
        """Permissions API are used to create read, write, edit, update and manage access for various
        users on different objects and endpoints.
        
        * **[Cluster permissions](:service:clusters)** — Manage which users can manage, restart,
        or attach to clusters.
        
        * **[Cluster policy permissions](:service:clusterpolicies)** — Manage which users can use
        cluster policies.
        
        * **[Delta Live Tables pipeline permissions](:service:pipelines)** — Manage which users
        can view, manage, run, cancel, or own a Delta Live Tables pipeline.
        
        * **[Job permissions](:service:jobs)** — Manage which users can view, manage, trigger,
        cancel, or own a job.
        
        * **[MLflow experiment permissions](:service:experiments)** — Manage which users can read,
        edit, or manage MLflow experiments.
        
        * **[MLflow registered model permissions](:service:modelregistry)** — Manage which users
        can read, edit, or manage MLflow registered models.
        
        * **[Password permissions](:service:users)** — Manage which users can use password login
        when SSO is enabled.
        
        * **[Instance Pool permissions](:service:instancepools)** — Manage which users can manage
        or attach to pools.
        
        * **[Repo permissions](repos)** — Manage which users can read, run, edit, or manage a
        repo.
        
        * **[Serving endpoint permissions](:service:servingendpoints)** — Manage which users can
        view, query, or manage a serving endpoint.
        
        * **[SQL warehouse permissions](:service:warehouses)** — Manage which users can use or
        manage SQL warehouses.
        
        * **[Token permissions](:service:tokenmanagement)** — Manage which users can create or use
        tokens.
        
        * **[Workspace object permissions](:service:workspace)** — Manage which users can read,
        run, edit, or manage directories, files, and notebooks.
        
        For the mapping of the required permissions for specific actions or abilities and other
        important information, see [Access Control].
        
        [Access Control]: https://docs.databricks.com/security/auth-authz/access-control/index.html"""

        self.pipelines: PipelinesAPI = PipelinesAPI(self.api_client)
        """The Delta Live Tables API allows you to create, edit, delete, start, and view details about
        pipelines.
        
        Delta Live Tables is a framework for building reliable, maintainable, and testable data
        processing pipelines. You define the transformations to perform on your data, and Delta Live
        Tables manages task orchestration, cluster management, monitoring, data quality, and error
        handling.
        
        Instead of defining your data pipelines using a series of separate Apache Spark tasks, Delta
        Live Tables manages how your data is transformed based on a target schema you define for
        each processing step. You can also enforce data quality with Delta Live Tables expectations.
        Expectations allow you to define expected data quality and specify how to handle records
        that fail those expectations."""

        self.policy_families: PolicyFamiliesAPI = PolicyFamiliesAPI(self.api_client)
        """View available policy families. A policy family contains a policy definition providing best
        practices for configuring clusters for a particular use case.
        
        Databricks manages and provides policy families for several common cluster use cases. You
        cannot create, edit, or delete policy families.
        
        Policy families cannot be used directly to create clusters. Instead, you create cluster
        policies using a policy family. Cluster policies created using a policy family inherit the
        policy family's policy definition."""

        self.providers: ProvidersAPI = ProvidersAPI(self.api_client)
        """A data provider is an object representing the organization in the real world who shares the
        data. A provider contains shares which further contain the shared data."""

        self.queries: QueriesAPI = QueriesAPI(self.api_client)
        """These endpoints are used for CRUD operations on query definitions. Query definitions include
        the target SQL warehouse, query text, name, description, tags, parameters, and
        visualizations. Queries can be scheduled using the `sql_task` type of the Jobs API, e.g.
        :method:jobs/create."""

        self.query_history: QueryHistoryAPI = QueryHistoryAPI(self.api_client)
        """Access the history of queries through SQL warehouses."""

        self.query_visualizations: QueryVisualizationsAPI = QueryVisualizationsAPI(self.api_client)
        """This is an evolving API that facilitates the addition and removal of vizualisations from
        existing queries within the Databricks Workspace. Data structures may change over time."""

        self.recipient_activation: RecipientActivationAPI = RecipientActivationAPI(self.api_client)
        """The Recipient Activation API is only applicable in the open sharing model where the
        recipient object has the authentication type of `TOKEN`. The data recipient follows the
        activation link shared by the data provider to download the credential file that includes
        the access token. The recipient will then use the credential file to establish a secure
        connection with the provider to receive the shared data.
        
        Note that you can download the credential file only once. Recipients should treat the
        downloaded credential as a secret and must not share it outside of their organization."""

        self.recipients: RecipientsAPI = RecipientsAPI(self.api_client)
        """A recipient is an object you create using :method:recipients/create to represent an
        organization which you want to allow access shares. The way how sharing works differs
        depending on whether or not your recipient has access to a Databricks workspace that is
        enabled for Unity Catalog:
        
        - For recipients with access to a Databricks workspace that is enabled for Unity Catalog,
        you can create a recipient object along with a unique sharing identifier you get from the
        recipient. The sharing identifier is the key identifier that enables the secure connection.
        This sharing mode is called **Databricks-to-Databricks sharing**.
        
        - For recipients without access to a Databricks workspace that is enabled for Unity Catalog,
        when you create a recipient object, Databricks generates an activation link you can send to
        the recipient. The recipient follows the activation link to download the credential file,
        and then uses the credential file to establish a secure connection to receive the shared
        data. This sharing mode is called **open sharing**."""

        self.registered_models: RegisteredModelsAPI = RegisteredModelsAPI(self.api_client)
        """Databricks provides a hosted version of MLflow Model Registry in Unity Catalog. Models in
        Unity Catalog provide centralized access control, auditing, lineage, and discovery of ML
        models across Databricks workspaces.
        
        An MLflow registered model resides in the third layer of Unity Catalog’s three-level
        namespace. Registered models contain model versions, which correspond to actual ML models
        (MLflow models). Creating new model versions currently requires use of the MLflow Python
        client. Once model versions are created, you can load them for batch inference using MLflow
        Python client APIs, or deploy them for real-time serving using Databricks Model Serving.
        
        All operations on registered models and model versions require USE_CATALOG permissions on
        the enclosing catalog and USE_SCHEMA permissions on the enclosing schema. In addition, the
        following additional privileges are required for various operations:
        
        * To create a registered model, users must additionally have the CREATE_MODEL permission on
        the target schema. * To view registered model or model version metadata, model version data
        files, or invoke a model version, users must additionally have the EXECUTE permission on the
        registered model * To update registered model or model version tags, users must additionally
        have APPLY TAG permissions on the registered model * To update other registered model or
        model version metadata (comments, aliases) create a new model version, or update permissions
        on the registered model, users must be owners of the registered model.
        
        Note: The securable type for models is "FUNCTION". When using REST APIs (e.g. tagging,
        grants) that specify a securable type, use "FUNCTION" as the securable type."""

        self.repos: ReposAPI = ReposAPI(self.api_client)
        """The Repos API allows users to manage their git repos. Users can use the API to access all
        repos that they have manage permissions on.
        
        Databricks Repos is a visual Git client in Databricks. It supports common Git operations
        such a cloning a repository, committing and pushing, pulling, branch management, and visual
        comparison of diffs when committing.
        
        Within Repos you can develop code in notebooks or other files and follow data science and
        engineering code development best practices using Git for version control, collaboration,
        and CI/CD."""

        self.schemas: SchemasAPI = SchemasAPI(self.api_client)
        """A schema (also called a database) is the second layer of Unity Catalog’s three-level
        namespace. A schema organizes tables, views and functions. To access (or list) a table or
        view in a schema, users must have the USE_SCHEMA data permission on the schema and its
        parent catalog, and they must have the SELECT permission on the table or view."""

        self.secrets: SecretsAPI = SecretsAPI(self.api_client)
        """The Secrets API allows you to manage secrets, secret scopes, and access permissions.
        
        Sometimes accessing data requires that you authenticate to external data sources through
        JDBC. Instead of directly entering your credentials into a notebook, use Databricks secrets
        to store your credentials and reference them in notebooks and jobs.
        
        Administrators, secret creators, and users granted permission can read Databricks secrets.
        While Databricks makes an effort to redact secret values that might be displayed in
        notebooks, it is not possible to prevent such users from reading secrets."""

        self.service_principals: ServicePrincipalsAPI = ServicePrincipalsAPI(self.api_client)
        """Identities for use with jobs, automated tools, and systems such as scripts, apps, and CI/CD
        platforms. Databricks recommends creating service principals to run production jobs or
        modify production data. If all processes that act on production data run with service
        principals, interactive users do not need any write, delete, or modify privileges in
        production. This eliminates the risk of a user overwriting production data by accident."""

        self.serving_endpoints: ServingEndpointsAPI = ServingEndpointsAPI(self.api_client)
        """The Serving Endpoints API allows you to create, update, and delete model serving endpoints.
        
        You can use a serving endpoint to serve models from the Databricks Model Registry or from
        Unity Catalog. Endpoints expose the underlying models as scalable REST API endpoints using
        serverless compute. This means the endpoints and associated compute resources are fully
        managed by Databricks and will not appear in your cloud account. A serving endpoint can
        consist of one or more MLflow models from the Databricks Model Registry, called served
        entities. A serving endpoint can have at most ten served entities. You can configure traffic
        settings to define how requests should be routed to your served entities behind an endpoint.
        Additionally, you can configure the scale of resources that should be applied to each served
        entity."""

        self.settings: SettingsAPI = SettingsAPI(self.api_client)
        """The default namespace setting API allows users to configure the default namespace for a
        Databricks workspace.
        
        Through this API, users can retrieve, set, or modify the default namespace used when queries
        do not reference a fully qualified three-level name. For example, if you use the API to set
        'retail_prod' as the default catalog, then a query 'SELECT * FROM myTable' would reference
        the object 'retail_prod.default.myTable' (the schema 'default' is always assumed).
        
        This setting requires a restart of clusters and SQL warehouses to take effect. Additionally,
        the default namespace only applies when using Unity Catalog-enabled compute."""

        self.shares: SharesAPI = SharesAPI(self.api_client)
        """A share is a container instantiated with :method:shares/create. Once created you can
        iteratively register a collection of existing data assets defined within the metastore using
        :method:shares/update. You can register data assets under their original name, qualified by
        their original schema, or provide alternate exposed names."""

        self.statement_execution: StatementExecutionAPI = StatementExecutionAPI(self.api_client)
        """The Databricks SQL Statement Execution API can be used to execute SQL statements on a SQL
        warehouse and fetch the result.
        
        **Getting started**
        
        We suggest beginning with the [Databricks SQL Statement Execution API tutorial].
        
        **Overview of statement execution and result fetching**
        
        Statement execution begins by issuing a :method:statementexecution/executeStatement request
        with a valid SQL statement and warehouse ID, along with optional parameters such as the data
        catalog and output format. If no other parameters are specified, the server will wait for up
        to 10s before returning a response. If the statement has completed within this timespan, the
        response will include the result data as a JSON array and metadata. Otherwise, if no result
        is available after the 10s timeout expired, the response will provide the statement ID that
        can be used to poll for results by using a :method:statementexecution/getStatement request.
        
        You can specify whether the call should behave synchronously, asynchronously or start
        synchronously with a fallback to asynchronous execution. This is controlled with the
        `wait_timeout` and `on_wait_timeout` settings. If `wait_timeout` is set between 5-50 seconds
        (default: 10s), the call waits for results up to the specified timeout; when set to `0s`,
        the call is asynchronous and responds immediately with a statement ID. The `on_wait_timeout`
        setting specifies what should happen when the timeout is reached while the statement
        execution has not yet finished. This can be set to either `CONTINUE`, to fallback to
        asynchronous mode, or it can be set to `CANCEL`, which cancels the statement.
        
        In summary: - Synchronous mode - `wait_timeout=30s` and `on_wait_timeout=CANCEL` - The call
        waits up to 30 seconds; if the statement execution finishes within this time, the result
        data is returned directly in the response. If the execution takes longer than 30 seconds,
        the execution is canceled and the call returns with a `CANCELED` state. - Asynchronous mode
        - `wait_timeout=0s` (`on_wait_timeout` is ignored) - The call doesn't wait for the statement
        to finish but returns directly with a statement ID. The status of the statement execution
        can be polled by issuing :method:statementexecution/getStatement with the statement ID. Once
        the execution has succeeded, this call also returns the result and metadata in the response.
        - Hybrid mode (default) - `wait_timeout=10s` and `on_wait_timeout=CONTINUE` - The call waits
        for up to 10 seconds; if the statement execution finishes within this time, the result data
        is returned directly in the response. If the execution takes longer than 10 seconds, a
        statement ID is returned. The statement ID can be used to fetch status and results in the
        same way as in the asynchronous mode.
        
        Depending on the size, the result can be split into multiple chunks. If the statement
        execution is successful, the statement response contains a manifest and the first chunk of
        the result. The manifest contains schema information and provides metadata for each chunk in
        the result. Result chunks can be retrieved by index with
        :method:statementexecution/getStatementResultChunkN which may be called in any order and in
        parallel. For sequential fetching, each chunk, apart from the last, also contains a
        `next_chunk_index` and `next_chunk_internal_link` that point to the next chunk.
        
        A statement can be canceled with :method:statementexecution/cancelExecution.
        
        **Fetching result data: format and disposition**
        
        To specify the format of the result data, use the `format` field, which can be set to one of
        the following options: `JSON_ARRAY` (JSON), `ARROW_STREAM` ([Apache Arrow Columnar]), or
        `CSV`.
        
        There are two ways to receive statement results, controlled by the `disposition` setting,
        which can be either `INLINE` or `EXTERNAL_LINKS`:
        
        - `INLINE`: In this mode, the result data is directly included in the response. It's best
        suited for smaller results. This mode can only be used with the `JSON_ARRAY` format.
        
        - `EXTERNAL_LINKS`: In this mode, the response provides links that can be used to download
        the result data in chunks separately. This approach is ideal for larger results and offers
        higher throughput. This mode can be used with all the formats: `JSON_ARRAY`, `ARROW_STREAM`,
        and `CSV`.
        
        By default, the API uses `format=JSON_ARRAY` and `disposition=INLINE`.
        
        **Limits and limitations**
        
        Note: The byte limit for INLINE disposition is based on internal storage metrics and will
        not exactly match the byte count of the actual payload.
        
        - Statements with `disposition=INLINE` are limited to 25 MiB and will fail when this limit
        is exceeded. - Statements with `disposition=EXTERNAL_LINKS` are limited to 100 GiB. Result
        sets larger than this limit will be truncated. Truncation is indicated by the `truncated`
        field in the result manifest. - The maximum query text size is 16 MiB. - Cancelation might
        silently fail. A successful response from a cancel request indicates that the cancel request
        was successfully received and sent to the processing engine. However, an outstanding
        statement might have already completed execution when the cancel request arrives. Polling
        for status until a terminal state is reached is a reliable way to determine the final state.
        - Wait timeouts are approximate, occur server-side, and cannot account for things such as
        caller delays and network latency from caller to service. - The system will auto-close a
        statement after one hour if the client stops polling and thus you must poll at least once an
        hour. - The results are only available for one hour after success; polling does not extend
        this.
        
        [Apache Arrow Columnar]: https://arrow.apache.org/overview/
        [Databricks SQL Statement Execution API tutorial]: https://docs.databricks.com/sql/api/sql-execution-tutorial.html"""

        self.storage_credentials: StorageCredentialsAPI = StorageCredentialsAPI(self.api_client)
        """A storage credential represents an authentication and authorization mechanism for accessing
        data stored on your cloud tenant. Each storage credential is subject to Unity Catalog
        access-control policies that control which users and groups can access the credential. If a
        user does not have access to a storage credential in Unity Catalog, the request fails and
        Unity Catalog does not attempt to authenticate to your cloud tenant on the user’s behalf.
        
        Databricks recommends using external locations rather than using storage credentials
        directly.
        
        To create storage credentials, you must be a Databricks account admin. The account admin who
        creates the storage credential can delegate ownership to another user or group to manage
        permissions on it."""

        self.system_schemas: SystemSchemasAPI = SystemSchemasAPI(self.api_client)
        """A system schema is a schema that lives within the system catalog. A system schema may
        contain information about customer usage of Unity Catalog such as audit-logs, billing-logs,
        lineage information, etc."""

        self.table_constraints: TableConstraintsAPI = TableConstraintsAPI(self.api_client)
        """Primary key and foreign key constraints encode relationships between fields in tables.
        
        Primary and foreign keys are informational only and are not enforced. Foreign keys must
        reference a primary key in another table. This primary key is the parent constraint of the
        foreign key and the table this primary key is on is the parent table of the foreign key.
        Similarly, the foreign key is the child constraint of its referenced primary key; the table
        of the foreign key is the child table of the primary key.
        
        You can declare primary keys and foreign keys as part of the table specification during
        table creation. You can also add or drop constraints on existing tables."""

        self.tables: TablesAPI = TablesAPI(self.api_client)
        """A table resides in the third layer of Unity Catalog’s three-level namespace. It contains
        rows of data. To create a table, users must have CREATE_TABLE and USE_SCHEMA permissions on
        the schema, and they must have the USE_CATALOG permission on its parent catalog. To query a
        table, users must have the SELECT permission on the table, and they must have the
        USE_CATALOG permission on its parent catalog and the USE_SCHEMA permission on its parent
        schema.
        
        A table can be managed or external. From an API perspective, a __VIEW__ is a particular kind
        of table (rather than a managed or external table)."""

        self.token_management: TokenManagementAPI = TokenManagementAPI(self.api_client)
        """Enables administrators to get all tokens and delete tokens for other users. Admins can
        either get every token, get a specific token by ID, or get all tokens for a particular user."""

        self.tokens: TokensAPI = TokensAPI(self.api_client)
        """The Token API allows you to create, list, and revoke tokens that can be used to authenticate
        and access Databricks REST APIs."""

        self.users: UsersAPI = UsersAPI(self.api_client)
        """User identities recognized by Databricks and represented by email addresses.
        
        Databricks recommends using SCIM provisioning to sync users and groups automatically from
        your identity provider to your Databricks workspace. SCIM streamlines onboarding a new
        employee or team by using your identity provider to create users and groups in Databricks
        workspace and give them the proper level of access. When a user leaves your organization or
        no longer needs access to Databricks workspace, admins can terminate the user in your
        identity provider and that user’s account will also be removed from Databricks workspace.
        This ensures a consistent offboarding process and prevents unauthorized users from accessing
        sensitive data."""

        self.volumes: VolumesAPI = VolumesAPI(self.api_client)
        """Volumes are a Unity Catalog (UC) capability for accessing, storing, governing, organizing
        and processing files. Use cases include running machine learning on unstructured data such
        as image, audio, video, or PDF files, organizing data sets during the data exploration
        stages in data science, working with libraries that require access to the local file system
        on cluster machines, storing library and config files of arbitrary formats such as .whl or
        .txt centrally and providing secure access across workspaces to it, or transforming and
        querying non-tabular data files in ETL."""

        self.warehouses: WarehousesAPI = WarehousesAPI(self.api_client)
        """A SQL warehouse is a compute resource that lets you run SQL commands on data objects within
        Databricks SQL. Compute resources are infrastructure resources that provide processing
        capabilities in the cloud."""

        self.workspace: WorkspaceExt = WorkspaceExt(self.api_client)
        """The Workspace API allows you to list, import, export, and delete notebooks and folders.
        
        A notebook is a web-based interface to a document that contains runnable code,
        visualizations, and explanatory text."""

        self.workspace_bindings: WorkspaceBindingsAPI = WorkspaceBindingsAPI(self.api_client)
        """A securable in Databricks can be configured as __OPEN__ or __ISOLATED__. An __OPEN__
        securable can be accessed from any workspace, while an __ISOLATED__ securable can only be
        accessed from a configured list of workspaces. This API allows you to configure (bind)
        securables to workspaces.
        
        NOTE: The __isolation_mode__ is configured for the securable itself (using its Update
        method) and the workspace bindings are only consulted when the securable's
        __isolation_mode__ is set to __ISOLATED__.
        
        A securable's workspace bindings can be configured by a metastore admin or the owner of the
        securable.
        
        The original path (/api/2.1/unity-catalog/workspace-bindings/catalogs/{name}) is deprecated.
        Please use the new path (/api/2.1/unity-catalog/bindings/{securable_type}/{securable_name})
        which introduces the ability to bind a securable in READ_ONLY mode (catalogs only).
        
        Securables that support binding: - catalog"""

        self.workspace_conf: WorkspaceConfAPI = WorkspaceConfAPI(self.api_client)
        """This API allows updating known workspace settings for advanced users."""


class AccountClient:
    """
    The AccountClient is a client for the account-level Databricks REST API.
    """

    def __init__(self,
                 *,
                 host: str = None,
                 account_id: str = None,
                 username: str = None,
                 password: str = None,
                 client_id: str = None,
                 client_secret: str = None,
                 token: str = None,
                 profile: str = None,
                 config_file: str = None,
                 azure_workspace_resource_id: str = None,
                 azure_client_secret: str = None,
                 azure_client_id: str = None,
                 azure_tenant_id: str = None,
                 azure_environment: str = None,
                 auth_type: str = None,
                 cluster_id: str = None,
                 google_credentials: str = None,
                 google_service_account: str = None,
                 debug_truncate_bytes: int = None,
                 debug_headers: bool = None,
                 product="unknown",
                 product_version="0.0.0",
                 credentials_provider: client.CredentialsProvider = None,
                 config: client.Config = None):
        if not config:
            config = client.Config(host=host,
                                   account_id=account_id,
                                   username=username,
                                   password=password,
                                   client_id=client_id,
                                   client_secret=client_secret,
                                   token=token,
                                   profile=profile,
                                   config_file=config_file,
                                   azure_workspace_resource_id=azure_workspace_resource_id,
                                   azure_client_secret=azure_client_secret,
                                   azure_client_id=azure_client_id,
                                   azure_tenant_id=azure_tenant_id,
                                   azure_environment=azure_environment,
                                   auth_type=auth_type,
                                   cluster_id=cluster_id,
                                   google_credentials=google_credentials,
                                   google_service_account=google_service_account,
                                   credentials_provider=credentials_provider,
                                   debug_truncate_bytes=debug_truncate_bytes,
                                   debug_headers=debug_headers,
                                   product=product,
                                   product_version=product_version)
        self.config = config.copy()
        self.api_client = client.ApiClient(self.config)
        self.access_control: AccountAccessControlAPI = AccountAccessControlAPI(self.api_client)
        """These APIs manage access rules on resources in an account. Currently, only grant rules are
        supported. A grant rule specifies a role assigned to a set of principals. A list of rules
        attached to a resource is called a rule set."""

        self.billable_usage: BillableUsageAPI = BillableUsageAPI(self.api_client)
        """This API allows you to download billable usage logs for the specified account and date
        range. This feature works with all account types."""

        self.budgets: BudgetsAPI = BudgetsAPI(self.api_client)
        """These APIs manage budget configuration including notifications for exceeding a budget for a
        period. They can also retrieve the status of each budget."""

        self.credentials: CredentialsAPI = CredentialsAPI(self.api_client)
        """These APIs manage credential configurations for this workspace. Databricks needs access to a
        cross-account service IAM role in your AWS account so that Databricks can deploy clusters in
        the appropriate VPC for the new workspace. A credential configuration encapsulates this role
        information, and its ID is used when creating a new workspace."""

        self.custom_app_integration: CustomAppIntegrationAPI = CustomAppIntegrationAPI(self.api_client)
        """These APIs enable administrators to manage custom oauth app integrations, which is required
        for adding/using Custom OAuth App Integration like Tableau Cloud for Databricks in AWS
        cloud."""

        self.encryption_keys: EncryptionKeysAPI = EncryptionKeysAPI(self.api_client)
        """These APIs manage encryption key configurations for this workspace (optional). A key
        configuration encapsulates the AWS KMS key information and some information about how the
        key configuration can be used. There are two possible uses for key configurations:
        
        * Managed services: A key configuration can be used to encrypt a workspace's notebook and
        secret data in the control plane, as well as Databricks SQL queries and query history. *
        Storage: A key configuration can be used to encrypt a workspace's DBFS and EBS data in the
        data plane.
        
        In both of these cases, the key configuration's ID is used when creating a new workspace.
        This Preview feature is available if your account is on the E2 version of the platform.
        Updating a running workspace with workspace storage encryption requires that the workspace
        is on the E2 version of the platform. If you have an older workspace, it might not be on the
        E2 version of the platform. If you are not sure, contact your Databricks representative."""

        self.groups: AccountGroupsAPI = AccountGroupsAPI(self.api_client)
        """Groups simplify identity management, making it easier to assign access to Databricks
        account, data, and other securable objects.
        
        It is best practice to assign access to workspaces and access-control policies in Unity
        Catalog to groups, instead of to users individually. All Databricks account identities can
        be assigned as members of groups, and members inherit permissions that are assigned to their
        group."""

        self.ip_access_lists: AccountIpAccessListsAPI = AccountIpAccessListsAPI(self.api_client)
        """The Accounts IP Access List API enables account admins to configure IP access lists for
        access to the account console.
        
        Account IP Access Lists affect web application access and REST API access to the account
        console and account APIs. If the feature is disabled for the account, all access is allowed
        for this account. There is support for allow lists (inclusion) and block lists (exclusion).
        
        When a connection is attempted: 1. **First, all block lists are checked.** If the connection
        IP address matches any block list, the connection is rejected. 2. **If the connection was
        not rejected by block lists**, the IP address is compared with the allow lists.
        
        If there is at least one allow list for the account, the connection is allowed only if the
        IP address matches an allow list. If there are no allow lists for the account, all IP
        addresses are allowed.
        
        For all allow lists and block lists combined, the account supports a maximum of 1000 IP/CIDR
        values, where one CIDR counts as a single value.
        
        After changes to the account-level IP access lists, it can take a few minutes for changes to
        take effect."""

        self.log_delivery: LogDeliveryAPI = LogDeliveryAPI(self.api_client)
        """These APIs manage log delivery configurations for this account. The two supported log types
        for this API are _billable usage logs_ and _audit logs_. This feature is in Public Preview.
        This feature works with all account ID types.
        
        Log delivery works with all account types. However, if your account is on the E2 version of
        the platform or on a select custom plan that allows multiple workspaces per account, you can
        optionally configure different storage destinations for each workspace. Log delivery status
        is also provided to know the latest status of log delivery attempts. The high-level flow of
        billable usage delivery:
        
        1. **Create storage**: In AWS, [create a new AWS S3 bucket] with a specific bucket policy.
        Using Databricks APIs, call the Account API to create a [storage configuration
        object](:method:Storage/Create) that uses the bucket name. 2. **Create credentials**: In
        AWS, create the appropriate AWS IAM role. For full details, including the required IAM role
        policies and trust relationship, see [Billable usage log delivery]. Using Databricks APIs,
        call the Account API to create a [credential configuration
        object](:method:Credentials/Create) that uses the IAM role"s ARN. 3. **Create log delivery
        configuration**: Using Databricks APIs, call the Account API to [create a log delivery
        configuration](:method:LogDelivery/Create) that uses the credential and storage
        configuration objects from previous steps. You can specify if the logs should include all
        events of that log type in your account (_Account level_ delivery) or only events for a
        specific set of workspaces (_workspace level_ delivery). Account level log delivery applies
        to all current and future workspaces plus account level logs, while workspace level log
        delivery solely delivers logs related to the specified workspaces. You can create multiple
        types of delivery configurations per account.
        
        For billable usage delivery: * For more information about billable usage logs, see [Billable
        usage log delivery]. For the CSV schema, see the [Usage page]. * The delivery location is
        `<bucket-name>/<prefix>/billable-usage/csv/`, where `<prefix>` is the name of the optional
        delivery path prefix you set up during log delivery configuration. Files are named
        `workspaceId=<workspace-id>-usageMonth=<month>.csv`. * All billable usage logs apply to
        specific workspaces (_workspace level_ logs). You can aggregate usage for your entire
        account by creating an _account level_ delivery configuration that delivers logs for all
        current and future workspaces in your account. * The files are delivered daily by
        overwriting the month's CSV file for each workspace.
        
        For audit log delivery: * For more information about about audit log delivery, see [Audit
        log delivery], which includes information about the used JSON schema. * The delivery
        location is
        `<bucket-name>/<delivery-path-prefix>/workspaceId=<workspaceId>/date=<yyyy-mm-dd>/auditlogs_<internal-id>.json`.
        Files may get overwritten with the same content multiple times to achieve exactly-once
        delivery. * If the audit log delivery configuration included specific workspace IDs, only
        _workspace-level_ audit logs for those workspaces are delivered. If the log delivery
        configuration applies to the entire account (_account level_ delivery configuration), the
        audit log delivery includes workspace-level audit logs for all workspaces in the account as
        well as account-level audit logs. See [Audit log delivery] for details. * Auditable events
        are typically available in logs within 15 minutes.
        
        [Audit log delivery]: https://docs.databricks.com/administration-guide/account-settings/audit-logs.html
        [Billable usage log delivery]: https://docs.databricks.com/administration-guide/account-settings/billable-usage-delivery.html
        [Usage page]: https://docs.databricks.com/administration-guide/account-settings/usage.html
        [create a new AWS S3 bucket]: https://docs.databricks.com/administration-guide/account-api/aws-storage.html"""

        self.metastore_assignments: AccountMetastoreAssignmentsAPI = AccountMetastoreAssignmentsAPI(
            self.api_client)
        """These APIs manage metastore assignments to a workspace."""

        self.metastores: AccountMetastoresAPI = AccountMetastoresAPI(self.api_client)
        """These APIs manage Unity Catalog metastores for an account. A metastore contains catalogs
        that can be associated with workspaces"""

        self.network_connectivity: NetworkConnectivityAPI = NetworkConnectivityAPI(self.api_client)
        """These APIs provide configurations for the network connectivity of your workspaces for
        serverless compute resources. This API provides stable subnets for your workspace so that
        you can configure your firewalls on your Azure Storage accounts to allow access from
        Databricks. You can also use the API to provision private endpoints for Databricks to
        privately connect serverless compute resources to your Azure resources using Azure Private
        Link. See [configure serverless secure connectivity].
        
        [configure serverless secure connectivity]: https://learn.microsoft.com/azure/databricks/security/network/serverless-network-security"""

        self.networks: NetworksAPI = NetworksAPI(self.api_client)
        """These APIs manage network configurations for customer-managed VPCs (optional). Its ID is
        used when creating a new workspace if you use customer-managed VPCs."""

        self.o_auth_published_apps: OAuthPublishedAppsAPI = OAuthPublishedAppsAPI(self.api_client)
        """These APIs enable administrators to view all the available published OAuth applications in
        Databricks. Administrators can add the published OAuth applications to their account through
        the OAuth Published App Integration APIs."""

        self.private_access: PrivateAccessAPI = PrivateAccessAPI(self.api_client)
        """These APIs manage private access settings for this account."""

        self.published_app_integration: PublishedAppIntegrationAPI = PublishedAppIntegrationAPI(
            self.api_client)
        """These APIs enable administrators to manage published oauth app integrations, which is
        required for adding/using Published OAuth App Integration like Tableau Desktop for
        Databricks in AWS cloud."""

        self.service_principal_secrets: ServicePrincipalSecretsAPI = ServicePrincipalSecretsAPI(
            self.api_client)
        """These APIs enable administrators to manage service principal secrets.
        
        You can use the generated secrets to obtain OAuth access tokens for a service principal,
        which can then be used to access Databricks Accounts and Workspace APIs. For more
        information, see [Authentication using OAuth tokens for service principals],
        
        In addition, the generated secrets can be used to configure the Databricks Terraform
        Provider to authenticate with the service principal. For more information, see [Databricks
        Terraform Provider].
        
        [Authentication using OAuth tokens for service principals]: https://docs.databricks.com/dev-tools/authentication-oauth.html
        [Databricks Terraform Provider]: https://github.com/databricks/terraform-provider-databricks/blob/master/docs/index.md#authenticating-with-service-principal"""

        self.service_principals: AccountServicePrincipalsAPI = AccountServicePrincipalsAPI(self.api_client)
        """Identities for use with jobs, automated tools, and systems such as scripts, apps, and CI/CD
        platforms. Databricks recommends creating service principals to run production jobs or
        modify production data. If all processes that act on production data run with service
        principals, interactive users do not need any write, delete, or modify privileges in
        production. This eliminates the risk of a user overwriting production data by accident."""

        self.settings: AccountSettingsAPI = AccountSettingsAPI(self.api_client)
        """The Personal Compute enablement setting lets you control which users can use the Personal
        Compute default policy to create compute resources. By default all users in all workspaces
        have access (ON), but you can change the setting to instead let individual workspaces
        configure access control (DELEGATE).
        
        There is only one instance of this setting per account. Since this setting has a default
        value, this setting is present on all accounts even though it's never set on a given
        account. Deletion reverts the value of the setting back to the default value."""

        self.storage: StorageAPI = StorageAPI(self.api_client)
        """These APIs manage storage configurations for this workspace. A root storage S3 bucket in
        your account is required to store objects like cluster logs, notebook revisions, and job
        results. You can also use the root storage S3 bucket for storage of non-production DBFS
        data. A storage configuration encapsulates this bucket information, and its ID is used when
        creating a new workspace."""

        self.storage_credentials: AccountStorageCredentialsAPI = AccountStorageCredentialsAPI(self.api_client)
        """These APIs manage storage credentials for a particular metastore."""

        self.users: AccountUsersAPI = AccountUsersAPI(self.api_client)
        """User identities recognized by Databricks and represented by email addresses.
        
        Databricks recommends using SCIM provisioning to sync users and groups automatically from
        your identity provider to your Databricks account. SCIM streamlines onboarding a new
        employee or team by using your identity provider to create users and groups in Databricks
        account and give them the proper level of access. When a user leaves your organization or no
        longer needs access to Databricks account, admins can terminate the user in your identity
        provider and that user’s account will also be removed from Databricks account. This
        ensures a consistent offboarding process and prevents unauthorized users from accessing
        sensitive data."""

        self.vpc_endpoints: VpcEndpointsAPI = VpcEndpointsAPI(self.api_client)
        """These APIs manage VPC endpoint configurations for this account."""

        self.workspace_assignment: WorkspaceAssignmentAPI = WorkspaceAssignmentAPI(self.api_client)
        """The Workspace Permission Assignment API allows you to manage workspace permissions for
        principals in your account."""

        self.workspaces: WorkspacesAPI = WorkspacesAPI(self.api_client)
        """These APIs manage workspaces for this account. A Databricks workspace is an environment for
        accessing all of your Databricks assets. The workspace organizes objects (notebooks,
        libraries, and experiments) into folders, and provides access to data and computational
        resources such as clusters and jobs.
        
        These endpoints are available if your account is on the E2 version of the platform or on a
        select custom plan that allows multiple workspaces per account."""
