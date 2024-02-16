# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import Dict, Iterator, List, Optional

from ._internal import _from_dict, _repeated_dict

_LOG = logging.getLogger('databricks.sdk')

# all definitions in this file are in alphabetical order


@dataclass
class CreateCustomAppIntegration:
    name: str
    """name of the custom oauth app"""

    redirect_urls: List[str]
    """List of oauth redirect urls"""

    confidential: Optional[bool] = None
    """indicates if an oauth client-secret should be generated"""

    scopes: Optional[List[str]] = None
    """OAuth scopes granted to the application. Supported scopes: all-apis, sql, offline_access,
    openid, profile, email."""

    token_access_policy: Optional[TokenAccessPolicy] = None
    """Token access policy"""

    def as_dict(self) -> dict:
        """Serializes the CreateCustomAppIntegration into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.confidential is not None: body['confidential'] = self.confidential
        if self.name is not None: body['name'] = self.name
        if self.redirect_urls: body['redirect_urls'] = [v for v in self.redirect_urls]
        if self.scopes: body['scopes'] = [v for v in self.scopes]
        if self.token_access_policy: body['token_access_policy'] = self.token_access_policy.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> CreateCustomAppIntegration:
        """Deserializes the CreateCustomAppIntegration from a dictionary."""
        return cls(confidential=d.get('confidential', None),
                   name=d.get('name', None),
                   redirect_urls=d.get('redirect_urls', None),
                   scopes=d.get('scopes', None),
                   token_access_policy=_from_dict(d, 'token_access_policy', TokenAccessPolicy))


@dataclass
class CreateCustomAppIntegrationOutput:
    client_id: Optional[str] = None
    """oauth client-id generated by the Databricks"""

    client_secret: Optional[str] = None
    """oauth client-secret generated by the Databricks if this is a confidential oauth app
    client-secret will be generated."""

    integration_id: Optional[str] = None
    """unique integration id for the custom oauth app"""

    def as_dict(self) -> dict:
        """Serializes the CreateCustomAppIntegrationOutput into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.client_id is not None: body['client_id'] = self.client_id
        if self.client_secret is not None: body['client_secret'] = self.client_secret
        if self.integration_id is not None: body['integration_id'] = self.integration_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> CreateCustomAppIntegrationOutput:
        """Deserializes the CreateCustomAppIntegrationOutput from a dictionary."""
        return cls(client_id=d.get('client_id', None),
                   client_secret=d.get('client_secret', None),
                   integration_id=d.get('integration_id', None))


@dataclass
class CreatePublishedAppIntegration:
    app_id: Optional[str] = None
    """app_id of the oauth published app integration. For example power-bi, tableau-deskop"""

    token_access_policy: Optional[TokenAccessPolicy] = None
    """Token access policy"""

    def as_dict(self) -> dict:
        """Serializes the CreatePublishedAppIntegration into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.app_id is not None: body['app_id'] = self.app_id
        if self.token_access_policy: body['token_access_policy'] = self.token_access_policy.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> CreatePublishedAppIntegration:
        """Deserializes the CreatePublishedAppIntegration from a dictionary."""
        return cls(app_id=d.get('app_id', None),
                   token_access_policy=_from_dict(d, 'token_access_policy', TokenAccessPolicy))


@dataclass
class CreatePublishedAppIntegrationOutput:
    integration_id: Optional[str] = None
    """unique integration id for the published oauth app"""

    def as_dict(self) -> dict:
        """Serializes the CreatePublishedAppIntegrationOutput into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.integration_id is not None: body['integration_id'] = self.integration_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> CreatePublishedAppIntegrationOutput:
        """Deserializes the CreatePublishedAppIntegrationOutput from a dictionary."""
        return cls(integration_id=d.get('integration_id', None))


