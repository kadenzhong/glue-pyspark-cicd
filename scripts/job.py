import sys
from pyspark.sql import SparkSession
from awsglue.context import GlueContext
from awsglue.job import Job
from scripts.utils import filter_adult_users  # 引入工具函数

# ✅ 直接在代码里定义 Glue Job 名称和 S3 路径
JOB_NAME = "GlueCICDJob"
INPUT_PATH = "s3://group-script1/script/raw-data/"  # ✅ 你的 S3 输入路径
OUTPUT_PATH = "s3://group-script1/script/processed-data/"  # ✅ 你的 S3 输出路径

# 初始化 Spark 和 Glue 上下文
spark = SparkSession.builder.appName(JOB_NAME).getOrCreate()
glueContext = GlueContext(spark.sparkContext)
job = Job(glueContext)
job.init(JOB_NAME, {})

# 读取数据
df = spark.read.option("header", "true").csv(INPUT_PATH)

# 处理数据
filtered_df = filter_adult_users(df)  # 过滤年龄小于18的用户

# 写回 S3
filtered_df.write.mode("overwrite").parquet(OUTPUT_PATH)

job.commit()


