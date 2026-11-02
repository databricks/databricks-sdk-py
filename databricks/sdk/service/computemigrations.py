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
import uuid

from databricks.sdk.service._internal import (
    _enum,
    _from_dict,
    _int64,
    _repeated_dict,
    _timestamp,
)


_LOG = logging.getLogger("databricks.sdk")


# all definitions in this file are in alphabetical order


@dataclass
class BakingConfig:
    """Configuration for the baking window (post-execution production monitoring)."""

    run_count: Optional[int] = None
    """Number of successful production runs required before the migration reaches MIGRATION_COMPLETE.
    Default applied by the server (configurable)."""

    time_window_hours: Optional[int] = None
    """Maximum baking window duration in hours. If the required run_count has not been reached within
    this window, the migration transitions to FAILED. Default applied by the server (configurable)."""

    def as_dict(self) -> dict:
        """Serializes the BakingConfig into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.run_count is not None:
            body["run_count"] = self.run_count
        if self.time_window_hours is not None:
            body["time_window_hours"] = self.time_window_hours
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the BakingConfig into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.run_count is not None:
            body["run_count"] = self.run_count
        if self.time_window_hours is not None:
            body["time_window_hours"] = self.time_window_hours
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> BakingConfig:
        """Deserializes the BakingConfig from a dictionary."""
        return cls(run_count=d.get("run_count", None), time_window_hours=d.get("time_window_hours", None))


@dataclass
class BakingReport:
    """Summary of baking metrics after the baking window completes."""

    successful_runs: Optional[int] = None
    """Number of successful runs."""

    total_runs: Optional[int] = None
    """Number of runs observed during the baking window."""

    def as_dict(self) -> dict:
        """Serializes the BakingReport into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.successful_runs is not None:
            body["successful_runs"] = self.successful_runs
        if self.total_runs is not None:
            body["total_runs"] = self.total_runs
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the BakingReport into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.successful_runs is not None:
            body["successful_runs"] = self.successful_runs
        if self.total_runs is not None:
            body["total_runs"] = self.total_runs
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> BakingReport:
        """Deserializes the BakingReport from a dictionary."""
        return cls(successful_runs=d.get("successful_runs", None), total_runs=d.get("total_runs", None))


