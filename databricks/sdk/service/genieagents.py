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
class GenieAgent:
    """A Genie Agent resource."""

    display_name: str
    """Display name of the Genie Agent. Must be unique within its folder (effective_parent_path): a
    create, rename, or move that would collide with an existing Genie Agent's name in the target
    folder is rejected with ALREADY_EXISTS.
    
    The maximum length is 63 characters. Requests with a longer value are rejected with
    INVALID_PARAMETER_VALUE."""

    definition: GenieAgentDefinition
    """The definition of the Genie Agent: its sample questions, data sources, instructions, and
    benchmarks. Must set at least one field. Returned on get and on list with
    ``GENIE_AGENT_VIEW_FULL``. Create and update return a submitted definition unchanged; one the
    service would store differently, or with a column config the workspace can't keep (unknown
    column, or a display name while those are disabled), is rejected with INVALID_PARAMETER_VALUE."""

    warehouse_id: str
    """Warehouse associated with the Genie Agent."""

    create_time: Optional[Timestamp] = None
    """Time when the Genie Agent was created."""

    description: Optional[str] = None
    """Description of the Genie Agent.
    
    The maximum length is 4,096 characters. Requests with a longer value are rejected with
    INVALID_PARAMETER_VALUE."""

    effective_parent_path: Optional[str] = None
    """The workspace folder that contains the Genie Agent."""

    etag: Optional[str] = None
    """Weak etag of ``definition`` only; metadata changes do not affect it. Send it on update or delete
    to detect concurrent definition changes."""

    name: Optional[str] = None
    """The resource name of the Genie Agent, in the form ``agents/{genie_agent_id}``. Ignored on
    create."""

    parent_path: Optional[str] = None
    """The workspace folder to create the Genie Agent in. If omitted, the caller's home folder is used.
    Returned exactly as submitted; see ``effective_parent_path`` for the current folder. On update,
    setting it moves the Genie Agent and clearing it does not. At most 4,096 characters."""

    update_time: Optional[Timestamp] = None
    """Time when the Genie Agent was last modified."""

    def as_dict(self) -> dict:
        """Serializes the GenieAgent into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.create_time is not None:
            body["create_time"] = self.create_time.ToJsonString()
        if self.definition:
            body["definition"] = self.definition.as_dict()
        if self.description is not None:
            body["description"] = self.description
        if self.display_name is not None:
            body["display_name"] = self.display_name
        if self.effective_parent_path is not None:
            body["effective_parent_path"] = self.effective_parent_path
        if self.etag is not None:
            body["etag"] = self.etag
        if self.name is not None:
            body["name"] = self.name
        if self.parent_path is not None:
            body["parent_path"] = self.parent_path
        if self.update_time is not None:
            body["update_time"] = self.update_time.ToJsonString()
        if self.warehouse_id is not None:
            body["warehouse_id"] = self.warehouse_id
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the GenieAgent into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.create_time is not None:
            body["create_time"] = self.create_time
        if self.definition:
            body["definition"] = self.definition
        if self.description is not None:
            body["description"] = self.description
        if self.display_name is not None:
            body["display_name"] = self.display_name
        if self.effective_parent_path is not None:
            body["effective_parent_path"] = self.effective_parent_path
        if self.etag is not None:
            body["etag"] = self.etag
        if self.name is not None:
            body["name"] = self.name
        if self.parent_path is not None:
            body["parent_path"] = self.parent_path
        if self.update_time is not None:
            body["update_time"] = self.update_time
        if self.warehouse_id is not None:
            body["warehouse_id"] = self.warehouse_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> GenieAgent:
        """Deserializes the GenieAgent from a dictionary."""
        return cls(
            create_time=_timestamp(d, "create_time"),
            definition=_from_dict(d, "definition", GenieAgentDefinition),
            description=d.get("description", None),
            display_name=d.get("display_name", None),
            effective_parent_path=d.get("effective_parent_path", None),
            etag=d.get("etag", None),
            name=d.get("name", None),
            parent_path=d.get("parent_path", None),
            update_time=_timestamp(d, "update_time"),
            warehouse_id=d.get("warehouse_id", None),
        )


@dataclass
class GenieAgentBenchmarkAnswer:
    """The expected answer to a benchmark question."""

    format: GenieAgentBenchmarkAnswerFormat
    """The format of the answer."""

    content: str
    """The answer."""

    def as_dict(self) -> dict:
        """Serializes the GenieAgentBenchmarkAnswer into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.content is not None:
            body["content"] = self.content
        if self.format is not None:
            body["format"] = self.format.value
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the GenieAgentBenchmarkAnswer into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.content is not None:
            body["content"] = self.content
        if self.format is not None:
            body["format"] = self.format
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> GenieAgentBenchmarkAnswer:
        """Deserializes the GenieAgentBenchmarkAnswer from a dictionary."""
        return cls(content=d.get("content", None), format=_enum(d, "format", GenieAgentBenchmarkAnswerFormat))


class GenieAgentBenchmarkAnswerFormat(Enum):
    """The format of a benchmark answer."""

    GENIE_AGENT_BENCHMARK_ANSWER_FORMAT_SQL = "GENIE_AGENT_BENCHMARK_ANSWER_FORMAT_SQL"


