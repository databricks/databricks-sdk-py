# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

from dataclasses import dataclass
from enum import Enum
from typing import Optional, Dict, List

__all__ = [
    
    'Channel',
    'ChannelName',
    'CreateWarehouseRequest',
    'CreateWarehouseRequestSpotInstancePolicy',
    'CreateWarehouseRequestWarehouseType',
    'CreateWarehouseResponse',
    'DeleteWarehouseRequest',
    'EditWarehouseRequest',
    'EditWarehouseRequestSpotInstancePolicy',
    'EditWarehouseRequestWarehouseType',
    'EndpointConfPair',
    'EndpointHealth',
    'EndpointHealthStatus',
    'EndpointInfo',
    'EndpointInfoSpotInstancePolicy',
    'EndpointInfoState',
    'EndpointInfoWarehouseType',
    'EndpointTagPair',
    'EndpointTags',
    'GetWarehouseRequest',
    'GetWarehouseResponse',
    'GetWarehouseResponseSpotInstancePolicy',
    'GetWarehouseResponseState',
    'GetWarehouseResponseWarehouseType',
    'GetWorkspaceWarehouseConfigResponse',
    'GetWorkspaceWarehouseConfigResponseSecurityPolicy',
    'ListWarehousesRequest',
    'ListWarehousesResponse',
    'OdbcParams',
    'RepeatedEndpointConfPairs',
    'SetWorkspaceWarehouseConfigRequest',
    'SetWorkspaceWarehouseConfigRequestSecurityPolicy',
    'StartWarehouseRequest',
    'StopWarehouseRequest',
    'TerminationReason',
    'TerminationReasonCode',
    'TerminationReasonType',
    'WarehouseTypePair',
    'WarehouseTypePairWarehouseType',
    
    'Warehouses',
]

# all definitions in this file are in alphabetical order

@dataclass
class Channel:
    
    
    dbsql_version: str = None
    
    name: 'ChannelName' = None

    def as_request(self) -> (dict, dict):
        channel_query, channel_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.dbsql_version:
            channel_body['dbsql_version'] = self.dbsql_version
        if self.name:
            channel_body['name'] = self.name.value
        
        return channel_query, channel_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Channel':
        return cls(
            dbsql_version=d.get('dbsql_version', None),
            name=ChannelName(d['name']) if 'name' in d else None,
        )



class ChannelName(Enum):
    
    
    CHANNEL_NAME_CURRENT = 'CHANNEL_NAME_CURRENT'
    CHANNEL_NAME_CUSTOM = 'CHANNEL_NAME_CUSTOM'
    CHANNEL_NAME_PREVIEW = 'CHANNEL_NAME_PREVIEW'
    CHANNEL_NAME_PREVIOUS = 'CHANNEL_NAME_PREVIOUS'
    CHANNEL_NAME_UNSPECIFIED = 'CHANNEL_NAME_UNSPECIFIED'

@dataclass
class CreateWarehouseRequest:
    
    # The amount of time in minutes that a SQL Endpoint must be idle (i.e., no
    # RUNNING queries) before it is automatically stopped.
    # 
    # Supported values: - Must be == 0 or >= 10 mins - 0 indicates no autostop.
    # 
    # Defaults to 120 mins
    auto_stop_mins: int = None
    # Channel Details
    channel: 'Channel' = None
    # Size of the clusters allocated for this endpoint. Increasing the size of a
    # spark cluster allows you to run larger queries on it. If you want to
    # increase the number of concurrent queries, please tune max_num_clusters.
    # 
    # Supported values: - 2X-Small - X-Small - Small - Medium - Large - X-Large
    # - 2X-Large - 3X-Large - 4X-Large
    cluster_size: str = None
    # endpoint creator name
    creator_name: str = None
    # Configures whether the endpoint should use Photon optimized clusters.
    # 
    # Defaults to false.
    enable_photon: bool = None
    # Configures whether the endpoint should use Serverless Compute (aka Nephos)
    # 
    # Defaults to value in global endpoint settings
    enable_serverless_compute: bool = None
    # Deprecated. Instance profile used to pass IAM role to the cluster
    instance_profile_arn: str = None
    # Maximum number of clusters that the autoscaler will create to handle
    # concurrent queries.
    # 
    # Supported values: - Must be >= min_num_clusters - Must be <= 30.
    # 
    # Defaults to min_clusters if unset.
    max_num_clusters: int = None
    # Minimum number of available clusters that will be maintained for this SQL
    # Endpoint. Increasing this will ensure that a larger number of clusters are
    # always running and therefore may reduce the cold start time for new
    # queries. This is similar to reserved vs. revocable cores in a resource
    # manager.
    # 
    # Supported values: - Must be > 0 - Must be <= min(max_num_clusters, 30)
    # 
    # Defaults to 1
    min_num_clusters: int = None
    # Logical name for the cluster.
    # 
    # Supported values: - Must be unique within an org. - Must be less than 100
    # characters.
    name: str = None
    # Configurations whether the endpoint should use spot instances.
    # 
    # Supported values: "COST_OPTIMIZED", "RELIABILITY_OPTIMIZED"
    # 
    # Defaults to COST_OPTIMIZED.
    # 
    # Please refer to documentation for EndpointSpotInstancePolicy for more
    # details.
    spot_instance_policy: 'CreateWarehouseRequestSpotInstancePolicy' = None
    # A set of key-value pairs that will be tagged on all resources (e.g., AWS
    # instances and EBS volumes) associated with this SQL Endpoints.
    # 
    # Supported values: - Number of tags < 45.
    tags: 'EndpointTags' = None
    # Warehouse type (Classic/Pro)
    warehouse_type: 'CreateWarehouseRequestWarehouseType' = None

    def as_request(self) -> (dict, dict):
        createWarehouseRequest_query, createWarehouseRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.auto_stop_mins:
            createWarehouseRequest_body['auto_stop_mins'] = self.auto_stop_mins
        if self.channel:
            createWarehouseRequest_body['channel'] = self.channel.as_request()[1]
        if self.cluster_size:
            createWarehouseRequest_body['cluster_size'] = self.cluster_size
        if self.creator_name:
            createWarehouseRequest_body['creator_name'] = self.creator_name
        if self.enable_photon:
            createWarehouseRequest_body['enable_photon'] = self.enable_photon
        if self.enable_serverless_compute:
            createWarehouseRequest_body['enable_serverless_compute'] = self.enable_serverless_compute
        if self.instance_profile_arn:
            createWarehouseRequest_body['instance_profile_arn'] = self.instance_profile_arn
        if self.max_num_clusters:
            createWarehouseRequest_body['max_num_clusters'] = self.max_num_clusters
        if self.min_num_clusters:
            createWarehouseRequest_body['min_num_clusters'] = self.min_num_clusters
        if self.name:
            createWarehouseRequest_body['name'] = self.name
        if self.spot_instance_policy:
            createWarehouseRequest_body['spot_instance_policy'] = self.spot_instance_policy.value
        if self.tags:
            createWarehouseRequest_body['tags'] = self.tags.as_request()[1]
        if self.warehouse_type:
            createWarehouseRequest_body['warehouse_type'] = self.warehouse_type.value
        
        return createWarehouseRequest_query, createWarehouseRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateWarehouseRequest':
        return cls(
            auto_stop_mins=d.get('auto_stop_mins', None),
            channel=Channel.from_dict(d['channel']) if 'channel' in d else None,
            cluster_size=d.get('cluster_size', None),
            creator_name=d.get('creator_name', None),
            enable_photon=d.get('enable_photon', None),
            enable_serverless_compute=d.get('enable_serverless_compute', None),
            instance_profile_arn=d.get('instance_profile_arn', None),
            max_num_clusters=d.get('max_num_clusters', None),
            min_num_clusters=d.get('min_num_clusters', None),
            name=d.get('name', None),
            spot_instance_policy=CreateWarehouseRequestSpotInstancePolicy(d['spot_instance_policy']) if 'spot_instance_policy' in d else None,
            tags=EndpointTags.from_dict(d['tags']) if 'tags' in d else None,
            warehouse_type=CreateWarehouseRequestWarehouseType(d['warehouse_type']) if 'warehouse_type' in d else None,
        )