@dataclass
class ListMigrationsResponse:
    """Response containing a paginated list of migrations matching the request filters."""

    migrations: Optional[List[Migration]] = None
    """The migrations matching the request filters."""

    next_page_token: Optional[str] = None
    """Token for the next page. Omitted if there are no more results."""

    def as_dict(self) -> dict:
        """Serializes the ListMigrationsResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.migrations:
            body["migrations"] = [v.as_dict() for v in self.migrations]
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ListMigrationsResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.migrations:
            body["migrations"] = self.migrations
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ListMigrationsResponse:
        """Deserializes the ListMigrationsResponse from a dictionary."""
        return cls(
            migrations=_repeated_dict(d, "migrations", Migration), next_page_token=d.get("next_page_token", None)
        )


@dataclass
class Migration:
    """A persistent object tracking the full lifecycle of migrating one Classic compute asset to
    Serverless. Each Migration has a well-defined state machine and is the unit of orchestration,
    approval, and rollback."""

    asset_type: MigrationAssetType
    """Type of Classic compute asset being migrated. Cannot be changed after creation."""

    asset_uri: str
    """URI of the source asset (e.g., "jobs/12345"). Cannot be changed after creation."""

    auto_approve: Optional[bool] = None
    """When true, the server skips the translation review (TRANSLATION_READY) instead of waiting for an
    explicit ApproveMigrationTranslation. MIGRATION_REVIEW is never skipped. Unset/false means the
    translation review requires explicit user action. Set at creation; cannot be changed afterward.
    Does not suppress cancellation or terminal failures."""

    baking_config: Optional[BakingConfig] = None
    """Baking window configuration. Mutable via UpdateMigration before baking starts."""

    baking_report: Optional[BakingReport] = None
    """Summary of baking metrics after the baking window completes."""

    create_time: Optional[Timestamp] = None
    """Timestamp when the migration was created."""

    etag: Optional[str] = None
    """Resource version for optimistic concurrency control. Clients read this from GetMigration or
    ListMigrations and pass it back as the request ``etag`` on update, delete, approve, reject, and
    cancel methods."""

    initiator: Optional[MigrationInitiator] = None
    """The user who initiated this migration and their role. Set at creation."""

    migration_id: Optional[str] = None
    """Server-generated unique identifier for this migration."""

    migration_report: Optional[MigrationReport] = None
    """Agent-produced planning report, presented to the user at the review gates."""

    run_validation: Optional[bool] = None
    """When true, Databricks runs the working copy to validate it after the translation review.
    Unset/false skips the run, so the migration goes from the translation review straight to
    execution review. Whether the translation review waits for the user is controlled by
    ``auto_approve``, not this field. Set at creation; cannot be changed afterward."""

    state: Optional[MigrationState] = None
    """Current state of the migration in the state machine. Managed by the server."""

    state_history: Optional[List[MigrationStateTransition]] = None
    """History of state transitions, ordered chronologically. Each entry records the state entered and
    the timestamp of the transition."""

    validation_report: Optional[ValidationReport] = None
    """Agent-produced validation results from sandbox execution."""

    def as_dict(self) -> dict:
        """Serializes the Migration into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.asset_type is not None:
            body["asset_type"] = self.asset_type.value
        if self.asset_uri is not None:
            body["asset_uri"] = self.asset_uri
        if self.auto_approve is not None:
            body["auto_approve"] = self.auto_approve
        if self.baking_config:
            body["baking_config"] = self.baking_config.as_dict()
        if self.baking_report:
            body["baking_report"] = self.baking_report.as_dict()
        if self.create_time is not None:
            body["create_time"] = self.create_time.ToJsonString()
        if self.etag is not None:
            body["etag"] = self.etag
        if self.initiator:
            body["initiator"] = self.initiator.as_dict()
        if self.migration_id is not None:
            body["migration_id"] = self.migration_id
        if self.migration_report:
            body["migration_report"] = self.migration_report.as_dict()
        if self.run_validation is not None:
            body["run_validation"] = self.run_validation
        if self.state is not None:
            body["state"] = self.state.value
        if self.state_history:
            body["state_history"] = [v.as_dict() for v in self.state_history]
        if self.validation_report:
            body["validation_report"] = self.validation_report.as_dict()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the Migration into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.asset_type is not None:
            body["asset_type"] = self.asset_type
        if self.asset_uri is not None:
            body["asset_uri"] = self.asset_uri
        if self.auto_approve is not None:
            body["auto_approve"] = self.auto_approve
        if self.baking_config:
            body["baking_config"] = self.baking_config
        if self.baking_report:
            body["baking_report"] = self.baking_report
        if self.create_time is not None:
            body["create_time"] = self.create_time
        if self.etag is not None:
            body["etag"] = self.etag
        if self.initiator:
            body["initiator"] = self.initiator
        if self.migration_id is not None:
            body["migration_id"] = self.migration_id
        if self.migration_report:
            body["migration_report"] = self.migration_report
        if self.run_validation is not None:
            body["run_validation"] = self.run_validation
        if self.state is not None:
            body["state"] = self.state
        if self.state_history:
            body["state_history"] = self.state_history
        if self.validation_report:
            body["validation_report"] = self.validation_report
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> Migration:
        """Deserializes the Migration from a dictionary."""
        return cls(
            asset_type=_enum(d, "asset_type", MigrationAssetType),
            asset_uri=d.get("asset_uri", None),
            auto_approve=d.get("auto_approve", None),
            baking_config=_from_dict(d, "baking_config", BakingConfig),
            baking_report=_from_dict(d, "baking_report", BakingReport),
            create_time=_timestamp(d, "create_time"),
            etag=d.get("etag", None),
            initiator=_from_dict(d, "initiator", MigrationInitiator),
            migration_id=d.get("migration_id", None),
            migration_report=_from_dict(d, "migration_report", MigrationReport),
            run_validation=d.get("run_validation", None),
            state=_enum(d, "state", MigrationState),
            state_history=_repeated_dict(d, "state_history", MigrationStateTransition),
            validation_report=_from_dict(d, "validation_report", ValidationReport),
        )


