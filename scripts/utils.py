from pyspark.sql.functions import col

def filter_adult_users(df):
    return df.filter(col("age") >= 19)
