# Spark and Data Lake
In this project, logs and songs data will undergo the ELT process for the usage of Sparkify.

## Structure
The files located in this repository are listed below:
- etl.py: Python script that will execute the ELT pipelines.
- dl.cfg: Configuration file that contains relevant AWS account information.

## Database Schema
The final database schema used for Sparkify's analytical purposes will follow a star schema design, as it is denormalised and hence, optimised for analytical queries. 

![Database Schema](Screenshot 2022-03-05 at 3.27.01 PM.png)

## ELT Process
The ELT process is done by spark and all the codes can be found on the etl.py file.
