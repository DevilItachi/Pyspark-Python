# Databricks notebook source
type(spark)

# COMMAND ----------

# DBTITLE 1,Spark_session
dir(spark)

# COMMAND ----------

help(spark.createDataFrame)

# COMMAND ----------

# DBTITLE 1,Create DF
my_list = [1,2,3,4,5]
df = spark.createDataFrame(data = my_list)
df.show()       # shows in form of dataframe text based
display(df)     # shows in form of table, databricks only , UI friendly

# COMMAND ----------

# schema and data needs to provided to create a dataframe
# if schema is not provided, spark will infer the schema
df.printSchema()

# COMMAND ----------

from pyspark.sql.types import *
schema = StructType([StructField(name ='id', dataType = IntegerType()) \
                     ,StructField(name ='name', dataType = StringType()) \
                     ,StructField(name ='salary', dataType = FloatType())
                     ])


# COMMAND ----------

#StructField("colname", dataType, nullable=True)

schema = StructType([
    StructField('id', IntegerType(), False),
    StructField('name', StringType(), True),
    StructField('salary', FloatType(), True)
])


# COMMAND ----------

# MAGIC %md
# MAGIC Read/write CSV in spark

# COMMAND ----------


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

df1.count()

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


df1.write.csv("/Volumes/pyspark_python/pyspark/ext_vol/Output/Customers_data", header= True , mode = "overwrite")

# COMMAND ----------

df1.selectExpr("spark_partition_id()").distinct().count() # shows number of partitions created


# COMMAND ----------

# MAGIC %md
# MAGIC Read/Write from Json file

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
# df.printSchema()

# COMMAND ----------

display(df)

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

# MAGIC %md
# MAGIC Parquet Read/write

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

# COMMAND ----------

print(df_csv.columns)
display(df_csv)
df_csv.printSchema()

# COMMAND ----------

# MAGIC %md
# MAGIC With Column usage

# COMMAND ----------

# add a new column or change values of column or datatype of column

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
df_csv = df_csv.withColumn("Salary",col("Salary") * 3)
display(df_csv)

# COMMAND ----------

# MAGIC %sql
# MAGIC use catalog  pyspark_python;
# MAGIC use schema pyspark;

# COMMAND ----------

# writes to delta table in databricks from DF 
# column name shouldnt contain space  , ; { } ( ) \n \t = -  or else it will give error
# Delta tables require SQL-safe column names
# ✔ lowercase
# ✔ underscores
# ✔ no spaces
# ✔ no special characters

df_csv.write.saveAsTable("csv_table")

# COMMAND ----------

# as above df was hvaing space in column name so we are renaming the column
df_clean = (
    df_csv
    .withColumnRenamed("Index", "index_id")
    .withColumnRenamed("Customer Id", "customer_id")
    .withColumnRenamed("First Name", "first_name")
    .withColumnRenamed("Last Name", "last_name")
    .withColumnRenamed("Company", "company")
    .withColumnRenamed("City", "city")
    .withColumnRenamed("Country", "country")
    .withColumnRenamed("Phone 1", "phone_1")
    .withColumnRenamed("Phone 2", "phone_2")
    .withColumnRenamed("Email", "email")
    .withColumnRenamed("Subscription Date", "subscription_date")
    .withColumnRenamed("Website", "website")
)


# COMMAND ----------

# writes the DF to delta table
df_clean.write.saveAsTable("csv_table")


# COMMAND ----------

spark.sql("select * from csv_table").display()

# COMMAND ----------

# MAGIC %md
# MAGIC StructType() & StructField
# MAGIC
# MAGIC Used to define schema manually , nested struct, array & map column
# MAGIC
# MAGIC StructType is collection of structField
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
    StructField("Salary", ArrayType(IntegerType()), True)
])
data = [(1, [100000, 200000 , 300000])]

df = spark.createDataFrame(data, schema)
df.show()

# COMMAND ----------

from  pyspark.sql.functions import *
#col() ONLY references existing columns

#df1 = df.withColumn("Salary", col("Salary")[0]).display() 
df1 = df.withColumn("Salary", col("Salary")[0])          # fetching value from that array column
display(df1)

# COMMAND ----------

# creates a new column of array type and assign value
df3 = df.withColumn(
    "number",
    array(lit(10), lit(20)))
display(df3)

# COMMAND ----------

from pyspark.sql.functions import array, lit, col

df4 = df.withColumn(
    "number",
    array(col("id"), lit(5000))
)

display(df4)


# COMMAND ----------

from pyspark.sql.functions import *

df5 = df4.withColumn("new_column",explode(col("number")))    # creates new rows for each element in array and store them in new column

display(df5)

# COMMAND ----------

df4 = df.withColumn("Skills",(lit("Python, Scala, Java"))) \
         .withColumn("primary", split(col("Skills"), ",").getItem(0)) \
         .withColumn("secondary", split(col("Skills"), ",").getItem(1))
display(df4)

# COMMAND ----------

