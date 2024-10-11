from databricks.sdk import WorkspaceClient
import logging

logging.basicConfig(level=logging.DEBUG)


def run():
    w = WorkspaceClient(
        host=input("Enter Databricks host: "),
        auth_type="external-browser",
    )
    me = w.current_user.me()
    print(me)


if __name__ == "__main__":
    run()
