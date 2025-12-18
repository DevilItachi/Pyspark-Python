# Databricks notebook source
# MAGIC %md
# MAGIC Object Oreineted Programming
# MAGIC
# MAGIC Group of functions and variables to identify easily. First create class, then create object. When we create a function within class, there should be a default parameter self Whenever we work in class, the variables will be called attributes and function will be called as method.  

# COMMAND ----------

class employee():
    emp_name = "Rahul"
    emp_dept = "IT"
    def info(self):
        return (f"Employee name is {self.emp_name} and work for {self.emp_dept}")

emp1 = employee()

print(emp1.emp_name)
print(emp1.emp_dept)
print(emp1.info())

# COMMAND ----------

# To distinguish between the parameters with the ones that are used with the attribute. We use self keyword 
# When self is used, it will call attribute. When self is not used, it will call normal parameter 
class employee():
    emp_name = "Rahul"
    emp_dept = "IT"
    def info(self, emp_name, emp_dept):
        return (f"Employee name is {emp_name} and work for {emp_dept}")

emp1 = employee()
# object = template

print(emp1.emp_name)
print(emp1.emp_dept)
print(emp1.info("Amit", "HR"))

# COMMAND ----------

# MAGIC %md
# MAGIC Multi threading 
# MAGIC
# MAGIC Let us say if we wanna run a function for ten times, then we can loop and run it 10 times. But in loop, first iteration will run, then the second iteration, then the third means it will run in series. So multithreading is used to do it parallely. 
# MAGIC
