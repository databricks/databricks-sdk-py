# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.
# ruff: noqa: F811, F841
# F401 is intentionally NOT covered: `make fmt` uses `ruff check --fix-only`
# to strip the fat-import header below; ignoring F401 would defeat that.

from __future__ import annotations
from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Any, Iterator, Optional

from google.protobuf.timestamp_pb2 import Timestamp

import logging

from databricks.sdk.service._internal import (
    _enum,
    _from_dict,
    _repeated_dict,
    _timestamp,
)
from databricks.sdk.common.types.fieldmask import FieldMask


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
class Catalog:
    """UC catalog asset_search scope. One tool authorizes asset_search over one catalog. Multiple
    catalog tools widen the scope; the backend merges them into a single CATALOG entry in
    asset_search's scoped_assets."""

    name: str
    """Bare UC catalog name this tool is authorized to search (no ``.``)."""

    def as_dict(self) -> dict:
        """Serializes the Catalog into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.name is not None:
            body["name"] = self.name
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the Catalog into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.name is not None:
            body["name"] = self.name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> Catalog:
        """Deserializes the Catalog from a dictionary."""
        return cls(name=d.get("name", None))


@dataclass
class Example:
    """An example associated with a Supervisor Agent. Contains a question and guidelines for how the
    agent should respond."""

    question: str
    """The example question."""

    guidelines: List[str]
    """Guidelines for answering the question."""

    example_id: Optional[str] = None
    """The universally unique identifier (UUID) of the example."""

    name: Optional[str] = None
    """Full resource name: supervisor-agents/{supervisor_agent_id}/examples/{example_id}"""

    def as_dict(self) -> dict:
        """Serializes the Example into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.example_id is not None:
            body["example_id"] = self.example_id
        if self.guidelines:
            body["guidelines"] = [v for v in self.guidelines]
        if self.name is not None:
            body["name"] = self.name
        if self.question is not None:
            body["question"] = self.question
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the Example into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.example_id is not None:
            body["example_id"] = self.example_id
        if self.guidelines:
            body["guidelines"] = self.guidelines
        if self.name is not None:
            body["name"] = self.name
        if self.question is not None:
            body["question"] = self.question
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> Example:
        """Deserializes the Example from a dictionary."""
        return cls(
            example_id=d.get("example_id", None),
            guidelines=d.get("guidelines", None),
            name=d.get("name", None),
            question=d.get("question", None),
        )


@dataclass
class GenieSpace:
    id: str
    """Deprecated: use space_id instead. Still REQUIRED for backward compatibility until a future API
    version removes it."""

    space_id: Optional[str] = None
    """The ID of the genie space."""

    def as_dict(self) -> dict:
        """Serializes the GenieSpace into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.id is not None:
            body["id"] = self.id
        if self.space_id is not None:
            body["space_id"] = self.space_id
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the GenieSpace into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.id is not None:
            body["id"] = self.id
        if self.space_id is not None:
            body["space_id"] = self.space_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> GenieSpace:
        """Deserializes the GenieSpace from a dictionary."""
        return cls(id=d.get("id", None), space_id=d.get("space_id", None))


@dataclass
class GetSupervisorAgentPermissionLevelsResponse:
    permission_levels: Optional[List[SupervisorAgentPermissionsDescription]] = None
    """Specific permission levels"""

    def as_dict(self) -> dict:
        """Serializes the GetSupervisorAgentPermissionLevelsResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.permission_levels:
            body["permission_levels"] = [v.as_dict() for v in self.permission_levels]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the GetSupervisorAgentPermissionLevelsResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.permission_levels:
            body["permission_levels"] = self.permission_levels
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> GetSupervisorAgentPermissionLevelsResponse:
        """Deserializes the GetSupervisorAgentPermissionLevelsResponse from a dictionary."""
        return cls(permission_levels=_repeated_dict(d, "permission_levels", SupervisorAgentPermissionsDescription))


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
class LakeviewDashboard:
    """Lakeview Dashboard tool scoped to a specific published dashboard."""

    dashboard_id: str
    """The unique identifier of the Lakeview dashboard."""

    def as_dict(self) -> dict:
        """Serializes the LakeviewDashboard into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.dashboard_id is not None:
            body["dashboard_id"] = self.dashboard_id
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the LakeviewDashboard into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.dashboard_id is not None:
            body["dashboard_id"] = self.dashboard_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> LakeviewDashboard:
        """Deserializes the LakeviewDashboard from a dictionary."""
        return cls(dashboard_id=d.get("dashboard_id", None))


@dataclass
class ListExamplesResponse:
    """A list of Supervisor Agent examples."""

    examples: Optional[List[Example]] = None

    next_page_token: Optional[str] = None

    def as_dict(self) -> dict:
        """Serializes the ListExamplesResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.examples:
            body["examples"] = [v.as_dict() for v in self.examples]
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ListExamplesResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.examples:
            body["examples"] = self.examples
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ListExamplesResponse:
        """Deserializes the ListExamplesResponse from a dictionary."""
        return cls(examples=_repeated_dict(d, "examples", Example), next_page_token=d.get("next_page_token", None))


