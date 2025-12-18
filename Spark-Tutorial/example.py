from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql import SparkSession

spark_apps = SparkSession.builder \
    .appName("Example Spark Apps") \
        .master("local[*]") \
            .config("spark.executor.memory", "4gb") \
                .config("spark.driver.memory", "4gb") \
                    .getOrCreate()

spark_apps.range(1, 10).show()