@dataclass
class CreateServicePrincipalSecretResponse:
    create_time: Optional[str] = None
    """UTC time when the secret was created"""

    id: Optional[str] = None
    """ID of the secret"""

    secret: Optional[str] = None
    """Secret Value"""

    secret_hash: Optional[str] = None
    """Secret Hash"""

    status: Optional[str] = None
    """Status of the secret"""

    update_time: Optional[str] = None
    """UTC time when the secret was updated"""

    def as_dict(self) -> dict:
        """Serializes the CreateServicePrincipalSecretResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.create_time is not None: body['create_time'] = self.create_time
        if self.id is not None: body['id'] = self.id
        if self.secret is not None: body['secret'] = self.secret
        if self.secret_hash is not None: body['secret_hash'] = self.secret_hash
        if self.status is not None: body['status'] = self.status
        if self.update_time is not None: body['update_time'] = self.update_time
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> CreateServicePrincipalSecretResponse:
        """Deserializes the CreateServicePrincipalSecretResponse from a dictionary."""
        return cls(create_time=d.get('create_time', None),
                   id=d.get('id', None),
                   secret=d.get('secret', None),
                   secret_hash=d.get('secret_hash', None),
                   status=d.get('status', None),
                   update_time=d.get('update_time', None))


@dataclass
class GetCustomAppIntegrationOutput:
    client_id: Optional[str] = None
    """oauth client id of the custom oauth app"""

    confidential: Optional[bool] = None
    """indicates if an oauth client-secret should be generated"""

    integration_id: Optional[str] = None
    """ID of this custom app"""

    name: Optional[str] = None
    """name of the custom oauth app"""

    redirect_urls: Optional[List[str]] = None
    """List of oauth redirect urls"""

    token_access_policy: Optional[TokenAccessPolicy] = None
    """Token access policy"""

    def as_dict(self) -> dict:
        """Serializes the GetCustomAppIntegrationOutput into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.client_id is not None: body['client_id'] = self.client_id
        if self.confidential is not None: body['confidential'] = self.confidential
        if self.integration_id is not None: body['integration_id'] = self.integration_id
        if self.name is not None: body['name'] = self.name
        if self.redirect_urls: body['redirect_urls'] = [v for v in self.redirect_urls]
        if self.token_access_policy: body['token_access_policy'] = self.token_access_policy.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> GetCustomAppIntegrationOutput:
        """Deserializes the GetCustomAppIntegrationOutput from a dictionary."""
        return cls(client_id=d.get('client_id', None),
                   confidential=d.get('confidential', None),
                   integration_id=d.get('integration_id', None),
                   name=d.get('name', None),
                   redirect_urls=d.get('redirect_urls', None),
                   token_access_policy=_from_dict(d, 'token_access_policy', TokenAccessPolicy))


@dataclass
class GetCustomAppIntegrationsOutput:
    apps: Optional[List[GetCustomAppIntegrationOutput]] = None
    """Array of Custom OAuth App Integrations defined for the account."""

    def as_dict(self) -> dict:
        """Serializes the GetCustomAppIntegrationsOutput into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.apps: body['apps'] = [v.as_dict() for v in self.apps]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> GetCustomAppIntegrationsOutput:
        """Deserializes the GetCustomAppIntegrationsOutput from a dictionary."""
        return cls(apps=_repeated_dict(d, 'apps', GetCustomAppIntegrationOutput))


@dataclass
class GetPublishedAppIntegrationOutput:
    app_id: Optional[str] = None
    """app-id of the published app integration"""

    integration_id: Optional[str] = None
    """unique integration id for the published oauth app"""

    name: Optional[str] = None
    """name of the published oauth app"""

    token_access_policy: Optional[TokenAccessPolicy] = None
    """Token access policy"""

    def as_dict(self) -> dict:
        """Serializes the GetPublishedAppIntegrationOutput into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.app_id is not None: body['app_id'] = self.app_id
        if self.integration_id is not None: body['integration_id'] = self.integration_id
        if self.name is not None: body['name'] = self.name
        if self.token_access_policy: body['token_access_policy'] = self.token_access_policy.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> GetPublishedAppIntegrationOutput:
        """Deserializes the GetPublishedAppIntegrationOutput from a dictionary."""
        return cls(app_id=d.get('app_id', None),
                   integration_id=d.get('integration_id', None),
                   name=d.get('name', None),
                   token_access_policy=_from_dict(d, 'token_access_policy', TokenAccessPolicy))


