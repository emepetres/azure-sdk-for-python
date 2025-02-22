# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class ActionType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Enum. Indicates the action type. "Internal" refers to actions that are for internal only APIs."""

    INTERNAL = "Internal"


class AutonomousDatabaseBackupLifecycleState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """AutonomousDatabaseBackupLifecycleState enum."""

    CREATING = "Creating"
    ACTIVE = "Active"
    DELETING = "Deleting"
    FAILED = "Failed"
    UPDATING = "Updating"


class AutonomousDatabaseBackupType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """AutonomousDatabaseBackupType enum."""

    INCREMENTAL = "Incremental"
    FULL = "Full"
    LONG_TERM = "LongTerm"


class AutonomousDatabaseLifecycleState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """AutonomousDatabaseLifecycleState enum."""

    PROVISIONING = "Provisioning"
    """PROVISIONING value"""
    AVAILABLE = "Available"
    """AVAILABLE value"""
    STOPPING = "Stopping"
    """STOPPING value"""
    STOPPED = "Stopped"
    """STOPPED value"""
    STARTING = "Starting"
    """STARTING value"""
    TERMINATING = "Terminating"
    """TERMINATING value"""
    TERMINATED = "Terminated"
    """TERMINATED value"""
    UNAVAILABLE = "Unavailable"
    """UNAVAILABLE value"""
    RESTORE_IN_PROGRESS = "RestoreInProgress"
    """RESTORE_IN_PROGRESS value"""
    RESTORE_FAILED = "RestoreFailed"
    """RESTORE_FAILED value"""
    BACKUP_IN_PROGRESS = "BackupInProgress"
    """BACKUP_IN_PROGRESS value"""
    SCALE_IN_PROGRESS = "ScaleInProgress"
    """SCALE_IN_PROGRESS value"""
    AVAILABLE_NEEDS_ATTENTION = "AvailableNeedsAttention"
    """AVAILABLE_NEEDS_ATTENTION value"""
    UPDATING = "Updating"
    """UPDATING value"""
    MAINTENANCE_IN_PROGRESS = "MaintenanceInProgress"
    """MAINTENANCE_IN_PROGRESS value"""
    RESTARTING = "Restarting"
    """RESTARTING value"""
    RECREATING = "Recreating"
    """RECREATING value"""
    ROLE_CHANGE_IN_PROGRESS = "RoleChangeInProgress"
    """ROLE_CHANGE_IN_PROGRESS value"""
    UPGRADING = "Upgrading"
    """UPGRADING value"""
    INACCESSIBLE = "Inaccessible"
    """INACCESSIBLE value"""
    STANDBY = "Standby"
    """STANDBY value"""


class AutonomousMaintenanceScheduleType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """AutonomousMaintenanceScheduleType enum."""

    EARLY = "Early"
    """EARLY value"""
    REGULAR = "Regular"
    """REGULAR value"""


class AzureResourceProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Azure Resource Provisioning State enum."""

    SUCCEEDED = "Succeeded"
    """Resource has been created."""
    FAILED = "Failed"
    """Resource creation failed."""
    CANCELED = "Canceled"
    """Resource creation was canceled."""
    PROVISIONING = "Provisioning"
    """Provisioning value"""


class CloneType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """CloneType enum."""

    FULL = "Full"
    """FULL value"""
    METADATA = "Metadata"
    """METADATA value"""


class CloudAccountProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """CloudAccountProvisioningState enum."""

    PENDING = "Pending"
    """Pending value"""
    PROVISIONING = "Provisioning"
    """Provisioning value"""
    AVAILABLE = "Available"
    """Available value"""


class CloudExadataInfrastructureLifecycleState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """CloudExadataInfrastructureLifecycleState enum."""

    PROVISIONING = "Provisioning"
    """PROVISIONING value"""
    AVAILABLE = "Available"
    """AVAILABLE value"""
    UPDATING = "Updating"
    """UPDATING value"""
    TERMINATING = "Terminating"
    """TERMINATING value"""
    TERMINATED = "Terminated"
    """TERMINATED value"""
    MAINTENANCE_IN_PROGRESS = "MaintenanceInProgress"
    """MAINTENANCE_IN_PROGRESS value"""
    FAILED = "Failed"
    """FAILED value"""


class CloudVmClusterLifecycleState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """CloudVmClusterLifecycleState enum."""

    PROVISIONING = "Provisioning"
    """PROVISIONING value"""
    AVAILABLE = "Available"
    """AVAILABLE value"""
    UPDATING = "Updating"
    """UPDATING value"""
    TERMINATING = "Terminating"
    """TERMINATING value"""
    TERMINATED = "Terminated"
    """TERMINATED value"""
    MAINTENANCE_IN_PROGRESS = "MaintenanceInProgress"
    """MAINTENANCE_IN_PROGRESS value"""
    FAILED = "Failed"
    """FAILED value"""


class ComputeModel(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """ComputeModel enum."""

    ECPU = "ECPU"
    """ECPU value"""
    OCPU = "OCPU"
    """OCPU value"""


class ConsumerGroup(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """ConsumerGroup enum."""

    HIGH = "High"
    """HIGH value"""
    MEDIUM = "Medium"
    """MEDIUM value"""
    LOW = "Low"
    """LOW value"""
    TP = "Tp"
    """TP value"""
    TPURGENT = "Tpurgent"
    """TPURGENT value"""


class CreatedByType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of identity that created the resource."""

    USER = "User"
    APPLICATION = "Application"
    MANAGED_IDENTITY = "ManagedIdentity"
    KEY = "Key"


