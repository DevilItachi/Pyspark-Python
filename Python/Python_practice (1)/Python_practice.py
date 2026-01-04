# Databricks notebook source
# *args allows a function to accept any number of positional arguments.
def my_func(*x):
    total = 0
    for i in x:
        total += i
    return total
print(my_func(10, 20))
print(my_func(1, 2, 3, 4, 5)) # multiple parameters passed thorugh tuples


# COMMAND ----------

# **kwargs allows a function to accept any number of keyword (named) arguments.
# Arguments are received as a dictionary
# Keys → argument names
# Values → argument values
def my_func(**x):
    for key, value in x.items():
        print(key, ":", value)
my_func(city="Pune", country="India", pin=411001)


# COMMAND ----------

def my_func(**x):
    total = 0
    for value in x.values():
        total += value
    avg = total / len(x)
    
    return total, avg

total_marks , avg_marks = my_func(math=80, science=90, english=70)
print(total_marks)
print(avg_marks)

# COMMAND ----------

# map() applies a function to every element of an iterable and returns an iterator.
my_list = [1,2,3,4,5,6,7,8,9]
def fsquare(x):
    return x*x
print((map(fsquare,my_list)))
print(list(map(fsquare,my_list)))  # takes 1 element at a time and applies function to it


# COMMAND ----------

# filter(function, iterable)
# filter first do map and then apply filter
# filter returns the original value and not the mapped value
my_list = [1,2,3,4,5,6,7,8,9]
def dsquare(x):
    if(x%2 == 0):
        return x*x
result = list(filter(dsquare,my_list))
print(result)

# COMMAND ----------

# Reduces the iterable to one single value
from functools import reduce
my_list = [1,2,3,4,5,6,7,8,9]
def sumnum(x,y):
    return x+y
result = reduce(sumnum,my_list)
print(result)

# COMMAND ----------

# MAGIC %md
# MAGIC Try Except - Error handling mechanism

# COMMAND ----------

x = "11"
try:
    if (x > 10):
        print("x is greater than 10")
    else:
        print("x is less than 10")
except Exception as e :
    print("Its not a number", e )   # this block executes
# Exception as e is used to show the actual error why the code failed

# COMMAND ----------

# MAGIC %md
# MAGIC F string or formatted strings

# COMMAND ----------

# MAGIC %md
# MAGIC Finally
# MAGIC
# MAGIC If try block completes, then except doesnt run , if try fails then except runs.
# MAGIC But Finally will run , even you have error or not
# MAGIC Finally is used to make sure our code is running fine even after try except block.

# COMMAND ----------

def my_func(x): -> none
    print("hello")
    try:
        if (x % 2 == 0):
            return 1
    except Exception as e:
        return e
      
    finally:
        print("Done work")

print(my_func(5))

# COMMAND ----------

x = 100 # global variable
print(x)
def my_func():
    x = 200
    return(x)       # local variable
result = (my_func())
print(result) # prints local variable
print(x)   # prints global variable

# COMMAND ----------

x = 99
try:
    if x < 100:
        raise ValueError("not allowed")   # user defined error can also be captured 
except ValueError as e:
    print(f"Exception caught: {e}")