@dataclass
class ListSupervisorAgentsResponse:
    next_page_token: Optional[str] = None
    """A token that can be sent as ``page_token`` to retrieve the next page. If this field is omitted,
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
class Schema:
    """UC schema asset_search scope. One tool authorizes asset_search over one schema. Multiple schema
    tools widen the scope."""

    name: str
    """Full UC schema name (catalog.schema) this tool is authorized to search."""

    def as_dict(self) -> dict:
        """Serializes the Schema into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.name is not None:
            body["name"] = self.name
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the Schema into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.name is not None:
            body["name"] = self.name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> Schema:
        """Deserializes the Schema from a dictionary."""
        return cls(name=d.get("name", None))


@dataclass
class ServingEndpoint:
    name: str

    def as_dict(self) -> dict:
        """Serializes the ServingEndpoint into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.name is not None:
            body["name"] = self.name
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ServingEndpoint into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.name is not None:
            body["name"] = self.name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ServingEndpoint:
        """Deserializes the ServingEndpoint from a dictionary."""
        return cls(name=d.get("name", None))


@dataclass
class Skill:
    """Skill tool. Points to a folder containing skill subdirectories with SKILL.md files (YAML
    frontmatter with name + description, followed by markdown instructions). Skills are discovered
    from the folder at runtime and loaded on demand via a read_skill tool registered by the
    supervisor."""

    path: str
    """Absolute WSFS path to a folder containing skill subdirectories. Example:
    /Workspace/Users/creator@company.com/.assistant/skills"""

    def as_dict(self) -> dict:
        """Serializes the Skill into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.path is not None:
            body["path"] = self.path
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the Skill into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.path is not None:
            body["path"] = self.path
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> Skill:
        """Deserializes the Skill from a dictionary."""
        return cls(path=d.get("path", None))


