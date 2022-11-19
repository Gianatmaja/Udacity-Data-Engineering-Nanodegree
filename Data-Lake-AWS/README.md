# Spark and Data Lake
In this project, we'll build an ETL pipeline for a data lake hosted on S3. The ETL pipeline will load data from S3, process the data into analytics tables using Spark, and load them back into S3. This Spark process will be deployed on a cluster using AWS.

## Project Structure
The main files in this repository are listed below:

    .
    ├── etl.py            # Python script that will execute the ETL pipelines.
    └── dwh.cfg           # Configuration file that contains relevant AWS account information.

## Database Schema
The final database schema used for Sparkify's analytical purposes will follow a star schema design, as it is denormalised and hence, optimised for analytical queries. 

![Database Schema](https://github.com/Gianatmaja/Udacity-Data-Engineering-Nanodegree/blob/main/Data-Lake-AWS/Screenshot%202022-03-05%20at%203.27.01%20PM.png)

## ELT Process
The ELT process is done by spark and all the codes can be found on the etl.py file.

There are 2 main functions, namely:
1. `process_song_data`: Load raw data from S3 buckets to Spark stonealone server and process song dataset to insert record into songs and artists dimension table.
2. `process_log_data`: Load raw data from S3 buckets to Spark stonealone server and Process event(log) dataset to insert record into time and users dimensio table and songplays fact table
