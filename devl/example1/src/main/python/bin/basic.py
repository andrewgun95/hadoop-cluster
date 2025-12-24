from pyspark.sql import SparkSession

# Client Mode
# spark = SparkSession.builder \
#     .appName("Basic Example") \
#     .master("local[*]") \
#     .getOrCreate()

# master("local[x]"), where x is how many partitions it should create when using a dataframe or dataset. x is number of cpus

# Cluster Mode
spark = SparkSession.builder \
    .appName("Basic Example") \
    .master("yarn") \
    .config("spark.executor.memory", "512m") \
    .config("spark.driver.memory", "512m") \
    .getOrCreate()

print("Spark Session created successfully.")

# Run example: spark-submit --conf spark.sql.shuffle.partitions=300 ./example1/src/main/python/bin/basic.py
#              spark-submit ./example1/src/main/python/bin/basic.py 
#              (by default 200 partitions)
print("Spark SQL Shuffle Partitions:", str(spark.conf.get("spark.sql.shuffle.partitions")))

# Run example: spark-submit --conf spark.yarn.appMasterEnv.HDFS_PATH="practice/retail_db/orders" ./example1/src/main/python/bin/basic.py
hdfs_path = spark.conf.get("spark.yarn.appMasterEnv.HDFS_PATH", None)
if hdfs_path is not None:
    print("Spark HDFS PATH:", str(hdfs_path))
else:
    print("HDFS PATH is not set in Spark configuration.")

# Spark Properties File 

# Default can be found at $SPARK_HOME/conf/spark-defaults.conf
# and can be override by using spark-submit --properties-file <file> or
# spark-submit --conf <property>=<value>

# Closing spark session
spark.stop()