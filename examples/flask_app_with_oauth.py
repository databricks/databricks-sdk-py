#!env python3
""" Flask with OAuth:

This application provides end-to-end demonstration of Databricks SDK for Python
capabilities of OAuth Authorization Code flow with PKCE security enabled. This
can help you build a hosted app with every user using their own identity to
access Databricks resources.

If you have already Custom App:

./flask_app_with_oauth.py --host <databricks workspace url> \
    --client_id <app-client-id> \
    --client_secret <app-secret> \
    --port 5001

If you want this script to register Custom App and redirect URL for you:

./flask_app_with_oauth.py --port 5001 --profile <databricks account profile>

You'll get prompted for Databricks Account username and password for
script to enroll your account into OAuth and create a custom app with
http://localhost:5001/callback as the redirect callback. Client and
secret credentials for this OAuth app will be printed to the console,
so that you could resume testing this app at a later stage.

Once started, please open http://localhost:5001 in your browser and
go through SSO flow to get a list of clusters on <databricks workspace url>.
"""

import argparse
import logging
import sys

from databricks.sdk.oauth import OAuthClient, get_workspace_endpoints
from databricks.sdk.service.compute import ListClustersFilterBy, State

APP_NAME = "flask-demo"
all_clusters_template = """<ul>
{% for cluster in clusters -%}
    <li><a 
        target="_blank" 
        href="{{ workspace_host }}/#setting/clusters/{{ cluster.cluster_id }}/configuration">
        {{ cluster.cluster_name }}</a> is {{ cluster.state }}</li>
{% endfor %}
</ul>"""


def create_flask_app(workspace_host: str, client_id: str, client_secret: str):
    """The create_flask_app function creates a Flask app that is enabled with OAuth.

    It initializes the app and web session secret keys with a randomly generated token. It defines two routes for
    handling the callback and index pages.
    """
    import secrets

    from flask import (Flask, redirect, render_template_string, request,
                       session, url_for)

    app = Flask(APP_NAME)
    app.secret_key = secrets.token_urlsafe(32)

    @app.route("/callback")
    def callback():
        """The callback route initiates consent using the OAuth client, exchanges
        the callback parameters, and redirects the user to the index page."""
        from databricks.sdk.oauth import Consent

        consent = Consent.from_dict(session["consent"], client_secret=client_secret)
        session["creds"] = consent.exchange_callback_parameters(request.args).as_dict()
        return redirect(url_for("index"))

    @app.route("/")
    def index():
        """The index page checks if the user has already authenticated and retrieves the user's credentials using
        the Databricks SDK WorkspaceClient. It then renders the template with the clusters' list.
        """
        oidc_endpoints = get_workspace_endpoints(workspace_host)
        port = request.environ.get("SERVER_PORT")
        redirect_url = f"http://localhost:{port}/callback"
        if "creds" not in session:
            oauth_client = OAuthClient(
                oidc_endpoints=oidc_endpoints,
                client_id=client_id,
                client_secret=client_secret,
                redirect_url=redirect_url,
            )
            consent = oauth_client.initiate_consent()
            session["consent"] = consent.as_dict()
            return redirect(consent.authorization_url)

        from databricks.sdk import WorkspaceClient
        from databricks.sdk.oauth import SessionCredentials

        credentials_strategy = SessionCredentials.from_dict(
            session["creds"],
            token_endpoint=oidc_endpoints.token_endpoint,
            client_id=client_id,
            client_secret=client_secret,
            redirect_url=redirect_url,
        )
        workspace_client = WorkspaceClient(
            host=workspace_host,
            product=APP_NAME,
            credentials_strategy=credentials_strategy,
        )
        clusters = workspace_client.clusters.list(
            filter_by=ListClustersFilterBy(cluster_states=[State.RUNNING, State.PENDING])
        )
        return render_template_string(
            all_clusters_template,
            workspace_host=workspace_host,
            clusters=clusters,
        )

    return app


def register_custom_app(args: argparse.Namespace) -> tuple[str, str]:
    """Creates new Custom OAuth App in Databricks Account"""
    logging.info("No OAuth custom app client/secret provided, creating new app")

    from databricks.sdk import AccountClient

    account_client = AccountClient(profile=args.profile)

    custom_app = account_client.custom_app_integration.create(
        name=APP_NAME,
        redirect_urls=[
            f"http://localhost:{args.port}/callback",
        ],
        confidential=True,
        scopes=["all-apis"],
    )
    logging.info(
        f"Created new custom app: " f"--client_id {custom_app.client_id} " f"--client_secret {custom_app.client_secret}"
    )

    return custom_app.client_id, custom_app.client_secret


def parse_arguments() -> argparse.Namespace:
    """Parses arguments for this demo"""
    parser = argparse.ArgumentParser(prog=APP_NAME, description=__doc__.strip())
    parser.add_argument("--host")
    for flag in ["client_id", "client_secret"]:
        parser.add_argument(f"--{flag}")
    parser.add_argument("--port", default=5001, type=int)
    parser.add_argument(
        "--profile",
        default="DEFAULT",
        help="Databricks account profile to use for authentication.",
    )
    return parser.parse_args()


if __name__ == "__main__":
    logging.basicConfig(
        stream=sys.stdout,
        level=logging.INFO,
        format="%(asctime)s [%(name)s][%(levelname)s] %(message)s",
    )
    logging.getLogger("databricks.sdk").setLevel(logging.DEBUG)

    args = parse_arguments()
    client_id, client_secret = args.client_id, args.client_secret
    if not client_id:
        client_id, client_secret = register_custom_app(args)
    app = create_flask_app(args.host, client_id, client_secret)

    app.run(
        host="localhost",
        port=args.port,
        debug=True,
        # to simplify this demo experience, we create OAuth Custom App for you,
        # but it intervenes with the werkzeug reloader. So we disable it
        use_reloader=args.client_id is not None,
    )