@dataclass
class GenieAgentBenchmarkQuestion:
    """A benchmark question with its expected answer."""

    id: str
    """Identifier of the question: 32 lowercase hexadecimal characters, unique within the Genie Agent."""

    question: str
    """The question."""

    answer: Optional[List[GenieAgentBenchmarkAnswer]] = None
    """The expected answer. At most one answer is supported; omit it when the question has no expected
    answer."""

    evaluation_note: Optional[str] = None
    """Notes on how to evaluate answers to the question."""

    def as_dict(self) -> dict:
        """Serializes the GenieAgentBenchmarkQuestion into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.answer:
            body["answer"] = [v.as_dict() for v in self.answer]
        if self.evaluation_note is not None:
            body["evaluation_note"] = self.evaluation_note
        if self.id is not None:
            body["id"] = self.id
        if self.question is not None:
            body["question"] = self.question
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the GenieAgentBenchmarkQuestion into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.answer:
            body["answer"] = self.answer
        if self.evaluation_note is not None:
            body["evaluation_note"] = self.evaluation_note
        if self.id is not None:
            body["id"] = self.id
        if self.question is not None:
            body["question"] = self.question
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> GenieAgentBenchmarkQuestion:
        """Deserializes the GenieAgentBenchmarkQuestion from a dictionary."""
        return cls(
            answer=_repeated_dict(d, "answer", GenieAgentBenchmarkAnswer),
            evaluation_note=d.get("evaluation_note", None),
            id=d.get("id", None),
            question=d.get("question", None),
        )


@dataclass
class GenieAgentBenchmarks:
    """Benchmarks for evaluating a Genie Agent."""

    questions: Optional[List[GenieAgentBenchmarkQuestion]] = None
    """The benchmark questions, sorted by ``id`` in descending order."""

    def as_dict(self) -> dict:
        """Serializes the GenieAgentBenchmarks into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.questions:
            body["questions"] = [v.as_dict() for v in self.questions]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the GenieAgentBenchmarks into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.questions:
            body["questions"] = self.questions
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> GenieAgentBenchmarks:
        """Deserializes the GenieAgentBenchmarks from a dictionary."""
        return cls(questions=_repeated_dict(d, "questions", GenieAgentBenchmarkQuestion))


@dataclass
class GenieAgentColumnConfig:
    """Settings for one column of a table or metric view."""

    column: str
    """The name of the column. Must exist in the table or metric view."""

    description: Optional[str] = None
    """Description of the column, overriding its Unity Catalog comment."""

    display_name: Optional[str] = None
    """Display name of the column in the Genie Agent. Accepted only where column display names are
    enabled for the workspace."""

    enable_entity_matching: Optional[bool] = None
    """Whether the Genie Agent indexes the column's values to match them in questions."""

    enable_format_assistance: Optional[bool] = None
    """Whether the Genie Agent samples example values from the column to learn its format."""

    exclude: Optional[bool] = None
    """Whether the column is hidden from the Genie Agent."""

    synonyms: Optional[List[str]] = None
    """Synonyms for the column name."""

    def as_dict(self) -> dict:
        """Serializes the GenieAgentColumnConfig into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.column is not None:
            body["column"] = self.column
        if self.description is not None:
            body["description"] = self.description
        if self.display_name is not None:
            body["display_name"] = self.display_name
        if self.enable_entity_matching is not None:
            body["enable_entity_matching"] = self.enable_entity_matching
        if self.enable_format_assistance is not None:
            body["enable_format_assistance"] = self.enable_format_assistance
        if self.exclude is not None:
            body["exclude"] = self.exclude
        if self.synonyms:
            body["synonyms"] = [v for v in self.synonyms]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the GenieAgentColumnConfig into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.column is not None:
            body["column"] = self.column
        if self.description is not None:
            body["description"] = self.description
        if self.display_name is not None:
            body["display_name"] = self.display_name
        if self.enable_entity_matching is not None:
            body["enable_entity_matching"] = self.enable_entity_matching
        if self.enable_format_assistance is not None:
            body["enable_format_assistance"] = self.enable_format_assistance
        if self.exclude is not None:
            body["exclude"] = self.exclude
        if self.synonyms:
            body["synonyms"] = self.synonyms
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> GenieAgentColumnConfig:
        """Deserializes the GenieAgentColumnConfig from a dictionary."""
        return cls(
            column=d.get("column", None),
            description=d.get("description", None),
            display_name=d.get("display_name", None),
            enable_entity_matching=d.get("enable_entity_matching", None),
            enable_format_assistance=d.get("enable_format_assistance", None),
            exclude=d.get("exclude", None),
            synonyms=d.get("synonyms", None),
        )


@dataclass
class GenieAgentConfig:
    """General settings of a Genie Agent. The warehouse, display name, and description are separate
    fields of the Genie Agent."""

    sample_questions: Optional[List[GenieAgentSampleQuestion]] = None
    """Sample questions shown to users of the Genie Agent, sorted by ``id``."""

    def as_dict(self) -> dict:
        """Serializes the GenieAgentConfig into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.sample_questions:
            body["sample_questions"] = [v.as_dict() for v in self.sample_questions]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the GenieAgentConfig into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.sample_questions:
            body["sample_questions"] = self.sample_questions
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> GenieAgentConfig:
        """Deserializes the GenieAgentConfig from a dictionary."""
        return cls(sample_questions=_repeated_dict(d, "sample_questions", GenieAgentSampleQuestion))