@dataclass
class MigrationAsset:
    """A working copy (job or notebook) the migration agent created for the migration."""

    asset_type: Optional[MigrationAssetType] = None
    """Type of asset this working copy represents."""

    id: Optional[str] = None
    """Identifier of the asset."""

    uri: Optional[str] = None
    """Link to the asset, e.g. "jobs/12345"."""

    def as_dict(self) -> dict:
        """Serializes the MigrationAsset into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.asset_type is not None:
            body["asset_type"] = self.asset_type.value
        if self.id is not None:
            body["id"] = self.id
        if self.uri is not None:
            body["uri"] = self.uri
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the MigrationAsset into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.asset_type is not None:
            body["asset_type"] = self.asset_type
        if self.id is not None:
            body["id"] = self.id
        if self.uri is not None:
            body["uri"] = self.uri
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> MigrationAsset:
        """Deserializes the MigrationAsset from a dictionary."""
        return cls(asset_type=_enum(d, "asset_type", MigrationAssetType), id=d.get("id", None), uri=d.get("uri", None))


class MigrationAssetType(Enum):
    """Type of a migration asset: the Classic asset being migrated, or an asset the migration agent
    created for it. Migrations can only be created for JOB assets."""

    FILE = "FILE"
    INTERACTIVE = "INTERACTIVE"
    JOB = "JOB"


@dataclass
class MigrationInitiator:
    """The initiator of a migration, including their role and user identity."""

    role: Optional[MigrationInitiatorRole] = None
    """The role of the initiator, determining approval authority. Set by the server: the role is
    resolved from the caller's identity and permissions on the asset, never taken from the request,
    since a caller must not be able to assert its own approval authority."""

    user_id: Optional[int] = None
    """The user ID of the initiator. Set by the server from the request context."""

    def as_dict(self) -> dict:
        """Serializes the MigrationInitiator into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.role is not None:
            body["role"] = self.role.value
        if self.user_id is not None:
            body["user_id"] = self.user_id
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the MigrationInitiator into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.role is not None:
            body["role"] = self.role
        if self.user_id is not None:
            body["user_id"] = self.user_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> MigrationInitiator:
        """Deserializes the MigrationInitiator from a dictionary."""
        return cls(role=_enum(d, "role", MigrationInitiatorRole), user_id=_int64(d, "user_id"))


class MigrationInitiatorRole(Enum):
    """Role of the migration initiator, determining approval authority."""

    ACCOUNT_ADMIN = "ACCOUNT_ADMIN"
    JOB_ADMIN = "JOB_ADMIN"
    SYSTEM = "SYSTEM"
    WORKSPACE_ADMIN = "WORKSPACE_ADMIN"


