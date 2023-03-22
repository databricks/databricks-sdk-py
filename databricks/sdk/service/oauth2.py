# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

import logging
from dataclasses import dataclass
from typing import Any, Dict, Iterator, List

from ._internal import _from_dict, _repeated

_LOG = logging.getLogger('databricks.sdk')

# all definitions in this file are in alphabetical order


@dataclass
class CreateCustomAppIntegration:
    name: str
    redirect_urls: 'List[str]'
    confidential: bool = None
    token_access_policy: 'TokenAccessPolicy' = None

    def as_dict(self) -> dict:
        body = {}
        if self.confidential: body['confidential'] = self.confidential
        if self.name: body['name'] = self.name
        if self.redirect_urls: body['redirect_urls'] = [v for v in self.redirect_urls]
        if self.token_access_policy: body['token_access_policy'] = self.token_access_policy.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateCustomAppIntegration':
        return cls(confidential=d.get('confidential', None),
                   name=d.get('name', None),
                   redirect_urls=d.get('redirect_urls', None),
                   token_access_policy=_from_dict(d, 'token_access_policy', TokenAccessPolicy))


@dataclass
class CreateCustomAppIntegrationOutput:
    client_id: str = None
    client_secret: str = None
    integration_id: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.client_id: body['client_id'] = self.client_id
        if self.client_secret: body['client_secret'] = self.client_secret
        if self.integration_id: body['integration_id'] = self.integration_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateCustomAppIntegrationOutput':
        return cls(client_id=d.get('client_id', None),
                   client_secret=d.get('client_secret', None),
                   integration_id=d.get('integration_id', None))


@dataclass
class CreateOAuthEnrollment:
    enable_all_published_apps: bool = None

    def as_dict(self) -> dict:
        body = {}
        if self.enable_all_published_apps: body['enable_all_published_apps'] = self.enable_all_published_apps
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateOAuthEnrollment':
        return cls(enable_all_published_apps=d.get('enable_all_published_apps', None))


@dataclass
class CreatePublishedAppIntegration:
    app_id: str = None
    token_access_policy: 'TokenAccessPolicy' = None

    def as_dict(self) -> dict:
        body = {}
        if self.app_id: body['app_id'] = self.app_id
        if self.token_access_policy: body['token_access_policy'] = self.token_access_policy.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreatePublishedAppIntegration':
        return cls(app_id=d.get('app_id', None),
                   token_access_policy=_from_dict(d, 'token_access_policy', TokenAccessPolicy))


@dataclass
class CreatePublishedAppIntegrationOutput:
    integration_id: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.integration_id: body['integration_id'] = self.integration_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreatePublishedAppIntegrationOutput':
        return cls(integration_id=d.get('integration_id', None))


@dataclass
class DeleteCustomAppIntegrationRequest:
    """Delete Custom OAuth App Integration"""

    integration_id: str


@dataclass
class DeletePublishedAppIntegrationRequest:
    """Delete Published OAuth App Integration"""

    integration_id: str


@dataclass
class GetCustomAppIntegrationOutput:
    client_id: str = None
    confidential: bool = None
    integration_id: str = None
    name: str = None
    redirect_urls: 'List[str]' = None
    token_access_policy: 'TokenAccessPolicy' = None

    def as_dict(self) -> dict:
        body = {}
        if self.client_id: body['client_id'] = self.client_id
        if self.confidential: body['confidential'] = self.confidential
        if self.integration_id: body['integration_id'] = self.integration_id
        if self.name: body['name'] = self.name
        if self.redirect_urls: body['redirect_urls'] = [v for v in self.redirect_urls]
        if self.token_access_policy: body['token_access_policy'] = self.token_access_policy.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetCustomAppIntegrationOutput':
        return cls(client_id=d.get('client_id', None),
                   confidential=d.get('confidential', None),
                   integration_id=d.get('integration_id', None),
                   name=d.get('name', None),
                   redirect_urls=d.get('redirect_urls', None),
                   token_access_policy=_from_dict(d, 'token_access_policy', TokenAccessPolicy))


