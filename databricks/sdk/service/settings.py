# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

from __future__ import annotations

import logging
from dataclasses import dataclass
from enum import Enum
from typing import Dict, Iterator, List, Optional

from ._internal import _enum, _from_dict, _repeated_dict, _repeated_enum

_LOG = logging.getLogger('databricks.sdk')

# all definitions in this file are in alphabetical order


@dataclass
class AutomaticClusterUpdateSetting:
    automatic_cluster_update_workspace: ClusterAutoRestartMessage

    etag: Optional[str] = None
    """etag used for versioning. The response is at least as fresh as the eTag provided. This is used
    for optimistic concurrency control as a way to help prevent simultaneous writes of a setting
    overwriting each other. It is strongly suggested that systems make use of the etag in the read
    -> update pattern to perform setting updates in order to avoid race conditions. That is, get an
    etag from a GET request, and pass it with the PATCH request to identify the setting version you
    are updating."""

    setting_name: Optional[str] = None
    """Name of the corresponding setting. This field is populated in the response, but it will not be
    respected even if it's set in the request body. The setting name in the path parameter will be
    respected instead. Setting name is required to be 'default' if the setting only has one instance
    per workspace."""

    def as_dict(self) -> dict:
        """Serializes the AutomaticClusterUpdateSetting into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.automatic_cluster_update_workspace:
            body['automatic_cluster_update_workspace'] = self.automatic_cluster_update_workspace.as_dict()
        if self.etag is not None: body['etag'] = self.etag
        if self.setting_name is not None: body['setting_name'] = self.setting_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> AutomaticClusterUpdateSetting:
        """Deserializes the AutomaticClusterUpdateSetting from a dictionary."""
        return cls(automatic_cluster_update_workspace=_from_dict(d, 'automatic_cluster_update_workspace',
                                                                 ClusterAutoRestartMessage),
                   etag=d.get('etag', None),
                   setting_name=d.get('setting_name', None))


@dataclass
class BooleanMessage:
    value: Optional[bool] = None

    def as_dict(self) -> dict:
        """Serializes the BooleanMessage into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.value is not None: body['value'] = self.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> BooleanMessage:
        """Deserializes the BooleanMessage from a dictionary."""
        return cls(value=d.get('value', None))


@dataclass
class ClusterAutoRestartMessage:
    can_toggle: Optional[bool] = None

    enabled: Optional[bool] = None

    enablement_details: Optional[ClusterAutoRestartMessageEnablementDetails] = None
    """Contains an information about the enablement status judging (e.g. whether the enterprise tier is
    enabled) This is only additional information that MUST NOT be used to decide whether the setting
    is enabled or not. This is intended to use only for purposes like showing an error message to
    the customer with the additional details. For example, using these details we can check why
    exactly the feature is disabled for this customer."""

    maintenance_window: Optional[ClusterAutoRestartMessageMaintenanceWindow] = None

    restart_even_if_no_updates_available: Optional[bool] = None

    def as_dict(self) -> dict:
        """Serializes the ClusterAutoRestartMessage into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.can_toggle is not None: body['can_toggle'] = self.can_toggle
        if self.enabled is not None: body['enabled'] = self.enabled
        if self.enablement_details: body['enablement_details'] = self.enablement_details.as_dict()
        if self.maintenance_window: body['maintenance_window'] = self.maintenance_window.as_dict()
        if self.restart_even_if_no_updates_available is not None:
            body['restart_even_if_no_updates_available'] = self.restart_even_if_no_updates_available
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ClusterAutoRestartMessage:
        """Deserializes the ClusterAutoRestartMessage from a dictionary."""
        return cls(can_toggle=d.get('can_toggle', None),
                   enabled=d.get('enabled', None),
                   enablement_details=_from_dict(d, 'enablement_details',
                                                 ClusterAutoRestartMessageEnablementDetails),
                   maintenance_window=_from_dict(d, 'maintenance_window',
                                                 ClusterAutoRestartMessageMaintenanceWindow),
                   restart_even_if_no_updates_available=d.get('restart_even_if_no_updates_available', None))


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
            body['forced_for_compliance_mode'] = self.forced_for_compliance_mode
        if self.unavailable_for_disabled_entitlement is not None:
            body['unavailable_for_disabled_entitlement'] = self.unavailable_for_disabled_entitlement
        if self.unavailable_for_non_enterprise_tier is not None:
            body['unavailable_for_non_enterprise_tier'] = self.unavailable_for_non_enterprise_tier
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ClusterAutoRestartMessageEnablementDetails:
        """Deserializes the ClusterAutoRestartMessageEnablementDetails from a dictionary."""
        return cls(forced_for_compliance_mode=d.get('forced_for_compliance_mode', None),
                   unavailable_for_disabled_entitlement=d.get('unavailable_for_disabled_entitlement', None),
                   unavailable_for_non_enterprise_tier=d.get('unavailable_for_non_enterprise_tier', None))


@dataclass
class ClusterAutoRestartMessageMaintenanceWindow:
    week_day_based_schedule: Optional[ClusterAutoRestartMessageMaintenanceWindowWeekDayBasedSchedule] = None

    def as_dict(self) -> dict:
        """Serializes the ClusterAutoRestartMessageMaintenanceWindow into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.week_day_based_schedule:
            body['week_day_based_schedule'] = self.week_day_based_schedule.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ClusterAutoRestartMessageMaintenanceWindow:
        """Deserializes the ClusterAutoRestartMessageMaintenanceWindow from a dictionary."""
        return cls(week_day_based_schedule=_from_dict(
            d, 'week_day_based_schedule', ClusterAutoRestartMessageMaintenanceWindowWeekDayBasedSchedule))


class ClusterAutoRestartMessageMaintenanceWindowDayOfWeek(Enum):

    FRIDAY = 'FRIDAY'
    MONDAY = 'MONDAY'
    SATURDAY = 'SATURDAY'
    SUNDAY = 'SUNDAY'
    THURSDAY = 'THURSDAY'
    TUESDAY = 'TUESDAY'
    WEDNESDAY = 'WEDNESDAY'


@dataclass
class ClusterAutoRestartMessageMaintenanceWindowWeekDayBasedSchedule:
    day_of_week: Optional[ClusterAutoRestartMessageMaintenanceWindowDayOfWeek] = None

    frequency: Optional[ClusterAutoRestartMessageMaintenanceWindowWeekDayFrequency] = None

    window_start_time: Optional[ClusterAutoRestartMessageMaintenanceWindowWindowStartTime] = None

    def as_dict(self) -> dict:
        """Serializes the ClusterAutoRestartMessageMaintenanceWindowWeekDayBasedSchedule into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.day_of_week is not None: body['day_of_week'] = self.day_of_week.value
        if self.frequency is not None: body['frequency'] = self.frequency.value
        if self.window_start_time: body['window_start_time'] = self.window_start_time.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ClusterAutoRestartMessageMaintenanceWindowWeekDayBasedSchedule:
        """Deserializes the ClusterAutoRestartMessageMaintenanceWindowWeekDayBasedSchedule from a dictionary."""
        return cls(day_of_week=_enum(d, 'day_of_week', ClusterAutoRestartMessageMaintenanceWindowDayOfWeek),
                   frequency=_enum(d, 'frequency',
                                   ClusterAutoRestartMessageMaintenanceWindowWeekDayFrequency),
                   window_start_time=_from_dict(d, 'window_start_time',
                                                ClusterAutoRestartMessageMaintenanceWindowWindowStartTime))


class ClusterAutoRestartMessageMaintenanceWindowWeekDayFrequency(Enum):

    EVERY_WEEK = 'EVERY_WEEK'
    FIRST_AND_THIRD_OF_MONTH = 'FIRST_AND_THIRD_OF_MONTH'
    FIRST_OF_MONTH = 'FIRST_OF_MONTH'
    FOURTH_OF_MONTH = 'FOURTH_OF_MONTH'
    SECOND_AND_FOURTH_OF_MONTH = 'SECOND_AND_FOURTH_OF_MONTH'
    SECOND_OF_MONTH = 'SECOND_OF_MONTH'
    THIRD_OF_MONTH = 'THIRD_OF_MONTH'


@dataclass
class ClusterAutoRestartMessageMaintenanceWindowWindowStartTime:
    hours: Optional[int] = None

    minutes: Optional[int] = None

    def as_dict(self) -> dict:
        """Serializes the ClusterAutoRestartMessageMaintenanceWindowWindowStartTime into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.hours is not None: body['hours'] = self.hours
        if self.minutes is not None: body['minutes'] = self.minutes
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ClusterAutoRestartMessageMaintenanceWindowWindowStartTime:
        """Deserializes the ClusterAutoRestartMessageMaintenanceWindowWindowStartTime from a dictionary."""
        return cls(hours=d.get('hours', None), minutes=d.get('minutes', None))


@dataclass
class ComplianceSecurityProfile:
    """SHIELD feature: CSP"""

    compliance_standards: Optional[List[ComplianceStandard]] = None
    """Set by customers when they request Compliance Security Profile (CSP)"""

    is_enabled: Optional[bool] = None

    def as_dict(self) -> dict:
        """Serializes the ComplianceSecurityProfile into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.compliance_standards:
            body['compliance_standards'] = [v.value for v in self.compliance_standards]
        if self.is_enabled is not None: body['is_enabled'] = self.is_enabled
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ComplianceSecurityProfile:
        """Deserializes the ComplianceSecurityProfile from a dictionary."""
        return cls(compliance_standards=_repeated_enum(d, 'compliance_standards', ComplianceStandard),
                   is_enabled=d.get('is_enabled', None))


@dataclass
class ComplianceSecurityProfileSetting:
    compliance_security_profile_workspace: ComplianceSecurityProfile
    """SHIELD feature: CSP"""

    etag: Optional[str] = None
    """etag used for versioning. The response is at least as fresh as the eTag provided. This is used
    for optimistic concurrency control as a way to help prevent simultaneous writes of a setting
    overwriting each other. It is strongly suggested that systems make use of the etag in the read
    -> update pattern to perform setting updates in order to avoid race conditions. That is, get an
    etag from a GET request, and pass it with the PATCH request to identify the setting version you
    are updating."""

    setting_name: Optional[str] = None
    """Name of the corresponding setting. This field is populated in the response, but it will not be
    respected even if it's set in the request body. The setting name in the path parameter will be
    respected instead. Setting name is required to be 'default' if the setting only has one instance
    per workspace."""

    def as_dict(self) -> dict:
        """Serializes the ComplianceSecurityProfileSetting into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.compliance_security_profile_workspace:
            body[
                'compliance_security_profile_workspace'] = self.compliance_security_profile_workspace.as_dict(
                )
        if self.etag is not None: body['etag'] = self.etag
        if self.setting_name is not None: body['setting_name'] = self.setting_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ComplianceSecurityProfileSetting:
        """Deserializes the ComplianceSecurityProfileSetting from a dictionary."""
        return cls(compliance_security_profile_workspace=_from_dict(d,
                                                                    'compliance_security_profile_workspace',
                                                                    ComplianceSecurityProfile),
                   etag=d.get('etag', None),
                   setting_name=d.get('setting_name', None))


class ComplianceStandard(Enum):
    """Compliance stardard for SHIELD customers"""

    CANADA_PROTECTED_B = 'CANADA_PROTECTED_B'
    CYBER_ESSENTIAL_PLUS = 'CYBER_ESSENTIAL_PLUS'
    FEDRAMP_HIGH = 'FEDRAMP_HIGH'
    FEDRAMP_IL5 = 'FEDRAMP_IL5'
    FEDRAMP_MODERATE = 'FEDRAMP_MODERATE'
    HIPAA = 'HIPAA'
    IRAP_PROTECTED = 'IRAP_PROTECTED'
    ITAR_EAR = 'ITAR_EAR'
    NONE = 'NONE'
    PCI_DSS = 'PCI_DSS'


@dataclass
class Config:
    email: Optional[EmailConfig] = None

    generic_webhook: Optional[GenericWebhookConfig] = None

    microsoft_teams: Optional[MicrosoftTeamsConfig] = None

    pagerduty: Optional[PagerdutyConfig] = None

    slack: Optional[SlackConfig] = None

    def as_dict(self) -> dict:
        """Serializes the Config into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.email: body['email'] = self.email.as_dict()
        if self.generic_webhook: body['generic_webhook'] = self.generic_webhook.as_dict()
        if self.microsoft_teams: body['microsoft_teams'] = self.microsoft_teams.as_dict()
        if self.pagerduty: body['pagerduty'] = self.pagerduty.as_dict()
        if self.slack: body['slack'] = self.slack.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> Config:
        """Deserializes the Config from a dictionary."""
        return cls(email=_from_dict(d, 'email', EmailConfig),
                   generic_webhook=_from_dict(d, 'generic_webhook', GenericWebhookConfig),
                   microsoft_teams=_from_dict(d, 'microsoft_teams', MicrosoftTeamsConfig),
                   pagerduty=_from_dict(d, 'pagerduty', PagerdutyConfig),
                   slack=_from_dict(d, 'slack', SlackConfig))


@dataclass
class CreateIpAccessList:
    """Details required to configure a block list or allow list."""

    label: str
    """Label for the IP access list. This **cannot** be empty."""

    list_type: ListType
    """Type of IP access list. Valid values are as follows and are case-sensitive:
    
    * `ALLOW`: An allow list. Include this IP or range. * `BLOCK`: A block list. Exclude this IP or
    range. IP addresses in the block list are excluded even if they are included in an allow list."""

    ip_addresses: Optional[List[str]] = None

    def as_dict(self) -> dict:
        """Serializes the CreateIpAccessList into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.ip_addresses: body['ip_addresses'] = [v for v in self.ip_addresses]
        if self.label is not None: body['label'] = self.label
        if self.list_type is not None: body['list_type'] = self.list_type.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> CreateIpAccessList:
        """Deserializes the CreateIpAccessList from a dictionary."""
        return cls(ip_addresses=d.get('ip_addresses', None),
                   label=d.get('label', None),
                   list_type=_enum(d, 'list_type', ListType))


@dataclass
class CreateIpAccessListResponse:
    """An IP access list was successfully created."""

    ip_access_list: Optional[IpAccessListInfo] = None
    """Definition of an IP Access list"""

    def as_dict(self) -> dict:
        """Serializes the CreateIpAccessListResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.ip_access_list: body['ip_access_list'] = self.ip_access_list.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> CreateIpAccessListResponse:
        """Deserializes the CreateIpAccessListResponse from a dictionary."""
        return cls(ip_access_list=_from_dict(d, 'ip_access_list', IpAccessListInfo))


@dataclass
class CreateNetworkConnectivityConfigRequest:
    name: str
    """The name of the network connectivity configuration. The name can contain alphanumeric
    characters, hyphens, and underscores. The length must be between 3 and 30 characters. The name
    must match the regular expression `^[0-9a-zA-Z-_]{3,30}$`."""

    region: str
    """The region for the network connectivity configuration. Only workspaces in the same region can be
    attached to the network connectivity configuration."""

    def as_dict(self) -> dict:
        """Serializes the CreateNetworkConnectivityConfigRequest into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.name is not None: body['name'] = self.name
        if self.region is not None: body['region'] = self.region
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> CreateNetworkConnectivityConfigRequest:
        """Deserializes the CreateNetworkConnectivityConfigRequest from a dictionary."""
        return cls(name=d.get('name', None), region=d.get('region', None))


@dataclass
class CreateNotificationDestinationRequest:
    config: Optional[Config] = None
    """The configuration for the notification destination. Must wrap EXACTLY one of the nested configs."""

    display_name: Optional[str] = None
    """The display name for the notification destination."""

    def as_dict(self) -> dict:
        """Serializes the CreateNotificationDestinationRequest into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.config: body['config'] = self.config.as_dict()
        if self.display_name is not None: body['display_name'] = self.display_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> CreateNotificationDestinationRequest:
        """Deserializes the CreateNotificationDestinationRequest from a dictionary."""
        return cls(config=_from_dict(d, 'config', Config), display_name=d.get('display_name', None))


@dataclass
class CreateOboTokenRequest:
    """Configuration details for creating on-behalf tokens."""

    application_id: str
    """Application ID of the service principal."""

    comment: Optional[str] = None
    """Comment that describes the purpose of the token."""

    lifetime_seconds: Optional[int] = None
    """The number of seconds before the token expires."""

    def as_dict(self) -> dict:
        """Serializes the CreateOboTokenRequest into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.application_id is not None: body['application_id'] = self.application_id
        if self.comment is not None: body['comment'] = self.comment
        if self.lifetime_seconds is not None: body['lifetime_seconds'] = self.lifetime_seconds
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> CreateOboTokenRequest:
        """Deserializes the CreateOboTokenRequest from a dictionary."""
        return cls(application_id=d.get('application_id', None),
                   comment=d.get('comment', None),
                   lifetime_seconds=d.get('lifetime_seconds', None))


@dataclass
class CreateOboTokenResponse:
    """An on-behalf token was successfully created for the service principal."""

    token_info: Optional[TokenInfo] = None

    token_value: Optional[str] = None
    """Value of the token."""

    def as_dict(self) -> dict:
        """Serializes the CreateOboTokenResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.token_info: body['token_info'] = self.token_info.as_dict()
        if self.token_value is not None: body['token_value'] = self.token_value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> CreateOboTokenResponse:
        """Deserializes the CreateOboTokenResponse from a dictionary."""
        return cls(token_info=_from_dict(d, 'token_info', TokenInfo), token_value=d.get('token_value', None))


@dataclass
class CreatePrivateEndpointRuleRequest:
    resource_id: str
    """The Azure resource ID of the target resource."""

    group_id: CreatePrivateEndpointRuleRequestGroupId
    """The sub-resource type (group ID) of the target resource. Note that to connect to workspace root
    storage (root DBFS), you need two endpoints, one for `blob` and one for `dfs`."""

    network_connectivity_config_id: Optional[str] = None
    """Your Network Connectvity Configuration ID."""

    def as_dict(self) -> dict:
        """Serializes the CreatePrivateEndpointRuleRequest into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.group_id is not None: body['group_id'] = self.group_id.value
        if self.network_connectivity_config_id is not None:
            body['network_connectivity_config_id'] = self.network_connectivity_config_id
        if self.resource_id is not None: body['resource_id'] = self.resource_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> CreatePrivateEndpointRuleRequest:
        """Deserializes the CreatePrivateEndpointRuleRequest from a dictionary."""
        return cls(group_id=_enum(d, 'group_id', CreatePrivateEndpointRuleRequestGroupId),
                   network_connectivity_config_id=d.get('network_connectivity_config_id', None),
                   resource_id=d.get('resource_id', None))


class CreatePrivateEndpointRuleRequestGroupId(Enum):
    """The sub-resource type (group ID) of the target resource. Note that to connect to workspace root
    storage (root DBFS), you need two endpoints, one for `blob` and one for `dfs`."""

    BLOB = 'blob'
    DFS = 'dfs'
    MYSQL_SERVER = 'mysqlServer'
    SQL_SERVER = 'sqlServer'


@dataclass
class CreateTokenRequest:
    comment: Optional[str] = None
    """Optional description to attach to the token."""

    lifetime_seconds: Optional[int] = None
    """The lifetime of the token, in seconds.
    
    If the lifetime is not specified, this token remains valid indefinitely."""

    def as_dict(self) -> dict:
        """Serializes the CreateTokenRequest into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.comment is not None: body['comment'] = self.comment
        if self.lifetime_seconds is not None: body['lifetime_seconds'] = self.lifetime_seconds
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> CreateTokenRequest:
        """Deserializes the CreateTokenRequest from a dictionary."""
        return cls(comment=d.get('comment', None), lifetime_seconds=d.get('lifetime_seconds', None))


@dataclass
class CreateTokenResponse:
    token_info: Optional[PublicTokenInfo] = None
    """The information for the new token."""

    token_value: Optional[str] = None
    """The value of the new token."""

    def as_dict(self) -> dict:
        """Serializes the CreateTokenResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.token_info: body['token_info'] = self.token_info.as_dict()
        if self.token_value is not None: body['token_value'] = self.token_value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> CreateTokenResponse:
        """Deserializes the CreateTokenResponse from a dictionary."""
        return cls(token_info=_from_dict(d, 'token_info', PublicTokenInfo),
                   token_value=d.get('token_value', None))


@dataclass
class CspEnablementAccount:
    """Account level policy for CSP"""

    compliance_standards: Optional[List[ComplianceStandard]] = None
    """Set by customers when they request Compliance Security Profile (CSP) Invariants are enforced in
    Settings policy."""

    is_enforced: Optional[bool] = None
    """Enforced = it cannot be overriden at workspace level."""

    def as_dict(self) -> dict:
        """Serializes the CspEnablementAccount into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.compliance_standards:
            body['compliance_standards'] = [v.value for v in self.compliance_standards]
        if self.is_enforced is not None: body['is_enforced'] = self.is_enforced
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> CspEnablementAccount:
        """Deserializes the CspEnablementAccount from a dictionary."""
        return cls(compliance_standards=_repeated_enum(d, 'compliance_standards', ComplianceStandard),
                   is_enforced=d.get('is_enforced', None))


@dataclass
class CspEnablementAccountSetting:
    csp_enablement_account: CspEnablementAccount
    """Account level policy for CSP"""

    etag: Optional[str] = None
    """etag used for versioning. The response is at least as fresh as the eTag provided. This is used
    for optimistic concurrency control as a way to help prevent simultaneous writes of a setting
    overwriting each other. It is strongly suggested that systems make use of the etag in the read
    -> update pattern to perform setting updates in order to avoid race conditions. That is, get an
    etag from a GET request, and pass it with the PATCH request to identify the setting version you
    are updating."""

    setting_name: Optional[str] = None
    """Name of the corresponding setting. This field is populated in the response, but it will not be
    respected even if it's set in the request body. The setting name in the path parameter will be
    respected instead. Setting name is required to be 'default' if the setting only has one instance
    per workspace."""

    def as_dict(self) -> dict:
        """Serializes the CspEnablementAccountSetting into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.csp_enablement_account: body['csp_enablement_account'] = self.csp_enablement_account.as_dict()
        if self.etag is not None: body['etag'] = self.etag
        if self.setting_name is not None: body['setting_name'] = self.setting_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> CspEnablementAccountSetting:
        """Deserializes the CspEnablementAccountSetting from a dictionary."""
        return cls(csp_enablement_account=_from_dict(d, 'csp_enablement_account', CspEnablementAccount),
                   etag=d.get('etag', None),
                   setting_name=d.get('setting_name', None))


