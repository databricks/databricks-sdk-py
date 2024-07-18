# Single-Sign-On (SSO) with OAuth

## Integration with Azure Active Directory

### Azure CLI Authentication

You can natively use credentials provided to `az login` (Azure CLI). The only argument you'll have to supply is `host`.
The SDK code for them should look like the following:

```python
from databricks.sdk import WorkspaceClient
w = WorkspaceClient(host='https://adb-30....azuredatabricks.net')
clusters = w.clusters.list()
for cl in clusters:
    print(f' - {cl.cluster_name} is {cl.state}')
```

This is the recommended way to for local-machine development with Azure Databricks, as you don't have to store any
credentials in the clear text and Azure CLI handles it all for you. When you have to run application in production,
please supply `ARM_CLIENT_ID`, `ARM_TENTANT_ID`, and `ARM_CLIENT_SECRET` environment variables for
the [Service Principal](#azure-active-directory-service-principals-2-legged-oauth-flow-on-cicd) auth to activate.

### PKCE 3-legged OAuth flow on local machines

You can make your command-line applications running on development machines authenticate with Azure AD Single-Page Application (SPA) flow by using creating the following application with terraform:

```hcl
data "azuread_client_config" "current" {}

resource "azuread_application" "pkce" {
  display_name     = "sample-oauth-app-pkce"
  owners           = [data.azuread_client_config.current.object_id]
  sign_in_audience = "AzureADMyOrg"
  single_page_application {
    redirect_uris = ["http://localhost:8080/"]
  }
}

output "pkce_app_client_id" {
  value = azuread_application.pkce.application_id
}
```

The SDK code for them should look like the following:

```python
from databricks.sdk import WorkspaceClient
w = WorkspaceClient(host='https://adb-30....azuredatabricks.net',
                    client_id='>>>value_from_pkce_app_client_id output<<<<',
                    auth_type='external-browser')
clusters = w.clusters.list()
for cl in clusters:
    print(f' - {cl.cluster_name} is {cl.state}')
```

It will launch a browser, prompting user to login with Azure credentials and give consent like described on the following screen:

![](images/aad-approve-app.png)

After giving consent, the user can close the browser tab:

![](images/external-browser-finish.png)

### Public Client 3-legged OAuth flow on local machines

You can make your command-line applications running on development machines authenticate with Public Client AuthCode flow by using creating the following application with terraform:

```hcl
resource "azuread_application" "public_client" {
  display_name     = "sample-oauth-app-public-client"
  owners           = [data.azuread_client_config.current.object_id]
  sign_in_audience = "AzureADMyOrg"
  public_client {
    redirect_uris = ["http://localhost:8080/"]
  }
}

output "public_client_id" {
  value = azuread_application.public_client.application_id
}
```

The SDK code for them should look like the following:

```python
from databricks.sdk import WorkspaceClient
w = WorkspaceClient(host='https://adb-30....azuredatabricks.net',
                    client_id='>>>value from public_client_id output<<<<',
                    auth_type='external-browser')
clusters = w.clusters.list()
for cl in clusters:
  print(f' - {cl.cluster_name} is {cl.state}')
```

### Private OAuth Apps 3-legged OAuth flow on local machines

You can make your command-line applications running on development machines authenticate with Private App AuthCode flow by using creating the following application with terraform:

```hcl
resource "azuread_application" "private_client" {
  display_name     = "sample-oauth-app-private-client"
  owners           = [data.azuread_client_config.current.object_id]
  sign_in_audience = "AzureADMyOrg"
  web {
    redirect_uris = ["http://localhost:8080/"]
  }
}

resource "time_rotating" "weekly" {
  rotation_days = 7
}

resource "azuread_application_password" "private_client" {
  application_object_id = azuread_application.private_client.object_id
  rotate_when_changed = {
    rotation = time_rotating.weekly.id
  }
}

output "private_client_id" {
  value = azuread_application.private_client.application_id
}

output "private_client_secret" {
  value = azuread_application_password.private_client.value
  sensitive = true
}
```

The SDK code for them should look like the following:

```python
from databricks.sdk import WorkspaceClient

w = WorkspaceClient(host='https://adb-30....azuredatabricks.net',
                    client_id='>>> value from private_client_id <<<',
                    client_secret='>>> value from private_client_secret <<<',
                    auth_type='external-browser')
clusters = w.clusters.list()
for cl in clusters:
    print(f' - {cl.cluster_name} is {cl.state}')
```

### Azure Active Directory Service Principals 2-legged OAuth flow on CI/CD

When running an application in an automated environment without user interaction, you should use AAD SPN flow.
You can create AAD Service Principal with secret using the following Terraform code:

```hcl
variable "name" {
  type = string
}

resource "azuread_application" "this" {
  display_name = var.name
}

resource "azuread_service_principal" "this" {
  application_id = azuread_application.this.application_id
}

resource "time_rotating" "month" {
  rotation_days = 30
}

resource "azuread_service_principal_password" "this" {
  service_principal_id = azuread_service_principal.this.object_id
  rotate_when_changed = {
    rotation = time_rotating.month.id
  }
}

output "client_id" {
  description = "value for ARM_CLIENT_ID environment variable"
  value       = azuread_application.this.application_id
}

output "client_secret" {
  description = "value for ARM_CLIENT_SECRET environment variable"
  value       = azuread_service_principal_password.this.value
  sensitive   = true
}
```

The SDK code to use it would look like the following:

```python
from databricks.sdk import WorkspaceClient

w = WorkspaceClient(host='https://adb-30....azuredatabricks.net',
                    azure_client_id='>>> value from client_id <<<',
                    azure_client_secret='>>> value from client_secret <<<',
                    azure_tenant_id='>>> your Azure Tenant ID <<<')
clusters = w.clusters.list()
for cl in clusters:
    print(f' - {cl.cluster_name} is {cl.state}')
```

On a local machine, you can also store Azure Service Principal credentials in the `~/.databrickscfg` file and refer to
them as `profile` argument in the SDK/CLI/Terraform configuration:

```text
[spn]
host=https://adb-30....azuredatabricks.net
azure_client_id=00000000-0000-0000-0000-000000000001
azure_client_secret=00000000-0000-0000-0000-000000000002
azure_tenant_id=00000000-0000-0000-0000-000000000003
```

The SDK code to use it would look like the following:

```python
from databricks.sdk import WorkspaceClient

w = WorkspaceClient(profile='spn')
clusters = w.clusters.list()
for cl in clusters:
    print(f' - {cl.cluster_name} is {cl.state}')
```

You can also supply the `ARM_CLIENT_ID`, `ARM_TENTANT_ID`, and `ARM_CLIENT_SECRET` environment variables instead of
hardcoded configuration properties.

## Authorization Code flow with PKCE

For a regular web app running on a server, it's recommended to use the Authorization Code Flow to obtain an Access Token
and a Refresh Token. This method is considered safe because the Access Token is transmitted directly to the server
hosting the app, without passing through the user's web browser and risking exposure.

To enhance the security of the Authorization Code Flow, the PKCE (Proof Key for Code Exchange) mechanism can be
employed. With PKCE, the calling application generates a secret called the Code Verifier, which is verified by
the authorization server. The app also creates a transform value of the Code Verifier, called the Code Challenge,
and sends it over HTTPS to obtain an Authorization Code. By intercepting the Authorization Code, a malicious attacker
cannot exchange it for a token without possessing the Code Verifier.

![session credentials flow with flask](images/flask-oauth.gif)

The [presented sample](https://github.com/databricks/databricks-sdk-py/blob/main/examples/flask_app_with_oauth.py)
is a Python3 script that uses the Flask web framework along with Databricks SDK for Python to demonstrate how to
implement the OAuth Authorization Code flow with PKCE security. It can be used to build an app where each user uses
their identity to access Databricks resources. The script can be executed with or without client and secret credentials
for a custom OAuth app.

Databricks SDK for Python exposes the `oauth_client.initiate_consent()` helper to acquire user redirect URL and initiate
PKCE state verification. Application developers are expected to persist `RefreshableCredentials` in the webapp session
and restore it via `RefreshableCredentials.from_dict(oauth_client, session['creds'])` helpers.

```python
from databricks.sdk.oauth import OAuthClient
oauth_client = OAuthClient(host='<workspace-url>',
                           client_id='<oauth client ID>',
                           redirect_url=f'http://host.domain/callback',
                           scopes=['clusters'])
import secrets
from flask import Flask, render_template_string, request, redirect, url_for, session
APP_NAME = 'flask-demo'
app = Flask(APP_NAME)
app.secret_key = secrets.token_urlsafe(32)
@app.route('/callback')
def callback():
    from databricks.sdk.oauth import Consent
    consent = Consent.from_dict(oauth_client, session['consent'])
    session['creds'] = consent.exchange_callback_parameters(request.args).as_dict()
    return redirect(url_for('index'))
@app.route('/')
def index():
    if 'creds' not in session:
        consent = oauth_client.initiate_consent()
        session['consent'] = consent.as_dict()
        return redirect(consent.auth_url)
    from databricks.sdk import WorkspaceClient
    from databricks.sdk.oauth import SessionCredentials
    credentials_provider = SessionCredentials.from_dict(oauth_client, session['creds'])
    workspace_client = WorkspaceClient(host=oauth_client.host,
                                       product=APP_NAME,
                                       credentials_provider=credentials_provider)
    return render_template_string('...', w=workspace_client)
```

## SSO for local scripts on development machines

For applications, that do run on developer workstations, Databricks SDK for Python provides `auth_type='external-browser'`
utility, that opens up a browser for a user to go through SSO flow. Azure support is still in the early experimental
stage.

```python
from databricks.sdk import WorkspaceClient
host = input('Enter Databricks host: ')
w = WorkspaceClient(host=host, auth_type='external-browser')
clusters = w.clusters.list()
for cl in clusters:
    print(f' - {cl.cluster_name} is {cl.state}')
```

## Creating custom OAuth applications

In order to use OAuth with Databricks SDK for Python, you should use `account_client.custom_app_integration.create` API.

```python
import logging, getpass
from databricks.sdk import AccountClient
account_client = AccountClient(host='https://accounts.cloud.databricks.com',
                               account_id=input('Databricks Account ID: '),
                               username=input('Username: '),
                               password=getpass.getpass('Password: '))
custom_app = account_client.custom_app_integration.create(
    name='awesome-app',
    redirect_urls=[f'https://host.domain/path/to/callback'],
    confidential=True)
logging.info(f'Created new custom app: '
             f'--client_id {custom_app.client_id} '
             f'--client_secret {custom_app.client_secret}')
```