@dataclass
class GenieAgentDataSources:
    """The data a Genie Agent can access."""

    mcp_connections: Optional[List[GenieAgentMcpConnection]] = None
    """Unity Catalog MCP connections, sorted by ``mcp_connection``."""

    tables: Optional[List[GenieAgentTable]] = None
    """Unity Catalog tables, views, and metric views, in the order they were added."""

    volumes: Optional[List[GenieAgentVolume]] = None
    """Unity Catalog volumes, in the order they were added."""

    def as_dict(self) -> dict:
        """Serializes the GenieAgentDataSources into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.mcp_connections:
            body["mcp_connections"] = [v.as_dict() for v in self.mcp_connections]
        if self.tables:
            body["tables"] = [v.as_dict() for v in self.tables]
        if self.volumes:
            body["volumes"] = [v.as_dict() for v in self.volumes]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the GenieAgentDataSources into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.mcp_connections:
            body["mcp_connections"] = self.mcp_connections
        if self.tables:
            body["tables"] = self.tables
        if self.volumes:
            body["volumes"] = self.volumes
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> GenieAgentDataSources:
        """Deserializes the GenieAgentDataSources from a dictionary."""
        return cls(
            mcp_connections=_repeated_dict(d, "mcp_connections", GenieAgentMcpConnection),
            tables=_repeated_dict(d, "tables", GenieAgentTable),
            volumes=_repeated_dict(d, "volumes", GenieAgentVolume),
        )


@dataclass
class GenieAgentDefinition:
    """The definition of a Genie Agent."""

    benchmarks: Optional[GenieAgentBenchmarks] = None
    """Benchmarks for evaluating the quality of the Genie Agent's answers."""

    config: Optional[GenieAgentConfig] = None
    """General settings of the Genie Agent."""

    data_sources: Optional[GenieAgentDataSources] = None
    """The data the Genie Agent can access."""

    instructions: Optional[GenieAgentInstructions] = None
    """Instructions and SQL that guide how the Genie Agent answers questions."""

    def as_dict(self) -> dict:
        """Serializes the GenieAgentDefinition into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.benchmarks:
            body["benchmarks"] = self.benchmarks.as_dict()
        if self.config:
            body["config"] = self.config.as_dict()
        if self.data_sources:
            body["data_sources"] = self.data_sources.as_dict()
        if self.instructions:
            body["instructions"] = self.instructions.as_dict()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the GenieAgentDefinition into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.benchmarks:
            body["benchmarks"] = self.benchmarks
        if self.config:
            body["config"] = self.config
        if self.data_sources:
            body["data_sources"] = self.data_sources
        if self.instructions:
            body["instructions"] = self.instructions
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> GenieAgentDefinition:
        """Deserializes the GenieAgentDefinition from a dictionary."""
        return cls(
            benchmarks=_from_dict(d, "benchmarks", GenieAgentBenchmarks),
            config=_from_dict(d, "config", GenieAgentConfig),
            data_sources=_from_dict(d, "data_sources", GenieAgentDataSources),
            instructions=_from_dict(d, "instructions", GenieAgentInstructions),
        )


@dataclass
class GenieAgentExampleQuestionSql:
    """An example question paired with the SQL that answers it."""

    id: str
    """Identifier of the example: 32 lowercase hexadecimal characters, unique within the Genie Agent."""

    question: str
    """The question."""

    sql: str
    """The SQL that answers the question."""

    parameters: Optional[List[GenieAgentSqlParameter]] = None
    """Parameters used in the SQL, in the order given."""

    usage_guidance: Optional[str] = None
    """Guidance on when to use this example."""

    def as_dict(self) -> dict:
        """Serializes the GenieAgentExampleQuestionSql into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.id is not None:
            body["id"] = self.id
        if self.parameters:
            body["parameters"] = [v.as_dict() for v in self.parameters]
        if self.question is not None:
            body["question"] = self.question
        if self.sql is not None:
            body["sql"] = self.sql
        if self.usage_guidance is not None:
            body["usage_guidance"] = self.usage_guidance
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the GenieAgentExampleQuestionSql into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.id is not None:
            body["id"] = self.id
        if self.parameters:
            body["parameters"] = self.parameters
        if self.question is not None:
            body["question"] = self.question
        if self.sql is not None:
            body["sql"] = self.sql
        if self.usage_guidance is not None:
            body["usage_guidance"] = self.usage_guidance
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> GenieAgentExampleQuestionSql:
        """Deserializes the GenieAgentExampleQuestionSql from a dictionary."""
        return cls(
            id=d.get("id", None),
            parameters=_repeated_dict(d, "parameters", GenieAgentSqlParameter),
            question=d.get("question", None),
            sql=d.get("sql", None),
            usage_guidance=d.get("usage_guidance", None),
        )