@dataclass
class SupervisorAgent:
    display_name: str
    """The display name of the Supervisor Agent, unique at workspace level."""

    create_time: Optional[Timestamp] = None
    """Creation timestamp."""

    creator: Optional[str] = None
    """The creator of the Supervisor Agent."""

    description: Optional[str] = None
    """Description of what this agent can do (user-facing)."""

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
class SupervisorAgentAccessControlRequest:
    group_name: Optional[str] = None
    """name of the group"""

    permission_level: Optional[SupervisorAgentPermissionLevel] = None

    service_principal_name: Optional[str] = None
    """application ID of a service principal"""

    user_name: Optional[str] = None
    """name of the user"""

    def as_dict(self) -> dict:
        """Serializes the SupervisorAgentAccessControlRequest into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.group_name is not None:
            body["group_name"] = self.group_name
        if self.permission_level is not None:
            body["permission_level"] = self.permission_level.value
        if self.service_principal_name is not None:
            body["service_principal_name"] = self.service_principal_name
        if self.user_name is not None:
            body["user_name"] = self.user_name
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the SupervisorAgentAccessControlRequest into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.group_name is not None:
            body["group_name"] = self.group_name
        if self.permission_level is not None:
            body["permission_level"] = self.permission_level
        if self.service_principal_name is not None:
            body["service_principal_name"] = self.service_principal_name
        if self.user_name is not None:
            body["user_name"] = self.user_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> SupervisorAgentAccessControlRequest:
        """Deserializes the SupervisorAgentAccessControlRequest from a dictionary."""
        return cls(
            group_name=d.get("group_name", None),
            permission_level=_enum(d, "permission_level", SupervisorAgentPermissionLevel),
            service_principal_name=d.get("service_principal_name", None),
            user_name=d.get("user_name", None),
        )


@dataclass
class SupervisorAgentAccessControlResponse:
    all_permissions: Optional[List[SupervisorAgentPermission]] = None
    """All permissions."""

    display_name: Optional[str] = None
    """Display name of the user or service principal."""

    group_name: Optional[str] = None
    """name of the group"""

    service_principal_name: Optional[str] = None
    """Name of the service principal."""

    user_name: Optional[str] = None
    """name of the user"""

    def as_dict(self) -> dict:
        """Serializes the SupervisorAgentAccessControlResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.all_permissions:
            body["all_permissions"] = [v.as_dict() for v in self.all_permissions]
        if self.display_name is not None:
            body["display_name"] = self.display_name
        if self.group_name is not None:
            body["group_name"] = self.group_name
        if self.service_principal_name is not None:
            body["service_principal_name"] = self.service_principal_name
        if self.user_name is not None:
            body["user_name"] = self.user_name
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the SupervisorAgentAccessControlResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.all_permissions:
            body["all_permissions"] = self.all_permissions
        if self.display_name is not None:
            body["display_name"] = self.display_name
        if self.group_name is not None:
            body["group_name"] = self.group_name
        if self.service_principal_name is not None:
            body["service_principal_name"] = self.service_principal_name
        if self.user_name is not None:
            body["user_name"] = self.user_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> SupervisorAgentAccessControlResponse:
        """Deserializes the SupervisorAgentAccessControlResponse from a dictionary."""
        return cls(
            all_permissions=_repeated_dict(d, "all_permissions", SupervisorAgentPermission),
            display_name=d.get("display_name", None),
            group_name=d.get("group_name", None),
            service_principal_name=d.get("service_principal_name", None),
            user_name=d.get("user_name", None),
        )


@dataclass
class SupervisorAgentPermission:
    inherited: Optional[bool] = None

    inherited_from_object: Optional[List[str]] = None

    permission_level: Optional[SupervisorAgentPermissionLevel] = None

    def as_dict(self) -> dict:
        """Serializes the SupervisorAgentPermission into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.inherited is not None:
            body["inherited"] = self.inherited
        if self.inherited_from_object:
            body["inherited_from_object"] = [v for v in self.inherited_from_object]
        if self.permission_level is not None:
            body["permission_level"] = self.permission_level.value
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the SupervisorAgentPermission into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.inherited is not None:
            body["inherited"] = self.inherited
        if self.inherited_from_object:
            body["inherited_from_object"] = self.inherited_from_object
        if self.permission_level is not None:
            body["permission_level"] = self.permission_level
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> SupervisorAgentPermission:
        """Deserializes the SupervisorAgentPermission from a dictionary."""
        return cls(
            inherited=d.get("inherited", None),
            inherited_from_object=d.get("inherited_from_object", None),
            permission_level=_enum(d, "permission_level", SupervisorAgentPermissionLevel),
        )


class SupervisorAgentPermissionLevel(Enum):
    """Permission level"""

    CAN_MANAGE = "CAN_MANAGE"
    CAN_QUERY = "CAN_QUERY"


@dataclass
class SupervisorAgentPermissions:
    access_control_list: Optional[List[SupervisorAgentAccessControlResponse]] = None

    object_id: Optional[str] = None

    object_type: Optional[str] = None

    def as_dict(self) -> dict:
        """Serializes the SupervisorAgentPermissions into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.access_control_list:
            body["access_control_list"] = [v.as_dict() for v in self.access_control_list]
        if self.object_id is not None:
            body["object_id"] = self.object_id
        if self.object_type is not None:
            body["object_type"] = self.object_type
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the SupervisorAgentPermissions into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.access_control_list:
            body["access_control_list"] = self.access_control_list
        if self.object_id is not None:
            body["object_id"] = self.object_id
        if self.object_type is not None:
            body["object_type"] = self.object_type
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> SupervisorAgentPermissions:
        """Deserializes the SupervisorAgentPermissions from a dictionary."""
        return cls(
            access_control_list=_repeated_dict(d, "access_control_list", SupervisorAgentAccessControlResponse),
            object_id=d.get("object_id", None),
            object_type=d.get("object_type", None),
        )


