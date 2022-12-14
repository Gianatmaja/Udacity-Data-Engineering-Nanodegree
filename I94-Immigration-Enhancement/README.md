# Project 6: Enhancing the I94 Immigration Data with External Data Sources

### Project Overview
This project will build up a data warehouse as a [single-source-of-truth](https://en.wikipedia.org/wiki/Single_source_of_truth) database by integrating data from different data sources. This project will provide the foundation for future analysis regarding possible relationships between a country's immigration and arrival statistics, and its temperature and population demographics.

The structure of this repository can be viewed below.

    .
    ├── data/                       # Folder containing some of the data, samples, and labels used
    ├── images/                     # Contains images for project documentation
    ├── Capstone_Project.ipynb      # Main project notebook
    ├── etl.py                      # ETL script to load data
    ├── quality_checks.py           # Testing scripts to check whether ETL has been done correctly
    ├── capstone.cfg                # Config file
    ├── Data Dictionary.xlsx        # Complete data dictionary
    └── README.md


### Scope of the Project

This project will integrate I94 immigration data, world temperature data and US demographic data to setup a data warehouse with fact and dimension tables.

| Data Set | Format | Description |
| ---      | ---    | ---         |
|[I94 Immigration Data](https://travel.trade.gov/research/reports/i94/historical/2016.html)| SAS | Contains international arrival statistics by world regions and countries, type of visa, mode of transportation, age groups, states visited, and the top ports of entry (for select countries).|
|[World Temperature Data](https://www.kaggle.com/berkeleyearth/climate-change-earth-surface-temperature-data)| CSV | Contains monthly temperature averages of different countries.|
|[US City Demographic Data](https://public.opendatasoft.com/explore/dataset/us-cities-demographics/export/)| CSV | Contains information about the demographics of US cities and census-designated places with a population greater or equal to 65,000.|

### Data Model
We propose a star schema data model to support OLAP and BI activities. This data model will support future analysis regarding the potential relationships of arrival statistics and a country's temperature as well as its population demographics.

Our proposed data model can be viewed below.
![schema](https://github.com/Gianatmaja/Udacity-Data-Engineering-Nanodegree/blob/main/I94-Immigration-Enhancement/images/DataModel.png)

### Running the ETL Pipelines
The Python script `etl.py` can be used to insert the data into the destination tables according to the above data model.

### Performing Data Quality Checks
The Python script `quality_checks.py` can be used to perform data quality checks after running the ETL pipeline. More specifically, there are 2 checks that will be performed. The first will be to check whether the destination tables match the desired schema. The second would be to confirm that the tables are filled with data.


### Data Dictionary
Here's a snapshot of the data dictionary. The complete file is also available [here](https://github.com/Gianatmaja/Udacity-Data-Engineering-Nanodegree/blob/main/I94-Immigration-Enhancement/Data%20Dictionary.xlsx).
![dict](https://github.com/Gianatmaja/Udacity-Data-Engineering-Nanodegree/blob/main/I94-Immigration-Enhancement/images/Datadictionary.png)


### Future Scenarios
1. The data was increased by 100x:
    If Spark (with standalone server) cannot process 100 times the current data set, we could consider to store the data in [AWS EMR](https://aws.amazon.com/emr/).


2. The data populates a dashboard that must be updated on a daily basis by 7am every day:
    [Apache Airflow](https://airflow.apache.org) could be used to automate an ETL data pipeline to regularly update the data.


3. The database needed to be accessed by 100+ people:
    [AWS Redshift](https://aws.amazon.com/tw/redshift/?nc2=h_ql_prod_db_rs&whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc) can handle up to 500 connections, and might be the suitable storage if the database needs to be accessed by a lot of users.

