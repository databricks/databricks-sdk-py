# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

from __future__ import annotations

import logging
from dataclasses import dataclass
from enum import Enum
from typing import Any, Dict, Iterator, List, Optional

from ._internal import _enum, _from_dict, _repeated_dict

_LOG = logging.getLogger("databricks.sdk")


# all definitions in this file are in alphabetical order


@dataclass
class AibiDashboardEmbeddingAccessPolicy:
    access_policy_type: AibiDashboardEmbeddingAccessPolicyAccessPolicyType

    def as_dict(self) -> dict:
        """Serializes the AibiDashboardEmbeddingAccessPolicy into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.access_policy_type is not None:
            body["access_policy_type"] = self.access_policy_type.value
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the AibiDashboardEmbeddingAccessPolicy into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.access_policy_type is not None:
            body["access_policy_type"] = self.access_policy_type
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> AibiDashboardEmbeddingAccessPolicy:
        """Deserializes the AibiDashboardEmbeddingAccessPolicy from a dictionary."""
        return cls(
            access_policy_type=_enum(d, "access_policy_type", AibiDashboardEmbeddingAccessPolicyAccessPolicyType)
        )


class AibiDashboardEmbeddingAccessPolicyAccessPolicyType(Enum):

    ALLOW_ALL_DOMAINS = "ALLOW_ALL_DOMAINS"
    ALLOW_APPROVED_DOMAINS = "ALLOW_APPROVED_DOMAINS"
    DENY_ALL_DOMAINS = "DENY_ALL_DOMAINS"


@dataclass
class AibiDashboardEmbeddingApprovedDomains:
    approved_domains: Optional[List[str]] = None

    def as_dict(self) -> dict:
        """Serializes the AibiDashboardEmbeddingApprovedDomains into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.approved_domains:
            body["approved_domains"] = [v for v in self.approved_domains]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the AibiDashboardEmbeddingApprovedDomains into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.approved_domains:
            body["approved_domains"] = self.approved_domains
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> AibiDashboardEmbeddingApprovedDomains:
        """Deserializes the AibiDashboardEmbeddingApprovedDomains from a dictionary."""
        return cls(approved_domains=d.get("approved_domains", None))


@dataclass
class BooleanMessage:
    value: Optional[bool] = None

    def as_dict(self) -> dict:
        """Serializes the BooleanMessage into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.value is not None:
            body["value"] = self.value
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the BooleanMessage into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.value is not None:
            body["value"] = self.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> BooleanMessage:
        """Deserializes the BooleanMessage from a dictionary."""
        return cls(value=d.get("value", None))


@dataclass
class ClusterAutoRestartMessage:
    can_toggle: Optional[bool] = None

    enabled: Optional[bool] = None

    enablement_details: Optional[ClusterAutoRestartMessageEnablementDetails] = None

    maintenance_window: Optional[ClusterAutoRestartMessageMaintenanceWindow] = None

    restart_even_if_no_updates_available: Optional[bool] = None

    def as_dict(self) -> dict:
        """Serializes the ClusterAutoRestartMessage into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.can_toggle is not None:
            body["can_toggle"] = self.can_toggle
        if self.enabled is not None:
            body["enabled"] = self.enabled
        if self.enablement_details:
            body["enablement_details"] = self.enablement_details.as_dict()
        if self.maintenance_window:
            body["maintenance_window"] = self.maintenance_window.as_dict()
        if self.restart_even_if_no_updates_available is not None:
            body["restart_even_if_no_updates_available"] = self.restart_even_if_no_updates_available
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ClusterAutoRestartMessage into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.can_toggle is not None:
            body["can_toggle"] = self.can_toggle
        if self.enabled is not None:
            body["enabled"] = self.enabled
        if self.enablement_details:
            body["enablement_details"] = self.enablement_details
        if self.maintenance_window:
            body["maintenance_window"] = self.maintenance_window
        if self.restart_even_if_no_updates_available is not None:
            body["restart_even_if_no_updates_available"] = self.restart_even_if_no_updates_available
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ClusterAutoRestartMessage:
        """Deserializes the ClusterAutoRestartMessage from a dictionary."""
        return cls(
            can_toggle=d.get("can_toggle", None),
            enabled=d.get("enabled", None),
            enablement_details=_from_dict(d, "enablement_details", ClusterAutoRestartMessageEnablementDetails),
            maintenance_window=_from_dict(d, "maintenance_window", ClusterAutoRestartMessageMaintenanceWindow),
            restart_even_if_no_updates_available=d.get("restart_even_if_no_updates_available", None),
        )