@dataclass
class SupervisorAgentPermissionsDescription:
    description: Optional[str] = None

    permission_level: Optional[SupervisorAgentPermissionLevel] = None

    def as_dict(self) -> dict:
        """Serializes the SupervisorAgentPermissionsDescription into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.description is not None:
            body["description"] = self.description
        if self.permission_level is not None:
            body["permission_level"] = self.permission_level.value
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the SupervisorAgentPermissionsDescription into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.description is not None:
            body["description"] = self.description
        if self.permission_level is not None:
            body["permission_level"] = self.permission_level
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> SupervisorAgentPermissionsDescription:
        """Deserializes the SupervisorAgentPermissionsDescription from a dictionary."""
        return cls(
            description=d.get("description", None),
            permission_level=_enum(d, "permission_level", SupervisorAgentPermissionLevel),
        )


@dataclass
class SupervisorAgentTool:
    """Nested Supervisor Agent tool."""

    supervisor_agent_id: str
    """The ID of the supervisor agent (tile ID)."""

    def as_dict(self) -> dict:
        """Serializes the SupervisorAgentTool into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.supervisor_agent_id is not None:
            body["supervisor_agent_id"] = self.supervisor_agent_id
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the SupervisorAgentTool into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.supervisor_agent_id is not None:
            body["supervisor_agent_id"] = self.supervisor_agent_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> SupervisorAgentTool:
        """Deserializes the SupervisorAgentTool from a dictionary."""
        return cls(supervisor_agent_id=d.get("supervisor_agent_id", None))


