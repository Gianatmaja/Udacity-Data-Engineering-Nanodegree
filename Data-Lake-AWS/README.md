# Spark and Data Lake
In this project, logs and songs data will undergo the ELT process for the usage of Sparkify.

## Structure
The files located in this repository are listed below:
- etl.py: Python script that will execute the ELT pipelines.
- dl.cfg: Configuration file that contains relevant AWS account information.

## Database Schema
The final database schema used for Sparkify's analytical purposes will follow a star schema design, as it is denormalised and hence, optimised for analytical queries. 

![Database Schema](https://github.com/Gianatmaja/Udacity-Data-Engineering-Nanodegree/blob/main/Data-Lake-AWS/Screenshot%202022-03-05%20at%203.27.01%20PM.png)

## ELT Process
The ELT process is done by spark and all the codes can be found on the etl.py file.

There are 2 main functions, namely:
1. `process_song_data`: Load raw data from S3 buckets to Spark stonealone server and process song dataset to insert record into songs and artists dimension table.
2. 1process_log_data`: Load raw data from S3 buckets to Spark stonealone server and Process event(log) dataset to insert record into time and users dimensio table and songplays fact table
