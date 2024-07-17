import logging

from databricks.sdk import AccountClient
from databricks.sdk.chaosgenius import CustomerConfig, DataPuller, LogSparkDBHandler
from databricks.sdk.service import iam
from pyspark.sql.session import SparkSession


def initiate_data_pull(
    host: str,
    account_id: str,
    client_id: str,
    client_secret: str,
    spark_session: SparkSession,
):
    logger = logging.getLogger("client_data_pull_logger")
    logger.setLevel(logging.DEBUG)

    spark_log_handler = LogSparkDBHandler(spark_session)
    logger.addHandler(spark_log_handler)

    streamhandler = logging.StreamHandler()
    logger.addHandler(streamhandler)

    logger.info(f"Initializing customer config: {account_id}")
    customer_config = CustomerConfig(sparkSession=spark_session, logger=logger)

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
    sp_list = list(a.service_principals.list())
    principal_id = None
    for sp in sp_list:
        if sp.application_id == client_id:
            principal_id = sp.id
            break
    if principal_id is None:
        raise ValueError("PRINCIPAL ID is None.")
    logger.info(f"SP ID is {principal_id}.")

    w_list = get_list_of_all_workspaces(
        logger=logger,
        customer_config=customer_config,
        account_client=a,
    )

    logger.info("Looping through workspaces.")
    for w_name, w_id in w_list:
        try:
            logger.info(f"Updating permissions of SP for workspace {w_id} {w_name}.")
            a.workspace_assignment.update(
                workspace_id=w_id,
                principal_id=principal_id,
                permissions=[iam.WorkspacePermission.ADMIN],
            )
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
    customer_config: CustomerConfig,
    account_client: AccountClient,
) -> list[tuple[str, str]]:
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
            if w_id_remove == w_id:
                index = i
                remove = True
                break
        if remove:
            w_list.pop(index)
            logger.info(f"Removed {w_id_remove} from list.")

    logger.info(f"Current len of w_list: {len(w_list)}")

    return w_list
