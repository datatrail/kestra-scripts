import sys
from operator import add
from random import random

from pyspark.sql import SparkSession

if __name__ == "__main__":
    spark = SparkSession.builder.appName("PythonPi").getOrCreate()

    spark.sparkContext.setLogLevel("DEBUG")

    partitions = 1
    n = 10 * partitions

    def f(_: int) -> float:
        x = random() * 2 - 1
        y = random() * 2 - 1
        return 1 if x**2 + y**2 <= 1 else 0

    count = (
        spark.sparkContext.parallelize(range(1, n + 1), partitions).map(f).reduce(add)
    )

    print(f"partitions is {n}")
    print(f"Pi is roughly 3.14")

    spark.stop()
