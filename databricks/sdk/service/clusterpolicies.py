# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

from dataclasses import dataclass
from enum import Enum
from typing import Optional, Dict, List

__all__ = [
    
    'CreatePolicy',
    'CreatePolicyResponse',
    'DeletePolicy',
    'EditPolicy',
    'ListPoliciesResponse',
    'Policy',
    'GetRequest',
    
    'ClusterPolicies',
]

# all definitions in this file are in alphabetical order

@dataclass
class CreatePolicy:
    
    # Policy definition document expressed in Databricks Cluster Policy
    # Definition Language.
    definition: str = None
    # Cluster Policy name requested by the user. This has to be unique. Length
    # must be between 1 and 100 characters.
    name: str = None

    def as_request(self) -> (dict, dict):
        createPolicy_query, createPolicy_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.definition:
            createPolicy_body['definition'] = self.definition
        if self.name:
            createPolicy_body['name'] = self.name
        
        return createPolicy_query, createPolicy_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreatePolicy':
        return cls(
            definition=d.get('definition', None),
            name=d.get('name', None),
        )



@dataclass
class CreatePolicyResponse:
    
    # Canonical unique identifier for the cluster policy.
    policy_id: str = None

    def as_request(self) -> (dict, dict):
        createPolicyResponse_query, createPolicyResponse_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.policy_id:
            createPolicyResponse_body['policy_id'] = self.policy_id
        
        return createPolicyResponse_query, createPolicyResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreatePolicyResponse':
        return cls(
            policy_id=d.get('policy_id', None),
        )



@dataclass
class DeletePolicy:
    
    # The ID of the policy to delete.
    policy_id: str

    def as_request(self) -> (dict, dict):
        deletePolicy_query, deletePolicy_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.policy_id:
            deletePolicy_body['policy_id'] = self.policy_id
        
        return deletePolicy_query, deletePolicy_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'DeletePolicy':
        return cls(
            policy_id=d.get('policy_id', None),
        )



@dataclass
class EditPolicy:
    
    # The ID of the policy to update.
    policy_id: str
    # Policy definition document expressed in Databricks Cluster Policy
    # Definition Language.
    definition: str = None
    # Cluster Policy name requested by the user. This has to be unique. Length
    # must be between 1 and 100 characters.
    name: str = None

    def as_request(self) -> (dict, dict):
        editPolicy_query, editPolicy_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.definition:
            editPolicy_body['definition'] = self.definition
        if self.name:
            editPolicy_body['name'] = self.name
        if self.policy_id:
            editPolicy_body['policy_id'] = self.policy_id
        
        return editPolicy_query, editPolicy_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'EditPolicy':
        return cls(
            definition=d.get('definition', None),
            name=d.get('name', None),
            policy_id=d.get('policy_id', None),
        )



@dataclass
class ListPoliciesResponse:
    
    # List of policies.
    policies: 'List[Policy]' = None

    def as_request(self) -> (dict, dict):
        listPoliciesResponse_query, listPoliciesResponse_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.policies:
            listPoliciesResponse_body['policies'] = [v.as_request()[1] for v in self.policies]
        
        return listPoliciesResponse_query, listPoliciesResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListPoliciesResponse':
        return cls(
            policies=[Policy.from_dict(v) for v in d['policies']] if 'policies' in d else None,
        )



@dataclass
class Policy:
    
    # Creation time. The timestamp (in millisecond) when this Cluster Policy was
    # created.
    created_at_timestamp: int = None
    # Creator user name. The field won't be included in the response if the user
    # has already been deleted.
    creator_user_name: str = None
    # Policy definition document expressed in Databricks Cluster Policy
    # Definition Language.
    definition: str = None
    # Cluster Policy name requested by the user. This has to be unique. Length
    # must be between 1 and 100 characters.
    name: str = None
    # Canonical unique identifier for the Cluster Policy.
    policy_id: str = None

    def as_request(self) -> (dict, dict):
        policy_query, policy_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.created_at_timestamp:
            policy_body['created_at_timestamp'] = self.created_at_timestamp
        if self.creator_user_name:
            policy_body['creator_user_name'] = self.creator_user_name
        if self.definition:
            policy_body['definition'] = self.definition
        if self.name:
            policy_body['name'] = self.name
        if self.policy_id:
            policy_body['policy_id'] = self.policy_id
        
        return policy_query, policy_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Policy':
        return cls(
            created_at_timestamp=d.get('created_at_timestamp', None),
            creator_user_name=d.get('creator_user_name', None),
            definition=d.get('definition', None),
            name=d.get('name', None),
            policy_id=d.get('policy_id', None),
        )



@dataclass
class GetRequest:
    
    # Canonical unique identifier for the cluster policy.
    policy_id: str = None # query

    def as_request(self) -> (dict, dict):
        getRequest_query, getRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.policy_id:
            getRequest_query['policy_id'] = self.policy_id
        
        return getRequest_query, getRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetRequest':
        return cls(
            policy_id=d.get('policy_id', None),
        )



class ClusterPoliciesAPI:
    def __init__(self, api_client):
        self._api = api_client
    
    def create(self, request: CreatePolicy) -> CreatePolicyResponse:
        """Create a new policy
        
        Creates a new policy with prescribed settings."""
        query, body = request.as_request()
        json = self._api.do('POST', '/api/2.0/policies/clusters/create', query=query, body=body)
        return CreatePolicyResponse.from_dict(json)
    
    def delete(self, request: DeletePolicy):
        """Delete a cluster policy
        
        Delete a policy for a cluster. Clusters governed by this policy can
        still run, but cannot be edited."""
        query, body = request.as_request()
        self._api.do('POST', '/api/2.0/policies/clusters/delete', query=query, body=body)
        
    
    def edit(self, request: EditPolicy):
        """Update a cluster policy
        
        Update an existing policy for cluster. This operation may make some
        clusters governed by the previous policy invalid."""
        query, body = request.as_request()
        self._api.do('POST', '/api/2.0/policies/clusters/edit', query=query, body=body)
        
    
    def get(self, request: GetRequest) -> Policy:
        """Get entity
        
        Get a cluster policy entity. Creation and editing is available to admins
        only."""
        query, body = request.as_request()
        json = self._api.do('GET', '/api/2.0/policies/clusters/get', query=query, body=body)
        return Policy.from_dict(json)
    
    def list(self) -> ListPoliciesResponse:
        """Get a cluster policy
        
        Returns a list of policies accessible by the requesting user."""
        
        json = self._api.do('GET', '/api/2.0/policies/clusters/list')
        return ListPoliciesResponse.from_dict(json)
    