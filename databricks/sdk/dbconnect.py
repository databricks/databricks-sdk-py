# TODO: figure out how not to fail for clients without grpc not installed
import os

import grpc # TODO: check if it's duck-typed
from typing import (
    Iterable,
    Optional,
    Any,
    Union,
    List,
    Tuple,
    Dict,
    NoReturn,
    cast,
    Callable,
    Generator,
    Type,
)
from databricks.sdk.client import Config, ApiClient
from databricks.sdk.mixins import compute

# r.headers["Authorization"]

from dataclasses import dataclass

@dataclass
class Request:
    headers: 'Dict[str,str]'


class DatabricksChannelBuilder:
    def __init__(self, connectionString: str, config: Config = None, channelOptions: Optional[List[Tuple[str, Any]]] = None) -> None:
        if not config:
            config = Config()
        self._cfg = config

        # TODO: change interfaces
        # dummy = Request(headers={})
        self._cfg.load()
        self._connection_string = connectionString
        self._channel_options = channelOptions

        a = os.getenv("DATABRICKS_DEFAULT_CLUSTER_ID", None)
        b = os.getenv("SPARK_CONNECT_CLUSTER_ID", None)
        self._cluster_id = a or b
        if not self._cluster_id:
            # TODO: do we need it?..
            raise ValueError('No Databricks Cluster ID specified')

        api_client = ApiClient(self._cfg, product='databricks-connect', product_version='13.0.0')
        self._clusters_api = compute.ClustersExt(api_client)

    @property
    def userId(self) -> str:
        # TODO: or should it be SCIM Me?
        return os.getenv("USER", None)

    def metadata(self) -> Iterable[Tuple[str, str]]:
        """
        Builds the GRPC specific metadata list to be injected into the request. All
        parameters will be converted to metadata except ones that are explicitly used
        by the channel.

        Returns
        -------
        A list of tuples (key, value)
        """
        # TODO: implement the rest of the options
        self._clusters_api.ensure_cluster_is_running(self._cluster_id)
        return [
            ('x-databricks-cluster-id', self._cluster_id),
        ]

    def toChannel(self) -> grpc.Channel:
        from grpc import _plugin_wrapping  # pylint: disable=cyclic-import

        ssl_creds = grpc.ssl_channel_credentials()
        databricks_creds = _plugin_wrapping.metadata_plugin_call_credentials(
            DatabricksAuthMetadataPlugin(self._cfg), None)
        composite_creds = grpc.composite_channel_credentials(ssl_creds, databricks_creds)

        destination = f"{self._cfg.hostname}:443"

        return grpc.secure_channel(destination,
                                   credentials=composite_creds,
                                   options=self._channel_options)


class DatabricksAuthMetadataPlugin(grpc.AuthMetadataPlugin):
    def __init__(self, config: Config):
        self._auth = config.auth()

    def __call__(self, context: grpc.AuthMetadataContext,
                 callback: grpc.AuthMetadataPluginCallback):
        dummy = Request(headers={})
        try:
            self._auth(dummy)
            metadata = ()
            for k,v in dummy.headers.items():
                # gRPC requires headers to be lower-cased
                metadata += ((k.lower(), v),)
            callback(metadata, None)
        except Exception as e:
            callback((), e)