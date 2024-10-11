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


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", help="Databricks host", required=True)
    parser.add_argument("--client_id", help="Databricks client_id", default=None)
    parser.add_argument("--azure_client_id", help="Databricks azure_client_id", default=None)
    parser.add_argument("--client_secret", help="Databricks client_secret", default=None)
    parser.add_argument("--azure_client_secret", help="Databricks azure_client_secret", default=None)
    namespace = parser.parse_args()
    run(namespace.host, namespace.client_id, namespace.client_secret, namespace.azure_client_id, namespace.azure_client_secret)
