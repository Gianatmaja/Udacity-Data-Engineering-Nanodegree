# Project 1: Data Modelling with Postgres
This project is part of the Udacity Data Engineering Nanodegree program.

### Background
A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

### Objective
In this project, the objective is to create a Postgres database with tables designed to optimize queries on song play analysis. To achieve this, we will define fact and dimension tables for a star schema, and write an ETL pipeline that transfers data from JSON files in two local directories into these tables in Postgres using Python and SQL.

### Contents
Below is a description of the files contained in this repository:
- create_tables.py: Running this Python script will create blank tables in the database.
- etl.ipynb: This Jupyter Notebook will illustrate the ETL process by performing it a subset of the data.
- etl.py: Running this Python script will perform the ETL process on the whole dataset.
- sql_queries.py: This Python script contains the SQL commands used to create, fill, and drop the tables in the database.
- test.ipynb: This Jupyter Notebook contains several SQL queries to test whether the tables have been correctly created and inputted.
- Data (Folder): This folder contains songs and logs data in JSON format.

Notes:
- To read the JSON files, use `pd.read_json()`. For example, `pd.read_json('data/song_data/A/A/A/TRAAAAW128F429D538.json', lines=True)`
- To run the Python scripts, open up a terminal and type in the command `python <filename.py>`. For example. `python  create_tables.py`.

### Data Model
Below is an ERD diagram of the PostgreSQL database designed for Sparkify.

![ERD Diagram of Sparkify Database](https://github.com/Gianatmaja/Udacity-Data-Engineering-Nanodegree/blob/main/Data-Modelling-with-Postgres/DataModel.png)

As observed in the diagram, we used a star schema with 1 fact tables, songplays, and 4 dimension tables, namely songs, users, artists and time. In the diagram, the PK of each table is formatted with bold, while FKs are underlined.

### ETL Pipeline
Below is an overview of the ETL pipeline implemented.

#### Extract
First, the list of all JSON filenames containing the logs and songs data are collected. Then, the data from each of those files are extracted using the `pd.read_json()` command.

#### Transform
Next, columns are grouped based on which tables they'll go into. Further, time related information are also extracted and preprocessed.

#### Load
Finally, data is inserted to their respective Postgres table using the `INSERT INTO` queries.
