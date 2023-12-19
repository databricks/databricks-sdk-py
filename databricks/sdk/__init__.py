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
        self._config = config.copy()
        self._dbutils = _make_dbutils(self._config)
        self._api_client = client.ApiClient(self._config)
        self._account_access_control_proxy = AccountAccessControlProxyAPI(self._api_client)
        self._alerts = AlertsAPI(self._api_client)
        self._apps = AppsAPI(self._api_client)
        self._artifact_allowlists = ArtifactAllowlistsAPI(self._api_client)
        self._catalogs = CatalogsAPI(self._api_client)
        self._clean_rooms = CleanRoomsAPI(self._api_client)
        self._cluster_policies = ClusterPoliciesAPI(self._api_client)
        self._clusters = ClustersExt(self._api_client)
        self._command_execution = CommandExecutionAPI(self._api_client)
        self._connections = ConnectionsAPI(self._api_client)
        self._credentials_manager = CredentialsManagerAPI(self._api_client)
        self._current_user = CurrentUserAPI(self._api_client)
        self._dashboard_widgets = DashboardWidgetsAPI(self._api_client)
        self._dashboards = DashboardsAPI(self._api_client)
        self._data_sources = DataSourcesAPI(self._api_client)
        self._dbfs = DbfsExt(self._api_client)
        self._dbsql_permissions = DbsqlPermissionsAPI(self._api_client)
        self._experiments = ExperimentsAPI(self._api_client)
        self._external_locations = ExternalLocationsAPI(self._api_client)
        self._files = FilesAPI(self._api_client)
        self._functions = FunctionsAPI(self._api_client)
        self._git_credentials = GitCredentialsAPI(self._api_client)
        self._global_init_scripts = GlobalInitScriptsAPI(self._api_client)
        self._grants = GrantsAPI(self._api_client)
        self._groups = GroupsAPI(self._api_client)
        self._instance_pools = InstancePoolsAPI(self._api_client)
        self._instance_profiles = InstanceProfilesAPI(self._api_client)
        self._ip_access_lists = IpAccessListsAPI(self._api_client)
        self._jobs = JobsAPI(self._api_client)
        self._libraries = LibrariesAPI(self._api_client)
        self._metastores = MetastoresAPI(self._api_client)
        self._model_registry = ModelRegistryAPI(self._api_client)
        self._model_versions = ModelVersionsAPI(self._api_client)
        self._permissions = PermissionsAPI(self._api_client)
        self._pipelines = PipelinesAPI(self._api_client)
        self._policy_families = PolicyFamiliesAPI(self._api_client)
        self._providers = ProvidersAPI(self._api_client)
        self._queries = QueriesAPI(self._api_client)
        self._query_history = QueryHistoryAPI(self._api_client)
        self._query_visualizations = QueryVisualizationsAPI(self._api_client)
        self._recipient_activation = RecipientActivationAPI(self._api_client)
        self._recipients = RecipientsAPI(self._api_client)
        self._registered_models = RegisteredModelsAPI(self._api_client)
        self._repos = ReposAPI(self._api_client)
        self._schemas = SchemasAPI(self._api_client)
        self._secrets = SecretsAPI(self._api_client)
        self._service_principals = ServicePrincipalsAPI(self._api_client)
        self._serving_endpoints = ServingEndpointsAPI(self._api_client)
        self._settings = SettingsAPI(self._api_client)
        self._shares = SharesAPI(self._api_client)
        self._statement_execution = StatementExecutionAPI(self._api_client)
        self._storage_credentials = StorageCredentialsAPI(self._api_client)
        self._system_schemas = SystemSchemasAPI(self._api_client)
        self._table_constraints = TableConstraintsAPI(self._api_client)
        self._tables = TablesAPI(self._api_client)
        self._token_management = TokenManagementAPI(self._api_client)
        self._tokens = TokensAPI(self._api_client)
        self._users = UsersAPI(self._api_client)
        self._volumes = VolumesAPI(self._api_client)
        self._warehouses = WarehousesAPI(self._api_client)
        self._workspace = WorkspaceExt(self._api_client)
        self._workspace_bindings = WorkspaceBindingsAPI(self._api_client)
        self._workspace_conf = WorkspaceConfAPI(self._api_client)

    @property
    def config(self) -> client.Config:
        return self._config

    @property
    def api_client(self) -> client.ApiClient:
        return self._api_client

    @property
    def dbutils(self) -> dbutils.RemoteDbUtils:
        return self._dbutils

    @property
    def account_access_control_proxy(self) -> AccountAccessControlProxyAPI:
        """These APIs manage access rules on resources in an account."""
        return self._account_access_control_proxy

    @property
    def alerts(self) -> AlertsAPI:
        """The alerts API can be used to perform CRUD operations on alerts."""
        return self._alerts

    @property
    def apps(self) -> AppsAPI:
        """Lakehouse Apps run directly on a customer’s Databricks instance, integrate with their data, use and extend Databricks services, and enable users to interact through single sign-on."""
        return self._apps

    @property
    def artifact_allowlists(self) -> ArtifactAllowlistsAPI:
        """In Databricks Runtime 13.3 and above, you can add libraries and init scripts to the `allowlist` in UC so that users can leverage these artifacts on compute configured with shared access mode."""
        return self._artifact_allowlists

    @property
    def catalogs(self) -> CatalogsAPI:
        """A catalog is the first layer of Unity Catalog’s three-level namespace."""
        return self._catalogs

    @property
    def clean_rooms(self) -> CleanRoomsAPI:
        """A clean room is a secure, privacy-protecting environment where two or more parties can share sensitive enterprise data, including customer data, for measurements, insights, activation and other use cases."""
        return self._clean_rooms

    @property
    def cluster_policies(self) -> ClusterPoliciesAPI:
        """You can use cluster policies to control users' ability to configure clusters based on a set of rules."""
        return self._cluster_policies

    @property
    def clusters(self) -> ClustersExt:
        """The Clusters API allows you to create, start, edit, list, terminate, and delete clusters."""
        return self._clusters

    @property
    def command_execution(self) -> CommandExecutionAPI:
        """This API allows execution of Python, Scala, SQL, or R commands on running Databricks Clusters."""
        return self._command_execution

    @property
    def connections(self) -> ConnectionsAPI:
        """Connections allow for creating a connection to an external data source."""
        return self._connections

    @property
    def credentials_manager(self) -> CredentialsManagerAPI:
        """Credentials manager interacts with with Identity Providers to to perform token exchanges using stored credentials and refresh tokens."""
        return self._credentials_manager

    @property
    def current_user(self) -> CurrentUserAPI:
        """This API allows retrieving information about currently authenticated user or service principal."""
        return self._current_user

    @property
    def dashboard_widgets(self) -> DashboardWidgetsAPI:
        """This is an evolving API that facilitates the addition and removal of widgets from existing dashboards within the Databricks Workspace."""
        return self._dashboard_widgets

    @property
    def dashboards(self) -> DashboardsAPI:
        """In general, there is little need to modify dashboards using the API."""
        return self._dashboards

    @property
    def data_sources(self) -> DataSourcesAPI:
        """This API is provided to assist you in making new query objects."""
        return self._data_sources

    @property
    def dbfs(self) -> DbfsExt:
        """DBFS API makes it simple to interact with various data sources without having to include a users credentials every time to read a file."""
        return self._dbfs

    @property
    def dbsql_permissions(self) -> DbsqlPermissionsAPI:
        """The SQL Permissions API is similar to the endpoints of the :method:permissions/set."""
        return self._dbsql_permissions

    @property
    def experiments(self) -> ExperimentsAPI:
        """Experiments are the primary unit of organization in MLflow; all MLflow runs belong to an experiment."""
        return self._experiments

    @property
    def external_locations(self) -> ExternalLocationsAPI:
        """An external location is an object that combines a cloud storage path with a storage credential that authorizes access to the cloud storage path."""
        return self._external_locations

    @property
    def files(self) -> FilesAPI:
        """The Files API allows you to read, write, and delete files and directories in Unity Catalog volumes."""
        return self._files

    @property
    def functions(self) -> FunctionsAPI:
        """Functions implement User-Defined Functions (UDFs) in Unity Catalog."""
        return self._functions

    @property
    def git_credentials(self) -> GitCredentialsAPI:
        """Registers personal access token for Databricks to do operations on behalf of the user."""
        return self._git_credentials

    @property
    def global_init_scripts(self) -> GlobalInitScriptsAPI:
        """The Global Init Scripts API enables Workspace administrators to configure global initialization scripts for their workspace."""
        return self._global_init_scripts

    @property
    def grants(self) -> GrantsAPI:
        """In Unity Catalog, data is secure by default."""
        return self._grants

    @property
    def groups(self) -> GroupsAPI:
        """Groups simplify identity management, making it easier to assign access to Databricks workspace, data, and other securable objects."""
        return self._groups

    @property
    def instance_pools(self) -> InstancePoolsAPI:
        """Instance Pools API are used to create, edit, delete and list instance pools by using ready-to-use cloud instances which reduces a cluster start and auto-scaling times."""
        return self._instance_pools

    @property
    def instance_profiles(self) -> InstanceProfilesAPI:
        """The Instance Profiles API allows admins to add, list, and remove instance profiles that users can launch clusters with."""
        return self._instance_profiles

    @property
    def ip_access_lists(self) -> IpAccessListsAPI:
        """IP Access List enables admins to configure IP access lists."""
        return self._ip_access_lists

    @property
    def jobs(self) -> JobsAPI:
        """The Jobs API allows you to create, edit, and delete jobs."""
        return self._jobs

    @property
    def libraries(self) -> LibrariesAPI:
        """The Libraries API allows you to install and uninstall libraries and get the status of libraries on a cluster."""
        return self._libraries

    @property
    def metastores(self) -> MetastoresAPI:
        """A metastore is the top-level container of objects in Unity Catalog."""
        return self._metastores

    @property
    def model_registry(self) -> ModelRegistryAPI:
        """Note: This API reference documents APIs for the Workspace Model Registry."""
        return self._model_registry

    @property
    def model_versions(self) -> ModelVersionsAPI:
        """Databricks provides a hosted version of MLflow Model Registry in Unity Catalog."""
        return self._model_versions

    @property
    def permissions(self) -> PermissionsAPI:
        """Permissions API are used to create read, write, edit, update and manage access for various users on different objects and endpoints."""
        return self._permissions

    @property
    def pipelines(self) -> PipelinesAPI:
        """The Delta Live Tables API allows you to create, edit, delete, start, and view details about pipelines."""
        return self._pipelines

    @property
    def policy_families(self) -> PolicyFamiliesAPI:
        """View available policy families."""
        return self._policy_families

    @property
    def providers(self) -> ProvidersAPI:
        """A data provider is an object representing the organization in the real world who shares the data."""
        return self._providers

    @property
    def queries(self) -> QueriesAPI:
        """These endpoints are used for CRUD operations on query definitions."""
        return self._queries

    @property
    def query_history(self) -> QueryHistoryAPI:
        """Access the history of queries through SQL warehouses."""
        return self._query_history

    @property
    def query_visualizations(self) -> QueryVisualizationsAPI:
        """This is an evolving API that facilitates the addition and removal of vizualisations from existing queries within the Databricks Workspace."""
        return self._query_visualizations

    @property
    def recipient_activation(self) -> RecipientActivationAPI:
        """The Recipient Activation API is only applicable in the open sharing model where the recipient object has the authentication type of `TOKEN`."""
        return self._recipient_activation

    @property
    def recipients(self) -> RecipientsAPI:
        """A recipient is an object you create using :method:recipients/create to represent an organization which you want to allow access shares."""
        return self._recipients

    @property
    def registered_models(self) -> RegisteredModelsAPI:
        """Databricks provides a hosted version of MLflow Model Registry in Unity Catalog."""
        return self._registered_models

    @property
    def repos(self) -> ReposAPI:
        """The Repos API allows users to manage their git repos."""
        return self._repos

    @property
    def schemas(self) -> SchemasAPI:
        """A schema (also called a database) is the second layer of Unity Catalog’s three-level namespace."""
        return self._schemas

    @property
    def secrets(self) -> SecretsAPI:
        """The Secrets API allows you to manage secrets, secret scopes, and access permissions."""
        return self._secrets

    @property
    def service_principals(self) -> ServicePrincipalsAPI:
        """Identities for use with jobs, automated tools, and systems such as scripts, apps, and CI/CD platforms."""
        return self._service_principals

    @property
    def serving_endpoints(self) -> ServingEndpointsAPI:
        """The Serving Endpoints API allows you to create, update, and delete model serving endpoints."""
        return self._serving_endpoints

    @property
    def settings(self) -> SettingsAPI:
        """The default namespace setting API allows users to configure the default namespace for a Databricks workspace."""
        return self._settings

    @property
    def shares(self) -> SharesAPI:
        """A share is a container instantiated with :method:shares/create."""
        return self._shares

    @property
    def statement_execution(self) -> StatementExecutionAPI:
        """The Databricks SQL Statement Execution API can be used to execute SQL statements on a SQL warehouse and fetch the result."""
        return self._statement_execution

    @property
    def storage_credentials(self) -> StorageCredentialsAPI:
        """A storage credential represents an authentication and authorization mechanism for accessing data stored on your cloud tenant."""
        return self._storage_credentials

    @property
    def system_schemas(self) -> SystemSchemasAPI:
        """A system schema is a schema that lives within the system catalog."""
        return self._system_schemas

    @property
    def table_constraints(self) -> TableConstraintsAPI:
        """Primary key and foreign key constraints encode relationships between fields in tables."""
        return self._table_constraints

    @property
    def tables(self) -> TablesAPI:
        """A table resides in the third layer of Unity Catalog’s three-level namespace."""
        return self._tables

    @property
    def token_management(self) -> TokenManagementAPI:
        """Enables administrators to get all tokens and delete tokens for other users."""
        return self._token_management

    @property
    def tokens(self) -> TokensAPI:
        """The Token API allows you to create, list, and revoke tokens that can be used to authenticate and access Databricks REST APIs."""
        return self._tokens

    @property
    def users(self) -> UsersAPI:
        """User identities recognized by Databricks and represented by email addresses."""
        return self._users

    @property
    def volumes(self) -> VolumesAPI:
        """Volumes are a Unity Catalog (UC) capability for accessing, storing, governing, organizing and processing files."""
        return self._volumes

    @property
    def warehouses(self) -> WarehousesAPI:
        """A SQL warehouse is a compute resource that lets you run SQL commands on data objects within Databricks SQL."""
        return self._warehouses

    @property
    def workspace(self) -> WorkspaceExt:
        """The Workspace API allows you to list, import, export, and delete notebooks and folders."""
        return self._workspace

    @property
    def workspace_bindings(self) -> WorkspaceBindingsAPI:
        """A securable in Databricks can be configured as __OPEN__ or __ISOLATED__."""
        return self._workspace_bindings

    @property
    def workspace_conf(self) -> WorkspaceConfAPI:
        """This API allows updating known workspace settings for advanced users."""
        return self._workspace_conf

    def __repr__(self):
        return f"WorkspaceClient(host='{self._config.host}', auth_type='{self._config.auth_type}', ...)"


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
        self._config = config.copy()
        self._api_client = client.ApiClient(self._config)
        self._access_control = AccountAccessControlAPI(self._api_client)
        self._billable_usage = BillableUsageAPI(self._api_client)
        self._budgets = BudgetsAPI(self._api_client)
        self._credentials = CredentialsAPI(self._api_client)
        self._custom_app_integration = CustomAppIntegrationAPI(self._api_client)
        self._encryption_keys = EncryptionKeysAPI(self._api_client)
        self._groups = AccountGroupsAPI(self._api_client)
        self._ip_access_lists = AccountIpAccessListsAPI(self._api_client)
        self._log_delivery = LogDeliveryAPI(self._api_client)
        self._metastore_assignments = AccountMetastoreAssignmentsAPI(self._api_client)
        self._metastores = AccountMetastoresAPI(self._api_client)
        self._network_connectivity = NetworkConnectivityAPI(self._api_client)
        self._networks = NetworksAPI(self._api_client)
        self._o_auth_published_apps = OAuthPublishedAppsAPI(self._api_client)
        self._private_access = PrivateAccessAPI(self._api_client)
        self._published_app_integration = PublishedAppIntegrationAPI(self._api_client)
        self._service_principal_secrets = ServicePrincipalSecretsAPI(self._api_client)
        self._service_principals = AccountServicePrincipalsAPI(self._api_client)
        self._settings = AccountSettingsAPI(self._api_client)
        self._storage = StorageAPI(self._api_client)
        self._storage_credentials = AccountStorageCredentialsAPI(self._api_client)
        self._users = AccountUsersAPI(self._api_client)
        self._vpc_endpoints = VpcEndpointsAPI(self._api_client)
        self._workspace_assignment = WorkspaceAssignmentAPI(self._api_client)
        self._workspaces = WorkspacesAPI(self._api_client)

    @property
    def config(self) -> client.Config:
        return self._config

    @property
    def api_client(self) -> client.ApiClient:
        return self._api_client

    @property
    def access_control(self) -> AccountAccessControlAPI:
        """These APIs manage access rules on resources in an account."""
        return self._access_control

    @property
    def billable_usage(self) -> BillableUsageAPI:
        """This API allows you to download billable usage logs for the specified account and date range."""
        return self._billable_usage

    @property
    def budgets(self) -> BudgetsAPI:
        """These APIs manage budget configuration including notifications for exceeding a budget for a period."""
        return self._budgets

    @property
    def credentials(self) -> CredentialsAPI:
        """These APIs manage credential configurations for this workspace."""
        return self._credentials

    @property
    def custom_app_integration(self) -> CustomAppIntegrationAPI:
        """These APIs enable administrators to manage custom oauth app integrations, which is required for adding/using Custom OAuth App Integration like Tableau Cloud for Databricks in AWS cloud."""
        return self._custom_app_integration

    @property
    def encryption_keys(self) -> EncryptionKeysAPI:
        """These APIs manage encryption key configurations for this workspace (optional)."""
        return self._encryption_keys

    @property
    def groups(self) -> AccountGroupsAPI:
        """Groups simplify identity management, making it easier to assign access to Databricks account, data, and other securable objects."""
        return self._groups

    @property
    def ip_access_lists(self) -> AccountIpAccessListsAPI:
        """The Accounts IP Access List API enables account admins to configure IP access lists for access to the account console."""
        return self._ip_access_lists

    @property
    def log_delivery(self) -> LogDeliveryAPI:
        """These APIs manage log delivery configurations for this account."""
        return self._log_delivery

    @property
    def metastore_assignments(self) -> AccountMetastoreAssignmentsAPI:
        """These APIs manage metastore assignments to a workspace."""
        return self._metastore_assignments

    @property
    def metastores(self) -> AccountMetastoresAPI:
        """These APIs manage Unity Catalog metastores for an account."""
        return self._metastores

    @property
    def network_connectivity(self) -> NetworkConnectivityAPI:
        """These APIs provide configurations for the network connectivity of your workspaces for serverless compute resources."""
        return self._network_connectivity

    @property
    def networks(self) -> NetworksAPI:
        """These APIs manage network configurations for customer-managed VPCs (optional)."""
        return self._networks

    @property
    def o_auth_published_apps(self) -> OAuthPublishedAppsAPI:
        """These APIs enable administrators to view all the available published OAuth applications in Databricks."""
        return self._o_auth_published_apps

    @property
    def private_access(self) -> PrivateAccessAPI:
        """These APIs manage private access settings for this account."""
        return self._private_access

    @property
    def published_app_integration(self) -> PublishedAppIntegrationAPI:
        """These APIs enable administrators to manage published oauth app integrations, which is required for adding/using Published OAuth App Integration like Tableau Desktop for Databricks in AWS cloud."""
        return self._published_app_integration

    @property
    def service_principal_secrets(self) -> ServicePrincipalSecretsAPI:
        """These APIs enable administrators to manage service principal secrets."""
        return self._service_principal_secrets

    @property
    def service_principals(self) -> AccountServicePrincipalsAPI:
        """Identities for use with jobs, automated tools, and systems such as scripts, apps, and CI/CD platforms."""
        return self._service_principals

    @property
    def settings(self) -> AccountSettingsAPI:
        """The Personal Compute enablement setting lets you control which users can use the Personal Compute default policy to create compute resources."""
        return self._settings

    @property
    def storage(self) -> StorageAPI:
        """These APIs manage storage configurations for this workspace."""
        return self._storage

    @property
    def storage_credentials(self) -> AccountStorageCredentialsAPI:
        """These APIs manage storage credentials for a particular metastore."""
        return self._storage_credentials

    @property
    def users(self) -> AccountUsersAPI:
        """User identities recognized by Databricks and represented by email addresses."""
        return self._users

    @property
    def vpc_endpoints(self) -> VpcEndpointsAPI:
        """These APIs manage VPC endpoint configurations for this account."""
        return self._vpc_endpoints

    @property
    def workspace_assignment(self) -> WorkspaceAssignmentAPI:
        """The Workspace Permission Assignment API allows you to manage workspace permissions for principals in your account."""
        return self._workspace_assignment

    @property
    def workspaces(self) -> WorkspacesAPI:
        """These APIs manage workspaces for this account."""
        return self._workspaces

    def __repr__(self):
        return f"AccountClient(account_id='{self._config.account_id}', auth_type='{self._config.auth_type}', ...)"