@dataclass
class DefaultNamespaceSetting:
    """This represents the setting configuration for the default namespace in the Databricks workspace.
    Setting the default catalog for the workspace determines the catalog that is used when queries
    do not reference a fully qualified 3 level name. For example, if the default catalog is set to
    'retail_prod' then a query 'SELECT * FROM myTable' would reference the object
    'retail_prod.default.myTable' (the schema 'default' is always assumed). This setting requires a
    restart of clusters and SQL warehouses to take effect. Additionally, the default namespace only
    applies when using Unity Catalog-enabled compute."""

    namespace: StringMessage

    etag: Optional[str] = None
    """etag used for versioning. The response is at least as fresh as the eTag provided. This is used
    for optimistic concurrency control as a way to help prevent simultaneous writes of a setting
    overwriting each other. It is strongly suggested that systems make use of the etag in the read
    -> update pattern to perform setting updates in order to avoid race conditions. That is, get an
    etag from a GET request, and pass it with the PATCH request to identify the setting version you
    are updating."""

    setting_name: Optional[str] = None
    """Name of the corresponding setting. This field is populated in the response, but it will not be
    respected even if it's set in the request body. The setting name in the path parameter will be
    respected instead. Setting name is required to be 'default' if the setting only has one instance
    per workspace."""

    def as_dict(self) -> dict:
        """Serializes the DefaultNamespaceSetting into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.etag is not None: body['etag'] = self.etag
        if self.namespace: body['namespace'] = self.namespace.as_dict()
        if self.setting_name is not None: body['setting_name'] = self.setting_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> DefaultNamespaceSetting:
        """Deserializes the DefaultNamespaceSetting from a dictionary."""
        return cls(etag=d.get('etag', None),
                   namespace=_from_dict(d, 'namespace', StringMessage),
                   setting_name=d.get('setting_name', None))


@dataclass
class DeleteDefaultNamespaceSettingResponse:
    """The etag is returned."""

    etag: str
    """etag used for versioning. The response is at least as fresh as the eTag provided. This is used
    for optimistic concurrency control as a way to help prevent simultaneous writes of a setting
    overwriting each other. It is strongly suggested that systems make use of the etag in the read
    -> delete pattern to perform setting deletions in order to avoid race conditions. That is, get
    an etag from a GET request, and pass it with the DELETE request to identify the rule set version
    you are deleting."""

    def as_dict(self) -> dict:
        """Serializes the DeleteDefaultNamespaceSettingResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.etag is not None: body['etag'] = self.etag
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> DeleteDefaultNamespaceSettingResponse:
        """Deserializes the DeleteDefaultNamespaceSettingResponse from a dictionary."""
        return cls(etag=d.get('etag', None))


@dataclass
class DeleteDisableLegacyAccessResponse:
    """The etag is returned."""

    etag: str
    """etag used for versioning. The response is at least as fresh as the eTag provided. This is used
    for optimistic concurrency control as a way to help prevent simultaneous writes of a setting
    overwriting each other. It is strongly suggested that systems make use of the etag in the read
    -> delete pattern to perform setting deletions in order to avoid race conditions. That is, get
    an etag from a GET request, and pass it with the DELETE request to identify the rule set version
    you are deleting."""

    def as_dict(self) -> dict:
        """Serializes the DeleteDisableLegacyAccessResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.etag is not None: body['etag'] = self.etag
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> DeleteDisableLegacyAccessResponse:
        """Deserializes the DeleteDisableLegacyAccessResponse from a dictionary."""
        return cls(etag=d.get('etag', None))


@dataclass
class DeleteDisableLegacyDbfsResponse:
    """The etag is returned."""

    etag: str
    """etag used for versioning. The response is at least as fresh as the eTag provided. This is used
    for optimistic concurrency control as a way to help prevent simultaneous writes of a setting
    overwriting each other. It is strongly suggested that systems make use of the etag in the read
    -> delete pattern to perform setting deletions in order to avoid race conditions. That is, get
    an etag from a GET request, and pass it with the DELETE request to identify the rule set version
    you are deleting."""

    def as_dict(self) -> dict:
        """Serializes the DeleteDisableLegacyDbfsResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.etag is not None: body['etag'] = self.etag
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> DeleteDisableLegacyDbfsResponse:
        """Deserializes the DeleteDisableLegacyDbfsResponse from a dictionary."""
        return cls(etag=d.get('etag', None))


@dataclass
class DeleteDisableLegacyFeaturesResponse:
    """The etag is returned."""

    etag: str
    """etag used for versioning. The response is at least as fresh as the eTag provided. This is used
    for optimistic concurrency control as a way to help prevent simultaneous writes of a setting
    overwriting each other. It is strongly suggested that systems make use of the etag in the read
    -> delete pattern to perform setting deletions in order to avoid race conditions. That is, get
    an etag from a GET request, and pass it with the DELETE request to identify the rule set version
    you are deleting."""

    def as_dict(self) -> dict:
        """Serializes the DeleteDisableLegacyFeaturesResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.etag is not None: body['etag'] = self.etag
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> DeleteDisableLegacyFeaturesResponse:
        """Deserializes the DeleteDisableLegacyFeaturesResponse from a dictionary."""
        return cls(etag=d.get('etag', None))


@dataclass
class DeleteNetworkConnectivityConfigurationResponse:

    def as_dict(self) -> dict:
        """Serializes the DeleteNetworkConnectivityConfigurationResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> DeleteNetworkConnectivityConfigurationResponse:
        """Deserializes the DeleteNetworkConnectivityConfigurationResponse from a dictionary."""
        return cls()


@dataclass
class DeletePersonalComputeSettingResponse:
    """The etag is returned."""

    etag: str
    """etag used for versioning. The response is at least as fresh as the eTag provided. This is used
    for optimistic concurrency control as a way to help prevent simultaneous writes of a setting
    overwriting each other. It is strongly suggested that systems make use of the etag in the read
    -> delete pattern to perform setting deletions in order to avoid race conditions. That is, get
    an etag from a GET request, and pass it with the DELETE request to identify the rule set version
    you are deleting."""

    def as_dict(self) -> dict:
        """Serializes the DeletePersonalComputeSettingResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.etag is not None: body['etag'] = self.etag
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> DeletePersonalComputeSettingResponse:
        """Deserializes the DeletePersonalComputeSettingResponse from a dictionary."""
        return cls(etag=d.get('etag', None))


@dataclass
class DeleteResponse:

    def as_dict(self) -> dict:
        """Serializes the DeleteResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> DeleteResponse:
        """Deserializes the DeleteResponse from a dictionary."""
        return cls()


@dataclass
class DeleteRestrictWorkspaceAdminsSettingResponse:
    """The etag is returned."""

    etag: str
    """etag used for versioning. The response is at least as fresh as the eTag provided. This is used
    for optimistic concurrency control as a way to help prevent simultaneous writes of a setting
    overwriting each other. It is strongly suggested that systems make use of the etag in the read
    -> delete pattern to perform setting deletions in order to avoid race conditions. That is, get
    an etag from a GET request, and pass it with the DELETE request to identify the rule set version
    you are deleting."""

    def as_dict(self) -> dict:
        """Serializes the DeleteRestrictWorkspaceAdminsSettingResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.etag is not None: body['etag'] = self.etag
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> DeleteRestrictWorkspaceAdminsSettingResponse:
        """Deserializes the DeleteRestrictWorkspaceAdminsSettingResponse from a dictionary."""
        return cls(etag=d.get('etag', None))


class DestinationType(Enum):

    EMAIL = 'EMAIL'
    MICROSOFT_TEAMS = 'MICROSOFT_TEAMS'
    PAGERDUTY = 'PAGERDUTY'
    SLACK = 'SLACK'
    WEBHOOK = 'WEBHOOK'


@dataclass
class DisableLegacyAccess:
    disable_legacy_access: BooleanMessage

    etag: Optional[str] = None
    """etag used for versioning. The response is at least as fresh as the eTag provided. This is used
    for optimistic concurrency control as a way to help prevent simultaneous writes of a setting
    overwriting each other. It is strongly suggested that systems make use of the etag in the read
    -> update pattern to perform setting updates in order to avoid race conditions. That is, get an
    etag from a GET request, and pass it with the PATCH request to identify the setting version you
    are updating."""

    setting_name: Optional[str] = None
    """Name of the corresponding setting. This field is populated in the response, but it will not be
    respected even if it's set in the request body. The setting name in the path parameter will be
    respected instead. Setting name is required to be 'default' if the setting only has one instance
    per workspace."""

    def as_dict(self) -> dict:
        """Serializes the DisableLegacyAccess into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.disable_legacy_access: body['disable_legacy_access'] = self.disable_legacy_access.as_dict()
        if self.etag is not None: body['etag'] = self.etag
        if self.setting_name is not None: body['setting_name'] = self.setting_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> DisableLegacyAccess:
        """Deserializes the DisableLegacyAccess from a dictionary."""
        return cls(disable_legacy_access=_from_dict(d, 'disable_legacy_access', BooleanMessage),
                   etag=d.get('etag', None),
                   setting_name=d.get('setting_name', None))


@dataclass
class DisableLegacyDbfs:
    disable_legacy_dbfs: BooleanMessage

    etag: Optional[str] = None
    """etag used for versioning. The response is at least as fresh as the eTag provided. This is used
    for optimistic concurrency control as a way to help prevent simultaneous writes of a setting
    overwriting each other. It is strongly suggested that systems make use of the etag in the read
    -> update pattern to perform setting updates in order to avoid race conditions. That is, get an
    etag from a GET request, and pass it with the PATCH request to identify the setting version you
    are updating."""

    setting_name: Optional[str] = None
    """Name of the corresponding setting. This field is populated in the response, but it will not be
    respected even if it's set in the request body. The setting name in the path parameter will be
    respected instead. Setting name is required to be 'default' if the setting only has one instance
    per workspace."""

    def as_dict(self) -> dict:
        """Serializes the DisableLegacyDbfs into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.disable_legacy_dbfs: body['disable_legacy_dbfs'] = self.disable_legacy_dbfs.as_dict()
        if self.etag is not None: body['etag'] = self.etag
        if self.setting_name is not None: body['setting_name'] = self.setting_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> DisableLegacyDbfs:
        """Deserializes the DisableLegacyDbfs from a dictionary."""
        return cls(disable_legacy_dbfs=_from_dict(d, 'disable_legacy_dbfs', BooleanMessage),
                   etag=d.get('etag', None),
                   setting_name=d.get('setting_name', None))


@dataclass
class DisableLegacyFeatures:
    disable_legacy_features: BooleanMessage

    etag: Optional[str] = None
    """etag used for versioning. The response is at least as fresh as the eTag provided. This is used
    for optimistic concurrency control as a way to help prevent simultaneous writes of a setting
    overwriting each other. It is strongly suggested that systems make use of the etag in the read
    -> update pattern to perform setting updates in order to avoid race conditions. That is, get an
    etag from a GET request, and pass it with the PATCH request to identify the setting version you
    are updating."""

    setting_name: Optional[str] = None
    """Name of the corresponding setting. This field is populated in the response, but it will not be
    respected even if it's set in the request body. The setting name in the path parameter will be
    respected instead. Setting name is required to be 'default' if the setting only has one instance
    per workspace."""

    def as_dict(self) -> dict:
        """Serializes the DisableLegacyFeatures into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.disable_legacy_features:
            body['disable_legacy_features'] = self.disable_legacy_features.as_dict()
        if self.etag is not None: body['etag'] = self.etag
        if self.setting_name is not None: body['setting_name'] = self.setting_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> DisableLegacyFeatures:
        """Deserializes the DisableLegacyFeatures from a dictionary."""
        return cls(disable_legacy_features=_from_dict(d, 'disable_legacy_features', BooleanMessage),
                   etag=d.get('etag', None),
                   setting_name=d.get('setting_name', None))


@dataclass
class EmailConfig:
    addresses: Optional[List[str]] = None
    """Email addresses to notify."""

    def as_dict(self) -> dict:
        """Serializes the EmailConfig into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.addresses: body['addresses'] = [v for v in self.addresses]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> EmailConfig:
        """Deserializes the EmailConfig from a dictionary."""
        return cls(addresses=d.get('addresses', None))


@dataclass
class Empty:

    def as_dict(self) -> dict:
        """Serializes the Empty into a dictionary suitable for use as a JSON request body."""
        body = {}
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> Empty:
        """Deserializes the Empty from a dictionary."""
        return cls()


@dataclass
class EnhancedSecurityMonitoring:
    """SHIELD feature: ESM"""

    is_enabled: Optional[bool] = None

    def as_dict(self) -> dict:
        """Serializes the EnhancedSecurityMonitoring into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.is_enabled is not None: body['is_enabled'] = self.is_enabled
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> EnhancedSecurityMonitoring:
        """Deserializes the EnhancedSecurityMonitoring from a dictionary."""
        return cls(is_enabled=d.get('is_enabled', None))


@dataclass
class EnhancedSecurityMonitoringSetting:
    enhanced_security_monitoring_workspace: EnhancedSecurityMonitoring
    """SHIELD feature: ESM"""

    etag: Optional[str] = None
    """etag used for versioning. The response is at least as fresh as the eTag provided. This is used
    for optimistic concurrency control as a way to help prevent simultaneous writes of a setting
    overwriting each other. It is strongly suggested that systems make use of the etag in the read
    -> update pattern to perform setting updates in order to avoid race conditions. That is, get an
    etag from a GET request, and pass it with the PATCH request to identify the setting version you
    are updating."""

    setting_name: Optional[str] = None
    """Name of the corresponding setting. This field is populated in the response, but it will not be
    respected even if it's set in the request body. The setting name in the path parameter will be
    respected instead. Setting name is required to be 'default' if the setting only has one instance
    per workspace."""

    def as_dict(self) -> dict:
        """Serializes the EnhancedSecurityMonitoringSetting into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.enhanced_security_monitoring_workspace:
            body[
                'enhanced_security_monitoring_workspace'] = self.enhanced_security_monitoring_workspace.as_dict(
                )
        if self.etag is not None: body['etag'] = self.etag
        if self.setting_name is not None: body['setting_name'] = self.setting_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> EnhancedSecurityMonitoringSetting:
        """Deserializes the EnhancedSecurityMonitoringSetting from a dictionary."""
        return cls(enhanced_security_monitoring_workspace=_from_dict(
            d, 'enhanced_security_monitoring_workspace', EnhancedSecurityMonitoring),
                   etag=d.get('etag', None),
                   setting_name=d.get('setting_name', None))


@dataclass
class EsmEnablementAccount:
    """Account level policy for ESM"""

    is_enforced: Optional[bool] = None

    def as_dict(self) -> dict:
        """Serializes the EsmEnablementAccount into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.is_enforced is not None: body['is_enforced'] = self.is_enforced
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> EsmEnablementAccount:
        """Deserializes the EsmEnablementAccount from a dictionary."""
        return cls(is_enforced=d.get('is_enforced', None))


@dataclass
class EsmEnablementAccountSetting:
    esm_enablement_account: EsmEnablementAccount
    """Account level policy for ESM"""

    etag: Optional[str] = None
    """etag used for versioning. The response is at least as fresh as the eTag provided. This is used
    for optimistic concurrency control as a way to help prevent simultaneous writes of a setting
    overwriting each other. It is strongly suggested that systems make use of the etag in the read
    -> update pattern to perform setting updates in order to avoid race conditions. That is, get an
    etag from a GET request, and pass it with the PATCH request to identify the setting version you
    are updating."""

    setting_name: Optional[str] = None
    """Name of the corresponding setting. This field is populated in the response, but it will not be
    respected even if it's set in the request body. The setting name in the path parameter will be
    respected instead. Setting name is required to be 'default' if the setting only has one instance
    per workspace."""

    def as_dict(self) -> dict:
        """Serializes the EsmEnablementAccountSetting into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.esm_enablement_account: body['esm_enablement_account'] = self.esm_enablement_account.as_dict()
        if self.etag is not None: body['etag'] = self.etag
        if self.setting_name is not None: body['setting_name'] = self.setting_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> EsmEnablementAccountSetting:
        """Deserializes the EsmEnablementAccountSetting from a dictionary."""
        return cls(esm_enablement_account=_from_dict(d, 'esm_enablement_account', EsmEnablementAccount),
                   etag=d.get('etag', None),
                   setting_name=d.get('setting_name', None))


@dataclass
class ExchangeToken:
    """The exchange token is the result of the token exchange with the IdP"""

    credential: Optional[str] = None
    """The requested token."""

    credential_eol_time: Optional[int] = None
    """The end-of-life timestamp of the token. The value is in milliseconds since the Unix epoch."""

    owner_id: Optional[int] = None
    """User ID of the user that owns this token."""

    scopes: Optional[List[str]] = None
    """The scopes of access granted in the token."""

    token_type: Optional[TokenType] = None
    """The type of this exchange token"""

    def as_dict(self) -> dict:
        """Serializes the ExchangeToken into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.credential is not None: body['credential'] = self.credential
        if self.credential_eol_time is not None: body['credentialEolTime'] = self.credential_eol_time
        if self.owner_id is not None: body['ownerId'] = self.owner_id
        if self.scopes: body['scopes'] = [v for v in self.scopes]
        if self.token_type is not None: body['tokenType'] = self.token_type.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ExchangeToken:
        """Deserializes the ExchangeToken from a dictionary."""
        return cls(credential=d.get('credential', None),
                   credential_eol_time=d.get('credentialEolTime', None),
                   owner_id=d.get('ownerId', None),
                   scopes=d.get('scopes', None),
                   token_type=_enum(d, 'tokenType', TokenType))


@dataclass
class ExchangeTokenRequest:
    """Exchange a token with the IdP"""

    partition_id: PartitionId
    """The partition of Credentials store"""

    token_type: List[TokenType]
    """A list of token types being requested"""

    scopes: List[str]
    """Array of scopes for the token request."""

    def as_dict(self) -> dict:
        """Serializes the ExchangeTokenRequest into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.partition_id: body['partitionId'] = self.partition_id.as_dict()
        if self.scopes: body['scopes'] = [v for v in self.scopes]
        if self.token_type: body['tokenType'] = [v.value for v in self.token_type]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ExchangeTokenRequest:
        """Deserializes the ExchangeTokenRequest from a dictionary."""
        return cls(partition_id=_from_dict(d, 'partitionId', PartitionId),
                   scopes=d.get('scopes', None),
                   token_type=_repeated_enum(d, 'tokenType', TokenType))


@dataclass
class ExchangeTokenResponse:
    """Exhanged tokens were successfully returned."""

    values: Optional[List[ExchangeToken]] = None

    def as_dict(self) -> dict:
        """Serializes the ExchangeTokenResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.values: body['values'] = [v.as_dict() for v in self.values]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ExchangeTokenResponse:
        """Deserializes the ExchangeTokenResponse from a dictionary."""
        return cls(values=_repeated_dict(d, 'values', ExchangeToken))


@dataclass
class FetchIpAccessListResponse:
    """An IP access list was successfully returned."""

    ip_access_list: Optional[IpAccessListInfo] = None
    """Definition of an IP Access list"""

    def as_dict(self) -> dict:
        """Serializes the FetchIpAccessListResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.ip_access_list: body['ip_access_list'] = self.ip_access_list.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> FetchIpAccessListResponse:
        """Deserializes the FetchIpAccessListResponse from a dictionary."""
        return cls(ip_access_list=_from_dict(d, 'ip_access_list', IpAccessListInfo))


@dataclass
class GenericWebhookConfig:
    password: Optional[str] = None
    """[Input-Only][Optional] Password for webhook."""

    password_set: Optional[bool] = None
    """[Output-Only] Whether password is set."""

    url: Optional[str] = None
    """[Input-Only] URL for webhook."""

    url_set: Optional[bool] = None
    """[Output-Only] Whether URL is set."""

    username: Optional[str] = None
    """[Input-Only][Optional] Username for webhook."""

    username_set: Optional[bool] = None
    """[Output-Only] Whether username is set."""

    def as_dict(self) -> dict:
        """Serializes the GenericWebhookConfig into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.password is not None: body['password'] = self.password
        if self.password_set is not None: body['password_set'] = self.password_set
        if self.url is not None: body['url'] = self.url
        if self.url_set is not None: body['url_set'] = self.url_set
        if self.username is not None: body['username'] = self.username
        if self.username_set is not None: body['username_set'] = self.username_set
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> GenericWebhookConfig:
        """Deserializes the GenericWebhookConfig from a dictionary."""
        return cls(password=d.get('password', None),
                   password_set=d.get('password_set', None),
                   url=d.get('url', None),
                   url_set=d.get('url_set', None),
                   username=d.get('username', None),
                   username_set=d.get('username_set', None))


