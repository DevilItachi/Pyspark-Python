df = spark.createDataFrame(emp_data, emp_schema)
print(df.columns) # prints column name in list
col_name = df.columns  # this can used now further
df.write.saveAsTable("csv_table")  # deafult mode is errorIfExists , so if table exisits it fails
df.write.mode("overwrite").saveAsTable("csv_table") # overwrite mode will delete the table and create new table
df.write.format("delta").saveAsTable("emp_delta")
spark.sql("OPTIMIZE emp_delta ZORDER BY (department_id)")
spark.sql("VACUUM emp_delta RETAIN 168 HOURS")
spark.sql("select * from csv_table")
df = df.withColumn("Index",col("Index").cast("int")) # change the datatype of existing column
df = df.withColumn("Salary", lit(100000)) # add a new column
df = df.withColumn("Salary",col("Salary") * 3) # change the value of existing column
df = df.withColumnRenamed("Index", "index_id") # df = df.withColumnRenamed("old_column_name", "new_column_name")
df = df.withColumn("newcol", when(col("gender") == "Male", "M")
                            .when(col("gender") == "Female", "F")
                            .otherwise("Unknown"))
r1 =Row(name="Amit", age=25)  # creates a row
df.select(col("name").alias("Emp_name")).show() 
df = df.select(col("age").cast("string"))
df.orderBy(col("age").asc(),df.name.desc()).show()
df.filter(col("name").like("A%")).show()
df.filter(col("age") > 30).show()
df.where((col("name").like("%C%")) & (col("age") > 25)).show()
df.distinct().show()
df = df.select(col("department_id")).distinct() # shows only particular column distinct
df.select(df.name,df.age).show()
df.select("*").show()
df.dropDuplicates().show()  # drops all duplicates
df = df.drop("age") # single column
df = df.drop("age","gender") # multiple column
df = df.limit(5) # shows starting 5 rows
df3 = df1.union(df2)
df3 = df1.unionByName(df2, allowMissingColumns=True)  # allowMissingColumns=True is used to add extra columns with null values
df4 = df.groupBy(col("gender")).count()
df4 = df.groupBy(col("gender")).count().where(col("count") > 1)  # having 
df5 = df.groupBy(col("Salary"))  \  # used to calulate more han 1 aggregrate at a time
        .agg(
         sum("Salary").alias("sum_sal"), \
         avg("Salary").alias("avg_sal"), \
         count("Salary").alias("count_sal")
         )     
df_emp.join(df_dept, df_emp.DEPARTMENT_ID == df_dept.DEPARTMENT_ID, "left")) # left join
df6 = df_emp.alias("e1").join(df_emp.alias("e2"), col("e1.DEPARTMENT_ID") == col("e2.DEPARTMENT_ID")) # self join
df= df.fillna(0)  # fillna(value) replaces nulls with value , only applies to columns whose data type matches the type of value.
df5 = df.fillna({"age": 0, "city": "Unknown"}) # applies to specific column with diff datatype
window_spec = Window.partitionBy("department_id").orderBy( col("salary").desc())
window_df = df.withColumn
    ("row_number",
    row_number().over(window_spec) ) # rank() and dense_rank() can also be used
lag("salary", 1).over(window_spec)
lead("salary", 1).over(window_spec)
sum("salary").over(window_spec)  # running total
df = df.withColumn('new_name', regexp_replace(col('name'), "J", "Z"))
df.show(truncate=False) # try to show all datawithin the screen
df.na.drop() # drops null value records. # not good for production
df2 = df.withColumn("salary_new", coalesce(col("name"), lit("no_name")) ) # sql coalesce
df.selectExpr("spark_partition_id()").distinct().count() # shows number of partitions created
df_repartition = df.repartition(2)  # parition become 2 
df_repartition = df.repartition(10, "department_id") # parition is 10 and done on department
df_coalesce = df.coalesce(10)  # parition become 10 
schema = StructType([
    StructField('id', IntegerType(), False),
    StructField('name', StringType(), True),
    StructField('salary', FloatType(), True)
])
df_fact.join(broadcast(df_dim), "id", "left")
df_joined = df1.join(df2, "id", "inner").drop(df2.id) # Handling duplicate columns after join
df = df.withColumn("salt", (rand() * 10).cast("int")) ## Salting technique
df.cache()
df.persist(StorageLevel.MEMORY_AND_DISK)
df.unpersist()
df.explain(True)   # Logical + physical plan

df = spark.range(start =1 , end=10)  # 1 to 9 numbers
collect()
    - Retrieves all elements in a df as an array of row type to driver node
    - It is an action, hence doesnt return a DF, instead return data in array
    - use it for small DF , for large data set it will show out of memory
df = df.collect()
df.createOrReplaceTempView("temp")
df.createOrReplaceGlobalTempView("global_temp")
def doublenumber(df):
    return df.withColumn("doube_number",df.id*2)
df2 = df.transform(doublenumber)
@udf(IntegerType())
def double(x):
    return x * 2

df.select(col("id"),col("Salary").getItem(0)).show()  
df5 = df4.withColumn("new_column",explode(col("Salary")))    # creates new rows for each element in array and store them in new column
df6 = (df4.withColumn("Coding",(lit("Python, Scala, Java"))) 
        .withColumn("primary", split(col("Coding"), ",").getItem(0))      # split is used to split the string with delimeter and get item
        .withColumn("secondary", split(col("Coding"), ",").getItem(1))
 )
df2.write.parquet("/Volumes/pyspark_python/pyspark/ext_vol/Output/partition", mode = "overwrite", partitionBy="Country")
df_all = spark.read.parquet("/Volumes/pyspark_python/pyspark/ext_vol/Output/partition")  # reads from all partitions
df = (
    spark.read
        .format("csv")
        .option("header", "true")
        .load("/Volumes/pyspark_python/pyspark/ext_vol/Customers/customers-100.csv")
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
df2.write.csv("/Volumes/pyspark_python/pyspark/ext_vol/Output/Customers_data", header= True , mode = "overwrite")
 df2.coalesce(1) \
   .write \
   .option("header", True) \
   .mode("overwrite") \
   .csv("/Volumes/pyspark_python/pyspark/ext_vol/Output/Customers_data")
df = (
    spark.read
    .format("json")
    .option("multiLine", True)
    .load("/Volumes/pyspark_python/pyspark/ext_vol/Json_input/employees_10KB.json")
)