@dataclass
class Tool:
    tool_type: str
    """Tool type. Must be one of: "genie_space", "knowledge_assistant", "uc_function", "uc_connection",
    "uc_mcp", "app", "volume", "dashboard", "serving_endpoint", "table", "vector_search_index",
    "catalog", "schema", "supervisor_agent", "databricks_web_search", "skill". The legacy values
    "lakeview_dashboard", "uc_table", and "web_search" are also accepted and remain equivalent to
    "dashboard", "table", and "databricks_web_search" respectively. The "databricks_web_search"
    tool_type maps to the ``web_search`` spec field."""

    app: Optional[App] = None

    catalog: Optional[Catalog] = None
    """Configuration for a UC catalog asset_search scope tool."""

    dashboard: Optional[LakeviewDashboard] = None
    """Lakeview dashboard tool. Replaces the deprecated ``lakeview_dashboard`` field."""

    description: Optional[str] = None
    """Description of what this tool does (user-facing)."""

    genie_space: Optional[GenieSpace] = None

    id: Optional[str] = None
    """Deprecated: Use tool_id instead."""

    knowledge_assistant: Optional[KnowledgeAssistant] = None

    lakeview_dashboard: Optional[LakeviewDashboard] = None
    """Deprecated: use ``dashboard`` instead."""

    name: Optional[str] = None
    """Full resource name: supervisor-agents/{supervisor_agent_id}/tools/{tool_id}"""

    schema: Optional[Schema] = None
    """Configuration for a UC schema asset_search scope tool."""

    serving_endpoint: Optional[ServingEndpoint] = None

    skill: Optional[Skill] = None
    """Skill tool. Points to a folder containing skill subdirectories with SKILL.md files. Skills are
    discovered from the folder at runtime and loaded on demand via a read_skill tool."""

    supervisor_agent: Optional[SupervisorAgentTool] = None

    table: Optional[UcTable] = None
    """Unity Catalog table tool. Replaces the deprecated ``uc_table`` field."""

    tool_id: Optional[str] = None
    """User specified id of the Tool."""

    uc_connection: Optional[UcConnection] = None

    uc_function: Optional[UcFunction] = None

    uc_mcp: Optional[UcMcpService] = None
    """UC-registered MCP service tool. The ``name`` field on UcMcpService is the three-level UC FQN
    (catalog.schema.mcp_service); the supervisor resolves it at request build time, calls
    ``tools/list`` against the AI Gateway mcp-services proxy, and dynamically registers every
    discovered MCP sub-tool as a separately-callable tool."""

    uc_table: Optional[UcTable] = None
    """Deprecated: use ``table`` instead."""

    vector_search_index: Optional[VectorSearchIndex] = None
    """Configuration for a Vector Search index tool."""

    volume: Optional[Volume] = None

    web_search: Optional[WebSearch] = None
    """Configuration for a public-web search tool. The supervisor collapses multiple web_search tools
    on the same agent into a single registered ``web_search`` tool at runtime."""

    def as_dict(self) -> dict:
        """Serializes the Tool into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.app:
            body["app"] = self.app.as_dict()
        if self.catalog:
            body["catalog"] = self.catalog.as_dict()
        if self.dashboard:
            body["dashboard"] = self.dashboard.as_dict()
        if self.description is not None:
            body["description"] = self.description
        if self.genie_space:
            body["genie_space"] = self.genie_space.as_dict()
        if self.id is not None:
            body["id"] = self.id
        if self.knowledge_assistant:
            body["knowledge_assistant"] = self.knowledge_assistant.as_dict()
        if self.lakeview_dashboard:
            body["lakeview_dashboard"] = self.lakeview_dashboard.as_dict()
        if self.name is not None:
            body["name"] = self.name
        if self.schema:
            body["schema"] = self.schema.as_dict()
        if self.serving_endpoint:
            body["serving_endpoint"] = self.serving_endpoint.as_dict()
        if self.skill:
            body["skill"] = self.skill.as_dict()
        if self.supervisor_agent:
            body["supervisor_agent"] = self.supervisor_agent.as_dict()
        if self.table:
            body["table"] = self.table.as_dict()
        if self.tool_id is not None:
            body["tool_id"] = self.tool_id
        if self.tool_type is not None:
            body["tool_type"] = self.tool_type
        if self.uc_connection:
            body["uc_connection"] = self.uc_connection.as_dict()
        if self.uc_function:
            body["uc_function"] = self.uc_function.as_dict()
        if self.uc_mcp:
            body["uc_mcp"] = self.uc_mcp.as_dict()
        if self.uc_table:
            body["uc_table"] = self.uc_table.as_dict()
        if self.vector_search_index:
            body["vector_search_index"] = self.vector_search_index.as_dict()
        if self.volume:
            body["volume"] = self.volume.as_dict()
        if self.web_search:
            body["web_search"] = self.web_search.as_dict()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the Tool into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.app:
            body["app"] = self.app
        if self.catalog:
            body["catalog"] = self.catalog
        if self.dashboard:
            body["dashboard"] = self.dashboard
        if self.description is not None:
            body["description"] = self.description
        if self.genie_space:
            body["genie_space"] = self.genie_space
        if self.id is not None:
            body["id"] = self.id
        if self.knowledge_assistant:
            body["knowledge_assistant"] = self.knowledge_assistant
        if self.lakeview_dashboard:
            body["lakeview_dashboard"] = self.lakeview_dashboard
        if self.name is not None:
            body["name"] = self.name
        if self.schema:
            body["schema"] = self.schema
        if self.serving_endpoint:
            body["serving_endpoint"] = self.serving_endpoint
        if self.skill:
            body["skill"] = self.skill
        if self.supervisor_agent:
            body["supervisor_agent"] = self.supervisor_agent
        if self.table:
            body["table"] = self.table
        if self.tool_id is not None:
            body["tool_id"] = self.tool_id
        if self.tool_type is not None:
            body["tool_type"] = self.tool_type
        if self.uc_connection:
            body["uc_connection"] = self.uc_connection
        if self.uc_function:
            body["uc_function"] = self.uc_function
        if self.uc_mcp:
            body["uc_mcp"] = self.uc_mcp
        if self.uc_table:
            body["uc_table"] = self.uc_table
        if self.vector_search_index:
            body["vector_search_index"] = self.vector_search_index
        if self.volume:
            body["volume"] = self.volume
        if self.web_search:
            body["web_search"] = self.web_search
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> Tool:
        """Deserializes the Tool from a dictionary."""
        return cls(
            app=_from_dict(d, "app", App),
            catalog=_from_dict(d, "catalog", Catalog),
            dashboard=_from_dict(d, "dashboard", LakeviewDashboard),
            description=d.get("description", None),
            genie_space=_from_dict(d, "genie_space", GenieSpace),
            id=d.get("id", None),
            knowledge_assistant=_from_dict(d, "knowledge_assistant", KnowledgeAssistant),
            lakeview_dashboard=_from_dict(d, "lakeview_dashboard", LakeviewDashboard),
            name=d.get("name", None),
            schema=_from_dict(d, "schema", Schema),
            serving_endpoint=_from_dict(d, "serving_endpoint", ServingEndpoint),
            skill=_from_dict(d, "skill", Skill),
            supervisor_agent=_from_dict(d, "supervisor_agent", SupervisorAgentTool),
            table=_from_dict(d, "table", UcTable),
            tool_id=d.get("tool_id", None),
            tool_type=d.get("tool_type", None),
            uc_connection=_from_dict(d, "uc_connection", UcConnection),
            uc_function=_from_dict(d, "uc_function", UcFunction),
            uc_mcp=_from_dict(d, "uc_mcp", UcMcpService),
            uc_table=_from_dict(d, "uc_table", UcTable),
            vector_search_index=_from_dict(d, "vector_search_index", VectorSearchIndex),
            volume=_from_dict(d, "volume", Volume),
            web_search=_from_dict(d, "web_search", WebSearch),
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
class UcMcpService:
    """UC-registered MCP service tool. The ``name`` field is the three-level UC FQN of the MCP service
    (``catalog.schema.mcp_service``). At request build time the supervisor calls ``tools/list``
    against the AI Gateway mcp-services proxy and dynamically registers every discovered MCP
    sub-tool as a separately-callable tool. Per-sub-tool config is not stored here — discovery is
    dynamic so newly published MCP functions are picked up without redeploying the agent."""

    name: str
    """Three-level UC FQN of the registered MCP service (catalog.schema.mcp_service)."""

    def as_dict(self) -> dict:
        """Serializes the UcMcpService into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.name is not None:
            body["name"] = self.name
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the UcMcpService into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.name is not None:
            body["name"] = self.name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> UcMcpService:
        """Deserializes the UcMcpService from a dictionary."""
        return cls(name=d.get("name", None))