@dataclass
class ClusterAutoRestartMessageEnablementDetails:
    """Contains an information about the enablement status judging (e.g. whether the enterprise tier is
    enabled) This is only additional information that MUST NOT be used to decide whether the setting
    is enabled or not. This is intended to use only for purposes like showing an error message to
    the customer with the additional details. For example, using these details we can check why
    exactly the feature is disabled for this customer."""

    forced_for_compliance_mode: Optional[bool] = None
    """The feature is force enabled if compliance mode is active"""

    unavailable_for_disabled_entitlement: Optional[bool] = None
    """The feature is unavailable if the corresponding entitlement disabled (see
    getShieldEntitlementEnable)"""

    unavailable_for_non_enterprise_tier: Optional[bool] = None
    """The feature is unavailable if the customer doesn't have enterprise tier"""

    def as_dict(self) -> dict:
        """Serializes the ClusterAutoRestartMessageEnablementDetails into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.forced_for_compliance_mode is not None:
            body["forced_for_compliance_mode"] = self.forced_for_compliance_mode
        if self.unavailable_for_disabled_entitlement is not None:
            body["unavailable_for_disabled_entitlement"] = self.unavailable_for_disabled_entitlement
        if self.unavailable_for_non_enterprise_tier is not None:
            body["unavailable_for_non_enterprise_tier"] = self.unavailable_for_non_enterprise_tier
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ClusterAutoRestartMessageEnablementDetails into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.forced_for_compliance_mode is not None:
            body["forced_for_compliance_mode"] = self.forced_for_compliance_mode
        if self.unavailable_for_disabled_entitlement is not None:
            body["unavailable_for_disabled_entitlement"] = self.unavailable_for_disabled_entitlement
        if self.unavailable_for_non_enterprise_tier is not None:
            body["unavailable_for_non_enterprise_tier"] = self.unavailable_for_non_enterprise_tier
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ClusterAutoRestartMessageEnablementDetails:
        """Deserializes the ClusterAutoRestartMessageEnablementDetails from a dictionary."""
        return cls(
            forced_for_compliance_mode=d.get("forced_for_compliance_mode", None),
            unavailable_for_disabled_entitlement=d.get("unavailable_for_disabled_entitlement", None),
            unavailable_for_non_enterprise_tier=d.get("unavailable_for_non_enterprise_tier", None),
        )


@dataclass
class ClusterAutoRestartMessageMaintenanceWindow:
    week_day_based_schedule: Optional[ClusterAutoRestartMessageMaintenanceWindowWeekDayBasedSchedule] = None

    def as_dict(self) -> dict:
        """Serializes the ClusterAutoRestartMessageMaintenanceWindow into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.week_day_based_schedule:
            body["week_day_based_schedule"] = self.week_day_based_schedule.as_dict()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ClusterAutoRestartMessageMaintenanceWindow into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.week_day_based_schedule:
            body["week_day_based_schedule"] = self.week_day_based_schedule
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ClusterAutoRestartMessageMaintenanceWindow:
        """Deserializes the ClusterAutoRestartMessageMaintenanceWindow from a dictionary."""
        return cls(
            week_day_based_schedule=_from_dict(
                d, "week_day_based_schedule", ClusterAutoRestartMessageMaintenanceWindowWeekDayBasedSchedule
            )
        )


