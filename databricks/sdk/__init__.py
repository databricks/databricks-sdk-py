# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

import logging
from typing import Optional

import databricks.sdk.core as client
import databricks.sdk.dbutils as dbutils
import databricks.sdk.service as service
from databricks.sdk import azure
from databricks.sdk.credentials_provider import CredentialsStrategy
from databricks.sdk.data_plane import DataPlaneTokenSource
from databricks.sdk.mixins.compute import ClustersExt
from databricks.sdk.mixins.files import DbfsExt, FilesExt
from databricks.sdk.mixins.jobs import JobsExt
from databricks.sdk.mixins.open_ai_client import ServingEndpointsExt
from databricks.sdk.mixins.workspace import WorkspaceExt
from databricks.sdk.service.apps import AppsAPI
from databricks.sdk.service.billing import (BillableUsageAPI, BudgetPolicyAPI,
                                            BudgetsAPI, LogDeliveryAPI,
                                            UsageDashboardsAPI)
from databricks.sdk.service.catalog import (AccountMetastoreAssignmentsAPI,
                                            AccountMetastoresAPI,
                                            AccountStorageCredentialsAPI,
                                            ArtifactAllowlistsAPI, CatalogsAPI,
                                            ConnectionsAPI, CredentialsAPI,
                                            ExternalLocationsAPI, FunctionsAPI,
                                            GrantsAPI, MetastoresAPI,
                                            ModelVersionsAPI, OnlineTablesAPI,
                                            QualityMonitorsAPI,
                                            RegisteredModelsAPI,
                                            ResourceQuotasAPI, SchemasAPI,
                                            StorageCredentialsAPI,
                                            SystemSchemasAPI,
                                            TableConstraintsAPI, TablesAPI,
                                            TemporaryTableCredentialsAPI,
                                            VolumesAPI, WorkspaceBindingsAPI)
from databricks.sdk.service.cleanrooms import (CleanRoomAssetsAPI,
                                               CleanRoomsAPI,
                                               CleanRoomTaskRunsAPI)
from databricks.sdk.service.compute import (ClusterPoliciesAPI, ClustersAPI,
                                            CommandExecutionAPI,
                                            GlobalInitScriptsAPI,
                                            InstancePoolsAPI,
                                            InstanceProfilesAPI, LibrariesAPI,
                                            PolicyComplianceForClustersAPI,
                                            PolicyFamiliesAPI)
from databricks.sdk.service.dashboards import (GenieAPI, LakeviewAPI,
                                               LakeviewEmbeddedAPI,
                                               QueryExecutionAPI)
from databricks.sdk.service.files import DbfsAPI, FilesAPI
from databricks.sdk.service.iam import (AccessControlAPI,
                                        AccountAccessControlAPI,
                                        AccountAccessControlProxyAPI,
                                        AccountGroupsAPI,
                                        AccountServicePrincipalsAPI,
                                        AccountUsersAPI, CurrentUserAPI,
                                        GroupsAPI, PermissionMigrationAPI,
                                        PermissionsAPI, ServicePrincipalsAPI,
                                        UsersAPI, WorkspaceAssignmentAPI)
from databricks.sdk.service.jobs import JobsAPI, PolicyComplianceForJobsAPI
from databricks.sdk.service.marketplace import (
    ConsumerFulfillmentsAPI, ConsumerInstallationsAPI, ConsumerListingsAPI,
    ConsumerPersonalizationRequestsAPI, ConsumerProvidersAPI,
    ProviderExchangeFiltersAPI, ProviderExchangesAPI, ProviderFilesAPI,
    ProviderListingsAPI, ProviderPersonalizationRequestsAPI,
    ProviderProviderAnalyticsDashboardsAPI, ProviderProvidersAPI)
from databricks.sdk.service.ml import (ExperimentsAPI, ForecastingAPI,
                                       ModelRegistryAPI)
from databricks.sdk.service.oauth2 import (AccountFederationPolicyAPI,
                                           CustomAppIntegrationAPI,
                                           OAuthPublishedAppsAPI,
                                           PublishedAppIntegrationAPI,
                                           ServicePrincipalFederationPolicyAPI,
                                           ServicePrincipalSecretsAPI)
from databricks.sdk.service.pipelines import PipelinesAPI
from databricks.sdk.service.provisioning import (CredentialsAPI,
                                                 EncryptionKeysAPI,
                                                 NetworksAPI, PrivateAccessAPI,
                                                 StorageAPI, VpcEndpointsAPI,
                                                 Workspace, WorkspacesAPI)
from databricks.sdk.service.serving import (ServingEndpointsAPI,
                                            ServingEndpointsDataPlaneAPI)
from databricks.sdk.service.settings import (
    AccountIpAccessListsAPI, AccountSettingsAPI,
    AibiDashboardEmbeddingAccessPolicyAPI,
    AibiDashboardEmbeddingApprovedDomainsAPI, AutomaticClusterUpdateAPI,
    ComplianceSecurityProfileAPI, CredentialsManagerAPI,
    CspEnablementAccountAPI, DefaultNamespaceAPI, DisableLegacyAccessAPI,
    DisableLegacyDbfsAPI, DisableLegacyFeaturesAPI, EnableExportNotebookAPI,
    EnableIpAccessListsAPI, EnableNotebookTableClipboardAPI,
    EnableResultsDownloadingAPI, EnhancedSecurityMonitoringAPI,
    EsmEnablementAccountAPI, IpAccessListsAPI, NetworkConnectivityAPI,
    NotificationDestinationsAPI, PersonalComputeAPI,
    RestrictWorkspaceAdminsAPI, SettingsAPI, TokenManagementAPI, TokensAPI,
    WorkspaceConfAPI)
from databricks.sdk.service.sharing import (ProvidersAPI,
                                            RecipientActivationAPI,
                                            RecipientsAPI, SharesAPI)
