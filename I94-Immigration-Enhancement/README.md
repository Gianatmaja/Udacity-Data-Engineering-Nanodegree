# Project 6: Enhancing the I94 Immigration Data with External Data Sources

### Project Overview
This project will build up a data warehouse as a [single-source-of-truth](https://en.wikipedia.org/wiki/Single_source_of_truth) database by integrating data from different data sources.

### Scope of the Project

This project will integrate I94 immigration data, world temperature data and US demographic data to setup a data warehouse with fact and dimension tables.

| Data Set | Format | Description |
| ---      | ---    | ---         |
|[I94 Immigration Data](https://travel.trade.gov/research/reports/i94/historical/2016.html)| SAS | Contains international arrival statistics by world regions and countries, type of visa, mode of transportation, age groups, states visited, and the top ports of entry (for select countries).|
|[World Temperature Data](https://www.kaggle.com/berkeleyearth/climate-change-earth-surface-temperature-data)| CSV | Contains monthly temperature averages of different countries.|
|[US City Demographic Data](https://public.opendatasoft.com/explore/dataset/us-cities-demographics/export/)| CSV | Contains information about the demographics of US cities and census-designated places with a population greater or equal to 65,000.|

### Data Model
We propose a star schema data model to support OLAP and BI activities. Our proposed data model can be viewed below.
![schema](https://github.com/Gianatmaja/Udacity-Data-Engineering-Nanodegree/blob/main/I94-Immigration-Enhancement/images/Picture1.png)

### Data Dictionary
Here's a snapshot of the data dictionary. The complete file is available [here](https://github.com/Gianatmaja/Udacity-Data-Engineering-Nanodegree/blob/main/I94-Immigration-Enhancement/Data%20Dictionary.xlsx).
![dict](https://github.com/Gianatmaja/Udacity-Data-Engineering-Nanodegree/blob/main/I94-Immigration-Enhancement/images/dict.png)

### Future Scenarios
1. The data was increased by 100x.
    If Spark with standalone server mode can not process 100x the current data set, we could consider to store the data in [AWS EMR](https://aws.amazon.com/emr/).


2. The data populates a dashboard that must be updated on a daily basis by 7am every day.
    [Apache Airflow](https://airflow.apache.org) could be used to automate an ETL data pipeline to regularly update the data.


3. The database needed to be accessed by 100+ people.
    [AWS Redshift](https://aws.amazon.com/tw/redshift/?nc2=h_ql_prod_db_rs&whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc) can handle up to 500 connections, and might be the suitable storage if the database needs to be accessed by a lot of users.