@dataclass
class GetPublishedAppIntegrationsOutput:
    apps: Optional[List[GetPublishedAppIntegrationOutput]] = None
    """Array of Published OAuth App Integrations defined for the account."""

    def as_dict(self) -> dict:
        """Serializes the GetPublishedAppIntegrationsOutput into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.apps: body['apps'] = [v.as_dict() for v in self.apps]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> GetPublishedAppIntegrationsOutput:
        """Deserializes the GetPublishedAppIntegrationsOutput from a dictionary."""
        return cls(apps=_repeated_dict(d, 'apps', GetPublishedAppIntegrationOutput))


@dataclass
class GetPublishedAppsOutput:
    apps: Optional[List[PublishedAppOutput]] = None
    """Array of Published OAuth Apps."""

    next_page_token: Optional[str] = None
    """A token that can be used to get the next page of results. If not present, there are no more
    results to show."""

    def as_dict(self) -> dict:
        """Serializes the GetPublishedAppsOutput into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.apps: body['apps'] = [v.as_dict() for v in self.apps]
        if self.next_page_token is not None: body['next_page_token'] = self.next_page_token
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> GetPublishedAppsOutput:
        """Deserializes the GetPublishedAppsOutput from a dictionary."""
        return cls(apps=_repeated_dict(d, 'apps', PublishedAppOutput),
                   next_page_token=d.get('next_page_token', None))


@dataclass
class ListServicePrincipalSecretsResponse:
    secrets: Optional[List[SecretInfo]] = None
    """List of the secrets"""

    def as_dict(self) -> dict:
        """Serializes the ListServicePrincipalSecretsResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.secrets: body['secrets'] = [v.as_dict() for v in self.secrets]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ListServicePrincipalSecretsResponse:
        """Deserializes the ListServicePrincipalSecretsResponse from a dictionary."""
        return cls(secrets=_repeated_dict(d, 'secrets', SecretInfo))


@dataclass
class PublishedAppOutput:
    app_id: Optional[str] = None
    """Unique ID of the published OAuth app."""

    client_id: Optional[str] = None
    """Client ID of the published OAuth app. It is the client_id in the OAuth flow"""

    description: Optional[str] = None
    """Description of the published OAuth app."""

    is_confidential_client: Optional[bool] = None
    """Whether the published OAuth app is a confidential client. It is always false for published OAuth
    apps."""

    name: Optional[str] = None
    """Name of the published OAuth app."""

    redirect_urls: Optional[List[str]] = None
    """Redirect URLs of the published OAuth app."""

    scopes: Optional[List[str]] = None
    """Required scopes for the published OAuth app."""

    def as_dict(self) -> dict:
        """Serializes the PublishedAppOutput into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.app_id is not None: body['app_id'] = self.app_id
        if self.client_id is not None: body['client_id'] = self.client_id
        if self.description is not None: body['description'] = self.description
        if self.is_confidential_client is not None:
            body['is_confidential_client'] = self.is_confidential_client
        if self.name is not None: body['name'] = self.name
        if self.redirect_urls: body['redirect_urls'] = [v for v in self.redirect_urls]
        if self.scopes: body['scopes'] = [v for v in self.scopes]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> PublishedAppOutput:
        """Deserializes the PublishedAppOutput from a dictionary."""
        return cls(app_id=d.get('app_id', None),
                   client_id=d.get('client_id', None),
                   description=d.get('description', None),
                   is_confidential_client=d.get('is_confidential_client', None),
                   name=d.get('name', None),
                   redirect_urls=d.get('redirect_urls', None),
                   scopes=d.get('scopes', None))


