from dataclasses import dataclass
from typing import Dict, Optional

import pytest  # type: ignore[import-not-found]

from databricks.sdk.oidc_token_supplier import AzureDevOpsOIDCTokenSupplier


@dataclass
class AzureDevOpsOIDCConstructorTestCase:
    """Test case for AzureDevOpsOIDCTokenSupplier constructor validation."""

    name: str
    env_vars: Optional[Dict[str, str]] = None
    should_raise_exception: bool = False
    expected_exception_message: Optional[str] = None


@dataclass
class AzureDevOpsOIDCTokenRequestTestCase:
    """Test case for OIDC token request/response handling (assumes constructor succeeds)."""

    name: str
    env_vars: Dict[str, str]  # Token request tests always have all required environment variables.
    response_ok: bool = True
    response_json: Optional[Dict[str, str]] = None
    want_token: Optional[str] = None
    want_none: bool = False


# Test cases for constructor validation (both success and failure).
_azure_devops_oidc_constructor_test_cases = [
    # Constructor success cases.
    AzureDevOpsOIDCConstructorTestCase(
        name="constructor_success_all_env_vars",
        env_vars={
            "SYSTEM_ACCESSTOKEN": "azure-devops-access-token",
            "SYSTEM_TEAMFOUNDATIONCOLLECTIONURI": "https://dev.azure.com/myorg/",
            "SYSTEM_TEAMPROJECTID": "project-123",
            "SYSTEM_PLANID": "plan-456",
            "SYSTEM_JOBID": "job-789",
            "SYSTEM_HOSTTYPE": "build",
        },
        should_raise_exception=False,
    ),
    # Constructor failure cases.
    AzureDevOpsOIDCConstructorTestCase(
        name="missing_access_token",
        env_vars={
            "SYSTEM_TEAMFOUNDATIONCOLLECTIONURI": "https://dev.azure.com/myorg/",
            "SYSTEM_TEAMPROJECTID": "project-123",
            "SYSTEM_PLANID": "plan-456",
            "SYSTEM_JOBID": "job-789",
            "SYSTEM_HOSTTYPE": "build",
        },
        should_raise_exception=True,
        expected_exception_message="Azure DevOps OIDC: SYSTEM_ACCESSTOKEN env var not found",
    ),
    AzureDevOpsOIDCConstructorTestCase(
        name="missing_hosttype",
        env_vars={
            "SYSTEM_ACCESSTOKEN": "azure-devops-access-token",
            "SYSTEM_TEAMFOUNDATIONCOLLECTIONURI": "https://dev.azure.com/myorg/",
            "SYSTEM_TEAMPROJECTID": "project-123",
            "SYSTEM_PLANID": "plan-456",
            "SYSTEM_JOBID": "job-789",
        },
        should_raise_exception=True,
        expected_exception_message="Azure DevOps OIDC: missing required environment variables: SYSTEM_HOSTTYPE",
    ),
    AzureDevOpsOIDCConstructorTestCase(
        name="missing_plan_id",
        env_vars={
            "SYSTEM_ACCESSTOKEN": "azure-devops-access-token",
            "SYSTEM_TEAMFOUNDATIONCOLLECTIONURI": "https://dev.azure.com/myorg/",
            "SYSTEM_TEAMPROJECTID": "project-123",
            "SYSTEM_JOBID": "job-789",
            "SYSTEM_HOSTTYPE": "build",
        },
        should_raise_exception=True,
        expected_exception_message="Azure DevOps OIDC: missing required environment variables: SYSTEM_PLANID",
    ),
    AzureDevOpsOIDCConstructorTestCase(
        name="missing_job_id",
        env_vars={
            "SYSTEM_ACCESSTOKEN": "azure-devops-access-token",
            "SYSTEM_TEAMFOUNDATIONCOLLECTIONURI": "https://dev.azure.com/myorg/",
            "SYSTEM_TEAMPROJECTID": "project-123",
            "SYSTEM_PLANID": "plan-456",
            "SYSTEM_HOSTTYPE": "build",
        },
        should_raise_exception=True,
        expected_exception_message="Azure DevOps OIDC: missing required environment variables: SYSTEM_JOBID",
    ),
    AzureDevOpsOIDCConstructorTestCase(
        name="missing_team_foundation_collection_uri",
        env_vars={
            "SYSTEM_ACCESSTOKEN": "azure-devops-access-token",
            "SYSTEM_TEAMPROJECTID": "project-123",
            "SYSTEM_PLANID": "plan-456",
            "SYSTEM_JOBID": "job-789",
            "SYSTEM_HOSTTYPE": "build",
        },
        should_raise_exception=True,
        expected_exception_message="Azure DevOps OIDC: missing required environment variables: SYSTEM_TEAMFOUNDATIONCOLLECTIONURI",
    ),
    AzureDevOpsOIDCConstructorTestCase(
        name="missing_project_id",
        env_vars={
            "SYSTEM_ACCESSTOKEN": "azure-devops-access-token",
            "SYSTEM_TEAMFOUNDATIONCOLLECTIONURI": "https://dev.azure.com/myorg/",
            "SYSTEM_PLANID": "plan-456",
            "SYSTEM_JOBID": "job-789",
            "SYSTEM_HOSTTYPE": "build",
        },
        should_raise_exception=True,
        expected_exception_message="Azure DevOps OIDC: missing required environment variables: SYSTEM_TEAMPROJECTID",
    ),
    AzureDevOpsOIDCConstructorTestCase(
        name="missing_multiple_vars",
        env_vars={
            "SYSTEM_ACCESSTOKEN": "azure-devops-access-token",
        },
        should_raise_exception=True,
        expected_exception_message="Azure DevOps OIDC: missing required environment variables:",
    ),
]