@dataclass
class GenieAgentInstructions:
    """Instructions and SQL that guide how a Genie Agent answers questions."""

    example_question_sqls: Optional[List[GenieAgentExampleQuestionSql]] = None
    """Example questions paired with the SQL that answers them."""

    join_specs: Optional[List[GenieAgentJoinSpec]] = None
    """Predefined joins between tables or metric views."""

    sql_functions: Optional[List[GenieAgentSqlFunction]] = None
    """Unity Catalog SQL functions the generated SQL may call."""

    sql_snippets: Optional[GenieAgentSqlSnippets] = None
    """Reusable SQL filters, expressions, and measures."""

    text_instructions: Optional[List[GenieAgentTextInstruction]] = None
    """General text instructions. At most one text instruction is supported."""

    def as_dict(self) -> dict:
        """Serializes the GenieAgentInstructions into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.example_question_sqls:
            body["example_question_sqls"] = [v.as_dict() for v in self.example_question_sqls]
        if self.join_specs:
            body["join_specs"] = [v.as_dict() for v in self.join_specs]
        if self.sql_functions:
            body["sql_functions"] = [v.as_dict() for v in self.sql_functions]
        if self.sql_snippets:
            body["sql_snippets"] = self.sql_snippets.as_dict()
        if self.text_instructions:
            body["text_instructions"] = [v.as_dict() for v in self.text_instructions]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the GenieAgentInstructions into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.example_question_sqls:
            body["example_question_sqls"] = self.example_question_sqls
        if self.join_specs:
            body["join_specs"] = self.join_specs
        if self.sql_functions:
            body["sql_functions"] = self.sql_functions
        if self.sql_snippets:
            body["sql_snippets"] = self.sql_snippets
        if self.text_instructions:
            body["text_instructions"] = self.text_instructions
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> GenieAgentInstructions:
        """Deserializes the GenieAgentInstructions from a dictionary."""
        return cls(
            example_question_sqls=_repeated_dict(d, "example_question_sqls", GenieAgentExampleQuestionSql),
            join_specs=_repeated_dict(d, "join_specs", GenieAgentJoinSpec),
            sql_functions=_repeated_dict(d, "sql_functions", GenieAgentSqlFunction),
            sql_snippets=_from_dict(d, "sql_snippets", GenieAgentSqlSnippets),
            text_instructions=_repeated_dict(d, "text_instructions", GenieAgentTextInstruction),
        )


class GenieAgentJoinRelationshipType(Enum):
    """How the rows of the two sides of a join relate."""

    GENIE_AGENT_JOIN_RELATIONSHIP_TYPE_MANY_TO_MANY = "GENIE_AGENT_JOIN_RELATIONSHIP_TYPE_MANY_TO_MANY"
    GENIE_AGENT_JOIN_RELATIONSHIP_TYPE_MANY_TO_ONE = "GENIE_AGENT_JOIN_RELATIONSHIP_TYPE_MANY_TO_ONE"
    GENIE_AGENT_JOIN_RELATIONSHIP_TYPE_ONE_TO_MANY = "GENIE_AGENT_JOIN_RELATIONSHIP_TYPE_ONE_TO_MANY"
    GENIE_AGENT_JOIN_RELATIONSHIP_TYPE_ONE_TO_ONE = "GENIE_AGENT_JOIN_RELATIONSHIP_TYPE_ONE_TO_ONE"


@dataclass
class GenieAgentJoinSource:
    """One side of a join."""

    identifier: str
    """The full three-level name of the table or metric view."""

    alias: Optional[str] = None
    """The alias the join condition uses for this side."""

    def as_dict(self) -> dict:
        """Serializes the GenieAgentJoinSource into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.alias is not None:
            body["alias"] = self.alias
        if self.identifier is not None:
            body["identifier"] = self.identifier
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the GenieAgentJoinSource into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.alias is not None:
            body["alias"] = self.alias
        if self.identifier is not None:
            body["identifier"] = self.identifier
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> GenieAgentJoinSource:
        """Deserializes the GenieAgentJoinSource from a dictionary."""
        return cls(alias=d.get("alias", None), identifier=d.get("identifier", None))


@dataclass
class GenieAgentJoinSpec:
    """A predefined join between two tables or metric views."""

    id: str
    """Identifier of the join: 32 lowercase hexadecimal characters, unique within the Genie Agent."""

    left: GenieAgentJoinSource
    """The left side of the join."""

    right: GenieAgentJoinSource
    """The right side of the join."""

    sql: str
    """The join condition, for example ``orders.customer_id = customers.id``."""

    comment: Optional[str] = None
    """Description of the join's purpose."""

    instruction: Optional[str] = None
    """Guidance on when to use the join."""

    relationship_type: Optional[GenieAgentJoinRelationshipType] = None
    """How the rows of the two sides relate."""

    def as_dict(self) -> dict:
        """Serializes the GenieAgentJoinSpec into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.comment is not None:
            body["comment"] = self.comment
        if self.id is not None:
            body["id"] = self.id
        if self.instruction is not None:
            body["instruction"] = self.instruction
        if self.left:
            body["left"] = self.left.as_dict()
        if self.relationship_type is not None:
            body["relationship_type"] = self.relationship_type.value
        if self.right:
            body["right"] = self.right.as_dict()
        if self.sql is not None:
            body["sql"] = self.sql
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the GenieAgentJoinSpec into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.comment is not None:
            body["comment"] = self.comment
        if self.id is not None:
            body["id"] = self.id
        if self.instruction is not None:
            body["instruction"] = self.instruction
        if self.left:
            body["left"] = self.left
        if self.relationship_type is not None:
            body["relationship_type"] = self.relationship_type
        if self.right:
            body["right"] = self.right
        if self.sql is not None:
            body["sql"] = self.sql
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> GenieAgentJoinSpec:
        """Deserializes the GenieAgentJoinSpec from a dictionary."""
        return cls(
            comment=d.get("comment", None),
            id=d.get("id", None),
            instruction=d.get("instruction", None),
            left=_from_dict(d, "left", GenieAgentJoinSource),
            relationship_type=_enum(d, "relationship_type", GenieAgentJoinRelationshipType),
            right=_from_dict(d, "right", GenieAgentJoinSource),
            sql=d.get("sql", None),
        )


@dataclass
class GenieAgentMcpConnection:
    """A Unity Catalog MCP connection the Genie Agent can use."""

    mcp_connection: str
    """The name of the Unity Catalog connection, for example ``system.ai.google_calendar``."""

    def as_dict(self) -> dict:
        """Serializes the GenieAgentMcpConnection into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.mcp_connection is not None:
            body["mcp_connection"] = self.mcp_connection
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the GenieAgentMcpConnection into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.mcp_connection is not None:
            body["mcp_connection"] = self.mcp_connection
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> GenieAgentMcpConnection:
        """Deserializes the GenieAgentMcpConnection from a dictionary."""
        return cls(mcp_connection=d.get("mcp_connection", None))


