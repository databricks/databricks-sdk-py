# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

import logging
from typing import Optional

import databricks.sdk.databricks.core as client
from databricks.sdk.databricks.credentials_provider import CredentialsStrategy

from .dashboards import (GenieAPI, LakeviewAPI, LakeviewEmbeddedAPI,
                         QueryExecutionAPI)

_LOG = logging.getLogger(__name__)


class GenieClient(GenieAPI):
    """
    Genie provides a no-code experience for business users, powered by AI/BI. Analysts set up spaces
    that business users can use to ask questions using natural language. Genie uses data registered
    to Unity Catalog and requires at least CAN USE permission on a Pro or Serverless SQL warehouse.
    Also, Databricks Assistant must be enabled.
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
            )
        self._config = config.copy()
        super().__init__(client.ApiClient(config))


class LakeviewClient(LakeviewAPI):
    """
    These APIs provide specific management operations for Lakeview dashboards. Generic resource
    management can be done with Workspace API (import, export, get-status, list, delete).
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
            )
        self._config = config.copy()
        super().__init__(client.ApiClient(config))


class LakeviewEmbeddedClient(LakeviewEmbeddedAPI):
    """
    Token-based Lakeview APIs for embedding dashboards in external applications.
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
            )
        self._config = config.copy()
        super().__init__(client.ApiClient(config))


class QueryExecutionClient(QueryExecutionAPI):
    """
    Query execution APIs for AI / BI Dashboards
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
            )
        self._config = config.copy()
        super().__init__(client.ApiClient(config))
