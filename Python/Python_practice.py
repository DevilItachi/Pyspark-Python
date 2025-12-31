# Databricks notebook source
# doubel quotes will work , mostly preffered
print("Hello")
print(11)
print("I am", 35, "years old.")

# COMMAND ----------

# single quotes will work
print('Hello')

# COMMAND ----------

#  going on next line in python gives error
print (" sjhsfkhksvhsbvksbdkks
       gjhgjg")

# COMMAND ----------

# want to write codes in next line then use triple single/doubel codes
print ('''sjhsfkhksvhsbvksbdkks
gjhgjg''')
print (""" snskfksbgs
       sgksjgksb""")

# COMMAND ----------

# using single quotes inside single quotoes wont work
print('Hi 'amit', how are you')

# COMMAND ----------

#using single quote under double and triple single  quote

print("Hi 'amit', how are you")
print ('''Hi 'amit', how are you''')

# COMMAND ----------

# use single quotes, when your string has double quotes in it
print('Hi "Amit" how are you')

# COMMAND ----------

# if code is to long to write in single line use \ to write in next line
print("Hi 'amit', \
      how are you")

# COMMAND ----------

print("c:\\amit\\downloads")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Variable

# COMMAND ----------

my_var = "Amit"
print(my_var)
x = 11
print(my_var,x)
y = 20
print(x+y)
last_name = "Bhosale"
print(my_var, last_name)   # Amit Bhosale -- space added
print(my_var + last_name)  # AmitBhosale --no space added , strings can be added as concatenation
z = "11"
print (z + my_var) # 11Amit  -- number written as string can be added 
print( x + my_var)          # error int and str cant be added



# COMMAND ----------

x = 3
x = 11
x = "Amit"
print(x)  # always takes the latest value of variable

# COMMAND ----------

# is used for comment


# COMMAND ----------

# multi line codes  
# use \ or () to write multi line code
x = 1 +2 +3 +4  +\
    5 + 6
y =(1 +2 +3 +4 +
    5 + 6)
print(x)
print(y)

# COMMAND ----------

# Indendation 4 spaces per indendation
# Python follows indendation and its important , if not followed can give errors 
x = 5
if (x==2):
    print(x) # indendation applied
else:
    print(x+1)


# COMMAND ----------

# type casting
a = 10
b = "11"
print(type(a))
print(type(b))
c= int(b)    # change datatype from str to int
print(type(c))
z = str(21)
print(z)
print(type(z))

# python variable is case senstive
y=21
Y = 25
print(y)  # 21
print(Y)  # 25  


# COMMAND ----------

a = 10
b = 10.5
print(a+b) # python itseld change 10 to to 10.0 and then add .

# COMMAND ----------

a= "amit"
b= a*10
print(b)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Arrays
# MAGIC Group of values inside []
# MAGIC
# MAGIC arr = [1, 2, 3, 4]
# MAGIC
# MAGIC Most commonly used
# MAGIC
# MAGIC Can store mixed data types
# MAGIC
# MAGIC Dynamic size
# MAGIC
# MAGIC Stores multiple values
# MAGIC
# MAGIC Accessed using an index
# MAGIC
# MAGIC Maintains order
# MAGIC
# MAGIC Allows mix datatype 
# MAGIC
# MAGIC String can also be treated as array. Counting starts from 0.

# COMMAND ----------

x = "Amit"
print(x[0])  # A
print(x[0:2]) # Am
print(x[-1]) #t
print(x[:])  #amit
print(len(x))  #4
print(x.upper()) #AMIT
print(x.replace("m","n"))   #Anit
print(x.replace("m","nz"))

# COMMAND ----------

x = "Amit Bhosale Pune"
y = x.split(" ")   
print(y)                # ['Amit', 'Bhosale', 'Pune']
filename = "raw.csv"
if (filename.endswith(".csv")):
    print("csv file")
if(filename.startswith("raw")):
    print("raw file")
print(x.isnumeric())    # False -- isnumeric is used to check if string is numeric or not
print(x.isalpha())      # False -- isalpha is used to check if string is alphabetic or not , no space no number , special cahracters
print(x.isalnum())      # False -- isalnum is used to check if string is alphanumeric or not , no space , special cahracters


# COMMAND ----------

# MAGIC %md
# MAGIC Conditonals

# COMMAND ----------

# = is used to assign value to variable
# == is used to compare value
x = 5
if (x>10):
    print("x is greater than 10")
elif(x==10):
    print("x is equal to 10")
else:
    print("x is less than 10")

# COMMAND ----------

# MAGIC %md
# MAGIC Loops

# COMMAND ----------

# for Loop
my_list = ['a','b','c']
for i in my_list:
    print(i)

for i in range(1,5):  # it will be 1 to 4 i.e 5-1 range start is inclued , stop is not included
    print(i)

# COMMAND ----------

my_list = ['a','b','c']
my_list2 =['d','e','f','g']
for i in my_list:
    for j in my_list2:
        print(i)


# COMMAND ----------

my_list = ['amit','bunny','cassy']
my_list2 =['d','e','f','g','b','a']
for i in my_list:
    for j in i:
        print(j)


# COMMAND ----------

# for Loop
my_list = ['a','b','c', 'd','e','f','g','h','i']
for i in my_list:
    print(i)
    if (i == 'c'):
        print ("found")
        if(i == 'c'):
            print("found c")
        break
    else:
        print("not found")       # stops the loop there and exit

# COMMAND ----------

# MAGIC %md
# MAGIC Lists

# COMMAND ----------

my_list = ['amit', 'a', 'b', ['c','d','e']]
print(my_list[3][1])        #d
print(my_list[-2:])


# COMMAND ----------

my_list = [1,2,3,4,5,6,7,8,9]
print(my_list[::3]) #[1, 4, 7]
my_list.append(11)
print(my_list)      # mutable , values are added at the end
my_list.insert(5,10) # at index 5 inserts 10
print(my_list)
my_list.remove(10)  # removes 10
print(my_list)
my_list.pop()       # removes last element
print(my_list)
my_list.pop(2)      # removes element at index 2
print(my_list)
my_list.reverse()   #revrse the list
print(my_list)
my_list.sort()
print(my_list)
print(my_list[::-1])
new_list = [i*i for i in my_list]
print(new_list)


# COMMAND ----------

# MAGIC %md
# MAGIC Dictionary
# MAGIC
# MAGIC Key value pairs

# COMMAND ----------

my_dict = {
    "x": 1,
    "y": 2,
    "z": 3
}
print(my_dict["x"])

my_dict["x"] = 10
print(my_dict)
my_dict.pop("z")
print(my_dict)
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())
print(my_dict.get("x", "found"))
print(my_dict.get("z", "Not Found"))


