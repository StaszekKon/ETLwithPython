"""
Python Extract Transform Load Example ETL
"""
from etl import *

if __name__ == '__main__':
    extracted_data = extract()
    df = transform(extracted_data)
    load(df)