from databricks.sdk.service.sql import (AlertsAPI, AlertsLegacyAPI,
                                        AlertsV2API, DashboardsAPI,
                                        DashboardWidgetsAPI, DataSourcesAPI,
                                        DbsqlPermissionsAPI, QueriesAPI,
                                        QueriesLegacyAPI, QueryHistoryAPI,
                                        QueryVisualizationsAPI,
                                        QueryVisualizationsLegacyAPI,
                                        RedashConfigAPI, StatementExecutionAPI,
                                        WarehousesAPI)
from databricks.sdk.service.vectorsearch import (VectorSearchEndpointsAPI,
                                                 VectorSearchIndexesAPI)
from databricks.sdk.service.workspace import (GitCredentialsAPI, ReposAPI,
                                              SecretsAPI, WorkspaceAPI)

_LOG = logging.getLogger(__name__)


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


def _make_files_client(apiClient: client.ApiClient, config: client.Config):
    if config.enable_experimental_files_api_client:
        _LOG.info("Experimental Files API client is enabled")
        return FilesExt(apiClient, config)
    else:
        return FilesAPI(apiClient)


class WorkspaceClient:
    """
    The WorkspaceClient is a client for the workspace-level Databricks REST API.
    """

    def __init__(
        self,
        *,
        host: Optional[str] = None,
        account_id: Optional[str] = None,
        username: Optional[str] = None,
        password: Optional[str] = None,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        token: Optional[str] = None,
        profile: Optional[str] = None,
        config_file: Optional[str] = None,
        azure_workspace_resource_id: Optional[str] = None,
        azure_client_secret: Optional[str] = None,
        azure_client_id: Optional[str] = None,
        azure_tenant_id: Optional[str] = None,
        azure_environment: Optional[str] = None,
        auth_type: Optional[str] = None,
        cluster_id: Optional[str] = None,
        google_credentials: Optional[str] = None,
        google_service_account: Optional[str] = None,
        debug_truncate_bytes: Optional[int] = None,
        debug_headers: Optional[bool] = None,
        product="unknown",
        product_version="0.0.0",
        credentials_strategy: Optional[CredentialsStrategy] = None,
        credentials_provider: Optional[CredentialsStrategy] = None,
        token_audience: Optional[str] = None,
        config: Optional[client.Config] = None,
    ):
        if not config:
            config = client.Config(
                host=host,
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
                credentials_strategy=credentials_strategy,
                credentials_provider=credentials_provider,
                debug_truncate_bytes=debug_truncate_bytes,
                debug_headers=debug_headers,
                product=product,
                product_version=product_version,
                token_audience=token_audience,
            )
        self._config = config.copy()
        self._dbutils = _make_dbutils(self._config)
        self._api_client = client.ApiClient(self._config)
        serving_endpoints = ServingEndpointsExt(self._api_client)
        self._access_control = service.iam.AccessControlAPI(self._api_client)
        self._account_access_control_proxy = service.iam.AccountAccessControlProxyAPI(self._api_client)
        self._alerts = service.sql.AlertsAPI(self._api_client)
        self._alerts_legacy = service.sql.AlertsLegacyAPI(self._api_client)
        self._alerts_v2 = service.sql.AlertsV2API(self._api_client)
        self._apps = service.apps.AppsAPI(self._api_client)
        self._artifact_allowlists = service.catalog.ArtifactAllowlistsAPI(self._api_client)
        self._catalogs = service.catalog.CatalogsAPI(self._api_client)
        self._clean_room_assets = service.cleanrooms.CleanRoomAssetsAPI(self._api_client)
        self._clean_room_task_runs = service.cleanrooms.CleanRoomTaskRunsAPI(self._api_client)
        self._clean_rooms = service.cleanrooms.CleanRoomsAPI(self._api_client)
        self._cluster_policies = service.compute.ClusterPoliciesAPI(self._api_client)
        self._clusters = ClustersExt(self._api_client)
        self._command_execution = service.compute.CommandExecutionAPI(self._api_client)
        self._connections = service.catalog.ConnectionsAPI(self._api_client)
        self._consumer_fulfillments = service.marketplace.ConsumerFulfillmentsAPI(self._api_client)
        self._consumer_installations = service.marketplace.ConsumerInstallationsAPI(self._api_client)
        self._consumer_listings = service.marketplace.ConsumerListingsAPI(self._api_client)
        self._consumer_personalization_requests = service.marketplace.ConsumerPersonalizationRequestsAPI(
            self._api_client
        )
        self._consumer_providers = service.marketplace.ConsumerProvidersAPI(self._api_client)
        self._credentials = service.catalog.CredentialsAPI(self._api_client)
        self._credentials_manager = service.settings.CredentialsManagerAPI(self._api_client)
        self._current_user = service.iam.CurrentUserAPI(self._api_client)
        self._dashboard_widgets = service.sql.DashboardWidgetsAPI(self._api_client)
        self._dashboards = service.sql.DashboardsAPI(self._api_client)
        self._data_sources = service.sql.DataSourcesAPI(self._api_client)
        self._dbfs = DbfsExt(self._api_client)
        self._dbsql_permissions = service.sql.DbsqlPermissionsAPI(self._api_client)
        self._experiments = service.ml.ExperimentsAPI(self._api_client)
        self._external_locations = service.catalog.ExternalLocationsAPI(self._api_client)
        self._files = _make_files_client(self._api_client, self._config)
        self._functions = service.catalog.FunctionsAPI(self._api_client)
        self._genie = service.dashboards.GenieAPI(self._api_client)
        self._git_credentials = service.workspace.GitCredentialsAPI(self._api_client)
        self._global_init_scripts = service.compute.GlobalInitScriptsAPI(self._api_client)
        self._grants = service.catalog.GrantsAPI(self._api_client)
        self._groups = service.iam.GroupsAPI(self._api_client)
        self._instance_pools = service.compute.InstancePoolsAPI(self._api_client)
        self._instance_profiles = service.compute.InstanceProfilesAPI(self._api_client)
        self._ip_access_lists = service.settings.IpAccessListsAPI(self._api_client)
        self._jobs = JobsExt(self._api_client)
        self._lakeview = service.dashboards.LakeviewAPI(self._api_client)
        self._lakeview_embedded = service.dashboards.LakeviewEmbeddedAPI(self._api_client)
        self._libraries = service.compute.LibrariesAPI(self._api_client)
        self._metastores = service.catalog.MetastoresAPI(self._api_client)
        self._model_registry = service.ml.ModelRegistryAPI(self._api_client)
        self._model_versions = service.catalog.ModelVersionsAPI(self._api_client)
        self._notification_destinations = service.settings.NotificationDestinationsAPI(self._api_client)
        self._online_tables = service.catalog.OnlineTablesAPI(self._api_client)
        self._permission_migration = service.iam.PermissionMigrationAPI(self._api_client)
        self._permissions = service.iam.PermissionsAPI(self._api_client)
        self._pipelines = service.pipelines.PipelinesAPI(self._api_client)
        self._policy_compliance_for_clusters = service.compute.PolicyComplianceForClustersAPI(self._api_client)
        self._policy_compliance_for_jobs = service.jobs.PolicyComplianceForJobsAPI(self._api_client)
        self._policy_families = service.compute.PolicyFamiliesAPI(self._api_client)
        self._provider_exchange_filters = service.marketplace.ProviderExchangeFiltersAPI(self._api_client)
        self._provider_exchanges = service.marketplace.ProviderExchangesAPI(self._api_client)
        self._provider_files = service.marketplace.ProviderFilesAPI(self._api_client)
        self._provider_listings = service.marketplace.ProviderListingsAPI(self._api_client)
        self._provider_personalization_requests = service.marketplace.ProviderPersonalizationRequestsAPI(
            self._api_client
        )
        self._provider_provider_analytics_dashboards = service.marketplace.ProviderProviderAnalyticsDashboardsAPI(
            self._api_client
        )
        self._provider_providers = service.marketplace.ProviderProvidersAPI(self._api_client)
        self._providers = service.sharing.ProvidersAPI(self._api_client)
        self._quality_monitors = service.catalog.QualityMonitorsAPI(self._api_client)
        self._queries = service.sql.QueriesAPI(self._api_client)
        self._queries_legacy = service.sql.QueriesLegacyAPI(self._api_client)
        self._query_execution = service.dashboards.QueryExecutionAPI(self._api_client)
        self._query_history = service.sql.QueryHistoryAPI(self._api_client)
        self._query_visualizations = service.sql.QueryVisualizationsAPI(self._api_client)
        self._query_visualizations_legacy = service.sql.QueryVisualizationsLegacyAPI(self._api_client)
        self._recipient_activation = service.sharing.RecipientActivationAPI(self._api_client)
        self._recipients = service.sharing.RecipientsAPI(self._api_client)
        self._redash_config = service.sql.RedashConfigAPI(self._api_client)
        self._registered_models = service.catalog.RegisteredModelsAPI(self._api_client)
        self._repos = service.workspace.ReposAPI(self._api_client)
        self._resource_quotas = service.catalog.ResourceQuotasAPI(self._api_client)
        self._schemas = service.catalog.SchemasAPI(self._api_client)
        self._secrets = service.workspace.SecretsAPI(self._api_client)
        self._service_principals = service.iam.ServicePrincipalsAPI(self._api_client)
        self._serving_endpoints = serving_endpoints
        serving_endpoints_data_plane_token_source = DataPlaneTokenSource(
            self._config.host, self._config.oauth_token, self._config.disable_async_token_refresh
        )
        self._serving_endpoints_data_plane = service.serving.ServingEndpointsDataPlaneAPI(
            self._api_client, serving_endpoints, serving_endpoints_data_plane_token_source
        )
        self._settings = service.settings.SettingsAPI(self._api_client)
        self._shares = service.sharing.SharesAPI(self._api_client)
        self._statement_execution = service.sql.StatementExecutionAPI(self._api_client)
        self._storage_credentials = service.catalog.StorageCredentialsAPI(self._api_client)
        self._system_schemas = service.catalog.SystemSchemasAPI(self._api_client)
        self._table_constraints = service.catalog.TableConstraintsAPI(self._api_client)
        self._tables = service.catalog.TablesAPI(self._api_client)
        self._temporary_table_credentials = service.catalog.TemporaryTableCredentialsAPI(self._api_client)
        self._token_management = service.settings.TokenManagementAPI(self._api_client)
        self._tokens = service.settings.TokensAPI(self._api_client)
        self._users = service.iam.UsersAPI(self._api_client)
        self._vector_search_endpoints = service.vectorsearch.VectorSearchEndpointsAPI(self._api_client)
        self._vector_search_indexes = service.vectorsearch.VectorSearchIndexesAPI(self._api_client)
        self._volumes = service.catalog.VolumesAPI(self._api_client)
        self._warehouses = service.sql.WarehousesAPI(self._api_client)
        self._workspace = WorkspaceExt(self._api_client)
        self._workspace_bindings = service.catalog.WorkspaceBindingsAPI(self._api_client)
        self._workspace_conf = service.settings.WorkspaceConfAPI(self._api_client)
        self._forecasting = service.ml.ForecastingAPI(self._api_client)

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
    def access_control(self) -> service.iam.AccessControlAPI:
        """Rule based Access Control for Databricks Resources."""
        return self._access_control

    @property
    def account_access_control_proxy(self) -> service.iam.AccountAccessControlProxyAPI:
        """These APIs manage access rules on resources in an account."""
        return self._account_access_control_proxy

    @property
    def alerts(self) -> service.sql.AlertsAPI:
        """The alerts API can be used to perform CRUD operations on alerts."""
        return self._alerts

    @property
    def alerts_legacy(self) -> service.sql.AlertsLegacyAPI:
        """The alerts API can be used to perform CRUD operations on alerts."""
        return self._alerts_legacy

    @property
    def alerts_v2(self) -> service.sql.AlertsV2API:
        """TODO: Add description."""
        return self._alerts_v2

    @property
    def apps(self) -> service.apps.AppsAPI:
        """Apps run directly on a customer’s Databricks instance, integrate with their data, use and extend Databricks services, and enable users to interact through single sign-on."""
        return self._apps

    @property
    def artifact_allowlists(self) -> service.catalog.ArtifactAllowlistsAPI:
        """In Databricks Runtime 13.3 and above, you can add libraries and init scripts to the `allowlist` in UC so that users can leverage these artifacts on compute configured with shared access mode."""
        return self._artifact_allowlists

    @property
    def catalogs(self) -> service.catalog.CatalogsAPI:
        """A catalog is the first layer of Unity Catalog’s three-level namespace."""
        return self._catalogs

    @property
    def clean_room_assets(self) -> service.cleanrooms.CleanRoomAssetsAPI:
        """Clean room assets are data and code objects — Tables, volumes, and notebooks that are shared with the clean room."""
        return self._clean_room_assets

    @property
    def clean_room_task_runs(self) -> service.cleanrooms.CleanRoomTaskRunsAPI:
        """Clean room task runs are the executions of notebooks in a clean room."""
        return self._clean_room_task_runs

    @property
    def clean_rooms(self) -> service.cleanrooms.CleanRoomsAPI:
        """A clean room uses Delta Sharing and serverless compute to provide a secure and privacy-protecting environment where multiple parties can work together on sensitive enterprise data without direct access to each other’s data."""
        return self._clean_rooms

    @property
    def cluster_policies(self) -> service.compute.ClusterPoliciesAPI:
        """You can use cluster policies to control users' ability to configure clusters based on a set of rules."""
        return self._cluster_policies

    @property
    def clusters(self) -> ClustersExt:
        """The Clusters API allows you to create, start, edit, list, terminate, and delete clusters."""
        return self._clusters

    @property
    def command_execution(self) -> service.compute.CommandExecutionAPI:
        """This API allows execution of Python, Scala, SQL, or R commands on running Databricks Clusters."""
        return self._command_execution

    @property
    def connections(self) -> service.catalog.ConnectionsAPI:
        """Connections allow for creating a connection to an external data source."""
        return self._connections

    @property
    def consumer_fulfillments(self) -> service.marketplace.ConsumerFulfillmentsAPI:
        """Fulfillments are entities that allow consumers to preview installations."""
        return self._consumer_fulfillments

    @property
    def consumer_installations(self) -> service.marketplace.ConsumerInstallationsAPI:
        """Installations are entities that allow consumers to interact with Databricks Marketplace listings."""
        return self._consumer_installations

    @property
    def consumer_listings(self) -> service.marketplace.ConsumerListingsAPI:
        """Listings are the core entities in the Marketplace."""
        return self._consumer_listings

    @property
    def consumer_personalization_requests(self) -> service.marketplace.ConsumerPersonalizationRequestsAPI:
        """Personalization Requests allow customers to interact with the individualized Marketplace listing flow."""
        return self._consumer_personalization_requests

    @property
    def consumer_providers(self) -> service.marketplace.ConsumerProvidersAPI:
        """Providers are the entities that publish listings to the Marketplace."""
        return self._consumer_providers

    @property
    def credentials(self) -> service.catalog.CredentialsAPI:
        """A credential represents an authentication and authorization mechanism for accessing services on your cloud tenant."""
        return self._credentials

    @property
    def credentials_manager(self) -> service.settings.CredentialsManagerAPI:
        """Credentials manager interacts with with Identity Providers to to perform token exchanges using stored credentials and refresh tokens."""
        return self._credentials_manager

    @property
    def current_user(self) -> service.iam.CurrentUserAPI:
        """This API allows retrieving information about currently authenticated user or service principal."""
        return self._current_user

    @property
    def dashboard_widgets(self) -> service.sql.DashboardWidgetsAPI:
        """This is an evolving API that facilitates the addition and removal of widgets from existing dashboards within the Databricks Workspace."""
        return self._dashboard_widgets

    @property
    def dashboards(self) -> service.sql.DashboardsAPI:
        """In general, there is little need to modify dashboards using the API."""
        return self._dashboards

    @property
    def data_sources(self) -> service.sql.DataSourcesAPI:
        """This API is provided to assist you in making new query objects."""
        return self._data_sources

    @property
    def dbfs(self) -> DbfsExt:
        """DBFS API makes it simple to interact with various data sources without having to include a users credentials every time to read a file."""
        return self._dbfs

    @property
    def dbsql_permissions(self) -> service.sql.DbsqlPermissionsAPI:
        """The SQL Permissions API is similar to the endpoints of the :method:permissions/set."""
        return self._dbsql_permissions

    @property
    def experiments(self) -> service.ml.ExperimentsAPI:
        """Experiments are the primary unit of organization in MLflow; all MLflow runs belong to an experiment."""
        return self._experiments

    @property
    def external_locations(self) -> service.catalog.ExternalLocationsAPI:
        """An external location is an object that combines a cloud storage path with a storage credential that authorizes access to the cloud storage path."""
        return self._external_locations

    @property
    def files(self) -> service.files.FilesAPI:
        """The Files API is a standard HTTP API that allows you to read, write, list, and delete files and directories by referring to their URI."""
        return self._files

    @property
    def functions(self) -> service.catalog.FunctionsAPI:
        """Functions implement User-Defined Functions (UDFs) in Unity Catalog."""
        return self._functions

    @property
    def genie(self) -> service.dashboards.GenieAPI:
        """Genie provides a no-code experience for business users, powered by AI/BI."""
        return self._genie

    @property
    def git_credentials(self) -> service.workspace.GitCredentialsAPI:
        """Registers personal access token for Databricks to do operations on behalf of the user."""
        return self._git_credentials

    @property
    def global_init_scripts(self) -> service.compute.GlobalInitScriptsAPI:
        """The Global Init Scripts API enables Workspace administrators to configure global initialization scripts for their workspace."""
        return self._global_init_scripts

    @property
    def grants(self) -> service.catalog.GrantsAPI:
        """In Unity Catalog, data is secure by default."""
        return self._grants

    @property
    def groups(self) -> service.iam.GroupsAPI:
        """Groups simplify identity management, making it easier to assign access to Databricks workspace, data, and other securable objects."""
        return self._groups

    @property
    def instance_pools(self) -> service.compute.InstancePoolsAPI:
        """Instance Pools API are used to create, edit, delete and list instance pools by using ready-to-use cloud instances which reduces a cluster start and auto-scaling times."""
        return self._instance_pools

    @property
    def instance_profiles(self) -> service.compute.InstanceProfilesAPI:
        """The Instance Profiles API allows admins to add, list, and remove instance profiles that users can launch clusters with."""
        return self._instance_profiles

    @property
    def ip_access_lists(self) -> service.settings.IpAccessListsAPI:
        """IP Access List enables admins to configure IP access lists."""
        return self._ip_access_lists

    @property
    def jobs(self) -> JobsExt:
        """The Jobs API allows you to create, edit, and delete jobs."""
        return self._jobs

    @property
    def lakeview(self) -> service.dashboards.LakeviewAPI:
        """These APIs provide specific management operations for Lakeview dashboards."""
        return self._lakeview

    @property
    def lakeview_embedded(self) -> service.dashboards.LakeviewEmbeddedAPI:
        """Token-based Lakeview APIs for embedding dashboards in external applications."""
        return self._lakeview_embedded

    @property
    def libraries(self) -> service.compute.LibrariesAPI:
        """The Libraries API allows you to install and uninstall libraries and get the status of libraries on a cluster."""
        return self._libraries

    @property
    def metastores(self) -> service.catalog.MetastoresAPI:
        """A metastore is the top-level container of objects in Unity Catalog."""
        return self._metastores

    @property
    def model_registry(self) -> service.ml.ModelRegistryAPI:
        """Note: This API reference documents APIs for the Workspace Model Registry."""
        return self._model_registry

    @property
    def model_versions(self) -> service.catalog.ModelVersionsAPI:
        """Databricks provides a hosted version of MLflow Model Registry in Unity Catalog."""
        return self._model_versions

    @property
    def notification_destinations(self) -> service.settings.NotificationDestinationsAPI:
        """The notification destinations API lets you programmatically manage a workspace's notification destinations."""
        return self._notification_destinations

    @property
    def online_tables(self) -> service.catalog.OnlineTablesAPI:
        """Online tables provide lower latency and higher QPS access to data from Delta tables."""
        return self._online_tables

    @property
    def permission_migration(self) -> service.iam.PermissionMigrationAPI:
        """APIs for migrating acl permissions, used only by the ucx tool: https://github.com/databrickslabs/ucx."""
        return self._permission_migration

    @property
    def permissions(self) -> service.iam.PermissionsAPI:
        """Permissions API are used to create read, write, edit, update and manage access for various users on different objects and endpoints."""
        return self._permissions

    @property
    def pipelines(self) -> service.pipelines.PipelinesAPI:
        """The Delta Live Tables API allows you to create, edit, delete, start, and view details about pipelines."""
        return self._pipelines

    @property
    def policy_compliance_for_clusters(self) -> service.compute.PolicyComplianceForClustersAPI:
        """The policy compliance APIs allow you to view and manage the policy compliance status of clusters in your workspace."""
        return self._policy_compliance_for_clusters

    @property
    def policy_compliance_for_jobs(self) -> service.jobs.PolicyComplianceForJobsAPI:
        """The compliance APIs allow you to view and manage the policy compliance status of jobs in your workspace."""
        return self._policy_compliance_for_jobs

    @property
    def policy_families(self) -> service.compute.PolicyFamiliesAPI:
        """View available policy families."""
        return self._policy_families

    @property
    def provider_exchange_filters(self) -> service.marketplace.ProviderExchangeFiltersAPI:
        """Marketplace exchanges filters curate which groups can access an exchange."""
        return self._provider_exchange_filters

    @property
    def provider_exchanges(self) -> service.marketplace.ProviderExchangesAPI:
        """Marketplace exchanges allow providers to share their listings with a curated set of customers."""
        return self._provider_exchanges

    @property
    def provider_files(self) -> service.marketplace.ProviderFilesAPI:
        """Marketplace offers a set of file APIs for various purposes such as preview notebooks and provider icons."""
        return self._provider_files

    @property
    def provider_listings(self) -> service.marketplace.ProviderListingsAPI:
        """Listings are the core entities in the Marketplace."""
        return self._provider_listings

    @property
    def provider_personalization_requests(self) -> service.marketplace.ProviderPersonalizationRequestsAPI:
        """Personalization requests are an alternate to instantly available listings."""
        return self._provider_personalization_requests

    @property
    def provider_provider_analytics_dashboards(self) -> service.marketplace.ProviderProviderAnalyticsDashboardsAPI:
        """Manage templated analytics solution for providers."""
        return self._provider_provider_analytics_dashboards

    @property
    def provider_providers(self) -> service.marketplace.ProviderProvidersAPI:
        """Providers are entities that manage assets in Marketplace."""
        return self._provider_providers

    @property
    def providers(self) -> service.sharing.ProvidersAPI:
        """A data provider is an object representing the organization in the real world who shares the data."""
        return self._providers

    @property
    def quality_monitors(self) -> service.catalog.QualityMonitorsAPI:
        """A monitor computes and monitors data or model quality metrics for a table over time."""
        return self._quality_monitors

    @property
    def queries(self) -> service.sql.QueriesAPI:
        """The queries API can be used to perform CRUD operations on queries."""
        return self._queries

    @property
    def queries_legacy(self) -> service.sql.QueriesLegacyAPI:
        """These endpoints are used for CRUD operations on query definitions."""
        return self._queries_legacy

    @property
    def query_execution(self) -> service.dashboards.QueryExecutionAPI:
        """Query execution APIs for AI / BI Dashboards."""
        return self._query_execution

    @property
    def query_history(self) -> service.sql.QueryHistoryAPI:
        """A service responsible for storing and retrieving the list of queries run against SQL endpoints and serverless compute."""
        return self._query_history

    @property
    def query_visualizations(self) -> service.sql.QueryVisualizationsAPI:
        """This is an evolving API that facilitates the addition and removal of visualizations from existing queries in the Databricks Workspace."""
        return self._query_visualizations

    @property
    def query_visualizations_legacy(self) -> service.sql.QueryVisualizationsLegacyAPI:
        """This is an evolving API that facilitates the addition and removal of vizualisations from existing queries within the Databricks Workspace."""
        return self._query_visualizations_legacy

    @property
    def recipient_activation(self) -> service.sharing.RecipientActivationAPI:
        """The Recipient Activation API is only applicable in the open sharing model where the recipient object has the authentication type of `TOKEN`."""
        return self._recipient_activation

    @property
    def recipients(self) -> service.sharing.RecipientsAPI:
        """A recipient is an object you create using :method:recipients/create to represent an organization which you want to allow access shares."""
        return self._recipients

    @property
    def redash_config(self) -> service.sql.RedashConfigAPI:
        """Redash V2 service for workspace configurations (internal)."""
        return self._redash_config

    @property
    def registered_models(self) -> service.catalog.RegisteredModelsAPI:
        """Databricks provides a hosted version of MLflow Model Registry in Unity Catalog."""
        return self._registered_models

    @property
    def repos(self) -> service.workspace.ReposAPI:
        """The Repos API allows users to manage their git repos."""
        return self._repos

    @property
    def resource_quotas(self) -> service.catalog.ResourceQuotasAPI:
        """Unity Catalog enforces resource quotas on all securable objects, which limits the number of resources that can be created."""
        return self._resource_quotas

    @property
    def schemas(self) -> service.catalog.SchemasAPI:
        """A schema (also called a database) is the second layer of Unity Catalog’s three-level namespace."""
        return self._schemas

    @property
    def secrets(self) -> service.workspace.SecretsAPI:
        """The Secrets API allows you to manage secrets, secret scopes, and access permissions."""
        return self._secrets

    @property
    def service_principals(self) -> service.iam.ServicePrincipalsAPI:
        """Identities for use with jobs, automated tools, and systems such as scripts, apps, and CI/CD platforms."""
        return self._service_principals

    @property
    def serving_endpoints(self) -> ServingEndpointsExt:
        """The Serving Endpoints API allows you to create, update, and delete model serving endpoints."""
        return self._serving_endpoints

    @property
    def serving_endpoints_data_plane(self) -> service.serving.ServingEndpointsDataPlaneAPI:
        """Serving endpoints DataPlane provides a set of operations to interact with data plane endpoints for Serving endpoints service."""
        return self._serving_endpoints_data_plane

    @property
    def settings(self) -> service.settings.SettingsAPI:
        """Workspace Settings API allows users to manage settings at the workspace level."""
        return self._settings

    @property
    def shares(self) -> service.sharing.SharesAPI:
        """A share is a container instantiated with :method:shares/create."""
        return self._shares

    @property
    def statement_execution(self) -> service.sql.StatementExecutionAPI:
        """The Databricks SQL Statement Execution API can be used to execute SQL statements on a SQL warehouse and fetch the result."""
        return self._statement_execution

    @property
    def storage_credentials(self) -> service.catalog.StorageCredentialsAPI:
        """A storage credential represents an authentication and authorization mechanism for accessing data stored on your cloud tenant."""
        return self._storage_credentials

    @property
    def system_schemas(self) -> service.catalog.SystemSchemasAPI:
        """A system schema is a schema that lives within the system catalog."""
        return self._system_schemas

    @property
    def table_constraints(self) -> service.catalog.TableConstraintsAPI:
        """Primary key and foreign key constraints encode relationships between fields in tables."""
        return self._table_constraints

    @property
    def tables(self) -> service.catalog.TablesAPI:
        """A table resides in the third layer of Unity Catalog’s three-level namespace."""
        return self._tables

    @property
    def temporary_table_credentials(self) -> service.catalog.TemporaryTableCredentialsAPI:
        """Temporary Table Credentials refer to short-lived, downscoped credentials used to access cloud storage locationswhere table data is stored in Databricks."""
        return self._temporary_table_credentials

    @property
    def token_management(self) -> service.settings.TokenManagementAPI:
        """Enables administrators to get all tokens and delete tokens for other users."""
        return self._token_management

    @property
    def tokens(self) -> service.settings.TokensAPI:
        """The Token API allows you to create, list, and revoke tokens that can be used to authenticate and access Databricks REST APIs."""
        return self._tokens

    @property
    def users(self) -> service.iam.UsersAPI:
        """User identities recognized by Databricks and represented by email addresses."""
        return self._users

    @property
    def vector_search_endpoints(self) -> service.vectorsearch.VectorSearchEndpointsAPI:
        """**Endpoint**: Represents the compute resources to host vector search indexes."""
        return self._vector_search_endpoints

    @property
    def vector_search_indexes(self) -> service.vectorsearch.VectorSearchIndexesAPI:
        """**Index**: An efficient representation of your embedding vectors that supports real-time and efficient approximate nearest neighbor (ANN) search queries."""
        return self._vector_search_indexes

    @property
    def volumes(self) -> service.catalog.VolumesAPI:
        """Volumes are a Unity Catalog (UC) capability for accessing, storing, governing, organizing and processing files."""
        return self._volumes

    @property
    def warehouses(self) -> service.sql.WarehousesAPI:
        """A SQL warehouse is a compute resource that lets you run SQL commands on data objects within Databricks SQL."""
        return self._warehouses

    @property
    def workspace(self) -> WorkspaceExt:
        """The Workspace API allows you to list, import, export, and delete notebooks and folders."""
        return self._workspace

    @property
    def workspace_bindings(self) -> service.catalog.WorkspaceBindingsAPI:
        """A securable in Databricks can be configured as __OPEN__ or __ISOLATED__."""
        return self._workspace_bindings

    @property
    def workspace_conf(self) -> service.settings.WorkspaceConfAPI:
        """This API allows updating known workspace settings for advanced users."""
        return self._workspace_conf

    @property
    def forecasting(self) -> service.ml.ForecastingAPI:
        """The Forecasting API allows you to create and get serverless forecasting experiments."""
        return self._forecasting

    def get_workspace_id(self) -> int:
        """Get the workspace ID of the workspace that this client is connected to."""
        response = self._api_client.do("GET", "/api/2.0/preview/scim/v2/Me", response_headers=["X-Databricks-Org-Id"])
        return int(response["X-Databricks-Org-Id"])

    def __repr__(self):
        return f"WorkspaceClient(host='{self._config.host}', auth_type='{self._config.auth_type}', ...)"