class DatabaseEditionType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """DatabaseEditionType enum."""

    STANDARD_EDITION = "StandardEdition"
    """STANDARD_EDITION value"""
    ENTERPRISE_EDITION = "EnterpriseEdition"
    """ENTERPRISE_EDITION value"""


class DataBaseType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """DataBaseType enum."""

    REGULAR = "Regular"
    """REGULAR value"""
    CLONE = "Clone"
    """CLONE value"""


class DataSafeStatusType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """DataSafeStatusType enum."""

    REGISTERING = "Registering"
    """REGISTERING value"""
    REGISTERED = "Registered"
    """REGISTERED value"""
    DEREGISTERING = "Deregistering"
    """DEREGISTERING value"""
    NOT_REGISTERED = "NotRegistered"
    """NOT_REGISTERED value"""
    FAILED = "Failed"
    """FAILED value"""


class DayOfWeekName(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """DayOfWeekName enum."""

    MONDAY = "Monday"
    """Monday value"""
    TUESDAY = "Tuesday"
    """Tuesday value"""
    WEDNESDAY = "Wednesday"
    """Wednesday value"""
    THURSDAY = "Thursday"
    """Thursday value"""
    FRIDAY = "Friday"
    """Friday value"""
    SATURDAY = "Saturday"
    """Saturday value"""
    SUNDAY = "Sunday"
    """Sunday value"""


class DbNodeActionEnum(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """DbNode action enum."""

    START = "Start"
    """Start DbNode"""
    STOP = "Stop"
    """Stop DbNode"""
    SOFT_RESET = "SoftReset"
    """Soft reset DbNode"""
    RESET = "Reset"
    """Reset DbNode"""


class DbNodeMaintenanceType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of database node maintenance."""

    VMDB_REBOOT_MIGRATION = "VmdbRebootMigration"
    """Provisioning value"""


class DbNodeProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """DnNode provisioning state enum."""

    PROVISIONING = "Provisioning"
    """PROVISIONING value"""
    AVAILABLE = "Available"
    """AVAILABLE value"""
    UPDATING = "Updating"
    """UPDATING value"""
    STOPPING = "Stopping"
    """STOPPING value"""
    STOPPED = "Stopped"
    """STOPPED value"""
    STARTING = "Starting"
    """STARTING value"""
    TERMINATING = "Terminating"
    """TERMINATING value"""
    TERMINATED = "Terminated"
    """TERMINATED value"""
    FAILED = "Failed"
    """FAILED value"""


class DbServerPatchingStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Db Server patching status enum."""

    SCHEDULED = "Scheduled"
    """SCHEDULED value"""
    MAINTENANCE_IN_PROGRESS = "MaintenanceInProgress"
    """MAINTENANCE_IN_PROGRESS value"""
    FAILED = "Failed"
    """FAILED value"""
    COMPLETE = "Complete"
    """COMPLETE value"""


class DbServerProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """DbServerProvisioningState enum."""

    CREATING = "Creating"
    """CREATING value"""
    AVAILABLE = "Available"
    """AVAILABLE value"""
    UNAVAILABLE = "Unavailable"
    """UNAVAILABLE value"""
    DELETING = "Deleting"
    """DELETING value"""
    DELETED = "Deleted"
    """DELETED value"""
    MAINTENANCE_IN_PROGRESS = "MaintenanceInProgress"
    """MAINTENANCE_IN_PROGRESS value"""


class DisasterRecoveryType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """DisasterRecoveryType enum."""

    ADG = "Adg"
    """ADG value"""
    BACKUP_BASED = "BackupBased"
    """BACKUP_BASED value"""


class DiskRedundancy(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """DiskRedundancy enum."""

    HIGH = "High"
    """High value"""
    NORMAL = "Normal"
    """Normal value"""


class DnsPrivateViewsLifecycleState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """DnsPrivateViews lifecycle state enum."""

    ACTIVE = "Active"
    """Active value"""
    DELETED = "Deleted"
    """Deleted value"""
    DELETING = "Deleting"
    """Deleting value"""
    UPDATING = "Updating"
    """Updating value"""


class DnsPrivateZonesLifecycleState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """DnsPrivateZones lifecycle state enum."""

    ACTIVE = "Active"
    """Active value"""
    CREATING = "Creating"
    """Creating value"""
    DELETED = "Deleted"
    """Deleted value"""
    DELETING = "Deleting"
    """Deleting value"""
    UPDATING = "Updating"
    """Updating value"""


class GenerateType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """GenerateType enum."""

    SINGLE = "Single"
    """SINGLE value"""
    ALL = "All"
    """ALL value"""


class HostFormatType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """HostFormatType enum."""

    FQDN = "Fqdn"
    """FQDN value"""
    IP = "Ip"
    """IP value"""


class Intent(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Intent enum."""

    RETAIN = "Retain"
    """Retain value"""
    RESET = "Reset"
    """Reset value"""


class IormLifecycleState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """IORMLifecycleState enum."""

    BOOT_STRAPPING = "BootStrapping"
    """BOOTSTRAPPING value"""
    ENABLED = "Enabled"
    """ENABLED value"""
    DISABLED = "Disabled"
    """DISABLED value"""
    UPDATING = "Updating"
    """UPDATING value"""
    FAILED = "Failed"
    """FAILED value"""


class LicenseModel(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """LicenseModel enum."""

    LICENSE_INCLUDED = "LicenseIncluded"
    """LicenseIncluded value"""
    BRING_YOUR_OWN_LICENSE = "BringYourOwnLicense"
    """BringYourOwnLicense value"""


class MonthName(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """MonthName enum."""

    JANUARY = "January"
    """January value"""
    FEBRUARY = "February"
    """February value"""
    MARCH = "March"
    """March value"""
    APRIL = "April"
    """April value"""
    MAY = "May"
    """May value"""
    JUNE = "June"
    """June value"""
    JULY = "July"
    """July value"""
    AUGUST = "August"
    """August value"""
    SEPTEMBER = "September"
    """September value"""
    OCTOBER = "October"
    """October value"""
    NOVEMBER = "November"
    """November value"""
    DECEMBER = "December"
    """December value"""


class Objective(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Objective enum."""

    LOW_LATENCY = "LowLatency"
    """LOW_LATENCY value"""
    HIGH_THROUGHPUT = "HighThroughput"
    """HIGH_THROUGHPUT value"""
    BALANCED = "Balanced"
    """BALANCED value"""
    AUTO = "Auto"
    """AUTO value"""
    BASIC = "Basic"
    """BASIC value"""


class OpenModeType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """OpenModeType enum."""

    READ_ONLY = "ReadOnly"
    """READ_ONLY value"""
    READ_WRITE = "ReadWrite"
    """READ_WRITE value"""


class OperationsInsightsStatusType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """OperationsInsightsStatusType enum."""

    ENABLING = "Enabling"
    """ENABLING value"""
    ENABLED = "Enabled"
    """ENABLED value"""
    DISABLING = "Disabling"
    """DISABLING value"""
    NOT_ENABLED = "NotEnabled"
    """NOT_ENABLED value"""
    FAILED_ENABLING = "FailedEnabling"
    """FAILED_ENABLING value"""
    FAILED_DISABLING = "FailedDisabling"
    """FAILED_DISABLING value"""


class OracleSubscriptionProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """OracleSubscriptionProvisioningState enum."""

    SUCCEEDED = "Succeeded"
    """Resource has been created."""
    FAILED = "Failed"
    """Resource creation failed."""
    CANCELED = "Canceled"
    """Resource creation was canceled."""


class Origin(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The intended executor of the operation; as in Resource Based Access Control (RBAC) and audit
    logs UX. Default value is "user,system".
    """

    USER = "user"
    SYSTEM = "system"
    USER_SYSTEM = "user,system"


class PatchingMode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """PatchingMode enum."""

    ROLLING = "Rolling"
    """Rolling value"""
    NON_ROLLING = "NonRolling"
    """Non Rolling value"""


class PermissionLevelType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """PermissionLevelType enum."""

    RESTRICTED = "Restricted"
    """RESTRICTED value"""
    UNRESTRICTED = "Unrestricted"
    """UNRESTRICTED value"""


class Preference(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Preference enum."""

    NO_PREFERENCE = "NoPreference"
    """NoPreference value"""
    CUSTOM_PREFERENCE = "CustomPreference"
    """CustomPreference value"""


class ProtocolType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """ProtocolType enum."""

    TCP = "TCP"
    """TCP value"""
    TCPS = "TCPS"
    """TCPS value"""


class RefreshableModelType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """RefreshableModelType enum."""

    AUTOMATIC = "Automatic"
    """AUTOMATIC value"""
    MANUAL = "Manual"
    """MANUAL value"""


class RefreshableStatusType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """RefreshableStatusType enum."""

    REFRESHING = "Refreshing"
    """REFRESHING value"""
    NOT_REFRESHING = "NotRefreshing"
    """NOT_REFRESHING value"""


class ResourceProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The provisioning state of a resource type."""

    SUCCEEDED = "Succeeded"
    """Resource has been created."""
    FAILED = "Failed"
    """Resource creation failed."""
    CANCELED = "Canceled"
    """Resource creation was canceled."""


class RoleType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """RoleType enum."""

    PRIMARY = "Primary"
    """PRIMARY value"""
    STANDBY = "Standby"
    """STANDBY value"""
    DISABLED_STANDBY = "DisabledStandby"
    """DISABLED_STANDBY value"""
    BACKUP_COPY = "BackupCopy"
    """BACKUP_COPY value"""
    SNAPSHOT_STANDBY = "SnapshotStandby"
    """SNAPSHOT_STANDBY value"""


class SessionModeType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """SessionModeType enum."""

    DIRECT = "Direct"
    """DIRECT value"""
    REDIRECT = "Redirect"
    """REDIRECT value"""


class SourceType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """SourceType enum."""

    NONE = "None"
    """NONE value"""
    DATABASE = "Database"
    """DATABASE value"""
    BACKUP_FROM_ID = "BackupFromId"
    """BACKUP_FROM_ID value"""
    BACKUP_FROM_TIMESTAMP = "BackupFromTimestamp"
    """BACKUP_FROM_TIMESTAMP value"""
    CLONE_TO_REFRESHABLE = "CloneToRefreshable"
    """CLONE_TO_REFRESHABLE value"""
    CROSS_REGION_DATAGUARD = "CrossRegionDataguard"
    """CROSS_REGION_DATAGUARD value"""
    CROSS_REGION_DISASTER_RECOVERY = "CrossRegionDisasterRecovery"
    """CROSS_REGION_DISASTER_RECOVERY value"""


class SyntaxFormatType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """SyntaxFormatType enum."""

    LONG = "Long"
    """LONG value"""
    EZCONNECT = "Ezconnect"
    """EZCONNECT value"""
    EZCONNECTPLUS = "Ezconnectplus"
    """EZCONNECTPLUS value"""


class TlsAuthenticationType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """TlsAuthenticationType enum."""

    SERVER = "Server"
    """SERVER value"""
    MUTUAL = "Mutual"
    """MUTUAL value"""


class UpdateAction(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """UpdateAction enum."""

    ROLLING_APPLY = "RollingApply"
    """ROLLING_APPLY value"""
    NON_ROLLING_APPLY = "NonRollingApply"
    """NON_ROLLING_APPLY value"""
    PRE_CHECK = "PreCheck"
    """PRECHECK value"""
    ROLL_BACK = "RollBack"
    """ROLLBACK value"""


class ValidationStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """validation status."""

    SUCCEEDED = "Succeeded"
    """Succeeded value"""
    FAILED = "Failed"
    """Failed value"""


class Versions(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Versions for API."""

    V20230901 = "2023-09-01-preview"
    """2023-09-01-preview"""
    V_INTERNAL_API = "internal"
    """internal api - RPaaS to ORP"""


class VirtualNetworkAddressLifecycleState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """VirtualNetworkAddressLifecycleState enum."""

    PROVISIONING = "Provisioning"
    """Provisioning value"""
    AVAILABLE = "Available"
    """Available value"""
    TERMINATING = "Terminating"
    """Terminating value"""
    TERMINATED = "Terminated"
    """Terminated value"""
    FAILED = "Failed"
    """Failed value"""


class WorkloadType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """WorkloadType enum."""

    OLTP = "OLTP"
    """OLTP - indicates an Autonomous Transaction Processing database"""
    DW = "DW"
    """DW - indicates an Autonomous Data Warehouse database"""
    AJD = "AJD"
    """AJD - indicates an Autonomous JSON Database"""
    APEX = "APEX"
    """APEX - indicates an Autonomous Database with the Oracle APEX Application Development workload
    type."""


class ZoneType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """ZoneType enum."""

    PRIMARY = "Primary"
    """Primary value"""
    SECONDARY = "Secondary"
    """Secondary value"""