@dataclass
class SecretInfo:
    create_time: Optional[str] = None
    """UTC time when the secret was created"""

    id: Optional[str] = None
    """ID of the secret"""

    secret_hash: Optional[str] = None
    """Secret Hash"""

    status: Optional[str] = None
    """Status of the secret"""

    update_time: Optional[str] = None
    """UTC time when the secret was updated"""

    def as_dict(self) -> dict:
        """Serializes the SecretInfo into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.create_time is not None: body['create_time'] = self.create_time
        if self.id is not None: body['id'] = self.id
        if self.secret_hash is not None: body['secret_hash'] = self.secret_hash
        if self.status is not None: body['status'] = self.status
        if self.update_time is not None: body['update_time'] = self.update_time
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> SecretInfo:
        """Deserializes the SecretInfo from a dictionary."""
        return cls(create_time=d.get('create_time', None),
                   id=d.get('id', None),
                   secret_hash=d.get('secret_hash', None),
                   status=d.get('status', None),
                   update_time=d.get('update_time', None))


@dataclass
class TokenAccessPolicy:
    access_token_ttl_in_minutes: Optional[int] = None
    """access token time to live in minutes"""

    refresh_token_ttl_in_minutes: Optional[int] = None
    """refresh token time to live in minutes"""

    def as_dict(self) -> dict:
        """Serializes the TokenAccessPolicy into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.access_token_ttl_in_minutes is not None:
            body['access_token_ttl_in_minutes'] = self.access_token_ttl_in_minutes
        if self.refresh_token_ttl_in_minutes is not None:
            body['refresh_token_ttl_in_minutes'] = self.refresh_token_ttl_in_minutes
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> TokenAccessPolicy:
        """Deserializes the TokenAccessPolicy from a dictionary."""
        return cls(access_token_ttl_in_minutes=d.get('access_token_ttl_in_minutes', None),
                   refresh_token_ttl_in_minutes=d.get('refresh_token_ttl_in_minutes', None))


@dataclass
class UpdateCustomAppIntegration:
    integration_id: Optional[str] = None
    """The oauth app integration ID."""

    redirect_urls: Optional[List[str]] = None
    """List of oauth redirect urls to be updated in the custom oauth app integration"""

    token_access_policy: Optional[TokenAccessPolicy] = None
    """Token access policy to be updated in the custom oauth app integration"""

    def as_dict(self) -> dict:
        """Serializes the UpdateCustomAppIntegration into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.integration_id is not None: body['integration_id'] = self.integration_id
        if self.redirect_urls: body['redirect_urls'] = [v for v in self.redirect_urls]
        if self.token_access_policy: body['token_access_policy'] = self.token_access_policy.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> UpdateCustomAppIntegration:
        """Deserializes the UpdateCustomAppIntegration from a dictionary."""
        return cls(integration_id=d.get('integration_id', None),
                   redirect_urls=d.get('redirect_urls', None),
                   token_access_policy=_from_dict(d, 'token_access_policy', TokenAccessPolicy))


@dataclass
class UpdatePublishedAppIntegration:
    integration_id: Optional[str] = None
    """The oauth app integration ID."""

    token_access_policy: Optional[TokenAccessPolicy] = None
    """Token access policy to be updated in the published oauth app integration"""

    def as_dict(self) -> dict:
        """Serializes the UpdatePublishedAppIntegration into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.integration_id is not None: body['integration_id'] = self.integration_id
        if self.token_access_policy: body['token_access_policy'] = self.token_access_policy.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> UpdatePublishedAppIntegration:
        """Deserializes the UpdatePublishedAppIntegration from a dictionary."""
        return cls(integration_id=d.get('integration_id', None),
                   token_access_policy=_from_dict(d, 'token_access_policy', TokenAccessPolicy))


