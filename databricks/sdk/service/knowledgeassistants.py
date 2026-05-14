# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

from __future__ import annotations

import logging
from dataclasses import dataclass
from enum import Enum
from typing import Any, Dict, Iterator, List, Optional

from google.protobuf.timestamp_pb2 import Timestamp

from databricks.sdk.common.types.fieldmask import FieldMask
from databricks.sdk.service._internal import (_enum, _from_dict,
                                              _repeated_dict, _timestamp)

_LOG = logging.getLogger("databricks.sdk")


# all definitions in this file are in alphabetical order


@dataclass
class Example:
    """An example associated with a Knowledge Assistant. Contains a question and guidelines for how the
    assistant should respond."""

    question: str
    """The example question."""

    create_time: Optional[Timestamp] = None
    """Timestamp when this example was created."""

    example_id: Optional[str] = None
    """The universally unique identifier (UUID) of the example."""

    guidelines: Optional[List[str]] = None
    """Guidelines for answering the question. Optional — examples may be created with just a
    question; the front-end form does not require guidelines."""

    name: Optional[str] = None
    """Full resource name: knowledge-assistants/{knowledge_assistant_id}/examples/{example_id}"""

    update_time: Optional[Timestamp] = None
    """Timestamp when this example was last updated."""

    def as_dict(self) -> dict:
        """Serializes the Example into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.create_time is not None:
            body["create_time"] = self.create_time.ToJsonString()
        if self.example_id is not None:
            body["example_id"] = self.example_id
        if self.guidelines:
            body["guidelines"] = [v for v in self.guidelines]
        if self.name is not None:
            body["name"] = self.name
        if self.question is not None:
            body["question"] = self.question
        if self.update_time is not None:
            body["update_time"] = self.update_time.ToJsonString()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the Example into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.create_time is not None:
            body["create_time"] = self.create_time
        if self.example_id is not None:
            body["example_id"] = self.example_id
        if self.guidelines:
            body["guidelines"] = self.guidelines
        if self.name is not None:
            body["name"] = self.name
        if self.question is not None:
            body["question"] = self.question
        if self.update_time is not None:
            body["update_time"] = self.update_time
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> Example:
        """Deserializes the Example from a dictionary."""
        return cls(
            create_time=_timestamp(d, "create_time"),
            example_id=d.get("example_id", None),
            guidelines=d.get("guidelines", None),
            name=d.get("name", None),
            question=d.get("question", None),
            update_time=_timestamp(d, "update_time"),
        )


@dataclass
class FileTableSpec:
    """FileTableSpec specifies a file table source configuration."""

    table_name: str
    """Full UC name of the table, in the format of {CATALOG}.{SCHEMA}.{TABLE_NAME}."""

    file_col: str
    """The name of the column containing BINARY file content to be indexed."""

    def as_dict(self) -> dict:
        """Serializes the FileTableSpec into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.file_col is not None:
            body["file_col"] = self.file_col
        if self.table_name is not None:
            body["table_name"] = self.table_name
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the FileTableSpec into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.file_col is not None:
            body["file_col"] = self.file_col
        if self.table_name is not None:
            body["table_name"] = self.table_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> FileTableSpec:
        """Deserializes the FileTableSpec from a dictionary."""
        return cls(file_col=d.get("file_col", None), table_name=d.get("table_name", None))


@dataclass
class FilesSpec:
    """FilesSpec specifies a files source configuration."""

    path: str
    """A UC volume path that includes a list of files."""

    def as_dict(self) -> dict:
        """Serializes the FilesSpec into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.path is not None:
            body["path"] = self.path
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the FilesSpec into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.path is not None:
            body["path"] = self.path
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> FilesSpec:
        """Deserializes the FilesSpec from a dictionary."""
        return cls(path=d.get("path", None))


@dataclass
class GetKnowledgeAssistantPermissionLevelsResponse:
    permission_levels: Optional[List[KnowledgeAssistantPermissionsDescription]] = None
    """Specific permission levels"""

    def as_dict(self) -> dict:
        """Serializes the GetKnowledgeAssistantPermissionLevelsResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.permission_levels:
            body["permission_levels"] = [v.as_dict() for v in self.permission_levels]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the GetKnowledgeAssistantPermissionLevelsResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.permission_levels:
            body["permission_levels"] = self.permission_levels
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> GetKnowledgeAssistantPermissionLevelsResponse:
        """Deserializes the GetKnowledgeAssistantPermissionLevelsResponse from a dictionary."""
        return cls(permission_levels=_repeated_dict(d, "permission_levels", KnowledgeAssistantPermissionsDescription))


