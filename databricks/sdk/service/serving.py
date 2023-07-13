# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

import logging
import random
import time
from dataclasses import dataclass
from datetime import timedelta
from enum import Enum
from typing import Any, Callable, Dict, Iterator, List, Optional

from ..errors import OperationFailed
from ._internal import Wait, _enum, _from_dict, _repeated

_LOG = logging.getLogger('databricks.sdk')

# all definitions in this file are in alphabetical order


@dataclass
class BuildLogsRequest:
    """Retrieve the logs associated with building the model's environment for a given serving
    endpoint's served model."""

    name: str
    served_model_name: str


@dataclass
class BuildLogsResponse:
    logs: str

    def as_dict(self) -> dict:
        body = {}
        if self.logs is not None: body['logs'] = self.logs
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'BuildLogsResponse':
        return cls(logs=d.get('logs', None))


@dataclass
class CreateServingEndpoint:
    name: str
    config: 'EndpointCoreConfigInput'

    def as_dict(self) -> dict:
        body = {}
        if self.config: body['config'] = self.config.as_dict()
        if self.name is not None: body['name'] = self.name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateServingEndpoint':
        return cls(config=_from_dict(d, 'config', EndpointCoreConfigInput), name=d.get('name', None))


@dataclass
class DeleteServingEndpointRequest:
    """Delete a serving endpoint"""

    name: str


