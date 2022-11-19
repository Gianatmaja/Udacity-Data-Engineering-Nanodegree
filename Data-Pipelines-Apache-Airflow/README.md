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
![Dag](https://github.com/Gianatmaja/Udacity-Data-Engineering-Nanodegree/blob/main/Data-Pipelines-Apache-Airflow/images/Screenshot%202022-11-19%20at%203.26.54%20PM.png)

### Database Schema
We'll be using a star schema for our data, with the following data model.
![Schema](https://github.com/Gianatmaja/Udacity-Data-Engineering-Nanodegree/blob/main/Data-Pipelines-Apache-Airflow/images/Screenshot%202022-03-05%20at%203.27.01%20PM%203.17.51%20PM.png)