class CustomAppIntegrationAPI:
    """These APIs enable administrators to manage custom oauth app integrations, which is required for
    adding/using Custom OAuth App Integration like Tableau Cloud for Databricks in AWS cloud."""

    def __init__(self, api_client):
        self._api = api_client

    def create(self,
               name: str,
               redirect_urls: List[str],
               *,
               confidential: Optional[bool] = None,
               scopes: Optional[List[str]] = None,
               token_access_policy: Optional[TokenAccessPolicy] = None) -> CreateCustomAppIntegrationOutput:
        """Create Custom OAuth App Integration.
        
        Create Custom OAuth App Integration.
        
        You can retrieve the custom oauth app integration via :method:CustomAppIntegration/get.
        
        :param name: str
          name of the custom oauth app
        :param redirect_urls: List[str]
          List of oauth redirect urls
        :param confidential: bool (optional)
          indicates if an oauth client-secret should be generated
        :param scopes: List[str] (optional)
          OAuth scopes granted to the application. Supported scopes: all-apis, sql, offline_access, openid,
          profile, email.
        :param token_access_policy: :class:`TokenAccessPolicy` (optional)
          Token access policy
        
        :returns: :class:`CreateCustomAppIntegrationOutput`
        """
        body = {}
        if confidential is not None: body['confidential'] = confidential
        if name is not None: body['name'] = name
        if redirect_urls is not None: body['redirect_urls'] = [v for v in redirect_urls]
        if scopes is not None: body['scopes'] = [v for v in scopes]
        if token_access_policy is not None: body['token_access_policy'] = token_access_policy.as_dict()
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        response_headers = []
        res = self._api.do('POST',
                           f'/api/2.0/accounts/{self._api.account_id}/oauth2/custom-app-integrations',
                           body=body,
                           headers=headers,
                           response_headers=response_headers)
        return CreateCustomAppIntegrationOutput.from_dict(res)

    def delete(self, integration_id: str):
        """Delete Custom OAuth App Integration.
        
        Delete an existing Custom OAuth App Integration. You can retrieve the custom oauth app integration via
        :method:CustomAppIntegration/get.
        
        :param integration_id: str
          The oauth app integration ID.
        
        
        """

        headers = {'Accept': 'application/json', }
        response_headers = []
        self._api.do(
            'DELETE',
            f'/api/2.0/accounts/{self._api.account_id}/oauth2/custom-app-integrations/{integration_id}',
            headers=headers,
            response_headers=response_headers)

    def get(self, integration_id: str) -> GetCustomAppIntegrationOutput:
        """Get OAuth Custom App Integration.
        
        Gets the Custom OAuth App Integration for the given integration id.
        
        :param integration_id: str
          The oauth app integration ID.
        
        :returns: :class:`GetCustomAppIntegrationOutput`
        """

        headers = {'Accept': 'application/json', }
        response_headers = []
        res = self._api.do(
            'GET',
            f'/api/2.0/accounts/{self._api.account_id}/oauth2/custom-app-integrations/{integration_id}',
            headers=headers,
            response_headers=response_headers)
        return GetCustomAppIntegrationOutput.from_dict(res)

    def list(self) -> Iterator[GetCustomAppIntegrationOutput]:
        """Get custom oauth app integrations.
        
        Get the list of custom oauth app integrations for the specified Databricks account
        
        :returns: Iterator over :class:`GetCustomAppIntegrationOutput`
        """

        headers = {'Accept': 'application/json', }
        response_headers = []
        json = self._api.do('GET',
                            f'/api/2.0/accounts/{self._api.account_id}/oauth2/custom-app-integrations',
                            headers=headers,
                            response_headers=response_headers)
        parsed = GetCustomAppIntegrationsOutput.from_dict(json).apps
        return parsed if parsed is not None else []

    def update(self,
               integration_id: str,
               *,
               redirect_urls: Optional[List[str]] = None,
               token_access_policy: Optional[TokenAccessPolicy] = None):
        """Updates Custom OAuth App Integration.
        
        Updates an existing custom OAuth App Integration. You can retrieve the custom oauth app integration
        via :method:CustomAppIntegration/get.
        
        :param integration_id: str
          The oauth app integration ID.
        :param redirect_urls: List[str] (optional)
          List of oauth redirect urls to be updated in the custom oauth app integration
        :param token_access_policy: :class:`TokenAccessPolicy` (optional)
          Token access policy to be updated in the custom oauth app integration
        
        
        """
        body = {}
        if redirect_urls is not None: body['redirect_urls'] = [v for v in redirect_urls]
        if token_access_policy is not None: body['token_access_policy'] = token_access_policy.as_dict()
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        response_headers = []
        self._api.do(
            'PATCH',
            f'/api/2.0/accounts/{self._api.account_id}/oauth2/custom-app-integrations/{integration_id}',
            body=body,
            headers=headers,
            response_headers=response_headers)