@dataclass
class IndexSpec:
    """IndexSpec specifies a vector search index source configuration."""

    index_name: str
    """Full UC name of the vector search index, in the format of {CATALOG}.{SCHEMA}.{INDEX_NAME}."""

    text_col: str
    """The column that includes the document text for retrieval."""

    doc_uri_col: str
    """The column that specifies a link or reference to where the information came from."""

    def as_dict(self) -> dict:
        """Serializes the IndexSpec into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.doc_uri_col is not None:
            body["doc_uri_col"] = self.doc_uri_col
        if self.index_name is not None:
            body["index_name"] = self.index_name
        if self.text_col is not None:
            body["text_col"] = self.text_col
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the IndexSpec into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.doc_uri_col is not None:
            body["doc_uri_col"] = self.doc_uri_col
        if self.index_name is not None:
            body["index_name"] = self.index_name
        if self.text_col is not None:
            body["text_col"] = self.text_col
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> IndexSpec:
        """Deserializes the IndexSpec from a dictionary."""
        return cls(
            doc_uri_col=d.get("doc_uri_col", None),
            index_name=d.get("index_name", None),
            text_col=d.get("text_col", None),
        )


@dataclass
class KnowledgeAssistant:
    """Entity message that represents a knowledge assistant. Note: REQUIRED annotations below represent
    create-time requirements. For updates, required fields are determined by the update mask."""

    display_name: str
    """The display name of the Knowledge Assistant, unique at workspace level. Required when creating a
    Knowledge Assistant. When updating a Knowledge Assistant, optional unless included in
    update_mask."""

    description: str
    """Description of what this agent can do (user-facing). Required when creating a Knowledge
    Assistant. When updating a Knowledge Assistant, optional unless included in update_mask."""

    create_time: Optional[Timestamp] = None
    """Creation timestamp."""

    creator: Optional[str] = None
    """The creator of the Knowledge Assistant."""

    endpoint_name: Optional[str] = None
    """The name of the knowledge assistant agent endpoint."""

    error_info: Optional[str] = None
    """Error details when the Knowledge Assistant is in FAILED state."""

    experiment_id: Optional[str] = None
    """The MLflow experiment ID."""

    id: Optional[str] = None
    """Deprecated: use knowledge_assistant_id instead."""

    instructions: Optional[str] = None
    """Additional global instructions on how the agent should generate answers. Optional on create and
    update. When updating a Knowledge Assistant, include this field in update_mask to modify it."""

    name: Optional[str] = None
    """The resource name of the Knowledge Assistant. Format:
    knowledge-assistants/{knowledge_assistant_id}"""

    state: Optional[KnowledgeAssistantState] = None
    """State of the Knowledge Assistant. Not returned in List responses."""

    def as_dict(self) -> dict:
        """Serializes the KnowledgeAssistant into a dictionary suitable for use as a JSON request body."""
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
        if self.error_info is not None:
            body["error_info"] = self.error_info
        if self.experiment_id is not None:
            body["experiment_id"] = self.experiment_id
        if self.id is not None:
            body["id"] = self.id
        if self.instructions is not None:
            body["instructions"] = self.instructions
        if self.name is not None:
            body["name"] = self.name
        if self.state is not None:
            body["state"] = self.state.value
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the KnowledgeAssistant into a shallow dictionary of its immediate attributes."""
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
        if self.error_info is not None:
            body["error_info"] = self.error_info
        if self.experiment_id is not None:
            body["experiment_id"] = self.experiment_id
        if self.id is not None:
            body["id"] = self.id
        if self.instructions is not None:
            body["instructions"] = self.instructions
        if self.name is not None:
            body["name"] = self.name
        if self.state is not None:
            body["state"] = self.state
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> KnowledgeAssistant:
        """Deserializes the KnowledgeAssistant from a dictionary."""
        return cls(
            create_time=_timestamp(d, "create_time"),
            creator=d.get("creator", None),
            description=d.get("description", None),
            display_name=d.get("display_name", None),
            endpoint_name=d.get("endpoint_name", None),
            error_info=d.get("error_info", None),
            experiment_id=d.get("experiment_id", None),
            id=d.get("id", None),
            instructions=d.get("instructions", None),
            name=d.get("name", None),
            state=_enum(d, "state", KnowledgeAssistantState),
        )


