from pyspark.sql import SparkSession


def test_spark_session():
    spark = SparkSession.builder.master("local[1]").appName("ci-test").getOrCreate()

    data = [("A", 1), ("B", 2)]
    df = spark.createDataFrame(data, ["name", "value"])

    assert df.count() == 2

    spark.stop()
