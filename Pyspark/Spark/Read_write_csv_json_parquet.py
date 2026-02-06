# Databricks notebook source

# All options must be set BEFORE .load(). Any .option() after load  is ignored / invalid
df_csv = (
    spark.read
        .format("csv")
        .option("header", "true")
        .load("/Volumes/pyspark_python/pyspark/ext_vol/Customers/customers-100.csv")
)

display(df_csv)



# COMMAND ----------

# loading multiple csv files which are in same folder use *.csv
# if files are at different location give all files path 
# the schema should be same for all csv files
# pass multiple paths in list 

file_format = "csv"
file_location = "/Volumes/pyspark_python/pyspark/ext_vol/Customers/"
df = (
    spark.read
    .format(f"{file_format}")
    .option("header", "true")
    .option("inferSchema", "true")
    .load(f"{file_location}*.csv")

)

df2 = (
    spark.read
    .format("csv")
    .option("header", "True")
    .option("inferSchema", "true")
    .load( ["/Volumes/pyspark_python/pyspark/ext_vol/Customers/customers-100.csv",
           "/Volumes/pyspark_python/pyspark/ext_vol/Customers/customers-1000.csv",
           "/Volumes/pyspark_python/pyspark/ext_vol/Customers/customers-10000.csv"])
)

# COMMAND ----------

df2.count() # shows count of records in the df

# COMMAND ----------

# write into csv file
# Just write the file name and not the extensions
# Multiple csv files are being created as spark works in parallel and partitions 
# Each file = one partition processed by one task
# extra files are also created , start , complete, success
# 4 types of mode avaialble default is Error
#   1. Append -- if file already exists, adds to it
#   2. Overwrite -- if file already exists, overwrites it
#   3. Ignore -- if file already exists, does nothing
#   4. Error -- if file already exists, throws an error


df2.write.csv("/Volumes/pyspark_python/pyspark/ext_vol/Output/Customers_data", header= True , mode = "overwrite")

# COMMAND ----------

df2.selectExpr("spark_partition_id()").distinct().count() # shows number of partitions created


# COMMAND ----------

# coalesce(1) means it will create only 1 partition, hence only  1 file will be generated.
# not good, as it will not be able to process in parallel
# bad for performance and for big data
df2.coalesce(1) \
   .write \
   .option("header", True) \
   .mode("overwrite") \
   .csv("/Volumes/pyspark_python/pyspark/ext_vol/Output/Customers_data")


# COMMAND ----------

# Nested Json file
# use multiline option

df = (
    spark.read
    .format("json")
    .option("multiLine", True)
    .load("/Volumes/pyspark_python/pyspark/ext_vol/Json_input/employees_10KB.json")
)

# display(df)
df.printSchema()

# COMMAND ----------

display(df)
# in bronze layer the data is kept like this only , when moved to dilver, separae columns  are created by withColumn

# COMMAND ----------

# creates a json file which is single line
# This is the most efficient format for Spark & big data
# spark cant write in multiline, its not effiecent way.
# Spark always writes JSON as JSON Lines (NDJSON):
# 1 row = 1 JSON object
# 1 object = 1 line
# Optimized for parallel processing
# No pretty-print support in Spark writer
# 4 modes same as csv

df.write.json("/Volumes/pyspark_python/pyspark/ext_vol/Output/sample4.json", mode = "overwrite")

# COMMAND ----------

# reading parquet file
# parquet file already contains schema
# Spark does NOT need to infer schema for Parquet

df1= (
    spark.read
    .format("parquet")
    .load("/Volumes/pyspark_python/pyspark/ext_vol/Parquet_input/iris.parquet")
)
display(df1)

# COMMAND ----------

# write to a parquet file
# 4 modes same as csv

df1.write.parquet("/Volumes/pyspark_python/pyspark/ext_vol/Output/sample6", mode = "overwrite")

# COMMAND ----------

# reading the same parquet which we creating in above cell
df3 = spark.read.parquet("/Volumes/pyspark_python/pyspark/ext_vol/Output/sample6")
display(df3)
