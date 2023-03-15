import databricks.sdk.core as client
import databricks.sdk.mixins.compute as compute_mixin
import databricks.sdk.mixins.dbfs as dbfs_mixin
import databricks.sdk.service.billing as billing
import databricks.sdk.service.clusterpolicies as clusterpolicies
import databricks.sdk.service.clusters as clusters
import databricks.sdk.service.commands as commands
import databricks.sdk.service.dbfs as dbfs
import databricks.sdk.service.deployment as deployment
import databricks.sdk.service.endpoints as endpoints
import databricks.sdk.service.gitcredentials as gitcredentials
import databricks.sdk.service.globalinitscripts as globalinitscripts
import databricks.sdk.service.instancepools as instancepools
import databricks.sdk.service.ipaccesslists as ipaccesslists
import databricks.sdk.service.jobs as jobs
import databricks.sdk.service.libraries as libraries
import databricks.sdk.service.mlflow as mlflow
import databricks.sdk.service.oauth2 as oauth2
import databricks.sdk.service.permissions as permissions
import databricks.sdk.service.pipelines as pipelines
import databricks.sdk.service.repos as repos
import databricks.sdk.service.scim as scim
import databricks.sdk.service.secrets as secrets
import databricks.sdk.service.sql as sql
import databricks.sdk.service.tokenmanagement as tokenmanagement
import databricks.sdk.service.tokens as tokens
import databricks.sdk.service.unitycatalog as unitycatalog
import databricks.sdk.service.workspace as workspace
import databricks.sdk.service.workspaceconf as workspaceconf


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
                 **kwargs):
        self.config = client.Config(host=host,
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
                                    **kwargs)
        self.api_client = client.ApiClient(self.config)
        self.alerts = sql.AlertsAPI(self.api_client)
        self.catalogs = unitycatalog.CatalogsAPI(self.api_client)
        self.cluster_policies = clusterpolicies.ClusterPoliciesAPI(self.api_client)
        self.clusters = compute_mixin.ClustersExt(self.api_client)
        self.command_execution = commands.CommandExecutionAPI(self.api_client)
        self.current_user = scim.CurrentUserAPI(self.api_client)
        self.dashboards = sql.DashboardsAPI(self.api_client)
        self.data_sources = sql.DataSourcesAPI(self.api_client)
        self.dbfs = dbfs_mixin.DbfsExt(self.api_client)
        self.dbsql_permissions = sql.DbsqlPermissionsAPI(self.api_client)
        self.experiments = mlflow.ExperimentsAPI(self.api_client)
        self.external_locations = unitycatalog.ExternalLocationsAPI(self.api_client)
        self.functions = unitycatalog.FunctionsAPI(self.api_client)
        self.git_credentials = gitcredentials.GitCredentialsAPI(self.api_client)
        self.global_init_scripts = globalinitscripts.GlobalInitScriptsAPI(self.api_client)
        self.grants = unitycatalog.GrantsAPI(self.api_client)
        self.groups = scim.GroupsAPI(self.api_client)
        self.instance_pools = instancepools.InstancePoolsAPI(self.api_client)
        self.instance_profiles = clusters.InstanceProfilesAPI(self.api_client)
        self.ip_access_lists = ipaccesslists.IpAccessListsAPI(self.api_client)
        self.jobs = jobs.JobsAPI(self.api_client)
        self.libraries = libraries.LibrariesAPI(self.api_client)
        self.m_lflow_artifacts = mlflow.MLflowArtifactsAPI(self.api_client)
        self.m_lflow_databricks = mlflow.MLflowDatabricksAPI(self.api_client)
        self.m_lflow_metrics = mlflow.MLflowMetricsAPI(self.api_client)
        self.m_lflow_runs = mlflow.MLflowRunsAPI(self.api_client)
        self.metastores = unitycatalog.MetastoresAPI(self.api_client)
        self.model_version_comments = mlflow.ModelVersionCommentsAPI(self.api_client)
        self.model_versions = mlflow.ModelVersionsAPI(self.api_client)
        self.permissions = permissions.PermissionsAPI(self.api_client)
        self.pipelines = pipelines.PipelinesAPI(self.api_client)
        self.policy_families = clusterpolicies.PolicyFamiliesAPI(self.api_client)
        self.providers = unitycatalog.ProvidersAPI(self.api_client)
        self.queries = sql.QueriesAPI(self.api_client)
        self.query_history = sql.QueryHistoryAPI(self.api_client)
        self.recipient_activation = unitycatalog.RecipientActivationAPI(self.api_client)
        self.recipients = unitycatalog.RecipientsAPI(self.api_client)
        self.registered_models = mlflow.RegisteredModelsAPI(self.api_client)
        self.registry_webhooks = mlflow.RegistryWebhooksAPI(self.api_client)
        self.repos = repos.ReposAPI(self.api_client)
        self.schemas = unitycatalog.SchemasAPI(self.api_client)
        self.secrets = secrets.SecretsAPI(self.api_client)
        self.service_principals = scim.ServicePrincipalsAPI(self.api_client)
        self.serving_endpoints = endpoints.ServingEndpointsAPI(self.api_client)
        self.shares = unitycatalog.SharesAPI(self.api_client)
        self.statement_execution = sql.StatementExecutionAPI(self.api_client)
        self.storage_credentials = unitycatalog.StorageCredentialsAPI(self.api_client)
        self.table_constraints = unitycatalog.TableConstraintsAPI(self.api_client)
        self.tables = unitycatalog.TablesAPI(self.api_client)
        self.token_management = tokenmanagement.TokenManagementAPI(self.api_client)
        self.tokens = tokens.TokensAPI(self.api_client)
        self.transition_requests = mlflow.TransitionRequestsAPI(self.api_client)
        self.users = scim.UsersAPI(self.api_client)
        self.warehouses = sql.WarehousesAPI(self.api_client)
        self.workspace = workspace.WorkspaceAPI(self.api_client)
        self.workspace_conf = workspaceconf.WorkspaceConfAPI(self.api_client)


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
                 **kwargs):
        self.config = client.Config(host=host,
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
                                    **kwargs)
        self.api_client = client.ApiClient(self.config)
        self.billable_usage = billing.BillableUsageAPI(self.api_client)
        self.budgets = billing.BudgetsAPI(self.api_client)
        self.credentials = deployment.CredentialsAPI(self.api_client)
        self.custom_app_integration = oauth2.CustomAppIntegrationAPI(self.api_client)
        self.encryption_keys = deployment.EncryptionKeysAPI(self.api_client)
        self.account_groups = scim.AccountGroupsAPI(self.api_client)
        self.log_delivery = billing.LogDeliveryAPI(self.api_client)
        self.account_metastore_assignments = unitycatalog.AccountMetastoreAssignmentsAPI(self.api_client)
        self.account_metastores = unitycatalog.AccountMetastoresAPI(self.api_client)
        self.networks = deployment.NetworksAPI(self.api_client)
        self.o_auth_enrollment = oauth2.OAuthEnrollmentAPI(self.api_client)
        self.private_access = deployment.PrivateAccessAPI(self.api_client)
        self.published_app_integration = oauth2.PublishedAppIntegrationAPI(self.api_client)
        self.account_service_principals = scim.AccountServicePrincipalsAPI(self.api_client)
        self.storage = deployment.StorageAPI(self.api_client)
        self.account_storage_credentials = unitycatalog.AccountStorageCredentialsAPI(self.api_client)
        self.account_users = scim.AccountUsersAPI(self.api_client)
        self.vpc_endpoints = deployment.VpcEndpointsAPI(self.api_client)
        self.workspace_assignment = permissions.WorkspaceAssignmentAPI(self.api_client)
        self.workspaces = deployment.WorkspacesAPI(self.api_client)