@dataclass
class GetIpAccessListResponse:
    ip_access_list: Optional[IpAccessListInfo] = None
    """Definition of an IP Access list"""

    def as_dict(self) -> dict:
        """Serializes the GetIpAccessListResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.ip_access_list: body['ip_access_list'] = self.ip_access_list.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> GetIpAccessListResponse:
        """Deserializes the GetIpAccessListResponse from a dictionary."""
        return cls(ip_access_list=_from_dict(d, 'ip_access_list', IpAccessListInfo))


@dataclass
class GetIpAccessListsResponse:
    """IP access lists were successfully returned."""

    ip_access_lists: Optional[List[IpAccessListInfo]] = None

    def as_dict(self) -> dict:
        """Serializes the GetIpAccessListsResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.ip_access_lists: body['ip_access_lists'] = [v.as_dict() for v in self.ip_access_lists]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> GetIpAccessListsResponse:
        """Deserializes the GetIpAccessListsResponse from a dictionary."""
        return cls(ip_access_lists=_repeated_dict(d, 'ip_access_lists', IpAccessListInfo))


@dataclass
class GetTokenPermissionLevelsResponse:
    permission_levels: Optional[List[TokenPermissionsDescription]] = None
    """Specific permission levels"""

    def as_dict(self) -> dict:
        """Serializes the GetTokenPermissionLevelsResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.permission_levels: body['permission_levels'] = [v.as_dict() for v in self.permission_levels]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> GetTokenPermissionLevelsResponse:
        """Deserializes the GetTokenPermissionLevelsResponse from a dictionary."""
        return cls(permission_levels=_repeated_dict(d, 'permission_levels', TokenPermissionsDescription))


@dataclass
class GetTokenResponse:
    """Token with specified Token ID was successfully returned."""

    token_info: Optional[TokenInfo] = None

    def as_dict(self) -> dict:
        """Serializes the GetTokenResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.token_info: body['token_info'] = self.token_info.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> GetTokenResponse:
        """Deserializes the GetTokenResponse from a dictionary."""
        return cls(token_info=_from_dict(d, 'token_info', TokenInfo))


@dataclass
class IpAccessListInfo:
    """Definition of an IP Access list"""

    address_count: Optional[int] = None
    """Total number of IP or CIDR values."""

    created_at: Optional[int] = None
    """Creation timestamp in milliseconds."""

    created_by: Optional[int] = None
    """User ID of the user who created this list."""

    enabled: Optional[bool] = None
    """Specifies whether this IP access list is enabled."""

    ip_addresses: Optional[List[str]] = None

    label: Optional[str] = None
    """Label for the IP access list. This **cannot** be empty."""

    list_id: Optional[str] = None
    """Universally unique identifier (UUID) of the IP access list."""

    list_type: Optional[ListType] = None
    """Type of IP access list. Valid values are as follows and are case-sensitive:
    
    * `ALLOW`: An allow list. Include this IP or range. * `BLOCK`: A block list. Exclude this IP or
    range. IP addresses in the block list are excluded even if they are included in an allow list."""

    updated_at: Optional[int] = None
    """Update timestamp in milliseconds."""

    updated_by: Optional[int] = None
    """User ID of the user who updated this list."""

    def as_dict(self) -> dict:
        """Serializes the IpAccessListInfo into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.address_count is not None: body['address_count'] = self.address_count
        if self.created_at is not None: body['created_at'] = self.created_at
        if self.created_by is not None: body['created_by'] = self.created_by
        if self.enabled is not None: body['enabled'] = self.enabled
        if self.ip_addresses: body['ip_addresses'] = [v for v in self.ip_addresses]
        if self.label is not None: body['label'] = self.label
        if self.list_id is not None: body['list_id'] = self.list_id
        if self.list_type is not None: body['list_type'] = self.list_type.value
        if self.updated_at is not None: body['updated_at'] = self.updated_at
        if self.updated_by is not None: body['updated_by'] = self.updated_by
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> IpAccessListInfo:
        """Deserializes the IpAccessListInfo from a dictionary."""
        return cls(address_count=d.get('address_count', None),
                   created_at=d.get('created_at', None),
                   created_by=d.get('created_by', None),
                   enabled=d.get('enabled', None),
                   ip_addresses=d.get('ip_addresses', None),
                   label=d.get('label', None),
                   list_id=d.get('list_id', None),
                   list_type=_enum(d, 'list_type', ListType),
                   updated_at=d.get('updated_at', None),
                   updated_by=d.get('updated_by', None))


@dataclass
class ListIpAccessListResponse:
    """IP access lists were successfully returned."""

    ip_access_lists: Optional[List[IpAccessListInfo]] = None

    def as_dict(self) -> dict:
        """Serializes the ListIpAccessListResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.ip_access_lists: body['ip_access_lists'] = [v.as_dict() for v in self.ip_access_lists]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ListIpAccessListResponse:
        """Deserializes the ListIpAccessListResponse from a dictionary."""
        return cls(ip_access_lists=_repeated_dict(d, 'ip_access_lists', IpAccessListInfo))


@dataclass
class ListNccAzurePrivateEndpointRulesResponse:
    items: Optional[List[NccAzurePrivateEndpointRule]] = None

    next_page_token: Optional[str] = None
    """A token that can be used to get the next page of results. If null, there are no more results to
    show."""

    def as_dict(self) -> dict:
        """Serializes the ListNccAzurePrivateEndpointRulesResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.items: body['items'] = [v.as_dict() for v in self.items]
        if self.next_page_token is not None: body['next_page_token'] = self.next_page_token
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ListNccAzurePrivateEndpointRulesResponse:
        """Deserializes the ListNccAzurePrivateEndpointRulesResponse from a dictionary."""
        return cls(items=_repeated_dict(d, 'items', NccAzurePrivateEndpointRule),
                   next_page_token=d.get('next_page_token', None))


@dataclass
class ListNetworkConnectivityConfigurationsResponse:
    items: Optional[List[NetworkConnectivityConfiguration]] = None

    next_page_token: Optional[str] = None
    """A token that can be used to get the next page of results. If null, there are no more results to
    show."""

    def as_dict(self) -> dict:
        """Serializes the ListNetworkConnectivityConfigurationsResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.items: body['items'] = [v.as_dict() for v in self.items]
        if self.next_page_token is not None: body['next_page_token'] = self.next_page_token
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ListNetworkConnectivityConfigurationsResponse:
        """Deserializes the ListNetworkConnectivityConfigurationsResponse from a dictionary."""
        return cls(items=_repeated_dict(d, 'items', NetworkConnectivityConfiguration),
                   next_page_token=d.get('next_page_token', None))


@dataclass
class ListNotificationDestinationsResponse:
    next_page_token: Optional[str] = None
    """Page token for next of results."""

    results: Optional[List[ListNotificationDestinationsResult]] = None

    def as_dict(self) -> dict:
        """Serializes the ListNotificationDestinationsResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.next_page_token is not None: body['next_page_token'] = self.next_page_token
        if self.results: body['results'] = [v.as_dict() for v in self.results]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ListNotificationDestinationsResponse:
        """Deserializes the ListNotificationDestinationsResponse from a dictionary."""
        return cls(next_page_token=d.get('next_page_token', None),
                   results=_repeated_dict(d, 'results', ListNotificationDestinationsResult))


@dataclass
class ListNotificationDestinationsResult:
    destination_type: Optional[DestinationType] = None
    """[Output-only] The type of the notification destination. The type can not be changed once set."""

    display_name: Optional[str] = None
    """The display name for the notification destination."""

    id: Optional[str] = None
    """UUID identifying notification destination."""

    def as_dict(self) -> dict:
        """Serializes the ListNotificationDestinationsResult into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.destination_type is not None: body['destination_type'] = self.destination_type.value
        if self.display_name is not None: body['display_name'] = self.display_name
        if self.id is not None: body['id'] = self.id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ListNotificationDestinationsResult:
        """Deserializes the ListNotificationDestinationsResult from a dictionary."""
        return cls(destination_type=_enum(d, 'destination_type', DestinationType),
                   display_name=d.get('display_name', None),
                   id=d.get('id', None))


@dataclass
class ListPublicTokensResponse:
    token_infos: Optional[List[PublicTokenInfo]] = None
    """The information for each token."""

    def as_dict(self) -> dict:
        """Serializes the ListPublicTokensResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.token_infos: body['token_infos'] = [v.as_dict() for v in self.token_infos]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ListPublicTokensResponse:
        """Deserializes the ListPublicTokensResponse from a dictionary."""
        return cls(token_infos=_repeated_dict(d, 'token_infos', PublicTokenInfo))


@dataclass
class ListTokensResponse:
    """Tokens were successfully returned."""

    token_infos: Optional[List[TokenInfo]] = None
    """Token metadata of each user-created token in the workspace"""

    def as_dict(self) -> dict:
        """Serializes the ListTokensResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.token_infos: body['token_infos'] = [v.as_dict() for v in self.token_infos]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ListTokensResponse:
        """Deserializes the ListTokensResponse from a dictionary."""
        return cls(token_infos=_repeated_dict(d, 'token_infos', TokenInfo))


class ListType(Enum):
    """Type of IP access list. Valid values are as follows and are case-sensitive:
    
    * `ALLOW`: An allow list. Include this IP or range. * `BLOCK`: A block list. Exclude this IP or
    range. IP addresses in the block list are excluded even if they are included in an allow list."""

    ALLOW = 'ALLOW'
    BLOCK = 'BLOCK'


@dataclass
class MicrosoftTeamsConfig:
    url: Optional[str] = None
    """[Input-Only] URL for Microsoft Teams."""

    url_set: Optional[bool] = None
    """[Output-Only] Whether URL is set."""

    def as_dict(self) -> dict:
        """Serializes the MicrosoftTeamsConfig into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.url is not None: body['url'] = self.url
        if self.url_set is not None: body['url_set'] = self.url_set
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> MicrosoftTeamsConfig:
        """Deserializes the MicrosoftTeamsConfig from a dictionary."""
        return cls(url=d.get('url', None), url_set=d.get('url_set', None))


@dataclass
class NccAwsStableIpRule:
    """The stable AWS IP CIDR blocks. You can use these to configure the firewall of your resources to
    allow traffic from your Databricks workspace."""

    cidr_blocks: Optional[List[str]] = None
    """The list of stable IP CIDR blocks from which Databricks network traffic originates when
    accessing your resources."""

    def as_dict(self) -> dict:
        """Serializes the NccAwsStableIpRule into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.cidr_blocks: body['cidr_blocks'] = [v for v in self.cidr_blocks]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> NccAwsStableIpRule:
        """Deserializes the NccAwsStableIpRule from a dictionary."""
        return cls(cidr_blocks=d.get('cidr_blocks', None))


@dataclass
class NccAzurePrivateEndpointRule:
    connection_state: Optional[NccAzurePrivateEndpointRuleConnectionState] = None
    """The current status of this private endpoint. The private endpoint rules are effective only if
    the connection state is `ESTABLISHED`. Remember that you must approve new endpoints on your
    resources in the Azure portal before they take effect.
    
    The possible values are: - INIT: (deprecated) The endpoint has been created and pending
    approval. - PENDING: The endpoint has been created and pending approval. - ESTABLISHED: The
    endpoint has been approved and is ready to use in your serverless compute resources. - REJECTED:
    Connection was rejected by the private link resource owner. - DISCONNECTED: Connection was
    removed by the private link resource owner, the private endpoint becomes informative and should
    be deleted for clean-up."""

    creation_time: Optional[int] = None
    """Time in epoch milliseconds when this object was created."""

    deactivated: Optional[bool] = None
    """Whether this private endpoint is deactivated."""

    deactivated_at: Optional[int] = None
    """Time in epoch milliseconds when this object was deactivated."""

    endpoint_name: Optional[str] = None
    """The name of the Azure private endpoint resource."""

    group_id: Optional[NccAzurePrivateEndpointRuleGroupId] = None
    """The sub-resource type (group ID) of the target resource. Note that to connect to workspace root
    storage (root DBFS), you need two endpoints, one for `blob` and one for `dfs`."""

    network_connectivity_config_id: Optional[str] = None
    """The ID of a network connectivity configuration, which is the parent resource of this private
    endpoint rule object."""

    resource_id: Optional[str] = None
    """The Azure resource ID of the target resource."""

    rule_id: Optional[str] = None
    """The ID of a private endpoint rule."""

    updated_time: Optional[int] = None
    """Time in epoch milliseconds when this object was updated."""

    def as_dict(self) -> dict:
        """Serializes the NccAzurePrivateEndpointRule into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.connection_state is not None: body['connection_state'] = self.connection_state.value
        if self.creation_time is not None: body['creation_time'] = self.creation_time
        if self.deactivated is not None: body['deactivated'] = self.deactivated
        if self.deactivated_at is not None: body['deactivated_at'] = self.deactivated_at
        if self.endpoint_name is not None: body['endpoint_name'] = self.endpoint_name
        if self.group_id is not None: body['group_id'] = self.group_id.value
        if self.network_connectivity_config_id is not None:
            body['network_connectivity_config_id'] = self.network_connectivity_config_id
        if self.resource_id is not None: body['resource_id'] = self.resource_id
        if self.rule_id is not None: body['rule_id'] = self.rule_id
        if self.updated_time is not None: body['updated_time'] = self.updated_time
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> NccAzurePrivateEndpointRule:
        """Deserializes the NccAzurePrivateEndpointRule from a dictionary."""
        return cls(connection_state=_enum(d, 'connection_state', NccAzurePrivateEndpointRuleConnectionState),
                   creation_time=d.get('creation_time', None),
                   deactivated=d.get('deactivated', None),
                   deactivated_at=d.get('deactivated_at', None),
                   endpoint_name=d.get('endpoint_name', None),
                   group_id=_enum(d, 'group_id', NccAzurePrivateEndpointRuleGroupId),
                   network_connectivity_config_id=d.get('network_connectivity_config_id', None),
                   resource_id=d.get('resource_id', None),
                   rule_id=d.get('rule_id', None),
                   updated_time=d.get('updated_time', None))


class NccAzurePrivateEndpointRuleConnectionState(Enum):
    """The current status of this private endpoint. The private endpoint rules are effective only if
    the connection state is `ESTABLISHED`. Remember that you must approve new endpoints on your
    resources in the Azure portal before they take effect.
    
    The possible values are: - INIT: (deprecated) The endpoint has been created and pending
    approval. - PENDING: The endpoint has been created and pending approval. - ESTABLISHED: The
    endpoint has been approved and is ready to use in your serverless compute resources. - REJECTED:
    Connection was rejected by the private link resource owner. - DISCONNECTED: Connection was
    removed by the private link resource owner, the private endpoint becomes informative and should
    be deleted for clean-up."""

    DISCONNECTED = 'DISCONNECTED'
    ESTABLISHED = 'ESTABLISHED'
    INIT = 'INIT'
    PENDING = 'PENDING'
    REJECTED = 'REJECTED'


class NccAzurePrivateEndpointRuleGroupId(Enum):
    """The sub-resource type (group ID) of the target resource. Note that to connect to workspace root
    storage (root DBFS), you need two endpoints, one for `blob` and one for `dfs`."""

    BLOB = 'blob'
    DFS = 'dfs'
    MYSQL_SERVER = 'mysqlServer'
    SQL_SERVER = 'sqlServer'


@dataclass
class NccAzureServiceEndpointRule:
    """The stable Azure service endpoints. You can configure the firewall of your Azure resources to
    allow traffic from your Databricks serverless compute resources."""

    subnets: Optional[List[str]] = None
    """The list of subnets from which Databricks network traffic originates when accessing your Azure
    resources."""

    target_region: Optional[str] = None
    """The Azure region in which this service endpoint rule applies."""

    target_services: Optional[List[str]] = None
    """The Azure services to which this service endpoint rule applies to."""

    def as_dict(self) -> dict:
        """Serializes the NccAzureServiceEndpointRule into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.subnets: body['subnets'] = [v for v in self.subnets]
        if self.target_region is not None: body['target_region'] = self.target_region
        if self.target_services: body['target_services'] = [v for v in self.target_services]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> NccAzureServiceEndpointRule:
        """Deserializes the NccAzureServiceEndpointRule from a dictionary."""
        return cls(subnets=d.get('subnets', None),
                   target_region=d.get('target_region', None),
                   target_services=d.get('target_services', None))


@dataclass
class NccEgressConfig:
    """The network connectivity rules that apply to network traffic from your serverless compute
    resources."""

    default_rules: Optional[NccEgressDefaultRules] = None
    """The network connectivity rules that are applied by default without resource specific
    configurations. You can find the stable network information of your serverless compute resources
    here."""

    target_rules: Optional[NccEgressTargetRules] = None
    """The network connectivity rules that configured for each destinations. These rules override
    default rules."""

    def as_dict(self) -> dict:
        """Serializes the NccEgressConfig into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.default_rules: body['default_rules'] = self.default_rules.as_dict()
        if self.target_rules: body['target_rules'] = self.target_rules.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> NccEgressConfig:
        """Deserializes the NccEgressConfig from a dictionary."""
        return cls(default_rules=_from_dict(d, 'default_rules', NccEgressDefaultRules),
                   target_rules=_from_dict(d, 'target_rules', NccEgressTargetRules))


@dataclass
class NccEgressDefaultRules:
    """The network connectivity rules that are applied by default without resource specific
    configurations. You can find the stable network information of your serverless compute resources
    here."""

    aws_stable_ip_rule: Optional[NccAwsStableIpRule] = None
    """The stable AWS IP CIDR blocks. You can use these to configure the firewall of your resources to
    allow traffic from your Databricks workspace."""

    azure_service_endpoint_rule: Optional[NccAzureServiceEndpointRule] = None
    """The stable Azure service endpoints. You can configure the firewall of your Azure resources to
    allow traffic from your Databricks serverless compute resources."""

    def as_dict(self) -> dict:
        """Serializes the NccEgressDefaultRules into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.aws_stable_ip_rule: body['aws_stable_ip_rule'] = self.aws_stable_ip_rule.as_dict()
        if self.azure_service_endpoint_rule:
            body['azure_service_endpoint_rule'] = self.azure_service_endpoint_rule.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> NccEgressDefaultRules:
        """Deserializes the NccEgressDefaultRules from a dictionary."""
        return cls(aws_stable_ip_rule=_from_dict(d, 'aws_stable_ip_rule', NccAwsStableIpRule),
                   azure_service_endpoint_rule=_from_dict(d, 'azure_service_endpoint_rule',
                                                          NccAzureServiceEndpointRule))


@dataclass
class NccEgressTargetRules:
    """The network connectivity rules that configured for each destinations. These rules override
    default rules."""

    azure_private_endpoint_rules: Optional[List[NccAzurePrivateEndpointRule]] = None

    def as_dict(self) -> dict:
        """Serializes the NccEgressTargetRules into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.azure_private_endpoint_rules:
            body['azure_private_endpoint_rules'] = [v.as_dict() for v in self.azure_private_endpoint_rules]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> NccEgressTargetRules:
        """Deserializes the NccEgressTargetRules from a dictionary."""
        return cls(azure_private_endpoint_rules=_repeated_dict(d, 'azure_private_endpoint_rules',
                                                               NccAzurePrivateEndpointRule))


@dataclass
class NetworkConnectivityConfiguration:
    account_id: Optional[str] = None
    """The Databricks account ID that hosts the credential."""

    creation_time: Optional[int] = None
    """Time in epoch milliseconds when this object was created."""

    egress_config: Optional[NccEgressConfig] = None
    """The network connectivity rules that apply to network traffic from your serverless compute
    resources."""

    name: Optional[str] = None
    """The name of the network connectivity configuration. The name can contain alphanumeric
    characters, hyphens, and underscores. The length must be between 3 and 30 characters. The name
    must match the regular expression `^[0-9a-zA-Z-_]{3,30}$`."""

    network_connectivity_config_id: Optional[str] = None
    """Databricks network connectivity configuration ID."""

    region: Optional[str] = None
    """The region for the network connectivity configuration. Only workspaces in the same region can be
    attached to the network connectivity configuration."""

    updated_time: Optional[int] = None
    """Time in epoch milliseconds when this object was updated."""

    def as_dict(self) -> dict:
        """Serializes the NetworkConnectivityConfiguration into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.account_id is not None: body['account_id'] = self.account_id
        if self.creation_time is not None: body['creation_time'] = self.creation_time
        if self.egress_config: body['egress_config'] = self.egress_config.as_dict()
        if self.name is not None: body['name'] = self.name
        if self.network_connectivity_config_id is not None:
            body['network_connectivity_config_id'] = self.network_connectivity_config_id
        if self.region is not None: body['region'] = self.region
        if self.updated_time is not None: body['updated_time'] = self.updated_time
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> NetworkConnectivityConfiguration:
        """Deserializes the NetworkConnectivityConfiguration from a dictionary."""
        return cls(account_id=d.get('account_id', None),
                   creation_time=d.get('creation_time', None),
                   egress_config=_from_dict(d, 'egress_config', NccEgressConfig),
                   name=d.get('name', None),
                   network_connectivity_config_id=d.get('network_connectivity_config_id', None),
                   region=d.get('region', None),
                   updated_time=d.get('updated_time', None))