class ClusterAutoRestartMessageMaintenanceWindowDayOfWeek(Enum):

    FRIDAY = "FRIDAY"
    MONDAY = "MONDAY"
    SATURDAY = "SATURDAY"
    SUNDAY = "SUNDAY"
    THURSDAY = "THURSDAY"
    TUESDAY = "TUESDAY"
    WEDNESDAY = "WEDNESDAY"


@dataclass
class ClusterAutoRestartMessageMaintenanceWindowWeekDayBasedSchedule:
    day_of_week: Optional[ClusterAutoRestartMessageMaintenanceWindowDayOfWeek] = None

    frequency: Optional[ClusterAutoRestartMessageMaintenanceWindowWeekDayFrequency] = None

    window_start_time: Optional[ClusterAutoRestartMessageMaintenanceWindowWindowStartTime] = None

    def as_dict(self) -> dict:
        """Serializes the ClusterAutoRestartMessageMaintenanceWindowWeekDayBasedSchedule into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.day_of_week is not None:
            body["day_of_week"] = self.day_of_week.value
        if self.frequency is not None:
            body["frequency"] = self.frequency.value
        if self.window_start_time:
            body["window_start_time"] = self.window_start_time.as_dict()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ClusterAutoRestartMessageMaintenanceWindowWeekDayBasedSchedule into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.day_of_week is not None:
            body["day_of_week"] = self.day_of_week
        if self.frequency is not None:
            body["frequency"] = self.frequency
        if self.window_start_time:
            body["window_start_time"] = self.window_start_time
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ClusterAutoRestartMessageMaintenanceWindowWeekDayBasedSchedule:
        """Deserializes the ClusterAutoRestartMessageMaintenanceWindowWeekDayBasedSchedule from a dictionary."""
        return cls(
            day_of_week=_enum(d, "day_of_week", ClusterAutoRestartMessageMaintenanceWindowDayOfWeek),
            frequency=_enum(d, "frequency", ClusterAutoRestartMessageMaintenanceWindowWeekDayFrequency),
            window_start_time=_from_dict(
                d, "window_start_time", ClusterAutoRestartMessageMaintenanceWindowWindowStartTime
            ),
        )


class ClusterAutoRestartMessageMaintenanceWindowWeekDayFrequency(Enum):

    EVERY_WEEK = "EVERY_WEEK"
    FIRST_AND_THIRD_OF_MONTH = "FIRST_AND_THIRD_OF_MONTH"
    FIRST_OF_MONTH = "FIRST_OF_MONTH"
    FOURTH_OF_MONTH = "FOURTH_OF_MONTH"
    SECOND_AND_FOURTH_OF_MONTH = "SECOND_AND_FOURTH_OF_MONTH"
    SECOND_OF_MONTH = "SECOND_OF_MONTH"
    THIRD_OF_MONTH = "THIRD_OF_MONTH"


@dataclass
class ClusterAutoRestartMessageMaintenanceWindowWindowStartTime:
    hours: Optional[int] = None

    minutes: Optional[int] = None

    def as_dict(self) -> dict:
        """Serializes the ClusterAutoRestartMessageMaintenanceWindowWindowStartTime into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.hours is not None:
            body["hours"] = self.hours
        if self.minutes is not None:
            body["minutes"] = self.minutes
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ClusterAutoRestartMessageMaintenanceWindowWindowStartTime into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.hours is not None:
            body["hours"] = self.hours
        if self.minutes is not None:
            body["minutes"] = self.minutes
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ClusterAutoRestartMessageMaintenanceWindowWindowStartTime:
        """Deserializes the ClusterAutoRestartMessageMaintenanceWindowWindowStartTime from a dictionary."""
        return cls(hours=d.get("hours", None), minutes=d.get("minutes", None))


