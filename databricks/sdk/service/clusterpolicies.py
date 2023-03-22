# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

import logging
from dataclasses import dataclass
from enum import Enum
from typing import Dict, Iterator, List

from ._internal import _repeated

_LOG = logging.getLogger('databricks.sdk')

# all definitions in this file are in alphabetical order


@dataclass
class CreatePolicy:
    name: str
    definition: str = None
    description: str = None
    max_clusters_per_user: int = None
    policy_family_definition_overrides: str = None
    policy_family_id: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.definition: body['definition'] = self.definition
        if self.description: body['description'] = self.description
        if self.max_clusters_per_user: body['max_clusters_per_user'] = self.max_clusters_per_user
        if self.name: body['name'] = self.name
        if self.policy_family_definition_overrides:
            body['policy_family_definition_overrides'] = self.policy_family_definition_overrides
        if self.policy_family_id: body['policy_family_id'] = self.policy_family_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreatePolicy':
        return cls(definition=d.get('definition', None),
                   description=d.get('description', None),
                   max_clusters_per_user=d.get('max_clusters_per_user', None),
                   name=d.get('name', None),
                   policy_family_definition_overrides=d.get('policy_family_definition_overrides', None),
                   policy_family_id=d.get('policy_family_id', None))


@dataclass
class CreatePolicyResponse:
    policy_id: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.policy_id: body['policy_id'] = self.policy_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreatePolicyResponse':
        return cls(policy_id=d.get('policy_id', None))


@dataclass
class DeletePolicy:
    policy_id: str

    def as_dict(self) -> dict:
        body = {}
        if self.policy_id: body['policy_id'] = self.policy_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'DeletePolicy':
        return cls(policy_id=d.get('policy_id', None))


@dataclass
class EditPolicy:
    policy_id: str
    name: str
    definition: str = None
    description: str = None
    max_clusters_per_user: int = None
    policy_family_definition_overrides: str = None
    policy_family_id: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.definition: body['definition'] = self.definition
        if self.description: body['description'] = self.description
        if self.max_clusters_per_user: body['max_clusters_per_user'] = self.max_clusters_per_user
        if self.name: body['name'] = self.name
        if self.policy_family_definition_overrides:
            body['policy_family_definition_overrides'] = self.policy_family_definition_overrides
        if self.policy_family_id: body['policy_family_id'] = self.policy_family_id
        if self.policy_id: body['policy_id'] = self.policy_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'EditPolicy':
        return cls(definition=d.get('definition', None),
                   description=d.get('description', None),
                   max_clusters_per_user=d.get('max_clusters_per_user', None),
                   name=d.get('name', None),
                   policy_family_definition_overrides=d.get('policy_family_definition_overrides', None),
                   policy_family_id=d.get('policy_family_id', None),
                   policy_id=d.get('policy_id', None))


@dataclass
class Get:
    """Get entity"""

    policy_id: str


@dataclass
class GetPolicyFamilyRequest:
    policy_family_id: str


@dataclass
class ListRequest:
    """Get a cluster policy"""

    sort_column: 'ListSortColumn' = None
    sort_order: 'ListSortOrder' = None


@dataclass
class ListPoliciesResponse:
    policies: 'List[Policy]' = None

    def as_dict(self) -> dict:
        body = {}
        if self.policies: body['policies'] = [v.as_dict() for v in self.policies]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListPoliciesResponse':
        return cls(policies=_repeated(d, 'policies', Policy))


@dataclass
class ListPolicyFamiliesRequest:
    max_results: int = None
    page_token: str = None


@dataclass
class ListPolicyFamiliesResponse:
    policy_families: 'List[PolicyFamily]'
    next_page_token: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.next_page_token: body['next_page_token'] = self.next_page_token
        if self.policy_families: body['policy_families'] = [v.as_dict() for v in self.policy_families]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListPolicyFamiliesResponse':
        return cls(next_page_token=d.get('next_page_token', None),
                   policy_families=_repeated(d, 'policy_families', PolicyFamily))