@dataclass
class KnowledgeAssistantAccessControlRequest:
    group_name: Optional[str] = None
    """name of the group"""

    permission_level: Optional[KnowledgeAssistantPermissionLevel] = None

    service_principal_name: Optional[str] = None
    """application ID of a service principal"""

    user_name: Optional[str] = None
    """name of the user"""

    def as_dict(self) -> dict:
        """Serializes the KnowledgeAssistantAccessControlRequest into a dictionary suitable for use as a JSON request body."""
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
        """Serializes the KnowledgeAssistantAccessControlRequest into a shallow dictionary of its immediate attributes."""
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
    def from_dict(cls, d: Dict[str, Any]) -> KnowledgeAssistantAccessControlRequest:
        """Deserializes the KnowledgeAssistantAccessControlRequest from a dictionary."""
        return cls(
            group_name=d.get("group_name", None),
            permission_level=_enum(d, "permission_level", KnowledgeAssistantPermissionLevel),
            service_principal_name=d.get("service_principal_name", None),
            user_name=d.get("user_name", None),
        )


@dataclass
class KnowledgeAssistantAccessControlResponse:
    all_permissions: Optional[List[KnowledgeAssistantPermission]] = None
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
        """Serializes the KnowledgeAssistantAccessControlResponse into a dictionary suitable for use as a JSON request body."""
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
        """Serializes the KnowledgeAssistantAccessControlResponse into a shallow dictionary of its immediate attributes."""
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
    def from_dict(cls, d: Dict[str, Any]) -> KnowledgeAssistantAccessControlResponse:
        """Deserializes the KnowledgeAssistantAccessControlResponse from a dictionary."""
        return cls(
            all_permissions=_repeated_dict(d, "all_permissions", KnowledgeAssistantPermission),
            display_name=d.get("display_name", None),
            group_name=d.get("group_name", None),
            service_principal_name=d.get("service_principal_name", None),
            user_name=d.get("user_name", None),
        )


@dataclass
class KnowledgeAssistantPermission:
    inherited: Optional[bool] = None

    inherited_from_object: Optional[List[str]] = None

    permission_level: Optional[KnowledgeAssistantPermissionLevel] = None

    def as_dict(self) -> dict:
        """Serializes the KnowledgeAssistantPermission into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.inherited is not None:
            body["inherited"] = self.inherited
        if self.inherited_from_object:
            body["inherited_from_object"] = [v for v in self.inherited_from_object]
        if self.permission_level is not None:
            body["permission_level"] = self.permission_level.value
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the KnowledgeAssistantPermission into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.inherited is not None:
            body["inherited"] = self.inherited
        if self.inherited_from_object:
            body["inherited_from_object"] = self.inherited_from_object
        if self.permission_level is not None:
            body["permission_level"] = self.permission_level
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> KnowledgeAssistantPermission:
        """Deserializes the KnowledgeAssistantPermission from a dictionary."""
        return cls(
            inherited=d.get("inherited", None),
            inherited_from_object=d.get("inherited_from_object", None),
            permission_level=_enum(d, "permission_level", KnowledgeAssistantPermissionLevel),
        )


class KnowledgeAssistantPermissionLevel(Enum):
    """Permission level"""

    CAN_MANAGE = "CAN_MANAGE"
    CAN_QUERY = "CAN_QUERY"


@dataclass
class KnowledgeAssistantPermissions:
    access_control_list: Optional[List[KnowledgeAssistantAccessControlResponse]] = None

    object_id: Optional[str] = None

    object_type: Optional[str] = None

    def as_dict(self) -> dict:
        """Serializes the KnowledgeAssistantPermissions into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.access_control_list:
            body["access_control_list"] = [v.as_dict() for v in self.access_control_list]
        if self.object_id is not None:
            body["object_id"] = self.object_id
        if self.object_type is not None:
            body["object_type"] = self.object_type
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the KnowledgeAssistantPermissions into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.access_control_list:
            body["access_control_list"] = self.access_control_list
        if self.object_id is not None:
            body["object_id"] = self.object_id
        if self.object_type is not None:
            body["object_type"] = self.object_type
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> KnowledgeAssistantPermissions:
        """Deserializes the KnowledgeAssistantPermissions from a dictionary."""
        return cls(
            access_control_list=_repeated_dict(d, "access_control_list", KnowledgeAssistantAccessControlResponse),
            object_id=d.get("object_id", None),
            object_type=d.get("object_type", None),
        )


