# Databricks notebook source
# test

# COMMAND ----------

# Create entry point for Spark application

from pyspark.sql import SparkSession
spark = SparkSession.builder \
    .appName("MyAPp") \
    .config("spark.sql.shuffle.partitions", 10) \
    .getOrCreate()

# COMMAND ----------

spark

# COMMAND ----------

df = spark.range(1,100)
optimized = df.filter("id > 50",).select("id")
optimized.explain(True)

# COMMAND ----------

spark.conf.get("spark.sql.shuffle.partitions")


# COMMAND ----------

# Create an RDD from a Python list and print its elements
# Doesnt work in databricks , RDD doesnt work in databricks

data = [1, 2, 3, 4, 5]
rdd = spark.sparkContext.parallelize(data)
print(rdd.collect())

# COMMAND ----------

# MAGIC %sql
# MAGIC use catalog pyspark_python;
# MAGIC use schema pyspark;
# MAGIC create volume ext_vol;

# COMMAND ----------

# reading data from csv 

df = spark.read.csv("/Volumes/pyspark_python/pyspark/ext_vol/bigmart.csv", header= True , inferSchema= True)

# COMMAND ----------

# Display the schema of a DataFrame

df.printSchema()

# COMMAND ----------

# shows the actual df with all data

# Filter rows in a DataFrame where a column value > 50
display(df)

# COMMAND ----------


display(df.filter(df.Item_MRP > 50))

# COMMAND ----------

# Count the number of rows in a DataFrame
row_count = df.count()


# COMMAND ----------

# Show the first 5 rows of a DataFrame  -- this is in text format
df.show(5)

# COMMAND ----------

# Show the first 5 rows of a DataFrame  -- this is in table format
display(df.limit(5))


# COMMAND ----------

# Convert a DataFrame to an RDD and print the first element   -- Databricks doesnt support RDD

rdd = df.rdd

# COMMAND ----------

# Create a DataFrame from a Python dictionary

data = [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 30}]
df1 = spark.createDataFrame(data)
display(df1)

# COMMAND ----------

# Register a DataFrame as a temporary SQL view

df1.createOrReplaceTempView("my_view")

display(spark.sql("select * from my_view"))


# COMMAND ----------

# Run a SQL query to select specific columns from a DataFrame

result = spark.sql("Select * from my_view where age > 25")
display(result)

# COMMAND ----------

# Save a DataFrame as a Parquet file

df.write.parquet("/Volumes/pyspark_python/pyspark/ext_vol/bigmart.parquet", mode= 'overwrite')

# COMMAND ----------

# Read a Parquet file into a DataFrame

df_parquet = spark.read.parquet("/Volumes/pyspark_python/pyspark/ext_vol/bigmart.parquet")


display(df_parquet)

# COMMAND ----------

# Group a DataFrame by a column and count occurrences
df_parquet.groupBy("Item_type").count().show()

# COMMAND ----------

# Add a new column to a DataFrame using withColumn()

from pyspark.sql.functions import col
df = df.withColumn("double_MRP", col("Item_MRP") * 2)

display(df)