@dataclass
class GetCustomAppIntegrationRequest:
    """Get OAuth Custom App Integration"""

    integration_id: str


@dataclass
class GetCustomAppIntegrationsOutput:
    apps: 'List[GetCustomAppIntegrationOutput]' = None

    def as_dict(self) -> dict:
        body = {}
        if self.apps: body['apps'] = [v.as_dict() for v in self.apps]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetCustomAppIntegrationsOutput':
        return cls(apps=_repeated(d, 'apps', GetCustomAppIntegrationOutput))


@dataclass
class GetPublishedAppIntegrationOutput:
    app_id: str = None
    integration_id: str = None
    name: str = None
    token_access_policy: 'TokenAccessPolicy' = None

    def as_dict(self) -> dict:
        body = {}
        if self.app_id: body['app_id'] = self.app_id
        if self.integration_id: body['integration_id'] = self.integration_id
        if self.name: body['name'] = self.name
        if self.token_access_policy: body['token_access_policy'] = self.token_access_policy.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetPublishedAppIntegrationOutput':
        return cls(app_id=d.get('app_id', None),
                   integration_id=d.get('integration_id', None),
                   name=d.get('name', None),
                   token_access_policy=_from_dict(d, 'token_access_policy', TokenAccessPolicy))


@dataclass
class GetPublishedAppIntegrationRequest:
    """Get OAuth Published App Integration"""

    integration_id: str


@dataclass
class GetPublishedAppIntegrationsOutput:
    apps: 'List[GetPublishedAppIntegrationOutput]' = None

    def as_dict(self) -> dict:
        body = {}
        if self.apps: body['apps'] = [v.as_dict() for v in self.apps]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetPublishedAppIntegrationsOutput':
        return cls(apps=_repeated(d, 'apps', GetPublishedAppIntegrationOutput))


@dataclass
class OAuthEnrollmentStatus:
    is_enabled: bool = None

    def as_dict(self) -> dict:
        body = {}
        if self.is_enabled: body['is_enabled'] = self.is_enabled
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'OAuthEnrollmentStatus':
        return cls(is_enabled=d.get('is_enabled', None))


@dataclass
class TokenAccessPolicy:
    access_token_ttl_in_minutes: Any = None
    refresh_token_ttl_in_minutes: Any = None

    def as_dict(self) -> dict:
        body = {}
        if self.access_token_ttl_in_minutes:
            body['access_token_ttl_in_minutes'] = self.access_token_ttl_in_minutes
        if self.refresh_token_ttl_in_minutes:
            body['refresh_token_ttl_in_minutes'] = self.refresh_token_ttl_in_minutes
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'TokenAccessPolicy':
        return cls(access_token_ttl_in_minutes=d.get('access_token_ttl_in_minutes', None),
                   refresh_token_ttl_in_minutes=d.get('refresh_token_ttl_in_minutes', None))


@dataclass
class UpdateCustomAppIntegration:
    integration_id: str
    redirect_urls: 'List[str]' = None
    token_access_policy: 'TokenAccessPolicy' = None

    def as_dict(self) -> dict:
        body = {}
        if self.integration_id: body['integration_id'] = self.integration_id
        if self.redirect_urls: body['redirect_urls'] = [v for v in self.redirect_urls]
        if self.token_access_policy: body['token_access_policy'] = self.token_access_policy.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'UpdateCustomAppIntegration':
        return cls(integration_id=d.get('integration_id', None),
                   redirect_urls=d.get('redirect_urls', None),
                   token_access_policy=_from_dict(d, 'token_access_policy', TokenAccessPolicy))


@dataclass
class UpdatePublishedAppIntegration:
    integration_id: str
    token_access_policy: 'TokenAccessPolicy' = None

    def as_dict(self) -> dict:
        body = {}
        if self.integration_id: body['integration_id'] = self.integration_id
        if self.token_access_policy: body['token_access_policy'] = self.token_access_policy.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'UpdatePublishedAppIntegration':
        return cls(integration_id=d.get('integration_id', None),
                   token_access_policy=_from_dict(d, 'token_access_policy', TokenAccessPolicy))


