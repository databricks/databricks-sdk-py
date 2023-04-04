# Single-Sign-On (SSO) with OAuth

### Authorization Code flow with PKCE

For a regular web app running on a server, it's recommended to use the Authorization Code Flow to obtain an Access Token
and a Refresh Token. This method is considered safe because the Access Token is transmitted directly to the server
hosting the app, without passing through the user's web browser and risking exposure.

To enhance the security of the Authorization Code Flow, the PKCE (Proof Key for Code Exchange) mechanism can be
employed. With PKCE, the calling application generates a secret called the Code Verifier, which is verified by
the authorization server. The app also creates a transform value of the Code Verifier, called the Code Challenge,
and sends it over HTTPS to obtain an Authorization Code. By intercepting the Authorization Code, a malicious attacker
cannot exchange it for a token without possessing the Code Verifier.

The [presented sample](https://github.com/databricks/databricks-sdk-py/blob/main/examples/flask_app_with_oauth.py)
is a Python3 script that uses the Flask web framework along with Databricks SDK for Python to demonstrate how to
implement the OAuth Authorization Code flow with PKCE security. It can be used to build an app where each user uses
their identity to access Databricks resources. The script can be executed with or without client and secret credentials
for a custom OAuth app.

Databricks SDK for Python exposes the `oauth_client.initiate_consent()` helper to acquire user redirect URL and initiate
PKCE state verification. Application developers are expected to persist `RefreshableCredentials` in the webapp session
and restore it via `RefreshableCredentials.from_dict(oauth_client, session['creds'])` helpers.

Works for both AWS and Azure. Not supported for GCP at the moment.

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
    from databricks.sdk.oauth import RefreshableCredentials

    credentials_provider = RefreshableCredentials.from_dict(oauth_client, session['creds'])
    workspace_client = WorkspaceClient(host=oauth_client.host,
                                       product=APP_NAME,
                                       credentials_provider=credentials_provider)

    return render_template_string('...', w=workspace_client)
```

### SSO for local scripts on development machines

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

### Creating custom OAuth applications

In order to use OAuth with Databricks SDK for Python, you should use `account_client.custom_app_integration.create` API.

```python
import logging, getpass
from databricks.sdk import AccountClient
account_client = AccountClient(host='https://accounts.cloud.databricks.com',
                               account_id=input('Databricks Account ID: '),
                               username=input('Username: '),
                               password=getpass.getpass('Password: '))

logging.info('Enrolling all published apps...')
account_client.o_auth_enrollment.create(enable_all_published_apps=True)

status = account_client.o_auth_enrollment.get()
logging.info(f'Enrolled all published apps: {status}')

custom_app = account_client.custom_app_integration.create(
    name='awesome-app',
    redirect_urls=[f'https://host.domain/path/to/callback'],
    confidential=True)
logging.info(f'Created new custom app: '
             f'--client_id {custom_app.client_id} '
             f'--client_secret {custom_app.client_secret}')
```