@dataclass
class NotificationDestination:
    config: Optional[Config] = None
    """The configuration for the notification destination. Will be exactly one of the nested configs.
    Only returns for users with workspace admin permissions."""

    destination_type: Optional[DestinationType] = None
    """[Output-only] The type of the notification destination. The type can not be changed once set."""

    display_name: Optional[str] = None
    """The display name for the notification destination."""

    id: Optional[str] = None
    """UUID identifying notification destination."""

    def as_dict(self) -> dict:
        """Serializes the NotificationDestination into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.config: body['config'] = self.config.as_dict()
        if self.destination_type is not None: body['destination_type'] = self.destination_type.value
        if self.display_name is not None: body['display_name'] = self.display_name
        if self.id is not None: body['id'] = self.id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> NotificationDestination:
        """Deserializes the NotificationDestination from a dictionary."""
        return cls(config=_from_dict(d, 'config', Config),
                   destination_type=_enum(d, 'destination_type', DestinationType),
                   display_name=d.get('display_name', None),
                   id=d.get('id', None))


@dataclass
class PagerdutyConfig:
    integration_key: Optional[str] = None
    """[Input-Only] Integration key for PagerDuty."""

    integration_key_set: Optional[bool] = None
    """[Output-Only] Whether integration key is set."""

    def as_dict(self) -> dict:
        """Serializes the PagerdutyConfig into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.integration_key is not None: body['integration_key'] = self.integration_key
        if self.integration_key_set is not None: body['integration_key_set'] = self.integration_key_set
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> PagerdutyConfig:
        """Deserializes the PagerdutyConfig from a dictionary."""
        return cls(integration_key=d.get('integration_key', None),
                   integration_key_set=d.get('integration_key_set', None))


@dataclass
class PartitionId:
    """Partition by workspace or account"""

    workspace_id: Optional[int] = None
    """The ID of the workspace."""

    def as_dict(self) -> dict:
        """Serializes the PartitionId into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.workspace_id is not None: body['workspaceId'] = self.workspace_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> PartitionId:
        """Deserializes the PartitionId from a dictionary."""
        return cls(workspace_id=d.get('workspaceId', None))


@dataclass
class PersonalComputeMessage:
    value: PersonalComputeMessageEnum
    """ON: Grants all users in all workspaces access to the Personal Compute default policy, allowing
    all users to create single-machine compute resources. DELEGATE: Moves access control for the
    Personal Compute default policy to individual workspaces and requires a workspace’s users or
    groups to be added to the ACLs of that workspace’s Personal Compute default policy before they
    will be able to create compute resources through that policy."""

    def as_dict(self) -> dict:
        """Serializes the PersonalComputeMessage into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.value is not None: body['value'] = self.value.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> PersonalComputeMessage:
        """Deserializes the PersonalComputeMessage from a dictionary."""
        return cls(value=_enum(d, 'value', PersonalComputeMessageEnum))


class PersonalComputeMessageEnum(Enum):
    """ON: Grants all users in all workspaces access to the Personal Compute default policy, allowing
    all users to create single-machine compute resources. DELEGATE: Moves access control for the
    Personal Compute default policy to individual workspaces and requires a workspace’s users or
    groups to be added to the ACLs of that workspace’s Personal Compute default policy before they
    will be able to create compute resources through that policy."""

    DELEGATE = 'DELEGATE'
    ON = 'ON'


@dataclass
class PersonalComputeSetting:
    personal_compute: PersonalComputeMessage

    etag: Optional[str] = None
    """etag used for versioning. The response is at least as fresh as the eTag provided. This is used
    for optimistic concurrency control as a way to help prevent simultaneous writes of a setting
    overwriting each other. It is strongly suggested that systems make use of the etag in the read
    -> update pattern to perform setting updates in order to avoid race conditions. That is, get an
    etag from a GET request, and pass it with the PATCH request to identify the setting version you
    are updating."""

    setting_name: Optional[str] = None
    """Name of the corresponding setting. This field is populated in the response, but it will not be
    respected even if it's set in the request body. The setting name in the path parameter will be
    respected instead. Setting name is required to be 'default' if the setting only has one instance
    per workspace."""

    def as_dict(self) -> dict:
        """Serializes the PersonalComputeSetting into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.etag is not None: body['etag'] = self.etag
        if self.personal_compute: body['personal_compute'] = self.personal_compute.as_dict()
        if self.setting_name is not None: body['setting_name'] = self.setting_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> PersonalComputeSetting:
        """Deserializes the PersonalComputeSetting from a dictionary."""
        return cls(etag=d.get('etag', None),
                   personal_compute=_from_dict(d, 'personal_compute', PersonalComputeMessage),
                   setting_name=d.get('setting_name', None))


@dataclass
class PublicTokenInfo:
    comment: Optional[str] = None
    """Comment the token was created with, if applicable."""

    creation_time: Optional[int] = None
    """Server time (in epoch milliseconds) when the token was created."""

    expiry_time: Optional[int] = None
    """Server time (in epoch milliseconds) when the token will expire, or -1 if not applicable."""

    token_id: Optional[str] = None
    """The ID of this token."""

    def as_dict(self) -> dict:
        """Serializes the PublicTokenInfo into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.comment is not None: body['comment'] = self.comment
        if self.creation_time is not None: body['creation_time'] = self.creation_time
        if self.expiry_time is not None: body['expiry_time'] = self.expiry_time
        if self.token_id is not None: body['token_id'] = self.token_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> PublicTokenInfo:
        """Deserializes the PublicTokenInfo from a dictionary."""
        return cls(comment=d.get('comment', None),
                   creation_time=d.get('creation_time', None),
                   expiry_time=d.get('expiry_time', None),
                   token_id=d.get('token_id', None))


@dataclass
class ReplaceIpAccessList:
    """Details required to replace an IP access list."""

    label: str
    """Label for the IP access list. This **cannot** be empty."""

    list_type: ListType
    """Type of IP access list. Valid values are as follows and are case-sensitive:
    
    * `ALLOW`: An allow list. Include this IP or range. * `BLOCK`: A block list. Exclude this IP or
    range. IP addresses in the block list are excluded even if they are included in an allow list."""

    enabled: bool
    """Specifies whether this IP access list is enabled."""

    ip_access_list_id: Optional[str] = None
    """The ID for the corresponding IP access list"""

    ip_addresses: Optional[List[str]] = None

    def as_dict(self) -> dict:
        """Serializes the ReplaceIpAccessList into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.enabled is not None: body['enabled'] = self.enabled
        if self.ip_access_list_id is not None: body['ip_access_list_id'] = self.ip_access_list_id
        if self.ip_addresses: body['ip_addresses'] = [v for v in self.ip_addresses]
        if self.label is not None: body['label'] = self.label
        if self.list_type is not None: body['list_type'] = self.list_type.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ReplaceIpAccessList:
        """Deserializes the ReplaceIpAccessList from a dictionary."""
        return cls(enabled=d.get('enabled', None),
                   ip_access_list_id=d.get('ip_access_list_id', None),
                   ip_addresses=d.get('ip_addresses', None),
                   label=d.get('label', None),
                   list_type=_enum(d, 'list_type', ListType))


@dataclass
class ReplaceResponse:

    def as_dict(self) -> dict:
        """Serializes the ReplaceResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ReplaceResponse:
        """Deserializes the ReplaceResponse from a dictionary."""
        return cls()


@dataclass
class RestrictWorkspaceAdminsMessage:
    status: RestrictWorkspaceAdminsMessageStatus

    def as_dict(self) -> dict:
        """Serializes the RestrictWorkspaceAdminsMessage into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.status is not None: body['status'] = self.status.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> RestrictWorkspaceAdminsMessage:
        """Deserializes the RestrictWorkspaceAdminsMessage from a dictionary."""
        return cls(status=_enum(d, 'status', RestrictWorkspaceAdminsMessageStatus))


class RestrictWorkspaceAdminsMessageStatus(Enum):

    ALLOW_ALL = 'ALLOW_ALL'
    RESTRICT_TOKENS_AND_JOB_RUN_AS = 'RESTRICT_TOKENS_AND_JOB_RUN_AS'


@dataclass
class RestrictWorkspaceAdminsSetting:
    restrict_workspace_admins: RestrictWorkspaceAdminsMessage

    etag: Optional[str] = None
    """etag used for versioning. The response is at least as fresh as the eTag provided. This is used
    for optimistic concurrency control as a way to help prevent simultaneous writes of a setting
    overwriting each other. It is strongly suggested that systems make use of the etag in the read
    -> update pattern to perform setting updates in order to avoid race conditions. That is, get an
    etag from a GET request, and pass it with the PATCH request to identify the setting version you
    are updating."""

    setting_name: Optional[str] = None
    """Name of the corresponding setting. This field is populated in the response, but it will not be
    respected even if it's set in the request body. The setting name in the path parameter will be
    respected instead. Setting name is required to be 'default' if the setting only has one instance
    per workspace."""

    def as_dict(self) -> dict:
        """Serializes the RestrictWorkspaceAdminsSetting into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.etag is not None: body['etag'] = self.etag
        if self.restrict_workspace_admins:
            body['restrict_workspace_admins'] = self.restrict_workspace_admins.as_dict()
        if self.setting_name is not None: body['setting_name'] = self.setting_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> RestrictWorkspaceAdminsSetting:
        """Deserializes the RestrictWorkspaceAdminsSetting from a dictionary."""
        return cls(etag=d.get('etag', None),
                   restrict_workspace_admins=_from_dict(d, 'restrict_workspace_admins',
                                                        RestrictWorkspaceAdminsMessage),
                   setting_name=d.get('setting_name', None))


@dataclass
class RevokeTokenRequest:
    token_id: str
    """The ID of the token to be revoked."""

    def as_dict(self) -> dict:
        """Serializes the RevokeTokenRequest into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.token_id is not None: body['token_id'] = self.token_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> RevokeTokenRequest:
        """Deserializes the RevokeTokenRequest from a dictionary."""
        return cls(token_id=d.get('token_id', None))


@dataclass
class RevokeTokenResponse:

    def as_dict(self) -> dict:
        """Serializes the RevokeTokenResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> RevokeTokenResponse:
        """Deserializes the RevokeTokenResponse from a dictionary."""
        return cls()


@dataclass
class SetStatusResponse:

    def as_dict(self) -> dict:
        """Serializes the SetStatusResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> SetStatusResponse:
        """Deserializes the SetStatusResponse from a dictionary."""
        return cls()


@dataclass
class SlackConfig:
    url: Optional[str] = None
    """[Input-Only] URL for Slack destination."""

    url_set: Optional[bool] = None
    """[Output-Only] Whether URL is set."""

    def as_dict(self) -> dict:
        """Serializes the SlackConfig into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.url is not None: body['url'] = self.url
        if self.url_set is not None: body['url_set'] = self.url_set
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> SlackConfig:
        """Deserializes the SlackConfig from a dictionary."""
        return cls(url=d.get('url', None), url_set=d.get('url_set', None))


@dataclass
class StringMessage:
    value: Optional[str] = None
    """Represents a generic string value."""

    def as_dict(self) -> dict:
        """Serializes the StringMessage into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.value is not None: body['value'] = self.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> StringMessage:
        """Deserializes the StringMessage from a dictionary."""
        return cls(value=d.get('value', None))


@dataclass
class TokenAccessControlRequest:
    group_name: Optional[str] = None
    """name of the group"""

    permission_level: Optional[TokenPermissionLevel] = None
    """Permission level"""

    service_principal_name: Optional[str] = None
    """application ID of a service principal"""

    user_name: Optional[str] = None
    """name of the user"""

    def as_dict(self) -> dict:
        """Serializes the TokenAccessControlRequest into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.group_name is not None: body['group_name'] = self.group_name
        if self.permission_level is not None: body['permission_level'] = self.permission_level.value
        if self.service_principal_name is not None:
            body['service_principal_name'] = self.service_principal_name
        if self.user_name is not None: body['user_name'] = self.user_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> TokenAccessControlRequest:
        """Deserializes the TokenAccessControlRequest from a dictionary."""
        return cls(group_name=d.get('group_name', None),
                   permission_level=_enum(d, 'permission_level', TokenPermissionLevel),
                   service_principal_name=d.get('service_principal_name', None),
                   user_name=d.get('user_name', None))


@dataclass
class TokenAccessControlResponse:
    all_permissions: Optional[List[TokenPermission]] = None
    """All permissions."""

    display_name: Optional[str] = None
    """Display name of the user or service principal."""

    group_name: Optional[str] = None
    """name of the group"""

    service_principal_name: Optional[str] = None
    """Name of the service principal."""

    user_name: Optional[str] = None
    """name of the user"""

    def as_dict(self) -> dict:
        """Serializes the TokenAccessControlResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.all_permissions: body['all_permissions'] = [v.as_dict() for v in self.all_permissions]
        if self.display_name is not None: body['display_name'] = self.display_name
        if self.group_name is not None: body['group_name'] = self.group_name
        if self.service_principal_name is not None:
            body['service_principal_name'] = self.service_principal_name
        if self.user_name is not None: body['user_name'] = self.user_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> TokenAccessControlResponse:
        """Deserializes the TokenAccessControlResponse from a dictionary."""
        return cls(all_permissions=_repeated_dict(d, 'all_permissions', TokenPermission),
                   display_name=d.get('display_name', None),
                   group_name=d.get('group_name', None),
                   service_principal_name=d.get('service_principal_name', None),
                   user_name=d.get('user_name', None))


@dataclass
class TokenInfo:
    comment: Optional[str] = None
    """Comment that describes the purpose of the token, specified by the token creator."""

    created_by_id: Optional[int] = None
    """User ID of the user that created the token."""

    created_by_username: Optional[str] = None
    """Username of the user that created the token."""

    creation_time: Optional[int] = None
    """Timestamp when the token was created."""

    expiry_time: Optional[int] = None
    """Timestamp when the token expires."""

    owner_id: Optional[int] = None
    """User ID of the user that owns the token."""

    token_id: Optional[str] = None
    """ID of the token."""

    workspace_id: Optional[int] = None
    """If applicable, the ID of the workspace that the token was created in."""

    def as_dict(self) -> dict:
        """Serializes the TokenInfo into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.comment is not None: body['comment'] = self.comment
        if self.created_by_id is not None: body['created_by_id'] = self.created_by_id
        if self.created_by_username is not None: body['created_by_username'] = self.created_by_username
        if self.creation_time is not None: body['creation_time'] = self.creation_time
        if self.expiry_time is not None: body['expiry_time'] = self.expiry_time
        if self.owner_id is not None: body['owner_id'] = self.owner_id
        if self.token_id is not None: body['token_id'] = self.token_id
        if self.workspace_id is not None: body['workspace_id'] = self.workspace_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> TokenInfo:
        """Deserializes the TokenInfo from a dictionary."""
        return cls(comment=d.get('comment', None),
                   created_by_id=d.get('created_by_id', None),
                   created_by_username=d.get('created_by_username', None),
                   creation_time=d.get('creation_time', None),
                   expiry_time=d.get('expiry_time', None),
                   owner_id=d.get('owner_id', None),
                   token_id=d.get('token_id', None),
                   workspace_id=d.get('workspace_id', None))


@dataclass
class TokenPermission:
    inherited: Optional[bool] = None

    inherited_from_object: Optional[List[str]] = None

    permission_level: Optional[TokenPermissionLevel] = None
    """Permission level"""

    def as_dict(self) -> dict:
        """Serializes the TokenPermission into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.inherited is not None: body['inherited'] = self.inherited
        if self.inherited_from_object: body['inherited_from_object'] = [v for v in self.inherited_from_object]
        if self.permission_level is not None: body['permission_level'] = self.permission_level.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> TokenPermission:
        """Deserializes the TokenPermission from a dictionary."""
        return cls(inherited=d.get('inherited', None),
                   inherited_from_object=d.get('inherited_from_object', None),
                   permission_level=_enum(d, 'permission_level', TokenPermissionLevel))


class TokenPermissionLevel(Enum):
    """Permission level"""

    CAN_USE = 'CAN_USE'


@dataclass
class TokenPermissions:
    access_control_list: Optional[List[TokenAccessControlResponse]] = None

    object_id: Optional[str] = None

    object_type: Optional[str] = None

    def as_dict(self) -> dict:
        """Serializes the TokenPermissions into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.access_control_list:
            body['access_control_list'] = [v.as_dict() for v in self.access_control_list]
        if self.object_id is not None: body['object_id'] = self.object_id
        if self.object_type is not None: body['object_type'] = self.object_type
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> TokenPermissions:
        """Deserializes the TokenPermissions from a dictionary."""
        return cls(access_control_list=_repeated_dict(d, 'access_control_list', TokenAccessControlResponse),
                   object_id=d.get('object_id', None),
                   object_type=d.get('object_type', None))


@dataclass
class TokenPermissionsDescription:
    description: Optional[str] = None

    permission_level: Optional[TokenPermissionLevel] = None
    """Permission level"""

    def as_dict(self) -> dict:
        """Serializes the TokenPermissionsDescription into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.description is not None: body['description'] = self.description
        if self.permission_level is not None: body['permission_level'] = self.permission_level.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> TokenPermissionsDescription:
        """Deserializes the TokenPermissionsDescription from a dictionary."""
        return cls(description=d.get('description', None),
                   permission_level=_enum(d, 'permission_level', TokenPermissionLevel))


@dataclass
class TokenPermissionsRequest:
    access_control_list: Optional[List[TokenAccessControlRequest]] = None

    def as_dict(self) -> dict:
        """Serializes the TokenPermissionsRequest into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.access_control_list:
            body['access_control_list'] = [v.as_dict() for v in self.access_control_list]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> TokenPermissionsRequest:
        """Deserializes the TokenPermissionsRequest from a dictionary."""
        return cls(access_control_list=_repeated_dict(d, 'access_control_list', TokenAccessControlRequest))


class TokenType(Enum):
    """The type of token request. As of now, only `AZURE_ACTIVE_DIRECTORY_TOKEN` is supported."""

    ARCLIGHT_AZURE_EXCHANGE_TOKEN = 'ARCLIGHT_AZURE_EXCHANGE_TOKEN'
    AZURE_ACTIVE_DIRECTORY_TOKEN = 'AZURE_ACTIVE_DIRECTORY_TOKEN'


@dataclass
class UpdateAutomaticClusterUpdateSettingRequest:
    """Details required to update a setting."""

    allow_missing: bool
    """This should always be set to true for Settings API. Added for AIP compliance."""

    setting: AutomaticClusterUpdateSetting

    field_mask: str
    """Field mask is required to be passed into the PATCH request. Field mask specifies which fields of
    the setting payload will be updated. The field mask needs to be supplied as single string. To
    specify multiple fields in the field mask, use comma as the separator (no space)."""

    def as_dict(self) -> dict:
        """Serializes the UpdateAutomaticClusterUpdateSettingRequest into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.allow_missing is not None: body['allow_missing'] = self.allow_missing
        if self.field_mask is not None: body['field_mask'] = self.field_mask
        if self.setting: body['setting'] = self.setting.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> UpdateAutomaticClusterUpdateSettingRequest:
        """Deserializes the UpdateAutomaticClusterUpdateSettingRequest from a dictionary."""
        return cls(allow_missing=d.get('allow_missing', None),
                   field_mask=d.get('field_mask', None),
                   setting=_from_dict(d, 'setting', AutomaticClusterUpdateSetting))


@dataclass
class UpdateComplianceSecurityProfileSettingRequest:
    """Details required to update a setting."""

    allow_missing: bool
    """This should always be set to true for Settings API. Added for AIP compliance."""

    setting: ComplianceSecurityProfileSetting

    field_mask: str
    """Field mask is required to be passed into the PATCH request. Field mask specifies which fields of
    the setting payload will be updated. The field mask needs to be supplied as single string. To
    specify multiple fields in the field mask, use comma as the separator (no space)."""

    def as_dict(self) -> dict:
        """Serializes the UpdateComplianceSecurityProfileSettingRequest into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.allow_missing is not None: body['allow_missing'] = self.allow_missing
        if self.field_mask is not None: body['field_mask'] = self.field_mask
        if self.setting: body['setting'] = self.setting.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> UpdateComplianceSecurityProfileSettingRequest:
        """Deserializes the UpdateComplianceSecurityProfileSettingRequest from a dictionary."""
        return cls(allow_missing=d.get('allow_missing', None),
                   field_mask=d.get('field_mask', None),
                   setting=_from_dict(d, 'setting', ComplianceSecurityProfileSetting))


@dataclass
class UpdateCspEnablementAccountSettingRequest:
    """Details required to update a setting."""

    allow_missing: bool
    """This should always be set to true for Settings API. Added for AIP compliance."""

    setting: CspEnablementAccountSetting

    field_mask: str
    """Field mask is required to be passed into the PATCH request. Field mask specifies which fields of
    the setting payload will be updated. The field mask needs to be supplied as single string. To
    specify multiple fields in the field mask, use comma as the separator (no space)."""

    def as_dict(self) -> dict:
        """Serializes the UpdateCspEnablementAccountSettingRequest into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.allow_missing is not None: body['allow_missing'] = self.allow_missing
        if self.field_mask is not None: body['field_mask'] = self.field_mask
        if self.setting: body['setting'] = self.setting.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> UpdateCspEnablementAccountSettingRequest:
        """Deserializes the UpdateCspEnablementAccountSettingRequest from a dictionary."""
        return cls(allow_missing=d.get('allow_missing', None),
                   field_mask=d.get('field_mask', None),
                   setting=_from_dict(d, 'setting', CspEnablementAccountSetting))


@dataclass
class UpdateDefaultNamespaceSettingRequest:
    """Details required to update a setting."""

    allow_missing: bool
    """This should always be set to true for Settings API. Added for AIP compliance."""

    setting: DefaultNamespaceSetting
    """This represents the setting configuration for the default namespace in the Databricks workspace.
    Setting the default catalog for the workspace determines the catalog that is used when queries
    do not reference a fully qualified 3 level name. For example, if the default catalog is set to
    'retail_prod' then a query 'SELECT * FROM myTable' would reference the object
    'retail_prod.default.myTable' (the schema 'default' is always assumed). This setting requires a
    restart of clusters and SQL warehouses to take effect. Additionally, the default namespace only
    applies when using Unity Catalog-enabled compute."""

    field_mask: str
    """Field mask is required to be passed into the PATCH request. Field mask specifies which fields of
    the setting payload will be updated. The field mask needs to be supplied as single string. To
    specify multiple fields in the field mask, use comma as the separator (no space)."""

    def as_dict(self) -> dict:
        """Serializes the UpdateDefaultNamespaceSettingRequest into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.allow_missing is not None: body['allow_missing'] = self.allow_missing
        if self.field_mask is not None: body['field_mask'] = self.field_mask
        if self.setting: body['setting'] = self.setting.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> UpdateDefaultNamespaceSettingRequest:
        """Deserializes the UpdateDefaultNamespaceSettingRequest from a dictionary."""
        return cls(allow_missing=d.get('allow_missing', None),
                   field_mask=d.get('field_mask', None),
                   setting=_from_dict(d, 'setting', DefaultNamespaceSetting))


