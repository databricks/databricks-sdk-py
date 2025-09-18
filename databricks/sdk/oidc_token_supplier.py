import os
from typing import Optional

import requests


class GitHubOIDCTokenSupplier:
    """
    Supplies OIDC tokens from GitHub Actions.
    """

    def get_oidc_token(self, audience: str) -> Optional[str]:
        if "ACTIONS_ID_TOKEN_REQUEST_TOKEN" not in os.environ or "ACTIONS_ID_TOKEN_REQUEST_URL" not in os.environ:
            # not in GitHub actions
            return None
        # See https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/configuring-openid-connect-in-cloud-providers
        headers = {"Authorization": f"Bearer {os.environ['ACTIONS_ID_TOKEN_REQUEST_TOKEN']}"}
        endpoint = f"{os.environ['ACTIONS_ID_TOKEN_REQUEST_URL']}&audience={audience}"
        response = requests.get(endpoint, headers=headers)
        if not response.ok:
            return None

        # get the ID Token with aud=api://AzureADTokenExchange sub=repo:org/repo:environment:name
        response_json = response.json()
        if "value" not in response_json:
            return None

        return response_json["value"]


class AzureDevOpsOIDCTokenSupplier:
    """
    Supplies OIDC tokens from Azure DevOps pipelines.
    
    Constructs the OIDC token request URL using official Azure DevOps predefined variables.
    See: https://docs.microsoft.com/en-us/azure/devops/pipelines/build/variables
    """

    def get_oidc_token(self, audience: str) -> Optional[str]:
        # Note: Azure DevOps OIDC tokens have a fixed audience of "api://AzureADTokenExchange"
        # The audience parameter is ignored but kept for interface compatibility with other OIDC suppliers
        
        # Check for required Azure DevOps environment variables
        access_token = os.environ.get("SYSTEM_ACCESSTOKEN")
        collection_uri = os.environ.get("SYSTEM_TEAMFOUNDATIONCOLLECTIONURI")
        project_id = os.environ.get("SYSTEM_TEAMPROJECTID")
        plan_id = os.environ.get("SYSTEM_PLANID")
        job_id = os.environ.get("SYSTEM_JOBID")
        hub_name = os.environ.get("SYSTEM_HOSTTYPE", "build")  # Default to "build"

        # Check for required variables
        if not all([access_token, collection_uri, project_id, plan_id, job_id]):
            # not in Azure DevOps pipeline
            return None
            
        try:
            # Construct the OIDC token request URL
            # Format: {collection_uri}{project_id}/_apis/distributedtask/hubs/{hubName}/plans/{planId}/jobs/{jobId}/oidctoken
            request_url = f"{collection_uri}{project_id}/_apis/distributedtask/hubs/{hub_name}/plans/{plan_id}/jobs/{job_id}/oidctoken"
            
            # Add API version (audience is fixed to "api://AzureADTokenExchange" by Azure DevOps)
            endpoint = f"{request_url}?api-version=7.2-preview.1"
            headers = {
                "Authorization": f"Bearer {access_token}",
                "Content-Type": "application/json",
                "Content-Length": "0"
            }
            
            # Azure DevOps OIDC endpoint requires POST request with empty body
            response = requests.post(endpoint, headers=headers)
            if not response.ok:
                return None

            # Azure DevOps returns the token in 'oidcToken' field
            response_json = response.json()
            if "oidcToken" not in response_json:
                return None

            return response_json["oidcToken"]
        except Exception:
            # If any error occurs, return None to fall back to other auth methods
            return None
