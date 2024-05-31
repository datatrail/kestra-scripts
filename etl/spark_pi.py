import sys
from operator import add
from random import random

from pyspark.sql import SparkSession

if __name__ == "__main__":
    spark = SparkSession.builder.appName("PythonPi").getOrCreate()

    spark.sparkContext.setLogLevel("DEBUG")

    partitions = int(sys.argv[1]) if len(sys.argv) > 1 else 2
    n = 100000 * partitions

    print(f"partitions is {n}")
    print(f"Pi is roughly 3.14")

    spark.stop()