class CreateWarehouseRequestSpotInstancePolicy(Enum):
    """Configurations whether the endpoint should use spot instances.
    
    Supported values: "COST_OPTIMIZED", "RELIABILITY_OPTIMIZED"
    
    Defaults to COST_OPTIMIZED.
    
    Please refer to documentation for EndpointSpotInstancePolicy for more
    details."""
    
    COST_OPTIMIZED = 'COST_OPTIMIZED'
    POLICY_UNSPECIFIED = 'POLICY_UNSPECIFIED'
    RELIABILITY_OPTIMIZED = 'RELIABILITY_OPTIMIZED'

class CreateWarehouseRequestWarehouseType(Enum):
    """Warehouse type (Classic/Pro)"""
    
    CLASSIC = 'CLASSIC'
    PRO = 'PRO'
    TYPE_UNSPECIFIED = 'TYPE_UNSPECIFIED'

@dataclass
class CreateWarehouseResponse:
    
    # Id for the SQL warehouse. This value is unique across all SQL warehouses.
    id: str = None

    def as_request(self) -> (dict, dict):
        createWarehouseResponse_query, createWarehouseResponse_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.id:
            createWarehouseResponse_body['id'] = self.id
        
        return createWarehouseResponse_query, createWarehouseResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateWarehouseResponse':
        return cls(
            id=d.get('id', None),
        )



@dataclass
class DeleteWarehouseRequest:
    
    # Required. Id of the SQL warehouse.
    id: str # path

    def as_request(self) -> (dict, dict):
        deleteWarehouseRequest_query, deleteWarehouseRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.id:
            deleteWarehouseRequest_body['id'] = self.id
        
        return deleteWarehouseRequest_query, deleteWarehouseRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'DeleteWarehouseRequest':
        return cls(
            id=d.get('id', None),
        )



@dataclass
class EditWarehouseRequest:
    
    # Required. Id of the warehouse to configure.
    id: str # path
    # The amount of time in minutes that a SQL Endpoint must be idle (i.e., no
    # RUNNING queries) before it is automatically stopped.
    # 
    # Supported values: - Must be == 0 or >= 10 mins - 0 indicates no autostop.
    # 
    # Defaults to 120 mins
    auto_stop_mins: int = None
    # Channel Details
    channel: 'Channel' = None
    # Size of the clusters allocated for this endpoint. Increasing the size of a
    # spark cluster allows you to run larger queries on it. If you want to
    # increase the number of concurrent queries, please tune max_num_clusters.
    # 
    # Supported values: - 2X-Small - X-Small - Small - Medium - Large - X-Large
    # - 2X-Large - 3X-Large - 4X-Large
    cluster_size: str = None
    # Needed for backwards compatibility. config.conf is json_inlined. We need
    # to keep confs here to make sure json calls with 'confs' explicitly
    # specified continue to work as is.
    confs: any /* MISSING TYPE */ = None
    # endpoint creator name
    creator_name: str = None
    # Configures whether the endpoint should use Databricks Compute (aka Nephos)
    # 
    # Deprecated: Use enable_serverless_compute TODO(SC-79930): Remove the field
    # once clients are updated
    enable_databricks_compute: bool = None
    # Configures whether the endpoint should use Photon optimized clusters.
    # 
    # Defaults to false.
    enable_photon: bool = None
    # Configures whether the endpoint should use Serverless Compute (aka Nephos)
    # 
    # Defaults to value in global endpoint settings
    enable_serverless_compute: bool = None
    # Deprecated. Instance profile used to pass IAM role to the cluster
    instance_profile_arn: str = None
    # Maximum number of clusters that the autoscaler will create to handle
    # concurrent queries.
    # 
    # Supported values: - Must be >= min_num_clusters - Must be <= 30.
    # 
    # Defaults to min_clusters if unset.
    max_num_clusters: int = None
    # Minimum number of available clusters that will be maintained for this SQL
    # Endpoint. Increasing this will ensure that a larger number of clusters are
    # always running and therefore may reduce the cold start time for new
    # queries. This is similar to reserved vs. revocable cores in a resource
    # manager.
    # 
    # Supported values: - Must be > 0 - Must be <= min(max_num_clusters, 30)
    # 
    # Defaults to 1
    min_num_clusters: int = None
    # Logical name for the cluster.
    # 
    # Supported values: - Must be unique within an org. - Must be less than 100
    # characters.
    name: str = None
    # Configurations whether the endpoint should use spot instances.
    # 
    # Supported values: "COST_OPTIMIZED", "RELIABILITY_OPTIMIZED"
    # 
    # Defaults to COST_OPTIMIZED.
    # 
    # Please refer to documentation for EndpointSpotInstancePolicy for more
    # details.
    spot_instance_policy: 'EditWarehouseRequestSpotInstancePolicy' = None
    # A set of key-value pairs that will be tagged on all resources (e.g., AWS
    # instances and EBS volumes) associated with this SQL Endpoints.
    # 
    # Supported values: - Number of tags < 45.
    tags: 'EndpointTags' = None
    # Warehouse type (Classic/Pro)
    warehouse_type: 'EditWarehouseRequestWarehouseType' = None

    def as_request(self) -> (dict, dict):
        editWarehouseRequest_query, editWarehouseRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.auto_stop_mins:
            editWarehouseRequest_body['auto_stop_mins'] = self.auto_stop_mins
        if self.channel:
            editWarehouseRequest_body['channel'] = self.channel.as_request()[1]
        if self.cluster_size:
            editWarehouseRequest_body['cluster_size'] = self.cluster_size
        if self.confs:
            editWarehouseRequest_body['confs'] = self.confs
        if self.creator_name:
            editWarehouseRequest_body['creator_name'] = self.creator_name
        if self.enable_databricks_compute:
            editWarehouseRequest_body['enable_databricks_compute'] = self.enable_databricks_compute
        if self.enable_photon:
            editWarehouseRequest_body['enable_photon'] = self.enable_photon
        if self.enable_serverless_compute:
            editWarehouseRequest_body['enable_serverless_compute'] = self.enable_serverless_compute
        if self.id:
            editWarehouseRequest_body['id'] = self.id
        if self.instance_profile_arn:
            editWarehouseRequest_body['instance_profile_arn'] = self.instance_profile_arn
        if self.max_num_clusters:
            editWarehouseRequest_body['max_num_clusters'] = self.max_num_clusters
        if self.min_num_clusters:
            editWarehouseRequest_body['min_num_clusters'] = self.min_num_clusters
        if self.name:
            editWarehouseRequest_body['name'] = self.name
        if self.spot_instance_policy:
            editWarehouseRequest_body['spot_instance_policy'] = self.spot_instance_policy.value
        if self.tags:
            editWarehouseRequest_body['tags'] = self.tags.as_request()[1]
        if self.warehouse_type:
            editWarehouseRequest_body['warehouse_type'] = self.warehouse_type.value
        
        return editWarehouseRequest_query, editWarehouseRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'EditWarehouseRequest':
        return cls(
            auto_stop_mins=d.get('auto_stop_mins', None),
            channel=Channel.from_dict(d['channel']) if 'channel' in d else None,
            cluster_size=d.get('cluster_size', None),
            confs=d.get('confs', None),
            creator_name=d.get('creator_name', None),
            enable_databricks_compute=d.get('enable_databricks_compute', None),
            enable_photon=d.get('enable_photon', None),
            enable_serverless_compute=d.get('enable_serverless_compute', None),
            id=d.get('id', None),
            instance_profile_arn=d.get('instance_profile_arn', None),
            max_num_clusters=d.get('max_num_clusters', None),
            min_num_clusters=d.get('min_num_clusters', None),
            name=d.get('name', None),
            spot_instance_policy=EditWarehouseRequestSpotInstancePolicy(d['spot_instance_policy']) if 'spot_instance_policy' in d else None,
            tags=EndpointTags.from_dict(d['tags']) if 'tags' in d else None,
            warehouse_type=EditWarehouseRequestWarehouseType(d['warehouse_type']) if 'warehouse_type' in d else None,
        )



