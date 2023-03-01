# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

import logging
import random
import time
from dataclasses import dataclass
from enum import Enum
from typing import Any, Dict, List

from ..errors import OperationFailed, OperationTimeout

_LOG = logging.getLogger('databricks.sdk.service.commands')

# all definitions in this file are in alphabetical order


@dataclass
class CancelCommand:
    cluster_id: str
    command_id: str
    context_id: str

    def as_dict(self) -> dict:
        body = {}
        if self.cluster_id: body['clusterId'] = self.cluster_id
        if self.command_id: body['commandId'] = self.command_id
        if self.context_id: body['contextId'] = self.context_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CancelCommand':
        return cls(cluster_id=d.get('clusterId', None),
                   command_id=d.get('commandId', None),
                   context_id=d.get('contextId', None))


@dataclass
class Command:
    cluster_id: str
    command: str
    context_id: str
    language: 'Language'

    def as_dict(self) -> dict:
        body = {}
        if self.cluster_id: body['clusterId'] = self.cluster_id
        if self.command: body['command'] = self.command
        if self.context_id: body['contextId'] = self.context_id
        if self.language: body['language'] = self.language.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Command':
        return cls(cluster_id=d.get('clusterId', None),
                   command=d.get('command', None),
                   context_id=d.get('contextId', None),
                   language=Language.__members__.get(d['language'], None) if 'language' in d else None)


class CommandStatus(Enum):

    Cancelled = 'Cancelled'
    Cancelling = 'Cancelling'
    Error = 'Error'
    Finished = 'Finished'
    Queued = 'Queued'
    Running = 'Running'


@dataclass
class CommandStatusRequest:
    """Get command info"""

    cluster_id: str
    command_id: str
    context_id: str


@dataclass
class CommandStatusResponse:
    id: str
    results: 'Results'
    status: 'CommandStatus'

    def as_dict(self) -> dict:
        body = {}
        if self.id: body['id'] = self.id
        if self.results: body['results'] = self.results.as_dict()
        if self.status: body['status'] = self.status.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CommandStatusResponse':
        return cls(id=d.get('id', None),
                   results=Results.from_dict(d['results']) if 'results' in d else None,
                   status=CommandStatus.__members__.get(d['status'], None) if 'status' in d else None)


class ContextStatus(Enum):

    Error = 'Error'
    Pending = 'Pending'
    Running = 'Running'


@dataclass
class ContextStatusRequest:
    """Get status"""

    cluster_id: str
    context_id: str


@dataclass
class ContextStatusResponse:
    id: str
    status: 'ContextStatus'

    def as_dict(self) -> dict:
        body = {}
        if self.id: body['id'] = self.id
        if self.status: body['status'] = self.status.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ContextStatusResponse':
        return cls(id=d.get('id', None),
                   status=ContextStatus.__members__.get(d['status'], None) if 'status' in d else None)


@dataclass
class CreateContext:
    cluster_id: str
    language: 'Language'

    def as_dict(self) -> dict:
        body = {}
        if self.cluster_id: body['clusterId'] = self.cluster_id
        if self.language: body['language'] = self.language.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateContext':
        return cls(cluster_id=d.get('clusterId', None),
                   language=Language.__members__.get(d['language'], None) if 'language' in d else None)


@dataclass
class Created:
    id: str

    def as_dict(self) -> dict:
        body = {}
        if self.id: body['id'] = self.id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Created':
        return cls(id=d.get('id', None))


@dataclass
class DestroyContext:
    cluster_id: str
    context_id: str

    def as_dict(self) -> dict:
        body = {}
        if self.cluster_id: body['clusterId'] = self.cluster_id
        if self.context_id: body['contextId'] = self.context_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'DestroyContext':
        return cls(cluster_id=d.get('clusterId', None), context_id=d.get('contextId', None))


class Language(Enum):

    python = 'python'
    scala = 'scala'
    sql = 'sql'


class ResultType(Enum):

    error = 'error'
    image = 'image'
    images = 'images'
    table = 'table'
    text = 'text'


