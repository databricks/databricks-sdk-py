from databricks.sdk import WorkspaceClient
import argparse
import logging

logging.basicConfig(level=logging.DEBUG)


def register_custom_app(confidential: bool) -> tuple[str, str]:
    """Creates new Custom OAuth App in Databricks Account"""
    logging.info("No OAuth custom app client/secret provided, creating new app")

    from databricks.sdk import AccountClient

    account_client = AccountClient()

    custom_app = account_client.custom_app_integration.create(
        name="external-browser-demo",
        redirect_urls=[
            f"http://localhost:8020",
        ],
        confidential=confidential,
        scopes=["all-apis"],
    )
    logging.info(f"Created new custom app: "
                 f"--client_id {custom_app.client_id} "
                 f"{'--client_secret ' + custom_app.client_secret if confidential else ''}")

    return custom_app.client_id, custom_app.client_secret


def delete_custom_app(client_id: str):
    """Creates new Custom OAuth App in Databricks Account"""
    logging.info(f"Deleting custom app {client_id}")
    from databricks.sdk import AccountClient
    account_client = AccountClient()
    account_client.custom_app_integration.delete(client_id)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", help="Databricks host", required=True)
    parser.add_argument("--client_id", help="Databricks client_id", default=None)
    parser.add_argument("--azure_client_id", help="Databricks azure_client_id", default=None)
    parser.add_argument("--client_secret", help="Databricks client_secret", default=None)
    parser.add_argument("--azure_client_secret", help="Databricks azure_client_secret", default=None)
    parser.add_argument("--register-custom-app", action="store_true", help="Register a new custom app")
    parser.add_argument("--register-custom-app-confidential", action="store_true", help="Register a new custom app")
    namespace = parser.parse_args()
    if namespace.register_custom_app and (namespace.client_id is not None or namespace.azure_client_id is not None):
        raise ValueError("Cannot register custom app and provide --client_id/--azure_client_id at the same time")
    if not namespace.register_custom_app and namespace.client_id is None and namespace.azure_client_secret is None:
        raise ValueError("Must provide --client_id/--azure_client_id or register a custom app")
    if namespace.register_custom_app:
        client_id, client_secret = register_custom_app(namespace.register_custom_app_confidential)
    else:
        client_id, client_secret = namespace.client_id, namespace.client_secret

    w = WorkspaceClient(
        host=namespace.host,
        client_id=client_id,
        client_secret=client_secret,
        azure_client_id=namespace.azure_client_id,
        azure_client_secret=namespace.azure_client_secret,
        auth_type="external-browser",
    )
    me = w.current_user.me()
    print(me)

    if namespace.register_custom_app:
        delete_custom_app(client_id)