class EditWarehouseRequestSpotInstancePolicy(Enum):
    """Configurations whether the endpoint should use spot instances.
    
    Supported values: "COST_OPTIMIZED", "RELIABILITY_OPTIMIZED"
    
    Defaults to COST_OPTIMIZED.
    
    Please refer to documentation for EndpointSpotInstancePolicy for more
    details."""
    
    COST_OPTIMIZED = 'COST_OPTIMIZED'
    POLICY_UNSPECIFIED = 'POLICY_UNSPECIFIED'
    RELIABILITY_OPTIMIZED = 'RELIABILITY_OPTIMIZED'

class EditWarehouseRequestWarehouseType(Enum):
    """Warehouse type (Classic/Pro)"""
    
    CLASSIC = 'CLASSIC'
    PRO = 'PRO'
    TYPE_UNSPECIFIED = 'TYPE_UNSPECIFIED'

@dataclass
class EndpointConfPair:
    
    
    key: str = None
    
    value: str = None

    def as_request(self) -> (dict, dict):
        endpointConfPair_query, endpointConfPair_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.key:
            endpointConfPair_body['key'] = self.key
        if self.value:
            endpointConfPair_body['value'] = self.value
        
        return endpointConfPair_query, endpointConfPair_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'EndpointConfPair':
        return cls(
            key=d.get('key', None),
            value=d.get('value', None),
        )



@dataclass
class EndpointHealth:
    
    # Details about errors that are causing current degraded/failed status.
    details: str = None
    # The reason for failure to bring up clusters for this endpoint. This is
    # available when status is 'FAILED' and sometimes when it is DEGRADED.
    failure_reason: 'TerminationReason' = None
    # Deprecated. split into summary and details for security
    message: str = None
    # Health status of the endpoint.
    status: 'EndpointHealthStatus' = None
    # A short summary of the health status in case of degraded/failed endpoints.
    summary: str = None

    def as_request(self) -> (dict, dict):
        endpointHealth_query, endpointHealth_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.details:
            endpointHealth_body['details'] = self.details
        if self.failure_reason:
            endpointHealth_body['failure_reason'] = self.failure_reason.as_request()[1]
        if self.message:
            endpointHealth_body['message'] = self.message
        if self.status:
            endpointHealth_body['status'] = self.status.value
        if self.summary:
            endpointHealth_body['summary'] = self.summary
        
        return endpointHealth_query, endpointHealth_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'EndpointHealth':
        return cls(
            details=d.get('details', None),
            failure_reason=TerminationReason.from_dict(d['failure_reason']) if 'failure_reason' in d else None,
            message=d.get('message', None),
            status=EndpointHealthStatus(d['status']) if 'status' in d else None,
            summary=d.get('summary', None),
        )



class EndpointHealthStatus(Enum):
    """Health status of the endpoint."""
    
    DEGRADED = 'DEGRADED'
    FAILED = 'FAILED'
    HEALTHY = 'HEALTHY'
    STATUS_UNSPECIFIED = 'STATUS_UNSPECIFIED'

@dataclass
class EndpointInfo:
    
    # The amount of time in minutes that a SQL Endpoint must be idle (i.e., no
    # RUNNING queries) before it is automatically stopped.
    # 
    # Supported values: - Must be == 0 or >= 10 mins - 0 indicates no autostop.
    # 
    # Defaults to 120 mins
    auto_stop_mins: int = None
    # Channel Details
    channel: 'Channel' = None
    # Size of the clusters allocated for this endpoint. Increasing the size of a
    # spark cluster allows you to run larger queries on it. If you want to
    # increase the number of concurrent queries, please tune max_num_clusters.
    # 
    # Supported values: - 2X-Small - X-Small - Small - Medium - Large - X-Large
    # - 2X-Large - 3X-Large - 4X-Large
    cluster_size: str = None
    # endpoint creator name
    creator_name: str = None
    # Configures whether the endpoint should use Databricks Compute (aka Nephos)
    # 
    # Deprecated: Use enable_serverless_compute TODO(SC-79930): Remove the field
    # once clients are updated
    enable_databricks_compute: bool = None
    # Configures whether the endpoint should use Photon optimized clusters.
    # 
    # Defaults to false.
    enable_photon: bool = None
    # Configures whether the endpoint should use Serverless Compute (aka Nephos)
    # 
    # Defaults to value in global endpoint settings
    enable_serverless_compute: bool = None
    # Optional health status. Assume the endpoint is healthy if this field is
    # not set.
    health: 'EndpointHealth' = None
    # unique identifier for endpoint
    id: str = None
    # Deprecated. Instance profile used to pass IAM role to the cluster
    instance_profile_arn: str = None
    # the jdbc connection string for this endpoint
    jdbc_url: str = None
    # Maximum number of clusters that the autoscaler will create to handle
    # concurrent queries.
    # 
    # Supported values: - Must be >= min_num_clusters - Must be <= 30.
    # 
    # Defaults to min_clusters if unset.
    max_num_clusters: int = None
    # Minimum number of available clusters that will be maintained for this SQL
    # Endpoint. Increasing this will ensure that a larger number of clusters are
    # always running and therefore may reduce the cold start time for new
    # queries. This is similar to reserved vs. revocable cores in a resource
    # manager.
    # 
    # Supported values: - Must be > 0 - Must be <= min(max_num_clusters, 30)
    # 
    # Defaults to 1
    min_num_clusters: int = None
    # Logical name for the cluster.
    # 
    # Supported values: - Must be unique within an org. - Must be less than 100
    # characters.
    name: str = None
    # current number of active sessions for the endpoint
    num_active_sessions: int = None
    # current number of clusters running for the service
    num_clusters: int = None
    # ODBC parameters for the sql endpoint
    odbc_params: 'OdbcParams' = None
    # Configurations whether the endpoint should use spot instances.
    # 
    # Supported values: "COST_OPTIMIZED", "RELIABILITY_OPTIMIZED"
    # 
    # Defaults to COST_OPTIMIZED.
    # 
    # Please refer to documentation for EndpointSpotInstancePolicy for more
    # details.
    spot_instance_policy: 'EndpointInfoSpotInstancePolicy' = None
    # state of the endpoint
    state: 'EndpointInfoState' = None
    # A set of key-value pairs that will be tagged on all resources (e.g., AWS
    # instances and EBS volumes) associated with this SQL Endpoints.
    # 
    # Supported values: - Number of tags < 45.
    tags: 'EndpointTags' = None
    # Warehouse type (Classic/Pro)
    warehouse_type: 'EndpointInfoWarehouseType' = None

    def as_request(self) -> (dict, dict):
        endpointInfo_query, endpointInfo_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.auto_stop_mins:
            endpointInfo_body['auto_stop_mins'] = self.auto_stop_mins
        if self.channel:
            endpointInfo_body['channel'] = self.channel.as_request()[1]
        if self.cluster_size:
            endpointInfo_body['cluster_size'] = self.cluster_size
        if self.creator_name:
            endpointInfo_body['creator_name'] = self.creator_name
        if self.enable_databricks_compute:
            endpointInfo_body['enable_databricks_compute'] = self.enable_databricks_compute
        if self.enable_photon:
            endpointInfo_body['enable_photon'] = self.enable_photon
        if self.enable_serverless_compute:
            endpointInfo_body['enable_serverless_compute'] = self.enable_serverless_compute
        if self.health:
            endpointInfo_body['health'] = self.health.as_request()[1]
        if self.id:
            endpointInfo_body['id'] = self.id
        if self.instance_profile_arn:
            endpointInfo_body['instance_profile_arn'] = self.instance_profile_arn
        if self.jdbc_url:
            endpointInfo_body['jdbc_url'] = self.jdbc_url
        if self.max_num_clusters:
            endpointInfo_body['max_num_clusters'] = self.max_num_clusters
        if self.min_num_clusters:
            endpointInfo_body['min_num_clusters'] = self.min_num_clusters
        if self.name:
            endpointInfo_body['name'] = self.name
        if self.num_active_sessions:
            endpointInfo_body['num_active_sessions'] = self.num_active_sessions
        if self.num_clusters:
            endpointInfo_body['num_clusters'] = self.num_clusters
        if self.odbc_params:
            endpointInfo_body['odbc_params'] = self.odbc_params.as_request()[1]
        if self.spot_instance_policy:
            endpointInfo_body['spot_instance_policy'] = self.spot_instance_policy.value
        if self.state:
            endpointInfo_body['state'] = self.state.value
        if self.tags:
            endpointInfo_body['tags'] = self.tags.as_request()[1]
        if self.warehouse_type:
            endpointInfo_body['warehouse_type'] = self.warehouse_type.value
        
        return endpointInfo_query, endpointInfo_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'EndpointInfo':
        return cls(
            auto_stop_mins=d.get('auto_stop_mins', None),
            channel=Channel.from_dict(d['channel']) if 'channel' in d else None,
            cluster_size=d.get('cluster_size', None),
            creator_name=d.get('creator_name', None),
            enable_databricks_compute=d.get('enable_databricks_compute', None),
            enable_photon=d.get('enable_photon', None),
            enable_serverless_compute=d.get('enable_serverless_compute', None),
            health=EndpointHealth.from_dict(d['health']) if 'health' in d else None,
            id=d.get('id', None),
            instance_profile_arn=d.get('instance_profile_arn', None),
            jdbc_url=d.get('jdbc_url', None),
            max_num_clusters=d.get('max_num_clusters', None),
            min_num_clusters=d.get('min_num_clusters', None),
            name=d.get('name', None),
            num_active_sessions=d.get('num_active_sessions', None),
            num_clusters=d.get('num_clusters', None),
            odbc_params=OdbcParams.from_dict(d['odbc_params']) if 'odbc_params' in d else None,
            spot_instance_policy=EndpointInfoSpotInstancePolicy(d['spot_instance_policy']) if 'spot_instance_policy' in d else None,
            state=EndpointInfoState(d['state']) if 'state' in d else None,
            tags=EndpointTags.from_dict(d['tags']) if 'tags' in d else None,
            warehouse_type=EndpointInfoWarehouseType(d['warehouse_type']) if 'warehouse_type' in d else None,
        )



