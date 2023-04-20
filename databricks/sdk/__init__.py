import databricks.sdk.core as client
import databricks.sdk.dbutils as dbutils
import databricks.sdk.mixins.compute as compute_mixin
import databricks.sdk.mixins.dbfs as dbfs_mixin
import databricks.sdk.service.billing as billing
import databricks.sdk.service.catalog as catalog
import databricks.sdk.service.compute as compute
import databricks.sdk.service.files as files
import databricks.sdk.service.iam as iam
import databricks.sdk.service.jobs as jobs
import databricks.sdk.service.ml as ml
import databricks.sdk.service.oauth2 as oauth2
import databricks.sdk.service.pipelines as pipelines
import databricks.sdk.service.provisioning as provisioning
import databricks.sdk.service.serving as serving
import databricks.sdk.service.settings as settings
import databricks.sdk.service.sharing as sharing
import databricks.sdk.service.sql as sql
import databricks.sdk.service.workspace as workspace


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
                 debug_headers: int = None,
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
        self.config = config
        self.dbutils = dbutils.RemoteDbUtils(self.config)
        self.api_client = client.ApiClient(self.config)
        self.alerts = sql.AlertsAPI(self.api_client)
        self.catalogs = catalog.CatalogsAPI(self.api_client)
        self.cluster_policies = compute.ClusterPoliciesAPI(self.api_client)
        self.clusters = compute_mixin.ClustersExt(self.api_client)
        self.command_execution = compute.CommandExecutionAPI(self.api_client)
        self.current_user = iam.CurrentUserAPI(self.api_client)
        self.dashboards = sql.DashboardsAPI(self.api_client)
        self.data_sources = sql.DataSourcesAPI(self.api_client)
        self.dbfs = dbfs_mixin.DbfsExt(self.api_client)
        self.dbsql_permissions = sql.DbsqlPermissionsAPI(self.api_client)
        self.experiments = ml.ExperimentsAPI(self.api_client)
        self.external_locations = catalog.ExternalLocationsAPI(self.api_client)
        self.functions = catalog.FunctionsAPI(self.api_client)
        self.git_credentials = workspace.GitCredentialsAPI(self.api_client)
        self.global_init_scripts = compute.GlobalInitScriptsAPI(self.api_client)
        self.grants = catalog.GrantsAPI(self.api_client)
        self.groups = iam.GroupsAPI(self.api_client)
        self.instance_pools = compute.InstancePoolsAPI(self.api_client)
        self.instance_profiles = compute.InstanceProfilesAPI(self.api_client)
        self.ip_access_lists = settings.IpAccessListsAPI(self.api_client)
        self.jobs = jobs.JobsAPI(self.api_client)
        self.libraries = compute.LibrariesAPI(self.api_client)
        self.metastores = catalog.MetastoresAPI(self.api_client)
        self.model_registry = ml.ModelRegistryAPI(self.api_client)
        self.permissions = iam.PermissionsAPI(self.api_client)
        self.pipelines = pipelines.PipelinesAPI(self.api_client)
        self.policy_families = compute.PolicyFamiliesAPI(self.api_client)
        self.providers = sharing.ProvidersAPI(self.api_client)
        self.queries = sql.QueriesAPI(self.api_client)
        self.query_history = sql.QueryHistoryAPI(self.api_client)
        self.recipient_activation = sharing.RecipientActivationAPI(self.api_client)
        self.recipients = sharing.RecipientsAPI(self.api_client)
        self.repos = workspace.ReposAPI(self.api_client)
        self.schemas = catalog.SchemasAPI(self.api_client)
        self.secrets = workspace.SecretsAPI(self.api_client)
        self.service_principals = iam.ServicePrincipalsAPI(self.api_client)
        self.serving_endpoints = serving.ServingEndpointsAPI(self.api_client)
        self.shares = sharing.SharesAPI(self.api_client)
        self.statement_execution = sql.StatementExecutionAPI(self.api_client)
        self.storage_credentials = catalog.StorageCredentialsAPI(self.api_client)
        self.table_constraints = catalog.TableConstraintsAPI(self.api_client)
        self.tables = catalog.TablesAPI(self.api_client)
        self.token_management = settings.TokenManagementAPI(self.api_client)
        self.tokens = settings.TokensAPI(self.api_client)
        self.users = iam.UsersAPI(self.api_client)
        self.volumes = catalog.VolumesAPI(self.api_client)
        self.warehouses = sql.WarehousesAPI(self.api_client)
        self.workspace = workspace.WorkspaceAPI(self.api_client)
        self.workspace_conf = settings.WorkspaceConfAPI(self.api_client)


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
                 debug_headers: int = None,
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
        self.config = config
        self.api_client = client.ApiClient(self.config)
        self.billable_usage = billing.BillableUsageAPI(self.api_client)
        self.budgets = billing.BudgetsAPI(self.api_client)
        self.credentials = provisioning.CredentialsAPI(self.api_client)
        self.custom_app_integration = oauth2.CustomAppIntegrationAPI(self.api_client)
        self.encryption_keys = provisioning.EncryptionKeysAPI(self.api_client)
        self.account_groups = iam.AccountGroupsAPI(self.api_client)
        self.account_ip_access_lists = settings.AccountIpAccessListsAPI(self.api_client)
        self.log_delivery = billing.LogDeliveryAPI(self.api_client)
        self.account_metastore_assignments = catalog.AccountMetastoreAssignmentsAPI(self.api_client)
        self.account_metastores = catalog.AccountMetastoresAPI(self.api_client)
        self.networks = provisioning.NetworksAPI(self.api_client)
        self.o_auth_enrollment = oauth2.OAuthEnrollmentAPI(self.api_client)
        self.private_access = provisioning.PrivateAccessAPI(self.api_client)
        self.published_app_integration = oauth2.PublishedAppIntegrationAPI(self.api_client)
        self.account_service_principals = iam.AccountServicePrincipalsAPI(self.api_client)
        self.storage = provisioning.StorageAPI(self.api_client)
        self.account_storage_credentials = catalog.AccountStorageCredentialsAPI(self.api_client)
        self.account_users = iam.AccountUsersAPI(self.api_client)
        self.vpc_endpoints = provisioning.VpcEndpointsAPI(self.api_client)
        self.workspace_assignment = iam.WorkspaceAssignmentAPI(self.api_client)
        self.workspaces = provisioning.WorkspacesAPI(self.api_client)
