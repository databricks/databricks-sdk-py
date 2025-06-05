# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

from __future__ import annotations

import logging
from dataclasses import dataclass
from enum import Enum
from typing import Any, Dict, List, Optional

from ._internal import _enum, _from_dict, _repeated_dict

_LOG = logging.getLogger("databricks.sdk")


# all definitions in this file are in alphabetical order


@dataclass
class CancelCustomLlmOptimizationRunRequest:
    id: Optional[str] = None


@dataclass
class CancelResponse:
    def as_dict(self) -> dict:
        """Serializes the CancelResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the CancelResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> CancelResponse:
        """Deserializes the CancelResponse from a dictionary."""
        return cls()


@dataclass
class CustomLlm:
    name: str
    """Name of the custom LLM"""

    instructions: str
    """Instructions for the custom LLM to follow"""

    optimization_state: State
    """If optimization is kicked off, tracks the state of the custom LLM"""

    agent_artifact_path: Optional[str] = None

    creation_time: Optional[str] = None
    """Creation timestamp of the custom LLM"""

    creator: Optional[str] = None
    """Creator of the custom LLM"""

    datasets: Optional[List[Dataset]] = None
    """Datasets used for training and evaluating the model, not for inference"""

    endpoint_name: Optional[str] = None
    """Name of the endpoint that will be used to serve the custom LLM"""

    guidelines: Optional[List[str]] = None
    """Guidelines for the custom LLM to adhere to"""

    id: Optional[str] = None

    def as_dict(self) -> dict:
        """Serializes the CustomLlm into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.agent_artifact_path is not None:
            body["agent_artifact_path"] = self.agent_artifact_path
        if self.creation_time is not None:
            body["creation_time"] = self.creation_time
        if self.creator is not None:
            body["creator"] = self.creator
        if self.datasets:
            body["datasets"] = [v.as_dict() for v in self.datasets]
        if self.endpoint_name is not None:
            body["endpoint_name"] = self.endpoint_name
        if self.guidelines:
            body["guidelines"] = [v for v in self.guidelines]
        if self.id is not None:
            body["id"] = self.id
        if self.instructions is not None:
            body["instructions"] = self.instructions
        if self.name is not None:
            body["name"] = self.name
        if self.optimization_state is not None:
            body["optimization_state"] = self.optimization_state.value
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the CustomLlm into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.agent_artifact_path is not None:
            body["agent_artifact_path"] = self.agent_artifact_path
        if self.creation_time is not None:
            body["creation_time"] = self.creation_time
        if self.creator is not None:
            body["creator"] = self.creator
        if self.datasets:
            body["datasets"] = self.datasets
        if self.endpoint_name is not None:
            body["endpoint_name"] = self.endpoint_name
        if self.guidelines:
            body["guidelines"] = self.guidelines
        if self.id is not None:
            body["id"] = self.id
        if self.instructions is not None:
            body["instructions"] = self.instructions
        if self.name is not None:
            body["name"] = self.name
        if self.optimization_state is not None:
            body["optimization_state"] = self.optimization_state
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> CustomLlm:
        """Deserializes the CustomLlm from a dictionary."""
        return cls(
            agent_artifact_path=d.get("agent_artifact_path", None),
            creation_time=d.get("creation_time", None),
            creator=d.get("creator", None),
            datasets=_repeated_dict(d, "datasets", Dataset),
            endpoint_name=d.get("endpoint_name", None),
            guidelines=d.get("guidelines", None),
            id=d.get("id", None),
            instructions=d.get("instructions", None),
            name=d.get("name", None),
            optimization_state=_enum(d, "optimization_state", State),
        )


@dataclass
class Dataset:
    table: Table

    def as_dict(self) -> dict:
        """Serializes the Dataset into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.table:
            body["table"] = self.table.as_dict()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the Dataset into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.table:
            body["table"] = self.table
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> Dataset:
        """Deserializes the Dataset from a dictionary."""
        return cls(table=_from_dict(d, "table", Table))


@dataclass
class StartCustomLlmOptimizationRunRequest:
    id: Optional[str] = None
    """The Id of the tile."""


class State(Enum):
    """States of Custom LLM optimization lifecycle."""

    CANCELLED = "CANCELLED"
    COMPLETED = "COMPLETED"
    CREATED = "CREATED"
    FAILED = "FAILED"
    PENDING = "PENDING"
    RUNNING = "RUNNING"


@dataclass
class Table:
    table_path: str
    """Full UC table path in catalog.schema.table_name format"""

    request_col: str
    """Name of the request column"""

    response_col: Optional[str] = None
    """Optional: Name of the response column if the data is labeled"""

    def as_dict(self) -> dict:
        """Serializes the Table into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.request_col is not None:
            body["request_col"] = self.request_col
        if self.response_col is not None:
            body["response_col"] = self.response_col
        if self.table_path is not None:
            body["table_path"] = self.table_path
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the Table into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.request_col is not None:
            body["request_col"] = self.request_col
        if self.response_col is not None:
            body["response_col"] = self.response_col
        if self.table_path is not None:
            body["table_path"] = self.table_path
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> Table:
        """Deserializes the Table from a dictionary."""
        return cls(
            request_col=d.get("request_col", None),
            response_col=d.get("response_col", None),
            table_path=d.get("table_path", None),
        )


