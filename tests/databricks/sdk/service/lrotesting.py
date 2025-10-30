# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

from __future__ import annotations

import logging
from dataclasses import dataclass
from datetime import timedelta
from enum import Enum
from typing import Any, Dict, List, Optional

from databricks.sdk.common import lro
from databricks.sdk.retries import RetryError, poll
from databricks.sdk.service._internal import _enum, _from_dict

_LOG = logging.getLogger("databricks.sdk")


# all definitions in this file are in alphabetical order


@dataclass
class DatabricksServiceExceptionWithDetailsProto:
    """Serialization format for DatabricksServiceException with error details. This message doesn't
    work for ScalaPB-04 as google.protobuf.Any is only available to ScalaPB-09. Note the definition
    of this message should be in sync with DatabricksServiceExceptionProto defined in
    /api-base/proto/legacy/databricks.proto except the later one doesn't have the error details
    field defined."""

    details: Optional[List[dict]] = None
    """@pbjson-skip"""

    error_code: Optional[ErrorCode] = None

    message: Optional[str] = None

    stack_trace: Optional[str] = None

    def as_dict(self) -> dict:
        """Serializes the DatabricksServiceExceptionWithDetailsProto into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.details:
            body["details"] = [v for v in self.details]
        if self.error_code is not None:
            body["error_code"] = self.error_code.value
        if self.message is not None:
            body["message"] = self.message
        if self.stack_trace is not None:
            body["stack_trace"] = self.stack_trace
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the DatabricksServiceExceptionWithDetailsProto into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.details:
            body["details"] = self.details
        if self.error_code is not None:
            body["error_code"] = self.error_code
        if self.message is not None:
            body["message"] = self.message
        if self.stack_trace is not None:
            body["stack_trace"] = self.stack_trace
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> DatabricksServiceExceptionWithDetailsProto:
        """Deserializes the DatabricksServiceExceptionWithDetailsProto from a dictionary."""
        return cls(
            details=d.get("details", None),
            error_code=_enum(d, "error_code", ErrorCode),
            message=d.get("message", None),
            stack_trace=d.get("stack_trace", None),
        )


class ErrorCode(Enum):
    """Legacy definition of the ErrorCode enum. Please keep in sync with
    api-base/proto/error_code.proto (except status code mapping annotations as this file doesn't
    have them). Will be removed eventually, pending the ScalaPB 0.4 cleanup."""

    ABORTED = "ABORTED"
    ALREADY_EXISTS = "ALREADY_EXISTS"
    BAD_REQUEST = "BAD_REQUEST"
    CANCELLED = "CANCELLED"
    CATALOG_ALREADY_EXISTS = "CATALOG_ALREADY_EXISTS"
    CATALOG_DOES_NOT_EXIST = "CATALOG_DOES_NOT_EXIST"
    CATALOG_NOT_EMPTY = "CATALOG_NOT_EMPTY"
    COULD_NOT_ACQUIRE_LOCK = "COULD_NOT_ACQUIRE_LOCK"
    CUSTOMER_UNAUTHORIZED = "CUSTOMER_UNAUTHORIZED"
    DAC_ALREADY_EXISTS = "DAC_ALREADY_EXISTS"
    DAC_DOES_NOT_EXIST = "DAC_DOES_NOT_EXIST"
    DATA_LOSS = "DATA_LOSS"
    DEADLINE_EXCEEDED = "DEADLINE_EXCEEDED"
    DEPLOYMENT_TIMEOUT = "DEPLOYMENT_TIMEOUT"
    DIRECTORY_NOT_EMPTY = "DIRECTORY_NOT_EMPTY"
    DIRECTORY_PROTECTED = "DIRECTORY_PROTECTED"
    DRY_RUN_FAILED = "DRY_RUN_FAILED"
    ENDPOINT_NOT_FOUND = "ENDPOINT_NOT_FOUND"
    EXTERNAL_LOCATION_ALREADY_EXISTS = "EXTERNAL_LOCATION_ALREADY_EXISTS"
    EXTERNAL_LOCATION_DOES_NOT_EXIST = "EXTERNAL_LOCATION_DOES_NOT_EXIST"
    FEATURE_DISABLED = "FEATURE_DISABLED"
    GIT_CONFLICT = "GIT_CONFLICT"
    GIT_REMOTE_ERROR = "GIT_REMOTE_ERROR"
    GIT_SENSITIVE_TOKEN_DETECTED = "GIT_SENSITIVE_TOKEN_DETECTED"
    GIT_UNKNOWN_REF = "GIT_UNKNOWN_REF"
    GIT_URL_NOT_ON_ALLOW_LIST = "GIT_URL_NOT_ON_ALLOW_LIST"
    INSECURE_PARTNER_RESPONSE = "INSECURE_PARTNER_RESPONSE"
    INTERNAL_ERROR = "INTERNAL_ERROR"
    INVALID_PARAMETER_VALUE = "INVALID_PARAMETER_VALUE"
    INVALID_STATE = "INVALID_STATE"
    INVALID_STATE_TRANSITION = "INVALID_STATE_TRANSITION"
    IO_ERROR = "IO_ERROR"
    IPYNB_FILE_IN_REPO = "IPYNB_FILE_IN_REPO"
    MALFORMED_PARTNER_RESPONSE = "MALFORMED_PARTNER_RESPONSE"
    MALFORMED_REQUEST = "MALFORMED_REQUEST"
    MANAGED_RESOURCE_GROUP_DOES_NOT_EXIST = "MANAGED_RESOURCE_GROUP_DOES_NOT_EXIST"
    MAX_BLOCK_SIZE_EXCEEDED = "MAX_BLOCK_SIZE_EXCEEDED"
    MAX_CHILD_NODE_SIZE_EXCEEDED = "MAX_CHILD_NODE_SIZE_EXCEEDED"
    MAX_LIST_SIZE_EXCEEDED = "MAX_LIST_SIZE_EXCEEDED"
    MAX_NOTEBOOK_SIZE_EXCEEDED = "MAX_NOTEBOOK_SIZE_EXCEEDED"
    MAX_READ_SIZE_EXCEEDED = "MAX_READ_SIZE_EXCEEDED"
    METASTORE_ALREADY_EXISTS = "METASTORE_ALREADY_EXISTS"
    METASTORE_DOES_NOT_EXIST = "METASTORE_DOES_NOT_EXIST"
    METASTORE_NOT_EMPTY = "METASTORE_NOT_EMPTY"
    NOT_FOUND = "NOT_FOUND"
    NOT_IMPLEMENTED = "NOT_IMPLEMENTED"
    PARTIAL_DELETE = "PARTIAL_DELETE"
    PERMISSION_DENIED = "PERMISSION_DENIED"
    PERMISSION_NOT_PROPAGATED = "PERMISSION_NOT_PROPAGATED"
    PRINCIPAL_DOES_NOT_EXIST = "PRINCIPAL_DOES_NOT_EXIST"
    PROJECTS_OPERATION_TIMEOUT = "PROJECTS_OPERATION_TIMEOUT"
    PROVIDER_ALREADY_EXISTS = "PROVIDER_ALREADY_EXISTS"
    PROVIDER_DOES_NOT_EXIST = "PROVIDER_DOES_NOT_EXIST"
    PROVIDER_SHARE_NOT_ACCESSIBLE = "PROVIDER_SHARE_NOT_ACCESSIBLE"
    QUOTA_EXCEEDED = "QUOTA_EXCEEDED"
    RECIPIENT_ALREADY_EXISTS = "RECIPIENT_ALREADY_EXISTS"
    RECIPIENT_DOES_NOT_EXIST = "RECIPIENT_DOES_NOT_EXIST"
    REQUEST_LIMIT_EXCEEDED = "REQUEST_LIMIT_EXCEEDED"
    RESOURCE_ALREADY_EXISTS = "RESOURCE_ALREADY_EXISTS"
    RESOURCE_CONFLICT = "RESOURCE_CONFLICT"
    RESOURCE_DOES_NOT_EXIST = "RESOURCE_DOES_NOT_EXIST"
    RESOURCE_EXHAUSTED = "RESOURCE_EXHAUSTED"
    RESOURCE_LIMIT_EXCEEDED = "RESOURCE_LIMIT_EXCEEDED"
    SCHEMA_ALREADY_EXISTS = "SCHEMA_ALREADY_EXISTS"
    SCHEMA_DOES_NOT_EXIST = "SCHEMA_DOES_NOT_EXIST"
    SCHEMA_NOT_EMPTY = "SCHEMA_NOT_EMPTY"
    SEARCH_QUERY_TOO_LONG = "SEARCH_QUERY_TOO_LONG"
    SEARCH_QUERY_TOO_SHORT = "SEARCH_QUERY_TOO_SHORT"
    SERVICE_UNDER_MAINTENANCE = "SERVICE_UNDER_MAINTENANCE"
    SHARE_ALREADY_EXISTS = "SHARE_ALREADY_EXISTS"
    SHARE_DOES_NOT_EXIST = "SHARE_DOES_NOT_EXIST"
    STORAGE_CREDENTIAL_ALREADY_EXISTS = "STORAGE_CREDENTIAL_ALREADY_EXISTS"
    STORAGE_CREDENTIAL_DOES_NOT_EXIST = "STORAGE_CREDENTIAL_DOES_NOT_EXIST"
    TABLE_ALREADY_EXISTS = "TABLE_ALREADY_EXISTS"
    TABLE_DOES_NOT_EXIST = "TABLE_DOES_NOT_EXIST"
    TEMPORARILY_UNAVAILABLE = "TEMPORARILY_UNAVAILABLE"
    UNAUTHENTICATED = "UNAUTHENTICATED"
    UNAVAILABLE = "UNAVAILABLE"
    UNKNOWN = "UNKNOWN"
    UNPARSEABLE_HTTP_ERROR = "UNPARSEABLE_HTTP_ERROR"
    WORKSPACE_TEMPORARILY_UNAVAILABLE = "WORKSPACE_TEMPORARILY_UNAVAILABLE"


@dataclass
class Operation:
    """This resource represents a long-running operation that is the result of a network API call."""

    done: Optional[bool] = None
    """If the value is `false`, it means the operation is still in progress. If `true`, the operation
    is completed, and either `error` or `response` is available."""

    error: Optional[DatabricksServiceExceptionWithDetailsProto] = None
    """The error result of the operation in case of failure or cancellation."""

    metadata: Optional[dict] = None
    """Service-specific metadata associated with the operation. It typically contains progress
    information and common metadata such as create time. Some services might not provide such
    metadata. Any method that returns a long-running operation should document the metadata type, if
    any."""

    name: Optional[str] = None
    """The server-assigned name, which is only unique within the same service that originally returns
    it. If you use the default HTTP mapping, the `name` should be a resource name ending with
    `operations/{unique_id}`.
    
    Note: multi-segment resource names are not yet supported in the RPC framework and SDK/TF. Until
    that support is added, `name` must be string without internal `/` separators."""

    response: Optional[dict] = None
    """The normal, successful response of the operation. If the original method returns no data on
    success, such as `Delete`, the response is `google.protobuf.Empty`. If the original method is
    standard `Get`/`Create`/`Update`, the response should be the resource. For other methods, the
    response should have the type `XxxResponse`, where `Xxx` is the original method name. For
    example, if the original method name is `TakeSnapshot()`, the inferred response type is
    `TakeSnapshotResponse`."""

    def as_dict(self) -> dict:
        """Serializes the Operation into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.done is not None:
            body["done"] = self.done
        if self.error:
            body["error"] = self.error.as_dict()
        if self.metadata:
            body["metadata"] = self.metadata
        if self.name is not None:
            body["name"] = self.name
        if self.response:
            body["response"] = self.response
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the Operation into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.done is not None:
            body["done"] = self.done
        if self.error:
            body["error"] = self.error
        if self.metadata:
            body["metadata"] = self.metadata
        if self.name is not None:
            body["name"] = self.name
        if self.response:
            body["response"] = self.response
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> Operation:
        """Deserializes the Operation from a dictionary."""
        return cls(
            done=d.get("done", None),
            error=_from_dict(d, "error", DatabricksServiceExceptionWithDetailsProto),
            metadata=d.get("metadata", None),
            name=d.get("name", None),
            response=d.get("response", None),
        )


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