@dataclass
class GenieAgentSampleQuestion:
    """A sample question shown to users of the Genie Agent."""

    id: str
    """Identifier of the sample question: 32 lowercase hexadecimal characters, unique within the Genie
    Agent."""

    question: str
    """The text of the question."""

    def as_dict(self) -> dict:
        """Serializes the GenieAgentSampleQuestion into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.id is not None:
            body["id"] = self.id
        if self.question is not None:
            body["question"] = self.question
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the GenieAgentSampleQuestion into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.id is not None:
            body["id"] = self.id
        if self.question is not None:
            body["question"] = self.question
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> GenieAgentSampleQuestion:
        """Deserializes the GenieAgentSampleQuestion from a dictionary."""
        return cls(id=d.get("id", None), question=d.get("question", None))


@dataclass
class GenieAgentSqlExpression:
    """A reusable non-aggregated SQL expression (dimension)."""

    id: str
    """Identifier of the expression: 32 lowercase hexadecimal characters, unique within the Genie
    Agent."""

    sql: str
    """The SQL of the expression."""

    alias: Optional[str] = None
    """The alias the Genie Agent uses for the expression in generated SQL."""

    display_name: Optional[str] = None
    """Display name of the expression."""

    instruction: Optional[str] = None
    """Guidance on when to use the expression."""

    synonyms: Optional[List[str]] = None
    """Synonyms for the expression."""

    def as_dict(self) -> dict:
        """Serializes the GenieAgentSqlExpression into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.alias is not None:
            body["alias"] = self.alias
        if self.display_name is not None:
            body["display_name"] = self.display_name
        if self.id is not None:
            body["id"] = self.id
        if self.instruction is not None:
            body["instruction"] = self.instruction
        if self.sql is not None:
            body["sql"] = self.sql
        if self.synonyms:
            body["synonyms"] = [v for v in self.synonyms]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the GenieAgentSqlExpression into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.alias is not None:
            body["alias"] = self.alias
        if self.display_name is not None:
            body["display_name"] = self.display_name
        if self.id is not None:
            body["id"] = self.id
        if self.instruction is not None:
            body["instruction"] = self.instruction
        if self.sql is not None:
            body["sql"] = self.sql
        if self.synonyms:
            body["synonyms"] = self.synonyms
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> GenieAgentSqlExpression:
        """Deserializes the GenieAgentSqlExpression from a dictionary."""
        return cls(
            alias=d.get("alias", None),
            display_name=d.get("display_name", None),
            id=d.get("id", None),
            instruction=d.get("instruction", None),
            sql=d.get("sql", None),
            synonyms=d.get("synonyms", None),
        )


@dataclass
class GenieAgentSqlFilter:
    """A reusable SQL filter."""

    id: str
    """Identifier of the filter: 32 lowercase hexadecimal characters, unique within the Genie Agent."""

    sql: str
    """The SQL of the filter."""

    display_name: Optional[str] = None
    """Display name of the filter."""

    instruction: Optional[str] = None
    """Guidance on when to use the filter."""

    synonyms: Optional[List[str]] = None
    """Synonyms for the filter."""

    def as_dict(self) -> dict:
        """Serializes the GenieAgentSqlFilter into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.display_name is not None:
            body["display_name"] = self.display_name
        if self.id is not None:
            body["id"] = self.id
        if self.instruction is not None:
            body["instruction"] = self.instruction
        if self.sql is not None:
            body["sql"] = self.sql
        if self.synonyms:
            body["synonyms"] = [v for v in self.synonyms]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the GenieAgentSqlFilter into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.display_name is not None:
            body["display_name"] = self.display_name
        if self.id is not None:
            body["id"] = self.id
        if self.instruction is not None:
            body["instruction"] = self.instruction
        if self.sql is not None:
            body["sql"] = self.sql
        if self.synonyms:
            body["synonyms"] = self.synonyms
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> GenieAgentSqlFilter:
        """Deserializes the GenieAgentSqlFilter from a dictionary."""
        return cls(
            display_name=d.get("display_name", None),
            id=d.get("id", None),
            instruction=d.get("instruction", None),
            sql=d.get("sql", None),
            synonyms=d.get("synonyms", None),
        )


@dataclass
class GenieAgentSqlFunction:
    """A Unity Catalog SQL function the generated SQL may call."""

    id: str
    """Identifier of the entry: 32 lowercase hexadecimal characters, unique within the Genie Agent."""

    identifier: str
    """The full three-level name of the function, for example ``catalog.schema.function``."""

    def as_dict(self) -> dict:
        """Serializes the GenieAgentSqlFunction into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.id is not None:
            body["id"] = self.id
        if self.identifier is not None:
            body["identifier"] = self.identifier
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the GenieAgentSqlFunction into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.id is not None:
            body["id"] = self.id
        if self.identifier is not None:
            body["identifier"] = self.identifier
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> GenieAgentSqlFunction:
        """Deserializes the GenieAgentSqlFunction from a dictionary."""
        return cls(id=d.get("id", None), identifier=d.get("identifier", None))


