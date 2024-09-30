import logging
from typing import Optional

from databricks.sdk import AccountClient
from databricks.sdk.chaosgenius.cg_config import CGConfig
from databricks.sdk.chaosgenius.data_puller import DataPuller
from databricks.sdk.chaosgenius.logger import LogSparkDBHandler
from databricks.sdk.service import iam
from pyspark.sql.session import SparkSession


def initiate_data_pull(
    host: str,
    account_id: str,
    client_id: str,
    client_secret: str,
    spark_session: SparkSession,
    workspace_list: Optional[list[int]] = None,
    account_admin: bool = True,
):
    print("Initiating logging.")
    logger = logging.getLogger("client_data_pull_logger")
    logger.setLevel(logging.DEBUG)

    print("Adding spark log handler.")
    spark_log_handler = LogSparkDBHandler(spark_session)
    logger.addHandler(spark_log_handler)

    print("Adding stream log handler.")
    streamhandler = logging.StreamHandler()
    logger.addHandler(streamhandler)

    print("Finished intializing logging.")

    logger.info(f"Initializing customer config: {account_id}")
    customer_config = CGConfig(sparkSession=spark_session, logger=logger)

    logger.info(f"Beginning pull for account ID: {account_id}")

    logger.info("Connecting to account.")
    a = AccountClient(
        host=host,
        account_id=account_id,
        client_id=client_id,
        client_secret=client_secret,
    )
    logger.info("Connected to account successfully.")

    logger.info("Getting SP ID")
    principal_id = None
    if account_admin:
        sp_list = list(a.service_principals.list())
        for sp in sp_list:
            if sp.application_id == client_id:
                principal_id = sp.id
                break
        if principal_id is None:
            raise ValueError("Unable to find principal ID of SP.")
        logger.info(f"SP ID is {principal_id}.")
    else:
        logger.info("We are not account admin, skipping SP ID retrieval.")

    if workspace_list is None or len(workspace_list) == 0:
        w_list = get_list_of_all_workspaces(
            logger=logger,
            customer_config=customer_config,
            account_client=a,
        )
    else:
        w_list = add_config_workspaces_to_list(
            w_list=workspace_list,
            logger=logger,
            customer_config=customer_config,
        )

    logger.info("Looping through workspaces.")
    for w_name, w_id in w_list:
        try:
            if account_admin:
                logger.info(
                    f"Updating permissions of SP for workspace {w_id} {w_name}."
                )
                a.workspace_assignment.update(
                    workspace_id=w_id,
                    principal_id=principal_id,
                    permissions=[iam.WorkspacePermission.ADMIN],
                )
            else:
                logger.info("We are not account admin, skipping permission update.")

            w = a.get_workspace_client(a.workspaces.get(w_id))
            logger.info(f"NEW RUN for workspace ID: {w_id}, {w_name}!!!!!")
            DataPuller(
                workspace_id=str(w_id),
                workspace_client=w,
                customer_config=customer_config,
                spark_session=spark_session,
                save_to_csv=False,
                logger=logger,
            )
        except Exception:
            logger.error(
                f"Failed pull for current workspace {w_id} {w_name}.", exc_info=True
            )


def get_list_of_all_workspaces(
    logger: logging.Logger,
    customer_config: CGConfig,
    account_client: AccountClient,
) -> list[tuple[str, int]]:
    logger.info("Getting list of all workspaces.")
    w_list = [
        (w.workspace_name, w.workspace_id) for w in account_client.workspaces.list()
    ]
    logger.info(f"Current len of w_list: {len(w_list)}")

    logger.info("Adding workspaces from customer config.")
    additional_workspaces = customer_config.get(
        entity_type="workspace",
        include_entity="yes",
    )["entity_id"].to_list()
    logger.info(f"Num additional workspaces: {len(additional_workspaces)}.")
    for addition_w_id in additional_workspaces:
        if addition_w_id not in [i[1] for i in w_list]:
            logger.info(
                f"Additional workspace ID {addition_w_id} not in list. Getting info."
            )
            try:
                w = account_client.workspaces.get(int(addition_w_id))
                w_list.append(w.workspace_name, w.workspace_id)
                logger.info(f"added workspace ID {addition_w_id} to list.")
            except Exception:
                logger.error(
                    f"Failed to get info for ID {addition_w_id}.", exc_info=True
                )
        else:
            logger.info(f"Additional workspace ID {addition_w_id} already in list.")

    logger.info(f"Current len of w_list: {len(w_list)}")

    logger.info("Removing workspaces from customer config.")
    w_to_remove = customer_config.get(
        entity_type="workspace",
        include_entity="no",
    )["entity_id"].to_list()
    logger.info(f"workspaces to be removed: {len(w_to_remove)}.")
    for w_id_remove in w_to_remove:
        logger.info(f"Checking to remove {w_id_remove}")
        remove = False
        index = None
        for i, (_, w_id) in enumerate(w_list):
            if int(w_id_remove) == w_id:
                index = i
                remove = True
                break
        if remove:
            w_list.pop(index)
            logger.info(f"Removed {w_id_remove} from list.")

    logger.info(f"Current len of w_list: {len(w_list)}")

    return w_list


def add_config_workspaces_to_list(
    w_list: list[int],
    logger: logging.Logger,
    customer_config: CGConfig,
) -> list[tuple[str, int]]:
    w_list = set(w_list)
    logger.info(f"Num initial workspaces: {len(w_list)}.")
    additional_workspaces = set(customer_config.get(
        entity_type="workspace",
        include_entity="yes",
    )["entity_id"].to_list())
    logger.info(f"Num additional workspaces: {len(additional_workspaces)}.")
    w_list = w_list.union(additional_workspaces)
    logger.info(f"Num workspaces after adding: {len(w_list)}.")
    w_to_remove = set(customer_config.get(
        entity_type="workspace",
        include_entity="no",
    )["entity_id"].to_list())
    logger.info(f"Num workspaces to remove: {len(w_to_remove)}.")
    w_list = w_list.difference(w_to_remove)
    logger.info(f"Num workspaces after removing: {len(w_list)}.")
    return [("unknown_name", w) for w in w_list]
