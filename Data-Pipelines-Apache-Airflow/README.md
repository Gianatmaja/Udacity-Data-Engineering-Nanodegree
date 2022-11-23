# Project 5: Data Pipelines on Apache Airflow
In this project, we'll build data pipelines using Apache Airflow to automate the data warehouse ETL process. For the ETL process, the source data resides in S3, and is transferred into a data warehouse hosted on Amazon Redshift.

### Project Structure
The main structure of this repository is listed below.

    .
    ├── dags                            
    │  ├── udac_example_dag.py    # Main DAG for this ETL data pipeline
    ├── plugins                
    │  ├── _helpers/              # Helper functions
    │  ├── operators/             # Airflow operators
    └── README.md

### Airflow DAG Pipeline
Below is the Airflow DAG pipeline used in this project
![Dag](https://github.com/Gianatmaja/Udacity-Data-Engineering-Nanodegree/blob/main/images/Dag.png)

1. `Begin_execution` & `End_execution`: Dummy operators at data pipeline end points.
2. `Stage_events` & `Stage_songs`: Extract/Transform data from S3 to Redshift to create staging tables.
3. `Load_songplays_fact_table` & `Load_*_dim_table`: Load data from staging tables to dimensional tables.
4. `run_data_quality_checks`: Check data quality.

### Database Schema
We'll be using a star schema for our data, with the following data model.
![Schema](https://github.com/Gianatmaja/Udacity-Data-Engineering-Nanodegree/blob/main/images/Datamodel.png)