@dataclass
class UcTable:
    """Unity Catalog table. One tool represents one authorized table; the backend collapses all
    uc_table tools on a supervisor agent into a single subagent that can access the union of their
    tables."""

    name: str
    """Full UC table name (catalog.schema.table) this tool is authorized to access."""

    def as_dict(self) -> dict:
        """Serializes the UcTable into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.name is not None:
            body["name"] = self.name
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the UcTable into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.name is not None:
            body["name"] = self.name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> UcTable:
        """Deserializes the UcTable from a dictionary."""
        return cls(name=d.get("name", None))


@dataclass
class VectorSearchIndex:
    """Vector Search index tool authorizing access to a single index."""

    name: str
    """Full Vector Search index name (catalog.schema.index)."""

    columns: Optional[List[str]] = None
    """Optional columns to return from the index. If unset, discovered from index schema at query time."""

    def as_dict(self) -> dict:
        """Serializes the VectorSearchIndex into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.columns:
            body["columns"] = [v for v in self.columns]
        if self.name is not None:
            body["name"] = self.name
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the VectorSearchIndex into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.columns:
            body["columns"] = self.columns
        if self.name is not None:
            body["name"] = self.name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> VectorSearchIndex:
        """Deserializes the VectorSearchIndex from a dictionary."""
        return cls(columns=d.get("columns", None), name=d.get("name", None))


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


