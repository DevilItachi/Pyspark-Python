# Databricks notebook source
# split() is used to convert a STRING column into an ARRAY, based on a delimiter.
# only works on strings and not integer
from pyspark.sql.functions import concat_ws, split, col

df7 = df6.withColumn("Skills_array",split( col("Coding"),","))
display(df7)

# COMMAND ----------

# array used to create a new column of array type from existing columns of string type
df8 = df7.withColumn("Skills_learned", array(col("primary"), col("secondary")))
display(df8)

# COMMAND ----------

# array_contains() used to check if array column has that value
# if yes then true, if no then false, if array is null it will be null
from pyspark.sql.functions import array_contains
df9 = df8.withColumn("Has_skill", array_contains(col("Skills_learned"), "Python"))
df10 = df8.withColumn("Has_skill", array_contains(col("Skills_learned"), "ADF"))
display(df9)
display(df10)