@dataclass
class MigrationReport:
    """Agent-produced planning report, presented to the user at the review gates."""

    primary_asset: Optional[MigrationAsset] = None
    """The primary asset the agent created — the entry point / validation target."""

    secondary_assets: Optional[List[MigrationAsset]] = None
    """Additional assets the agent created (e.g. notebooks or jobs the primary asset invokes)."""

    def as_dict(self) -> dict:
        """Serializes the MigrationReport into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.primary_asset:
            body["primary_asset"] = self.primary_asset.as_dict()
        if self.secondary_assets:
            body["secondary_assets"] = [v.as_dict() for v in self.secondary_assets]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the MigrationReport into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.primary_asset:
            body["primary_asset"] = self.primary_asset
        if self.secondary_assets:
            body["secondary_assets"] = self.secondary_assets
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> MigrationReport:
        """Deserializes the MigrationReport from a dictionary."""
        return cls(
            primary_asset=_from_dict(d, "primary_asset", MigrationAsset),
            secondary_assets=_repeated_dict(d, "secondary_assets", MigrationAsset),
        )


class MigrationState(Enum):
    """The state of a migration in its lifecycle."""

    CANCELLED = "CANCELLED"
    FAILED = "FAILED"
    MIGRATION_COMPLETE = "MIGRATION_COMPLETE"
    MIGRATION_OBSERVATION = "MIGRATION_OBSERVATION"
    MIGRATION_PENDING = "MIGRATION_PENDING"
    MIGRATION_REVIEW = "MIGRATION_REVIEW"
    MIGRATION_RUNNING = "MIGRATION_RUNNING"
    NOT_SUPPORTED = "NOT_SUPPORTED"
    PLANNING_PENDING = "PLANNING_PENDING"
    PLANNING_REVIEW = "PLANNING_REVIEW"
    PLANNING_RUNNING = "PLANNING_RUNNING"
    REVISION_PENDING = "REVISION_PENDING"
    TRANSLATION_CREATING = "TRANSLATION_CREATING"
    TRANSLATION_PENDING = "TRANSLATION_PENDING"
    TRANSLATION_READY = "TRANSLATION_READY"
    VALIDATION_RUNNING = "VALIDATION_RUNNING"
    VALIDATION_SCHEDULING = "VALIDATION_SCHEDULING"


@dataclass
class MigrationStateTransition:
    """A record of a state transition in the migration lifecycle."""

    internal_comment: Optional[str] = None
    """Free-text the service recorded for this transition — e.g. an internally-determined
    cancellation or failure reason. Empty for user-driven transitions."""

    state: Optional[MigrationState] = None
    """The state that was entered."""

    transition_time: Optional[Timestamp] = None
    """Timestamp when this state was entered."""

    user_comment: Optional[str] = None
    """Free-text the initiating user supplied at a user-driven transition — reviewer feedback on an
    approval, or the reason for a rejection or cancellation. Empty for transitions the service
    drives internally."""

    def as_dict(self) -> dict:
        """Serializes the MigrationStateTransition into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.internal_comment is not None:
            body["internal_comment"] = self.internal_comment
        if self.state is not None:
            body["state"] = self.state.value
        if self.transition_time is not None:
            body["transition_time"] = self.transition_time.ToJsonString()
        if self.user_comment is not None:
            body["user_comment"] = self.user_comment
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the MigrationStateTransition into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.internal_comment is not None:
            body["internal_comment"] = self.internal_comment
        if self.state is not None:
            body["state"] = self.state
        if self.transition_time is not None:
            body["transition_time"] = self.transition_time
        if self.user_comment is not None:
            body["user_comment"] = self.user_comment
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> MigrationStateTransition:
        """Deserializes the MigrationStateTransition from a dictionary."""
        return cls(
            internal_comment=d.get("internal_comment", None),
            state=_enum(d, "state", MigrationState),
            transition_time=_timestamp(d, "transition_time"),
            user_comment=d.get("user_comment", None),
        )


