# Project 2: Data Modelling with Apache Cassandra
This project is part of the Udacity Data Engineering Nanodegree program.

### Background
A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analysis team is particularly interested in understanding what songs users are listening to. Currently, there is no easy way to query the data to generate the results, since the data reside in a directory of CSV files on user activity on the app.

### Objective
In this project, the objective is to create a Apache Cassandra database with tables to perform queries on song play analysis. To achieve this, we will perform ETL on local csv files and transfer them to Apache Cassandra tables, with data models according to the queries required.

### Scope of Project
Below is an outline of the tasks performed in this project.

#### Data Modelling for the NoSQL Database
1. Design tables according to the queries.
2. Write Apache Cassandra `CREATE KEYSPACE` and `SET KEYSPACE` statements.
3. Develop `CREATE` statement for each of the tables to address each question
4. Load the data with `INSERT` statement for each of the tables.
5. Include `IF NOT EXISTS` clauses in the `CREATE` statements to create tables only if the tables do not already exist.
6. Test by running the proper select statements with the correct `WHERE` clause.

#### ETL Pipeline Build
1. Implement the logic in the Jupyter notebook to iterate through each event file in event_data to process and create a new CSV file in Python.
2. Make necessary edits to include Apache Cassandra `CREATE` and `INSERT` statements to load processed records into relevant tables in your data model.
3. Test by running `SELECT` statements after running the queries on the database. 