@dataclass
class GenieAgentSqlMeasure:
    """A reusable aggregated SQL measure."""

    id: str
    """Identifier of the measure: 32 lowercase hexadecimal characters, unique within the Genie Agent."""

    sql: str
    """The SQL of the measure."""

    alias: Optional[str] = None
    """The alias the Genie Agent uses for the measure in generated SQL."""

    display_name: Optional[str] = None
    """Display name of the measure."""

    instruction: Optional[str] = None
    """Guidance on when to use the measure."""

    synonyms: Optional[List[str]] = None
    """Synonyms for the measure."""

    def as_dict(self) -> dict:
        """Serializes the GenieAgentSqlMeasure into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.alias is not None:
            body["alias"] = self.alias
        if self.display_name is not None:
            body["display_name"] = self.display_name
        if self.id is not None:
            body["id"] = self.id
        if self.instruction is not None:
            body["instruction"] = self.instruction
        if self.sql is not None:
            body["sql"] = self.sql
        if self.synonyms:
            body["synonyms"] = [v for v in self.synonyms]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the GenieAgentSqlMeasure into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.alias is not None:
            body["alias"] = self.alias
        if self.display_name is not None:
            body["display_name"] = self.display_name
        if self.id is not None:
            body["id"] = self.id
        if self.instruction is not None:
            body["instruction"] = self.instruction
        if self.sql is not None:
            body["sql"] = self.sql
        if self.synonyms:
            body["synonyms"] = self.synonyms
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> GenieAgentSqlMeasure:
        """Deserializes the GenieAgentSqlMeasure from a dictionary."""
        return cls(
            alias=d.get("alias", None),
            display_name=d.get("display_name", None),
            id=d.get("id", None),
            instruction=d.get("instruction", None),
            sql=d.get("sql", None),
            synonyms=d.get("synonyms", None),
        )


@dataclass
class GenieAgentSqlParameter:
    """A parameter of a parameterized SQL example."""

    name: str
    """The name of the parameter in the SQL."""

    default_value: Optional[GenieAgentSqlParameterDefaultValue] = None
    """The parameter's default value."""

    description: Optional[str] = None
    """Description of the parameter."""

    type_hint: Optional[str] = None
    """The parameter's data type, for example ``STRING`` or ``INTEGER``."""

    def as_dict(self) -> dict:
        """Serializes the GenieAgentSqlParameter into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.default_value:
            body["default_value"] = self.default_value.as_dict()
        if self.description is not None:
            body["description"] = self.description
        if self.name is not None:
            body["name"] = self.name
        if self.type_hint is not None:
            body["type_hint"] = self.type_hint
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the GenieAgentSqlParameter into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.default_value:
            body["default_value"] = self.default_value
        if self.description is not None:
            body["description"] = self.description
        if self.name is not None:
            body["name"] = self.name
        if self.type_hint is not None:
            body["type_hint"] = self.type_hint
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> GenieAgentSqlParameter:
        """Deserializes the GenieAgentSqlParameter from a dictionary."""
        return cls(
            default_value=_from_dict(d, "default_value", GenieAgentSqlParameterDefaultValue),
            description=d.get("description", None),
            name=d.get("name", None),
            type_hint=d.get("type_hint", None),
        )


@dataclass
class GenieAgentSqlParameterDefaultRange:
    """A range of default values for a SQL parameter."""

    max: Optional[str] = None
    """The upper end of the range."""

    min: Optional[str] = None
    """The lower end of the range."""

    def as_dict(self) -> dict:
        """Serializes the GenieAgentSqlParameterDefaultRange into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.max is not None:
            body["max"] = self.max
        if self.min is not None:
            body["min"] = self.min
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the GenieAgentSqlParameterDefaultRange into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.max is not None:
            body["max"] = self.max
        if self.min is not None:
            body["min"] = self.min
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> GenieAgentSqlParameterDefaultRange:
        """Deserializes the GenieAgentSqlParameterDefaultRange from a dictionary."""
        return cls(max=d.get("max", None), min=d.get("min", None))


@dataclass
class GenieAgentSqlParameterDefaultValue:
    """The default value of a SQL parameter: a list of values or a range."""

    value_range: Optional[GenieAgentSqlParameterDefaultRange] = None
    """The default range."""

    values: Optional[List[str]] = None
    """The default values. A single default is a one-element list."""

    def as_dict(self) -> dict:
        """Serializes the GenieAgentSqlParameterDefaultValue into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.value_range:
            body["value_range"] = self.value_range.as_dict()
        if self.values:
            body["values"] = [v for v in self.values]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the GenieAgentSqlParameterDefaultValue into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.value_range:
            body["value_range"] = self.value_range
        if self.values:
            body["values"] = self.values
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> GenieAgentSqlParameterDefaultValue:
        """Deserializes the GenieAgentSqlParameterDefaultValue from a dictionary."""
        return cls(
            value_range=_from_dict(d, "value_range", GenieAgentSqlParameterDefaultRange), values=d.get("values", None)
        )


@dataclass
class GenieAgentSqlSnippets:
    """Reusable SQL snippets."""

    expressions: Optional[List[GenieAgentSqlExpression]] = None
    """Non-aggregated expressions (dimensions), such as ``price * units``."""

    filters: Optional[List[GenieAgentSqlFilter]] = None
    """Filters, such as ``state = 'CA'``."""

    measures: Optional[List[GenieAgentSqlMeasure]] = None
    """Aggregated measures, such as ``SUM(price * units)``."""

    def as_dict(self) -> dict:
        """Serializes the GenieAgentSqlSnippets into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.expressions:
            body["expressions"] = [v.as_dict() for v in self.expressions]
        if self.filters:
            body["filters"] = [v.as_dict() for v in self.filters]
        if self.measures:
            body["measures"] = [v.as_dict() for v in self.measures]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the GenieAgentSqlSnippets into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.expressions:
            body["expressions"] = self.expressions
        if self.filters:
            body["filters"] = self.filters
        if self.measures:
            body["measures"] = self.measures
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> GenieAgentSqlSnippets:
        """Deserializes the GenieAgentSqlSnippets from a dictionary."""
        return cls(
            expressions=_repeated_dict(d, "expressions", GenieAgentSqlExpression),
            filters=_repeated_dict(d, "filters", GenieAgentSqlFilter),
            measures=_repeated_dict(d, "measures", GenieAgentSqlMeasure),
        )


