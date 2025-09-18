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
    """

    def get_oidc_token(self, audience: str) -> Optional[str]:
        # Retrieve necessary environment variables
        access_token = os.environ.get('SYSTEM_ACCESSTOKEN')
        collection_uri = os.environ.get('SYSTEM_TEAMFOUNDATIONCOLLECTIONURI')
        project_id = os.environ.get('SYSTEM_TEAMPROJECTID')
        plan_id = os.environ.get('SYSTEM_PLANID')
        job_id = os.environ.get('SYSTEM_JOBID')
        hub_name = os.environ.get('SYSTEM_HOSTTYPE')

        # Check for required variables
        if not all([access_token, collection_uri, project_id, plan_id, job_id]):
            # not in Azure DevOps pipeline
            return None
            
        # Construct the URL
        request_url = f"{collection_uri}{project_id}/_apis/distributedtask/hubs/{hub_name}/plans/{plan_id}/jobs/{job_id}/oidctoken?api-version=7.1-preview.1"

        # See https://docs.microsoft.com/en-us/azure/devops/pipelines/build/variables
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }

        # Set up the JSON payload for the request body
        payload = {
            'audience': audience
        }
        try:
            # Make the POST request
            response = requests.post(request_url, headers=headers, json=payload)
            response.raise_for_status() # Raise an exception for bad status codes

            # Return the OIDC token from the JSON response
            return response.json()['oidcToken']
        except requests.exceptions.RequestException as e:
            print(f"Error requesting OIDC token: {e}")
            return None
        