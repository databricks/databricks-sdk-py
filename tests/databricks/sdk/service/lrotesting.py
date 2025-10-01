# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import Any, Dict, Optional

_LOG = logging.getLogger("databricks.sdk")


# all definitions in this file are in alphabetical order


@dataclass
class TestResource:
    """Test resource for LRO operations"""

    id: Optional[str] = None
    """Unique identifier for the resource"""

    name: Optional[str] = None
    """Name of the resource"""

    def as_dict(self) -> dict:
        """Serializes the TestResource into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.id is not None:
            body["id"] = self.id
        if self.name is not None:
            body["name"] = self.name
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the TestResource into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.id is not None:
            body["id"] = self.id
        if self.name is not None:
            body["name"] = self.name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> TestResource:
        """Deserializes the TestResource from a dictionary."""
        return cls(id=d.get("id", None), name=d.get("name", None))


class LroTestingAPI:
    """Test service for Long Running Operations"""

    def __init__(self, api_client):
        self._api = api_client

    def cancel_operation(self, name: str):

        headers = {
            "Accept": "application/json",
        }

        self._api.do("POST", f"/api/2.0/lro-testing/operations/{name}/cancel", headers=headers)

    def create_test_resource(self, resource: TestResource) -> common.Operation:
        """Simple method to create test resource for LRO testing

        :param resource: :class:`TestResource`
          The resource to create

        :returns: :class:`common.Operation`
        """
        body = resource.as_dict()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do("POST", "/api/2.0/lro-testing/resources", body=body, headers=headers)
        return common.Operation.from_dict(res)

    def get_operation(self, name: str) -> common.Operation:

        headers = {
            "Accept": "application/json",
        }

        res = self._api.do("GET", f"/api/2.0/lro-testing/operations/{name}", headers=headers)
        return common.Operation.from_dict(res)

    def get_test_resource(self, resource_id: str) -> TestResource:
        """Simple method to get test resource

        :param resource_id: str
          Resource ID to get

        :returns: :class:`TestResource`
        """

        headers = {
            "Accept": "application/json",
        }

        res = self._api.do("GET", f"/api/2.0/lro-testing/resources/{resource_id}", headers=headers)
        return TestResource.from_dict(res)
