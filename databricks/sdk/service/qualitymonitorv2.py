# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

from __future__ import annotations

import logging
from dataclasses import dataclass
from enum import Enum
from typing import Any, Dict, Iterator, List, Optional

from databricks.sdk.service._internal import _enum, _from_dict, _repeated_dict

_LOG = logging.getLogger("databricks.sdk")


# all definitions in this file are in alphabetical order


@dataclass
class AnomalyDetectionConfig:
    last_run_id: Optional[str] = None
    """Run id of the last run of the workflow"""

    latest_run_status: Optional[AnomalyDetectionRunStatus] = None
    """The status of the last run of the workflow."""

    def as_dict(self) -> dict:
        """Serializes the AnomalyDetectionConfig into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.last_run_id is not None:
            body["last_run_id"] = self.last_run_id
        if self.latest_run_status is not None:
            body["latest_run_status"] = self.latest_run_status.value
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the AnomalyDetectionConfig into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.last_run_id is not None:
            body["last_run_id"] = self.last_run_id
        if self.latest_run_status is not None:
            body["latest_run_status"] = self.latest_run_status
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> AnomalyDetectionConfig:
        """Deserializes the AnomalyDetectionConfig from a dictionary."""
        return cls(
            last_run_id=d.get("last_run_id", None),
            latest_run_status=_enum(d, "latest_run_status", AnomalyDetectionRunStatus),
        )


class AnomalyDetectionRunStatus(Enum):
    """Status of Anomaly Detection Job Run"""

    ANOMALY_DETECTION_RUN_STATUS_CANCELED = "ANOMALY_DETECTION_RUN_STATUS_CANCELED"
    ANOMALY_DETECTION_RUN_STATUS_FAILED = "ANOMALY_DETECTION_RUN_STATUS_FAILED"
    ANOMALY_DETECTION_RUN_STATUS_JOB_DELETED = "ANOMALY_DETECTION_RUN_STATUS_JOB_DELETED"
    ANOMALY_DETECTION_RUN_STATUS_PENDING = "ANOMALY_DETECTION_RUN_STATUS_PENDING"
    ANOMALY_DETECTION_RUN_STATUS_RUNNING = "ANOMALY_DETECTION_RUN_STATUS_RUNNING"
    ANOMALY_DETECTION_RUN_STATUS_SUCCESS = "ANOMALY_DETECTION_RUN_STATUS_SUCCESS"
    ANOMALY_DETECTION_RUN_STATUS_UNKNOWN = "ANOMALY_DETECTION_RUN_STATUS_UNKNOWN"
    ANOMALY_DETECTION_RUN_STATUS_WORKSPACE_MISMATCH_ERROR = "ANOMALY_DETECTION_RUN_STATUS_WORKSPACE_MISMATCH_ERROR"


@dataclass
class ListQualityMonitorResponse:
    next_page_token: Optional[str] = None

    quality_monitors: Optional[List[QualityMonitor]] = None

    def as_dict(self) -> dict:
        """Serializes the ListQualityMonitorResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        if self.quality_monitors:
            body["quality_monitors"] = [v.as_dict() for v in self.quality_monitors]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ListQualityMonitorResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        if self.quality_monitors:
            body["quality_monitors"] = self.quality_monitors
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ListQualityMonitorResponse:
        """Deserializes the ListQualityMonitorResponse from a dictionary."""
        return cls(
            next_page_token=d.get("next_page_token", None),
            quality_monitors=_repeated_dict(d, "quality_monitors", QualityMonitor),
        )


@dataclass
class QualityMonitor:
    object_type: str
    """The type of the monitored object. Can be one of the following: schema."""

    object_id: str
    """The uuid of the request object. For example, schema id."""

    anomaly_detection_config: Optional[AnomalyDetectionConfig] = None

    def as_dict(self) -> dict:
        """Serializes the QualityMonitor into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.anomaly_detection_config:
            body["anomaly_detection_config"] = self.anomaly_detection_config.as_dict()
        if self.object_id is not None:
            body["object_id"] = self.object_id
        if self.object_type is not None:
            body["object_type"] = self.object_type
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the QualityMonitor into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.anomaly_detection_config:
            body["anomaly_detection_config"] = self.anomaly_detection_config
        if self.object_id is not None:
            body["object_id"] = self.object_id
        if self.object_type is not None:
            body["object_type"] = self.object_type
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> QualityMonitor:
        """Deserializes the QualityMonitor from a dictionary."""
        return cls(
            anomaly_detection_config=_from_dict(d, "anomaly_detection_config", AnomalyDetectionConfig),
            object_id=d.get("object_id", None),
            object_type=d.get("object_type", None),
        )


class QualityMonitorV2API:
    """Manage data quality of UC objects (currently support `schema`)"""

    def __init__(self, api_client):
        self._api = api_client

    def create_quality_monitor(self, quality_monitor: QualityMonitor) -> QualityMonitor:
        """Create a quality monitor on UC object

        :param quality_monitor: :class:`QualityMonitor`

        :returns: :class:`QualityMonitor`
        """

        body = quality_monitor.as_dict()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do("POST", "/api/2.0/quality-monitors", body=body, headers=headers)
        return QualityMonitor.from_dict(res)

    def delete_quality_monitor(self, object_type: str, object_id: str):
        """Delete a quality monitor on UC object

        :param object_type: str
          The type of the monitored object. Can be one of the following: schema.
        :param object_id: str
          The uuid of the request object. For example, schema id.


        """

        headers = {
            "Accept": "application/json",
        }

        self._api.do("DELETE", f"/api/2.0/quality-monitors/{object_type}/{object_id}", headers=headers)

    def get_quality_monitor(self, object_type: str, object_id: str) -> QualityMonitor:
        """Read a quality monitor on UC object

        :param object_type: str
          The type of the monitored object. Can be one of the following: schema.
        :param object_id: str
          The uuid of the request object. For example, schema id.

        :returns: :class:`QualityMonitor`
        """

        headers = {
            "Accept": "application/json",
        }

        res = self._api.do("GET", f"/api/2.0/quality-monitors/{object_type}/{object_id}", headers=headers)
        return QualityMonitor.from_dict(res)

    def list_quality_monitor(
        self, *, page_size: Optional[int] = None, page_token: Optional[str] = None
    ) -> Iterator[QualityMonitor]:
        """(Unimplemented) List quality monitors

        :param page_size: int (optional)
        :param page_token: str (optional)

        :returns: Iterator over :class:`QualityMonitor`
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
            json = self._api.do("GET", "/api/2.0/quality-monitors", query=query, headers=headers)
            if "quality_monitors" in json:
                for v in json["quality_monitors"]:
                    yield QualityMonitor.from_dict(v)
            if "next_page_token" not in json or not json["next_page_token"]:
                return
            query["page_token"] = json["next_page_token"]

    def update_quality_monitor(
        self, object_type: str, object_id: str, quality_monitor: QualityMonitor
    ) -> QualityMonitor:
        """(Unimplemented) Update a quality monitor on UC object

        :param object_type: str
          The type of the monitored object. Can be one of the following: schema.
        :param object_id: str
          The uuid of the request object. For example, schema id.
        :param quality_monitor: :class:`QualityMonitor`

        :returns: :class:`QualityMonitor`
        """

        body = quality_monitor.as_dict()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do("PUT", f"/api/2.0/quality-monitors/{object_type}/{object_id}", body=body, headers=headers)
        return QualityMonitor.from_dict(res)