@dataclass
class DefaultDataSecurityModeMessage:
    """Changes the behaviour of Jobs service when creating job clusters.

    Before this setting is introduced, all workspaces with metastore attached had behaviour matching
    SINGLE_USER setting.

    See: - go/defaultdatasecuritymode - go/defaultdatasecuritymode/setting - go/datasecuritymode"""

    status: DefaultDataSecurityModeMessageStatus

    def as_dict(self) -> dict:
        """Serializes the DefaultDataSecurityModeMessage into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.status is not None:
            body["status"] = self.status.value
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the DefaultDataSecurityModeMessage into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.status is not None:
            body["status"] = self.status
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> DefaultDataSecurityModeMessage:
        """Deserializes the DefaultDataSecurityModeMessage from a dictionary."""
        return cls(status=_enum(d, "status", DefaultDataSecurityModeMessageStatus))


class DefaultDataSecurityModeMessageStatus(Enum):

    NOT_SET = "NOT_SET"
    SINGLE_USER = "SINGLE_USER"
    USER_ISOLATION = "USER_ISOLATION"


@dataclass
class IntegerMessage:
    value: Optional[int] = None

    def as_dict(self) -> dict:
        """Serializes the IntegerMessage into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.value is not None:
            body["value"] = self.value
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the IntegerMessage into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.value is not None:
            body["value"] = self.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> IntegerMessage:
        """Deserializes the IntegerMessage from a dictionary."""
        return cls(value=d.get("value", None))


@dataclass
class ListAccountSettingsMetadataResponse:
    next_page_token: Optional[str] = None
    """A token that can be sent as `page_token` to retrieve the next page. If this field is omitted,
    there are no subsequent pages."""

    settings_metadata: Optional[List[SettingsMetadata]] = None
    """List of all settings available via public APIs and their metadata"""

    def as_dict(self) -> dict:
        """Serializes the ListAccountSettingsMetadataResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        if self.settings_metadata:
            body["settings_metadata"] = [v.as_dict() for v in self.settings_metadata]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ListAccountSettingsMetadataResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        if self.settings_metadata:
            body["settings_metadata"] = self.settings_metadata
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ListAccountSettingsMetadataResponse:
        """Deserializes the ListAccountSettingsMetadataResponse from a dictionary."""
        return cls(
            next_page_token=d.get("next_page_token", None),
            settings_metadata=_repeated_dict(d, "settings_metadata", SettingsMetadata),
        )


@dataclass
class ListWorkspaceSettingsMetadataResponse:
    next_page_token: Optional[str] = None
    """A token that can be sent as `page_token` to retrieve the next page. If this field is omitted,
    there are no subsequent pages."""

    settings_metadata: Optional[List[SettingsMetadata]] = None
    """List of all settings available via public APIs and their metadata"""

    def as_dict(self) -> dict:
        """Serializes the ListWorkspaceSettingsMetadataResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        if self.settings_metadata:
            body["settings_metadata"] = [v.as_dict() for v in self.settings_metadata]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ListWorkspaceSettingsMetadataResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.next_page_token is not None:
            body["next_page_token"] = self.next_page_token
        if self.settings_metadata:
            body["settings_metadata"] = self.settings_metadata
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ListWorkspaceSettingsMetadataResponse:
        """Deserializes the ListWorkspaceSettingsMetadataResponse from a dictionary."""
        return cls(
            next_page_token=d.get("next_page_token", None),
            settings_metadata=_repeated_dict(d, "settings_metadata", SettingsMetadata),
        )


@dataclass
class PersonalComputeMessage:
    value: Optional[PersonalComputeMessagePersonalComputeMessageEnum] = None

    def as_dict(self) -> dict:
        """Serializes the PersonalComputeMessage into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.value is not None:
            body["value"] = self.value.value
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the PersonalComputeMessage into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.value is not None:
            body["value"] = self.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> PersonalComputeMessage:
        """Deserializes the PersonalComputeMessage from a dictionary."""
        return cls(value=_enum(d, "value", PersonalComputeMessagePersonalComputeMessageEnum))


class PersonalComputeMessagePersonalComputeMessageEnum(Enum):
    """ON: Grants all users in all workspaces access to the Personal Compute default policy, allowing
    all users to create single-machine compute resources. DELEGATE: Moves access control for the
    Personal Compute default policy to individual workspaces and requires a workspace’s users or
    groups to be added to the ACLs of that workspace’s Personal Compute default policy before they
    will be able to create compute resources through that policy."""

    DELEGATE = "DELEGATE"
    ON = "ON"


@dataclass
class RestrictWorkspaceAdminsMessage:
    status: RestrictWorkspaceAdminsMessageStatus

    def as_dict(self) -> dict:
        """Serializes the RestrictWorkspaceAdminsMessage into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.status is not None:
            body["status"] = self.status.value
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the RestrictWorkspaceAdminsMessage into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.status is not None:
            body["status"] = self.status
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> RestrictWorkspaceAdminsMessage:
        """Deserializes the RestrictWorkspaceAdminsMessage from a dictionary."""
        return cls(status=_enum(d, "status", RestrictWorkspaceAdminsMessageStatus))


