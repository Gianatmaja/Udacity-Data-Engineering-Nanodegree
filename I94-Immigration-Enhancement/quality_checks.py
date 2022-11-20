# Import required libraries
import os
import configparser
from pathlib import Path
from pyspark.sql import SparkSession

# Get configuration
config = configparser.ConfigParser()
config.read('capstone.cfg', encoding='utf-8-sig')

os.environ['AWS_ACCESS_KEY_ID']=config['AWS']['AWS_ACCESS_KEY_ID']
os.environ['AWS_SECRET_ACCESS_KEY']=config['AWS']['AWS_SECRET_ACCESS_KEY']
SOURCE_S3_BUCKET = config['S3']['SOURCE_S3_BUCKET']
DEST_S3_BUCKET = config['S3']['DEST_S3_BUCKET']

# Initiate Spark session
spark = SparkSession.builder\
                    .config("spark.jars.packages", "org.apache.hadoop:hadoop-aws:2.7.0")\
                    .enableHiveSupport().getOrCreate()


s3_bucket = Path(DEST_S3_BUCKET)

# Check data model
for file_dir in s3_bucket.iterdir():
    if file_dir.is_dir():
        path = str(file_dir)
        df = spark.read.parquet(path)
        print("Table: " + path.split('/')[-1])
        schema = df.printSchema()

# Confirm records are fully present
for file_dir in s3_bucket.iterdir():
    if file_dir.is_dir():
        path = str(file_dir)
        df = spark.read.parquet(path)
        record_num = df.count()
        if record_num <= 0:
            raise ValueError("This table is empty!")
        else:
            print("Table: " + path.split('/')[-1] + f" is not empty: total {record_num} records.")