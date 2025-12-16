# Databricks notebook source
# doubel quotes will work , mostly preffered
print("Hello")

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

# if code is to long to write in single line use \ to write in next line
print("Hi 'amit', \
      how are you")

# COMMAND ----------

# MAGIC %md
# MAGIC Variable

# COMMAND ----------

my_var = "Amit"
print(my_var)
x = 11
print(my_var,x)
y = 20
print(x+y)
last_name = "Bhosale"
print(my_var, last_name)   # space added
print(my_var + last_name)  # no space added , strings can be added as concatenation
z = "11"
print (z + my_var) # number written as string can be added 
print( x + my_var)          # error int and str cant be added



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
b= int(b)    # change datatype from str to int
print(type(c))


# COMMAND ----------

a = 10
b = 10.5
print(a+b) # python itseld change 10 to to 10.0 and then add .