class CustomAppIntegrationAPI:
    """These APIs enable administrators to manage custom oauth app integrations, which is required for
    adding/using Custom OAuth App Integration like Tableau Cloud for Databricks in AWS cloud.
    
    **Note:** You can only add/use the OAuth custom application integrations when OAuth enrollment status is
    enabled. For more details see :method:OAuthEnrollment/create"""

    def __init__(self, api_client):
        self._api = api_client

    def create(self,
               name: str,
               redirect_urls: List[str],
               *,
               confidential: bool = None,
               token_access_policy: TokenAccessPolicy = None,
               **kwargs) -> CreateCustomAppIntegrationOutput:
        """Create Custom OAuth App Integration.
        
        Create Custom OAuth App Integration.
        
        You can retrieve the custom oauth app integration via :method:get."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = CreateCustomAppIntegration(confidential=confidential,
                                                 name=name,
                                                 redirect_urls=redirect_urls,
                                                 token_access_policy=token_access_policy)
        body = request.as_dict()

        json = self._api.do('POST',
                            f'/api/2.0/accounts/{self._api.account_id}/oauth2/custom-app-integrations',
                            body=body)
        return CreateCustomAppIntegrationOutput.from_dict(json)

    def delete(self, integration_id: str, **kwargs):
        """Delete Custom OAuth App Integration.
        
        Delete an existing Custom OAuth App Integration. You can retrieve the custom oauth app integration via
        :method:get."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = DeleteCustomAppIntegrationRequest(integration_id=integration_id)

        self._api.do(
            'DELETE',
            f'/api/2.0/accounts/{self._api.account_id}/oauth2/custom-app-integrations/{request.integration_id}'
        )

    def get(self, integration_id: str, **kwargs) -> GetCustomAppIntegrationOutput:
        """Get OAuth Custom App Integration.
        
        Gets the Custom OAuth App Integration for the given integration id."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GetCustomAppIntegrationRequest(integration_id=integration_id)

        json = self._api.do(
            'GET',
            f'/api/2.0/accounts/{self._api.account_id}/oauth2/custom-app-integrations/{request.integration_id}'
        )
        return GetCustomAppIntegrationOutput.from_dict(json)

    def list(self) -> Iterator[GetCustomAppIntegrationOutput]:
        """Get custom oauth app integrations.
        
        Get the list of custom oauth app integrations for the specified Databricks Account"""

        json = self._api.do('GET', f'/api/2.0/accounts/{self._api.account_id}/oauth2/custom-app-integrations')
        return [GetCustomAppIntegrationOutput.from_dict(v) for v in json.get('apps', [])]

    def update(self,
               integration_id: str,
               *,
               redirect_urls: List[str] = None,
               token_access_policy: TokenAccessPolicy = None,
               **kwargs):
        """Updates Custom OAuth App Integration.
        
        Updates an existing custom OAuth App Integration. You can retrieve the custom oauth app integration
        via :method:get."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = UpdateCustomAppIntegration(integration_id=integration_id,
                                                 redirect_urls=redirect_urls,
                                                 token_access_policy=token_access_policy)
        body = request.as_dict()
        self._api.do(
            'PATCH',
            f'/api/2.0/accounts/{self._api.account_id}/oauth2/custom-app-integrations/{request.integration_id}',
            body=body)