@dataclass
class EndpointCoreConfigInput:
    served_models: 'List[ServedModelInput]'
    name: Optional[str] = None
    traffic_config: Optional['TrafficConfig'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.name is not None: body['name'] = self.name
        if self.served_models: body['served_models'] = [v.as_dict() for v in self.served_models]
        if self.traffic_config: body['traffic_config'] = self.traffic_config.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'EndpointCoreConfigInput':
        return cls(name=d.get('name', None),
                   served_models=_repeated(d, 'served_models', ServedModelInput),
                   traffic_config=_from_dict(d, 'traffic_config', TrafficConfig))


@dataclass
class EndpointCoreConfigOutput:
    config_version: Optional[int] = None
    served_models: Optional['List[ServedModelOutput]'] = None
    traffic_config: Optional['TrafficConfig'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.config_version is not None: body['config_version'] = self.config_version
        if self.served_models: body['served_models'] = [v.as_dict() for v in self.served_models]
        if self.traffic_config: body['traffic_config'] = self.traffic_config.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'EndpointCoreConfigOutput':
        return cls(config_version=d.get('config_version', None),
                   served_models=_repeated(d, 'served_models', ServedModelOutput),
                   traffic_config=_from_dict(d, 'traffic_config', TrafficConfig))


@dataclass
class EndpointCoreConfigSummary:
    served_models: Optional['List[ServedModelSpec]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.served_models: body['served_models'] = [v.as_dict() for v in self.served_models]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'EndpointCoreConfigSummary':
        return cls(served_models=_repeated(d, 'served_models', ServedModelSpec))


@dataclass
class EndpointPendingConfig:
    config_version: Optional[int] = None
    served_models: Optional['List[ServedModelOutput]'] = None
    start_time: Optional[int] = None
    traffic_config: Optional['TrafficConfig'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.config_version is not None: body['config_version'] = self.config_version
        if self.served_models: body['served_models'] = [v.as_dict() for v in self.served_models]
        if self.start_time is not None: body['start_time'] = self.start_time
        if self.traffic_config: body['traffic_config'] = self.traffic_config.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'EndpointPendingConfig':
        return cls(config_version=d.get('config_version', None),
                   served_models=_repeated(d, 'served_models', ServedModelOutput),
                   start_time=d.get('start_time', None),
                   traffic_config=_from_dict(d, 'traffic_config', TrafficConfig))


@dataclass
class EndpointState:
    config_update: Optional['EndpointStateConfigUpdate'] = None
    ready: Optional['EndpointStateReady'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.config_update is not None: body['config_update'] = self.config_update.value
        if self.ready is not None: body['ready'] = self.ready.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'EndpointState':
        return cls(config_update=_enum(d, 'config_update', EndpointStateConfigUpdate),
                   ready=_enum(d, 'ready', EndpointStateReady))


class EndpointStateConfigUpdate(Enum):
    """The state of an endpoint's config update. This informs the user if the pending_config is in
    progress, if the update failed, or if there is no update in progress. Note that if the
    endpoint's config_update state value is IN_PROGRESS, another update can not be made until the
    update completes or fails."""

    IN_PROGRESS = 'IN_PROGRESS'
    NOT_UPDATING = 'NOT_UPDATING'
    UPDATE_FAILED = 'UPDATE_FAILED'


class EndpointStateReady(Enum):
    """The state of an endpoint, indicating whether or not the endpoint is queryable. An endpoint is
    READY if all of the served models in its active configuration are ready. If any of the actively
    served models are in a non-ready state, the endpoint state will be NOT_READY."""

    NOT_READY = 'NOT_READY'
    READY = 'READY'


@dataclass
class ExportMetricsRequest:
    """Retrieve the metrics associated with a serving endpoint"""

    name: str


@dataclass
class GetServingEndpointRequest:
    """Get a single serving endpoint"""

    name: str


@dataclass
class ListEndpointsResponse:
    endpoints: Optional['List[ServingEndpoint]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.endpoints: body['endpoints'] = [v.as_dict() for v in self.endpoints]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListEndpointsResponse':
        return cls(endpoints=_repeated(d, 'endpoints', ServingEndpoint))


@dataclass
class LogsRequest:
    """Retrieve the most recent log lines associated with a given serving endpoint's served model"""

    name: str
    served_model_name: str


@dataclass
class QueryEndpointResponse:
    predictions: 'List[Any]'

    def as_dict(self) -> dict:
        body = {}
        if self.predictions: body['predictions'] = [v for v in self.predictions]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'QueryEndpointResponse':
        return cls(predictions=d.get('predictions', None))


@dataclass
class QueryRequest:
    """Query a serving endpoint with provided model input."""

    name: str


@dataclass
class Route:
    served_model_name: str
    traffic_percentage: int

    def as_dict(self) -> dict:
        body = {}
        if self.served_model_name is not None: body['served_model_name'] = self.served_model_name
        if self.traffic_percentage is not None: body['traffic_percentage'] = self.traffic_percentage
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Route':
        return cls(served_model_name=d.get('served_model_name', None),
                   traffic_percentage=d.get('traffic_percentage', None))


@dataclass
class ServedModelInput:
    model_name: str
    model_version: str
    workload_size: str
    scale_to_zero_enabled: bool
    environment_vars: Optional['Dict[str,str]'] = None
    name: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.environment_vars: body['environment_vars'] = self.environment_vars
        if self.model_name is not None: body['model_name'] = self.model_name
        if self.model_version is not None: body['model_version'] = self.model_version
        if self.name is not None: body['name'] = self.name
        if self.scale_to_zero_enabled is not None: body['scale_to_zero_enabled'] = self.scale_to_zero_enabled
        if self.workload_size is not None: body['workload_size'] = self.workload_size
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ServedModelInput':
        return cls(environment_vars=d.get('environment_vars', None),
                   model_name=d.get('model_name', None),
                   model_version=d.get('model_version', None),
                   name=d.get('name', None),
                   scale_to_zero_enabled=d.get('scale_to_zero_enabled', None),
                   workload_size=d.get('workload_size', None))


@dataclass
class ServedModelOutput:
    creation_timestamp: Optional[int] = None
    creator: Optional[str] = None
    environment_vars: Optional['Dict[str,str]'] = None
    model_name: Optional[str] = None
    model_version: Optional[str] = None
    name: Optional[str] = None
    scale_to_zero_enabled: Optional[bool] = None
    state: Optional['ServedModelState'] = None
    workload_size: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.creation_timestamp is not None: body['creation_timestamp'] = self.creation_timestamp
        if self.creator is not None: body['creator'] = self.creator
        if self.environment_vars: body['environment_vars'] = self.environment_vars
        if self.model_name is not None: body['model_name'] = self.model_name
        if self.model_version is not None: body['model_version'] = self.model_version
        if self.name is not None: body['name'] = self.name
        if self.scale_to_zero_enabled is not None: body['scale_to_zero_enabled'] = self.scale_to_zero_enabled
        if self.state: body['state'] = self.state.as_dict()
        if self.workload_size is not None: body['workload_size'] = self.workload_size
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ServedModelOutput':
        return cls(creation_timestamp=d.get('creation_timestamp', None),
                   creator=d.get('creator', None),
                   environment_vars=d.get('environment_vars', None),
                   model_name=d.get('model_name', None),
                   model_version=d.get('model_version', None),
                   name=d.get('name', None),
                   scale_to_zero_enabled=d.get('scale_to_zero_enabled', None),
                   state=_from_dict(d, 'state', ServedModelState),
                   workload_size=d.get('workload_size', None))


@dataclass
class ServedModelSpec:
    model_name: Optional[str] = None
    model_version: Optional[str] = None
    name: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.model_name is not None: body['model_name'] = self.model_name
        if self.model_version is not None: body['model_version'] = self.model_version
        if self.name is not None: body['name'] = self.name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ServedModelSpec':
        return cls(model_name=d.get('model_name', None),
                   model_version=d.get('model_version', None),
                   name=d.get('name', None))


@dataclass
class ServedModelState:
    deployment: Optional['ServedModelStateDeployment'] = None
    deployment_state_message: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.deployment is not None: body['deployment'] = self.deployment.value
        if self.deployment_state_message is not None:
            body['deployment_state_message'] = self.deployment_state_message
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ServedModelState':
        return cls(deployment=_enum(d, 'deployment', ServedModelStateDeployment),
                   deployment_state_message=d.get('deployment_state_message', None))


class ServedModelStateDeployment(Enum):
    """The state of the served model deployment. DEPLOYMENT_CREATING indicates that the served model is
    not ready yet because the deployment is still being created (i.e container image is building,
    model server is deploying for the first time, etc.). DEPLOYMENT_RECOVERING indicates that the
    served model was previously in a ready state but no longer is and is attempting to recover.
    DEPLOYMENT_READY indicates that the served model is ready to receive traffic. DEPLOYMENT_FAILED
    indicates that there was an error trying to bring up the served model (e.g container image build
    failed, the model server failed to start due to a model loading error, etc.) DEPLOYMENT_ABORTED
    indicates that the deployment was terminated likely due to a failure in bringing up another
    served model under the same endpoint and config version."""

    DEPLOYMENT_ABORTED = 'DEPLOYMENT_ABORTED'
    DEPLOYMENT_CREATING = 'DEPLOYMENT_CREATING'
    DEPLOYMENT_FAILED = 'DEPLOYMENT_FAILED'
    DEPLOYMENT_READY = 'DEPLOYMENT_READY'
    DEPLOYMENT_RECOVERING = 'DEPLOYMENT_RECOVERING'


@dataclass
class ServerLogsResponse:
    logs: str

    def as_dict(self) -> dict:
        body = {}
        if self.logs is not None: body['logs'] = self.logs
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ServerLogsResponse':
        return cls(logs=d.get('logs', None))


@dataclass
class ServingEndpoint:
    config: Optional['EndpointCoreConfigSummary'] = None
    creation_timestamp: Optional[int] = None
    creator: Optional[str] = None
    id: Optional[str] = None
    last_updated_timestamp: Optional[int] = None
    name: Optional[str] = None
    state: Optional['EndpointState'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.config: body['config'] = self.config.as_dict()
        if self.creation_timestamp is not None: body['creation_timestamp'] = self.creation_timestamp
        if self.creator is not None: body['creator'] = self.creator
        if self.id is not None: body['id'] = self.id
        if self.last_updated_timestamp is not None:
            body['last_updated_timestamp'] = self.last_updated_timestamp
        if self.name is not None: body['name'] = self.name
        if self.state: body['state'] = self.state.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ServingEndpoint':
        return cls(config=_from_dict(d, 'config', EndpointCoreConfigSummary),
                   creation_timestamp=d.get('creation_timestamp', None),
                   creator=d.get('creator', None),
                   id=d.get('id', None),
                   last_updated_timestamp=d.get('last_updated_timestamp', None),
                   name=d.get('name', None),
                   state=_from_dict(d, 'state', EndpointState))


@dataclass
class ServingEndpointDetailed:
    config: Optional['EndpointCoreConfigOutput'] = None
    creation_timestamp: Optional[int] = None
    creator: Optional[str] = None
    id: Optional[str] = None
    last_updated_timestamp: Optional[int] = None
    name: Optional[str] = None
    pending_config: Optional['EndpointPendingConfig'] = None
    permission_level: Optional['ServingEndpointDetailedPermissionLevel'] = None
    state: Optional['EndpointState'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.config: body['config'] = self.config.as_dict()
        if self.creation_timestamp is not None: body['creation_timestamp'] = self.creation_timestamp
        if self.creator is not None: body['creator'] = self.creator
        if self.id is not None: body['id'] = self.id
        if self.last_updated_timestamp is not None:
            body['last_updated_timestamp'] = self.last_updated_timestamp
        if self.name is not None: body['name'] = self.name
        if self.pending_config: body['pending_config'] = self.pending_config.as_dict()
        if self.permission_level is not None: body['permission_level'] = self.permission_level.value
        if self.state: body['state'] = self.state.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ServingEndpointDetailed':
        return cls(config=_from_dict(d, 'config', EndpointCoreConfigOutput),
                   creation_timestamp=d.get('creation_timestamp', None),
                   creator=d.get('creator', None),
                   id=d.get('id', None),
                   last_updated_timestamp=d.get('last_updated_timestamp', None),
                   name=d.get('name', None),
                   pending_config=_from_dict(d, 'pending_config', EndpointPendingConfig),
                   permission_level=_enum(d, 'permission_level', ServingEndpointDetailedPermissionLevel),
                   state=_from_dict(d, 'state', EndpointState))


class ServingEndpointDetailedPermissionLevel(Enum):
    """The permission level of the principal making the request."""

    CAN_MANAGE = 'CAN_MANAGE'
    CAN_QUERY = 'CAN_QUERY'
    CAN_VIEW = 'CAN_VIEW'


@dataclass
class TrafficConfig:
    routes: Optional['List[Route]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.routes: body['routes'] = [v.as_dict() for v in self.routes]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'TrafficConfig':
        return cls(routes=_repeated(d, 'routes', Route))


class ServingEndpointsAPI:
    """The Serving Endpoints API allows you to create, update, and delete model serving endpoints.
    
    You can use a serving endpoint to serve models from the Databricks Model Registry or from Unity Catalog.
    Endpoints expose the underlying models as scalable REST API endpoints using serverless compute. This means
    the endpoints and associated compute resources are fully managed by Databricks and will not appear in your
    cloud account. A serving endpoint can consist of one or more MLflow models from the Databricks Model
    Registry, called served models. A serving endpoint can have at most ten served models. You can configure
    traffic settings to define how requests should be routed to your served models behind an endpoint.
    Additionally, you can configure the scale of resources that should be applied to each served model."""

    def __init__(self, api_client):
        self._api = api_client

    def wait_get_serving_endpoint_not_updating(
            self,
            name: str,
            timeout=timedelta(minutes=20),
            callback: Optional[Callable[[ServingEndpointDetailed], None]] = None) -> ServingEndpointDetailed:
        deadline = time.time() + timeout.total_seconds()
        target_states = (EndpointStateConfigUpdate.NOT_UPDATING, )
        failure_states = (EndpointStateConfigUpdate.UPDATE_FAILED, )
        status_message = 'polling...'
        attempt = 1
        while time.time() < deadline:
            poll = self.get(name=name)
            status = poll.state.config_update
            status_message = f'current status: {status}'
            if status in target_states:
                return poll
            if callback:
                callback(poll)
            if status in failure_states:
                msg = f'failed to reach NOT_UPDATING, got {status}: {status_message}'
                raise OperationFailed(msg)
            prefix = f"name={name}"
            sleep = attempt
            if sleep > 10:
                # sleep 10s max per attempt
                sleep = 10
            _LOG.debug(f'{prefix}: ({status}) {status_message} (sleeping ~{sleep}s)')
            time.sleep(sleep + random.random())
            attempt += 1
        raise TimeoutError(f'timed out after {timeout}: {status_message}')

    def build_logs(self, name: str, served_model_name: str, **kwargs) -> BuildLogsResponse:
        """Retrieve the logs associated with building the model's environment for a given serving endpoint's
        served model.
        
        Retrieves the build logs associated with the provided served model.
        
        :param name: str
          The name of the serving endpoint that the served model belongs to. This field is required.
        :param served_model_name: str
          The name of the served model that build logs will be retrieved for. This field is required.
        
        :returns: :class:`BuildLogsResponse`
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = BuildLogsRequest(name=name, served_model_name=served_model_name)

        json = self._api.do(
            'GET',
            f'/api/2.0/serving-endpoints/{request.name}/served-models/{request.served_model_name}/build-logs')
        return BuildLogsResponse.from_dict(json)

    def create(self, name: str, config: EndpointCoreConfigInput, **kwargs) -> Wait[ServingEndpointDetailed]:
        """Create a new serving endpoint.
        
        :param name: str
          The name of the serving endpoint. This field is required and must be unique across a Databricks
          workspace. An endpoint name can consist of alphanumeric characters, dashes, and underscores.
        :param config: :class:`EndpointCoreConfigInput`
          The core config of the serving endpoint.
        
        :returns:
          Long-running operation waiter for :class:`ServingEndpointDetailed`.
          See :method:wait_get_serving_endpoint_not_updating for more details.
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = CreateServingEndpoint(config=config, name=name)
        body = request.as_dict()
        op_response = self._api.do('POST', '/api/2.0/serving-endpoints', body=body)
        return Wait(self.wait_get_serving_endpoint_not_updating,
                    response=ServingEndpointDetailed.from_dict(op_response),
                    name=op_response['name'])

    def create_and_wait(
        self, name: str, config: EndpointCoreConfigInput,
        timeout=timedelta(minutes=20)) -> ServingEndpointDetailed:
        return self.create(config=config, name=name).result(timeout=timeout)

    def delete(self, name: str, **kwargs):
        """Delete a serving endpoint.
        
        :param name: str
          The name of the serving endpoint. This field is required.
        
        
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = DeleteServingEndpointRequest(name=name)

        self._api.do('DELETE', f'/api/2.0/serving-endpoints/{request.name}')

    def export_metrics(self, name: str, **kwargs):
        """Retrieve the metrics associated with a serving endpoint.
        
        Retrieves the metrics associated with the provided serving endpoint in either Prometheus or
        OpenMetrics exposition format.
        
        :param name: str
          The name of the serving endpoint to retrieve metrics for. This field is required.
        
        
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = ExportMetricsRequest(name=name)

        self._api.do('GET', f'/api/2.0/serving-endpoints/{request.name}/metrics')

    def get(self, name: str, **kwargs) -> ServingEndpointDetailed:
        """Get a single serving endpoint.
        
        Retrieves the details for a single serving endpoint.
        
        :param name: str
          The name of the serving endpoint. This field is required.
        
        :returns: :class:`ServingEndpointDetailed`
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GetServingEndpointRequest(name=name)

        json = self._api.do('GET', f'/api/2.0/serving-endpoints/{request.name}')
        return ServingEndpointDetailed.from_dict(json)

    def list(self) -> Iterator[ServingEndpoint]:
        """Retrieve all serving endpoints.
        
        :returns: Iterator over :class:`ServingEndpoint`
        """

        json = self._api.do('GET', '/api/2.0/serving-endpoints')
        return [ServingEndpoint.from_dict(v) for v in json.get('endpoints', [])]

    def logs(self, name: str, served_model_name: str, **kwargs) -> ServerLogsResponse:
        """Retrieve the most recent log lines associated with a given serving endpoint's served model.
        
        Retrieves the service logs associated with the provided served model.
        
        :param name: str
          The name of the serving endpoint that the served model belongs to. This field is required.
        :param served_model_name: str
          The name of the served model that logs will be retrieved for. This field is required.
        
        :returns: :class:`ServerLogsResponse`
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = LogsRequest(name=name, served_model_name=served_model_name)

        json = self._api.do(
            'GET',
            f'/api/2.0/serving-endpoints/{request.name}/served-models/{request.served_model_name}/logs')
        return ServerLogsResponse.from_dict(json)

    def query(self, name: str, **kwargs) -> QueryEndpointResponse:
        """Query a serving endpoint with provided model input.
        
        :param name: str
          The name of the serving endpoint. This field is required.
        
        :returns: :class:`QueryEndpointResponse`
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = QueryRequest(name=name)

        json = self._api.do('POST', f'/serving-endpoints/{request.name}/invocations')
        return QueryEndpointResponse.from_dict(json)

    def update_config(self,
                      served_models: List[ServedModelInput],
                      name: str,
                      *,
                      traffic_config: Optional[TrafficConfig] = None,
                      **kwargs) -> Wait[ServingEndpointDetailed]:
        """Update a serving endpoint with a new config.
        
        Updates any combination of the serving endpoint's served models, the compute configuration of those
        served models, and the endpoint's traffic config. An endpoint that already has an update in progress
        can not be updated until the current update completes or fails.
        
        :param served_models: List[:class:`ServedModelInput`]
          A list of served models for the endpoint to serve. A serving endpoint can have up to 10 served
          models.
        :param name: str
          The name of the serving endpoint to update. This field is required.
        :param traffic_config: :class:`TrafficConfig` (optional)
          The traffic config defining how invocations to the serving endpoint should be routed.
        
        :returns:
          Long-running operation waiter for :class:`ServingEndpointDetailed`.
          See :method:wait_get_serving_endpoint_not_updating for more details.
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = EndpointCoreConfigInput(name=name,
                                              served_models=served_models,
                                              traffic_config=traffic_config)
        body = request.as_dict()
        op_response = self._api.do('PUT', f'/api/2.0/serving-endpoints/{request.name}/config', body=body)
        return Wait(self.wait_get_serving_endpoint_not_updating,
                    response=ServingEndpointDetailed.from_dict(op_response),
                    name=op_response['name'])

    def update_config_and_wait(
        self,
        served_models: List[ServedModelInput],
        name: str,
        *,
        traffic_config: Optional[TrafficConfig] = None,
        timeout=timedelta(minutes=20)) -> ServingEndpointDetailed:
        return self.update_config(name=name, served_models=served_models,
                                  traffic_config=traffic_config).result(timeout=timeout)