@dataclass
class WebSearch:
    """Public-web search tool. Empty body — backend, model registration, and client_id are not
    customer-tunable. The display name and description for this tool come from the parent
    ``Tool.name`` / ``Tool.description`` fields. Reserved for future scoping (allowed domains,
    region overrides)."""

    def as_dict(self) -> dict:
        """Serializes the WebSearch into a dictionary suitable for use as a JSON request body."""
        body = {}
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the WebSearch into a shallow dictionary of its immediate attributes."""
        body = {}
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> WebSearch:
        """Deserializes the WebSearch from a dictionary."""
        return cls()


class SupervisorAgentsAPI:
    """Manage Supervisor Agents and related resources."""

    def __init__(self, api_client):
        self._api = api_client

    def create_example(self, parent: str, example: Example) -> Example:
        """Creates an example for a Supervisor Agent.

        :param parent: str
          Parent resource where this example will be created. Format: supervisor-agents/{supervisor_agent_id}
        :param example: :class:`Example`
          The example to create under the parent Supervisor Agent.

        :returns: :class:`Example`
        """

        body = example.as_dict()
        query = {}
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("POST", f"/api/2.1/{parent}/examples", body=body, headers=headers)
        return Example.from_dict(res)

    def create_supervisor_agent(self, supervisor_agent: SupervisorAgent) -> SupervisorAgent:
        """Creates a new Supervisor Agent.

        :param supervisor_agent: :class:`SupervisorAgent`
          The Supervisor Agent to create.

        :returns: :class:`SupervisorAgent`
        """

        body = supervisor_agent.as_dict()
        query = {}
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("POST", "/api/2.1/supervisor-agents", body=body, headers=headers)
        return SupervisorAgent.from_dict(res)

    def create_tool(self, parent: str, tool: Tool, tool_id: str) -> Tool:
        """Creates a Tool under a Supervisor Agent. Specify one of "genie_space", "knowledge_assistant",
        "uc_function", "uc_connection", "app", "volume", "dashboard", "table", "vector_search_index",
        "catalog", "schema", "supervisor_agent", "databricks_web_search", "skill" in the request body. The
        legacy values "lakeview_dashboard", "uc_table", and "web_search" are also accepted and remain
        equivalent to "dashboard", "table", and "databricks_web_search" respectively. The
        "databricks_web_search" tool_type maps to the ``web_search`` spec field.

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
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("POST", f"/api/2.1/{parent}/tools", query=query, body=body, headers=headers)
        return Tool.from_dict(res)

    def delete_example(self, name: str):
        """Deletes an example from a Supervisor Agent.

        :param name: str
          The resource name of the example to delete. Format:
          supervisor-agents/{supervisor_agent_id}/examples/{example_id}


        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        self._api.do("DELETE", f"/api/2.1/{name}", headers=headers)

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
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

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
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        self._api.do("DELETE", f"/api/2.1/{name}", headers=headers)

    def get_example(self, name: str) -> Example:
        """Gets an example from a Supervisor Agent.

        :param name: str
          The resource name of the example. Format:
          supervisor-agents/{supervisor_agent_id}/examples/{example_id}

        :returns: :class:`Example`
        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("GET", f"/api/2.1/{name}", headers=headers)
        return Example.from_dict(res)

    def get_permission_levels(self, supervisor_agent_id: str) -> GetSupervisorAgentPermissionLevelsResponse:
        """Gets the permission levels that a user can have on an object.

        :param supervisor_agent_id: str
          The supervisor agent for which to get or manage permissions.

        :returns: :class:`GetSupervisorAgentPermissionLevelsResponse`
        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do(
            "GET", f"/api/2.0/permissions/supervisor-agents/{supervisor_agent_id}/permissionLevels", headers=headers
        )
        return GetSupervisorAgentPermissionLevelsResponse.from_dict(res)

    def get_permissions(self, supervisor_agent_id: str) -> SupervisorAgentPermissions:
        """Gets the permissions of a supervisor agent. Supervisor agents can inherit permissions from their root
        object.

        :param supervisor_agent_id: str
          The supervisor agent for which to get or manage permissions.

        :returns: :class:`SupervisorAgentPermissions`
        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("GET", f"/api/2.0/permissions/supervisor-agents/{supervisor_agent_id}", headers=headers)
        return SupervisorAgentPermissions.from_dict(res)

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
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

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
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("GET", f"/api/2.1/{name}", headers=headers)
        return Tool.from_dict(res)

    def list_examples(
        self, parent: str, *, page_size: Optional[int] = None, page_token: Optional[str] = None
    ) -> Iterator[Example]:
        """Lists examples under a Supervisor Agent.

        :param parent: str
          Parent resource to list from. Format: supervisor-agents/{supervisor_agent_id}
        :param page_size: int (optional)
          The maximum number of examples to return. If unspecified, at most 100 examples will be returned. The
          maximum value is 100; values above 100 will be coerced to 100.
        :param page_token: str (optional)
          A page token, received from a previous ``ListExamples`` call. Provide this to retrieve the
          subsequent page. If unspecified, the first page will be returned.

        :returns: Iterator over :class:`Example`
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
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        while True:
            json = self._api.do("GET", f"/api/2.1/{parent}/examples", query=query, headers=headers)
            if "examples" in json:
                for v in json["examples"]:
                    yield Example.from_dict(v)
            if "next_page_token" not in json or not json["next_page_token"]:
                return
            query["page_token"] = json["next_page_token"]

    def list_supervisor_agents(
        self, *, page_size: Optional[int] = None, page_token: Optional[str] = None
    ) -> Iterator[SupervisorAgent]:
        """Lists Supervisor Agents.

        :param page_size: int (optional)
          The maximum number of supervisor agents to return. If unspecified, at most 100 supervisor agents
          will be returned. The maximum value is 100; values above 100 will be coerced to 100.
        :param page_token: str (optional)
          A page token, received from a previous ``ListSupervisorAgents`` call. Provide this to retrieve the
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
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

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
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        while True:
            json = self._api.do("GET", f"/api/2.1/{parent}/tools", query=query, headers=headers)
            if "tools" in json:
                for v in json["tools"]:
                    yield Tool.from_dict(v)
            if "next_page_token" not in json or not json["next_page_token"]:
                return
            query["page_token"] = json["next_page_token"]

    def set_permissions(
        self,
        supervisor_agent_id: str,
        *,
        access_control_list: Optional[List[SupervisorAgentAccessControlRequest]] = None,
    ) -> SupervisorAgentPermissions:
        """Sets permissions on an object, replacing existing permissions if they exist. Deletes all direct
        permissions if none are specified. Objects can inherit permissions from their root object.

        :param supervisor_agent_id: str
          The supervisor agent for which to get or manage permissions.
        :param access_control_list: List[:class:`SupervisorAgentAccessControlRequest`] (optional)

        :returns: :class:`SupervisorAgentPermissions`
        """

        body = {}
        if access_control_list is not None:
            body["access_control_list"] = [v.as_dict() for v in access_control_list]
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do(
            "PUT", f"/api/2.0/permissions/supervisor-agents/{supervisor_agent_id}", body=body, headers=headers
        )
        return SupervisorAgentPermissions.from_dict(res)

    def update_example(self, name: str, example: Example, update_mask: FieldMask) -> Example:
        """Updates an example in a Supervisor Agent.

        :param name: str
          The resource name of the example to update. Format:
          supervisor-agents/{supervisor_agent_id}/examples/{example_id}
        :param example: :class:`Example`
        :param update_mask: FieldMask
          Comma-delimited list of fields to update on the example. Allowed values: ``question``,
          ``guidelines``. Examples:

          - ``question``
          - ``question,guidelines``

        :returns: :class:`Example`
        """

        body = example.as_dict()
        query = {}
        if update_mask is not None:
            query["update_mask"] = update_mask.ToJsonString()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("PATCH", f"/api/2.1/{name}", query=query, body=body, headers=headers)
        return Example.from_dict(res)

    def update_permissions(
        self,
        supervisor_agent_id: str,
        *,
        access_control_list: Optional[List[SupervisorAgentAccessControlRequest]] = None,
    ) -> SupervisorAgentPermissions:
        """Updates the permissions on a supervisor agent. Supervisor agents can inherit permissions from their
        root object.

        :param supervisor_agent_id: str
          The supervisor agent for which to get or manage permissions.
        :param access_control_list: List[:class:`SupervisorAgentAccessControlRequest`] (optional)

        :returns: :class:`SupervisorAgentPermissions`
        """

        body = {}
        if access_control_list is not None:
            body["access_control_list"] = [v.as_dict() for v in access_control_list]
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do(
            "PATCH", f"/api/2.0/permissions/supervisor-agents/{supervisor_agent_id}", body=body, headers=headers
        )
        return SupervisorAgentPermissions.from_dict(res)

    def update_supervisor_agent(
        self, name: str, supervisor_agent: SupervisorAgent, update_mask: FieldMask
    ) -> SupervisorAgent:
        """Updates a Supervisor Agent. The fields that are required depend on the paths specified in
        ``update_mask``. Only fields included in the mask will be updated.

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
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("PATCH", f"/api/2.1/{name}", query=query, body=body, headers=headers)
        return SupervisorAgent.from_dict(res)

    def update_tool(self, name: str, tool: Tool, update_mask: FieldMask) -> Tool:
        """Updates a Tool. Only the ``description`` field can be updated. To change immutable fields such as tool
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
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("PATCH", f"/api/2.1/{name}", query=query, body=body, headers=headers)
        return Tool.from_dict(res)
