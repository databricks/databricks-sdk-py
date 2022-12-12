# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

from dataclasses import dataclass
from enum import Enum
from typing import Optional, Dict, List, Any


# all definitions in this file are in alphabetical order


@dataclass
class CancelCommand:

    clusterId: str

    commandId: str

    contextId: str

    def as_request(self) -> (dict, dict):
        cancelCommand_query, cancelCommand_body = {}, {}
        if self.clusterId:
            cancelCommand_body["clusterId"] = self.clusterId
        if self.commandId:
            cancelCommand_body["commandId"] = self.commandId
        if self.contextId:
            cancelCommand_body["contextId"] = self.contextId

        return cancelCommand_query, cancelCommand_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "CancelCommand":
        return cls(
            clusterId=d.get("clusterId", None),
            commandId=d.get("commandId", None),
            contextId=d.get("contextId", None),
        )


@dataclass
class Command:

    # Running cluster id
    clusterId: str
    # Executable code
    command: str
    # Running context id
    contextId: str

    language: "Language"

    def as_request(self) -> (dict, dict):
        command_query, command_body = {}, {}
        if self.clusterId:
            command_body["clusterId"] = self.clusterId
        if self.command:
            command_body["command"] = self.command
        if self.contextId:
            command_body["contextId"] = self.contextId
        if self.language:
            command_body["language"] = self.language.value

        return command_query, command_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "Command":
        return cls(
            clusterId=d.get("clusterId", None),
            command=d.get("command", None),
            contextId=d.get("contextId", None),
            language=Language(d["language"]) if "language" in d else None,
        )


class CommandStatus(Enum):

    Cancelled = "Cancelled"
    Cancelling = "Cancelling"
    Error = "Error"
    Finished = "Finished"
    Queued = "Queued"
    Running = "Running"


@dataclass
class CommandStatusRequest:
    """Get command info"""

    clusterId: str  # query

    commandId: str  # query

    contextId: str  # query

    def as_request(self) -> (dict, dict):
        commandStatusRequest_query, commandStatusRequest_body = {}, {}
        if self.clusterId:
            commandStatusRequest_query["clusterId"] = self.clusterId
        if self.commandId:
            commandStatusRequest_query["commandId"] = self.commandId
        if self.contextId:
            commandStatusRequest_query["contextId"] = self.contextId

        return commandStatusRequest_query, commandStatusRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "CommandStatusRequest":
        return cls(
            clusterId=d.get("clusterId", None),
            commandId=d.get("commandId", None),
            contextId=d.get("contextId", None),
        )


@dataclass
class CommandStatusResponse:

    id: str

    results: "Results"

    status: "CommandStatus"

    def as_request(self) -> (dict, dict):
        commandStatusResponse_query, commandStatusResponse_body = {}, {}
        if self.id:
            commandStatusResponse_body["id"] = self.id
        if self.results:
            commandStatusResponse_body["results"] = self.results.as_request()[1]
        if self.status:
            commandStatusResponse_body["status"] = self.status.value

        return commandStatusResponse_query, commandStatusResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "CommandStatusResponse":
        return cls(
            id=d.get("id", None),
            results=Results.from_dict(d["results"]) if "results" in d else None,
            status=CommandStatus(d["status"]) if "status" in d else None,
        )


class ContextStatus(Enum):

    Error = "Error"
    Pending = "Pending"
    Running = "Running"


@dataclass
class ContextStatusRequest:
    """Get status"""

    clusterId: str  # query

    contextId: str  # query

    def as_request(self) -> (dict, dict):
        contextStatusRequest_query, contextStatusRequest_body = {}, {}
        if self.clusterId:
            contextStatusRequest_query["clusterId"] = self.clusterId
        if self.contextId:
            contextStatusRequest_query["contextId"] = self.contextId

        return contextStatusRequest_query, contextStatusRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ContextStatusRequest":
        return cls(
            clusterId=d.get("clusterId", None),
            contextId=d.get("contextId", None),
        )


@dataclass
class ContextStatusResponse:

    id: str

    status: "ContextStatus"

    def as_request(self) -> (dict, dict):
        contextStatusResponse_query, contextStatusResponse_body = {}, {}
        if self.id:
            contextStatusResponse_body["id"] = self.id
        if self.status:
            contextStatusResponse_body["status"] = self.status.value

        return contextStatusResponse_query, contextStatusResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ContextStatusResponse":
        return cls(
            id=d.get("id", None),
            status=ContextStatus(d["status"]) if "status" in d else None,
        )


@dataclass
class CreateContext:

    # Running cluster id
    clusterId: str

    language: "Language"

    def as_request(self) -> (dict, dict):
        createContext_query, createContext_body = {}, {}
        if self.clusterId:
            createContext_body["clusterId"] = self.clusterId
        if self.language:
            createContext_body["language"] = self.language.value

        return createContext_query, createContext_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "CreateContext":
        return cls(
            clusterId=d.get("clusterId", None),
            language=Language(d["language"]) if "language" in d else None,
        )


