# Databricks notebook source
#StructField("colname", dataType, nullable=True)

from pyspark.sql.types import *

schema = StructType([
    StructField('id', IntegerType(), False),
    StructField('name', StringType(), True),
    StructField('salary', FloatType(), True)
])


# COMMAND ----------

# MAGIC %md
# MAGIC StructType() & StructField
# MAGIC
# MAGIC Used to define schema manually , nested struct, array & map column
# MAGIC
# MAGIC StructType is collection of structField. Struct means a column contains multiple fields, or row inside row 
# MAGIC
# MAGIC Import this before use
# MAGIC
# MAGIC Define before creating schema

# COMMAND ----------

# from pyspark.sqlTypes import *

from pyspark.sql.types import *

schema = StructType([
    StructField("id", IntegerType(), True),
    StructField("name", StringType(), True)
])

# COMMAND ----------

data = [(1, "John"), (2, "Jane"), (3, "Bob")]
df = spark.createDataFrame(data, schema)
df.show()

# COMMAND ----------

# Array type column
from pyspark.sql.types import *

schema = StructType([
    StructField("id", IntegerType(), True),
    StructField("Salary", ArrayType(IntegerType()), True), # array type column
    StructField ("Skills", StringType(), True),
    StructField("Name", StringType(), True),
])
data = [(1, [100000, 200000 , 300000], "Python", "Amit"), (2, [400000, 500000 , 600000], "java", "Rohit")]

df = spark.createDataFrame(data, schema)
df.show()

# COMMAND ----------

from pyspark.sql.functions import col
df.select(col("id"),col("Salary").getItem(0)).show()  
# select only 1st element from array column and required column. getItem() is used in spark select to fetch item

# COMMAND ----------

from  pyspark.sql.functions import *
#col() ONLY references existing columns

#df1 = df.withColumn("Salary", col("Salary")[0]).display() 
df1 = df.withColumn("Salary", col("Salary")[0])          # creating new DF with value from that array column, here salary is not array type
display(df1)

# COMMAND ----------

# creates a new column of array type and assign value
df3 = df.withColumn("number",array(lit(10), lit(20)))
display(df3)

# COMMAND ----------

from pyspark.sql.functions import array, lit, col

df4 = df3.withColumn( "number_id", array(col("id"), lit(5000)) # in array column we can use existing column value


display(df4)


# COMMAND ----------

from pyspark.sql.functions import *

df5 = df4.withColumn("new_column",explode(col("Salary")))    # creates new rows for each element in array and store them in new column

display(df5)

# COMMAND ----------

df5 =( df4.withColumn("new_column",explode(col("Salary"))) 
          .withColumn("new_number",explode(col("number"))) )  # multiple explode 
display(df5)

# COMMAND ----------

df6 = (df4.withColumn("Coding",(lit("Python, Scala, Java"))) 
        .withColumn("primary", split(col("Coding"), ",").getItem(0))      # split is used to split the string with delimeter and get item
        .withColumn("secondary", split(col("Coding"), ",").getItem(1))
 )
display(df6)

# COMMAND ----------

# Map type column -- its a schema datatype MAP
# Map is used to represent map Key value pair similar to Dictinoary in Python
from pyspark.sql.types import *

schema = StructType([
    StructField("id", IntegerType(), True),
    StructField("Salary", MapType(StringType(), IntegerType()), True)
])
data = [(1, {"Python": 100000, "Scala": 200000 , "Java": 300000})]

df = spark.createDataFrame(data, schema)
display(df)

# COMMAND ----------

df1 = df.withColumn("Salary",df.Salary["Python"])      # accessing the value of key 
display(df1)

# COMMAND ----------

from pyspark.sql.functions import *
df2 = df.select("id","Salary",explode(df.Salary)) # explode() is used to create new rows for each element in array and store them in new column
df3 = df.withColumn("keys", map_keys(df.Salary)) #map_keys is used to get all keys from map column and creates a araay column
df4 = df.withColumn("Values", map_values(df.Salary)) #map_values is used to get all values from map column and creates a araay column

display(df2)
display(df3)
display(df4)

# COMMAND ----------