class EndpointInfoSpotInstancePolicy(Enum):
    """Configurations whether the endpoint should use spot instances.
    
    Supported values: "COST_OPTIMIZED", "RELIABILITY_OPTIMIZED"
    
    Defaults to COST_OPTIMIZED.
    
    Please refer to documentation for EndpointSpotInstancePolicy for more
    details."""
    
    COST_OPTIMIZED = 'COST_OPTIMIZED'
    POLICY_UNSPECIFIED = 'POLICY_UNSPECIFIED'
    RELIABILITY_OPTIMIZED = 'RELIABILITY_OPTIMIZED'

class EndpointInfoState(Enum):
    """state of the endpoint"""
    
    DELETED = 'DELETED'
    DELETING = 'DELETING'
    RUNNING = 'RUNNING'
    STARTING = 'STARTING'
    STOPPED = 'STOPPED'
    STOPPING = 'STOPPING'

class EndpointInfoWarehouseType(Enum):
    """Warehouse type (Classic/Pro)"""
    
    CLASSIC = 'CLASSIC'
    PRO = 'PRO'
    TYPE_UNSPECIFIED = 'TYPE_UNSPECIFIED'

@dataclass
class EndpointTagPair:
    
    
    key: str = None
    
    value: str = None

    def as_request(self) -> (dict, dict):
        endpointTagPair_query, endpointTagPair_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.key:
            endpointTagPair_body['key'] = self.key
        if self.value:
            endpointTagPair_body['value'] = self.value
        
        return endpointTagPair_query, endpointTagPair_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'EndpointTagPair':
        return cls(
            key=d.get('key', None),
            value=d.get('value', None),
        )



@dataclass
class EndpointTags:
    
    
    custom_tags: 'List[EndpointTagPair]' = None

    def as_request(self) -> (dict, dict):
        endpointTags_query, endpointTags_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.custom_tags:
            endpointTags_body['custom_tags'] = [v.as_request()[1] for v in self.custom_tags]
        
        return endpointTags_query, endpointTags_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'EndpointTags':
        return cls(
            custom_tags=[EndpointTagPair.from_dict(v) for v in d['custom_tags']] if 'custom_tags' in d else None,
        )



@dataclass
class GetWarehouseRequest:
    
    # Required. Id of the SQL warehouse.
    id: str # path

    def as_request(self) -> (dict, dict):
        getWarehouseRequest_query, getWarehouseRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.id:
            getWarehouseRequest_body['id'] = self.id
        
        return getWarehouseRequest_query, getWarehouseRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetWarehouseRequest':
        return cls(
            id=d.get('id', None),
        )



@dataclass
class GetWarehouseResponse:
    
    # The amount of time in minutes that a SQL Endpoint must be idle (i.e., no
    # RUNNING queries) before it is automatically stopped.
    # 
    # Supported values: - Must be == 0 or >= 10 mins - 0 indicates no autostop.
    # 
    # Defaults to 120 mins
    auto_stop_mins: int = None
    # Channel Details
    channel: 'Channel' = None
    # Size of the clusters allocated for this endpoint. Increasing the size of a
    # spark cluster allows you to run larger queries on it. If you want to
    # increase the number of concurrent queries, please tune max_num_clusters.
    # 
    # Supported values: - 2X-Small - X-Small - Small - Medium - Large - X-Large
    # - 2X-Large - 3X-Large - 4X-Large
    cluster_size: str = None
    # endpoint creator name
    creator_name: str = None
    # Configures whether the endpoint should use Databricks Compute (aka Nephos)
    # 
    # Deprecated: Use enable_serverless_compute TODO(SC-79930): Remove the field
    # once clients are updated
    enable_databricks_compute: bool = None
    # Configures whether the endpoint should use Photon optimized clusters.
    # 
    # Defaults to false.
    enable_photon: bool = None
    # Configures whether the endpoint should use Serverless Compute (aka Nephos)
    # 
    # Defaults to value in global endpoint settings
    enable_serverless_compute: bool = None
    # Optional health status. Assume the endpoint is healthy if this field is
    # not set.
    health: 'EndpointHealth' = None
    # unique identifier for endpoint
    id: str = None
    # Deprecated. Instance profile used to pass IAM role to the cluster
    instance_profile_arn: str = None
    # the jdbc connection string for this endpoint
    jdbc_url: str = None
    # Maximum number of clusters that the autoscaler will create to handle
    # concurrent queries.
    # 
    # Supported values: - Must be >= min_num_clusters - Must be <= 30.
    # 
    # Defaults to min_clusters if unset.
    max_num_clusters: int = None
    # Minimum number of available clusters that will be maintained for this SQL
    # Endpoint. Increasing this will ensure that a larger number of clusters are
    # always running and therefore may reduce the cold start time for new
    # queries. This is similar to reserved vs. revocable cores in a resource
    # manager.
    # 
    # Supported values: - Must be > 0 - Must be <= min(max_num_clusters, 30)
    # 
    # Defaults to 1
    min_num_clusters: int = None
    # Logical name for the cluster.
    # 
    # Supported values: - Must be unique within an org. - Must be less than 100
    # characters.
    name: str = None
    # current number of active sessions for the endpoint
    num_active_sessions: int = None
    # current number of clusters running for the service
    num_clusters: int = None
    # ODBC parameters for the sql endpoint
    odbc_params: 'OdbcParams' = None
    # Configurations whether the endpoint should use spot instances.
    # 
    # Supported values: "COST_OPTIMIZED", "RELIABILITY_OPTIMIZED"
    # 
    # Defaults to COST_OPTIMIZED.
    # 
    # Please refer to documentation for EndpointSpotInstancePolicy for more
    # details.
    spot_instance_policy: 'GetWarehouseResponseSpotInstancePolicy' = None
    # state of the endpoint
    state: 'GetWarehouseResponseState' = None
    # A set of key-value pairs that will be tagged on all resources (e.g., AWS
    # instances and EBS volumes) associated with this SQL Endpoints.
    # 
    # Supported values: - Number of tags < 45.
    tags: 'EndpointTags' = None
    # Warehouse type (Classic/Pro)
    warehouse_type: 'GetWarehouseResponseWarehouseType' = None

    def as_request(self) -> (dict, dict):
        getWarehouseResponse_query, getWarehouseResponse_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.auto_stop_mins:
            getWarehouseResponse_body['auto_stop_mins'] = self.auto_stop_mins
        if self.channel:
            getWarehouseResponse_body['channel'] = self.channel.as_request()[1]
        if self.cluster_size:
            getWarehouseResponse_body['cluster_size'] = self.cluster_size
        if self.creator_name:
            getWarehouseResponse_body['creator_name'] = self.creator_name
        if self.enable_databricks_compute:
            getWarehouseResponse_body['enable_databricks_compute'] = self.enable_databricks_compute
        if self.enable_photon:
            getWarehouseResponse_body['enable_photon'] = self.enable_photon
        if self.enable_serverless_compute:
            getWarehouseResponse_body['enable_serverless_compute'] = self.enable_serverless_compute
        if self.health:
            getWarehouseResponse_body['health'] = self.health.as_request()[1]
        if self.id:
            getWarehouseResponse_body['id'] = self.id
        if self.instance_profile_arn:
            getWarehouseResponse_body['instance_profile_arn'] = self.instance_profile_arn
        if self.jdbc_url:
            getWarehouseResponse_body['jdbc_url'] = self.jdbc_url
        if self.max_num_clusters:
            getWarehouseResponse_body['max_num_clusters'] = self.max_num_clusters
        if self.min_num_clusters:
            getWarehouseResponse_body['min_num_clusters'] = self.min_num_clusters
        if self.name:
            getWarehouseResponse_body['name'] = self.name
        if self.num_active_sessions:
            getWarehouseResponse_body['num_active_sessions'] = self.num_active_sessions
        if self.num_clusters:
            getWarehouseResponse_body['num_clusters'] = self.num_clusters
        if self.odbc_params:
            getWarehouseResponse_body['odbc_params'] = self.odbc_params.as_request()[1]
        if self.spot_instance_policy:
            getWarehouseResponse_body['spot_instance_policy'] = self.spot_instance_policy.value
        if self.state:
            getWarehouseResponse_body['state'] = self.state.value
        if self.tags:
            getWarehouseResponse_body['tags'] = self.tags.as_request()[1]
        if self.warehouse_type:
            getWarehouseResponse_body['warehouse_type'] = self.warehouse_type.value
        
        return getWarehouseResponse_query, getWarehouseResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetWarehouseResponse':
        return cls(
            auto_stop_mins=d.get('auto_stop_mins', None),
            channel=Channel.from_dict(d['channel']) if 'channel' in d else None,
            cluster_size=d.get('cluster_size', None),
            creator_name=d.get('creator_name', None),
            enable_databricks_compute=d.get('enable_databricks_compute', None),
            enable_photon=d.get('enable_photon', None),
            enable_serverless_compute=d.get('enable_serverless_compute', None),
            health=EndpointHealth.from_dict(d['health']) if 'health' in d else None,
            id=d.get('id', None),
            instance_profile_arn=d.get('instance_profile_arn', None),
            jdbc_url=d.get('jdbc_url', None),
            max_num_clusters=d.get('max_num_clusters', None),
            min_num_clusters=d.get('min_num_clusters', None),
            name=d.get('name', None),
            num_active_sessions=d.get('num_active_sessions', None),
            num_clusters=d.get('num_clusters', None),
            odbc_params=OdbcParams.from_dict(d['odbc_params']) if 'odbc_params' in d else None,
            spot_instance_policy=GetWarehouseResponseSpotInstancePolicy(d['spot_instance_policy']) if 'spot_instance_policy' in d else None,
            state=GetWarehouseResponseState(d['state']) if 'state' in d else None,
            tags=EndpointTags.from_dict(d['tags']) if 'tags' in d else None,
            warehouse_type=GetWarehouseResponseWarehouseType(d['warehouse_type']) if 'warehouse_type' in d else None,
        )



