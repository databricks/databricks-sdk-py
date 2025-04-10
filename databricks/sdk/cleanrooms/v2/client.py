# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

import logging
from typing import Optional

import databricks.sdk.databricks.core as client
from databricks.sdk.databricks.credentials_provider import CredentialsStrategy

from .cleanrooms import CleanRoomAssetsAPI, CleanRoomsAPI, CleanRoomTaskRunsAPI

_LOG = logging.getLogger(__name__)


class CleanRoomAssetsClient(CleanRoomAssetsAPI):
    """
    Clean room assets are data and code objects — Tables, volumes, and notebooks that are shared
    with the clean room.
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


class CleanRoomTaskRunsClient(CleanRoomTaskRunsAPI):
    """
    Clean room task runs are the executions of notebooks in a clean room.
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


class CleanRoomsClient(CleanRoomsAPI):
    """
    A clean room uses Delta Sharing and serverless compute to provide a secure and
    privacy-protecting environment where multiple parties can work together on sensitive enterprise
    data without direct access to each other’s data.
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
