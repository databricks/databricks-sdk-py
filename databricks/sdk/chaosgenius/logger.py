import logging
import time
import traceback

import pandas as pd
from pyspark.sql.session import SparkSession


class LogSparkDBHandler(logging.Handler):
    def __init__(self, sparkSession: SparkSession):
        logging.Handler.__init__(self)
        self.sparkSession = sparkSession
        sparkSession.sql("""
            CREATE TABLE IF NOT EXISTS chaosgenius.default.chaosgenius_logs (
                msg string,
                name string,
                levelname string,
                levelno long,
                pathname string,
                filename string,
                module string,
                lineno long,
                funcName string,
                createdAt double,
                exc_info string
            )
        """)

    def emit(self, record):
        try:
            exc_info = "" if record.exc_info is None else "".join(
                traceback.format_exception(
                    record.exc_info[0], record.exc_info[1], record.exc_info[2]
                )
            )
            df = pd.DataFrame(
                [
                    {
                        "msg": record.getMessage(),
                        "name": record.name,
                        "levelname": record.levelname,
                        "levelno": record.levelno,
                        "pathname": record.pathname,
                        "filename": record.filename,
                        "module": record.module,
                        "lineno": record.lineno,
                        "funcName": record.funcName,
                        "createdAt": time.time(),
                        "exc_info": exc_info,
                    }
                ]
            )
            self.sparkSession.createDataFrame(df).write.saveAsTable(
                "chaosgenius.default.chaosgenius_logs", mode="append"
            )
        except Exception:
            traceback.print_exc()
            print("LOGGING TO SPARK FAILED!!!")