class ListSortColumn(Enum):

    POLICY_CREATION_TIME = 'POLICY_CREATION_TIME'
    POLICY_NAME = 'POLICY_NAME'


class ListSortOrder(Enum):

    ASC = 'ASC'
    DESC = 'DESC'


@dataclass
class Policy:
    created_at_timestamp: int = None
    creator_user_name: str = None
    definition: str = None
    description: str = None
    is_default: bool = None
    max_clusters_per_user: int = None
    name: str = None
    policy_family_definition_overrides: str = None
    policy_family_id: str = None
    policy_id: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.created_at_timestamp: body['created_at_timestamp'] = self.created_at_timestamp
        if self.creator_user_name: body['creator_user_name'] = self.creator_user_name
        if self.definition: body['definition'] = self.definition
        if self.description: body['description'] = self.description
        if self.is_default: body['is_default'] = self.is_default
        if self.max_clusters_per_user: body['max_clusters_per_user'] = self.max_clusters_per_user
        if self.name: body['name'] = self.name
        if self.policy_family_definition_overrides:
            body['policy_family_definition_overrides'] = self.policy_family_definition_overrides
        if self.policy_family_id: body['policy_family_id'] = self.policy_family_id
        if self.policy_id: body['policy_id'] = self.policy_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Policy':
        return cls(created_at_timestamp=d.get('created_at_timestamp', None),
                   creator_user_name=d.get('creator_user_name', None),
                   definition=d.get('definition', None),
                   description=d.get('description', None),
                   is_default=d.get('is_default', None),
                   max_clusters_per_user=d.get('max_clusters_per_user', None),
                   name=d.get('name', None),
                   policy_family_definition_overrides=d.get('policy_family_definition_overrides', None),
                   policy_family_id=d.get('policy_family_id', None),
                   policy_id=d.get('policy_id', None))


@dataclass
class PolicyFamily:
    policy_family_id: str
    name: str
    description: str
    definition: str

    def as_dict(self) -> dict:
        body = {}
        if self.definition: body['definition'] = self.definition
        if self.description: body['description'] = self.description
        if self.name: body['name'] = self.name
        if self.policy_family_id: body['policy_family_id'] = self.policy_family_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'PolicyFamily':
        return cls(definition=d.get('definition', None),
                   description=d.get('description', None),
                   name=d.get('name', None),
                   policy_family_id=d.get('policy_family_id', None))


