# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

import logging
from dataclasses import dataclass
from typing import Dict, Iterator, List, Optional

from ._internal import _from_dict, _repeated

_LOG = logging.getLogger('databricks.sdk')

# all definitions in this file are in alphabetical order


@dataclass
class CreateCustomAppIntegration:
    name: str
    redirect_urls: 'List[str]'
    confidential: Optional[bool] = None
    token_access_policy: Optional['TokenAccessPolicy'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.confidential is not None: body['confidential'] = self.confidential
        if self.name is not None: body['name'] = self.name
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
    client_id: Optional[str] = None
    client_secret: Optional[str] = None
    integration_id: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.client_id is not None: body['client_id'] = self.client_id
        if self.client_secret is not None: body['client_secret'] = self.client_secret
        if self.integration_id is not None: body['integration_id'] = self.integration_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateCustomAppIntegrationOutput':
        return cls(client_id=d.get('client_id', None),
                   client_secret=d.get('client_secret', None),
                   integration_id=d.get('integration_id', None))


@dataclass
class CreateOAuthEnrollment:
    enable_all_published_apps: Optional[bool] = None

    def as_dict(self) -> dict:
        body = {}
        if self.enable_all_published_apps is not None:
            body['enable_all_published_apps'] = self.enable_all_published_apps
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateOAuthEnrollment':
        return cls(enable_all_published_apps=d.get('enable_all_published_apps', None))


@dataclass
class CreatePublishedAppIntegration:
    app_id: Optional[str] = None
    token_access_policy: Optional['TokenAccessPolicy'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.app_id is not None: body['app_id'] = self.app_id
        if self.token_access_policy: body['token_access_policy'] = self.token_access_policy.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreatePublishedAppIntegration':
        return cls(app_id=d.get('app_id', None),
                   token_access_policy=_from_dict(d, 'token_access_policy', TokenAccessPolicy))


@dataclass
class CreatePublishedAppIntegrationOutput:
    integration_id: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.integration_id is not None: body['integration_id'] = self.integration_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreatePublishedAppIntegrationOutput':
        return cls(integration_id=d.get('integration_id', None))


@dataclass
class CreateServicePrincipalSecretRequest:
    """Create service principal secret"""

    service_principal_id: int


@dataclass
class CreateServicePrincipalSecretResponse:
    create_time: Optional[str] = None
    id: Optional[str] = None
    secret: Optional[str] = None
    secret_hash: Optional[str] = None
    status: Optional[str] = None
    update_time: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.create_time is not None: body['create_time'] = self.create_time
        if self.id is not None: body['id'] = self.id
        if self.secret is not None: body['secret'] = self.secret
        if self.secret_hash is not None: body['secret_hash'] = self.secret_hash
        if self.status is not None: body['status'] = self.status
        if self.update_time is not None: body['update_time'] = self.update_time
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateServicePrincipalSecretResponse':
        return cls(create_time=d.get('create_time', None),
                   id=d.get('id', None),
                   secret=d.get('secret', None),
                   secret_hash=d.get('secret_hash', None),
                   status=d.get('status', None),
                   update_time=d.get('update_time', None))


@dataclass
class DeleteCustomAppIntegrationRequest:
    """Delete Custom OAuth App Integration"""

    integration_id: str


@dataclass
class DeletePublishedAppIntegrationRequest:
    """Delete Published OAuth App Integration"""

    integration_id: str


@dataclass
class DeleteServicePrincipalSecretRequest:
    """Delete service principal secret"""

    service_principal_id: int
    secret_id: str


@dataclass
class GetCustomAppIntegrationOutput:
    client_id: Optional[str] = None
    confidential: Optional[bool] = None
    integration_id: Optional[str] = None
    name: Optional[str] = None
    redirect_urls: Optional['List[str]'] = None
    token_access_policy: Optional['TokenAccessPolicy'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.client_id is not None: body['client_id'] = self.client_id
        if self.confidential is not None: body['confidential'] = self.confidential
        if self.integration_id is not None: body['integration_id'] = self.integration_id
        if self.name is not None: body['name'] = self.name
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
    apps: Optional['List[GetCustomAppIntegrationOutput]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.apps: body['apps'] = [v.as_dict() for v in self.apps]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetCustomAppIntegrationsOutput':
        return cls(apps=_repeated(d, 'apps', GetCustomAppIntegrationOutput))


@dataclass
class GetPublishedAppIntegrationOutput:
    app_id: Optional[str] = None
    integration_id: Optional[str] = None
    name: Optional[str] = None
    token_access_policy: Optional['TokenAccessPolicy'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.app_id is not None: body['app_id'] = self.app_id
        if self.integration_id is not None: body['integration_id'] = self.integration_id
        if self.name is not None: body['name'] = self.name
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
    apps: Optional['List[GetPublishedAppIntegrationOutput]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.apps: body['apps'] = [v.as_dict() for v in self.apps]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetPublishedAppIntegrationsOutput':
        return cls(apps=_repeated(d, 'apps', GetPublishedAppIntegrationOutput))


@dataclass
class ListServicePrincipalSecretsRequest:
    """List service principal secrets"""

    service_principal_id: int


@dataclass
class ListServicePrincipalSecretsResponse:
    secrets: Optional['List[SecretInfo]'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.secrets: body['secrets'] = [v.as_dict() for v in self.secrets]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListServicePrincipalSecretsResponse':
        return cls(secrets=_repeated(d, 'secrets', SecretInfo))


@dataclass
class OAuthEnrollmentStatus:
    is_enabled: Optional[bool] = None

    def as_dict(self) -> dict:
        body = {}
        if self.is_enabled is not None: body['is_enabled'] = self.is_enabled
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'OAuthEnrollmentStatus':
        return cls(is_enabled=d.get('is_enabled', None))


@dataclass
class SecretInfo:
    create_time: Optional[str] = None
    id: Optional[str] = None
    secret_hash: Optional[str] = None
    status: Optional[str] = None
    update_time: Optional[str] = None

    def as_dict(self) -> dict:
        body = {}
        if self.create_time is not None: body['create_time'] = self.create_time
        if self.id is not None: body['id'] = self.id
        if self.secret_hash is not None: body['secret_hash'] = self.secret_hash
        if self.status is not None: body['status'] = self.status
        if self.update_time is not None: body['update_time'] = self.update_time
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'SecretInfo':
        return cls(create_time=d.get('create_time', None),
                   id=d.get('id', None),
                   secret_hash=d.get('secret_hash', None),
                   status=d.get('status', None),
                   update_time=d.get('update_time', None))


@dataclass
class TokenAccessPolicy:
    access_token_ttl_in_minutes: Optional[int] = None
    refresh_token_ttl_in_minutes: Optional[int] = None

    def as_dict(self) -> dict:
        body = {}
        if self.access_token_ttl_in_minutes is not None:
            body['access_token_ttl_in_minutes'] = self.access_token_ttl_in_minutes
        if self.refresh_token_ttl_in_minutes is not None:
            body['refresh_token_ttl_in_minutes'] = self.refresh_token_ttl_in_minutes
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'TokenAccessPolicy':
        return cls(access_token_ttl_in_minutes=d.get('access_token_ttl_in_minutes', None),
                   refresh_token_ttl_in_minutes=d.get('refresh_token_ttl_in_minutes', None))


@dataclass
class UpdateCustomAppIntegration:
    integration_id: Optional[str] = None
    redirect_urls: Optional['List[str]'] = None
    token_access_policy: Optional['TokenAccessPolicy'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.integration_id is not None: body['integration_id'] = self.integration_id
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
    integration_id: Optional[str] = None
    token_access_policy: Optional['TokenAccessPolicy'] = None

    def as_dict(self) -> dict:
        body = {}
        if self.integration_id is not None: body['integration_id'] = self.integration_id
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
               confidential: Optional[bool] = None,
               token_access_policy: Optional[TokenAccessPolicy] = None,
               **kwargs) -> CreateCustomAppIntegrationOutput:
        """Create Custom OAuth App Integration.
        
        Create Custom OAuth App Integration.
        
        You can retrieve the custom oauth app integration via :method:CustomAppIntegration/get.
        
        :param name: str
          name of the custom oauth app
        :param redirect_urls: List[str]
          List of oauth redirect urls
        :param confidential: bool (optional)
          indicates if an oauth client-secret should be generated
        :param token_access_policy: :class:`TokenAccessPolicy` (optional)
          Token access policy
        
        :returns: :class:`CreateCustomAppIntegrationOutput`
        """
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
        :method:CustomAppIntegration/get.
        
        :param integration_id: str
          The oauth app integration ID.
        
        
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = DeleteCustomAppIntegrationRequest(integration_id=integration_id)

        self._api.do(
            'DELETE',
            f'/api/2.0/accounts/{self._api.account_id}/oauth2/custom-app-integrations/{request.integration_id}'
        )

    def get(self, integration_id: str, **kwargs) -> GetCustomAppIntegrationOutput:
        """Get OAuth Custom App Integration.
        
        Gets the Custom OAuth App Integration for the given integration id.
        
        :param integration_id: str
          The oauth app integration ID.
        
        :returns: :class:`GetCustomAppIntegrationOutput`
        """
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
        
        Get the list of custom oauth app integrations for the specified Databricks account
        
        :returns: Iterator over :class:`GetCustomAppIntegrationOutput`
        """

        json = self._api.do('GET', f'/api/2.0/accounts/{self._api.account_id}/oauth2/custom-app-integrations')
        return [GetCustomAppIntegrationOutput.from_dict(v) for v in json.get('apps', [])]

    def update(self,
               integration_id: str,
               *,
               redirect_urls: Optional[List[str]] = None,
               token_access_policy: Optional[TokenAccessPolicy] = None,
               **kwargs):
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

    def create(self, *, enable_all_published_apps: Optional[bool] = None, **kwargs):
        """Create OAuth Enrollment request.
        
        Create an OAuth Enrollment request to enroll OAuth for this account and optionally enable the OAuth
        integration for all the partner applications in the account.
        
        The parter applications are: - Power BI - Tableau Desktop - Databricks CLI
        
        The enrollment is executed asynchronously, so the API will return 204 immediately. The actual
        enrollment take a few minutes, you can check the status via API :method:OAuthEnrollment/get.
        
        :param enable_all_published_apps: bool (optional)
          If true, enable OAuth for all the published applications in the account.
        
        
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = CreateOAuthEnrollment(enable_all_published_apps=enable_all_published_apps)
        body = request.as_dict()
        self._api.do('POST', f'/api/2.0/accounts/{self._api.account_id}/oauth2/enrollment', body=body)

    def get(self) -> OAuthEnrollmentStatus:
        """Get OAuth enrollment status.
        
        Gets the OAuth enrollment status for this Account.
        
        You can only add/use the OAuth published/custom application integrations when OAuth enrollment status
        is enabled.
        
        :returns: :class:`OAuthEnrollmentStatus`
        """

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
               app_id: Optional[str] = None,
               token_access_policy: Optional[TokenAccessPolicy] = None,
               **kwargs) -> CreatePublishedAppIntegrationOutput:
        """Create Published OAuth App Integration.
        
        Create Published OAuth App Integration.
        
        You can retrieve the published oauth app integration via :method:PublishedAppIntegration/get.
        
        :param app_id: str (optional)
          app_id of the oauth published app integration. For example power-bi, tableau-deskop
        :param token_access_policy: :class:`TokenAccessPolicy` (optional)
          Token access policy
        
        :returns: :class:`CreatePublishedAppIntegrationOutput`
        """
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
        integration via :method:PublishedAppIntegration/get.
        
        :param integration_id: str
          The oauth app integration ID.
        
        
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = DeletePublishedAppIntegrationRequest(integration_id=integration_id)

        self._api.do(
            'DELETE',
            f'/api/2.0/accounts/{self._api.account_id}/oauth2/published-app-integrations/{request.integration_id}'
        )

    def get(self, integration_id: str, **kwargs) -> GetPublishedAppIntegrationOutput:
        """Get OAuth Published App Integration.
        
        Gets the Published OAuth App Integration for the given integration id.
        
        :param integration_id: str
          The oauth app integration ID.
        
        :returns: :class:`GetPublishedAppIntegrationOutput`
        """
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
        
        Get the list of published oauth app integrations for the specified Databricks account
        
        :returns: Iterator over :class:`GetPublishedAppIntegrationOutput`
        """

        json = self._api.do('GET',
                            f'/api/2.0/accounts/{self._api.account_id}/oauth2/published-app-integrations')
        return [GetPublishedAppIntegrationOutput.from_dict(v) for v in json.get('apps', [])]

    def update(self,
               integration_id: str,
               *,
               token_access_policy: Optional[TokenAccessPolicy] = None,
               **kwargs):
        """Updates Published OAuth App Integration.
        
        Updates an existing published OAuth App Integration. You can retrieve the published oauth app
        integration via :method:PublishedAppIntegration/get.
        
        :param integration_id: str
          The oauth app integration ID.
        :param token_access_policy: :class:`TokenAccessPolicy` (optional)
          Token access policy to be updated in the published oauth app integration
        
        
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = UpdatePublishedAppIntegration(integration_id=integration_id,
                                                    token_access_policy=token_access_policy)
        body = request.as_dict()
        self._api.do(
            'PATCH',
            f'/api/2.0/accounts/{self._api.account_id}/oauth2/published-app-integrations/{request.integration_id}',
            body=body)


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

    def create(self, service_principal_id: int, **kwargs) -> CreateServicePrincipalSecretResponse:
        """Create service principal secret.
        
        Create a secret for the given service principal.
        
        :param service_principal_id: int
          The service principal ID.
        
        :returns: :class:`CreateServicePrincipalSecretResponse`
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = CreateServicePrincipalSecretRequest(service_principal_id=service_principal_id)

        json = self._api.do(
            'POST',
            f'/api/2.0/accounts/{self._api.account_id}/servicePrincipals/{request.service_principal_id}/credentials/secrets'
        )
        return CreateServicePrincipalSecretResponse.from_dict(json)

    def delete(self, service_principal_id: int, secret_id: str, **kwargs):
        """Delete service principal secret.
        
        Delete a secret from the given service principal.
        
        :param service_principal_id: int
          The service principal ID.
        :param secret_id: str
          The secret ID.
        
        
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = DeleteServicePrincipalSecretRequest(secret_id=secret_id,
                                                          service_principal_id=service_principal_id)

        self._api.do(
            'DELETE',
            f'/api/2.0/accounts/{self._api.account_id}/servicePrincipals/{request.service_principal_id}/credentials/secrets/{request.secret_id},'
        )

    def list(self, service_principal_id: int, **kwargs) -> Iterator[SecretInfo]:
        """List service principal secrets.
        
        List all secrets associated with the given service principal. This operation only returns information
        about the secrets themselves and does not include the secret values.
        
        :param service_principal_id: int
          The service principal ID.
        
        :returns: Iterator over :class:`SecretInfo`
        """
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = ListServicePrincipalSecretsRequest(service_principal_id=service_principal_id)

        json = self._api.do(
            'GET',
            f'/api/2.0/accounts/{self._api.account_id}/servicePrincipals/{request.service_principal_id}/credentials/secrets'
        )
        return [SecretInfo.from_dict(v) for v in json.get('secrets', [])]
