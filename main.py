from databricks.connect import DatabricksSession
from databricks.sdk.core import Config

config = Config(host='https://x', token='x', product="xapp", product_version="0.0.0")
spark = DatabricksSession().builder.userAgent("custom-agent").getOrCreate()