@dataclass
class UpdateCustomLlmRequest:
    custom_llm: CustomLlm
    """The CustomLlm containing the fields which should be updated."""

    update_mask: str
    """The list of the CustomLlm fields to update. These should correspond to the values (or lack
    thereof) present in `custom_llm`.
    
    The field mask must be a single string, with multiple fields separated by commas (no spaces).
    The field path is relative to the resource object, using a dot (`.`) to navigate sub-fields
    (e.g., `author.given_name`). Specification of elements in sequence or map fields is not allowed,
    as only the entire collection field can be specified. Field names must exactly match the
    resource field names.
    
    A field mask of `*` indicates full replacement. It’s recommended to always explicitly list the
    fields being updated and avoid using `*` wildcards, as it can lead to unintended results if the
    API changes in the future."""

    id: Optional[str] = None
    """The id of the custom llm"""

    def as_dict(self) -> dict:
        """Serializes the UpdateCustomLlmRequest into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.custom_llm:
            body["custom_llm"] = self.custom_llm.as_dict()
        if self.id is not None:
            body["id"] = self.id
        if self.update_mask is not None:
            body["update_mask"] = self.update_mask
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the UpdateCustomLlmRequest into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.custom_llm:
            body["custom_llm"] = self.custom_llm
        if self.id is not None:
            body["id"] = self.id
        if self.update_mask is not None:
            body["update_mask"] = self.update_mask
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> UpdateCustomLlmRequest:
        """Deserializes the UpdateCustomLlmRequest from a dictionary."""
        return cls(
            custom_llm=_from_dict(d, "custom_llm", CustomLlm),
            id=d.get("id", None),
            update_mask=d.get("update_mask", None),
        )


class CustomLlmsAPI:
    """The Custom LLMs service manages state and powers the UI for the Custom LLM product."""

    def __init__(self, api_client):
        self._api = api_client

    def cancel(self, id: str):
        """Cancel a Custom LLM Optimization Run.

        :param id: str


        """

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        self._api.do("POST", f"/api/2.0/custom-llms/{id}/optimize/cancel", headers=headers)

    def create(self, id: str) -> CustomLlm:
        """Start a Custom LLM Optimization Run.

        :param id: str
          The Id of the tile.

        :returns: :class:`CustomLlm`
        """

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do("POST", f"/api/2.0/custom-llms/{id}/optimize", headers=headers)
        return CustomLlm.from_dict(res)

    def get(self, id: str) -> CustomLlm:
        """Get a Custom LLM.

        :param id: str
          The id of the custom llm

        :returns: :class:`CustomLlm`
        """

        headers = {
            "Accept": "application/json",
        }

        res = self._api.do("GET", f"/api/2.0/custom-llms/{id}", headers=headers)
        return CustomLlm.from_dict(res)

    def update(self, id: str, custom_llm: CustomLlm, update_mask: str) -> CustomLlm:
        """Update a Custom LLM.

        :param id: str
          The id of the custom llm
        :param custom_llm: :class:`CustomLlm`
          The CustomLlm containing the fields which should be updated.
        :param update_mask: str
          The list of the CustomLlm fields to update. These should correspond to the values (or lack thereof)
          present in `custom_llm`.

          The field mask must be a single string, with multiple fields separated by commas (no spaces). The
          field path is relative to the resource object, using a dot (`.`) to navigate sub-fields (e.g.,
          `author.given_name`). Specification of elements in sequence or map fields is not allowed, as only
          the entire collection field can be specified. Field names must exactly match the resource field
          names.

          A field mask of `*` indicates full replacement. It’s recommended to always explicitly list the
          fields being updated and avoid using `*` wildcards, as it can lead to unintended results if the API
          changes in the future.

        :returns: :class:`CustomLlm`
        """
        body = {}
        if custom_llm is not None:
            body["custom_llm"] = custom_llm.as_dict()
        if update_mask is not None:
            body["update_mask"] = update_mask
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do("PATCH", f"/api/2.0/custom-llms/{id}", body=body, headers=headers)
        return CustomLlm.from_dict(res)