# Test cases for OIDC token request/response handling.
_azure_devops_oidc_token_request_test_cases = [
    AzureDevOpsOIDCTokenRequestTestCase(
        name="success_with_hosttype",
        env_vars={
            "SYSTEM_ACCESSTOKEN": "azure-devops-access-token",
            "SYSTEM_TEAMFOUNDATIONCOLLECTIONURI": "https://dev.azure.com/myorg/",
            "SYSTEM_TEAMPROJECTID": "project-123",
            "SYSTEM_PLANID": "plan-456",
            "SYSTEM_JOBID": "job-789",
            "SYSTEM_HOSTTYPE": "build",
        },
        response_ok=True,
        response_json={"oidcToken": "test-azure-devops-jwt-token"},
        want_token="test-azure-devops-jwt-token",
    ),
    AzureDevOpsOIDCTokenRequestTestCase(
        name="request_failure",
        env_vars={
            "SYSTEM_ACCESSTOKEN": "azure-devops-access-token",
            "SYSTEM_TEAMFOUNDATIONCOLLECTIONURI": "https://dev.azure.com/myorg/",
            "SYSTEM_TEAMPROJECTID": "project-123",
            "SYSTEM_PLANID": "plan-456",
            "SYSTEM_JOBID": "job-789",
            "SYSTEM_HOSTTYPE": "build",
        },
        response_ok=False,
        want_none=True,
    ),
    AzureDevOpsOIDCTokenRequestTestCase(
        name="missing_oidc_token_in_response",
        env_vars={
            "SYSTEM_ACCESSTOKEN": "azure-devops-access-token",
            "SYSTEM_TEAMFOUNDATIONCOLLECTIONURI": "https://dev.azure.com/myorg/",
            "SYSTEM_TEAMPROJECTID": "project-123",
            "SYSTEM_PLANID": "plan-456",
            "SYSTEM_JOBID": "job-789",
            "SYSTEM_HOSTTYPE": "build",
        },
        response_ok=True,
        response_json={"error": "no oidcToken"},
        want_none=True,
    ),
]


@pytest.mark.parametrize("test_case", _azure_devops_oidc_constructor_test_cases)
def test_azure_devops_oidc_constructor_validation(test_case: AzureDevOpsOIDCConstructorTestCase, monkeypatch):
    """Test AzureDevOpsOIDCTokenSupplier constructor validation with various environment variable scenarios."""
    # Set up environment variables.
    if test_case.env_vars:
        for key, value in test_case.env_vars.items():
            monkeypatch.setenv(key, value)

    if test_case.should_raise_exception:
        # Test that constructor raises ValueError with expected message.
        with pytest.raises(ValueError) as exc_info:
            AzureDevOpsOIDCTokenSupplier()

        # Verify the exception message contains the expected text.
        if test_case.expected_exception_message:
            assert test_case.expected_exception_message in str(
                exc_info.value
            ), f"Exception message should contain '{test_case.expected_exception_message}', but got: {str(exc_info.value)}"
    else:
        # Test that constructor succeeds.
        supplier = AzureDevOpsOIDCTokenSupplier()
        assert supplier is not None
        # Verify that all required attributes are set.
        assert supplier.access_token is not None
        assert supplier.collection_uri is not None
        assert supplier.project_id is not None
        assert supplier.plan_id is not None
        assert supplier.job_id is not None
        assert supplier.hub_name is not None


@pytest.mark.parametrize("test_case", _azure_devops_oidc_token_request_test_cases)
def test_azure_devops_oidc_token_request(test_case: AzureDevOpsOIDCTokenRequestTestCase, monkeypatch, mocker):
    """Test OIDC token request/response handling (assumes constructor succeeds)."""
    # Set up environment variables.
    for key, value in test_case.env_vars.items():
        monkeypatch.setenv(key, value)

    # Mock HTTP response.
    mock_response = mocker.Mock()
    mock_response.ok = test_case.response_ok
    if test_case.response_json:
        mock_response.json.return_value = test_case.response_json
    mock_post = mocker.patch("requests.post", return_value=mock_response)

    # Initialize supplier (should succeed for these test cases since they have all required environment variables).
    supplier = AzureDevOpsOIDCTokenSupplier()

    # Get token.
    token = supplier.get_oidc_token("ignored-audience")  # Audience is ignored for Azure DevOps.

    # Verify token result.
    if test_case.want_none:
        assert token is None
    else:
        assert token == test_case.want_token

        # Verify the HTTP request was made correctly (only for successful token cases).
        expected_url = (
            "https://dev.azure.com/myorg/project-123/_apis/distributedtask/"
            "hubs/build/plans/plan-456/jobs/job-789/oidctoken?api-version=7.2-preview.1"
        )
        mock_post.assert_called_once_with(
            expected_url,
            headers={
                "Authorization": "Bearer azure-devops-access-token",
                "Content-Type": "application/json",
                "Content-Length": "0",
            },
        )

    # For failure cases, verify HTTP request was still made but returned failure.
    if test_case.want_none and test_case.response_ok is False:
        mock_post.assert_called_once()  # Request was made but failed.
