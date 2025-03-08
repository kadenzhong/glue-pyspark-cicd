import pytest
from pyspark.sql import SparkSession
from scripts.utils import filter_adult_users

@pytest.fixture
def spark():
    return SparkSession.builder.appName("Test").getOrCreate()

def test_filter_adult_users(spark):
    data = [("Alice", 25), ("Bob", 17), ("Charlie", 30)]
    columns = ["name", "age"]
    df = spark.createDataFrame(data, columns)

    filtered_df = filter_adult_users(df)

    assert filtered_df.count() == 2  # 过滤掉了 Bob
    assert "Bob" not in [row["name"] for row in filtered_df.collect()]
