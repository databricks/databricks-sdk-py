# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import Any, Dict, Iterator, List, Optional

from ._internal import _repeated_dict

_LOG = logging.getLogger("databricks.sdk")


# all definitions in this file are in alphabetical order


@dataclass
class ListTagPoliciesResponse:
    next_page_token: Optional[str] = None

    tag_policies: Optional[List[TagPolicy]] = None

    def as_dict(self) -> dict:
        """Serializes the ListTagPoliciesResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        if self.tag_policies:
            body["tag_policies"] = [v.as_dict() for v in self.tag_policies]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ListTagPoliciesResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        if self.tag_policies:
            body["tag_policies"] = self.tag_policies
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ListTagPoliciesResponse:
        """Deserializes the ListTagPoliciesResponse from a dictionary."""
        return cls(
            next_page_token=d.get("next_page_token", None), tag_policies=_repeated_dict(d, "tag_policies", TagPolicy)
        )


@dataclass
class TagPolicy:
    tag_key: str

    description: Optional[str] = None

    id: Optional[str] = None

    values: Optional[List[Value]] = None

    def as_dict(self) -> dict:
        """Serializes the TagPolicy into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.description is not None:
            body["description"] = self.description
        if self.id is not None:
            body["id"] = self.id
        if self.tag_key is not None:
            body["tag_key"] = self.tag_key
        if self.values:
            body["values"] = [v.as_dict() for v in self.values]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the TagPolicy into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.description is not None:
            body["description"] = self.description
        if self.id is not None:
            body["id"] = self.id
        if self.tag_key is not None:
            body["tag_key"] = self.tag_key
        if self.values:
            body["values"] = self.values
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> TagPolicy:
        """Deserializes the TagPolicy from a dictionary."""
        return cls(
            description=d.get("description", None),
            id=d.get("id", None),
            tag_key=d.get("tag_key", None),
            values=_repeated_dict(d, "values", Value),
        )


@dataclass
class Value:
    name: str

    def as_dict(self) -> dict:
        """Serializes the Value into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.name is not None:
            body["name"] = self.name
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the Value into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.name is not None:
            body["name"] = self.name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> Value:
        """Deserializes the Value from a dictionary."""
        return cls(name=d.get("name", None))


class TagPoliciesAPI:
    """The Tag Policy API allows you to manage tag policies in Databricks."""

    def __init__(self, api_client):
        self._api = api_client

    def create_tag_policy(self, tag_policy: TagPolicy) -> TagPolicy:
        """Creates a new tag policy.

        :param tag_policy: :class:`TagPolicy`

        :returns: :class:`TagPolicy`
        """
        body = tag_policy.as_dict()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do("POST", "/api/2.1/tag-policies", body=body, headers=headers)
        return TagPolicy.from_dict(res)

    def delete_tag_policy(self, tag_key: str):
        """Deletes a tag policy by its key.

        :param tag_key: str


        """

        headers = {
            "Accept": "application/json",
        }

        self._api.do("DELETE", f"/api/2.1/tag-policies/{tag_key}", headers=headers)

    def get_tag_policy(self, tag_key: str) -> TagPolicy:
        """Gets a single tag policy by its key.

        :param tag_key: str

        :returns: :class:`TagPolicy`
        """

        headers = {
            "Accept": "application/json",
        }

        res = self._api.do("GET", f"/api/2.1/tag-policies/{tag_key}", headers=headers)
        return TagPolicy.from_dict(res)

    def list_tag_policies(
        self, *, page_size: Optional[int] = None, page_token: Optional[str] = None
    ) -> Iterator[TagPolicy]:
        """Lists all tag policies in the account.

        :param page_size: int (optional)
          The maximum number of results to return in this request. Fewer results may be returned than
          requested. If unspecified or set to 0, this defaults to 1000. The maximum value is 1000; values
          above 1000 will be coerced down to 1000.
        :param page_token: str (optional)
          An optional page token received from a previous list tag policies call.

        :returns: Iterator over :class:`TagPolicy`
        """

        query = {}
        if page_size is not None:
            query["page_size"] = page_size
        if page_token is not None:
            query["page_token"] = page_token
        headers = {
            "Accept": "application/json",
        }

        while True:
            json = self._api.do("GET", "/api/2.1/tag-policies", query=query, headers=headers)
            if "tag_policies" in json:
                for v in json["tag_policies"]:
                    yield TagPolicy.from_dict(v)
            if "next_page_token" not in json or not json["next_page_token"]:
                return
            query["page_token"] = json["next_page_token"]

    def update_tag_policy(self, tag_key: str, tag_policy: TagPolicy, update_mask: str) -> TagPolicy:
        """Updates an existing tag policy.

        :param tag_key: str
        :param tag_policy: :class:`TagPolicy`
        :param update_mask: str
          The field mask must be a single string, with multiple fields separated by commas (no spaces). The
          field path is relative to the resource object, using a dot (`.`) to navigate sub-fields (e.g.,
          `author.given_name`). Specification of elements in sequence or map fields is not allowed, as only
          the entire collection field can be specified. Field names must exactly match the resource field
          names.

          A field mask of `*` indicates full replacement. It’s recommended to always explicitly list the
          fields being updated and avoid using `*` wildcards, as it can lead to unintended results if the API
          changes in the future.

        :returns: :class:`TagPolicy`
        """
        body = tag_policy.as_dict()
        query = {}
        if update_mask is not None:
            query["update_mask"] = update_mask
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do("PATCH", f"/api/2.1/tag-policies/{tag_key}", query=query, body=body, headers=headers)
        return TagPolicy.from_dict(res)
