# Databricks notebook source
df2 = (
    spark.read
    .format("csv")
    .option("header", "True")
    .option("inferSchema", "true")
    .load( ["/Volumes/pyspark_python/pyspark/ext_vol/Customers/customers-100.csv",
           "/Volumes/pyspark_python/pyspark/ext_vol/Customers/customers-1000.csv",
           "/Volumes/pyspark_python/pyspark/ext_vol/Customers/customers-10000.csv"])
)
display(df2)

# COMMAND ----------

df2.write.parquet("/Volumes/pyspark_python/pyspark/ext_vol/Output/partition", mode = "overwrite", partitionBy="Country")

#  data is stored in location in  partition by country
# for each country a sseprate folder will be created
#  when you read data from specific country folder only that data will be read



# COMMAND ----------

df_all = spark.read.parquet("/Volumes/pyspark_python/pyspark/ext_vol/Output/partition")  # reads from all partitions
display(df_all)
