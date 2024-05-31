import sys
from operator import add
from random import random

from pyspark.sql import SparkSession

if __name__ == "__main__":
    spark = SparkSession.builder.appName("PythonPi").getOrCreate()

    spark.sparkContext.setLogLevel("DEBUG")

    print(f"Pi is roughly 3.14")

    spark.stop()