# split() is used to convert a STRING column into an ARRAY, based on a delimiter.
# only works on strings and not integer
from pyspark.sql.functions import concat_ws, split, col

df6 = df4.withColumn("Skills_array",split( col("Skills"),","))
display(df6)

# COMMAND ----------

# array used to create a new column of array type from exissting columns of string type
df6 = df4.withColumn("Skills_array", array(col("primary"), col("secondary")))
display(df6)

# COMMAND ----------

# array_contains() used to check if array column has that value
# if yes then true, if no then false, if array is null it will be null
from pyspark.sql.functions import array_contains
df7 = df6.withColumn("Has_skill", array_contains(col("Skills_array"), "Python"))
df8 = df6.withColumn("Has_skill", array_contains(col("Skills_array"), "ADF"))
display(df7)
display(df8)

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
df3 = df.withColumn("keys", map_keys(df.Salary)) #map_keys is used to get all keys from map column
df4 = df.withColumn("Values", map_values(df.Salary)) #map_values is used to get all values from map column

display(df2)
display(df3)
display(df4)

# COMMAND ----------

# row class()
#This are used to create row for DF
from pyspark.sql import Row

r = Row("James","Bond")
print(r)
print(r[0] + "," + r[1])
r1 =Row(name="Amit", age=25)
print(r1)
print(r1.name + "," + str(r1.age))


# COMMAND ----------

Person = Row("name", "age")
p1 = Person("James", 40)
p2 = Person("Alice", 35)
print(p1.name)  # same like class and object


# COMMAND ----------

# column class
# represents a single column in DF

from pyspark.sql.functions import *
col1 = lit("AMit")

df = spark.createDataFrame([("James", 40), ("Alice", 35)], ["name", "age"])
df1 = df.withColumn("newcol", lit("value"))
display(df1)
df.select(df.name).show()



# COMMAND ----------

#when and otherwise
# similar to case statement in SQL

from pyspark.sql.functions import *
from pyspark.sql.types import *
data = [("James", 40, "Male"), ("Alice", 35, "Female"), ("Bob", 50, "Male"), ("Charlie", 30, "Female"), ("David", 35, "Male"), ("Esther", 40, "Female"), ("Fiona", 45, "Female")]

Schema = StructType([StructField("name", StringType(), True), StructField("age", IntegerType(), True), StructField("gender", StringType(), True)])

df = spark.createDataFrame(data, Schema)
display(df)
df1 = df.withColumn("newcol", when(df.gender == "Male", "M")
                    .when(df.gender == "Female", "F")
                    .otherwise("Unknown"))
display(df1)

# COMMAND ----------

# alias() , asc(), desc(), cast(), like()
from pyspark.sql.functions import *
df.select(df.name.alias("Emp_name")).show()
df.orderBy(df.age.asc()).show()
df.orderBy(df.age.asc(),df.name.desc()).show()
df1 = df.select(df.age.cast("string"))
df.printSchema()
df1.printSchema()
df.select(df.name.like("A%")).show()



# COMMAND ----------

# filter and where , both works same
df.filter(df.age > 30).show()
df.where((df.name.like("%A%")) & (df.age > 30)).show()


# COMMAND ----------

# Distinct and dropDuplicates
df.distinct().show()
df.dropDuplicates().show()

# COMMAND ----------

# union and union all, both are same. Union doesnt remove duplicates like SQL
df1 = df.filter(df.age > 40)
display(df)
display(df1)
df2 = df.union(df1)
display(df2)


# COMMAND ----------

# unionbyname used to merge 2 DF with different number of columns

df2= df.select(df.name,df.age)
display(df2)
df3 = df2.unionByName(df, allowMissingColumns=True)
display(df3)

# COMMAND ----------

# grouup by can do only 1 aggreation at a time, for multiple use agg
df4 = df.groupBy(df.gender).count()
display(df4)

# COMMAND ----------

#group by and agg  -- used to calulate more han 1 aggregrate at a time
from pyspark.sql.functions import *
df5 = df.groupBy(df.gender).agg(sum(df.age).alias("sum_age"), \
    avg(df.age).alias("avg_age"), \
    count(df.age).alias("count_age"))
display(df5)


# COMMAND ----------

df.select(df.name,df.age).show()
df.select("*").show()

# COMMAND ----------

# Joins
df_emp= spark.read.format("csv") \
        .option("header", "true") \
        .option("inferSchema", "true") \
        .load("/Volumes/pyspark_python/pyspark/ext_vol/Emp_Dept/employees.csv")
df_dept = spark.read.format("csv") \
        .option("header", "true") \
        .option("inferSchema", "true") \
        .load("/Volumes/pyspark_python/pyspark/ext_vol/Emp_Dept/departments.csv")
              
(df_emp.join(df_dept, df_emp.DEPARTMENT_ID == df_dept.DEPARTMENT_ID, "inner")) # inner join
(df_emp.join(df_dept, df_emp.DEPARTMENT_ID == df_dept.DEPARTMENT_ID, "left")) # left join
(df_emp.join(df_dept, df_emp.DEPARTMENT_ID == df_dept.DEPARTMENT_ID, "right")) # right join
(df_emp.join(df_dept, df_emp.DEPARTMENT_ID == df_dept.DEPARTMENT_ID, "full"))    #full join

