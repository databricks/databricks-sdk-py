from dataclasses import dataclass
from typing import Dict, Optional

import pytest

from databricks.sdk.oidc_token_supplier import AzureDevOpsOIDCTokenSupplier


@dataclass
class AzureDevOpsOIDCTestCase:
    name: str
    env_vars: Optional[Dict[str, str]] = None
    response_ok: bool = True
    response_json: Optional[Dict[str, str]] = None
    want_token: Optional[str] = None
    want_none: bool = False


_azure_devops_oidc_test_cases = [
    AzureDevOpsOIDCTestCase(
        name="success_with_hosttype",
        env_vars={
            "SYSTEM_ACCESSTOKEN": "azdo-access-token",
            "SYSTEM_TEAMFOUNDATIONCOLLECTIONURI": "https://dev.azure.com/myorg/",
            "SYSTEM_TEAMPROJECTID": "project-123",
            "SYSTEM_PLANID": "plan-456",
            "SYSTEM_JOBID": "job-789",
            "SYSTEM_HOSTTYPE": "build"
        },
        response_ok=True,
        response_json={"oidcToken": "test-azdo-jwt-token"},
        want_token="test-azdo-jwt-token",
    ),
    AzureDevOpsOIDCTestCase(
        name="missing_hosttype",
        env_vars={
            "SYSTEM_ACCESSTOKEN": "azdo-access-token",
            "SYSTEM_TEAMFOUNDATIONCOLLECTIONURI": "https://dev.azure.com/myorg/",
            "SYSTEM_TEAMPROJECTID": "project-123", 
            "SYSTEM_PLANID": "plan-456",
            "SYSTEM_JOBID": "job-789"
        },
        want_none=True,
    ),
    AzureDevOpsOIDCTestCase(
        name="missing_access_token",
        env_vars={
            "SYSTEM_TEAMFOUNDATIONCOLLECTIONURI": "https://dev.azure.com/myorg/",
            "SYSTEM_TEAMPROJECTID": "project-123",
            "SYSTEM_PLANID": "plan-456", 
            "SYSTEM_JOBID": "job-789",
            "SYSTEM_HOSTTYPE": "build"
        },
        want_none=True,
    ),
    AzureDevOpsOIDCTestCase(
        name="missing_plan_id",
        env_vars={
            "SYSTEM_ACCESSTOKEN": "azdo-access-token",
            "SYSTEM_TEAMFOUNDATIONCOLLECTIONURI": "https://dev.azure.com/myorg/",
            "SYSTEM_TEAMPROJECTID": "project-123",
            "SYSTEM_JOBID": "job-789",
            "SYSTEM_HOSTTYPE": "build"
        },
        want_none=True,
    ),
    AzureDevOpsOIDCTestCase(
        name="missing_job_id",
        env_vars={
            "SYSTEM_ACCESSTOKEN": "azdo-access-token",
            "SYSTEM_TEAMFOUNDATIONCOLLECTIONURI": "https://dev.azure.com/myorg/",
            "SYSTEM_TEAMPROJECTID": "project-123",
            "SYSTEM_PLANID": "plan-456",
            "SYSTEM_HOSTTYPE": "build"
        },
        want_none=True,
    ),
    AzureDevOpsOIDCTestCase(
        name="missing_team_foundation_collection_uri",
        env_vars={
            "SYSTEM_ACCESSTOKEN": "azdo-access-token",
            "SYSTEM_TEAMPROJECTID": "project-123",
            "SYSTEM_PLANID": "plan-456",
            "SYSTEM_JOBID": "job-789",
            "SYSTEM_HOSTTYPE": "build"
        },
        want_none=True,
    ),
    AzureDevOpsOIDCTestCase(
        name="missing_project_id",
        env_vars={
            "SYSTEM_ACCESSTOKEN": "azdo-access-token",
            "SYSTEM_TEAMFOUNDATIONCOLLECTIONURI": "https://dev.azure.com/myorg/",
            "SYSTEM_PLANID": "plan-456",
            "SYSTEM_JOBID": "job-789",
            "SYSTEM_HOSTTYPE": "build"
        },
        want_none=True,
    ),
    AzureDevOpsOIDCTestCase(
        name="request_failure",
        env_vars={
            "SYSTEM_ACCESSTOKEN": "azdo-access-token",
            "SYSTEM_TEAMFOUNDATIONCOLLECTIONURI": "https://dev.azure.com/myorg/",
            "SYSTEM_TEAMPROJECTID": "project-123",
            "SYSTEM_PLANID": "plan-456",
            "SYSTEM_JOBID": "job-789",
            "SYSTEM_HOSTTYPE": "build"
        },
        response_ok=False,
        want_none=True,
    ),
    AzureDevOpsOIDCTestCase(
        name="missing_oidc_token_in_response",
        env_vars={
            "SYSTEM_ACCESSTOKEN": "azdo-access-token",
            "SYSTEM_TEAMFOUNDATIONCOLLECTIONURI": "https://dev.azure.com/myorg/",
            "SYSTEM_TEAMPROJECTID": "project-123",
            "SYSTEM_PLANID": "plan-456", 
            "SYSTEM_JOBID": "job-789",
            "SYSTEM_HOSTTYPE": "build"
        },
        response_ok=True,
        response_json={"error": "no oidcToken"},
        want_none=True,
    ),
]


@pytest.mark.parametrize("test_case", _azure_devops_oidc_test_cases)
def test_azure_devops_oidc_token_supplier(test_case: AzureDevOpsOIDCTestCase, monkeypatch, mocker):
    """Test AzureDevOpsOIDCTokenSupplier with various scenarios"""
    # Set up environment variables
    if test_case.env_vars:
        for key, value in test_case.env_vars.items():
            monkeypatch.setenv(key, value)
    
    # Mock requests.post if we have all required environment variables (including HOSTTYPE)
    required_vars = ["SYSTEM_ACCESSTOKEN", "SYSTEM_TEAMFOUNDATIONCOLLECTIONURI", 
                     "SYSTEM_TEAMPROJECTID", "SYSTEM_PLANID", "SYSTEM_JOBID", "SYSTEM_HOSTTYPE"]
    has_required_vars = test_case.env_vars and all(var in test_case.env_vars for var in required_vars)
    
    mock_post = None
    if has_required_vars:  # Only mock if all required vars exist
        mock_response = mocker.Mock()
        mock_response.ok = test_case.response_ok
        if test_case.response_json:
            mock_response.json.return_value = test_case.response_json
        mock_post = mocker.patch('requests.post', return_value=mock_response)
    
    supplier = AzureDevOpsOIDCTokenSupplier()
    token = supplier.get_oidc_token("ignored-audience")  # Audience is ignored for Azure DevOps
    
    if test_case.want_none:
        assert token is None
    else:
        assert token == test_case.want_token
        # Verify the request was made correctly
        if mock_post is not None:
            expected_url = (
                "https://dev.azure.com/myorg/project-123/_apis/distributedtask/"
                "hubs/build/plans/plan-456/jobs/job-789/oidctoken?api-version=7.2-preview.1"
            )
            mock_post.assert_called_once_with(
                expected_url,
                headers={
                    "Authorization": "Bearer azdo-access-token",
                    "Content-Type": "application/json",
                    "Content-Length": "0"
                }
            )