# COMMAND ----------

# MAGIC %md
# MAGIC Sets

# COMMAND ----------

a = {1,2,3,4,4,4,4,5} # sets , no duplicates, no key value pair
print(a)
b = {6,7,8,9,10}
print(a.union(b)) # unions
print(a.intersection(b)) # mataching
print(a.difference(b)) # a-b
print(a.symmetric_difference(b)) # a-b and b-a
print(a.issubset(b))
print(a.issuperset(b))
print(a.isdisjoint(b))
print(a.add(11))
print(a)

# COMMAND ----------

# MAGIC %md
# MAGIC Tuples
# MAGIC
# MAGIC Behaves like list
# MAGIC
# MAGIC Conert all tuples to list and do operations , list can be converted to tuple

# COMMAND ----------

my_tub = (1,2,3,4,5)
print(my_tub)
print(my_tub[0])

# COMMAND ----------

# MAGIC %md
# MAGIC Functions
# MAGIC
# MAGIC Print just shows the output, cannot resuse later, dont send value back , for debugging / learning
# MAGIC
# MAGIC Return shares the output and stores value , Sends the value to be used later, stops the function Use return → for logic / real programs

# COMMAND ----------

def avg1(a,b):  #function defined with positional arguments
    return (a+b)/2      #logic defined



# COMMAND ----------

avg(2,4)    # function called with parameters

# COMMAND ----------

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

# F string are a way to insert variables into a string
# used for dynamic purpose
name = "Amit"
my_name = f"Hello {name}"
print(my_name)

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

# COMMAND ----------

# Enumerator
# Stores index and the value in tuple
my_list = ["a","b","c","d"]
for i in enumerate(my_list):
    print(i)
