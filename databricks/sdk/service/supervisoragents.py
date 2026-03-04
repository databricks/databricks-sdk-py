# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import Any, Dict, Iterator, List, Optional

from google.protobuf.timestamp_pb2 import Timestamp

from databricks.sdk.client_types import HostType
from databricks.sdk.common.types.fieldmask import FieldMask
from databricks.sdk.service._internal import _repeated_dict, _timestamp

_LOG = logging.getLogger("databricks.sdk")


# all definitions in this file are in alphabetical order


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

    create_time: Optional[Timestamp] = None
    """Create timestamp."""

    creator: Optional[str] = None
    """The creator of the Supervisor Agent."""

    endpoint_name: Optional[str] = None
    """The name of the supervisor agent endpoint."""

    experiment_id: Optional[str] = None
    """The MLflow experiment ID."""

    id: Optional[str] = None
    """The universally unique identifier (UUID) of the Supervisor Agent."""

    instructions: Optional[str] = None
    """Optional natural-language routing instructions for the supervisor agent."""

    name: Optional[str] = None
    """The resource name of the Supervisor Agent. Format: supervisor-agents/{supervisor_agent_id}"""

    tools: Optional[List[Tool]] = None

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
        if self.tools:
            body["tools"] = [v.as_dict() for v in self.tools]
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
        if self.tools:
            body["tools"] = self.tools
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
            tools=_repeated_dict(d, "tools", Tool),
        )


@dataclass
class SupervisorAgentListResponse:
    next_page_token: Optional[str] = None
    """A token that can be sent as `page_token` to retrieve the next page. If this field is omitted,
    there are no subsequent pages."""

    supervisor_agents: Optional[List[SupervisorAgent]] = None

    def as_dict(self) -> dict:
        """Serializes the SupervisorAgentListResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        if self.supervisor_agents:
            body["supervisor_agents"] = [v.as_dict() for v in self.supervisor_agents]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the SupervisorAgentListResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        if self.supervisor_agents:
            body["supervisor_agents"] = self.supervisor_agents
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> SupervisorAgentListResponse:
        """Deserializes the SupervisorAgentListResponse from a dictionary."""
        return cls(
            next_page_token=d.get("next_page_token", None),
            supervisor_agents=_repeated_dict(d, "supervisor_agents", SupervisorAgent),
        )


@dataclass
class Tool:
    """Tool is a Sub-resource of SupervisorAgent"""

    type: str

    id: str

    endpoint_name: str
    """The name of the serving endpoint."""

    name: str

    connection_name: str

    description: Optional[str] = None

    def as_dict(self) -> dict:
        """Serializes the Tool into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.connection_name is not None:
            body["connection_name"] = self.connection_name
        if self.description is not None:
            body["description"] = self.description
        if self.endpoint_name is not None:
            body["endpoint_name"] = self.endpoint_name
        if self.id is not None:
            body["id"] = self.id
        if self.name is not None:
            body["name"] = self.name
        if self.type is not None:
            body["type"] = self.type
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the Tool into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.connection_name is not None:
            body["connection_name"] = self.connection_name
        if self.description is not None:
            body["description"] = self.description
        if self.endpoint_name is not None:
            body["endpoint_name"] = self.endpoint_name
        if self.id is not None:
            body["id"] = self.id
        if self.name is not None:
            body["name"] = self.name
        if self.type is not None:
            body["type"] = self.type
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> Tool:
        """Deserializes the Tool from a dictionary."""
        return cls(
            connection_name=d.get("connection_name", None),
            description=d.get("description", None),
            endpoint_name=d.get("endpoint_name", None),
            id=d.get("id", None),
            name=d.get("name", None),
            type=d.get("type", None),
        )


class SupervisorAgentsAPI:
    """Manage Supervisor Agents and related resources."""

    def __init__(self, api_client):
        self._api = api_client

    def create_supervisor_agent(self, supervisor_agent: SupervisorAgent) -> SupervisorAgent:

        body = supervisor_agent.as_dict()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.host_type == HostType.UNIFIED and cfg.workspace_id:
            headers["X-Databricks-Org-Id"] = cfg.workspace_id

        res = self._api.do("POST", "/api/2.1/supervisor-agents", body=body, headers=headers)
        return SupervisorAgent.from_dict(res)

    def create_tool(self, parent: str, tool: Tool) -> Tool:
        """Creates a Tool under a Supervisor Agent.

        :param parent: str
          Parent resource where this tool will be created. Format: supervisor-agents/{supervisor_agent_id}
        :param tool: :class:`Tool`

        :returns: :class:`Tool`
        """

        body = tool.as_dict()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.host_type == HostType.UNIFIED and cfg.workspace_id:
            headers["X-Databricks-Org-Id"] = cfg.workspace_id

        res = self._api.do("POST", f"/api/2.1/{parent}/tools", body=body, headers=headers)
        return Tool.from_dict(res)

    def delete_supervisor_agent(self, name: str):

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.host_type == HostType.UNIFIED and cfg.workspace_id:
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
        if cfg.host_type == HostType.UNIFIED and cfg.workspace_id:
            headers["X-Databricks-Org-Id"] = cfg.workspace_id

        self._api.do("DELETE", f"/api/2.1/{name}", headers=headers)

    def get_supervisor_agent(self, name: str) -> SupervisorAgent:

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.host_type == HostType.UNIFIED and cfg.workspace_id:
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
        if cfg.host_type == HostType.UNIFIED and cfg.workspace_id:
            headers["X-Databricks-Org-Id"] = cfg.workspace_id

        res = self._api.do("GET", f"/api/2.1/{name}", headers=headers)
        return Tool.from_dict(res)

    def list_supervisor_agents(
        self, *, page_size: Optional[int] = None, page_token: Optional[str] = None
    ) -> Iterator[SupervisorAgent]:

        query = {}
        if page_size is not None:
            query["page_size"] = page_size
        if page_token is not None:
            query["page_token"] = page_token
        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.host_type == HostType.UNIFIED and cfg.workspace_id:
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
        if cfg.host_type == HostType.UNIFIED and cfg.workspace_id:
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

        body = supervisor_agent.as_dict()
        query = {}
        if update_mask is not None:
            query["update_mask"] = update_mask.ToJsonString()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.host_type == HostType.UNIFIED and cfg.workspace_id:
            headers["X-Databricks-Org-Id"] = cfg.workspace_id

        res = self._api.do("PATCH", f"/api/2.1/{name}", query=query, body=body, headers=headers)
        return SupervisorAgent.from_dict(res)

    def update_tool(self, name: str, tool: Tool, update_mask: FieldMask) -> Tool:
        """Updates a Tool.

        :param name: str
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
        if cfg.host_type == HostType.UNIFIED and cfg.workspace_id:
            headers["X-Databricks-Org-Id"] = cfg.workspace_id

        res = self._api.do("PATCH", f"/api/2.1/{name}", query=query, body=body, headers=headers)
        return Tool.from_dict(res)