class RestrictWorkspaceAdminsMessageStatus(Enum):

    ALLOW_ALL = "ALLOW_ALL"
    RESTRICT_TOKENS_AND_JOB_RUN_AS = "RESTRICT_TOKENS_AND_JOB_RUN_AS"


@dataclass
class Setting:
    aibi_dashboard_embedding_access_policy: Optional[AibiDashboardEmbeddingAccessPolicy] = None

    aibi_dashboard_embedding_approved_domains: Optional[AibiDashboardEmbeddingApprovedDomains] = None

    automatic_cluster_update_workspace: Optional[ClusterAutoRestartMessage] = None
    """todo: Mark these Public after onboarded to DSL"""

    boolean_val: Optional[BooleanMessage] = None

    default_data_security_mode: Optional[DefaultDataSecurityModeMessage] = None

    effective_aibi_dashboard_embedding_access_policy: Optional[AibiDashboardEmbeddingAccessPolicy] = None

    effective_aibi_dashboard_embedding_approved_domains: Optional[AibiDashboardEmbeddingApprovedDomains] = None

    effective_automatic_cluster_update_workspace: Optional[ClusterAutoRestartMessage] = None

    effective_boolean_val: Optional[BooleanMessage] = None

    effective_default_data_security_mode: Optional[DefaultDataSecurityModeMessage] = None

    effective_integer_val: Optional[IntegerMessage] = None

    effective_personal_compute: Optional[PersonalComputeMessage] = None

    effective_restrict_workspace_admins: Optional[RestrictWorkspaceAdminsMessage] = None

    effective_string_val: Optional[StringMessage] = None

    integer_val: Optional[IntegerMessage] = None

    name: Optional[str] = None
    """Name of the setting."""

    personal_compute: Optional[PersonalComputeMessage] = None

    restrict_workspace_admins: Optional[RestrictWorkspaceAdminsMessage] = None

    string_val: Optional[StringMessage] = None

    def as_dict(self) -> dict:
        """Serializes the Setting into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.aibi_dashboard_embedding_access_policy:
            body["aibi_dashboard_embedding_access_policy"] = self.aibi_dashboard_embedding_access_policy.as_dict()
        if self.aibi_dashboard_embedding_approved_domains:
            body["aibi_dashboard_embedding_approved_domains"] = self.aibi_dashboard_embedding_approved_domains.as_dict()
        if self.automatic_cluster_update_workspace:
            body["automatic_cluster_update_workspace"] = self.automatic_cluster_update_workspace.as_dict()
        if self.boolean_val:
            body["boolean_val"] = self.boolean_val.as_dict()
        if self.default_data_security_mode:
            body["default_data_security_mode"] = self.default_data_security_mode.as_dict()
        if self.effective_aibi_dashboard_embedding_access_policy:
            body["effective_aibi_dashboard_embedding_access_policy"] = (
                self.effective_aibi_dashboard_embedding_access_policy.as_dict()
            )
        if self.effective_aibi_dashboard_embedding_approved_domains:
            body["effective_aibi_dashboard_embedding_approved_domains"] = (
                self.effective_aibi_dashboard_embedding_approved_domains.as_dict()
            )
        if self.effective_automatic_cluster_update_workspace:
            body["effective_automatic_cluster_update_workspace"] = (
                self.effective_automatic_cluster_update_workspace.as_dict()
            )
        if self.effective_boolean_val:
            body["effective_boolean_val"] = self.effective_boolean_val.as_dict()
        if self.effective_default_data_security_mode:
            body["effective_default_data_security_mode"] = self.effective_default_data_security_mode.as_dict()
        if self.effective_integer_val:
            body["effective_integer_val"] = self.effective_integer_val.as_dict()
        if self.effective_personal_compute:
            body["effective_personal_compute"] = self.effective_personal_compute.as_dict()
        if self.effective_restrict_workspace_admins:
            body["effective_restrict_workspace_admins"] = self.effective_restrict_workspace_admins.as_dict()
        if self.effective_string_val:
            body["effective_string_val"] = self.effective_string_val.as_dict()
        if self.integer_val:
            body["integer_val"] = self.integer_val.as_dict()
        if self.name is not None:
            body["name"] = self.name
        if self.personal_compute:
            body["personal_compute"] = self.personal_compute.as_dict()
        if self.restrict_workspace_admins:
            body["restrict_workspace_admins"] = self.restrict_workspace_admins.as_dict()
        if self.string_val:
            body["string_val"] = self.string_val.as_dict()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the Setting into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.aibi_dashboard_embedding_access_policy:
            body["aibi_dashboard_embedding_access_policy"] = self.aibi_dashboard_embedding_access_policy
        if self.aibi_dashboard_embedding_approved_domains:
            body["aibi_dashboard_embedding_approved_domains"] = self.aibi_dashboard_embedding_approved_domains
        if self.automatic_cluster_update_workspace:
            body["automatic_cluster_update_workspace"] = self.automatic_cluster_update_workspace
        if self.boolean_val:
            body["boolean_val"] = self.boolean_val
        if self.default_data_security_mode:
            body["default_data_security_mode"] = self.default_data_security_mode
        if self.effective_aibi_dashboard_embedding_access_policy:
            body["effective_aibi_dashboard_embedding_access_policy"] = (
                self.effective_aibi_dashboard_embedding_access_policy
            )
        if self.effective_aibi_dashboard_embedding_approved_domains:
            body["effective_aibi_dashboard_embedding_approved_domains"] = (
                self.effective_aibi_dashboard_embedding_approved_domains
            )
        if self.effective_automatic_cluster_update_workspace:
            body["effective_automatic_cluster_update_workspace"] = self.effective_automatic_cluster_update_workspace
        if self.effective_boolean_val:
            body["effective_boolean_val"] = self.effective_boolean_val
        if self.effective_default_data_security_mode:
            body["effective_default_data_security_mode"] = self.effective_default_data_security_mode
        if self.effective_integer_val:
            body["effective_integer_val"] = self.effective_integer_val
        if self.effective_personal_compute:
            body["effective_personal_compute"] = self.effective_personal_compute
        if self.effective_restrict_workspace_admins:
            body["effective_restrict_workspace_admins"] = self.effective_restrict_workspace_admins
        if self.effective_string_val:
            body["effective_string_val"] = self.effective_string_val
        if self.integer_val:
            body["integer_val"] = self.integer_val
        if self.name is not None:
            body["name"] = self.name
        if self.personal_compute:
            body["personal_compute"] = self.personal_compute
        if self.restrict_workspace_admins:
            body["restrict_workspace_admins"] = self.restrict_workspace_admins
        if self.string_val:
            body["string_val"] = self.string_val
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> Setting:
        """Deserializes the Setting from a dictionary."""
        return cls(
            aibi_dashboard_embedding_access_policy=_from_dict(
                d, "aibi_dashboard_embedding_access_policy", AibiDashboardEmbeddingAccessPolicy
            ),
            aibi_dashboard_embedding_approved_domains=_from_dict(
                d, "aibi_dashboard_embedding_approved_domains", AibiDashboardEmbeddingApprovedDomains
            ),
            automatic_cluster_update_workspace=_from_dict(
                d, "automatic_cluster_update_workspace", ClusterAutoRestartMessage
            ),
            boolean_val=_from_dict(d, "boolean_val", BooleanMessage),
            default_data_security_mode=_from_dict(d, "default_data_security_mode", DefaultDataSecurityModeMessage),
            effective_aibi_dashboard_embedding_access_policy=_from_dict(
                d, "effective_aibi_dashboard_embedding_access_policy", AibiDashboardEmbeddingAccessPolicy
            ),
            effective_aibi_dashboard_embedding_approved_domains=_from_dict(
                d, "effective_aibi_dashboard_embedding_approved_domains", AibiDashboardEmbeddingApprovedDomains
            ),
            effective_automatic_cluster_update_workspace=_from_dict(
                d, "effective_automatic_cluster_update_workspace", ClusterAutoRestartMessage
            ),
            effective_boolean_val=_from_dict(d, "effective_boolean_val", BooleanMessage),
            effective_default_data_security_mode=_from_dict(
                d, "effective_default_data_security_mode", DefaultDataSecurityModeMessage
            ),
            effective_integer_val=_from_dict(d, "effective_integer_val", IntegerMessage),
            effective_personal_compute=_from_dict(d, "effective_personal_compute", PersonalComputeMessage),
            effective_restrict_workspace_admins=_from_dict(
                d, "effective_restrict_workspace_admins", RestrictWorkspaceAdminsMessage
            ),
            effective_string_val=_from_dict(d, "effective_string_val", StringMessage),
            integer_val=_from_dict(d, "integer_val", IntegerMessage),
            name=d.get("name", None),
            personal_compute=_from_dict(d, "personal_compute", PersonalComputeMessage),
            restrict_workspace_admins=_from_dict(d, "restrict_workspace_admins", RestrictWorkspaceAdminsMessage),
            string_val=_from_dict(d, "string_val", StringMessage),
        )


@dataclass
class SettingsMetadata:
    description: Optional[str] = None
    """Setting description for what this setting controls"""

    docs_link: Optional[str] = None
    """Link to databricks documentation for the setting"""

    name: Optional[str] = None
    """Name of the setting."""

    type: Optional[str] = None
    """Type of the setting. To set this setting, the value sent must match this type."""

    def as_dict(self) -> dict:
        """Serializes the SettingsMetadata into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.description is not None:
            body["description"] = self.description
        if self.docs_link is not None:
            body["docs_link"] = self.docs_link
        if self.name is not None:
            body["name"] = self.name
        if self.type is not None:
            body["type"] = self.type
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the SettingsMetadata into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.description is not None:
            body["description"] = self.description
        if self.docs_link is not None:
            body["docs_link"] = self.docs_link
        if self.name is not None:
            body["name"] = self.name
        if self.type is not None:
            body["type"] = self.type
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> SettingsMetadata:
        """Deserializes the SettingsMetadata from a dictionary."""
        return cls(
            description=d.get("description", None),
            docs_link=d.get("docs_link", None),
            name=d.get("name", None),
            type=d.get("type", None),
        )