class OAuthPublishedAppsAPI:
    """These APIs enable administrators to view all the available published OAuth applications in Databricks.
    Administrators can add the published OAuth applications to their account through the OAuth Published App
    Integration APIs."""

    def __init__(self, api_client):
        self._api = api_client

    def list(self,
             *,
             page_size: Optional[int] = None,
             page_token: Optional[str] = None) -> Iterator[PublishedAppOutput]:
        """Get all the published OAuth apps.
        
        Get all the available published OAuth apps in Databricks.
        
        :param page_size: int (optional)
          The max number of OAuth published apps to return.
        :param page_token: str (optional)
          A token that can be used to get the next page of results.
        
        :returns: Iterator over :class:`PublishedAppOutput`
        """

        query = {}
        if page_size is not None: query['page_size'] = page_size
        if page_token is not None: query['page_token'] = page_token
        headers = {'Accept': 'application/json', }
        response_headers = []

        while True:
            json = self._api.do('GET',
                                f'/api/2.0/accounts/{self._api.account_id}/oauth2/published-apps/',
                                query=query,
                                headers=headers,
                                response_headers=response_headers)
            if 'apps' in json:
                for v in json['apps']:
                    yield PublishedAppOutput.from_dict(v)
            if 'next_page_token' not in json or not json['next_page_token']:
                return
            query['page_token'] = json['next_page_token']


class PublishedAppIntegrationAPI:
    """These APIs enable administrators to manage published oauth app integrations, which is required for
    adding/using Published OAuth App Integration like Tableau Desktop for Databricks in AWS cloud."""

    def __init__(self, api_client):
        self._api = api_client

    def create(
            self,
            *,
            app_id: Optional[str] = None,
            token_access_policy: Optional[TokenAccessPolicy] = None) -> CreatePublishedAppIntegrationOutput:
        """Create Published OAuth App Integration.
        
        Create Published OAuth App Integration.
        
        You can retrieve the published oauth app integration via :method:PublishedAppIntegration/get.
        
        :param app_id: str (optional)
          app_id of the oauth published app integration. For example power-bi, tableau-deskop
        :param token_access_policy: :class:`TokenAccessPolicy` (optional)
          Token access policy
        
        :returns: :class:`CreatePublishedAppIntegrationOutput`
        """
        body = {}
        if app_id is not None: body['app_id'] = app_id
        if token_access_policy is not None: body['token_access_policy'] = token_access_policy.as_dict()
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        response_headers = []
        res = self._api.do('POST',
                           f'/api/2.0/accounts/{self._api.account_id}/oauth2/published-app-integrations',
                           body=body,
                           headers=headers,
                           response_headers=response_headers)
        return CreatePublishedAppIntegrationOutput.from_dict(res)

    def delete(self, integration_id: str):
        """Delete Published OAuth App Integration.
        
        Delete an existing Published OAuth App Integration. You can retrieve the published oauth app
        integration via :method:PublishedAppIntegration/get.
        
        :param integration_id: str
          The oauth app integration ID.
        
        
        """

        headers = {'Accept': 'application/json', }
        response_headers = []
        self._api.do(
            'DELETE',
            f'/api/2.0/accounts/{self._api.account_id}/oauth2/published-app-integrations/{integration_id}',
            headers=headers,
            response_headers=response_headers)

    def get(self, integration_id: str) -> GetPublishedAppIntegrationOutput:
        """Get OAuth Published App Integration.
        
        Gets the Published OAuth App Integration for the given integration id.
        
        :param integration_id: str
          The oauth app integration ID.
        
        :returns: :class:`GetPublishedAppIntegrationOutput`
        """

        headers = {'Accept': 'application/json', }
        response_headers = []
        res = self._api.do(
            'GET',
            f'/api/2.0/accounts/{self._api.account_id}/oauth2/published-app-integrations/{integration_id}',
            headers=headers,
            response_headers=response_headers)
        return GetPublishedAppIntegrationOutput.from_dict(res)

    def list(self) -> Iterator[GetPublishedAppIntegrationOutput]:
        """Get published oauth app integrations.
        
        Get the list of published oauth app integrations for the specified Databricks account
        
        :returns: Iterator over :class:`GetPublishedAppIntegrationOutput`
        """

        headers = {'Accept': 'application/json', }
        response_headers = []
        json = self._api.do('GET',
                            f'/api/2.0/accounts/{self._api.account_id}/oauth2/published-app-integrations',
                            headers=headers,
                            response_headers=response_headers)
        parsed = GetPublishedAppIntegrationsOutput.from_dict(json).apps
        return parsed if parsed is not None else []

    def update(self, integration_id: str, *, token_access_policy: Optional[TokenAccessPolicy] = None):
        """Updates Published OAuth App Integration.
        
        Updates an existing published OAuth App Integration. You can retrieve the published oauth app
        integration via :method:PublishedAppIntegration/get.
        
        :param integration_id: str
          The oauth app integration ID.
        :param token_access_policy: :class:`TokenAccessPolicy` (optional)
          Token access policy to be updated in the published oauth app integration
        
        
        """
        body = {}
        if token_access_policy is not None: body['token_access_policy'] = token_access_policy.as_dict()
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        response_headers = []
        self._api.do(
            'PATCH',
            f'/api/2.0/accounts/{self._api.account_id}/oauth2/published-app-integrations/{integration_id}',
            body=body,
            headers=headers,
            response_headers=response_headers)


