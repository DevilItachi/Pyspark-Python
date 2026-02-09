# Databricks notebook source
# add a new column or change values of column or datatype of column
# withcolumn does 3 things
#   1. If column doesnt exist, it will add a new column
#   2. If column exist, it will change the value of column
#   3. If column exist, it will change the datatype of column

from pyspark.sql.functions import col, lit
#col() → used to refer to a DataFrame column
#lit() is used to add a constant value to a DataFrame column.

#df = df.withColumn("columnname",col("columnname").cast("datatype"))
df_csv = df_csv.withColumn("Index",col("Index").cast("int")) # change the datatype of existing column

df_csv.printSchema()

# COMMAND ----------

from pyspark.sql.functions import col, lit
df_csv = df_csv.withColumn("Salary", lit(100000)) # add a new column
display(df_csv)

# COMMAND ----------

# change value of existing column
cdisplay(df_csv)

# COMMAND ----------