class GetWarehouseResponseSpotInstancePolicy(Enum):
    """Configurations whether the endpoint should use spot instances.
    
    Supported values: "COST_OPTIMIZED", "RELIABILITY_OPTIMIZED"
    
    Defaults to COST_OPTIMIZED.
    
    Please refer to documentation for EndpointSpotInstancePolicy for more
    details."""
    
    COST_OPTIMIZED = 'COST_OPTIMIZED'
    POLICY_UNSPECIFIED = 'POLICY_UNSPECIFIED'
    RELIABILITY_OPTIMIZED = 'RELIABILITY_OPTIMIZED'

class GetWarehouseResponseState(Enum):
    """state of the endpoint"""
    
    DELETED = 'DELETED'
    DELETING = 'DELETING'
    RUNNING = 'RUNNING'
    STARTING = 'STARTING'
    STOPPED = 'STOPPED'
    STOPPING = 'STOPPING'

class GetWarehouseResponseWarehouseType(Enum):
    """Warehouse type (Classic/Pro)"""
    
    CLASSIC = 'CLASSIC'
    PRO = 'PRO'
    TYPE_UNSPECIFIED = 'TYPE_UNSPECIFIED'

@dataclass
class GetWorkspaceWarehouseConfigResponse:
    
    # Optional: Channel selection details
    channel: 'Channel' = None
    # Deprecated: Use sql_configuration_parameters
    config_param: 'RepeatedEndpointConfPairs' = None
    # Spark confs for external hive metastore configuration JSON serialized size
    # must be less than <= 512K
    data_access_config: 'List[EndpointConfPair]' = None
    # Enable Serverless compute for SQL Endpoints
    # 
    # Deprecated: Use enable_serverless_compute TODO(SC-79930): Remove the field
    # once clients are updated
    enable_databricks_compute: bool = None
    # Enable Serverless compute for SQL Endpoints
    enable_serverless_compute: bool = None
    # List of Warehouse Types allowed in this workspace (limits allowed value of
    # the type field in CreateWarehouse and EditWarehouse). Note: Some types
    # cannot be disabled, they don't need to be specified in
    # SetWorkspaceWarehouseConfig. Note: Disabling a type may cause existing
    # warehouses to be converted to another type. Used by frontend to save
    # specific type availability in the warehouse create and edit form UI.
    enabled_warehouse_types: 'List[WarehouseTypePair]' = None
    # Deprecated: Use sql_configuration_parameters
    global_param: 'RepeatedEndpointConfPairs' = None
    # GCP only: Google Service Account used to pass to cluster to access Google
    # Cloud Storage
    google_service_account: str = None
    # AWS Only: Instance profile used to pass IAM role to the cluster
    instance_profile_arn: str = None
    # Security policy for endpoints
    security_policy: 'GetWorkspaceWarehouseConfigResponseSecurityPolicy' = None
    # SQL configuration parameters
    sql_configuration_parameters: 'RepeatedEndpointConfPairs' = None

    def as_request(self) -> (dict, dict):
        getWorkspaceWarehouseConfigResponse_query, getWorkspaceWarehouseConfigResponse_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.channel:
            getWorkspaceWarehouseConfigResponse_body['channel'] = self.channel.as_request()[1]
        if self.config_param:
            getWorkspaceWarehouseConfigResponse_body['config_param'] = self.config_param.as_request()[1]
        if self.data_access_config:
            getWorkspaceWarehouseConfigResponse_body['data_access_config'] = [v.as_request()[1] for v in self.data_access_config]
        if self.enable_databricks_compute:
            getWorkspaceWarehouseConfigResponse_body['enable_databricks_compute'] = self.enable_databricks_compute
        if self.enable_serverless_compute:
            getWorkspaceWarehouseConfigResponse_body['enable_serverless_compute'] = self.enable_serverless_compute
        if self.enabled_warehouse_types:
            getWorkspaceWarehouseConfigResponse_body['enabled_warehouse_types'] = [v.as_request()[1] for v in self.enabled_warehouse_types]
        if self.global_param:
            getWorkspaceWarehouseConfigResponse_body['global_param'] = self.global_param.as_request()[1]
        if self.google_service_account:
            getWorkspaceWarehouseConfigResponse_body['google_service_account'] = self.google_service_account
        if self.instance_profile_arn:
            getWorkspaceWarehouseConfigResponse_body['instance_profile_arn'] = self.instance_profile_arn
        if self.security_policy:
            getWorkspaceWarehouseConfigResponse_body['security_policy'] = self.security_policy.value
        if self.sql_configuration_parameters:
            getWorkspaceWarehouseConfigResponse_body['sql_configuration_parameters'] = self.sql_configuration_parameters.as_request()[1]
        
        return getWorkspaceWarehouseConfigResponse_query, getWorkspaceWarehouseConfigResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetWorkspaceWarehouseConfigResponse':
        return cls(
            channel=Channel.from_dict(d['channel']) if 'channel' in d else None,
            config_param=RepeatedEndpointConfPairs.from_dict(d['config_param']) if 'config_param' in d else None,
            data_access_config=[EndpointConfPair.from_dict(v) for v in d['data_access_config']] if 'data_access_config' in d else None,
            enable_databricks_compute=d.get('enable_databricks_compute', None),
            enable_serverless_compute=d.get('enable_serverless_compute', None),
            enabled_warehouse_types=[WarehouseTypePair.from_dict(v) for v in d['enabled_warehouse_types']] if 'enabled_warehouse_types' in d else None,
            global_param=RepeatedEndpointConfPairs.from_dict(d['global_param']) if 'global_param' in d else None,
            google_service_account=d.get('google_service_account', None),
            instance_profile_arn=d.get('instance_profile_arn', None),
            security_policy=GetWorkspaceWarehouseConfigResponseSecurityPolicy(d['security_policy']) if 'security_policy' in d else None,
            sql_configuration_parameters=RepeatedEndpointConfPairs.from_dict(d['sql_configuration_parameters']) if 'sql_configuration_parameters' in d else None,
        )