@dataclass
class Results:
    cause: str
    data: Any
    file_name: str
    file_names: 'List[str]'
    is_json_schema: bool
    pos: int
    result_type: 'ResultType'
    schema: 'List[Dict[str,Any]]'
    summary: str
    truncated: bool

    def as_dict(self) -> dict:
        body = {}
        if self.cause: body['cause'] = self.cause
        if self.data: body['data'] = self.data
        if self.file_name: body['fileName'] = self.file_name
        if self.file_names: body['fileNames'] = [v for v in self.file_names]
        if self.is_json_schema: body['isJsonSchema'] = self.is_json_schema
        if self.pos: body['pos'] = self.pos
        if self.result_type: body['resultType'] = self.result_type.value
        if self.schema: body['schema'] = [v for v in self.schema]
        if self.summary: body['summary'] = self.summary
        if self.truncated: body['truncated'] = self.truncated
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Results':
        return cls(
            cause=d.get('cause', None),
            data=d.get('data', None),
            file_name=d.get('fileName', None),
            file_names=d.get('fileNames', None),
            is_json_schema=d.get('isJsonSchema', None),
            pos=d.get('pos', None),
            result_type=ResultType.__members__.get(d['resultType'], None) if 'resultType' in d else None,
            schema=d.get('schema', None),
            summary=d.get('summary', None),
            truncated=d.get('truncated', None))


