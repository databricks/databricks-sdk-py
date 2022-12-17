# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Any


# all definitions in this file are in alphabetical order


@dataclass
class CreatePolicy:
    definition: str
    name: str

    def as_dict(self) -> dict:
        body = {}
        if self.definition:
            body["definition"] = self.definition
        if self.name:
            body["name"] = self.name

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "CreatePolicy":
        return cls(
            definition=d.get("definition", None),
            name=d.get("name", None),
        )


@dataclass
class CreatePolicyResponse:
    policy_id: str

    def as_dict(self) -> dict:
        body = {}
        if self.policy_id:
            body["policy_id"] = self.policy_id

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "CreatePolicyResponse":
        return cls(
            policy_id=d.get("policy_id", None),
        )


@dataclass
class DeletePolicy:
    policy_id: str

    def as_dict(self) -> dict:
        body = {}
        if self.policy_id:
            body["policy_id"] = self.policy_id

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "DeletePolicy":
        return cls(
            policy_id=d.get("policy_id", None),
        )


@dataclass
class EditPolicy:
    definition: str
    name: str
    policy_id: str

    def as_dict(self) -> dict:
        body = {}
        if self.definition:
            body["definition"] = self.definition
        if self.name:
            body["name"] = self.name
        if self.policy_id:
            body["policy_id"] = self.policy_id

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "EditPolicy":
        return cls(
            definition=d.get("definition", None),
            name=d.get("name", None),
            policy_id=d.get("policy_id", None),
        )


@dataclass
class Get:
    """Get entity"""

    policy_id: str  # query


@dataclass
class ListPoliciesResponse:
    policies: "List[Policy]"

    def as_dict(self) -> dict:
        body = {}
        if self.policies:
            body["policies"] = [v.as_dict() for v in self.policies]

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ListPoliciesResponse":
        return cls(
            policies=[Policy.from_dict(v) for v in d["policies"]]
            if "policies" in d
            else None,
        )


@dataclass
class Policy:
    created_at_timestamp: int
    creator_user_name: str
    definition: str
    name: str
    policy_id: str

    def as_dict(self) -> dict:
        body = {}
        if self.created_at_timestamp:
            body["created_at_timestamp"] = self.created_at_timestamp
        if self.creator_user_name:
            body["creator_user_name"] = self.creator_user_name
        if self.definition:
            body["definition"] = self.definition
        if self.name:
            body["name"] = self.name
        if self.policy_id:
            body["policy_id"] = self.policy_id

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "Policy":
        return cls(
            created_at_timestamp=d.get("created_at_timestamp", None),
            creator_user_name=d.get("creator_user_name", None),
            definition=d.get("definition", None),
            name=d.get("name", None),
            policy_id=d.get("policy_id", None),
        )


class ClusterPoliciesAPI:
    def __init__(self, api_client):
        self._api = api_client

    def create(self, name: str, definition: str, **kwargs) -> CreatePolicyResponse:
        """Create a new policy.

        Creates a new policy with prescribed settings."""
        request = kwargs.get("request", None)
        if not request:  # request is not given through keyed args
            request = CreatePolicy(definition=definition, name=name)
        body = request.as_dict()

        json = self._api.do("POST", "/api/2.0/policies/clusters/create", body=body)
        return CreatePolicyResponse.from_dict(json)

    def delete(self, policy_id: str, **kwargs):
        """Delete a cluster policy.

        Delete a policy for a cluster. Clusters governed by this policy can
        still run, but cannot be edited."""
        request = kwargs.get("request", None)
        if not request:  # request is not given through keyed args
            request = DeletePolicy(policy_id=policy_id)
        body = request.as_dict()

        self._api.do("POST", "/api/2.0/policies/clusters/delete", body=body)

    def edit(self, policy_id: str, name: str, definition: str, **kwargs):
        """Update a cluster policy.

        Update an existing policy for cluster. This operation may make some
        clusters governed by the previous policy invalid."""
        request = kwargs.get("request", None)
        if not request:  # request is not given through keyed args
            request = EditPolicy(definition=definition, name=name, policy_id=policy_id)
        body = request.as_dict()

        self._api.do("POST", "/api/2.0/policies/clusters/edit", body=body)

    def get(self, policy_id: str, **kwargs) -> Policy:
        """Get entity.

        Get a cluster policy entity. Creation and editing is available to admins
        only."""
        request = kwargs.get("request", None)
        if not request:  # request is not given through keyed args
            request = Get(policy_id=policy_id)

        query = {}
        if policy_id:
            query["policy_id"] = request.policy_id

        json = self._api.do("GET", "/api/2.0/policies/clusters/get", query=query)
        return Policy.from_dict(json)

    def list(self) -> ListPoliciesResponse:
        """Get a cluster policy.

        Returns a list of policies accessible by the requesting user."""

        json = self._api.do("GET", "/api/2.0/policies/clusters/list")
        return ListPoliciesResponse.from_dict(json)