# left semi - only matched rows from left df and columns from only left df
# left anti - only unmatched rows from left df and columns from only left df
# join with multiple conditions

# self join
from pyspark.sql.functions import *

df6 = df_emp.alias("e1").join(df_emp.alias("e2"), col("e1.DEPARTMENT_ID") == col("e2.DEPARTMENT_ID"))
display(df6)


# COMMAND ----------

#when and otherwise
# similar to case statement in SQL

from pyspark.sql.functions import *

display(df_emp)

# COMMAND ----------

# pivot used to rotate data in 1 column into multiple column
# it is an aggregration where one of the grouping column value will be converted in individual column
# rows become column

display(df_emp.groupby("department_id").pivot("Job_id").count())

# COMMAND ----------

display(df_emp.groupby("department_id").pivot("Job_id", ["FI_ACCOUNT"]).count())

# COMMAND ----------

# unpivot 
#column to row



# COMMAND ----------

# fill & fillna
# used to replace null/none on all or selected multiple DF column with either zero, empty  string or any other value
# fillna(value) only applies to columns whose data type matches the type of value.
from pyspark.sql import Row

data = [
    Row(name=None, age=25, city=None),
    Row(name="Alice", age=None, city="New York"),
    Row(name="Bob", age=30, city=None),
    Row(name=None, age=None, city="London"),
    Row(name="Charlie", age=35, city=None),
    Row(name=None, age=None, city=None),
    Row(name="David", age=None, city="Paris"),
    Row(name=None, age=40, city="Berlin"),
    Row(name="Eve", age=None, city=None),
    Row(name=None, age=28, city="Tokyo")
]

df_nulls = spark.createDataFrame(data)
display(df_nulls)
df1= df_nulls.fillna(0)  # only age will be 0
display(df1)


# COMMAND ----------

df2 = df_nulls.fillna("Unknown") # only string will be unkwown, age wont be affected
display(df2)


# COMMAND ----------

df3 = df_nulls.fillna("unknown", subset=["name"]) # only applies to 1 column
display(df3)


# COMMAND ----------

df4 = df_nulls.fillna("none", subset=["name", "city"]) #applies to both or all column speciefied in list
display(df4)


# COMMAND ----------

df5 = df_nulls.fillna({"age": 0, "city": "Unknown"}) # applies to specific column with diff datatype
display(df5)

# COMMAND ----------

# MAGIC %md
# MAGIC Samples

# COMMAND ----------

df = spark.range(start =1 , end=10)
display(df)


# COMMAND ----------

df.sample(fraction=0.5).show()  # sample means it will return subset of original data. each time it will be different

# COMMAND ----------

df.sample(fraction=0.5, seed = 0.1).show()  # generate subset of original data with seed, i.e same values will be created , if want to change value change the  seed value

# COMMAND ----------

# MAGIC %md
# MAGIC collect()
# MAGIC
# MAGIC Retrieves all elements in a df as an array of row type to driver node
# MAGIC
# MAGIC It is an action, hence doesnt return a DF, instead return data in array
# MAGIC
# MAGIC use it for small DF , for large data set it will show out of memory

# COMMAND ----------

df1 = df.collect()
print(df1)


# COMMAND ----------

# MAGIC %md
# MAGIC Dataframe Transform

# COMMAND ----------

def doublenumber(df):
    return df.withColumn("doube_number",df.id*2)

df2 = df.transform(doublenumber)
display(df2)

# create a function and then use it with df.transform

# COMMAND ----------

# MAGIC %md
# MAGIC Temp views

# COMMAND ----------

# local temp
df.createOrReplaceTempView("temp")

spark.sql("select * from temp").show()


# COMMAND ----------

# global temp
# can be accessed across multiple session
# global temp view are stored in global_temp schema
df.createOrReplaceGlobalTempView("global_temp")
spark.sql("select * from global_temp.global_temp").show()

# COMMAND ----------

spark.catalog.currentDatabase

# COMMAND ----------

spark.catalog.listDatabases()
spark.catalog.listTables()


# COMMAND ----------

# MAGIC %md
# MAGIC UDF

# COMMAND ----------

# MAGIC %md
# MAGIC Partition by

# COMMAND ----------

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

#  how to combine data now into a single df/table?

# COMMAND ----------

# rank , dense rank , row_number

from pyspark.sql.window import Window
from pyspark.sql.functions import rank, dense_rank, row_number
df = spark.read.format("csv").option("header", "true").option("inferSchema", "true").load("/Volumes/pyspark_python/pyspark/ext_vol/Emp_Dept/employees.csv")
display(df)

# COMMAND ----------

from pyspark.sql.window import Window

window_spec = Window.partitionBy("department_id").orderBy( "salary")

window_df = df.withColumn(
    "row_number",
    row_number().over(window_spec)
)
display(window_df)
