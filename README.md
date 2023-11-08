# ETL pipeline with Python
## EUR currency rate quotes in JSON format
+ Data is downloaded via API https://api.nbp.pl from NBP.
+ Then the EUR exchange rate is transformed.
+ The transformed data are loaded into the sqlite database.

Loaded data into sqlite database (by using client Sqliteman)

![image](https://github.com/StaszekKon/ETLwithPython/assets/47722600/c9e0bd6b-f97d-4e9a-ad46-295e921fe4bf)


+ Tests of  methods - functions were performed using the pytest tool (command in terminal **pytest -v** or  **python -m pytest**).

   **PyCharm environment**
  
![image](https://github.com/StaszekKon/ETLwithPython/assets/47722600/ca353302-fe04-4bc0-a980-27c6f729e612)



## Tools used:
+ Python: 3.11.2
+ Pytest: 7.4.3
+ SQLite Version: 3.39.4