@dataclass
class KnowledgeAssistantPermissionsDescription:
    description: Optional[str] = None

    permission_level: Optional[KnowledgeAssistantPermissionLevel] = None

    def as_dict(self) -> dict:
        """Serializes the KnowledgeAssistantPermissionsDescription into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.description is not None:
            body["description"] = self.description
        if self.permission_level is not None:
            body["permission_level"] = self.permission_level.value
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the KnowledgeAssistantPermissionsDescription into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.description is not None:
            body["description"] = self.description
        if self.permission_level is not None:
            body["permission_level"] = self.permission_level
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> KnowledgeAssistantPermissionsDescription:
        """Deserializes the KnowledgeAssistantPermissionsDescription from a dictionary."""
        return cls(
            description=d.get("description", None),
            permission_level=_enum(d, "permission_level", KnowledgeAssistantPermissionLevel),
        )


class KnowledgeAssistantState(Enum):

    ACTIVE = "ACTIVE"
    CREATING = "CREATING"
    FAILED = "FAILED"


@dataclass
class KnowledgeSource:
    """KnowledgeSource represents a source of knowledge for the KnowledgeAssistant. Used in
    create/update requests and returned in Get/List responses. Note: REQUIRED annotations below
    represent create-time requirements. For updates, required fields are determined by the update
    mask."""

    display_name: str
    """Human-readable display name of the knowledge source. Required when creating a Knowledge Source.
    When updating a Knowledge Source, optional unless included in update_mask."""

    description: str
    """Description of the knowledge source. Required when creating a Knowledge Source. When updating a
    Knowledge Source, optional unless included in update_mask."""

    source_type: str
    """The type of the source: "index", "files", or "file_table". Required when creating a Knowledge
    Source. When updating a Knowledge Source, this field is ignored."""

    create_time: Optional[Timestamp] = None
    """Timestamp when this knowledge source was created."""

    file_table: Optional[FileTableSpec] = None

    files: Optional[FilesSpec] = None

    id: Optional[str] = None

    index: Optional[IndexSpec] = None

    knowledge_cutoff_time: Optional[Timestamp] = None
    """Timestamp representing the cutoff before which content in this knowledge source is being
    ingested."""

    name: Optional[str] = None
    """Full resource name:
    knowledge-assistants/{knowledge_assistant_id}/knowledge-sources/{knowledge_source_id}"""

    state: Optional[KnowledgeSourceState] = None

    def as_dict(self) -> dict:
        """Serializes the KnowledgeSource into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.create_time is not None:
            body["create_time"] = self.create_time.ToJsonString()
        if self.description is not None:
            body["description"] = self.description
        if self.display_name is not None:
            body["display_name"] = self.display_name
        if self.file_table:
            body["file_table"] = self.file_table.as_dict()
        if self.files:
            body["files"] = self.files.as_dict()
        if self.id is not None:
            body["id"] = self.id
        if self.index:
            body["index"] = self.index.as_dict()
        if self.knowledge_cutoff_time is not None:
            body["knowledge_cutoff_time"] = self.knowledge_cutoff_time.ToJsonString()
        if self.name is not None:
            body["name"] = self.name
        if self.source_type is not None:
            body["source_type"] = self.source_type
        if self.state is not None:
            body["state"] = self.state.value
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the KnowledgeSource into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.create_time is not None:
            body["create_time"] = self.create_time
        if self.description is not None:
            body["description"] = self.description
        if self.display_name is not None:
            body["display_name"] = self.display_name
        if self.file_table:
            body["file_table"] = self.file_table
        if self.files:
            body["files"] = self.files
        if self.id is not None:
            body["id"] = self.id
        if self.index:
            body["index"] = self.index
        if self.knowledge_cutoff_time is not None:
            body["knowledge_cutoff_time"] = self.knowledge_cutoff_time
        if self.name is not None:
            body["name"] = self.name
        if self.source_type is not None:
            body["source_type"] = self.source_type
        if self.state is not None:
            body["state"] = self.state
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> KnowledgeSource:
        """Deserializes the KnowledgeSource from a dictionary."""
        return cls(
            create_time=_timestamp(d, "create_time"),
            description=d.get("description", None),
            display_name=d.get("display_name", None),
            file_table=_from_dict(d, "file_table", FileTableSpec),
            files=_from_dict(d, "files", FilesSpec),
            id=d.get("id", None),
            index=_from_dict(d, "index", IndexSpec),
            knowledge_cutoff_time=_timestamp(d, "knowledge_cutoff_time"),
            name=d.get("name", None),
            source_type=d.get("source_type", None),
            state=_enum(d, "state", KnowledgeSourceState),
        )


