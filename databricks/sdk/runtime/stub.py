from pyspark.sql.context import SQLContext
from pyspark.sql.functions import udf as U
from pyspark.sql.session import SparkSession

udf = U
spark: SparkSession
sc = spark.sparkContext
sqlContext: SQLContext
sql = sqlContext.sql
table = sqlContext.table


def displayHTML(html):
    """
    Display HTML data.
    Parameters
    ----------
    data : URL or HTML string
                    If data is a URL, display the resource at that URL, the resource is loaded dynamically by the browser.
                    Otherwise data should be the HTML to be displayed.
    See also:
    IPython.display.HTML
    IPython.display.display_html
    """
    ...


def display(input=None, *args, **kwargs):
    """
    Display plots or data.
    Display plot:
                    - display() # no-op
                    - display(matplotlib.figure.Figure)
    Display dataset:
                    - display(spark.DataFrame)
                    - display(list) # if list can be converted to DataFrame, e.g., list of named tuples
                    - display(pandas.DataFrame)
                    - display(koalas.DataFrame)
                    - display(pyspark.pandas.DataFrame)
    Display any other value that has a _repr_html_() method
    For Spark 2.0 and 2.1:
                    - display(DataFrame, streamName='optional', trigger=optional pyspark.sql.streaming.Trigger,
                                                    checkpointLocation='optional')
    For Spark 2.2+:
                    - display(DataFrame, streamName='optional', trigger=optional interval like '1 second',
                                                    checkpointLocation='optional')
    """
    ...