@dataclass
class Created:

    id: str

    def as_request(self) -> (dict, dict):
        created_query, created_body = {}, {}
        if self.id:
            created_body["id"] = self.id

        return created_query, created_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "Created":
        return cls(
            id=d.get("id", None),
        )


@dataclass
class DestroyContext:

    clusterId: str

    contextId: str

    def as_request(self) -> (dict, dict):
        destroyContext_query, destroyContext_body = {}, {}
        if self.clusterId:
            destroyContext_body["clusterId"] = self.clusterId
        if self.contextId:
            destroyContext_body["contextId"] = self.contextId

        return destroyContext_query, destroyContext_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "DestroyContext":
        return cls(
            clusterId=d.get("clusterId", None),
            contextId=d.get("contextId", None),
        )


class Language(Enum):

    python = "python"
    scala = "scala"
    sql = "sql"


class ResultType(Enum):

    error = "error"
    image = "image"
    images = "images"
    table = "table"
    text = "text"


@dataclass
class Results:

    # The cause of the error
    cause: str

    data: Any
    # The image filename
    fileName: str

    fileNames: "List[str]"
    # true if a JSON schema is returned instead of a string representation of
    # the Hive type.
    isJsonSchema: bool
    # internal field used by SDK
    pos: int

    resultType: "ResultType"
    # The table schema
    schema: "List[any /* MISSING TYPE */]"
    # The summary of the error
    summary: str
    # true if partial results are returned.
    truncated: bool

    def as_request(self) -> (dict, dict):
        results_query, results_body = {}, {}
        if self.cause:
            results_body["cause"] = self.cause
        if self.data:
            results_body["data"] = self.data
        if self.fileName:
            results_body["fileName"] = self.fileName
        if self.fileNames:
            results_body["fileNames"] = [v for v in self.fileNames]
        if self.isJsonSchema:
            results_body["isJsonSchema"] = self.isJsonSchema
        if self.pos:
            results_body["pos"] = self.pos
        if self.resultType:
            results_body["resultType"] = self.resultType.value
        if self.schema:
            results_body["schema"] = [v for v in self.schema]
        if self.summary:
            results_body["summary"] = self.summary
        if self.truncated:
            results_body["truncated"] = self.truncated

        return results_query, results_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "Results":
        return cls(
            cause=d.get("cause", None),
            data=d.get("data", None),
            fileName=d.get("fileName", None),
            fileNames=d.get("fileNames", None),
            isJsonSchema=d.get("isJsonSchema", None),
            pos=d.get("pos", None),
            resultType=ResultType(d["resultType"]) if "resultType" in d else None,
            schema=d.get("schema", None),
            summary=d.get("summary", None),
            truncated=d.get("truncated", None),
        )


class CommandExecutionAPI:
    def __init__(self, api_client):
        self._api = api_client

    def cancel(self, request: CancelCommand):
        """Cancel a command.

        Cancels a currently running command within an execution context.

        The command ID is obtained from a prior successful call to __execute__."""
        query, body = request.as_request()
        self._api.do("POST", "/api/1.2/commands/cancel", query=query, body=body)

    def command_status(self, request: CommandStatusRequest) -> CommandStatusResponse:
        """Get command info.

        Gets the status of and, if available, the results from a currently
        executing command.

        The command ID is obtained from a prior successful call to __execute__."""
        query, body = request.as_request()
        json = self._api.do("GET", "/api/1.2/commands/status", query=query, body=body)
        return CommandStatusResponse.from_dict(json)

    def context_status(self, request: ContextStatusRequest) -> ContextStatusResponse:
        """Get status.

        Gets the status for an execution context."""
        query, body = request.as_request()
        json = self._api.do("GET", "/api/1.2/contexts/status", query=query, body=body)
        return ContextStatusResponse.from_dict(json)

    def create(self, request: CreateContext) -> Created:
        """Create an execution context.

        Creates an execution context for running cluster commands.

        If successful, this method returns the ID of the new execution context."""
        query, body = request.as_request()
        json = self._api.do("POST", "/api/1.2/contexts/create", query=query, body=body)
        return Created.from_dict(json)

    def destroy(self, request: DestroyContext):
        """Delete an execution context.

        Deletes an execution context."""
        query, body = request.as_request()
        self._api.do("POST", "/api/1.2/contexts/destroy", query=query, body=body)

    def execute(self, request: Command) -> Created:
        """Run a command.

        Runs a cluster command in the given execution context, using the
        provided language.

        If successful, it returns an ID for tracking the status of the command's
        execution."""
        query, body = request.as_request()
        json = self._api.do("POST", "/api/1.2/commands/execute", query=query, body=body)
        return Created.from_dict(json)