class KnowledgeSourceState(Enum):

    FAILED_UPDATE = "FAILED_UPDATE"
    UPDATED = "UPDATED"
    UPDATING = "UPDATING"


@dataclass
class ListExamplesResponse:
    """A list of Knowledge Assistant examples."""

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
class ListKnowledgeAssistantsResponse:
    """A list of Knowledge Assistants."""

    knowledge_assistants: Optional[List[KnowledgeAssistant]] = None

    next_page_token: Optional[str] = None
    """A token that can be sent as `page_token` to retrieve the next page. If this field is omitted,
    there are no subsequent pages."""

    def as_dict(self) -> dict:
        """Serializes the ListKnowledgeAssistantsResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.knowledge_assistants:
            body["knowledge_assistants"] = [v.as_dict() for v in self.knowledge_assistants]
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ListKnowledgeAssistantsResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.knowledge_assistants:
            body["knowledge_assistants"] = self.knowledge_assistants
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ListKnowledgeAssistantsResponse:
        """Deserializes the ListKnowledgeAssistantsResponse from a dictionary."""
        return cls(
            knowledge_assistants=_repeated_dict(d, "knowledge_assistants", KnowledgeAssistant),
            next_page_token=d.get("next_page_token", None),
        )


@dataclass
class ListKnowledgeSourcesResponse:
    knowledge_sources: Optional[List[KnowledgeSource]] = None

    next_page_token: Optional[str] = None

    def as_dict(self) -> dict:
        """Serializes the ListKnowledgeSourcesResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.knowledge_sources:
            body["knowledge_sources"] = [v.as_dict() for v in self.knowledge_sources]
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ListKnowledgeSourcesResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.knowledge_sources:
            body["knowledge_sources"] = self.knowledge_sources
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ListKnowledgeSourcesResponse:
        """Deserializes the ListKnowledgeSourcesResponse from a dictionary."""
        return cls(
            knowledge_sources=_repeated_dict(d, "knowledge_sources", KnowledgeSource),
            next_page_token=d.get("next_page_token", None),
        )


