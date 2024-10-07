"""Utilities for pulling data."""

import datetime as dt
import logging
import json
from typing import Callable, Optional, Union

import pandas as pd
from pyspark.sql.session import SparkSession
from pyspark.sql import DataFrame as SparkDataFrame
from databricks.sdk import WorkspaceClient
from databricks.sdk.chaosgenius.cg_config import CGConfig
from databricks.sdk.service.compute import InstancePoolAndStats
from databricks.sdk.service.iam import User
from databricks.sdk.service.sql import EndpointInfo


PANDAS_CHUNK_SIZE = 10000


class DataPuller:
    """Responsible for pulling all data from a client."""

    def __init__(
        self,
        workspace_id: str,
        workspace_client: WorkspaceClient,
        customer_config: CGConfig,
        spark_session: Optional[SparkSession],
        save_to_csv: bool = False,
        logger: Optional[logging.Logger] = None,
    ) -> None:
        self._workspace_id = workspace_id
        self._workspace_client = workspace_client
        self._customer_config = customer_config
        self._spark_session = spark_session
        self._logger = logger if logger else logging.getLogger("data_puller")
        self._pull_time = dt.datetime.now()

        # TODO: Add override here
        self._end_time = int(
            (dt.datetime.now() - dt.timedelta(days=1)).timestamp() * 1000
        )
        self._save_to_csv = save_to_csv

        self._logger.info(
            f"Initializing data puller with workspace id: {workspace_id}, "
            f"pull time: {self._pull_time}, end_time: {self._end_time}, "
            f"save_to_csv: {self._save_to_csv}"
        )
        self._add_status_entry(
            "overall",
            "initializing",
            {
                "workspace_id": self._workspace_id,
                "pull_time": self._pull_time,
                "end_time": self._end_time,
                "save_to_csv": self._save_to_csv,
            },
        )

        self._logger.info("Getting instance pools list")
        self._ip_list = self._get_full_instance_pool_info()
        self._logger.info(f"Total pools: {len(self._ip_list)}")

        self._logger.info("Getting warehouses list")
        self._wh_list = self._get_full_warehouse_info()
        self._logger.info(f"Total warehouses: {len(self._wh_list)}")

        self._logger.info("Getting users list")
        self._user_list = self._get_full_user_info()
        self._logger.info(f"Total users: {len(self._user_list)}")

        self._logger.info("Starting data pull")
        results = self.get_all()
        success = True
        for res in results:
            if res[1] is False:
                success = False
                break
        status = "success" if success else "failed"
        self._add_status_entry("overall", status=status, data={"results": results})
        self._logger.info("Completed data pull.")

    def _generic_get_full_list(
        self,
        name: str,
        root_list_getter: Callable,
        root_item_getter: Callable,
        id_attribute_name: str,
        additional_ids: Optional[set] = None,
    ) -> list:
        self._logger.info(f"Getting {name}.")
        root_list = [i for i in root_list_getter()]
        root_list_ids = set(getattr(i, id_attribute_name) for i in root_list)
        self._logger.info(f"Current count: {len(root_list_ids)}")

        self._logger.info(f"Adding {name} from customer config.")
        config_ids = self._customer_config.get_ids(
            entity_type=name,
            include_entity="yes",
            entity_config_filter={"workspace_id": self._workspace_id},
        )
        self._logger.info(f"Found {len(config_ids)} items from customer config.")

        if additional_ids is not None:
            self._logger.info("Adding additional IDs.")
            config_ids = config_ids.union(additional_ids)
            self._logger.info(f"Total count after additional items: {len(config_ids)}")

        new_ids = root_list_ids.union(config_ids) - root_list_ids

        for item_id in new_ids:
            self._logger.info(f"New {name} ID {item_id} not in list. Getting info.")
            try:
                root_list.append(root_item_getter(item_id))
            except Exception:
                self._logger.exception(f"Failed to get {name} ID {item_id}.")

        root_list_ids = set(getattr(i, id_attribute_name) for i in root_list)
        self._logger.info(f"Current count of items: {len(root_list_ids)}")

        self._logger.info("Removing items from customer config.")
        ids_to_remove = self._customer_config.get_ids(
            entity_type="cluster",
            include_entity="no",
            entity_config_filter={"workspace_id": self._workspace_id},
        )
        self._logger.info(f"Items to be removed: {len(ids_to_remove)}.")

        ids_to_remove = root_list_ids.intersection(ids_to_remove)
        self._logger.info(f"Actual items to be removed: {len(ids_to_remove)}.")

        root_list = [
            i for i in root_list if getattr(i, id_attribute_name) not in ids_to_remove
        ]
        self._logger.info(f"Current count: {len(root_list)}")

        return root_list

    def _get_full_instance_pool_info(self) -> list[InstancePoolAndStats]:
        self._logger.info("Getting workspace instance pools.")
        return self._generic_get_full_list(
            "instance_pool",
            self._workspace_client.instance_pools.list,
            self._workspace_client.instance_pools.get,
            "instance_pool_id",
        )

    def _get_full_warehouse_info(self) -> list[EndpointInfo]:
        self._logger.info("Getting workspace warehouses.")
        return self._generic_get_full_list(
            "warehouse",
            self._workspace_client.warehouses.list,
            self._workspace_client.warehouses.get,
            "id",
        )

    def _get_full_user_info(self) -> list[User]:
        self._logger.info("Getting workspace users.")
        return self._generic_get_full_list(
            "user",
            self._workspace_client.users.list,
            self._workspace_client.users.get,
            "id",
        )

    def _add_status_entry(self, module: str, status: str, data: dict):
        self._write_to_table(
            df=pd.DataFrame(
                [
                    {
                        "module": module,
                        "status": status,
                        "data": json.dumps(data),
                        "entry_time": dt.datetime.now(),
                    }
                ]
            ),
            table_name="chaosgenius_status",
        )

    def _write_to_table(
        self,
        df: Union[pd.DataFrame, SparkDataFrame],
        table_name: str,
        mode: str = "append",
    ):
        df["data_end_time"] = self._end_time
        df["data_pull_time"] = self._pull_time
        df["workspace_id"] = self._workspace_id
        self._logger.info(f"saving {table_name}")
        if self._spark_session is not None:
            df = self._spark_session.createDataFrame(df)
        if self._save_to_csv:
            if isinstance(df, pd.DataFrame):
                try:
                    df.to_csv(f"output/{table_name}.csv", index=None, mode="x")
                except Exception:  # if file already exists, append without header
                    df.to_csv(
                        f"output/{table_name}.csv", index=None, mode="a", header=False
                    )
            else:
                df.write.csv(f"output/{table_name}.csv")
        else:
            df.write.saveAsTable(f"chaosgenius.default.{table_name}", mode=mode)

    def get_instance_pools_list(self) -> bool:
        self._logger.info("Saving instance pools list.")
        self._add_status_entry("instance_pools", "initializing", {})
        try:
            ip_df = pd.DataFrame(
                [
                    {
                        "instance_pool_id": ip.instance_pool_id,
                        "data": json.dumps(ip.as_dict()),
                    }
                    for ip in self._ip_list
                ]
            )
            if not ip_df.empty:
                self._write_to_table(ip_df, "instance_pools_list")
            self._add_status_entry("instance_pools", "success", {})
            return True
        except Exception:
            self._logger.exception("Saving instance pools failed :(")
            self._add_status_entry("instance_pools", "failed", {})
            return False

    def get_sql_warehouses_list(self) -> bool:
        self._logger.info("Saving warehouses list.")
        self._add_status_entry("warehouses", "initializing", {})
        try:
            wh_df = pd.DataFrame(
                [
                    {"warehouse_id": wh.id, "data": json.dumps(wh.as_dict())}
                    for wh in self._wh_list
                ]
            )
            if not wh_df.empty:
                self._write_to_table(wh_df, "warehouses_list")
            self._add_status_entry("warehouses", "success", {})
            return True
        except Exception:
            self._logger.exception("Saving warehouses failed :(")
            self._add_status_entry("warehouses", "failed", {})
            return False

    def get_users_list(self) -> bool:
        self._logger.info("Saving users list.")
        self._add_status_entry("users", "initializing", {})
        try:
            users_df = pd.DataFrame(
                [
                    {"user_id": i.id, "data": json.dumps(i.as_dict())}
                    for i in self._user_list
                ]
            )
            if not users_df.empty:
                self._write_to_table(users_df, "users_list")
            self._add_status_entry("users", "success", {})
            return True
        except Exception:
            self._logger.exception("Saving users failed :(")
            self._add_status_entry("users", "failed", {})
            return False

    def get_all(self) -> list[tuple[str, bool]]:
        data = [
            ("instance pools", self.get_instance_pools_list),
            ("warehouses list", self.get_sql_warehouses_list),
            ("users list", self.get_users_list),
        ]

        results = []
        for name, func in data:
            try:
                out = func()
            except Exception:
                self._logger.exception(f"Failed saving {name}.")
                out = False
            results.append((name, out))

        return results


if __name__ == "__main__":
    import os

    logger = logging.Logger("data_puller")
    logger.addHandler(logging.StreamHandler())

    dp = DataPuller(
        workspace_id=os.getenv("DATABRICKS_WORKSPACE_ID"),
        workspace_client=WorkspaceClient(
            host=os.getenv("DATABRICKS_WORKSPACE_HOST"),
            token=os.getenv("DATABRICKS_WORKSPACE_TOKEN"),
        ),
        logger=logger,
        spark_session=None,
        save_to_csv=True,
    )
    dp.get_all()
