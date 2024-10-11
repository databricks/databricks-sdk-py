from databricks.sdk import WorkspaceClient
import argparse
import logging
from typing import Optional

logging.basicConfig(level=logging.DEBUG)


def run(host: str, client_id: Optional[str], client_secret: Optional[str], azure_client_id: Optional[str], azure_client_secret: Optional[str]):
    w = WorkspaceClient(
        host=host,
        client_id=client_id,
        client_secret=client_secret,
        azure_client_id=azure_client_id,
        azure_client_secret=azure_client_secret,
        auth_type="external-browser",
    )
    me = w.current_user.me()
    print(me)


def register_custom_app() -> tuple[str, str]:
    """Creates new Custom OAuth App in Databricks Account"""
    logging.info("No OAuth custom app client/secret provided, creating new app")

    from databricks.sdk import AccountClient

    account_client = AccountClient()

    custom_app = account_client.custom_app_integration.create(
        name="external-browser-demo",
        redirect_urls=[
            f"http://localhost:8020",
        ],
        confidential=True,
        scopes=["all-apis"],
    )
    logging.info(f"Created new custom app: "
                 f"--client_id {custom_app.client_id} "
                 f"--client_secret {custom_app.client_secret}")

    return custom_app.client_id, custom_app.client_secret


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", help="Databricks host", required=True)
    parser.add_argument("--client_id", help="Databricks client_id", default=None)
    parser.add_argument("--azure_client_id", help="Databricks azure_client_id", default=None)
    parser.add_argument("--client_secret", help="Databricks client_secret", default=None)
    parser.add_argument("--azure_client_secret", help="Databricks azure_client_secret", default=None)
    parser.add_argument("--register-custom-app", action="store_true", help="Register a new custom app")
    namespace = parser.parse_args()
    if namespace.register_custom_app and (namespace.client_id is not None or namespace.azure_client_id is not None):
        raise ValueError("Cannot register custom app and provide --client_id/--azure_client_id at the same time")
    if not namespace.register_custom_app and namespace.client_id is None and namespace.azure_client_secret is None:
        raise ValueError("Must provide --client_id/--azure_client_id or register a custom app")
    if namespace.register_custom_app:
        client_id, client_secret = register_custom_app()
    else:
        client_id, client_secret = namespace.client_id, namespace.client_secret

    run(namespace.host, client_id, client_secret, namespace.azure_client_id, namespace.azure_client_secret)