@dataclass
class ValidationReport:
    """Validation results from running the translated workload in the sandbox."""

    duration_ms: Optional[int] = None
    """Duration of the sandbox validation run in milliseconds. Pair with start_time to derive the end
    time."""

    passed: Optional[bool] = None
    """Databricks-internal recommendation on whether to proceed with the migration, based on the
    validation run. May differ from run_status: a run can succeed while the recommendation is
    negative, or vice versa."""

    run_status: Optional[str] = None
    """Status of the validation run itself (the objective run outcome), as reported by the run system,
    e.g. "SUCCESS" / "FAILED" / "TIMED_OUT"."""

    run_url: Optional[str] = None
    """Link to the validation run (job or notebook)."""

    start_time: Optional[Timestamp] = None
    """Timestamp when validation started in the sandbox."""

    def as_dict(self) -> dict:
        """Serializes the ValidationReport into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.duration_ms is not None:
            body["duration_ms"] = self.duration_ms
        if self.passed is not None:
            body["passed"] = self.passed
        if self.run_status is not None:
            body["run_status"] = self.run_status
        if self.run_url is not None:
            body["run_url"] = self.run_url
        if self.start_time is not None:
            body["start_time"] = self.start_time.ToJsonString()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ValidationReport into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.duration_ms is not None:
            body["duration_ms"] = self.duration_ms
        if self.passed is not None:
            body["passed"] = self.passed
        if self.run_status is not None:
            body["run_status"] = self.run_status
        if self.run_url is not None:
            body["run_url"] = self.run_url
        if self.start_time is not None:
            body["start_time"] = self.start_time
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ValidationReport:
        """Deserializes the ValidationReport from a dictionary."""
        return cls(
            duration_ms=_int64(d, "duration_ms"),
            passed=d.get("passed", None),
            run_status=d.get("run_status", None),
            run_url=d.get("run_url", None),
            start_time=_timestamp(d, "start_time"),
        )


class ComputeMigrationsAPI:
    """Manage migrations of Classic compute workloads to Serverless."""

    def __init__(self, api_client):
        self._api = api_client

    def approve_migration_execution(
        self, migration_id: str, *, additional_feedback: Optional[str] = None, etag: Optional[str] = None
    ) -> Migration:
        """Approves migration execution at the MIGRATION_REVIEW gate, advancing to execution.

        Valid only when the migration is in MIGRATION_REVIEW. If supplied, the ``etag`` must match the current
        server value.

        Returns NOT_FOUND if the migration does not exist. Returns FAILED_PRECONDITION if the migration is not
        in MIGRATION_REVIEW. Returns ABORTED if the etag does not match the current resource version.

        :param migration_id: str
          The ID of the migration to approve for execution.
        :param additional_feedback: str (optional)
          Optional free-text feedback or instructions the user provides along with the approval, carried into
          the next stage of the migration.
        :param etag: str (optional)
          Optional resource version for optimistic concurrency control. If supplied, it must match the current
          server value.

        :returns: :class:`Migration`
        """

        body = {}
        if additional_feedback is not None:
            body["additional_feedback"] = additional_feedback
        if etag is not None:
            body["etag"] = etag
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do(
            "POST", f"/api/compute-migrations/v1/migrations/{migration_id}/approveExecution", body=body, headers=headers
        )
        return Migration.from_dict(res)

    def approve_migration_translation(
        self, migration_id: str, *, additional_feedback: Optional[str] = None, etag: Optional[str] = None
    ) -> Migration:
        """Approves the working copy at the TRANSLATION_READY gate. If the migration was created with
        ``run_validation``, the working copy is then run to verify it executes successfully before the
        migration is presented for execution review; otherwise it advances straight to MIGRATION_REVIEW.

        Valid only when the migration is in TRANSLATION_READY. If supplied, the ``etag`` must match the
        current server value.

        Returns NOT_FOUND if the migration does not exist. Returns FAILED_PRECONDITION if the migration is not
        in TRANSLATION_READY. Returns ABORTED if the etag does not match the current resource version.

        :param migration_id: str
          The ID of the migration to approve.
        :param additional_feedback: str (optional)
          Optional free-text feedback or instructions the user provides along with the approval, carried into
          the next stage of the migration.
        :param etag: str (optional)
          Optional resource version for optimistic concurrency control. If supplied, it must match the current
          server value.

        :returns: :class:`Migration`
        """

        body = {}
        if additional_feedback is not None:
            body["additional_feedback"] = additional_feedback
        if etag is not None:
            body["etag"] = etag
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do(
            "POST",
            f"/api/compute-migrations/v1/migrations/{migration_id}/approveTranslation",
            body=body,
            headers=headers,
        )
        return Migration.from_dict(res)

    def cancel_migration(
        self, migration_id: str, *, cancellation_reason: Optional[str] = None, etag: Optional[str] = None
    ) -> Migration:
        """Cancels the migration, transitioning it to CANCELLED.

        Valid from any non-terminal state, unlike the review-gate transitions, which each require a specific
        state. Any in-flight agent work is abandoned and the migration stops advancing. The resource is
        retained for auditability.

        Returns NOT_FOUND if the migration does not exist. Returns FAILED_PRECONDITION if the migration is
        already in a terminal state. Returns ABORTED if the etag does not match the current resource version.

        :param migration_id: str
          The ID of the migration to cancel.
        :param cancellation_reason: str (optional)
          Optional free-text reason for the cancellation.
        :param etag: str (optional)
          Optional resource version for optimistic concurrency control. If supplied, it must match the current
          server value.

        :returns: :class:`Migration`
        """

        body = {}
        if cancellation_reason is not None:
            body["cancellation_reason"] = cancellation_reason
        if etag is not None:
            body["etag"] = etag
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do(
            "POST", f"/api/compute-migrations/v1/migrations/{migration_id}/cancel", body=body, headers=headers
        )
        return Migration.from_dict(res)

    def create(self, migration: Migration, *, request_id: Optional[str] = None) -> Migration:
        """Creates a new migration for a Classic compute asset.

        The migration is created in PLANNING_PENDING and advances through the state machine as planning work
        is scheduled. The caller must have appropriate permissions: workspace admin for infrastructure-scoped
        migrations, job owner/admin for individual workload migrations.

        At most one migration may hold an asset. Returns ALREADY_EXISTS if the asset has a migration in
        flight, or one that already migrated it successfully; a migration that ended without succeeding, or
        was deleted, releases the asset so it can be migrated again. Returns INVALID_PARAMETER_VALUE if the
        asset is not eligible for migration.

        :param migration: :class:`Migration`
          The migration to create. The server generates ``migration_id`` and sets ``state`` to
          PLANNING_PENDING. Required fields: ``asset_type``, ``asset_uri``.
        :param request_id: str (optional)
          Client-generated request ID for idempotent request deduplication. The server de-duplicates requests
          with the same request_id for at least 24 hours, returning the existing migration instead of creating
          a duplicate.

        :returns: :class:`Migration`
        """

        if request_id is None or request_id == "":
            request_id = str(uuid.uuid4())
        body = migration.as_dict()
        query = {}
        if request_id is not None:
            query["request_id"] = request_id
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("POST", "/api/compute-migrations/v1/migrations", query=query, body=body, headers=headers)
        return Migration.from_dict(res)

    def delete(self, migration_id: str, *, etag: Optional[str] = None) -> Migration:
        """Deletes a migration (soft-delete).

        Allowed from any state. Deleting a migration marks the record deleted only — it does not roll back a
        migration that already ran, and resources created during the migration are not cleaned up. The
        migration resource is retained for auditability. To stop an in-flight migration (agent teardown,
        transition to CANCELLED), use CancelMigration instead.

        Returns NOT_FOUND if the migration does not exist, or was already deleted: a deleted migration is
        hidden from every method (Get, Update, List, and Delete), so it cannot be deleted again. Returns
        ABORTED if a supplied nonempty request etag does not match the resource version.

        :param migration_id: str
          The ID of the migration to cancel.
        :param etag: str (optional)
          If nonempty, must match the current resource etag or the request fails with ABORTED.

        :returns: :class:`Migration`
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

        res = self._api.do(
            "DELETE", f"/api/compute-migrations/v1/migrations/{migration_id}", query=query, headers=headers
        )
        return Migration.from_dict(res)

    def get(self, migration_id: str) -> Migration:
        """Retrieves a migration by its ID.

        Returns the current state, configuration, and output artifacts of the migration. Use this to poll
        migration progress or inspect artifacts after state transitions. Returns NOT_FOUND if the migration
        does not exist in the caller's workspace.

        :param migration_id: str
          The ID of the migration to retrieve.

        :returns: :class:`Migration`
        """

        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("GET", f"/api/compute-migrations/v1/migrations/{migration_id}", headers=headers)
        return Migration.from_dict(res)

    def list(
        self,
        *,
        asset_type: Optional[MigrationAssetType] = None,
        page_size: Optional[int] = None,
        page_token: Optional[str] = None,
        states: Optional[List[MigrationState]] = None,
    ) -> Iterator[Migration]:
        """Lists migrations in the caller's workspace, ordered by migration ID, with cursor-based pagination and
        filtering by asset type and state.

        Eventually consistent: results are read from a cache, and pagination is not a point-in-time snapshot,
        so a migration created during a List may not appear until a subsequent one.

        :param asset_type: :class:`MigrationAssetType` (optional)
          Filter by asset type.
        :param page_size: int (optional)
          Maximum number of migrations to return. Default: 50, maximum: 1000.
        :param page_token: str (optional)
          Page token from a previous ListMigrations call. When paginating, all other parameters must match the
          call that provided the page token.
        :param states: List[:class:`MigrationState`] (optional)
          Filter by migration state. Returns migrations in any of the specified states.

        :returns: Iterator over :class:`Migration`
        """

        query = {}
        if asset_type is not None:
            query["asset_type"] = asset_type.value
        if page_size is not None:
            query["page_size"] = page_size
        if page_token is not None:
            query["page_token"] = page_token
        if states is not None:
            query["states"] = [v.value for v in states]
        headers = {
            "Accept": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        while True:
            json = self._api.do("GET", "/api/compute-migrations/v1/migrations", query=query, headers=headers)
            if "migrations" in json:
                for v in json["migrations"]:
                    yield Migration.from_dict(v)
            if "next_page_token" not in json or not json["next_page_token"]:
                return
            query["page_token"] = json["next_page_token"]

    def reject_migration_execution(
        self, migration_id: str, rejection_reason: str, *, etag: Optional[str] = None
    ) -> Migration:
        """Rejects migration execution at the MIGRATION_REVIEW gate, sending the migration to REVISION_PENDING to
        loop back for re-planning.

        Valid only when the migration is in MIGRATION_REVIEW. If supplied, the ``etag`` must match the current
        server value.

        Returns NOT_FOUND if the migration does not exist. Returns FAILED_PRECONDITION if the migration is not
        in MIGRATION_REVIEW. Returns ABORTED if the etag does not match the current resource version.

        :param migration_id: str
          The ID of the migration to reject.
        :param rejection_reason: str
          Required free-text reason for the rejection, fed back into re-planning so the next plan can address
          the user's concerns.
        :param etag: str (optional)
          Optional resource version for optimistic concurrency control. If supplied, it must match the current
          server value.

        :returns: :class:`Migration`
        """

        body = {}
        if etag is not None:
            body["etag"] = etag
        if rejection_reason is not None:
            body["rejection_reason"] = rejection_reason
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do(
            "POST", f"/api/compute-migrations/v1/migrations/{migration_id}/rejectExecution", body=body, headers=headers
        )
        return Migration.from_dict(res)

    def reject_migration_translation(
        self, migration_id: str, rejection_reason: str, *, etag: Optional[str] = None
    ) -> Migration:
        """Rejects the working copy at the TRANSLATION_READY gate, sending the migration to REVISION_PENDING to
        loop back for re-planning.

        Valid only when the migration is in TRANSLATION_READY. If supplied, the ``etag`` must match the
        current server value.

        Returns NOT_FOUND if the migration does not exist. Returns FAILED_PRECONDITION if the migration is not
        in TRANSLATION_READY. Returns ABORTED if the etag does not match the current resource version.

        :param migration_id: str
          The ID of the migration to reject.
        :param rejection_reason: str
          Required free-text reason for the rejection, fed back into re-planning so the next plan can address
          the user's concerns.
        :param etag: str (optional)
          Optional resource version for optimistic concurrency control. If supplied, it must match the current
          server value.

        :returns: :class:`Migration`
        """

        body = {}
        if etag is not None:
            body["etag"] = etag
        if rejection_reason is not None:
            body["rejection_reason"] = rejection_reason
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do(
            "POST",
            f"/api/compute-migrations/v1/migrations/{migration_id}/rejectTranslation",
            body=body,
            headers=headers,
        )
        return Migration.from_dict(res)
