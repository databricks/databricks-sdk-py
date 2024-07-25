"""Utilities for pulling data."""

import datetime as dt
import logging
import json
from typing import Callable, Optional, Union

import pandas as pd
from pyspark.sql.session import SparkSession
from pyspark.sql import DataFrame as SparkDataFrame
from pyspark.sql.functions import explode
from databricks.sdk import WorkspaceClient
from databricks.sdk.chaosgenius.cg_config import CGConfig
from databricks.sdk.service import sql as databricks_sql
from databricks.sdk.service.compute import ClusterDetails, InstancePoolAndStats
from databricks.sdk.service.iam import User
from databricks.sdk.service.sql import EndpointInfo
from databricks.sdk.service.jobs import BaseJob


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
        self._start_time, self._end_time = self._get_start_end_time()
        self._save_to_csv = save_to_csv

        self._logger.info(
            f"Initializing data puller with workspace id: {workspace_id}, "
            f"pull time: {self._pull_time}, start_time: {self._start_time}, "
            f"end_time: {self._end_time}, save_to_csv: {self._save_to_csv}"
        )
        self._add_status_entry(
            "overall",
            "initializing",
            {
                "workspace_id": self._workspace_id,
                "pull_time": self._end_time,
                "start_time": self._start_time,
                "end_time": self._end_time,
                "save_to_csv": self._save_to_csv,
            },
        )

        # TODO(KB): refactor into multiple files by clusters, wh, etc
        self._logger.info("Getting cluster list")
        self._cluster_list = self._get_full_cluster_list()
        self._logger.info(f"Total clusters: {len(self._cluster_list)}")

        self._logger.info("Getting instance pools list")
        self._ip_list = self._get_full_instance_pool_info()
        self._logger.info(f"Total pools: {len(self._ip_list)}")

        self._logger.info("Getting warehouses list")
        self._wh_list = self._get_full_warehouse_info()
        self._logger.info(f"Total warehouses: {len(self._wh_list)}")

        self._logger.info("Getting jobs list")
        self._job_list = self._get_full_jobs_info()
        self._logger.info(f"Total jobs: {len(self._job_list)}")

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

    def _get_job_cluster_ids(self) -> set[str]:
        job_compute_id_list = self._spark_session.sql(
            "select compute_ids from system.workflow.job_task_run_timeline "
            f"where period_start_time < from_unixtime({self._start_time//1000}) "
            f"and period_start_time >= from_unixtime({self._end_time//1000}) "
        )
        job_compute_id_list = (
            job_compute_id_list.select(
                explode(job_compute_id_list.compute_ids).alias("compute_id")
            )
            .distinct()
            .toPandas()["compute_id"]
            .values.tolist()
        )
        return set(i for i in job_compute_id_list if len(i.split("-")) == 3)

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

        self._logger.info("Removing items from customer config.")
        ids_to_remove = self._customer_config.get_ids(
            entity_type="cluster",
            include_entity="no",
            entity_config_filter={"workspace_id": self._workspace_id},
        )
        self._logger.info(f"Items to be removed: {len(ids_to_remove)}.")

        ids_to_remove = root_list_ids.union(config_ids).intersection(ids_to_remove)
        self._logger.info(f"Actual items to be removed: {len(ids_to_remove)}.")

        root_list = [
            i for i in root_list if getattr(i, id_attribute_name) not in ids_to_remove
        ]
        self._logger.info(f"Current count: {len(root_list)}")

        return root_list

    def _get_full_cluster_list(self) -> list[ClusterDetails]:
        self._logger.info("Getting workspace clusters.")

        self._logger.info("Getting job cluster IDs.")
        job_cluster_ids = self._get_job_cluster_ids()
        self._logger.info(f"Total job cluster IDs: {len(job_cluster_ids)}")

        return self._generic_get_full_list(
            "cluster",
            self._workspace_client.clusters.list,
            self._workspace_client.clusters.get,
            "cluster_id",
            additional_ids=job_cluster_ids,
        )

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

    def _get_full_jobs_info(self) -> list[BaseJob]:
        self._logger.info("Getting workspace jobs.")
        return self._generic_get_full_list(
            "job",
            self._workspace_client.jobs.list,
            self._workspace_client.jobs.get,
            "job_id",
        )

    def _get_full_user_info(self) -> list[User]:
        self._logger.info("Getting workspace users.")
        return self._generic_get_full_list(
            "user",
            self._workspace_client.users.list,
            self._workspace_client.users.get,
            "id",
        )

    def _get_start_end_time(self) -> tuple[int, int]:
        try:
            df = self._spark_session.sql(
                f"""
                select max(data_end_time) as end_time
                from chaosgenius.default.chaosgenius_status
                where module = 'overall' and status = 'success'
                and workspace_id = '{self._workspace_id}'
            """
            ).toPandas()
        except Exception:
            self._logger.exception("Exception in fetching result from status table.")

        try:
            start_time = dt.datetime.fromtimestamp(df["end_time"][0] / 1000)
        except Exception:
            self._logger.exception(
                "Unable to extract previous end time from status table output."
            )
            start_time = dt.datetime.now() - dt.timedelta(days=91)

        end_time = dt.datetime.now() - dt.timedelta(days=1)

        end_time = int(end_time.timestamp() * 1000)
        start_time = int(start_time.timestamp() * 1000)

        return start_time, end_time

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

    def _save_iterator_in_chunks(self, iterator, metadata, table_name):
        chunk = []
        for i, item in enumerate(iterator):
            chunk.append({**metadata, "data": json.dumps(item.as_dict())})
            if i % PANDAS_CHUNK_SIZE == 0:
                self._logger.info(f"saving chunk {i // PANDAS_CHUNK_SIZE}")
                chunk_df = pd.DataFrame(chunk)
                self._write_to_table(chunk_df, table_name)
                chunk.clear()

        if chunk:
            self._logger.info(f"saving chunk {i // PANDAS_CHUNK_SIZE}")
            chunk_df = pd.DataFrame(chunk)
            self._write_to_table(chunk_df, table_name)
            chunk.clear()

    def get_clusters_list(
        self,
        clusters_list: Optional[list] = None,
        status_data: Optional[dict] = None,
    ) -> bool:
        self._logger.info("Saving cluster list.")
        status_data = status_data or {}
        self._add_status_entry("clusters", "initializing", {"status_data": status_data})
        try:
            if clusters_list is None:
                clusters_list = self._cluster_list
            cluster_df = pd.DataFrame(
                [
                    {"cluster_id": c.cluster_id, "data": json.dumps(c.as_dict())}
                    for c in clusters_list
                ]
            )
            if not cluster_df.empty:
                self._write_to_table(cluster_df, "clusters_list")
            self._add_status_entry("clusters", "success", {"status_data": status_data})
            return True
        except Exception:
            self._logger.exception("Saving cluster list failed :(")
            self._add_status_entry("clusters", "failed", {"status_data": status_data})
            return False

    def get_clusters_events(
        self,
        clusters_list: Optional[list] = None,
        status_data: Optional[dict] = None,
    ) -> bool:
        self._logger.info("Saving cluster events.")
        status_data = status_data or {}
        self._add_status_entry(
            "cluster_events", "initializing", {"status_data": status_data}
        )

        if clusters_list is None:
            clusters_list = self._cluster_list

        results = []
        for cluster in clusters_list:
            try:
                cluster_events = self._workspace_client.clusters.events(
                    cluster.cluster_id,
                    end_time=self._end_time,
                    start_time=self._start_time,
                )
                self._logger.info(f"saving cluster run for id {cluster.cluster_id}")
                self._save_iterator_in_chunks(
                    iterator=cluster_events,
                    metadata={"cluster_id": cluster.cluster_id},
                    table_name="clusters_events",
                )
                results.append((cluster.cluster_id, True))
            except Exception:
                self._logger.exception("Failed to save cluster event info :(")
                results.append((cluster.cluster_id, False))

        success = True
        for res in results:
            if res[1] is False:
                success = False
                break
        status = "success" if success else "failed"
        self._add_status_entry(
            "cluster_events",
            status=status,
            data={"results": results, "status_data": status_data},
        )
        return success

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

    def get_sql_query_history(self) -> bool:
        self._logger.info("Saving query history.")
        self._add_status_entry("query_history", "initializing", {})

        results = []
        for wh in self._wh_list:
            try:
                wh_queries = self._workspace_client.query_history.list(
                    include_metrics=True,
                    filter_by=databricks_sql.QueryFilter(
                        warehouse_ids=[wh.id],
                        query_start_time_range=databricks_sql.TimeRange(
                            start_time_ms=self._start_time,
                            end_time_ms=self._end_time,
                        ),
                        statuses=[
                            databricks_sql.QueryStatus.CANCELED,
                            databricks_sql.QueryStatus.FAILED,
                            databricks_sql.QueryStatus.FINISHED,
                        ],
                    ),
                )
                self._logger.info(f"saving queries for wh id {wh.id}")
                self._save_iterator_in_chunks(
                    iterator=wh_queries,
                    metadata={"warehouse_id": wh.id},
                    table_name="queries_list",
                )
                results.append((wh.id, True))
            except Exception:
                self._logger.exception("Failed to save query history :(")
                results.append((wh.id, False))

        success = True
        for res in results:
            if res[1] is False:
                success = False
                break
        status = "success" if success else "failed"
        self._add_status_entry(
            "query_history",
            status=status,
            data={"results": results},
        )
        return success

    # TODO: Not being used currently.
    def get_jobs_list(self) -> bool:
        self._logger.info("Saving jobs list.")
        self._add_status_entry("jobs", "initializing", {})
        try:
            job_df = pd.DataFrame(
                [
                    {"job_id": job.job_id, "data": json.dumps(job.as_dict())}
                    for job in self._job_list
                ]
            )
            if not job_df.empty:
                self._write_to_table(job_df, "jobs_list")
            self._add_status_entry("jobs", "success", {})
            return True
        except Exception:
            self._logger.exception("Saving jobs failed :(")
            self._add_status_entry("jobs", "failed", {})
            return False

    # TODO: Not being used currently.
    def get_job_runs_list(self) -> bool:
        self._logger.info("Saving job runs.")
        self._add_status_entry("job_runs", "initializing", {})

        # TODO: Get job cluster ids name from job-id-run-id because API is not giving
        cluster_ids = []
        job_results = []
        for job in self._job_list:
            try:
                job_runs = self._workspace_client.jobs.list_runs(
                    completed_only=True,
                    expand_tasks=True,
                    job_id=job.job_id,
                    start_time_from=self._start_time,
                    start_time_to=self._end_time,
                )
                cluster_ids.extend([i.cluster_instance.cluster_id for i in job_runs])
                self._logger.info(f"saving job runs for job id {job.job_id}")
                self._save_iterator_in_chunks(
                    iterator=job_runs,
                    metadata={"job_id": job.job_id},
                    table_name="jobs_runs_list",
                )
                job_results.append((job.job_id, True))
            except Exception:
                self._logger.exception("Failed to save job runs :(")
                job_results.append((job.job_id, False))

        cluster_list = [
            self._workspace_client.clusters.get(cluster_id=i) for i in cluster_ids
        ]
        result_cl = self.get_clusters_list(
            clusters_list=cluster_list, status_data={"origin": "job_runs"}
        )
        result_ce = self.get_clusters_events(
            clusters_list=cluster_list, status_data={"origin": "job_runs"}
        )

        success = True
        for res in job_results:
            if res[1] is False:
                success = False
                break
        success = success and result_ce and result_cl
        status = "success" if success else "failed"
        self._add_status_entry(
            "job_runs",
            status=status,
            data={
                "results": {
                    "job_results": job_results,
                    "cluster_list": result_cl,
                    "cluster_event": result_ce,
                }
            },
        )
        return success

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
            ("cluster list", self.get_clusters_list),
            ("cluster events", self.get_clusters_events),
            ("instance pools", self.get_instance_pools_list),
            ("warehouses list", self.get_sql_warehouses_list),
            ("query history", self.get_sql_query_history),
            # ("jobs list", self.get_jobs_list),
            # ("job runs", self.get_job_runs_list),
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