@dataclass
class GenieAgentTable:
    """A Unity Catalog table, view, or metric view the Genie Agent can access."""

    identifier: str
    """The full three-level name, for example ``catalog.schema.table``."""

    column_configs: Optional[List[GenieAgentColumnConfig]] = None
    """Column settings for the table, sorted by ``column``."""

    description: Optional[str] = None
    """Description of the table."""

    def as_dict(self) -> dict:
        """Serializes the GenieAgentTable into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.column_configs:
            body["column_configs"] = [v.as_dict() for v in self.column_configs]
        if self.description is not None:
            body["description"] = self.description
        if self.identifier is not None:
            body["identifier"] = self.identifier
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the GenieAgentTable into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.column_configs:
            body["column_configs"] = self.column_configs
        if self.description is not None:
            body["description"] = self.description
        if self.identifier is not None:
            body["identifier"] = self.identifier
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> GenieAgentTable:
        """Deserializes the GenieAgentTable from a dictionary."""
        return cls(
            column_configs=_repeated_dict(d, "column_configs", GenieAgentColumnConfig),
            description=d.get("description", None),
            identifier=d.get("identifier", None),
        )


@dataclass
class GenieAgentTextInstruction:
    """A general text instruction for the Genie Agent."""

    id: str
    """Identifier of the instruction: 32 lowercase hexadecimal characters, unique within the Genie
    Agent."""

    content: str
    """The text of the instruction."""

    def as_dict(self) -> dict:
        """Serializes the GenieAgentTextInstruction into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.content is not None:
            body["content"] = self.content
        if self.id is not None:
            body["id"] = self.id
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the GenieAgentTextInstruction into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.content is not None:
            body["content"] = self.content
        if self.id is not None:
            body["id"] = self.id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> GenieAgentTextInstruction:
        """Deserializes the GenieAgentTextInstruction from a dictionary."""
        return cls(content=d.get("content", None), id=d.get("id", None))


class GenieAgentView(Enum):
    """The fields returned for each Genie Agent in a list response."""

    GENIE_AGENT_VIEW_BASIC = "GENIE_AGENT_VIEW_BASIC"
    GENIE_AGENT_VIEW_FULL = "GENIE_AGENT_VIEW_FULL"


