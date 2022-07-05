## Data Lake

A data lake is a storage repository that holds a vast amount of raw data in its native format until it is needed for analytics applications. While a traditional data warehouse stores data in hierarchical dimensions and tables, a data lake uses a flat architecture to store data, primarily in files or object storage. 

It follow ELT process: Extract Load Transform

Data lake (Presentation)[https://docs.google.com/presentation/d/1RkH-YhBz2apIjYZAxUz2Uks4Pt51-fVWVN9CcH9ckyY/edit#slide=id.g10c891aba4d_0_12]

## Workflow orchestration

Data orchestration is a process carried out by a piece of software that takes siloed data from multiple data storage locations, combines it, and makes it available to data analysis tools

We have:

- LUIGI
- Apache airflow
- Prefect

## Airflow 