class AccountClient:
    """
    The AccountClient is a client for the account-level Databricks REST API.
    """

    def __init__(
        self,
        *,
        host: Optional[str] = None,
        account_id: Optional[str] = None,
        username: Optional[str] = None,
        password: Optional[str] = None,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        token: Optional[str] = None,
        profile: Optional[str] = None,
        config_file: Optional[str] = None,
        azure_workspace_resource_id: Optional[str] = None,
        azure_client_secret: Optional[str] = None,
        azure_client_id: Optional[str] = None,
        azure_tenant_id: Optional[str] = None,
        azure_environment: Optional[str] = None,
        auth_type: Optional[str] = None,
        cluster_id: Optional[str] = None,
        google_credentials: Optional[str] = None,
        google_service_account: Optional[str] = None,
        debug_truncate_bytes: Optional[int] = None,
        debug_headers: Optional[bool] = None,
        product="unknown",
        product_version="0.0.0",
        credentials_strategy: Optional[CredentialsStrategy] = None,
        credentials_provider: Optional[CredentialsStrategy] = None,
        token_audience: Optional[str] = None,
        config: Optional[client.Config] = None,
    ):
        if not config:
            config = client.Config(
                host=host,
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
                credentials_strategy=credentials_strategy,
                credentials_provider=credentials_provider,
                debug_truncate_bytes=debug_truncate_bytes,
                debug_headers=debug_headers,
                product=product,
                product_version=product_version,
                token_audience=token_audience,
            )
        self._config = config.copy()
        self._api_client = client.ApiClient(self._config)
        self._access_control = service.iam.AccountAccessControlAPI(self._api_client)
        self._billable_usage = service.billing.BillableUsageAPI(self._api_client)
        self._budget_policy = service.billing.BudgetPolicyAPI(self._api_client)
        self._credentials = service.provisioning.CredentialsAPI(self._api_client)
        self._custom_app_integration = service.oauth2.CustomAppIntegrationAPI(self._api_client)
        self._encryption_keys = service.provisioning.EncryptionKeysAPI(self._api_client)
        self._federation_policy = service.oauth2.AccountFederationPolicyAPI(self._api_client)
        self._groups = service.iam.AccountGroupsAPI(self._api_client)
        self._ip_access_lists = service.settings.AccountIpAccessListsAPI(self._api_client)
        self._log_delivery = service.billing.LogDeliveryAPI(self._api_client)
        self._metastore_assignments = service.catalog.AccountMetastoreAssignmentsAPI(self._api_client)
        self._metastores = service.catalog.AccountMetastoresAPI(self._api_client)
        self._network_connectivity = service.settings.NetworkConnectivityAPI(self._api_client)
        self._networks = service.provisioning.NetworksAPI(self._api_client)
        self._o_auth_published_apps = service.oauth2.OAuthPublishedAppsAPI(self._api_client)
        self._private_access = service.provisioning.PrivateAccessAPI(self._api_client)
        self._published_app_integration = service.oauth2.PublishedAppIntegrationAPI(self._api_client)
        self._service_principal_federation_policy = service.oauth2.ServicePrincipalFederationPolicyAPI(self._api_client)
        self._service_principal_secrets = service.oauth2.ServicePrincipalSecretsAPI(self._api_client)
        self._service_principals = service.iam.AccountServicePrincipalsAPI(self._api_client)
        self._settings = service.settings.AccountSettingsAPI(self._api_client)
        self._storage = service.provisioning.StorageAPI(self._api_client)
        self._storage_credentials = service.catalog.AccountStorageCredentialsAPI(self._api_client)
        self._usage_dashboards = service.billing.UsageDashboardsAPI(self._api_client)
        self._users = service.iam.AccountUsersAPI(self._api_client)
        self._vpc_endpoints = service.provisioning.VpcEndpointsAPI(self._api_client)
        self._workspace_assignment = service.iam.WorkspaceAssignmentAPI(self._api_client)
        self._workspaces = service.provisioning.WorkspacesAPI(self._api_client)
        self._budgets = service.billing.BudgetsAPI(self._api_client)

    @property
    def config(self) -> client.Config:
        return self._config

    @property
    def api_client(self) -> client.ApiClient:
        return self._api_client

    @property
    def access_control(self) -> service.iam.AccountAccessControlAPI:
        """These APIs manage access rules on resources in an account."""
        return self._access_control

    @property
    def billable_usage(self) -> service.billing.BillableUsageAPI:
        """This API allows you to download billable usage logs for the specified account and date range."""
        return self._billable_usage

    @property
    def budget_policy(self) -> service.billing.BudgetPolicyAPI:
        """A service serves REST API about Budget policies."""
        return self._budget_policy

    @property
    def credentials(self) -> service.provisioning.CredentialsAPI:
        """These APIs manage credential configurations for this workspace."""
        return self._credentials

    @property
    def custom_app_integration(self) -> service.oauth2.CustomAppIntegrationAPI:
        """These APIs enable administrators to manage custom OAuth app integrations, which is required for adding/using Custom OAuth App Integration like Tableau Cloud for Databricks in AWS cloud."""
        return self._custom_app_integration

    @property
    def encryption_keys(self) -> service.provisioning.EncryptionKeysAPI:
        """These APIs manage encryption key configurations for this workspace (optional)."""
        return self._encryption_keys

    @property
    def federation_policy(self) -> service.oauth2.AccountFederationPolicyAPI:
        """These APIs manage account federation policies."""
        return self._federation_policy

    @property
    def groups(self) -> service.iam.AccountGroupsAPI:
        """Groups simplify identity management, making it easier to assign access to Databricks account, data, and other securable objects."""
        return self._groups

    @property
    def ip_access_lists(self) -> service.settings.AccountIpAccessListsAPI:
        """The Accounts IP Access List API enables account admins to configure IP access lists for access to the account console."""
        return self._ip_access_lists

    @property
    def log_delivery(self) -> service.billing.LogDeliveryAPI:
        """These APIs manage log delivery configurations for this account."""
        return self._log_delivery

    @property
    def metastore_assignments(self) -> service.catalog.AccountMetastoreAssignmentsAPI:
        """These APIs manage metastore assignments to a workspace."""
        return self._metastore_assignments

    @property
    def metastores(self) -> service.catalog.AccountMetastoresAPI:
        """These APIs manage Unity Catalog metastores for an account."""
        return self._metastores

    @property
    def network_connectivity(self) -> service.settings.NetworkConnectivityAPI:
        """These APIs provide configurations for the network connectivity of your workspaces for serverless compute resources."""
        return self._network_connectivity

    @property
    def networks(self) -> service.provisioning.NetworksAPI:
        """These APIs manage network configurations for customer-managed VPCs (optional)."""
        return self._networks

    @property
    def o_auth_published_apps(self) -> service.oauth2.OAuthPublishedAppsAPI:
        """These APIs enable administrators to view all the available published OAuth applications in Databricks."""
        return self._o_auth_published_apps

    @property
    def private_access(self) -> service.provisioning.PrivateAccessAPI:
        """These APIs manage private access settings for this account."""
        return self._private_access

    @property
    def published_app_integration(self) -> service.oauth2.PublishedAppIntegrationAPI:
        """These APIs enable administrators to manage published OAuth app integrations, which is required for adding/using Published OAuth App Integration like Tableau Desktop for Databricks in AWS cloud."""
        return self._published_app_integration

    @property
    def service_principal_federation_policy(self) -> service.oauth2.ServicePrincipalFederationPolicyAPI:
        """These APIs manage service principal federation policies."""
        return self._service_principal_federation_policy

    @property
    def service_principal_secrets(self) -> service.oauth2.ServicePrincipalSecretsAPI:
        """These APIs enable administrators to manage service principal secrets."""
        return self._service_principal_secrets

    @property
    def service_principals(self) -> service.iam.AccountServicePrincipalsAPI:
        """Identities for use with jobs, automated tools, and systems such as scripts, apps, and CI/CD platforms."""
        return self._service_principals

    @property
    def settings(self) -> service.settings.AccountSettingsAPI:
        """Accounts Settings API allows users to manage settings at the account level."""
        return self._settings

    @property
    def storage(self) -> service.provisioning.StorageAPI:
        """These APIs manage storage configurations for this workspace."""
        return self._storage

    @property
    def storage_credentials(self) -> service.catalog.AccountStorageCredentialsAPI:
        """These APIs manage storage credentials for a particular metastore."""
        return self._storage_credentials

    @property
    def usage_dashboards(self) -> service.billing.UsageDashboardsAPI:
        """These APIs manage usage dashboards for this account."""
        return self._usage_dashboards

    @property
    def users(self) -> service.iam.AccountUsersAPI:
        """User identities recognized by Databricks and represented by email addresses."""
        return self._users

    @property
    def vpc_endpoints(self) -> service.provisioning.VpcEndpointsAPI:
        """These APIs manage VPC endpoint configurations for this account."""
        return self._vpc_endpoints

    @property
    def workspace_assignment(self) -> service.iam.WorkspaceAssignmentAPI:
        """The Workspace Permission Assignment API allows you to manage workspace permissions for principals in your account."""
        return self._workspace_assignment

    @property
    def workspaces(self) -> service.provisioning.WorkspacesAPI:
        """These APIs manage workspaces for this account."""
        return self._workspaces

    @property
    def budgets(self) -> service.billing.BudgetsAPI:
        """These APIs manage budget configurations for this account."""
        return self._budgets

    def get_workspace_client(self, workspace: Workspace) -> WorkspaceClient:
        """Constructs a ``WorkspaceClient`` for the given workspace.

        Returns a ``WorkspaceClient`` that is configured to use the same
        credentials as this ``AccountClient``. The underlying config is
        copied from this ``AccountClient``, but the ``host`` and
        ``azure_workspace_resource_id`` are overridden to match the
        given workspace, and the ``account_id`` field is cleared.

        Usage:

        .. code-block::

            wss = list(a.workspaces.list())
            if len(wss) == 0:
                pytest.skip("no workspaces")
            w = a.get_workspace_client(wss[0])
            assert w.current_user.me().active

        :param workspace: The workspace to construct a client for.
        :return: A ``WorkspaceClient`` for the given workspace.
        """
        config = self._config.deep_copy()
        config.host = config.environment.deployment_url(workspace.deployment_name)
        config.azure_workspace_resource_id = azure.get_azure_resource_id(workspace)
        config.account_id = None
        config.init_auth()
        return WorkspaceClient(config=config)

    def __repr__(self):
        return f"AccountClient(account_id='{self._config.account_id}', auth_type='{self._config.auth_type}', ...)"
