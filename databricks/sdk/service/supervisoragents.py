# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import Any, Dict, Iterator, List, Optional

from google.protobuf.timestamp_pb2 import Timestamp

from databricks.sdk.common.types.fieldmask import FieldMask
from databricks.sdk.service._internal import (_from_dict, _repeated_dict,
                                              _timestamp)

_LOG = logging.getLogger("databricks.sdk")


# all definitions in this file are in alphabetical order


@dataclass
class App:
    """Databricks app. Supported app: custom mcp, custom agent."""

    name: str
    """App name"""

    def as_dict(self) -> dict:
        """Serializes the App into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.name is not None:
            body["name"] = self.name
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the App into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.name is not None:
            body["name"] = self.name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> App:
        """Deserializes the App from a dictionary."""
        return cls(name=d.get("name", None))


@dataclass
class Connection:
    """Deprecated: Use UcConnection instead. Databricks connection. Supported connection: external mcp
    server."""

    name: Optional[str] = None

    def as_dict(self) -> dict:
        """Serializes the Connection into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.name is not None:
            body["name"] = self.name
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the Connection into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.name is not None:
            body["name"] = self.name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> Connection:
        """Deserializes the Connection from a dictionary."""
        return cls(name=d.get("name", None))


@dataclass
class GenieSpace:
    id: str
    """The ID of the genie space."""

    def as_dict(self) -> dict:
        """Serializes the GenieSpace into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.id is not None:
            body["id"] = self.id
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the GenieSpace into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.id is not None:
            body["id"] = self.id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> GenieSpace:
        """Deserializes the GenieSpace from a dictionary."""
        return cls(id=d.get("id", None))


@dataclass
class KnowledgeAssistant:
    knowledge_assistant_id: str
    """The ID of the knowledge assistant."""

    serving_endpoint_name: Optional[str] = None
    """Deprecated: use knowledge_assistant_id instead."""

    def as_dict(self) -> dict:
        """Serializes the KnowledgeAssistant into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.knowledge_assistant_id is not None:
            body["knowledge_assistant_id"] = self.knowledge_assistant_id
        if self.serving_endpoint_name is not None:
            body["serving_endpoint_name"] = self.serving_endpoint_name
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the KnowledgeAssistant into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.knowledge_assistant_id is not None:
            body["knowledge_assistant_id"] = self.knowledge_assistant_id
        if self.serving_endpoint_name is not None:
            body["serving_endpoint_name"] = self.serving_endpoint_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> KnowledgeAssistant:
        """Deserializes the KnowledgeAssistant from a dictionary."""
        return cls(
            knowledge_assistant_id=d.get("knowledge_assistant_id", None),
            serving_endpoint_name=d.get("serving_endpoint_name", None),
        )


@dataclass
class ListSupervisorAgentsResponse:
    next_page_token: Optional[str] = None
    """A token that can be sent as `page_token` to retrieve the next page. If this field is omitted,
    there are no subsequent pages."""

    supervisor_agents: Optional[List[SupervisorAgent]] = None

    def as_dict(self) -> dict:
        """Serializes the ListSupervisorAgentsResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        if self.supervisor_agents:
            body["supervisor_agents"] = [v.as_dict() for v in self.supervisor_agents]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ListSupervisorAgentsResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        if self.supervisor_agents:
            body["supervisor_agents"] = self.supervisor_agents
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ListSupervisorAgentsResponse:
        """Deserializes the ListSupervisorAgentsResponse from a dictionary."""
        return cls(
            next_page_token=d.get("next_page_token", None),
            supervisor_agents=_repeated_dict(d, "supervisor_agents", SupervisorAgent),
        )


@dataclass
class ListToolsResponse:
    next_page_token: Optional[str] = None

    tools: Optional[List[Tool]] = None

    def as_dict(self) -> dict:
        """Serializes the ListToolsResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        if self.tools:
            body["tools"] = [v.as_dict() for v in self.tools]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ListToolsResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        if self.tools:
            body["tools"] = self.tools
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ListToolsResponse:
        """Deserializes the ListToolsResponse from a dictionary."""
        return cls(next_page_token=d.get("next_page_token", None), tools=_repeated_dict(d, "tools", Tool))