@dataclass
class UpdateDisableLegacyAccessRequest:
    """Details required to update a setting."""

    allow_missing: bool
    """This should always be set to true for Settings API. Added for AIP compliance."""

    setting: DisableLegacyAccess

    field_mask: str
    """Field mask is required to be passed into the PATCH request. Field mask specifies which fields of
    the setting payload will be updated. The field mask needs to be supplied as single string. To
    specify multiple fields in the field mask, use comma as the separator (no space)."""

    def as_dict(self) -> dict:
        """Serializes the UpdateDisableLegacyAccessRequest into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.allow_missing is not None: body['allow_missing'] = self.allow_missing
        if self.field_mask is not None: body['field_mask'] = self.field_mask
        if self.setting: body['setting'] = self.setting.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> UpdateDisableLegacyAccessRequest:
        """Deserializes the UpdateDisableLegacyAccessRequest from a dictionary."""
        return cls(allow_missing=d.get('allow_missing', None),
                   field_mask=d.get('field_mask', None),
                   setting=_from_dict(d, 'setting', DisableLegacyAccess))


@dataclass
class UpdateDisableLegacyDbfsRequest:
    """Details required to update a setting."""

    allow_missing: bool
    """This should always be set to true for Settings API. Added for AIP compliance."""

    setting: DisableLegacyDbfs

    field_mask: str
    """Field mask is required to be passed into the PATCH request. Field mask specifies which fields of
    the setting payload will be updated. The field mask needs to be supplied as single string. To
    specify multiple fields in the field mask, use comma as the separator (no space)."""

    def as_dict(self) -> dict:
        """Serializes the UpdateDisableLegacyDbfsRequest into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.allow_missing is not None: body['allow_missing'] = self.allow_missing
        if self.field_mask is not None: body['field_mask'] = self.field_mask
        if self.setting: body['setting'] = self.setting.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> UpdateDisableLegacyDbfsRequest:
        """Deserializes the UpdateDisableLegacyDbfsRequest from a dictionary."""
        return cls(allow_missing=d.get('allow_missing', None),
                   field_mask=d.get('field_mask', None),
                   setting=_from_dict(d, 'setting', DisableLegacyDbfs))


@dataclass
class UpdateDisableLegacyFeaturesRequest:
    """Details required to update a setting."""

    allow_missing: bool
    """This should always be set to true for Settings API. Added for AIP compliance."""

    setting: DisableLegacyFeatures

    field_mask: str
    """Field mask is required to be passed into the PATCH request. Field mask specifies which fields of
    the setting payload will be updated. The field mask needs to be supplied as single string. To
    specify multiple fields in the field mask, use comma as the separator (no space)."""

    def as_dict(self) -> dict:
        """Serializes the UpdateDisableLegacyFeaturesRequest into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.allow_missing is not None: body['allow_missing'] = self.allow_missing
        if self.field_mask is not None: body['field_mask'] = self.field_mask
        if self.setting: body['setting'] = self.setting.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> UpdateDisableLegacyFeaturesRequest:
        """Deserializes the UpdateDisableLegacyFeaturesRequest from a dictionary."""
        return cls(allow_missing=d.get('allow_missing', None),
                   field_mask=d.get('field_mask', None),
                   setting=_from_dict(d, 'setting', DisableLegacyFeatures))


@dataclass
class UpdateEnhancedSecurityMonitoringSettingRequest:
    """Details required to update a setting."""

    allow_missing: bool
    """This should always be set to true for Settings API. Added for AIP compliance."""

    setting: EnhancedSecurityMonitoringSetting

    field_mask: str
    """Field mask is required to be passed into the PATCH request. Field mask specifies which fields of
    the setting payload will be updated. The field mask needs to be supplied as single string. To
    specify multiple fields in the field mask, use comma as the separator (no space)."""

    def as_dict(self) -> dict:
        """Serializes the UpdateEnhancedSecurityMonitoringSettingRequest into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.allow_missing is not None: body['allow_missing'] = self.allow_missing
        if self.field_mask is not None: body['field_mask'] = self.field_mask
        if self.setting: body['setting'] = self.setting.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> UpdateEnhancedSecurityMonitoringSettingRequest:
        """Deserializes the UpdateEnhancedSecurityMonitoringSettingRequest from a dictionary."""
        return cls(allow_missing=d.get('allow_missing', None),
                   field_mask=d.get('field_mask', None),
                   setting=_from_dict(d, 'setting', EnhancedSecurityMonitoringSetting))


@dataclass
class UpdateEsmEnablementAccountSettingRequest:
    """Details required to update a setting."""

    allow_missing: bool
    """This should always be set to true for Settings API. Added for AIP compliance."""

    setting: EsmEnablementAccountSetting

    field_mask: str
    """Field mask is required to be passed into the PATCH request. Field mask specifies which fields of
    the setting payload will be updated. The field mask needs to be supplied as single string. To
    specify multiple fields in the field mask, use comma as the separator (no space)."""

    def as_dict(self) -> dict:
        """Serializes the UpdateEsmEnablementAccountSettingRequest into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.allow_missing is not None: body['allow_missing'] = self.allow_missing
        if self.field_mask is not None: body['field_mask'] = self.field_mask
        if self.setting: body['setting'] = self.setting.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> UpdateEsmEnablementAccountSettingRequest:
        """Deserializes the UpdateEsmEnablementAccountSettingRequest from a dictionary."""
        return cls(allow_missing=d.get('allow_missing', None),
                   field_mask=d.get('field_mask', None),
                   setting=_from_dict(d, 'setting', EsmEnablementAccountSetting))


@dataclass
class UpdateIpAccessList:
    """Details required to update an IP access list."""

    enabled: Optional[bool] = None
    """Specifies whether this IP access list is enabled."""

    ip_access_list_id: Optional[str] = None
    """The ID for the corresponding IP access list"""

    ip_addresses: Optional[List[str]] = None

    label: Optional[str] = None
    """Label for the IP access list. This **cannot** be empty."""

    list_type: Optional[ListType] = None
    """Type of IP access list. Valid values are as follows and are case-sensitive:
    
    * `ALLOW`: An allow list. Include this IP or range. * `BLOCK`: A block list. Exclude this IP or
    range. IP addresses in the block list are excluded even if they are included in an allow list."""

    def as_dict(self) -> dict:
        """Serializes the UpdateIpAccessList into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.enabled is not None: body['enabled'] = self.enabled
        if self.ip_access_list_id is not None: body['ip_access_list_id'] = self.ip_access_list_id
        if self.ip_addresses: body['ip_addresses'] = [v for v in self.ip_addresses]
        if self.label is not None: body['label'] = self.label
        if self.list_type is not None: body['list_type'] = self.list_type.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> UpdateIpAccessList:
        """Deserializes the UpdateIpAccessList from a dictionary."""
        return cls(enabled=d.get('enabled', None),
                   ip_access_list_id=d.get('ip_access_list_id', None),
                   ip_addresses=d.get('ip_addresses', None),
                   label=d.get('label', None),
                   list_type=_enum(d, 'list_type', ListType))


@dataclass
class UpdateNotificationDestinationRequest:
    config: Optional[Config] = None
    """The configuration for the notification destination. Must wrap EXACTLY one of the nested configs."""

    display_name: Optional[str] = None
    """The display name for the notification destination."""

    id: Optional[str] = None

    def as_dict(self) -> dict:
        """Serializes the UpdateNotificationDestinationRequest into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.config: body['config'] = self.config.as_dict()
        if self.display_name is not None: body['display_name'] = self.display_name
        if self.id is not None: body['id'] = self.id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> UpdateNotificationDestinationRequest:
        """Deserializes the UpdateNotificationDestinationRequest from a dictionary."""
        return cls(config=_from_dict(d, 'config', Config),
                   display_name=d.get('display_name', None),
                   id=d.get('id', None))


@dataclass
class UpdatePersonalComputeSettingRequest:
    """Details required to update a setting."""

    allow_missing: bool
    """This should always be set to true for Settings API. Added for AIP compliance."""

    setting: PersonalComputeSetting

    field_mask: str
    """Field mask is required to be passed into the PATCH request. Field mask specifies which fields of
    the setting payload will be updated. The field mask needs to be supplied as single string. To
    specify multiple fields in the field mask, use comma as the separator (no space)."""

    def as_dict(self) -> dict:
        """Serializes the UpdatePersonalComputeSettingRequest into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.allow_missing is not None: body['allow_missing'] = self.allow_missing
        if self.field_mask is not None: body['field_mask'] = self.field_mask
        if self.setting: body['setting'] = self.setting.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> UpdatePersonalComputeSettingRequest:
        """Deserializes the UpdatePersonalComputeSettingRequest from a dictionary."""
        return cls(allow_missing=d.get('allow_missing', None),
                   field_mask=d.get('field_mask', None),
                   setting=_from_dict(d, 'setting', PersonalComputeSetting))


@dataclass
class UpdateResponse:

    def as_dict(self) -> dict:
        """Serializes the UpdateResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> UpdateResponse:
        """Deserializes the UpdateResponse from a dictionary."""
        return cls()


@dataclass
class UpdateRestrictWorkspaceAdminsSettingRequest:
    """Details required to update a setting."""

    allow_missing: bool
    """This should always be set to true for Settings API. Added for AIP compliance."""

    setting: RestrictWorkspaceAdminsSetting

    field_mask: str
    """Field mask is required to be passed into the PATCH request. Field mask specifies which fields of
    the setting payload will be updated. The field mask needs to be supplied as single string. To
    specify multiple fields in the field mask, use comma as the separator (no space)."""

    def as_dict(self) -> dict:
        """Serializes the UpdateRestrictWorkspaceAdminsSettingRequest into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.allow_missing is not None: body['allow_missing'] = self.allow_missing
        if self.field_mask is not None: body['field_mask'] = self.field_mask
        if self.setting: body['setting'] = self.setting.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> UpdateRestrictWorkspaceAdminsSettingRequest:
        """Deserializes the UpdateRestrictWorkspaceAdminsSettingRequest from a dictionary."""
        return cls(allow_missing=d.get('allow_missing', None),
                   field_mask=d.get('field_mask', None),
                   setting=_from_dict(d, 'setting', RestrictWorkspaceAdminsSetting))


WorkspaceConf = Dict[str, str]


class AccountIpAccessListsAPI:
    """The Accounts IP Access List API enables account admins to configure IP access lists for access to the
    account console.
    
    Account IP Access Lists affect web application access and REST API access to the account console and
    account APIs. If the feature is disabled for the account, all access is allowed for this account. There is
    support for allow lists (inclusion) and block lists (exclusion).
    
    When a connection is attempted: 1. **First, all block lists are checked.** If the connection IP address
    matches any block list, the connection is rejected. 2. **If the connection was not rejected by block
    lists**, the IP address is compared with the allow lists.
    
    If there is at least one allow list for the account, the connection is allowed only if the IP address
    matches an allow list. If there are no allow lists for the account, all IP addresses are allowed.
    
    For all allow lists and block lists combined, the account supports a maximum of 1000 IP/CIDR values, where
    one CIDR counts as a single value.
    
    After changes to the account-level IP access lists, it can take a few minutes for changes to take effect."""

    def __init__(self, api_client):
        self._api = api_client

    def create(self,
               label: str,
               list_type: ListType,
               *,
               ip_addresses: Optional[List[str]] = None) -> CreateIpAccessListResponse:
        """Create access list.
        
        Creates an IP access list for the account.
        
        A list can be an allow list or a block list. See the top of this file for a description of how the
        server treats allow lists and block lists at runtime.
        
        When creating or updating an IP access list:
        
        * For all allow lists and block lists combined, the API supports a maximum of 1000 IP/CIDR values,
        where one CIDR counts as a single value. Attempts to exceed that number return error 400 with
        `error_code` value `QUOTA_EXCEEDED`. * If the new list would block the calling user's current IP,
        error 400 is returned with `error_code` value `INVALID_STATE`.
        
        It can take a few minutes for the changes to take effect.
        
        :param label: str
          Label for the IP access list. This **cannot** be empty.
        :param list_type: :class:`ListType`
          Type of IP access list. Valid values are as follows and are case-sensitive:
          
          * `ALLOW`: An allow list. Include this IP or range. * `BLOCK`: A block list. Exclude this IP or
          range. IP addresses in the block list are excluded even if they are included in an allow list.
        :param ip_addresses: List[str] (optional)
        
        :returns: :class:`CreateIpAccessListResponse`
        """
        body = {}
        if ip_addresses is not None: body['ip_addresses'] = [v for v in ip_addresses]
        if label is not None: body['label'] = label
        if list_type is not None: body['list_type'] = list_type.value
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        res = self._api.do('POST',
                           f'/api/2.0/accounts/{self._api.account_id}/ip-access-lists',
                           body=body,
                           headers=headers)
        return CreateIpAccessListResponse.from_dict(res)

    def delete(self, ip_access_list_id: str):
        """Delete access list.
        
        Deletes an IP access list, specified by its list ID.
        
        :param ip_access_list_id: str
          The ID for the corresponding IP access list
        
        
        """

        headers = {'Accept': 'application/json', }

        self._api.do('DELETE',
                     f'/api/2.0/accounts/{self._api.account_id}/ip-access-lists/{ip_access_list_id}',
                     headers=headers)

    def get(self, ip_access_list_id: str) -> GetIpAccessListResponse:
        """Get IP access list.
        
        Gets an IP access list, specified by its list ID.
        
        :param ip_access_list_id: str
          The ID for the corresponding IP access list
        
        :returns: :class:`GetIpAccessListResponse`
        """

        headers = {'Accept': 'application/json', }

        res = self._api.do('GET',
                           f'/api/2.0/accounts/{self._api.account_id}/ip-access-lists/{ip_access_list_id}',
                           headers=headers)
        return GetIpAccessListResponse.from_dict(res)

    def list(self) -> Iterator[IpAccessListInfo]:
        """Get access lists.
        
        Gets all IP access lists for the specified account.
        
        :returns: Iterator over :class:`IpAccessListInfo`
        """

        headers = {'Accept': 'application/json', }

        json = self._api.do('GET',
                            f'/api/2.0/accounts/{self._api.account_id}/ip-access-lists',
                            headers=headers)
        parsed = GetIpAccessListsResponse.from_dict(json).ip_access_lists
        return parsed if parsed is not None else []

    def replace(self,
                ip_access_list_id: str,
                label: str,
                list_type: ListType,
                enabled: bool,
                *,
                ip_addresses: Optional[List[str]] = None):
        """Replace access list.
        
        Replaces an IP access list, specified by its ID.
        
        A list can include allow lists and block lists. See the top of this file for a description of how the
        server treats allow lists and block lists at run time. When replacing an IP access list: * For all
        allow lists and block lists combined, the API supports a maximum of 1000 IP/CIDR values, where one
        CIDR counts as a single value. Attempts to exceed that number return error 400 with `error_code` value
        `QUOTA_EXCEEDED`. * If the resulting list would block the calling user's current IP, error 400 is
        returned with `error_code` value `INVALID_STATE`. It can take a few minutes for the changes to take
        effect.
        
        :param ip_access_list_id: str
          The ID for the corresponding IP access list
        :param label: str
          Label for the IP access list. This **cannot** be empty.
        :param list_type: :class:`ListType`
          Type of IP access list. Valid values are as follows and are case-sensitive:
          
          * `ALLOW`: An allow list. Include this IP or range. * `BLOCK`: A block list. Exclude this IP or
          range. IP addresses in the block list are excluded even if they are included in an allow list.
        :param enabled: bool
          Specifies whether this IP access list is enabled.
        :param ip_addresses: List[str] (optional)
        
        
        """
        body = {}
        if enabled is not None: body['enabled'] = enabled
        if ip_addresses is not None: body['ip_addresses'] = [v for v in ip_addresses]
        if label is not None: body['label'] = label
        if list_type is not None: body['list_type'] = list_type.value
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        self._api.do('PUT',
                     f'/api/2.0/accounts/{self._api.account_id}/ip-access-lists/{ip_access_list_id}',
                     body=body,
                     headers=headers)

    def update(self,
               ip_access_list_id: str,
               *,
               enabled: Optional[bool] = None,
               ip_addresses: Optional[List[str]] = None,
               label: Optional[str] = None,
               list_type: Optional[ListType] = None):
        """Update access list.
        
        Updates an existing IP access list, specified by its ID.
        
        A list can include allow lists and block lists. See the top of this file for a description of how the
        server treats allow lists and block lists at run time.
        
        When updating an IP access list:
        
        * For all allow lists and block lists combined, the API supports a maximum of 1000 IP/CIDR values,
        where one CIDR counts as a single value. Attempts to exceed that number return error 400 with
        `error_code` value `QUOTA_EXCEEDED`. * If the updated list would block the calling user's current IP,
        error 400 is returned with `error_code` value `INVALID_STATE`.
        
        It can take a few minutes for the changes to take effect.
        
        :param ip_access_list_id: str
          The ID for the corresponding IP access list
        :param enabled: bool (optional)
          Specifies whether this IP access list is enabled.
        :param ip_addresses: List[str] (optional)
        :param label: str (optional)
          Label for the IP access list. This **cannot** be empty.
        :param list_type: :class:`ListType` (optional)
          Type of IP access list. Valid values are as follows and are case-sensitive:
          
          * `ALLOW`: An allow list. Include this IP or range. * `BLOCK`: A block list. Exclude this IP or
          range. IP addresses in the block list are excluded even if they are included in an allow list.
        
        
        """
        body = {}
        if enabled is not None: body['enabled'] = enabled
        if ip_addresses is not None: body['ip_addresses'] = [v for v in ip_addresses]
        if label is not None: body['label'] = label
        if list_type is not None: body['list_type'] = list_type.value
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        self._api.do('PATCH',
                     f'/api/2.0/accounts/{self._api.account_id}/ip-access-lists/{ip_access_list_id}',
                     body=body,
                     headers=headers)


class AccountSettingsAPI:
    """Accounts Settings API allows users to manage settings at the account level."""

    def __init__(self, api_client):
        self._api = api_client

        self._csp_enablement_account = CspEnablementAccountAPI(self._api)
        self._disable_legacy_features = DisableLegacyFeaturesAPI(self._api)
        self._esm_enablement_account = EsmEnablementAccountAPI(self._api)
        self._personal_compute = PersonalComputeAPI(self._api)

    @property
    def csp_enablement_account(self) -> CspEnablementAccountAPI:
        """The compliance security profile settings at the account level control whether to enable it for new workspaces."""
        return self._csp_enablement_account

    @property
    def disable_legacy_features(self) -> DisableLegacyFeaturesAPI:
        """Disable legacy features for new Databricks workspaces."""
        return self._disable_legacy_features

    @property
    def esm_enablement_account(self) -> EsmEnablementAccountAPI:
        """The enhanced security monitoring setting at the account level controls whether to enable the feature on new workspaces."""
        return self._esm_enablement_account

    @property
    def personal_compute(self) -> PersonalComputeAPI:
        """The Personal Compute enablement setting lets you control which users can use the Personal Compute default policy to create compute resources."""
        return self._personal_compute


class AutomaticClusterUpdateAPI:
    """Controls whether automatic cluster update is enabled for the current workspace. By default, it is turned
    off."""

    def __init__(self, api_client):
        self._api = api_client

    def get(self, *, etag: Optional[str] = None) -> AutomaticClusterUpdateSetting:
        """Get the automatic cluster update setting.
        
        Gets the automatic cluster update setting.
        
        :param etag: str (optional)
          etag used for versioning. The response is at least as fresh as the eTag provided. This is used for
          optimistic concurrency control as a way to help prevent simultaneous writes of a setting overwriting
          each other. It is strongly suggested that systems make use of the etag in the read -> delete pattern
          to perform setting deletions in order to avoid race conditions. That is, get an etag from a GET
          request, and pass it with the DELETE request to identify the rule set version you are deleting.
        
        :returns: :class:`AutomaticClusterUpdateSetting`
        """

        query = {}
        if etag is not None: query['etag'] = etag
        headers = {'Accept': 'application/json', }

        res = self._api.do('GET',
                           '/api/2.0/settings/types/automatic_cluster_update/names/default',
                           query=query,
                           headers=headers)
        return AutomaticClusterUpdateSetting.from_dict(res)

    def update(self, allow_missing: bool, setting: AutomaticClusterUpdateSetting,
               field_mask: str) -> AutomaticClusterUpdateSetting:
        """Update the automatic cluster update setting.
        
        Updates the automatic cluster update setting for the workspace. A fresh etag needs to be provided in
        `PATCH` requests (as part of the setting field). The etag can be retrieved by making a `GET` request
        before the `PATCH` request. If the setting is updated concurrently, `PATCH` fails with 409 and the
        request must be retried by using the fresh etag in the 409 response.
        
        :param allow_missing: bool
          This should always be set to true for Settings API. Added for AIP compliance.
        :param setting: :class:`AutomaticClusterUpdateSetting`
        :param field_mask: str
          Field mask is required to be passed into the PATCH request. Field mask specifies which fields of the
          setting payload will be updated. The field mask needs to be supplied as single string. To specify
          multiple fields in the field mask, use comma as the separator (no space).
        
        :returns: :class:`AutomaticClusterUpdateSetting`
        """
        body = {}
        if allow_missing is not None: body['allow_missing'] = allow_missing
        if field_mask is not None: body['field_mask'] = field_mask
        if setting is not None: body['setting'] = setting.as_dict()
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        res = self._api.do('PATCH',
                           '/api/2.0/settings/types/automatic_cluster_update/names/default',
                           body=body,
                           headers=headers)
        return AutomaticClusterUpdateSetting.from_dict(res)