class ServicePrincipalSecretsAPI:
    """These APIs enable administrators to manage service principal secrets.
    
    You can use the generated secrets to obtain OAuth access tokens for a service principal, which can then be
    used to access Databricks Accounts and Workspace APIs. For more information, see [Authentication using
    OAuth tokens for service principals],
    
    In addition, the generated secrets can be used to configure the Databricks Terraform Provider to
    authenticate with the service principal. For more information, see [Databricks Terraform Provider].
    
    [Authentication using OAuth tokens for service principals]: https://docs.databricks.com/dev-tools/authentication-oauth.html
    [Databricks Terraform Provider]: https://github.com/databricks/terraform-provider-databricks/blob/master/docs/index.md#authenticating-with-service-principal"""

    def __init__(self, api_client):
        self._api = api_client

    def create(self, service_principal_id: int) -> CreateServicePrincipalSecretResponse:
        """Create service principal secret.
        
        Create a secret for the given service principal.
        
        :param service_principal_id: int
          The service principal ID.
        
        :returns: :class:`CreateServicePrincipalSecretResponse`
        """

        headers = {'Accept': 'application/json', }
        response_headers = []
        res = self._api.do(
            'POST',
            f'/api/2.0/accounts/{self._api.account_id}/servicePrincipals/{service_principal_id}/credentials/secrets',
            headers=headers,
            response_headers=response_headers)
        return CreateServicePrincipalSecretResponse.from_dict(res)

    def delete(self, service_principal_id: int, secret_id: str):
        """Delete service principal secret.
        
        Delete a secret from the given service principal.
        
        :param service_principal_id: int
          The service principal ID.
        :param secret_id: str
          The secret ID.
        
        
        """

        headers = {}
        response_headers = []
        self._api.do(
            'DELETE',
            f'/api/2.0/accounts/{self._api.account_id}/servicePrincipals/{service_principal_id}/credentials/secrets/{secret_id}',
            headers=headers,
            response_headers=response_headers)

    def list(self, service_principal_id: int) -> Iterator[SecretInfo]:
        """List service principal secrets.
        
        List all secrets associated with the given service principal. This operation only returns information
        about the secrets themselves and does not include the secret values.
        
        :param service_principal_id: int
          The service principal ID.
        
        :returns: Iterator over :class:`SecretInfo`
        """

        headers = {'Accept': 'application/json', }
        response_headers = []
        json = self._api.do(
            'GET',
            f'/api/2.0/accounts/{self._api.account_id}/servicePrincipals/{service_principal_id}/credentials/secrets',
            headers=headers,
            response_headers=response_headers)
        parsed = ListServicePrincipalSecretsResponse.from_dict(json).secrets
        return parsed if parsed is not None else []
