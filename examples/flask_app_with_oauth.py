#!env python3
""" Flask with OAuth:

This application provides end-to-end demonstration of Databricks SDK for Python
capabilities of OAuth Authorization Code flow with PKCE security enabled. This
can help you build a hosted app with every user using their own identity to
access Databricks resources.

If you have already Custom App:

./flask_app_with_oauth.py <databricks workspace url> \
    --client_id <app-client-id> \
    --client_secret <app-secret> \
    --port 5001

If you want this script to register Custom App and redirect URL for you:

./flask_app_with_oauth.py <databricks workspace url> \
    --account_id <databricks-account-id>

You'll get prompted for Databricks Account username and password for
script to enroll your account into OAuth and create a custom app with
http://localhost:5001/callback as the redirect callback. Client and
secret credentials for this OAuth app will be printed to the console,
so that you could resume testing this app at a later stage.

Once started, please open http://localhost:5001 in your browser and
go through SSO flow to get a list of clusters on <databricks workspace url>.
"""

import logging
import argparse
import sys

from databricks.sdk.core import Config

APP_NAME = 'flask-demo'
all_clusters_template = '''<ul>
{% for cluster in w.clusters.list() -%}
    <li><a 
        target="_blank" 
        href="{{ w.config.host }}/#setting/clusters/{{ cluster.cluster_id }}/configuration">
        {{ cluster.cluster_name }}</a> is {{ cluster.state }}</li>
{% endfor %}
</ul>'''


def create_flask_app(oauth_cfg: Config, port: int):
    """Creates OAuth-enabled flask app"""
    import secrets
    from flask import Flask, render_template_string, request, redirect, url_for, session

    app = Flask(APP_NAME)
    app.secret_key = secrets.token_urlsafe(32)

    @app.route('/callback')
    def callback():
        from databricks.sdk.oauth import Consent
        consent = Consent.from_dict(session['consent'])
        session['creds'] = consent.exchange_query(request.args).as_dict()
        return redirect(url_for('index'))

    @app.route('/')
    def index():
        if 'creds' not in session:
            redirect_url = f'http://localhost:{port}/callback'
            consent = oauth_cfg.oauth_interactive_flow(redirect_url, scopes=['clusters'])
            session['consent'] = consent.as_dict()
            return redirect(consent.auth_url)

        from databricks.sdk import WorkspaceClient
        from databricks.sdk.oauth import RefreshableCredentials

        credentials_provider = RefreshableCredentials.from_dict(session['creds'])
        workspace_client = WorkspaceClient(host=oauth_cfg.host,
                                           product=APP_NAME,
                                           credentials_provider=credentials_provider)

        return render_template_string(all_clusters_template, w=workspace_client)

    return app


def register_custom_app(oauth_cfg: Config, args: argparse.Namespace) -> tuple[str,str]:
    """Creates new Custom OAuth App in Databricks Account"""
    if not oauth_cfg.is_aws:
        logging.error('Not supported for other clouds than AWS')
        sys.exit(2)

    logging.info('No OAuth custom app client/secret provided, creating new app')

    import getpass
    from databricks.sdk import AccountClient
    account_client = AccountClient(host='https://accounts.cloud.databricks.com',
                                   account_id=args.account_id,
                                   username=input('Username: '),
                                   password=getpass.getpass('Password: '))

    logging.info('Enrolling all published apps...')
    account_client.o_auth_enrollment.create(enable_all_published_apps=True)

    status = account_client.o_auth_enrollment.get()
    logging.info(f'Enrolled all published apps: {status}')

    custom_app = account_client.custom_app_integration.create(
        name=APP_NAME,
        redirect_urls=[f'http://localhost:{args.port}/callback'],
        confidential=True)
    logging.info(f'Created new custom app: '
                 f'--client_id {custom_app.client_id} '
                 f'--client_secret {custom_app.client_secret}')

    return custom_app.client_id, custom_app.client_secret


def init_oauth_config(args) -> Config:
    """Creates Databricks SDK configuration for OAuth"""
    # TODO: (TBD) make auth init in the config lazy (???) and remove this hack
    # or alternatively introduce the OAuthConfig class
    def dummy_auth(cfg): return lambda: {}
    dummy_auth.auth_type = lambda: 'dummy'

    # create Databricks SDK config for OAuth flow
    oauth_cfg = Config(**vars(args), credentials_provider=dummy_auth)
    if not oauth_cfg.client_id and not args.account_id:
        logging.error('No custom app client/secret provided. Please provide --account_id with '
                      'Databricks Account ID to create a custom OAuth app.')
        sys.exit(1)

    if not oauth_cfg.client_id and args.account_id:
        client_id, client_secret = register_custom_app(oauth_cfg, args)
        oauth_cfg.client_id = client_id
        oauth_cfg.client_secret = client_secret

    return oauth_cfg


def parse_arguments() -> argparse.Namespace:
    """Parses arguments for this demo"""
    parser = argparse.ArgumentParser(prog=APP_NAME, description=__doc__.strip())
    parser.add_argument('host')
    for flag in ['client_id', 'client_secret']:
        parser.add_argument(f'--{flag}')
    parser.add_argument('--account_id')
    parser.add_argument('--port', default=5001, type=int)
    return parser.parse_args()


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout, level=logging.INFO, format='[%(levelname)s] %(message)s')

    args = parse_arguments()
    oauth_cfg = init_oauth_config(args)
    app = create_flask_app(oauth_cfg, args.port)

    app.run(host='localhost', port=args.port, debug=True,
            # to simplify this demo experience, we create OAuth Custom App for you,
            # but it intervenes with the werkzeug reloader. So we disable it
            use_reloader=not args.account_id)