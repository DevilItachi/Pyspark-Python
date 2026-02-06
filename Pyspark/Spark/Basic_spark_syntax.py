# Databricks notebook source
type(spark)

# COMMAND ----------

dir(spark)  #shows all function that can be used by spark

# COMMAND ----------

help(spark.createDataFrame)  # to know how the function works

# COMMAND ----------

my_list = [1,2,3,4,5]
df = spark.createDataFrame(data = my_list)
df.show()       # shows in form of dataframe text based
display(df)     # shows in form of table, databricks only , UI friendly

# COMMAND ----------

# schema and data needs to provided to create a dataframe
# if schema is not provided, spark will infer the schema
df.printSchema()

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

print(df_csv.columns) # prints column name in list
col_name = df_csv.columns  # this can used now further
print(col_name)
display(df_csv)
df_csv.printSchema()

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

# writes the DF to delta table
df_clean.write.mode("overwrite").saveAsTable("csv_table")


# COMMAND ----------

spark.sql("select * from csv_table").display()

# COMMAND ----------

# as above df was hvaing space in column name so we are renaming the column
# df = df.withColumnRenamed("old_column_name", "new_column_name")
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

display(df4)

# Now new_row matches the schema (4 columns)
new_row = (3, {"ADF":80, "PySpark":90}, [10,20,30])
df = df4.union(spark.createDataFrame([new_row], df4.schema))
display(df)

# if a new row needs to be added to DF , create the row, then create a new DF, then union it with exisitng DF

# COMMAND ----------

Person = Row("name", "age")
p1 = Person("James", 40)
p2 = Person("Alice", 35)
print(p1.name)  # same like class and object, created 2 rows and then accessed


# COMMAND ----------

# column class
# represents a single column in DF

from pyspark.sql.functions import *
col1 = lit("AMit")

df = spark.createDataFrame([("James", 40), ("Alice", 35)], ["name", "age"])
df1 = df.withColumn("newcol", lit("Amit"))
display(df1)
df.select(df.name).show()



# COMMAND ----------

#when and otherwise
# similar to case statement in SQL

from pyspark.sql.functions import *
from pyspark.sql.types import *
data = [("James", 40, "Male"), ("Alice", 35, "Female"), ("Bob", 50, "Male"), ("Charlie", 30, "Female"), ("David", 35, "Male"), ("Esther", 40, None), ("Fiona", 45, "Female"), ("Charlie", 30, "Female"), ("Charlie", 35, "Female")]

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
df.where((df.name.like("%C%")) & (df.age > 25)).show()


# COMMAND ----------

# Distinct and dropDuplicates
df.distinct().show()
df.dropDuplicates().show()  # if full row is identical , it will delete the duplicate

# COMMAND ----------

df1= df.select("department_id").distinct() # shows only particular column distinct

# COMMAND ----------

# drops column from df
df11 = df.drop("age") # single col
df12 = df.drop("age","gender") # multiple col

# COMMAND ----------

# limits the records
df13 = df.limit(5)

# COMMAND ----------

# union and union all, both are same. Union doesnt remove duplicates like SQL
df1 = df.filter(df.age > 40)
display(df)
display(df1)
df2 = df.union(df1)
display(df2)


# COMMAND ----------

# union to work
# schema should be same, order of column should be same , same column number
# if schema is same, column no. same , but order is diff then use unionbyname

# COMMAND ----------

# unionbyname used to merge 2 DF with different number of columns

df2= df.select(df.name,df.age)
display(df2)
df3 = df2.unionByName(df, allowMissingColumns=True)  # allowMissingColumns=True is used to add extra columns with null values
display(df3)

# COMMAND ----------

# grouup by can do only 1 aggreation at a time, for multiple use agg
df4 = df.groupBy(df.gender).count()
display(df4)

# COMMAND ----------

# groupby and having in sql 
# we use where after groupby instead of having
df4 = df.groupBy(df.gender).count().where(col(count("count") > 1))

# COMMAND ----------

#group by and agg  -- used to calulate more han 1 aggregrate at a time
from pyspark.sql.functions import *
df5 = df.groupBy(df.gender)  \
        .agg(
         sum(df.age).alias("sum_age"), \
         avg(df.age).alias("avg_age"), \
         count(df.age).alias("count_age")
         )
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

def doublenumber(df):
    return df.withColumn("doube_number",df.id*2)