class ComplianceSecurityProfileAPI:
    """Controls whether to enable the compliance security profile for the current workspace. Enabling it on a
    workspace is permanent. By default, it is turned off.
    
    This settings can NOT be disabled once it is enabled."""

    def __init__(self, api_client):
        self._api = api_client

    def get(self, *, etag: Optional[str] = None) -> ComplianceSecurityProfileSetting:
        """Get the compliance security profile setting.
        
        Gets the compliance security profile setting.
        
        :param etag: str (optional)
          etag used for versioning. The response is at least as fresh as the eTag provided. This is used for
          optimistic concurrency control as a way to help prevent simultaneous writes of a setting overwriting
          each other. It is strongly suggested that systems make use of the etag in the read -> delete pattern
          to perform setting deletions in order to avoid race conditions. That is, get an etag from a GET
          request, and pass it with the DELETE request to identify the rule set version you are deleting.
        
        :returns: :class:`ComplianceSecurityProfileSetting`
        """

        query = {}
        if etag is not None: query['etag'] = etag
        headers = {'Accept': 'application/json', }

        res = self._api.do('GET',
                           '/api/2.0/settings/types/shield_csp_enablement_ws_db/names/default',
                           query=query,
                           headers=headers)
        return ComplianceSecurityProfileSetting.from_dict(res)

    def update(self, allow_missing: bool, setting: ComplianceSecurityProfileSetting,
               field_mask: str) -> ComplianceSecurityProfileSetting:
        """Update the compliance security profile setting.
        
        Updates the compliance security profile setting for the workspace. A fresh etag needs to be provided
        in `PATCH` requests (as part of the setting field). The etag can be retrieved by making a `GET`
        request before the `PATCH` request. If the setting is updated concurrently, `PATCH` fails with 409 and
        the request must be retried by using the fresh etag in the 409 response.
        
        :param allow_missing: bool
          This should always be set to true for Settings API. Added for AIP compliance.
        :param setting: :class:`ComplianceSecurityProfileSetting`
        :param field_mask: str
          Field mask is required to be passed into the PATCH request. Field mask specifies which fields of the
          setting payload will be updated. The field mask needs to be supplied as single string. To specify
          multiple fields in the field mask, use comma as the separator (no space).
        
        :returns: :class:`ComplianceSecurityProfileSetting`
        """
        body = {}
        if allow_missing is not None: body['allow_missing'] = allow_missing
        if field_mask is not None: body['field_mask'] = field_mask
        if setting is not None: body['setting'] = setting.as_dict()
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        res = self._api.do('PATCH',
                           '/api/2.0/settings/types/shield_csp_enablement_ws_db/names/default',
                           body=body,
                           headers=headers)
        return ComplianceSecurityProfileSetting.from_dict(res)


class CredentialsManagerAPI:
    """Credentials manager interacts with with Identity Providers to to perform token exchanges using stored
    credentials and refresh tokens."""

    def __init__(self, api_client):
        self._api = api_client

    def exchange_token(self, partition_id: PartitionId, token_type: List[TokenType],
                       scopes: List[str]) -> ExchangeTokenResponse:
        """Exchange token.
        
        Exchange tokens with an Identity Provider to get a new access token. It allows specifying scopes to
        determine token permissions.
        
        :param partition_id: :class:`PartitionId`
          The partition of Credentials store
        :param token_type: List[:class:`TokenType`]
          A list of token types being requested
        :param scopes: List[str]
          Array of scopes for the token request.
        
        :returns: :class:`ExchangeTokenResponse`
        """
        body = {}
        if partition_id is not None: body['partitionId'] = partition_id.as_dict()
        if scopes is not None: body['scopes'] = [v for v in scopes]
        if token_type is not None: body['tokenType'] = [v.value for v in token_type]
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        res = self._api.do('POST',
                           '/api/2.0/credentials-manager/exchange-tokens/token',
                           body=body,
                           headers=headers)
        return ExchangeTokenResponse.from_dict(res)


class CspEnablementAccountAPI:
    """The compliance security profile settings at the account level control whether to enable it for new
    workspaces. By default, this account-level setting is disabled for new workspaces. After workspace
    creation, account admins can enable the compliance security profile individually for each workspace.
    
    This settings can be disabled so that new workspaces do not have compliance security profile enabled by
    default."""

    def __init__(self, api_client):
        self._api = api_client

    def get(self, *, etag: Optional[str] = None) -> CspEnablementAccountSetting:
        """Get the compliance security profile setting for new workspaces.
        
        Gets the compliance security profile setting for new workspaces.
        
        :param etag: str (optional)
          etag used for versioning. The response is at least as fresh as the eTag provided. This is used for
          optimistic concurrency control as a way to help prevent simultaneous writes of a setting overwriting
          each other. It is strongly suggested that systems make use of the etag in the read -> delete pattern
          to perform setting deletions in order to avoid race conditions. That is, get an etag from a GET
          request, and pass it with the DELETE request to identify the rule set version you are deleting.
        
        :returns: :class:`CspEnablementAccountSetting`
        """

        query = {}
        if etag is not None: query['etag'] = etag
        headers = {'Accept': 'application/json', }

        res = self._api.do(
            'GET',
            f'/api/2.0/accounts/{self._api.account_id}/settings/types/shield_csp_enablement_ac/names/default',
            query=query,
            headers=headers)
        return CspEnablementAccountSetting.from_dict(res)

    def update(self, allow_missing: bool, setting: CspEnablementAccountSetting,
               field_mask: str) -> CspEnablementAccountSetting:
        """Update the compliance security profile setting for new workspaces.
        
        Updates the value of the compliance security profile setting for new workspaces.
        
        :param allow_missing: bool
          This should always be set to true for Settings API. Added for AIP compliance.
        :param setting: :class:`CspEnablementAccountSetting`
        :param field_mask: str
          Field mask is required to be passed into the PATCH request. Field mask specifies which fields of the
          setting payload will be updated. The field mask needs to be supplied as single string. To specify
          multiple fields in the field mask, use comma as the separator (no space).
        
        :returns: :class:`CspEnablementAccountSetting`
        """
        body = {}
        if allow_missing is not None: body['allow_missing'] = allow_missing
        if field_mask is not None: body['field_mask'] = field_mask
        if setting is not None: body['setting'] = setting.as_dict()
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        res = self._api.do(
            'PATCH',
            f'/api/2.0/accounts/{self._api.account_id}/settings/types/shield_csp_enablement_ac/names/default',
            body=body,
            headers=headers)
        return CspEnablementAccountSetting.from_dict(res)


class DefaultNamespaceAPI:
    """The default namespace setting API allows users to configure the default namespace for a Databricks
    workspace.
    
    Through this API, users can retrieve, set, or modify the default namespace used when queries do not
    reference a fully qualified three-level name. For example, if you use the API to set 'retail_prod' as the
    default catalog, then a query 'SELECT * FROM myTable' would reference the object
    'retail_prod.default.myTable' (the schema 'default' is always assumed).
    
    This setting requires a restart of clusters and SQL warehouses to take effect. Additionally, the default
    namespace only applies when using Unity Catalog-enabled compute."""

    def __init__(self, api_client):
        self._api = api_client

    def delete(self, *, etag: Optional[str] = None) -> DeleteDefaultNamespaceSettingResponse:
        """Delete the default namespace setting.
        
        Deletes the default namespace setting for the workspace. A fresh etag needs to be provided in `DELETE`
        requests (as a query parameter). The etag can be retrieved by making a `GET` request before the
        `DELETE` request. If the setting is updated/deleted concurrently, `DELETE` fails with 409 and the
        request must be retried by using the fresh etag in the 409 response.
        
        :param etag: str (optional)
          etag used for versioning. The response is at least as fresh as the eTag provided. This is used for
          optimistic concurrency control as a way to help prevent simultaneous writes of a setting overwriting
          each other. It is strongly suggested that systems make use of the etag in the read -> delete pattern
          to perform setting deletions in order to avoid race conditions. That is, get an etag from a GET
          request, and pass it with the DELETE request to identify the rule set version you are deleting.
        
        :returns: :class:`DeleteDefaultNamespaceSettingResponse`
        """

        query = {}
        if etag is not None: query['etag'] = etag
        headers = {'Accept': 'application/json', }

        res = self._api.do('DELETE',
                           '/api/2.0/settings/types/default_namespace_ws/names/default',
                           query=query,
                           headers=headers)
        return DeleteDefaultNamespaceSettingResponse.from_dict(res)

    def get(self, *, etag: Optional[str] = None) -> DefaultNamespaceSetting:
        """Get the default namespace setting.
        
        Gets the default namespace setting.
        
        :param etag: str (optional)
          etag used for versioning. The response is at least as fresh as the eTag provided. This is used for
          optimistic concurrency control as a way to help prevent simultaneous writes of a setting overwriting
          each other. It is strongly suggested that systems make use of the etag in the read -> delete pattern
          to perform setting deletions in order to avoid race conditions. That is, get an etag from a GET
          request, and pass it with the DELETE request to identify the rule set version you are deleting.
        
        :returns: :class:`DefaultNamespaceSetting`
        """

        query = {}
        if etag is not None: query['etag'] = etag
        headers = {'Accept': 'application/json', }

        res = self._api.do('GET',
                           '/api/2.0/settings/types/default_namespace_ws/names/default',
                           query=query,
                           headers=headers)
        return DefaultNamespaceSetting.from_dict(res)

    def update(self, allow_missing: bool, setting: DefaultNamespaceSetting,
               field_mask: str) -> DefaultNamespaceSetting:
        """Update the default namespace setting.
        
        Updates the default namespace setting for the workspace. A fresh etag needs to be provided in `PATCH`
        requests (as part of the setting field). The etag can be retrieved by making a `GET` request before
        the `PATCH` request. Note that if the setting does not exist, `GET` returns a NOT_FOUND error and the
        etag is present in the error response, which should be set in the `PATCH` request. If the setting is
        updated concurrently, `PATCH` fails with 409 and the request must be retried by using the fresh etag
        in the 409 response.
        
        :param allow_missing: bool
          This should always be set to true for Settings API. Added for AIP compliance.
        :param setting: :class:`DefaultNamespaceSetting`
          This represents the setting configuration for the default namespace in the Databricks workspace.
          Setting the default catalog for the workspace determines the catalog that is used when queries do
          not reference a fully qualified 3 level name. For example, if the default catalog is set to
          'retail_prod' then a query 'SELECT * FROM myTable' would reference the object
          'retail_prod.default.myTable' (the schema 'default' is always assumed). This setting requires a
          restart of clusters and SQL warehouses to take effect. Additionally, the default namespace only
          applies when using Unity Catalog-enabled compute.
        :param field_mask: str
          Field mask is required to be passed into the PATCH request. Field mask specifies which fields of the
          setting payload will be updated. The field mask needs to be supplied as single string. To specify
          multiple fields in the field mask, use comma as the separator (no space).
        
        :returns: :class:`DefaultNamespaceSetting`
        """
        body = {}
        if allow_missing is not None: body['allow_missing'] = allow_missing
        if field_mask is not None: body['field_mask'] = field_mask
        if setting is not None: body['setting'] = setting.as_dict()
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        res = self._api.do('PATCH',
                           '/api/2.0/settings/types/default_namespace_ws/names/default',
                           body=body,
                           headers=headers)
        return DefaultNamespaceSetting.from_dict(res)


class DisableLegacyAccessAPI:
    """'Disabling legacy access' has the following impacts:
    
    1. Disables direct access to the Hive Metastore. However, you can still access Hive Metastore through HMS
    Federation. 2. Disables Fallback Mode (docs link) on any External Location access from the workspace. 3.
    Alters DBFS path access to use External Location permissions in place of legacy credentials. 4. Enforces
    Unity Catalog access on all path based access."""

    def __init__(self, api_client):
        self._api = api_client

    def delete(self, *, etag: Optional[str] = None) -> DeleteDisableLegacyAccessResponse:
        """Delete Legacy Access Disablement Status.
        
        Deletes legacy access disablement status.
        
        :param etag: str (optional)
          etag used for versioning. The response is at least as fresh as the eTag provided. This is used for
          optimistic concurrency control as a way to help prevent simultaneous writes of a setting overwriting
          each other. It is strongly suggested that systems make use of the etag in the read -> delete pattern
          to perform setting deletions in order to avoid race conditions. That is, get an etag from a GET
          request, and pass it with the DELETE request to identify the rule set version you are deleting.
        
        :returns: :class:`DeleteDisableLegacyAccessResponse`
        """

        query = {}
        if etag is not None: query['etag'] = etag
        headers = {'Accept': 'application/json', }

        res = self._api.do('DELETE',
                           '/api/2.0/settings/types/disable_legacy_access/names/default',
                           query=query,
                           headers=headers)
        return DeleteDisableLegacyAccessResponse.from_dict(res)

    def get(self, *, etag: Optional[str] = None) -> DisableLegacyAccess:
        """Retrieve Legacy Access Disablement Status.
        
        Retrieves legacy access disablement Status.
        
        :param etag: str (optional)
          etag used for versioning. The response is at least as fresh as the eTag provided. This is used for
          optimistic concurrency control as a way to help prevent simultaneous writes of a setting overwriting
          each other. It is strongly suggested that systems make use of the etag in the read -> delete pattern
          to perform setting deletions in order to avoid race conditions. That is, get an etag from a GET
          request, and pass it with the DELETE request to identify the rule set version you are deleting.
        
        :returns: :class:`DisableLegacyAccess`
        """

        query = {}
        if etag is not None: query['etag'] = etag
        headers = {'Accept': 'application/json', }

        res = self._api.do('GET',
                           '/api/2.0/settings/types/disable_legacy_access/names/default',
                           query=query,
                           headers=headers)
        return DisableLegacyAccess.from_dict(res)

    def update(self, allow_missing: bool, setting: DisableLegacyAccess,
               field_mask: str) -> DisableLegacyAccess:
        """Update Legacy Access Disablement Status.
        
        Updates legacy access disablement status.
        
        :param allow_missing: bool
          This should always be set to true for Settings API. Added for AIP compliance.
        :param setting: :class:`DisableLegacyAccess`
        :param field_mask: str
          Field mask is required to be passed into the PATCH request. Field mask specifies which fields of the
          setting payload will be updated. The field mask needs to be supplied as single string. To specify
          multiple fields in the field mask, use comma as the separator (no space).
        
        :returns: :class:`DisableLegacyAccess`
        """
        body = {}
        if allow_missing is not None: body['allow_missing'] = allow_missing
        if field_mask is not None: body['field_mask'] = field_mask
        if setting is not None: body['setting'] = setting.as_dict()
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        res = self._api.do('PATCH',
                           '/api/2.0/settings/types/disable_legacy_access/names/default',
                           body=body,
                           headers=headers)
        return DisableLegacyAccess.from_dict(res)


class DisableLegacyDbfsAPI:
    """When this setting is on, access to DBFS root and DBFS mounts is disallowed (as well as creation of new
    mounts). When the setting is off, all DBFS functionality is enabled"""

    def __init__(self, api_client):
        self._api = api_client

    def delete(self, *, etag: Optional[str] = None) -> DeleteDisableLegacyDbfsResponse:
        """Delete the disable legacy DBFS setting.
        
        Deletes the disable legacy DBFS setting for a workspace, reverting back to the default.
        
        :param etag: str (optional)
          etag used for versioning. The response is at least as fresh as the eTag provided. This is used for
          optimistic concurrency control as a way to help prevent simultaneous writes of a setting overwriting
          each other. It is strongly suggested that systems make use of the etag in the read -> delete pattern
          to perform setting deletions in order to avoid race conditions. That is, get an etag from a GET
          request, and pass it with the DELETE request to identify the rule set version you are deleting.
        
        :returns: :class:`DeleteDisableLegacyDbfsResponse`
        """

        query = {}
        if etag is not None: query['etag'] = etag
        headers = {'Accept': 'application/json', }

        res = self._api.do('DELETE',
                           '/api/2.0/settings/types/disable_legacy_dbfs/names/default',
                           query=query,
                           headers=headers)
        return DeleteDisableLegacyDbfsResponse.from_dict(res)

    def get(self, *, etag: Optional[str] = None) -> DisableLegacyDbfs:
        """Get the disable legacy DBFS setting.
        
        Gets the disable legacy DBFS setting.
        
        :param etag: str (optional)
          etag used for versioning. The response is at least as fresh as the eTag provided. This is used for
          optimistic concurrency control as a way to help prevent simultaneous writes of a setting overwriting
          each other. It is strongly suggested that systems make use of the etag in the read -> delete pattern
          to perform setting deletions in order to avoid race conditions. That is, get an etag from a GET
          request, and pass it with the DELETE request to identify the rule set version you are deleting.
        
        :returns: :class:`DisableLegacyDbfs`
        """

        query = {}
        if etag is not None: query['etag'] = etag
        headers = {'Accept': 'application/json', }

        res = self._api.do('GET',
                           '/api/2.0/settings/types/disable_legacy_dbfs/names/default',
                           query=query,
                           headers=headers)
        return DisableLegacyDbfs.from_dict(res)

    def update(self, allow_missing: bool, setting: DisableLegacyDbfs, field_mask: str) -> DisableLegacyDbfs:
        """Update the disable legacy DBFS setting.
        
        Updates the disable legacy DBFS setting for the workspace.
        
        :param allow_missing: bool
          This should always be set to true for Settings API. Added for AIP compliance.
        :param setting: :class:`DisableLegacyDbfs`
        :param field_mask: str
          Field mask is required to be passed into the PATCH request. Field mask specifies which fields of the
          setting payload will be updated. The field mask needs to be supplied as single string. To specify
          multiple fields in the field mask, use comma as the separator (no space).
        
        :returns: :class:`DisableLegacyDbfs`
        """
        body = {}
        if allow_missing is not None: body['allow_missing'] = allow_missing
        if field_mask is not None: body['field_mask'] = field_mask
        if setting is not None: body['setting'] = setting.as_dict()
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        res = self._api.do('PATCH',
                           '/api/2.0/settings/types/disable_legacy_dbfs/names/default',
                           body=body,
                           headers=headers)
        return DisableLegacyDbfs.from_dict(res)


class DisableLegacyFeaturesAPI:
    """Disable legacy features for new Databricks workspaces.
    
    For newly created workspaces: 1. Disables the use of DBFS root and mounts. 2. Hive Metastore will not be
    provisioned. 3. Disables the use of ‘No-isolation clusters’. 4. Disables Databricks Runtime versions
    prior to 13.3LTS."""

    def __init__(self, api_client):
        self._api = api_client

    def delete(self, *, etag: Optional[str] = None) -> DeleteDisableLegacyFeaturesResponse:
        """Delete the disable legacy features setting.
        
        Deletes the disable legacy features setting.
        
        :param etag: str (optional)
          etag used for versioning. The response is at least as fresh as the eTag provided. This is used for
          optimistic concurrency control as a way to help prevent simultaneous writes of a setting overwriting
          each other. It is strongly suggested that systems make use of the etag in the read -> delete pattern
          to perform setting deletions in order to avoid race conditions. That is, get an etag from a GET
          request, and pass it with the DELETE request to identify the rule set version you are deleting.
        
        :returns: :class:`DeleteDisableLegacyFeaturesResponse`
        """

        query = {}
        if etag is not None: query['etag'] = etag
        headers = {'Accept': 'application/json', }

        res = self._api.do(
            'DELETE',
            f'/api/2.0/accounts/{self._api.account_id}/settings/types/disable_legacy_features/names/default',
            query=query,
            headers=headers)
        return DeleteDisableLegacyFeaturesResponse.from_dict(res)

    def get(self, *, etag: Optional[str] = None) -> DisableLegacyFeatures:
        """Get the disable legacy features setting.
        
        Gets the value of the disable legacy features setting.
        
        :param etag: str (optional)
          etag used for versioning. The response is at least as fresh as the eTag provided. This is used for
          optimistic concurrency control as a way to help prevent simultaneous writes of a setting overwriting
          each other. It is strongly suggested that systems make use of the etag in the read -> delete pattern
          to perform setting deletions in order to avoid race conditions. That is, get an etag from a GET
          request, and pass it with the DELETE request to identify the rule set version you are deleting.
        
        :returns: :class:`DisableLegacyFeatures`
        """

        query = {}
        if etag is not None: query['etag'] = etag
        headers = {'Accept': 'application/json', }

        res = self._api.do(
            'GET',
            f'/api/2.0/accounts/{self._api.account_id}/settings/types/disable_legacy_features/names/default',
            query=query,
            headers=headers)
        return DisableLegacyFeatures.from_dict(res)

    def update(self, allow_missing: bool, setting: DisableLegacyFeatures,
               field_mask: str) -> DisableLegacyFeatures:
        """Update the disable legacy features setting.
        
        Updates the value of the disable legacy features setting.
        
        :param allow_missing: bool
          This should always be set to true for Settings API. Added for AIP compliance.
        :param setting: :class:`DisableLegacyFeatures`
        :param field_mask: str
          Field mask is required to be passed into the PATCH request. Field mask specifies which fields of the
          setting payload will be updated. The field mask needs to be supplied as single string. To specify
          multiple fields in the field mask, use comma as the separator (no space).
        
        :returns: :class:`DisableLegacyFeatures`
        """
        body = {}
        if allow_missing is not None: body['allow_missing'] = allow_missing
        if field_mask is not None: body['field_mask'] = field_mask
        if setting is not None: body['setting'] = setting.as_dict()
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        res = self._api.do(
            'PATCH',
            f'/api/2.0/accounts/{self._api.account_id}/settings/types/disable_legacy_features/names/default',
            body=body,
            headers=headers)
        return DisableLegacyFeatures.from_dict(res)