class GetWorkspaceWarehouseConfigResponseSecurityPolicy(Enum):
    """Security policy for endpoints"""
    
    DATA_ACCESS_CONTROL = 'DATA_ACCESS_CONTROL'
    NONE = 'NONE'
    PASSTHROUGH = 'PASSTHROUGH'

@dataclass
class ListWarehousesRequest:
    
    # Service Principal which will be used to fetch the list of endpoints. If
    # not specified, GW will use the user from the session header.
    run_as_user_id: int = None # query

    def as_request(self) -> (dict, dict):
        listWarehousesRequest_query, listWarehousesRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.run_as_user_id:
            listWarehousesRequest_query['run_as_user_id'] = self.run_as_user_id
        
        return listWarehousesRequest_query, listWarehousesRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListWarehousesRequest':
        return cls(
            run_as_user_id=d.get('run_as_user_id', None),
        )



@dataclass
class ListWarehousesResponse:
    
    # A list of warehouses and their configurations.
    warehouses: 'List[EndpointInfo]' = None

    def as_request(self) -> (dict, dict):
        listWarehousesResponse_query, listWarehousesResponse_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.warehouses:
            listWarehousesResponse_body['warehouses'] = [v.as_request()[1] for v in self.warehouses]
        
        return listWarehousesResponse_query, listWarehousesResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListWarehousesResponse':
        return cls(
            warehouses=[EndpointInfo.from_dict(v) for v in d['warehouses']] if 'warehouses' in d else None,
        )



@dataclass
class OdbcParams:
    
    
    hostname: str = None
    
    path: str = None
    
    port: int = None
    
    protocol: str = None

    def as_request(self) -> (dict, dict):
        odbcParams_query, odbcParams_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.hostname:
            odbcParams_body['hostname'] = self.hostname
        if self.path:
            odbcParams_body['path'] = self.path
        if self.port:
            odbcParams_body['port'] = self.port
        if self.protocol:
            odbcParams_body['protocol'] = self.protocol
        
        return odbcParams_query, odbcParams_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'OdbcParams':
        return cls(
            hostname=d.get('hostname', None),
            path=d.get('path', None),
            port=d.get('port', None),
            protocol=d.get('protocol', None),
        )



@dataclass
class RepeatedEndpointConfPairs:
    
    # Deprecated: Use configuration_pairs
    config_pair: 'List[EndpointConfPair]' = None
    
    configuration_pairs: 'List[EndpointConfPair]' = None

    def as_request(self) -> (dict, dict):
        repeatedEndpointConfPairs_query, repeatedEndpointConfPairs_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.config_pair:
            repeatedEndpointConfPairs_body['config_pair'] = [v.as_request()[1] for v in self.config_pair]
        if self.configuration_pairs:
            repeatedEndpointConfPairs_body['configuration_pairs'] = [v.as_request()[1] for v in self.configuration_pairs]
        
        return repeatedEndpointConfPairs_query, repeatedEndpointConfPairs_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'RepeatedEndpointConfPairs':
        return cls(
            config_pair=[EndpointConfPair.from_dict(v) for v in d['config_pair']] if 'config_pair' in d else None,
            configuration_pairs=[EndpointConfPair.from_dict(v) for v in d['configuration_pairs']] if 'configuration_pairs' in d else None,
        )



@dataclass
class SetWorkspaceWarehouseConfigRequest:
    
    # Optional: Channel selection details
    channel: 'Channel' = None
    # Deprecated: Use sql_configuration_parameters
    config_param: 'RepeatedEndpointConfPairs' = None
    # Spark confs for external hive metastore configuration JSON serialized size
    # must be less than <= 512K
    data_access_config: 'List[EndpointConfPair]' = None
    # Enable Serverless compute for SQL Endpoints
    # 
    # Deprecated: Use enable_serverless_compute TODO(SC-79930): Remove the field
    # once clients are updated
    enable_databricks_compute: bool = None
    # Enable Serverless compute for SQL Endpoints
    enable_serverless_compute: bool = None
    # List of Warehouse Types allowed in this workspace (limits allowed value of
    # the type field in CreateWarehouse and EditWarehouse). Note: Some types
    # cannot be disabled, they don't need to be specified in
    # SetWorkspaceWarehouseConfig. Note: Disabling a type may cause existing
    # warehouses to be converted to another type. Used by frontend to save
    # specific type availability in the warehouse create and edit form UI.
    enabled_warehouse_types: 'List[WarehouseTypePair]' = None
    # Deprecated: Use sql_configuration_parameters
    global_param: 'RepeatedEndpointConfPairs' = None
    # GCP only: Google Service Account used to pass to cluster to access Google
    # Cloud Storage
    google_service_account: str = None
    # AWS Only: Instance profile used to pass IAM role to the cluster
    instance_profile_arn: str = None
    # Security policy for endpoints
    security_policy: 'SetWorkspaceWarehouseConfigRequestSecurityPolicy' = None
    # Internal. Used by frontend to save Serverless Compute agreement value.
    serverless_agreement: bool = None
    # SQL configuration parameters
    sql_configuration_parameters: 'RepeatedEndpointConfPairs' = None

    def as_request(self) -> (dict, dict):
        setWorkspaceWarehouseConfigRequest_query, setWorkspaceWarehouseConfigRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.channel:
            setWorkspaceWarehouseConfigRequest_body['channel'] = self.channel.as_request()[1]
        if self.config_param:
            setWorkspaceWarehouseConfigRequest_body['config_param'] = self.config_param.as_request()[1]
        if self.data_access_config:
            setWorkspaceWarehouseConfigRequest_body['data_access_config'] = [v.as_request()[1] for v in self.data_access_config]
        if self.enable_databricks_compute:
            setWorkspaceWarehouseConfigRequest_body['enable_databricks_compute'] = self.enable_databricks_compute
        if self.enable_serverless_compute:
            setWorkspaceWarehouseConfigRequest_body['enable_serverless_compute'] = self.enable_serverless_compute
        if self.enabled_warehouse_types:
            setWorkspaceWarehouseConfigRequest_body['enabled_warehouse_types'] = [v.as_request()[1] for v in self.enabled_warehouse_types]
        if self.global_param:
            setWorkspaceWarehouseConfigRequest_body['global_param'] = self.global_param.as_request()[1]
        if self.google_service_account:
            setWorkspaceWarehouseConfigRequest_body['google_service_account'] = self.google_service_account
        if self.instance_profile_arn:
            setWorkspaceWarehouseConfigRequest_body['instance_profile_arn'] = self.instance_profile_arn
        if self.security_policy:
            setWorkspaceWarehouseConfigRequest_body['security_policy'] = self.security_policy.value
        if self.serverless_agreement:
            setWorkspaceWarehouseConfigRequest_body['serverless_agreement'] = self.serverless_agreement
        if self.sql_configuration_parameters:
            setWorkspaceWarehouseConfigRequest_body['sql_configuration_parameters'] = self.sql_configuration_parameters.as_request()[1]
        
        return setWorkspaceWarehouseConfigRequest_query, setWorkspaceWarehouseConfigRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'SetWorkspaceWarehouseConfigRequest':
        return cls(
            channel=Channel.from_dict(d['channel']) if 'channel' in d else None,
            config_param=RepeatedEndpointConfPairs.from_dict(d['config_param']) if 'config_param' in d else None,
            data_access_config=[EndpointConfPair.from_dict(v) for v in d['data_access_config']] if 'data_access_config' in d else None,
            enable_databricks_compute=d.get('enable_databricks_compute', None),
            enable_serverless_compute=d.get('enable_serverless_compute', None),
            enabled_warehouse_types=[WarehouseTypePair.from_dict(v) for v in d['enabled_warehouse_types']] if 'enabled_warehouse_types' in d else None,
            global_param=RepeatedEndpointConfPairs.from_dict(d['global_param']) if 'global_param' in d else None,
            google_service_account=d.get('google_service_account', None),
            instance_profile_arn=d.get('instance_profile_arn', None),
            security_policy=SetWorkspaceWarehouseConfigRequestSecurityPolicy(d['security_policy']) if 'security_policy' in d else None,
            serverless_agreement=d.get('serverless_agreement', None),
            sql_configuration_parameters=RepeatedEndpointConfPairs.from_dict(d['sql_configuration_parameters']) if 'sql_configuration_parameters' in d else None,
        )