class ClusterPoliciesAPI:
    """Cluster policy limits the ability to configure clusters based on a set of rules. The policy rules limit
    the attributes or attribute values available for cluster creation. Cluster policies have ACLs that limit
    their use to specific users and groups.
    
    Cluster policies let you limit users to create clusters with prescribed settings, simplify the user
    interface and enable more users to create their own clusters (by fixing and hiding some values), control
    cost by limiting per cluster maximum cost (by setting limits on attributes whose values contribute to
    hourly price).
    
    Cluster policy permissions limit which policies a user can select in the Policy drop-down when the user
    creates a cluster: - A user who has cluster create permission can select the Unrestricted policy and
    create fully-configurable clusters. - A user who has both cluster create permission and access to cluster
    policies can select the Unrestricted policy and policies they have access to. - A user that has access to
    only cluster policies, can select the policies they have access to.
    
    If no policies have been created in the workspace, the Policy drop-down does not display.
    
    Only admin users can create, edit, and delete policies. Admin users also have access to all policies."""

    def __init__(self, api_client):
        self._api = api_client

    def create(self,
               name: str,
               *,
               definition: str = None,
               description: str = None,
               max_clusters_per_user: int = None,
               policy_family_definition_overrides: str = None,
               policy_family_id: str = None,
               **kwargs) -> CreatePolicyResponse:
        """Create a new policy.
        
        Creates a new policy with prescribed settings."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = CreatePolicy(definition=definition,
                                   description=description,
                                   max_clusters_per_user=max_clusters_per_user,
                                   name=name,
                                   policy_family_definition_overrides=policy_family_definition_overrides,
                                   policy_family_id=policy_family_id)
        body = request.as_dict()

        json = self._api.do('POST', '/api/2.0/policies/clusters/create', body=body)
        return CreatePolicyResponse.from_dict(json)

    def delete(self, policy_id: str, **kwargs):
        """Delete a cluster policy.
        
        Delete a policy for a cluster. Clusters governed by this policy can still run, but cannot be edited."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = DeletePolicy(policy_id=policy_id)
        body = request.as_dict()
        self._api.do('POST', '/api/2.0/policies/clusters/delete', body=body)

    def edit(self,
             policy_id: str,
             name: str,
             *,
             definition: str = None,
             description: str = None,
             max_clusters_per_user: int = None,
             policy_family_definition_overrides: str = None,
             policy_family_id: str = None,
             **kwargs):
        """Update a cluster policy.
        
        Update an existing policy for cluster. This operation may make some clusters governed by the previous
        policy invalid."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = EditPolicy(definition=definition,
                                 description=description,
                                 max_clusters_per_user=max_clusters_per_user,
                                 name=name,
                                 policy_family_definition_overrides=policy_family_definition_overrides,
                                 policy_family_id=policy_family_id,
                                 policy_id=policy_id)
        body = request.as_dict()
        self._api.do('POST', '/api/2.0/policies/clusters/edit', body=body)

    def get(self, policy_id: str, **kwargs) -> Policy:
        """Get entity.
        
        Get a cluster policy entity. Creation and editing is available to admins only."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = Get(policy_id=policy_id)

        query = {}
        if policy_id: query['policy_id'] = request.policy_id

        json = self._api.do('GET', '/api/2.0/policies/clusters/get', query=query)
        return Policy.from_dict(json)

    def list(self,
             *,
             sort_column: ListSortColumn = None,
             sort_order: ListSortOrder = None,
             **kwargs) -> Iterator[Policy]:
        """Get a cluster policy.
        
        Returns a list of policies accessible by the requesting user."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = ListRequest(sort_column=sort_column, sort_order=sort_order)

        query = {}
        if sort_column: query['sort_column'] = request.sort_column.value
        if sort_order: query['sort_order'] = request.sort_order.value

        json = self._api.do('GET', '/api/2.0/policies/clusters/list', query=query)
        return [Policy.from_dict(v) for v in json.get('policies', [])]


class PolicyFamiliesAPI:
    """View available policy families. A policy family contains a policy definition providing best practices for
    configuring clusters for a particular use case.
    
    Databricks manages and provides policy families for several common cluster use cases. You cannot create,
    edit, or delete policy families.
    
    Policy families cannot be used directly to create clusters. Instead, you create cluster policies using a
    policy family. Cluster policies created using a policy family inherit the policy family's policy
    definition."""

    def __init__(self, api_client):
        self._api = api_client

    def get(self, policy_family_id: str, **kwargs) -> PolicyFamily:

        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GetPolicyFamilyRequest(policy_family_id=policy_family_id)

        json = self._api.do('GET', f'/api/2.0/policy-families/{request.policy_family_id}')
        return PolicyFamily.from_dict(json)

    def list(self, *, max_results: int = None, page_token: str = None, **kwargs) -> Iterator[PolicyFamily]:

        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = ListPolicyFamiliesRequest(max_results=max_results, page_token=page_token)

        query = {}
        if max_results: query['max_results'] = request.max_results
        if page_token: query['page_token'] = request.page_token

        while True:
            json = self._api.do('GET', '/api/2.0/policy-families', query=query)
            if 'policy_families' not in json or not json['policy_families']:
                return
            for v in json['policy_families']:
                yield PolicyFamily.from_dict(v)
            if 'next_page_token' not in json or not json['next_page_token']:
                return
            query['page_token'] = json['next_page_token']
