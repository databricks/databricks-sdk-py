# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

from dataclasses import dataclass
from enum import Enum
from typing import Optional, Dict, List, Any


# all definitions in this file are in alphabetical order


@dataclass
class CreateCredentials:

    # Git provider. This field is case-insensitive. The available Git providers
    # are awsCodeCommit, azureDevOpsServices,
    git_provider: str
    # Git username.
    git_username: str
    # The personal access token used to authenticate to the corresponding Git
    # provider.
    personal_access_token: str

    def as_request(self) -> (dict, dict):
        createCredentials_query, createCredentials_body = {}, {}
        if self.git_provider:
            createCredentials_body["git_provider"] = self.git_provider
        if self.git_username:
            createCredentials_body["git_username"] = self.git_username
        if self.personal_access_token:
            createCredentials_body["personal_access_token"] = self.personal_access_token

        return createCredentials_query, createCredentials_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "CreateCredentials":
        return cls(
            git_provider=d.get("git_provider", None),
            git_username=d.get("git_username", None),
            personal_access_token=d.get("personal_access_token", None),
        )


@dataclass
class CreateCredentialsResponse:

    # ID of the credential object in the workspace.
    credential_id: int
    # Git provider. This field is case-insensitive. The available Git providers
    # are awsCodeCommit, azureDevOpsServices,
    git_provider: str
    # Git username.
    git_username: str

    def as_request(self) -> (dict, dict):
        createCredentialsResponse_query, createCredentialsResponse_body = {}, {}
        if self.credential_id:
            createCredentialsResponse_body["credential_id"] = self.credential_id
        if self.git_provider:
            createCredentialsResponse_body["git_provider"] = self.git_provider
        if self.git_username:
            createCredentialsResponse_body["git_username"] = self.git_username

        return createCredentialsResponse_query, createCredentialsResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "CreateCredentialsResponse":
        return cls(
            credential_id=d.get("credential_id", None),
            git_provider=d.get("git_provider", None),
            git_username=d.get("git_username", None),
        )


@dataclass
class CredentialInfo:

    # ID of the credential object in the workspace.
    credential_id: int
    # Git provider. This field is case-insensitive. The available Git providers
    # are awsCodeCommit, azureDevOpsServices,
    git_provider: str
    # Git username.
    git_username: str

    def as_request(self) -> (dict, dict):
        credentialInfo_query, credentialInfo_body = {}, {}
        if self.credential_id:
            credentialInfo_body["credential_id"] = self.credential_id
        if self.git_provider:
            credentialInfo_body["git_provider"] = self.git_provider
        if self.git_username:
            credentialInfo_body["git_username"] = self.git_username

        return credentialInfo_query, credentialInfo_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "CredentialInfo":
        return cls(
            credential_id=d.get("credential_id", None),
            git_provider=d.get("git_provider", None),
            git_username=d.get("git_username", None),
        )


@dataclass
class Delete:
    """Delete a credential"""

    # The ID for the corresponding credential to access.
    credential_id: int  # path

    def as_request(self) -> (dict, dict):
        delete_query, delete_body = {}, {}
        if self.credential_id:
            delete_body["credential_id"] = self.credential_id

        return delete_query, delete_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "Delete":
        return cls(
            credential_id=d.get("credential_id", None),
        )


@dataclass
class Get:
    """Get a credential entry"""

    # The ID for the corresponding credential to access.
    credential_id: int  # path

    def as_request(self) -> (dict, dict):
        get_query, get_body = {}, {}
        if self.credential_id:
            get_body["credential_id"] = self.credential_id

        return get_query, get_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "Get":
        return cls(
            credential_id=d.get("credential_id", None),
        )


@dataclass
class GetCredentialsResponse:

    credentials: "List[CredentialInfo]"

    def as_request(self) -> (dict, dict):
        getCredentialsResponse_query, getCredentialsResponse_body = {}, {}
        if self.credentials:
            getCredentialsResponse_body["credentials"] = [
                v.as_request()[1] for v in self.credentials
            ]

        return getCredentialsResponse_query, getCredentialsResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "GetCredentialsResponse":
        return cls(
            credentials=[CredentialInfo.from_dict(v) for v in d["credentials"]]
            if "credentials" in d
            else None,
        )


@dataclass
class UpdateCredentials:

    # The ID for the corresponding credential to access.
    credential_id: int  # path
    # Git provider. This field is case-insensitive. The available Git providers
    # are awsCodeCommit, azureDevOpsServices,
    git_provider: str
    # Git username.
    git_username: str
    # The personal access token used to authenticate to the corresponding Git
    # provider.
    personal_access_token: str

    def as_request(self) -> (dict, dict):
        updateCredentials_query, updateCredentials_body = {}, {}
        if self.credential_id:
            updateCredentials_body["credential_id"] = self.credential_id
        if self.git_provider:
            updateCredentials_body["git_provider"] = self.git_provider
        if self.git_username:
            updateCredentials_body["git_username"] = self.git_username
        if self.personal_access_token:
            updateCredentials_body["personal_access_token"] = self.personal_access_token

        return updateCredentials_query, updateCredentials_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "UpdateCredentials":
        return cls(
            credential_id=d.get("credential_id", None),
            git_provider=d.get("git_provider", None),
            git_username=d.get("git_username", None),
            personal_access_token=d.get("personal_access_token", None),
        )


class GitCredentialsAPI:
    def __init__(self, api_client):
        self._api = api_client

    def create(self, request: CreateCredentials) -> CreateCredentialsResponse:
        """Create a credential entry.

        Creates a Git credential entry for the user. Only one Git credential per
        user is supported, so any attempts to create credentials if an entry
        already exists will fail. Use the PATCH endpoint to update existing
        credentials, or the DELETE endpoint to delete existing credentials."""
        query, body = request.as_request()
        json = self._api.do("POST", "/api/2.0/git-credentials", query=query, body=body)
        return CreateCredentialsResponse.from_dict(json)

    def delete(self, request: Delete):
        """Delete a credential.

        Deletes the specified Git credential."""
        query, body = request.as_request()
        self._api.do(
            "DELETE",
            f"/api/2.0/git-credentials/{request.credential_id}",
            query=query,
            body=body,
        )

    def get(self, request: Get) -> CredentialInfo:
        """Get a credential entry.

        Gets the Git credential with the specified credential ID."""
        query, body = request.as_request()
        json = self._api.do(
            "GET",
            f"/api/2.0/git-credentials/{request.credential_id}",
            query=query,
            body=body,
        )
        return CredentialInfo.from_dict(json)

    def list(self) -> GetCredentialsResponse:
        """Get Git credentials.

        Lists the calling user's Git credentials. One credential per user is
        supported."""

        json = self._api.do("GET", "/api/2.0/git-credentials")
        return GetCredentialsResponse.from_dict(json)

    def update(self, request: UpdateCredentials):
        """Update a credential.

        Updates the specified Git credential."""
        query, body = request.as_request()
        self._api.do(
            "PATCH",
            f"/api/2.0/git-credentials/{request.credential_id}",
            query=query,
            body=body,
        )