class EnhancedSecurityMonitoringAPI:
    """Controls whether enhanced security monitoring is enabled for the current workspace. If the compliance
    security profile is enabled, this is automatically enabled. By default, it is disabled. However, if the
    compliance security profile is enabled, this is automatically enabled.
    
    If the compliance security profile is disabled, you can enable or disable this setting and it is not
    permanent."""

    def __init__(self, api_client):
        self._api = api_client

    def get(self, *, etag: Optional[str] = None) -> EnhancedSecurityMonitoringSetting:
        """Get the enhanced security monitoring setting.
        
        Gets the enhanced security monitoring setting.
        
        :param etag: str (optional)
          etag used for versioning. The response is at least as fresh as the eTag provided. This is used for
          optimistic concurrency control as a way to help prevent simultaneous writes of a setting overwriting
          each other. It is strongly suggested that systems make use of the etag in the read -> delete pattern
          to perform setting deletions in order to avoid race conditions. That is, get an etag from a GET
          request, and pass it with the DELETE request to identify the rule set version you are deleting.
        
        :returns: :class:`EnhancedSecurityMonitoringSetting`
        """

        query = {}
        if etag is not None: query['etag'] = etag
        headers = {'Accept': 'application/json', }

        res = self._api.do('GET',
                           '/api/2.0/settings/types/shield_esm_enablement_ws_db/names/default',
                           query=query,
                           headers=headers)
        return EnhancedSecurityMonitoringSetting.from_dict(res)

    def update(self, allow_missing: bool, setting: EnhancedSecurityMonitoringSetting,
               field_mask: str) -> EnhancedSecurityMonitoringSetting:
        """Update the enhanced security monitoring setting.
        
        Updates the enhanced security monitoring setting for the workspace. A fresh etag needs to be provided
        in `PATCH` requests (as part of the setting field). The etag can be retrieved by making a `GET`
        request before the `PATCH` request. If the setting is updated concurrently, `PATCH` fails with 409 and
        the request must be retried by using the fresh etag in the 409 response.
        
        :param allow_missing: bool
          This should always be set to true for Settings API. Added for AIP compliance.
        :param setting: :class:`EnhancedSecurityMonitoringSetting`
        :param field_mask: str
          Field mask is required to be passed into the PATCH request. Field mask specifies which fields of the
          setting payload will be updated. The field mask needs to be supplied as single string. To specify
          multiple fields in the field mask, use comma as the separator (no space).
        
        :returns: :class:`EnhancedSecurityMonitoringSetting`
        """
        body = {}
        if allow_missing is not None: body['allow_missing'] = allow_missing
        if field_mask is not None: body['field_mask'] = field_mask
        if setting is not None: body['setting'] = setting.as_dict()
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        res = self._api.do('PATCH',
                           '/api/2.0/settings/types/shield_esm_enablement_ws_db/names/default',
                           body=body,
                           headers=headers)
        return EnhancedSecurityMonitoringSetting.from_dict(res)


class EsmEnablementAccountAPI:
    """The enhanced security monitoring setting at the account level controls whether to enable the feature on
    new workspaces. By default, this account-level setting is disabled for new workspaces. After workspace
    creation, account admins can enable enhanced security monitoring individually for each workspace."""

    def __init__(self, api_client):
        self._api = api_client

    def get(self, *, etag: Optional[str] = None) -> EsmEnablementAccountSetting:
        """Get the enhanced security monitoring setting for new workspaces.
        
        Gets the enhanced security monitoring setting for new workspaces.
        
        :param etag: str (optional)
          etag used for versioning. The response is at least as fresh as the eTag provided. This is used for
          optimistic concurrency control as a way to help prevent simultaneous writes of a setting overwriting
          each other. It is strongly suggested that systems make use of the etag in the read -> delete pattern
          to perform setting deletions in order to avoid race conditions. That is, get an etag from a GET
          request, and pass it with the DELETE request to identify the rule set version you are deleting.
        
        :returns: :class:`EsmEnablementAccountSetting`
        """

        query = {}
        if etag is not None: query['etag'] = etag
        headers = {'Accept': 'application/json', }

        res = self._api.do(
            'GET',
            f'/api/2.0/accounts/{self._api.account_id}/settings/types/shield_esm_enablement_ac/names/default',
            query=query,
            headers=headers)
        return EsmEnablementAccountSetting.from_dict(res)

    def update(self, allow_missing: bool, setting: EsmEnablementAccountSetting,
               field_mask: str) -> EsmEnablementAccountSetting:
        """Update the enhanced security monitoring setting for new workspaces.
        
        Updates the value of the enhanced security monitoring setting for new workspaces.
        
        :param allow_missing: bool
          This should always be set to true for Settings API. Added for AIP compliance.
        :param setting: :class:`EsmEnablementAccountSetting`
        :param field_mask: str
          Field mask is required to be passed into the PATCH request. Field mask specifies which fields of the
          setting payload will be updated. The field mask needs to be supplied as single string. To specify
          multiple fields in the field mask, use comma as the separator (no space).
        
        :returns: :class:`EsmEnablementAccountSetting`
        """
        body = {}
        if allow_missing is not None: body['allow_missing'] = allow_missing
        if field_mask is not None: body['field_mask'] = field_mask
        if setting is not None: body['setting'] = setting.as_dict()
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        res = self._api.do(
            'PATCH',
            f'/api/2.0/accounts/{self._api.account_id}/settings/types/shield_esm_enablement_ac/names/default',
            body=body,
            headers=headers)
        return EsmEnablementAccountSetting.from_dict(res)


class IpAccessListsAPI:
    """IP Access List enables admins to configure IP access lists.
    
    IP access lists affect web application access and REST API access to this workspace only. If the feature
    is disabled for a workspace, all access is allowed for this workspace. There is support for allow lists
    (inclusion) and block lists (exclusion).
    
    When a connection is attempted: 1. **First, all block lists are checked.** If the connection IP address
    matches any block list, the connection is rejected. 2. **If the connection was not rejected by block
    lists**, the IP address is compared with the allow lists.
    
    If there is at least one allow list for the workspace, the connection is allowed only if the IP address
    matches an allow list. If there are no allow lists for the workspace, all IP addresses are allowed.
    
    For all allow lists and block lists combined, the workspace supports a maximum of 1000 IP/CIDR values,
    where one CIDR counts as a single value.
    
    After changes to the IP access list feature, it can take a few minutes for changes to take effect."""

    def __init__(self, api_client):
        self._api = api_client

    def create(self,
               label: str,
               list_type: ListType,
               *,
               ip_addresses: Optional[List[str]] = None) -> CreateIpAccessListResponse:
        """Create access list.
        
        Creates an IP access list for this workspace.
        
        A list can be an allow list or a block list. See the top of this file for a description of how the
        server treats allow lists and block lists at runtime.
        
        When creating or updating an IP access list:
        
        * For all allow lists and block lists combined, the API supports a maximum of 1000 IP/CIDR values,
        where one CIDR counts as a single value. Attempts to exceed that number return error 400 with
        `error_code` value `QUOTA_EXCEEDED`. * If the new list would block the calling user's current IP,
        error 400 is returned with `error_code` value `INVALID_STATE`.
        
        It can take a few minutes for the changes to take effect. **Note**: Your new IP access list has no
        effect until you enable the feature. See :method:workspaceconf/setStatus
        
        :param label: str
          Label for the IP access list. This **cannot** be empty.
        :param list_type: :class:`ListType`
          Type of IP access list. Valid values are as follows and are case-sensitive:
          
          * `ALLOW`: An allow list. Include this IP or range. * `BLOCK`: A block list. Exclude this IP or
          range. IP addresses in the block list are excluded even if they are included in an allow list.
        :param ip_addresses: List[str] (optional)
        
        :returns: :class:`CreateIpAccessListResponse`
        """
        body = {}
        if ip_addresses is not None: body['ip_addresses'] = [v for v in ip_addresses]
        if label is not None: body['label'] = label
        if list_type is not None: body['list_type'] = list_type.value
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        res = self._api.do('POST', '/api/2.0/ip-access-lists', body=body, headers=headers)
        return CreateIpAccessListResponse.from_dict(res)

    def delete(self, ip_access_list_id: str):
        """Delete access list.
        
        Deletes an IP access list, specified by its list ID.
        
        :param ip_access_list_id: str
          The ID for the corresponding IP access list
        
        
        """

        headers = {'Accept': 'application/json', }

        self._api.do('DELETE', f'/api/2.0/ip-access-lists/{ip_access_list_id}', headers=headers)

    def get(self, ip_access_list_id: str) -> FetchIpAccessListResponse:
        """Get access list.
        
        Gets an IP access list, specified by its list ID.
        
        :param ip_access_list_id: str
          The ID for the corresponding IP access list
        
        :returns: :class:`FetchIpAccessListResponse`
        """

        headers = {'Accept': 'application/json', }

        res = self._api.do('GET', f'/api/2.0/ip-access-lists/{ip_access_list_id}', headers=headers)
        return FetchIpAccessListResponse.from_dict(res)

    def list(self) -> Iterator[IpAccessListInfo]:
        """Get access lists.
        
        Gets all IP access lists for the specified workspace.
        
        :returns: Iterator over :class:`IpAccessListInfo`
        """

        headers = {'Accept': 'application/json', }

        json = self._api.do('GET', '/api/2.0/ip-access-lists', headers=headers)
        parsed = ListIpAccessListResponse.from_dict(json).ip_access_lists
        return parsed if parsed is not None else []

    def replace(self,
                ip_access_list_id: str,
                label: str,
                list_type: ListType,
                enabled: bool,
                *,
                ip_addresses: Optional[List[str]] = None):
        """Replace access list.
        
        Replaces an IP access list, specified by its ID.
        
        A list can include allow lists and block lists. See the top of this file for a description of how the
        server treats allow lists and block lists at run time. When replacing an IP access list: * For all
        allow lists and block lists combined, the API supports a maximum of 1000 IP/CIDR values, where one
        CIDR counts as a single value. Attempts to exceed that number return error 400 with `error_code` value
        `QUOTA_EXCEEDED`. * If the resulting list would block the calling user's current IP, error 400 is
        returned with `error_code` value `INVALID_STATE`. It can take a few minutes for the changes to take
        effect. Note that your resulting IP access list has no effect until you enable the feature. See
        :method:workspaceconf/setStatus.
        
        :param ip_access_list_id: str
          The ID for the corresponding IP access list
        :param label: str
          Label for the IP access list. This **cannot** be empty.
        :param list_type: :class:`ListType`
          Type of IP access list. Valid values are as follows and are case-sensitive:
          
          * `ALLOW`: An allow list. Include this IP or range. * `BLOCK`: A block list. Exclude this IP or
          range. IP addresses in the block list are excluded even if they are included in an allow list.
        :param enabled: bool
          Specifies whether this IP access list is enabled.
        :param ip_addresses: List[str] (optional)
        
        
        """
        body = {}
        if enabled is not None: body['enabled'] = enabled
        if ip_addresses is not None: body['ip_addresses'] = [v for v in ip_addresses]
        if label is not None: body['label'] = label
        if list_type is not None: body['list_type'] = list_type.value
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        self._api.do('PUT', f'/api/2.0/ip-access-lists/{ip_access_list_id}', body=body, headers=headers)

    def update(self,
               ip_access_list_id: str,
               *,
               enabled: Optional[bool] = None,
               ip_addresses: Optional[List[str]] = None,
               label: Optional[str] = None,
               list_type: Optional[ListType] = None):
        """Update access list.
        
        Updates an existing IP access list, specified by its ID.
        
        A list can include allow lists and block lists. See the top of this file for a description of how the
        server treats allow lists and block lists at run time.
        
        When updating an IP access list:
        
        * For all allow lists and block lists combined, the API supports a maximum of 1000 IP/CIDR values,
        where one CIDR counts as a single value. Attempts to exceed that number return error 400 with
        `error_code` value `QUOTA_EXCEEDED`. * If the updated list would block the calling user's current IP,
        error 400 is returned with `error_code` value `INVALID_STATE`.
        
        It can take a few minutes for the changes to take effect. Note that your resulting IP access list has
        no effect until you enable the feature. See :method:workspaceconf/setStatus.
        
        :param ip_access_list_id: str
          The ID for the corresponding IP access list
        :param enabled: bool (optional)
          Specifies whether this IP access list is enabled.
        :param ip_addresses: List[str] (optional)
        :param label: str (optional)
          Label for the IP access list. This **cannot** be empty.
        :param list_type: :class:`ListType` (optional)
          Type of IP access list. Valid values are as follows and are case-sensitive:
          
          * `ALLOW`: An allow list. Include this IP or range. * `BLOCK`: A block list. Exclude this IP or
          range. IP addresses in the block list are excluded even if they are included in an allow list.
        
        
        """
        body = {}
        if enabled is not None: body['enabled'] = enabled
        if ip_addresses is not None: body['ip_addresses'] = [v for v in ip_addresses]
        if label is not None: body['label'] = label
        if list_type is not None: body['list_type'] = list_type.value
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        self._api.do('PATCH', f'/api/2.0/ip-access-lists/{ip_access_list_id}', body=body, headers=headers)


class NetworkConnectivityAPI:
    """These APIs provide configurations for the network connectivity of your workspaces for serverless compute
    resources."""

    def __init__(self, api_client):
        self._api = api_client

    def create_network_connectivity_configuration(self, name: str,
                                                  region: str) -> NetworkConnectivityConfiguration:
        """Create a network connectivity configuration.
        
        :param name: str
          The name of the network connectivity configuration. The name can contain alphanumeric characters,
          hyphens, and underscores. The length must be between 3 and 30 characters. The name must match the
          regular expression `^[0-9a-zA-Z-_]{3,30}$`.
        :param region: str
          The region for the network connectivity configuration. Only workspaces in the same region can be
          attached to the network connectivity configuration.
        
        :returns: :class:`NetworkConnectivityConfiguration`
        """
        body = {}
        if name is not None: body['name'] = name
        if region is not None: body['region'] = region
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        res = self._api.do('POST',
                           f'/api/2.0/accounts/{self._api.account_id}/network-connectivity-configs',
                           body=body,
                           headers=headers)
        return NetworkConnectivityConfiguration.from_dict(res)

    def create_private_endpoint_rule(
            self, network_connectivity_config_id: str, resource_id: str,
            group_id: CreatePrivateEndpointRuleRequestGroupId) -> NccAzurePrivateEndpointRule:
        """Create a private endpoint rule.
        
        Create a private endpoint rule for the specified network connectivity config object. Once the object
        is created, Databricks asynchronously provisions a new Azure private endpoint to your specified Azure
        resource.
        
        **IMPORTANT**: You must use Azure portal or other Azure tools to approve the private endpoint to
        complete the connection. To get the information of the private endpoint created, make a `GET` request
        on the new private endpoint rule. See [serverless private link].
        
        [serverless private link]: https://learn.microsoft.com/azure/databricks/security/network/serverless-network-security/serverless-private-link
        
        :param network_connectivity_config_id: str
          Your Network Connectvity Configuration ID.
        :param resource_id: str
          The Azure resource ID of the target resource.
        :param group_id: :class:`CreatePrivateEndpointRuleRequestGroupId`
          The sub-resource type (group ID) of the target resource. Note that to connect to workspace root
          storage (root DBFS), you need two endpoints, one for `blob` and one for `dfs`.
        
        :returns: :class:`NccAzurePrivateEndpointRule`
        """
        body = {}
        if group_id is not None: body['group_id'] = group_id.value
        if resource_id is not None: body['resource_id'] = resource_id
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        res = self._api.do(
            'POST',
            f'/api/2.0/accounts/{self._api.account_id}/network-connectivity-configs/{network_connectivity_config_id}/private-endpoint-rules',
            body=body,
            headers=headers)
        return NccAzurePrivateEndpointRule.from_dict(res)

    def delete_network_connectivity_configuration(self, network_connectivity_config_id: str):
        """Delete a network connectivity configuration.
        
        Deletes a network connectivity configuration.
        
        :param network_connectivity_config_id: str
          Your Network Connectvity Configuration ID.
        
        
        """

        headers = {'Accept': 'application/json', }

        self._api.do(
            'DELETE',
            f'/api/2.0/accounts/{self._api.account_id}/network-connectivity-configs/{network_connectivity_config_id}',
            headers=headers)

    def delete_private_endpoint_rule(self, network_connectivity_config_id: str,
                                     private_endpoint_rule_id: str) -> NccAzurePrivateEndpointRule:
        """Delete a private endpoint rule.
        
        Initiates deleting a private endpoint rule. If the connection state is PENDING or EXPIRED, the private
        endpoint is immediately deleted. Otherwise, the private endpoint is deactivated and will be deleted
        after seven days of deactivation. When a private endpoint is deactivated, the `deactivated` field is
        set to `true` and the private endpoint is not available to your serverless compute resources.
        
        :param network_connectivity_config_id: str
          Your Network Connectvity Configuration ID.
        :param private_endpoint_rule_id: str
          Your private endpoint rule ID.
        
        :returns: :class:`NccAzurePrivateEndpointRule`
        """

        headers = {'Accept': 'application/json', }

        res = self._api.do(
            'DELETE',
            f'/api/2.0/accounts/{self._api.account_id}/network-connectivity-configs/{network_connectivity_config_id}/private-endpoint-rules/{private_endpoint_rule_id}',
            headers=headers)
        return NccAzurePrivateEndpointRule.from_dict(res)

    def get_network_connectivity_configuration(
            self, network_connectivity_config_id: str) -> NetworkConnectivityConfiguration:
        """Get a network connectivity configuration.
        
        Gets a network connectivity configuration.
        
        :param network_connectivity_config_id: str
          Your Network Connectvity Configuration ID.
        
        :returns: :class:`NetworkConnectivityConfiguration`
        """

        headers = {'Accept': 'application/json', }

        res = self._api.do(
            'GET',
            f'/api/2.0/accounts/{self._api.account_id}/network-connectivity-configs/{network_connectivity_config_id}',
            headers=headers)
        return NetworkConnectivityConfiguration.from_dict(res)

    def get_private_endpoint_rule(self, network_connectivity_config_id: str,
                                  private_endpoint_rule_id: str) -> NccAzurePrivateEndpointRule:
        """Get a private endpoint rule.
        
        Gets the private endpoint rule.
        
        :param network_connectivity_config_id: str
          Your Network Connectvity Configuration ID.
        :param private_endpoint_rule_id: str
          Your private endpoint rule ID.
        
        :returns: :class:`NccAzurePrivateEndpointRule`
        """

        headers = {'Accept': 'application/json', }

        res = self._api.do(
            'GET',
            f'/api/2.0/accounts/{self._api.account_id}/network-connectivity-configs/{network_connectivity_config_id}/private-endpoint-rules/{private_endpoint_rule_id}',
            headers=headers)
        return NccAzurePrivateEndpointRule.from_dict(res)

    def list_network_connectivity_configurations(self,
                                                 *,
                                                 page_token: Optional[str] = None
                                                 ) -> Iterator[NetworkConnectivityConfiguration]:
        """List network connectivity configurations.
        
        Gets an array of network connectivity configurations.
        
        :param page_token: str (optional)
          Pagination token to go to next page based on previous query.
        
        :returns: Iterator over :class:`NetworkConnectivityConfiguration`
        """

        query = {}
        if page_token is not None: query['page_token'] = page_token
        headers = {'Accept': 'application/json', }

        while True:
            json = self._api.do('GET',
                                f'/api/2.0/accounts/{self._api.account_id}/network-connectivity-configs',
                                query=query,
                                headers=headers)
            if 'items' in json:
                for v in json['items']:
                    yield NetworkConnectivityConfiguration.from_dict(v)
            if 'next_page_token' not in json or not json['next_page_token']:
                return
            query['page_token'] = json['next_page_token']

    def list_private_endpoint_rules(
            self,
            network_connectivity_config_id: str,
            *,
            page_token: Optional[str] = None) -> Iterator[NccAzurePrivateEndpointRule]:
        """List private endpoint rules.
        
        Gets an array of private endpoint rules.
        
        :param network_connectivity_config_id: str
          Your Network Connectvity Configuration ID.
        :param page_token: str (optional)
          Pagination token to go to next page based on previous query.
        
        :returns: Iterator over :class:`NccAzurePrivateEndpointRule`
        """

        query = {}
        if page_token is not None: query['page_token'] = page_token
        headers = {'Accept': 'application/json', }

        while True:
            json = self._api.do(
                'GET',
                f'/api/2.0/accounts/{self._api.account_id}/network-connectivity-configs/{network_connectivity_config_id}/private-endpoint-rules',
                query=query,
                headers=headers)
            if 'items' in json:
                for v in json['items']:
                    yield NccAzurePrivateEndpointRule.from_dict(v)
            if 'next_page_token' not in json or not json['next_page_token']:
                return
            query['page_token'] = json['next_page_token']


