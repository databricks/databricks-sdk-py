import json
from logging import Logger
from typing import Optional

import pandas as pd
from pyspark.sql.session import SparkSession


class CustomerConfig:
    """
    Customer Config class.

    Entity type: workspace, cluster, warehouse, job etc
    Entity ID: ID of above
    Include Entity: "yes"/"no"
    Entity Config: JSON {"something": "else"}
    """

    def __init__(self, sparkSession: SparkSession, logger: Logger):
        self.logger = logger
        self.logger.info("Creating customer config table.")
        self.sparkSession = sparkSession

        try:
            sparkSession.sql(
                """
                CREATE TABLE IF NOT EXISTS chaosgenius.default.customer_config (
                    entity_type string,
                    entity_id string,
                    include_entity string,
                    entity_config string
                )
            """
            )
        except Exception:
            self.logger.error("Unable to create customer config table.", exc_info=True)

    def get(
        self,
        entity_type: Optional[str] = None,
        entity_ids: Optional[list[str]] = None,
        include_entity: Optional[str] = None,
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
                f"select * from chaosgenius.default.customer_config {where_query}"
            ).toPandas()
            df["entity_config"] = (
                df["entity_config"].replace("", "{}").apply(lambda x: json.loads(x))
            )
        except Exception:
            self.logger.error("Unable to get config.", exc_info=True)
            return pd.DataFrame(
                columns=["entity_type", "entity_id", "include_entity", "entity_config"]
            )