@dataclass
class StringMessage:
    value: Optional[str] = None
    """Represents a generic string value."""

    def as_dict(self) -> dict:
        """Serializes the StringMessage into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.value is not None:
            body["value"] = self.value
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the StringMessage into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.value is not None:
            body["value"] = self.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> StringMessage:
        """Deserializes the StringMessage from a dictionary."""
        return cls(value=d.get("value", None))


class AccountSettingsV2API:
    """APIs to manage account level settings"""

    def __init__(self, api_client):
        self._api = api_client

    def get_public_account_setting(self, name: str) -> Setting:
        """Get a setting value at account level

        :param name: str

        :returns: :class:`Setting`
        """

        headers = {
            "Accept": "application/json",
        }

        res = self._api.do("GET", f"/api/2.1/accounts/{self._api.account_id}/settings/{name}", headers=headers)
        return Setting.from_dict(res)

    def list_account_settings_metadata(
        self, *, page_size: Optional[int] = None, page_token: Optional[str] = None
    ) -> Iterator[SettingsMetadata]:
        """List valid setting keys and metadata. These settings are available to referenced via [GET
        /api/2.1/settings/{name}](#~1api~1account~1settingsv2~1getpublicaccountsetting) and [PATCH
        /api/2.1/settings/{name}](#~1api~1account~1settingsv2~patchpublicaccountsetting) APIs

        :param page_size: int (optional)
          The maximum number of settings to return. The service may return fewer than this value. If
          unspecified, at most 200 settings will be returned. The maximum value is 1000; values above 1000
          will be coerced to 1000.
        :param page_token: str (optional)
          A page token, received from a previous `ListAccountSettingsMetadataRequest` call. Provide this to
          retrieve the subsequent page.

          When paginating, all other parameters provided to `ListAccountSettingsMetadataRequest` must match
          the call that provided the page token.

        :returns: Iterator over :class:`SettingsMetadata`
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
            json = self._api.do(
                "GET", f"/api/2.1/accounts/{self._api.account_id}/settings-metadata", query=query, headers=headers
            )
            if "settings_metadata" in json:
                for v in json["settings_metadata"]:
                    yield SettingsMetadata.from_dict(v)
            if "next_page_token" not in json or not json["next_page_token"]:
                return
            query["page_token"] = json["next_page_token"]

    def patch_public_account_setting(self, name: str, setting: Setting) -> Setting:
        """Patch a setting value at account level

        :param name: str
        :param setting: :class:`Setting`

        :returns: :class:`Setting`
        """
        body = setting.as_dict()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do(
            "PATCH", f"/api/2.1/accounts/{self._api.account_id}/settings/{name}", body=body, headers=headers
        )
        return Setting.from_dict(res)


class WorkspaceSettingsV2API:
    """APIs to manage workspace level settings"""

    def __init__(self, api_client):
        self._api = api_client

    def get_public_workspace_setting(self, name: str) -> Setting:
        """Get a setting value at workspace level

        :param name: str

        :returns: :class:`Setting`
        """

        headers = {
            "Accept": "application/json",
        }

        res = self._api.do("GET", f"/api/2.1/settings/{name}", headers=headers)
        return Setting.from_dict(res)

    def list_workspace_settings_metadata(
        self, *, page_size: Optional[int] = None, page_token: Optional[str] = None
    ) -> Iterator[SettingsMetadata]:
        """List valid setting keys and metadata. These settings are available to referenced via [GET
        /api/2.1/settings/{name}](#~1api~1workspace~1settingsv2~1getpublicworkspacesetting) and [PATCH
        /api/2.1/settings/{name}](#~1api~1workspace~1settingsv2~patchpublicworkspacesetting) APIs

        :param page_size: int (optional)
          The maximum number of settings to return. The service may return fewer than this value. If
          unspecified, at most 200 settings will be returned. The maximum value is 1000; values above 1000
          will be coerced to 1000.
        :param page_token: str (optional)
          A page token, received from a previous `ListWorkspaceSettingsMetadataRequest` call. Provide this to
          retrieve the subsequent page.

          When paginating, all other parameters provided to `ListWorkspaceSettingsMetadataRequest` must match
          the call that provided the page token.

        :returns: Iterator over :class:`SettingsMetadata`
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
            json = self._api.do("GET", "/api/2.1/settings-metadata", query=query, headers=headers)
            if "settings_metadata" in json:
                for v in json["settings_metadata"]:
                    yield SettingsMetadata.from_dict(v)
            if "next_page_token" not in json or not json["next_page_token"]:
                return
            query["page_token"] = json["next_page_token"]

    def patch_public_workspace_setting(self, name: str, setting: Setting) -> Setting:
        """Patch a setting value at workspace level

        :param name: str
        :param setting: :class:`Setting`

        :returns: :class:`Setting`
        """
        body = setting.as_dict()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do("PATCH", f"/api/2.1/settings/{name}", body=body, headers=headers)
        return Setting.from_dict(res)
