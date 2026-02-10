# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

from __future__ import annotations

import logging
import uuid
from dataclasses import dataclass
from typing import Any, Dict, Optional

from databricks.sdk.client_types import HostType

_LOG = logging.getLogger("databricks.sdk")


# all definitions in this file are in alphabetical order


@dataclass
class TestResource:
    id: Optional[str] = None

    name: Optional[str] = None

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


class IdempotencyTestingAPI:
    """Test service for Idempotency of Operations"""

    def __init__(self, api_client):
        self._api = api_client

    def create_test_resource(self, test_resource: TestResource, *, request_id: Optional[str] = None) -> TestResource:

        if request_id is None or request_id == "":
            request_id = str(uuid.uuid4())
        body = test_resource.as_dict()
        query = {}
        if request_id is not None:
            query["request_id"] = request_id
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.host_type == HostType.UNIFIED and cfg.workspace_id:
            headers["X-Databricks-Org-Id"] = cfg.workspace_id

        res = self._api.do("POST", "/api/2.0/idempotency-testing/resources", query=query, body=body, headers=headers)
        return TestResource.from_dict(res)