df2 = df.transform(doublenumber)
display(df2)

# create a function and then use it with df.transform

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

# rank , dense rank , row_number

from pyspark.sql.window import Window
from pyspark.sql.functions import rank, dense_rank, row_number
df = spark.read.format("csv").option("header", "true").option("inferSchema", "true").load("/Volumes/pyspark_python/pyspark/ext_vol/Emp_Dept/employees.csv")
display(df)

# COMMAND ----------

from pyspark.sql.window import Window

window_spec = Window.partitionBy("department_id").orderBy( col("salary").desc())

window_df = df.withColumn(
    "row_number",
    row_number().over(window_spec)
)
display(window_df)

# COMMAND ----------

spark.conf.set("spark.databricks.delta.schema.autoMerge.enabled", "true")
# Enables automatic schema evolution for Delta Lake.

#👉 When writing data to an existing Delta table, Spark will automatically merge new columns into the table schema instead of failing.
# Default behavior (autoMerge = false)

# COMMAND ----------

spark.conf.set("spark.databricks.delta.rowLevelConcurrencyPreview", "true")
# Allows multiple writers to update different rows of the same Delta table at the same time, reducing write conflicts.
# Only conflicting rows fail
# Non-conflicting updates succeed

# COMMAND ----------

emp_data = [
["001","101","John Doe","30","Male","50000","2015-01-01"],
["002","101","Jane Smith","25","Female","45000","2016-02-15"],
["003","102","Bob Brown","35","Male","55000","2014-05-01"],
["004","102","Alice Lee","28","Female","48000","2017-09-30"],
["005","103","Jack Chan","40","Male","60000","2013-04-01"],
["006","103","Jill Wong","32","Female","52000","2018-07-01"],
["007","101","James Johnson","42","Male","70000","2012-03-15"],
["008","102","Kate Kim","29","Female","51000","2019-10-01"],
["009","103","Tom Tan","33","Male","58000","2016-06-01"],
["010","104","Lisa Lee","27","Female","47000","2018-08-01"],
["011","104","David Park","38","Male","65000","2015-11-01"],
["012","105","Susan Chen","31","Female","54000","2017-02-15"],
["013","106","Brian Kim","45","Male","75000","2011-07-01"],
["014","107","Emily Lee","26","Female","46000","2019-01-01"],
["015","106","Michael Lee","37","Male","63000","2014-09-30"],
["016","107","Kelly Zhang","30","Female","49000","2018-04-01"],
["017","105","George Wang","34","Male","57000","2016-03-15"],
["018","104","Nancy Liu","29","Female","50000","2017-06-01"],
["019","103","Steven Chen","36","Male","62000","2015-08-01"],
["020","102","Grace Kim","32","Female","53000","2018-11-01"]
]

emp_schema = "employee_id string, department_id string, name string, age string, gender string, salary string, hire_date string"

# COMMAND ----------

# regex-replace
df = spark.createDataFrame(emp_data, emp_schema)


# COMMAND ----------

# replae J with Z
from pyspark.sql.functions import regexp_replace, col
df = df.withColumn('new_name', regexp_replace(col('name'), "J", "Z"))
display(df)


# COMMAND ----------

df.show(truncate=False) # try to show all datawithin the screen

# COMMAND ----------

# drops null value records.
# not good thing, not used in prod

df.na.drop()

# COMMAND ----------

# same as sql coalesce , if st value null, use 2nd value
df12 = df.withColumn("salary_new", coalesce(col("age"), lit("no_age")) )


# COMMAND ----------

df.selectExpr("spark_partition_id()").distinct().count() # shows number of partitions created


# COMMAND ----------

df_repartition = df.repartition(2)  # parition become 2 
df_repartition.selectExpr("spark_partition_id()").distinct().count() # shows number of partitions created


# COMMAND ----------

df_repartition = df.repartition(10)  # parition become 10 
df_repartition.selectExpr("spark_partition_id()").distinct().count() # shows number of partitions created
# can increase and decrease partition

# COMMAND ----------

df_repartition = df.repartition(10, "department_id") # parition is 10 and done on department
df_repartition.selectExpr("spark_partition_id()").distinct().count() # shows number of partitions created


# COMMAND ----------

df_coalesce = df.coalesce(10)  # parition become 10 
df_coalesce.selectExpr("spark_partition_id()").distinct().count() # shows number of partitions created
# can increase and decrease partition