@dataclass
class GenieAgentVolume:
    """A Unity Catalog volume the Genie Agent can access."""

    path: str
    """The volume path, for example ``/Volumes/catalog/schema/volume``. May name a directory or file
    within the volume."""

    description: Optional[str] = None
    """Description of the volume."""

    def as_dict(self) -> dict:
        """Serializes the GenieAgentVolume into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.description is not None:
            body["description"] = self.description
        if self.path is not None:
            body["path"] = self.path
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the GenieAgentVolume into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.description is not None:
            body["description"] = self.description
        if self.path is not None:
            body["path"] = self.path
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> GenieAgentVolume:
        """Deserializes the GenieAgentVolume from a dictionary."""
        return cls(description=d.get("description", None), path=d.get("path", None))


@dataclass
class ListGenieAgentsResponse:
    """Response for a list request: a page of Genie Agents plus the token for the next page."""

    genie_agents: Optional[List[GenieAgent]] = None
    """The Genie Agents, with the fields selected by the request's ``view``."""

    next_page_token: Optional[str] = None
    """Token to get the next page of results."""

    unreachable: Optional[List[str]] = None
    """Resource names, in the form ``agents/{genie_agent_id}``, of Genie Agents in this page that could
    not be read and are omitted from ``genie_agents``. Populated only for ``GENIE_AGENT_VIEW_FULL``.
    To see why, get the Genie Agent by name; to retry, repeat the request. Other kinds of resource
    names may be added to this field in the future."""

    def as_dict(self) -> dict:
        """Serializes the ListGenieAgentsResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.genie_agents:
            body["genie_agents"] = [v.as_dict() for v in self.genie_agents]
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        if self.unreachable:
            body["unreachable"] = [v for v in self.unreachable]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ListGenieAgentsResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.genie_agents:
            body["genie_agents"] = self.genie_agents
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        if self.unreachable:
            body["unreachable"] = self.unreachable
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ListGenieAgentsResponse:
        """Deserializes the ListGenieAgentsResponse from a dictionary."""
        return cls(
            genie_agents=_repeated_dict(d, "genie_agents", GenieAgent),
            next_page_token=d.get("next_page_token", None),
            unreachable=d.get("unreachable", None),
        )


class GenieAgentsAPI:
    """Genie provides a no-code experience for business users, powered by AI/BI. Analysts set up Genie Agents
    that business users can use to ask questions using natural language. Genie uses data registered to Unity
    Catalog and requires at least CAN USE permission on a Pro or Serverless SQL warehouse. Also, Databricks
    Assistant must be enabled."""

    def __init__(self, api_client):
        self._api = api_client

    def create_genie_agent(self, genie_agent: GenieAgent, *, genie_agent_id: Optional[str] = None) -> GenieAgent:
        """Creates a Genie Agent.

        :param genie_agent: :class:`GenieAgent`
          The Genie Agent to create.
        :param genie_agent_id: str (optional)
          The ID for the new Genie Agent: 32 lowercase hexadecimal characters (a UUID without dashes), not all
          zeros. Assigned by the server if omitted. Fails with ALREADY_EXISTS if the ID is in use in the
          workspace, including by a Genie Agent in the trash, or PERMISSION_DENIED if the caller cannot view
          the Genie Agent using it.

        :returns: :class:`GenieAgent`
        """

        body = genie_agent.as_dict()
        query = {}
        if genie_agent_id is not None:
            query["genie_agent_id"] = genie_agent_id
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("POST", "/api/2.0/genie/agents", query=query, body=body, headers=headers)
        return GenieAgent.from_dict(res)

    def delete_genie_agent(self, name: str, *, etag: Optional[str] = None):
        """Deletes a Genie Agent, moving it to trash.

        :param name: str
          The resource name of the Genie Agent to delete, in the form ``agents/{genie_agent_id}``.
        :param etag: str (optional)
          Etag from a previous read. On mismatch the delete fails with ABORTED and nothing is deleted.


        """

        query = {}
        if etag is not None:
            query["etag"] = etag
        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        self._api.do("DELETE", f"/api/2.0/genie/{name}", query=query, headers=headers)

    def get_genie_agent(self, name: str) -> GenieAgent:
        """Gets a Genie Agent.

        :param name: str
          The resource name of the Genie Agent to retrieve, in the form ``agents/{genie_agent_id}``.

        :returns: :class:`GenieAgent`
        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("GET", f"/api/2.0/genie/{name}", headers=headers)
        return GenieAgent.from_dict(res)

    def list_genie_agents(
        self,
        *,
        page_size: Optional[int] = None,
        page_token: Optional[str] = None,
        view: Optional[GenieAgentView] = None,
    ) -> Iterator[GenieAgent]:
        """Lists the Genie Agents in the workspace. Genie Agents created from an integration (for example, from a
        dashboard) are not listed.

        :param page_size: int (optional)
          Maximum number of Genie Agents to return per page. Defaults to 20 when unset or 0; values above 100
          are coerced to 100. Negative values are rejected with INVALID_PARAMETER_VALUE. With
          ``GENIE_AGENT_VIEW_FULL``, a smaller per-page maximum applies.
        :param page_token: str (optional)
          Pagination token from a previous response's ``next_page_token``. A token that was not returned by
          this method is rejected with INVALID_PARAMETER_VALUE.
        :param view: :class:`GenieAgentView` (optional)
          The fields to return for each Genie Agent. Defaults to ``GENIE_AGENT_VIEW_BASIC``. Use
          ``GENIE_AGENT_VIEW_FULL`` only when the agent bodies are needed, since it returns smaller pages.

        :returns: Iterator over :class:`GenieAgent`
        """

        query = {}
        if page_size is not None:
            query["page_size"] = page_size
        if page_token is not None:
            query["page_token"] = page_token
        if view is not None:
            query["view"] = view.value
        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        while True:
            json = self._api.do("GET", "/api/2.0/genie/agents", query=query, headers=headers)
            if "genie_agents" in json:
                for v in json["genie_agents"]:
                    yield GenieAgent.from_dict(v)
            if "next_page_token" not in json or not json["next_page_token"]:
                return
            query["page_token"] = json["next_page_token"]

    def update_genie_agent(
        self, name: str, genie_agent: GenieAgent, update_mask: FieldMask, *, etag: Optional[str] = None
    ) -> GenieAgent:
        """Updates a Genie Agent. Only the fields named in update_mask are applied.

        :param name: str
          The resource name of the Genie Agent, in the form ``agents/{genie_agent_id}``. Ignored on create.
        :param genie_agent: :class:`GenieAgent`
          The Genie Agent to update. Its ``name`` identifies the resource; fields named in update_mask are
          applied.
        :param update_mask: FieldMask
          The set of fields to update. The mask is required and must name at least one field; an empty or
          absent mask is rejected with INVALID_PARAMETER_VALUE, as is a path that is not an updatable field.

          A field named in the mask takes the value from ``genie_agent``, even when it is unset there: an
          unset ``description`` is cleared; an unset ``display_name``, ``warehouse_id``, or ``definition`` is
          rejected with INVALID_PARAMETER_VALUE; an unset ``parent_path`` is cleared without moving the Genie
          Agent. ``definition`` is replaced as a whole; paths within it are not supported.

          The special value ``*`` replaces the whole Genie Agent, as if every updatable field were named. It
          must be the only path in the mask. Prefer naming fields explicitly: with ``*``, any field added to
          Genie Agent later is also replaced, so a client unaware of it may clear it.
        :param etag: str (optional)
          Etag from a previous read. On mismatch the update fails with ABORTED (metadata changes may already
          be applied); get the agent and retry. May return TEMPORARILY_UNAVAILABLE.

        :returns: :class:`GenieAgent`
        """

        body = genie_agent.as_dict()
        query = {}
        if etag is not None:
            query["etag"] = etag
        if update_mask is not None:
            query["update_mask"] = update_mask.ToJsonString()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("PATCH", f"/api/2.0/genie/{name}", query=query, body=body, headers=headers)
        return GenieAgent.from_dict(res)