class SetWorkspaceWarehouseConfigRequestSecurityPolicy(Enum):
    """Security policy for endpoints"""
    
    DATA_ACCESS_CONTROL = 'DATA_ACCESS_CONTROL'
    NONE = 'NONE'
    PASSTHROUGH = 'PASSTHROUGH'

@dataclass
class StartWarehouseRequest:
    
    # Required. Id of the SQL warehouse.
    id: str # path

    def as_request(self) -> (dict, dict):
        startWarehouseRequest_query, startWarehouseRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.id:
            startWarehouseRequest_body['id'] = self.id
        
        return startWarehouseRequest_query, startWarehouseRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'StartWarehouseRequest':
        return cls(
            id=d.get('id', None),
        )



@dataclass
class StopWarehouseRequest:
    
    # Required. Id of the SQL warehouse.
    id: str # path

    def as_request(self) -> (dict, dict):
        stopWarehouseRequest_query, stopWarehouseRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.id:
            stopWarehouseRequest_body['id'] = self.id
        
        return stopWarehouseRequest_query, stopWarehouseRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'StopWarehouseRequest':
        return cls(
            id=d.get('id', None),
        )



@dataclass
class TerminationReason:
    
    # status code indicating why the cluster was terminated
    code: 'TerminationReasonCode' = None
    # list of parameters that provide additional information about why the
    # cluster was terminated
    parameters: 'Dict[str,str]' = None
    # type of the termination
    type: 'TerminationReasonType' = None

    def as_request(self) -> (dict, dict):
        terminationReason_query, terminationReason_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.code:
            terminationReason_body['code'] = self.code.value
        if self.parameters:
            terminationReason_body['parameters'] = self.parameters
        if self.type:
            terminationReason_body['type'] = self.type.value
        
        return terminationReason_query, terminationReason_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'TerminationReason':
        return cls(
            code=TerminationReasonCode(d['code']) if 'code' in d else None,
            parameters=d.get('parameters', None),
            type=TerminationReasonType(d['type']) if 'type' in d else None,
        )



class TerminationReasonCode(Enum):
    """status code indicating why the cluster was terminated"""
    
    ABUSE_DETECTED = 'ABUSE_DETECTED'
    ATTACH_PROJECT_FAILURE = 'ATTACH_PROJECT_FAILURE'
    AWS_AUTHORIZATION_FAILURE = 'AWS_AUTHORIZATION_FAILURE'
    AWS_INSUFFICIENT_FREE_ADDRESSES_IN_SUBNET_FAILURE = 'AWS_INSUFFICIENT_FREE_ADDRESSES_IN_SUBNET_FAILURE'
    AWS_INSUFFICIENT_INSTANCE_CAPACITY_FAILURE = 'AWS_INSUFFICIENT_INSTANCE_CAPACITY_FAILURE'
    AWS_MAX_SPOT_INSTANCE_COUNT_EXCEEDED_FAILURE = 'AWS_MAX_SPOT_INSTANCE_COUNT_EXCEEDED_FAILURE'
    AWS_REQUEST_LIMIT_EXCEEDED = 'AWS_REQUEST_LIMIT_EXCEEDED'
    AWS_UNSUPPORTED_FAILURE = 'AWS_UNSUPPORTED_FAILURE'
    AZURE_BYOK_KEY_PERMISSION_FAILURE = 'AZURE_BYOK_KEY_PERMISSION_FAILURE'
    AZURE_EPHEMERAL_DISK_FAILURE = 'AZURE_EPHEMERAL_DISK_FAILURE'
    AZURE_INVALID_DEPLOYMENT_TEMPLATE = 'AZURE_INVALID_DEPLOYMENT_TEMPLATE'
    AZURE_OPERATION_NOT_ALLOWED_EXCEPTION = 'AZURE_OPERATION_NOT_ALLOWED_EXCEPTION'
    AZURE_QUOTA_EXCEEDED_EXCEPTION = 'AZURE_QUOTA_EXCEEDED_EXCEPTION'
    AZURE_RESOURCE_MANAGER_THROTTLING = 'AZURE_RESOURCE_MANAGER_THROTTLING'
    AZURE_RESOURCE_PROVIDER_THROTTLING = 'AZURE_RESOURCE_PROVIDER_THROTTLING'
    AZURE_UNEXPECTED_DEPLOYMENT_TEMPLATE_FAILURE = 'AZURE_UNEXPECTED_DEPLOYMENT_TEMPLATE_FAILURE'
    AZURE_VM_EXTENSION_FAILURE = 'AZURE_VM_EXTENSION_FAILURE'
    AZURE_VNET_CONFIGURATION_FAILURE = 'AZURE_VNET_CONFIGURATION_FAILURE'
    BOOTSTRAP_TIMEOUT = 'BOOTSTRAP_TIMEOUT'
    BOOTSTRAP_TIMEOUT_CLOUD_PROVIDER_EXCEPTION = 'BOOTSTRAP_TIMEOUT_CLOUD_PROVIDER_EXCEPTION'
    CLOUD_PROVIDER_DISK_SETUP_FAILURE = 'CLOUD_PROVIDER_DISK_SETUP_FAILURE'
    CLOUD_PROVIDER_LAUNCH_FAILURE = 'CLOUD_PROVIDER_LAUNCH_FAILURE'
    CLOUD_PROVIDER_RESOURCE_STOCKOUT = 'CLOUD_PROVIDER_RESOURCE_STOCKOUT'
    CLOUD_PROVIDER_SHUTDOWN = 'CLOUD_PROVIDER_SHUTDOWN'
    COMMUNICATION_LOST = 'COMMUNICATION_LOST'
    CONTAINER_LAUNCH_FAILURE = 'CONTAINER_LAUNCH_FAILURE'
    CONTROL_PLANE_REQUEST_FAILURE = 'CONTROL_PLANE_REQUEST_FAILURE'
    DATABASE_CONNECTION_FAILURE = 'DATABASE_CONNECTION_FAILURE'
    DBFS_COMPONENT_UNHEALTHY = 'DBFS_COMPONENT_UNHEALTHY'
    DOCKER_IMAGE_PULL_FAILURE = 'DOCKER_IMAGE_PULL_FAILURE'
    DRIVER_UNREACHABLE = 'DRIVER_UNREACHABLE'
    DRIVER_UNRESPONSIVE = 'DRIVER_UNRESPONSIVE'
    EXECUTION_COMPONENT_UNHEALTHY = 'EXECUTION_COMPONENT_UNHEALTHY'
    GCP_QUOTA_EXCEEDED = 'GCP_QUOTA_EXCEEDED'
    GCP_SERVICE_ACCOUNT_DELETED = 'GCP_SERVICE_ACCOUNT_DELETED'
    GLOBAL_INIT_SCRIPT_FAILURE = 'GLOBAL_INIT_SCRIPT_FAILURE'
    HIVE_METASTORE_PROVISIONING_FAILURE = 'HIVE_METASTORE_PROVISIONING_FAILURE'
    IMAGE_PULL_PERMISSION_DENIED = 'IMAGE_PULL_PERMISSION_DENIED'
    INACTIVITY = 'INACTIVITY'
    INIT_SCRIPT_FAILURE = 'INIT_SCRIPT_FAILURE'
    INSTANCE_POOL_CLUSTER_FAILURE = 'INSTANCE_POOL_CLUSTER_FAILURE'
    INSTANCE_UNREACHABLE = 'INSTANCE_UNREACHABLE'
    INTERNAL_ERROR = 'INTERNAL_ERROR'
    INVALID_ARGUMENT = 'INVALID_ARGUMENT'
    INVALID_SPARK_IMAGE = 'INVALID_SPARK_IMAGE'
    IP_EXHAUSTION_FAILURE = 'IP_EXHAUSTION_FAILURE'
    JOB_FINISHED = 'JOB_FINISHED'
    K8S_AUTOSCALING_FAILURE = 'K8S_AUTOSCALING_FAILURE'
    K8S_DBR_CLUSTER_LAUNCH_TIMEOUT = 'K8S_DBR_CLUSTER_LAUNCH_TIMEOUT'
    METASTORE_COMPONENT_UNHEALTHY = 'METASTORE_COMPONENT_UNHEALTHY'
    NEPHOS_RESOURCE_MANAGEMENT = 'NEPHOS_RESOURCE_MANAGEMENT'
    NETWORK_CONFIGURATION_FAILURE = 'NETWORK_CONFIGURATION_FAILURE'
    NFS_MOUNT_FAILURE = 'NFS_MOUNT_FAILURE'
    NPIP_TUNNEL_SETUP_FAILURE = 'NPIP_TUNNEL_SETUP_FAILURE'
    NPIP_TUNNEL_TOKEN_FAILURE = 'NPIP_TUNNEL_TOKEN_FAILURE'
    REQUEST_REJECTED = 'REQUEST_REJECTED'
    REQUEST_THROTTLED = 'REQUEST_THROTTLED'
    SECRET_RESOLUTION_ERROR = 'SECRET_RESOLUTION_ERROR'
    SECURITY_DAEMON_REGISTRATION_EXCEPTION = 'SECURITY_DAEMON_REGISTRATION_EXCEPTION'
    SELF_BOOTSTRAP_FAILURE = 'SELF_BOOTSTRAP_FAILURE'
    SKIPPED_SLOW_NODES = 'SKIPPED_SLOW_NODES'
    SLOW_IMAGE_DOWNLOAD = 'SLOW_IMAGE_DOWNLOAD'
    SPARK_ERROR = 'SPARK_ERROR'
    SPARK_IMAGE_DOWNLOAD_FAILURE = 'SPARK_IMAGE_DOWNLOAD_FAILURE'
    SPARK_STARTUP_FAILURE = 'SPARK_STARTUP_FAILURE'
    SPOT_INSTANCE_TERMINATION = 'SPOT_INSTANCE_TERMINATION'
    STORAGE_DOWNLOAD_FAILURE = 'STORAGE_DOWNLOAD_FAILURE'
    STS_CLIENT_SETUP_FAILURE = 'STS_CLIENT_SETUP_FAILURE'
    SUBNET_EXHAUSTED_FAILURE = 'SUBNET_EXHAUSTED_FAILURE'
    TEMPORARILY_UNAVAILABLE = 'TEMPORARILY_UNAVAILABLE'
    TRIAL_EXPIRED = 'TRIAL_EXPIRED'
    UNEXPECTED_LAUNCH_FAILURE = 'UNEXPECTED_LAUNCH_FAILURE'
    UNKNOWN = 'UNKNOWN'
    UNSUPPORTED_INSTANCE_TYPE = 'UNSUPPORTED_INSTANCE_TYPE'
    UPDATE_INSTANCE_PROFILE_FAILURE = 'UPDATE_INSTANCE_PROFILE_FAILURE'
    USER_REQUEST = 'USER_REQUEST'
    WORKER_SETUP_FAILURE = 'WORKER_SETUP_FAILURE'
    WORKSPACE_CANCELLED_ERROR = 'WORKSPACE_CANCELLED_ERROR'
    WORKSPACE_CONFIGURATION_ERROR = 'WORKSPACE_CONFIGURATION_ERROR'

