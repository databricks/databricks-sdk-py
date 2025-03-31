# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

import logging
from typing import Optional

import databricks.sdk.databricks.core as client
import databricks.sdk.databricks.dbutils as dbutils
import databricks.sdk.service as service
from databricks.sdk.databricks import azure
from databricks.sdk.databricks.credentials_provider import CredentialsStrategy
from databricks.sdk.databricks.data_plane import DataPlaneTokenSource
from databricks.sdk.files.v2.mixin import DbfsExt, FilesExt
from databricks.sdk.files.v2.files import FilesAPI

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
    from databricks.sdk.databricks.runtime import dbutils as runtime_dbutils

    return runtime_dbutils


def _make_files_client(apiClient: client.ApiClient, config: client.Config):
    if config.enable_experimental_files_api_client:
        _LOG.info("Experimental Files API client is enabled")
        return FilesExt(apiClient, config)
    else:
        return FilesAPI(apiClient)
