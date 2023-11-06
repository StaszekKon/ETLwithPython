# ETL pipeline with Python
## EUR currency rate quotes in JSON format
+ Data is downloaded via API https://api.nbp.pl from NBP.
+ Then the EUR exchange rate is transformed.
+ The transformed data are loaded into the sqlite database.
+ Tests of  methods - functions were performed using the pytest tool (command in terminal pytest -v or  python -m pytest).


## Tools used:
+ Python: 3.11.2
+ Pytest: 7.4.3
+ SQLite Version: 3.39.4