@dataclass
class TestResourceOperationMetadata:
    """Metadata for test resource operations"""

    progress_percent: Optional[int] = None
    """Progress percentage (0-100)"""

    resource_id: Optional[str] = None
    """ID of the resource being operated on"""

    def as_dict(self) -> dict:
        """Serializes the TestResourceOperationMetadata into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.progress_percent is not None:
            body["progress_percent"] = self.progress_percent
        if self.resource_id is not None:
            body["resource_id"] = self.resource_id
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the TestResourceOperationMetadata into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.progress_percent is not None:
            body["progress_percent"] = self.progress_percent
        if self.resource_id is not None:
            body["resource_id"] = self.resource_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> TestResourceOperationMetadata:
        """Deserializes the TestResourceOperationMetadata from a dictionary."""
        return cls(progress_percent=d.get("progress_percent", None), resource_id=d.get("resource_id", None))


class LroTestingAPI:
    """Test service for Long Running Operations"""

    def __init__(self, api_client):
        self._api = api_client

    def cancel_operation(self, name: str):

        headers = {
            "Accept": "application/json",
        }

        self._api.do("POST", f"/api/2.0/lro-testing/operations/{name}/cancel", headers=headers)

    def create_test_resource(self, resource: TestResource) -> CreateTestResourceOperation:
        """Simple method to create test resource for LRO testing

        :param resource: :class:`TestResource`
          The resource to create

        :returns: :class:`Operation`
        """

        body = resource.as_dict()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        res = self._api.do("POST", "/api/2.0/lro-testing/resources", body=body, headers=headers)
        operation = Operation.from_dict(res)
        return CreateTestResourceOperation(self, operation)

    def delete_test_resource(self, resource_id: str) -> DeleteTestResourceOperation:

        headers = {
            "Accept": "application/json",
        }

        res = self._api.do("DELETE", f"/api/2.0/lro-testing/resources/{resource_id}", headers=headers)
        operation = Operation.from_dict(res)
        return DeleteTestResourceOperation(self, operation)

    def get_operation(self, name: str) -> Operation:

        headers = {
            "Accept": "application/json",
        }

        res = self._api.do("GET", f"/api/2.0/lro-testing/operations/{name}", headers=headers)
        return Operation.from_dict(res)

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


class CreateTestResourceOperation:
    """Long-running operation for create_test_resource"""

    def __init__(self, impl: LroTestingAPI, operation: Operation):
        self._impl = impl
        self._operation = operation

    def wait(self, opts: Optional[lro.LroOptions] = None) -> TestResource:
        """Wait blocks until the long-running operation is completed with default 20 min
        timeout. If the operation didn't finish within the timeout, this function will
        raise an error of type TimeoutError, otherwise returns successful response and
        any errors encountered.

        :param opts: :class:`LroOptions`
          Timeout options (default: 20 minutes)

        :returns: :class:`TestResource`
        """

        def poll_operation():
            operation = self._impl.get_operation(name=self._operation.name)

            # Update local operation state
            self._operation = operation

            if not operation.done:
                return None, RetryError.continues("operation still in progress")

            if operation.error:
                error_msg = operation.error.message if operation.error.message else "unknown error"
                if operation.error.error_code:
                    error_msg = f"[{operation.error.error_code}] {error_msg}"
                return None, RetryError.halt(Exception(f"operation failed: {error_msg}"))

            # Operation completed successfully, unmarshal response.
            if operation.response is None:
                return None, RetryError.halt(Exception("operation completed but no response available"))

            test_resource = TestResource.from_dict(operation.response)

            return test_resource, None

        return poll(poll_operation, timeout=opts.timeout if opts is not None else timedelta(minutes=20))

    def cancel(self):
        """Starts asynchronous cancellation on a long-running operation. The server
        makes a best effort to cancel the operation, but success is not guaranteed.
        """
        self._impl.cancel_operation(name=self._operation.name)

    def name(self) -> str:
        """Name returns the name of the long-running operation. The name is assigned
        by the server and is unique within the service from which the operation is created.

        :returns: str
        """
        return self._operation.name

    def metadata(self) -> TestResourceOperationMetadata:
        """Metadata returns metadata associated with the long-running operation.
        If the metadata is not available, the returned metadata is None.

        :returns: :class:`TestResourceOperationMetadata` or None
        """
        if self._operation.metadata is None:
            return None

        return TestResourceOperationMetadata.from_dict(self._operation.metadata)

    def done(self) -> bool:
        """Done reports whether the long-running operation has completed.

        :returns: bool
        """
        # Refresh the operation state first
        operation = self._impl.get_operation(name=self._operation.name)

        # Update local operation state
        self._operation = operation

        return operation.done


class DeleteTestResourceOperation:
    """Long-running operation for delete_test_resource"""

    def __init__(self, impl: LroTestingAPI, operation: Operation):
        self._impl = impl
        self._operation = operation

    def wait(self, opts: Optional[lro.LroOptions] = None):
        """Wait blocks until the long-running operation is completed with default 20 min
        timeout. If the operation didn't finish within the timeout, this function will
        raise an error of type TimeoutError, otherwise returns successful response and
        any errors encountered.

        :param opts: :class:`LroOptions`
          Timeout options (default: 20 minutes)

        :returns: :class:`Any /* MISSING TYPE */`
        """

        def poll_operation():
            operation = self._impl.get_operation(name=self._operation.name)

            # Update local operation state
            self._operation = operation

            if not operation.done:
                return None, RetryError.continues("operation still in progress")

            if operation.error:
                error_msg = operation.error.message if operation.error.message else "unknown error"
                if operation.error.error_code:
                    error_msg = f"[{operation.error.error_code}] {error_msg}"
                return None, RetryError.halt(Exception(f"operation failed: {error_msg}"))

            # Operation completed successfully, unmarshal response.
            if operation.response is None:
                return None, RetryError.halt(Exception("operation completed but no response available"))

            return {}, None

        poll(poll_operation, timeout=opts.timeout if opts is not None else timedelta(minutes=20))

    def cancel(self):
        """Starts asynchronous cancellation on a long-running operation. The server
        makes a best effort to cancel the operation, but success is not guaranteed.
        """
        self._impl.cancel_operation(name=self._operation.name)

    def name(self) -> str:
        """Name returns the name of the long-running operation. The name is assigned
        by the server and is unique within the service from which the operation is created.

        :returns: str
        """
        return self._operation.name

    def metadata(self) -> TestResourceOperationMetadata:
        """Metadata returns metadata associated with the long-running operation.
        If the metadata is not available, the returned metadata is None.

        :returns: :class:`TestResourceOperationMetadata` or None
        """
        if self._operation.metadata is None:
            return None

        return TestResourceOperationMetadata.from_dict(self._operation.metadata)

    def done(self) -> bool:
        """Done reports whether the long-running operation has completed.

        :returns: bool
        """
        # Refresh the operation state first
        operation = self._impl.get_operation(name=self._operation.name)

        # Update local operation state
        self._operation = operation

        return operation.done
