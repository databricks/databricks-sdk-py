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
                                           OAuthEnrollmentAPI,
                                           OAuthPublishedAppsAPI,
                                           PublishedAppIntegrationAPI,
                                           ServicePrincipalSecretsAPI)
from databricks.sdk.service.pipelines import PipelinesAPI
from databricks.sdk.service.provisioning import (CredentialsAPI,
                                                 EncryptionKeysAPI,
                                                 NetworksAPI, PrivateAccessAPI,
                                                 StorageAPI, VpcEndpointsAPI,
                                                 WorkspacesAPI)
from databricks.sdk.service.serving import ServingEndpointsAPI
from databricks.sdk.service.settings import (AccountIpAccessListsAPI,
                                             AccountSettingsAPI,
                                             CredentialsManagerAPI,
                                             IpAccessListsAPI, SettingsAPI,
                                             TokenManagementAPI, TokensAPI,
                                             WorkspaceConfAPI)
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
                                   credentials_provider=credentials_provider,
                                   debug_truncate_bytes=debug_truncate_bytes,
                                   debug_headers=debug_headers,
                                   product=product,
                                   product_version=product_version)
        self.config = config.copy()
        self.dbutils = _make_dbutils(self.config)
        self.api_client = client.ApiClient(self.config)
        self.account_access_control_proxy = AccountAccessControlProxyAPI(self.api_client)
        self.alerts = AlertsAPI(self.api_client)
        self.artifact_allowlists = ArtifactAllowlistsAPI(self.api_client)
        self.catalogs = CatalogsAPI(self.api_client)
        self.clean_rooms = CleanRoomsAPI(self.api_client)
        self.cluster_policies = ClusterPoliciesAPI(self.api_client)
        self.clusters = ClustersExt(self.api_client)
        self.command_execution = CommandExecutionAPI(self.api_client)
        self.connections = ConnectionsAPI(self.api_client)
        self.credentials_manager = CredentialsManagerAPI(self.api_client)
        self.current_user = CurrentUserAPI(self.api_client)
        self.dashboard_widgets = DashboardWidgetsAPI(self.api_client)
        self.dashboards = DashboardsAPI(self.api_client)
        self.data_sources = DataSourcesAPI(self.api_client)
        self.dbfs = DbfsExt(self.api_client)
        self.dbsql_permissions = DbsqlPermissionsAPI(self.api_client)
        self.experiments = ExperimentsAPI(self.api_client)
        self.external_locations = ExternalLocationsAPI(self.api_client)
        self.files = FilesAPI(self.api_client)
        self.functions = FunctionsAPI(self.api_client)
        self.git_credentials = GitCredentialsAPI(self.api_client)
        self.global_init_scripts = GlobalInitScriptsAPI(self.api_client)
        self.grants = GrantsAPI(self.api_client)
        self.groups = GroupsAPI(self.api_client)
        self.instance_pools = InstancePoolsAPI(self.api_client)
        self.instance_profiles = InstanceProfilesAPI(self.api_client)
        self.ip_access_lists = IpAccessListsAPI(self.api_client)
        self.jobs = JobsAPI(self.api_client)
        self.libraries = LibrariesAPI(self.api_client)
        self.metastores = MetastoresAPI(self.api_client)
        self.model_registry = ModelRegistryAPI(self.api_client)
        self.model_versions = ModelVersionsAPI(self.api_client)
        self.permissions = PermissionsAPI(self.api_client)
        self.pipelines = PipelinesAPI(self.api_client)
        self.policy_families = PolicyFamiliesAPI(self.api_client)
        self.providers = ProvidersAPI(self.api_client)
        self.queries = QueriesAPI(self.api_client)
        self.query_history = QueryHistoryAPI(self.api_client)
        self.query_visualizations = QueryVisualizationsAPI(self.api_client)
        self.recipient_activation = RecipientActivationAPI(self.api_client)
        self.recipients = RecipientsAPI(self.api_client)
        self.registered_models = RegisteredModelsAPI(self.api_client)
        self.repos = ReposAPI(self.api_client)
        self.schemas = SchemasAPI(self.api_client)
        self.secrets = SecretsAPI(self.api_client)
        self.service_principals = ServicePrincipalsAPI(self.api_client)
        self.serving_endpoints = ServingEndpointsAPI(self.api_client)
        self.settings = SettingsAPI(self.api_client)
        self.shares = SharesAPI(self.api_client)
        self.statement_execution = StatementExecutionAPI(self.api_client)
        self.storage_credentials = StorageCredentialsAPI(self.api_client)
        self.system_schemas = SystemSchemasAPI(self.api_client)
        self.table_constraints = TableConstraintsAPI(self.api_client)
        self.tables = TablesAPI(self.api_client)
        self.token_management = TokenManagementAPI(self.api_client)
        self.tokens = TokensAPI(self.api_client)
        self.users = UsersAPI(self.api_client)
        self.volumes = VolumesAPI(self.api_client)
        self.warehouses = WarehousesAPI(self.api_client)
        self.workspace = WorkspaceExt(self.api_client)
        self.workspace_bindings = WorkspaceBindingsAPI(self.api_client)
        self.workspace_conf = WorkspaceConfAPI(self.api_client)


class AccountClient:

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
                                   credentials_provider=credentials_provider,
                                   debug_truncate_bytes=debug_truncate_bytes,
                                   debug_headers=debug_headers,
                                   product=product,
                                   product_version=product_version)
        self.config = config.copy()
        self.api_client = client.ApiClient(self.config)
        self.access_control = AccountAccessControlAPI(self.api_client)
        self.billable_usage = BillableUsageAPI(self.api_client)
        self.budgets = BudgetsAPI(self.api_client)
        self.credentials = CredentialsAPI(self.api_client)
        self.custom_app_integration = CustomAppIntegrationAPI(self.api_client)
        self.encryption_keys = EncryptionKeysAPI(self.api_client)
        self.groups = AccountGroupsAPI(self.api_client)
        self.ip_access_lists = AccountIpAccessListsAPI(self.api_client)
        self.log_delivery = LogDeliveryAPI(self.api_client)
        self.metastore_assignments = AccountMetastoreAssignmentsAPI(self.api_client)
        self.metastores = AccountMetastoresAPI(self.api_client)
        self.networks = NetworksAPI(self.api_client)
        self.o_auth_enrollment = OAuthEnrollmentAPI(self.api_client)
        self.o_auth_published_apps = OAuthPublishedAppsAPI(self.api_client)
        self.private_access = PrivateAccessAPI(self.api_client)
        self.published_app_integration = PublishedAppIntegrationAPI(self.api_client)
        self.service_principal_secrets = ServicePrincipalSecretsAPI(self.api_client)
        self.service_principals = AccountServicePrincipalsAPI(self.api_client)
        self.settings = AccountSettingsAPI(self.api_client)
        self.storage = StorageAPI(self.api_client)
        self.storage_credentials = AccountStorageCredentialsAPI(self.api_client)
        self.users = AccountUsersAPI(self.api_client)
        self.vpc_endpoints = VpcEndpointsAPI(self.api_client)
        self.workspace_assignment = WorkspaceAssignmentAPI(self.api_client)
        self.workspaces = WorkspacesAPI(self.api_client)
