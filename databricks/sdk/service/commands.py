# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

from dataclasses import dataclass
from enum import Enum
from typing import Any, Dict, List

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
                   language=Language(d['language']) if 'language' in d else None)


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
                   status=CommandStatus(d['status']) if 'status' in d else None)


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
        return cls(id=d.get('id', None), status=ContextStatus(d['status']) if 'status' in d else None)


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
                   language=Language(d['language']) if 'language' in d else None)


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
    schema: 'List[List[Any]]'
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
        return cls(cause=d.get('cause', None),
                   data=d.get('data', None),
                   file_name=d.get('fileName', None),
                   file_names=d.get('fileNames', None),
                   is_json_schema=d.get('isJsonSchema', None),
                   pos=d.get('pos', None),
                   result_type=ResultType(d['resultType']) if 'resultType' in d else None,
                   schema=d.get('schema', None),
                   summary=d.get('summary', None),
                   truncated=d.get('truncated', None))


class CommandExecutionAPI:
    """This API allows execution of Python, Scala, SQL, or R commands on running Databricks Clusters."""

    def __init__(self, api_client):
        self._api = api_client

    def cancel(self, *, cluster_id: str = None, command_id: str = None, context_id: str = None, **kwargs):
        """Cancel a command.
        
        Cancels a currently running command within an execution context.
        
        The command ID is obtained from a prior successful call to __execute__."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = CancelCommand(cluster_id=cluster_id, command_id=command_id, context_id=context_id)
        body = request.as_dict()
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

    def create(self, *, cluster_id: str = None, language: Language = None, **kwargs) -> Created:
        """Create an execution context.
        
        Creates an execution context for running cluster commands.
        
        If successful, this method returns the ID of the new execution context."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = CreateContext(cluster_id=cluster_id, language=language)
        body = request.as_dict()

        json = self._api.do('POST', '/api/1.2/contexts/create', body=body)
        return Created.from_dict(json)

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
                **kwargs) -> Created:
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

        json = self._api.do('POST', '/api/1.2/commands/execute', body=body)
        return Created.from_dict(json)
