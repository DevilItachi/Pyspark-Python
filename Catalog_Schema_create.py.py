# Databricks notebook source
# MAGIC %sql
# MAGIC create catalog Pyspark_python

# COMMAND ----------

# MAGIC %sql
# MAGIC use catalog Pyspark_python;

# COMMAND ----------

# MAGIC %sql
# MAGIC create schema if not exists Python

# COMMAND ----------

# MAGIC %sql
# MAGIC create schema if not exists Pyspark