@dataclass
class SupervisorAgent:
    display_name: str
    """The display name of the Supervisor Agent, unique at workspace level."""

    description: str
    """Description of what this agent can do (user-facing)."""

    create_time: Optional[Timestamp] = None
    """Creation timestamp."""

    creator: Optional[str] = None
    """The creator of the Supervisor Agent."""

    endpoint_name: Optional[str] = None
    """The name of the supervisor agent's serving endpoint."""

    experiment_id: Optional[str] = None
    """The MLflow experiment ID."""

    id: Optional[str] = None
    """Deprecated: Use supervisor_agent_id instead."""

    instructions: Optional[str] = None
    """Optional natural-language instructions for the supervisor agent."""

    name: Optional[str] = None
    """The resource name of the SupervisorAgent. Format: supervisor-agents/{supervisor_agent_id}"""

    supervisor_agent_id: Optional[str] = None
    """The universally unique identifier (UUID) of the Supervisor Agent."""

    def as_dict(self) -> dict:
        """Serializes the SupervisorAgent into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.create_time is not None:
            body["create_time"] = self.create_time.ToJsonString()
        if self.creator is not None:
            body["creator"] = self.creator
        if self.description is not None:
            body["description"] = self.description
        if self.display_name is not None:
            body["display_name"] = self.display_name
        if self.endpoint_name is not None:
            body["endpoint_name"] = self.endpoint_name
        if self.experiment_id is not None:
            body["experiment_id"] = self.experiment_id
        if self.id is not None:
            body["id"] = self.id
        if self.instructions is not None:
            body["instructions"] = self.instructions
        if self.name is not None:
            body["name"] = self.name
        if self.supervisor_agent_id is not None:
            body["supervisor_agent_id"] = self.supervisor_agent_id
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the SupervisorAgent into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.create_time is not None:
            body["create_time"] = self.create_time
        if self.creator is not None:
            body["creator"] = self.creator
        if self.description is not None:
            body["description"] = self.description
        if self.display_name is not None:
            body["display_name"] = self.display_name
        if self.endpoint_name is not None:
            body["endpoint_name"] = self.endpoint_name
        if self.experiment_id is not None:
            body["experiment_id"] = self.experiment_id
        if self.id is not None:
            body["id"] = self.id
        if self.instructions is not None:
            body["instructions"] = self.instructions
        if self.name is not None:
            body["name"] = self.name
        if self.supervisor_agent_id is not None:
            body["supervisor_agent_id"] = self.supervisor_agent_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> SupervisorAgent:
        """Deserializes the SupervisorAgent from a dictionary."""
        return cls(
            create_time=_timestamp(d, "create_time"),
            creator=d.get("creator", None),
            description=d.get("description", None),
            display_name=d.get("display_name", None),
            endpoint_name=d.get("endpoint_name", None),
            experiment_id=d.get("experiment_id", None),
            id=d.get("id", None),
            instructions=d.get("instructions", None),
            name=d.get("name", None),
            supervisor_agent_id=d.get("supervisor_agent_id", None),
        )


@dataclass
class Tool:
    tool_type: str
    """Tool type. Must be one of: "genie_space", "knowledge_assistant", "uc_function", "uc_connection",
    "app", "volume", "lakeview_dashboard", "serving_endpoint", "uc_table", "vector_search_index"."""

    description: str
    """Description of what this tool does (user-facing)."""

    app: Optional[App] = None

    connection: Optional[Connection] = None
    """Deprecated: Use uc_connection instead."""

    genie_space: Optional[GenieSpace] = None

    id: Optional[str] = None
    """Deprecated: Use tool_id instead."""

    knowledge_assistant: Optional[KnowledgeAssistant] = None

    name: Optional[str] = None
    """Full resource name: supervisor-agents/{supervisor_agent_id}/tools/{tool_id}"""

    tool_id: Optional[str] = None
    """User specified id of the Tool."""

    uc_connection: Optional[UcConnection] = None

    uc_function: Optional[UcFunction] = None

    volume: Optional[Volume] = None

    def as_dict(self) -> dict:
        """Serializes the Tool into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.app:
            body["app"] = self.app.as_dict()
        if self.connection:
            body["connection"] = self.connection.as_dict()
        if self.description is not None:
            body["description"] = self.description
        if self.genie_space:
            body["genie_space"] = self.genie_space.as_dict()
        if self.id is not None:
            body["id"] = self.id
        if self.knowledge_assistant:
            body["knowledge_assistant"] = self.knowledge_assistant.as_dict()
        if self.name is not None:
            body["name"] = self.name
        if self.tool_id is not None:
            body["tool_id"] = self.tool_id
        if self.tool_type is not None:
            body["tool_type"] = self.tool_type
        if self.uc_connection:
            body["uc_connection"] = self.uc_connection.as_dict()
        if self.uc_function:
            body["uc_function"] = self.uc_function.as_dict()
        if self.volume:
            body["volume"] = self.volume.as_dict()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the Tool into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.app:
            body["app"] = self.app
        if self.connection:
            body["connection"] = self.connection
        if self.description is not None:
            body["description"] = self.description
        if self.genie_space:
            body["genie_space"] = self.genie_space
        if self.id is not None:
            body["id"] = self.id
        if self.knowledge_assistant:
            body["knowledge_assistant"] = self.knowledge_assistant
        if self.name is not None:
            body["name"] = self.name
        if self.tool_id is not None:
            body["tool_id"] = self.tool_id
        if self.tool_type is not None:
            body["tool_type"] = self.tool_type
        if self.uc_connection:
            body["uc_connection"] = self.uc_connection
        if self.uc_function:
            body["uc_function"] = self.uc_function
        if self.volume:
            body["volume"] = self.volume
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> Tool:
        """Deserializes the Tool from a dictionary."""
        return cls(
            app=_from_dict(d, "app", App),
            connection=_from_dict(d, "connection", Connection),
            description=d.get("description", None),
            genie_space=_from_dict(d, "genie_space", GenieSpace),
            id=d.get("id", None),
            knowledge_assistant=_from_dict(d, "knowledge_assistant", KnowledgeAssistant),
            name=d.get("name", None),
            tool_id=d.get("tool_id", None),
            tool_type=d.get("tool_type", None),
            uc_connection=_from_dict(d, "uc_connection", UcConnection),
            uc_function=_from_dict(d, "uc_function", UcFunction),
            volume=_from_dict(d, "volume", Volume),
        )