class TerminationReasonType(Enum):
    """type of the termination"""
    
    CLIENT_ERROR = 'CLIENT_ERROR'
    CLOUD_FAILURE = 'CLOUD_FAILURE'
    SERVICE_FAULT = 'SERVICE_FAULT'
    SUCCESS = 'SUCCESS'

@dataclass
class WarehouseTypePair:
    
    # If set to false the specific warehouse type will not be be allowed as a
    # value for warehouse_type in CreateWarehouse and EditWarehouse
    enabled: bool = None
    
    warehouse_type: 'WarehouseTypePairWarehouseType' = None

    def as_request(self) -> (dict, dict):
        warehouseTypePair_query, warehouseTypePair_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.enabled:
            warehouseTypePair_body['enabled'] = self.enabled
        if self.warehouse_type:
            warehouseTypePair_body['warehouse_type'] = self.warehouse_type.value
        
        return warehouseTypePair_query, warehouseTypePair_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'WarehouseTypePair':
        return cls(
            enabled=d.get('enabled', None),
            warehouse_type=WarehouseTypePairWarehouseType(d['warehouse_type']) if 'warehouse_type' in d else None,
        )



class WarehouseTypePairWarehouseType(Enum):
    
    
    CLASSIC = 'CLASSIC'
    PRO = 'PRO'
    TYPE_UNSPECIFIED = 'TYPE_UNSPECIFIED'

class WarehousesAPI:
    def __init__(self, api_client):
        self._api = api_client
    
    def createWarehouse(self, request: CreateWarehouseRequest) -> CreateWarehouseResponse:
        """Creates a new SQL warehouse."""
        query, body = request.as_request()
        json = self._api.do('POST', '/api/2.0/sql/warehouses', query=query, body=body)
        return CreateWarehouseResponse.from_dict(json)
    
    def deleteWarehouse(self, request: DeleteWarehouseRequest):
        """Deletes a SQL warehouse."""
        query, body = request.as_request()
        self._api.do('DELETE', f'/api/2.0/sql/warehouses/{request.id}', query=query, body=body)
        
    
    def editWarehouse(self, request: EditWarehouseRequest):
        """Edits a SQL warehouse."""
        query, body = request.as_request()
        self._api.do('POST', f'/api/2.0/sql/warehouses/{request.id}/edit', query=query, body=body)
        
    
    def getWarehouse(self, request: GetWarehouseRequest) -> GetWarehouseResponse:
        """Gets the information for a single SQL warehouse."""
        query, body = request.as_request()
        json = self._api.do('GET', f'/api/2.0/sql/warehouses/{request.id}', query=query, body=body)
        return GetWarehouseResponse.from_dict(json)
    
    def getWorkspaceWarehouseConfig(self) -> GetWorkspaceWarehouseConfigResponse:
        """Gets the workspace level configuration that is shared by all SQL
        warehouses in a workspace."""
        
        json = self._api.do('GET', '/api/2.0/sql/config/warehouses')
        return GetWorkspaceWarehouseConfigResponse.from_dict(json)
    
    def listWarehouses(self, request: ListWarehousesRequest) -> ListWarehousesResponse:
        """Lists all SQL warehouse a user has manager permissions for."""
        query, body = request.as_request()
        json = self._api.do('GET', '/api/2.0/sql/warehouses', query=query, body=body)
        return ListWarehousesResponse.from_dict(json)
    
    def setWorkspaceWarehouseConfig(self, request: SetWorkspaceWarehouseConfigRequest):
        """Sets the workspace level configuration that is shared by all SQL
        warehouses in a workspace."""
        query, body = request.as_request()
        self._api.do('PUT', '/api/2.0/sql/config/warehouses', query=query, body=body)
        
    
    def startWarehouse(self, request: StartWarehouseRequest):
        """Starts a SQL warehouse."""
        query, body = request.as_request()
        self._api.do('POST', f'/api/2.0/sql/warehouses/{request.id}/start', query=query, body=body)
        
    
    def stopWarehouse(self, request: StopWarehouseRequest):
        """Stops a SQL warehouse."""
        query, body = request.as_request()
        self._api.do('POST', f'/api/2.0/sql/warehouses/{request.id}/stop', query=query, body=body)
        
    