class NotificationDestinationsAPI:
    """The notification destinations API lets you programmatically manage a workspace's notification
    destinations. Notification destinations are used to send notifications for query alerts and jobs to
    destinations outside of Databricks. Only workspace admins can create, update, and delete notification
    destinations."""

    def __init__(self, api_client):
        self._api = api_client

    def create(self,
               *,
               config: Optional[Config] = None,
               display_name: Optional[str] = None) -> NotificationDestination:
        """Create a notification destination.
        
        Creates a notification destination. Requires workspace admin permissions.
        
        :param config: :class:`Config` (optional)
          The configuration for the notification destination. Must wrap EXACTLY one of the nested configs.
        :param display_name: str (optional)
          The display name for the notification destination.
        
        :returns: :class:`NotificationDestination`
        """
        body = {}
        if config is not None: body['config'] = config.as_dict()
        if display_name is not None: body['display_name'] = display_name
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        res = self._api.do('POST', '/api/2.0/notification-destinations', body=body, headers=headers)
        return NotificationDestination.from_dict(res)

    def delete(self, id: str):
        """Delete a notification destination.
        
        Deletes a notification destination. Requires workspace admin permissions.
        
        :param id: str
        
        
        """

        headers = {'Accept': 'application/json', }

        self._api.do('DELETE', f'/api/2.0/notification-destinations/{id}', headers=headers)

    def get(self, id: str) -> NotificationDestination:
        """Get a notification destination.
        
        Gets a notification destination.
        
        :param id: str
        
        :returns: :class:`NotificationDestination`
        """

        headers = {'Accept': 'application/json', }

        res = self._api.do('GET', f'/api/2.0/notification-destinations/{id}', headers=headers)
        return NotificationDestination.from_dict(res)

    def list(self,
             *,
             page_size: Optional[int] = None,
             page_token: Optional[str] = None) -> Iterator[ListNotificationDestinationsResult]:
        """List notification destinations.
        
        Lists notification destinations.
        
        :param page_size: int (optional)
        :param page_token: str (optional)
        
        :returns: Iterator over :class:`ListNotificationDestinationsResult`
        """

        query = {}
        if page_size is not None: query['page_size'] = page_size
        if page_token is not None: query['page_token'] = page_token
        headers = {'Accept': 'application/json', }

        while True:
            json = self._api.do('GET', '/api/2.0/notification-destinations', query=query, headers=headers)
            if 'results' in json:
                for v in json['results']:
                    yield ListNotificationDestinationsResult.from_dict(v)
            if 'next_page_token' not in json or not json['next_page_token']:
                return
            query['page_token'] = json['next_page_token']

    def update(self,
               id: str,
               *,
               config: Optional[Config] = None,
               display_name: Optional[str] = None) -> NotificationDestination:
        """Update a notification destination.
        
        Updates a notification destination. Requires workspace admin permissions. At least one field is
        required in the request body.
        
        :param id: str
        :param config: :class:`Config` (optional)
          The configuration for the notification destination. Must wrap EXACTLY one of the nested configs.
        :param display_name: str (optional)
          The display name for the notification destination.
        
        :returns: :class:`NotificationDestination`
        """
        body = {}
        if config is not None: body['config'] = config.as_dict()
        if display_name is not None: body['display_name'] = display_name
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        res = self._api.do('PATCH', f'/api/2.0/notification-destinations/{id}', body=body, headers=headers)
        return NotificationDestination.from_dict(res)


class PersonalComputeAPI:
    """The Personal Compute enablement setting lets you control which users can use the Personal Compute default
    policy to create compute resources. By default all users in all workspaces have access (ON), but you can
    change the setting to instead let individual workspaces configure access control (DELEGATE).
    
    There is only one instance of this setting per account. Since this setting has a default value, this
    setting is present on all accounts even though it's never set on a given account. Deletion reverts the
    value of the setting back to the default value."""

    def __init__(self, api_client):
        self._api = api_client

    def delete(self, *, etag: Optional[str] = None) -> DeletePersonalComputeSettingResponse:
        """Delete Personal Compute setting.
        
        Reverts back the Personal Compute setting value to default (ON)
        
        :param etag: str (optional)
          etag used for versioning. The response is at least as fresh as the eTag provided. This is used for
          optimistic concurrency control as a way to help prevent simultaneous writes of a setting overwriting
          each other. It is strongly suggested that systems make use of the etag in the read -> delete pattern
          to perform setting deletions in order to avoid race conditions. That is, get an etag from a GET
          request, and pass it with the DELETE request to identify the rule set version you are deleting.
        
        :returns: :class:`DeletePersonalComputeSettingResponse`
        """

        query = {}
        if etag is not None: query['etag'] = etag
        headers = {'Accept': 'application/json', }

        res = self._api.do(
            'DELETE',
            f'/api/2.0/accounts/{self._api.account_id}/settings/types/dcp_acct_enable/names/default',
            query=query,
            headers=headers)
        return DeletePersonalComputeSettingResponse.from_dict(res)

    def get(self, *, etag: Optional[str] = None) -> PersonalComputeSetting:
        """Get Personal Compute setting.
        
        Gets the value of the Personal Compute setting.
        
        :param etag: str (optional)
          etag used for versioning. The response is at least as fresh as the eTag provided. This is used for
          optimistic concurrency control as a way to help prevent simultaneous writes of a setting overwriting
          each other. It is strongly suggested that systems make use of the etag in the read -> delete pattern
          to perform setting deletions in order to avoid race conditions. That is, get an etag from a GET
          request, and pass it with the DELETE request to identify the rule set version you are deleting.
        
        :returns: :class:`PersonalComputeSetting`
        """

        query = {}
        if etag is not None: query['etag'] = etag
        headers = {'Accept': 'application/json', }

        res = self._api.do(
            'GET',
            f'/api/2.0/accounts/{self._api.account_id}/settings/types/dcp_acct_enable/names/default',
            query=query,
            headers=headers)
        return PersonalComputeSetting.from_dict(res)

    def update(self, allow_missing: bool, setting: PersonalComputeSetting,
               field_mask: str) -> PersonalComputeSetting:
        """Update Personal Compute setting.
        
        Updates the value of the Personal Compute setting.
        
        :param allow_missing: bool
          This should always be set to true for Settings API. Added for AIP compliance.
        :param setting: :class:`PersonalComputeSetting`
        :param field_mask: str
          Field mask is required to be passed into the PATCH request. Field mask specifies which fields of the
          setting payload will be updated. The field mask needs to be supplied as single string. To specify
          multiple fields in the field mask, use comma as the separator (no space).
        
        :returns: :class:`PersonalComputeSetting`
        """
        body = {}
        if allow_missing is not None: body['allow_missing'] = allow_missing
        if field_mask is not None: body['field_mask'] = field_mask
        if setting is not None: body['setting'] = setting.as_dict()
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        res = self._api.do(
            'PATCH',
            f'/api/2.0/accounts/{self._api.account_id}/settings/types/dcp_acct_enable/names/default',
            body=body,
            headers=headers)
        return PersonalComputeSetting.from_dict(res)


class RestrictWorkspaceAdminsAPI:
    """The Restrict Workspace Admins setting lets you control the capabilities of workspace admins. With the
    setting status set to ALLOW_ALL, workspace admins can create service principal personal access tokens on
    behalf of any service principal in their workspace. Workspace admins can also change a job owner to any
    user in their workspace. And they can change the job run_as setting to any user in their workspace or to a
    service principal on which they have the Service Principal User role. With the setting status set to
    RESTRICT_TOKENS_AND_JOB_RUN_AS, workspace admins can only create personal access tokens on behalf of
    service principals they have the Service Principal User role on. They can also only change a job owner to
    themselves. And they can change the job run_as setting to themselves or to a service principal on which
    they have the Service Principal User role."""

    def __init__(self, api_client):
        self._api = api_client

    def delete(self, *, etag: Optional[str] = None) -> DeleteRestrictWorkspaceAdminsSettingResponse:
        """Delete the restrict workspace admins setting.
        
        Reverts the restrict workspace admins setting status for the workspace. A fresh etag needs to be
        provided in `DELETE` requests (as a query parameter). The etag can be retrieved by making a `GET`
        request before the DELETE request. If the setting is updated/deleted concurrently, `DELETE` fails with
        409 and the request must be retried by using the fresh etag in the 409 response.
        
        :param etag: str (optional)
          etag used for versioning. The response is at least as fresh as the eTag provided. This is used for
          optimistic concurrency control as a way to help prevent simultaneous writes of a setting overwriting
          each other. It is strongly suggested that systems make use of the etag in the read -> delete pattern
          to perform setting deletions in order to avoid race conditions. That is, get an etag from a GET
          request, and pass it with the DELETE request to identify the rule set version you are deleting.
        
        :returns: :class:`DeleteRestrictWorkspaceAdminsSettingResponse`
        """

        query = {}
        if etag is not None: query['etag'] = etag
        headers = {'Accept': 'application/json', }

        res = self._api.do('DELETE',
                           '/api/2.0/settings/types/restrict_workspace_admins/names/default',
                           query=query,
                           headers=headers)
        return DeleteRestrictWorkspaceAdminsSettingResponse.from_dict(res)

    def get(self, *, etag: Optional[str] = None) -> RestrictWorkspaceAdminsSetting:
        """Get the restrict workspace admins setting.
        
        Gets the restrict workspace admins setting.
        
        :param etag: str (optional)
          etag used for versioning. The response is at least as fresh as the eTag provided. This is used for
          optimistic concurrency control as a way to help prevent simultaneous writes of a setting overwriting
          each other. It is strongly suggested that systems make use of the etag in the read -> delete pattern
          to perform setting deletions in order to avoid race conditions. That is, get an etag from a GET
          request, and pass it with the DELETE request to identify the rule set version you are deleting.
        
        :returns: :class:`RestrictWorkspaceAdminsSetting`
        """

        query = {}
        if etag is not None: query['etag'] = etag
        headers = {'Accept': 'application/json', }

        res = self._api.do('GET',
                           '/api/2.0/settings/types/restrict_workspace_admins/names/default',
                           query=query,
                           headers=headers)
        return RestrictWorkspaceAdminsSetting.from_dict(res)

    def update(self, allow_missing: bool, setting: RestrictWorkspaceAdminsSetting,
               field_mask: str) -> RestrictWorkspaceAdminsSetting:
        """Update the restrict workspace admins setting.
        
        Updates the restrict workspace admins setting for the workspace. A fresh etag needs to be provided in
        `PATCH` requests (as part of the setting field). The etag can be retrieved by making a GET request
        before the `PATCH` request. If the setting is updated concurrently, `PATCH` fails with 409 and the
        request must be retried by using the fresh etag in the 409 response.
        
        :param allow_missing: bool
          This should always be set to true for Settings API. Added for AIP compliance.
        :param setting: :class:`RestrictWorkspaceAdminsSetting`
        :param field_mask: str
          Field mask is required to be passed into the PATCH request. Field mask specifies which fields of the
          setting payload will be updated. The field mask needs to be supplied as single string. To specify
          multiple fields in the field mask, use comma as the separator (no space).
        
        :returns: :class:`RestrictWorkspaceAdminsSetting`
        """
        body = {}
        if allow_missing is not None: body['allow_missing'] = allow_missing
        if field_mask is not None: body['field_mask'] = field_mask
        if setting is not None: body['setting'] = setting.as_dict()
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        res = self._api.do('PATCH',
                           '/api/2.0/settings/types/restrict_workspace_admins/names/default',
                           body=body,
                           headers=headers)
        return RestrictWorkspaceAdminsSetting.from_dict(res)


class SettingsAPI:
    """Workspace Settings API allows users to manage settings at the workspace level."""

    def __init__(self, api_client):
        self._api = api_client

        self._automatic_cluster_update = AutomaticClusterUpdateAPI(self._api)
        self._compliance_security_profile = ComplianceSecurityProfileAPI(self._api)
        self._default_namespace = DefaultNamespaceAPI(self._api)
        self._disable_legacy_access = DisableLegacyAccessAPI(self._api)
        self._disable_legacy_dbfs = DisableLegacyDbfsAPI(self._api)
        self._enhanced_security_monitoring = EnhancedSecurityMonitoringAPI(self._api)
        self._restrict_workspace_admins = RestrictWorkspaceAdminsAPI(self._api)

    @property
    def automatic_cluster_update(self) -> AutomaticClusterUpdateAPI:
        """Controls whether automatic cluster update is enabled for the current workspace."""
        return self._automatic_cluster_update

    @property
    def compliance_security_profile(self) -> ComplianceSecurityProfileAPI:
        """Controls whether to enable the compliance security profile for the current workspace."""
        return self._compliance_security_profile

    @property
    def default_namespace(self) -> DefaultNamespaceAPI:
        """The default namespace setting API allows users to configure the default namespace for a Databricks workspace."""
        return self._default_namespace

    @property
    def disable_legacy_access(self) -> DisableLegacyAccessAPI:
        """'Disabling legacy access' has the following impacts: 1."""
        return self._disable_legacy_access

    @property
    def disable_legacy_dbfs(self) -> DisableLegacyDbfsAPI:
        """When this setting is on, access to DBFS root and DBFS mounts is disallowed (as well as creation of new mounts)."""
        return self._disable_legacy_dbfs

    @property
    def enhanced_security_monitoring(self) -> EnhancedSecurityMonitoringAPI:
        """Controls whether enhanced security monitoring is enabled for the current workspace."""
        return self._enhanced_security_monitoring

    @property
    def restrict_workspace_admins(self) -> RestrictWorkspaceAdminsAPI:
        """The Restrict Workspace Admins setting lets you control the capabilities of workspace admins."""
        return self._restrict_workspace_admins


class TokenManagementAPI:
    """Enables administrators to get all tokens and delete tokens for other users. Admins can either get every
    token, get a specific token by ID, or get all tokens for a particular user."""

    def __init__(self, api_client):
        self._api = api_client

    def create_obo_token(self,
                         application_id: str,
                         *,
                         comment: Optional[str] = None,
                         lifetime_seconds: Optional[int] = None) -> CreateOboTokenResponse:
        """Create on-behalf token.
        
        Creates a token on behalf of a service principal.
        
        :param application_id: str
          Application ID of the service principal.
        :param comment: str (optional)
          Comment that describes the purpose of the token.
        :param lifetime_seconds: int (optional)
          The number of seconds before the token expires.
        
        :returns: :class:`CreateOboTokenResponse`
        """
        body = {}
        if application_id is not None: body['application_id'] = application_id
        if comment is not None: body['comment'] = comment
        if lifetime_seconds is not None: body['lifetime_seconds'] = lifetime_seconds
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        res = self._api.do('POST',
                           '/api/2.0/token-management/on-behalf-of/tokens',
                           body=body,
                           headers=headers)
        return CreateOboTokenResponse.from_dict(res)

    def delete(self, token_id: str):
        """Delete a token.
        
        Deletes a token, specified by its ID.
        
        :param token_id: str
          The ID of the token to get.
        
        
        """

        headers = {'Accept': 'application/json', }

        self._api.do('DELETE', f'/api/2.0/token-management/tokens/{token_id}', headers=headers)

    def get(self, token_id: str) -> GetTokenResponse:
        """Get token info.
        
        Gets information about a token, specified by its ID.
        
        :param token_id: str
          The ID of the token to get.
        
        :returns: :class:`GetTokenResponse`
        """

        headers = {'Accept': 'application/json', }

        res = self._api.do('GET', f'/api/2.0/token-management/tokens/{token_id}', headers=headers)
        return GetTokenResponse.from_dict(res)

    def get_permission_levels(self) -> GetTokenPermissionLevelsResponse:
        """Get token permission levels.
        
        Gets the permission levels that a user can have on an object.
        
        :returns: :class:`GetTokenPermissionLevelsResponse`
        """

        headers = {'Accept': 'application/json', }

        res = self._api.do('GET',
                           '/api/2.0/permissions/authorization/tokens/permissionLevels',
                           headers=headers)
        return GetTokenPermissionLevelsResponse.from_dict(res)

    def get_permissions(self) -> TokenPermissions:
        """Get token permissions.
        
        Gets the permissions of all tokens. Tokens can inherit permissions from their root object.
        
        :returns: :class:`TokenPermissions`
        """

        headers = {'Accept': 'application/json', }

        res = self._api.do('GET', '/api/2.0/permissions/authorization/tokens', headers=headers)
        return TokenPermissions.from_dict(res)

    def list(self,
             *,
             created_by_id: Optional[int] = None,
             created_by_username: Optional[str] = None) -> Iterator[TokenInfo]:
        """List all tokens.
        
        Lists all tokens associated with the specified workspace or user.
        
        :param created_by_id: int (optional)
          User ID of the user that created the token.
        :param created_by_username: str (optional)
          Username of the user that created the token.
        
        :returns: Iterator over :class:`TokenInfo`
        """

        query = {}
        if created_by_id is not None: query['created_by_id'] = created_by_id
        if created_by_username is not None: query['created_by_username'] = created_by_username
        headers = {'Accept': 'application/json', }

        json = self._api.do('GET', '/api/2.0/token-management/tokens', query=query, headers=headers)
        parsed = ListTokensResponse.from_dict(json).token_infos
        return parsed if parsed is not None else []

    def set_permissions(
            self,
            *,
            access_control_list: Optional[List[TokenAccessControlRequest]] = None) -> TokenPermissions:
        """Set token permissions.
        
        Sets permissions on all tokens. Tokens can inherit permissions from their root object.
        
        :param access_control_list: List[:class:`TokenAccessControlRequest`] (optional)
        
        :returns: :class:`TokenPermissions`
        """
        body = {}
        if access_control_list is not None:
            body['access_control_list'] = [v.as_dict() for v in access_control_list]
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        res = self._api.do('PUT', '/api/2.0/permissions/authorization/tokens', body=body, headers=headers)
        return TokenPermissions.from_dict(res)

    def update_permissions(
            self,
            *,
            access_control_list: Optional[List[TokenAccessControlRequest]] = None) -> TokenPermissions:
        """Update token permissions.
        
        Updates the permissions on all tokens. Tokens can inherit permissions from their root object.
        
        :param access_control_list: List[:class:`TokenAccessControlRequest`] (optional)
        
        :returns: :class:`TokenPermissions`
        """
        body = {}
        if access_control_list is not None:
            body['access_control_list'] = [v.as_dict() for v in access_control_list]
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        res = self._api.do('PATCH', '/api/2.0/permissions/authorization/tokens', body=body, headers=headers)
        return TokenPermissions.from_dict(res)


class TokensAPI:
    """The Token API allows you to create, list, and revoke tokens that can be used to authenticate and access
    Databricks REST APIs."""

    def __init__(self, api_client):
        self._api = api_client

    def create(self,
               *,
               comment: Optional[str] = None,
               lifetime_seconds: Optional[int] = None) -> CreateTokenResponse:
        """Create a user token.
        
        Creates and returns a token for a user. If this call is made through token authentication, it creates
        a token with the same client ID as the authenticated token. If the user's token quota is exceeded,
        this call returns an error **QUOTA_EXCEEDED**.
        
        :param comment: str (optional)
          Optional description to attach to the token.
        :param lifetime_seconds: int (optional)
          The lifetime of the token, in seconds.
          
          If the lifetime is not specified, this token remains valid indefinitely.
        
        :returns: :class:`CreateTokenResponse`
        """
        body = {}
        if comment is not None: body['comment'] = comment
        if lifetime_seconds is not None: body['lifetime_seconds'] = lifetime_seconds
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        res = self._api.do('POST', '/api/2.0/token/create', body=body, headers=headers)
        return CreateTokenResponse.from_dict(res)

    def delete(self, token_id: str):
        """Revoke token.
        
        Revokes an access token.
        
        If a token with the specified ID is not valid, this call returns an error **RESOURCE_DOES_NOT_EXIST**.
        
        :param token_id: str
          The ID of the token to be revoked.
        
        
        """
        body = {}
        if token_id is not None: body['token_id'] = token_id
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        self._api.do('POST', '/api/2.0/token/delete', body=body, headers=headers)

    def list(self) -> Iterator[PublicTokenInfo]:
        """List tokens.
        
        Lists all the valid tokens for a user-workspace pair.
        
        :returns: Iterator over :class:`PublicTokenInfo`
        """

        headers = {'Accept': 'application/json', }

        json = self._api.do('GET', '/api/2.0/token/list', headers=headers)
        parsed = ListPublicTokensResponse.from_dict(json).token_infos
        return parsed if parsed is not None else []


class WorkspaceConfAPI:
    """This API allows updating known workspace settings for advanced users."""

    def __init__(self, api_client):
        self._api = api_client

    def get_status(self, keys: str) -> WorkspaceConf:
        """Check configuration status.
        
        Gets the configuration status for a workspace.
        
        :param keys: str
        
        :returns: Dict[str,str]
        """

        query = {}
        if keys is not None: query['keys'] = keys
        headers = {'Accept': 'application/json', }

        res = self._api.do('GET', '/api/2.0/workspace-conf', query=query, headers=headers)
        return res

    def set_status(self, contents: Dict[str, str]):
        """Enable/disable features.
        
        Sets the configuration status for a workspace, including enabling or disabling it.
        
        
        
        """

        headers = {'Content-Type': 'application/json', }

        self._api.do('PATCH', '/api/2.0/workspace-conf', body=contents, headers=headers)