@dataclass
class UcConnection:
    """Databricks UC connection. Supported connection: external mcp server."""

    name: str

    def as_dict(self) -> dict:
        """Serializes the UcConnection into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.name is not None:
            body["name"] = self.name
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the UcConnection into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.name is not None:
            body["name"] = self.name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> UcConnection:
        """Deserializes the UcConnection from a dictionary."""
        return cls(name=d.get("name", None))


@dataclass
class UcFunction:
    name: str
    """Full uc function name"""

    def as_dict(self) -> dict:
        """Serializes the UcFunction into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.name is not None:
            body["name"] = self.name
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the UcFunction into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.name is not None:
            body["name"] = self.name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> UcFunction:
        """Deserializes the UcFunction from a dictionary."""
        return cls(name=d.get("name", None))


@dataclass
class Volume:
    name: str
    """Full uc volume name"""

    def as_dict(self) -> dict:
        """Serializes the Volume into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.name is not None:
            body["name"] = self.name
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the Volume into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.name is not None:
            body["name"] = self.name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> Volume:
        """Deserializes the Volume from a dictionary."""
        return cls(name=d.get("name", None))


class SupervisorAgentsAPI:
    """Manage Supervisor Agents and related resources."""

    def __init__(self, api_client):
        self._api = api_client

    def create_supervisor_agent(self, supervisor_agent: SupervisorAgent) -> SupervisorAgent:
        """Creates a new Supervisor Agent.

        :param supervisor_agent: :class:`SupervisorAgent`
          The Supervisor Agent to create.

        :returns: :class:`SupervisorAgent`
        """

        body = supervisor_agent.as_dict()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Org-Id"] = cfg.workspace_id

        res = self._api.do("POST", "/api/2.1/supervisor-agents", body=body, headers=headers)
        return SupervisorAgent.from_dict(res)

    def create_tool(self, parent: str, tool: Tool, tool_id: str) -> Tool:
        """Creates a Tool under a Supervisor Agent. Specify one of "genie_space", "knowledge_assistant",
        "uc_function", "uc_connection", "app", "volume", "lakeview_dashboard", "uc_table",
        "vector_search_index" in the request body.

        :param parent: str
          Parent resource where this tool will be created. Format: supervisor-agents/{supervisor_agent_id}
        :param tool: :class:`Tool`
        :param tool_id: str
          The ID to use for the tool, which will become the final component of the tool's resource name.

        :returns: :class:`Tool`
        """

        body = tool.as_dict()
        query = {}
        if tool_id is not None:
            query["tool_id"] = tool_id
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Org-Id"] = cfg.workspace_id

        res = self._api.do("POST", f"/api/2.1/{parent}/tools", query=query, body=body, headers=headers)
        return Tool.from_dict(res)

    def delete_supervisor_agent(self, name: str):
        """Deletes a Supervisor Agent.

        :param name: str
          The resource name of the Supervisor Agent. Format: supervisor-agents/{supervisor_agent_id}


        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Org-Id"] = cfg.workspace_id

        self._api.do("DELETE", f"/api/2.1/{name}", headers=headers)

    def delete_tool(self, name: str):
        """Deletes a Tool.

        :param name: str
          The resource name of the Tool. Format: supervisor-agents/{supervisor_agent_id}/tools/{tool_id}


        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Org-Id"] = cfg.workspace_id

        self._api.do("DELETE", f"/api/2.1/{name}", headers=headers)

    def get_supervisor_agent(self, name: str) -> SupervisorAgent:
        """Gets a Supervisor Agent.

        :param name: str
          The resource name of the Supervisor Agent. Format: supervisor-agents/{supervisor_agent_id}

        :returns: :class:`SupervisorAgent`
        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Org-Id"] = cfg.workspace_id

        res = self._api.do("GET", f"/api/2.1/{name}", headers=headers)
        return SupervisorAgent.from_dict(res)

    def get_tool(self, name: str) -> Tool:
        """Gets a Tool.

        :param name: str
          The resource name of the Tool. Format: supervisor-agents/{supervisor_agent_id}/tools/{tool_id}

        :returns: :class:`Tool`
        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Org-Id"] = cfg.workspace_id

        res = self._api.do("GET", f"/api/2.1/{name}", headers=headers)
        return Tool.from_dict(res)

    def list_supervisor_agents(
        self, *, page_size: Optional[int] = None, page_token: Optional[str] = None
    ) -> Iterator[SupervisorAgent]:
        """Lists Supervisor Agents.

        :param page_size: int (optional)
          The maximum number of supervisor agents to return. If unspecified, at most 100 supervisor agents
          will be returned. The maximum value is 100; values above 100 will be coerced to 100.
        :param page_token: str (optional)
          A page token, received from a previous `ListSupervisorAgents` call. Provide this to retrieve the
          subsequent page. If unspecified, the first page will be returned.

        :returns: Iterator over :class:`SupervisorAgent`
        """

        query = {}
        if page_size is not None:
            query["page_size"] = page_size
        if page_token is not None:
            query["page_token"] = page_token
        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Org-Id"] = cfg.workspace_id

        while True:
            json = self._api.do("GET", "/api/2.1/supervisor-agents", query=query, headers=headers)
            if "supervisor_agents" in json:
                for v in json["supervisor_agents"]:
                    yield SupervisorAgent.from_dict(v)
            if "next_page_token" not in json or not json["next_page_token"]:
                return
            query["page_token"] = json["next_page_token"]

    def list_tools(
        self, parent: str, *, page_size: Optional[int] = None, page_token: Optional[str] = None
    ) -> Iterator[Tool]:
        """Lists Tools under a Supervisor Agent.

        :param parent: str
          Parent resource to list from. Format: supervisor-agents/{supervisor_agent_id}
        :param page_size: int (optional)
        :param page_token: str (optional)

        :returns: Iterator over :class:`Tool`
        """

        query = {}
        if page_size is not None:
            query["page_size"] = page_size
        if page_token is not None:
            query["page_token"] = page_token
        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Org-Id"] = cfg.workspace_id

        while True:
            json = self._api.do("GET", f"/api/2.1/{parent}/tools", query=query, headers=headers)
            if "tools" in json:
                for v in json["tools"]:
                    yield Tool.from_dict(v)
            if "next_page_token" not in json or not json["next_page_token"]:
                return
            query["page_token"] = json["next_page_token"]

    def update_supervisor_agent(
        self, name: str, supervisor_agent: SupervisorAgent, update_mask: FieldMask
    ) -> SupervisorAgent:
        """Updates a Supervisor Agent. The fields that are required depend on the paths specified in
        `update_mask`. Only fields included in the mask will be updated.

        :param name: str
          The resource name of the SupervisorAgent. Format: supervisor-agents/{supervisor_agent_id}
        :param supervisor_agent: :class:`SupervisorAgent`
          The SupervisorAgent to update.
        :param update_mask: FieldMask
          Field mask for fields to be updated.

        :returns: :class:`SupervisorAgent`
        """

        body = supervisor_agent.as_dict()
        query = {}
        if update_mask is not None:
            query["update_mask"] = update_mask.ToJsonString()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Org-Id"] = cfg.workspace_id

        res = self._api.do("PATCH", f"/api/2.1/{name}", query=query, body=body, headers=headers)
        return SupervisorAgent.from_dict(res)

    def update_tool(self, name: str, tool: Tool, update_mask: FieldMask) -> Tool:
        """Updates a Tool. Only the `description` field can be updated. To change immutable fields such as tool
        type, spec, or tool ID, delete the tool and recreate it.

        :param name: str
          Full resource name: supervisor-agents/{supervisor_agent_id}/tools/{tool_id}
        :param tool: :class:`Tool`
          The Tool to update.
        :param update_mask: FieldMask
          Field mask for fields to be updated.

        :returns: :class:`Tool`
        """

        body = tool.as_dict()
        query = {}
        if update_mask is not None:
            query["update_mask"] = update_mask.ToJsonString()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Org-Id"] = cfg.workspace_id

        res = self._api.do("PATCH", f"/api/2.1/{name}", query=query, body=body, headers=headers)
        return Tool.from_dict(res)
