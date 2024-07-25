import json
from logging import Logger
from typing import Optional

import pandas as pd
from pyspark.sql.session import SparkSession


class CGConfig:
    """
    CG Config class.

    Entity type: workspace, cluster, warehouse, job etc
    Entity ID: ID of above
    Include Entity: "yes"/"no"
    Entity Config: JSON {"something": "else"}
    """

    def __init__(self, sparkSession: SparkSession, logger: Logger):
        self.logger = logger
        self.logger.info("Creating customer config table if not exists.")
        self.sparkSession = sparkSession

        try:
            sparkSession.sql(
                """
                CREATE TABLE IF NOT EXISTS chaosgenius.default.chaosgenius_config (
                    entity_type string,
                    entity_id string,
                    include_entity string,
                    entity_config string
                )
            """
            )
        except Exception:
            self.logger.error("Unable to create config table.", exc_info=True)

    def get(
        self,
        entity_type: Optional[str] = None,
        entity_ids: Optional[list[str]] = None,
        include_entity: Optional[str] = None,
        entity_config_filter: Optional[dict] = None,
    ) -> pd.DataFrame:
        try:
            where_query = ""
            if entity_type is not None:
                where_query += f"where entity_type = '{entity_type}'"

            if entity_ids is not None:
                if where_query == "":
                    where_query += "where "
                else:
                    where_query += " and "
                entity_ids_string = ",".join(map(lambda x: f"'{x}'", entity_ids))
                where_query += f"entity_id in ({entity_ids_string})"

            if include_entity is not None:
                if where_query == "":
                    where_query += "where "
                else:
                    where_query += " and "
                where_query += f"include_entity = '{include_entity}'"

            df = self.sparkSession.sql(
                f"select * from chaosgenius.default.chaosgenius_config {where_query}"
            ).toPandas()

            if df.empty:
                return pd.DataFrame(
                    columns=[
                        "entity_type",
                        "entity_id",
                        "include_entity",
                        "entity_config",
                    ]
                )

            df["entity_config"] = (
                df["entity_config"].replace("", "{}").apply(lambda x: json.loads(x))
            )
            if entity_config_filter is not None:
                df = df[
                    df["entity_config"].apply(
                        lambda x: all(
                            item in x.items() for item in entity_config_filter.items()
                        )
                    )
                ]
            return df
        except Exception:
            self.logger.error("Unable to get config.", exc_info=True)
            return pd.DataFrame(
                columns=["entity_type", "entity_id", "include_entity", "entity_config"]
            )

    def get_ids(
        self,
        entity_type: Optional[str] = None,
        entity_ids: Optional[list[str]] = None,
        include_entity: Optional[str] = None,
        entity_config_filter: Optional[dict] = None,
    ) -> set[str]:
        return set(
            self.get(
                entity_type=entity_type,
                entity_ids=entity_ids,
                include_entity=include_entity,
                entity_config_filter=entity_config_filter,
            )["entity_id"].values.tolist()
        )