class OAuthEnrollmentAPI:
    """These APIs enable administrators to enroll OAuth for their accounts, which is required for adding/using
    any OAuth published/custom application integration.
    
    **Note:** Your account must be on the E2 version to use these APIs, this is because OAuth is only
    supported on the E2 version."""

    def __init__(self, api_client):
        self._api = api_client

    def create(self, *, enable_all_published_apps: bool = None, **kwargs):
        """Create OAuth Enrollment request.
        
        Create an OAuth Enrollment request to enroll OAuth for this account and optionally enable the OAuth
        integration for all the partner applications in the account.
        
        The parter applications are: - Power BI - Tableau Desktop - Databricks CLI
        
        The enrollment is executed asynchronously, so the API will return 204 immediately. The actual
        enrollment take a few minutes, you can check the status via API :method:get."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = CreateOAuthEnrollment(enable_all_published_apps=enable_all_published_apps)
        body = request.as_dict()
        self._api.do('POST', f'/api/2.0/accounts/{self._api.account_id}/oauth2/enrollment', body=body)

    def get(self) -> OAuthEnrollmentStatus:
        """Get OAuth enrollment status.
        
        Gets the OAuth enrollment status for this Account.
        
        You can only add/use the OAuth published/custom application integrations when OAuth enrollment status
        is enabled."""

        json = self._api.do('GET', f'/api/2.0/accounts/{self._api.account_id}/oauth2/enrollment')
        return OAuthEnrollmentStatus.from_dict(json)


class PublishedAppIntegrationAPI:
    """These APIs enable administrators to manage published oauth app integrations, which is required for
    adding/using Published OAuth App Integration like Tableau Cloud for Databricks in AWS cloud.
    
    **Note:** You can only add/use the OAuth published application integrations when OAuth enrollment status
    is enabled. For more details see :method:OAuthEnrollment/create"""

    def __init__(self, api_client):
        self._api = api_client

    def create(self,
               *,
               app_id: str = None,
               token_access_policy: TokenAccessPolicy = None,
               **kwargs) -> CreatePublishedAppIntegrationOutput:
        """Create Published OAuth App Integration.
        
        Create Published OAuth App Integration.
        
        You can retrieve the published oauth app integration via :method:get."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = CreatePublishedAppIntegration(app_id=app_id, token_access_policy=token_access_policy)
        body = request.as_dict()

        json = self._api.do('POST',
                            f'/api/2.0/accounts/{self._api.account_id}/oauth2/published-app-integrations',
                            body=body)
        return CreatePublishedAppIntegrationOutput.from_dict(json)

    def delete(self, integration_id: str, **kwargs):
        """Delete Published OAuth App Integration.
        
        Delete an existing Published OAuth App Integration. You can retrieve the published oauth app
        integration via :method:get."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = DeletePublishedAppIntegrationRequest(integration_id=integration_id)

        self._api.do(
            'DELETE',
            f'/api/2.0/accounts/{self._api.account_id}/oauth2/published-app-integrations/{request.integration_id}'
        )

    def get(self, integration_id: str, **kwargs) -> GetPublishedAppIntegrationOutput:
        """Get OAuth Published App Integration.
        
        Gets the Published OAuth App Integration for the given integration id."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GetPublishedAppIntegrationRequest(integration_id=integration_id)

        json = self._api.do(
            'GET',
            f'/api/2.0/accounts/{self._api.account_id}/oauth2/published-app-integrations/{request.integration_id}'
        )
        return GetPublishedAppIntegrationOutput.from_dict(json)

    def list(self) -> Iterator[GetPublishedAppIntegrationOutput]:
        """Get published oauth app integrations.
        
        Get the list of published oauth app integrations for the specified Databricks Account"""

        json = self._api.do('GET',
                            f'/api/2.0/accounts/{self._api.account_id}/oauth2/published-app-integrations')
        return [GetPublishedAppIntegrationOutput.from_dict(v) for v in json.get('apps', [])]

    def update(self, integration_id: str, *, token_access_policy: TokenAccessPolicy = None, **kwargs):
        """Updates Published OAuth App Integration.
        
        Updates an existing published OAuth App Integration. You can retrieve the published oauth app
        integration via :method:get."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = UpdatePublishedAppIntegration(integration_id=integration_id,
                                                    token_access_policy=token_access_policy)
        body = request.as_dict()
        self._api.do(
            'PATCH',
            f'/api/2.0/accounts/{self._api.account_id}/oauth2/published-app-integrations/{request.integration_id}',
            body=body)