class CommandExecutionAPI:
    """This API allows execution of Python, Scala, SQL, or R commands on running Databricks Clusters."""

    def __init__(self, api_client):
        self._api = api_client

    def cancel(self,
               *,
               cluster_id: str = None,
               command_id: str = None,
               context_id: str = None,
               wait=True,
               timeout=20,
               **kwargs) -> CommandStatusResponse:
        """Cancel a command.
        
        Cancels a currently running command within an execution context.
        
        The command ID is obtained from a prior successful call to __execute__."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = CancelCommand(cluster_id=cluster_id, command_id=command_id, context_id=context_id)
        body = request.as_dict()
        if wait:
            self._api.do('POST', '/api/1.2/commands/cancel', body=body)
            started = time.time()
            target_states = (CommandStatus.Cancelled, )
            failure_states = (CommandStatus.Error, )
            status_message = 'polling...'
            attempt = 1
            while (started + (timeout * 60)) > time.time():
                poll = self.command_status(cluster_id=request.cluster_id,
                                           command_id=request.command_id,
                                           context_id=request.context_id)
                status = poll.status
                status_message = f'current status: {status}'
                if poll.results:
                    status_message = poll.results.cause
                if status in target_states:
                    return poll
                if status in failure_states:
                    msg = f'failed to reach Cancelled, got {status}: {status_message}'
                    raise OperationFailed(msg)
                prefix = f"command_execution.command_status(cluster_id={request.cluster_id}, command_id={request.command_id}, context_id={request.context_id})"
                sleep = attempt
                if sleep > 10:
                    # sleep 10s max per attempt
                    sleep = 10
                _LOG.debug(f'{prefix}: ({status}) {status_message} (sleeping ~{sleep}s)')
                time.sleep(sleep + random.random())
                attempt += 1
            raise OperationTimeout(f'timed out after {timeout} minutes: {status_message}')
        self._api.do('POST', '/api/1.2/commands/cancel', body=body)

    def command_status(self, cluster_id: str, context_id: str, command_id: str,
                       **kwargs) -> CommandStatusResponse:
        """Get command info.
        
        Gets the status of and, if available, the results from a currently executing command.
        
        The command ID is obtained from a prior successful call to __execute__."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = CommandStatusRequest(cluster_id=cluster_id,
                                           command_id=command_id,
                                           context_id=context_id)

        query = {}
        if cluster_id: query['clusterId'] = request.cluster_id
        if command_id: query['commandId'] = request.command_id
        if context_id: query['contextId'] = request.context_id

        json = self._api.do('GET', '/api/1.2/commands/status', query=query)
        return CommandStatusResponse.from_dict(json)

    def context_status(self, cluster_id: str, context_id: str, **kwargs) -> ContextStatusResponse:
        """Get status.
        
        Gets the status for an execution context."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = ContextStatusRequest(cluster_id=cluster_id, context_id=context_id)

        query = {}
        if cluster_id: query['clusterId'] = request.cluster_id
        if context_id: query['contextId'] = request.context_id

        json = self._api.do('GET', '/api/1.2/contexts/status', query=query)
        return ContextStatusResponse.from_dict(json)

    def create(self,
               *,
               cluster_id: str = None,
               language: Language = None,
               wait=True,
               timeout=20,
               **kwargs) -> ContextStatusResponse:
        """Create an execution context.
        
        Creates an execution context for running cluster commands.
        
        If successful, this method returns the ID of the new execution context."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = CreateContext(cluster_id=cluster_id, language=language)
        body = request.as_dict()
        if wait:
            op_response = self._api.do('POST', '/api/1.2/contexts/create', body=body)
            started = time.time()
            target_states = (ContextStatus.Running, )
            failure_states = (ContextStatus.Error, )
            status_message = 'polling...'
            attempt = 1
            while (started + (timeout * 60)) > time.time():
                poll = self.context_status(cluster_id=request.cluster_id, context_id=op_response['id'])
                status = poll.status
                status_message = f'current status: {status}'
                if status in target_states:
                    return poll
                if status in failure_states:
                    msg = f'failed to reach Running, got {status}: {status_message}'
                    raise OperationFailed(msg)
                prefix = f"command_execution.context_status(cluster_id={request.cluster_id}, context_id={op_response['id']})"
                sleep = attempt
                if sleep > 10:
                    # sleep 10s max per attempt
                    sleep = 10
                _LOG.debug(f'{prefix}: ({status}) {status_message} (sleeping ~{sleep}s)')
                time.sleep(sleep + random.random())
                attempt += 1
            raise OperationTimeout(f'timed out after {timeout} minutes: {status_message}')
        self._api.do('POST', '/api/1.2/contexts/create', body=body)

    def destroy(self, cluster_id: str, context_id: str, **kwargs):
        """Delete an execution context.
        
        Deletes an execution context."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = DestroyContext(cluster_id=cluster_id, context_id=context_id)
        body = request.as_dict()
        self._api.do('POST', '/api/1.2/contexts/destroy', body=body)

    def execute(self,
                *,
                cluster_id: str = None,
                command: str = None,
                context_id: str = None,
                language: Language = None,
                wait=True,
                timeout=20,
                **kwargs) -> CommandStatusResponse:
        """Run a command.
        
        Runs a cluster command in the given execution context, using the provided language.
        
        If successful, it returns an ID for tracking the status of the command's execution."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = Command(cluster_id=cluster_id,
                              command=command,
                              context_id=context_id,
                              language=language)
        body = request.as_dict()
        if wait:
            op_response = self._api.do('POST', '/api/1.2/commands/execute', body=body)
            started = time.time()
            target_states = (CommandStatus.Finished, CommandStatus.Error, )
            failure_states = (CommandStatus.Cancelled, CommandStatus.Cancelling, )
            status_message = 'polling...'
            attempt = 1
            while (started + (timeout * 60)) > time.time():
                poll = self.command_status(cluster_id=request.cluster_id,
                                           command_id=op_response['id'],
                                           context_id=request.context_id)
                status = poll.status
                status_message = f'current status: {status}'
                if status in target_states:
                    return poll
                if status in failure_states:
                    msg = f'failed to reach Finished or Error, got {status}: {status_message}'
                    raise OperationFailed(msg)
                prefix = f"command_execution.command_status(cluster_id={request.cluster_id}, command_id={op_response['id']}, context_id={request.context_id})"
                sleep = attempt
                if sleep > 10:
                    # sleep 10s max per attempt
                    sleep = 10
                _LOG.debug(f'{prefix}: ({status}) {status_message} (sleeping ~{sleep}s)')
                time.sleep(sleep + random.random())
                attempt += 1
            raise OperationTimeout(f'timed out after {timeout} minutes: {status_message}')
        self._api.do('POST', '/api/1.2/commands/execute', body=body)