class KnowledgeAssistantsAPI:
    """Manage Knowledge Assistants and related resources."""

    def __init__(self, api_client):
        self._api = api_client

    def create_example(self, parent: str, example: Example) -> Example:
        """Creates an example for a Knowledge Assistant.

        :param parent: str
          Parent resource where this example will be created. Format:
          knowledge-assistants/{knowledge_assistant_id}
        :param example: :class:`Example`
          The example to create under the parent Knowledge Assistant.

        :returns: :class:`Example`
        """

        body = example.as_dict()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Org-Id"] = cfg.workspace_id

        res = self._api.do("POST", f"/api/2.1/{parent}/examples", body=body, headers=headers)
        return Example.from_dict(res)

    def create_knowledge_assistant(self, knowledge_assistant: KnowledgeAssistant) -> KnowledgeAssistant:
        """Creates a Knowledge Assistant.

        :param knowledge_assistant: :class:`KnowledgeAssistant`
          The Knowledge Assistant to create.

        :returns: :class:`KnowledgeAssistant`
        """

        body = knowledge_assistant.as_dict()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Org-Id"] = cfg.workspace_id

        res = self._api.do("POST", "/api/2.1/knowledge-assistants", body=body, headers=headers)
        return KnowledgeAssistant.from_dict(res)

    def create_knowledge_source(self, parent: str, knowledge_source: KnowledgeSource) -> KnowledgeSource:
        """Creates a Knowledge Source under a Knowledge Assistant.

        :param parent: str
          Parent resource where this source will be created. Format:
          knowledge-assistants/{knowledge_assistant_id}
        :param knowledge_source: :class:`KnowledgeSource`

        :returns: :class:`KnowledgeSource`
        """

        body = knowledge_source.as_dict()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Org-Id"] = cfg.workspace_id

        res = self._api.do("POST", f"/api/2.1/{parent}/knowledge-sources", body=body, headers=headers)
        return KnowledgeSource.from_dict(res)

    def delete_example(self, name: str):
        """Deletes an example from a Knowledge Assistant.

        :param name: str
          The resource name of the example to delete. Format:
          knowledge-assistants/{knowledge_assistant_id}/examples/{example_id}


        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Org-Id"] = cfg.workspace_id

        self._api.do("DELETE", f"/api/2.1/{name}", headers=headers)

    def delete_knowledge_assistant(self, name: str):
        """Deletes a Knowledge Assistant.

        :param name: str
          The resource name of the knowledge assistant to be deleted. Format:
          knowledge-assistants/{knowledge_assistant_id}


        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Org-Id"] = cfg.workspace_id

        self._api.do("DELETE", f"/api/2.1/{name}", headers=headers)

    def delete_knowledge_source(self, name: str):
        """Deletes a Knowledge Source.

        :param name: str
          The resource name of the Knowledge Source to delete. Format:
          knowledge-assistants/{knowledge_assistant_id}/knowledge-sources/{knowledge_source_id}


        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Org-Id"] = cfg.workspace_id

        self._api.do("DELETE", f"/api/2.1/{name}", headers=headers)

    def get_example(self, name: str) -> Example:
        """Gets an example from a Knowledge Assistant.

        :param name: str
          The resource name of the example. Format:
          knowledge-assistants/{knowledge_assistant_id}/examples/{example_id}

        :returns: :class:`Example`
        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Org-Id"] = cfg.workspace_id

        res = self._api.do("GET", f"/api/2.1/{name}", headers=headers)
        return Example.from_dict(res)

    def get_knowledge_assistant(self, name: str) -> KnowledgeAssistant:
        """Gets a Knowledge Assistant.

        :param name: str
          The resource name of the knowledge assistant. Format: knowledge-assistants/{knowledge_assistant_id}

        :returns: :class:`KnowledgeAssistant`
        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Org-Id"] = cfg.workspace_id

        res = self._api.do("GET", f"/api/2.1/{name}", headers=headers)
        return KnowledgeAssistant.from_dict(res)

    def get_knowledge_source(self, name: str) -> KnowledgeSource:
        """Gets a Knowledge Source.

        :param name: str
          The resource name of the Knowledge Source. Format:
          knowledge-assistants/{knowledge_assistant_id}/knowledge-sources/{knowledge_source_id}

        :returns: :class:`KnowledgeSource`
        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Org-Id"] = cfg.workspace_id

        res = self._api.do("GET", f"/api/2.1/{name}", headers=headers)
        return KnowledgeSource.from_dict(res)

    def get_permission_levels(self, knowledge_assistant_id: str) -> GetKnowledgeAssistantPermissionLevelsResponse:
        """Gets the permission levels that a user can have on an object.

        :param knowledge_assistant_id: str
          The knowledge assistant for which to get or manage permissions.

        :returns: :class:`GetKnowledgeAssistantPermissionLevelsResponse`
        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Org-Id"] = cfg.workspace_id

        res = self._api.do(
            "GET",
            f"/api/2.0/permissions/knowledge-assistants/{knowledge_assistant_id}/permissionLevels",
            headers=headers,
        )
        return GetKnowledgeAssistantPermissionLevelsResponse.from_dict(res)

    def get_permissions(self, knowledge_assistant_id: str) -> KnowledgeAssistantPermissions:
        """Gets the permissions of a knowledge assistant. Knowledge assistants can inherit permissions from their
        root object.

        :param knowledge_assistant_id: str
          The knowledge assistant for which to get or manage permissions.

        :returns: :class:`KnowledgeAssistantPermissions`
        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Org-Id"] = cfg.workspace_id

        res = self._api.do(
            "GET", f"/api/2.0/permissions/knowledge-assistants/{knowledge_assistant_id}", headers=headers
        )
        return KnowledgeAssistantPermissions.from_dict(res)

    def list_examples(
        self, parent: str, *, page_size: Optional[int] = None, page_token: Optional[str] = None
    ) -> Iterator[Example]:
        """Lists examples under a Knowledge Assistant.

        :param parent: str
          Parent resource to list from. Format: knowledge-assistants/{knowledge_assistant_id}
        :param page_size: int (optional)
          The maximum number of examples to return. If unspecified, at most 100 examples will be returned. The
          maximum value is 100; values above 100 will be coerced to 100.
        :param page_token: str (optional)
          A page token, received from a previous `ListExamples` call. Provide this to retrieve the subsequent
          page. If unspecified, the first page will be returned.

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
            headers["X-Databricks-Org-Id"] = cfg.workspace_id

        while True:
            json = self._api.do("GET", f"/api/2.1/{parent}/examples", query=query, headers=headers)
            if "examples" in json:
                for v in json["examples"]:
                    yield Example.from_dict(v)
            if "next_page_token" not in json or not json["next_page_token"]:
                return
            query["page_token"] = json["next_page_token"]

    def list_knowledge_assistants(
        self, *, page_size: Optional[int] = None, page_token: Optional[str] = None
    ) -> Iterator[KnowledgeAssistant]:
        """List Knowledge Assistants

        :param page_size: int (optional)
          The maximum number of knowledge assistants to return. If unspecified, at most 100 knowledge
          assistants will be returned. The maximum value is 100; values above 100 will be coerced to 100.
        :param page_token: str (optional)
          A page token, received from a previous `ListKnowledgeAssistants` call. Provide this to retrieve the
          subsequent page. If unspecified, the first page will be returned.

        :returns: Iterator over :class:`KnowledgeAssistant`
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
            json = self._api.do("GET", "/api/2.1/knowledge-assistants", query=query, headers=headers)
            if "knowledge_assistants" in json:
                for v in json["knowledge_assistants"]:
                    yield KnowledgeAssistant.from_dict(v)
            if "next_page_token" not in json or not json["next_page_token"]:
                return
            query["page_token"] = json["next_page_token"]

    def list_knowledge_sources(
        self, parent: str, *, page_size: Optional[int] = None, page_token: Optional[str] = None
    ) -> Iterator[KnowledgeSource]:
        """Lists Knowledge Sources under a Knowledge Assistant.

        :param parent: str
          Parent resource to list from. Format: knowledge-assistants/{knowledge_assistant_id}
        :param page_size: int (optional)
        :param page_token: str (optional)

        :returns: Iterator over :class:`KnowledgeSource`
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
            json = self._api.do("GET", f"/api/2.1/{parent}/knowledge-sources", query=query, headers=headers)
            if "knowledge_sources" in json:
                for v in json["knowledge_sources"]:
                    yield KnowledgeSource.from_dict(v)
            if "next_page_token" not in json or not json["next_page_token"]:
                return
            query["page_token"] = json["next_page_token"]

    def set_permissions(
        self,
        knowledge_assistant_id: str,
        *,
        access_control_list: Optional[List[KnowledgeAssistantAccessControlRequest]] = None,
    ) -> KnowledgeAssistantPermissions:
        """Sets permissions on an object, replacing existing permissions if they exist. Deletes all direct
        permissions if none are specified. Objects can inherit permissions from their root object.

        :param knowledge_assistant_id: str
          The knowledge assistant for which to get or manage permissions.
        :param access_control_list: List[:class:`KnowledgeAssistantAccessControlRequest`] (optional)

        :returns: :class:`KnowledgeAssistantPermissions`
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
            headers["X-Databricks-Org-Id"] = cfg.workspace_id

        res = self._api.do(
            "PUT", f"/api/2.0/permissions/knowledge-assistants/{knowledge_assistant_id}", body=body, headers=headers
        )
        return KnowledgeAssistantPermissions.from_dict(res)

    def sync_knowledge_sources(self, name: str):
        """Sync all non-index Knowledge Sources for a Knowledge Assistant (index sources do not require sync)

        :param name: str
          The resource name of the Knowledge Assistant. Format: knowledge-assistants/{knowledge_assistant_id}


        """

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Org-Id"] = cfg.workspace_id

        self._api.do("POST", f"/api/2.1/{name}/knowledge-sources:sync", headers=headers)

    def update_example(self, name: str, example: Example, update_mask: FieldMask) -> Example:
        """Updates an example in a Knowledge Assistant.

        :param name: str
          The resource name of the example to update. Format:
          knowledge-assistants/{knowledge_assistant_id}/examples/{example_id}
        :param example: :class:`Example`
        :param update_mask: FieldMask
          Comma-delimited list of fields to update on the example. Allowed values: `question`, `guidelines`.
          Examples: - `question` - `question,guidelines`

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
            headers["X-Databricks-Org-Id"] = cfg.workspace_id

        res = self._api.do("PATCH", f"/api/2.1/{name}", query=query, body=body, headers=headers)
        return Example.from_dict(res)

    def update_knowledge_assistant(
        self, name: str, knowledge_assistant: KnowledgeAssistant, update_mask: FieldMask
    ) -> KnowledgeAssistant:
        """Updates a Knowledge Assistant.

        :param name: str
          The resource name of the Knowledge Assistant. Format: knowledge-assistants/{knowledge_assistant_id}
        :param knowledge_assistant: :class:`KnowledgeAssistant`
          The Knowledge Assistant update payload. Only fields listed in update_mask are updated. REQUIRED
          annotations on Knowledge Assistant fields describe create-time requirements and do not mean all
          those fields are required for update.
        :param update_mask: FieldMask
          Comma-delimited list of fields to update on the Knowledge Assistant. Allowed values: `display_name`,
          `description`, `instructions`. Examples: - `display_name` - `description,instructions`

        :returns: :class:`KnowledgeAssistant`
        """

        body = knowledge_assistant.as_dict()
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
        return KnowledgeAssistant.from_dict(res)

    def update_knowledge_source(
        self, name: str, knowledge_source: KnowledgeSource, update_mask: FieldMask
    ) -> KnowledgeSource:
        """Updates a Knowledge Source.

        :param name: str
          The resource name of the Knowledge Source to update. Format:
          knowledge-assistants/{knowledge_assistant_id}/knowledge-sources/{knowledge_source_id}
        :param knowledge_source: :class:`KnowledgeSource`
          The Knowledge Source update payload. Only fields listed in update_mask are updated. REQUIRED
          annotations on Knowledge Source fields describe create-time requirements and do not mean all those
          fields are required for update.
        :param update_mask: FieldMask
          Comma-delimited list of fields to update on the Knowledge Source. Allowed values: `display_name`,
          `description`. Examples: - `display_name` - `display_name,description`

        :returns: :class:`KnowledgeSource`
        """

        body = knowledge_source.as_dict()
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
        return KnowledgeSource.from_dict(res)

    def update_permissions(
        self,
        knowledge_assistant_id: str,
        *,
        access_control_list: Optional[List[KnowledgeAssistantAccessControlRequest]] = None,
    ) -> KnowledgeAssistantPermissions:
        """Updates the permissions on a knowledge assistant. Knowledge assistants can inherit permissions from
        their root object.

        :param knowledge_assistant_id: str
          The knowledge assistant for which to get or manage permissions.
        :param access_control_list: List[:class:`KnowledgeAssistantAccessControlRequest`] (optional)

        :returns: :class:`KnowledgeAssistantPermissions`
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
            headers["X-Databricks-Org-Id"] = cfg.workspace_id

        res = self._api.do(
            "PATCH", f"/api/2.0/permissions/knowledge-assistants/{knowledge_assistant_id}", body=body, headers=headers
        )
        return KnowledgeAssistantPermissions.from_dict(res)
